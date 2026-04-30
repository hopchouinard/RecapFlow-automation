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


def build_transcript_embed_text(
    *,
    topic_label: str | None,
    speakers_spoke: list[str] | None,
    speakers_mentioned: list[str] | None,
    entities: list[str] | None,
    keywords: list[str] | None,
    summary: str,
) -> str:
    """Synthesize embed_text for a prepared_transcript chunk.

    v3 format (per spec §6.4): structured-field-enriched layout.
    Vector retrieval grips on proper nouns + keywords + topic + summary,
    not on raw conversation. Hybrid retrieval (BM25 over bm25_text)
    covers raw-conversation lexical search separately.

        topic: <topic_label>
        speakers: <speakers_spoke joined>
        mentions: <speakers_mentioned joined>
        entities: <entities joined>
        keywords: <keywords joined>
        summary: <LLM-written summary>
    """
    return (
        f"topic: {topic_label or ''}\n"
        f"speakers: {', '.join(speakers_spoke or [])}\n"
        f"mentions: {', '.join(speakers_mentioned or [])}\n"
        f"entities: {', '.join(entities or [])}\n"
        f"keywords: {', '.join(keywords or [])}\n"
        f"summary: {summary}"
    )


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
