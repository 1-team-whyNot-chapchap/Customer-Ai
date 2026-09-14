from dataclasses import replace

import pytest

from chapchap_customer_ai.consultation.models import Capability, GroundedAnswerDraft, StateFact
from chapchap_customer_ai.consultation.navigation import PAGES, Destination
from chapchap_customer_ai.consultation.plans import ConsultationPlans
from chapchap_customer_ai.contracts.models import UserRole
from tests.consultation.model_fixtures import interpretation
from tests.consultation.test_conversation_quality import execute, turn
from tests.consultation.test_response_service import Dependencies, context, request


def decision(intent, destination=None):
    return {**interpretation(intent, ("SUBSCRIPTION",)), "destination": destination}


@pytest.mark.parametrize("destination", list(Destination))
def test_navigation_returns_only_approved_page_without_business_reads(destination):
    deps = Dependencies()
    deps.composer.interpret = lambda *a, **kw: decision("NAVIGATION", destination)
    deps.composer.converse = lambda *a, **kw: "아래 페이지에서 확인해 주세요."
    plan, result = execute(ConsultationPlans(deps.service()), "어디로 가면 돼요?")
    assert result.answer.endswith(PAGES[destination].link)
    assert result.decision == "ANSWER" and not result.handoff_required
    assert plan["capabilities"] == []
    assert deps.state.calls == deps.retriever.calls == deps.versions.calls == 0


@pytest.mark.parametrize(
    "draft", ["[신청](https://evil.test)", "javascript:alert(1)", "결제 완료했어요."]
)
def test_generated_link_or_action_claim_is_replaced_by_approved_guidance(draft):
    deps = Dependencies()
    deps.composer.interpret = lambda *a, **kw: decision("NAVIGATION", "SUBSCRIBE")
    deps.composer.converse = lambda *a, **kw: draft
    _, result = execute(ConsultationPlans(deps.service()), "구독하려면 어디로 가?")
    page = PAGES[Destination.SUBSCRIBE]
    assert result.answer == page.guidance + "\n\n" + page.link


@pytest.mark.parametrize("destination", [None, "/admin", "https://evil.test"])
def test_missing_or_invalid_destination_never_creates_a_link(destination):
    deps = Dependencies()
    deps.composer.interpret = lambda *a, **kw: decision("NAVIGATION", destination)
    _, result = execute(ConsultationPlans(deps.service()), "어디로 가?")
    assert "](" not in result.answer and not result.handoff_required
    assert deps.state.calls == 0


def test_rider_cannot_receive_customer_navigation():
    deps = Dependencies()
    deps.composer.interpret = lambda *a, **kw: decision("NAVIGATION", "SUBSCRIBE")
    req = request("구독 신청", ("customer-ai.policy.read",))
    req = req.model_copy(
        update={"subject": req.subject.model_copy(update={"role": UserRole.RIDER})}
    )
    auth = context(req)
    auth = replace(auth, subject=replace(auth.subject, role=UserRole.RIDER))
    plans = ConsultationPlans(deps.service())
    plan = plans.prepare(req, auth)
    result = plans.execute(plan["planId"], req, auth, "rider-nav")
    assert "](" not in result.answer and "고객 계정" in result.answer


def test_handoff_information_does_not_deny_explicit_chat_handoff():
    deps = Dependencies()
    deps.composer.interpret = lambda *a, **kw: decision("HANDOFF_INFO")
    denial = "제가 대신 연결해 드리는 건 아니고 직접 눌러주셔야 합니다."
    deps.composer.converse = lambda *a, **kw: denial
    _, result = execute(ConsultationPlans(deps.service()), "상담사 연결은 어떻게 해?")
    assert result.answer == "상단의 상담사 연결 버튼을 누르시면 상담사에게 상담을 요청할 수 있어요."
    assert not result.handoff_required


def test_new_user_then_application_navigation_keeps_conversation_open():
    deps = Dependencies()
    deps.state.values = (StateFact(Capability.SUBSCRIPTION_CURRENT, "NOT_FOUND"),)
    deps.composer.draft = GroundedAnswerDraft("조회되는 구독 정보가 없어요.", ())
    deps.composer.interpret = lambda *a, **kw: interpretation("STATE", ("SUBSCRIPTION",))
    plans = ConsultationPlans(deps.service())
    _, first = execute(plans, "저 지금 구독 중인가요?")
    assert first.answer == "조회되는 구독 정보가 없어요."
    deps.composer.interpret = lambda *a, **kw: decision("NAVIGATION", "SUBSCRIBE")
    _, second = execute(plans, "처음인데 어디서 신청해?", [turn(1, first.answer, "AI")])
    assert second.answer.endswith(PAGES[Destination.SUBSCRIBE].link)
    assert deps.state.calls == 1 and not second.handoff_required


def test_dispute_does_not_repeat_or_requery_record_and_can_change_topic():
    deps = Dependencies()
    deps.composer.interpret = lambda *a, **kw: decision("STATE_DISPUTE")
    deps.composer.converse = lambda *a, **kw: "고객님이 구독 취소했어요."
    plans = ConsultationPlans(deps.service())
    history = [turn(1, "현재 구독은 시작 전에 취소됐어요.", "AI")]
    _, dispute = execute(plans, "구독한 적이 없는데 어떻게 취소야?", history)
    assert "경위" in dispute.answer and "시작 전 취소" not in dispute.answer
    assert not dispute.handoff_required and deps.state.calls == 0
    deps.composer.interpret = lambda *a, **kw: decision("NAVIGATION", "SUBSCRIBE")
    _, navigation = execute(
        plans, "그럼 신청은 어디로 가?", history + [turn(2, dispute.answer, "AI")]
    )
    assert navigation.answer.endswith(PAGES[Destination.SUBSCRIBE].link)
    assert deps.state.calls == deps.retriever.calls == 0
