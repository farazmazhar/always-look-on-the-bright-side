"""
Django REST Framework demo — JSON APIs on top of Django.

Run with:  .venv/bin/python 19-django-rest-framework/demo.py

Django gives you the request/response cycle, the ORM, auth, and the admin.
DRF adds the API layer: serializers (the pydantic equivalent — declare a
schema, validate input, shape output), Request/Response objects that speak
JSON natively, and ViewSets that generate a whole CRUD API from a model.

Like the Django demo, this runs without a server: DRF ships an API test
client (APIClient) that exercises the full request pipeline in-process,
against a throwaway in-memory SQLite database.
"""

import os
import sys
from typing import cast

# Make this folder importable so `import demo_app` works no matter where the
# script is run from (repo root or inside the folder).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import django
from django.conf import settings

# ---------------------------------------------------------------------------
# 0. Minimal settings — rest_framework is an app like any other.
# ---------------------------------------------------------------------------
settings.configure(
    DEBUG=True,
    SECRET_KEY="demo",  # normally a random secret — demo only
    ALLOWED_HOSTS=["testserver"],  # the test client's virtual host
    ROOT_URLCONF="demo_app.urls",
    INSTALLED_APPS=[
        "django.contrib.contenttypes",
        "django.contrib.auth",
        "rest_framework",  # <-- DRF is just an installed Django app
        "demo_app",
    ],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",  # throwaway database, gone when the process ends
        }
    },
    DEFAULT_AUTO_FIELD="django.db.models.AutoField",
)

django.setup()

import logging

logging.getLogger("django.request").setLevel(logging.CRITICAL)  # quiet 404 logs

from django.core.management import call_command  # noqa: E402

call_command("migrate", verbosity=0)  # create tables in the :memory: database

from demo_app.models import Book  # noqa: E402

def show(title: str) -> None:
    print(f"\n{title}")


# ---------------------------------------------------------------------------
# 1. Serializer alone — validation without any HTTP. pydantic-style:
#    declare the schema, feed it data, read .is_valid() / .errors / .data.
# ---------------------------------------------------------------------------
show("1. Serializer: validate + shape data (no HTTP yet)")
from demo_app.serializers import BookSerializer  # noqa: E402

payload = {"title": "Dune", "author": "Frank Herbert", "year": 1965, "rating": 8.5}
ser = BookSerializer(data=payload)
print("   is_valid():", ser.is_valid())
print("   .data:     ", ser.data)  # validated, normalized dict
print("   .errors:   ", ser.errors)

bad = BookSerializer(data={"title": "   ", "author": "X", "year": 1800, "rating": 99})
print("   bad is_valid():", bad.is_valid())
print("   bad .errors:   ", bad.errors)


# ---------------------------------------------------------------------------
# 2. APIClient — DRF's version of Django's test Client. JSON in, JSON out.
# ---------------------------------------------------------------------------
from rest_framework.test import APIClient  # noqa: E402

client = APIClient()

show("2. Function-based API views (@api_view)")
# DRF renders the request to JSON for us — no manual json.dumps/loads.
resp = client.post(
    "/books/",
    {"title": "Dune", "author": "Frank Herbert", "year": 1965, "rating": 8.5},
    format="json",
)
print("   POST /books/      ->", resp.status_code, resp.json())

resp = client.post(
    "/books/",
    {"title": "", "author": "Nobody", "year": 1965, "rating": 8.5},
    format="json",
)
print("   POST bad /books/  ->", resp.status_code, resp.json())

resp = client.get("/books/")
print("   GET /books/       ->", resp.status_code, resp.json())


# ---------------------------------------------------------------------------
# 3. ModelSerializer — fields, create() and update() come from the model.
# ---------------------------------------------------------------------------
show("3. ModelSerializer (fields + create/update from the model)")
from demo_app.serializers import BookModelSerializer  # noqa: E402

mser = BookModelSerializer(data={"title": "1984", "author": "Orwell", "year": 1949, "rating": 9.0})
print("   is_valid():", mser.is_valid())
if mser.is_valid():
    # save() returns a Book, but DRF's untyped Serializer.save() is
    # inferred as list[Unknown] by Pylance — cast to the real type.
    book: Book = cast(Book, mser.save())  # model instance created by the serializer
    print("   saved:", book, "| id:", book.pk)  # .pk is the model's primary key
    print("   Book model rows:", Book.objects.count())  # the serializer wrote to the ORM
print("   .data:", BookModelSerializer(book).data)


# ---------------------------------------------------------------------------
# 4. APIView — class-based API views, one method per HTTP verb.
# ---------------------------------------------------------------------------
show("4. Class-based APIView")
resp = client.get("/api/books/")
print("   GET  /api/books/  ->", resp.status_code, resp.json())
resp = client.post(
    "/api/books/",
    {"title": "Brave New World", "author": "Huxley", "year": 1932, "rating": 7.8},
    format="json",
)
print("   POST /api/books/  ->", resp.status_code, resp.json())


# ---------------------------------------------------------------------------
# 5. ViewSet + router — the whole CRUD API, declared not implemented.
# ---------------------------------------------------------------------------
show("5. ModelViewSet + router (full CRUD from a model)")
resp = client.get("/api/books/")
print("   GET    /api/books/       ->", resp.status_code, "count =", len(resp.json()))

new_id = resp.json()[0]["id"]
resp = client.get(f"/api/books/{new_id}/")
print(f"   GET    /api/books/{new_id}/ ->", resp.status_code, resp.json())

resp = client.patch(
    f"/api/books/{new_id}/", {"rating": 9.5}, format="json"
)  # PATCH = partial update
print(f"   PATCH  /api/books/{new_id}/ ->", resp.status_code, resp.json())

resp = client.delete(f"/api/books/{new_id}/")
print(f"   DELETE /api/books/{new_id}/ ->", resp.status_code)

resp = client.get(f"/api/books/{new_id}/")
print(f"   GET    /api/books/{new_id}/ ->", resp.status_code, resp.json())  # 404 now


# ---------------------------------------------------------------------------
# 6. Browsable API — DRF also renders a human UI at /api/ so you can poke
#    at endpoints in a browser. The router registers it for free.
# ---------------------------------------------------------------------------
show("6. Browsable API")
resp = client.get("/api/")
print("   GET /api/  ->", resp.status_code, "(browsable API root)")
from demo_app.urls import router  # noqa: E402

print("   router routes:", [str(r.pattern) for r in router.urls])

print("\nDone — serializers, APIClient, APIView, ViewSet and the router.")
