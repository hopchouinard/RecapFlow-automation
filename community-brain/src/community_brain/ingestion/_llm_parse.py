"""Shared helpers for parsing LLM responses.

Several extractors (chunk, session-themes, future ones) need the same
defensive JSON-with-code-fence parsing. Centralized here so fixes apply
everywhere.
"""

from __future__ import annotations

import re

_FENCE_RE = re.compile(r"^```(?:json)?\s*\n(.*?)\n```\s*$", re.DOTALL)


def strip_code_fence(raw: str) -> str:
    """Remove a leading/trailing ```json ... ``` fence if present."""
    match = _FENCE_RE.match(raw.strip())
    if match:
        return match.group(1)
    return raw
