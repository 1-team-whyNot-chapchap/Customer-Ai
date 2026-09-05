from dataclasses import dataclass

from chapchap_customer_ai.contracts.models import KnowledgeProcessingFailureCode


class KnowledgeRequestError(ValueError):
    def __init__(self, message: str, *, status_code: int = 400) -> None:
        super().__init__(message)
        self.status_code = status_code


class SourceFetchError(RuntimeError):
    """A safe source retrieval failure without URL or body details."""


class CallbackDeliveryError(RuntimeError):
    """A callback could not be delivered within the bounded policy."""


@dataclass(frozen=True, slots=True)
class JobRegistration:
    processing_id: int
    should_schedule: bool


RETRYABLE_FAILURES = frozenset(
    {
        KnowledgeProcessingFailureCode.SOURCE_FETCH_FAILED,
        KnowledgeProcessingFailureCode.EMBEDDING_UNAVAILABLE,
        KnowledgeProcessingFailureCode.VECTOR_STORE_UNAVAILABLE,
        KnowledgeProcessingFailureCode.PROCESSING_TIMEOUT,
        KnowledgeProcessingFailureCode.CUSTOMER_AI_UNAVAILABLE,
    }
)
