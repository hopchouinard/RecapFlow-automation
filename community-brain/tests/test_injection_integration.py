"""End-to-end cue-driven injection through search_chunks (v5 D2, D6, D7).

Seeds the golden corpus, points COMMUNITY_BRAIN_CUE_RULES_PATH at a
recruit-enabled cue YAML, and proves a quiet session invisible to both
hybrid legs is recruited into top_k — and missed without recruitment
(the pool-limit finding reproduced in miniature).
"""
from __future__ import annotations

import sys
from pathlib import Path

import lancedb
import pytest

from community_brain.ingestion.schema import EMBEDDING_DIM
from community_brain.query.fts_lifecycle import ensure_fts_index, optimize_fts_index
from community_brain.query.query_local import search_chunks

FIXTURES_DIR = Path(__file__).parent / "fixtures"

RECRUIT_CUES_YAML = """
cue_rules:
  - name: date_iso_match
    question_regex: '\\b(\\d{4}-\\d{2}-\\d{2})\\b'
    match_field: session_date
    match_strategy: iso_date_equals
    delta: 0.04
    recruit: true
"""

QUESTION = "What was discussed on 2025-12-30?"


@pytest.fixture()
def injection_db(tmp_path):
    sys.path.insert(0, str(FIXTURES_DIR / "golden_corpus"))
    from seed import seed  # type: ignore

    db_path = tmp_path / "golden_db"
    seed(str(db_path))
    db = lancedb.connect(str(db_path))
    table = db.open_table("chunks")
    ensure_fts_index(table, "bm25_text")
    optimize_fts_index(table, "bm25_text")
    return str(db_path)


@pytest.fixture()
def recruit_cues(tmp_path, monkeypatch):
    p = tmp_path / "query-cues.yaml"
    p.write_text(RECRUIT_CUES_YAML)
    monkeypatch.setenv("COMMUNITY_BRAIN_CUE_RULES_PATH", str(p))
    monkeypatch.setenv(
        "COMMUNITY_BRAIN_SPEAKER_ALIASES_PATH", str(tmp_path / "missing-aliases.yaml")
    )


@pytest.fixture()
def boost_only_cues(tmp_path, monkeypatch):
    p = tmp_path / "query-cues-boost-only.yaml"
    p.write_text(RECRUIT_CUES_YAML.replace("\n    recruit: true", ""))
    monkeypatch.setenv("COMMUNITY_BRAIN_CUE_RULES_PATH", str(p))
    monkeypatch.setenv(
        "COMMUNITY_BRAIN_SPEAKER_ALIASES_PATH", str(tmp_path / "missing-aliases.yaml")
    )


@pytest.fixture()
def fake_embed(monkeypatch):
    def _embed(model, input):
        return {"embeddings": [[0.5] * EMBEDDING_DIM]}

    import ollama

    monkeypatch.setattr(ollama, "embed", _embed)


def test_iso_date_query_recruits_quiet_session(injection_db, recruit_cues, fake_embed):
    result = search_chunks(
        question=QUESTION, db_path=injection_db, top_k=5, filters=None
    )
    ids = [c["chunk_id"] for c in result["chunks"]]
    assert "v5-quiet-1" in ids
    assert "v5-quiet-2" in ids


def test_quiet_session_missed_without_recruit(injection_db, boost_only_cues, fake_embed):
    """The pool-limit finding: the same rule as boost-only cannot rescue
    chunks that never entered the candidate pool."""
    result = search_chunks(
        question=QUESTION, db_path=injection_db, top_k=5, filters=None
    )
    ids = [c["chunk_id"] for c in result["chunks"]]
    assert "v5-quiet-1" not in ids
    assert "v5-quiet-2" not in ids


def test_injected_chunks_report_injected_by(injection_db, recruit_cues, fake_embed):
    result = search_chunks(
        question=QUESTION, db_path=injection_db, top_k=5, filters=None
    )
    by_id = {c["chunk_id"]: c for c in result["chunks"]}
    quiet = by_id["v5-quiet-1"]
    assert quiet["score_breakdown"]["injected_by"] == ["date_iso_match"]
    assert quiet["score_breakdown"]["rrf_score"] == 0.0
    assert quiet["score_breakdown"]["cue_delta"] == pytest.approx(0.04)
    assert "date_iso_match" in quiet["score_breakdown"]["cue_rules_fired"]


def test_pool_native_chunks_report_empty_injected_by(injection_db, recruit_cues, fake_embed):
    result = search_chunks(
        question=QUESTION, db_path=injection_db, top_k=5, filters=None
    )
    natives = [
        c for c in result["chunks"] if c["chunk_id"] not in ("v5-quiet-1", "v5-quiet-2")
    ]
    assert natives, "expected some pool-native chunks in top_k"
    for c in natives:
        assert c["score_breakdown"]["injected_by"] == []


def test_injection_respects_user_filters(injection_db, recruit_cues, fake_embed):
    result = search_chunks(
        question=QUESTION,
        db_path=injection_db,
        top_k=5,
        filters={"session_date_range": ["2026-01-01", "2026-12-31"]},
    )
    ids = [c["chunk_id"] for c in result["chunks"]]
    assert "v5-quiet-1" not in ids
    assert "v5-quiet-2" not in ids
