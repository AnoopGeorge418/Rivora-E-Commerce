# Resonsible for loading all the env variables from .env files to entire project

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from functools import lru_cache
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    # App Settings
    APP_NAME: str = "Rivora"
    ENVIRONMENT: str = Field(default="development") # development | production
    DEBUG: bool = Field(default=True)

    # Env variables here
    ...

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )

# Use lru_cache to prevent creating multiple instances
@lru_cache
def get_settings() -> Settings:
    return Settings() # type: ignore unnecessary warning

# Global Settings instance
app_settings = get_settings()
