from enum import StrEnum
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, StrictInt

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


class KnowledgeProcessingRequest(ContractModel):
    schema_version: str = Field(alias="schemaVersion", pattern=r"^1\.0$")
    knowledge_version_id: PositiveInt64 = Field(alias="knowledgeVersionId")
    attempt: Annotated[StrictInt, Field(ge=1, le=3)]
    source: KnowledgeSource
    metadata: KnowledgeMetadata
    chunk_profile: str = Field(alias="chunkProfile", pattern=r"^HYBRID_POLICY_V1$")


class KnowledgeProcessingAccepted(ContractModel):
    schema_version: str = Field(alias="schemaVersion", pattern=r"^1\.0$")
    processing_id: PositiveInt64 = Field(alias="processingId")
    knowledge_version_id: PositiveInt64 = Field(alias="knowledgeVersionId")
    status: str = Field(pattern=r"^ACCEPTED$")


class ConsultationResponseRequest(ContractModel):
    schema_version: str = Field(alias="schemaVersion", pattern=r"^1\.0$")
    request_id: UUID = Field(alias="requestId")
    consultation_id: PositiveInt64 = Field(alias="consultationId")
    trigger_message_id: PositiveInt64 = Field(alias="triggerMessageId")
    subject: TrustedSubject
    message: str = Field(min_length=1, max_length=10_000)
    conversation_context: list[str] = Field(alias="conversationContext", max_length=20)
