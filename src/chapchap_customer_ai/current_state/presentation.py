"""Customer-facing labels; domain codes remain unchanged in internal facts."""

from datetime import datetime, timedelta, timezone

from chapchap_customer_ai.current_state.contracts import (
    DelayStatus,
    DeliveryStatus,
    PaymentStatus,
    PaymentType,
    RefundStatus,
    SubscriptionStatus,
)

PAYMENT_STATUS = {
    PaymentStatus.PROCESSING: "처리 중",
    PaymentStatus.SUCCESS: "완료",
    PaymentStatus.RETRY_WAITING: "재시도 대기 중",
    PaymentStatus.RETRY_STOPPED: "재시도 중단",
    PaymentStatus.FAILED: "실패",
}
PAYMENT_TYPE = {
    PaymentType.FIRST_SUBSCRIPTION_PAYMENT: "첫 구독 결제",
    PaymentType.REGULAR_PAYMENT: "정기 결제",
    PaymentType.SETTING_CHANGE_PAYMENT: "구독 설정 변경에 따른 추가 결제",
}
REFUND_STATUS = {
    RefundStatus.PENDING: "처리 대기 중",
    RefundStatus.COMPLETED: "완료",
    RefundStatus.FAILED: "실패",
    RefundStatus.REVIEW_REQUIRED: "추가 확인 필요",
}
REFUND_TYPE = {
    "SETTING_CHANGE_REDUCTION": "구독 설정 변경에 따른 차액 환불",
    "CANCELLATION_BEFORE_START": "구독 시작 전 취소에 따른 환불",
    "NEXT_PERIOD_FULL_CANCELLATION": "다음 구독 기간 취소에 따른 전액 환불",
    "DELIVERY_PARTIAL_CANCELLATION": "배송 취소에 따른 부분 환불",
}
SUBSCRIPTION_STATUS = {
    SubscriptionStatus.AWAITING_CONFIRMATION: "확정 대기 중",
    SubscriptionStatus.SCHEDULED: "시작 예정",
    SubscriptionStatus.IN_PROGRESS: "이용 중",
    SubscriptionStatus.CANCELLATION_SCHEDULED: "해지 예정",
    SubscriptionStatus.PAYMENT_FAILED: "결제 실패",
    SubscriptionStatus.CANCELED_BEFORE_START: "시작 전 취소",
    SubscriptionStatus.ENDED: "종료",
}
DELIVERY_STATUS = {
    DeliveryStatus.READY: "준비 중",
    DeliveryStatus.DELIVERING: "배송 중",
    DeliveryStatus.COMPLETED: "완료",
    DeliveryStatus.FAILED: "실패",
}
DELAY_STATUS = {
    DelayStatus.DELAYED: "배송 지연이 확인됐어요.",
    DelayStatus.NOT_DELAYED: "확인된 배송 지연은 없어요.",
    DelayStatus.UNKNOWN: "배송 지연 여부는 아직 확인할 수 없어요.",
}


def customer_time(value: datetime) -> str:
    """Use explicit KST, independent of the host OS timezone/database."""
    local = value.astimezone(timezone(timedelta(hours=9)))
    period = "오전" if local.hour < 12 else "오후"
    return (
        f"{local.year}년 {local.month}월 {local.day}일 "
        f"{period} {local.hour % 12 or 12}시 {local.minute:02d}분"
    )
