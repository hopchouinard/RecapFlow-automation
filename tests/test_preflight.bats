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

@test "preflight_require_free_space succeeds when filesystem has plenty of space" {
  # 0 GB requirement always passes on a real filesystem.
  run preflight_require_free_space "${TMPDIR_TEST}" 0
  [ "$status" -eq 0 ]
}

@test "preflight_require_free_space fails when requirement exceeds available" {
  # Require an absurdly large amount; no test filesystem has 999999 GB free.
  run preflight_require_free_space "${TMPDIR_TEST}" 999999
  [ "$status" -ne 0 ]
  [[ "$output" =~ "need 999999GB" ]]
}

@test "preflight_require_free_space rejects empty required_gb" {
  run preflight_require_free_space "${TMPDIR_TEST}" ""
  [ "$status" -ne 0 ]
  [[ "$output" =~ "must be a non-negative integer" ]]
}

@test "preflight_require_free_space rejects suffixed required_gb (10G)" {
  run preflight_require_free_space "${TMPDIR_TEST}" "10G"
  [ "$status" -ne 0 ]
  [[ "$output" =~ "must be a non-negative integer" ]]
}

@test "preflight_require_free_space rejects decimal required_gb (10.5)" {
  run preflight_require_free_space "${TMPDIR_TEST}" "10.5"
  [ "$status" -ne 0 ]
  [[ "$output" =~ "must be a non-negative integer" ]]
}

@test "preflight_require_free_space fails when path does not exist" {
  run preflight_require_free_space "${TMPDIR_TEST}/does-not-exist" 1
  [ "$status" -ne 0 ]
  [[ "$output" =~ "could not stat filesystem" ]]
}
