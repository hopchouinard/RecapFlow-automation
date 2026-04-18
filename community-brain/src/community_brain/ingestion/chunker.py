"""Compose Chunk records from parsed artifacts.

Three chunking strategies per content type (spec §5.2):

- prepared_transcript: one chunk per <!--SEGMENT. embed_text = segment header
  (topic + summary + keywords). full_text = segment body. Over-long segments
  get sliding-window sub-chunks that share the segment header as embed_text.
- extracted_signal: one chunk per canonical section. embed_text = full_text
  (section is already dense). topic_label = canonical slug.
- community_post: whole doc as one chunk if small; sliding-window split otherwise.

LLM-derived fields (entities, speech_acts, stance, etc.) are left as defaults.
The extractor (Task 15) fills them. Provenance fields (extraction_model,
extraction_prompt_version, extracted_at) are also left as defaults; the
pipeline orchestrator (Task 18) fills them.
"""

from __future__ import annotations

import datetime as dt
import logging
import re

from community_brain.chunk_utils import count_tokens

logger = logging.getLogger(__name__)
from community_brain.ingestion.parser import (
    CommunityPost,
    SignalSection,
    TranscriptSegment,
)
from community_brain.ingestion.schema import Chunk, SCHEMA_VERSION


_TRANSCRIPT_LINE_RE = re.compile(
    r"^(?:<[QA]>)?\[\d{2}:\d{2}:\d{2}\]\s+(.+?):\s+",
    re.MULTILINE,
)

_Q_OPEN_RE = re.compile(r"<Q>")
_Q_PAIR_RE = re.compile(r"<Q>.*?</Q>\s*<A>.*?</A>", re.DOTALL)


def _has_unresolved_question(full_text: str) -> bool:
    """True if any <Q>...</Q> block lacks a following <A>...</A>.

    Heuristic: count <Q> tags vs completed Q+A pair regex. Any extra
    <Q> opens beyond matched pairs are treated as unresolved.
    """
    q_count = len(_Q_OPEN_RE.findall(full_text))
    paired = len(_Q_PAIR_RE.findall(full_text))
    return q_count > paired


def chunk_prepared_transcript(
    segments: list[TranscriptSegment],
    session_id: str,
    session_date: str,
    session_title: str | None,
    source_file: str,
    segment_max_tokens: int,
) -> list[Chunk]:
    """Produce one Chunk per transcript segment (sub-chunk overlong ones).

    Each Chunk's embed_text is the segment header (topic + summary + keywords)
    so the embedding targets a short, topical vector rather than the raw
    conversational body. The body — with inline tags, speaker attribution,
    and timestamps — becomes the full_text returned at query time.
    """
    # First pass: decide how each segment splits so we can compute total_chunks.
    plans: list[tuple[TranscriptSegment, list[str]]] = []
    for segment in segments:
        body = segment.body.replace("\r\n", "\n").replace("\r", "\n")
        body_tokens = count_tokens(body)
        if body_tokens <= segment_max_tokens:
            plans.append((segment, [body]))
        else:
            plans.append((segment, _slide_window_split(body, segment_max_tokens)))

    total_chunks = sum(len(bodies) for _, bodies in plans)

    chunks: list[Chunk] = []
    global_position = 0
    for segment_idx, (segment, bodies) in enumerate(plans, start=1):
        embed_text = _segment_embed_text(segment)
        for sub_idx, body in enumerate(bodies, start=1):
            global_position += 1
            # Segment-index-based ID keeps upsert stable even if sub-chunking changes.
            # Format: {session}:transcript:{segment:03d}  (single-chunk segment)
            #         {session}:transcript:{segment:03d}.{sub:02d}  (sub-chunks)
            if len(bodies) == 1:
                chunk_id = f"{session_id}:transcript:{segment_idx:03d}"
            else:
                chunk_id = f"{session_id}:transcript:{segment_idx:03d}.{sub_idx:02d}"
            chunks.append(_base_chunk(
                session_id=session_id,
                session_date=session_date,
                session_title=session_title,
                source_file=source_file,
                content_type="prepared_transcript",
                chunk_id=chunk_id,
                chunk_index=global_position,
                total_chunks_in_source=total_chunks,
                embed_text=embed_text,
                full_text=body,
                topic_label=segment.topic,
                speakers_spoke=_extract_speakers_from_body(body) or list(segment.speakers),
                keywords=list(segment.keywords),
            ))
    return chunks


def chunk_extracted_signal(
    sections: list[SignalSection],
    session_id: str,
    session_date: str,
    session_title: str | None,
    source_file: str,
) -> list[Chunk]:
    """One Chunk per canonical signal section. embed_text == full_text."""
    total = len(sections)
    chunks: list[Chunk] = []
    for i, section in enumerate(sections, start=1):
        chunk_id = f"{session_id}:signal:{section.slug}"
        chunks.append(_base_chunk(
            session_id=session_id,
            session_date=session_date,
            session_title=session_title,
            source_file=source_file,
            content_type="extracted_signal",
            chunk_id=chunk_id,
            chunk_index=i,
            total_chunks_in_source=total,
            embed_text=section.body,
            full_text=section.body,
            topic_label=section.slug,
            speakers_spoke=None,  # signal is LLM-synthesized; no spoken attribution
            keywords=None,
        ))
    return chunks


def chunk_community_post(
    post: CommunityPost,
    session_id: str,
    session_date: str,
    session_title: str | None,
    source_file: str,
    post_max_tokens: int,
) -> list[Chunk]:
    """Community post as one chunk if small enough, else sliding-window split."""
    if post.token_count <= post_max_tokens:
        return [_base_chunk(
            session_id=session_id,
            session_date=session_date,
            session_title=session_title,
            source_file=source_file,
            content_type="community_post",
            chunk_id=f"{session_id}:post:main",
            chunk_index=1,
            total_chunks_in_source=1,
            embed_text=post.body,
            full_text=post.body,
            topic_label="session_narrative",
            speakers_spoke=None,
            keywords=None,
        )]

    parts = _slide_window_split(post.body, post_max_tokens)
    total = len(parts)
    return [
        _base_chunk(
            session_id=session_id,
            session_date=session_date,
            session_title=session_title,
            source_file=source_file,
            content_type="community_post",
            chunk_id=f"{session_id}:post:{i:03d}",
            chunk_index=i,
            total_chunks_in_source=total,
            embed_text=part,
            full_text=part,
            topic_label="session_narrative",
            speakers_spoke=None,
            keywords=None,
        )
        for i, part in enumerate(parts, start=1)
    ]


# --- Internal helpers ---


def _base_chunk(
    *,
    session_id: str,
    session_date: str,
    session_title: str | None,
    source_file: str,
    content_type: str,
    chunk_id: str,
    chunk_index: int,
    total_chunks_in_source: int,
    embed_text: str,
    full_text: str,
    topic_label: str | None,
    speakers_spoke: list[str] | None,
    keywords: list[str] | None,
) -> Chunk:
    """Construct a Chunk with deterministic fields populated.

    LLM-derived fields default to empty/null; the extractor fills them later.
    Embedding defaults to an empty list; the pipeline orchestrator fills it.
    """
    return Chunk(
        schema_version=SCHEMA_VERSION,
        chunk_id=chunk_id,
        session_id=session_id,
        session_date=session_date,
        session_title=session_title,
        content_type=content_type,  # type: ignore[arg-type]
        source_file=source_file,
        chunk_index=chunk_index,
        total_chunks_in_source=total_chunks_in_source,
        speakers_spoke=speakers_spoke,
        speakers_mentioned=None,
        entities=[],
        keywords=keywords,
        topic_label=topic_label,
        session_themes=[],
        speech_acts=[],
        stance=None,
        certainty="asserted",
        chunk_local_markers=[],
        corpus_derived_markers=[],
        corpus_markers_computed_at=None,
        has_question="<Q>" in full_text,
        has_answer="<A>" in full_text,
        has_unresolved_question=_has_unresolved_question(full_text),
        has_insight="\u25b6" in full_text,
        decisions=None,
        action_items=None,
        external_refs=None,
        references_prior=False,
        extraction_model="",
        extraction_prompt_version="",
        extraction_status="pending",
        extraction_error=None,
        extracted_at=None,
        embed_text=embed_text,
        full_text=full_text,
        embedding=[],
    )


def _extract_speakers_from_body(body: str) -> list[str]:
    """Pull distinct speaker labels from `[HH:MM:SS] Speaker: ...` lines."""
    return sorted(set(_TRANSCRIPT_LINE_RE.findall(body)))


def _segment_embed_text(segment: TranscriptSegment) -> str:
    """Build the text that gets embedded for a transcript segment.

    Per dual-field design: embed the topical header fields, not the body.
    """
    return (
        f"topic: {segment.topic}\n"
        f"summary: {segment.summary}\n"
        f"keywords: {', '.join(segment.keywords)}"
    )


def _slide_window_split(text: str, max_tokens: int, overlap_tokens: int = 50) -> list[str]:
    """Split text into paragraph-bounded windows of ~max_tokens each.

    Paragraphs are kept intact — never mid-paragraph splits. If a single
    paragraph exceeds max_tokens, it becomes its own oversized window
    (logged implicitly via chunk-size monitoring). A small overlap of whole
    trailing paragraphs is preserved when it fits within overlap_tokens.
    """
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    if not paragraphs:
        return [text]

    out: list[str] = []
    current: list[str] = []
    current_tokens = 0
    for para in paragraphs:
        t = count_tokens(para)
        if t > max_tokens:
            logger.warning(
                "Paragraph of %d tokens exceeds max_tokens=%d; emitting as oversize chunk",
                t, max_tokens,
            )
        if current_tokens + t > max_tokens and current:
            out.append("\n\n".join(current))
            if current and count_tokens(current[-1]) <= overlap_tokens:
                current = [current[-1]]
                current_tokens = count_tokens(current[-1])
            else:
                current = []
                current_tokens = 0
        current.append(para)
        current_tokens += t

    if current:
        out.append("\n\n".join(current))

    return out or [text]
