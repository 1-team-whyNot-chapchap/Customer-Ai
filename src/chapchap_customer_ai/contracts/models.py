from enum import StrEnum
from typing import Annotated, Literal
from uuid import UUID

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    StrictBool,
    StrictInt,
    field_validator,
    model_validator,
)

PositiveInt64 = Annotated[StrictInt, Field(gt=0, le=9_223_372_036_854_775_807)]


class ContractModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")


class UserRole(StrEnum):
    CUSTOMER = "CUSTOMER"
    RIDER = "RIDER"
    ADMIN = "ADMIN"
    SUPER_ADMIN = "SUPER_ADMIN"


class TrustedSubject(ContractModel):
    user_id: PositiveInt64 = Field(alias="userId")
    role: UserRole
    allowed_ai_scopes: list[str] = Field(alias="allowedAiScopes", min_length=1)

    @field_validator("allowed_ai_scopes")
    @classmethod
    def validate_scopes(cls, scopes: list[str]) -> list[str]:
        if any(not scope.strip() for scope in scopes) or len(scopes) != len(set(scopes)):
            raise ValueError("allowedAiScopes must contain unique non-blank scopes")
        return scopes


class KnowledgeSource(ContractModel):
    download_url: HttpUrl = Field(alias="downloadUrl")
    content_type: str = Field(alias="contentType", min_length=1, max_length=255)
    file_size: PositiveInt64 = Field(alias="fileSize")


class KnowledgeMetadata(ContractModel):
    document_key: str = Field(alias="documentKey", min_length=1, max_length=100)
    source_service: str = Field(alias="sourceService", min_length=1, max_length=100)
    category: str = Field(min_length=1, max_length=50)
    version: str = Field(min_length=1, max_length=100)
    effective_from: str = Field(alias="effectiveFrom", min_length=1)


class KnowledgeCallback(ContractModel):
    result_uri: Literal["/internal/v1/knowledge-processing-results"] = Field(alias="resultUri")


class KnowledgeProcessingRequest(ContractModel):
    schema_version: str = Field(alias="schemaVersion", pattern=r"^1\.0$")
    knowledge_version_id: PositiveInt64 = Field(alias="knowledgeVersionId")
    attempt: Annotated[StrictInt, Field(ge=1, le=3)]
    source: KnowledgeSource
    metadata: KnowledgeMetadata
    chunk_profile: str = Field(alias="chunkProfile", pattern=r"^HYBRID_POLICY_V1$")
    callback: KnowledgeCallback


class KnowledgeProcessingAccepted(ContractModel):
    schema_version: str = Field(alias="schemaVersion", pattern=r"^1\.0$")
    processing_id: PositiveInt64 = Field(alias="processingId")
    knowledge_version_id: PositiveInt64 = Field(alias="knowledgeVersionId")
    status: str = Field(pattern=r"^ACCEPTED$")


class KnowledgeProcessingFailureCode(StrEnum):
    SOURCE_FETCH_FAILED = "SOURCE_FETCH_FAILED"
    TEXT_EXTRACTION_FAILED = "TEXT_EXTRACTION_FAILED"
    UNSUPPORTED_DOCUMENT = "UNSUPPORTED_DOCUMENT"
    ENCRYPTED_DOCUMENT = "ENCRYPTED_DOCUMENT"
    CHUNK_PROFILE_INVALID = "CHUNK_PROFILE_INVALID"
    EMBEDDING_UNAVAILABLE = "EMBEDDING_UNAVAILABLE"
    VECTOR_STORE_UNAVAILABLE = "VECTOR_STORE_UNAVAILABLE"
    PROCESSING_TIMEOUT = "PROCESSING_TIMEOUT"
    CUSTOMER_AI_UNAVAILABLE = "CUSTOMER_AI_UNAVAILABLE"


class KnowledgeProcessingCompleted(ContractModel):
    schema_version: Literal["1.0"] = Field(alias="schemaVersion")
    processing_id: PositiveInt64 = Field(alias="processingId")
    knowledge_version_id: PositiveInt64 = Field(alias="knowledgeVersionId")
    status: Literal["COMPLETED"]
    chunk_count: Annotated[StrictInt, Field(gt=0)] = Field(alias="chunkCount")
    chunk_profile: Literal["HYBRID_POLICY_V1"] = Field(alias="chunkProfile")


class KnowledgeProcessingFailed(ContractModel):
    schema_version: Literal["1.0"] = Field(alias="schemaVersion")
    processing_id: PositiveInt64 = Field(alias="processingId")
    knowledge_version_id: PositiveInt64 = Field(alias="knowledgeVersionId")
    status: Literal["FAILED"]
    failure_code: KnowledgeProcessingFailureCode = Field(alias="failureCode")
    retryable: StrictBool


class ConsultationResponseRequest(ContractModel):
    schema_version: str = Field(alias="schemaVersion", pattern=r"^1\.0$")
    request_id: UUID = Field(alias="requestId")
    consultation_id: PositiveInt64 = Field(alias="consultationId")
    trigger_message_id: PositiveInt64 = Field(alias="triggerMessageId")
    subject: TrustedSubject
    message: str = Field(min_length=1, max_length=10_000)
    conversation_context: list[str] = Field(alias="conversationContext", max_length=20)
    knowledge_version_ids: list[PositiveInt64] = Field(
        default_factory=list, alias="knowledgeVersionIds", max_length=1000
    )

    @field_validator("knowledge_version_ids")
    @classmethod
    def validate_knowledge_versions(cls, ids: list[int]) -> list[int]:
        if len(ids) != len(set(ids)):
            raise ValueError("knowledgeVersionIds must be unique")
        return ids


class ConsultationRoute(StrEnum):
    POLICY = "POLICY"
    USER_STATE = "USER_STATE"
    POLICY_AND_STATE = "POLICY_AND_STATE"
    UNSUPPORTED = "UNSUPPORTED"


class ConsultationDecision(StrEnum):
    ANSWER = "ANSWER"
    HANDOFF = "HANDOFF"
    DEGRADED = "DEGRADED"


class ConsultationEvidence(ContractModel):
    knowledge_version_id: PositiveInt64 = Field(alias="knowledgeVersionId")
    chunk_id: str = Field(alias="chunkId", min_length=1, max_length=200)
    retrieval_rank: Annotated[StrictInt, Field(gt=0)] = Field(alias="retrievalRank")
    retrieval_score: float = Field(alias="retrievalScore", ge=0.0, le=1.0)


class ConsultationResponse(ContractModel):
    schema_version: Literal["1.0"] = Field(alias="schemaVersion")
    request_id: UUID = Field(alias="requestId")
    decision: ConsultationDecision
    answer: str | None = Field(default=None, min_length=1, max_length=10_000)
    route: ConsultationRoute
    degraded: StrictBool
    handoff_required: StrictBool = Field(alias="handoffRequired")
    evidence: list[ConsultationEvidence] = Field(default_factory=list, max_length=5)

    @model_validator(mode="after")
    def validate_decision_contract(self) -> "ConsultationResponse":
        if self.answer is not None and not self.answer.strip():
            raise ValueError("answer must not be blank")
        if self.decision == ConsultationDecision.ANSWER:
            if self.answer is None or self.degraded or self.handoff_required:
                raise ValueError("ANSWER requires an answer without degradation or handoff")
        elif self.decision == ConsultationDecision.HANDOFF:
            if not self.handoff_required or self.answer is not None or self.evidence:
                raise ValueError("HANDOFF requires only the handoff signal")
        elif self.answer is None or not self.degraded:
            raise ValueError("DEGRADED requires a partial answer and degraded=true")
        if (
            self.decision != ConsultationDecision.HANDOFF
            and self.route in {ConsultationRoute.POLICY, ConsultationRoute.POLICY_AND_STATE}
            and not self.evidence
        ):
            raise ValueError("policy answers require evidence")
        if len({item.chunk_id for item in self.evidence}) != len(self.evidence):
            raise ValueError("evidence chunk ids must be unique")
        return self


class ConsultationMessageSender(StrEnum):
    USER = "USER"
    ADMIN = "ADMIN"
    AI = "AI"


class ConsultationSummaryMessage(ContractModel):
    sender_type: ConsultationMessageSender = Field(alias="senderType")
    content: str = Field(min_length=1, max_length=10_000)

    @field_validator("content")
    @classmethod
    def validate_content(cls, content: str) -> str:
        if not content.strip():
            raise ValueError("content must not be blank")
        return content


class ConsultationSummaryCallback(ContractModel):
    result_uri: Literal["/internal/v1/consultation-summary-results"] = Field(
        alias="resultUri"
    )


class ConsultationSummaryRequest(ContractModel):
    schema_version: Literal["1.0"] = Field(alias="schemaVersion")
    summary_job_id: PositiveInt64 = Field(alias="summaryJobId")
    consultation_id: PositiveInt64 = Field(alias="consultationId")
    messages: list[ConsultationSummaryMessage] = Field(min_length=1)
    callback: ConsultationSummaryCallback


class ConsultationSummaryAccepted(ContractModel):
    schema_version: Literal["1.0"] = Field(alias="schemaVersion")
    summary_job_id: PositiveInt64 = Field(alias="summaryJobId")
    consultation_id: PositiveInt64 = Field(alias="consultationId")
    status: Literal["ACCEPTED"]


class ConsultationSummaryFailureCode(StrEnum):
    UNSAFE_CONTEXT = "UNSAFE_CONTEXT"
    SUMMARY_GENERATION_FAILED = "SUMMARY_GENERATION_FAILED"
    LLM_UNAVAILABLE = "LLM_UNAVAILABLE"
    PROCESSING_TIMEOUT = "PROCESSING_TIMEOUT"
    CUSTOMER_AI_UNAVAILABLE = "CUSTOMER_AI_UNAVAILABLE"


class ConsultationSummaryCompleted(ContractModel):
    schema_version: Literal["1.0"] = Field(alias="schemaVersion")
    summary_job_id: PositiveInt64 = Field(alias="summaryJobId")
    consultation_id: PositiveInt64 = Field(alias="consultationId")
    status: Literal["COMPLETED"]
    summary: str = Field(min_length=1, max_length=10_000)

    @field_validator("summary")
    @classmethod
    def validate_summary(cls, summary: str) -> str:
        if not summary.strip():
            raise ValueError("summary must not be blank")
        return summary


class ConsultationSummaryFailed(ContractModel):
    schema_version: Literal["1.0"] = Field(alias="schemaVersion")
    summary_job_id: PositiveInt64 = Field(alias="summaryJobId")
    consultation_id: PositiveInt64 = Field(alias="consultationId")
    status: Literal["FAILED"]
    failure_code: ConsultationSummaryFailureCode = Field(alias="failureCode")
    retryable: StrictBool
