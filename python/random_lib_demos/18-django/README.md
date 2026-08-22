# 18-django

Django is the "batteries included" Python web framework: URL routing, an
ORM, templates, forms, an admin UI, auth, sessions, middleware — all built
in. This demo walks through the pieces that matter, in code, without
scaffolding a whole project.

## Why Django?

- **Everything in one place** — no glue code between a router, an ORM, and
  a template engine; they are designed to work together.
- **The ORM** — write Python classes, get SQL tables. Queries are `filter()`
  calls, not strings.
- **Forms** — declarative, schema-style validation of user input (the same
  mental model as pydantic, but for HTML forms).
- **Free admin + auth** — register your models and get a CRUD UI; users,
  sessions and password hashing come built in.
- **Mature** — 20 years old, huge ecosystem, the default choice for many
  Python web apps.

## Install

```bash
source .venv/bin/activate
pip install django
```

## Run

```bash
.venv/bin/python 18-django/demo.py
```

The demo configures Django in code and drives it through Django's test
`Client`, so it needs no running server and no database file (SQLite is
held in memory).

## What the demo shows

1. **URL routing → view → response** — how a path becomes HTML.
2. **The ORM** — create, filter, and query rows without writing SQL.
3. **Views + ORM together** — rendering database rows into HTML.
4. **Forms** — validating user input and reading `cleaned_data`.
5. **Admin** — registering a model for Django's built-in CRUD UI.
6. **Auth** — users and password hashing out of the box.
7. **Class-based views** — a full list view in a few lines.

## Use cases

- Full-stack web apps (server-rendered HTML) with minimal dependencies.
- Content-heavy sites, dashboards, and internal tools where the admin and
  auth save weeks.
- Any app that wants one coherent stack instead of assembled parts.

## References

- Docs: <https://docs.djangoproject.com/>
- Tutorial: <https://docs.djangoproject.com/en/stable/intro/tutorial01/>
- DRF (the API layer built on Django): <https://www.django-rest-framework.org/>
- Django Ninja (pydantic-based APIs on Django): <https://django-ninja.dev/>

## Capabilities you can build

- A blog or CMS using models, the admin, and template views.
- A form-driven app (signups, surveys) using `forms.Form` + validation.
- A user-facing site with login, permissions, and sessions from Django auth.
- An API — either with DRF (see demo 19) or Django Ninja.
