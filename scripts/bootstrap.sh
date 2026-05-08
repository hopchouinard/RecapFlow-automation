#!/usr/bin/env bash
# RecapFlow operator-tier bootstrap script.
# Restores a fresh VM from a snapshot tarball produced by snapshot-vm.sh
# (or workstation pull) and brings the stack up.
#
# Usage:
#   ./scripts/bootstrap.sh <restore-tarball-path>
#   ./scripts/bootstrap.sh --force <restore-tarball-path>
#
# The tarball is the contents of a single timestamped staging dir, packed
# from the workstation:
#   tar -cf restore.tar -C /Volumes/HDD_4TB_Archive/RecapFlow-backups/staging/latest/ .
#   scp restore.tar new-vm:/tmp/

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# shellcheck source=lib/manifest.sh
source "${SCRIPT_DIR}/lib/manifest.sh"
# shellcheck source=lib/preflight.sh
source "${SCRIPT_DIR}/lib/preflight.sh"
# shellcheck source=lib/smoke-tests.sh
source "${SCRIPT_DIR}/lib/smoke-tests.sh"

FORCE=0
TARBALL=""

usage() {
  cat <<EOF
Usage: $0 [--force] <restore-tarball-path>

Restores a fresh VM from a snapshot tarball.

Options:
  --force    Clobber existing state in data/, lancedb/, etc. Default: refuse.

Example:
  $0 /tmp/recapflow-restore.tar
  $0 --force /tmp/recapflow-restore.tar

Tarball is the contents of a snapshot's "latest" dir, e.g.:
  tar -cf restore.tar -C /Volumes/HDD_4TB_Archive/RecapFlow-backups/staging/latest/ .
  scp restore.tar new-vm:/tmp/
EOF
}

parse_args() {
  while [ $# -gt 0 ]; do
    case "$1" in
      --force) FORCE=1; shift ;;
      -h|--help) usage; exit 0 ;;
      -*) echo "Unknown flag: $1" >&2; usage; exit 1 ;;
      *) TARBALL="$1"; shift ;;
    esac
  done
  if [ -z "${TARBALL}" ]; then
    echo "ERROR: tarball path required" >&2
    usage
    exit 1
  fi
}

log() {
  echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*"
}

phase() {
  echo ""
  echo "=== $* ==="
}

# Phase 1: preflight
phase1_preflight() {
  phase "Phase 1: preflight"

  preflight_require_not_root
  preflight_require_file_exists "${TARBALL}"

  local os
  os=$(preflight_detect_os)
  if [ "${os}" != "ubuntu" ] && [ "${os}" != "debian" ]; then
    echo "ERROR: bootstrap currently supports Ubuntu/Debian only (detected: ${os})" >&2
    exit 1
  fi
  log "OS: ${os}"

  if [ ! -f "${REPO_ROOT}/docker-compose.yml" ]; then
    echo "ERROR: not in repo root (${REPO_ROOT}/docker-compose.yml not found)" >&2
    exit 1
  fi

  if [ "${FORCE}" -eq 0 ]; then
    preflight_check_dir_empty "${REPO_ROOT}/data"
    preflight_check_dir_empty "${REPO_ROOT}/community-brain/lancedb"
  else
    log "WARN: --force passed; will clobber existing state"
  fi

  # Port checks
  for port in 5678 8999 3000 5432; do
    if ss -tlnp 2>/dev/null | grep -q ":${port} "; then
      echo "ERROR: port ${port} already in use" >&2
      exit 1
    fi
  done
}

# Phase 2: install host prereqs
phase2_install_prereqs() {
  phase "Phase 2: install host prerequisites"

  if ! command -v docker >/dev/null 2>&1; then
    log "installing Docker Engine via official apt repo"
    sudo apt-get update
    sudo apt-get install -y ca-certificates curl gnupg
    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "${VERSION_CODENAME}") stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    sudo usermod -aG docker "${USER}"
    log "NOTE: log out and back in for docker group membership to take effect"
    log "      then re-run this bootstrap script"
    exit 2
  fi

  if ! docker compose version >/dev/null 2>&1; then
    echo "ERROR: docker compose v2 not available; install docker-compose-plugin" >&2
    exit 1
  fi

  for pkg in rsync zstd tar; do
    if ! command -v "${pkg}" >/dev/null 2>&1; then
      log "installing ${pkg}"
      sudo apt-get install -y "${pkg}"
    fi
  done
}

# Phase 3: stage and verify tarball
phase3_stage_and_verify() {
  phase "Phase 3: stage and verify tarball"

  local staging="${REPO_ROOT}/restore-staging"
  if [ -d "${staging}" ]; then
    log "removing existing restore-staging/"
    rm -rf "${staging}"
  fi
  mkdir -p "${staging}"

  log "extracting ${TARBALL} to ${staging}/"
  tar -xf "${TARBALL}" -C "${staging}/"

  log "verifying manifest"
  manifest_verify "${staging}"

  local timestamp
  timestamp=$(grep "^snapshot_timestamp:" "${staging}/MANIFEST.txt" | awk '{print $2}')
  log "snapshot timestamp: ${timestamp}"
}

# Phase 4: restore state
phase4_restore_state() {
  phase "Phase 4: restore state into repo paths"

  local staging="${REPO_ROOT}/restore-staging"

  log "unpacking n8n state tarball"
  tar --use-compress-program=zstd -xf "${staging}/n8n-state.tar.zst" -C "${REPO_ROOT}"

  log "extracting lancedb tar"
  mkdir -p "${REPO_ROOT}/community-brain/lancedb"
  tar -xf "${staging}/lancedb/lancedb.tar" -C "${REPO_ROOT}/community-brain/lancedb"

  log "installing secrets"
  if [ -f "${staging}/secrets/.env" ]; then
    install -m 600 "${staging}/secrets/.env" "${REPO_ROOT}/.env"
  else
    echo "ERROR: missing ${staging}/secrets/.env" >&2
    exit 1
  fi
  if [ -f "${staging}/secrets/community-brain.env" ]; then
    install -m 600 "${staging}/secrets/community-brain.env" "${REPO_ROOT}/community-brain/config/.env"
  else
    echo "ERROR: missing ${staging}/secrets/community-brain.env" >&2
    exit 1
  fi

  if ! diff -q "${staging}/code-snapshot/docker-compose.yml" "${REPO_ROOT}/docker-compose.yml" >/dev/null 2>&1; then
    log "WARN: backup compose differs from git compose; using git version"
  fi
}

# Phase 5: database restore
phase5_database_restore() {
  phase "Phase 5: database restore"

  local staging="${REPO_ROOT}/restore-staging"

  log "starting db service"
  cd "${REPO_ROOT}"
  docker compose up -d db

  log "waiting for postgres"
  local i=0
  until docker exec n8n_db pg_isready -U n8n -q 2>/dev/null; do
    i=$((i + 1))
    if [ "${i}" -gt 60 ]; then
      echo "ERROR: postgres did not become ready within 60s" >&2
      exit 1
    fi
    sleep 1
  done

  log "restoring n8n.pgdump"
  docker cp "${staging}/postgres/n8n.pgdump" n8n_db:/tmp/n8n.pgdump
  docker exec n8n_db pg_restore -U n8n -d n8n --clean --if-exists /tmp/n8n.pgdump
  docker exec n8n_db rm /tmp/n8n.pgdump
}

# Phase 5b: open-webui volume restore
phase5b_openwebui_restore() {
  phase "Phase 5b: open-webui volume restore"

  local staging="${REPO_ROOT}/restore-staging"

  if [ -f "${staging}/openwebui/open-webui-data.tar" ]; then
    log "creating open-webui-data volume and restoring contents"
    docker volume create open-webui-data >/dev/null
    docker run --rm -v open-webui-data:/data -v "${staging}/openwebui:/import" alpine \
      tar -xf /import/open-webui-data.tar -C /data
  else
    log "WARN: no open-webui volume in snapshot; service will start fresh"
  fi
}

# Phase 6: bring up full stack
phase6_bring_up_stack() {
  phase "Phase 6: bring up full stack"

  cd "${REPO_ROOT}"
  docker compose up -d

  log "waiting for containers"
  local i=0
  while true; do
    local running
    running=$(docker compose ps --status running -q | wc -l)
    if [ "${running}" -ge 4 ]; then
      break
    fi
    i=$((i + 1))
    if [ "${i}" -gt 120 ]; then
      echo "ERROR: not all containers running after 120s" >&2
      docker compose ps
      exit 1
    fi
    sleep 1
  done

  log "all containers running"
  docker compose ps
}

# Phase 7: smoke tests
phase7_smoke_tests() {
  phase "Phase 7: smoke tests"

  local failures=0

  smoke_http_200 "http://localhost:5678/healthz" "n8n" || failures=$((failures + 1))
  smoke_http_200 "http://localhost:8999/health" "retrieval-server" || failures=$((failures + 1))
  smoke_http_200 "http://localhost:3000" "open-webui" || failures=$((failures + 1))
  smoke_n8n_workflows_listed || failures=$((failures + 1))
  smoke_retrieval_query || failures=$((failures + 1))

  if [ "${failures}" -gt 0 ]; then
    echo ""
    echo "FAIL: ${failures} smoke test(s) failed" >&2
    echo "  Stack is up but degraded. Investigate before declaring DR complete." >&2
    exit 1
  fi

  echo ""
  echo "All smoke tests passed."
}

# Phase 8: final operator instructions
phase8_final_instructions() {
  phase "Phase 8: post-install checklist"

  cat <<EOF

Bootstrap complete. Next steps:

1. Update workstation-side sync target if VM hostname/IP changed:
   - Edit ~/scripts/sync-zoom-chats.sh on the workstation
   - Edit ~/Library/LaunchAgents/com.patchoutech.recapflow-pull.plist
     (VM_HOST env override if hostname changed)

2. Test sync from workstation to VM:
   ssh ${USER}@$(hostname) 'echo ok'

3. Schedule first snapshot from this VM:
   crontab -l   # confirm the snapshot cron entry was restored
   To run an ad-hoc snapshot now (recommended): ./scripts/snapshot-vm.sh

4. Verify Arq picks up the staged backup at next workstation pull.

5. Browse to http://$(hostname):5678 and confirm your workflows.
   Workflows should retain credentials because the encryption key was
   restored as part of data/. If credentials show as broken, check that
   data/config (the encryption key file) is correctly in place.
EOF
}

main() {
  parse_args "$@"

  phase1_preflight
  phase2_install_prereqs
  phase3_stage_and_verify
  phase4_restore_state
  phase5_database_restore
  phase5b_openwebui_restore
  phase6_bring_up_stack
  phase7_smoke_tests
  phase8_final_instructions
}

main "$@"
