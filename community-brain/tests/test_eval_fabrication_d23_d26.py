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


class TestD23RefusalDateExemption:
    """A forbidden date is a forbidden ASSERTION, not a forbidden MENTION."""

    NONEXISTENT_PROBE = {
        "id": "nonexistent-session",
        "class": "adversarial",
        "question": "Summarize the 2025-12-15 session.",
        "expect_refusal": True,
        "forbidden_dates": ["2025-12-15"],
    }

    def test_refusal_naming_the_forbidden_date_is_not_fabrication(self):
        ef = _harness()
        answer = "I don't see a session from 2025-12-15 in the retrieved sources."
        # "" is the no-sources context this probe actually receives.
        scored = ef.score_answer(self.NONEXISTENT_PROBE, answer, "")
        assert scored["forbidden_date_hits"] == []
        assert scored["unverified_dates"] == []
        assert scored["fabricated"] is False
        assert scored["refused"] is True

    def test_mixed_refusal_then_assertion_still_fabricates(self):
        """D23 clause 4 - mandatory regression. The trap must stay live."""
        ef = _harness()
        answer = (
            "I don't see a session from 2025-12-15 in the retrieved sources. "
            "The 2025-12-15 call covered the pricing rollout and Q3 targets."
        )
        scored = ef.score_answer(self.NONEXISTENT_PROBE, answer, "")
        assert scored["forbidden_date_hits"] == ["2025-12-15"]
        assert scored["fabricated"] is True

    def test_bare_assertion_of_the_forbidden_date_fabricates(self):
        ef = _harness()
        answer = "The 2025-12-15 session covered the pricing rollout."
        scored = ef.score_answer(self.NONEXISTENT_PROBE, answer, "")
        assert scored["forbidden_date_hits"] == ["2025-12-15"]
        assert scored["fabricated"] is True

    def test_unicode_dash_date_inside_a_refusal_is_also_exempt(self):
        ef = _harness()
        answer = "I don't see a session from 2025‑12‑15 in the retrieved sources."
        scored = ef.score_answer(self.NONEXISTENT_PROBE, answer, "")
        assert scored["forbidden_date_hits"] == []
        assert scored["fabricated"] is False

    def test_default_call_is_unchanged_for_the_production_path(self):
        """The exemption is eval-side only and MUST be opt-in: the deployed
        guard still annotates the date, which is correct for a reader who
        needs to know it was not in the sources."""
        ef = _harness()
        answer = "I don't see a session from 2025-12-15 in the retrieved sources."
        assert ef.find_forbidden_dates(answer, ["2025-12-15"]) == ["2025-12-15"]


class TestD26ContextStability:
    """Answer-phase results are not evidence without a distinct-context count."""

    def test_summarize_runs_reports_distinct_contexts(self):
        ef = _harness()
        runs = [
            [{"id": "p1", "context_digest": "aaaa", "expect_refusal": False},
             {"id": "p2", "context_digest": "cccc", "expect_refusal": False}],
            [{"id": "p1", "context_digest": "bbbb", "expect_refusal": False},
             {"id": "p2", "context_digest": "cccc", "expect_refusal": False}],
        ]
        summary = ef.summarize_runs(runs, answered=True)
        assert summary["per_probe"]["p1"]["distinct_contexts"] == 2
        assert summary["per_probe"]["p2"]["distinct_contexts"] == 1

    def test_missing_digest_does_not_crash_the_summary(self):
        ef = _harness()
        runs = [[{"id": "p1", "expect_refusal": False}]]
        summary = ef.summarize_runs(runs, answered=True)
        assert summary["per_probe"]["p1"]["distinct_contexts"] == 0

    def test_summary_stays_json_serializable(self):
        """The digest set must not survive into the report: main() writes it
        with json.dumps and a set is not encodable."""
        import json as _json
        ef = _harness()
        runs = [[{"id": "p1", "context_digest": "aaaa", "expect_refusal": False}]]
        summary = ef.summarize_runs(runs, answered=True)
        _json.dumps(summary)

    def test_digest_is_stable_for_identical_context(self):
        ef = _harness()
        assert ef._context_digest("abc") == ef._context_digest("abc")
        assert ef._context_digest("abc") != ef._context_digest("abd")
        assert len(ef._context_digest("abc")) == 16
