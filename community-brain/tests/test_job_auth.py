from datetime import datetime, timedelta, timezone
from types import SimpleNamespace

from cryptography.hazmat.primitives.asymmetric import rsa
import jwt
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from community_brain.jobs.auth import Authenticator, Principal
from community_brain.jobs.runtime import ProtectedRetrieval


@pytest.mark.parametrize(
    "change", [{}, {"aud": "wrong"}, {"iss": "https://wrong"}, {"exp": 1}]
)
def test_real_signed_jwt_verification(monkeypatch, change):
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    auth = Authenticator("https://issuer", "audience", "https://issuer/jwks")
    monkeypatch.setattr(
        auth.jwks,
        "get_signing_key_from_jwt",
        lambda token: SimpleNamespace(key=key.public_key()),
    )
    now = datetime.now(timezone.utc)
    claims = {
        "iss": "https://issuer",
        "aud": "audience",
        "sub": "person",
        "iat": now,
        "exp": now + timedelta(minutes=5),
        "cb_scope": "community",
        "cb_permissions": ["jobs:read"],
        **change,
    }
    token = jwt.encode(claims, key, algorithm="RS256")
    if change:
        with pytest.raises(jwt.PyJWTError):
            auth(token)
    else:
        assert auth(token) == Principal("person", "community", frozenset(["jobs:read"]))


def test_retrieval_boundary_preserves_reads_and_blocks_writes():
    inner = FastAPI()

    @inner.post("/query")
    def query():
        return {
            "chunks": [
                {
                    "ground_truth": {"full_text": "fixture"},
                    "derived_metadata": {},
                    "provenance": {},
                }
            ]
        }

    app = FastAPI()

    def auth(token):
        return Principal(
            "service",
            "community" if token == "valid" else "other",
            frozenset(["retrieval:read"]),
        )

    app.mount("/retrieval", ProtectedRetrieval(inner, auth, "community"))
    with TestClient(app) as client:
        assert (
            client.post("/retrieval/query", headers={"X-API-Key": "valid"}).status_code
            == 200
        )
        assert client.post("/retrieval/query").status_code == 401
        assert (
            client.post(
                "/retrieval/query", headers={"Authorization": "Bearer other"}
            ).status_code
            == 401
        )
        assert (
            client.post(
                "/retrieval/query", headers={"Authorization": "Bearer valid"}
            ).json()["chunks"][0]["ground_truth"]["full_text"]
            == "fixture"
        )
        assert (
            client.post(
                "/retrieval/ingest", headers={"Authorization": "Bearer valid"}
            ).status_code
            == 404
        )


@pytest.mark.parametrize("expiry", [None, 1, 4102444800])
def test_service_identity_requires_unexpired_scoped_token(expiry):
    import hashlib

    service = {
        "sha256": hashlib.sha256(b"fixture-token").hexdigest(),
        "subject": "collector",
        "scope": "community",
        "permissions": ["sources:upload:chat"],
    }
    if expiry is not None:
        service["expires_at"] = expiry
    auth = Authenticator("https://issuer", "audience", "https://issuer/jwks", [service])
    if expiry is None or expiry == 1:
        with pytest.raises(ValueError, match="expired"):
            auth("fixture-token")
    else:
        assert auth("fixture-token") == Principal(
            "collector", "community", frozenset(["sources:upload:chat"])
        )
