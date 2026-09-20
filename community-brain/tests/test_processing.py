import hashlib
import json
from pathlib import Path
import subprocess

import pytest

from community_brain.processing.pipeline import (
    CANON,
    SNAPSHOT,
    Pipeline,
    PipelineFailure,
    OutcomeUnknown,
    aggregate_prep,
    call_component,
    classify,
    escalate,
    next_tuesday,
    normalize,
    run_backfill,
)

ROOT = Path(__file__).resolve().parents[2]
SIGNAL = "\n\n".join("## " + s + "\n\nBody content" for s in CANON)
PREP = (
    "=== SESSION ===\ndate: ignored\nmain_themes: tools, agents\n\n<!--SEGMENT\ntopic: tools\nspeakers: A\nkeywords: tools\nsummary: details\n-->\n"
    + "useful transcript content " * 10
)


def oracle(workflow, node, *, items=(), nodes=None):
    result = subprocess.run(
        ["node", str(ROOT / "tests/workflows/oracle-cli.js")],
        input=json.dumps(
            [
                {
                    "workflow": workflow,
                    "node": node,
                    "context": {
                        "items": [{"json": x} for x in items],
                        "nodes": nodes or {},
                    },
                }
            ]
        ),
        text=True,
        capture_output=True,
        check=True,
        timeout=10,
    )
    return [x["json"] for x in json.loads(result.stdout)[0]]


def response(text, finish="stop"):
    return {
        "choices": [{"message": {"content": text}, "finish_reason": finish}],
        "usage": {"prompt_tokens": 10, "completion_tokens": 20, "cost": 0.1},
    }


def fake_call(request):
    return response(
        PREP
        if request["expect"] == "prep.chunk"
        else SIGNAL
        if request["expect"].startswith("signal.")
        else "Plain text result"
    )


@pytest.mark.parametrize("mode", SNAPSHOT)
def test_prompts_config_requests_match_live_workflow_oracle(mode):
    pipeline = Pipeline(mode)
    workflow = SNAPSHOT[mode]["workflow"]
    assert (
        hashlib.sha256((ROOT / "workflows" / workflow).read_bytes()).hexdigest()
        == SNAPSHOT[mode]["sha256"]
    )
    assert pipeline.config == oracle(workflow, "Code: Pipeline Config")[0]
    transcript = (ROOT / "output/2026-09-01/transcript.txt").read_text()
    nodes = {
        "Code: Pipeline Config": pipeline.config,
        "Code: Validate and Check Partner": {
            "transcriptText": transcript,
            "chatText": "chat",
        },
        "Code: Read Transcript": {"transcriptText": transcript},
        "HTTP Request: Get Speaker Aliases": {"data": "aliases"},
    }
    for step, node in [
        ("prep", "Code: Split Prep"),
        ("signalMap", "Code: Split Signal"),
    ]:
        for halving in range(3):
            assert pipeline.split_requests(
                step, transcript, "aliases", halving
            ) == oracle(workflow, node, items=[{"halving": halving}], nodes=nodes)
    results = [
        {"ok": True, "text": SIGNAL, "chunkIndex": 1},
        {"ok": True, "text": SIGNAL, "chunkIndex": 0},
    ]
    assert (
        pipeline.reduce_request(results, "chat")
        == oracle(workflow, "Code: Build Signal Reduce", items=results, nodes=nodes)[0]
    )
    assert pipeline.post_requests(SIGNAL) == oracle(
        workflow,
        "Code: Split Post Sections",
        items=[{"signalText": SIGNAL}],
        nodes=nodes,
    )
    if mode == "weekly":
        assert (
            pipeline.request("compress", "compress", "post")
            == oracle(
                workflow,
                "Code: Build Compress Request",
                items=[{"communityPostText": "post"}],
                nodes=nodes,
            )[0]
        )
        _, formatted = next_tuesday("2026-09-08")
        user = f"Next call date: Tuesday {formatted} at 6PM ET\n\nHere is last week's community post:\n\npost"
        assert (
            pipeline.request("invite", "invite", user)
            == oracle(
                workflow,
                "Code: Build Invite Request",
                items=[{"compressedText": "post", "formattedDate": formatted}],
                nodes=nodes,
            )[0]
        )


@pytest.mark.parametrize(
    "expect,text,finish",
    [
        ("none", "hello", "stop"),
        ("none", "", "length"),
        ("none", "partial", "length"),
        ("prep.chunk", PREP, "stop"),
        ("prep.chunk", PREP.replace("keywords: tools\n", ""), "stop"),
        (
            "prep.chunk",
            PREP.split("-->")[0]
            + "-->\n=== UNRESOLVED SPEAKERS ===\n"
            + "- Speaker\n" * 20,
            "stop",
        ),
        ("signal.map", "## general\nbody", "stop"),
        ("signal.map", "```\n" + SIGNAL + "\n```", "stop"),
        ("signal.reduce", SIGNAL, "stop"),
        ("signal.reduce", SIGNAL.replace("##", "#"), "stop"),
        ("signal.reduce", SIGNAL + "\n## Appendix Notes\nextra", "stop"),
        ("signal.reduce", SIGNAL.replace("Body content", ""), "stop"),
        ("signal.reduce", SIGNAL.replace("Body content", "_None._"), "stop"),
        ("signal.reduce", SIGNAL.replace("general", "insights", 1), "stop"),
        ("post.section", "- **bold**", "stop"),
        ("post.section", "[Link](https://example.test)", "stop"),
        ("post.section", "Plain https://example.test", "stop"),
    ],
)
def test_classifier_matches_oracle(expect, text, finish):
    request = Pipeline().request("prep", "prep", "source", expect)
    normalized = normalize(request)
    assert (
        normalized
        == oracle("openrouter-call.json", "Code: Normalize", items=[request])[0]
    )
    result = classify(normalized, response(text, finish))
    assert (
        result
        == oracle(
            "openrouter-call.json",
            "Code: Classify",
            items=[response(text, finish)],
            nodes={"Code: Normalize": [normalized]},
        )[0]
    )
    if not result["ok"]:
        assert (
            escalate(result)
            == oracle("openrouter-call.json", "Code: Escalate", items=[result])[0]
        )


def test_prep_assembly_matches_oracle():
    results = [
        {
            "ok": True,
            "chunkIndex": i,
            "text": PREP + "\n=== UNRESOLVED SPEAKERS ===\n-  Someone   unknown",
            "usage": {},
        }
        for i in (1, 0)
    ]
    transcript = "[00:00:00] A: Hi\n02:13:45 - A\nLater"
    expected = oracle(
        "merged-call-summarizer.json",
        "Code: Aggregate Prep",
        items=results,
        nodes={
            "Code: Create Output Folder": {"datePrefix": "2026-09-08"},
            "Code: Validate and Check Partner": {"transcriptText": transcript},
        },
    )[0]["preparedTranscript"]
    assert aggregate_prep(results, "2026-09-08", transcript) == expected


@pytest.mark.parametrize("mode,count", [("weekly", 6), ("transcript_backfill", 3)])
def test_complete_pipeline_has_preserved_outputs(mode, count):
    artifacts = Pipeline(mode).run("source", "2026-09-08", fake_call)
    assert len(artifacts) == count
    assert list(artifacts)[-1] == (
        "2026-09-15-weekly-invite.md" if mode == "weekly" else "community-post.md"
    )
    assert all(x.strip() for x in artifacts.values())


def test_component_caps_and_metadata():
    calls = []

    def call(request):
        calls.append(request)
        return response("", "length")

    result = call_component(
        {
            **Pipeline().request("postSection", "post.section.qa", "source"),
            "section": "qa",
        },
        call,
    )
    assert result["section"] == "qa" and not result["ok"]
    assert [r["maxTokens"] for r in calls] == [16384, 24576, 32768]
    assert [r.get("reasoningEffort") for r in calls] == ["low", "low", "minimal"]


def test_retry_exhaustion_preserves_prior_artifacts_and_never_halves_post():
    saved, calls = {}, []

    def call(request):
        calls.append(request)
        return (
            response("", "length")
            if request["expect"] == "post.section"
            else fake_call(request)
        )

    with pytest.raises(PipelineFailure):
        Pipeline().run(
            "source", "2026-09-08", call, emit=lambda n, t: saved.update({n: t})
        )
    assert set(saved) == {
        "transcript.txt",
        "prepared-transcript.md",
        "extracted-signal.md",
    }
    assert len([r for r in calls if r["stepName"] == "post.section.general"]) == 3


def test_prep_halving_is_bounded():
    calls = []

    def call(request):
        calls.append(request)
        return response("", "length")

    with pytest.raises(PipelineFailure):
        Pipeline().run("one line", "2026-09-08", call)
    assert len(calls) == 9 and {r["halving"] for r in calls} == {0, 1, 2}


def test_unknown_model_outcome_never_retries():
    calls = []

    def call(request):
        calls.append(request)
        raise OutcomeUnknown()

    with pytest.raises(OutcomeUnknown):
        Pipeline().run("source", "2026-09-08", call)
    assert len(calls) == 1


def test_backfill_continues_and_skips_completed():
    def call(request):
        if request["user"] == "bad":
            raise OutcomeUnknown()
        return fake_call(request)

    meetings = [
        {"id": s, "transcript": s, "date": "2026-09-08"}
        for s in ("done", "bad", "good")
    ]
    results = run_backfill(meetings, call, completed=["done"])
    assert list(results) == ["bad", "good"]
    assert results["bad"]["processing"] == "outcome_unknown"
    assert results["good"]["indexing"] == "pending"


def test_sentinel_no_paid_post_and_reduce_context_guard():
    assert Pipeline().post_requests(SIGNAL.replace("Body content", "_None._")) == []
    pipeline = Pipeline()
    pipeline.config["steps"]["signalReduce"]["contextLimit"] = 10
    with pytest.raises(PipelineFailure, match="too large"):
        pipeline.reduce_request([{"ok": True, "text": SIGNAL, "chunkIndex": 0}], "chat")
