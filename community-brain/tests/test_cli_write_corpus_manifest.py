"""write_corpus_manifest CLI: emits corpus-manifest.json per Tier B spec §5.5.

Manifest fields:
  - corpus_version (string, from --version flag)
  - schema_version (from community_brain.ingestion.schema.SCHEMA_VERSION)
  - embedding_model (from COMMUNITY_BRAIN_EMBED_MODEL env or default)
  - session_count (distinct values of session_id column)
  - chunk_count (total row count)
  - generation_timestamp_utc (ISO 8601 'Z')
"""
import json
import os
import re
import subprocess
import sys

import lancedb
import pyarrow as pa

from community_brain.ingestion.schema import SCHEMA_VERSION


def _seed_db(path, sessions: list[str], chunks_per_session: int = 2):
    db = lancedb.connect(str(path))
    schema = pa.schema([
        ("session_id", pa.string()),
        ("chunk_id", pa.string()),
        ("bm25_text", pa.string()),
    ])
    table = db.create_table("chunks", schema=schema, mode="overwrite")
    rows = []
    for s in sessions:
        for i in range(chunks_per_session):
            rows.append({
                "session_id": s,
                "chunk_id": f"{s}:c{i}",
                "bm25_text": f"chunk {i} of {s}",
            })
    table.add(rows)
    return path


def _run_cli(staging_path, out_path, version, extra_env=None):
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)
    return subprocess.run(
        [sys.executable, "-m", "community_brain.cli.write_corpus_manifest",
         "--staging", str(staging_path),
         "--out", str(out_path),
         "--version", version],
        capture_output=True, text=True, env=env,
    )


def test_writes_manifest_with_expected_fields(tmp_path):
    db_dir = tmp_path / "lancedb" / "nomic-v1"
    db_dir.mkdir(parents=True)
    _seed_db(db_dir, sessions=["s1", "s2", "s3"], chunks_per_session=4)
    out = tmp_path / "manifest.json"

    result = _run_cli(tmp_path, out, "v1.0.0")
    assert result.returncode == 0, f"stderr: {result.stderr}"

    data = json.loads(out.read_text())
    assert data["corpus_version"] == "v1.0.0"
    assert data["schema_version"] == SCHEMA_VERSION
    assert data["session_count"] == 3
    assert data["chunk_count"] == 12  # 3 sessions * 4 chunks
    assert "embedding_model" in data
    assert "generation_timestamp_utc" in data
    # ISO 8601 with 'Z' suffix
    assert re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", data["generation_timestamp_utc"])
    assert data["generation_timestamp_utc"].endswith("Z")


def test_embedding_model_respects_env(tmp_path):
    db_dir = tmp_path / "lancedb" / "nomic-v1"
    db_dir.mkdir(parents=True)
    _seed_db(db_dir, sessions=["s1"], chunks_per_session=1)
    out = tmp_path / "m.json"

    result = _run_cli(tmp_path, out, "v0.0.1",
                      extra_env={"COMMUNITY_BRAIN_EMBED_MODEL": "custom-model"})
    assert result.returncode == 0, f"stderr: {result.stderr}"
    data = json.loads(out.read_text())
    assert data["embedding_model"] == "custom-model"


def test_exits_2_on_missing_db(tmp_path):
    out = tmp_path / "m.json"
    bogus = tmp_path / "nonexistent"
    result = _run_cli(bogus, out, "v1.0.0")
    assert result.returncode == 2, f"stderr: {result.stderr}"
