#!/usr/bin/env bash
# scripts/release-corpus.sh — produce a Tier B corpus tarball + manifest.
#
# Performs the safe-snapshot sequence from spec §5.4:
#   1. Pauses retrieval-server on the VM
#   2. rsync-snapshots the live LanceDB to a staging path
#   3. Unpauses retrieval-server
#   4. Compacts the staging copy (LanceDB optimize with cleanup_older_than)
#   5. Verifies clean v3 state on the compacted copy
#   6. Tarballs + computes SHA-256 + writes corpus-manifest.json
#
# Output files (in $OUTPUT_DIR, default /tmp/corpus-release):
#   corpus-<VERSION>.tar.gz
#   sha256sum.txt
#   corpus-manifest.json
#
# Usage:
#   ./scripts/release-corpus.sh <VERSION>
#   ./scripts/release-corpus.sh v1.0.0
#
# Environment overrides:
#   VM_HOST                 (default: n8n-automation.patchoutech.lab)
#   VM_USER                 (default: pchouinard)
#   VM_LANCEDB_PATH         (default: /home/pchouinard/n8n/community-brain/lancedb)
#   VM_COMPOSE_DIR          (default: /home/pchouinard/n8n)
#   OUTPUT_DIR              (default: /tmp/corpus-release)
#   COMMUNITY_BRAIN_VENV    (default: ./community-brain/.venv)
#
# Exit codes:
#   0 — success
#   1 — verification or release step failed
#   2 — usage error or pre-flight failure

set -euo pipefail

if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <VERSION>  (e.g. $0 v1.0.0)" >&2
    exit 2
fi

VERSION="$1"
VM_HOST="${VM_HOST:-n8n-automation.patchoutech.lab}"
VM_USER="${VM_USER:-pchouinard}"
VM_LANCEDB_PATH="${VM_LANCEDB_PATH:-/home/pchouinard/n8n/community-brain/lancedb}"
VM_COMPOSE_DIR="${VM_COMPOSE_DIR:-/home/pchouinard/n8n}"
OUTPUT_DIR="${OUTPUT_DIR:-/tmp/corpus-release}"
COMMUNITY_BRAIN_VENV="${COMMUNITY_BRAIN_VENV:-$(pwd)/community-brain/.venv}"

PYTHON="${COMMUNITY_BRAIN_VENV}/bin/python"

# SSH defaults for every VM call. ServerAliveInterval+CountMax detects dead
# connections during the multi-minute rsync window; ConnectTimeout bounds
# the trap-time unpause call so the script never hangs on a flapping network.
SSH_OPTS=(-o BatchMode=yes -o ConnectTimeout=30 -o ServerAliveInterval=10 -o ServerAliveCountMax=3)

# Local staging path (on operator workstation; we rsync FROM the VM TO here).
STAGING_LOCAL="/tmp/corpus-staging-${VERSION}"

log() { echo "[release-corpus] $*" >&2; }

# Pre-flight checks
[[ -x "$PYTHON" ]] || { log "FATAL: python not found at $PYTHON"; exit 2; }
ssh "${SSH_OPTS[@]}" "${VM_USER}@${VM_HOST}" 'true' \
    || { log "FATAL: cannot SSH to ${VM_USER}@${VM_HOST}"; exit 2; }

# Step 1: pause retrieval-server on VM and rsync the live LanceDB.
log "pausing retrieval-server on ${VM_HOST}"
ssh "${SSH_OPTS[@]}" "${VM_USER}@${VM_HOST}" \
    "cd ${VM_COMPOSE_DIR} && docker compose pause retrieval-server"

# Trap to ensure unpause on any failure.
unpause_vm() {
    log "unpausing retrieval-server"
    ssh "${SSH_OPTS[@]}" "${VM_USER}@${VM_HOST}" \
        "cd ${VM_COMPOSE_DIR} && docker compose unpause retrieval-server" \
        || log "WARN: unpause failed; manual recovery required"
}
trap unpause_vm EXIT

log "rsyncing LanceDB from VM (this is the longest step; ~5-10 min at 5 GB)"
rm -rf "${STAGING_LOCAL}"
mkdir -p "${STAGING_LOCAL}/lancedb"
# --no-owner --no-group: the retrieval-server container runs as root, so
# files on the VM host are root-owned. A non-root operator's rsync -a
# would exit 23 trying to preserve ownership. We don't need original
# ownership/groups on the staging copy — only file contents and timestamps.
rsync -a --no-owner --no-group \
    "${VM_USER}@${VM_HOST}:${VM_LANCEDB_PATH}/" \
    "${STAGING_LOCAL}/lancedb/"

log "unpausing retrieval-server"
ssh "${SSH_OPTS[@]}" "${VM_USER}@${VM_HOST}" \
    "cd ${VM_COMPOSE_DIR} && docker compose unpause retrieval-server"
trap - EXIT  # clear the unpause trap; we already unpaused

# Step 2: compact the staging copy.
log "compacting staged LanceDB"
"${PYTHON}" - <<PYEOF
import lancedb
from datetime import timedelta
db = lancedb.connect("${STAGING_LOCAL}/lancedb/nomic-v1")
table = db.open_table("chunks")
# optimize() with cleanup_older_than=0 does compaction + prune in one call
# (the old two-step optimize()+cleanup_old_versions() API requires pylance).
table.optimize(cleanup_older_than=timedelta(seconds=0))
print("compaction OK")
PYEOF

# Step 3: assert clean v3 state on compacted copy.
log "verifying clean v3 state on compacted copy"
"${PYTHON}" -m community_brain.cli.verify_corpus_clean_v3 \
    "${STAGING_LOCAL}/lancedb/nomic-v1"

# Step 4: produce output artifacts.
mkdir -p "${OUTPUT_DIR}"
cd "${OUTPUT_DIR}"

TARBALL="corpus-${VERSION}.tar.gz"
log "tarring -> ${OUTPUT_DIR}/${TARBALL}"
tar -czf "${TARBALL}" -C "${STAGING_LOCAL}" .

# SHA-256 — detect tool per platform (operator may be on macOS).
log "writing sha256sum.txt"
if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "${TARBALL}" > sha256sum.txt
elif command -v shasum >/dev/null 2>&1; then
    # Match sha256sum format: "<hash>  <filename>"
    shasum -a 256 "${TARBALL}" > sha256sum.txt
else
    log "FATAL: neither sha256sum nor shasum found"
    exit 2
fi

log "writing corpus-manifest.json"
"${PYTHON}" -m community_brain.cli.write_corpus_manifest \
    --staging "${STAGING_LOCAL}" \
    --out "${OUTPUT_DIR}/corpus-manifest.json" \
    --version "${VERSION}"

log "release artifacts ready in ${OUTPUT_DIR}:"
ls -lh "${OUTPUT_DIR}"

log "next steps:"
log "  1. gh release create ${VERSION} ${OUTPUT_DIR}/${TARBALL} \\"
log "       ${OUTPUT_DIR}/sha256sum.txt ${OUTPUT_DIR}/corpus-manifest.json \\"
log "       --repo <operator>/community-brain-distribution"
log "  2. Open PR in community-brain-distribution updating download-corpus.sh"
log "     constants: CORPUS_VERSION=\"${VERSION}\", EXPECTED_SHA256=\"\$(awk '{print \$1}' sha256sum.txt)\""
