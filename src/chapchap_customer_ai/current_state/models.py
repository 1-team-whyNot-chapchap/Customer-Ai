from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum

from chapchap_customer_ai.consultation.models import Capability


class CurrentStateRequestError(ValueError):
    """A safe request error that never contains raw Tool data."""


class TransportOutcome(StrEnum):
    SUCCESS = "SUCCESS"
    BUSINESS_NOT_FOUND = "BUSINESS_NOT_FOUND"
    FORBIDDEN = "FORBIDDEN"
    UNAVAILABLE = "UNAVAILABLE"
    TIMEOUT = "TIMEOUT"
    CONTRACT_ERROR = "CONTRACT_ERROR"


@dataclass(frozen=True, slots=True)
class TransportResult:
    outcome: TransportOutcome
    payload: Mapping[str, object] | None = None
    retryable: bool = False

    def __post_init__(self) -> None:
        if not isinstance(self.outcome, TransportOutcome) or type(self.retryable) is not bool:
            raise ValueError("Tool outcome and retryable flag must use strict contract types")
        if self.payload is not None and not isinstance(self.payload, Mapping):
            raise ValueError("Tool payload must be an object")
        if self.outcome == TransportOutcome.SUCCESS:
            if self.payload is None or self.retryable:
                raise ValueError("successful Tool results require a non-retryable payload")
        elif self.payload is not None:
            raise ValueError("non-successful Tool results must not contain a payload")
        if self.retryable and self.outcome != TransportOutcome.UNAVAILABLE:
            raise ValueError("only an unavailable Tool result may be retryable")


@dataclass(frozen=True, slots=True)
class CapabilityBinding:
    capability: Capability
    tool_name: str
    required_scope: str
    domain_owner: str
