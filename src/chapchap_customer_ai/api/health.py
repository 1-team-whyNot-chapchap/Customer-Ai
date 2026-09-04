from fastapi import APIRouter

from chapchap_customer_ai.core.settings import get_settings

router = APIRouter(tags=["system"])


@router.get("/healthz", include_in_schema=False)
def health() -> dict[str, str]:
    settings = get_settings()
    return {
        "status": "ok",
        "service": settings.app_name,
        "environment": settings.environment,
    }
