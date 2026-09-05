from enum import StrEnum
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, model_validator

from chapchap_customer_ai.consultation.models import Capability, StateAvailability
from chapchap_customer_ai.contracts.models import (
    ConsultationDecision,
    ConsultationRoute,
    PositiveInt64,
)


class DiagnosticEventType(StrEnum):
    CONSULTATION_RESULT = "CONSULTATION_RESULT"
    KNOWLEDGE_COMPLETED = "KNOWLEDGE_COMPLETED"
    KNOWLEDGE_FAILED = "KNOWLEDGE_FAILED"
    SUMMARY_COMPLETED = "SUMMARY_COMPLETED"
    SUMMARY_FAILED = "SUMMARY_FAILED"
    CURRENT_STATE_RESULT = "CURRENT_STATE_RESULT"


class DiagnosticFailureCode(StrEnum):
    SOURCE_FETCH_FAILED = "SOURCE_FETCH_FAILED"
    TEXT_EXTRACTION_FAILED = "TEXT_EXTRACTION_FAILED"
    UNSUPPORTED_DOCUMENT = "UNSUPPORTED_DOCUMENT"
    ENCRYPTED_DOCUMENT = "ENCRYPTED_DOCUMENT"
    CHUNK_PROFILE_INVALID = "CHUNK_PROFILE_INVALID"
    EMBEDDING_UNAVAILABLE = "EMBEDDING_UNAVAILABLE"
    VECTOR_STORE_UNAVAILABLE = "VECTOR_STORE_UNAVAILABLE"
    PROCESSING_TIMEOUT = "PROCESSING_TIMEOUT"
    CUSTOMER_AI_UNAVAILABLE = "CUSTOMER_AI_UNAVAILABLE"
    UNSAFE_CONTEXT = "UNSAFE_CONTEXT"
    SUMMARY_GENERATION_FAILED = "SUMMARY_GENERATION_FAILED"
    LLM_UNAVAILABLE = "LLM_UNAVAILABLE"
    CONTRACT_ERROR = "CONTRACT_ERROR"


class DiagnosticEvent(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    event_type: DiagnosticEventType = Field(alias="eventType")
    request_id: UUID = Field(alias="requestId")
    trace_id: str | None = Field(
        default=None, alias="traceId", pattern=r"^[0-9a-f]{32}$"
    )
    consultation_id: PositiveInt64 | None = Field(default=None, alias="consultationId")
    knowledge_version_id: PositiveInt64 | None = Field(
        default=None, alias="knowledgeVersionId"
    )
    processing_id: PositiveInt64 | None = Field(default=None, alias="processingId")
    route: ConsultationRoute | None = None
    capability_id: Capability | None = Field(default=None, alias="capabilityId")
    decision: ConsultationDecision | None = None
    availability: StateAvailability | None = None
    failure_code: DiagnosticFailureCode | None = Field(default=None, alias="failureCode")
    retryable: StrictBool | None = None
    latency_ms: Annotated[StrictInt, Field(ge=0)] | None = Field(
        default=None, alias="latencyMs"
    )
    chunk_count: Annotated[StrictInt, Field(gt=0)] | None = Field(
        default=None, alias="chunkCount"
    )

    @model_validator(mode="after")
    def validate_event_shape(self) -> "DiagnosticEvent":
        common = {"event_type", "request_id", "trace_id", "latency_ms"}
        allowed = {
            DiagnosticEventType.CONSULTATION_RESULT: common
            | {"consultation_id", "route", "decision"},
            DiagnosticEventType.KNOWLEDGE_COMPLETED: common
            | {"knowledge_version_id", "processing_id", "chunk_count"},
            DiagnosticEventType.KNOWLEDGE_FAILED: common
            | {
                "knowledge_version_id",
                "processing_id",
                "failure_code",
                "retryable",
            },
            DiagnosticEventType.SUMMARY_COMPLETED: common | {"consultation_id"},
            DiagnosticEventType.SUMMARY_FAILED: common
            | {"consultation_id", "failure_code", "retryable"},
            DiagnosticEventType.CURRENT_STATE_RESULT: common
            | {"consultation_id", "capability_id", "availability", "failure_code"},
        }[self.event_type]
        values = self.model_dump()
        populated = {name for name, value in values.items() if value is not None}
        required = allowed - common | {"event_type", "request_id"}
        if self.event_type == DiagnosticEventType.CURRENT_STATE_RESULT:
            required -= {"availability", "failure_code"}
            if (self.availability is None) == (self.failure_code is None):
                raise ValueError(
                    "Current-State diagnostics require either availability or failureCode"
                )
            if (
                self.failure_code is not None
                and self.failure_code != DiagnosticFailureCode.CONTRACT_ERROR
            ):
                raise ValueError("Current-State failureCode must be CONTRACT_ERROR")
        if not required.issubset(populated) or not populated.issubset(allowed):
            raise ValueError("diagnostic fields do not match the event type")
        return self

    def metric_dimensions(self) -> dict[str, str]:
        dimensions: dict[str, str] = {"eventType": self.event_type.value}
        candidates = {
            "route": self.route,
            "capabilityId": self.capability_id,
            "decision": self.decision,
            "availability": self.availability,
            "failureCode": self.failure_code,
        }
        for name, value in candidates.items():
            if value is not None:
                dimensions[name] = value.value
        if self.retryable is not None:
            dimensions["retryable"] = str(self.retryable).lower()
        return dimensions
