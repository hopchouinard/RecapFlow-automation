"""forbidden_dates trap detection in the v5 fabrication eval harness.

PR #6 review (2026-07-25) caught that `adcddad` normalized Unicode dashes in
the FILTER's verifier but left the harness's own `forbidden_dates` checks as
raw substring matches against the un-normalized answer.

This is not theoretical — it demonstrably fired in the rev2 v4 baseline. The
`nonexistent-session` probe named the forbidden date `2025-12-15` but wrote
it with U+2011, so `forbidden_date_hits` recorded `[]`. That probe was still
scored `fabricated` via `unverified_dates`, so the aggregate held; but on the
NO-SOURCES path `forbidden_dates` is the only verification available, and
there a missed trap silently undercounts fabrication.

The trap check lived inline in `evaluate_query()`, which does network I/O and
so could not be unit-tested. Extracted to the pure `find_forbidden_dates()`.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

_SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "eval-fabrication.py"

_NB_HYPHEN = "‑"   # U+2011, what gpt-oss:20b actually emitted
_EN_DASH = "–"
_MINUS = "−"


def _harness():
    spec = importlib.util.spec_from_file_location("eval_fabrication", _SCRIPT)
    if spec is None or spec.loader is None:  # pragma: no cover - defensive
        pytest.skip(f"cannot load {_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_trap_detected_with_the_exact_u2011_form_from_the_v4_baseline():
    m = _harness()
    answer = f"**2025{_NB_HYPHEN}12{_NB_HYPHEN}15 – AI Developer Accelerator Weekly Call**"
    assert m.find_forbidden_dates(answer, ["2025-12-15"]) == ["2025-12-15"]


@pytest.mark.parametrize("dash", [_NB_HYPHEN, _EN_DASH, _MINUS])
def test_trap_detected_across_dash_variants(dash):
    m = _harness()
    answer = f"Discussed on 2025{dash}12{dash}15."
    assert m.find_forbidden_dates(answer, ["2025-12-15"]) == ["2025-12-15"]


def test_trap_still_detected_with_plain_ascii_hyphen():
    m = _harness()
    assert m.find_forbidden_dates("Discussed on 2025-12-15.", ["2025-12-15"]) == [
        "2025-12-15"
    ]


def test_clean_answer_trips_no_trap():
    m = _harness()
    answer = "I don't see that date in the retrieved sources."
    assert m.find_forbidden_dates(answer, ["2025-12-15"]) == []


def test_no_forbidden_dates_configured_is_empty():
    m = _harness()
    assert m.find_forbidden_dates("anything at all", []) == []
    assert m.find_forbidden_dates("anything at all", None) == []


def test_returns_every_configured_trap_that_hit():
    m = _harness()
    answer = f"Both 2025{_NB_HYPHEN}12{_NB_HYPHEN}15 and 2026-05-12 were named."
    assert m.find_forbidden_dates(answer, ["2025-12-15", "2026-05-12"]) == [
        "2025-12-15",
        "2026-05-12",
    ]
