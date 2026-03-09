# Chapter 4 — Workstation-Side File Sync

**Category:** Infrastructure & Deployment
**Reading time:** 5 minutes

---

## The Challenge

Zoom saves chat logs to `~/Documents/Zoom/` inside date-stamped subfolders. This directory is protected — background processes cannot access it without Full Disk Access, which is a significant security grant.

## Solution: Automator Folder Action

Instead of a background daemon, the system uses Automator Folder Action. Folder Actions inherit the user's file access permissions without requiring additional TCC grants.

### How It Works

1. Zoom call ends → Zoom saves chat to `~/Documents/Zoom/<date> <time> <meeting>/chat.txt`
2. Automator Folder Action on `~/Documents/Zoom/` detects the new subfolder
3. Action calls `~/scripts/sync-zoom-chats.sh` with the new item paths as arguments
4. Script extracts the date from the folder name, renames the file, and rsyncs to the VM

### The Sync Script

```bash
#!/bin/bash
set -euo pipefail

SENT_LOG="$HOME/.zoom-chat-synced"
REMOTE_HOST="n8n-automation"
REMOTE_USER="YOURUSERNAME"
REMOTE_DIR="/home/YOURUSERNAME/n8n/watch"
LOG_FILE="$HOME/.zoom-chat-sync.log"

exec >> "$LOG_FILE" 2>&1

touch "$SENT_LOG"

process_file() {
    local file="$1"
    local folder_name="$2"

    # Skip if already synced
    if grep -qxF "$file" "$SENT_LOG"; then
        return
    fi

    # Extract date from folder name (format: "2026-03-06 14.30.00 Meeting Name")
    local date_prefix
    date_prefix=$(echo "$folder_name" | grep -oE '^[0-9]{4}-[0-9]{2}-[0-9]{2}' || true)

    if [ -z "$date_prefix" ]; then
        return
    fi

    local dest_name="${date_prefix}-zoom-chat.txt"

    if rsync -az "$file" "${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_DIR}/${dest_name}"; then
        echo "$file" >> "$SENT_LOG"
    fi
}

for item in "$@"; do
    if [ -d "$item" ]; then
        sleep 3  # Wait for Zoom to finish writing
        folder_name=$(basename "$item")
        for file in "$item"/*.txt; do
            [ -f "$file" ] && process_file "$file" "$folder_name"
        done
    elif [ -f "$item" ] && [[ "$item" == *.txt ]]; then
        folder_name=$(basename "$(dirname "$item")")
        process_file "$item" "$folder_name"
    fi
done
```

### Key Design Decisions

**Idempotency via sent log:** The script tracks synced files in `~/.zoom-chat-synced`. This prevents duplicate syncs if the Folder Action fires multiple times. Clear this file to reprocess.

**3-second sleep:** Zoom writes the chat file asynchronously after the folder is created. The script waits 3 seconds to ensure the file is fully written before attempting to sync.

**Date extraction from folder name:** Zoom names folders as `YYYY-MM-DD HH.MM.SS Meeting Title`. The script uses `grep -oE` to extract just the date prefix, which becomes the filename.

**Flatten to single file:** The original folder structure is discarded. The output is a single flat file named `YYYY-MM-DD-zoom-chat.txt`, which makes correlation with transcripts trivial.

## Setup on Mac

1. Copy `scripts/sync-zoom-chats.sh` to `~/scripts/sync-zoom-chats.sh`
2. `chmod +x ~/scripts/sync-zoom-chats.sh`
3. Create Automator Folder Action:
   - Open Automator → New → Folder Action
   - Set "Folder Action receives files and folders added to" → `~/Documents/Zoom`
   - Add "Run Shell Script" action
   - Set shell to `/bin/bash`, pass input as arguments
   - Script content: `~/scripts/sync-zoom-chats.sh "$@"`
   - Save as "Sync Zoom Chats"

## Debugging

```bash
# Check sync log
cat ~/.zoom-chat-sync.log

# Check what's been synced
cat ~/.zoom-chat-synced

# Clear sync history to reprocess all files
> ~/.zoom-chat-synced
```
