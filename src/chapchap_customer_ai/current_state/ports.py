from collections.abc import Mapping
from typing import Protocol

from chapchap_customer_ai.current_state.models import TransportResult
from chapchap_customer_ai.security.models import AuthenticatedContext


class CurrentStateTransport(Protocol):
    def invoke(
        self,
        tool_name: str,
        arguments: Mapping[str, object],
        security_context: AuthenticatedContext,
        *,
        required_scope: str,
        timeout_seconds: float,
    ) -> TransportResult: ...
