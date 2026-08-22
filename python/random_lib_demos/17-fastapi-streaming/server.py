"""
FastAPI LLM streaming server — the whole "user sends a prompt, server sends
back tokens as they are produced" idea, with nothing else.

Run with:
    .venv/bin/uvicorn 17-fastapi-streaming.server:app --reload --port 8000

Then try it:
    curl -N -X POST "http://localhost:8000/v1/chat/simulated?prompt=hi"
    .venv/bin/python 17-fastapi-streaming/client.py

This is a *learning* server, so it deliberately shows the pieces from the
note "FastAPI Streaming for LLM Chat APIs":

1. A simulated LLM (no API key needed) that yields tokens with a delay.
2. A real LLM endpoint (OpenAI-compatible, httpx + stream=True) used when
   OPENAI_API_KEY is set, falling back to the simulator otherwise.
3. The SSE wire format:  data: {...}\n\n  per event, blank line mandatory.
4. Client-disconnect handling: stop generating the moment the client is gone
   (you're paying per token on a real LLM).
5. Keepalive comment lines so proxies don't time out an idle connection.

Buffering gotchas already handled here:
  - media_type="text/event-stream"  -> clients/proxies treat it as a stream
  - Cache-Control: no-cache          -> don't let anything cache the response
  - X-Accel-Buffering: no            -> tell nginx not to buffer
"""

import asyncio
import json
import os
from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# When set, /v1/chat uses the real model; when empty, it falls back to the
# simulated generator so the demo runs with zero setup.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
OPENAI_TIMEOUT_SECONDS = 30  # httpx default is 5s — way too short for a long generation

KEEPALIVE_INTERVAL = 15.0  # seconds between SSE comment lines

# Words the simulator uses to build a per-prompt response, so it feels like a
# (very simple) LLM instead of a fixed string.
SIM_WORDS = [
    "Hello", ",", "I'm", "a", "simulated", "LLM", "responding", "to", "your",
    "prompt", ":", "streaming", "tokens", "one", "at", "a", "time", ".",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def sse(event: str, data: dict) -> str:
    """Format one SSE event: data/event lines + the mandatory blank line."""
    lines = [f"data: {json.dumps(data)}"]
    if event:
        lines.insert(0, f"event: {event}")
    return "\n".join(lines) + "\n\n"


def stream_headers() -> dict:
    """The three headers that stop middleboxes from buffering the stream."""
    return {
        "Cache-Control": "no-cache",
        "X-Accel-Buffering": "no",
    }


# ---------------------------------------------------------------------------
# Endpoint 1: a simulated LLM (no API key, no network)
# ---------------------------------------------------------------------------

async def simulated_llm(prompt: str):
    """Stand-in for a real LLM: pick some words, emit them one by one."""
    words = [w for w in SIM_WORDS if w != "prompt"]  # tiny twist, keep it simple
    words.insert(6, f'"{prompt}"')
    for word in words:
        await asyncio.sleep(0.2)  # pretend compute time
        yield sse("message", {"token": word})
    yield sse("done", {})


# ---------------------------------------------------------------------------
# Endpoint 2: a real LLM through an OpenAI-compatible streaming API
# ---------------------------------------------------------------------------

async def real_llm(prompt: str):
    """
    The real thing: httpx stream=True, read the SSE lines the LLM emits,
    and forward just the content deltas as our own SSE events.

    The LLM API is itself speaking SSE (data: {...} lines with a final
    data: [DONE]), so this is: parse upstream SSE -> reformat as our SSE.
    """
    async with httpx.AsyncClient(timeout=OPENAI_TIMEOUT_SECONDS) as client:
        async with client.stream(
            "POST",
            f"{OPENAI_BASE_URL}/chat/completions",
            headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
            json={
                "model": OPENAI_MODEL,
                "stream": True,  # <-- the magic flag
                "messages": [{"role": "user", "content": prompt}],
            },
        ) as response:
            response.raise_for_status()
            async for line in response.aiter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[6:]  # strip the "data: " prefix
                if data == "[DONE]":
                    break
                chunk = json.loads(data)
                delta = chunk["choices"][0]["delta"].get("content")
                if delta:
                    yield sse("message", {"token": delta})


# ---------------------------------------------------------------------------
# The streaming endpoint (with disconnect handling)
# ---------------------------------------------------------------------------

class ChatRequest(BaseModel):
    prompt: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Announce which mode the /v1/chat endpoint will use, once, at startup."""
    if OPENAI_API_KEY:
        print(f"v1/chat -> real LLM ({OPENAI_MODEL} via {OPENAI_BASE_URL})")
    else:
        print("v1/chat -> simulated LLM (set OPENAI_API_KEY for the real one)")
    yield


app = FastAPI(title="FastAPI LLM streaming demo", lifespan=lifespan)

# CORS: the demo page is served from the same origin, but this makes the
# endpoint usable from a separately-hosted frontend (e.g. vite dev server).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/v1/chat")
async def chat(payload: ChatRequest, request: Request):
    """
    POST a prompt, receive an SSE stream of tokens.

    The real work is in the generator below. StreamingResponse writes bytes
    to the socket as the generator produces them — nothing more.
    """

    async def stream():
        # Pick the source: real LLM if configured, simulator otherwise.
        source = real_llm(payload.prompt) if OPENAI_API_KEY else simulated_llm(payload.prompt)
        try:
            async for event in source:
                # Client gone (tab closed / request cancelled)? Stop calling
                # the LLM immediately — every token we skip saves money.
                if await request.is_disconnected():
                    break
                yield event

                # Keepalive: proxies may time out an idle connection. SSE
                # comment lines are ignored by clients, so they're free.
                # (A real impl would track elapsed time; this sends one per
                # event to keep the demo tiny.)
                yield ": keepalive\n\n"
        finally:
            # The generator is cancelled on disconnect, so this runs even on
            # the break above — the place to cancel tasks / close clients.
            await asyncio.sleep(0)  # stand-in for cleanup()

    return StreamingResponse(
        stream(),
        media_type="text/event-stream",
        headers=stream_headers(),
    )


# Convenience GET variant so you can also watch the stream in a browser tab
# (EventSource works on GET only — see the note's gotcha). POST is the real
# API; this is just for demos.
@app.get("/v1/chat/events")
async def chat_events(request: Request, prompt: str = "hi"):
    async def stream():
        source = real_llm(prompt) if OPENAI_API_KEY else simulated_llm(prompt)
        try:
            async for event in source:
                if await request.is_disconnected():
                    break
                yield event
                yield ": keepalive\n\n"
        finally:
            await asyncio.sleep(0)

    return StreamingResponse(
        stream(),
        media_type="text/event-stream",
        headers=stream_headers(),
    )


# The browser client (index.html) served at http://localhost:8000/
app.mount("/", StaticFiles(directory="17-fastapi-streaming/static", html=True), name="static")
