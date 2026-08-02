"""D23-D26 probe-contract amendment (2026-07-26).

Each test pins one decision of
tasks/03-community-brain-grounding/2026-07-26-v5-probe-contract-amendment-design.md
(Patchou-plan PR #24, merged 2026-08-02) and was watched fail against the
pre-amendment harness before its implementation step.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

_SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "eval-fabrication.py"


def _harness():
    spec = importlib.util.spec_from_file_location("eval_fabrication", _SCRIPT)
    if spec is None or spec.loader is None:  # pragma: no cover - defensive
        pytest.skip(f"cannot load {_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestD24AnchoredRefusal:
    """A refusal pattern buried in a substantive answer is not a refusal."""

    def test_substantive_answer_with_late_negative_clause_is_not_a_refusal(self):
        ef = _harness()
        # Shape of hemal-garron-conjunction, block 4 run 3: opens with a
        # substantive "Yes", then mentions absent sources two sentences later.
        answer = (
            "Yes - the mid-December call (Dec 17, 2025) included both "
            "individuals discussing the rollout.\n"
            "Beyond that, there are no retrieved sources covering their "
            "later conversations."
        )
        assert ef.looks_like_refusal(answer) is False

    def test_genuine_leading_refusal_is_still_a_refusal(self):
        ef = _harness()
        answer = (
            "I don't see a session from 2025-12-15 in the retrieved sources. "
            "Nothing further can be said about it."
        )
        assert ef.looks_like_refusal(answer) is True

    def test_typographic_apostrophe_refusal_still_detected(self):
        ef = _harness()
        answer = "I don’t see a session from 2025-12-15 in the retrieved sources."
        assert ef.looks_like_refusal(answer) is True

    def test_leading_refusal_on_a_multi_line_answer(self):
        ef = _harness()
        answer = (
            "I couldn't locate any reference to Zara Whitfield talking about "
            "pricing in the transcripts you've supplied.\n"
            "None of the sessions contain a statement from her on that topic."
        )
        assert ef.looks_like_refusal(answer) is True

    def test_empty_answer_is_not_a_refusal(self):
        ef = _harness()
        assert ef.looks_like_refusal("") is False
