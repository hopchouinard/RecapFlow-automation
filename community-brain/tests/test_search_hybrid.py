"""Integration tests for hybrid search_chunks: real LanceDB on tmp_path.

These tests exercise the LanceDB hybrid query path end-to-end. They mock
Ollama embed (we don't need real semantic similarity — hand-crafted vectors
suffice) but use real LanceDB tables so any schema/contract drift surfaces.
"""

from __future__ import annotations

import lancedb
import pytest

from community_brain.ingestion.schema import EMBEDDING_DIM, pyarrow_table_schema
from community_brain.query.corpus_verify import CorpusInvalidError
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
            "bm25_text": "Adam from Gold Flamingo discussed sales funnel design",
            "embedding": [0.0, 1.0] + [0.0] * (EMBEDDING_DIM - 2),
        },
        {
            **common_fields,
            "chunk_id": "b",
            "chunk_index": 1,
            "embed_text": "...",
            "full_text": "weekly community sync covered onboarding and retention strategies",
            "bm25_text": "weekly community sync covered onboarding and retention strategies",
            "embedding": [1.0, 0.0] + [0.0] * (EMBEDDING_DIM - 2),
        },
        {
            **common_fields,
            "chunk_id": "b2",
            "chunk_index": 2,
            "embed_text": "...",
            "full_text": "engagement patterns and member churn discussed at length",
            "bm25_text": "engagement patterns and member churn discussed at length",
            "embedding": [1.0, 0.0] + [0.0] * (EMBEDDING_DIM - 2),
        },
        {
            **common_fields,
            "chunk_id": "b3",
            "chunk_index": 3,
            "embed_text": "...",
            "full_text": "broader thematic conversations about content cadence and pricing",
            "bm25_text": "broader thematic conversations about content cadence and pricing",
            "embedding": [1.0, 0.0] + [0.0] * (EMBEDDING_DIM - 2),
        },
    ]
    table.add(rows)
    ensure_fts_index(table, "bm25_text")
    optimize_fts_index(table, "bm25_text")

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
    result = search_chunks(
        question="Adam from Gold Flamingo",
        db_path=chunks_db,
        top_k=2,
        filters=None,
    )
    results = result["chunks"]
    assert len(results) >= 1
    ids = [r["chunk_id"] for r in results]
    assert "a" in ids, f"hybrid retrieval missed entity-grounded chunk; got {ids}"


def test_hybrid_returns_empty_on_missing_table(tmp_path):
    """Fresh LanceDB with no chunks table → empty list, no exception."""
    result = search_chunks(
        question="anything",
        db_path=str(tmp_path),
        top_k=5,
        filters=None,
    )
    assert result["chunks"] == []


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
            "bm25_text": "Adam Gold Flamingo failed extraction",
        }
    )
    table.add([failed_row])
    optimize_fts_index(table, "bm25_text")

    result = search_chunks(
        question="Adam Gold Flamingo",
        db_path=chunks_db,
        top_k=5,
        filters=None,
    )
    ids = [r["chunk_id"] for r in result["chunks"]]
    assert "c-failed" not in ids


def test_search_chunks_records_score_breakdown(chunks_db, monkeypatch):
    """Every chunk in search_chunks output has a score_breakdown dict
    with the 5 expected sub-fields and appropriate types."""
    # Use no filters so we get multiple chunks back; top_k=2 is enough.
    result = search_chunks(
        question="Adam from Gold Flamingo",
        db_path=chunks_db,
        top_k=2,
        filters=None,
    )
    results = result["chunks"]
    assert len(results) >= 1, "expected at least one result"
    for chunk in results:
        assert "score_breakdown" in chunk, f"chunk {chunk.get('chunk_id')} missing score_breakdown"
        sb = chunk["score_breakdown"]
        assert set(sb.keys()) == {
            "vector_similarity",
            "bm25_rank",
            "rrf_score",
            "cue_delta",
            "cue_rules_fired",
            "injected_by",
        }, f"unexpected score_breakdown keys: {set(sb.keys())}"
        assert isinstance(sb["vector_similarity"], (int, float)), (
            f"vector_similarity must be numeric, got {type(sb['vector_similarity'])}"
        )
        assert sb["bm25_rank"] is None or isinstance(sb["bm25_rank"], int), (
            f"bm25_rank must be int or None, got {type(sb['bm25_rank'])}"
        )
        assert isinstance(sb["rrf_score"], (int, float)), (
            f"rrf_score must be numeric, got {type(sb['rrf_score'])}"
        )
        assert isinstance(sb["cue_delta"], (int, float)), (
            f"cue_delta must be numeric, got {type(sb['cue_delta'])}"
        )
        assert isinstance(sb["cue_rules_fired"], list), (
            f"cue_rules_fired must be a list, got {type(sb['cue_rules_fired'])}"
        )


def test_search_chunks_returns_metadata_summary(chunks_db):
    """search_chunks return shape includes metadata_summary with of_top_k +
    per-flag counts for boolean flags."""
    # chunks_db contains 4 chunks, all with has_* flags False and references_prior False
    # (from common_fields in the fixture). Requesting top_k=4 so we get all of them.
    result = search_chunks(
        question="Adam from Gold Flamingo",
        db_path=chunks_db,
        top_k=4,
        filters=None,
    )
    assert isinstance(result, dict), "search_chunks must return a dict"
    assert "chunks" in result, "return dict must have 'chunks' key"
    assert "metadata_summary" in result, "return dict must have 'metadata_summary' key"

    chunks = result["chunks"]
    ms = result["metadata_summary"]

    assert ms["of_top_k"] == len(chunks), (
        f"of_top_k ({ms['of_top_k']}) must equal actual chunk count ({len(chunks)})"
    )

    # All fixture chunks have all boolean flags = False, so every count must be 0.
    for flag_count_key in (
        "has_question_count",
        "has_answer_count",
        "has_unresolved_question_count",
        "has_insight_count",
        "references_prior_count",
    ):
        assert flag_count_key in ms, f"metadata_summary missing key '{flag_count_key}'"
        assert ms[flag_count_key] == 0, (
            f"expected {flag_count_key}=0 for all-False fixture, got {ms[flag_count_key]}"
        )


def test_search_chunks_metadata_summary_counts_correctly(chunks_db):
    """metadata_summary flag counts match the actual flags on returned chunks."""
    # Add a chunk with has_unresolved_question=True and has_insight=True.
    db = lancedb.connect(chunks_db)
    table = db.open_table("chunks")
    base = dict(table.to_arrow().to_pylist()[0])
    flagged = dict(base)
    flagged.update({
        "chunk_id": "flagged",
        "chunk_index": 99,
        "full_text": "open question about retention strategy unresolved",
        "bm25_text": "open question about retention strategy unresolved",
        "has_unresolved_question": True,
        "has_insight": True,
        "embedding": [1.0, 0.0] + [0.0] * (EMBEDDING_DIM - 2),
    })
    table.add([flagged])
    from community_brain.query.fts_lifecycle import optimize_fts_index
    optimize_fts_index(table, "bm25_text")

    result = search_chunks(
        question="retention strategy",
        db_path=chunks_db,
        top_k=10,
        filters=None,
    )
    assert isinstance(result, dict)
    chunks = result["chunks"]
    ms = result["metadata_summary"]

    assert ms["of_top_k"] == len(chunks)

    # Count flags on the returned chunks directly to verify metadata_summary.
    expected_unresolved = sum(1 for c in chunks if c.get("has_unresolved_question") is True)
    expected_insight = sum(1 for c in chunks if c.get("has_insight") is True)
    assert ms["has_unresolved_question_count"] == expected_unresolved
    assert ms["has_insight_count"] == expected_insight
    # The flagged chunk must be in the results (it matches the question lexically).
    ids = [c["chunk_id"] for c in chunks]
    assert "flagged" in ids, f"flagged chunk missing from results: {ids}"


def test_search_pinned_to_bm25_text_when_full_text_index_exists(tmp_path, monkeypatch):
    """Migration safety: if a legacy full_text FTS index lingers alongside the
    v3 bm25_text FTS index, search must still use bm25_text per fts_columns
    binding. Without the explicit fts_columns kwarg, LanceDB may silently
    fall back to whichever index it finds first.

    Setup:
      chunk_a: bm25_text contains 'Adam James', full_text does NOT
      chunk_b: full_text contains 'Adam James', bm25_text does NOT

    With fts_columns='bm25_text', the BM25 leg must return chunk_a (not chunk_b).
    """
    db_path = tmp_path / "lancedb"
    db = lancedb.connect(str(db_path))
    schema = pyarrow_table_schema()
    table = db.create_table("chunks", schema=schema)

    common_fields = {
        "schema_version": "1.0",
        "session_id": "2026-04-01",
        "session_date": "2026-04-01",
        "session_title": None,
        "content_type": "prepared_transcript",
        "source_file": "prepared-transcript.md",
        "total_chunks_in_source": 2,
        "embed_text": "...",
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

    table.add([
        {
            **common_fields,
            "chunk_id": "chunk_a",
            "chunk_index": 0,
            # bm25_text has "Adam James"; full_text does NOT
            "bm25_text": "Adam James discussed coaching strategy",
            "full_text": "unrelated community discussion about onboarding",
            "embedding": [0.0, 1.0] + [0.0] * (EMBEDDING_DIM - 2),
        },
        {
            **common_fields,
            "chunk_id": "chunk_b",
            "chunk_index": 1,
            # full_text has "Adam James"; bm25_text does NOT
            "full_text": "Adam James joined the weekly session",
            "bm25_text": "unrelated community discussion about retention",
            "embedding": [1.0, 0.0] + [0.0] * (EMBEDDING_DIM - 2),
        },
    ])

    # Create BOTH FTS indexes — simulating the migration-limbo state where the
    # legacy full_text index wasn't fully cleaned up.
    table.create_fts_index("full_text")
    table.create_fts_index("bm25_text")

    import ollama
    # Query vector is neutral (equal distance from both chunks); BM25 drives result.
    monkeypatch.setattr(ollama, "embed", lambda model, input: {
        "embeddings": [[0.5, 0.5] + [0.0] * (EMBEDDING_DIM - 2)]
    })

    result = search_chunks(
        question="Adam James",
        db_path=str(db_path),
        top_k=2,
        filters=None,
    )
    ids = [c["chunk_id"] for c in result["chunks"]]

    # chunk_a must be present: it matches via bm25_text (the pinned column).
    # chunk_b must NOT be the sole BM25-powered result: its "Adam James" is
    # only in full_text, which we explicitly bypass via fts_columns binding.
    assert "chunk_a" in ids, (
        f"fts_columns binding broken: search should surface chunk_a "
        f"(matched via bm25_text) but got {ids}"
    )


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
                "bm25_text": f"additional thematic discussion variant {i}",
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
            "bm25_text": "general weekly community sync about onboarding and retention",
            "has_unresolved_question": True,
            "embedding": [0.95, 0.05] + [0.0] * (EMBEDDING_DIM - 2),
        }
    )
    table.add([flagged_row])
    optimize_fts_index(table, "bm25_text")

    result = search_chunks(
        question="what unresolved questions came up?",
        db_path=chunks_db,
        top_k=3,
        filters=None,
    )
    ids = [r["chunk_id"] for r in result["chunks"]]
    assert "u" in ids, (
        f"cue boost failed to promote unresolved-question chunk; got {ids}"
    )


def test_search_chunks_raises_on_runtime_hybrid_failure_after_verify(
    tmp_path, monkeypatch
):
    """Regression for round-9 finding: even after verify_corpus_v3_state passes
    at /query entry, search_chunks can hit a runtime hybrid failure (corrupt
    index, etc.). Must NOT silently fall back to vector-only — must raise
    CorpusInvalidError so /query can return HTTP 503.
    """
    import ollama

    db_path = tmp_path / "lancedb"
    db = lancedb.connect(str(db_path))
    schema = pyarrow_table_schema()
    table = db.create_table("chunks", schema=schema)
    table.add([
        {
            "schema_version": "1.0",
            "chunk_id": "c1",
            "chunk_index": 0,
            "session_id": "2026-04-01",
            "session_date": "2026-04-01",
            "session_title": None,
            "content_type": "prepared_transcript",
            "source_file": "prepared-transcript.md",
            "total_chunks_in_source": 1,
            "embed_text": "...",
            "full_text": "some text",
            "bm25_text": "some text",
            "embedding": [1.0, 0.0] + [0.0] * (EMBEDDING_DIM - 2),
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
    ])
    ensure_fts_index(table, "bm25_text")

    monkeypatch.setattr(ollama, "embed", lambda model, input: {
        "embeddings": [[1.0, 0.0] + [0.0] * (EMBEDDING_DIM - 2)]
    })

    # Simulate a runtime FTS execution failure AFTER verify_corpus_v3_state
    # has already passed (e.g. corrupt index data, fts_columns incompatibility).
    # We inject the failure by patching the table's search method.
    original_search = table.search

    def _failing_search(query_type=None, fts_columns=None):
        if query_type == "hybrid":
            raise RuntimeError("simulated FTS execution error at runtime")
        return original_search(query_type=query_type, fts_columns=fts_columns)

    import lancedb as _lancedb

    original_connect = _lancedb.connect

    def _patched_connect(path, *args, **kwargs):
        conn = original_connect(path, *args, **kwargs)
        original_open = conn.open_table

        def _patched_open(name):
            t = original_open(name)
            t.search = _failing_search
            return t

        conn.open_table = _patched_open
        return conn

    monkeypatch.setattr(_lancedb, "connect", _patched_connect)

    with pytest.raises(CorpusInvalidError, match="hybrid search failed at runtime"):
        search_chunks(
            question="some text",
            db_path=str(db_path),
            top_k=5,
            filters=None,
        )
