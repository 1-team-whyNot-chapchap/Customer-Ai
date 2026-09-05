from concurrent.futures import Future
from dataclasses import dataclass
from threading import Lock

from chapchap_customer_ai.consultation.models import ConsultationRequestError
from chapchap_customer_ai.consultation.ports import ResponseFactory
from chapchap_customer_ai.contracts.models import ConsultationResponse


@dataclass(slots=True)
class _Entry:
    fingerprint: str
    future: Future[ConsultationResponse]


class InMemoryConsultationResponseRegistry:
    """Single-process reference adapter. Production requires shared response idempotency."""

    def __init__(self) -> None:
        self._entries: dict[str, _Entry] = {}
        self._lock = Lock()

    def execute_once(
        self,
        key: str,
        fingerprint: str,
        factory: ResponseFactory,
    ) -> ConsultationResponse:
        with self._lock:
            entry = self._entries.get(key)
            if entry is not None and entry.fingerprint != fingerprint:
                raise ConsultationRequestError(
                    "The idempotency key was used with a different request.", status_code=409
                )
            owner = entry is None
            if entry is None:
                entry = _Entry(fingerprint, Future())
                self._entries[key] = entry
        if not owner:
            return entry.future.result()
        try:
            response = factory()
        except BaseException as error:
            entry.future.set_exception(error)
            with self._lock:
                if self._entries.get(key) is entry:
                    self._entries.pop(key)
            raise
        entry.future.set_result(response)
        return response
