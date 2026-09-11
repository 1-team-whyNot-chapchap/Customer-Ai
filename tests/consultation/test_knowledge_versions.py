import json
from dataclasses import replace
from pathlib import Path

import pytest
from pydantic import ValidationError

from chapchap_customer_ai.consultation.knowledge_versions import RequestApprovedKnowledgeVersions
from chapchap_customer_ai.contracts.models import ConsultationResponseRequest
from chapchap_customer_ai.security.models import (
    AuthenticatedContext,
    AuthenticatedSubject,
    InternalAuthError,
)


def request(ids=None):
    data = json.loads(
        Path("tests/contract/fixtures/customer_ai_candidate_v1.json").read_text(encoding="utf-8")
    )["consultation"]["request"]
    if ids is not None:
        data["knowledgeVersionIds"] = ids
    return ConsultationResponseRequest.model_validate(data)


def context(req):
    return AuthenticatedContext(
        "customer-service",
        AuthenticatedSubject(
            req.subject.user_id,
            req.subject.role,
            frozenset(req.subject.allowed_ai_scopes),
            req.request_id,
            req.consultation_id,
        ),
    )


@pytest.mark.parametrize("ids", [[], [101, 102], [2**63 - 1]])
def test_resolves_only_customer_approved_snapshot(ids):
    req = request(ids)
    assert RequestApprovedKnowledgeVersions().resolve(context(req), req) == tuple(ids)


def test_legacy_request_has_no_permission_to_search_all_versions():
    req = request()
    assert RequestApprovedKnowledgeVersions().resolve(context(req), req) == ()


@pytest.mark.parametrize("ids", [[0], [-1], [True], ["101"], [2**63], [1, 1], list(range(1, 1002))])
def test_rejects_invalid_version_ids(ids):
    with pytest.raises(ValidationError):
        request(ids)


def test_rejects_cross_user_and_scope_mismatch():
    req = request([101])
    ctx = context(req)
    for invalid in [
        replace(ctx, service_subject="delivery-service"),
        replace(ctx, subject=replace(ctx.subject, user_id=999)),
        replace(ctx, subject=replace(ctx.subject, consultation_id=999)),
        replace(ctx, subject=replace(ctx.subject, allowed_ai_scopes=frozenset())),
    ]:
        with pytest.raises(InternalAuthError):
            RequestApprovedKnowledgeVersions().resolve(invalid, req)


def test_requires_policy_scope_even_when_context_matches():
    req = request([101])
    req.subject.allowed_ai_scopes = ["subscription.status.read"]
    with pytest.raises(InternalAuthError):
        RequestApprovedKnowledgeVersions().resolve(context(req), req)
