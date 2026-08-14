# dishka

**dishka** is a dependency injection (DI) / IoC container for Python. It
focuses on *one* job — wiring dependencies together — and does it with scopes
so objects live exactly as long as they should.

"dishka" means "cute DI" in Russian.

## Why use it?

- Stop threading objects through `__init__` calls by hand ("wiring").
- Centralize *how* objects are created in `Provider`s instead of scattering
  factories and singletons across the codebase.
- Scopes give you control over object lifetimes: `APP` (one per application)
  vs `REQUEST` (one per request/event/unit of work).
- Finalization: resources created with a `yield` factory are cleaned up when
  their scope ends.

## Key features

- `Provider` + `.provide(...)` to register factories.
- Bind an interface to an implementation: `.provide(SQLiteUserDAO, provides=UserDAO)`.
- `Scope.APP`, `Scope.REQUEST`, `Scope.SESSION` and custom scopes.
- `@provide`-decorated generator factories with teardown (`yield`).
- `make_container` / `make_async_container` (sync and async).
- Context-manager sub-containers: `with container() as request_scope: ...`.
- Framework integrations (FastAPI, Aiogram, Flask, etc.).

## Install

```bash
pip install dishka
```

## Use cases

- Wiring services, repositories, and clients in web apps (FastAPI etc.).
- Managing per-request resources (DB connections, sessions).
- Clean separation of business logic from object construction.
- Testability: swap implementations by changing one provider line.

## Things you can achieve

- A `Service` that asks for `APIClient` and `UserDAO` by type hint, and gets
  them injected automatically.
- A DB connection that is opened at request start and closed at request end.
- One shared (APP-scoped) config/client reused across every request.
- Async dependencies (`await container.get(...)`) for async applications.

## References

- Docs: https://dishka.readthedocs.io/
- PyPI: https://pypi.org/project/dishka/
- GitHub: https://github.com/reagento/dishka
