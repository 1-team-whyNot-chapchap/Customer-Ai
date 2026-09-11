from typing import Annotated, Protocol
from uuid import UUID

from fastapi import APIRouter, Header, HTTPException, status

from chapchap_customer_ai.contracts.models import (
    KnowledgeProcessingAccepted,
    KnowledgeProcessingRequest,
)
from chapchap_customer_ai.knowledge.models import KnowledgeRequestError
from chapchap_customer_ai.knowledge.services import KnowledgeProcessingService
from chapchap_customer_ai.security.models import AuthenticatedService, InternalAuthError


class ServiceOnlyVerifier(Protocol):
    def verify_service(self, authorization: str) -> AuthenticatedService: ...


def build_candidate_knowledge_router(
    service: KnowledgeProcessingService,
    verifier: ServiceOnlyVerifier,
) -> APIRouter:
    router = APIRouter(include_in_schema=False)

    @router.post(
        "/internal/v1/knowledge-processings",
        status_code=status.HTTP_202_ACCEPTED,
        response_model=KnowledgeProcessingAccepted,
    )
    def accept_knowledge_processing(
        request: KnowledgeProcessingRequest,
        authorization: Annotated[str, Header(alias="Authorization")],
        request_id: Annotated[UUID, Header(alias="X-Request-Id")],
        idempotency_key: Annotated[str, Header(alias="Idempotency-Key")],
    ) -> KnowledgeProcessingAccepted:
        try:
            verifier.verify_service(authorization)
            return service.accept(
                request, request_id=request_id, idempotency_key=idempotency_key
            )
        except InternalAuthError as error:
            raise HTTPException(status_code=error.status_code, detail=error.code.value) from None
        except KnowledgeRequestError as error:
            raise HTTPException(status_code=error.status_code, detail=str(error)) from None

    return router
