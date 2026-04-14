"""Query tools and retrieval server for Community Brain."""

from __future__ import annotations

import re


def build_filter_expression(
    filter_date: str | None = None,
    filter_speaker: str | None = None,
) -> str | None:
    """Build a safe LanceDB filter expression from user-provided values.

    Validates and escapes inputs to prevent injection via crafted filter values.
    Returns None if no filters are provided.
    """
    clauses = []

    if filter_date:
        # Validate YYYY-MM-DD format strictly
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", filter_date):
            raise ValueError(f"Invalid date format: {filter_date!r} (expected YYYY-MM-DD)")
        clauses.append(f"session_date = '{filter_date}'")

    if filter_speaker:
        # Escape single quotes to prevent expression injection
        safe_speaker = filter_speaker.replace("'", "''")
        clauses.append(f"speakers_in_chunk LIKE '%{safe_speaker}%'")

    if not clauses:
        return None

    return " AND ".join(clauses)
