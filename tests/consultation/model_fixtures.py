"""Canned model outputs for runtime tests, not a substitute semantic classifier."""


def interpretation(
    intent="STATE", topics=("DELIVERY",), period="UNSPECIFIED", detail="STATUS", subject="SELF"
):
    return dict(intent=intent, topics=list(topics), period=period, detail=detail, subject=subject)


def canned_interpret(message, history, **kwargs):
    values = {
        "다른 고객 배송 상태 알려줘": interpretation(subject="OTHER"),
        "다른고객정보 조회 안했는데": interpretation("CORRECTION", ()),
        "밥은먹었어?": interpretation("SMALL_TALK", ()),
        "밥은 먹었어?": interpretation("SMALL_TALK", ()),
        "내 배송 상태 알려줘": interpretation(),
        "고마워": interpretation("SMALL_TALK", ()),
        "상담사 연결해줘": interpretation("HANDOFF", ()),
        "상담사 연결은 어떻게 하나요?": interpretation("SMALL_TALK", ()),
    }
    return values.get(message, interpretation("UNCLEAR", (), subject="UNCLEAR"))
