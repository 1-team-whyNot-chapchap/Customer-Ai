import hashlib
import json
import time
from dataclasses import dataclass
from uuid import UUID

from chapchap_customer_ai.consultation.guardrails import ConsultationGuardrails
from chapchap_customer_ai.consultation.models import (
    CAPABILITY_SCOPES,
    Capability,
    ConsultationDependencyError,
    ConsultationRequestError,
    StateAvailability,
    StateFact,
)
from chapchap_customer_ai.consultation.ports import (
    ApprovedKnowledgeVersions,
    Clock,
    ConsultationResponseRegistry,
    ConsultationRetriever,
    CurrentStateProvider,
    ResponseComposer,
)
from chapchap_customer_ai.consultation.routing import (
    CapabilityResolver,
    RuleBasedRouteResolver,
)
from chapchap_customer_ai.contracts.models import (
    ConsultationDecision,
    ConsultationEvidence,
    ConsultationResponse,
    ConsultationResponseRequest,
    ConsultationRoute,
)
from chapchap_customer_ai.rag.models import RagCoreError, RetrievedKnowledge
from chapchap_customer_ai.security.models import AuthenticatedContext


class SystemMonotonicClock:
    def monotonic(self) -> float:
        return time.monotonic()


@dataclass(slots=True)
class _Deadline:
    clock: Clock
    expires_at: float

    def remaining(self, stage_cap: float) -> float:
        remaining = self.expires_at - self.clock.monotonic()
        if remaining <= 0:
            raise TimeoutError("The consultation deadline was exceeded.")
        return min(stage_cap, remaining)


@dataclass(frozen=True, slots=True)
class ConsultationResponseService:
    approved_versions: ApprovedKnowledgeVersions
    retriever: ConsultationRetriever
    state_provider: CurrentStateProvider
    composer: ResponseComposer
    registry: ConsultationResponseRegistry
    route_resolver: RuleBasedRouteResolver = RuleBasedRouteResolver()
    capability_resolver: CapabilityResolver = CapabilityResolver()
    guardrails: ConsultationGuardrails = ConsultationGuardrails()
    clock: Clock = SystemMonotonicClock()
    request_deadline_seconds: float = 8.0
    route_timeout_seconds: float = 0.5
    rag_timeout_seconds: float = 2.5
    state_timeout_seconds: float = 3.0
    compose_timeout_seconds: float = 3.0

    def __post_init__(self) -> None:
        if self.request_deadline_seconds <= 0 or any(
            cap <= 0
            for cap in (
                self.route_timeout_seconds,
                self.rag_timeout_seconds,
                self.state_timeout_seconds,
                self.compose_timeout_seconds,
            )
        ):
            raise ValueError("consultation deadline and stage caps must be positive")

    def respond(
        self,
        request: ConsultationResponseRequest,
        context: AuthenticatedContext,
        *,
        idempotency_key: str,
    ) -> ConsultationResponse:
        self._validate_request_context(request, context)
        key = idempotency_key.strip() if isinstance(idempotency_key, str) else ""
        if not key or len(key) > 200:
            raise ConsultationRequestError("A valid Idempotency-Key is required.")
        fingerprint = self._fingerprint(request)
        return self.registry.execute_once(
            key,
            fingerprint,
            lambda: self._respond_once(request, context),
        )

    def _respond_once(
        self, request: ConsultationResponseRequest, context: AuthenticatedContext
    ) -> ConsultationResponse:
        deadline = _Deadline(self.clock, self.clock.monotonic() + self.request_deadline_seconds)
        if not self.guardrails.input_is_safe(request.message, request.conversation_context):
            safe_route = RuleBasedRouteResolver().resolve(request.message)
            return self._handoff(request.request_id, safe_route)
        try:
            route = self.route_resolver.resolve(
                request.message, timeout_seconds=deadline.remaining(self.route_timeout_seconds)
            )
        except Exception:
            return self._handoff(request.request_id, ConsultationRoute.UNSUPPORTED)
        capabilities = self.capability_resolver.resolve(request.message)
        self._authorize_route(route, capabilities, context)
        if route == ConsultationRoute.UNSUPPORTED:
            return ConsultationResponse(
                schema_version="1.0",
                request_id=request.request_id,
                decision=ConsultationDecision.DEGRADED,
                answer="현재 고객지원 범위에서는 해당 요청에 답변하기 어렵습니다.",
                route=route,
                degraded=True,
                handoff_required=False,
            )
        if len(capabilities) > 2:
            return self._handoff(request.request_id, route)
        if (
            route in {ConsultationRoute.USER_STATE, ConsultationRoute.POLICY_AND_STATE}
            and not capabilities
        ):
            return self._handoff(request.request_id, route)

        evidence: tuple[RetrievedKnowledge, ...] = ()
        if route in {ConsultationRoute.POLICY, ConsultationRoute.POLICY_AND_STATE}:
            evidence = self._retrieve_policy(request, context, deadline)
            if not evidence:
                return self._handoff(request.request_id, route)

        state_facts: tuple[StateFact, ...] = ()
        if route in {ConsultationRoute.USER_STATE, ConsultationRoute.POLICY_AND_STATE}:
            state_facts = self._fetch_state(capabilities, context, deadline)
            if any(fact.availability == StateAvailability.FORBIDDEN for fact in state_facts):
                raise ConsultationRequestError(
                    "The current-state capability is forbidden.", status_code=403
                )

        if route == ConsultationRoute.USER_STATE:
            return self._state_response(request.request_id, route, capabilities, state_facts)
        return self._composed_response(request, route, evidence, state_facts, deadline)

    def _retrieve_policy(
        self,
        request: ConsultationResponseRequest,
        context: AuthenticatedContext,
        deadline: _Deadline,
    ) -> tuple[RetrievedKnowledge, ...]:
        try:
            raw_versions = self.approved_versions.resolve(context, request)
            versions = tuple(dict.fromkeys(raw_versions))
            if not versions or any(
                isinstance(version, bool) or not isinstance(version, int) or version <= 0
                for version in versions
            ):
                return ()
            rag_budget = deadline.remaining(self.rag_timeout_seconds)
            started_at = self.clock.monotonic()
            results = self.retriever.retrieve(
                request.message,
                versions,
            )
            if self.clock.monotonic() - started_at > rag_budget:
                return ()
            if any(item.evidence.knowledge_version_id not in versions for item in results):
                return ()
            return self.guardrails.safe_evidence(results)
        except (ConsultationDependencyError, RagCoreError, TimeoutError, ValueError):
            return ()
        except Exception:
            return ()

    def _fetch_state(
        self,
        capabilities: tuple[Capability, ...],
        context: AuthenticatedContext,
        deadline: _Deadline,
    ) -> tuple[StateFact, ...]:
        try:
            facts = tuple(
                self.state_provider.fetch(
                    capabilities,
                    context,
                    timeout_seconds=deadline.remaining(self.state_timeout_seconds),
                )
            )
        except Exception:
            return ()
        if (
            len(facts) != len(capabilities)
            or len({fact.capability for fact in facts}) != len(facts)
            or {fact.capability for fact in facts} != set(capabilities)
        ):
            return ()
        return facts

    def _state_response(
        self,
        request_id: UUID,
        route: ConsultationRoute,
        capabilities: tuple[Capability, ...],
        facts: tuple[StateFact, ...],
    ) -> ConsultationResponse:
        answers = self._state_answers(capabilities, facts)
        if not answers:
            return self._handoff(request_id, route)
        unresolved = any(
            fact.availability in {StateAvailability.UNAVAILABLE, StateAvailability.TIMEOUT}
            for fact in facts
        ) or len(facts) != len(capabilities)
        answer = " ".join(answers)
        if unresolved:
            answer += " 일부 현재 상태는 확인할 수 없어 관리자 확인이 필요합니다."
        if not self.guardrails.output_text_is_safe(answer):
            return self._handoff(request_id, route)
        return ConsultationResponse(
            schema_version="1.0",
            request_id=request_id,
            decision=(
                ConsultationDecision.DEGRADED if unresolved else ConsultationDecision.ANSWER
            ),
            answer=answer,
            route=route,
            degraded=unresolved,
            handoff_required=unresolved,
        )

    def _composed_response(
        self,
        request: ConsultationResponseRequest,
        route: ConsultationRoute,
        evidence: tuple[RetrievedKnowledge, ...],
        state_facts: tuple[StateFact, ...],
        deadline: _Deadline,
    ) -> ConsultationResponse:
        available_state = tuple(
            fact for fact in state_facts if fact.availability == StateAvailability.AVAILABLE
        )
        try:
            draft = self.composer.compose(
                request.message,
                request.conversation_context,
                evidence,
                available_state,
                timeout_seconds=deadline.remaining(self.compose_timeout_seconds),
            )
            used = self.guardrails.validate_draft(draft, evidence)
        except Exception:
            return self._handoff(request.request_id, route)
        if not used:
            return self._handoff(request.request_id, route)
        unresolved_state = route == ConsultationRoute.POLICY_AND_STATE and (
            len(available_state) != len(state_facts) or not state_facts
        )
        answer = draft.answer
        if unresolved_state:
            answer += " 현재 상태 일부는 확인할 수 없어 관리자 확인이 필요합니다."
        if not self.guardrails.output_text_is_safe(answer):
            return self._handoff(request.request_id, route)
        return ConsultationResponse(
            schema_version="1.0",
            request_id=request.request_id,
            decision=(
                ConsultationDecision.DEGRADED
                if unresolved_state
                else ConsultationDecision.ANSWER
            ),
            answer=answer,
            route=route,
            degraded=unresolved_state,
            handoff_required=unresolved_state,
            evidence=[self._evidence(item) for item in used],
        )

    @staticmethod
    def _state_answers(
        capabilities: tuple[Capability, ...], facts: tuple[StateFact, ...]
    ) -> tuple[str, ...]:
        by_capability = {fact.capability: fact for fact in facts}
        not_found = {
            Capability.PAYMENT_CURRENT: "조회 범위에 해당하는 결제 정보가 없습니다.",
            Capability.REFUND_RECENT: "조회 범위에 해당하는 환불 업무가 없습니다.",
            Capability.SUBSCRIPTION_CURRENT: "조회 범위에 해당하는 구독 정보가 없습니다.",
            Capability.DELIVERY_CURRENT: "오늘 조회 가능한 배송 정보가 없습니다.",
        }
        answers: list[str] = []
        for capability in capabilities:
            fact = by_capability.get(capability)
            if fact is None:
                continue
            if fact.availability == StateAvailability.AVAILABLE and fact.safe_answer:
                answers.append(fact.safe_answer)
            elif fact.availability == StateAvailability.NOT_FOUND:
                answers.append(not_found[capability])
        return tuple(answers)

    @staticmethod
    def _authorize_route(
        route: ConsultationRoute,
        capabilities: tuple[Capability, ...],
        context: AuthenticatedContext,
    ) -> None:
        required: set[str] = set()
        if route in {ConsultationRoute.POLICY, ConsultationRoute.POLICY_AND_STATE}:
            required.add("customer-ai.policy.read")
        if route in {ConsultationRoute.USER_STATE, ConsultationRoute.POLICY_AND_STATE}:
            required.update(CAPABILITY_SCOPES[capability] for capability in capabilities)
        if not required.issubset(context.subject.allowed_ai_scopes):
            raise ConsultationRequestError(
                "The subject scope is not allowed for this route.", status_code=403
            )

    @staticmethod
    def _validate_request_context(
        request: ConsultationResponseRequest, context: AuthenticatedContext
    ) -> None:
        subject = request.subject
        authenticated = context.subject
        if (
            context.service_subject != "customer-service"
            or subject.user_id != authenticated.user_id
            or subject.role != authenticated.role
            or frozenset(subject.allowed_ai_scopes) != authenticated.allowed_ai_scopes
            or request.request_id != authenticated.request_id
            or request.consultation_id != authenticated.consultation_id
        ):
            raise ConsultationRequestError(
                "The signed consultation context does not match the request.", status_code=401
            )

    @staticmethod
    def _evidence(item: RetrievedKnowledge) -> ConsultationEvidence:
        evidence = item.evidence
        return ConsultationEvidence(
            knowledge_version_id=evidence.knowledge_version_id,
            chunk_id=evidence.chunk_id,
            retrieval_rank=evidence.retrieval_rank,
            retrieval_score=evidence.retrieval_score,
        )

    @staticmethod
    def _handoff(request_id: UUID, route: ConsultationRoute) -> ConsultationResponse:
        return ConsultationResponse(
            schema_version="1.0",
            request_id=request_id,
            decision=ConsultationDecision.HANDOFF,
            route=route,
            degraded=False,
            handoff_required=True,
        )

    @staticmethod
    def _fingerprint(request: ConsultationResponseRequest) -> str:
        payload = request.model_dump(by_alias=True, mode="json")
        canonical = json.dumps(
            payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True
        ).encode("utf-8")
        return hashlib.sha256(canonical).hexdigest()
