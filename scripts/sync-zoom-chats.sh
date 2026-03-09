#!/bin/bash
# sync-zoom-chats.sh
# Called by Automator Folder Action when new items appear in ~/Documents/zoom/
# Receives new item paths as arguments.
# Looks for .txt chat files inside new subfolders, renames to YYYY-MM-DD-zoom-chat.txt,
# and rsyncs to the n8n VM.
#
# Setup:
#   1. Copy this script to ~/scripts/sync-zoom-chats.sh
#   2. chmod +x ~/scripts/sync-zoom-chats.sh
#   3. Create Automator Folder Action (see README)

set -euo pipefail

SENT_LOG="$HOME/.zoom-chat-synced"
REMOTE_HOST="n8n-automation"
REMOTE_USER="pchouinard"
REMOTE_DIR="/home/pchouinard/n8n/watch"
LOG_FILE="$HOME/.zoom-chat-sync.log"

exec >> "$LOG_FILE" 2>&1
echo "$(date): Triggered with $# items"

touch "$SENT_LOG"

process_file() {
    local file="$1"
    local folder_name="$2"

    # Skip if already synced
    if grep -qxF "$file" "$SENT_LOG"; then
        echo "Already synced: $file"
        return
    fi

    # Extract date from folder name (format: "2026-03-06 14.30.00 Meeting Name")
    local date_prefix
    date_prefix=$(echo "$folder_name" | grep -oE '^[0-9]{4}-[0-9]{2}-[0-9]{2}' || true)

    if [ -z "$date_prefix" ]; then
        echo "Skipping $file — could not extract date from folder: $folder_name"
        return
    fi

    local dest_name="${date_prefix}-zoom-chat.txt"

    if rsync -az "$file" "${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_DIR}/${dest_name}"; then
        echo "$file" >> "$SENT_LOG"
        echo "$(date): Synced: $file → ${dest_name}"
    else
        echo "$(date): Failed to sync: $file"
    fi
}

for item in "$@"; do
    if [ -d "$item" ]; then
        # New subfolder added — wait for Zoom to finish writing
        sleep 3
        folder_name=$(basename "$item")
        # Look for .txt files inside
        for file in "$item"/*.txt; do
            [ -f "$file" ] && process_file "$file" "$folder_name"
        done
    elif [ -f "$item" ] && [[ "$item" == *.txt ]]; then
        # Direct .txt file added
        folder_name=$(basename "$(dirname "$item")")
        process_file "$item" "$folder_name"
    fi
done
