# pydantic-settings

**pydantic-settings** extends **pydantic** so you can manage application
configuration (settings) with the same validation you get from data models.
You define settings as a class, and values are automatically loaded from
**environment variables**, `.env` files, secrets, or any custom source.

## Why use it?

- Configuration is the #1 source of "works on my machine" bugs — this makes it
  typed, validated, and centralized.
- Environment variables are strings; pydantic-settings coerces them to the
  types you actually want (`int`, `bool`, `list`, `Enum`, …).
- No more hand-written `os.environ.get("PORT", 8000)` scattered everywhere.
- Integrates with pydantic's validation, so a bad setting fails fast at startup
  with a clear message instead of crashing hours later.

## Key features

- `BaseSettings` (a pydantic `BaseModel` that reads from settings sources).
- Automatic mapping of environment variables to fields (case-insensitive).
- `.env` / `.env.prod` file support via `python-dotenv`.
- `Field(validation_alias=...)` to bind a field to a differently-named env var.
- Nested settings via `BaseSettings` sub-models (prefixes like `APP__DB__HOST`).
- Custom `settings_customise_sources()` for arbitrary sources (JSON, Vault…).
- Secrets directory support (`/run/secrets/<name>`).
- `@no_type_check`, aliases, and pydantic validators all still work.

## Install

```bash
pip install pydantic-settings
```

## Use cases

- 12-factor app configuration.
- Web apps (FastAPI/Starlette) settings: host, port, DB URL, secret keys.
- Different environments: `.env`, `.env.prod`, `.env.test`.
- Feature flags and tunable knobs loaded from env vars.
- Cloud/container deployments where config arrives as environment variables.

## Things you can achieve

- One `Settings` class that reads a whole configuration tree from env vars.
- Fail-fast validation of ports, URLs, and enum choices at boot time.
- Per-environment overrides via multiple `.env` files.
- Sensible type coercion (`"true"` → `True`, `"1,2,3"` → `[1, 2, 3]`).

## References

- Docs: https://docs.pydantic.dev/latest/concepts/pydantic_settings/
- PyPI: https://pypi.org/project/pydantic-settings/
- GitHub: https://github.com/pydantic/pydantic-settings
