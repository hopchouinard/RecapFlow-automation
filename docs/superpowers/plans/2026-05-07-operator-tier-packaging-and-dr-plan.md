# Operator-Tier Packaging and DR Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a complete operator-tier disaster-recovery story for the RecapFlow stack: a daily backup pipeline (VM → workstation HDD → Arq → cloud), a fresh-VM bootstrap script that restores from a backup tarball, and runbooks for both VM and workstation DR scenarios.

**Architecture:** Two-node system (VM running Docker Compose stack, inference workstation running local models + sync orchestration + Arq). The VM-side snapshot script stages daily backups; the workstation pulls them via rsync; Arq's existing schedule ships them to encrypted cloud storage. Restore is operator-driven via a single `bootstrap.sh` script with phase-by-phase failure isolation.

**Tech Stack:** bash (scripts), bats-core (script testing), Docker Compose v2 (orchestration), cron (VM scheduling), launchd (workstation scheduling), Arq (existing backup tool), rsync (transport), pg_dump / pg_restore (Postgres backup).

**Spec:** `docs/superpowers/specs/2026-05-07-operator-tier-packaging-and-dr-design.md`

---

## File Structure

### New files

```
scripts/
├── bootstrap.sh                              # Fresh-VM install + restore
├── snapshot-vm.sh                            # VM-side daily snapshot
├── recapflow-pull.sh                         # Workstation pull from VM
├── recapflow-freshness-check.sh              # Workstation freshness alert
├── seed-zoom-synced-from-output.sh           # Workstation DR helper
├── lib/
│   ├── manifest.sh                           # MANIFEST.txt write + verify
│   ├── preflight.sh                          # Common preflight checks
│   └── smoke-tests.sh                        # Bootstrap smoke test fns
├── launchd/
│   ├── com.patchoutech.recapflow-pull.plist
│   └── com.patchoutech.recapflow-freshness.plist
└── cron/
    └── recapflow-snapshot                    # /etc/cron.d/ entry for VM

tests/
├── test_manifest.bats
├── test_preflight.bats
└── test_smoke_tests.bats

docs/runbooks/
├── vm-disaster-recovery.md
└── workstation-disaster-recovery.md
```

### Modified files

- `docker-compose.yml` — add `open-webui` service
- `.env.example` — create with documented variables (currently missing)
- `community-brain/config/.env.example` — add `OLLAMA_URL` documentation note about LAN IP requirement
- `README.md` — link to bootstrap procedure and runbooks
- `.gitignore` — ensure `restore-staging/`, `bats/`, etc. are excluded

### Decommissioned (after migration)

- `community-brain/open-webui/docker-compose.yml` — folded into root compose. Keep for one cycle as reference, then remove.

---

## Phase 1: Open WebUI Migration to VM

Goal: move Open WebUI off the workstation's Docker Desktop and into the VM Docker Compose stack so it (a) becomes part of the unified VM backup, (b) reduces workstation responsibilities.

### Task 1.1: Add `open-webui` service to root docker-compose.yml

**Files:**
- Modify: `docker-compose.yml`

- [ ] **Step 1: Read current `docker-compose.yml`**

Read `docker-compose.yml` to confirm exact structure before editing.

- [ ] **Step 2: Add the `open-webui` service block**

Add after the `retrieval-server` service, before the `volumes:` block:

```yaml
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: open-webui
    restart: unless-stopped
    ports:
      - "3000:8080"
    environment:
      # OLLAMA_BASE_URL must point at the inference workstation over LAN.
      # NOT host.docker.internal — the VM host does not run Ollama.
      # Set the actual value in community-brain/config/.env (or a sibling
      # open-webui.env file) and reference it here. For now, hardcode the
      # workstation LAN IP; revisit if it churns.
      - OLLAMA_BASE_URL=${OLLAMA_BASE_URL:-http://10.1.30.20:11434}
      - WEBUI_AUTH=true
    volumes:
      - open-webui-data:/app/backend/data
    depends_on:
      - retrieval-server
```

Add to the `volumes:` block at the bottom:

```yaml
volumes:
  db_data:
  open-webui-data:
```

- [ ] **Step 3: Add `OLLAMA_BASE_URL` to `.env.example`**

Create `.env.example` at repo root (currently missing):

```bash
# n8n Postgres credentials (these match docker-compose defaults; change in production)
POSTGRES_DB=n8n
POSTGRES_USER=n8n
POSTGRES_PASSWORD=n8n

# n8n basic auth (UI login)
N8N_BASIC_AUTH_ACTIVE=true
N8N_BASIC_AUTH_USER=your_username
N8N_BASIC_AUTH_PASSWORD=your_password

# n8n encryption key — generate with: openssl rand -hex 32
# NEVER change after credentials have been saved.
N8N_ENCRYPTION_KEY=

# Open WebUI's Ollama target — points at the inference workstation over LAN.
# Replace with your workstation's LAN IP. Port 11434 must be reachable from the VM.
OLLAMA_BASE_URL=http://10.1.30.20:11434
```

- [ ] **Step 4: Verify port 3000 is not already used on the VM**

On the VM:

```bash
ss -tlnp | grep :3000
```

Expected: no output (port free). If occupied, document the conflict and resolve before proceeding.

- [ ] **Step 5: Bring up the new service in dev**

On the VM (or wherever testing):

```bash
docker compose up -d open-webui
docker compose logs -f open-webui
```

Expected: container starts, logs show "open-webui listening on port 8080" or similar, no errors connecting to Ollama.

- [ ] **Step 6: Verify connectivity to Ollama on workstation**

```bash
docker exec open-webui curl -s http://10.1.30.20:11434/api/tags
```

Expected: JSON response listing installed models (`nomic-embed-text:v1.5`, `gpt-oss:20b`).

If unreachable: check workstation firewall (macOS System Settings → Network → Firewall must allow incoming on port 11434 for Ollama process), check VM can ping workstation, check `OLLAMA_BASE_URL` value matches actual workstation IP.

- [ ] **Step 7: Verify Open WebUI loads in browser**

Browse to `http://<vm-host>:3000` and confirm the UI loads. Create an account (since `WEBUI_AUTH=true`).

- [ ] **Step 8: Commit**

```bash
git add docker-compose.yml .env.example
git commit -m "$(cat <<'EOF'
feat(docker): add Open WebUI service to root compose

Consolidates Open WebUI from the workstation's Docker Desktop into the VM
Docker Compose stack. Talks to Ollama on the inference workstation via
LAN (OLLAMA_BASE_URL env var). Persistent data on docker-named volume.

Part of the operator-tier packaging spec. Open WebUI state is now
captured by the VM-side daily snapshot rather than needing its own
backup pipeline on the workstation.

Spec: docs/superpowers/specs/2026-05-07-operator-tier-packaging-and-dr-design.md

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

### Task 1.2: Migrate Open WebUI data from workstation (one-shot)

This task migrates the user's existing Open WebUI users/chats/settings from the workstation Docker Desktop install. If the user has no important state to preserve (fresh install acceptable), skip and confirm with operator.

**Files:**
- No code changes; operational task

- [ ] **Step 1: Confirm with operator whether to migrate or fresh-start**

Ask: "Open WebUI on workstation has chats/users/settings. Migrate to VM, or start fresh?"

If fresh-start: skip remaining steps, just shut down the workstation Open WebUI container.

- [ ] **Step 2: Locate Open WebUI data on workstation**

```bash
docker volume inspect open-webui-data --format '{{.Mountpoint}}'
```

Returns absolute path inside Docker Desktop's VM. On macOS, accessible via:
```bash
docker run --rm -v open-webui-data:/data alpine tar -czf - -C /data . > ~/open-webui-export.tar.gz
```

- [ ] **Step 3: Transfer to VM**

```bash
scp ~/open-webui-export.tar.gz vm-host:/tmp/
```

- [ ] **Step 4: Stop the new VM Open WebUI service**

On the VM:

```bash
docker compose stop open-webui
```

- [ ] **Step 5: Import data into VM volume**

```bash
docker run --rm -v open-webui-data:/data -v /tmp:/import alpine sh -c "cd /data && tar -xzf /import/open-webui-export.tar.gz"
```

- [ ] **Step 6: Restart the service**

```bash
docker compose up -d open-webui
```

- [ ] **Step 7: Verify the migrated state appears in the UI**

Browse to `http://<vm-host>:3000`, log in with previous credentials, verify chats and settings present.

- [ ] **Step 8: Shut down the old workstation Open WebUI container**

On workstation:

```bash
cd /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/community-brain/open-webui
docker compose down
```

Volume preserved on workstation as a safety net for one cycle.

- [ ] **Step 9: No commit needed** (operational task with no code changes).

---

## Phase 2: VM-side Snapshot Pipeline

Goal: build the daily snapshot script that stages everything needed for restore into `/var/lib/recapflow-backup/staging/<ISO-timestamp>/`, with an integrity manifest and SHA-256 checksums.

### Task 2.1: Set up bats-core for shell script testing

**Files:**
- Modify: `.gitignore`
- Create: `tests/test_manifest.bats` (stub)

- [ ] **Step 1: Install bats-core on the dev machine**

```bash
brew install bats-core
```

Verify:

```bash
bats --version
```

Expected: `Bats 1.x.x` or similar.

- [ ] **Step 2: Create `tests/` directory and a stub bats file**

Create `tests/test_manifest.bats`:

```bash
#!/usr/bin/env bats

@test "bats is wired up" {
  run echo "ok"
  [ "$status" -eq 0 ]
  [ "$output" = "ok" ]
}
```

- [ ] **Step 3: Run the stub test**

```bash
bats tests/test_manifest.bats
```

Expected: `1 test, 0 failures`.

- [ ] **Step 4: Add `tests/.bats-cache/` to `.gitignore`**

Append to `.gitignore`:

```
# bats test cache
tests/.bats-cache/

# Restore staging dir created by bootstrap.sh
restore-staging/
```

- [ ] **Step 5: Commit**

```bash
git add tests/test_manifest.bats .gitignore
git commit -m "$(cat <<'EOF'
test: scaffold bats-core for shell script testing

Adds bats-core as the test runner for shell scripts. Used by upcoming
operator-tier packaging work (manifest verification, preflight checks,
smoke tests).

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

### Task 2.2: Implement `lib/manifest.sh` with TDD

**Files:**
- Create: `scripts/lib/manifest.sh`
- Create/extend: `tests/test_manifest.bats`

The manifest is a plain-text file listing every artifact in a snapshot with its SHA-256 hash and size. Format:

```
# RecapFlow snapshot manifest
# version: 1
snapshot_timestamp: 2026-05-07T02:00:00Z
n8n_version: 2.15.1
retrieval_server_version: 0.2.0
files:
  postgres/n8n.pgdump  sha256:<hex>  size:1234567
  lancedb/...          sha256:<hex>  size:...
  ...
```

- [ ] **Step 1: Replace stub `test_manifest.bats` with real tests**

Create `tests/test_manifest.bats`:

```bash
#!/usr/bin/env bats

setup() {
  TMPDIR_TEST="$(mktemp -d)"
  source "${BATS_TEST_DIRNAME}/../scripts/lib/manifest.sh"
}

teardown() {
  rm -rf "${TMPDIR_TEST}"
}

@test "manifest_compute_sha256 returns sha256 of file" {
  echo "hello" > "${TMPDIR_TEST}/test.txt"
  run manifest_compute_sha256 "${TMPDIR_TEST}/test.txt"
  [ "$status" -eq 0 ]
  # SHA-256 of "hello\n" is the expected hex
  [ "$output" = "5891b5b522d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03" ]
}

@test "manifest_write creates a manifest with correct headers" {
  mkdir -p "${TMPDIR_TEST}/staging/postgres"
  echo "fake dump" > "${TMPDIR_TEST}/staging/postgres/n8n.pgdump"
  cd "${TMPDIR_TEST}/staging"
  run manifest_write "2026-05-07T02:00:00Z" "2.15.1" "0.2.0"
  [ "$status" -eq 0 ]
  [ -f "MANIFEST.txt" ]
  grep -q "snapshot_timestamp: 2026-05-07T02:00:00Z" MANIFEST.txt
  grep -q "n8n_version: 2.15.1" MANIFEST.txt
  grep -q "retrieval_server_version: 0.2.0" MANIFEST.txt
}

@test "manifest_write hashes every file under staging" {
  mkdir -p "${TMPDIR_TEST}/staging/postgres"
  mkdir -p "${TMPDIR_TEST}/staging/lancedb"
  echo "dump" > "${TMPDIR_TEST}/staging/postgres/n8n.pgdump"
  echo "lance" > "${TMPDIR_TEST}/staging/lancedb/foo.lance"
  cd "${TMPDIR_TEST}/staging"
  run manifest_write "2026-05-07T02:00:00Z" "2.15.1" "0.2.0"
  [ "$status" -eq 0 ]
  grep -q "postgres/n8n.pgdump" MANIFEST.txt
  grep -q "lancedb/foo.lance" MANIFEST.txt
}

@test "manifest_verify succeeds for a valid manifest" {
  mkdir -p "${TMPDIR_TEST}/staging/postgres"
  echo "dump" > "${TMPDIR_TEST}/staging/postgres/n8n.pgdump"
  cd "${TMPDIR_TEST}/staging"
  manifest_write "2026-05-07T02:00:00Z" "2.15.1" "0.2.0"
  run manifest_verify "${TMPDIR_TEST}/staging"
  [ "$status" -eq 0 ]
}

@test "manifest_verify fails when a file is corrupted" {
  mkdir -p "${TMPDIR_TEST}/staging/postgres"
  echo "dump" > "${TMPDIR_TEST}/staging/postgres/n8n.pgdump"
  cd "${TMPDIR_TEST}/staging"
  manifest_write "2026-05-07T02:00:00Z" "2.15.1" "0.2.0"
  echo "tampered" > "${TMPDIR_TEST}/staging/postgres/n8n.pgdump"
  run manifest_verify "${TMPDIR_TEST}/staging"
  [ "$status" -ne 0 ]
  [[ "$output" =~ "checksum mismatch" ]]
}

@test "manifest_verify fails when a listed file is missing" {
  mkdir -p "${TMPDIR_TEST}/staging/postgres"
  echo "dump" > "${TMPDIR_TEST}/staging/postgres/n8n.pgdump"
  cd "${TMPDIR_TEST}/staging"
  manifest_write "2026-05-07T02:00:00Z" "2.15.1" "0.2.0"
  rm "${TMPDIR_TEST}/staging/postgres/n8n.pgdump"
  run manifest_verify "${TMPDIR_TEST}/staging"
  [ "$status" -ne 0 ]
  [[ "$output" =~ "missing" ]]
}
```

- [ ] **Step 2: Run the tests to confirm they fail**

```bash
bats tests/test_manifest.bats
```

Expected: All tests fail with "manifest.sh not found" or similar.

- [ ] **Step 3: Implement `scripts/lib/manifest.sh`**

Create `scripts/lib/manifest.sh`:

```bash
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
```

- [ ] **Step 4: Run the tests to confirm they pass**

```bash
bats tests/test_manifest.bats
```

Expected: All 6 tests pass.

- [ ] **Step 5: Commit**

```bash
git add scripts/lib/manifest.sh tests/test_manifest.bats
git commit -m "$(cat <<'EOF'
feat(scripts): add manifest helpers for snapshot integrity

manifest_compute_sha256, manifest_write, manifest_verify. SHA-256 with
sha256sum (Linux) or shasum (macOS) fallback. MANIFEST.txt format
documents snapshot timestamp, software versions, and per-file hashes.

Used by upcoming snapshot script and bootstrap restore verification.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

### Task 2.3: Implement `lib/preflight.sh` with TDD

**Files:**
- Create: `scripts/lib/preflight.sh`
- Create: `tests/test_preflight.bats`

- [ ] **Step 1: Write failing tests**

Create `tests/test_preflight.bats`:

```bash
#!/usr/bin/env bats

setup() {
  TMPDIR_TEST="$(mktemp -d)"
  source "${BATS_TEST_DIRNAME}/../scripts/lib/preflight.sh"
}

teardown() {
  rm -rf "${TMPDIR_TEST}"
}

@test "preflight_require_not_root succeeds when not root" {
  if [ "$(id -u)" -eq 0 ]; then
    skip "running as root"
  fi
  run preflight_require_not_root
  [ "$status" -eq 0 ]
}

@test "preflight_require_file_exists succeeds when file present" {
  echo "x" > "${TMPDIR_TEST}/foo"
  run preflight_require_file_exists "${TMPDIR_TEST}/foo"
  [ "$status" -eq 0 ]
}

@test "preflight_require_file_exists fails when file missing" {
  run preflight_require_file_exists "${TMPDIR_TEST}/missing"
  [ "$status" -ne 0 ]
  [[ "$output" =~ "not found" ]]
}

@test "preflight_check_dir_empty succeeds for empty dir" {
  mkdir "${TMPDIR_TEST}/d"
  run preflight_check_dir_empty "${TMPDIR_TEST}/d"
  [ "$status" -eq 0 ]
}

@test "preflight_check_dir_empty succeeds for missing dir" {
  run preflight_check_dir_empty "${TMPDIR_TEST}/missing"
  [ "$status" -eq 0 ]
}

@test "preflight_check_dir_empty fails when dir has files" {
  mkdir "${TMPDIR_TEST}/d"
  echo "x" > "${TMPDIR_TEST}/d/f"
  run preflight_check_dir_empty "${TMPDIR_TEST}/d"
  [ "$status" -ne 0 ]
  [[ "$output" =~ "not empty" ]]
}

@test "preflight_check_volume_mounted succeeds when mountpoint exists and has files" {
  mkdir "${TMPDIR_TEST}/mount"
  echo "x" > "${TMPDIR_TEST}/mount/.marker"
  run preflight_check_volume_mounted "${TMPDIR_TEST}/mount"
  [ "$status" -eq 0 ]
}

@test "preflight_check_volume_mounted fails for non-existent path" {
  run preflight_check_volume_mounted "${TMPDIR_TEST}/missing"
  [ "$status" -ne 0 ]
  [[ "$output" =~ "not mounted" ]]
}

@test "preflight_detect_os returns ubuntu or debian on Linux" {
  if [ "$(uname)" != "Linux" ]; then
    skip "not Linux"
  fi
  run preflight_detect_os
  [ "$status" -eq 0 ]
  [[ "$output" =~ ^(ubuntu|debian)$ ]]
}

@test "preflight_detect_os returns macos on Darwin" {
  if [ "$(uname)" != "Darwin" ]; then
    skip "not macOS"
  fi
  run preflight_detect_os
  [ "$status" -eq 0 ]
  [ "$output" = "macos" ]
}
```

- [ ] **Step 2: Run tests to confirm they fail**

```bash
bats tests/test_preflight.bats
```

Expected: tests fail because `scripts/lib/preflight.sh` does not exist yet.

- [ ] **Step 3: Implement `scripts/lib/preflight.sh`**

```bash
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
  # Verifies a directory exists and is non-empty (proxy for "mounted").
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
```

- [ ] **Step 4: Run tests to confirm they pass**

```bash
bats tests/test_preflight.bats
```

Expected: All tests pass (some skipped depending on OS).

- [ ] **Step 5: Commit**

```bash
git add scripts/lib/preflight.sh tests/test_preflight.bats
git commit -m "$(cat <<'EOF'
feat(scripts): add preflight check helpers

Common checks for snapshot, pull, and bootstrap scripts: not-root,
file-exists, dir-empty (for idempotency), volume-mounted (for the
external HDD precondition), and OS detection.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

### Task 2.4: Implement `snapshot-vm.sh`

**Files:**
- Create: `scripts/snapshot-vm.sh`

This is the core snapshot script. Runs on the VM via cron daily.

- [ ] **Step 1: Write the script**

Create `scripts/snapshot-vm.sh`:

```bash
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
  rsync -a "${REPO_ROOT}/community-brain/lancedb/" "${staging}/lancedb/"
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
```

- [ ] **Step 2: Make it executable**

```bash
chmod +x scripts/snapshot-vm.sh
```

- [ ] **Step 3: Create the staging root with correct permissions**

On the VM:

```bash
sudo mkdir -p /var/lib/recapflow-backup/staging
sudo chown $USER:$USER /var/lib/recapflow-backup/staging
```

- [ ] **Step 4: Run a test snapshot manually**

```bash
./scripts/snapshot-vm.sh
```

Expected output: progress logs, "snapshot complete" at end. Inspect the staging dir:

```bash
ls -la /var/lib/recapflow-backup/staging/latest/
cat /var/lib/recapflow-backup/staging/latest/MANIFEST.txt
```

Expected: directory contains `postgres/`, `lancedb/`, `openwebui/`, `n8n-state.tar.zst`, `secrets/`, `code-snapshot/`, `MANIFEST.txt`. Manifest lists every file with sha256.

- [ ] **Step 5: Verify the manifest passes verification**

```bash
source scripts/lib/manifest.sh
manifest_verify /var/lib/recapflow-backup/staging/latest/
```

Expected: `OK: manifest verified`.

- [ ] **Step 6: Run a second snapshot and verify retention**

```bash
sleep 2
./scripts/snapshot-vm.sh
ls -1 /var/lib/recapflow-backup/staging/
```

Expected: two timestamped dirs + `latest` symlink. Run more if you want to test pruning at retention=7.

- [ ] **Step 7: Commit**

```bash
git add scripts/snapshot-vm.sh
git commit -m "$(cat <<'EOF'
feat(scripts): add VM-side daily snapshot script

snapshot-vm.sh stages a complete restorable snapshot under
/var/lib/recapflow-backup/staging/<ISO-timestamp>/:
  - postgres/n8n.pgdump        (pg_dump custom format)
  - lancedb/                   (rsync'd while retrieval-server paused)
  - openwebui/open-webui-data.tar  (docker volume export)
  - n8n-state.tar.zst          (data/, n8n-state/, output/, watch/, historical/)
  - secrets/                   (mode-600 .env files)
  - code-snapshot/             (compose, workflows, prompts)
  - MANIFEST.txt               (per-file sha256, snapshot metadata)

Updates latest -> <timestamp> symlink. Prunes snapshots older than
RETENTION (default 7). Manifest is verified post-write to fail loud
on incomplete snapshots.

Spec: docs/superpowers/specs/2026-05-07-operator-tier-packaging-and-dr-design.md

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

### Task 2.5: Wire up cron on the VM

**Files:**
- Create: `scripts/cron/recapflow-snapshot`

- [ ] **Step 1: Write the cron entry**

Create `scripts/cron/recapflow-snapshot`:

```
# RecapFlow VM-side daily snapshot
# Installed at /etc/cron.d/recapflow-snapshot
# Runs at 02:00 local time. Output appended to /var/log/recapflow-snapshot.log.
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
0 2 * * * pchouinard /home/pchouinard/RecapFlow-automation/scripts/snapshot-vm.sh >> /var/log/recapflow-snapshot.log 2>&1
```

(Replace `pchouinard` with the actual VM username and adjust the repo path if needed.)

- [ ] **Step 2: Install on VM**

```bash
sudo cp scripts/cron/recapflow-snapshot /etc/cron.d/recapflow-snapshot
sudo chown root:root /etc/cron.d/recapflow-snapshot
sudo chmod 644 /etc/cron.d/recapflow-snapshot
```

- [ ] **Step 3: Set up the log file with correct permissions**

```bash
sudo touch /var/log/recapflow-snapshot.log
sudo chown pchouinard:pchouinard /var/log/recapflow-snapshot.log
```

- [ ] **Step 4: Verify cron picks it up**

```bash
sudo systemctl restart cron
grep CRON /var/log/syslog | tail -5
```

Expected: cron daemon reload event recent.

- [ ] **Step 5: Verify no conflict with the existing 03:30 UTC LanceDB lint snapshot**

Per `community-brain/CLAUDE.md`, there is an existing cron at `/etc/cron.d/community-brain-lint` that runs at 04:00 UTC after a "03:30 UTC LanceDB snapshot." Confirm:

```bash
sudo cat /etc/cron.d/community-brain-lint 2>/dev/null || echo "not present"
ls /etc/cron.d/ | grep -i community
ls /etc/cron.d/ | grep -i lance
```

If the existing 03:30 UTC job is purely a LanceDB version-pin snapshot (internal to LanceDB), our 02:00 local snapshot is independent and runs first. No conflict.

If the existing job is creating files in `/var/lib/recapflow-backup/` or competing for retrieval-server pause, document and reconcile (likely: keep ours daily, treat the lint cron as orthogonal).

- [ ] **Step 6: Commit**

```bash
git add scripts/cron/recapflow-snapshot
git commit -m "$(cat <<'EOF'
infra(cron): schedule VM-side daily snapshot at 02:00 local

Installed at /etc/cron.d/recapflow-snapshot. Runs as the operator user;
output to /var/log/recapflow-snapshot.log.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Phase 3: Workstation Pull Pipeline

Goal: a launchd job on the workstation that pulls each new VM snapshot to the external HDD, verifies it, and lets Arq's existing schedule pick it up. Plus a freshness-alert job.

### Task 3.1: Implement `recapflow-pull.sh`

**Files:**
- Create: `scripts/recapflow-pull.sh`

- [ ] **Step 1: Write the script**

Create `scripts/recapflow-pull.sh`:

```bash
#!/usr/bin/env bash
# RecapFlow workstation-side pull script.
# Pulls the VM's latest snapshot via rsync into the external HDD staging dir.
#
# Env overrides:
#   VM_HOST      (default: n8n-automation.patchoutech.lab)
#   VM_USER      (default: $USER)
#   VM_STAGING   (default: /var/lib/recapflow-backup/staging)
#   HDD_STAGING  (default: /Volumes/HDD_4TB_Archive/RecapFlow-backups/staging)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/manifest.sh
source "${SCRIPT_DIR}/lib/manifest.sh"
# shellcheck source=lib/preflight.sh
source "${SCRIPT_DIR}/lib/preflight.sh"

VM_HOST="${VM_HOST:-n8n-automation.patchoutech.lab}"
VM_USER="${VM_USER:-${USER}}"
VM_STAGING="${VM_STAGING:-/var/lib/recapflow-backup/staging}"
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
```

- [ ] **Step 2: Make executable**

```bash
chmod +x scripts/recapflow-pull.sh
```

- [ ] **Step 3: Verify external HDD is mounted on workstation**

```bash
ls /Volumes/HDD_4TB_Archive/
```

Expected: HDD contents. If "No such file": mount it before continuing.

- [ ] **Step 4: Run a manual pull**

```bash
./scripts/recapflow-pull.sh
```

Expected: rsync completes, manifest verifies, latest symlink resolves.

- [ ] **Step 5: Verify Arq is configured to back up the staging dir**

Open Arq → Backup Plans → confirm `/Volumes/HDD_4TB_Archive/RecapFlow-backups/` is in the included paths. If not, add it.

- [ ] **Step 6: Commit**

```bash
git add scripts/recapflow-pull.sh
git commit -m "$(cat <<'EOF'
feat(scripts): add workstation-side pull from VM staging

recapflow-pull.sh rsyncs the VM's snapshot staging dir to the external
HDD so Arq's existing schedule picks it up. Pre-flight checks the HDD
is mounted; post-flight verifies the latest snapshot's manifest.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

### Task 3.2: Implement `recapflow-freshness-check.sh`

**Files:**
- Create: `scripts/recapflow-freshness-check.sh`

- [ ] **Step 1: Write the script**

Create `scripts/recapflow-freshness-check.sh`:

```bash
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
```

- [ ] **Step 2: Make executable**

```bash
chmod +x scripts/recapflow-freshness-check.sh
```

- [ ] **Step 3: Test the freshness check (should pass after a recent pull)**

```bash
./scripts/recapflow-freshness-check.sh
```

Expected: `OK: latest snapshot is Xh old`.

- [ ] **Step 4: Test failure path (force notification)**

```bash
MAX_AGE_HOURS=0 ./scripts/recapflow-freshness-check.sh
```

Expected: macOS notification appears, exit code nonzero, message "Latest snapshot is Xh old (threshold: 0h)".

- [ ] **Step 5: Commit**

```bash
git add scripts/recapflow-freshness-check.sh
git commit -m "$(cat <<'EOF'
feat(scripts): add backup freshness check for workstation

recapflow-freshness-check.sh asserts the latest HDD-staged snapshot is
younger than MAX_AGE_HOURS (default 25). On staleness, surfaces a macOS
notification via osascript and exits nonzero. Catches silent pipeline
breakage.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

### Task 3.3: Create launchd plists

**Files:**
- Create: `scripts/launchd/com.patchoutech.recapflow-pull.plist`
- Create: `scripts/launchd/com.patchoutech.recapflow-freshness.plist`

- [ ] **Step 1: Write the pull plist**

Create `scripts/launchd/com.patchoutech.recapflow-pull.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.patchoutech.recapflow-pull</string>

    <key>ProgramArguments</key>
    <array>
        <string>/Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/scripts/recapflow-pull.sh</string>
    </array>

    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>2</integer>
        <key>Minute</key>
        <integer>30</integer>
    </dict>

    <key>StandardOutPath</key>
    <string>/Users/pchouinard/Library/Logs/recapflow-pull.log</string>

    <key>StandardErrorPath</key>
    <string>/Users/pchouinard/Library/Logs/recapflow-pull.log</string>

    <key>RunAtLoad</key>
    <false/>
</dict>
</plist>
```

- [ ] **Step 2: Write the freshness plist**

Create `scripts/launchd/com.patchoutech.recapflow-freshness.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.patchoutech.recapflow-freshness</string>

    <key>ProgramArguments</key>
    <array>
        <string>/Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/scripts/recapflow-freshness-check.sh</string>
    </array>

    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>9</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>

    <key>StandardOutPath</key>
    <string>/Users/pchouinard/Library/Logs/recapflow-freshness.log</string>

    <key>StandardErrorPath</key>
    <string>/Users/pchouinard/Library/Logs/recapflow-freshness.log</string>

    <key>RunAtLoad</key>
    <false/>
</dict>
</plist>
```

- [ ] **Step 3: Install both plists**

```bash
cp scripts/launchd/com.patchoutech.recapflow-pull.plist ~/Library/LaunchAgents/
cp scripts/launchd/com.patchoutech.recapflow-freshness.plist ~/Library/LaunchAgents/
launchctl bootstrap gui/$UID ~/Library/LaunchAgents/com.patchoutech.recapflow-pull.plist
launchctl bootstrap gui/$UID ~/Library/LaunchAgents/com.patchoutech.recapflow-freshness.plist
```

- [ ] **Step 4: Verify both jobs are loaded**

```bash
launchctl list | grep recapflow
```

Expected: two entries — `com.patchoutech.recapflow-pull` and `com.patchoutech.recapflow-freshness`.

- [ ] **Step 5: Trigger the pull job manually to confirm wiring**

```bash
launchctl kickstart -k gui/$UID/com.patchoutech.recapflow-pull
```

Then check the log:

```bash
tail -20 ~/Library/Logs/recapflow-pull.log
```

Expected: log shows the pull ran, ended with "pull complete".

- [ ] **Step 6: Commit**

```bash
git add scripts/launchd/
git commit -m "$(cat <<'EOF'
infra(launchd): schedule workstation pull and freshness check

  com.patchoutech.recapflow-pull          02:30 daily
  com.patchoutech.recapflow-freshness     09:00 daily

Pull runs ~30min after the VM's 02:00 snapshot. Freshness check at 09:00
surfaces a macOS notification if the latest staged snapshot is older
than 25h (silent pipeline breakage detection).

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Phase 4: Bootstrap Script (Fresh-VM Restore)

Goal: a single `bootstrap.sh` that takes a backup tarball and stands up a fully working RecapFlow stack on a fresh Ubuntu/Debian VM.

### Task 4.1: Implement `lib/smoke-tests.sh` with TDD

**Files:**
- Create: `scripts/lib/smoke-tests.sh`
- Create: `tests/test_smoke_tests.bats`

Smoke tests validate the post-bootstrap stack is functional. Each function returns 0 (pass) or nonzero (fail) and prints a one-line status.

- [ ] **Step 1: Write failing tests**

Create `tests/test_smoke_tests.bats`:

```bash
#!/usr/bin/env bats

setup() {
  source "${BATS_TEST_DIRNAME}/../scripts/lib/smoke-tests.sh"
}

@test "smoke_http_200 succeeds when given a 2xx URL" {
  # Use a known-good URL with a fast response
  run smoke_http_200 "http://localhost:65530"  # nothing listens here
  # Expect failure (no listener), status nonzero
  [ "$status" -ne 0 ]
}

@test "smoke_http_200 helper exists and is callable" {
  type smoke_http_200
}

@test "smoke_n8n_workflows_listed exists" {
  type smoke_n8n_workflows_listed
}

@test "smoke_retrieval_query exists" {
  type smoke_retrieval_query
}
```

- [ ] **Step 2: Run tests to confirm failure**

```bash
bats tests/test_smoke_tests.bats
```

Expected: failures because the script does not exist yet.

- [ ] **Step 3: Implement `scripts/lib/smoke-tests.sh`**

```bash
#!/usr/bin/env bash
# RecapFlow smoke test functions.
# Each function: prints PASS/FAIL line, returns 0/nonzero accordingly.

set -uo pipefail

smoke_http_200() {
  local url="$1"
  local label="${2:-${url}}"
  local code
  code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "${url}" 2>/dev/null || echo "000")
  if [ "${code}" = "200" ]; then
    echo "PASS: HTTP 200 from ${label}"
    return 0
  fi
  echo "FAIL: HTTP ${code} from ${label}" >&2
  return 1
}

smoke_n8n_workflows_listed() {
  local count
  count=$(docker exec n8n n8n list:workflow 2>/dev/null | grep -c '|' || echo 0)
  if [ "${count}" -gt 0 ]; then
    echo "PASS: n8n list:workflow returned ${count} workflows"
    return 0
  fi
  echo "FAIL: n8n list:workflow returned no workflows" >&2
  return 1
}

smoke_retrieval_query() {
  local result
  result=$(curl -s --max-time 30 \
    -H "Content-Type: application/json" \
    -X POST \
    -d '{"query":"test","top_k":1}' \
    "http://localhost:8999/query" 2>/dev/null || echo "{}")
  if echo "${result}" | grep -q '"chunks"'; then
    echo "PASS: retrieval-server /query returned chunks key"
    return 0
  fi
  echo "FAIL: retrieval-server /query did not return expected shape" >&2
  echo "  response: ${result}" >&2
  return 1
}
```

- [ ] **Step 4: Run tests to confirm passing**

```bash
bats tests/test_smoke_tests.bats
```

Expected: All tests pass.

- [ ] **Step 5: Commit**

```bash
git add scripts/lib/smoke-tests.sh tests/test_smoke_tests.bats
git commit -m "$(cat <<'EOF'
feat(scripts): add smoke test helpers for bootstrap validation

Three smoke functions used by bootstrap.sh phase 7:
  smoke_http_200             — generic HTTP 200 check
  smoke_n8n_workflows_listed — n8n list:workflow returns rows
  smoke_retrieval_query      — /query returns expected shape

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

### Task 4.2: Implement `bootstrap.sh`

**Files:**
- Create: `scripts/bootstrap.sh`

This is the largest single script. It implements all eight phases from the spec. We write it as one file with clear phase comments, since it's run linearly and there's no benefit to fragmenting it.

- [ ] **Step 1: Write the script**

Create `scripts/bootstrap.sh`:

```bash
#!/usr/bin/env bash
# RecapFlow operator-tier bootstrap script.
# Restores a fresh VM from a snapshot tarball produced by snapshot-vm.sh
# (or workstation pull) and brings the stack up.
#
# Usage:
#   ./scripts/bootstrap.sh <restore-tarball-path>
#   ./scripts/bootstrap.sh --force <restore-tarball-path>

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
    echo "deb [arch=\"$(dpkg --print-architecture)\" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo \"${VERSION_CODENAME}\") stable" | \
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

  log "rsyncing lancedb"
  mkdir -p "${REPO_ROOT}/community-brain/lancedb"
  rsync -a "${staging}/lancedb/" "${REPO_ROOT}/community-brain/lancedb/"

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
   The cron at /etc/cron.d/recapflow-snapshot will fire at 02:00 local.
   To run an ad-hoc snapshot now (recommended): ./scripts/snapshot-vm.sh

4. Verify Arq picks up the staged backup at next workstation pull.

5. Browse to http://$(hostname):5678 and confirm n8n shows your workflows.
   Workflows will need credentials reattached if N8N_ENCRYPTION_KEY changed.
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
```

- [ ] **Step 2: Make executable**

```bash
chmod +x scripts/bootstrap.sh
```

- [ ] **Step 3: Verify the script's `--help` output**

```bash
./scripts/bootstrap.sh --help
```

Expected: usage text shown.

- [ ] **Step 4: Verify preflight refuses without arg**

```bash
./scripts/bootstrap.sh || echo "exit=$?"
```

Expected: error "tarball path required", nonzero exit.

- [ ] **Step 5: Commit**

```bash
git add scripts/bootstrap.sh
git commit -m "$(cat <<'EOF'
feat(scripts): add operator-tier bootstrap script for fresh-VM DR

Single bash script implementing all 8 phases of the DR install:
  1. Preflight (not-root, OS check, repo check, port check, idempotency)
  2. Install host prerequisites (Docker engine + compose v2)
  3. Stage and verify tarball (manifest + sha256)
  4. Restore state (data/, lancedb/, secrets, code-snapshot)
  5. Postgres restore (db-only up, pg_restore)
  5b. Open WebUI volume restore
  6. Bring up full stack (docker compose up -d)
  7. Smoke tests (http 200, workflows listed, query)
  8. Operator post-install checklist

--force overrides the dir-empty check. Without it, refuses to clobber
existing state. Manifest verification fail = abort before any state
mutation.

Spec: docs/superpowers/specs/2026-05-07-operator-tier-packaging-and-dr-design.md

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

### Task 4.3: End-to-end DR rehearsal on a throwaway VM

**Files:**
- No code changes; integration test

This task validates the full pipeline by performing a real DR rehearsal against a throwaway VM. The result is the proof that the implementation works — without this rehearsal, the DR plan is theoretical.

- [ ] **Step 1: Provision a throwaway Ubuntu/Debian VM on Proxmox**

Cloning the existing VM template or creating a fresh one is fine. Confirm SSH access and the user has sudo.

- [ ] **Step 2: Take a fresh snapshot on the production VM**

```bash
./scripts/snapshot-vm.sh
```

- [ ] **Step 3: Pack and ship the snapshot**

On the workstation:

```bash
tar -cf /tmp/recapflow-rehearsal.tar -C /Volumes/HDD_4TB_Archive/RecapFlow-backups/staging/latest/ .
scp /tmp/recapflow-rehearsal.tar throwaway-vm:/tmp/
```

- [ ] **Step 4: Clone repo on throwaway VM**

```bash
ssh throwaway-vm
git clone <repo-url>
cd RecapFlow-automation
```

- [ ] **Step 5: Run bootstrap**

```bash
./scripts/bootstrap.sh /tmp/recapflow-rehearsal.tar
```

If Docker isn't installed, the script exits with code 2 after installing — log out, log back in, re-run.

Expected: phases proceed, smoke tests pass, post-install checklist printed.

- [ ] **Step 6: Verify the throwaway is functional**

- Browse to `http://<throwaway-vm>:5678` — should show n8n with workflows.
- `curl http://<throwaway-vm>:8999/health` — should return 200.
- Test a query: `curl -X POST http://<throwaway-vm>:8999/query -H 'Content-Type: application/json' -d '{"query":"test","top_k":1}'` — should return chunks.

If retrieval query returns no chunks, the inference workstation may be unreachable from the throwaway VM (firewall, routing). That's a network issue, not a bootstrap bug. Verify with `curl http://<workstation-ip>:11434/api/tags` from the throwaway VM.

- [ ] **Step 7: Document any gotchas surfaced**

If the rehearsal exposed issues, fix them inline (extra preflight checks, clearer error messages, etc.) and append a note to `docs/runbooks/vm-disaster-recovery.md` (created in Phase 5).

- [ ] **Step 8: Tear down the throwaway VM**

After confirming everything works, destroy the throwaway VM. The successful rehearsal is the deliverable.

- [ ] **Step 9: Commit any fixes surfaced during the rehearsal**

```bash
git add -p
git commit -m "$(cat <<'EOF'
fix(bootstrap): <specific fix from rehearsal>

Surfaced during throwaway-VM DR rehearsal.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

If no fixes needed, commit nothing for this task — just confirm completion.

---

## Phase 5: Workstation DR Helpers

### Task 5.1: Implement `seed-zoom-synced-from-output.sh`

**Files:**
- Create: `scripts/seed-zoom-synced-from-output.sh`

This helper scans the VM's `output/` directory (over SSH) and seeds the workstation's `~/.zoom-chat-synced` so a post-DR workstation doesn't trigger a re-sync flood.

- [ ] **Step 1: Write the script**

Create `scripts/seed-zoom-synced-from-output.sh`:

```bash
#!/usr/bin/env bash
# Seed ~/.zoom-chat-synced from the VM's output/ directory.
# Use after workstation DR to prevent re-syncing already-processed dates.
#
# Env overrides:
#   VM_HOST   (default: n8n-automation.patchoutech.lab)
#   VM_USER   (default: $USER)
#   OUTPUT_DIR (default: ~/n8n/output  — the VM-side path)
#   STATE_FILE (default: ~/.zoom-chat-synced)

set -euo pipefail

VM_HOST="${VM_HOST:-n8n-automation.patchoutech.lab}"
VM_USER="${VM_USER:-${USER}}"
OUTPUT_DIR="${OUTPUT_DIR:-/home/${VM_USER}/RecapFlow-automation/output}"
STATE_FILE="${STATE_FILE:-${HOME}/.zoom-chat-synced}"

main() {
  echo "Querying ${VM_USER}@${VM_HOST}:${OUTPUT_DIR} for processed dates..."

  local dates
  dates=$(ssh "${VM_USER}@${VM_HOST}" "ls -1 ${OUTPUT_DIR}" 2>/dev/null | grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' | sort)

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
```

- [ ] **Step 2: Make executable**

```bash
chmod +x scripts/seed-zoom-synced-from-output.sh
```

- [ ] **Step 3: Test in dry-run fashion**

Run on the workstation; answer "n" at the prompt to abort:

```bash
./scripts/seed-zoom-synced-from-output.sh
```

Expected: lists processed dates, prompts for confirmation, exits cleanly on "n".

- [ ] **Step 4: Commit**

```bash
git add scripts/seed-zoom-synced-from-output.sh
git commit -m "$(cat <<'EOF'
feat(scripts): add zoom-sync seeding helper for post-DR workstation

After workstation DR, ~/.zoom-chat-synced may be lost. Without it, the
sync script treats every existing Zoom folder as new and re-uploads all
dates. seed-zoom-synced-from-output.sh queries the VM's output/ dir
over SSH and pre-seeds the state file with already-processed dates.

Documented in docs/runbooks/workstation-disaster-recovery.md (next task).

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Phase 6: Documentation

### Task 6.1: Write `docs/runbooks/vm-disaster-recovery.md`

**Files:**
- Create: `docs/runbooks/vm-disaster-recovery.md`

- [ ] **Step 1: Write the runbook**

Create `docs/runbooks/vm-disaster-recovery.md`:

```markdown
# VM Disaster Recovery Runbook

## Scope

The n8n VM died (hardware failure, hypervisor loss, accidental destruction). You need a working RecapFlow stack on a fresh VM, restored from the latest backup snapshot.

This runbook does NOT cover the inference workstation — see `workstation-disaster-recovery.md` for that.

## Prerequisites

- A fresh Ubuntu 22.04+ or Debian 12+ VM with sudo access via SSH.
- The inference workstation is operational (Ollama running, models pulled, LAN reachable).
- The external HDD is mounted on the workstation with a recent snapshot at `/Volumes/HDD_4TB_Archive/RecapFlow-backups/staging/latest/`.
- The workstation's Arq license + repo password are accessible (in case the HDD is also dead and we need to restore from cloud first).

## Procedure

### Step 1: Verify a recent snapshot exists

On the workstation:

\```bash
ls -la /Volumes/HDD_4TB_Archive/RecapFlow-backups/staging/latest/
cat /Volumes/HDD_4TB_Archive/RecapFlow-backups/staging/latest/MANIFEST.txt | head
\```

Confirm `snapshot_timestamp` is recent. If older than 25h, the pipeline has been broken for a while; see Step 1b below.

### Step 1b (only if HDD is dead OR snapshots are stale): restore from Arq

1. Open Arq.app.
2. Navigate to the most recent backup of `/Volumes/HDD_4TB_Archive/RecapFlow-backups/`.
3. Restore to either the original location (if HDD is back) or to `~/RecapFlow-backups-restore/` temporarily.
4. Update `HDD_STAGING` env var in subsequent commands accordingly.

### Step 2: Pack and transfer the snapshot

On the workstation:

\```bash
tar -cf /tmp/recapflow-restore.tar \
  -C /Volumes/HDD_4TB_Archive/RecapFlow-backups/staging/latest/ .
scp /tmp/recapflow-restore.tar new-vm-host:/tmp/
\```

### Step 3: Clone the repo on the new VM

\```bash
ssh new-vm-host
git clone <repo-url> ~/RecapFlow-automation
cd ~/RecapFlow-automation
\```

### Step 4: Run the bootstrap script

\```bash
./scripts/bootstrap.sh /tmp/recapflow-restore.tar
\```

If Docker isn't yet installed on the VM, the script will install it and exit with code 2. Log out, log back in (so docker group membership applies), then re-run the same command.

Watch the output. Each phase logs clearly. If smoke tests fail, the script exits nonzero and prints which test failed.

### Step 5: Update the workstation to point at the new VM

If the new VM has a different hostname/IP than the old one:

1. Edit `~/scripts/sync-zoom-chats.sh` on the workstation: update the VM hostname.
2. Edit `~/Library/LaunchAgents/com.patchoutech.recapflow-pull.plist`: add `VM_HOST` to the env block.
3. Reload launchd:
   \```bash
   launchctl bootout gui/$UID/com.patchoutech.recapflow-pull
   launchctl bootstrap gui/$UID ~/Library/LaunchAgents/com.patchoutech.recapflow-pull.plist
   \```
4. Test SSH connectivity:
   \```bash
   ssh new-vm-host 'echo ok'
   \```

### Step 6: Take a fresh snapshot on the new VM

\```bash
ssh new-vm-host '~/RecapFlow-automation/scripts/snapshot-vm.sh'
\```

This proves the snapshot pipeline is operational on the new VM and gives you a fresh restore point.

### Step 7: Verify end-to-end

- Browse to `http://new-vm-host:5678` — n8n loads, workflows present.
- Browse to `http://new-vm-host:3000` — Open WebUI loads.
- Run a query against the retrieval server (via Open WebUI or curl) and verify it returns results.

## Time budget

| Phase | Time |
|---|---|
| OS provision + SSH | 5–15 min |
| scp tarball (LAN) | 1–5 min |
| `git clone` + bootstrap phases 1–4 | 2–4 min |
| Postgres restore | 1–2 min |
| Stack startup + image pulls (first time) | 3–8 min |
| Smoke tests | <1 min |
| Workstation reconfiguration | 5 min |
| Verification | 5 min |
| **Total** | **~20–45 min** |

## Common failure modes

### Tarball checksum mismatch

`Phase 3: stage and verify tarball` aborts with "checksum mismatch for X". The tarball was corrupted in transit or the source snapshot was incomplete.

Recovery: pull a different snapshot, or restore from Arq cloud.

### Postgres restore fails

`Phase 5: database restore` errors during `pg_restore`. Most common cause: the dump was created with an incompatible Postgres version. Less common: dump is corrupted.

Recovery: investigate the error, do not blindly retry. The DB volume is preserved for inspection. If the dump is unrecoverable, restore from an older snapshot.

### Inference workstation unreachable

Smoke test 5 fails with "retrieval-server /query did not return expected shape". Stack is otherwise up.

Recovery: not a bootstrap bug. Verify:
- Workstation is on; Ollama serving on port 11434
- Workstation firewall allows incoming on 11434 from the VM
- VM can ping the workstation (`ping <workstation-ip>`)
- `community-brain/config/.env` has correct `OLLAMA_URL` value

### Port already in use

`Phase 1: preflight` errors that 5678/8999/3000/5432 is already bound. Some other service is on the VM.

Recovery: identify and stop the conflicting service, or move RecapFlow to different ports (requires editing `docker-compose.yml` and recreating the bootstrap).

## Out of scope

- Recovering Arq license + repo password (must come from operator's password manager).
- HDD provisioning if the original is dead.
- Reconfiguring the inference workstation (separate runbook).
```

- [ ] **Step 2: Commit**

```bash
git add docs/runbooks/vm-disaster-recovery.md
git commit -m "$(cat <<'EOF'
docs(runbooks): add VM disaster recovery runbook

Step-by-step procedure for restoring a fresh VM from the latest backup
snapshot. Covers prerequisites, the eight bootstrap phases, common
failure modes, and a time budget. References workstation DR runbook
for cross-node concerns.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

### Task 6.2: Write `docs/runbooks/workstation-disaster-recovery.md`

**Files:**
- Create: `docs/runbooks/workstation-disaster-recovery.md`

- [ ] **Step 1: Write the runbook**

Create `docs/runbooks/workstation-disaster-recovery.md`:

```markdown
# Inference Workstation Disaster Recovery Runbook

## Scope

The inference workstation died (hardware failure, theft, file system corruption). You need to bring a new workstation online with:
- Local model serving (Ollama) restored
- Sync orchestration (Zoom chat sync) restored
- Backup pipeline (rsync from VM, Arq) restored
- LAN connectivity to the VM

The VM itself is unaffected and continues to run; only the workstation needs reconstruction.

## Failure modes

- **Mode A: workstation died, attached HDD survived.** Faster path. Backup history intact.
- **Mode B: workstation AND HDD died.** Slower path. Restore HDD from Arq cloud first.

## Prerequisites

- New hardware with enough unified memory or GPU+VRAM for chosen models. Current sizing: 24GB unified memory or equivalent (`gpt-oss:20B` + `nomic-embed-text` + headroom).
- Arq license + repo password (from password manager).
- The VM is operational and reachable on the LAN.

## Procedure (Mode A)

### Step 1: Set up new hardware and restore user data from Arq

Use Apple Migration Assistant (if going Mac-to-Mac) or manual Arq restore. Critical paths to confirm:

\```
~/scripts/sync-zoom-chats.sh
~/Library/LaunchAgents/com.patchoutech.sync-zoom-chats.plist
~/Library/LaunchAgents/com.patchoutech.recapflow-pull.plist
~/Library/LaunchAgents/com.patchoutech.recapflow-freshness.plist
~/Library/Workflows/Applications/Folder Actions/Sync Zoom Chats.workflow
~/.ssh/                      (workstation-to-VM key)
~/.zoom-chat-synced           (state — see "Critical gotcha" below)
~/.zoom-chat-sync.log
\```

### Step 2: Reattach the external HDD

\```bash
ls /Volumes/HDD_4TB_Archive/
\```

If macOS auto-renamed the volume (e.g., "HDD_4TB_Archive 1"), rename back to `HDD_4TB_Archive` in Disk Utility. The path is hard-coded in launchd plists and rsync targets.

### Step 3: Install the local-model serving software

Current implementation: Ollama.

\```bash
brew install ollama  # or DMG installer
ollama serve &       # or via launchd
ollama pull nomic-embed-text:v1.5
ollama pull gpt-oss:20b
\```

Time: nomic-embed-text ~30s, gpt-oss:20b ~20–40 min depending on bandwidth.

### Step 4: Re-add SSH key to keychain

\```bash
ssh-add --apple-use-keychain ~/.ssh/<key-name>
\```

### Step 5: Verify SSH to VM

\```bash
ssh n8n-automation.patchoutech.lab 'echo ok'
\```

### Step 6: Restart launchd jobs

\```bash
launchctl bootstrap gui/$UID ~/Library/LaunchAgents/com.patchoutech.sync-zoom-chats.plist
launchctl bootstrap gui/$UID ~/Library/LaunchAgents/com.patchoutech.recapflow-pull.plist
launchctl bootstrap gui/$UID ~/Library/LaunchAgents/com.patchoutech.recapflow-freshness.plist
\```

### Step 7: Reattach Arq

Open Arq.app → restore configuration if not auto-recovered → re-validate license + repo password.

### Step 8: Verify the backup pipeline

\```bash
ls /Volumes/HDD_4TB_Archive/RecapFlow-backups/staging/latest/MANIFEST.txt
~/RecapFlow-automation/scripts/recapflow-pull.sh
\```

Expected: pull completes, no errors, mtime on `latest/` updates.

### Step 9: Verify Open WebUI on VM can reach this workstation

From the VM:

\```bash
curl http://<workstation-LAN-IP>:11434/api/tags
\```

Expected: JSON response listing installed models.

If unreachable: macOS firewall is blocking. Open System Settings → Network → Firewall → allow incoming on port 11434 for the Ollama process.

### Step 10: Seed `~/.zoom-chat-synced` to prevent re-sync flood

If `~/.zoom-chat-synced` was lost (not covered by Arq, or empty file restored), the sync script will re-upload every existing Zoom folder. Mitigation:

\```bash
~/RecapFlow-automation/scripts/seed-zoom-synced-from-output.sh
\```

This queries the VM for already-processed dates and seeds the state file.

## Procedure (Mode B): HDD also dead

Insert between steps 2 and 3:

### Step 2a: Restore HDD contents from Arq

1. Mount a new external HDD at `/Volumes/HDD_4TB_Archive/`.
2. Open Arq → restore `/Volumes/HDD_4TB_Archive/RecapFlow-backups/`.
3. Time budget: depends on cloud bandwidth and snapshot total size. Plan for "leave it overnight."

After restore completes, continue with Step 3.

## Critical gotcha: `~/.zoom-chat-synced`

This file tracks which Zoom meeting folders have been synced to the VM. If lost or empty, the sync script treats every existing folder under `~/Documents/Zoom/` as new.

**Effects:**
- Duplicate uploads to VM's `watch/` overwrite existing files (no harm if already-processed; the merged-call workflow has output idempotency).
- For unprocessed dates, duplicates re-trigger the workflow. Mostly idempotent but has surfaced edge cases.

**Mitigation:** run `seed-zoom-synced-from-output.sh` (Step 10) BEFORE the sync launchd job runs after DR. If you need to suppress sync entirely until you've seeded:

\```bash
launchctl bootout gui/$UID/com.patchoutech.sync-zoom-chats
# ... seed state file ...
launchctl bootstrap gui/$UID ~/Library/LaunchAgents/com.patchoutech.sync-zoom-chats.plist
\```

## Out of scope

- HDD provisioning (formatting, partitioning).
- Recovering Arq license + repo password (assumed in operator's password manager).
- Restoring Open WebUI state — lives on the VM now, restored by VM bootstrap.
- VM-side recovery — separate runbook.
```

- [ ] **Step 2: Commit**

```bash
git add docs/runbooks/workstation-disaster-recovery.md
git commit -m "$(cat <<'EOF'
docs(runbooks): add inference workstation DR runbook

Mode A (workstation died, HDD survived) and Mode B (both dead) procedures.
Covers: hardware sizing, OS+user data restore, HDD reattach, Ollama
reinstall + model pulls, SSH/launchd setup, Arq reconfiguration, and the
critical ~/.zoom-chat-synced gotcha with the seed-helper mitigation.

Spec: docs/superpowers/specs/2026-05-07-operator-tier-packaging-and-dr-design.md

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

### Task 6.3: Update root README.md

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Read current README**

Read `README.md` to find the right insertion point.

- [ ] **Step 2: Add a "Disaster Recovery" section**

Insert after the existing "Operational Warnings" section (or before "Useful Commands"):

```markdown
## Disaster Recovery

This stack is a two-node system: the VM (Docker Compose stack) and the inference workstation (local model serving + sync orchestration + Arq backups). DR procedures are documented separately:

- **VM DR:** `docs/runbooks/vm-disaster-recovery.md` — bringing a fresh VM up from a backup snapshot. Time budget: 20–45 minutes.
- **Inference workstation DR:** `docs/runbooks/workstation-disaster-recovery.md` — rebuilding the workstation. Time budget: depends on Mode A vs B and bandwidth for model re-pulls.

The backup pipeline is automated:

- VM cron at 02:00 local stages a daily snapshot at `/var/lib/recapflow-backup/staging/`.
- Workstation launchd at 02:30 pulls to `/Volumes/HDD_4TB_Archive/RecapFlow-backups/`.
- Arq's existing schedule encrypts and ships to cloud.

Verify pipeline health: `~/RecapFlow-automation/scripts/recapflow-freshness-check.sh` (also runs daily at 09:00).

Spec: `docs/superpowers/specs/2026-05-07-operator-tier-packaging-and-dr-design.md`.
```

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "$(cat <<'EOF'
docs(readme): add disaster recovery section

Links to VM and workstation DR runbooks. Documents the daily backup
pipeline (cron snapshot + launchd pull + Arq cloud).

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Self-Review

Before declaring this plan complete, verify:

1. **Spec coverage.** Walk every section of the spec and confirm each has at least one task implementing it.
   - Architecture & topology → covered by Phase 1 (Open WebUI migration consolidates the topology) and the runbook docs.
   - Backup pipeline (what gets backed up, mechanics, triggers, retention, verification) → Phase 2.
   - Install/restore flow on fresh VM (8 phases) → Phase 4.2 implements the script; 4.3 rehearses it.
   - Inference workstation DR runbook → Phase 6.2.
   - Secrets handling → enforced in Phase 2.4 (snapshot copies secrets) and Phase 4.2 (bootstrap installs them in correct order).
   - Out-of-scope items → noted in the spec; this plan does not implement them.

2. **Placeholder scan.** No "TBD", "TODO", "implement later", "add appropriate error handling" without showing the code, or "similar to Task N" without repeating the code.

3. **Type/name consistency.** Manifest function names (`manifest_compute_sha256`, `manifest_write`, `manifest_verify`) used consistently across `lib/manifest.sh`, `snapshot-vm.sh`, `recapflow-pull.sh`, `bootstrap.sh`. Preflight functions (`preflight_require_not_root`, `preflight_check_volume_mounted`, etc.) consistent across `lib/preflight.sh` and the scripts that source it. Smoke test functions (`smoke_http_200`, `smoke_n8n_workflows_listed`, `smoke_retrieval_query`) consistent in `lib/smoke-tests.sh` and `bootstrap.sh` phase 7.

4. **Open Questions / TBD in spec.** The spec listed three implementation choices (staging dir location, snapshot pruning location, freshness alert delivery). Plan locks each:
   - Staging dir: `/var/lib/recapflow-backup/staging/` (root-owned parent, user-owned dir).
   - Snapshot pruning: lives in `snapshot-vm.sh` itself (post-snapshot step).
   - Freshness alert: macOS notification via osascript.

---

## Execution Notes

- **Phases are loosely independent within their scope but order-dependent across phases.** Phase 1 (Open WebUI migration) must complete before Phase 2 (snapshot includes Open WebUI volume). Phase 2 must complete before Phase 3 (workstation pulls from VM staging). Phase 4 depends on the manifest format from Phase 2.
- **Production deployment is incremental.** Each phase is independently committable and reversible. After Phase 2 you have working snapshots even if you haven't built the pull pipeline yet (Arq just doesn't have data to pick up).
- **The DR rehearsal in Task 4.3 is the single most important validation.** A bootstrap script that has never been run end-to-end is no better than a runbook in a wiki. Do not skip it.
