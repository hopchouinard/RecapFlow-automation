"""Exercise the development spending guard without network or paid calls."""

import importlib.util
from pathlib import Path
from unittest.mock import Mock, patch

import pytest
from community_brain.processing.pipeline import OutcomeUnknown

path = (
    Path(__file__).resolve().parents[2]
    / "deploy/community-brain/live-development/bounded_worker.py"
)
spec = importlib.util.spec_from_file_location("bounded_worker", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


@pytest.mark.parametrize(
    "changes",
    [
        {"limit_remaining": 0},
        {"limit": 50},
        {"limit_reset": "daily"},
        {"is_management_key": True},
        {"include_byok_in_limit": False},
        {"limit_remaining": None},
    ],
)
def test_invalid_allowance_never_reaches_inference(changes):
    allowance = {
        "limit": 5,
        "limit_remaining": 5,
        "limit_reset": None,
        "is_management_key": False,
        "include_byok_in_limit": True,
    }
    allowance.update(changes)
    response = Mock()
    response.json.return_value = {"data": allowance}
    with (
        patch.object(module.httpx, "get", return_value=response),
        patch.object(module.OpenRouter, "__call__") as inference,
    ):
        with pytest.raises(OutcomeUnknown):
            module.BoundedOpenRouter("fixture-only")({})
        inference.assert_not_called()


def test_request_count_guard_stops_before_network():
    worker = module.BoundedOpenRouter("fixture-only")
    worker.calls = 12
    with (
        patch.object(module.httpx, "get") as allowance,
        patch.object(module.OpenRouter, "__call__") as inference,
    ):
        with pytest.raises(OutcomeUnknown):
            worker({})
        allowance.assert_not_called()
        inference.assert_not_called()


def test_indexing_malformed_response_stops_with_private_intent(tmp_path, monkeypatch):
    from community_brain import llm
    from community_brain.llm import LLMOutcomeUnknown

    journal = tmp_path / "indexing.jsonl"
    monkeypatch.setattr(module, "Path", lambda _: journal)
    monkeypatch.setenv("CB_OPENROUTER_API_KEY", "fixture-only")
    allowance = Mock()
    allowance.json.return_value = {
        "data": {
            "limit": 5,
            "limit_reset": None,
            "limit_remaining": 4,
            "is_management_key": False,
            "include_byok_in_limit": True,
        }
    }
    invalid = Mock()
    invalid.json.side_effect = ValueError("malformed")
    post = Mock(return_value=invalid)
    monkeypatch.setattr(llm.httpx, "get", Mock(return_value=allowance))
    monkeypatch.setattr(llm.httpx, "post", post)
    module.audit_ingestion(Mock())
    with pytest.raises(LLMOutcomeUnknown):
        llm.httpx.post(llm.OPENROUTER_URL, json={"model": "fixture"})
    assert post.call_count == 1
    assert '"state": "intent"' in journal.read_text()
    assert "fixture-only" not in journal.read_text()


@pytest.mark.parametrize(
    "field", ["scope", "mode", "parent_id", "recording", "timestamp", "source", "chat"]
)
def test_approved_recording_guard_rejects_other_inputs(field):
    from types import SimpleNamespace

    job = SimpleNamespace(
        scope="community-brain-dev",
        mode="transcript_backfill",
        parent_id="33cc7538-e326-4f74-93ef-f2fcbb5c1624",
        identity={"meeting_id": "181075701", "started_at": "2026-09-08T21:54:33Z"},
        sources={"transcript": "27969d75-10a9-4a46-8cf4-b63d1d7035d9"},
    )
    module.verify_approved_recording(job)
    if field in ("scope", "mode", "parent_id"):
        setattr(job, field, "unapproved")
    elif field == "recording":
        job.identity["meeting_id"] = "unapproved"
    elif field == "timestamp":
        job.identity["started_at"] = "2026-09-09T00:00:00Z"
    elif field == "source":
        job.sources["transcript"] = "unapproved"
    else:
        job.sources["chat"] = "unapproved"
    with pytest.raises(AssertionError):
        module.verify_approved_recording(job)


def test_indexing_ceiling_stops_before_next_provider_call(tmp_path, monkeypatch):
    from community_brain import llm
    from community_brain.llm import LLMOutcomeUnknown

    journal = tmp_path / "recording.jsonl"
    monkeypatch.setenv("CB_OPENROUTER_API_KEY", "fixture-only")
    allowance = Mock()
    allowance.json.return_value = {
        "data": {
            "limit": 5,
            "limit_reset": None,
            "limit_remaining": 4,
            "is_management_key": False,
            "include_byok_in_limit": True,
        }
    }
    response = Mock()
    response.json.return_value = {"usage": {"cost": 0.001}}
    get = Mock(return_value=allowance)
    post = Mock(return_value=response)
    monkeypatch.setattr(llm.httpx, "get", get)
    monkeypatch.setattr(llm.httpx, "post", post)
    store = Mock()
    store.storage.put.return_value = ("private", "hash", 1)
    module.audit_ingestion(store, journal_path=str(journal), ceiling=30)
    for _ in range(30):
        llm.httpx.post(llm.OPENROUTER_URL, json={"model": "fixture"})
    with pytest.raises(LLMOutcomeUnknown):
        llm.httpx.post(llm.OPENROUTER_URL, json={"model": "fixture"})
    assert post.call_count == get.call_count == 30
    assert len(journal.read_text().splitlines()) == 60
    with pytest.raises(RuntimeError, match="Previous indexing intents"):
        module.audit_ingestion(store, journal_path=str(journal), ceiling=30)


def test_weekly_recording_requires_exact_chat_and_mode():
    from types import SimpleNamespace

    job = SimpleNamespace(
        scope="community-brain-dev",
        mode="weekly",
        parent_id="33cc7538-e326-4f74-93ef-f2fcbb5c1624",
        identity={"meeting_id": "181075701", "started_at": "2026-09-08T21:54:33Z"},
        sources={
            "transcript": "27969d75-10a9-4a46-8cf4-b63d1d7035d9",
            "chat": "23d9780b-513e-4782-96d2-97211e31e855",
        },
    )
    module.verify_approved_recording(job, weekly=True)
    with pytest.raises(AssertionError):
        module.verify_approved_recording(job)
    for chat in (None, "unapproved"):
        job.sources["chat"] = chat
        with pytest.raises(AssertionError):
            module.verify_approved_recording(job, weekly=True)
