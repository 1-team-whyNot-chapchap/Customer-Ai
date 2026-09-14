"""Tool-free interpretation and deterministic capability boundary checks."""

import json
import re
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field

from chapchap_customer_ai.consultation.models import Capability
from chapchap_customer_ai.consultation.navigation import PAGES, Destination
from chapchap_customer_ai.contracts.models import ConsultationRoute


class Intent(StrEnum):
    NAVIGATION = "NAVIGATION"
    STATE_DISPUTE = "STATE_DISPUTE"
    SMALL_TALK = "SMALL_TALK"
    CORRECTION = "CORRECTION"
    COMPLAINT = "COMPLAINT"
    HANDOFF = "HANDOFF"
    HANDOFF_INFO = "HANDOFF_INFO"
    CONTINUE_CHAT = "CONTINUE_CHAT"
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
    destination: Destination | None = None


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
    return sorted(turns, key=lambda turn: turn["sequence"])


def is_followup(text):
    return bool(re.search(r"그럼|그건|그거|지금은|내꺼|내거|언제|어디|내일은|어제는", text))


def active_context(context):
    """An unrelated customer turn ends the implicit topic, including a refused topic."""
    turns = customer_context(context)
    start = 0
    for turn in turns:
        text = turn["content"].casefold()
        if not explicit_topics(text) and not is_followup(text):
            start = turn["sequence"]
        elif is_correction(text):
            start = turn["sequence"]
    if not start:
        return tuple(context)
    kept = []
    for raw in context:
        try:
            turn = json.loads(raw)
            if isinstance(turn, dict) and turn.get("sequence", 0) >= start:
                kept.append(raw)
        except (ValueError, TypeError):
            continue
    return tuple(kept)


def is_correction(text):
    # A denial alone is feedback, never permission for a lookup. A new positive
    # request in the same utterance must still be classified and authorized.
    denial = re.search(
        r"안\s*(했|물었|요청했)|(?:조회|요청|질문).*(?:않았|아닌데)|그런\s*뜻|오해", text
    )
    positive = re.search(r"알려\s*줘|보여\s*줘|조회해|확인해|상태.*(?:알려|보여|확인)", text)
    return bool(denial and not positive)


def interpret_rules(message, context):
    """Legacy rule interpreter; the active two-phase runtime uses the LLM instead."""
    text = message.casefold().strip()
    compact = re.sub(r"\s+", "", text)
    topics = explicit_topics(text)
    followup = is_followup(text)
    inherited_period = Period.UNSPECIFIED
    inherited_subject = SubjectReference.SELF
    if not topics and followup:
        for item in customer_context(active_context(context)):
            previous = item["content"].casefold()
            if is_correction(previous):
                topics = []
                inherited_period = Period.UNSPECIFIED
                inherited_subject = SubjectReference.SELF
                continue
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
    if (
        not explicit_topics(text)
        and followup
        and subject == SubjectReference.SELF
        and not re.search(r"내\s*(꺼|거|것)|본인|나의", text)
    ):
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
        r"(환불|취소|해지|변경|결제)\s*(해\s*줘|해\s*주|해요|해주세요|해\s*주세요)", text
    )
    policy = re.search(r"방법|규정|정책|수수료|조건|기준|어떻게|가능", text)
    state = re.search(
        r"상태|결과|지금|현재|최근|됐|되었|중|있어|확인|안\s*와|안\s*왔|늦|언제|어디|얼마", text
    )
    handoff = re.search(r"상담\s*사|사람|직원|상담\s*원", text) and re.search(
        r"연결|상담하고|바꿔|대화하고", text
    )
    negative_handoff = re.search(r"하지\s*마|말아|안\s*(해|할)|필요\s*없|원하지", text)
    handoff_information = handoff and re.search(r"방법|어떻게|하면|기능", text)
    if handoff and not negative_handoff and not handoff_information:
        intent = Intent.HANDOFF
    elif is_correction(text):
        intent = Intent.CORRECTION
    elif not topics and re.search(r"답답|같은\s*(말|답)|말귀|이해.*못|왜.*반복", text):
        intent = Intent.COMPLAINT
    elif not topics and (
        compact.strip("!?.~") in {"안녕", "안녕하세요", "hi", "hello", "고마워", "감사합니다"}
        or re.search(r"(?:밥|식사).*(?:먹|했|하셨)|고마워|감사해|너.*누구|잘\s*자", text)
        or (handoff and (negative_handoff or handoff_information))
    ):
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
    # Only an explicit contrast followed by a self reference cancels the earlier
    # other-person reference. A later OTHER reference remains restricted.
    contrast = re.search(r"(?:말고|아니라)\s*(?:내|제|나의|본인)", text)
    if contrast:
        text = text[contrast.start() :]
    if re.search(
        r"user\s*id\s*[:=]|다른\s*(사람|고객|사용자)|친구|타인|남의|그\s*사람|엄마|아빠|가족", text
    ):
        return SubjectReference.OTHER
    return SubjectReference.SELF


def boundary(candidate, message, role):
    """Return only server-owned routing, scopes and fixed safe notices."""
    if candidate.intent == Intent.NAVIGATION:
        if role != "CUSTOMER":
            return (), "이 페이지는 고객 계정으로 이용할 수 있어요."
        page = PAGES.get(candidate.destination)
        return (), page.guidance if page else (
            "찾으시는 페이지의 위치를 확인하지 못했어요. 페이지 이름이나 하려는 일을 알려주세요."
        )
    if candidate.intent == Intent.STATE_DISPUTE:
        return (), (
            "말씀하신 내용과 앞서 안내된 기록이 달라 확인이 필요해요. "
            "지금 정보만으로는 기록이 생긴 경위를 확인할 수 없어요. "
            "확인을 요청하시려면 상단의 상담사 연결을 눌러 주세요."
        )
    if candidate.intent == Intent.HANDOFF:
        return (), None
    if candidate.intent == Intent.HANDOFF_INFO:
        return (), "상단의 상담사 연결 버튼을 누르시면 상담사에게 상담을 요청할 수 있어요."
    if candidate.intent == Intent.CONTINUE_CHAT:
        return (), "네, 이 채팅에서 계속 도와드릴게요. 궁금한 내용을 말씀해 주세요."
    if candidate.intent == Intent.CORRECTION:
        return (), "말씀을 잘못 이해했어요. 어떤 도움을 원하셨는지 다시 말씀해 주세요."
    if candidate.intent == Intent.COMPLAINT:
        return (
            (),
            "말씀해 주신 점을 반영해 질문에 맞춰 간결하게 안내할게요.",
        )
    if candidate.intent == Intent.ACTION_REQUEST:
        return (), (
            "이 채팅에서 요청하신 작업을 직접 실행할 수는 없어요. "
            "이용 방법은 안내해 드릴 수 있어요."
        )
    if candidate.intent == Intent.SMALL_TALK:
        return (), small_talk_answer(message)
    if candidate.intent == Intent.OUT_OF_SCOPE:
        return (), (
            "저는 챱챱 이용 문의를 도와드리고 있어요. "
            "서비스 이용에 관해 궁금한 점을 말씀해 주세요."
        )
    if candidate.intent == Intent.POLICY:
        return (), None
    if candidate.intent == Intent.UNCLEAR or not candidate.topics:
        return (), "어떤 내용을 확인할까요? 배송, 결제, 환불, 구독 중 하나를 알려주세요."
    if len(set(candidate.topics)) != len(candidate.topics) or len(candidate.topics) > 2:
        return (), "한 번에 두 가지까지 확인할 수 있어요. 먼저 확인할 항목을 골라 주세요."
    if candidate.intent in {Intent.STATE, Intent.POLICY_AND_STATE}:
        if candidate.subject == SubjectReference.OTHER:
            return (), "다른 고객의 정보는 조회할 수 없어요. 본인 정보에 관한 질문을 남겨 주세요."
        if candidate.subject == SubjectReference.UNCLEAR:
            return (), "본인의 이용 내역을 확인하시려는 건가요?"
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


def small_talk_answer(message):
    """Tool-free persona responses never imply a human experience or a business fact."""
    if re.search(r"밥|식사", message):
        return "저는 AI라 밥을 먹지는 않지만, 챙겨 물어봐 주셔서 고마워요! 식사는 하셨어요?"
    if re.search(r"고마|감사", message):
        return "도움이 됐다니 다행이에요. 더 궁금한 점이 있으면 편하게 말씀해 주세요."
    if re.search(r"하지\s*마|말아|필요\s*없|원하지", message):
        return "네, 이 채팅에서 계속 도와드릴게요. 궁금한 내용을 말씀해 주세요."
    if re.search(r"누구|이름|정체", message):
        return (
            "저는 챱챱 AI 상담 도우미예요. "
            "서비스 이용 안내와 본인의 현재 이용 상태 확인을 도와드려요."
        )
    if re.search(r"상담\s*사|상담\s*원", message) and re.search(r"방법|어떻게|하면|기능", message):
        return "상단의 상담사 연결 버튼을 누르시면 상담사에게 상담을 요청할 수 있어요."
    if re.search(r"잘\s*자|잘\s*가|안녕히", message):
        return "편안한 시간 보내세요. 필요하시면 언제든 다시 말씀해 주세요."
    if re.search(r"안녕|hello|\bhi\b", message, re.IGNORECASE):
        return "안녕하세요! 챱챱 AI 상담 도우미예요. 무엇을 도와드릴까요?"
    return "편하게 말씀해 주세요. 챱챱 이용 중 궁금한 점도 함께 도와드릴게요."


def route_for(candidate, notice):
    if notice:
        return ConsultationRoute.UNSUPPORTED
    return {
        Intent.STATE: ConsultationRoute.USER_STATE,
        Intent.POLICY: ConsultationRoute.POLICY,
        Intent.POLICY_AND_STATE: ConsultationRoute.POLICY_AND_STATE,
    }.get(candidate.intent, ConsultationRoute.UNSUPPORTED)
