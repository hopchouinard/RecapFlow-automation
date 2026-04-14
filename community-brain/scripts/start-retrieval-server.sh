#!/bin/bash
# Start the Community Brain retrieval server.
# Called by launchd via com.communitybrain.retrieval.plist.

set -euo pipefail

PROJECT_DIR="/Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/community-brain"
VENV_PYTHON="${PROJECT_DIR}/.venv/bin/python"
LOG_DIR="${HOME}/Library/Logs/CommunityBrain"

mkdir -p "${LOG_DIR}"

export RETRIEVAL_HOST="${RETRIEVAL_HOST:-0.0.0.0}"
export RETRIEVAL_PORT="${RETRIEVAL_PORT:-8999}"
export OLLAMA_BASE_URL="${OLLAMA_BASE_URL:-http://localhost:11434}"
# RETRIEVAL_API_KEY must be set in the launchd plist or environment

cd "${PROJECT_DIR}"
exec "${VENV_PYTHON}" -m community_brain.query.retrieval_server
