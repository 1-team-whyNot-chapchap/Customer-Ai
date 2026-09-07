import pytest

from chapchap_customer_ai.core.settings import Settings
from chapchap_customer_ai.security.models import AuthFailureCode, InternalAuthError
from chapchap_customer_ai.security.runtime import create_internal_auth_runtime


def test_runtime_fails_closed_when_trusted_jwks_urls_are_missing() -> None:
    with pytest.raises(InternalAuthError) as error:
        create_internal_auth_runtime(Settings(environment="local"))

    assert error.value.code == AuthFailureCode.KEY_UNAVAILABLE


def test_runtime_rejects_unapproved_trust_contract_before_activation() -> None:
    settings = Settings(
        environment="local",
        service_jwt_issuer="unapproved-auth",
        service_jwks_url="https://auth.internal/.well-known/jwks.json",
        subject_assertion_jwks_url=(
            "https://customer.internal/.well-known/customer-ai-subject-jwks.json"
        ),
    )

    with pytest.raises(InternalAuthError) as error:
        create_internal_auth_runtime(settings)

    assert error.value.code == AuthFailureCode.INVALID_TOKEN
