"""
Django demo — the full web framework, minus the boilerplate.

Run with:  .venv/bin/python 18-django/demo.py

A real Django project is a folder with settings.py, urls.py, models.py,
views.py, migrations, an admin site, templates, ... created by `django-admin
startproject`. That is a lot of machinery, and *none of it* is what Django
is actually teaching us here.

So instead of scaffolding a project, this demo configures Django in code:
  - settings are plain Python variables (DATABASES, INSTALLED_APPS, ...)
  - models, views and URLs live in the demo_app/ package next to this file
  - the "browser" is Django's test Client: it runs the full request ->
    middleware -> URL resolver -> view -> template -> response pipeline
    in-process, with a throwaway SQLite database held in memory.

Django is about the *request/response cycle*: an HTTP request comes in, the
URL resolver matches it to a view, the view does work (usually with the ORM)
and returns an HttpResponse. Everything else is supporting cast.
"""

import os
import sys

# Make this folder importable so `import demo_app` works no matter where the
# script is run from (repo root or inside the folder).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import django
from django.conf import settings

# ---------------------------------------------------------------------------
# 0. Minimal settings — normally these live in a project's settings.py.
#    We configure the bare minimum before importing any model code.
# ---------------------------------------------------------------------------
settings.configure(
    DEBUG=True,
    ROOT_URLCONF="demo_app.urls",  # where the URL resolver looks for urlpatterns
    INSTALLED_APPS=[
        "django.contrib.contenttypes",  # needed by the ORM's auth-less models
        "django.contrib.auth",          # User model used in section 8
        "django.contrib.admin",         # the /admin/ CRUD UI in section 7
        "demo_app",                     # the app defined in this folder
    ],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",  # throwaway database, gone when the process ends
        }
    },
    DEFAULT_AUTO_FIELD="django.db.models.AutoField",
)

django.setup()  # make the ORM, apps, and settings importable everywhere

import logging

# Quiet Django's "Not Found: /url" stderr log for the intentional 404 demo.
logging.getLogger("django.request").setLevel(logging.CRITICAL)

from django.core.management import call_command  # noqa: E402

call_command("migrate", verbosity=0)  # create tables in the :memory: database

from demo_app.models import Article  # noqa: E402


def show(title: str) -> None:
    print(f"\n{title}")


# ---------------------------------------------------------------------------
# 1. The test Client — a fake browser with no network, no server process.
#    Every .get()/post() runs the entire Django request pipeline:
#    URL resolver -> view -> HttpResponse.
# ---------------------------------------------------------------------------
from django.test import Client  # noqa: E402

client = Client()

show("1. URL routing -> view -> response")
response = client.get("/")
print("   status:", response.status_code)  # 200
print("   body:  ", response.content.decode())


# ---------------------------------------------------------------------------
# 2. The ORM — create, query, update, delete. No SQL written by hand.
# ---------------------------------------------------------------------------
show("2. The ORM (object-relational mapper)")
Article.objects.create(title="Hello ORM", body="Created without SQL.", published=True)
Article.objects.create(title="Second post", body="Another row.", published=False)

print("   all:", list(Article.objects.all()))
print("   published only:", list(Article.objects.filter(published=True)))
print("   first by title: ", Article.objects.get(title="Hello ORM"))


# ---------------------------------------------------------------------------
# 3. Views + ORM together: hit the URL, get back the rendered HTML.
# ---------------------------------------------------------------------------
show("3. Views render ORM data into HTML")
for url in ("/articles/", "/articles/1/", "/articles/999/"):
    resp = client.get(url)
    print(f"   GET {url:20} -> {resp.status_code}  {resp.content.decode()[:45]}")


# ---------------------------------------------------------------------------
# 4. Forms — Django's built-in way to validate user input.
#    Same shape as pydantic: declare fields, validate, read cleaned_data.
# ---------------------------------------------------------------------------
from django import forms  # noqa: E402


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(min_length=10)


show("4. Forms: validate user input like a schema")
valid = ContactForm({"name": "Carol", "email": "carol@example.com", "message": "Hello there!"})
print("   valid form is_valid():", valid.is_valid())
print("   cleaned_data:         ", valid.cleaned_data)

invalid = ContactForm({"name": "", "email": "not-an-email", "message": "short"})
print("   invalid form is_valid():", invalid.is_valid())
print("   errors:               ", dict(invalid.errors))


# ---------------------------------------------------------------------------
# 5. Admin — Django's free CRUD UI. In a real project you register models
#    and get a /admin/ page with login, list, edit and delete for free.
#    (We can't click through it here, but this is all it takes to enable it.)
# ---------------------------------------------------------------------------
from django.contrib import admin  # noqa: E402

admin.site.register(Article)

show("5. Admin")
print("   admin.site registered:", [m.__name__ for m in admin.site._registry])


# ---------------------------------------------------------------------------
# 6. The auth system — users, login, permissions come with Django.
# ---------------------------------------------------------------------------
from django.contrib.auth.models import User  # noqa: E402

show("6. Built-in auth")
u = User.objects.create_user(username="carol", password="secret123")
print("   created user:", u.username, "| is_staff:", u.is_staff)
print("   password is hashed, not stored:", u.password.startswith("pbkdf2"))


# ---------------------------------------------------------------------------
# 7. Class-based views (CBVs) — built-in generic views that replace whole
#    patterns with one line. The template isn't rendered here (no template
#    files in a one-file demo), but the query set is assembled for you.
# ---------------------------------------------------------------------------
from django.views.generic import ListView  # noqa: E402


class ArticleListView(ListView):
    """A CBV: ORM query + pagination + template lookup — all built in."""

    model = Article


show("7. Class-based views")
print("   ArticleListView defined with 2 lines (model only)")
print("   queryset:", list(ArticleListView().get_queryset()))

print("\nDone — Django's request/response cycle, ORM, forms, admin and auth.")
