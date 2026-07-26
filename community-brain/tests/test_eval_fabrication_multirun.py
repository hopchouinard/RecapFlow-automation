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


# --- Empty answers must not count as passes ------------------------------
# The 2026-07-25 D19 run returned EMPTY content for 14 of 60 probes (23%).
# gpt-oss:20b is a reasoning model: Ollama returns `thinking` separately from
# `content`, and when the model spends its budget reasoning without emitting
# a final answer, `content` is "". Such a probe trivially satisfied
# "did not fabricate" and was scored a clean pass, inflating pass rates and
# making the acceptance evidence unusable.

def test_empty_answer_is_recorded_as_no_answer():
    m = _harness()
    out = m.score_answer({"id": "p", "class": "c"}, "", "ctx")
    assert out["no_answer"] is True


def test_whitespace_only_answer_is_recorded_as_no_answer():
    m = _harness()
    out = m.score_answer({"id": "p", "class": "c"}, "   \n  ", "ctx")
    assert out["no_answer"] is True


def test_real_answer_is_not_no_answer():
    m = _harness()
    out = m.score_answer({"id": "p", "class": "c"}, "Patrick said hello.", "ctx")
    assert out["no_answer"] is False


def test_probe_with_no_answer_does_not_pass():
    """A probe cannot pass on the strength of having produced nothing."""
    m = _harness()
    r = _result("p")
    r["no_answer"] = True
    assert m.probe_passed(r) is False


def test_summary_counts_no_answer_per_probe():
    m = _harness()
    empty = _result("p"); empty["no_answer"] = True
    ok = _result("p")
    s = m.summarize_runs([[empty], [ok], [ok]])
    assert s["per_probe"]["p"]["no_answer_count"] == 1
    assert s["per_probe"]["p"]["passes"] == 2
    assert s["per_probe"]["p"]["unanimous"] is False


# --- PR #17 review: vacuous results must not manufacture acceptance ------
# Same defect class as the empty-answer bug this file already covers: a
# non-result being counted as a pass. Three more routes were found in review.

def test_errored_probe_does_not_pass():
    """A transient retrieval/Ollama failure is not a passing run."""
    m = _harness()
    assert m.probe_passed({"id": "p", "error": "boom"}) is False


def test_errored_run_breaks_unanimity_and_is_counted():
    """Filtering errors out before summarizing let a probe that passed 4
    times and errored once report as unanimous over 4 runs."""
    m = _harness()
    runs = [[_result("p")], [_result("p")], [{"id": "p", "error": "timeout"}]]
    s = m.summarize_runs(runs, answered=True)
    assert s["per_probe"]["p"]["runs"] == 3
    assert s["per_probe"]["p"]["passes"] == 2
    assert s["per_probe"]["p"]["error_count"] == 1
    assert s["per_probe"]["p"]["unanimous"] is False
    assert s["all_unanimous"] is False


def test_probe_that_errors_every_run_still_appears():
    """It must not vanish from the report and leave all_unanimous true."""
    m = _harness()
    runs = [[_result("ok"), {"id": "bad", "error": "x"}] for _ in range(5)]
    s = m.summarize_runs(runs, answered=True)
    assert "bad" in s["per_probe"]
    assert s["all_unanimous"] is False


def test_acceptance_requires_at_least_five_runs():
    """D19 sets N >= 5. Two to four runs must not present an acceptance
    signal, even when every probe passes."""
    m = _harness()
    for n in (2, 3, 4):
        s = m.summarize_runs([[_result("a")]] * n, answered=True)
        assert s["acceptance_eligible"] is False, f"{n} runs claimed eligibility"
    s = m.summarize_runs([[_result("a")]] * 5, answered=True)
    assert s["acceptance_eligible"] is True


def test_retrieval_only_runs_claim_no_answer_phase_verdict():
    """Without --answer there is no fabricated/refused/no_answer data, so a
    unanimity or fabrication verdict would be fabricated evidence itself."""
    m = _harness()
    runs = [[{"id": "a", "target_recall": 0.5, "injected_counts": 1}] for _ in range(5)]
    s = m.summarize_runs(runs, answered=False)
    assert s["acceptance_eligible"] is False
    assert s.get("all_unanimous") is None
    assert "fabrication_rate" not in s["aggregates"]
    assert "mean_target_recall" in s["aggregates"]


def test_fabrication_rate_denominator_excludes_empty_answers():
    """aggregate()'s answered set counted no_answer results, so one
    fabrication among one real answer and one empty read as 0.5, not 1.0 —
    preserving the exact inflation the empty-answer fix was meant to remove."""
    m = _harness()
    fab = _result("a", fabricated=True)
    empty = _result("b")
    empty["no_answer"] = True
    agg = m.aggregate([fab, empty], True)
    assert agg["fabrication_rate"] == 1.0


def test_compare_uses_multirun_summary_when_present(capsys):
    """--compare read top-level per_query/aggregates, which for a multi-run
    report hold one arbitrary stochastic run — the very thing D19 exists to
    prevent."""
    import json as _json
    m = _harness()
    summary = {
        "runs": 5,
        "acceptance_eligible": True,
        "all_unanimous": False,
        "per_probe": {"a": {"runs": 5, "passes": 3, "unanimous": False}},
        "aggregates": {"fabrication_rate": {"mean": 0.2, "min": 0.0, "max": 0.4}},
    }
    base = tmp = None
    import tempfile, pathlib
    d = pathlib.Path(tempfile.mkdtemp())
    b = d / "b.json"; c = d / "c.json"
    b.write_text(_json.dumps({"summary": summary, "aggregates": {}, "per_query": []}))
    c.write_text(_json.dumps({"summary": summary, "aggregates": {}, "per_query": []}))
    m.compare(b, c)
    out = capsys.readouterr().out
    assert "runs=5" in out
    assert "unanimous" in out.lower()


def test_invalid_run_counts_are_rejected(monkeypatch):
    """PR #17 second-pass (suppressed low-confidence) finding: --runs 0 ran
    once while reporting runs_requested=0 and skipping the summary — output
    describing a run that never happened."""
    import sys
    m = _harness()
    for bad in ("0", "-1"):
        monkeypatch.setattr(sys, "argv", ["eval-fabrication.py", "--runs", bad])
        with pytest.raises(SystemExit) as exc:
            m.main()
        assert exc.value.code != 0
