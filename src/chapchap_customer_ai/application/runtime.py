"""Single-process isolated verification and explicit academy deployment runtime."""

import logging
from contextlib import ExitStack, asynccontextmanager
from dataclasses import dataclass, field
from uuid import UUID

import httpx
from fastapi import FastAPI

from chapchap_customer_ai.api.consultation import build_candidate_consultation_router
from chapchap_customer_ai.api.health import router as health_router
from chapchap_customer_ai.api.knowledge import build_candidate_knowledge_router
from chapchap_customer_ai.api.summary import build_candidate_summary_router
from chapchap_customer_ai.application.deepseek import DeepSeekComposer
from chapchap_customer_ai.application.persistence import (
    PersistentConsultationResponseRegistry,
    PersistentKnowledgeJobRegistry,
    PersistentSummaryJobRegistry,
    RuntimeStore,
    claim_runtime_volume,
)
from chapchap_customer_ai.consultation.idempotency import InMemoryConsultationResponseRegistry
from chapchap_customer_ai.consultation.knowledge_versions import RequestApprovedKnowledgeVersions
from chapchap_customer_ai.consultation.services import ConsultationResponseService
from chapchap_customer_ai.contracts.models import (
    ConsultationSummaryRequest,
    KnowledgeProcessingRequest,
)
from chapchap_customer_ai.core.settings import Settings, get_settings
from chapchap_customer_ai.current_state.adapter import CurrentStateAdapter
from chapchap_customer_ai.current_state.delivery_http import (
    DomainCurrentStateTransport,
    HttpDeliveryCurrentStateTransport,
)
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
    academy = settings.provider_runtime_mode == "academy"
    if not academy and (
        settings.provider_runtime_mode != "isolated"
        or settings.environment
        not in {
            "local",
            "test",
        }
    ):
        raise ValueError(
            "Provider runtime requires isolated mode in local/test; production is blocked"
        )
    if academy and (
        settings.environment not in {"academy", "production"}
        or settings.runtime_state_directory is None
        or not settings.runtime_state_directory.is_absolute()
        or settings.chroma_persist_directory is None
        or not settings.chroma_persist_directory.is_absolute()
    ):
        raise ValueError("Academy runtime requires absolute persistent state and Chroma paths")
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
    delivery_configured = settings.delivery_current_state_base_url is not None
    if delivery_configured != (settings.delivery_current_state_api_key is not None):
        raise ValueError("Delivery current-state requires both base URL and dedicated API key")
    if delivery_configured and deps.delivery is not None:
        raise ValueError("Delivery configuration and injection are mutually exclusive")
    resources = ExitStack()
    try:
        if academy:
            resources.enter_context(claim_runtime_volume(settings.runtime_state_directory))
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
            http_allowed_origins=settings.http_allowed_origins,
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
            http_allowed_origins=settings.knowledge_source_http_allowed_origins,
        )
        callback_client = client("callback")
        knowledge_publisher = HttpKnowledgeResultPublisher(
            callback_client,
            token_provider,
            settings.knowledge_callback_base_url,
            settings.knowledge_callback_timeout_seconds,
            settings.knowledge_callback_max_attempts,
            http_allowed_origins=settings.http_allowed_origins,
        )
        summary_publisher = HttpSummaryResultPublisher(
            callback_client,
            token_provider,
            settings.summary_callback_base_url,
            settings.summary_callback_timeout_seconds,
            settings.summary_callback_max_attempts,
            http_allowed_origins=settings.http_allowed_origins,
        )
        subscription = None
        if settings.subscription_current_state_base_url is not None:
            subscription = HttpSubscriptionCurrentStateTransport(
                client("subscription"),
                settings.subscription_current_state_base_url,
                settings.subscription_current_state_allow_loopback_http,
                http_allowed_origins=settings.http_allowed_origins,
            )
        delivery = deps.delivery
        if delivery_configured:
            delivery = HttpDeliveryCurrentStateTransport(
                client("delivery"),
                settings.delivery_current_state_base_url,
                settings.delivery_current_state_api_key,
                settings.delivery_current_state_allow_loopback_http,
                http_allowed_origins=settings.http_allowed_origins,
            )
        retrieval = deps.retrieval or create_vector_retrieval_service(settings)
        chunk_builder = deps.chunk_builder or RagCoreService(
            TextDocumentExtractor(),
            HybridPolicyV1Chunker(MultilingualE5TokenCounter.from_pretrained()),
        )
        diagnostics = JsonLogDiagnosticSink(logging.getLogger("chapchap_customer_ai.runtime"))
        state_provider = CurrentStateAdapter(
            DomainCurrentStateTransport(subscription, delivery), diagnostics=diagnostics
        )
        # Registered last: drain jobs before their HTTP clients are closed.
        scheduler = ThreadPoolJobScheduler(max_workers=settings.provider_job_workers)
        resources.callback(scheduler.close)
        store = RuntimeStore(settings.runtime_state_directory) if academy else None
        consultation = ConsultationResponseService(
            RequestApprovedKnowledgeVersions(),
            retrieval,
            state_provider,
            composer,
            PersistentConsultationResponseRegistry(store)
            if store
            else InMemoryConsultationResponseRegistry(),
            request_deadline_seconds=settings.consultation_deadline_seconds,
            route_timeout_seconds=settings.consultation_route_timeout_seconds,
            rag_timeout_seconds=settings.consultation_rag_timeout_seconds,
            state_timeout_seconds=settings.consultation_state_timeout_seconds,
            compose_timeout_seconds=settings.consultation_compose_timeout_seconds,
            diagnostics=diagnostics,
        )
        knowledge = KnowledgeProcessingService(
            PersistentKnowledgeJobRegistry(store) if store else InMemoryKnowledgeJobRegistry(),
            scheduler,
            source_fetcher,
            chunk_builder,
            retrieval,
            knowledge_publisher,
            diagnostics=diagnostics,
        )
        summary = ConsultationSummaryService(
            PersistentSummaryJobRegistry(store) if store else InMemorySummaryJobRegistry(),
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
        if store:
            for kind, key, request_id, payload in store.pending():
                service, model = (
                    (knowledge, KnowledgeProcessingRequest)
                    if kind == "knowledge"
                    else (summary, ConsultationSummaryRequest)
                )
                service.accept(
                    model.model_validate_json(payload),
                    request_id=UUID(request_id),
                    idempotency_key=key,
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
