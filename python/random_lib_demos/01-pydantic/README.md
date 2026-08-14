# pydantic

**pydantic** is the most popular data-validation library for Python. It lets you
declare the *shape* of your data using standard Python type hints, and then
automatically:

- **validate** incoming data (raising clear errors when it is wrong),
- **coerce** data into the right types where sensible (e.g. `"42"` → `42`),
- **serialize** models back to JSON-compatible dicts.

It powers FastAPI, and is the foundation of many other tools (including
`pydantic-settings`, which has its own demo in `../02-pydantic-settings`).

## Why use it?

- Write one model, get validation + serialization + docs for free.
- Catches bad data *at the boundary* of your program instead of deep inside.
- Produces descriptive, structured errors instead of `KeyError` / `TypeError`.
- Great editor support thanks to type hints and mypy/pyright integration.

## Key features

- `BaseModel` with full type-hint support (`str`, `int`, `float`, `bool`,
  `datetime`, `list[T]`, `dict[K, V]`, `Optional[T]`, `Literal[...]`, `Enum`…).
- `Field(...)` for defaults, aliases, constraints (`gt`, `le`, `min_length`…).
- `@field_validator` and `@model_validator` for custom rules.
- Nested models (a model can contain other models).
- Serialization: `.model_dump()`, `.model_dump_json()`, `.model_validate()`.
- Config knobs: strict mode, extra-field handling, frozen (immutable) models.
- Data classes (`@dataclass`) and `TypeAdapter` for non-model types.

## Install

```bash
pip install pydantic
```

## Use cases

- API request/response schemas (FastAPI, etc.).
- Configuration and settings validation.
- Parsing JSON/YAML/TOML into typed objects.
- Validating CLI arguments, event payloads, or database rows.
- Feature-flag and environment variable schemas.

## Things you can achieve

- Auto-generated JSON Schema from a model.
- Round-trip: `dict` → validated model → JSON string → model again.
- Field aliasing to map ugly external names to clean Python names.
- Custom cross-field validation (e.g. "end date must be after start date").
- Reusable, immutable config objects.

## References

- Docs: https://docs.pydantic.dev/
- PyPI: https://pypi.org/project/pydantic/
- GitHub: https://github.com/pydantic/pydantic
