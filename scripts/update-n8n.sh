#!/bin/bash
# update-n8n.sh
# Updates n8n to the latest Docker image version.
# Pulls the latest n8nio/n8n:latest image, recreates the container,
# and lets n8n auto-migrate the database on startup.
#
# Usage:
#   cd ~/n8n && bash scripts/update-n8n.sh
#   -- or, from any directory --
#   bash ~/n8n/scripts/update-n8n.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
N8N_DIR="$(dirname "$SCRIPT_DIR")"
LOG_FILE="$N8N_DIR/update-n8n.log"

log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S')  $*" | tee -a "$LOG_FILE"
}

cd "$N8N_DIR"

log "=== n8n update started ==="

# Capture current image digest before update
BEFORE=$(docker inspect --format '{{.Image}}' n8n 2>/dev/null || echo "unknown")
log "Current image digest: $BEFORE"

# Pull latest image
log "Pulling latest n8nio/n8n image..."
docker compose pull

# Stop and remove the running containers
log "Stopping containers..."
docker compose down

# Start containers with the new image (n8n auto-migrates the DB on startup)
log "Starting containers..."
docker compose up -d

# Wait for n8n to become healthy
log "Waiting for n8n to be ready..."
for i in $(seq 1 30); do
    if docker compose logs n8n --since 10s 2>/dev/null | grep -q "n8n ready on"; then
        break
    fi
    sleep 2
done

# Capture new image digest
AFTER=$(docker inspect --format '{{.Image}}' n8n 2>/dev/null || echo "unknown")
log "New image digest: $AFTER"

if [ "$BEFORE" = "$AFTER" ]; then
    log "Already on the latest version — no update applied."
else
    log "Update complete (image changed)."
fi

log "=== n8n update finished ==="
