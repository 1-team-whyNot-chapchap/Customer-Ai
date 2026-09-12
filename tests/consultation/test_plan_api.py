from uuid import uuid4

from fastapi import FastAPI
from fastapi.testclient import TestClient

from chapchap_customer_ai.api.consultation import build_candidate_consultation_router
from tests.consultation.test_candidate_api import Verifier, payload
from tests.consultation.test_response_service import Dependencies


def client(monkeypatch, enabled):
    monkeypatch.setenv("CONSULTATION_BOUNDARIES_ENABLED", str(enabled).lower())
    app = FastAPI()
    app.include_router(build_candidate_consultation_router(Dependencies().service(), Verifier()))
    return TestClient(app)


def headers(request_id):
    return {
        "Authorization": "Bearer service-token",
        "X-Subject-Assertion": "signed-subject",
        "X-Request-Id": request_id,
        "Idempotency-Key": "plan-test",
    }


def test_two_phase_notice_contract(monkeypatch):
    api = client(monkeypatch, True)
    id = str(uuid4())
    request = {**payload(id), "message": "내일 배송 상태 알려줘"}
    response = api.post(
        "/internal/v1/consultation-interpretations", headers=headers(id), json=request
    )
    assert response.status_code == 200
    plan = response.json()
    assert set(plan) == {"schemaVersion", "requestId", "planId", "route", "capabilities"}
    assert plan["route"] == "UNSUPPORTED" and plan["capabilities"] == []
    execution = api.post(
        "/internal/v1/consultation-plan-responses",
        headers=headers(id),
        json={"planId": plan["planId"], "request": request},
    )
    assert execution.status_code == 200
    assert "요청하신 기간" in execution.json()["answer"]
    altered = api.post(
        "/internal/v1/consultation-plan-responses",
        headers=headers(id),
        json={"planId": plan["planId"], "request": {**request, "message": "내 배송 상태"}},
    )
    assert altered.status_code == 409


def test_feature_off_cannot_activate_new_calls(monkeypatch):
    api = client(monkeypatch, False)
    id = str(uuid4())
    assert (
        api.post(
            "/internal/v1/consultation-interpretations", headers=headers(id), json=payload(id)
        ).status_code
        == 404
    )


def test_header_and_unsigned_extra_fields_are_rejected(monkeypatch):
    api = client(monkeypatch, True)
    id = str(uuid4())
    assert (
        api.post(
            "/internal/v1/consultation-interpretations",
            headers=headers(str(uuid4())),
            json=payload(id),
        ).status_code
        == 400
    )
    assert (
        api.post(
            "/internal/v1/consultation-interpretations",
            headers=headers(id),
            json={**payload(id), "scope": "admin"},
        ).status_code
        == 422
    )
