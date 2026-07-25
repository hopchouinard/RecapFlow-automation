"""Multi-run acceptance measurement for the v5 fabrication eval harness.

Implements the D19/D20 half of the acceptance-criteria amendment
(Patchou-plan `tasks/03-community-brain-grounding/2026-07-25-v5-acceptance-criteria-amendment-design.md`):

  D19 — answer-phase criteria are evaluated over N >= 5 runs; a probe passes
        only if it passes in EVERY run (unanimity). Single-run figures may
        not be used for acceptance.
  D20 — runs persist the rendered context, so a later verifier change can be
        re-scored offline instead of requiring a re-baseline.

Both come from a concrete failure: the 2026-07-25 post-deploy eval reported
`refusal_correctness` 0.5 -> 0.0, which read as a regression. A replicate
disconfirmed it — 11 of 12 probes were identical and one probe flipped at
temperature 0. A 2-probe metric moves 0.5 on one coin flip.
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


def _result(probe_id, *, fabricated=False, refused=False, expect_refusal=False):
    return {
        "id": probe_id,
        "class": "test",
        "expect_refusal": expect_refusal,
        "fabricated": fabricated,
        "refused": refused,
        "target_recall": 0.5,
        "injected_counts": 1,
    }


# --- D20: the rendered context must be persisted -------------------------

def test_score_answer_persists_the_rendered_context():
    m = _harness()
    context = "[COMMUNITY_BRAIN_CONTEXT]\n## Retrieved Sources\nwhatever was shown"
    out = m.score_answer({"id": "p", "class": "c"}, "some answer", context)
    assert out["context"] == context, (
        "D20: without the context, a verifier change cannot be re-scored offline"
    )


def test_score_answer_records_expect_refusal_for_downstream_aggregation():
    m = _harness()
    out = m.score_answer(
        {"id": "p", "class": "c", "expect_refusal": True}, "answer", "ctx"
    )
    assert out["expect_refusal"] is True


# --- D19: unanimity across runs ------------------------------------------

def test_probe_passing_in_every_run_is_unanimous():
    m = _harness()
    runs = [[_result("a")], [_result("a")], [_result("a")]]
    s = m.summarize_runs(runs)
    assert s["per_probe"]["a"]["passes"] == 3
    assert s["per_probe"]["a"]["unanimous"] is True


def test_probe_flipping_once_is_not_unanimous():
    """The exact 2026-07-25 fictitious-speaker situation: passes twice,
    fails once. Under D19 that probe has NOT been fixed."""
    m = _harness()
    runs = [
        [_result("flaky", refused=True, expect_refusal=True)],
        [_result("flaky", refused=False, expect_refusal=True)],
        [_result("flaky", refused=True, expect_refusal=True)],
    ]
    s = m.summarize_runs(runs)
    assert s["per_probe"]["flaky"]["passes"] == 2
    assert s["per_probe"]["flaky"]["runs"] == 3
    assert s["per_probe"]["flaky"]["unanimous"] is False


def test_expect_refusal_probe_passes_only_when_it_refuses():
    m = _harness()
    runs = [[_result("r", refused=False, expect_refusal=True)]]
    s = m.summarize_runs(runs)
    assert s["per_probe"]["r"]["unanimous"] is False

    runs = [[_result("r", refused=True, expect_refusal=True)]]
    s = m.summarize_runs(runs)
    assert s["per_probe"]["r"]["unanimous"] is True


def test_fabricating_probe_never_passes():
    m = _harness()
    runs = [[_result("f", fabricated=True)], [_result("f", fabricated=True)]]
    s = m.summarize_runs(runs)
    assert s["per_probe"]["f"]["passes"] == 0
    assert s["per_probe"]["f"]["unanimous"] is False


def test_summary_reports_spread_not_just_a_point_estimate():
    """A single number hid the instability that caused the false regression
    report; the summary must expose min/max."""
    m = _harness()
    runs = [
        [_result("a", fabricated=True), _result("b")],
        [_result("a"), _result("b")],
    ]
    s = m.summarize_runs(runs)
    fab = s["aggregates"]["fabrication_rate"]
    assert fab["min"] == 0.0
    assert fab["max"] == 0.5
    assert fab["mean"] == pytest.approx(0.25)


def test_summary_counts_runs():
    m = _harness()
    s = m.summarize_runs([[_result("a")], [_result("a")], [_result("a")]])
    assert s["runs"] == 3


def test_all_probes_unanimous_flag_is_the_acceptance_signal():
    m = _harness()
    good = m.summarize_runs([[_result("a"), _result("b")]] * 5)
    assert good["all_unanimous"] is True

    bad = m.summarize_runs(
        [[_result("a"), _result("b")]] * 4 + [[_result("a", fabricated=True), _result("b")]]
    )
    assert bad["all_unanimous"] is False
