"""verify_corpus_clean_v3 CLI: release-time gate per Tier B spec §5.4.

Asserts a compacted-and-staged LanceDB is in clean v3 state (FTS index
built on bm25_text, no legacy v2 FTS index on full_text). Exit 0 if
clean; exit non-zero with stderr message if not.
"""
import subprocess
import sys

import lancedb
import pyarrow as pa


def _make_db(path, *, with_bm25=True, with_fts_index=True, with_legacy_fts=False):
    db = lancedb.connect(str(path))
    fields = [("session_id", pa.string())]
    if with_bm25:
        fields.append(("bm25_text", pa.string()))
    fields.append(("full_text", pa.string()))
    table = db.create_table("chunks", schema=pa.schema(fields), mode="overwrite")
    if with_bm25:
        table.add([{"session_id": "s1", "bm25_text": "hi", "full_text": "hi"}])
    else:
        table.add([{"session_id": "s1", "full_text": "hi"}])
    if with_fts_index and with_bm25:
        table.create_fts_index("bm25_text", replace=True)
    if with_legacy_fts:
        table.create_fts_index("full_text", replace=True)
    return path


def _run_cli(db_path):
    return subprocess.run(
        [sys.executable, "-m",
         "community_brain.cli.verify_corpus_clean_v3", str(db_path)],
        capture_output=True, text=True,
    )


def test_cli_exits_zero_on_clean_v3_corpus(tmp_path):
    _make_db(tmp_path, with_bm25=True, with_fts_index=True, with_legacy_fts=False)
    result = _run_cli(tmp_path)
    assert result.returncode == 0, f"stderr: {result.stderr}"


def test_cli_exits_nonzero_when_bm25_column_missing(tmp_path):
    _make_db(tmp_path, with_bm25=False, with_fts_index=False)
    result = _run_cli(tmp_path)
    assert result.returncode == 1, f"stderr: {result.stderr}"
    assert "bm25_text" in result.stderr.lower()


def test_cli_exits_nonzero_when_fts_index_missing(tmp_path):
    _make_db(tmp_path, with_bm25=True, with_fts_index=False)
    result = _run_cli(tmp_path)
    assert result.returncode == 1, f"stderr: {result.stderr}"
    assert "fts" in result.stderr.lower() or "index" in result.stderr.lower()


def test_cli_exits_nonzero_when_legacy_full_text_fts_present(tmp_path):
    _make_db(tmp_path, with_bm25=True, with_fts_index=True, with_legacy_fts=True)
    result = _run_cli(tmp_path)
    assert result.returncode == 1, f"stderr: {result.stderr}"
    assert "full_text" in result.stderr.lower() or "legacy" in result.stderr.lower()


def test_cli_handles_nonexistent_path(tmp_path):
    bogus = tmp_path / "nonexistent"
    result = _run_cli(bogus)
    assert result.returncode == 2, f"stderr: {result.stderr}"
