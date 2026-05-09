#!/usr/bin/env bash
# RecapFlow workstation-side pull script.
# Pulls the VM's latest snapshot via rsync into local staging on the boot volume.
#
# Staging on the boot volume (~/) avoids macOS TCC restrictions: launchd UserAgents
# cannot write to secondary APFS volumes (/Volumes/...) even with Full Disk Access
# granted to /bin/bash and /usr/bin/rsync. Terminal-spawned runs inherit Terminal.app's
# TCC context and work fine; launchd-spawned runs do not.
#
# Env overrides:
#   VM_HOST       (default: n8n-automation)
#   VM_USER       (default: $USER)
#   VM_STAGING    (default: /home/$VM_USER/recapflow-backup/staging)
#   LOCAL_STAGING (default: ${HOME}/RecapFlow-backups/staging)
#
# NOTE: Arq's backup scope must include this directory; default is ${HOME}/RecapFlow-backups/.
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
VM_STAGING="${VM_STAGING:-/home/${VM_USER}/recapflow-backup/staging}"
LOCAL_STAGING="${LOCAL_STAGING:-${HOME}/RecapFlow-backups/staging}"

log() {
  echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*"
}

main() {
  log "starting workstation pull"

  mkdir -p "${LOCAL_STAGING}"

  log "pulling from ${VM_USER}@${VM_HOST}:${VM_STAGING}/"
  rsync -avz --delete \
    "${VM_USER}@${VM_HOST}:${VM_STAGING}/" \
    "${LOCAL_STAGING}/"

  log "checking latest snapshot"
  if [ ! -L "${LOCAL_STAGING}/latest" ]; then
    echo "ERROR: ${LOCAL_STAGING}/latest is not a symlink (rsync did not preserve it?)" >&2
    exit 1
  fi

  log "verifying manifest of latest snapshot"
  local latest_target
  latest_target=$(readlink "${LOCAL_STAGING}/latest")
  manifest_verify "${LOCAL_STAGING}/${latest_target}"

  log "pull complete; latest = ${latest_target}"
}

main "$@"
