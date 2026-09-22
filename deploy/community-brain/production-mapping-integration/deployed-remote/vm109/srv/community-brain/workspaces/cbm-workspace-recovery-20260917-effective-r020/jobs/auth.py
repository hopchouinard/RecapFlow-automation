from dataclasses import dataclass
import hashlib
import hmac
import time

import jwt


@dataclass(frozen=True)
class Principal:
    subject: str
    scope: str
    permissions: frozenset[str]


class Authenticator:
    """OIDC JWT verification plus independently scoped opaque service identities."""

    def __init__(self, issuer, audience, jwks_url, services=()):
        if not issuer.startswith("https://") or not jwks_url.startswith("https://"):
            raise ValueError("OIDC requires HTTPS")
        self.issuer, self.audience = issuer, audience
        self.jwks = jwt.PyJWKClient(jwks_url, cache_keys=True, timeout=5)
        self.services = services

    def __call__(self, token):
        hashed = hashlib.sha256(token.encode()).hexdigest()
        for service in self.services:
            if hmac.compare_digest(hashed, service["sha256"]):
                if service.get("expires_at", 0) <= time.time():
                    raise ValueError("service identity expired")
                return Principal(
                    service["subject"],
                    service["scope"],
                    frozenset(service["permissions"]),
                )
        key = self.jwks.get_signing_key_from_jwt(token).key
        claims = jwt.decode(
            token,
            key,
            algorithms=["RS256"],
            audience=self.audience,
            issuer=self.issuer,
            options={
                "require": [
                    "exp",
                    "iat",
                    "sub",
                    "iss",
                    "aud",
                    "cb_scope",
                    "cb_permissions",
                ]
            },
        )
        if not isinstance(claims["cb_scope"], str) or not isinstance(
            claims["cb_permissions"], list
        ):
            raise ValueError("invalid authorization claims")
        return Principal(
            claims["sub"], claims["cb_scope"], frozenset(claims["cb_permissions"])
        )
