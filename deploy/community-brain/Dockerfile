FROM node:24-bookworm-slim@sha256:ba849c60be29959425b8734d57b8b4b7d56f98edd9504c9af091d5281095a71e AS web
WORKDIR /web
COPY web/package.json web/package-lock.json ./
RUN npm ci
COPY web/ ./
RUN npm run build

FROM python:3.11-slim-bookworm@sha256:528257d48c1da0dcecc2e725d1ae34498d60c965f1241e39cd6a85a8859bdf84
COPY --from=ghcr.io/astral-sh/uv:0.12.11 /uv /usr/local/bin/uv
RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --uid 10001 --create-home brain
WORKDIR /app/community-brain
COPY --chown=10001:10001 community-brain/pyproject.toml community-brain/uv.lock community-brain/alembic.ini ./
COPY --chown=10001:10001 community-brain/src/ ./src/
COPY --chown=10001:10001 community-brain/migrations/ ./migrations/
# Forge's .python-version must not select a root-private managed interpreter.
RUN uv sync --python /usr/local/bin/python3.11 --no-python-downloads --locked --no-dev --no-editable
ENV TIKTOKEN_CACHE_DIR=/app/tiktoken-cache
RUN .venv/bin/python -c "import tiktoken; tiktoken.get_encoding('cl100k_base')" \
    && chmod -R a+rX /app/tiktoken-cache
COPY --from=web /web/dist /app/web/dist
ENV PATH="/app/community-brain/.venv/bin:$PATH" PYTHONUNBUFFERED=1 CB_WEB_DIST=/app/web/dist
USER 10001:10001
RUN /app/community-brain/.venv/bin/python -c "from community_brain.jobs import runtime"
EXPOSE 8090
CMD ["uvicorn", "community_brain.jobs.runtime:app", "--factory", "--host", "0.0.0.0", "--port", "8090", "--no-access-log"]
