import time
from collections.abc import Callable
from contextlib import closing
from dataclasses import dataclass
from urllib.parse import urlsplit
from uuid import UUID

import httpx

from chapchap_customer_ai.summary.models import SummaryCallbackDeliveryError
from chapchap_customer_ai.summary.ports import (
    ServiceTokenProvider,
    SummaryResult,
)


@dataclass(frozen=True, slots=True)
class HttpSummaryResultPublisher:
    client: httpx.Client
    token_provider: ServiceTokenProvider
    base_url: str
    timeout_seconds: float = 5.0
    max_attempts: int = 3
    sleeper: Callable[[float], None] = time.sleep

    def __post_init__(self) -> None:
        parsed = urlsplit(self.base_url)
        if (
            parsed.scheme != "https"
            or not parsed.hostname
            or parsed.username is not None
            or parsed.password is not None
            or parsed.query
            or parsed.fragment
            or parsed.path not in {"", "/"}
        ):
            raise ValueError("summary callback base URL must be an HTTPS origin")
        if self.timeout_seconds <= 0 or not 1 <= self.max_attempts <= 5:
            raise ValueError("summary callback timeout or maximum attempts is invalid")

    def publish(self, result: SummaryResult, request_id: UUID) -> None:
        endpoint = self.base_url.rstrip("/") + "/internal/v1/consultation-summary-results"
        for attempt in range(1, self.max_attempts + 1):
            retryable = True
            try:
                token = self.token_provider.get_token()
                if not token or any(character.isspace() for character in token):
                    raise SummaryCallbackDeliveryError(
                        "A callback service token is unavailable."
                    )
                request = httpx.Request(
                    "POST", endpoint,
                    headers={
                        "Authorization": f"Bearer {token}",
                        "X-Request-Id": str(request_id),
                        "Idempotency-Key": str(result.summary_job_id),
                    },
                    json=result.model_dump(by_alias=True, mode="json"),
                    extensions={"timeout": httpx.Timeout(self.timeout_seconds).as_dict()},
                )
                with closing(self.client.send(
                    request, auth=None, follow_redirects=False, stream=True
                )) as response:
                    if response.status_code == 204:
                        return
                    retryable = response.status_code in {408, 429} or response.status_code >= 500
            except SummaryCallbackDeliveryError:
                raise
            except Exception:
                retryable = True
            if not retryable or attempt == self.max_attempts:
                break
            self.sleeper(min(0.1 * (2 ** (attempt - 1)), 1.0))
        raise SummaryCallbackDeliveryError(
            "The consultation summary callback could not be delivered."
        )
