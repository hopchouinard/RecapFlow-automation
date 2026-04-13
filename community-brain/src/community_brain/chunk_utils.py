"""Shared chunking utilities for Community Brain.

Provides transcript parsing, speaker normalization, token counting,
speaker-aware chunking, and output formatting (JSONL + markdown).
"""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass, asdict

import tiktoken

logger = logging.getLogger(__name__)

TRANSCRIPT_LINE_RE = re.compile(
    r"\[(\d{2}:\d{2}:\d{2})\]\s+(.+?):\s+(.*)"
)


@dataclass
class SpeakerTurn:
    """A single speaker turn from a transcript."""
    timestamp: str
    speaker: str
    text: str


def parse_transcript(text: str) -> list[SpeakerTurn]:
    """Parse raw transcript text into structured speaker turns.

    Each line is expected to match: [HH:MM:SS] Speaker Name: text
    Blank lines and unparseable lines are skipped with a warning.
    """
    turns: list[SpeakerTurn] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        match = TRANSCRIPT_LINE_RE.match(line)
        if not match:
            logger.warning("Skipping unparseable line: %s", line[:80])
            continue
        turns.append(SpeakerTurn(
            timestamp=match.group(1),
            speaker=match.group(2),
            text=match.group(3),
        ))
    return turns


def normalize_speaker(
    name: str,
    aliases: dict[str, str] | None = None,
) -> str:
    """Normalize a speaker name using an optional alias map."""
    if aliases and name in aliases:
        return aliases[name]
    return name


_ENCODING = tiktoken.get_encoding("cl100k_base")


def count_tokens(text: str) -> int:
    """Count tokens using cl100k_base encoding (standard for modern embedding models)."""
    return len(_ENCODING.encode(text))


@dataclass
class Chunk:
    """A single chunk of transcript content with metadata."""
    chunk_id: str
    session_date: str
    session_title: str
    speakers_in_chunk: list[str]
    chunk_position: int
    total_chunks_in_session: int
    content_tier: str
    content_type: str
    source: str
    text: str


def _format_turn(turn: SpeakerTurn) -> str:
    """Format a speaker turn back to transcript line format."""
    return f"[{turn.timestamp}] {turn.speaker}: {turn.text}"


def chunk_transcript(
    turns: list[SpeakerTurn],
    session_date: str,
    session_title: str,
    target_tokens: int = 500,
    overlap_tokens: int = 50,
    content_tier: str = "historical",
    content_type: str = "transcript",
    source: str = "fathom_transcript",
) -> list[Chunk]:
    """Chunk speaker turns into overlapping, speaker-boundary-aware chunks.

    Algorithm:
    1. Accumulate turns until approaching target_tokens.
    2. At boundary, finalize chunk and start new one with overlap.
    3. Never split mid-turn. A single long turn becomes its own chunk.
    4. Overlap is whole turns from the end of the previous chunk.
    """
    if not turns:
        return []

    header = f"## Session: {session_title} | Date: {session_date}\n\n"
    header_tokens = count_tokens(header)

    chunks: list[Chunk] = []
    current_turns: list[SpeakerTurn] = []
    current_tokens = header_tokens

    def _finalize_chunk(chunk_turns: list[SpeakerTurn]) -> None:
        text = header + "\n".join(_format_turn(t) for t in chunk_turns)
        speakers = sorted(set(t.speaker for t in chunk_turns))
        chunks.append(Chunk(
            chunk_id="",
            session_date=session_date,
            session_title=session_title,
            speakers_in_chunk=speakers,
            chunk_position=0,
            total_chunks_in_session=0,
            content_tier=content_tier,
            content_type=content_type,
            source=source,
            text=text,
        ))

    def _get_overlap_turns(turns_list: list[SpeakerTurn]) -> list[SpeakerTurn]:
        """Get trailing turns that fit within overlap_tokens.

        Always includes at least the last turn to guarantee overlap continuity.
        """
        overlap: list[SpeakerTurn] = []
        tokens = 0
        for turn in reversed(turns_list):
            turn_tokens = count_tokens(_format_turn(turn))
            if tokens + turn_tokens > overlap_tokens and overlap:
                # Stop adding once budget exceeded, but keep at least one turn
                break
            overlap.insert(0, turn)
            tokens += turn_tokens
        return overlap

    for turn in turns:
        turn_text = _format_turn(turn)
        turn_tokens = count_tokens(turn_text)

        if turn_tokens > target_tokens:
            if current_turns:
                _finalize_chunk(current_turns)
            logger.warning(
                "Turn at %s by %s is %d tokens (target: %d), making it its own chunk",
                turn.timestamp, turn.speaker, turn_tokens, target_tokens,
            )
            _finalize_chunk([turn])
            current_turns = []
            current_tokens = header_tokens
            continue

        if current_tokens + turn_tokens > target_tokens and current_turns:
            _finalize_chunk(current_turns)
            overlap_turns = _get_overlap_turns(current_turns)
            current_turns = list(overlap_turns)
            current_tokens = header_tokens + sum(
                count_tokens(_format_turn(t)) for t in current_turns
            )

        current_turns.append(turn)
        current_tokens += turn_tokens

    if current_turns:
        _finalize_chunk(current_turns)

    total = len(chunks)
    for i, chunk in enumerate(chunks):
        chunk.chunk_position = i + 1
        chunk.total_chunks_in_session = total
        chunk.chunk_id = f"{session_date}-chunk-{i + 1:03d}"

    return chunks


def chunks_to_jsonl(chunks: list[Chunk]) -> str:
    """Serialize chunks to JSONL format (one JSON object per line)."""
    lines = []
    for chunk in chunks:
        obj = asdict(chunk)
        lines.append(json.dumps(obj, ensure_ascii=False))
    return "\n".join(lines) + "\n"


def chunks_to_markdown(
    chunks: list[Chunk],
    session_date: str,
    session_title: str,
) -> str:
    """Produce a markdown file with YAML frontmatter and chunks separated by ---."""
    if not chunks:
        return ""

    all_speakers = sorted(set(
        speaker
        for chunk in chunks
        for speaker in chunk.speakers_in_chunk
    ))
    content_tier = chunks[0].content_tier

    speakers_yaml = json.dumps(all_speakers)
    frontmatter = (
        f"---\n"
        f'session_date: "{session_date}"\n'
        f'session_title: "{session_title}"\n'
        f'content_tier: "{content_tier}"\n'
        f"speakers: {speakers_yaml}\n"
        f"chunk_count: {len(chunks)}\n"
        f"---\n"
    )

    sections = []
    total = len(chunks)
    for chunk in chunks:
        text_without_header = chunk.text
        header_prefix = f"## Session: {session_title} | Date: {session_date}\n\n"
        if text_without_header.startswith(header_prefix):
            text_without_header = text_without_header[len(header_prefix):]

        section = f"### Chunk {chunk.chunk_position} of {total}\n\n{text_without_header}"
        sections.append(section)

    body = f"\n## Session: {session_title} | Date: {session_date}\n\n"
    body += "\n\n---\n\n".join(sections)

    return frontmatter + body + "\n"
