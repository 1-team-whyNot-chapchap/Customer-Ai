from collections.abc import Mapping

from pydantic import ValidationError

from chapchap_customer_ai.consultation.models import (
    Capability,
    StateAvailability,
    StateErrorCode,
    StateFact,
)
from chapchap_customer_ai.current_state.contracts import (
    CurrentDeliveryState,
    CurrentPaymentState,
    CurrentSubscriptionState,
    RecentRefundResult,
)


class ToolResultNormalizer:
    def normalize(self, capability: Capability, payload: Mapping[str, object]) -> StateFact:
        try:
            if capability == Capability.PAYMENT_CURRENT:
                return self._payment(CurrentPaymentState.model_validate(payload))
            if capability == Capability.REFUND_RECENT:
                return self._refund(RecentRefundResult.model_validate(payload))
            if capability == Capability.SUBSCRIPTION_CURRENT:
                return self._subscription(CurrentSubscriptionState.model_validate(payload))
            if capability == Capability.DELIVERY_CURRENT:
                return self._delivery(CurrentDeliveryState.model_validate(payload))
        except (ValidationError, TypeError, ValueError):
            return self.contract_error(capability)
        return self.contract_error(capability)

    @staticmethod
    def contract_error(capability: Capability) -> StateFact:
        return StateFact(capability, None, error_code=StateErrorCode.CONTRACT_ERROR)

    @staticmethod
    def _payment(value: CurrentPaymentState) -> StateFact:
        occurred_at = value.occurred_at.isoformat()
        return StateFact(
            Capability.PAYMENT_CURRENT,
            StateAvailability.AVAILABLE,
            (
                f"최근 결제 상태는 {value.status}이며 결제 유형은 {value.payment_type}, "
                f"금액은 {value.amount}원, 발생 시각은 {occurred_at}입니다."
            ),
            (
                ("status", value.status.value),
                ("paymentType", value.payment_type.value),
                ("amount", value.amount),
                ("occurredAt", occurred_at),
            ),
        )

    @staticmethod
    def _refund(value: RecentRefundResult) -> StateFact:
        requested_at = value.requested_at.isoformat()
        completed_at = value.completed_at.isoformat() if value.completed_at else None
        return StateFact(
            Capability.REFUND_RECENT,
            StateAvailability.AVAILABLE,
            (
                f"최근 환불 상태는 {value.status}이며 요청 금액은 {value.requested_amount}원, "
                f"환불 금액은 {value.refunded_amount}원, 미처리 금액은 "
                f"{value.unprocessed_amount}원입니다."
            ),
            (
                ("status", value.status.value),
                ("refundType", value.refund_type),
                ("requestedAmount", value.requested_amount),
                ("refundedAmount", value.refunded_amount),
                ("unprocessedAmount", value.unprocessed_amount),
                ("requestedAt", requested_at),
                ("completedAt", completed_at),
            ),
        )

    @staticmethod
    def _subscription(value: CurrentSubscriptionState) -> StateFact:
        return StateFact(
            Capability.SUBSCRIPTION_CURRENT,
            StateAvailability.AVAILABLE,
            f"현재 구독 상태는 {value.status}입니다.",
            (("status", value.status.value),),
        )

    @staticmethod
    def _delivery(value: CurrentDeliveryState) -> StateFact:
        changed_at = value.status_changed_at.isoformat() if value.status_changed_at else None
        time_text = f" 상태 변경 시각은 {changed_at}입니다." if changed_at else ""
        return StateFact(
            Capability.DELIVERY_CURRENT,
            StateAvailability.AVAILABLE,
            f"오늘 배송 상태는 {value.status}, 지연 상태는 {value.delay_status}입니다.{time_text}",
            (
                ("status", value.status.value),
                ("delayStatus", value.delay_status.value),
                ("statusChangedAt", changed_at),
            ),
        )
