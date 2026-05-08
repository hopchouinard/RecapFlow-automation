#!/usr/bin/env bats

@test "bats is wired up" {
  run echo "ok"
  [ "$status" -eq 0 ]
  [ "$output" = "ok" ]
}
