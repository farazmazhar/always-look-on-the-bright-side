# random_lib_demos — AGENTS.md

Python library demo collection. One self-contained folder per library so
demos never overlap or get tangled together.

## Environment

- A single virtualenv lives in this folder at `.venv/` (Python 3.14).
- All libraries are installed into `.venv` with pip.
- Activate it before running any demo:

  ```bash
  source .venv/bin/activate   # Linux/macOS
  .venv\Scripts\activate      # Windows
  ```

- Run a demo from this folder (or anywhere) with:

  ```bash
  .venv/bin/python 01-pydantic/demo.py
  ```

## Layout

Each library gets its own **numbered** folder:

```
01-pydantic/
02-pydantic-settings/
03-dacite/
04-autoregistry/
05-python-statemachine/
06-dishka/
07-schedium/
08-whenever/
09-pint/
10-geopy/
11-nicegui/
12-faker/
13-zensical/
14-complexipy/
15-heapq/
16-graphlib/
17-fastapi-streaming/
18-django/
19-django-rest-framework/
```

Inside every folder you will find:

- `README.md` — what the library is, why you'd use it, its features,
  use cases, references, and the kinds of things you can build with it.
- `demo.py` (or `demo_*.py`) — a runnable, heavily-commented demo script
  that walks through the library's core ideas.

## Libraries covered

1. `pydantic` — data validation & serialization via type hints
2. `pydantic-settings` — config/settings management built on pydantic
3. `dacite` — create dataclasses from plain dicts
4. `autoregistry` — automatic registry design pattern (string → code)
5. `python-statemachine` — finite state machines
6. `dishka` — dependency injection / IoC container with scopes
7. `schedium` — lightweight in-process job scheduler
8. `whenever` — typed, DST-safe datetime library
9. `pint` — physical units & unit conversion
10. `geopy` — geocoding & geodesic distance
11. `nicegui` — build web UIs with pure Python
12. `faker` — generate realistic fake data
13. `zensical` — static site generator from the Material for MkDocs team
14. `complexipy` — cognitive complexity analysis for Python code
15. `heapq` — heap queue / priority queue (standard library)
16. `graphlib` — topological sorting of directed graphs (standard library)
17. `fastapi-streaming` — SSE streaming for LLM chat APIs with FastAPI
18. `django` — the batteries-included web framework (ORM, forms, admin, auth)
19. `django-rest-framework` — JSON APIs on Django (serializers, ViewSets, routers)

## Conventions

- One folder per library; do not mix demos between folders.
- Folder names are zero-padded two-digit numbers followed by the library name.
- Demos must be runnable as `python demo.py` (no arguments, no external data).
- Keep comments beginner-friendly and explain *why*, not just *what*.
- Each README is standalone: intro, install, features, use cases, references,
  and example-capabilities.
- If a library is updated, pin/verify against its docs; demos target the
  version installed in `.venv`.

## Adding a new library demo

1. Pick the next number (15, 16, ...).
2. `mkdir NN-library-name`
3. Write `README.md` and `demo.py`.
4. `source .venv/bin/activate && pip install <library>`
5. Run the demo to confirm it works, then list it in the table above.
