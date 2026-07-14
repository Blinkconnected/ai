from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Blink AI"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"

    ERP_URL: str
    ERP_API_KEY: str
    ERP_API_SECRET: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
