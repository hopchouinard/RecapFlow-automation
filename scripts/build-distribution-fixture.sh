#!/usr/bin/env bash
# build-distribution-fixture.sh — construct the tiny clean-v3 LanceDB
# fixture used by the community-brain-distribution repo's CI smoke test
# (verify-on-pr.yml).
#
# The fixture is a 2-session / 3-chunk LanceDB with 768-dim zero vectors —
# enough to exercise route shape, schema-version metadata, /sessions
# counting, and FTS index presence, without shipping real corpus content.
#
# Run when:
#   - the distribution repo's fixture is being created from scratch, or
#   - the LanceDB schema evolves and the fixture needs to be regenerated.
#
# This script lives in the operator repo because it depends on the
# community-brain Python package (community_brain.ingestion.schema). The
# OUTPUT is committed to the public distribution repo; the BUILDER stays
# private to avoid leaking operator-side paths.
#
# Usage:
#   ./scripts/build-distribution-fixture.sh [TARGET_CORPUS_DIR]
#
# TARGET_CORPUS_DIR defaults to ../community-brain-distribution/tests/fixtures/corpus
# (i.e. assumes the distribution repo is checked out as a sibling).

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEFAULT_TARGET="${REPO_ROOT}/../community-brain-distribution/tests/fixtures/corpus"
CORPUS="${1:-$DEFAULT_TARGET}"

PYTHON="${COMMUNITY_BRAIN_VENV:-${REPO_ROOT}/community-brain/.venv}/bin/python"

if [[ ! -x "$PYTHON" ]]; then
    echo "ERROR: python venv not found at $(dirname "$PYTHON")" >&2
    echo "  Either set COMMUNITY_BRAIN_VENV pointing at a venv that has the" >&2
    echo "  community-brain package installed, or run from the operator repo" >&2
    echo "  with community-brain/.venv present." >&2
    exit 2
fi

# Resolve TARGET to an absolute path before we change directory contexts.
CORPUS="$(cd "$(dirname "$CORPUS")" 2>/dev/null && pwd)/$(basename "$CORPUS")" || {
    echo "ERROR: parent of TARGET_CORPUS_DIR does not exist: $(dirname "$CORPUS")" >&2
    exit 2
}

rm -rf "$CORPUS"
mkdir -p "$CORPUS/lancedb/nomic-v1"

"$PYTHON" - <<PYEOF
import json, pathlib
import lancedb

# Reuse the REAL pyarrow schema so every column /sessions reads
# (session_date, session_title, content_type, has_unresolved_question,
# session_themes) and every field the server expects (e.g. \`embedding\`,
# not \`vector\`) is present. Anything less makes _load_all_session_rows()
# return empty and verify-install.sh fails on count-mismatch.
from community_brain.ingestion.schema import pyarrow_table_schema, SCHEMA_VERSION

DB_PATH = "${CORPUS}/lancedb/nomic-v1"
db = lancedb.connect(DB_PATH)
schema = pyarrow_table_schema()
table = db.create_table("chunks", schema=schema, mode="overwrite")

import datetime as _dt
import pyarrow.types as _pat

pa_types_is_string = _pat.is_string
pa_types_is_floating = _pat.is_floating
pa_types_is_integer = _pat.is_integer
pa_types_is_boolean = _pat.is_boolean
pa_types_is_timestamp = _pat.is_timestamp
pa_types_is_date = _pat.is_date
pa_types_is_fixed_size_list = _pat.is_fixed_size_list
pa_types_is_list = _pat.is_list
pa_types_is_struct = _pat.is_struct


def _default_for_field(field):
    """Best-effort default value matching a pyarrow field type."""
    t = field.type
    if pa_types_is_string(t):
        if field.name in ("session_id", "chunk_id", "bm25_text",
                          "session_title", "content_type", "extraction_status"):
            return f"fixture-{field.name}"
        return ""
    if pa_types_is_floating(t):
        return 0.0
    if pa_types_is_integer(t):
        return 0
    if pa_types_is_boolean(t):
        return False
    if pa_types_is_timestamp(t) or pa_types_is_date(t):
        return _dt.datetime(2026, 5, 10, 0, 0, 0, tzinfo=_dt.timezone.utc)
    if pa_types_is_fixed_size_list(t):
        return [0.0] * t.list_size  # 768-dim zero embedding
    if pa_types_is_list(t):
        return []
    if pa_types_is_struct(t):
        return None
    return None


def _make_row(session_id, chunk_id, bm25_text):
    row = {f.name: _default_for_field(f) for f in schema}
    row["session_id"] = session_id
    row["chunk_id"] = chunk_id
    row["bm25_text"] = bm25_text
    if "extraction_status" in row:
        row["extraction_status"] = "success"
    if "session_date" in row:
        row["session_date"] = _dt.datetime(2026, 1, 1, tzinfo=_dt.timezone.utc)
    if "session_title" in row:
        row["session_title"] = f"Fixture session {session_id}"
    if "content_type" in row:
        row["content_type"] = "prepared_transcript"
    if "has_unresolved_question" in row:
        row["has_unresolved_question"] = False
    return row


rows = [
    _make_row("fixture-001", "fixture-001:c0", "hello fixture corpus"),
    _make_row("fixture-001", "fixture-001:c1", "second chunk of fixture-001"),
    _make_row("fixture-002", "fixture-002:c0", "another fixture session"),
]
table.add(rows)
table.create_fts_index("bm25_text", replace=True)

manifest = {
    "corpus_version": "v0.0.0-fixture",
    "schema_version": SCHEMA_VERSION,
    "embedding_model": "nomic-embed-text",
    "session_count": 2,
    "chunk_count": 3,
    "generation_timestamp_utc": "2026-05-10T00:00:00Z",
}
pathlib.Path("${CORPUS}/corpus-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
print(f"fixture built at ${CORPUS} (schema_version={SCHEMA_VERSION})")
PYEOF
