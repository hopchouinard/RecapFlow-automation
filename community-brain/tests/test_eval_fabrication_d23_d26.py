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


class TestD23VerifierProducedDates:
    """D23 clause 2: the exemption must cover BOTH fabrication inputs.

    The 2026-08-02 checkpoint caught this the hard way. nonexistent-session
    retrieves 36,717 characters of context, so `extract_grounding_facts`
    returns facts and the VERIFIER path runs — a branch that exempting
    `forbidden_date_hits` and the no-sources branch never touches. Live shape:

        refused             = True
        forbidden_date_hits = []              <- exempted
        unverified_dates    = ['2025-12-15']  <- not exempted
        fabricated          = True            <- 0/5, worse than before

    A correct refusal names the date precisely to say it was NOT found, so the
    date is absent from context by construction and the verifier flags exactly
    the token that proves correct behaviour.
    """

    PROBE = {
        "id": "nonexistent-session",
        "class": "adversarial",
        "question": "Summarize the 2025-12-15 session.",
        "expect_refusal": True,
        "forbidden_dates": ["2025-12-15"],
    }

    @staticmethod
    def _force_verifier_path(ef, monkeypatch, unverified_dates):
        """Make score_answer take the `facts is not None` branch."""
        monkeypatch.setattr(ef, "extract_grounding_facts", lambda ctx: {"dates": []})
        monkeypatch.setattr(
            ef,
            "verify_answer_grounding",
            lambda ans, facts: {
                "unverified_dates": list(unverified_dates),
                "unverified_sources": [],
                "unverified_chunk_ids": [],
            },
        )

    def test_verifier_dates_inside_a_refusal_are_exempt(self, monkeypatch):
        ef = _harness()
        self._force_verifier_path(ef, monkeypatch, ["2025-12-15"])
        answer = (
            "I don't see any of the retrieved sources covering a session "
            "from 2025-12-15."
        )
        scored = ef.score_answer(self.PROBE, answer, "<non-empty context>")
        assert scored["unverified_dates"] == []
        assert scored["fabricated"] is False
        assert scored["refused"] is True

    def test_verifier_dates_asserted_outside_a_refusal_still_fabricate(self, monkeypatch):
        ef = _harness()
        self._force_verifier_path(ef, monkeypatch, ["2025-12-15"])
        answer = (
            "I don't see a session from 2025-12-15 in the retrieved sources. "
            "The 2025-12-15 call covered the pricing rollout."
        )
        scored = ef.score_answer(self.PROBE, answer, "<non-empty context>")
        assert scored["unverified_dates"] == ["2025-12-15"]
        assert scored["fabricated"] is True

    def test_verifier_dates_in_a_substantive_answer_still_fabricate(self, monkeypatch):
        """No refusal anywhere: nothing is exempt."""
        ef = _harness()
        self._force_verifier_path(ef, monkeypatch, ["2026-01-09"])
        answer = "The 2026-01-09 session covered onboarding and Q1 planning."
        scored = ef.score_answer(self.PROBE, answer, "<non-empty context>")
        assert scored["unverified_dates"] == ["2026-01-09"]
        assert scored["fabricated"] is True

    def test_verifier_sources_and_chunk_ids_are_never_exempted(self, monkeypatch):
        """D23 covers dates only. Invented sources stay fabrications even
        inside a refusal sentence."""
        ef = _harness()
        monkeypatch.setattr(ef, "extract_grounding_facts", lambda ctx: {"dates": []})
        monkeypatch.setattr(
            ef,
            "verify_answer_grounding",
            lambda ans, facts: {
                "unverified_dates": [],
                "unverified_sources": ["source 9"],
                "unverified_chunk_ids": [],
            },
        )
        answer = "I don't see a session from 2025-12-15 in source 9."
        scored = ef.score_answer(self.PROBE, answer, "<non-empty context>")
        assert scored["unverified_sources"] == ["source 9"]
        assert scored["fabricated"] is True


class TestD25UnhelpfulRefusal:
    """A probe that expected an answer and got a refusal has proved nothing."""

    ANSWER_PROBE = {
        "id": "phrased-date-with-day",
        "class": "retrieval",
        "question": "What was covered on Wednesday March 4th, 2026?",
        "expect_refusal": False,
    }
    REFUSAL_PROBE = {
        "id": "nonexistent-session",
        "class": "adversarial",
        "question": "Summarize the 2025-12-15 session.",
        "expect_refusal": True,
        "forbidden_dates": ["2025-12-15"],
    }

    def test_refusal_after_retrieval_failure_is_flagged(self):
        """target_recall == 0.0: retrieval genuinely failed, so the refusal
        proves nothing about grounding."""
        ef = _harness()
        answer = "I don't see any sessions from that date in the retrieved sources."
        scored = ef.score_answer(self.ANSWER_PROBE, answer, "", target_recall=0.0)
        assert scored["unhelpful_refusal"] is True

    def test_unhelpful_refusal_does_not_pass(self):
        ef = _harness()
        answer = "I don't see any sessions from that date in the retrieved sources."
        scored = ef.score_answer(self.ANSWER_PROBE, answer, "", target_recall=0.0)
        assert ef.probe_passed(scored) is False

    def test_refusal_with_successful_retrieval_is_not_unhelpful(self):
        """D25 is titled "caused by RETRIEVAL FAILURE". If the targets were
        retrieved, a refusal is a model judgement, not a vacuous probe --
        and misclassifying it would make the keyword heuristic in
        looks_like_refusal decide the acceptance gate."""
        ef = _harness()
        answer = "I don't see any sessions from that date in the retrieved sources."
        scored = ef.score_answer(self.ANSWER_PROBE, answer, "", target_recall=1.0)
        assert scored["unhelpful_refusal"] is False
        assert ef.probe_passed(scored) is True

    def test_refusal_on_a_probe_with_no_targets_is_not_unhelpful(self):
        """target_recall is None when the probe declares no target_sessions
        (codex-production, unresolved-survey). A probe with nothing to
        retrieve cannot have suffered a retrieval failure."""
        ef = _harness()
        answer = "I don't find any question that was left unanswered."
        scored = ef.score_answer(self.ANSWER_PROBE, answer, "", target_recall=None)
        assert scored["unhelpful_refusal"] is False
        assert ef.probe_passed(scored) is True

    def test_expected_refusal_is_not_unhelpful(self):
        ef = _harness()
        answer = "I don't see a session from 2025-12-15 in the retrieved sources."
        scored = ef.score_answer(self.REFUSAL_PROBE, answer, "", target_recall=0.0)
        assert scored["unhelpful_refusal"] is False
        assert ef.probe_passed(scored) is True

    def test_substantive_answer_is_not_unhelpful(self):
        ef = _harness()
        answer = "The session covered the pricing rollout and Q3 targets."
        scored = ef.score_answer(self.ANSWER_PROBE, answer, "", target_recall=0.0)
        assert scored["unhelpful_refusal"] is False
        assert ef.probe_passed(scored) is True

    def test_summary_counts_unhelpful_refusals(self):
        ef = _harness()
        runs = [
            [{"id": "p1", "unhelpful_refusal": True, "expect_refusal": False}],
            [{"id": "p1", "unhelpful_refusal": True, "expect_refusal": False}],
        ]
        summary = ef.summarize_runs(runs, answered=True)
        assert summary["per_probe"]["p1"]["unhelpful_refusal_count"] == 2
        assert summary["per_probe"]["p1"]["passes"] == 0
        assert summary["per_probe"]["p1"]["unanimous"] is False


class TestProbeContract:
    """Pins the probe file's refusal expectations.

    D25 made expect_refusal decide pass/fail for every answer-expecting probe,
    so a wrong value is no longer cosmetic. garron-subscription-trap carried
    expect_refusal: false while being a speaker_attribution_trap whose correct
    answer is a refusal; it read as a pass until D25 turned it into 0/5.
    """

    @staticmethod
    def _queries():
        ef = _harness()
        return {q["id"]: q for q in ef.load_queries(_SCRIPT.parent / "eval" / "fabrication-queries.yaml")}

    def test_the_three_traps_expect_refusal(self):
        q = self._queries()
        for pid in ("nonexistent-session", "fictitious-speaker",
                    "garron-subscription-trap"):
            assert q[pid]["expect_refusal"] is True, (
                f"{pid} is a trap whose correct answer is a refusal"
            )

    def test_retrieval_probes_do_not_expect_refusal(self):
        q = self._queries()
        for pid in ("iso-quiet-date", "phrased-date-with-day",
                    "relative-late-december", "quarter-q1-2026",
                    "adam-james-contributions"):
            assert q[pid]["expect_refusal"] is False, (
                f"{pid} asks for content that exists; a refusal is a failure"
            )

    def test_every_probe_declares_expect_refusal(self):
        q = self._queries()
        missing = [pid for pid, v in q.items() if "expect_refusal" not in v]
        assert missing == [], f"probes missing expect_refusal: {missing}"


class TestD24LeadingNegation:
    """A bare leading negation must not hide the refusal that follows.

    Codex review of PR #22. "No. I don't see that session in the retrieved
    sources." -> _leading_clause returns "No.", which matches no
    REFUSAL_PATTERNS, so an expect_refusal probe is scored not-refused and
    FAILS. The pre-D24 whole-body scan caught it, so D24 introduced this.

    Verified against the harness before fixing: the comma form scored True
    and the period form False. One punctuation mark decided the verdict.
    """

    @pytest.mark.parametrize("answer", [
        "No. I don't see that session in the retrieved sources.",
        "None. I couldn't locate any reference to that speaker.",
        "No.\nI don't see a session from 2025-12-15.",
        "Nope. I cannot answer that from the retrieved transcripts.",
    ])
    def test_bare_leading_negation_does_not_hide_the_refusal(self, answer):
        ef = _harness()
        assert ef.looks_like_refusal(answer) is True

    def test_comma_form_still_classifies_as_a_refusal(self):
        ef = _harness()
        answer = "No, I don't see that session in the retrieved sources."
        assert ef.looks_like_refusal(answer) is True

    def test_a_substantive_negative_answer_is_not_a_refusal(self):
        """"No." answering a yes/no question is an ANSWER. Widening the
        window must not convert substantive negatives into refusals --
        codex-production asks "Has anyone used Codex for production work?"
        and a grounded "No" is a correct answer, not a failure to answer."""
        ef = _harness()
        answer = (
            "No. Several participants discussed evaluating it, but the "
            "transcripts record no production deployment."
        )
        assert ef.looks_like_refusal(answer) is False

    def test_bare_negation_with_nothing_following_is_not_a_refusal(self):
        ef = _harness()
        assert ef.looks_like_refusal("No.") is False

    def test_widening_stops_at_one_sentence(self):
        """Only the sentence immediately after the negation is admitted; a
        refusal phrase three sentences down must still not count."""
        ef = _harness()
        answer = (
            "No. The rollout completed on schedule. It shipped in December. "
            "I don't see any later sessions covering it."
        )
        assert ef.looks_like_refusal(answer) is False


class TestD25UsesContextThatReachedTheModel:
    """D25 must gate on what the model actually saw, not on what retrieval
    returned before filtering.

    Codex review of PR #22. `target_recall` is computed from the UNFILTERED
    server response; `render_context` then applies --min-score. If min_score
    drops every chunk from the target session, recall stays positive while
    the model receives a context without the target -- so an honest
    no-source refusal scores unhelpful_refusal=False and PASSES, which is
    precisely the vacuous-probe behaviour D25 exists to stop.

    Latent, not active: measured across the 2026-08-02 block, 0 of 60
    probe-runs diverged at min_score 0.2. It goes live the moment min_score
    or the score distribution moves.
    """

    @staticmethod
    def _args():
        import types
        return types.SimpleNamespace(
            server="http://s", api_key="k", top_k=10, answer=True,
            min_score=0.2, ollama_url="http://o", model="m",
            system_prompt_text="sys", temperature=0.0, num_ctx=65536,
            answer_timeout=1800.0,
        )

    def _evaluate(self, ef, monkeypatch, *, retrieved, kept, answer):
        monkeypatch.setattr(ef, "run_retrieval", lambda *a, **k: {
            "chunks": [{"ground_truth": {"session_date": d}} for d in retrieved]
        })
        monkeypatch.setattr(ef, "render_context", lambda chunks, ms: (
            "ctx", [{"ground_truth": {"session_date": d}} for d in kept]
        ))
        monkeypatch.setattr(ef, "run_answer", lambda *a, **k: {
            "content": answer, "thinking": "", "done_reason": "stop",
            "prompt_eval_count": 100, "eval_count": 100, "prompt_clipped": False,
        })
        q = {"id": "p", "class": "c", "question": "q",
             "expect_refusal": False, "target_sessions": ["2026-03-04"]}
        return ef.evaluate_query(q, self._args())

    def test_target_filtered_out_makes_an_honest_refusal_unhelpful(self):
        """Retrieval found it; min_score dropped it; the model never saw it."""
        ef = _harness()
        pytest.MonkeyPatch  # noqa - documents intent
        mp = pytest.MonkeyPatch()
        try:
            r = self._evaluate(
                ef, mp,
                retrieved=["2026-03-04"],      # pre-filter: target present
                kept=["2025-01-01"],           # post-filter: target GONE
                answer="I don't see that session in the retrieved sources.",
            )
        finally:
            mp.undo()
        assert r["target_recall"] == 1.0, "pre-filter metric must be preserved"
        assert r["kept_target_recall"] == 0.0
        assert r["unhelpful_refusal"] is True

    def test_target_survives_filtering_so_a_refusal_is_the_models_call(self):
        ef = _harness()
        mp = pytest.MonkeyPatch()
        try:
            r = self._evaluate(
                ef, mp,
                retrieved=["2026-03-04"],
                kept=["2026-03-04"],
                answer="I don't see that session in the retrieved sources.",
            )
        finally:
            mp.undo()
        assert r["target_recall"] == 1.0
        assert r["kept_target_recall"] == 1.0
        assert r["unhelpful_refusal"] is False

    def test_pre_filter_recall_is_still_what_the_retrieval_metric_reports(self):
        """mean_target_recall measures RETRIEVAL, so it must keep using the
        unfiltered value even when D25 uses the filtered one."""
        ef = _harness()
        mp = pytest.MonkeyPatch()
        try:
            r = self._evaluate(
                ef, mp,
                retrieved=["2026-03-04"],
                kept=[],
                answer="The session covered the pricing rollout.",
            )
        finally:
            mp.undo()
        agg = ef.aggregate([r], answered=True)
        assert agg["mean_target_recall"] == 1.0


class TestUnwarrantedRefusal:
    """A refusal where the material WAS present is a model failure.

    D25 covers the vacuous case: retrieval failed, so the probe proved
    nothing. It says nothing about the opposite case, and that gap let a real
    failure through on the C1c acceptance evidence.

    Measured, block B `unresolved-survey`:

        run1: refused=False  digest=1d066b3bd7df423c  11 unresolved_question chunks
        run5: refused=True   digest=1d066b3bd7df423c  11 unresolved_question chunks

    Byte-identical context, opposite behaviour. Run 5 answered "I don't find
    any question ... that was left unanswered" against eleven chunks tagged as
    unresolved questions, and scored a PASS -- because the probe declares no
    target_sessions, so target_recall is None and D25's rule never engaged.
    """

    PROBE = {"id": "unresolved-survey", "class": "unresolved_survey",
             "question": "List five questions nobody fully answered.",
             "expect_refusal": False}
    REFUSAL = "I don't find any question in the retrieved transcripts that was left unanswered."

    def test_refusal_with_material_present_is_unwarranted(self):
        """Non-empty context, no retrieval failure -> the model had material."""
        ef = _harness()
        scored = ef.score_answer(self.PROBE, self.REFUSAL, "<sources: 11 chunks>",
                                 target_recall=None)
        assert scored["unwarranted_refusal"] is True
        assert ef.probe_passed(scored) is False

    def test_retrieval_failure_stays_D25_not_unwarranted(self):
        """recall 0.0 is vacuous, not a model failure. The two outcomes are
        distinct and must not collapse into one another."""
        ef = _harness()
        probe = dict(self.PROBE, target_sessions=["2026-03-04"])
        scored = ef.score_answer(probe, self.REFUSAL, "<sources>", target_recall=0.0)
        assert scored["unhelpful_refusal"] is True
        assert scored["unwarranted_refusal"] is False
        assert ef.probe_passed(scored) is False

    def test_no_sources_at_all_is_not_unwarranted(self):
        """An empty context means nothing reached the model; refusing is
        correct and is not the model's failure."""
        ef = _harness()
        scored = ef.score_answer(self.PROBE, self.REFUSAL, "", target_recall=None)
        assert scored["unwarranted_refusal"] is False

    def test_expected_refusal_is_never_unwarranted(self):
        ef = _harness()
        probe = {"id": "nonexistent-session", "class": "nonexistent_date",
                 "question": "Summarize the 2025-12-15 session.",
                 "expect_refusal": True, "forbidden_dates": ["2025-12-15"]}
        answer = "I don't see a session from 2025-12-15 in the retrieved sources."
        scored = ef.score_answer(probe, answer, "<sources>", target_recall=None)
        assert scored["unwarranted_refusal"] is False
        assert ef.probe_passed(scored) is True

    def test_negative_answer_ok_probes_may_answer_in_the_negative(self):
        """codex-production legitimately answers "no evidence found". That is
        an ANSWER, not a refusal, and looks_like_refusal cannot tell them
        apart -- so the probe contract states it instead of the heuristic
        guessing."""
        ef = _harness()
        probe = dict(self.PROBE, id="codex-production", negative_answer_ok=True)
        answer = "I don't see any of the retrieved transcripts mentioning production use."
        scored = ef.score_answer(probe, answer, "<sources>", target_recall=None)
        assert scored["unwarranted_refusal"] is False
        assert ef.probe_passed(scored) is True

    def test_substantive_answer_is_never_unwarranted(self):
        ef = _harness()
        answer = "Five questions went unanswered: ..."
        scored = ef.score_answer(self.PROBE, answer, "<sources>", target_recall=None)
        assert scored["unwarranted_refusal"] is False

    def test_summary_counts_unwarranted_refusals(self):
        ef = _harness()
        runs = [[{"id": "p", "unwarranted_refusal": True, "expect_refusal": False}],
                [{"id": "p", "unwarranted_refusal": False, "expect_refusal": False}]]
        s = ef.summarize_runs(runs, answered=True)
        assert s["per_probe"]["p"]["unwarranted_refusal_count"] == 1
        assert s["per_probe"]["p"]["unanimous"] is False


class TestTrapPreconditionGate:
    """A trap whose target evidence never arrived is INCONCLUSIVE, not a pass.

    garron-subscription-trap refused 10/10 across both acceptance blocks with
    target_recall 0.0 and zero occurrences of Garron in the context. The model
    refused because the person was absent -- it would have behaved identically
    if retrieval were completely broken. That supplied no grounding evidence
    and still counted toward all_unanimous.
    """

    TRAP = {"id": "garron-subscription-trap", "class": "topic_attribution_trap",
            "question": "What did Garron say about subscription models?",
            "expect_refusal": True,
            "target_sessions": ["2025-10-22", "2025-10-30"]}
    REFUSAL = "I don't see any record of Garron speaking about subscription models."

    def test_trap_without_its_evidence_is_inconclusive(self):
        ef = _harness()
        scored = ef.score_answer(self.TRAP, self.REFUSAL, "<sources>", target_recall=0.0)
        assert scored["inconclusive"] is True
        assert ef.probe_passed(scored) is False, \
            "a trap that never received its evidence must not pass"

    def test_trap_with_evidence_can_pass(self):
        ef = _harness()
        scored = ef.score_answer(self.TRAP, self.REFUSAL, "<sources>", target_recall=0.8)
        assert scored["inconclusive"] is False
        assert ef.probe_passed(scored) is True

    def test_targetless_trap_is_not_gated(self):
        """nonexistent-session and fictitious-speaker declare no targets by
        design -- there is nothing to retrieve, so the gate must not fire."""
        ef = _harness()
        probe = {"id": "nonexistent-session", "class": "nonexistent_date",
                 "question": "Summarize the 2025-12-15 session.",
                 "expect_refusal": True, "forbidden_dates": ["2025-12-15"]}
        answer = "I don't see a session from 2025-12-15 in the retrieved sources."
        scored = ef.score_answer(probe, answer, "", target_recall=None)
        assert scored["inconclusive"] is False
        assert ef.probe_passed(scored) is True

    def test_summary_counts_inconclusive(self):
        ef = _harness()
        runs = [[{"id": "t", "inconclusive": True, "expect_refusal": True}]] * 2
        s = ef.summarize_runs(runs, answered=True)
        assert s["per_probe"]["t"]["inconclusive_count"] == 2
        assert s["per_probe"]["t"]["passes"] == 0


class TestMustNotAssert:
    """A trap asserts CONTENT, not phrasing.

    `expect_refusal` conflated two things: "the correct answer is negative"
    (what we care about) and "the answer matches REFUSAL_PATTERNS" (an
    accident of wording). That 23-keyword list has now decided an acceptance
    verdict three times -- hemal-garron-conjunction, codex-production, and
    garron-subscription-trap block A run 2:

        run2 "The retrieved sources don't include any statement from Garron
              Selliken about subscription models..."   -> refused=False, FAIL
        run4 "I don't see any statement from Garron Selliken about
              subscription models..."                   -> refused=True,  PASS

    Same context, same meaning, opposite verdicts, decided by the opening
    four words.

    `must_not_assert` replaces that with the question the trap exists to ask:
    did the model ASSERT the forbidden claim? A token appearing inside a
    NEGATED sentence is a denial; the same token in an affirmative sentence
    is an attribution. Negation is far more stable to detect than refusal
    phrasing, and it is what distinguishes a fabrication from a denial.
    """

    TRAP = {
        "id": "garron-subscription-trap",
        "class": "topic_attribution_trap",
        "question": "What did Garron say about subscription models?",
        "expect_refusal": True,
        "must_not_assert": ["subscription model"],
    }

    def test_negated_denial_passes_however_it_is_phrased(self):
        """Both real block-A phrasings must pass. Neither asserts anything."""
        ef = _harness()
        for answer in [
            "The retrieved sources don't include any statement from Garron "
            "Selliken about subscription models, nor is there a session "
            "where he discusses them.",
            "I don't see any statement from Garron Selliken about "
            "subscription models in the retrieved transcripts.",
            "I don't find any mention of subscription models spoken by Garron.",
            "No statement from Garron about subscription models appears in "
            "the sources.",
        ]:
            scored = ef.score_answer(self.TRAP, answer, "<sources>", target_recall=0.8)
            assert scored["asserted_forbidden"] == [], f"false positive on: {answer[:60]}"
            assert ef.probe_passed(scored) is True, f"should pass: {answer[:60]}"

    def test_affirmative_attribution_fails(self):
        """The fabrication the trap exists to catch."""
        ef = _harness()
        answer = ("Garron discussed subscription models during the October "
                  "session, arguing for annual billing.")
        scored = ef.score_answer(self.TRAP, answer, "<sources>", target_recall=0.8)
        assert scored["asserted_forbidden"] == ["subscription model"]
        assert ef.probe_passed(scored) is False

    def test_denial_followed_by_assertion_still_fails(self):
        """The mixed shape D23 also has to defend against: deny, then assert
        anyway. The second sentence is not negated."""
        ef = _harness()
        answer = ("I don't see a direct quote. Garron nonetheless covered "
                  "subscription models at length in that call.")
        scored = ef.score_answer(self.TRAP, answer, "<sources>", target_recall=0.8)
        assert scored["asserted_forbidden"] == ["subscription model"]
        assert ef.probe_passed(scored) is False

    def test_phrasing_no_longer_decides_the_verdict(self):
        """The regression this replaces: two semantically identical answers
        must now agree, where REFUSAL_PATTERNS made them disagree."""
        ef = _harness()
        a = ("The retrieved sources don't include any statement from Garron "
             "about subscription models.")
        b = "I don't see any statement from Garron about subscription models."
        sa = ef.score_answer(self.TRAP, a, "<sources>", target_recall=0.8)
        sb = ef.score_answer(self.TRAP, b, "<sources>", target_recall=0.8)
        assert ef.probe_passed(sa) == ef.probe_passed(sb) is True
        # and the old keyword classifier genuinely disagreed on these two
        assert ef.looks_like_refusal(a) != ef.looks_like_refusal(b)

    def test_probes_without_the_field_are_unaffected(self):
        """expect_refusal keeps its old meaning where must_not_assert is
        absent -- nonexistent-session and fictitious-speaker are untouched."""
        ef = _harness()
        probe = {"id": "nonexistent-session", "class": "nonexistent_date",
                 "question": "Summarize the 2025-12-15 session.",
                 "expect_refusal": True, "forbidden_dates": ["2025-12-15"]}
        answer = "I don't see a session from 2025-12-15 in the retrieved sources."
        scored = ef.score_answer(probe, answer, "", target_recall=None)
        assert scored["asserted_forbidden"] == []
        assert ef.probe_passed(scored) is True

    def test_inconclusive_still_wins_over_a_clean_assertion_check(self):
        """A trap that never got its evidence stays inconclusive even though
        it asserted nothing -- otherwise the vacuous pass returns."""
        ef = _harness()
        probe = dict(self.TRAP, target_sessions=["2025-10-22"])
        answer = "I don't see any statement from Garron about subscription models."
        scored = ef.score_answer(probe, answer, "<sources>", target_recall=0.0)
        assert scored["asserted_forbidden"] == []
        assert scored["inconclusive"] is True
        assert ef.probe_passed(scored) is False

    def test_summary_counts_forbidden_assertions(self):
        ef = _harness()
        runs = [[{"id": "t", "asserted_forbidden": ["subscription model"],
                  "expect_refusal": True}],
                [{"id": "t", "asserted_forbidden": [], "expect_refusal": True}]]
        s = ef.summarize_runs(runs, answered=True)
        assert s["per_probe"]["t"]["asserted_forbidden_count"] == 1
