"""Tool-free interpretation and deterministic capability boundary checks."""

import json
import re
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field

from chapchap_customer_ai.consultation.models import Capability
from chapchap_customer_ai.contracts.models import ConsultationRoute


class Intent(StrEnum):
    SMALL_TALK = "SMALL_TALK"
    POLICY = "POLICY"
    STATE = "STATE"
    POLICY_AND_STATE = "POLICY_AND_STATE"
    ACTION_REQUEST = "ACTION_REQUEST"
    UNCLEAR = "UNCLEAR"
    OUT_OF_SCOPE = "OUT_OF_SCOPE"


class Topic(StrEnum):
    PAYMENT = "PAYMENT"
    REFUND = "REFUND"
    SUBSCRIPTION = "SUBSCRIPTION"
    DELIVERY = "DELIVERY"


class Period(StrEnum):
    CURRENT = "CURRENT"
    TODAY = "TODAY"
    TOMORROW = "TOMORROW"
    EXPLICIT_DATE = "EXPLICIT_DATE"
    HISTORY = "HISTORY"
    UNSPECIFIED = "UNSPECIFIED"


class Detail(StrEnum):
    STATUS = "STATUS"
    IN_PROGRESS_EXISTENCE = "IN_PROGRESS_EXISTENCE"
    ETA = "ETA"
    LIST = "LIST"
    AMOUNT = "AMOUNT"
    PROCEDURE = "PROCEDURE"
    OTHER = "OTHER"


class SubjectReference(StrEnum):
    SELF = "SELF"
    OTHER = "OTHER"
    UNCLEAR = "UNCLEAR"


class Interpretation(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
    intent: Intent
    topics: list[Topic] = Field(max_length=4)
    period: Period
    detail: Detail
    subject: SubjectReference


TOPICS = {
    Topic.PAYMENT: ("결제", "payment"),
    Topic.REFUND: ("환불", "refund"),
    Topic.SUBSCRIPTION: ("구독", "subscription"),
    Topic.DELIVERY: ("배송", "배달", "delivery"),
}
CAPABILITIES = {
    Topic.PAYMENT: Capability.PAYMENT_CURRENT,
    Topic.REFUND: Capability.REFUND_RECENT,
    Topic.SUBSCRIPTION: Capability.SUBSCRIPTION_CURRENT,
    Topic.DELIVERY: Capability.DELIVERY_CURRENT,
}


def explicit_topics(text):
    return [topic for topic, words in TOPICS.items() if any(word in text for word in words)]


def customer_context(context):
    """Only server-serialized customer/rider turns establish a previous topic."""
    turns = []
    for text in context:
        try:
            item = json.loads(text)
            if (
                isinstance(item, dict)
                and item.get("sender") == "USER"
                and isinstance(item.get("sequence"), int)
                and isinstance(item.get("content"), str)
            ):
                turns.append(item)
        except (ValueError, TypeError):
            continue
    return turns


def interpret_rules(message, context):
    text = message.casefold().strip()
    compact = re.sub(r"\s+", "", text)
    topics = explicit_topics(text)
    followup = bool(re.search(r"그럼|그건|그거|지금은|내꺼|내거|언제|어디|내일은|어제는", text))
    inherited_period = Period.UNSPECIFIED
    inherited_subject = SubjectReference.SELF
    if not topics and followup:
        for item in customer_context(context):
            previous = item["content"].casefold()
            found = explicit_topics(previous)
            if found:
                topics = found if len(found) == 1 else []
                inherited_period = detect_period(previous)
                inherited_subject = detect_subject(previous)
            elif topics and detect_period(previous) != Period.UNSPECIFIED:
                inherited_period = detect_period(previous)
    period = detect_period(text)
    if period == Period.UNSPECIFIED and followup:
        period = inherited_period
    subject = detect_subject(text)
    if not explicit_topics(text) and followup and subject == SubjectReference.SELF:
        subject = inherited_subject
    detail = Detail.STATUS
    if re.search(r"몇\s*시|언제.*(와|오|도착)|도착.*(예정|시간)|\beta\b", text) or (
        Topic.DELIVERY in topics and "언제" in text
    ):
        detail = Detail.ETA
    elif re.search(r"목록|몇\s*건|전부|전체\s*(내역|이력)|모든", text):
        detail = Detail.LIST
    elif re.search(r"금액|얼마", text):
        detail = Detail.AMOUNT
    elif re.search(r"중.*있|오고\s*있", text):
        detail = Detail.IN_PROGRESS_EXISTENCE
    action = re.search(
        r"(환불|취소|해지|변경|결제)(해\s*줘|해\s*주|해요|해주세요|해\s*주세요)", text
    )
    policy = re.search(r"방법|규정|정책|수수료|조건|기준|어떻게|가능", text)
    state = re.search(
        r"상태|결과|지금|현재|최근|됐|되었|중|있어|확인|안\s*와|안\s*왔|늦|언제|어디|얼마", text
    )
    if compact.strip("!?.~") in {"안녕", "안녕하세요", "hi", "hello", "고마워", "감사합니다"}:
        intent = Intent.SMALL_TALK
    elif action:
        intent = Intent.ACTION_REQUEST
    elif topics and policy:
        intent = (
            Intent.POLICY_AND_STATE if state and re.search(r"내|나의|본인", text) else Intent.POLICY
        )
    elif topics and (state or followup):
        intent = Intent.STATE
    else:
        intent = Intent.UNCLEAR
    return Interpretation(
        intent=intent, topics=topics, period=period, detail=detail, subject=subject
    )


def detect_period(text):
    if re.search(r"내일|모레|다음\s*(주|달)|tomorrow", text):
        return Period.TOMORROW
    if re.search(r"어제|그제|지난|과거|이력|history", text):
        return Period.HISTORY
    if re.search(r"\d{1,4}[./-]\d{1,2}|\d+\s*[월일]", text):
        return Period.EXPLICIT_DATE
    if "오늘" in text:
        return Period.TODAY
    if re.search(r"지금|현재", text):
        return Period.CURRENT
    return Period.UNSPECIFIED


def detect_subject(text):
    if re.search(
        r"user\s*id\s*[:=]|다른\s*(사람|고객|사용자)|친구|타인|남의|그\s*사람|엄마|아빠|가족", text
    ):
        return SubjectReference.OTHER
    return SubjectReference.SELF


def boundary(candidate, message, role):
    """Return only server-owned routing, scopes and fixed safe notices."""
    if candidate.subject != SubjectReference.SELF:
        return (), "다른 고객의 정보는 조회할 수 없어요. 본인 정보에 관한 질문을 남겨 주세요."
    if candidate.intent == Intent.ACTION_REQUEST:
        return (), "이 채팅에서는 취소나 환불을 직접 처리할 수 없어요. 상담사 연결을 이용해 주세요."
    if candidate.intent == Intent.SMALL_TALK:
        return (), "안녕하세요! 배송, 결제, 환불, 구독 중 궁금한 내용을 말씀해 주세요."
    if candidate.intent in {Intent.UNCLEAR, Intent.OUT_OF_SCOPE} or not candidate.topics:
        return (), "어떤 내용을 확인할까요? 배송, 결제, 환불, 구독 중 하나를 알려주세요."
    if len(set(candidate.topics)) != len(candidate.topics) or len(candidate.topics) > 2:
        return (), "한 번에 두 가지까지 확인할 수 있어요. 먼저 확인할 항목을 골라 주세요."
    if candidate.intent in {Intent.STATE, Intent.POLICY_AND_STATE}:
        if candidate.period == Period.TODAY and any(t != Topic.DELIVERY for t in candidate.topics):
            return (), (
                "현재는 최근 결제·환불과 현재 구독 상태를 조회해요. "
                "특정 날짜의 내역은 조회할 수 없어요."
            )
        if candidate.period in {Period.TOMORROW, Period.EXPLICIT_DATE, Period.HISTORY}:
            return (
                (),
                "현재는 최근 결제·환불, 현재 구독, 오늘 배송 상태만 조회할 수 있어요. "
                "요청하신 기간의 정보는 확인할 수 없어요.",
            )
        if candidate.detail == Detail.ETA:
            return (
                (),
                "현재 이 채팅에서는 정확한 도착 예정 시각을 확인할 수 없어요. "
                "오늘 배송 상태는 확인해 드릴 수 있어요.",
            )
        if candidate.detail == Detail.LIST:
            return (), "현재는 대표 상태만 확인할 수 있어요. 전체 목록이나 건수는 조회할 수 없어요."
        if role == "RIDER" and Topic.DELIVERY in candidate.topics:
            return (), "이 계정에서는 고객 배송 상태를 조회할 수 없어요."
        return tuple(CAPABILITIES[topic] for topic in candidate.topics), None
    return (), None


def route_for(candidate, notice):
    if notice:
        return ConsultationRoute.UNSUPPORTED
    return {
        Intent.STATE: ConsultationRoute.USER_STATE,
        Intent.POLICY: ConsultationRoute.POLICY,
        Intent.POLICY_AND_STATE: ConsultationRoute.POLICY_AND_STATE,
    }.get(candidate.intent, ConsultationRoute.UNSUPPORTED)
