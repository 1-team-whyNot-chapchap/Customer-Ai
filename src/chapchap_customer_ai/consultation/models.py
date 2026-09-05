from dataclasses import dataclass
from enum import StrEnum


class ConsultationRequestError(ValueError):
    def __init__(self, message: str, *, status_code: int = 400) -> None:
        super().__init__(message)
        self.status_code = status_code


class ConsultationDependencyError(RuntimeError):
    """A safe dependency failure without raw external data."""


class Capability(StrEnum):
    PAYMENT_CURRENT = "CAP-PAYMENT-CURRENT"
    REFUND_RECENT = "CAP-REFUND-RECENT"
    SUBSCRIPTION_CURRENT = "CAP-SUBSCRIPTION-CURRENT"
    DELIVERY_CURRENT = "CAP-DELIVERY-CURRENT"


CAPABILITY_SCOPES: dict[Capability, str] = {
    Capability.PAYMENT_CURRENT: "subscription.payment.read",
    Capability.REFUND_RECENT: "subscription.refund.read",
    Capability.SUBSCRIPTION_CURRENT: "subscription.status.read",
    Capability.DELIVERY_CURRENT: "delivery.status.read",
}

APPROVED_CONSULTATION_SCOPES = frozenset(
    {"customer-ai.policy.read", *CAPABILITY_SCOPES.values()}
)


class StateAvailability(StrEnum):
    AVAILABLE = "AVAILABLE"
    NOT_FOUND = "NOT_FOUND"
    UNAVAILABLE = "UNAVAILABLE"
    TIMEOUT = "TIMEOUT"
    FORBIDDEN = "FORBIDDEN"


class StateErrorCode(StrEnum):
    CONTRACT_ERROR = "CONTRACT_ERROR"


@dataclass(frozen=True, slots=True)
class StateFact:
    capability: Capability
    availability: StateAvailability | None
    safe_answer: str | None = None
    values: tuple[tuple[str, str | int | None], ...] = ()
    error_code: StateErrorCode | None = None

    def __post_init__(self) -> None:
        if self.error_code is not None:
            if self.availability is not None or self.safe_answer is not None or self.values:
                raise ValueError("state errors must not contain availability or business facts")
        elif self.availability is None:
            raise ValueError("state facts require an availability or error code")
        elif self.availability == StateAvailability.AVAILABLE:
            if self.safe_answer is None or not self.safe_answer.strip():
                raise ValueError("available state facts require a safe answer")
            if len({name for name, _ in self.values}) != len(self.values):
                raise ValueError("state fact names must be unique")
        elif self.safe_answer is not None or self.values:
            raise ValueError("unavailable state facts must not contain business data")


@dataclass(frozen=True, slots=True)
class GroundedAnswerDraft:
    answer: str
    used_chunk_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.answer.strip():
            raise ValueError("draft answer must not be blank")
        if len(self.used_chunk_ids) != len(set(self.used_chunk_ids)):
            raise ValueError("used chunk ids must be unique")
