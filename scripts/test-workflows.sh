#!/usr/bin/env bash
# Run n8n Code-node unit tests in a throwaway container (no host node required).
set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
exec docker run --rm --entrypoint node \
  -v "$REPO/tests/workflows:/work" \
  -v "$REPO:/repo:ro" \
  -w /work -e REPO_ROOT=/repo \
  n8nio/n8n:latest --test "$@"
