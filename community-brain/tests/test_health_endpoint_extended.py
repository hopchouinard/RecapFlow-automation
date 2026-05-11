"""/health returns server + corpus metadata per Tier B spec §4.2."""
from importlib.metadata import version
from fastapi.testclient import TestClient

from community_brain.ingestion.schema import SCHEMA_VERSION
from community_brain.query.retrieval_server import app


def test_health_returns_status_ok():
    client = TestClient(app)
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_health_returns_server_version():
    client = TestClient(app)
    r = client.get("/health")
    assert r.json()["server_version"] == version("community-brain")


def test_health_returns_schema_version_bare_numeric():
    """Schema version is bare numeric (e.g. '1.1'), no 'v' prefix.
    Matches community_brain.ingestion.schema.SCHEMA_VERSION format."""
    client = TestClient(app)
    r = client.get("/health")
    assert r.json()["schema_version"] == SCHEMA_VERSION
    assert not r.json()["schema_version"].startswith("v")


def test_health_returns_embedding_model_default(monkeypatch):
    """When COMMUNITY_BRAIN_EMBED_MODEL is unset, /health returns the default."""
    monkeypatch.delenv("COMMUNITY_BRAIN_EMBED_MODEL", raising=False)
    client = TestClient(app)
    r = client.get("/health")
    assert r.json()["embedding_model"] == "nomic-embed-text"


def test_health_returns_embedding_model_override(monkeypatch):
    """COMMUNITY_BRAIN_EMBED_MODEL override surfaces in /health."""
    monkeypatch.setenv("COMMUNITY_BRAIN_EMBED_MODEL", "custom-embed-model")
    client = TestClient(app)
    r = client.get("/health")
    assert r.json()["embedding_model"] == "custom-embed-model"


def test_health_distribution_mode_false_by_default(monkeypatch):
    monkeypatch.delenv("COMMUNITY_BRAIN_DISTRIBUTION_MODE", raising=False)
    client = TestClient(app)
    r = client.get("/health")
    assert r.json()["distribution_mode"] is False


def test_health_distribution_mode_true_when_env_set(monkeypatch):
    monkeypatch.setenv("COMMUNITY_BRAIN_DISTRIBUTION_MODE", "true")
    client = TestClient(app)
    r = client.get("/health")
    assert r.json()["distribution_mode"] is True


def test_health_distribution_mode_accepts_case_variants(monkeypatch):
    """Documents the case-insensitive truthy contract.

    COMMUNITY_BRAIN_DISTRIBUTION_MODE accepts any case of "true"
    (True, TRUE, tRuE, ...). This is the documented operator contract.
    """
    for value in ("true", "True", "TRUE", "tRuE"):
        monkeypatch.setenv("COMMUNITY_BRAIN_DISTRIBUTION_MODE", value)
        client = TestClient(app)
        r = client.get("/health")
        assert r.json()["distribution_mode"] is True, (
            f"value {value!r} should activate distribution_mode"
        )


def test_health_distribution_mode_rejects_non_true_truthy_strings(monkeypatch):
    """Documents that "1", "yes", "on", etc. are NOT recognized.

    Operators who write COMMUNITY_BRAIN_DISTRIBUTION_MODE=1 expecting
    boolean-style truthiness will silently get distribution_mode=False.
    The contract is the literal string "true" (case-insensitive); no
    other shape works.
    """
    for value in ("1", "yes", "on", "True ", " true", "false", ""):
        monkeypatch.setenv("COMMUNITY_BRAIN_DISTRIBUTION_MODE", value)
        client = TestClient(app)
        r = client.get("/health")
        assert r.json()["distribution_mode"] is False, (
            f"value {value!r} must NOT activate distribution_mode"
        )
