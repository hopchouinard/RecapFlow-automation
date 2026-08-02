"""PR #18 review findings — non-results must not reach acceptance metrics.

Four defects found by review on the num_ctx fix, all the same family the fix
itself was written to close: a verdict computed from data the model never
produced, or never saw.

1. `done_reason == "length"` only catches output-length termination. A prompt
   clipped to fit `num_ctx` can still finish its (short) reply normally, so
   the probe passes while the verifier scores it against context the model
   never received. `prompt_eval_count` was recorded and never consulted.
2. `refusal_correctness` counted truncated and empty probes as refusals.
3. An empty fabrication denominator reported 0.0 — the most reassuring
   possible value for "nothing was measured".
4. `compare()` ignored `num_ctx`/`answer_timeout`, so a 4096-window report
   diffed against a 32768-window report blames the system for truncation.

Plus one raised on the Patchou-plan side (PR #24): an answer-phase failure
discarded the probe's already-successful retrieval result, coupling
`mean_target_recall` to Ollama availability.
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


class _FakeResponse:
    def __init__(self, payload):
        self._payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self._payload


# --- 1. prompt clipped before generation, reply still ends normally --------

def test_prompt_filling_the_window_is_truncated_even_when_done_reason_is_stop():
    """The measured pre-fix case was num_ctx=4096 / prompt_eval_count=4098:
    Ollama clipped the prompt and reported the overflow. A short reply after
    a clipped prompt terminates with done_reason='stop', so output-length
    detection alone misses exactly the defect this harness exists to catch."""
    m = _harness()

    def fake_post(url, **kwargs):
        return _FakeResponse({
            "message": {"content": "a short answer", "thinking": "..."},
            "done_reason": "stop",
            "prompt_eval_count": 4098,
            "eval_count": 40,
        })

    m.httpx.post = fake_post
    reply = m.run_answer(
        "http://o", "gpt-oss:20b", "sys", "ctx", "q", 0.0, num_ctx=4096,
    )
    assert reply["prompt_clipped"] is True


def test_prompt_well_inside_the_window_is_not_flagged():
    """Blocks 4 and 5 peaked at 16,243 tokens against num_ctx=32768. The
    check must not fire on healthy runs."""
    m = _harness()

    def fake_post(url, **kwargs):
        return _FakeResponse({
            "message": {"content": "answer", "thinking": "..."},
            "done_reason": "stop",
            "prompt_eval_count": 16243,
            "eval_count": 1073,
        })

    m.httpx.post = fake_post
    reply = m.run_answer(
        "http://o", "gpt-oss:20b", "sys", "ctx", "q", 0.0, num_ctx=32768,
    )
    assert reply["prompt_clipped"] is False


def test_probe_with_clipped_prompt_does_not_pass():
    m = _harness()
    assert not m.probe_passed({
        "id": "p", "truncated": True, "fabricated": False, "no_answer": False,
    })


# --- 2. refusal_correctness must ignore non-results ------------------------

def test_truncated_probe_is_excluded_from_refusal_correctness():
    """A truncated fragment containing 'I don't see' is not a refusal —
    it is a generation the harness already defines as a non-result."""
    m = _harness()
    agg = m.aggregate(
        [
            {"id": "a", "expect_refusal": True, "refusal_correct": True,
             "refused": True, "truncated": True, "no_answer": False,
             "fabricated": False},
            {"id": "b", "expect_refusal": True, "refusal_correct": False,
             "refused": False, "truncated": False, "no_answer": False,
             "fabricated": False},
        ],
        answered=True,
    )
    assert agg["refusal_correctness"] == 0.0


def test_empty_answer_is_excluded_from_refusal_correctness():
    m = _harness()
    agg = m.aggregate(
        [
            {"id": "a", "expect_refusal": True, "refusal_correct": False,
             "refused": False, "no_answer": True, "truncated": False,
             "fabricated": False},
            {"id": "b", "expect_refusal": True, "refusal_correct": True,
             "refused": True, "no_answer": False, "truncated": False,
             "fabricated": False},
        ],
        answered=True,
    )
    assert agg["refusal_correctness"] == 1.0


def test_refusal_correctness_is_none_when_every_refusal_probe_is_a_non_result():
    m = _harness()
    agg = m.aggregate(
        [{"id": "a", "expect_refusal": True, "refusal_correct": True,
          "refused": True, "truncated": True, "no_answer": False,
          "fabricated": False}],
        answered=True,
    )
    assert agg["refusal_correctness"] is None


# --- 3. empty fabrication denominator must not read 0.0 --------------------

def test_fabrication_rate_is_none_when_nothing_was_measurable():
    """0.0 from an empty denominator is the single most misleading value the
    harness can emit: it is indistinguishable from a perfect result."""
    m = _harness()
    agg = m.aggregate(
        [
            {"id": "a", "truncated": True, "refused": False,
             "no_answer": False, "fabricated": False},
            {"id": "b", "no_answer": True, "refused": False,
             "truncated": False, "fabricated": False},
        ],
        answered=True,
    )
    assert agg["fabrication_rate"] is None


# --- 4. compare() must flag incompatible answer-phase settings -------------

def _multirun(num_ctx, timeout):
    return {
        # answer_phase gates the settings check: a retrieval-only comparison
        # has no num_ctx on either side and must not warn about it.
        "answer_phase": True,
        "num_ctx": num_ctx,
        "answer_timeout": timeout,
        "summary": {
            "runs": 5, "acceptance_eligible": True, "all_unanimous": True,
            "aggregates": {"fabrication_rate": {"mean": 0.0, "min": 0.0, "max": 0.0}},
            "per_probe": {"p": {"passes": 5, "runs": 5}},
        },
    }


def test_compare_flags_mismatched_num_ctx(tmp_path, capsys):
    """The pre-fix blocks carry no num_ctx at all; diffing one against a
    32768-window block attributes truncation to the evaluated system."""
    import json
    m = _harness()
    b = tmp_path / "b.json"
    c = tmp_path / "c.json"
    b.write_text(json.dumps(_multirun(None, 600.0)))
    c.write_text(json.dumps(_multirun(32768, 1800.0)))
    m.compare(b, c)
    out = capsys.readouterr().out
    assert "num_ctx" in out
    assert "WARNING" in out.upper()


def test_compare_is_quiet_when_settings_match(tmp_path, capsys):
    import json
    m = _harness()
    b = tmp_path / "b.json"
    c = tmp_path / "c.json"
    b.write_text(json.dumps(_multirun(32768, 1800.0)))
    c.write_text(json.dumps(_multirun(32768, 1800.0)))
    m.compare(b, c)
    assert "WARNING" not in capsys.readouterr().out.upper()


def test_compare_does_not_warn_about_settings_on_retrieval_only_reports(
    tmp_path, capsys
):
    """A retrieval-only report legitimately has no num_ctx; warning that it
    is 'not recorded' would be noise on a comparison that never touched the
    answer phase."""
    import json
    m = _harness()
    r = dict(_multirun(None, None), answer_phase=False)
    b = tmp_path / "b.json"
    c = tmp_path / "c.json"
    b.write_text(json.dumps(r))
    c.write_text(json.dumps(r))
    m.compare(b, c)
    assert "WARNING" not in capsys.readouterr().out.upper()


# --- 5. an answer-phase failure must not destroy the retrieval result ------

def test_answer_phase_failure_preserves_the_retrieval_metrics():
    """Block 3's mean_target_recall read 0.2889 in run 1 purely because two
    timeouts removed already-computed recall-bearing probes from the
    denominator. A retrieval metric must not depend on Ollama's availability."""
    m = _harness()

    class Args:
        server = "http://s"
        api_key = ""
        top_k = 10
        min_score = 0.2
        answer = True
        ollama_url = "http://o"
        model = "gpt-oss:20b"
        system_prompt_text = "sys"
        temperature = 0.0
        num_ctx = 32768
        answer_timeout = 1800.0

    m.run_retrieval = lambda *a, **k: {
        "chunks": [{
            "ground_truth": {"session_date": "2026-01-01", "chunk_id": "c1"},
            "similarity": 0.9, "score_breakdown": {},
        }]
    }

    def boom(*a, **k):
        raise TimeoutError("timed out")

    m.run_answer = boom
    r = m.evaluate_query(
        {"id": "p", "class": "c", "question": "q",
         "target_sessions": ["2026-01-01"]},
        Args(),
    )
    assert r["target_recall"] == 1.0
    assert r["answer_error"]
    assert not m.probe_passed(r)


def test_answer_phase_failure_still_breaks_unanimity_and_is_counted():
    m = _harness()
    runs = [
        [{"id": "p", "target_recall": 1.0, "answer_error": "timed out"}],
        [{"id": "p", "target_recall": 1.0, "fabricated": False,
          "no_answer": False, "truncated": False}],
    ]
    s = m.summarize_runs(runs, answered=True)
    assert s["per_probe"]["p"]["error_count"] == 1
    assert s["all_unanimous"] is False
    # the retrieval metric survives both runs
    assert s["aggregates"]["mean_target_recall"]["mean"] == 1.0
