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
