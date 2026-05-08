#!/usr/bin/env bash
# RecapFlow freshness check.
# Asserts the latest snapshot on the HDD is younger than MAX_AGE_HOURS.
# Surfaces failure as a macOS notification (osascript) if too old.
#
# Env overrides:
#   HDD_STAGING      (default: /Volumes/HDD_4TB_Archive/RecapFlow-backups/staging)
#   MAX_AGE_HOURS    (default: 25)

set -euo pipefail

HDD_STAGING="${HDD_STAGING:-/Volumes/HDD_4TB_Archive/RecapFlow-backups/staging}"
MAX_AGE_HOURS="${MAX_AGE_HOURS:-25}"

notify_failure() {
  local msg="$1"
  if command -v osascript >/dev/null 2>&1; then
    osascript -e "display notification \"${msg}\" with title \"RecapFlow Backup Stale\" sound name \"Basso\""
  fi
  echo "FAIL: ${msg}" >&2
}

main() {
  if [ ! -d "/Volumes/HDD_4TB_Archive" ]; then
    notify_failure "External HDD not mounted"
    exit 1
  fi

  if [ ! -L "${HDD_STAGING}/latest" ]; then
    notify_failure "No latest snapshot symlink at ${HDD_STAGING}"
    exit 1
  fi

  local latest_target
  latest_target=$(readlink "${HDD_STAGING}/latest")
  local latest_path="${HDD_STAGING}/${latest_target}"

  if [ ! -d "${latest_path}" ]; then
    notify_failure "Latest snapshot dir does not exist: ${latest_path}"
    exit 1
  fi

  # Snapshot age = now - directory mtime, in seconds
  local now
  now=$(date +%s)
  local mtime
  mtime=$(stat -f %m "${latest_path}")
  local age_seconds=$((now - mtime))
  local age_hours=$((age_seconds / 3600))

  if [ "${age_hours}" -gt "${MAX_AGE_HOURS}" ]; then
    notify_failure "Latest snapshot is ${age_hours}h old (threshold: ${MAX_AGE_HOURS}h). Pipeline may be broken."
    exit 1
  fi

  echo "OK: latest snapshot is ${age_hours}h old (${latest_target})"
}

main "$@"
