"""bm25_text synthesis for v4 hybrid retrieval.

The synthesized field concatenates structured metadata (topic_label,
entities, speakers_spoke, speakers_mentioned, keywords) with the chunk's
full_text AND a date-variants block to enable date-aware queries.

Spec: docs/superpowers/specs/2026-05-03-retrieval-v4-quality-improvements-design.md §5.1a
"""
from __future__ import annotations

import datetime as _dt


_MONTH_NAMES = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
)


def _date_variants(session_date: str) -> str:
    """Build the date-variants token block for a given ISO session_date.

    Returns a single line of whitespace-separated tokens. Empty string if
    session_date is malformed.
    """
    try:
        dt = _dt.date.fromisoformat(session_date)
    except (ValueError, TypeError):
        return ""

    year = dt.year
    month_num = dt.month
    day = dt.day
    month_name = _MONTH_NAMES[month_num - 1]

    quarter = (month_num - 1) // 3 + 1  # 1..4
    half = 1 if month_num <= 6 else 2

    if day <= 10:
        rel_prefix = "early"
    elif day <= 20:
        rel_prefix = "mid"
    else:
        rel_prefix = "late"

    tokens = [
        session_date,                         # 2026-03-04
        f"{year}-{month_num:02d}",            # 2026-03
        month_name,                           # March
        f"{month_name}-{year}",               # March-2026
        f"{month_name} {day} {year}",         # March 4 2026
        f"{month_name} {day}th {year}",       # March 4th 2026
        f"Q{quarter}-{year}",                 # Q1-2026
        f"H{half}-{year}",                    # H1-2026
        f"{rel_prefix}-{month_name}-{year}",  # early-March-2026
    ]
    return " ".join(tokens)


def synthesize_bm25_text(
    *,
    topic_label: str | None,
    entities: list[str] | None,
    speakers_spoke: list[str] | None,
    speakers_mentioned: list[str] | None,
    keywords: list[str] | None,
    full_text: str,
    session_date: str,
) -> str:
    """Build the bm25_text representation for a chunk.

    Layout (one section per line, empty sections render as empty strings):

        <topic_label or "">
        <entities joined with ", ">
        <speakers_spoke joined with ", ">
        <speakers_mentioned joined with ", ">
        <keywords joined with ", ">
        <full_text>
        <date variants line>

    Date variants line includes ISO date, month name, year-month, phrased
    forms, quarter, half, and an early/mid/late-prefixed month-year token.
    """
    parts = [
        topic_label or "",
        ", ".join(entities or []),
        ", ".join(speakers_spoke or []),
        ", ".join(speakers_mentioned or []),
        ", ".join(keywords or []),
        full_text,
        _date_variants(session_date),
    ]
    return "\n".join(parts)
