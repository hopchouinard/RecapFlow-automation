"""Tests for the lint_corpus CLI."""
from __future__ import annotations

import datetime as dt
from pathlib import Path

import lancedb
import pytest

from community_brain.cli.lint_corpus import lint_corpus_chunks
from community_brain.ingestion.schema import EMBEDDING_DIM, pyarrow_table_schema


def _make_chunk_row(
    *,
    chunk_id: str,
    session_id: str,
    embedding: list[float] | None = None,
    full_text: str = "test content",
    content_type: str = "prepared_transcript",
    corpus_derived_markers: list[str] | None = None,
) -> dict:
    """Construct a minimal v1.1 chunk row for in-test LanceDB seeding."""
    if embedding is None:
        embedding = [0.0] * EMBEDDING_DIM
    return {
        "schema_version": "1.1",
        "chunk_id": chunk_id,
        "session_id": session_id,
        "session_date": "2026-01-01",
        "session_title": None,
        "content_type": content_type,
        "source_file": "test.md",
        "chunk_index": 0,
        "total_chunks_in_source": 1,
        "speakers_spoke": [],
        "speakers_mentioned": [],
        "entities": [],
        "keywords": [],
        "topic_label": "Test topic",
        "session_themes": [],
        "speech_acts": [],
        "stance": None,
        "certainty": "asserted",
        "chunk_local_markers": [],
        "corpus_derived_markers": corpus_derived_markers or [],
        "corpus_markers_computed_at": None,
        "has_question": False,
        "has_answer": False,
        "has_unresolved_question": False,
        "has_insight": False,
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
        "extraction_model": "test-model",
        "extraction_prompt_version": "chunk-extraction-v2",
        "extraction_status": "success",
        "extraction_error": None,
        "extracted_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "embed_text": "test embed_text",
        "full_text": full_text,
        "bm25_text": "test bm25_text",
        "embedding": embedding,
    }


def _create_table(db_path: Path, rows: list[dict]):
    db = lancedb.connect(str(db_path))
    table = db.create_table("chunks", schema=pyarrow_table_schema())
    if rows:
        table.add(rows)
    return table


def _direction_vector(seed: int) -> list[float]:
    """Build a normalized embedding pointing in a specific direction.
    Two chunks with the same seed have cosine similarity ~1.0; different
    seeds give similarity ~0.0.
    """
    vec = [0.0] * EMBEDDING_DIM
    vec[seed % EMBEDDING_DIM] = 1.0
    return vec


@pytest.fixture
def db_path(tmp_path: Path) -> Path:
    return tmp_path / "test.lancedb"


def test_recurrent_marker_applied_to_cross_session_neighbors(db_path: Path):
    """A chunk with K-nearest neighbors spanning 2+ sessions at high similarity
    receives the 'recurrent' marker."""
    # 3 sessions, 2 chunks each, all chunks share the same embedding direction.
    # Every chunk has 5 high-similarity neighbors across 2 different sessions.
    rows = []
    for sid in ("s1", "s2", "s3"):
        for i in range(2):
            rows.append(_make_chunk_row(
                chunk_id=f"{sid}:c{i}",
                session_id=sid,
                embedding=_direction_vector(0),  # all aligned
            ))
    _create_table(db_path, rows)
    stats = lint_corpus_chunks(db_path)
    assert stats["scanned"] == 6
    # All chunks should be marked recurrent (each has >=2 cross-session high-sim neighbors).
    assert stats["recurrent"] == 6
    db = lancedb.connect(str(db_path))
    rows_after = db.open_table("chunks").to_arrow().to_pylist()
    for r in rows_after:
        assert "recurrent" in r["corpus_derived_markers"]


def test_unique_chunk_no_recurrent_marker(db_path: Path):
    """Chunks without high-similarity cross-session neighbors stay unmarked."""
    # Each chunk has a unique embedding direction; no neighbors above threshold.
    rows = [
        _make_chunk_row(
            chunk_id=f"s{i}:c0",
            session_id=f"s{i}",
            embedding=_direction_vector(i),
        )
        for i in range(3)
    ]
    _create_table(db_path, rows)
    stats = lint_corpus_chunks(db_path)
    assert stats["scanned"] == 3
    assert stats["recurrent"] == 0
    db = lancedb.connect(str(db_path))
    rows_after = db.open_table("chunks").to_arrow().to_pylist()
    for r in rows_after:
        assert r["corpus_derived_markers"] == []


def test_lint_corpus_idempotent(db_path: Path):
    """Running lint_corpus twice produces the same markers (no duplication)."""
    rows = []
    for sid in ("s1", "s2", "s3"):
        rows.append(_make_chunk_row(
            chunk_id=f"{sid}:c0",
            session_id=sid,
            embedding=_direction_vector(0),
        ))
    _create_table(db_path, rows)
    stats1 = lint_corpus_chunks(db_path)
    stats2 = lint_corpus_chunks(db_path)
    assert stats1["recurrent"] == stats2["recurrent"]
    db = lancedb.connect(str(db_path))
    rows_after = db.open_table("chunks").to_arrow().to_pylist()
    for r in rows_after:
        # Marker should appear exactly once even after two passes.
        assert r["corpus_derived_markers"].count("recurrent") <= 1


def test_lint_corpus_writes_corpus_markers_computed_at(db_path: Path):
    """corpus_markers_computed_at is set to a non-null UTC timestamp on rows
    whose marker state actually changes.

    Post Change A (spec 2026-05-02-ingest-lint-decoupling-design.md §7), the
    timestamp records "last meaningful marker change" rather than "last lint
    pass." Rows without a state change retain whatever timestamp they had,
    including null for never-touched chunks. So this test seeds a 3-session
    aligned corpus where every chunk transitions to recurrent — guaranteed
    state change for all rows.
    """
    rows = [
        _make_chunk_row(
            chunk_id=f"{sid}:c0",
            session_id=sid,
            embedding=_direction_vector(0),
        )
        for sid in ("s1", "s2", "s3")
    ]
    _create_table(db_path, rows)
    lint_corpus_chunks(db_path)
    db = lancedb.connect(str(db_path))
    rows_after = db.open_table("chunks").to_arrow().to_pylist()
    for row in rows_after:
        assert row["corpus_markers_computed_at"] is not None, (
            f"chunk {row['chunk_id']} transitioned to recurrent — its "
            "corpus_markers_computed_at must be set"
        )


def test_lint_corpus_neighbors_in_same_session_dont_count(db_path: Path):
    """Three chunks in ONE session, all aligned. No cross-session neighbors,
    so no recurrent marker."""
    rows = [
        _make_chunk_row(
            chunk_id=f"s1:c{i}",
            session_id="s1",
            embedding=_direction_vector(0),
        )
        for i in range(3)
    ]
    _create_table(db_path, rows)
    stats = lint_corpus_chunks(db_path)
    assert stats["recurrent"] == 0


def test_lint_corpus_below_threshold_neighbors_dont_count(db_path: Path):
    """Cross-session neighbors below similarity threshold don't trigger recurrent."""
    # Each chunk in a different direction -> low cross-similarity.
    rows = [
        _make_chunk_row(
            chunk_id=f"s{i}:c0",
            session_id=f"s{i}",
            embedding=_direction_vector(i),
        )
        for i in range(5)
    ]
    _create_table(db_path, rows)
    stats = lint_corpus_chunks(db_path)
    assert stats["recurrent"] == 0


def test_recurrent_requires_neighbors_from_distinct_sessions(db_path: Path):
    """HIGH 2 regression: two highly-similar neighbors from a SINGLE other session
    must NOT mark the target as recurrent.

    cross_session_session_ids counts distinct sessions, not neighbor chunks.
    {s2} has len=1 which is below CROSS_SESSION_COUNT_MIN=2, so no recurrent mark.
    """
    rows = [
        # Target chunk in s1
        _make_chunk_row(
            chunk_id="s1:c0",
            session_id="s1",
            embedding=_direction_vector(0),
        ),
        # Two highly-similar neighbors in s2 (single other session)
        _make_chunk_row(
            chunk_id="s2:c0",
            session_id="s2",
            embedding=_direction_vector(0),
        ),
        _make_chunk_row(
            chunk_id="s2:c1",
            session_id="s2",
            embedding=_direction_vector(0),
        ),
    ]
    _create_table(db_path, rows)
    stats = lint_corpus_chunks(db_path)
    # cross_session_session_ids = {"s2"} -> len=1 -> below CROSS_SESSION_COUNT_MIN=2
    assert stats["recurrent"] == 0, (
        "Two neighbors from ONE other session should not satisfy recurrent threshold"
    )


def test_lint_corpus_marker_update_non_destructive_on_failure(
    db_path: Path, monkeypatch
) -> None:
    """HIGH 1 regression: if the marker write fails, the row must be unchanged.

    Under the update()-based implementation, a failed update leaves the row
    intact (no delete has occurred). The lint function raises, which propagates
    out of the auto-trigger. Chunks are NOT destroyed.

    Three sessions all aligned to the same direction so every chunk has 2
    cross-session high-similarity neighbors and qualifies as recurrent —
    guarantees the ADD-marker branch fires update() and the faulty proxy
    has something to raise on. (Post Change A spec
    2026-05-02-ingest-lint-decoupling-design.md, the no-op timestamp branches
    don't write, so the corpus must trigger a real state change.)
    """
    import lancedb as _ldb
    from community_brain.cli import lint_corpus as _lint_mod

    rows = [
        _make_chunk_row(
            chunk_id="s1:c0",
            session_id="s1",
            embedding=_direction_vector(0),
            full_text="original content",
        ),
        _make_chunk_row(
            chunk_id="s2:c0",
            session_id="s2",
            embedding=_direction_vector(0),
        ),
        _make_chunk_row(
            chunk_id="s3:c0",
            session_id="s3",
            embedding=_direction_vector(0),
        ),
    ]
    _create_table(db_path, rows)

    class _FaultyTable:
        """Proxy that raises on update() to simulate a write failure."""
        def __init__(self, real_table):
            self._real = real_table

        def __getattr__(self, name):
            return getattr(self._real, name)

        def update(self, *_a, **_kw):
            raise RuntimeError("simulated marker write failure")

    class _FaultyDB:
        def __init__(self, real_db):
            self._real = real_db

        def open_table(self, name):
            return _FaultyTable(self._real.open_table(name))

    original_connect = _ldb.connect

    def patched_connect(path, *args, **kwargs):
        return _FaultyDB(original_connect(path, *args, **kwargs))

    monkeypatch.setattr(_lint_mod, "lancedb", type("mod", (), {
        "connect": staticmethod(patched_connect),
    })())

    # lint_corpus raises because update() fails
    with pytest.raises(RuntimeError, match="simulated marker write failure"):
        _lint_mod.lint_corpus_chunks(db_path)

    # The row must still be present and its full_text must be unchanged
    db = _ldb.connect(str(db_path))
    rows_after = db.open_table("chunks").to_arrow().to_pylist()
    assert len(rows_after) == 3, "Row count changed — data was destroyed"
    s1_row = next(r for r in rows_after if r["chunk_id"] == "s1:c0")
    assert s1_row["full_text"] == "original content", (
        "full_text was mutated — row was not left intact after update failure"
    )


def test_recurrent_marker_removed_when_chunk_no_longer_qualifies(db_path: Path):
    """Regression: lint_corpus must REMOVE 'recurrent' from a chunk whose
    cross-session-neighbor count drops below CROSS_SESSION_COUNT_MIN, not
    just leave it stuck. Otherwise re-extracts, deleted sessions, or
    threshold tweaks leave stale markers that look freshly validated.

    Setup: seed a chunk in s1 with 'recurrent' already in corpus_derived_markers,
    but its only neighbor is in the SAME session s1 — so cross-session count
    is 0, below CROSS_SESSION_COUNT_MIN=2. After lint runs, 'recurrent' must
    be gone.
    """
    rows = [
        # Chunk in s1 that was previously marked recurrent (stale marker).
        _make_chunk_row(
            chunk_id="s1:c0",
            session_id="s1",
            embedding=_direction_vector(0),
            corpus_derived_markers=["recurrent"],
        ),
        # Another chunk in the SAME session s1 (does NOT count cross-session).
        _make_chunk_row(
            chunk_id="s1:c1",
            session_id="s1",
            embedding=_direction_vector(0),
        ),
    ]
    _create_table(db_path, rows)

    # Pre-condition: the stale marker is present before lint runs.
    db = lancedb.connect(str(db_path))
    pre_rows = db.open_table("chunks").to_arrow().to_pylist()
    s1c0_pre = next(r for r in pre_rows if r["chunk_id"] == "s1:c0")
    assert "recurrent" in s1c0_pre["corpus_derived_markers"], (
        "test setup: 'recurrent' should be present before lint runs"
    )

    # rebuild=True: full recompute, removes stale markers
    stats = lint_corpus_chunks(db_path, rebuild=True)

    # No cross-session neighbors -> recurrent_count should be 0.
    assert stats["recurrent"] == 0, (
        "Chunks with only same-session neighbors must not be marked recurrent"
    )

    # The stale marker must have been removed.
    db2 = lancedb.connect(str(db_path))
    post_rows = db2.open_table("chunks").to_arrow().to_pylist()
    s1c0_post = next(r for r in post_rows if r["chunk_id"] == "s1:c0")
    assert "recurrent" not in s1c0_post["corpus_derived_markers"], (
        "Stale 'recurrent' marker must be stripped when chunk no longer qualifies"
    )
    # corpus_markers_computed_at must be set (lint did run on this row).
    assert s1c0_post["corpus_markers_computed_at"] is not None


# ---------------------------------------------------------------------------
# NEW: rebuild=False / rebuild=True mode tests (verification adversarial review)
# ---------------------------------------------------------------------------


def test_lint_corpus_default_does_not_remove_stale_recurrent(db_path: Path, caplog) -> None:
    """rebuild=False (default, auto-trigger): leaves stale 'recurrent' alone
    and logs a WARN. Trade-off: safer under interruption, but operator must
    run rebuild=True manually to clean up.
    """
    import logging

    rows = [
        # Chunk in s1 with stale 'recurrent' but no cross-session high-sim neighbors.
        _make_chunk_row(
            chunk_id="s1:c0",
            session_id="s1",
            embedding=_direction_vector(0),
            corpus_derived_markers=["recurrent"],
        ),
        # Same-session neighbor — does NOT satisfy cross-session requirement.
        _make_chunk_row(
            chunk_id="s1:c1",
            session_id="s1",
            embedding=_direction_vector(0),
        ),
    ]
    _create_table(db_path, rows)

    with caplog.at_level(logging.WARNING, logger="community_brain.cli.lint_corpus"):
        stats = lint_corpus_chunks(db_path)  # rebuild=False is the default

    # Marker must still be present — auto-trigger does NOT remove stale markers.
    db = lancedb.connect(str(db_path))
    post_rows = db.open_table("chunks").to_arrow().to_pylist()
    s1c0 = next(r for r in post_rows if r["chunk_id"] == "s1:c0")
    assert "recurrent" in s1c0["corpus_derived_markers"], (
        "rebuild=False must leave stale 'recurrent' in place (no destructive write)"
    )

    # A WARN must have been emitted signalling the staleness.
    stale_warnings = [r for r in caplog.records if "stale" in r.message and "recurrent" in r.message]
    assert stale_warnings, (
        "rebuild=False must log a WARN about stale 'recurrent' marker so operators know cleanup is pending"
    )

    # recurrent_count in stats: stale marker was not re-added, so this chunk
    # was NOT counted as a new recurrent addition (it was already marked, and
    # the already-marked path increments only in the should_be_recurrent branch).
    assert stats["scanned"] == 2


def test_lint_corpus_rebuild_removes_stale_recurrent(db_path: Path) -> None:
    """rebuild=True (manual operator command): actually removes stale markers
    via row-rewrite for the empty-result case."""
    rows = [
        # Chunk in s1 with stale 'recurrent' marker, no qualifying cross-session neighbors.
        _make_chunk_row(
            chunk_id="s1:c0",
            session_id="s1",
            embedding=_direction_vector(0),
            corpus_derived_markers=["recurrent"],
        ),
        # Same-session neighbor — does NOT count as cross-session.
        _make_chunk_row(
            chunk_id="s1:c1",
            session_id="s1",
            embedding=_direction_vector(0),
        ),
    ]
    _create_table(db_path, rows)

    stats = lint_corpus_chunks(db_path, rebuild=True)

    db = lancedb.connect(str(db_path))
    post_rows = db.open_table("chunks").to_arrow().to_pylist()
    s1c0 = next(r for r in post_rows if r["chunk_id"] == "s1:c0")
    assert "recurrent" not in s1c0["corpus_derived_markers"], (
        "rebuild=True must remove stale 'recurrent' when chunk no longer qualifies"
    )
    assert stats["recurrent"] == 0


def test_lint_corpus_default_uses_update_not_delete_add(db_path: Path, monkeypatch) -> None:
    """Verify the auto-trigger path never calls table.delete (data-loss
    safety regression: prior fix used delete+add even in the default path)."""
    import lancedb as _ldb
    from community_brain.cli import lint_corpus as _lint_mod

    rows = [
        _make_chunk_row(
            chunk_id="s1:c0",
            session_id="s1",
            embedding=_direction_vector(0),
        ),
        _make_chunk_row(
            chunk_id="s2:c0",
            session_id="s2",
            embedding=_direction_vector(0),
        ),
        _make_chunk_row(
            chunk_id="s3:c0",
            session_id="s3",
            embedding=_direction_vector(0),
        ),
    ]
    _create_table(db_path, rows)

    # Monkeypatch: intercept lancedb.connect and wrap the table so table.delete raises.
    original_connect = _ldb.connect

    class _NoDeleteTable:
        def __init__(self, real_table):
            self._real = real_table

        def __getattr__(self, name):
            return getattr(self._real, name)

        def delete(self, *_a, **_kw):
            raise AssertionError(
                "table.delete() was called in the rebuild=False (auto-trigger) path — "
                "this is a data-loss risk and must NOT happen"
            )

    class _NoDeleteDB:
        def __init__(self, real_db):
            self._real = real_db

        def open_table(self, name):
            return _NoDeleteTable(self._real.open_table(name))

    def patched_connect(path, *args, **kwargs):
        return _NoDeleteDB(original_connect(path, *args, **kwargs))

    monkeypatch.setattr(_lint_mod, "lancedb", type("mod", (), {
        "connect": staticmethod(patched_connect),
    })())

    # rebuild=False (default) must not call table.delete — no exception from the patch.
    stats = lint_corpus_chunks(db_path)  # default rebuild=False
    assert stats["scanned"] == 3


# ---------------------------------------------------------------------------
# Phase 1 of ingest-lint-decoupling fix
# Spec: docs/superpowers/specs/2026-05-02-ingest-lint-decoupling-design.md
# ---------------------------------------------------------------------------


def _make_stable_corpus(n_recurrent_groups: int, n_unique: int) -> list[dict]:
    """Build a corpus with stable marker state — running lint twice in a row
    should produce zero state changes on the second pass.

    n_recurrent_groups: groups of 3 cross-session chunks each, all aligned to
        a unique direction. Each chunk in the group has 2 high-similarity
        neighbors in distinct other sessions, so all qualify as recurrent.
    n_unique: chunks each in their own session with a unique direction.
        No high-similarity neighbors anywhere, so none qualify as recurrent.

    Total chunks: n_recurrent_groups * 3 + n_unique.
    """
    rows: list[dict] = []
    for i in range(n_recurrent_groups):
        for sid_idx in range(3):
            rows.append(_make_chunk_row(
                chunk_id=f"rec{i}_s{sid_idx}",
                session_id=f"rec_session_{i}_{sid_idx}",
                embedding=_direction_vector(i),
            ))
    # Use a large offset for unique seeds to avoid collision with recurrent group directions.
    for i in range(n_unique):
        rows.append(_make_chunk_row(
            chunk_id=f"uniq{i}",
            session_id=f"uniq_s{i}",
            embedding=_direction_vector(1000 + i),
        ))
    return rows


@pytest.mark.parametrize("n_recurrent_groups,n_unique", [
    pytest.param(2, 4, id="small_10_chunks"),
    pytest.param(5, 10, id="medium_25_chunks"),
    pytest.param(10, 20, id="large_50_chunks"),
])
def test_lint_corpus_write_count_scales_with_state_changes_not_corpus_size(
    db_path: Path, monkeypatch, n_recurrent_groups: int, n_unique: int,
) -> None:
    """A stable second-pass lint must produce zero writes regardless of corpus size.

    Setup: build a corpus where every chunk's marker state is correct already
    (recurrent chunks marked, non-recurrent chunks unmarked). First lint pass
    establishes that state. Second pass should be a no-op at the write layer.

    Before Change A: every chunk gets a write per pass (timestamp bump),
        so a 50-chunk corpus does 50 writes on the second pass. That's
        the bug — at production scale (1500+) this saturates the LanceDB
        manifest writer and looks like "concurrent writers" contention.
    After Change A: only chunks whose marker state changes get written.
        On a stable corpus, zero writes.
    """
    import lancedb as _ldb
    from community_brain.cli import lint_corpus as _lint_mod

    rows = _make_stable_corpus(n_recurrent_groups, n_unique)
    _create_table(db_path, rows)

    # First pass establishes the baseline marker state. Writes are expected here.
    lint_corpus_chunks(db_path)

    # Second pass: count every table.update() call.
    update_count = {"value": 0}
    real_connect = _ldb.connect

    class _CountingTable:
        def __init__(self, real_table):
            self._real = real_table

        def __getattr__(self, name):
            return getattr(self._real, name)

        def update(self, *args, **kwargs):
            update_count["value"] += 1
            return self._real.update(*args, **kwargs)

    class _CountingDB:
        def __init__(self, real_db):
            self._real = real_db

        def __getattr__(self, name):
            return getattr(self._real, name)

        def open_table(self, name):
            return _CountingTable(self._real.open_table(name))

    def patched_connect(path, *args, **kwargs):
        return _CountingDB(real_connect(path, *args, **kwargs))

    monkeypatch.setattr(_lint_mod, "lancedb", type("mod", (), {
        "connect": staticmethod(patched_connect),
    })())

    lint_corpus_chunks(db_path)

    n_total = n_recurrent_groups * 3 + n_unique
    assert update_count["value"] == 0, (
        f"Stable second-pass lint on {n_total}-chunk corpus produced "
        f"{update_count['value']} writes — expected 0. Every chunk's marker "
        f"state was already correct from the first pass; no chunk's "
        f"corpus_derived_markers needs to change. The extra writes are "
        f"pure timestamp bumps (corpus_markers_computed_at) that don't "
        f"reflect real state change. Fix: drop the no-op branches in "
        f"lint_corpus_chunks (Change A in spec 2026-05-02-ingest-lint-decoupling-design.md)."
    )


def _count_table_updates(monkeypatch) -> dict[str, int]:
    """Install a patched lancedb.connect that counts table.update() calls.

    Returns a dict {"value": int} that increments on every update. The dict
    is mutable so the caller can read it after lint_corpus_chunks runs.
    """
    import lancedb as _ldb
    from community_brain.cli import lint_corpus as _lint_mod

    counter = {"value": 0}
    real_connect = _ldb.connect

    class _CountingTable:
        def __init__(self, real_table):
            self._real = real_table

        def __getattr__(self, name):
            return getattr(self._real, name)

        def update(self, *args, **kwargs):
            counter["value"] += 1
            return self._real.update(*args, **kwargs)

    class _CountingDB:
        def __init__(self, real_db):
            self._real = real_db

        def __getattr__(self, name):
            return getattr(self._real, name)

        def open_table(self, name):
            return _CountingTable(self._real.open_table(name))

    def patched_connect(path, *args, **kwargs):
        return _CountingDB(real_connect(path, *args, **kwargs))

    monkeypatch.setattr(_lint_mod, "lancedb", type("mod", (), {
        "connect": staticmethod(patched_connect),
    })())
    return counter


def test_lint_corpus_skips_writes_when_marker_state_unchanged(
    db_path: Path, monkeypatch,
) -> None:
    """Single-pass lint on a corpus where no chunk needs a marker change
    must not call table.update() at all.

    Setup: 4 unique-direction chunks across 4 sessions. None have cross-session
    high-similarity neighbors (different directions), so none qualify as
    recurrent. Pre-existing corpus_derived_markers are empty. The desired
    end-state matches the current state for every chunk — zero writes needed.
    """
    rows = [
        _make_chunk_row(
            chunk_id=f"uniq{i}:c0",
            session_id=f"uniq_s{i}",
            embedding=_direction_vector(i),
        )
        for i in range(4)
    ]
    _create_table(db_path, rows)

    counter = _count_table_updates(monkeypatch)
    lint_corpus_chunks(db_path)

    assert counter["value"] == 0, (
        f"lint_corpus called table.update() {counter['value']} times on a "
        "corpus where every chunk already has the correct marker state. "
        "Expected 0 writes."
    )


def test_lint_corpus_writes_only_when_state_changes(
    db_path: Path, monkeypatch,
) -> None:
    """Lint on a corpus with exactly one chunk that needs to flip recurrent
    must call table.update() exactly once — the one transition.

    Setup: 3 chunks aligned across 3 sessions (all qualify as recurrent),
    plus 5 unique chunks (none qualify). All chunks start with empty markers.
    Expected writes = 3 (the recurrent chunks transition empty → ['recurrent']).
    """
    rows = []
    # 3 cross-session aligned chunks → all transition to recurrent (3 writes)
    for sid_idx in range(3):
        rows.append(_make_chunk_row(
            chunk_id=f"rec_s{sid_idx}",
            session_id=f"rec_session_{sid_idx}",
            embedding=_direction_vector(0),
        ))
    # 5 unique chunks → no state change needed (0 writes)
    for i in range(5):
        rows.append(_make_chunk_row(
            chunk_id=f"uniq{i}",
            session_id=f"uniq_s{i}",
            embedding=_direction_vector(100 + i),
        ))
    _create_table(db_path, rows)

    counter = _count_table_updates(monkeypatch)
    stats = lint_corpus_chunks(db_path)

    assert stats["recurrent"] == 3, (
        "Three cross-session aligned chunks should all qualify as recurrent"
    )
    assert counter["value"] == 3, (
        f"Expected exactly 3 writes (one per recurrent transition), "
        f"got {counter['value']}. The 5 unique chunks should not have "
        "triggered any writes since their state was already correct."
    )
