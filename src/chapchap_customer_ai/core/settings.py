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
    subject_assertion_issuer: str = "chapchap-customer-service"
    service_jwks_url: str | None = None
    subject_assertion_jwks_url: str | None = None
    jwks_timeout_seconds: float = Field(default=5.0, gt=0, le=10)
    jwks_cache_lifespan_seconds: int = Field(default=300, ge=60, le=3600)
    request_deadline_seconds: float = Field(default=8.0, gt=0, le=30)
    rag_embedding_model: str = "intfloat/multilingual-e5-small"
    rag_embedding_dimensions: int = Field(default=384, gt=0)
    rag_top_k: int = Field(default=5, gt=0, le=50)
    rag_similarity_threshold: float = Field(default=0.70, ge=0.0, le=1.0)
    chroma_collection_name: str = Field(
        default="customer_ai_knowledge_v1", pattern=r"^[a-z0-9][a-z0-9_-]{2,62}$"
    )
    chroma_persist_directory: Path | None = None


@lru_cache
def get_settings() -> Settings:
    return Settings()
