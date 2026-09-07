import time
from collections.abc import Callable, Collection
from contextlib import closing
from dataclasses import dataclass
from urllib.parse import urlsplit
from uuid import UUID

import httpx

from chapchap_customer_ai.contracts.models import KnowledgeSource
from chapchap_customer_ai.knowledge.models import CallbackDeliveryError, SourceFetchError
from chapchap_customer_ai.knowledge.ports import (
    KnowledgeResult,
    ServiceTokenProvider,
)


@dataclass(frozen=True, slots=True)
class HttpKnowledgeSourceFetcher:
    client: httpx.Client
    allowed_hosts: Collection[str]
    timeout_seconds: float = 5.0
    max_bytes: int = 10 * 1024 * 1024

    def __post_init__(self) -> None:
        normalized_hosts = frozenset(host.lower().strip() for host in self.allowed_hosts)
        if not normalized_hosts or any(not host for host in normalized_hosts):
            raise ValueError("knowledge source allowed hosts must be configured")
        if self.timeout_seconds <= 0 or self.max_bytes <= 0:
            raise ValueError("source timeout and maximum size must be positive")
        object.__setattr__(self, "allowed_hosts", normalized_hosts)

    def fetch(self, source: KnowledgeSource) -> bytes:
        url = str(source.download_url)
        parsed = urlsplit(url)
        if (
            parsed.scheme != "https"
            or not parsed.hostname
            or parsed.hostname.lower() not in self.allowed_hosts
            or parsed.username is not None
            or parsed.password is not None
            or parsed.fragment
            or source.file_size > self.max_bytes
        ):
            raise SourceFetchError("The knowledge source is not allowed.")

        try:
            request = httpx.Request("GET", url, extensions={
                "timeout": httpx.Timeout(self.timeout_seconds).as_dict(),
            })
            with closing(self.client.send(
                request, auth=None, follow_redirects=False, stream=True
            )) as response:
                if response.status_code != 200:
                    raise SourceFetchError("The knowledge source could not be fetched.")
                actual_content_type = response.headers.get("content-type", "").split(";", 1)[0]
                if actual_content_type.lower().strip() != source.content_type.lower().strip():
                    raise SourceFetchError("The knowledge source content type does not match.")
                declared_length = response.headers.get("content-length")
                if (
                    declared_length is not None
                    and self._content_length(declared_length) != source.file_size
                ):
                    raise SourceFetchError("The knowledge source size does not match.")
                content = bytearray()
                for block in response.iter_bytes():
                    content.extend(block)
                    if len(content) > self.max_bytes or len(content) > source.file_size:
                        raise SourceFetchError("The knowledge source exceeds the allowed size.")
        except SourceFetchError:
            raise
        except Exception:
            raise SourceFetchError("The knowledge source could not be fetched.") from None
        if len(content) != source.file_size:
            raise SourceFetchError("The knowledge source size does not match.")
        return bytes(content)

    @staticmethod
    def _content_length(value: str) -> int:
        try:
            parsed = int(value)
        except (TypeError, ValueError):
            raise SourceFetchError("The knowledge source size is invalid.") from None
        if parsed < 0:
            raise SourceFetchError("The knowledge source size is invalid.")
        return parsed


@dataclass(frozen=True, slots=True)
class HttpKnowledgeResultPublisher:
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
            raise ValueError("callback base URL must be an HTTPS origin")
        if self.timeout_seconds <= 0 or not 1 <= self.max_attempts <= 5:
            raise ValueError("callback timeout or maximum attempts is invalid")

    def publish(self, result: KnowledgeResult, request_id: UUID) -> None:
        endpoint = (
            self.base_url.rstrip("/") + "/internal/v1/knowledge-processing-results"
        )
        for attempt in range(1, self.max_attempts + 1):
            retryable = True
            try:
                token = self.token_provider.get_token()
                if not token or any(character.isspace() for character in token):
                    raise CallbackDeliveryError("A callback service token is unavailable.")
                request = httpx.Request(
                    "POST", endpoint,
                    headers={
                        "Authorization": f"Bearer {token}",
                        "X-Request-Id": str(request_id),
                        "Idempotency-Key": str(result.processing_id),
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
            except CallbackDeliveryError:
                raise
            except Exception:
                retryable = True
            if not retryable or attempt == self.max_attempts:
                break
            self.sleeper(min(0.1 * (2 ** (attempt - 1)), 1.0))
        raise CallbackDeliveryError("The knowledge processing callback could not be delivered.")
