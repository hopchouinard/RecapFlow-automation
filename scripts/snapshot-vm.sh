#!/usr/bin/env bash
# RecapFlow VM-side snapshot script.
# Stages a daily snapshot under STAGING_ROOT/<ISO-timestamp>/ and updates
# STAGING_ROOT/latest -> <ISO-timestamp>.
#
# Usage:
#   snapshot-vm.sh                    # daily snapshot
#   snapshot-vm.sh now                # ad-hoc snapshot (same behavior)
#
# Env overrides:
#   STAGING_ROOT (default: /var/lib/recapflow-backup/staging)
#   REPO_ROOT    (default: directory containing this script's parent)
#   RETENTION    (default: 7  — number of snapshots to keep)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/manifest.sh
source "${SCRIPT_DIR}/lib/manifest.sh"
# shellcheck source=lib/preflight.sh
source "${SCRIPT_DIR}/lib/preflight.sh"

STAGING_ROOT="${STAGING_ROOT:-/var/lib/recapflow-backup/staging}"
REPO_ROOT="${REPO_ROOT:-$(cd "${SCRIPT_DIR}/.." && pwd)}"
RETENTION="${RETENTION:-7}"

log() {
  echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*"
}

main() {
  preflight_require_not_root

  local timestamp
  timestamp=$(date -u +%Y-%m-%dT%H-%M-%SZ)
  local staging="${STAGING_ROOT}/${timestamp}"

  log "starting snapshot: ${staging}"

  mkdir -p "${staging}/postgres"
  mkdir -p "${staging}/lancedb"
  mkdir -p "${staging}/openwebui"
  mkdir -p "${staging}/secrets"
  mkdir -p "${staging}/code-snapshot"

  log "dumping postgres"
  docker exec n8n_db pg_dump -U n8n -F c --no-acl --no-owner -f /tmp/n8n.pgdump n8n
  docker cp n8n_db:/tmp/n8n.pgdump "${staging}/postgres/n8n.pgdump"
  docker exec n8n_db rm /tmp/n8n.pgdump

  log "snapshotting lancedb"
  docker compose --project-directory "${REPO_ROOT}" pause retrieval-server
  trap 'docker compose --project-directory "${REPO_ROOT}" unpause retrieval-server || true' EXIT
  # LanceDB files are owned by root (container process UID). docker exec into
  # a paused container is refused. docker cp from a paused container works and
  # uses the daemon's kernel-level copy path — ~5x faster than alpine volume
  # tar because it avoids per-file Docker API round-trips. Produces a POSIX
  # tar archive at staging/lancedb/lancedb.tar. Restore: tar -xf lancedb.tar.
  # NOTE: with 5GB of version history this step takes ~20 min. Run
  # `lance compact` on the table before the first production cron to bring
  # _versions/ down to <100MB and get this under 2 minutes.
  docker cp "community_brain_retrieval:/data/lancedb" - > "${staging}/lancedb/lancedb.tar"
  docker compose --project-directory "${REPO_ROOT}" unpause retrieval-server
  trap - EXIT

  log "snapshotting open-webui volume"
  docker run --rm -v open-webui-data:/data -v "${staging}/openwebui:/out" alpine \
    tar -cf /out/open-webui-data.tar -C /data .

  log "tarring n8n state"
  tar -cf "${staging}/n8n-state.tar.zst" \
    --use-compress-program=zstd \
    -C "${REPO_ROOT}" \
    data n8n-state output watch historical 2>/dev/null || {
      log "WARN: some directories missing; continuing"
    }

  log "copying secrets"
  if [ -f "${REPO_ROOT}/.env" ]; then
    install -m 600 "${REPO_ROOT}/.env" "${staging}/secrets/.env"
  fi
  if [ -f "${REPO_ROOT}/community-brain/config/.env" ]; then
    install -m 600 "${REPO_ROOT}/community-brain/config/.env" "${staging}/secrets/community-brain.env"
  fi

  log "copying code snapshot"
  cp "${REPO_ROOT}/docker-compose.yml" "${staging}/code-snapshot/docker-compose.yml"
  cp -r "${REPO_ROOT}/workflows" "${staging}/code-snapshot/workflows"
  cp -r "${REPO_ROOT}/prompts" "${staging}/code-snapshot/prompts"

  log "writing manifest"
  local n8n_version
  n8n_version=$(docker exec n8n n8n --version 2>/dev/null | tail -1 || echo "unknown")
  local rs_version
  rs_version=$(docker exec community_brain_retrieval python -c "from community_brain import __version__; print(__version__)" 2>/dev/null || echo "unknown")
  cd "${staging}"
  manifest_write "${timestamp}" "${n8n_version}" "${rs_version}"

  log "verifying manifest"
  manifest_verify "${staging}"

  log "updating latest symlink"
  ln -sfn "${timestamp}" "${STAGING_ROOT}/latest"

  log "pruning old snapshots (keeping ${RETENTION})"
  cd "${STAGING_ROOT}"
  ls -1d 20*-*-*T*-*-*Z 2>/dev/null | sort -r | tail -n "+$((RETENTION + 1))" | while read -r old; do
    log "  pruning ${old}"
    rm -rf "${old}"
  done

  log "snapshot complete: ${staging}"
}

main "$@"
