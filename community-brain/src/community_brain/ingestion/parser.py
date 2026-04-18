"""Parsers for the three ingestable artifact types.

- prepared-transcript.md -> list[TranscriptSegment]  (split on <!--SEGMENT markers)
- extracted-signal.md    -> list[SignalSection]       (split on ## headings; canonical vocab only)
- community-post.md      -> CommunityPost              (whole document)

Downstream chunker consumes these records and composes Chunk instances.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass

from community_brain.chunk_utils import count_tokens

logger = logging.getLogger(__name__)

#: Canonical heading slugs allowed in extracted-signal.md. Any non-canonical
#: heading causes parse_extracted_signal to raise ValueError, so prompt drift
#: in the upstream LLM surfaces immediately rather than leaking into the corpus.
CANONICAL_SIGNAL_SLUGS: frozenset[str] = frozenset({
    "tools", "qa", "insights", "links", "decisions", "general",
})


@dataclass(frozen=True)
class TranscriptSegment:
    """One <!--SEGMENT--> block from prepared-transcript.md."""
    topic: str
    speakers: list[str]
    keywords: list[str]
    summary: str
    body: str


@dataclass(frozen=True)
class SignalSection:
    """One top-level section from extracted-signal.md."""
    slug: str
    body: str


@dataclass(frozen=True)
class CommunityPost:
    """A community post. Kept whole unless oversized (chunker handles that)."""
    body: str
    token_count: int


_FENCED_CODE_RE = re.compile(r"```.*?```", re.DOTALL)


def _normalize_line_endings(text: str) -> str:
    """Normalize CRLF and lone CR to LF for consistent downstream parsing."""
    return text.replace("\r\n", "\n").replace("\r", "\n")


def _strip_fenced_code(text: str) -> str:
    """Remove fenced code blocks before structural parsing.

    The signal prompt doesn't emit fenced code in practice, but if the LLM
    ever drifts into that, a `## qa` line inside a fence would be mis-parsed
    as a new section. Strip fences first so section detection is robust.
    """
    return _FENCED_CODE_RE.sub("", text)


_SEGMENT_HEADER_RE = re.compile(
    r"<!--SEGMENT\s*\n"
    r"topic:\s*(?P<topic>.*?)\n"
    r"speakers:\s*(?P<speakers>.*?)\n"
    r"keywords:\s*(?P<keywords>.*?)\n"
    r"summary:\s*(?P<summary>.*?)\n"
    r"-->",
    re.DOTALL,
)

_UNRESOLVED_MARKER = "=== UNRESOLVED SPEAKERS ==="


def parse_prepared_transcript(text: str) -> list[TranscriptSegment]:
    """Parse a prepared transcript into segments.

    Splits on `<!--SEGMENT ... -->` headers. Content between a header and the
    next header (or end-of-file) becomes the segment body. A trailing
    `=== UNRESOLVED SPEAKERS ===` block (if present) is stripped from the
    final segment's body.
    """
    text = _normalize_line_endings(text)
    if not text.strip():
        return []

    matches = list(_SEGMENT_HEADER_RE.finditer(text))
    if not matches:
        return []

    segments: list[TranscriptSegment] = []
    for i, match in enumerate(matches):
        body_start = match.end()
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[body_start:body_end]

        unresolved_pos = body.find(_UNRESOLVED_MARKER)
        if unresolved_pos != -1:
            body = body[:unresolved_pos]

        body = body.strip()
        if not body:
            logger.warning(
                "Skipping empty segment '%s' (no body content between markers)",
                match.group("topic").strip(),
            )
            continue

        segments.append(TranscriptSegment(
            topic=match.group("topic").strip(),
            speakers=_split_csv(match.group("speakers")),
            keywords=_split_csv(match.group("keywords")),
            summary=match.group("summary").strip(),
            body=body,
        ))

    return segments


def parse_extracted_signal(text: str) -> list[SignalSection]:
    """Parse extracted-signal.md into canonical sections.

    Raises ValueError if a non-canonical heading is encountered, so prompt
    drift surfaces at ingestion time rather than producing unqueryable chunks.
    """
    text = _normalize_line_endings(text)
    if not text.strip():
        return []

    # Split on `## ` at start of line. First element is preamble before any
    # heading -- ignore it (typically empty). Strip fenced code blocks first
    # so `## heading` inside a ``` fence is not mis-parsed as a section.
    cleaned = _strip_fenced_code(text)
    parts = re.split(r"(?m)^##\s+", cleaned)
    sections: list[SignalSection] = []
    for part in parts[1:]:
        lines = part.splitlines()
        if not lines:
            continue
        heading = lines[0].strip()
        slug = heading.lower().split()[0] if heading else ""
        if slug not in CANONICAL_SIGNAL_SLUGS:
            raise ValueError(
                f"non-canonical signal section heading: {heading!r}. "
                f"Allowed: {sorted(CANONICAL_SIGNAL_SLUGS)}"
            )
        body = f"## {heading}\n" + "\n".join(lines[1:])
        sections.append(SignalSection(slug=slug, body=body.strip()))

    return sections


def parse_community_post(text: str) -> CommunityPost:
    """Parse community-post.md into a single whole-document record."""
    text = _normalize_line_endings(text)
    return CommunityPost(body=text, token_count=count_tokens(text) if text else 0)


def _split_csv(raw: str) -> list[str]:
    """Split a comma-separated header value, stripping and ignoring empty parts."""
    return [part.strip() for part in raw.split(",") if part.strip()]
