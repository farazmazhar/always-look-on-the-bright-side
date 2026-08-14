# dacite

**dacite** creates data class instances from plain dictionaries. Where you
might otherwise write repetitive `MyClass(**data)` glue or manual `.get()`
chains, dacite does it for you — recursively, and with sensible type
conversion for nested data classes, enums, unions, and collections.

## Why use it?

- You receive JSON/dicts (from APIs, config files, DB rows) and want typed
  objects quickly, without a heavy validation framework.
- It plays nicely with `@dataclass`, so it fits codebases that already use
  the standard library rather than pydantic models.
- Handles messy real-world inputs: missing keys, `None` for optional fields,
  nested structures, and `Union`/`Optional` types.

## Key features

- `from_dict(DataClass, data)` — the one entry point you need.
- Recursively builds nested data classes.
- Handles `Optional[T]`, `Union[...]`, `Enum`, `list[T]`, `dict[K, V]`, `tuple`.
- `Config` object to customize behavior:
  - `type_hooks` — register a converter for a specific type,
  - `cast` — control how `Union`/`Optional` fields are chosen,
  - `strict` / `check_types` — type-safety knobs,
  - `forward_references` — resolve self-referencing classes.
- Works with `typing.TypedDict`, `NamedTuple`, and plain classes too.

## Install

```bash
pip install dacite
```

## Use cases

- Turning API JSON responses into typed Python objects.
- Loading YAML/JSON config files into nested data classes.
- Hydrating domain objects from database documents.
- Adapter/anti-corruption layers between systems.

## Things you can achieve

- One line to convert a deeply nested dict into a tree of data classes.
- Convert string enums to real `Enum` members automatically.
- Custom conversion hooks (e.g. parse ISO date strings into `date`).
- Optional-field handling without `KeyError` noise.

## References

- Docs (README): https://github.com/konradhalas/dacite
- PyPI: https://pypi.org/project/dacite/
- GitHub: https://github.com/konradhalas/dacite
