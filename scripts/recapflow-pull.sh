#!/usr/bin/env bash
# RecapFlow workstation-side pull script.
# Pulls the VM's latest snapshot via rsync into the external HDD staging dir.
#
# Env overrides:
#   VM_HOST      (default: n8n-automation)
#   VM_USER      (default: $USER)
#   VM_STAGING   (default: /home/pchouinard/recapflow-backup/staging)
#   HDD_STAGING  (default: /Volumes/HDD_4TB_Archive/RecapFlow-backups/staging)
#
# NOTE: VM_STAGING default matches the snapshot-vm.sh STAGING_ROOT default
# (~/recapflow-backup/staging on the VM operator's home dir). Override
# both consistently if you change the VM-side location.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/manifest.sh
source "${SCRIPT_DIR}/lib/manifest.sh"
# shellcheck source=lib/preflight.sh
source "${SCRIPT_DIR}/lib/preflight.sh"

VM_HOST="${VM_HOST:-n8n-automation}"
VM_USER="${VM_USER:-${USER}}"
VM_STAGING="${VM_STAGING:-/home/pchouinard/recapflow-backup/staging}"
HDD_STAGING="${HDD_STAGING:-/Volumes/HDD_4TB_Archive/RecapFlow-backups/staging}"

log() {
  echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*"
}

main() {
  log "starting workstation pull"

  log "checking external HDD is mounted"
  preflight_check_volume_mounted "/Volumes/HDD_4TB_Archive"

  mkdir -p "${HDD_STAGING}"

  log "pulling from ${VM_USER}@${VM_HOST}:${VM_STAGING}/"
  rsync -avz --delete \
    "${VM_USER}@${VM_HOST}:${VM_STAGING}/" \
    "${HDD_STAGING}/"

  log "checking latest snapshot"
  if [ ! -L "${HDD_STAGING}/latest" ]; then
    echo "ERROR: ${HDD_STAGING}/latest is not a symlink (rsync did not preserve it?)" >&2
    exit 1
  fi

  log "verifying manifest of latest snapshot"
  local latest_target
  latest_target=$(readlink "${HDD_STAGING}/latest")
  manifest_verify "${HDD_STAGING}/${latest_target}"

  log "pull complete; latest = ${latest_target}"
}

main "$@"
