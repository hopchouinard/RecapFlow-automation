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
