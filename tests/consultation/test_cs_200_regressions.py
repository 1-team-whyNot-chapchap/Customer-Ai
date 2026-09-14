import json
from pathlib import Path

from chapchap_customer_ai.consultation.guardrails import ConsultationGuardrails
from chapchap_customer_ai.consultation.plans import ConsultationPlans
from tests.consultation.model_fixtures import interpretation
from tests.consultation.test_conversation_quality import execute
from tests.consultation.test_response_service import Dependencies


def test_evaluation_contains_200_distinct_questions_in_ten_groups():
    cases = json.loads(
        (Path(__file__).parents[1] / "fixtures/cs_200_questions.json").read_text(encoding="utf-8")
    )
    assert len(cases) == len({c["question"] for c in cases}) == 200
    assert len({c["group"] for c in cases}) == 10
    assert all(
        len([c for c in cases if c["group"] == group]) == 20
        for group in {c["group"] for c in cases}
    )


def test_unknown_destination_never_promises_a_nonexistent_link():
    deps = Dependencies()
    deps.composer.interpret = lambda *a, **kw: {
        **interpretation("NAVIGATION", ()),
        "destination": None,
    }
    calls = []
    deps.composer.converse = lambda *a, **kw: calls.append(1) or "아래 링크를 눌러 주세요."
    _, result = execute(ConsultationPlans(deps.service()), "지원하지 않는 기능의 페이지 알려줘")
    assert not calls and "링크" not in result.answer and not result.handoff_required


def test_general_policy_without_private_topic_can_retrieve_approved_knowledge():
    deps = Dependencies()
    deps.composer.interpret = lambda *a, **kw: interpretation("POLICY", ())
    _, result = execute(ConsultationPlans(deps.service()), "회원 탈퇴 개인정보 처리 정책은?")
    assert deps.retriever.calls == 1 and deps.state.calls == 0
    assert result.evidence and not result.handoff_required


def test_feedback_fallback_does_not_repeat_handoff_recommendation():
    deps = Dependencies()
    deps.composer.interpret = lambda *a, **kw: interpretation("COMPLAINT", ())
    _, result = execute(ConsultationPlans(deps.service()), "왜 자꾸 상담사 연결하래?")
    assert "상담사 연결" not in result.answer and not result.handoff_required


def test_resolved_state_does_not_request_another_service_as_lookup_key():
    guard = ConsultationGuardrails()
    assert not guard.state_output_is_safe(
        "신청한 서비스명이나 상품을 알려주시면 다시 확인해 드릴게요."
    )
    assert not guard.state_output_is_safe("어떤 서비스를 말씀하시는 걸까요?")
    assert guard.state_output_is_safe("현재 구독 중이 아니에요.")


def test_interpretation_budget_does_not_extend_total_plan_lifetime():
    deps = Dependencies()
    now = [100.0]
    observed = []

    def interpret(*args, timeout_seconds):
        observed.append(timeout_seconds)
        now[0] += 2.0
        return interpretation("SMALL_TALK", ())

    deps.composer.interpret = interpret
    plans = ConsultationPlans(deps.service(), clock=lambda: now[0])
    execute(plans, "안녕하세요")
    assert observed == [2.5]
    # Execution consumes the plan. Capture a second prepared plan to inspect
    # its absolute deadline, which must still include interpretation time.
    from tests.consultation.test_boundaries import POLICY
    from tests.consultation.test_response_service import context, request

    req = request("안녕하세요", POLICY)
    started = now[0]
    prepared = plans.prepare(req, context(req))
    assert plans._plans[prepared["planId"]].expires == started + 8.0


def test_policy_rejects_unperformed_lookup_and_handoff_promises():
    from chapchap_customer_ai.consultation.models import GroundedAnswerDraft

    for answer in (
        "상담사 연결을 도와드릴게요.",
        "상담사에게 연결해 드리겠습니다.",
        "조회된 결제 건이 없어서 확인할 수 없어요.",
    ):
        deps = Dependencies()
        deps.composer.interpret = lambda *a, **kw: interpretation("POLICY", ())
        deps.composer.compose = lambda *a, **kw: GroundedAnswerDraft(answer, ("chunk-1",))
        _, result = execute(ConsultationPlans(deps.service()), "환불 절차는 어떻게 돼요?")
        assert result.degraded and not result.handoff_required
        assert result.answer != answer and deps.state.calls == 0
    assert ConsultationGuardrails().policy_output_is_safe(
        "확인이 필요하시면 상담사 연결 버튼을 이용해 주세요."
    )
