#!/bin/bash
# Start the Community Brain retrieval server.
# Called by launchd via com.communitybrain.retrieval.plist.

set -euo pipefail

PROJECT_DIR="/Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/community-brain"
VENV_PYTHON="${PROJECT_DIR}/.venv/bin/python"
LOG_DIR="${HOME}/Library/Logs/CommunityBrain"

mkdir -p "${LOG_DIR}"

# Redirect stdout/stderr to log files (launchd doesn't create the dir)
exec >> "${LOG_DIR}/retrieval-server.log" 2>> "${LOG_DIR}/retrieval-server.err"

export RETRIEVAL_HOST="${RETRIEVAL_HOST:-0.0.0.0}"
export RETRIEVAL_PORT="${RETRIEVAL_PORT:-8999}"
export OLLAMA_BASE_URL="${OLLAMA_BASE_URL:-http://localhost:11434}"

# Abort on missing or placeholder API key
if [ -z "${RETRIEVAL_API_KEY:-}" ] || [ "${RETRIEVAL_API_KEY}" = "CHANGE_ME_BEFORE_LOADING" ]; then
    echo "FATAL: RETRIEVAL_API_KEY is not set or still has the placeholder value." >&2
    echo "Set a real key in the launchd plist before loading." >&2
    exit 1
fi

cd "${PROJECT_DIR}"
exec "${VENV_PYTHON}" -m community_brain.query.retrieval_server
