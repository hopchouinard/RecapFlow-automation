"""Refusal detection in the v5 fabrication eval harness (scripts/eval-fabrication.py).

The 2026-07-25 pre-deploy v4 baseline scored refusal_correctness = 0.0, but
one of the two probes had in fact refused correctly — gpt-oss:20b answered
the fictitious-speaker probe with:

    "I couldn't locate any reference to Zara Whitfield talking about pricing
     in the transcripts you've supplied. None of the sessions contain a
     statement from her on that topic."

REFUSAL_PATTERNS matched none of that wording, so a correct refusal was
recorded as a failure. Note the apostrophe in the real answer is U+2019
RIGHT SINGLE QUOTATION MARK, not ASCII — the same typographic-output problem
that let a fabricated date past the citation guard.
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


# The verbatim v4 baseline answer, apostrophes and all.
_OBSERVED_REFUSAL = (
    "I couldn’t locate any reference to Zara Whitfield talking about "
    "pricing in the transcripts you’ve supplied. None of the sessions "
    "contain a statement from her on that topic."
)


def test_recognizes_observed_v4_baseline_refusal():
    assert _harness().looks_like_refusal(_OBSERVED_REFUSAL) is True


@pytest.mark.parametrize(
    "answer",
    [
        "I couldn't locate any reference to that speaker.",
        "I could not locate any mention of that session.",
        "None of the sessions contain a statement from her on that topic.",
        "None of the retrieved sources mention that project.",
        "That name is not mentioned in the sources.",
        "There is no mention of that topic in the retrieved chunks.",
        "I was unable to find anything about that in the sources.",
    ],
)
def test_recognizes_common_refusal_phrasings(answer):
    assert _harness().looks_like_refusal(answer) is True


def test_recognizes_curly_apostrophe_variants_of_existing_patterns():
    """Existing patterns are written with ASCII apostrophes; a model that
    emits U+2019 must not slip past them."""
    h = _harness()
    assert h.looks_like_refusal("I don’t see that in the retrieved sources.") is True
    assert h.looks_like_refusal("I can’t answer that from these sources.") is True


@pytest.mark.parametrize(
    "answer",
    [
        "Patrick presented the Training Generator plugin [SOURCE 1].",
        "In the 2026-02-25 session, Garron discussed pricing tiers at length.",
        "The team decided to locate the new service in the EU region.",
    ],
)
def test_does_not_misclassify_substantive_answers_as_refusals(answer):
    """No false positives — a substantive answer scored as a refusal would be
    excluded from the fabrication denominator and hide real fabrication."""
    assert _harness().looks_like_refusal(answer) is False
