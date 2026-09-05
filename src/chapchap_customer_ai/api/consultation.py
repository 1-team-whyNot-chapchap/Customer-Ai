from collections.abc import Collection
from typing import Annotated, Protocol
from uuid import UUID

from fastapi import APIRouter, Header, HTTPException

from chapchap_customer_ai.consultation.models import (
    APPROVED_CONSULTATION_SCOPES,
    ConsultationRequestError,
)
from chapchap_customer_ai.consultation.services import ConsultationResponseService
from chapchap_customer_ai.contracts.models import (
    ConsultationResponse,
    ConsultationResponseRequest,
    UserRole,
)
from chapchap_customer_ai.security.models import AuthenticatedContext, InternalAuthError


class ConsultationSecurityVerifier(Protocol):
    def verify_consultation(
        self,
        authorization: str,
        subject_assertion: str,
        *,
        expected_request_id: UUID,
        expected_consultation_id: int,
        allowed_subject_scopes: Collection[str],
        allowed_roles: Collection[UserRole],
    ) -> AuthenticatedContext: ...


def build_candidate_consultation_router(
    service: ConsultationResponseService,
    verifier: ConsultationSecurityVerifier,
) -> APIRouter:
    router = APIRouter(include_in_schema=False)

    @router.post(
        "/internal/v1/consultation-responses",
        response_model=ConsultationResponse,
        response_model_exclude_none=True,
    )
    def create_consultation_response(
        request: ConsultationResponseRequest,
        authorization: Annotated[str, Header(alias="Authorization")],
        subject_assertion: Annotated[str, Header(alias="X-Subject-Assertion")],
        request_id: Annotated[UUID, Header(alias="X-Request-Id")],
        idempotency_key: Annotated[str, Header(alias="Idempotency-Key")],
    ) -> ConsultationResponse:
        if request_id != request.request_id:
            raise HTTPException(status_code=400, detail="REQUEST_ID_MISMATCH")
        try:
            context = verifier.verify_consultation(
                authorization,
                subject_assertion,
                expected_request_id=request.request_id,
                expected_consultation_id=request.consultation_id,
                allowed_subject_scopes=APPROVED_CONSULTATION_SCOPES,
                allowed_roles={UserRole.CUSTOMER, UserRole.RIDER},
            )
            return service.respond(request, context, idempotency_key=idempotency_key)
        except InternalAuthError as error:
            raise HTTPException(status_code=error.status_code, detail=error.code.value) from None
        except ConsultationRequestError as error:
            raise HTTPException(status_code=error.status_code, detail=str(error)) from None

    return router
