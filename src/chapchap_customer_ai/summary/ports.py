from collections.abc import Callable, Sequence
from typing import Protocol, TypeAlias
from uuid import UUID

from chapchap_customer_ai.contracts.models import (
    ConsultationSummaryCompleted,
    ConsultationSummaryFailed,
    ConsultationSummaryMessage,
)
from chapchap_customer_ai.summary.models import SummaryDraft, SummaryJobRegistration

SummaryResult: TypeAlias = ConsultationSummaryCompleted | ConsultationSummaryFailed


class SummaryComposer(Protocol):
    def summarize(
        self,
        messages: Sequence[ConsultationSummaryMessage],
        *,
        timeout_seconds: float,
    ) -> SummaryDraft: ...


class SummaryJobRegistry(Protocol):
    def register(
        self, key: str, summary_job_id: int, fingerprint: str
    ) -> SummaryJobRegistration: ...

    def release(self, key: str, summary_job_id: int) -> None: ...


class SummaryJobScheduler(Protocol):
    def submit(self, task: Callable[[], None]) -> None: ...


class SummaryResultPublisher(Protocol):
    def publish(self, result: SummaryResult, request_id: UUID) -> None: ...


class ServiceTokenProvider(Protocol):
    def get_token(self) -> str: ...
