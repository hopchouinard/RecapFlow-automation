"""Golden query suite — regression protection for hybrid retrieval v2.

For each query in tests/fixtures/golden_queries.yaml:
  1. Run search_chunks (hybrid + cue boost) against the seeded golden corpus.
  2. Assert top-K contains at least `min_match_count` of `expected_chunk_ids`.
  3. If `expect_lift_over_vector_only`, also run search_chunks(_use_hybrid=False)
     and assert it does NOT satisfy the same min_match_count — proving the
     hybrid path is responsible for the surfaced chunks.

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
