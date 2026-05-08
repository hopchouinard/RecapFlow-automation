#!/usr/bin/env bash
# Seed ~/.zoom-chat-synced from the VM's output/ directory.
# Use after workstation DR to prevent re-syncing already-processed dates.
#
# Env overrides:
#   VM_HOST    (default: n8n-automation)
#   VM_USER    (default: $USER)
#   OUTPUT_DIR (default: /home/pchouinard/n8n/output)
#   STATE_FILE (default: ~/.zoom-chat-synced)

set -euo pipefail

VM_HOST="${VM_HOST:-n8n-automation}"
VM_USER="${VM_USER:-${USER}}"
OUTPUT_DIR="${OUTPUT_DIR:-/home/pchouinard/n8n/output}"
STATE_FILE="${STATE_FILE:-${HOME}/.zoom-chat-synced}"

main() {
  echo "Querying ${VM_USER}@${VM_HOST}:${OUTPUT_DIR} for processed dates..."

  local dates
  dates=$(ssh -n "${VM_USER}@${VM_HOST}" "ls -1 ${OUTPUT_DIR}" 2>/dev/null | grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' | sort)

  if [ -z "${dates}" ]; then
    echo "No processed dates found. Aborting." >&2
    exit 1
  fi

  local count
  count=$(echo "${dates}" | wc -l | tr -d ' ')

  echo "Found ${count} processed dates."
  echo "Will seed ${STATE_FILE} with these. The sync script will then SKIP these dates"
  echo "during its first post-DR run (preventing duplicate processing)."
  echo ""
  echo "First few dates:"
  echo "${dates}" | head -5
  echo "..."
  echo ""
  read -r -p "Proceed? [y/N] " ans
  case "${ans}" in
    y|Y) ;;
    *) echo "Aborted."; exit 0 ;;
  esac

  if [ -f "${STATE_FILE}" ]; then
    cp "${STATE_FILE}" "${STATE_FILE}.bak.$(date +%Y%m%d-%H%M%S)"
    echo "Backed up existing ${STATE_FILE}"
  fi

  echo "${dates}" > "${STATE_FILE}"
  echo "Seeded ${count} dates into ${STATE_FILE}"
}

main "$@"
