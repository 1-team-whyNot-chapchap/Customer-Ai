import logging
from dataclasses import dataclass

from chapchap_customer_ai.observability.models import DiagnosticEvent
from chapchap_customer_ai.observability.ports import DiagnosticSink


@dataclass(frozen=True, slots=True)
class NoOpDiagnosticSink:
    def emit(self, event: DiagnosticEvent) -> None:
        return None


@dataclass(frozen=True, slots=True)
class JsonLogDiagnosticSink:
    logger: logging.Logger

    def emit(self, event: DiagnosticEvent) -> None:
        self.logger.info(event.model_dump_json(by_alias=True, exclude_none=True))


def emit_safely(sink: DiagnosticSink, event: DiagnosticEvent) -> None:
    try:
        sink.emit(event)
    except Exception:
        return None
