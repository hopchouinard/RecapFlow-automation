"""Batch embedding helper for the ingestion pipeline.

Wraps Ollama's `embed` call for nomic-embed-text. Centralized here so the
pipeline orchestrator can mock a single boundary for tests, and so the
embedding model + host configuration lives in one place.
"""

from __future__ import annotations

import ollama

#: Pinned embedding model. v1.0 corpus is embedded with this; changing it
#: requires re-embedding (not just re-extraction). See docs/migrations/CHANGELOG.md.
EMBED_MODEL = "nomic-embed-text"


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

    if ollama_base_url:
        client = ollama.Client(host=ollama_base_url)
        response = client.embed(model=EMBED_MODEL, input=texts)
    else:
        response = ollama.embed(model=EMBED_MODEL, input=texts)

    return list(response["embeddings"])
