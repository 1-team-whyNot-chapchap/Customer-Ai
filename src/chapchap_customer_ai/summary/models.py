from dataclasses import dataclass

from chapchap_customer_ai.contracts.models import ConsultationSummaryFailureCode


class SummaryRequestError(ValueError):
    def __init__(self, message: str, *, status_code: int = 400) -> None:
        super().__init__(message)
        self.status_code = status_code


class SummaryComposerError(RuntimeError):
    """A safe temporary composer failure without raw provider data."""


class SummaryCallbackDeliveryError(RuntimeError):
    """A callback delivery failure without response content or credentials."""


@dataclass(frozen=True, slots=True)
class SummaryDraft:
    text: str


@dataclass(frozen=True, slots=True)
class SummaryJobRegistration:
    should_schedule: bool


RETRYABLE_FAILURES = frozenset(
    {
        ConsultationSummaryFailureCode.LLM_UNAVAILABLE,
        ConsultationSummaryFailureCode.PROCESSING_TIMEOUT,
        ConsultationSummaryFailureCode.CUSTOMER_AI_UNAVAILABLE,
    }
)
