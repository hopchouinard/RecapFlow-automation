"""Integration tests for hybrid search_chunks: real LanceDB on tmp_path.

These tests exercise the LanceDB hybrid query path end-to-end. They mock
Ollama embed (we don't need real semantic similarity — hand-crafted vectors
suffice) but use real LanceDB tables so any schema/contract drift surfaces.
"""

from __future__ import annotations

import lancedb
import pytest

from community_brain.ingestion.schema import EMBEDDING_DIM, pyarrow_table_schema
from community_brain.query.query_local import search_chunks
from community_brain.query.fts_lifecycle import ensure_fts_index, optimize_fts_index


@pytest.fixture
def chunks_db(tmp_path, monkeypatch):
    """A real LanceDB with a chunks table populated for hybrid search tests."""
    db_path = tmp_path / "lancedb"
    db = lancedb.connect(str(db_path))
    schema = pyarrow_table_schema()
    table = db.create_table("chunks", schema=schema)

    # Chunks: 'a' has Adam in full_text but its vector is far from the query
    # vector. Several 'b'-like chunks have only thematic content and vectors
    # close to the query vector. Under pure-vector ranking with top_k=1, 'a'
    # is pushed out of the top-K. Under hybrid (BM25 finds 'Adam' in 'a'),
    # 'a' must surface via RRF fusion.
    common_fields = {
        "schema_version": "1.0",
        "session_id": "2026-04-01",
        "session_date": "2026-04-01",
        "session_title": None,
        "content_type": "prepared_transcript",
        "source_file": "prepared-transcript.md",
        "total_chunks_in_source": 2,
        "speakers_spoke": [],
        "speakers_mentioned": [],
        "entities": [],
        "keywords": [],
        "topic_label": None,
        "session_themes": [],
        "speech_acts": [],
        "stance": None,
        "certainty": "asserted",
        "chunk_local_markers": [],
        "corpus_derived_markers": [],
        "corpus_markers_computed_at": None,
        "has_question": False,
        "has_answer": False,
        "has_unresolved_question": False,
        "has_insight": False,
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
        "extraction_model": "test",
        "extraction_prompt_version": "test-v1",
        "extraction_status": "success",
        "extraction_error": None,
        "extracted_at": "2026-04-01T00:00:00",
    }

    rows = [
        {
            **common_fields,
            "chunk_id": "a",
            "chunk_index": 0,
            "embed_text": "...",
            "full_text": "Adam from Gold Flamingo discussed sales funnel design",
            "embedding": [0.0, 1.0] + [0.0] * (EMBEDDING_DIM - 2),
        },
        {
            **common_fields,
            "chunk_id": "b",
            "chunk_index": 1,
            "embed_text": "...",
            "full_text": "weekly community sync covered onboarding and retention strategies",
            "embedding": [1.0, 0.0] + [0.0] * (EMBEDDING_DIM - 2),
        },
        {
            **common_fields,
            "chunk_id": "b2",
            "chunk_index": 2,
            "embed_text": "...",
            "full_text": "engagement patterns and member churn discussed at length",
            "embedding": [1.0, 0.0] + [0.0] * (EMBEDDING_DIM - 2),
        },
        {
            **common_fields,
            "chunk_id": "b3",
            "chunk_index": 3,
            "embed_text": "...",
            "full_text": "broader thematic conversations about content cadence and pricing",
            "embedding": [1.0, 0.0] + [0.0] * (EMBEDDING_DIM - 2),
        },
    ]
    table.add(rows)
    ensure_fts_index(table, "full_text")
    optimize_fts_index(table, "full_text")

    # Mock the ollama embed call: return a vector close to 'b' (so pure
    # vector would rank 'b' first; hybrid+BM25 should surface 'a' for
    # an Adam-keyword question).
    def _fake_embed(model, input):
        # 'input' is a list; we always return a single embedding
        return {"embeddings": [[1.0, 0.0] + [0.0] * (EMBEDDING_DIM - 2)]}

    import ollama
    monkeypatch.setattr(ollama, "embed", _fake_embed)

    return str(db_path)


def test_hybrid_surfaces_adam_chunk_for_keyword_query(chunks_db):
    """The query vector is identical to chunks 'b', 'b2', 'b3' — pure-vector
    ranks all three at distance 0 and would fill top_k with one or more of
    them, pushing 'a' (entity match in full_text but distant vector) out
    under pure-vector ranking. Hybrid (vector + BM25 over 'Adam Gold
    Flamingo') must surface 'a' via the RRF fusion — proving the lexical
    leg pulls in entity-grounded chunks the vector leg misses.

    `top_k=2` here gives RRF a stable window: 'a' and 'b' tie on RRF score
    (sample lift = `1/61` from each leg's #1 rank), so top-1 alone would
    be brittle to sort-ties. Top-2 is enough to prove the lexical pull
    without depending on tie-break order.
    """
    results = search_chunks(
        question="Adam from Gold Flamingo",
        db_path=chunks_db,
        top_k=2,
        filters=None,
    )
    assert len(results) >= 1
    ids = [r["chunk_id"] for r in results]
    assert "a" in ids, f"hybrid retrieval missed entity-grounded chunk; got {ids}"


def test_hybrid_returns_empty_on_missing_table(tmp_path):
    """Fresh LanceDB with no chunks table → empty list, no exception."""
    results = search_chunks(
        question="anything",
        db_path=str(tmp_path),
        top_k=5,
        filters=None,
    )
    assert results == []


def test_hybrid_excludes_failed_extraction_chunks(chunks_db):
    """Pre-existing v1 contract: extraction_status='success' guard is preserved."""
    # Add a 'failed' chunk that lexically matches the query
    db = lancedb.connect(chunks_db)
    table = db.open_table("chunks")
    failed_row = dict(table.to_arrow().to_pylist()[0])
    failed_row.update(
        {
            "chunk_id": "c-failed",
            "extraction_status": "failed",
            "embedding": [0.0] * EMBEDDING_DIM,
            "full_text": "Adam Gold Flamingo failed extraction",
        }
    )
    table.add([failed_row])
    optimize_fts_index(table, "full_text")

    results = search_chunks(
        question="Adam Gold Flamingo",
        db_path=chunks_db,
        top_k=5,
        filters=None,
    )
    ids = [r["chunk_id"] for r in results]
    assert "c-failed" not in ids


def test_search_chunks_promotes_unresolved_question_chunk_via_cue_boost(
    chunks_db, monkeypatch
):
    """When the question contains 'unresolved questions', a chunk tagged
    has_unresolved_question=True must rank above an otherwise-equal chunk
    without the tag — even when their RRF scores are very close.

    Verifies the cue boost layer runs after RRF fusion and before top_k
    truncation.
    """
    # Point the YAML loader at the real config file so cue rules load correctly.
    from pathlib import Path
    real_yaml = Path(__file__).parent.parent / "config" / "query-cues.yaml"
    monkeypatch.setenv("COMMUNITY_BRAIN_CUE_RULES_PATH", str(real_yaml))

    db = lancedb.connect(chunks_db)
    table = db.open_table("chunks")
    base = dict(table.to_arrow().to_pylist()[0])

    # Add additional 'b'-clones so the b-cluster fully saturates top_k=3
    # at zero vector distance. Without cue boost, 'u' (vector slightly
    # offset from b's vector) sits one rank below and falls out of top-3.
    extra_b_clones = []
    for i, suffix in enumerate(("b4", "b5")):
        clone = dict(base)
        clone.update(
            {
                "chunk_id": suffix,
                "full_text": f"additional thematic discussion variant {i}",
                "has_unresolved_question": False,
                "embedding": [1.0, 0.0] + [0.0] * (EMBEDDING_DIM - 2),
            }
        )
        extra_b_clones.append(clone)
    table.add(extra_b_clones)

    flagged_row = dict(base)
    flagged_row.update(
        {
            "chunk_id": "u",
            "full_text": "general weekly community sync about onboarding and retention",
            "has_unresolved_question": True,
            "embedding": [0.95, 0.05] + [0.0] * (EMBEDDING_DIM - 2),
        }
    )
    table.add([flagged_row])
    optimize_fts_index(table, "full_text")

    results = search_chunks(
        question="what unresolved questions came up?",
        db_path=chunks_db,
        top_k=3,
        filters=None,
    )
    ids = [r["chunk_id"] for r in results]
    assert "u" in ids, (
        f"cue boost failed to promote unresolved-question chunk; got {ids}"
    )
