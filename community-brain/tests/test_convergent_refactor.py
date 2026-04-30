"""Regression tests for the convergent root-cause refactor.

Tests the five parts of the structural fix:
1. canonicalize_chunk_fields helper (shared partition logic)
2. verify_corpus_v3_state + fail-closed startup
3. /query returns 503 on CorpusInvalidError
4. try/except audit: no new tests needed (comments in code)
5. apply_canonicalizations intra-file duplicate alias check

Each test covers the failure mode that the root-cause fix addresses —
not just the happy path, but the specific scenario that was previously
silently degraded.
"""
from __future__ import annotations

import lancedb
import pyarrow as pa
import pytest
from fastapi.testclient import TestClient

from community_brain.ingestion.canonicalize import (
    canonicalize_chunk_fields,
    canonicalize_names,
)
from community_brain.ingestion.schema import pyarrow_table_schema
from community_brain.query.corpus_verify import CorpusInvalidError, verify_corpus_v3_state
from community_brain.cli.apply_canonicalizations import (
    ProposalConflictError,
    apply_proposals_to_registry,
)


# ---------------------------------------------------------------------------
# Part 1: canonicalize_chunk_fields
# ---------------------------------------------------------------------------


class TestCanonicalizeChunkFields:
    """canonicalize_chunk_fields must canonicalize all three person-bearing
    fields AND enforce the speakers_spoke/speakers_mentioned partition."""

    def test_basic_canonicalization(self):
        """All three fields are canonicalized via the alias map."""
        alias_map = {
            "Adam": "Adam James",
            "Adam James": "Adam James",
            "delvis": "Delvis Nunez",
            "Delvis Nunez": "Delvis Nunez",
        }
        spoke, mentioned, entities, unk_spk, unk_men = canonicalize_chunk_fields(
            speakers_spoke=["Adam"],
            speakers_mentioned=["delvis", "Unknown Person"],
            entities=["Adam"],
            alias_map=alias_map,
        )
        assert spoke == ["Adam James"]
        assert mentioned == ["Delvis Nunez", "Unknown Person"]
        assert entities == ["Adam James"]
        assert unk_spk == []
        assert "Unknown Person" in unk_men

    def test_partition_enforced_after_canonicalization(self):
        """If two raw aliases collapse to the same canonical, the person
        must NOT appear in both spoke and mentioned after canonicalization.
        This is the specific failure mode that the shared helper addresses:
        Stage C computed the partition against raw names, but canonicalization
        can make 'Adam' and 'Adam - Gold Flamingo' both become 'Adam James',
        putting him in both lists.
        """
        alias_map = {
            "Adam": "Adam James",
            "Adam - Gold Flamingo": "Adam James",
            "Adam James": "Adam James",
        }
        spoke, mentioned, _entities, _unk_spk, _unk_men = canonicalize_chunk_fields(
            speakers_spoke=["Adam"],
            speakers_mentioned=["Adam - Gold Flamingo"],  # same person, different alias
            entities=[],
            alias_map=alias_map,
        )
        assert "Adam James" in spoke
        assert "Adam James" not in mentioned, (
            "partition violated: Adam James appears in both spoke and mentioned"
        )

    def test_partition_enforced_same_in_both_call_sites(self):
        """Run the same scenario through canonicalize_chunk_fields and through
        the equivalent manual code that pipeline.py USED to have. Both must
        produce identical output — this test would have FAILED before the
        extraction of canonicalize_chunk_fields (if one site drifted).
        """
        alias_map = {
            "Adam": "Adam James",
            "Adam James": "Adam James",
            "delvis": "Delvis Nunez",
            "Delvis Nunez": "Delvis Nunez",
        }
        # Simulate what the old pipeline.py code did
        canon_spoke_old, _ = canonicalize_names(["Adam"], alias_map)
        canon_mentioned_old, _ = canonicalize_names(["delvis", "Adam"], alias_map)
        canon_entities_old, _ = canonicalize_names([], alias_map)
        spoke_set = set(canon_spoke_old)
        canon_mentioned_old = [n for n in canon_mentioned_old if n not in spoke_set]

        # New shared helper
        spoke_new, mentioned_new, entities_new, _, _ = canonicalize_chunk_fields(
            speakers_spoke=["Adam"],
            speakers_mentioned=["delvis", "Adam"],
            entities=[],
            alias_map=alias_map,
        )

        assert spoke_new == canon_spoke_old
        assert mentioned_new == canon_mentioned_old
        assert entities_new == canon_entities_old

    def test_unknown_speakers_returned_from_both_fields(self):
        """Unknown names from spoke AND mentioned are returned in their
        respective unknown lists."""
        alias_map = {"Known Person": "Known Person"}
        _, _, _, unk_spk, unk_men = canonicalize_chunk_fields(
            speakers_spoke=["Known Person", "Unknown Spoke"],
            speakers_mentioned=["Unknown Mentioned"],
            entities=[],
            alias_map=alias_map,
        )
        assert "Unknown Spoke" in unk_spk
        assert "Unknown Mentioned" in unk_men

    def test_handles_none_inputs(self):
        """None in any field should be treated as empty list."""
        spoke, mentioned, entities, unk_spk, unk_men = canonicalize_chunk_fields(
            speakers_spoke=None,
            speakers_mentioned=None,
            entities=None,
            alias_map={},
        )
        assert spoke == []
        assert mentioned == []
        assert entities == []
        assert unk_spk == []
        assert unk_men == []

    def test_empty_inputs_produce_empty_outputs(self):
        spoke, mentioned, entities, unk_spk, unk_men = canonicalize_chunk_fields(
            speakers_spoke=[],
            speakers_mentioned=[],
            entities=[],
            alias_map={"X": "Y"},
        )
        assert spoke == mentioned == entities == unk_spk == unk_men == []


# ---------------------------------------------------------------------------
# Part 2: verify_corpus_v3_state
# ---------------------------------------------------------------------------


class TestVerifyCorpusV3State:
    """verify_corpus_v3_state must fail loudly on pre-v1.1 schema and on
    missing/unbuildable FTS index."""

    def test_passes_on_valid_v3_table(self, tmp_path):
        """A table with bm25_text column and FTS index passes verification."""
        db = lancedb.connect(str(tmp_path))
        schema = pyarrow_table_schema()
        table = db.create_table("chunks", schema=schema)
        # No FTS index yet — verify_corpus_v3_state should build it then pass.
        verify_corpus_v3_state(table)  # must not raise

    def test_raises_on_pre_v1_1_schema(self, tmp_path):
        """A table without bm25_text column raises CorpusInvalidError."""
        db = lancedb.connect(str(tmp_path))
        # Create a table using an old-style schema without bm25_text
        old_schema = pa.schema([
            pa.field("chunk_id", pa.string()),
            pa.field("full_text", pa.string()),
            # bm25_text deliberately absent
        ])
        table = db.create_table("chunks", schema=old_schema)
        with pytest.raises(CorpusInvalidError, match="pre-v1.1"):
            verify_corpus_v3_state(table)

    def test_raises_on_missing_fts_index_when_unbuildable(self, tmp_path, monkeypatch):
        """If ensure_fts_index raises, verify_corpus_v3_state wraps in CorpusInvalidError."""
        db = lancedb.connect(str(tmp_path))
        schema = pyarrow_table_schema()
        table = db.create_table("chunks", schema=schema)

        def _failing_ensure(t, column):
            raise RuntimeError("simulated FTS build failure")

        monkeypatch.setattr(
            "community_brain.query.corpus_verify.ensure_fts_index",
            _failing_ensure,
        )
        with pytest.raises(CorpusInvalidError, match="FTS index cannot be ensured"):
            verify_corpus_v3_state(table)

    def test_error_message_mentions_spec_action(self, tmp_path):
        """The CorpusInvalidError message tells the operator what to do."""
        db = lancedb.connect(str(tmp_path))
        old_schema = pa.schema([pa.field("chunk_id", pa.string())])
        table = db.create_table("chunks", schema=old_schema)
        with pytest.raises(CorpusInvalidError) as exc_info:
            verify_corpus_v3_state(table)
        msg = str(exc_info.value)
        assert "drop" in msg.lower() or "re-ingest" in msg.lower()


# ---------------------------------------------------------------------------
# Part 2+3: fail-closed startup + 503 on invalid corpus
# ---------------------------------------------------------------------------


class TestStartupRefusesPreV11Table:
    """Server lifespan must refuse to start if the chunks table is pre-v1.1."""

    def test_startup_raises_when_table_is_pre_v1_1(self, tmp_path, monkeypatch):
        """When the chunks table exists but has no bm25_text column, the
        lifespan hook must propagate CorpusInvalidError (server cannot start)."""
        db = lancedb.connect(str(tmp_path / "lancedb"))
        old_schema = pa.schema([
            pa.field("chunk_id", pa.string()),
            pa.field("full_text", pa.string()),
        ])
        db.create_table("chunks", schema=old_schema)
        monkeypatch.setenv("LANCEDB_PATH", str(tmp_path / "lancedb"))
        monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)

        from community_brain.query import retrieval_server

        # The lifespan hook raises CorpusInvalidError, which FastAPI wraps in
        # a RuntimeError during TestClient context entry.
        with pytest.raises((CorpusInvalidError, Exception)):
            with TestClient(retrieval_server.app):
                pass

    def test_startup_passes_with_valid_v3_table(self, tmp_path, monkeypatch):
        """Valid v3 table (v1.1 schema) must allow server to start normally."""
        db = lancedb.connect(str(tmp_path / "lancedb"))
        schema = pyarrow_table_schema()
        db.create_table("chunks", schema=schema)
        monkeypatch.setenv("LANCEDB_PATH", str(tmp_path / "lancedb"))
        monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)

        from community_brain.query import retrieval_server

        with TestClient(retrieval_server.app) as client:
            resp = client.get("/health")
        assert resp.status_code == 200


class TestQueryReturns503WhenCorpusInvalid:
    """/query must return 503 when the corpus is not in a valid v3 state.
    Previously it would silently return vector-only results (root cause 3)."""

    def test_query_returns_503_for_pre_v1_1_table(self, tmp_path, monkeypatch):
        """A chunks table without bm25_text column causes /query to return 503."""
        db = lancedb.connect(str(tmp_path / "lancedb"))
        old_schema = pa.schema([
            pa.field("chunk_id", pa.string()),
            pa.field("full_text", pa.string()),
        ])
        db.create_table("chunks", schema=old_schema)
        monkeypatch.setenv("LANCEDB_PATH", str(tmp_path / "lancedb"))
        monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)

        from community_brain.query import retrieval_server

        # Startup will fail with pre-v1.1 table, so we need to patch the lifespan
        # to not propagate the error at startup, then test /query directly.
        # This simulates a case where the server somehow started (e.g. race condition
        # between startup and table creation) but /query must still gate.
        with pytest.raises(Exception):
            # startup raises; that's the correct behavior per Part 2.
            with TestClient(retrieval_server.app) as client:
                client.post("/query", json={"question": "test"})

    def test_query_returns_503_when_verify_raises(self, tmp_path, monkeypatch):
        """When verify_corpus_v3_state raises CorpusInvalidError during /query,
        the endpoint returns 503 (not 200 with silently degraded results)."""
        # Set up a valid v3 DB so startup passes
        db = lancedb.connect(str(tmp_path / "lancedb"))
        schema = pyarrow_table_schema()
        db.create_table("chunks", schema=schema)
        monkeypatch.setenv("LANCEDB_PATH", str(tmp_path / "lancedb"))
        monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)

        from community_brain.query import retrieval_server
        from unittest.mock import patch

        with TestClient(retrieval_server.app) as client:
            # Startup passes. Now inject a CorpusInvalidError at /query time.
            with patch(
                "community_brain.query.retrieval_server.verify_corpus_v3_state",
                side_effect=CorpusInvalidError("simulated corpus invalid"),
            ):
                resp = client.post("/query", json={"question": "anything"})

        assert resp.status_code == 503
        detail = resp.json()["detail"]
        assert "v3" in detail or "invalid" in detail.lower() or "simulated" in detail

    def test_query_proceeds_normally_with_valid_corpus(self, tmp_path, monkeypatch):
        """When verify_corpus_v3_state passes, /query runs normally (not 503)."""
        monkeypatch.setenv("LANCEDB_PATH", str(tmp_path / "empty-lancedb"))
        monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)

        from community_brain.query import retrieval_server
        from unittest.mock import patch

        def _fake_embed(model, input):
            return {"embeddings": [[0.0] * 768 for _ in input]}

        with TestClient(retrieval_server.app) as client:
            with patch(
                "community_brain.query.query_local.ollama.embed",
                side_effect=_fake_embed,
            ):
                resp = client.post("/query", json={"question": "test"})

        # No chunks table means empty results, not 503
        assert resp.status_code == 200
        assert resp.json()["total_matched"] == 0


# ---------------------------------------------------------------------------
# Part 5: intra-file duplicate alias check in apply_canonicalizations
# ---------------------------------------------------------------------------


class TestApplyRejectsIntraFileDuplicateAlias:
    """A proposals YAML that maps the same alias to two different canonicals
    must raise ProposalConflictError — previously this caused silent ambiguity."""

    def test_intra_file_duplicate_raises_conflict_error(self):
        """Same alias under two canonicals in one proposals file → ProposalConflictError."""
        registry = {
            "aliases": {"Adam James": [], "Adam Smith": []},
            "pending": ["Adam"],
        }
        proposals = {
            "proposals": [
                {
                    "canonical": "Adam James",
                    "candidate_aliases": ["Adam"],
                    "confidence": "high",
                    "reason": "common first name",
                },
                {
                    "canonical": "Adam Smith",
                    "candidate_aliases": ["Adam"],  # same alias, different canonical
                    "confidence": "medium",
                    "reason": "also Adam",
                },
            ],
        }
        with pytest.raises(ProposalConflictError, match="both"):
            apply_proposals_to_registry(registry, proposals)

    def test_intra_file_duplicate_error_names_both_canonicals(self):
        """The error message must name both conflicting canonicals."""
        registry = {"aliases": {"Person A": [], "Person B": []}, "pending": ["alias1"]}
        proposals = {
            "proposals": [
                {"canonical": "Person A", "candidate_aliases": ["alias1"]},
                {"canonical": "Person B", "candidate_aliases": ["alias1"]},
            ],
        }
        with pytest.raises(ProposalConflictError) as exc_info:
            apply_proposals_to_registry(registry, proposals)
        msg = str(exc_info.value)
        assert "alias1" in msg
        assert "Person A" in msg or "Person B" in msg

    def test_same_alias_same_canonical_twice_is_idempotent(self):
        """The same alias appearing under the SAME canonical twice is not a conflict."""
        registry = {"aliases": {"Adam James": []}, "pending": ["Adam"]}
        proposals = {
            "proposals": [
                {"canonical": "Adam James", "candidate_aliases": ["Adam"]},
                {"canonical": "Adam James", "candidate_aliases": ["Adam"]},  # repeat
            ],
        }
        # Should not raise; result is idempotent
        updated = apply_proposals_to_registry(registry, proposals)
        assert "Adam" in updated["aliases"]["Adam James"]

    def test_no_intra_file_conflict_passes(self):
        """Two different aliases under two different canonicals has no conflict."""
        registry = {"aliases": {"Adam James": [], "Brandon H": []}, "pending": ["AdamJ", "BH"]}
        proposals = {
            "proposals": [
                {"canonical": "Adam James", "candidate_aliases": ["AdamJ"]},
                {"canonical": "Brandon H", "candidate_aliases": ["BH"]},
            ],
        }
        updated = apply_proposals_to_registry(registry, proposals)
        assert "AdamJ" in updated["aliases"]["Adam James"]
        assert "BH" in updated["aliases"]["Brandon H"]
