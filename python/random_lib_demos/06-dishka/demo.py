"""
dishka demo — dependency injection with scopes.

Run with:  .venv/bin/python 06-dishka/demo.py

The idea: classes declare their dependencies in `__init__` type hints, and a
Provider tells dishka how to build each one. The container then wires the
graph for you, respecting object lifetimes (scopes).
"""

from collections.abc import Iterable

from dishka import Provider, Scope, make_container, provide


# ---------------------------------------------------------------------------
# 1. The classes — note how dependencies are only type hints
# ---------------------------------------------------------------------------
class Config:
    """Shared, read-only configuration (lives for the whole app)."""

    def __init__(self, database_url: str = "postgres://localhost/app"):
        self.database_url = database_url


class APIClient:
    """A stateless HTTP client (also app-wide)."""

    def fetch_user(self, user_id: int) -> str:
        return f"user-{user_id} from API"


class UserRepository:
    """Data-access object. Has an interface (base class) so we can swap impls."""

    def find(self, user_id: int) -> str:
        raise NotImplementedError


class PostgresUserRepository(UserRepository):
    def __init__(self, config: Config):
        self.config = config

    def find(self, user_id: int) -> str:
        return f"user-{user_id} from DB ({self.config.database_url})"


class UserService:
    """Business logic. Depends on the client and the repository."""

    def __init__(self, api: APIClient, repo: UserRepository):
        self.api = api
        self.repo = repo

    def get_user(self, user_id: int) -> str:
        return f"Service used: {self.api.fetch_user(user_id)} and {self.repo.find(user_id)}"


# ---------------------------------------------------------------------------
# 2. Providers: tell dishka *how* to build things
# ---------------------------------------------------------------------------
# A provider with a default scope: everything registered on it uses REQUEST
# scope unless overridden.
service_provider = Provider(scope=Scope.REQUEST)
service_provider.provide(UserService)
# Bind the interface (UserRepository) to the concrete class.
service_provider.provide(PostgresUserRepository, provides=UserRepository)
# This one is app-wide: overridden with scope=Scope.APP.
service_provider.provide(APIClient, scope=Scope.APP)
service_provider.provide(Config, scope=Scope.APP)


# A provider that builds a resource requiring cleanup. The `yield`-based
# factory opens the connection on enter and closes it on exit of its scope.
class DatabaseConnectionProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def connection(self) -> Iterable[str]:
        conn = "db-connection-123"
        print("      [dishka] opened:", conn)
        yield conn
        print("      [dishka] closed:", conn)


# ---------------------------------------------------------------------------
# 3. Build the container and resolve dependencies
# ---------------------------------------------------------------------------
container = make_container(service_provider, DatabaseConnectionProvider())

print("1. App-scoped dependencies (shared singletons):")
cfg1 = container.get(Config)
cfg2 = container.get(Config)
client = container.get(APIClient)
print(f"   config is a singleton: {cfg1 is cfg2}")
print(f"   client available at app level: {client is not None}")

# REQUEST-scoped dependencies live inside a sub-container context manager.
# They can also reach *up* into the APP scope (e.g. Config, APIClient).
print("\n2. Request-scoped dependencies (inside a request):")
with container() as request_scope:
    service = request_scope.get(UserService)
    print("   ", service.get_user(42))

    # Within one request, the same service instance is reused...
    again = request_scope.get(UserService)
    print(f"   same service within a request: {service is again}")

    # ...and the DB connection is opened now (see yield above).

# Exiting the `with` block closed the DB connection (see the "[dishka] closed"
# line printed just before this message).
print("   (request ended -> connection closed automatically)")


# ---------------------------------------------------------------------------
# 4. Two requests are independent
# ---------------------------------------------------------------------------
print("\n3. Requests are isolated:")
with container() as r1:
    a = r1.get(UserService)
with container() as r2:
    b = r2.get(UserService)
print(f"   service in request 1 == request 2? {a is b}")

# Close the container to run app-scope teardown (none here, but good practice).
container.close()

print("\nDone — dishka wired and cleaned up the object graph.")
