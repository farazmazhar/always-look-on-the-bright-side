"""
dacite demo — build data classes from plain dictionaries.

Run with:  .venv/bin/python 03-dacite/demo.py

dacite's one job: `from_dict(SomeClass, some_dict)` -> a populated instance.
This script shows the basics plus the Config options for real-world data.
"""

from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import List, Optional, Union

from dacite import Config, from_dict


# ---------------------------------------------------------------------------
# 1. The basic case
# ---------------------------------------------------------------------------
@dataclass
class Person:
    name: str
    age: int


data = {"name": "Alice", "age": 30}
alice = from_dict(Person, data)
print("1. Basic from_dict:", alice, "->", type(alice).__name__)


# ---------------------------------------------------------------------------
# 2. Nested data classes and collections
# ---------------------------------------------------------------------------
@dataclass
class Address:
    street: str
    city: str


@dataclass
class Employee:
    name: str
    address: Address            # nested: dacite recurses automatically
    skills: List[str]           # list of simple types


emp_data = {
    "name": "Bob",
    "address": {"street": "1 Main St", "city": "Springfield"},
    "skills": ["python", "rust"],
}
bob = from_dict(Employee, emp_data)
print("\n2. Nested + list:")
print("   ", bob)
print("   bob.address is an Address:", isinstance(bob.address, Address))


# ---------------------------------------------------------------------------
# 3. Enums and Optional fields
# ---------------------------------------------------------------------------
class Status(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


@dataclass
class Account:
    username: str
    status: Status
    note: Optional[str] = None     # missing key or None both work
    tags: Optional[List[str]] = None


acct = from_dict(Account, {"username": "carol", "status": "active"})
print("\n3. Enum + Optional:")
print("   ", acct)
print("   acct.status is a Status enum:", type(acct.status).__name__)


# ---------------------------------------------------------------------------
# 4. Custom type hooks via Config
# ---------------------------------------------------------------------------
# Real data often arrives with strings where you want dates, decimals, etc.
# A type hook says: "whenever you see a `date` field, parse it like this".
def parse_date(value: str) -> date:
    return date.fromisoformat(value)


@dataclass
class Article:
    title: str
    published: date


config = Config(type_hooks={date: parse_date})
article = from_dict(
    Article,
    {"title": "Hello", "published": "2026-08-14"},
    config=config,
)
print("\n4. Type hook (string -> date):")
print("   ", article, "->", type(article.published).__name__)


# ---------------------------------------------------------------------------
# 5. Union / Optional coercion with cast
# ---------------------------------------------------------------------------
@dataclass
class Payload:
    # A field that may be an int or a string — dacite picks by config.
    value: Union[int, str]


# Without `cast`, dacite prefers the first union member that works (int).
print("\n5. Union handling:")
print("   int kept as int:   ", from_dict(Payload, {"value": 42}))
print("   '42' stays str:    ", from_dict(Payload, {"value": "42"}))

# With cast=[int], dacite tries to coerce to int when possible.
coercing = Config(cast=[int])
print("   '42' cast to int:  ", from_dict(Payload, {"value": "42"}, coercing))


# ---------------------------------------------------------------------------
# 6. Strict / check_types
# ---------------------------------------------------------------------------
# check_types=True verifies the *values* match the declared types and raises
# DaciteError instead of silently accepting a wrong type.
try:
    from_dict(Person, {"name": "Mallory", "age": "old"}, Config(check_types=True))
except Exception as exc:
    print(f"\n6. check_types caught a bad value: {type(exc).__name__}: {exc}")


print("\nDone — dacite turned raw dicts into typed data classes.")
