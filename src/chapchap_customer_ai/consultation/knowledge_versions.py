from chapchap_customer_ai.contracts.models import ConsultationResponseRequest, UserRole
from chapchap_customer_ai.security.models import (
    AuthenticatedContext,
    AuthFailureCode,
    InternalAuthError,
)


class RequestApprovedKnowledgeVersions:
    """Customer-Service supplies its approved snapshot over the authenticated API."""

    def resolve(
        self, context: AuthenticatedContext, request: ConsultationResponseRequest
    ) -> tuple[int, ...]:
        subject = context.subject
        if (
            context.service_subject != "customer-service"
            or subject.role not in {UserRole.CUSTOMER, UserRole.RIDER}
            or subject.request_id != request.request_id
            or subject.consultation_id != request.consultation_id
            or subject.user_id != request.subject.user_id
            or subject.role != request.subject.role
            or subject.allowed_ai_scopes != frozenset(request.subject.allowed_ai_scopes)
        ):
            raise InternalAuthError(
                AuthFailureCode.INVALID_SUBJECT_CONTEXT, 403, "Invalid knowledge context"
            )
        if "customer-ai.policy.read" not in subject.allowed_ai_scopes:
            raise InternalAuthError(
                AuthFailureCode.INSUFFICIENT_SCOPE, 403, "Policy scope required"
            )
        return tuple(request.knowledge_version_ids)
