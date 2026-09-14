import os
from collections.abc import Collection
from typing import Annotated, Protocol
from uuid import UUID

from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel, ConfigDict

from chapchap_customer_ai.consultation.models import (
    APPROVED_CONSULTATION_SCOPES,
    ConsultationRequestError,
)
from chapchap_customer_ai.consultation.plans import ConsultationPlans
from chapchap_customer_ai.consultation.services import ConsultationResponseService
from chapchap_customer_ai.contracts.models import (
    ConsultationResponse,
    ConsultationResponseRequest,
    UserRole,
)
from chapchap_customer_ai.security.models import AuthenticatedContext, InternalAuthError


class PlanExecutionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    planId: UUID
    request: ConsultationResponseRequest


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
    plans = ConsultationPlans(
        service, enabled=os.environ.get("CONSULTATION_BOUNDARIES_ENABLED", "").lower() == "true"
    )

    def authenticate(request, authorization, assertion, request_id):
        if request_id != request.request_id:
            raise ConsultationRequestError("REQUEST_ID_MISMATCH")
        return verifier.verify_consultation(
            authorization,
            assertion,
            expected_request_id=request.request_id,
            expected_consultation_id=request.consultation_id,
            allowed_subject_scopes=APPROVED_CONSULTATION_SCOPES,
            allowed_roles={UserRole.CUSTOMER, UserRole.RIDER},
        )

    @router.post("/internal/v1/consultation-interpretations")
    def interpret(
        request: ConsultationResponseRequest,
        authorization: Annotated[str, Header(alias="Authorization")],
        assertion: Annotated[str, Header(alias="X-Subject-Assertion")],
        request_id: Annotated[UUID, Header(alias="X-Request-Id")],
    ):
        if not plans.enabled:
            raise HTTPException(status_code=404, detail="NOT_ENABLED")
        try:
            context = authenticate(request, authorization, assertion, request_id)
            return plans.prepare(request, context)
        except InternalAuthError as error:
            raise HTTPException(status_code=error.status_code, detail=error.code.value) from None
        except ConsultationRequestError as error:
            raise HTTPException(status_code=error.status_code, detail=str(error)) from None

    @router.post(
        "/internal/v1/consultation-plan-responses",
        response_model=ConsultationResponse,
        response_model_exclude_none=True,
    )
    def execute(
        body: PlanExecutionRequest,
        authorization: Annotated[str, Header(alias="Authorization")],
        assertion: Annotated[str, Header(alias="X-Subject-Assertion")],
        request_id: Annotated[UUID, Header(alias="X-Request-Id")],
        key: Annotated[str, Header(alias="Idempotency-Key")],
    ):
        if not plans.enabled:
            raise HTTPException(status_code=404, detail="NOT_ENABLED")
        try:
            context = authenticate(body.request, authorization, assertion, request_id)
            return plans.execute(body.planId, body.request, context, key)
        except InternalAuthError as error:
            raise HTTPException(status_code=error.status_code, detail=error.code.value) from None
        except ConsultationRequestError as error:
            raise HTTPException(status_code=error.status_code, detail=str(error)) from None

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
