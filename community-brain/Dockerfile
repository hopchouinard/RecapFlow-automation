FROM python:3.11-slim

WORKDIR /app

# System deps: build-essential for pyarrow/lancedb wheels that need compilation
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml ./
COPY src ./src
# Bundle default config. Compose volume mount overrides this for local edits.
COPY config ./config

RUN pip install --no-cache-dir -e "."

EXPOSE 8999

# RETRIEVAL_HOST defaults to 0.0.0.0 inside the container so uvicorn binds to
# the container network interface. Compose publishes 127.0.0.1:8999 externally
# so the server is only reachable from the VM host, not from the LAN.
ENV RETRIEVAL_HOST=0.0.0.0
ENV RETRIEVAL_PORT=8999

# Sensible container defaults. Overridable by both env_file (community-brain/
# config/.env) AND the compose `environment:` block because Dockerfile ENV is
# the lowest-precedence default — operator-supplied values always win.
ENV OLLAMA_BASE_URL=http://host.docker.internal:11434
ENV LANCEDB_PATH=/data/lancedb/nomic-v1
ENV COMMUNITY_BRAIN_CONFIG_DIR=/app/config
ENV COMMUNITY_BRAIN_ARTIFACT_ROOT=/data/output

CMD ["uvicorn", "community_brain.query.retrieval_server:app", "--host", "0.0.0.0", "--port", "8999"]
