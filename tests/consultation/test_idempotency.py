from concurrent.futures import ThreadPoolExecutor
from threading import Event, Lock
from uuid import uuid4

import pytest

from chapchap_customer_ai.consultation.idempotency import (
    InMemoryConsultationResponseRegistry,
)
from chapchap_customer_ai.consultation.models import ConsultationRequestError
from chapchap_customer_ai.contracts.models import (
    ConsultationDecision,
    ConsultationResponse,
    ConsultationRoute,
)


def response() -> ConsultationResponse:
    return ConsultationResponse(
        schema_version="1.0",
        request_id=uuid4(),
        decision=ConsultationDecision.DEGRADED,
        answer="지원 범위가 아닙니다.",
        route=ConsultationRoute.UNSUPPORTED,
        degraded=True,
        handoff_required=False,
    )


def test_concurrent_duplicate_executes_factory_once() -> None:
    registry = InMemoryConsultationResponseRegistry()
    started = Event()
    release = Event()
    lock = Lock()
    calls = 0
    result = response()

    def factory() -> ConsultationResponse:
        nonlocal calls
        with lock:
            calls += 1
        started.set()
        release.wait(timeout=2)
        return result

    with ThreadPoolExecutor(max_workers=2) as executor:
        first = executor.submit(registry.execute_once, "key", "fingerprint", factory)
        started.wait(timeout=2)
        second = executor.submit(registry.execute_once, "key", "fingerprint", factory)
        release.set()
        assert first.result() is result
        assert second.result() is result

    assert calls == 1


def test_same_key_with_different_fingerprint_is_rejected() -> None:
    registry = InMemoryConsultationResponseRegistry()
    registry.execute_once("key", "first", response)

    with pytest.raises(ConsultationRequestError) as error:
        registry.execute_once("key", "second", response)

    assert error.value.status_code == 409
