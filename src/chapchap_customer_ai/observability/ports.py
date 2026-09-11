from typing import Protocol

from chapchap_customer_ai.observability.models import DiagnosticEvent


class DiagnosticSink(Protocol):
    def emit(self, event: DiagnosticEvent) -> None: ...
