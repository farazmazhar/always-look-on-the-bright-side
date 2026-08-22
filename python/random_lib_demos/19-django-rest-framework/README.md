# 19-django-rest-framework

Django REST Framework (DRF) is the standard toolkit for building JSON APIs
on top of Django. It layers serializers, Request/Response objects, and
ViewSets onto Django's request/response cycle so your endpoints speak JSON
natively. Pair with demo 18 — this is "Django, but for APIs."

## Why DRF?

- **Serializers** — the pydantic equivalent: declare a schema, validate
  input, shape output. `ModelSerializer` derives fields from a Django model.
- **Request/Response** — DRF's `Request` parses the JSON body; its
  `Response` renders to JSON. No manual `json.dumps`/`loads`.
- **ViewSets + routers** — a full CRUD API (list, create, retrieve, update,
  partial-update, delete) generated from a model in a few lines.
- **Browsable API** — every endpoint also renders as a human UI you can
  poke at in a browser.
- **Batteries included** — auth, permissions, throttling, pagination,
  filtering, and OpenAPI schema generation come with it.

## Install

```bash
source .venv/bin/activate
pip install django djangorestframework
```

## Run

```bash
.venv/bin/python 19-django-rest-framework/demo.py
```

The demo drives DRF through its `APIClient` (DRF's version of Django's
test client) with an in-memory SQLite database — no server, no DB file.

## What the demo shows

1. **Serializer alone** — validation and shaping with no HTTP at all
   (the pydantic comparison point).
2. **Function-based API views** — `@api_view` + `Request`/`Response`.
3. **ModelSerializer** — fields and `create()`/`update()` derived from the
   model.
4. **APIView** — class-based views, one method per HTTP verb.
5. **ModelViewSet + router** — the whole CRUD API declared, not written.
6. **Browsable API** — DRF's built-in human UI at the API root.

## Use cases

- JSON APIs for single-page apps or mobile clients.
- Replacing hand-rolled `JsonResponse` endpoints with validated schemas.
- CRUD backends where Django's models and admin already exist.
- Projects that want Django's ORM/auth/admin *and* a proper API layer.

## References

- Docs: <https://www.django-rest-framework.org/>
- Serializers: <https://www.django-rest-framework.org/api-guide/serializers/>
- ViewSets & routers: <https://www.django-rest-framework.org/api-guide/viewsets/>
- Django Ninja (pydantic-based alternative): <https://django-ninja.dev/>

## Capabilities you can build

- A book/product catalog API with full CRUD from one `ModelViewSet`.
- Token- or session-authenticated APIs for a frontend.
- Filterable, paginated, throttled endpoints with DRF's built-ins.
- An OpenAPI-documented backend that a JS/TS frontend can consume.
