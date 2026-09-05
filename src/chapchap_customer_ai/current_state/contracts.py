from enum import StrEnum
from typing import Annotated, Literal

from pydantic import (
    AwareDatetime,
    BaseModel,
    ConfigDict,
    Field,
    StrictInt,
    model_validator,
)

MoneyAmount = Annotated[StrictInt, Field(ge=0)]


class DomainStateModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")


class PaymentStatus(StrEnum):
    PROCESSING = "PROCESSING"
    SUCCESS = "SUCCESS"
    RETRY_WAITING = "RETRY_WAITING"
    RETRY_STOPPED = "RETRY_STOPPED"
    FAILED = "FAILED"


class PaymentType(StrEnum):
    FIRST_SUBSCRIPTION_PAYMENT = "FIRST_SUBSCRIPTION_PAYMENT"
    REGULAR_PAYMENT = "REGULAR_PAYMENT"
    SETTING_CHANGE_PAYMENT = "SETTING_CHANGE_PAYMENT"


class CurrentPaymentState(DomainStateModel):
    availability: Literal["AVAILABLE"]
    status: PaymentStatus
    payment_type: PaymentType = Field(alias="paymentType")
    amount: MoneyAmount
    occurred_at: AwareDatetime = Field(alias="occurredAt")


class RefundStatus(StrEnum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"


class RecentRefundResult(DomainStateModel):
    availability: Literal["AVAILABLE"]
    status: RefundStatus
    refund_type: str = Field(alias="refundType", pattern=r"^[A-Z][A-Z0-9_]{0,99}$")
    requested_amount: MoneyAmount = Field(alias="requestedAmount")
    refunded_amount: MoneyAmount = Field(alias="refundedAmount")
    unprocessed_amount: MoneyAmount = Field(alias="unprocessedAmount")
    requested_at: AwareDatetime = Field(alias="requestedAt")
    completed_at: AwareDatetime | None = Field(alias="completedAt")

    @model_validator(mode="after")
    def validate_refund_totals_and_completion(self) -> "RecentRefundResult":
        if self.requested_amount != self.refunded_amount + self.unprocessed_amount:
            raise ValueError("refund amounts must preserve the requested total")
        if (self.status == RefundStatus.COMPLETED) != (self.completed_at is not None):
            raise ValueError("completedAt is required only for COMPLETED refunds")
        return self


class SubscriptionStatus(StrEnum):
    AWAITING_CONFIRMATION = "AWAITING_CONFIRMATION"
    SCHEDULED = "SCHEDULED"
    IN_PROGRESS = "IN_PROGRESS"
    CANCELLATION_SCHEDULED = "CANCELLATION_SCHEDULED"
    PAYMENT_FAILED = "PAYMENT_FAILED"
    CANCELED_BEFORE_START = "CANCELED_BEFORE_START"
    ENDED = "ENDED"


class CurrentSubscriptionState(DomainStateModel):
    availability: Literal["AVAILABLE"]
    status: SubscriptionStatus


class DeliveryStatus(StrEnum):
    READY = "READY"
    DELIVERING = "DELIVERING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class DelayStatus(StrEnum):
    DELAYED = "DELAYED"
    NOT_DELAYED = "NOT_DELAYED"
    UNKNOWN = "UNKNOWN"


class CurrentDeliveryState(DomainStateModel):
    availability: Literal["AVAILABLE"]
    status: DeliveryStatus
    delay_status: DelayStatus = Field(alias="delayStatus")
    status_changed_at: AwareDatetime | None = Field(default=None, alias="statusChangedAt")
