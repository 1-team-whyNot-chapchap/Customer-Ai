"""Explicit runtime composition; does not mount or activate Candidate routes."""

import logging
from dataclasses import dataclass

import httpx

from chapchap_customer_ai.core.settings import Settings
from chapchap_customer_ai.current_state.adapter import CurrentStateAdapter
from chapchap_customer_ai.current_state.http import (
    HttpSubscriptionCurrentStateTransport,
    validate_subscription_origin,
)
from chapchap_customer_ai.observability.ports import DiagnosticSink
from chapchap_customer_ai.observability.sinks import JsonLogDiagnosticSink


@dataclass(frozen=True, slots=True)
class SubscriptionCurrentStateRuntime:
    adapter: CurrentStateAdapter
    client: httpx.Client

    def close(self) -> None:
        self.client.close()

    def __enter__(self) -> "SubscriptionCurrentStateRuntime":
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()


def create_subscription_current_state_runtime(
    settings: Settings,
    *,
    diagnostics: DiagnosticSink | None = None,
    transport: httpx.BaseTransport | None = None,
) -> SubscriptionCurrentStateRuntime:
    if settings.subscription_current_state_base_url is None:
        raise ValueError("Subscription Current-State origin is not configured.")
    origin = validate_subscription_origin(
        settings.subscription_current_state_base_url,
        allow_loopback_http=settings.subscription_current_state_allow_loopback_http,
    )
    client = httpx.Client(
        transport=transport if transport is not None else httpx.HTTPTransport(retries=0),
        trust_env=False,
        follow_redirects=False,
        timeout=settings.consultation_state_timeout_seconds,
    )
    adapter = CurrentStateAdapter(
        HttpSubscriptionCurrentStateTransport(
            client, origin, settings.subscription_current_state_allow_loopback_http
        ),
        diagnostics=diagnostics if diagnostics is not None else JsonLogDiagnosticSink(
            logging.getLogger("chapchap_customer_ai.current_state")
        ),
    )
    return SubscriptionCurrentStateRuntime(adapter, client)
