"""The answer phase must not be silently truncated by Ollama's context window.

RecapFlow #16, problem 1: 25% of probe answers came back with empty `content`.
The cause was not the model declining to answer. `run_answer` never sent
`num_ctx`, so Ollama applied its 4096-token default to a prompt of ~12,900
tokens. Replaying a stored empty probe against the live stack showed it
exactly:

    done_reason       = length
    prompt_eval_count = 4098      # rendered context is ~12,900 tokens
    eval_count        = 4094
    content_len       = 0

Two distinct defects, both fixed here:

  1. The prompt was truncated, so the model answered from roughly a third of
     the retrieved context while the verifier checked its answer against all
     of it. Every figure in the 2026-07-25/26 blocks was computed that way.
  2. Generation stopped at the window edge while still inside the `thinking`
     channel, so `content` was "".

The same replay with `num_ctx=32768` returned `done_reason=stop`,
`prompt_eval_count=12881` and a 1856-character answer.

The second defect is the one that matters for the harness's credibility: a
truncated generation is a NON-RESULT, and before this commit it was invisible.
`done_reason` is now recorded per probe and a truncated probe cannot pass —
the same treatment `no_answer` already gets, for the same reason. A verdict
computed from a prompt the model never fully saw reads as evidence and is not.
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


def _capture_post(module, payload):
    """Stub module-level httpx.post, returning the list of captured requests."""
    captured: list[dict] = []

    def fake_post(url, **kwargs):
        captured.append({"url": url, **kwargs})
        return _FakeResponse(payload)

    module.httpx.post = fake_post  # type: ignore[attr-defined]
    return captured


_OK = {
    "message": {"content": "an answer", "thinking": "some reasoning"},
    "done_reason": "stop",
    "prompt_eval_count": 12881,
    "eval_count": 1073,
}


def test_run_answer_sends_num_ctx_so_the_prompt_is_not_truncated():
    """Without num_ctx, Ollama silently clips the prompt to its 4096 default
    and the model answers from a fraction of the retrieved context."""
    m = _harness()
    captured = _capture_post(m, _OK)
    m.run_answer(
        "http://ollama", "gpt-oss:20b", "system", "context", "question", 0.0,
        num_ctx=32768,
    )
    options = captured[0]["json"]["options"]
    assert options["num_ctx"] == 32768


def test_run_answer_reports_done_reason_and_token_counts():
    """The truncation signal must reach the report. It was available from
    Ollama all along and was being discarded."""
    m = _harness()
    _capture_post(m, _OK)
    result = m.run_answer(
        "http://ollama", "gpt-oss:20b", "system", "context", "question", 0.0,
        num_ctx=32768,
    )
    assert result["content"] == "an answer"
    assert result["thinking"] == "some reasoning"
    assert result["done_reason"] == "stop"
    assert result["prompt_eval_count"] == 12881
    assert result["eval_count"] == 1073


def test_truncated_generation_is_flagged_even_when_content_is_present():
    """done_reason=length with non-empty content is still a non-result: the
    answer was cut off mid-emission. no_answer alone would not catch it."""
    m = _harness()
    _capture_post(m, {
        "message": {"content": "a partial ans", "thinking": "..."},
        "done_reason": "length",
        "prompt_eval_count": 4098,
        "eval_count": 4094,
    })
    result = m.run_answer(
        "http://ollama", "gpt-oss:20b", "system", "context", "question", 0.0,
        num_ctx=4096,
    )
    assert result["done_reason"] == "length"


def test_probe_with_truncated_generation_does_not_pass():
    """Same rule as no_answer: a probe the model could not finish answering
    has not demonstrated anything about grounding."""
    m = _harness()
    assert not m.probe_passed({
        "id": "p", "truncated": True, "fabricated": False, "no_answer": False,
    })


def test_untruncated_probe_still_passes():
    m = _harness()
    assert m.probe_passed({
        "id": "p", "truncated": False, "fabricated": False, "no_answer": False,
    })


def test_summary_counts_truncated_probes():
    """A truncation rate must be visible per probe, so a block cannot look
    clean while a quarter of it was clipped at the window edge."""
    m = _harness()
    runs = [
        [{"id": "p", "truncated": True, "fabricated": False, "no_answer": False}],
        [{"id": "p", "truncated": False, "fabricated": False, "no_answer": False}],
    ]
    summary = m.summarize_runs(runs, answered=True)
    assert summary["per_probe"]["p"]["truncated_count"] == 1
    assert summary["per_probe"]["p"]["passes"] == 1
    assert summary["all_unanimous"] is False


def test_truncated_results_are_excluded_from_the_fabrication_denominator():
    """Identical reasoning to the no_answer exclusion fixed in PR #17: a
    non-result must not dilute a rate computed over real answers."""
    m = _harness()
    agg = m.aggregate(
        [
            {"id": "a", "fabricated": True, "refused": False, "no_answer": False,
             "truncated": False},
            {"id": "b", "fabricated": False, "refused": False, "no_answer": False,
             "truncated": True},
        ],
        answered=True,
    )
    assert agg["fabrication_rate"] == 1.0


def test_num_ctx_is_exposed_on_the_command_line(monkeypatch, capsys):
    """The operator must be able to see and set the window the evidence was
    produced under; it belongs in the report, not in a constant.

    Asserting on --help output rather than just SystemExit: an unrecognized
    flag also exits, so a bare `pytest.raises(SystemExit)` would pass whether
    or not the option exists.
    """
    import sys
    m = _harness()
    monkeypatch.setattr(sys, "argv", ["eval-fabrication.py", "--help"])
    with pytest.raises(SystemExit) as exc:
        m.main()
    assert exc.value.code == 0
    assert "--num-ctx" in capsys.readouterr().out


def test_default_num_ctx_covers_the_largest_observed_context(monkeypatch):
    """The largest rendered context measured on this corpus was 60,290 chars
    (~15,100 tokens) plus the system prompt and generation headroom. The
    default must clear that without the operator having to know it."""
    import sys
    m = _harness()
    monkeypatch.setattr(sys, "argv", ["eval-fabrication.py", "--compare", "a", "b"])
    m.httpx = None  # ensure no network path is reachable
    parser_default = m.DEFAULT_NUM_CTX
    assert parser_default >= 32768
