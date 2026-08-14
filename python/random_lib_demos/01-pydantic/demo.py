"""
pydantic demo — data validation & serialization using type hints.

Run with:  .venv/bin/python 01-pydantic/demo.py

The script builds a small "user signup" model step by step so you can see
how pydantic turns plain Python type hints into validation logic.
"""

from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    ValidationError,
    field_validator,
    model_validator,
)


# ---------------------------------------------------------------------------
# 1. The simplest possible model
# ---------------------------------------------------------------------------
# Declare a class with typed fields. pydantic reads the type hints and uses
# them to validate whatever dict/object you pass in.
class User(BaseModel):
    name: str
    age: int
    is_admin: bool = False  # a default value means the field is optional


alice = User(name="Alice", age=30)
print("1. Basic model:", alice)
print("   alice.age is an int:", type(alice.age).__name__)

# pydantic *coerces* where it makes sense: the string "42" becomes the int 42.
coerced = User(name="Bob", age="42")
print("   Coercion:", coerced, "->", type(coerced.age).__name__)


# ---------------------------------------------------------------------------
# 2. Validation errors are descriptive
# ---------------------------------------------------------------------------
# Passing the wrong type raises a ValidationError with one message per problem.
try:
    User(name="Eve", age="not-a-number")
except ValidationError as err:
    print("\n2. Validation error:")
    for e in err.errors():
        print(f"   - field={e['loc']}  msg={e['msg']}  input={e['input']!r}")


# ---------------------------------------------------------------------------
# 3. Field constraints & metadata via Field(...)
# ---------------------------------------------------------------------------
class Product(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    price: float = Field(gt=0, description="Price must be greater than zero")
    tags: list[str] = []


try:
    Product(name="X", price=-5.0)
except ValidationError as err:
    print("\n3. Field constraints:")
    for e in err.errors():
        print(f"   - field={e['loc']}  msg={e['msg']}")


# ---------------------------------------------------------------------------
# 4. Enums, Literals, and nested models
# ---------------------------------------------------------------------------
class Role(str, Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class Account(BaseModel):
    username: str
    role: Role  # invalid strings are rejected, valid ones become Role members
    address: Address  # nested model: pass a dict and it is validated too


acct = Account(
    username="carol",
    role="admin",
    address={"street": "1 Main St", "city": "Springfield", "zip_code": "12345"},
)
print("\n4. Nested models:", acct)
print("   acct.role is a Role enum:", acct.role, type(acct.role).__name__)


# ---------------------------------------------------------------------------
# 5. Custom validators
# ---------------------------------------------------------------------------
class Signup(BaseModel):
    email: str
    password: str = Field(min_length=8)
    birth_date: date
    start_date: date
    end_date: date

    # field_validator: extra rule applied to a single field after type parsing.
    @field_validator("email")
    @classmethod
    def email_must_contain_at(cls, value: str) -> str:
        if "@" not in value:
            raise ValueError("email must contain '@'")
        return value

    # model_validator: rule that can look at *several* fields at once.
    @model_validator(mode="after")
    def dates_must_be_in_order(self) -> "Signup":
        if self.start_date >= self.end_date:
            raise ValueError("end_date must be after start_date")
        return self


ok = Signup(
    email="carol@example.com",
    password="s3cret-pw",
    birth_date=date(1990, 1, 1),
    start_date=date(2026, 1, 1),
    end_date=date(2026, 12, 31),
)
print("\n5. Custom validators passed for:", ok.email)

try:
    Signup(
        email="no-at-sign.example.com",  # fails field_validator
        password="s3cret-pw",
        birth_date=date(1990, 1, 1),
        start_date=date(2026, 1, 1),
        end_date=date(2026, 12, 31),
    )
except ValidationError as err:
    print("   Caught bad email:")
    for e in err.errors():
        print(f"   - field={e['loc']}  msg={e['msg']}")


# ---------------------------------------------------------------------------
# 6. Serialization: model -> dict / JSON, and back
# ---------------------------------------------------------------------------
class Event(BaseModel):
    title: str
    starts_at: datetime
    capacity: Optional[int] = None


evt = Event(title="Launch", starts_at=datetime(2026, 8, 14, 18, 0), capacity=250)

# dict is JSON-friendly (datetime is preserved as a datetime object here)...
print("\n6. Serialization:")
print("   model_dump():", evt.model_dump())
# ...while model_dump_json() stringifies everything (datetime -> ISO string).
print("   model_dump_json():", evt.model_dump_json())

# Round-trip: parse a JSON string back into a validated Event.
parsed = Event.model_validate_json(
    '{"title":"Launch","starts_at":"2026-08-14T18:00:00"}'
)
print("   Round-tripped:", parsed)


# ---------------------------------------------------------------------------
# 7. Config: frozen (immutable) models and aliases
# ---------------------------------------------------------------------------
class Settings(BaseModel):
    # forbid mutation after creation and allow extra keys to be ignored.
    model_config = ConfigDict(frozen=True, extra="ignore")

    # alias lets you map an ugly external name to a clean Python attribute.
    api_endpoint: str = Field(alias="api.endpoint")


settings = Settings(**{"api.endpoint": "https://api.example.com", "ignored": 1})
print("\n7. Frozen + aliased model:")
print("   settings.api_endpoint =", settings.api_endpoint)
print("   dumped by alias:", settings.model_dump(by_alias=True))

try:
    settings.api_endpoint = "nope"  # type: ignore[misc]
except Exception as exc:  # pydantic raises ValidationError for frozen models
    print(f"   Mutation blocked ({type(exc).__name__}).")


print("\nDone — every section above shows a pydantic feature in isolation.")
