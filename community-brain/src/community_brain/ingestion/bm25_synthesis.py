"""bm25_text synthesis for v3 hybrid retrieval.

The synthesized field concatenates structured metadata (topic_label,
entities, speakers_spoke, speakers_mentioned, keywords) with the chunk's
full_text. The FTS index targets this column rather than full_text-only
so lexical retrieval benefits from the extracted structured fields.

Spec: docs/superpowers/specs/2026-04-29-retrieval-v3-and-stage-c-v2-design.md §10
"""
from __future__ import annotations


def synthesize_bm25_text(
    *,
    topic_label: str | None,
    entities: list[str] | None,
    speakers_spoke: list[str] | None,
    speakers_mentioned: list[str] | None,
    keywords: list[str] | None,
    full_text: str,
) -> str:
    """Build the bm25_text representation for a chunk.

    Layout (one section per line, empty sections render as empty strings):

        <topic_label or "">
        <entities joined with ", ">
        <speakers_spoke joined with ", ">
        <speakers_mentioned joined with ", ">
        <keywords joined with ", ">
        <full_text>

    None list values are normalized to empty.
    """
    parts = [
        topic_label or "",
        ", ".join(entities or []),
        ", ".join(speakers_spoke or []),
        ", ".join(speakers_mentioned or []),
        ", ".join(keywords or []),
        full_text,
    ]
    return "\n".join(parts)
