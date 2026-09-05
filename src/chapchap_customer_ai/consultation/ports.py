from collections.abc import Sequence
from typing import Protocol
from uuid import UUID

from chapchap_customer_ai.consultation.models import (
    Capability,
    GroundedAnswerDraft,
    StateFact,
)
from chapchap_customer_ai.contracts.models import (
    ConsultationResponse,
    ConsultationResponseRequest,
    ConsultationRoute,
)
from chapchap_customer_ai.rag.models import RetrievedKnowledge
from chapchap_customer_ai.security.models import AuthenticatedContext


class ApprovedKnowledgeVersions(Protocol):
    def resolve(
        self, context: AuthenticatedContext, request: ConsultationResponseRequest
    ) -> Sequence[int]: ...


class ConsultationRetriever(Protocol):
    def retrieve(
        self,
        query: str,
        allowed_knowledge_version_ids: Sequence[int],
    ) -> Sequence[RetrievedKnowledge]: ...


class CurrentStateProvider(Protocol):
    def fetch(
        self,
        capabilities: Sequence[Capability],
        context: AuthenticatedContext,
        *,
        timeout_seconds: float,
    ) -> Sequence[StateFact]: ...


class ResponseComposer(Protocol):
    def compose(
        self,
        message: str,
        conversation_context: Sequence[str],
        evidence: Sequence[RetrievedKnowledge],
        state_facts: Sequence[StateFact],
        *,
        timeout_seconds: float,
    ) -> GroundedAnswerDraft: ...


class AmbiguousRouteClassifier(Protocol):
    def classify(self, message: str, *, timeout_seconds: float) -> ConsultationRoute: ...


class ConsultationResponseRegistry(Protocol):
    def execute_once(
        self,
        key: str,
        fingerprint: str,
        factory: "ResponseFactory",
    ) -> ConsultationResponse: ...


class ResponseFactory(Protocol):
    def __call__(self) -> ConsultationResponse: ...


class Clock(Protocol):
    def monotonic(self) -> float: ...


class RequestIdObserver(Protocol):
    def observe(self, request_id: UUID) -> None: ...
