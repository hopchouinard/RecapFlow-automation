#!/usr/bin/env bash
# RecapFlow preflight check helpers.
# Source this from snapshot, pull, and bootstrap scripts.

set -euo pipefail

preflight_require_not_root() {
  if [ "$(id -u)" -eq 0 ]; then
    echo "ERROR: refusing to run as root. Run as your normal user with docker group access." >&2
    return 1
  fi
}

preflight_require_file_exists() {
  local path="$1"
  if [ ! -f "${path}" ]; then
    echo "ERROR: file not found: ${path}" >&2
    return 1
  fi
}

preflight_check_dir_empty() {
  # Returns 0 if directory is empty OR does not exist.
  # Returns nonzero if directory exists and contains files.
  local dir="$1"
  if [ ! -d "${dir}" ]; then
    return 0
  fi
  if [ -n "$(ls -A "${dir}" 2>/dev/null)" ]; then
    echo "ERROR: ${dir} is not empty. Refusing to clobber existing state. Use --force to override." >&2
    return 1
  fi
  return 0
}

preflight_check_volume_mounted() {
  # Verifies a directory exists (proxy for "mounted").
  # On macOS, an unmounted volume path simply doesn't exist under /Volumes/.
  local mountpoint="$1"
  if [ ! -d "${mountpoint}" ]; then
    echo "ERROR: ${mountpoint} not mounted (path does not exist)" >&2
    return 1
  fi
  return 0
}

preflight_detect_os() {
  # Returns: ubuntu, debian, macos, or unknown
  case "$(uname)" in
    Darwin)
      echo "macos"
      return 0
      ;;
    Linux)
      if [ -f /etc/os-release ]; then
        # shellcheck disable=SC1091
        . /etc/os-release
        case "${ID:-unknown}" in
          ubuntu) echo "ubuntu"; return 0 ;;
          debian) echo "debian"; return 0 ;;
          *) echo "unknown"; return 0 ;;
        esac
      fi
      echo "unknown"
      return 0
      ;;
    *)
      echo "unknown"
      return 0
      ;;
  esac
}
