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
#   STAGING_ROOT (default: ~/recapflow-backup/staging — no sudo required)
#   REPO_ROOT    (default: directory containing this script's parent)
#   RETENTION    (default: 4  — number of snapshots to keep)
#   MIN_FREE_GB  (default: 10 — minimum free space required before snapshotting)
#   METRICS_DIR  (default: /var/lib/node_exporter/textfile — Prometheus
#                textfile-collector dir; metric emission is silently skipped
#                if this dir is missing or unwritable)
#
# Failure handling:
#   - Old snapshots beyond RETENTION are pruned at the START of every run, so
#     repeated failures cannot starve disk space indefinitely.
#   - On any failure (set -e), the EXIT trap unpauses the retrieval-server (if
#     paused) and removes the partial staging dir — no zombie partials accrete.
#
# Observability:
#   - Every run (success or failure) updates METRICS_DIR/recapflow_snapshot.prom
#     with last_run_timestamp_seconds, last_exit_code, last_duration_seconds.
#   - Successful runs additionally update METRICS_DIR/recapflow_snapshot_success.prom
#     with last_success_timestamp_seconds. Prometheus scrapes both via the
#     node_exporter textfile collector and alerts on stale success timestamps.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/manifest.sh
source "${SCRIPT_DIR}/lib/manifest.sh"
# shellcheck source=lib/preflight.sh
source "${SCRIPT_DIR}/lib/preflight.sh"

STAGING_ROOT="${STAGING_ROOT:-${HOME}/recapflow-backup/staging}"
REPO_ROOT="${REPO_ROOT:-$(cd "${SCRIPT_DIR}/.." && pwd)}"
RETENTION="${RETENTION:-4}"
MIN_FREE_GB="${MIN_FREE_GB:-10}"
METRICS_DIR="${METRICS_DIR:-/var/lib/node_exporter/textfile}"
METRICS_FILE="${METRICS_DIR}/recapflow_snapshot.prom"
METRICS_SUCCESS_FILE="${METRICS_DIR}/recapflow_snapshot_success.prom"

# Tracks whether retrieval-server is currently paused — cleanup() must unpause.
PAUSED=0
# Set to 1 when main() completes successfully — cleanup() uses this to decide
# whether to remove the partial staging dir.
SUCCESS=0
# Set by main() once the timestamp is known.
STAGING_DIR=""
# Epoch seconds at the start of main(); used by cleanup() to compute duration.
START_TIME=0

log() {
  echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*"
}

# Atomic write to METRICS_DIR. Best-effort: silently skip if the dir is missing
# or unwritable so that monitoring infra absence never breaks the snapshot.
write_metrics_file() {
  local exit_code="$1"
  local duration="$2"
  local now
  now=$(date +%s)
  if [ ! -d "${METRICS_DIR}" ] || [ ! -w "${METRICS_DIR}" ]; then
    return 0
  fi
  local tmp="${METRICS_FILE}.tmp.$$"
  {
    echo "# HELP recapflow_snapshot_last_run_timestamp_seconds Unix timestamp of the last attempted snapshot run."
    echo "# TYPE recapflow_snapshot_last_run_timestamp_seconds gauge"
    echo "recapflow_snapshot_last_run_timestamp_seconds ${now}"
    echo "# HELP recapflow_snapshot_last_exit_code Exit code of the last snapshot run (0 = success)."
    echo "# TYPE recapflow_snapshot_last_exit_code gauge"
    echo "recapflow_snapshot_last_exit_code ${exit_code}"
    echo "# HELP recapflow_snapshot_last_duration_seconds Duration in seconds of the last snapshot run."
    echo "# TYPE recapflow_snapshot_last_duration_seconds gauge"
    echo "recapflow_snapshot_last_duration_seconds ${duration}"
  } > "${tmp}" 2>/dev/null && mv -f "${tmp}" "${METRICS_FILE}" 2>/dev/null || rm -f "${tmp}" 2>/dev/null || true
}

write_success_metric_file() {
  local now
  now=$(date +%s)
  if [ ! -d "${METRICS_DIR}" ] || [ ! -w "${METRICS_DIR}" ]; then
    return 0
  fi
  local tmp="${METRICS_SUCCESS_FILE}.tmp.$$"
  {
    echo "# HELP recapflow_snapshot_last_success_timestamp_seconds Unix timestamp of the last successful snapshot."
    echo "# TYPE recapflow_snapshot_last_success_timestamp_seconds gauge"
    echo "recapflow_snapshot_last_success_timestamp_seconds ${now}"
  } > "${tmp}" 2>/dev/null && mv -f "${tmp}" "${METRICS_SUCCESS_FILE}" 2>/dev/null || rm -f "${tmp}" 2>/dev/null || true
}

cleanup() {
  local exit_code=$?
  if [ "${PAUSED}" -eq 1 ]; then
    log "cleanup: unpausing retrieval-server"
    docker compose --project-directory "${REPO_ROOT}" unpause retrieval-server >/dev/null 2>&1 || true
    PAUSED=0
  fi
  if [ "${SUCCESS}" -eq 0 ] && [ -n "${STAGING_DIR}" ] && [ -d "${STAGING_DIR}" ]; then
    log "FAILED (exit ${exit_code}); removing partial snapshot: ${STAGING_DIR}"
    # Best-effort cleanup: a permission/IO error here must not abort the trap
    # before write_metrics_file runs, otherwise the failure is invisible.
    rm -rf "${STAGING_DIR}" || log "WARN: failed to remove ${STAGING_DIR}; continuing"
  fi
  local duration=0
  if [ "${START_TIME}" -gt 0 ]; then
    duration=$(( $(date +%s) - START_TIME ))
  fi
  write_metrics_file "${exit_code}" "${duration}"
}
trap cleanup EXIT

prune_old_snapshots() {
  # Keep the most recent RETENTION snapshots. Runs at the start of every run so
  # space is freed even if previous attempts failed mid-snapshot.
  if [ ! -d "${STAGING_ROOT}" ]; then
    return 0
  fi
  cd "${STAGING_ROOT}"
  local snapshots
  snapshots=$(ls -1d 20*-*-*T*-*-*Z 2>/dev/null || true)
  if [ -z "${snapshots}" ]; then
    log "prune: no snapshots yet; nothing to remove"
    return 0
  fi
  local count
  count=$(echo "${snapshots}" | wc -l)
  if [ "${count}" -le "${RETENTION}" ]; then
    log "prune: ${count} snapshot(s) present, retention=${RETENTION}; nothing to remove"
    return 0
  fi
  log "prune: ${count} snapshots present, retention=${RETENTION}; removing oldest"
  echo "${snapshots}" | sort -r | tail -n "+$((RETENTION + 1))" | while read -r old; do
    log "  pruning ${old}"
    rm -rf "${old}"
  done
}

main() {
  preflight_require_not_root

  START_TIME=$(date +%s)

  mkdir -p "${STAGING_ROOT}"

  prune_old_snapshots

  preflight_require_free_space "${STAGING_ROOT}" "${MIN_FREE_GB}"

  local timestamp
  timestamp=$(date -u +%Y-%m-%dT%H-%M-%SZ)
  STAGING_DIR="${STAGING_ROOT}/${timestamp}"

  log "starting snapshot: ${STAGING_DIR}"

  mkdir -p "${STAGING_DIR}/postgres"
  mkdir -p "${STAGING_DIR}/lancedb"
  mkdir -p "${STAGING_DIR}/openwebui"
  mkdir -p "${STAGING_DIR}/secrets"
  mkdir -p "${STAGING_DIR}/code-snapshot"

  log "dumping postgres"
  docker exec n8n_db pg_dump -U n8n -F c --no-acl --no-owner -f /tmp/n8n.pgdump n8n
  docker cp n8n_db:/tmp/n8n.pgdump "${STAGING_DIR}/postgres/n8n.pgdump"
  docker exec n8n_db rm /tmp/n8n.pgdump

  log "snapshotting lancedb"
  docker compose --project-directory "${REPO_ROOT}" pause retrieval-server
  PAUSED=1
  # LanceDB files are owned by root (container process UID). docker exec into
  # a paused container is refused. docker cp from a paused container works and
  # uses the daemon's kernel-level copy path — ~5x faster than alpine volume
  # tar because it avoids per-file Docker API round-trips. Produces a POSIX
  # tar archive at staging/lancedb/lancedb.tar. Restore: tar -xf lancedb.tar.
  # NOTE: with 5GB of version history this step takes ~20 min. Run
  # `lance compact` on the table before the first production cron to bring
  # _versions/ down to <100MB and get this under 2 minutes.
  docker cp "community_brain_retrieval:/data/lancedb" - > "${STAGING_DIR}/lancedb/lancedb.tar"
  docker compose --project-directory "${REPO_ROOT}" unpause retrieval-server
  PAUSED=0

  log "snapshotting open-webui volume"
  docker run --rm -v open-webui-data:/data -v "${STAGING_DIR}/openwebui:/out" alpine \
    tar -cf /out/open-webui-data.tar -C /data .

  log "tarring n8n state"
  tar -cf "${STAGING_DIR}/n8n-state.tar.zst" \
    --use-compress-program=zstd \
    -C "${REPO_ROOT}" \
    data n8n-state output watch historical 2>/dev/null || {
      log "WARN: some directories missing; continuing"
    }

  log "copying secrets"
  if [ -f "${REPO_ROOT}/.env" ]; then
    install -m 600 "${REPO_ROOT}/.env" "${STAGING_DIR}/secrets/.env"
  fi
  if [ -f "${REPO_ROOT}/community-brain/config/.env" ]; then
    install -m 600 "${REPO_ROOT}/community-brain/config/.env" "${STAGING_DIR}/secrets/community-brain.env"
  fi

  log "copying code snapshot"
  cp "${REPO_ROOT}/docker-compose.yml" "${STAGING_DIR}/code-snapshot/docker-compose.yml"
  cp -r "${REPO_ROOT}/workflows" "${STAGING_DIR}/code-snapshot/workflows"
  cp -r "${REPO_ROOT}/prompts" "${STAGING_DIR}/code-snapshot/prompts"

  log "writing manifest"
  local n8n_version
  n8n_version=$(docker exec n8n n8n --version 2>/dev/null | tail -1 || echo "unknown")
  local rs_version
  rs_version=$(docker exec community_brain_retrieval python -c "from community_brain import __version__; print(__version__)" 2>/dev/null || echo "unknown")
  cd "${STAGING_DIR}"
  manifest_write "${timestamp}" "${n8n_version}" "${rs_version}"

  log "verifying manifest"
  manifest_verify "${STAGING_DIR}"

  log "updating latest symlink"
  ln -sfn "${timestamp}" "${STAGING_ROOT}/latest"

  log "snapshot complete: ${STAGING_DIR}"
  write_success_metric_file
  SUCCESS=1
}

main "$@"
