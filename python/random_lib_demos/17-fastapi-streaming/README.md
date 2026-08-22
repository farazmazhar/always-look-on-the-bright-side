# fastapi-streaming — SSE token streaming for LLM chat APIs

Demo for the note [fastapi-llm-streaming.md](../../../work/notes/notes/fastapi-llm-streaming.md):
a FastAPI server that streams LLM tokens to the client as SSE events, exactly
like ChatGPT's word-by-word output. No agent logic, no tool calling — just
"user sends a prompt, server sends back tokens as they are produced."

```
Client ──POST /v1/chat──▶ FastAPI ──HTTP request (stream=True)──▶ LLM API
Client ◀──SSE events── FastAPI ◀───────token stream─────────────── LLM API
        (data: {"token": "Hello"}\n\n)
        (data: {"token": ", I"}\n\n)
        ...
```

## What's in the box

| File | What it shows |
|---|---|
| `server.py` | The whole server: simulated LLM + real LLM endpoints, SSE formatting, disconnect handling, keepalives, buffering headers, CORS |
| `static/index.html` | Browser client using `fetch` + `ReadableStream` — the note's gotcha: `EventSource` can't do POST, so we parse SSE ourselves |
| `client.py` | Same SSE parsing in Python, plus a `--stop-after` flag to watch the server stop on client disconnect |

## Install / run

Packages: `fastapi`, `uvicorn`, `httpx` (already in this repo's `.venv`).

```bash
source .venv/bin/activate            # or use .venv/bin/uvicorn directly
uvicorn 17-fastapi-streaming.server:app --reload --port 8000
```

Then, in another terminal:

```bash
# 1. Raw SSE over curl (-N disables curl's buffering so tokens appear live)
curl -N -X POST "http://localhost:8000/v1/chat" -H "Content-Type: application/json" \
     -d '{"prompt":"hi"}'

# 2. Browser UI at http://localhost:8000/ — type a prompt, watch tokens stream in

# 3. Python CLI client
.venv/bin/python 17-fastapi-streaming/client.py

# 4. Disconnect handling: the server stops mid-generation when the client leaves
.venv/bin/python 17-fastapi-streaming/client.py --stop-after 3
```

### Using a real LLM

The server falls back to a built-in simulator when no key is set, so the demo
runs with zero setup. To hit a real OpenAI-compatible API instead:

```bash
export OPENAI_API_KEY="sk-..."
export OPENAI_MODEL="gpt-4o-mini"      # optional, default
export OPENAI_BASE_URL="https://api.openai.com/v1"   # optional, default
uvicorn 17-fastapi-streaming.server:app --reload --port 8000
```

(If you use a proxy like Ollama, point `OPENAI_BASE_URL` at its OpenAI-compatible
endpoint — e.g. `http://localhost:11434/v1`.)

## The two moving pieces (from the note)

1. **Outbound**: call the LLM with `stream=True` and read its response
   incrementally — `httpx`'s `client.stream(...)` + `aiter_lines()`.
2. **Inbound**: hand FastAPI an async generator that yields SSE-formatted
   chunks via `StreamingResponse`.

`StreamingResponse(async_generator)` = "write these bytes to the socket as the
generator produces them". Everything else is plumbing: parse the upstream LLM
stream, reformat as SSE, split lines on the client.

## SSE wire format

Each event is `key: value` lines terminated by a **blank line** (mandatory —
forgetting it merges events):

```
data: {"token": "Hello"}

event: done
data: {}

```

## Gotchas the demo implements

- **Buffering**: `curl -N`, `Cache-Control: no-cache`, `X-Accel-Buffering: no`,
  `media_type="text/event-stream"` — middleboxes that buffer turn your stream
  into one delayed blob.
- **Chunk boundaries**: TCP/HTTP chunks don't respect SSE event boundaries —
  the client always buffers and splits on `\n`, holding back a partial last line.
- **`EventSource` can't POST**: the browser client uses `fetch` + `ReadableStream`;
  a GET variant of the endpoint (`/v1/chat/events`) exists for `EventSource` demos.
- **Disconnects**: `request.is_disconnected()` stops the generator (and the LLM
  call) the moment the client is gone — you're paying per token.
- **Keepalives**: `: keepalive` comment lines keep proxies from timing out an
  idle connection; clients ignore them.
- **Timeouts**: the httpx client uses `timeout=None` — the default 5s cuts long
  generations.
- **CORS**: enabled for cross-origin frontends.

## When to use SSE vs WebSockets

SSE if you only push generated text to the client (one-way, plain HTTP, low
complexity). Reach for WebSockets when the client needs to *talk back mid-stream*
(e.g. "stop generating") or the server emits many event types with round trips —
a real agent loop.
