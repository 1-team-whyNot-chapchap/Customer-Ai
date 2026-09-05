from dataclasses import dataclass, field
from threading import Lock

from chapchap_customer_ai.knowledge.models import JobRegistration, KnowledgeRequestError


@dataclass(slots=True)
class _StoredJob:
    processing_id: int
    fingerprint: str
    attempts: set[int] = field(default_factory=set)


class InMemoryKnowledgeJobRegistry:
    """Single-process reference adapter. Production needs a distributed implementation."""

    def __init__(self, *, starting_processing_id: int = 1) -> None:
        if starting_processing_id <= 0:
            raise ValueError("starting_processing_id must be positive")
        self._next_processing_id = starting_processing_id
        self._jobs: dict[str, _StoredJob] = {}
        self._lock = Lock()

    def register(self, logical_key: str, fingerprint: str, attempt: int) -> JobRegistration:
        if not logical_key or not fingerprint or not 1 <= attempt <= 3:
            raise ValueError("logical key, fingerprint, and attempt must be valid")
        with self._lock:
            stored = self._jobs.get(logical_key)
            if stored is None:
                stored = _StoredJob(self._next_processing_id, fingerprint)
                self._next_processing_id += 1
                self._jobs[logical_key] = stored
            elif stored.fingerprint != fingerprint:
                raise KnowledgeRequestError(
                    "The idempotency key was used with different immutable request data.",
                    status_code=409,
                )
            should_schedule = attempt not in stored.attempts
            stored.attempts.add(attempt)
            return JobRegistration(stored.processing_id, should_schedule)

    def release_attempt(self, logical_key: str, attempt: int) -> None:
        with self._lock:
            stored = self._jobs.get(logical_key)
            if stored is not None:
                stored.attempts.discard(attempt)
