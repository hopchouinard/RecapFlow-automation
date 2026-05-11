#!/usr/bin/env bash
# Minimal sanity test for release-corpus.sh.
# Builds a tiny fake LanceDB on this machine and runs the script's
# compaction + verification + tarball steps against it (no VM needed).
#
# Skip the rsync-from-VM portion by pre-staging the fake DB at the
# location the script expects.

set -euo pipefail

VERSION="v0.0.0-test"
STAGING="/tmp/corpus-staging-${VERSION}"
OUTPUT_DIR="/tmp/corpus-release-test"
PYTHON="$(pwd)/community-brain/.venv/bin/python"

rm -rf "${STAGING}" "${OUTPUT_DIR}"
mkdir -p "${STAGING}/lancedb/nomic-v1"

# Build a tiny clean-v3 fake corpus directly into staging.
"${PYTHON}" <<PYEOF
import lancedb
import pyarrow as pa
db = lancedb.connect("${STAGING}/lancedb/nomic-v1")
schema = pa.schema([
    ("session_id", pa.string()),
    ("chunk_id", pa.string()),
    ("bm25_text", pa.string()),
])
table = db.create_table("chunks", schema=schema, mode="overwrite")
table.add([
    {"session_id": "s1", "chunk_id": "s1:c0", "bm25_text": "alpha beta gamma"},
    {"session_id": "s1", "chunk_id": "s1:c1", "bm25_text": "delta epsilon"},
    {"session_id": "s2", "chunk_id": "s2:c0", "bm25_text": "zeta eta theta"},
])
table.create_fts_index("bm25_text", replace=True)
print("staging built")
PYEOF

# Run only the local-effect portion of release-corpus.sh.
echo "--- compact ---"
"${PYTHON}" - <<PYEOF
import lancedb
from datetime import timedelta
db = lancedb.connect("${STAGING}/lancedb/nomic-v1")
t = db.open_table("chunks")
# optimize() with cleanup_older_than=0 does compaction + prune in one call
# (the old two-step optimize()+cleanup_old_versions() API requires pylance).
t.optimize(cleanup_older_than=timedelta(seconds=0))
PYEOF

echo "--- verify ---"
"${PYTHON}" -m community_brain.cli.verify_corpus_clean_v3 \
    "${STAGING}/lancedb/nomic-v1"

echo "--- tar + sha + manifest ---"
mkdir -p "${OUTPUT_DIR}"
cd "${OUTPUT_DIR}"
tar -czf "corpus-${VERSION}.tar.gz" -C "${STAGING}" .
# SHA-256 — detect tool per platform.
if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "corpus-${VERSION}.tar.gz" > sha256sum.txt
else
    shasum -a 256 "corpus-${VERSION}.tar.gz" > sha256sum.txt
fi
"${PYTHON}" -m community_brain.cli.write_corpus_manifest \
    --staging "${STAGING}" \
    --out "${OUTPUT_DIR}/corpus-manifest.json" \
    --version "${VERSION}"

echo "--- artifacts ---"
ls -lh "${OUTPUT_DIR}"
cat "${OUTPUT_DIR}/corpus-manifest.json"

echo
echo "OK: release-corpus.sh local sanity test passed"
