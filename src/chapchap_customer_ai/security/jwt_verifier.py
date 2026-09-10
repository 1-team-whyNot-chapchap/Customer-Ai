from collections.abc import Collection, Mapping
from dataclasses import dataclass
from typing import Any
from urllib.parse import urlsplit
from uuid import UUID

import jwt

from chapchap_customer_ai.contracts.models import UserRole
from chapchap_customer_ai.core.settings import Settings
from chapchap_customer_ai.security.clock import Clock, SystemClock
from chapchap_customer_ai.security.keys import (
    JwksVerificationKeyResolver,
    VerificationKeyResolver,
)
from chapchap_customer_ai.security.models import (
    AuthenticatedContext,
    AuthenticatedService,
    AuthenticatedSubject,
    AuthFailureCode,
    InternalAuthError,
)
from chapchap_customer_ai.security.transport import allowed_url

INT64_MAX = 9_223_372_036_854_775_807


@dataclass(frozen=True, slots=True)
class InternalSecurityVerifier:
    key_resolver: VerificationKeyResolver
    clock: Clock = SystemClock()
    service_issuer: str = "chapchap-auth-service"
    subject_issuer: str = "chapchap-customer-service"
    audience: str = "chapchap-customer-ai"
    service_subject: str = "customer-service"
    service_scope: str = "customer-ai.invoke"
    service_max_lifetime_seconds: int = 300
    subject_max_lifetime_seconds: int = 60

    def verify_service(self, authorization: str) -> AuthenticatedService:
        self._verified_service_claims(authorization)
        return AuthenticatedService(self.service_subject)

    def verify(
        self,
        authorization: str,
        subject_assertion: str,
        *,
        expected_request_id: UUID,
        expected_consultation_id: int,
        required_subject_scope: str,
        allowed_roles: Collection[UserRole],
    ) -> AuthenticatedContext:
        if not isinstance(expected_request_id, UUID):
            raise ValueError("expected_request_id must be a UUID")
        if (
            isinstance(expected_consultation_id, bool)
            or not isinstance(expected_consultation_id, int)
            or expected_consultation_id <= 0
            or expected_consultation_id > INT64_MAX
        ):
            raise ValueError("expected_consultation_id must be a positive int64")
        if not required_subject_scope.strip() or not allowed_roles:
            raise ValueError("required subject scope and allowed roles must be non-empty")
        self._verified_service_claims(authorization)

        subject_claims = self._decode(
            subject_assertion,
            issuer=self.subject_issuer,
            required_claims=(
                "userId",
                "role",
                "allowedAiScopes",
                "requestId",
                "consultationId",
                "iat",
                "exp",
                "jti",
                "kid",
            ),
            require_key_id_claim=True,
        )
        subject = self._verify_subject_claims(
            subject_claims,
            expected_request_id=expected_request_id,
            expected_consultation_id=expected_consultation_id,
            required_scope=required_subject_scope,
            allowed_roles=allowed_roles,
        )

        return AuthenticatedContext(self.service_subject, subject)

    def verify_consultation(
        self,
        authorization: str,
        subject_assertion: str,
        *,
        expected_request_id: UUID,
        expected_consultation_id: int,
        allowed_subject_scopes: Collection[str],
        allowed_roles: Collection[UserRole],
    ) -> AuthenticatedContext:
        if not isinstance(expected_request_id, UUID):
            raise ValueError("expected_request_id must be a UUID")
        if (
            isinstance(expected_consultation_id, bool)
            or not isinstance(expected_consultation_id, int)
            or expected_consultation_id <= 0
            or expected_consultation_id > INT64_MAX
        ):
            raise ValueError("expected_consultation_id must be a positive int64")
        if not allowed_subject_scopes or not allowed_roles:
            raise ValueError("allowed subject scopes and roles must be non-empty")
        self._verified_service_claims(authorization)
        subject_claims = self._decode(
            subject_assertion,
            issuer=self.subject_issuer,
            required_claims=(
                "userId",
                "role",
                "allowedAiScopes",
                "requestId",
                "consultationId",
                "iat",
                "exp",
                "jti",
                "kid",
            ),
            require_key_id_claim=True,
        )
        subject = self._verify_subject_claims(
            subject_claims,
            expected_request_id=expected_request_id,
            expected_consultation_id=expected_consultation_id,
            required_scope=None,
            allowed_scopes=allowed_subject_scopes,
            allowed_roles=allowed_roles,
        )
        return AuthenticatedContext(self.service_subject, subject)

    def _verified_service_claims(self, authorization: str) -> Mapping[str, Any]:
        service_token = self._bearer_token(authorization)
        service_claims = self._decode(
            service_token,
            issuer=self.service_issuer,
            required_claims=("sub", "scope", "iat", "exp", "jti"),
        )
        self._verify_service_claims(service_claims)
        return service_claims

    @staticmethod
    def _bearer_token(authorization: str) -> str:
        if not isinstance(authorization, str):
            raise InternalSecurityVerifier._authentication_error(
                AuthFailureCode.MISSING_CREDENTIALS,
                "A Bearer service token is required.",
            )
        parts = authorization.strip().split()
        if len(parts) != 2 or parts[0].lower() != "bearer" or not parts[1]:
            raise InternalSecurityVerifier._authentication_error(
                AuthFailureCode.MISSING_CREDENTIALS,
                "A Bearer service token is required.",
            )
        return parts[1]

    def _decode(
        self,
        token: str,
        *,
        issuer: str,
        required_claims: tuple[str, ...],
        require_key_id_claim: bool = False,
    ) -> Mapping[str, Any]:
        if not isinstance(token, str) or not token.strip():
            raise self._authentication_error(
                AuthFailureCode.MISSING_CREDENTIALS,
                "A signed token is required.",
            )
        try:
            header = jwt.get_unverified_header(token)
        except jwt.PyJWTError:
            raise self._authentication_error(
                AuthFailureCode.INVALID_TOKEN,
                "The signed token is invalid.",
            ) from None
        algorithm = header.get("alg")
        key_id = header.get("kid")
        if algorithm != "RS256" or not isinstance(key_id, str) or not key_id.strip():
            raise self._authentication_error(
                AuthFailureCode.INVALID_TOKEN,
                "The signed token uses an unsupported header.",
            )
        try:
            key = self.key_resolver.resolve(issuer, key_id)
        except InternalAuthError:
            raise
        except Exception:
            raise self._authentication_error(
                AuthFailureCode.KEY_UNAVAILABLE,
                "A trusted verification key is unavailable.",
            ) from None
        try:
            claims = jwt.decode(
                token,
                key,
                algorithms=["RS256"],
                audience=self.audience,
                issuer=issuer,
                options={"require": list(required_claims)},
            )
        except jwt.PyJWTError:
            raise self._authentication_error(
                AuthFailureCode.INVALID_TOKEN,
                "The signed token could not be verified.",
            ) from None
        if require_key_id_claim and claims.get("kid") != key_id:
            raise self._authentication_error(
                AuthFailureCode.INVALID_TOKEN,
                "The signed token key identifier is inconsistent.",
            )
        return claims

    def _verify_service_claims(self, claims: Mapping[str, Any]) -> None:
        if claims.get("sub") != self.service_subject:
            raise self._authorization_error("The service identity is not allowed.")
        scope = claims.get("scope")
        if not isinstance(scope, str) or self.service_scope not in scope.split():
            raise self._authorization_error("The service scope is not allowed.")
        self._verify_lifetime(claims, self.service_max_lifetime_seconds)
        self._text(claims, "jti")

    def _verify_subject_claims(
        self,
        claims: Mapping[str, Any],
        *,
        expected_request_id: UUID,
        expected_consultation_id: int,
        required_scope: str | None,
        allowed_scopes: Collection[str] | None = None,
        allowed_roles: Collection[UserRole],
    ) -> AuthenticatedSubject:
        self._verify_lifetime(claims, self.subject_max_lifetime_seconds)
        user_id = self._positive_int64(claims.get("userId"), "userId")
        consultation_id = self._positive_int64(claims.get("consultationId"), "consultationId")
        if consultation_id != expected_consultation_id:
            raise self._subject_error("The subject consultation context does not match.")
        try:
            request_id = UUID(claims["requestId"])
        except (KeyError, TypeError, ValueError, AttributeError):
            raise self._subject_error("The subject request context is invalid.") from None
        if request_id != expected_request_id:
            raise self._subject_error("The subject request context does not match.")
        try:
            role = UserRole(claims["role"])
        except (KeyError, TypeError, ValueError):
            raise self._authorization_error("The subject role is not allowed.") from None
        if role not in allowed_roles:
            raise self._authorization_error("The subject role is not allowed.")
        raw_scopes = claims.get("allowedAiScopes")
        if (
            not isinstance(raw_scopes, list)
            or not raw_scopes
            or any(not isinstance(scope, str) or not scope.strip() for scope in raw_scopes)
        ):
            raise self._authorization_error("The subject scope is not allowed.")
        scopes = frozenset(raw_scopes)
        if len(scopes) != len(raw_scopes):
            raise self._authorization_error("The subject scope is not allowed.")
        if required_scope is not None and required_scope not in scopes:
            raise self._authorization_error("The subject scope is not allowed.")
        if allowed_scopes is not None and not scopes.issubset(set(allowed_scopes)):
            raise self._authorization_error("The subject scope is not allowed.")
        self._text(claims, "jti")
        return AuthenticatedSubject(user_id, role, scopes, request_id, consultation_id)

    def _verify_lifetime(self, claims: Mapping[str, Any], maximum_seconds: int) -> None:
        issued_at = self._numeric_date(claims.get("iat"), "iat")
        expires_at = self._numeric_date(claims.get("exp"), "exp")
        now = self.clock.now_epoch_seconds()
        if issued_at > now or expires_at <= now or expires_at <= issued_at:
            raise self._authentication_error(
                AuthFailureCode.INVALID_TOKEN,
                "The signed token lifetime is invalid.",
            )
        if expires_at - issued_at > maximum_seconds:
            raise self._authentication_error(
                AuthFailureCode.INVALID_TOKEN,
                "The signed token lifetime exceeds the allowed maximum.",
            )

    @staticmethod
    def _numeric_date(value: Any, field_name: str) -> int:
        if isinstance(value, bool) or not isinstance(value, int):
            raise InternalSecurityVerifier._subject_error(
                f"The token {field_name} claim is invalid."
            )
        return value

    @staticmethod
    def _positive_int64(value: Any, field_name: str) -> int:
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0 or value > INT64_MAX:
            raise InternalSecurityVerifier._subject_error(
                f"The subject {field_name} claim is invalid."
            )
        return value

    @staticmethod
    def _text(claims: Mapping[str, Any], field_name: str) -> str:
        value = claims.get(field_name)
        if not isinstance(value, str) or not value.strip():
            raise InternalSecurityVerifier._authentication_error(
                AuthFailureCode.INVALID_TOKEN,
                f"The token {field_name} claim is invalid.",
            )
        return value

    @staticmethod
    def _authentication_error(code: AuthFailureCode, message: str) -> InternalAuthError:
        return InternalAuthError(code, 401, message)

    @staticmethod
    def _authorization_error(message: str) -> InternalAuthError:
        return InternalAuthError(AuthFailureCode.INSUFFICIENT_SCOPE, 403, message)

    @staticmethod
    def _subject_error(message: str) -> InternalAuthError:
        return InternalAuthError(AuthFailureCode.INVALID_SUBJECT_CONTEXT, 401, message)


def create_internal_security_verifier(settings: Settings) -> InternalSecurityVerifier:
    if (
        settings.service_jwt_issuer != "chapchap-auth-service"
        or settings.subject_assertion_issuer != "chapchap-customer-service"
        or settings.service_jwt_audience != "chapchap-customer-ai"
    ):
        raise InternalAuthError(
            AuthFailureCode.INVALID_TOKEN,
            401,
            "The configured trust contract is not approved.",
        )
    urls = {
        settings.service_jwt_issuer: settings.service_jwks_url,
        settings.subject_assertion_issuer: settings.subject_assertion_jwks_url,
    }
    if any(not url or not allowed_url(url, settings.http_allowed_origins) for url in urls.values()):
        raise InternalAuthError(
            AuthFailureCode.KEY_UNAVAILABLE,
            401,
            "Trusted JWKS endpoints are not configured.",
        )
    resolver = JwksVerificationKeyResolver.from_urls(
        {issuer: url for issuer, url in urls.items() if url is not None},
        timeout_seconds=settings.jwks_timeout_seconds,
        cache_lifespan_seconds=settings.jwks_cache_lifespan_seconds,
    )
    return InternalSecurityVerifier(
        resolver,
        service_issuer=settings.service_jwt_issuer,
        subject_issuer=settings.subject_assertion_issuer,
        audience=settings.service_jwt_audience,
    )


def _is_trusted_https_url(url: str) -> bool:
    try:
        parsed = urlsplit(url)
    except (TypeError, ValueError):
        return False
    return (
        parsed.scheme == "https"
        and bool(parsed.hostname)
        and parsed.username is None
        and parsed.password is None
        and not parsed.fragment
    )
