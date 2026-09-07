"""Explicit single-process verification runtime; production activation is unsupported."""

import logging
from contextlib import ExitStack, asynccontextmanager
from dataclasses import dataclass, field

import httpx
from fastapi import FastAPI

from chapchap_customer_ai.api.consultation import build_candidate_consultation_router
from chapchap_customer_ai.api.health import router as health_router
from chapchap_customer_ai.api.knowledge import build_candidate_knowledge_router
from chapchap_customer_ai.api.summary import build_candidate_summary_router
from chapchap_customer_ai.application.deepseek import DeepSeekComposer
from chapchap_customer_ai.consultation.idempotency import InMemoryConsultationResponseRegistry
from chapchap_customer_ai.consultation.knowledge_versions import RequestApprovedKnowledgeVersions
from chapchap_customer_ai.consultation.services import ConsultationResponseService
from chapchap_customer_ai.core.settings import Settings, get_settings
from chapchap_customer_ai.current_state.adapter import CurrentStateAdapter
from chapchap_customer_ai.current_state.delivery_http import DomainCurrentStateTransport
from chapchap_customer_ai.current_state.http import HttpSubscriptionCurrentStateTransport
from chapchap_customer_ai.current_state.ports import CurrentStateTransport
from chapchap_customer_ai.knowledge.http import (
    HttpKnowledgeResultPublisher,
    HttpKnowledgeSourceFetcher,
)
from chapchap_customer_ai.knowledge.idempotency import InMemoryKnowledgeJobRegistry
from chapchap_customer_ai.knowledge.scheduling import ThreadPoolJobScheduler
from chapchap_customer_ai.knowledge.services import KnowledgeProcessingService
from chapchap_customer_ai.observability.sinks import JsonLogDiagnosticSink
from chapchap_customer_ai.rag.chunking import HybridPolicyV1Chunker
from chapchap_customer_ai.rag.extraction import TextDocumentExtractor
from chapchap_customer_ai.rag.retrieval import (
    VectorRetrievalService,
    create_vector_retrieval_service,
)
from chapchap_customer_ai.rag.services import RagCoreService
from chapchap_customer_ai.rag.tokenization import MultilingualE5TokenCounter
from chapchap_customer_ai.security.jwt_verifier import InternalSecurityVerifier
from chapchap_customer_ai.security.runtime import create_internal_auth_runtime
from chapchap_customer_ai.security.service_tokens import AuthServiceCallbackTokenProvider
from chapchap_customer_ai.summary.guardrails import SummaryGuardrails
from chapchap_customer_ai.summary.http import HttpSummaryResultPublisher
from chapchap_customer_ai.summary.idempotency import InMemorySummaryJobRegistry
from chapchap_customer_ai.summary.services import ConsultationSummaryService


@dataclass(frozen=True)
class ProviderRuntimeDependencies:
    """Explicit test/host injection. Factories own only resources they create."""

    verifier: InternalSecurityVerifier | None = None
    retrieval: VectorRetrievalService | None = None
    chunk_builder: RagCoreService | None = None
    delivery: CurrentStateTransport | None = None
    http_transports: dict[str, httpx.BaseTransport] = field(default_factory=dict)


@dataclass
class ProviderRuntime:
    consultation: ConsultationResponseService
    knowledge: KnowledgeProcessingService
    summary: ConsultationSummaryService
    verifier: InternalSecurityVerifier
    _resources: ExitStack = field(repr=False)

    def close(self):
        self._resources.close()


def create_provider_runtime(
    settings: Settings, dependencies: ProviderRuntimeDependencies | None = None
) -> ProviderRuntime:
    if settings.provider_runtime_mode != "isolated" or settings.environment not in {
        "local",
        "test",
    }:
        raise ValueError(
            "Provider runtime requires isolated mode in local/test; production is blocked"
        )
    if not settings.internal_security_enabled:
        raise ValueError("Provider runtime requires internal authentication")
    required = (
        settings.auth_token_base_url,
        settings.auth_client_id,
        settings.auth_client_secret,
        settings.deepseek_api_key,
        settings.knowledge_callback_base_url,
        settings.summary_callback_base_url,
        settings.knowledge_source_allowed_hosts,
    )
    if not all(required):
        raise ValueError("Provider runtime dependency configuration is incomplete")
    deps = dependencies or ProviderRuntimeDependencies()
    resources = ExitStack()
    try:
        if deps.verifier is None:
            auth = create_internal_auth_runtime(settings)
            resources.callback(auth.close)
            verifier = auth.verifier
        else:
            verifier = deps.verifier

        def client(name):
            return resources.enter_context(
                httpx.Client(
                    transport=deps.http_transports.get(name) or httpx.HTTPTransport(retries=0),
                    follow_redirects=False,
                    trust_env=False,
                )
            )

        token_provider = AuthServiceCallbackTokenProvider(
            client("auth"),
            settings.auth_token_base_url,
            settings.auth_client_id,
            settings.auth_client_secret,
            timeout_seconds=settings.auth_token_timeout_seconds,
        )
        composer = DeepSeekComposer(
            client("llm"),
            settings.deepseek_api_key,
            settings.deepseek_model,
            settings.deepseek_temperature,
            settings.deepseek_max_output_tokens,
            settings.summary_max_output_characters,
        )
        source_fetcher = HttpKnowledgeSourceFetcher(
            client("source"),
            settings.knowledge_source_allowed_hosts,
            settings.knowledge_source_timeout_seconds,
            settings.knowledge_source_max_bytes,
        )
        callback_client = client("callback")
        knowledge_publisher = HttpKnowledgeResultPublisher(
            callback_client,
            token_provider,
            settings.knowledge_callback_base_url,
            settings.knowledge_callback_timeout_seconds,
            settings.knowledge_callback_max_attempts,
        )
        summary_publisher = HttpSummaryResultPublisher(
            callback_client,
            token_provider,
            settings.summary_callback_base_url,
            settings.summary_callback_timeout_seconds,
            settings.summary_callback_max_attempts,
        )
        subscription = None
        if settings.subscription_current_state_base_url is not None:
            subscription = HttpSubscriptionCurrentStateTransport(
                client("subscription"),
                settings.subscription_current_state_base_url,
                settings.subscription_current_state_allow_loopback_http,
            )
        retrieval = deps.retrieval or create_vector_retrieval_service(settings)
        chunk_builder = deps.chunk_builder or RagCoreService(
            TextDocumentExtractor(),
            HybridPolicyV1Chunker(MultilingualE5TokenCounter.from_pretrained()),
        )
        diagnostics = JsonLogDiagnosticSink(logging.getLogger("chapchap_customer_ai.runtime"))
        state_provider = CurrentStateAdapter(
            DomainCurrentStateTransport(subscription, deps.delivery), diagnostics=diagnostics
        )
        # Registered last: drain jobs before their HTTP clients are closed.
        scheduler = ThreadPoolJobScheduler(max_workers=settings.provider_job_workers)
        resources.callback(scheduler.close)
        consultation = ConsultationResponseService(
            RequestApprovedKnowledgeVersions(),
            retrieval,
            state_provider,
            composer,
            InMemoryConsultationResponseRegistry(),
            request_deadline_seconds=settings.consultation_deadline_seconds,
            route_timeout_seconds=settings.consultation_route_timeout_seconds,
            rag_timeout_seconds=settings.consultation_rag_timeout_seconds,
            state_timeout_seconds=settings.consultation_state_timeout_seconds,
            compose_timeout_seconds=settings.consultation_compose_timeout_seconds,
            diagnostics=diagnostics,
        )
        knowledge = KnowledgeProcessingService(
            InMemoryKnowledgeJobRegistry(),
            scheduler,
            source_fetcher,
            chunk_builder,
            retrieval,
            knowledge_publisher,
            diagnostics=diagnostics,
        )
        summary = ConsultationSummaryService(
            InMemorySummaryJobRegistry(),
            scheduler,
            composer,
            summary_publisher,
            guardrails=SummaryGuardrails(
                settings.summary_max_messages,
                settings.summary_max_context_characters,
                settings.summary_max_output_characters,
            ),
            compose_timeout_seconds=settings.summary_compose_timeout_seconds,
            diagnostics=diagnostics,
        )
        return ProviderRuntime(consultation, knowledge, summary, verifier, resources.pop_all())
    except BaseException:
        resources.close()
        raise


def create_isolated_app(
    settings: Settings | None = None, dependencies: ProviderRuntimeDependencies | None = None
) -> FastAPI:
    configured = settings or get_settings()
    runtime = create_provider_runtime(configured, dependencies)

    @asynccontextmanager
    async def lifespan(app):
        try:
            yield
        finally:
            runtime.close()

    try:
        app = FastAPI(
            title=configured.app_name,
            docs_url=None,
            redoc_url=None,
            openapi_url=None,
            lifespan=lifespan,
        )
        app.state.provider_runtime = runtime
        app.include_router(health_router)
        app.include_router(
            build_candidate_consultation_router(runtime.consultation, runtime.verifier)
        )
        app.include_router(build_candidate_knowledge_router(runtime.knowledge, runtime.verifier))
        app.include_router(build_candidate_summary_router(runtime.summary, runtime.verifier))
        return app
    except BaseException:
        runtime.close()
        raise
