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
