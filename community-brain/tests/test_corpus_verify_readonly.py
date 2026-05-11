"""verify_corpus_v3_state_readonly: structural check + index-presence assert,
no mutation. Per Tier B spec §5.6."""
import pytest
import lancedb
import pyarrow as pa

from community_brain.query.corpus_verify import (
    CorpusInvalidError,
    verify_corpus_v3_state_readonly,
)


def _make_table(tmp_path, schema_fields):
    """Build a test LanceDB table at tmp_path with given fields."""
    db = lancedb.connect(str(tmp_path))
    schema = pa.schema(schema_fields)
    table = db.create_table("chunks", schema=schema, mode="overwrite")
    return table


def test_readonly_passes_on_clean_v3_table(tmp_path):
    """A table with bm25_text column AND an FTS index on it passes."""
    schema = [
        ("session_id", pa.string()),
        ("bm25_text", pa.string()),
    ]
    table = _make_table(tmp_path, schema)
    # Need data to build an FTS index
    table.add([{"session_id": "s1", "bm25_text": "hello world"}])
    table.create_fts_index("bm25_text", replace=True)
    # Should not raise
    verify_corpus_v3_state_readonly(table)


def test_readonly_raises_when_bm25_text_column_missing(tmp_path):
    """No bm25_text column → CorpusInvalidError (pre-v1.1 corpus)."""
    schema = [
        ("session_id", pa.string()),
        ("full_text", pa.string()),
    ]
    table = _make_table(tmp_path, schema)
    with pytest.raises(CorpusInvalidError, match="bm25_text"):
        verify_corpus_v3_state_readonly(table)


def test_readonly_raises_when_fts_index_missing(tmp_path):
    """bm25_text column present but no FTS index → CorpusInvalidError.
    Critical: the function must NOT try to create the index."""
    schema = [
        ("session_id", pa.string()),
        ("bm25_text", pa.string()),
    ]
    table = _make_table(tmp_path, schema)
    # Note: no index built
    with pytest.raises(CorpusInvalidError, match="FTS"):
        verify_corpus_v3_state_readonly(table)


def test_readonly_does_not_call_ensure_fts_index(tmp_path, monkeypatch):
    """Spy on ensure_fts_index — readonly variant must not invoke it."""
    schema = [
        ("session_id", pa.string()),
        ("bm25_text", pa.string()),
    ]
    table = _make_table(tmp_path, schema)
    table.add([{"session_id": "s1", "bm25_text": "hello world"}])
    table.create_fts_index("bm25_text", replace=True)

    calls = []
    import community_brain.query.corpus_verify as cv
    monkeypatch.setattr(
        cv, "ensure_fts_index",
        lambda *args, **kwargs: calls.append((args, kwargs))
    )
    verify_corpus_v3_state_readonly(table)
    assert calls == [], (
        f"verify_corpus_v3_state_readonly must NOT call ensure_fts_index "
        f"(would mutate). Got calls: {calls}"
    )


def test_readonly_accepts_mixed_case_index_type(tmp_path, monkeypatch):
    """Regression guard: LanceDB returns "Inverted" (mixed case) on some
    versions. Without delegating to has_fts_index (which is case-insensitive),
    the readonly check would falsely reject a valid corpus.

    Simulates by monkeypatching list_indices to return an index object
    with index_type='Inverted' instead of 'INVERTED'. The function must
    still accept it.
    """
    schema = [
        ("session_id", pa.string()),
        ("bm25_text", pa.string()),
    ]
    table = _make_table(tmp_path, schema)
    table.add([{"session_id": "s1", "bm25_text": "hello world"}])
    table.create_fts_index("bm25_text", replace=True)

    # Wrap list_indices to return mixed-case index_type. If the readonly check
    # were doing exact-match against ("FTS", "INVERTED"), it would fail here.
    class _MixedCaseIndex:
        def __init__(self, real_idx):
            self.index_type = "Inverted"  # mixed case, not "INVERTED"
            self.columns = real_idx.columns
            self.name = real_idx.name

    real_list_indices = table.list_indices
    def fake_list_indices():
        return [_MixedCaseIndex(idx) for idx in real_list_indices()]
    monkeypatch.setattr(table, "list_indices", fake_list_indices)

    # Must not raise.
    verify_corpus_v3_state_readonly(table)
