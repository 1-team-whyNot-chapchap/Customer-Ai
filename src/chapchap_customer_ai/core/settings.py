from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(".env"),
        env_file_encoding="utf-8",
        env_prefix="CUSTOMER_AI_",
        extra="ignore",
    )

    app_name: str = "chapchap-customer-ai"
    environment: str = "local"
    log_level: str = "INFO"
    service_jwt_issuer: str = "chapchap-auth-service"
    service_jwt_audience: str = "chapchap-customer-ai"
    service_jwks_url: str | None = None
    subject_assertion_jwks_url: str | None = None
    request_deadline_seconds: float = Field(default=8.0, gt=0, le=30)


@lru_cache
def get_settings() -> Settings:
    return Settings()
