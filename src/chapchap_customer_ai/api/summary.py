from typing import Annotated, Protocol
from uuid import UUID

from fastapi import APIRouter, Header, HTTPException, status

from chapchap_customer_ai.contracts.models import (
    ConsultationSummaryAccepted,
    ConsultationSummaryRequest,
)
from chapchap_customer_ai.security.models import AuthenticatedService, InternalAuthError
from chapchap_customer_ai.summary.models import SummaryRequestError
from chapchap_customer_ai.summary.services import ConsultationSummaryService


class ServiceOnlyVerifier(Protocol):
    def verify_service(self, authorization: str) -> AuthenticatedService: ...


def build_candidate_summary_router(
    service: ConsultationSummaryService,
    verifier: ServiceOnlyVerifier,
) -> APIRouter:
    router = APIRouter(include_in_schema=False)

    @router.post(
        "/internal/v1/consultation-summaries",
        status_code=status.HTTP_202_ACCEPTED,
        response_model=ConsultationSummaryAccepted,
    )
    def accept_consultation_summary(
        request: ConsultationSummaryRequest,
        authorization: Annotated[str, Header(alias="Authorization")],
        request_id: Annotated[UUID, Header(alias="X-Request-Id")],
        idempotency_key: Annotated[str, Header(alias="Idempotency-Key")],
    ) -> ConsultationSummaryAccepted:
        try:
            verifier.verify_service(authorization)
            return service.accept(
                request,
                request_id=request_id,
                idempotency_key=idempotency_key,
            )
        except InternalAuthError as error:
            raise HTTPException(status_code=error.status_code, detail=error.code.value) from None
        except SummaryRequestError as error:
            raise HTTPException(status_code=error.status_code, detail=str(error)) from None

    return router
