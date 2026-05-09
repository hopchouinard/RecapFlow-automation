#!/usr/bin/env bash
# install-launchd.sh — install or update the RecapFlow launchd agents on this Mac.
#
# macOS TCC (Full Disk Access) restriction: launchd UserAgent processes cannot
# read files on external or secondary APFS volumes (like /Volumes/NVMe_2TB_Work)
# even when the interactive shell can. Scripts must live on the boot volume
# (under ~/Library/Scripts/) to be reachable by launchd. This installer copies
# the canonical scripts and lib files there, installs the plists, and loads the
# agents. Run again after any script change to sync.
#
# Usage:
#   ./scripts/install-launchd.sh          # install or update
#   ./scripts/install-launchd.sh --unload # unload and remove

set -euo pipefail

REPO_SCRIPTS="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_LAUNCHD="${REPO_SCRIPTS}/launchd"
INSTALL_DIR="${HOME}/Library/Scripts/recapflow"
LAUNCH_AGENTS="${HOME}/Library/LaunchAgents"

JOBS=(
  "com.patchoutech.recapflow-pull"
  "com.patchoutech.recapflow-freshness"
)

log() { echo "[install-launchd] $*"; }

unload_jobs() {
  for job in "${JOBS[@]}"; do
    if launchctl list | grep -q "${job}"; then
      log "unloading ${job}"
      launchctl bootout "gui/${UID}/${job}" 2>/dev/null || true
    fi
  done
}

if [[ "${1:-}" == "--unload" ]]; then
  unload_jobs
  for job in "${JOBS[@]}"; do
    rm -f "${LAUNCH_AGENTS}/${job}.plist"
    log "removed ${LAUNCH_AGENTS}/${job}.plist"
  done
  log "done. Scripts left in place at ${INSTALL_DIR}/"
  exit 0
fi

# --- install / update ---

log "creating install dir: ${INSTALL_DIR}"
mkdir -p "${INSTALL_DIR}/lib"

log "copying scripts to ${INSTALL_DIR}/"
cp "${REPO_SCRIPTS}/recapflow-pull.sh"          "${INSTALL_DIR}/recapflow-pull.sh"
cp "${REPO_SCRIPTS}/recapflow-freshness-check.sh" "${INSTALL_DIR}/recapflow-freshness-check.sh"
chmod +x "${INSTALL_DIR}/recapflow-pull.sh" "${INSTALL_DIR}/recapflow-freshness-check.sh"

log "copying lib/ to ${INSTALL_DIR}/lib/"
cp "${REPO_SCRIPTS}/lib/manifest.sh"   "${INSTALL_DIR}/lib/manifest.sh"
cp "${REPO_SCRIPTS}/lib/preflight.sh"  "${INSTALL_DIR}/lib/preflight.sh"

log "unloading any existing agents"
unload_jobs

log "installing plists to ${LAUNCH_AGENTS}/"
for job in "${JOBS[@]}"; do
  cp "${REPO_LAUNCHD}/${job}.plist" "${LAUNCH_AGENTS}/${job}.plist"
done

log "bootstrapping agents"
for job in "${JOBS[@]}"; do
  launchctl bootstrap "gui/${UID}" "${LAUNCH_AGENTS}/${job}.plist"
  log "  loaded: ${job}"
done

echo ""
log "installed agents:"
launchctl list | grep recapflow || true
echo ""
log "done. Run again after any script change to sync."
