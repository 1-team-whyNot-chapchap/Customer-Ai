from dataclasses import dataclass

from chapchap_customer_ai.core.settings import Settings
from chapchap_customer_ai.security.jwt_verifier import (
    InternalSecurityVerifier,
    create_internal_security_verifier,
)
from chapchap_customer_ai.security.replay import InMemoryReplayStore, ReplayStore


@dataclass(slots=True)
class InternalAuthRuntime:
    """내부 인증 검증기와 수명주기 자원을 함께 보관한다."""

    verifier: InternalSecurityVerifier
    replay_store: ReplayStore

    def close(self) -> None:
        close = getattr(self.replay_store, "close", None)
        if callable(close):
            close()


def create_internal_auth_runtime(settings: Settings) -> InternalAuthRuntime:
    """승인된 설정으로 내부 인증 Runtime을 Fail-Closed 방식으로 조립한다."""

    if settings.environment.lower() not in {"local", "test"}:
        raise RuntimeError("Operational replay protection is not configured.")
    replay_store = InMemoryReplayStore()
    try:
        verifier = create_internal_security_verifier(settings, replay_store)
    except Exception:
        close = getattr(replay_store, "close", None)
        if callable(close):
            close()
        raise
    return InternalAuthRuntime(verifier, replay_store)
