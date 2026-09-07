from dataclasses import dataclass

from chapchap_customer_ai.core.settings import Settings
from chapchap_customer_ai.security.jwt_verifier import (
    InternalSecurityVerifier,
    create_internal_security_verifier,
)


@dataclass(slots=True)
class InternalAuthRuntime:
    """검증이 완료된 내부 인증 Runtime을 보관한다."""

    verifier: InternalSecurityVerifier

    def close(self) -> None:
        """현재 Runtime에는 명시적으로 닫을 인증 자원이 없다."""


def create_internal_auth_runtime(settings: Settings) -> InternalAuthRuntime:
    """승인된 설정으로 내부 인증 Runtime을 Fail-Closed 방식으로 조립한다."""

    return InternalAuthRuntime(create_internal_security_verifier(settings))
