#!/bin/bash
# Idempotent installer for the community-brain lint cron.
# Run with sudo on the n8n VM after pulling the latest from main.
# Spec: docs/superpowers/specs/2026-05-02-ingest-lint-decoupling-design.md
set -euo pipefail

SOURCE="$(dirname "$0")/community-brain-lint.cron"
DEST="/etc/cron.d/community-brain-lint"

if [ ! -f "$SOURCE" ]; then
    echo "ERROR: $SOURCE not found" >&2
    exit 1
fi

# /etc/cron.d/ entries must be 0644 owned by root.
sudo install -m 644 -o root -g root "$SOURCE" "$DEST"

# Reload cron to pick up the new file. systemd vs sysv compatibility.
if command -v systemctl >/dev/null 2>&1; then
    sudo systemctl reload cron 2>/dev/null || sudo systemctl restart cron 2>/dev/null || true
else
    sudo service cron reload 2>/dev/null || sudo service cron restart 2>/dev/null || true
fi

echo "Installed: $DEST"
echo "Verify with: cat $DEST"
echo "Manual run: docker exec community_brain_retrieval python -m community_brain.cli.lint_corpus"
echo "Next scheduled run: 04:00 UTC tomorrow"
