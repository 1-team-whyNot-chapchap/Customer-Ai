from dataclasses import dataclass
from threading import Lock

from chapchap_customer_ai.summary.models import SummaryJobRegistration, SummaryRequestError


@dataclass(frozen=True, slots=True)
class _StoredSummaryJob:
    summary_job_id: int
    fingerprint: str


class InMemorySummaryJobRegistry:
    """Single-process reference adapter. Production requires shared idempotency."""

    def __init__(self) -> None:
        self._jobs: dict[str, _StoredSummaryJob] = {}
        self._keys_by_job_id: dict[int, str] = {}
        self._lock = Lock()

    def register(
        self, key: str, summary_job_id: int, fingerprint: str
    ) -> SummaryJobRegistration:
        if not key.strip() or summary_job_id <= 0 or not fingerprint:
            raise ValueError("summary job registration values must be valid")
        with self._lock:
            stored = self._jobs.get(key)
            if stored is None:
                existing_key = self._keys_by_job_id.get(summary_job_id)
                if existing_key is not None:
                    raise SummaryRequestError(
                        "The summary job id was used with a different idempotency key.",
                        status_code=409,
                    )
                self._jobs[key] = _StoredSummaryJob(summary_job_id, fingerprint)
                self._keys_by_job_id[summary_job_id] = key
                return SummaryJobRegistration(should_schedule=True)
            if stored.summary_job_id != summary_job_id or stored.fingerprint != fingerprint:
                raise SummaryRequestError(
                    "The idempotency key was used with a different summary request.",
                    status_code=409,
                )
            return SummaryJobRegistration(should_schedule=False)

    def release(self, key: str, summary_job_id: int) -> None:
        with self._lock:
            stored = self._jobs.get(key)
            if stored is not None and stored.summary_job_id == summary_job_id:
                self._jobs.pop(key)
                self._keys_by_job_id.pop(summary_job_id, None)
