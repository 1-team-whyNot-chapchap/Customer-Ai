"""Bounded, short-lived, subject-bound plans. No tools are run during preparation."""

import hashlib
import json
import re
import time
from dataclasses import dataclass, replace
from threading import Lock
from uuid import uuid4

from chapchap_customer_ai.consultation.interpretation import (
    Intent,
    Interpretation,
    Period,
    SubjectReference,
    active_context,
    boundary,
    customer_context,
    explicit_topics,
    interpret_rules,
    route_for,
)
from chapchap_customer_ai.consultation.models import CAPABILITY_SCOPES, ConsultationRequestError
from chapchap_customer_ai.contracts.models import ConsultationResponse


@dataclass(frozen=True)
class FixedRoute:
    route: object

    def resolve(self, message, **kwargs):
        return self.route


@dataclass(frozen=True)
class FixedCapabilities:
    capabilities: tuple

    def resolve(self, message):
        return self.capabilities


@dataclass(frozen=True)
class Plan:
    fingerprint: str
    expires: float
    capabilities: tuple
    route: object
    notice: str | None
    scopes: frozenset
    intent: Intent


def fingerprint(request):
    body = request.model_dump(mode="json")
    body["subject"].pop("allowed_ai_scopes", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()


class ConsultationPlans:
    def __init__(self, service, enabled=False, clock=time.monotonic):
        self.service = service
        self.enabled = enabled
        self.clock = clock
        self._plans = {}
        self._lock = Lock()

    def prepare(self, request, context):
        self.service._validate_request_context(request, context)
        if context.subject.allowed_ai_scopes != frozenset({"customer-ai.policy.read"}):
            raise ConsultationRequestError(
                "Interpretation requires policy-only scope.", status_code=403
            )
        start = self.clock()
        safe = self.service.guardrails.input_is_safe(request.message, request.conversation_context)
        safe_history = active_context(
            self.service.guardrails.safe_context(request.conversation_context)
        )
        candidate = interpret_rules(request.message, safe_history)
        history = customer_context(safe_history)
        explicit_history = [
            explicit_topics(t["content"]) for t in history if explicit_topics(t["content"])
        ]
        ambiguous_reference = (
            not candidate.topics
            and bool(re.search(r"그건|그거|그럼|내꺼|내거", request.message))
            and (not history or (explicit_history and len(explicit_history[-1]) > 1))
        )
        if safe and candidate.intent == Intent.UNCLEAR and not ambiguous_reference:
            try:
                body = self.service.composer.interpret(
                    request.message, safe_history, timeout_seconds=1.5
                )
                model_candidate = Interpretation.model_validate(body)
                # Explicit restrictions cannot be removed by a probabilistic classifier.
                if candidate.subject == SubjectReference.OTHER:
                    model_candidate = model_candidate.model_copy(
                        update={"subject": candidate.subject}
                    )
                if candidate.period != Period.UNSPECIFIED:
                    model_candidate = model_candidate.model_copy(
                        update={"period": candidate.period}
                    )
                candidate = model_candidate
            except Exception:
                pass  # No tool calls on ambiguous model failure.
        capabilities, notice = boundary(candidate, request.message, request.subject.role.value)
        if candidate.intent == Intent.UNCLEAR and safe:
            repeated = 0
            for item in request.conversation_context:
                try:
                    turn = json.loads(item)
                    if turn.get("sender") == "AI" and "어떤 내용을 확인할까요?" in turn.get(
                        "content", ""
                    ):
                        repeated += 1
                except (ValueError, AttributeError):
                    continue
            if repeated >= 2:
                notice = (
                    "예를 들어 “오늘 배송 상태 알려줘”처럼 말씀해 주세요. "
                    "계속 설명하기 어려우시면 상단의 상담사 연결을 이용해 주세요."
                )
        if not safe:
            capabilities = ()
            notice = (
                "요청하신 지시는 따를 수 없어요. "
                "본인의 배송, 결제, 환불, 구독에 관한 질문을 남겨 주세요."
            )
        route = route_for(candidate, notice)
        scopes = frozenset(
            {"customer-ai.policy.read"} | {CAPABILITY_SCOPES[c] for c in capabilities}
        )
        plan = Plan(
            fingerprint(request),
            start + 8.0,
            capabilities,
            route,
            notice,
            scopes,
            candidate.intent if safe else Intent.OUT_OF_SCOPE,
        )
        plan_id = str(uuid4())
        with self._lock:
            self._plans = {k: v for k, v in self._plans.items() if v.expires > self.clock()}
            if len(self._plans) >= 1024:
                raise ConsultationRequestError("Plan capacity reached.", status_code=503)
            self._plans[plan_id] = plan
        return {
            "schemaVersion": "1.0",
            "requestId": str(request.request_id),
            "planId": plan_id,
            "route": route.value,
            "capabilities": [c.value for c in capabilities],
        }

    def execute(self, plan_id, request, context, key):
        self.service._validate_request_context(request, context)
        with self._lock:
            plan = self._plans.get(str(plan_id))
        if plan is None or plan.expires <= self.clock() or plan.fingerprint != fingerprint(request):
            raise ConsultationRequestError("Invalid or expired consultation plan.", status_code=409)
        if context.subject.allowed_ai_scopes != plan.scopes:
            raise ConsultationRequestError("Plan scope mismatch.", status_code=403)
        if plan.intent == Intent.HANDOFF:
            return self.service._handoff(request.request_id, plan.route)
        if plan.notice:
            conversational = plan.intent in {Intent.SMALL_TALK, Intent.CORRECTION, Intent.COMPLAINT}
            if conversational:
                if not isinstance(key, str) or not key.strip() or len(key.strip()) > 200:
                    raise ConsultationRequestError("A valid Idempotency-Key is required.")
                return self.service.registry.execute_once(
                    key.strip(),
                    self.service._fingerprint(request),
                    lambda: self._conversation_response(plan, request),
                )
            return ConsultationResponse(
                schema_version="1.0",
                request_id=request.request_id,
                decision="ANSWER" if conversational else "DEGRADED",
                answer=plan.notice,
                route="UNSUPPORTED",
                degraded=not conversational,
                handoff_required=False,
            )
        service = replace(
            self.service,
            route_resolver=FixedRoute(plan.route),
            capability_resolver=FixedCapabilities(plan.capabilities),
            request_deadline_seconds=max(0.001, plan.expires - self.clock()),
        )
        return service.respond(request, context, idempotency_key=key)

    def _conversation_response(self, plan, request):
        answer = plan.notice
        try:
            draft = self.service.composer.converse(
                request.message,
                plan.intent.value,
                plan.notice,
                timeout_seconds=min(1.5, max(0.001, plan.expires - self.clock())),
            )
            if (
                isinstance(draft, str)
                and 0 < len(draft) <= 300
                and self.service.guardrails.dialogue_output_is_safe(draft)
            ):
                answer = draft
        except Exception:
            pass  # A bounded, useful fallback keeps the conversation available.
        return ConsultationResponse(
            schema_version="1.0",
            request_id=request.request_id,
            decision="ANSWER",
            answer=answer,
            route="UNSUPPORTED",
            degraded=False,
            handoff_required=False,
        )
