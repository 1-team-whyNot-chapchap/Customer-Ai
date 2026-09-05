from dataclasses import dataclass
from enum import StrEnum
from uuid import UUID

from chapchap_customer_ai.contracts.models import UserRole


class AuthFailureCode(StrEnum):
    MISSING_CREDENTIALS = "MISSING_CREDENTIALS"
    INVALID_TOKEN = "INVALID_TOKEN"
    KEY_UNAVAILABLE = "KEY_UNAVAILABLE"
    INSUFFICIENT_SCOPE = "INSUFFICIENT_SCOPE"
    INVALID_SUBJECT_CONTEXT = "INVALID_SUBJECT_CONTEXT"
    TOKEN_REPLAYED = "TOKEN_REPLAYED"


class InternalAuthError(RuntimeError):
    def __init__(self, code: AuthFailureCode, status_code: int, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.status_code = status_code


@dataclass(frozen=True, slots=True)
class AuthenticatedSubject:
    user_id: int
    role: UserRole
    allowed_ai_scopes: frozenset[str]
    request_id: UUID
    consultation_id: int


@dataclass(frozen=True, slots=True)
class AuthenticatedContext:
    service_subject: str
    subject: AuthenticatedSubject
