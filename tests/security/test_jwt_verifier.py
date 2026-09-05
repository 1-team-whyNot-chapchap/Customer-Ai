from collections.abc import Mapping
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any
from uuid import UUID, uuid4

import jwt
import pytest
from cryptography.hazmat.primitives.asymmetric import rsa

from chapchap_customer_ai.contracts.models import UserRole
from chapchap_customer_ai.security.jwt_verifier import INT64_MAX, InternalSecurityVerifier
from chapchap_customer_ai.security.keys import StaticVerificationKeyResolver
from chapchap_customer_ai.security.models import AuthFailureCode, InternalAuthError
from chapchap_customer_ai.security.replay import InMemoryReplayStore, ReplayEntry


@dataclass(frozen=True)
class FixedClock:
    value: int

    def now_epoch_seconds(self) -> int:
        return self.value


@pytest.fixture(scope="module")
def keys() -> dict[str, Any]:
    auth_private = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    subject_private = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    other_private = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return {
        "auth_private": auth_private,
        "auth_public": auth_private.public_key(),
        "subject_private": subject_private,
        "subject_public": subject_private.public_key(),
        "other_private": other_private,
    }


@pytest.fixture
def now() -> int:
    return int(datetime.now(UTC).timestamp())


@pytest.fixture
def request_id() -> UUID:
    return uuid4()


@pytest.fixture
def verifier(keys: Mapping[str, Any], now: int) -> InternalSecurityVerifier:
    resolver = StaticVerificationKeyResolver(
        {
            ("chapchap-auth-service", "auth-1"): keys["auth_public"],
            ("chapchap-customer-service", "subject-1"): keys["subject_public"],
        }
    )
    return InternalSecurityVerifier(resolver, InMemoryReplayStore(), FixedClock(now))


def service_claims(now: int, **overrides: Any) -> dict[str, Any]:
    claims = {
        "iss": "chapchap-auth-service",
        "sub": "customer-service",
        "aud": "chapchap-customer-ai",
        "scope": "customer-ai.invoke",
        "iat": now - 1,
        "exp": now + 299,
        "jti": str(uuid4()),
    }
    claims.update(overrides)
    return claims


def subject_claims(now: int, request_id: UUID, **overrides: Any) -> dict[str, Any]:
    claims = {
        "iss": "chapchap-customer-service",
        "aud": "chapchap-customer-ai",
        "userId": 42,
        "role": "CUSTOMER",
        "allowedAiScopes": ["customer-ai.policy.read"],
        "requestId": str(request_id),
        "consultationId": 501,
        "iat": now - 1,
        "exp": now + 59,
        "jti": str(uuid4()),
        "kid": "subject-1",
    }
    claims.update(overrides)
    return claims


def encode_rs256(claims: Mapping[str, Any], key: Any, key_id: str) -> str:
    return jwt.encode(dict(claims), key, algorithm="RS256", headers={"kid": key_id})


def verify_request(
    verifier: InternalSecurityVerifier,
    keys: Mapping[str, Any],
    now: int,
    request_id: UUID,
    *,
    service_overrides: Mapping[str, Any] | None = None,
    subject_overrides: Mapping[str, Any] | None = None,
    service_key: str = "auth_private",
    subject_key: str = "subject_private",
) -> Any:
    service = encode_rs256(
        service_claims(now, **dict(service_overrides or {})), keys[service_key], "auth-1"
    )
    subject = encode_rs256(
        subject_claims(now, request_id, **dict(subject_overrides or {})),
        keys[subject_key],
        "subject-1",
    )
    return verifier.verify(
        f"Bearer {service}",
        subject,
        expected_request_id=request_id,
        expected_consultation_id=501,
        required_subject_scope="customer-ai.policy.read",
        allowed_roles={UserRole.CUSTOMER},
    )


def test_valid_service_and_subject_tokens_return_minimal_context(
    verifier: InternalSecurityVerifier,
    keys: Mapping[str, Any],
    now: int,
    request_id: UUID,
) -> None:
    context = verify_request(verifier, keys, now, request_id)

    assert context.service_subject == "customer-service"
    assert context.subject.user_id == 42
    assert context.subject.request_id == request_id
    assert context.subject.allowed_ai_scopes == frozenset({"customer-ai.policy.read"})
    assert not hasattr(context, "service_token")
    assert not hasattr(context.subject, "assertion")


@pytest.mark.parametrize(
    ("overrides", "status_code"),
    [
        ({"sub": "other-service"}, 403),
        ({"scope": "customer-ai.callback"}, 403),
        ({"aud": "other-audience"}, 401),
        ({"iss": "other-issuer"}, 401),
        ({"exp": 1}, 401),
    ],
)
def test_service_contract_rejects_invalid_identity_claims(
    verifier: InternalSecurityVerifier,
    keys: Mapping[str, Any],
    now: int,
    request_id: UUID,
    overrides: Mapping[str, Any],
    status_code: int,
) -> None:
    with pytest.raises(InternalAuthError) as error:
        verify_request(verifier, keys, now, request_id, service_overrides=overrides)

    assert error.value.status_code == status_code


def test_service_rejects_signature_and_algorithm_confusion(
    verifier: InternalSecurityVerifier,
    keys: Mapping[str, Any],
    now: int,
    request_id: UUID,
) -> None:
    with pytest.raises(InternalAuthError) as signature_error:
        verify_request(verifier, keys, now, request_id, service_key="other_private")

    hs_token = jwt.encode(
        service_claims(now),
        "not-a-real-secret-that-is-long-enough",
        algorithm="HS256",
        headers={"kid": "auth-1"},
    )
    subject = encode_rs256(
        subject_claims(now, request_id), keys["subject_private"], "subject-1"
    )
    with pytest.raises(InternalAuthError) as algorithm_error:
        verifier.verify(
            f"Bearer {hs_token}",
            subject,
            expected_request_id=request_id,
            expected_consultation_id=501,
            required_subject_scope="customer-ai.policy.read",
            allowed_roles={UserRole.CUSTOMER},
        )

    assert signature_error.value.code == AuthFailureCode.INVALID_TOKEN
    assert algorithm_error.value.code == AuthFailureCode.INVALID_TOKEN
    assert hs_token not in str(algorithm_error.value)


def test_service_and_subject_lifetime_caps_are_enforced(
    verifier: InternalSecurityVerifier,
    keys: Mapping[str, Any],
    now: int,
    request_id: UUID,
) -> None:
    with pytest.raises(InternalAuthError):
        verify_request(
            verifier,
            keys,
            now,
            request_id,
            service_overrides={"iat": now - 1, "exp": now + 300},
        )
    with pytest.raises(InternalAuthError):
        verify_request(
            verifier,
            keys,
            now,
            request_id,
            subject_overrides={"iat": now - 1, "exp": now + 60},
        )


@pytest.mark.parametrize("user_id", ["42", 0, -1, INT64_MAX + 1, True])
def test_subject_rejects_invalid_user_id(
    verifier: InternalSecurityVerifier,
    keys: Mapping[str, Any],
    now: int,
    request_id: UUID,
    user_id: Any,
) -> None:
    with pytest.raises(InternalAuthError) as error:
        verify_request(
            verifier, keys, now, request_id, subject_overrides={"userId": user_id}
        )

    assert error.value.code == AuthFailureCode.INVALID_SUBJECT_CONTEXT
    assert error.value.status_code == 401


@pytest.mark.parametrize(
    "overrides",
    [
        {"requestId": str(uuid4())},
        {"consultationId": 999},
        {"kid": "different-key"},
    ],
)
def test_subject_rejects_mismatched_trusted_context(
    verifier: InternalSecurityVerifier,
    keys: Mapping[str, Any],
    now: int,
    request_id: UUID,
    overrides: Mapping[str, Any],
) -> None:
    with pytest.raises(InternalAuthError) as error:
        verify_request(verifier, keys, now, request_id, subject_overrides=overrides)

    assert error.value.status_code == 401


def test_subject_rejects_invalid_signature_audience_and_expiry(
    verifier: InternalSecurityVerifier,
    keys: Mapping[str, Any],
    now: int,
    request_id: UUID,
) -> None:
    with pytest.raises(InternalAuthError) as signature_error:
        verify_request(verifier, keys, now, request_id, subject_key="other_private")
    with pytest.raises(InternalAuthError) as audience_error:
        verify_request(
            verifier,
            keys,
            now,
            request_id,
            subject_overrides={"aud": "other-audience"},
        )
    with pytest.raises(InternalAuthError) as expiry_error:
        verify_request(
            verifier,
            keys,
            now,
            request_id,
            subject_overrides={"exp": 1},
        )

    assert signature_error.value.code == AuthFailureCode.INVALID_TOKEN
    assert audience_error.value.code == AuthFailureCode.INVALID_TOKEN
    assert expiry_error.value.code == AuthFailureCode.INVALID_TOKEN


@pytest.mark.parametrize(
    "overrides",
    [
        {"role": "ADMIN"},
        {"allowedAiScopes": ["subscription.status.read"]},
        {"allowedAiScopes": ["customer-ai.policy.read", "customer-ai.policy.read"]},
    ],
)
def test_subject_rejects_disallowed_role_or_scope(
    verifier: InternalSecurityVerifier,
    keys: Mapping[str, Any],
    now: int,
    request_id: UUID,
    overrides: Mapping[str, Any],
) -> None:
    with pytest.raises(InternalAuthError) as error:
        verify_request(verifier, keys, now, request_id, subject_overrides=overrides)

    assert error.value.code == AuthFailureCode.INSUFFICIENT_SCOPE
    assert error.value.status_code == 403


def test_replay_is_rejected_after_atomic_reservation(
    verifier: InternalSecurityVerifier,
    keys: Mapping[str, Any],
    now: int,
    request_id: UUID,
) -> None:
    service = encode_rs256(service_claims(now), keys["auth_private"], "auth-1")
    subject = encode_rs256(subject_claims(now, request_id), keys["subject_private"], "subject-1")
    arguments = {
        "expected_request_id": request_id,
        "expected_consultation_id": 501,
        "required_subject_scope": "customer-ai.policy.read",
        "allowed_roles": {UserRole.CUSTOMER},
    }

    verifier.verify(f"Bearer {service}", subject, **arguments)
    with pytest.raises(InternalAuthError) as error:
        verifier.verify(f"Bearer {service}", subject, **arguments)

    assert error.value.code == AuthFailureCode.TOKEN_REPLAYED


def test_invalid_subject_does_not_consume_service_replay_key(
    verifier: InternalSecurityVerifier,
    keys: Mapping[str, Any],
    now: int,
    request_id: UUID,
) -> None:
    service = encode_rs256(service_claims(now), keys["auth_private"], "auth-1")
    invalid_subject = encode_rs256(
        subject_claims(now, request_id, consultationId=999),
        keys["subject_private"],
        "subject-1",
    )
    valid_subject = encode_rs256(
        subject_claims(now, request_id), keys["subject_private"], "subject-1"
    )
    arguments = {
        "expected_request_id": request_id,
        "expected_consultation_id": 501,
        "required_subject_scope": "customer-ai.policy.read",
        "allowed_roles": {UserRole.CUSTOMER},
    }

    with pytest.raises(InternalAuthError):
        verifier.verify(f"Bearer {service}", invalid_subject, **arguments)

    context = verifier.verify(f"Bearer {service}", valid_subject, **arguments)
    assert context.subject.consultation_id == 501


def test_missing_bearer_and_unknown_key_are_safe(
    verifier: InternalSecurityVerifier,
    keys: Mapping[str, Any],
    now: int,
    request_id: UUID,
) -> None:
    with pytest.raises(InternalAuthError) as bearer_error:
        verifier.verify(
            "service-token",
            "subject-token",
            expected_request_id=request_id,
            expected_consultation_id=501,
            required_subject_scope="customer-ai.policy.read",
            allowed_roles={UserRole.CUSTOMER},
        )

    unknown_key_token = encode_rs256(service_claims(now), keys["auth_private"], "unknown")
    subject = encode_rs256(
        subject_claims(now, request_id), keys["subject_private"], "subject-1"
    )
    with pytest.raises(InternalAuthError) as key_error:
        verifier.verify(
            f"Bearer {unknown_key_token}",
            subject,
            expected_request_id=request_id,
            expected_consultation_id=501,
            required_subject_scope="customer-ai.policy.read",
            allowed_roles={UserRole.CUSTOMER},
        )

    assert bearer_error.value.code == AuthFailureCode.MISSING_CREDENTIALS
    assert key_error.value.code == AuthFailureCode.KEY_UNAVAILABLE
    assert unknown_key_token not in str(key_error.value)


def test_replay_store_reserves_all_entries_atomically_and_expires_them() -> None:
    store = InMemoryReplayStore()

    assert store.reserve([ReplayEntry("a", 20), ReplayEntry("b", 20)], now=10)
    assert not store.reserve([ReplayEntry("b", 30), ReplayEntry("c", 30)], now=10)
    assert store.reserve([ReplayEntry("b", 30), ReplayEntry("c", 30)], now=20)


def test_service_only_verification_does_not_require_subject_assertion(
    verifier: InternalSecurityVerifier,
    keys: Mapping[str, Any],
    now: int,
) -> None:
    token = encode_rs256(service_claims(now), keys["auth_private"], "auth-1")

    identity = verifier.verify_service(f"Bearer {token}")

    assert identity.service_subject == "customer-service"
    with pytest.raises(InternalAuthError) as replay_error:
        verifier.verify_service(f"Bearer {token}")
    assert replay_error.value.code == AuthFailureCode.TOKEN_REPLAYED


def test_consultation_verification_accepts_only_approved_scope_set(
    verifier: InternalSecurityVerifier,
    keys: Mapping[str, Any],
    now: int,
    request_id: UUID,
) -> None:
    service = encode_rs256(service_claims(now), keys["auth_private"], "auth-1")
    subject = encode_rs256(
        subject_claims(
            now,
            request_id,
            allowedAiScopes=["customer-ai.policy.read", "subscription.refund.read"],
        ),
        keys["subject_private"],
        "subject-1",
    )

    result = verifier.verify_consultation(
        f"Bearer {service}",
        subject,
        expected_request_id=request_id,
        expected_consultation_id=501,
        allowed_subject_scopes={
            "customer-ai.policy.read",
            "subscription.refund.read",
        },
        allowed_roles={UserRole.CUSTOMER},
    )

    assert result.subject.allowed_ai_scopes == frozenset(
        {"customer-ai.policy.read", "subscription.refund.read"}
    )


def test_consultation_verification_rejects_unknown_scope(
    verifier: InternalSecurityVerifier,
    keys: Mapping[str, Any],
    now: int,
    request_id: UUID,
) -> None:
    service = encode_rs256(service_claims(now), keys["auth_private"], "auth-1")
    subject = encode_rs256(
        subject_claims(now, request_id, allowedAiScopes=["unknown.scope"]),
        keys["subject_private"],
        "subject-1",
    )

    with pytest.raises(InternalAuthError) as error:
        verifier.verify_consultation(
            f"Bearer {service}",
            subject,
            expected_request_id=request_id,
            expected_consultation_id=501,
            allowed_subject_scopes={"customer-ai.policy.read"},
            allowed_roles={UserRole.CUSTOMER},
        )

    assert error.value.status_code == 403
