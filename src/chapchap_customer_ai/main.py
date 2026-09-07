from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from chapchap_customer_ai.api.health import router as health_router
from chapchap_customer_ai.core.settings import get_settings
from chapchap_customer_ai.security.runtime import create_internal_auth_runtime


@asynccontextmanager
async def _lifespan(app: FastAPI) -> AsyncIterator[None]:
    settings = get_settings()
    runtime = None
    if settings.internal_security_enabled:
        runtime = create_internal_auth_runtime(settings)
        app.state.internal_auth_runtime = runtime
    try:
        yield
    finally:
        if runtime is not None:
            runtime.close()


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
        lifespan=_lifespan,
    )
    app.include_router(health_router)
    return app
