from dataclasses import dataclass

from chapchap_customer_ai.consultation.models import Capability
from chapchap_customer_ai.consultation.ports import AmbiguousRouteClassifier
from chapchap_customer_ai.contracts.models import ConsultationRoute


@dataclass(frozen=True, slots=True)
class RuleBasedRouteResolver:
    classifier: AmbiguousRouteClassifier | None = None

    _policy_terms = frozenset(
        {"정책", "규정", "기간", "조건", "수수료", "기준", "방법", "가능", "faq"}
    )
    _state_terms = frozenset(
        {"상태", "결과", "진행", "완료", "실패", "최근", "현재", "언제", "어디"}
    )
    _personal_terms = frozenset({"내", "제", "나의", "제가", "나는", "본인"})
    _customer_terms = frozenset(
        {"결제", "환불", "구독", "배송", "해지", "취소", "주문", "챱챱",
         "프로필", "로그인", "회원가입", "배송지", "플랜", "메뉴"}
    )

    def resolve(self, message: str, *, timeout_seconds: float = 0.5) -> ConsultationRoute:
        normalized = message.casefold()
        has_policy = self._contains(normalized, self._policy_terms)
        has_state = self._contains(normalized, self._state_terms) and (
            self._contains(normalized, self._personal_terms)
            or self._contains(normalized, self._customer_terms)
        )
        if has_policy and has_state:
            return ConsultationRoute.POLICY_AND_STATE
        if has_state:
            return ConsultationRoute.USER_STATE
        if has_policy:
            return ConsultationRoute.POLICY
        if normalized.strip(" !?.~\n\t") in self._customer_terms:
            return ConsultationRoute.UNSUPPORTED
        if self._contains(normalized, self._customer_terms) and self.classifier is not None:
            try:
                return ConsultationRoute(
                    self.classifier.classify(message, timeout_seconds=timeout_seconds)
                )
            except ValueError:
                return ConsultationRoute.UNSUPPORTED
        if self._contains(normalized, self._customer_terms):
            return ConsultationRoute.POLICY
        return ConsultationRoute.UNSUPPORTED

    @classmethod
    def clarification(cls, message: str) -> str | None:
        text = message.casefold().strip(" !?.~\n\t")
        if text in {"안녕", "안녕하세요", "안녕하세요오", "반가워", "반갑습니다", "hello", "hi"}:
            return "안녕하세요! 챱챱 상담 도우미예요. 배송, 구독, 결제 등 어떤 도움이 필요하신가요?"
        if text in cls._customer_terms:
            return f"{text} 관련해서 어떤 점이 궁금하신가요? 확인하고 싶은 내용이나 겪고 있는 상황을 조금 더 자세히 알려주세요."
        return None

    @staticmethod
    def _contains(message: str, terms: frozenset[str]) -> bool:
        return any(term in message for term in terms)


class CapabilityResolver:
    _terms: tuple[tuple[Capability, tuple[str, ...]], ...] = (
        (Capability.PAYMENT_CURRENT, ("결제", "payment")),
        (Capability.REFUND_RECENT, ("환불", "refund")),
        (Capability.SUBSCRIPTION_CURRENT, ("구독", "subscription")),
        (Capability.DELIVERY_CURRENT, ("배송", "delivery")),
    )

    def resolve(self, message: str) -> tuple[Capability, ...]:
        normalized = message.casefold()
        capabilities = tuple(
            capability
            for capability, terms in self._terms
            if any(term in normalized for term in terms)
        )
        return capabilities
