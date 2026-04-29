"""Golden query suite — regression protection for hybrid retrieval.

For each query in tests/fixtures/golden_queries.yaml:
  1. Run search_chunks (hybrid + cue boost) against the seeded golden corpus.
  2. Assert top-K contains at least `min_match_count` of `expected_chunk_ids`.
  3. If `expect_lift_over_vector_only`, also run search_chunks(_use_hybrid=False)
     and assert it does NOT satisfy the same min_match_count — proving the
     hybrid path is responsible for the surfaced chunks.

v3 additions (T28):
  4. test_v3_corpus_has_some_populated_entities — seed has >= 1 chunk with
     non-empty entities array (locks Stage C v2 entities extraction contract).
  5. test_v3_query_response_has_metadata_summary — every /query response
     carries metadata_summary with the 6 expected keys.
  6. test_v3_query_response_chunks_have_score_breakdown — every chunk in top-K
     carries score_breakdown with the 5 expected keys.

If a query starts failing under code change, the implementation regressed.
Fix the implementation, not the test.
"""

from __future__ import annotations

from pathlib import Path

import lancedb
import pytest
import yaml

from community_brain.ingestion.schema import EMBEDDING_DIM
from community_brain.query.query_local import search_chunks
from community_brain.query.fts_lifecycle import ensure_fts_index, optimize_fts_index


FIXTURES_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture(scope="module")
def golden_db(tmp_path_factory):
    """Seed a LanceDB at module scope (once per pytest run); shared across queries."""
    import sys
    sys.path.insert(0, str(FIXTURES_DIR / "golden_corpus"))
    from seed import seed  # type: ignore

    db_path = tmp_path_factory.mktemp("golden_db")
    seed(str(db_path))

    db = lancedb.connect(str(db_path))
    table = db.open_table("chunks")
    ensure_fts_index(table, "bm25_text")
    optimize_fts_index(table, "bm25_text")
    return str(db_path)


@pytest.fixture
def fake_embed(monkeypatch):
    """Return a generic embedding for any input — golden tests rely on the
    BM25 + cue boost layers, not on semantic similarity. Vector path returns
    a constant vector that doesn't favor any specific golden chunk."""
    def _embed(model, input):
        return {"embeddings": [[0.5] * EMBEDDING_DIM]}
    import ollama
    monkeypatch.setattr(ollama, "embed", _embed)


def _load_queries():
    with open(FIXTURES_DIR / "golden_queries.yaml") as f:
        return yaml.safe_load(f)["queries"]


@pytest.mark.parametrize("query_spec", _load_queries(), ids=lambda q: q["id"])
def test_golden_query_hybrid(query_spec, golden_db, fake_embed):
    result = search_chunks(
        question=query_spec["question"],
        db_path=golden_db,
        top_k=query_spec["top_k"],
        filters=None,
    )
    ids = [r["chunk_id"] for r in result["chunks"]]
    matches = [c for c in query_spec["expected_chunk_ids"] if c in ids]
    assert len(matches) >= query_spec["min_match_count"], (
        f"hybrid retrieval missed expected chunks for {query_spec['id']}: "
        f"got {ids}; expected >={query_spec['min_match_count']} of "
        f"{query_spec['expected_chunk_ids']}"
    )


@pytest.mark.parametrize(
    "query_spec",
    [q for q in _load_queries() if q.get("expect_lift_over_vector_only")],
    ids=lambda q: q["id"],
)
def test_golden_query_vector_only_baseline_misses(query_spec, golden_db, fake_embed):
    """Lift validation: pure-vector path must NOT satisfy min_match_count
    on these queries — proves the hybrid+cue layers are doing the work."""
    result = search_chunks(
        question=query_spec["question"],
        db_path=golden_db,
        top_k=query_spec["top_k"],
        filters=None,
        _use_hybrid=False,
    )
    ids = [r["chunk_id"] for r in result["chunks"]]
    matches = [c for c in query_spec["expected_chunk_ids"] if c in ids]
    assert len(matches) < query_spec["min_match_count"], (
        f"vector-only baseline UNEXPECTEDLY satisfied {query_spec['id']}: "
        f"got {ids}; the lift assertion is now meaningless. Either the test "
        f"corpus is wrong (vector path got lucky) or the fixture needs "
        f"more thematic divergence between flagged and unflagged chunks."
    )


# ---------------------------------------------------------------------------
# v3 assertions (T28): entities, metadata_summary, score_breakdown
# ---------------------------------------------------------------------------

_V3_QUERY_IDS = {"v3-entities-populated", "v3-metadata-summary-present", "v3-score-breakdown-per-chunk"}


def _get_v3_query(query_id: str) -> dict:
    """Return the YAML entry for the given v3 query id."""
    for q in _load_queries():
        if q["id"] == query_id:
            return q
    raise KeyError(f"v3 query {query_id!r} not found in golden_queries.yaml")  # pragma: no cover


def test_v3_corpus_has_some_populated_entities(golden_db):
    """The v3 test corpus has at least one chunk with non-empty entities array.

    Locks the Stage C v2 contract: entities extraction must persist data that
    the seed's entity-grounded chunks carry.
    """
    import lancedb as _lancedb
    db = _lancedb.connect(golden_db)
    table = db.open_table("chunks")
    rows = table.to_arrow().to_pylist()
    chunks_with_entities = [r for r in rows if r.get("entities")]
    assert len(chunks_with_entities) >= 1, (
        "Expected at least one chunk with a non-empty entities array in the "
        "golden corpus; found none. The seed.py entity-grounded fixtures may "
        "have been stripped or the schema changed."
    )


def test_v3_query_returns_chunks_with_populated_entities(golden_db, fake_embed):
    """Regression guard: search_chunks must preserve `entities` on returned chunks.

    A bug in query-side projection/serialization that empties entities on the
    response would otherwise ship undetected — the storage-level sanity check
    above only scans rows directly, never exercises the retrieval path.

    Loads the v3-entities-populated golden query, runs search_chunks, then
    asserts each expected chunk (by ID) appears in the result with a non-empty
    entities array and that the arrays contain expected values.
    """
    spec = _get_v3_query("v3-entities-populated")
    result = search_chunks(
        question=spec["question"],
        db_path=golden_db,
        top_k=spec["top_k"],
        filters=None,
    )
    chunks_by_id = {c["chunk_id"]: c for c in result["chunks"]}
    for expected_id in spec["expected_chunk_ids"]:
        assert expected_id in chunks_by_id, (
            f"Expected chunk {expected_id!r} not found in search_chunks result; "
            f"got chunk_ids: {list(chunks_by_id)}"
        )
        chunk = chunks_by_id[expected_id]
        entities = chunk.get("entities")
        assert entities, (
            f"Chunk {expected_id!r} returned by search_chunks has empty or missing "
            f"entities — projection/serialization may have dropped the field. "
            f"Chunk keys: {list(chunk)}"
        )
    # Spot-check specific expected entity values from the seed fixtures.
    assert "Adam" in chunks_by_id["f6-adam-1"]["entities"], (
        "f6-adam-1 should carry 'Adam' in entities; got: "
        f"{chunks_by_id['f6-adam-1']['entities']}"
    )
    assert "Gold Flamingo" in chunks_by_id["f6-adam-1"]["entities"], (
        "f6-adam-1 should carry 'Gold Flamingo' in entities; got: "
        f"{chunks_by_id['f6-adam-1']['entities']}"
    )
    assert "Adam" in chunks_by_id["f6-adam-2"]["entities"], (
        "f6-adam-2 should carry 'Adam' in entities; got: "
        f"{chunks_by_id['f6-adam-2']['entities']}"
    )


def test_v3_query_response_has_metadata_summary(golden_db, fake_embed):
    """Every /query response includes metadata_summary with the 6 expected keys.

    The summary is the authoritative aggregate counts returned alongside chunks.
    Keys: of_top_k, has_question_count, has_answer_count,
    has_unresolved_question_count, has_insight_count, references_prior_count.
    """
    spec = _get_v3_query("v3-metadata-summary-present")
    result = search_chunks(
        question=spec["question"],
        db_path=golden_db,
        top_k=spec["top_k"],
        filters=None,
    )
    assert "metadata_summary" in result, (
        "/query response is missing metadata_summary key"
    )
    summary = result["metadata_summary"]
    expected_keys = {
        "of_top_k",
        "has_question_count",
        "has_answer_count",
        "has_unresolved_question_count",
        "has_insight_count",
        "references_prior_count",
    }
    missing = expected_keys - set(summary.keys())
    assert not missing, (
        f"metadata_summary is missing keys: {sorted(missing)}"
    )
    assert isinstance(summary["of_top_k"], int), "metadata_summary.of_top_k must be int"
    for key in expected_keys - {"of_top_k"}:
        assert isinstance(summary[key], int), f"metadata_summary.{key} must be int"


def test_v3_query_response_chunks_have_score_breakdown(golden_db, fake_embed):
    """Every chunk in /query response has score_breakdown with the 5 expected keys.

    Keys: vector_similarity, bm25_rank, rrf_score, cue_delta, cue_rules_fired.
    """
    spec = _get_v3_query("v3-score-breakdown-per-chunk")
    result = search_chunks(
        question=spec["question"],
        db_path=golden_db,
        top_k=spec["top_k"],
        filters=None,
    )
    chunks = result["chunks"]
    assert len(chunks) >= 1, "Expected at least one chunk in response to verify score_breakdown"
    expected_keys = {"vector_similarity", "bm25_rank", "rrf_score", "cue_delta", "cue_rules_fired"}
    for chunk in chunks:
        assert "score_breakdown" in chunk, (
            f"chunk {chunk.get('chunk_id')!r} is missing score_breakdown"
        )
        breakdown = chunk["score_breakdown"]
        missing = expected_keys - set(breakdown.keys())
        assert not missing, (
            f"chunk {chunk.get('chunk_id')!r} score_breakdown missing keys: {sorted(missing)}"
        )
        assert isinstance(breakdown["vector_similarity"], float), (
            f"chunk {chunk.get('chunk_id')!r} score_breakdown.vector_similarity must be float"
        )
        assert isinstance(breakdown["rrf_score"], float), (
            f"chunk {chunk.get('chunk_id')!r} score_breakdown.rrf_score must be float"
        )
        assert isinstance(breakdown["cue_delta"], float), (
            f"chunk {chunk.get('chunk_id')!r} score_breakdown.cue_delta must be float"
        )
        assert isinstance(breakdown["cue_rules_fired"], list), (
            f"chunk {chunk.get('chunk_id')!r} score_breakdown.cue_rules_fired must be list"
        )
