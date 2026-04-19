"""Batch embedding helper for the ingestion pipeline.

Wraps Ollama's `embed` call for nomic-embed-text. Centralized here so the
pipeline orchestrator can mock a single boundary for tests, and so the
embedding model + host configuration lives in one place.
"""

from __future__ import annotations

import os

import ollama

#: Default embedding model. Override per-deployment via COMMUNITY_BRAIN_EMBED_MODEL.
#: Changing this after a corpus is embedded requires full re-embedding (vectors
#: from different models are incompatible). See docs/migrations/CHANGELOG.md §8.4.
DEFAULT_EMBED_MODEL = "nomic-embed-text"

# Backwards-compat alias for any existing code that imported EMBED_MODEL.
EMBED_MODEL = DEFAULT_EMBED_MODEL


def _active_embed_model() -> str:
    """Resolve the embedding model name with env override.

    Env: COMMUNITY_BRAIN_EMBED_MODEL. Empty/unset falls through to the
    default (nomic-embed-text).
    """
    return os.environ.get("COMMUNITY_BRAIN_EMBED_MODEL") or DEFAULT_EMBED_MODEL


def embed_texts(texts: list[str], ollama_base_url: str | None) -> list[list[float]]:
    """Embed a batch of texts in one Ollama call.

    Args:
        texts: The texts to embed (in order). Empty list returns empty list
            without invoking Ollama.
        ollama_base_url: Explicit Ollama host like "http://localhost:11434".
            When None, uses the ollama module's default (process env or default
            localhost). Needed when the retrieval server and Ollama are on
            different hosts — e.g. FastAPI in Docker calling Ollama on the
            host via host.docker.internal.

    Returns:
        List of vectors in input order. Each vector's length is determined by
        the embedding model (768 for nomic-embed-text).
    """
    if not texts:
        return []

    model = _active_embed_model()
    if ollama_base_url:
        client = ollama.Client(host=ollama_base_url)
        response = client.embed(model=model, input=texts)
    else:
        response = ollama.embed(model=model, input=texts)

    return list(response["embeddings"])
