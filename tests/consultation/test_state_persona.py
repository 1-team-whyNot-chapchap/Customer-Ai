import pytest

from chapchap_customer_ai.consultation.models import Capability, GroundedAnswerDraft, StateFact
from chapchap_customer_ai.current_state.normalization import ToolResultNormalizer
from tests.consultation.test_response_service import Dependencies, context, request


def subscription(status="CANCELED_BEFORE_START"):
    return ToolResultNormalizer().normalize(
        Capability.SUBSCRIPTION_CURRENT, {"availability": "AVAILABLE", "status": status}
    )


def respond(deps, message="내 구독 상태 알려줘"):
    req = request(message, ("subscription.status.read",))
    return deps.service().respond(req, context(req), idempotency_key="state-persona")


@pytest.mark.parametrize(
    "message,answer",
    [
        ("제가 지금 구독중인가요?", "현재 구독 중이 아니에요."),
        ("신청했던 구독은 어떻게 됐나요?", "신청하신 구독은 시작 전에 취소됐어요."),
    ],
)
def test_state_answer_uses_question_and_verified_meaning_in_composer(message, answer):
    from dataclasses import replace

    from chapchap_customer_ai.consultation.plans import FixedCapabilities, FixedRoute
    from chapchap_customer_ai.contracts.models import ConsultationRoute

    deps = Dependencies()
    deps.state.values = (subscription(),)
    received = []

    def compose(message, history, evidence, facts, **kwargs):
        received.append((message, evidence, facts))
        return GroundedAnswerDraft(answer, ())

    deps.composer.compose = compose
    service = replace(
        deps.service(),
        route_resolver=FixedRoute(ConsultationRoute.USER_STATE),
        capability_resolver=FixedCapabilities((Capability.SUBSCRIPTION_CURRENT,)),
    )
    req = request(message, ("subscription.status.read",))
    result = service.respond(req, context(req), idempotency_key="question")
    assert result.answer == answer and result.decision == "ANSWER"
    assert received[0][0] == message and received[0][1] == ()
    values = dict(received[0][2][0].values)
    assert values["status"] == "CANCELED_BEFORE_START"
    assert "현재 구독 이용 중이 아닌" in values["statusMeaning"]


@pytest.mark.parametrize(
    "failure",
    [
        TimeoutError(),
        GroundedAnswerDraft("허위 인용", ("made-up",)),
        GroundedAnswerDraft("Authorization: Bearer secret", ()),
    ],
)
def test_generation_failure_retains_verified_fallback(failure):
    deps = Dependencies()
    fact = subscription()
    deps.state.values = (fact,)
    if isinstance(failure, Exception):
        deps.composer.error = failure
    else:
        deps.composer.draft = failure
    result = respond(deps)
    assert result.answer == fact.safe_answer and not result.handoff_required


def test_not_found_can_be_worded_by_model_but_timeout_cannot_become_absence():
    deps = Dependencies()
    deps.state.values = (StateFact(Capability.SUBSCRIPTION_CURRENT, "NOT_FOUND"),)
    deps.composer.draft = GroundedAnswerDraft("조회 가능한 구독 정보가 없어요.", ())
    assert respond(deps).answer == "조회 가능한 구독 정보가 없어요."
    assert deps.composer.calls == 1
    deps = Dependencies()
    deps.state.values = (StateFact(Capability.SUBSCRIPTION_CURRENT, "TIMEOUT"),)
    result = respond(deps)
    assert result.handoff_required and deps.composer.calls == 0
