#!/usr/bin/env bash
# RecapFlow snapshot manifest helpers.
# Source this file from scripts that produce or verify snapshots.

set -euo pipefail

# Compute the SHA-256 hex digest of a file.
# Works on Linux (sha256sum) and macOS (shasum).
manifest_compute_sha256() {
  local file="$1"
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "${file}" | awk '{print $1}'
  elif command -v shasum >/dev/null 2>&1; then
    shasum -a 256 "${file}" | awk '{print $1}'
  else
    echo "ERROR: neither sha256sum nor shasum available" >&2
    return 1
  fi
}

# Write a MANIFEST.txt in the current directory listing every regular file
# under the current directory with its SHA-256 and size.
# Args: snapshot_timestamp n8n_version retrieval_server_version
manifest_write() {
  local snapshot_timestamp="$1"
  local n8n_version="$2"
  local retrieval_server_version="$3"

  {
    echo "# RecapFlow snapshot manifest"
    echo "# version: 1"
    echo "snapshot_timestamp: ${snapshot_timestamp}"
    echo "n8n_version: ${n8n_version}"
    echo "retrieval_server_version: ${retrieval_server_version}"
    echo "files:"
    # Find every regular file except MANIFEST.txt itself
    find . -type f ! -name "MANIFEST.txt" | sort | while read -r f; do
      local rel="${f#./}"
      local size
      size=$(stat -c %s "${f}" 2>/dev/null || stat -f %z "${f}")
      local hash
      hash=$(manifest_compute_sha256 "${f}")
      echo "  ${rel}  sha256:${hash}  size:${size}"
    done
  } > MANIFEST.txt
}

# Verify a snapshot directory against its MANIFEST.txt.
# Args: staging_dir
# Returns 0 on success, nonzero on any mismatch or missing file.
manifest_verify() {
  local staging_dir="$1"
  if [ ! -f "${staging_dir}/MANIFEST.txt" ]; then
    echo "ERROR: ${staging_dir}/MANIFEST.txt not found" >&2
    return 1
  fi

  local errors=0
  while IFS= read -r line; do
    # Parse "  <path>  sha256:<hex>  size:<n>"
    if [[ "${line}" =~ ^[[:space:]]+([^[:space:]]+)[[:space:]]+sha256:([0-9a-f]+)[[:space:]]+size:([0-9]+) ]]; then
      local rel="${BASH_REMATCH[1]}"
      local expected_hash="${BASH_REMATCH[2]}"
      local file="${staging_dir}/${rel}"
      if [ ! -f "${file}" ]; then
        echo "ERROR: missing ${rel}" >&2
        errors=$((errors + 1))
        continue
      fi
      local actual_hash
      actual_hash=$(manifest_compute_sha256 "${file}")
      if [ "${actual_hash}" != "${expected_hash}" ]; then
        echo "ERROR: checksum mismatch for ${rel}" >&2
        echo "  expected: ${expected_hash}" >&2
        echo "  actual:   ${actual_hash}" >&2
        errors=$((errors + 1))
      fi
    fi
  done < "${staging_dir}/MANIFEST.txt"

  if [ "${errors}" -gt 0 ]; then
    echo "ERROR: ${errors} manifest verification error(s)" >&2
    return 1
  fi
  echo "OK: manifest verified (${staging_dir}/MANIFEST.txt)"
  return 0
}
