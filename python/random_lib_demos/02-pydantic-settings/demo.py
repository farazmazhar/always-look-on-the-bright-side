"""
pydantic-settings demo — typed application configuration from env vars.

Run with:  .venv/bin/python 02-pydantic-settings/demo.py

The demo reads settings from a real .env file (created next to this script)
and from the process environment, then validates them like any pydantic model.
"""

import os
from enum import Enum
from pathlib import Path

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# Point pydantic-settings at a real .env file so the demo is reproducible.
# (If you delete the file, the defaults below are used instead.)
ENV_FILE = Path(__file__).with_name(".env")


# ---------------------------------------------------------------------------
# 1. A flat settings class
# ---------------------------------------------------------------------------
# SettingsConfigDict controls *where* settings come from. Here we read from a
# .env file first, then fall back to real environment variables.
class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE, extra="ignore")

    app_name: str = "my-app"                    # default, overridable via APP_NAME
    port: int = 8000                            # coerced from the string "8000"
    debug: bool = False                         # "true"/"1"/"yes" all -> True
    log_level: str = "INFO"


settings = AppSettings()
print("1. Flat settings (from .env or defaults):")
print("   ", settings.model_dump())


# ---------------------------------------------------------------------------
# 2. Field aliases, lists and enums
# ---------------------------------------------------------------------------
class Environment(str, Enum):
    DEV = "dev"
    STAGING = "staging"
    PROD = "prod"


class ServerSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE, extra="ignore")

    # validation_alias binds this field to a specific env-var name.
    environment: Environment = Environment.DEV
    # pydantic parses a comma-separated string into a list of str.
    allowed_hosts: list[str] = ["localhost"]
    # A JSON-ish string also works for list[int].
    port_range: list[int] = [8080, 8081]


srv = ServerSettings()
print("\n2. Aliases, enums and lists:")
print("   environment =", srv.environment, "(", type(srv.environment).__name__, ")")
print("   allowed_hosts =", srv.allowed_hosts)
print("   port_range =", srv.port_range)


# ---------------------------------------------------------------------------
# 3. Nested settings with a prefix (Django/12-factor style)
# ---------------------------------------------------------------------------
class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="DB__", env_file=ENV_FILE)

    host: str = "localhost"
    port: int = 5432
    user: str = "postgres"
    password: str = Field(default="", repr=False)  # never printed in repr


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE, env_nested_delimiter="__")

    app: AppSettings = AppSettings()
    db: DatabaseSettings = DatabaseSettings()


cfg = Config()
print("\n3. Nested settings:")
print("   cfg.db.host =", cfg.db.host)
print("   cfg.db.port =", cfg.db.port)
print("   cfg.db.password repr hidden:", cfg.db.password != "", "(see .env)")


# ---------------------------------------------------------------------------
# 4. Validation on settings — fail fast at startup
# ---------------------------------------------------------------------------
class ValidatedSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE, extra="ignore")

    api_key: str = Field(min_length=10)
    retries: int = Field(ge=0, le=10)

    @field_validator("api_key")
    @classmethod
    def no_spaces(cls, v: str) -> str:
        if " " in v:
            raise ValueError("api_key must not contain spaces")
        return v


try:
    # Simulate a bad environment by injecting a short API key.
    os.environ["API_KEY"] = "short"
    bad = ValidatedSettings()
    print("\n4. (no error — check your .env / environment)")
except Exception as exc:
    print(f"\n4. Invalid setting caught at startup: {type(exc).__name__}")
finally:
    os.environ.pop("API_KEY", None)  # clean up so the demo stays repeatable


# ---------------------------------------------------------------------------
# 5. Show exactly what a real .env file looks like
# ---------------------------------------------------------------------------
# pydantic-settings uses the same format as `dotenv`: KEY=VALUE lines.
print("\n5. This demo ships with a .env file. Here is its content:")
print("   " + ENV_FILE.read_text().replace("\n", "\n   ") if ENV_FILE.exists()
      else "   (no .env file present — defaults were used)")

print("\nDone — settings are validated, typed pydantic models.")
