from fastapi.testclient import TestClient

from chapchap_customer_ai.main import create_app


def test_health_endpoint_is_available_without_exposing_api_schema() -> None:
    client = TestClient(create_app())

    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert client.get("/openapi.json").status_code == 404
