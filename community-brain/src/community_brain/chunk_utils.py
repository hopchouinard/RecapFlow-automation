"""Shared chunking utilities for Community Brain.

Provides transcript parsing, speaker normalization, token counting,
speaker-aware chunking, and output formatting (JSONL + markdown).
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass

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
