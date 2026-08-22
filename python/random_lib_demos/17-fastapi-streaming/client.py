"""
Command-line SSE client for the FastAPI streaming demo.

Run with:
    .venv/bin/python 17-fastapi-streaming/client.py

This is the same code the browser page runs, in Python: POST a prompt,
read the HTTP body as a stream, split on newlines (chunks don't respect
SSE event boundaries), and print tokens as they arrive. Also shows a
"stop after N seconds" mode that demonstrates the server's disconnect
handling (the server stops generating when the client goes away).
"""

import argparse
import asyncio
import json

import httpx

URL = "http://localhost:8000/v1/chat"


async def stream_tokens(prompt: str, stop_after: float | None):
    async with httpx.AsyncClient(timeout=None) as client:  # no timeout: long generations
        async with client.stream("POST", URL, json={"prompt": prompt}) as response:
            response.raise_for_status()
            print(f"HTTP {response.status_code} — streaming tokens:\n")

            buffer = ""
            async for chunk in response.aiter_bytes():
                # simulate a user closing the tab mid-stream
                if stop_after and asyncio.get_event_loop().time() > stop_after:
                    print(f"\n[client] giving up after {stop_after}s — closing the connection")
                    break

                buffer += chunk.decode()
                lines = buffer.split("\n")
                buffer = lines.pop()  # keep partial line for the next chunk

                for line in lines:
                    if line.startswith("data: "):
                        payload = json.loads(line[6:])
                        if payload.get("token"):
                            print(payload["token"], end="", flush=True)

            if buffer.startswith("data: "):
                payload = json.loads(buffer[6:])
                if payload.get("token"):
                    print(payload["token"], end="", flush=True)

            print("\n[client] done")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prompt", default="tell me a haiku about streaming")
    parser.add_argument("--stop-after", type=float, default=None,
                        help="close the connection after N seconds (tests disconnect handling)")
    args = parser.parse_args()
    asyncio.run(stream_tokens(args.prompt, args.stop_after))
