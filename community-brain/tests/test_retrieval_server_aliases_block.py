"""Tests for GET /speaker-aliases-block endpoint."""

from __future__ import annotations

from pathlib import Path

import yaml
from fastapi.testclient import TestClient

from community_brain.query import retrieval_server as server_mod


def _write_speaker_yaml(path: Path, aliases: dict[str, list[str]], pending: list[str]) -> None:
    path.write_text(
        yaml.safe_dump({"version": "test", "aliases": aliases, "pending": pending}),
        encoding="utf-8",
    )


def test_get_speaker_aliases_block_returns_rendered_block(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(tmp_path))

    _write_speaker_yaml(tmp_path / "speaker-aliases.yaml", {"Alex Rojas": ["alexrojas"]}, [])

    client = TestClient(server_mod.app)
    response = client.get("/speaker-aliases-block")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/plain")
    assert "## SPEAKER_ALIASES" in response.text
    assert "- Alex Rojas — aliases: alexrojas" in response.text


def test_get_speaker_aliases_block_empty_registry(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(tmp_path))

    _write_speaker_yaml(tmp_path / "speaker-aliases.yaml", {}, [])

    client = TestClient(server_mod.app)
    response = client.get("/speaker-aliases-block")

    assert response.status_code == 200
    # Header still present; no bullet lines
    assert "## SPEAKER_ALIASES" in response.text
    assert "\n- " not in response.text


def test_get_speaker_aliases_block_403_when_api_key_enabled_and_missing_header(
    monkeypatch, tmp_path: Path
) -> None:
    monkeypatch.setenv("RETRIEVAL_API_KEY", "secret-test-key")
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(tmp_path))
    _write_speaker_yaml(tmp_path / "speaker-aliases.yaml", {}, [])

    client = TestClient(server_mod.app)
    response = client.get("/speaker-aliases-block")

    assert response.status_code == 403


def test_get_speaker_aliases_block_200_when_api_key_enabled_and_header_matches(
    monkeypatch, tmp_path: Path
) -> None:
    monkeypatch.setenv("RETRIEVAL_API_KEY", "secret-test-key")
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(tmp_path))
    _write_speaker_yaml(tmp_path / "speaker-aliases.yaml", {}, [])

    client = TestClient(server_mod.app)
    response = client.get("/speaker-aliases-block", headers={"X-API-Key": "secret-test-key"})

    assert response.status_code == 200


def test_get_speaker_aliases_block_503_when_yaml_missing(monkeypatch, tmp_path: Path) -> None:
    """When speaker-aliases.yaml is absent, endpoint returns 503 with a
    message naming the expected path (operator-recoverable)."""
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(tmp_path))
    # Note: NO yaml file written to tmp_path.

    client = TestClient(server_mod.app)
    response = client.get("/speaker-aliases-block")

    assert response.status_code == 503
    assert "speaker-aliases.yaml" in response.json()["detail"]


def test_get_speaker_aliases_block_500_when_yaml_malformed(monkeypatch, tmp_path: Path) -> None:
    """When speaker-aliases.yaml is structurally invalid, endpoint returns
    500 with a message mentioning malformed input."""
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(tmp_path))
    # Write something yaml-parsable but NOT a dict (load_speaker_registry
    # expects aliases: {canonical: [...]} structure)
    (tmp_path / "speaker-aliases.yaml").write_text("just a plain string", encoding="utf-8")

    client = TestClient(server_mod.app)
    response = client.get("/speaker-aliases-block")

    assert response.status_code == 500
    assert "malformed" in response.json()["detail"].lower()
