#!/usr/bin/env bash
# Development-only baseline; uses fixtures and temporary databases, never deployment.
set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export REPO_ROOT="$REPO"
if [[ -f "$REPO/.env" || -f "$REPO/community-brain/config/.env" ]]; then
  echo "Use the credential-free Forge development checkout for this verification." >&2
  exit 1
fi
node --test "$REPO/tests/workflows/"*.test.js
cd "$REPO/community-brain"
"$REPO/community-brain/.venv/bin/python" -m pytest tests -q
"$REPO/community-brain/.venv/bin/python" -m pytest "$REPO/tests/cbm" -q
cd "$REPO/web"
npm test
npm run build
npm run test:e2e
