import importlib.util
from pathlib import Path

import httpx
import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    "acquisition_worker",
    ROOT / "deploy/community-brain/live-development/acquisition_worker.py",
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_acquisition_credential_only_in_one_shot_worker():
    base = yaml.safe_load(
        (ROOT / "deploy/community-brain/compose.live-development.yml").read_text()
    )
    overlay = yaml.safe_load(
        (
            ROOT / "deploy/community-brain/compose.acquisition-development.yml"
        ).read_text()
    )
    assert all(
        "CB_FATHOM_API_KEY" not in service.get("environment", {})
        for service in base["services"].values()
    )
    worker = overlay["services"]["acquisition-worker"]
    assert worker["profiles"] == ["acquisition"]
    assert worker["environment"]["CB_ENABLE_MODEL_CALLS"] == "false"
    assert worker["environment"]["CB_ENABLE_NETWORK_PUBLICATION"] == "false"
    assert "CB_OPENROUTER_API_KEY" not in worker["environment"]
    assert not worker.get("ports") and not worker.get("restart")
    assert "corpus:/state/corpus" not in worker["volumes"]


def test_selected_identity_and_single_transcript_only():
    requests = []

    def respond(request):
        requests.append(request)
        if request.url.path.endswith("/meetings"):
            assert request.url.params["include_transcript"] == "false"
            assert request.url.params["include_summary"] == "false"
            return httpx.Response(
                200,
                json={
                    "items": [
                        {
                            "recording_id": 123,
                            "recording_start_time": "2026-09-08T22:00:00Z",
                        }
                    ]
                },
            )
        return httpx.Response(200, json={"transcript": [{"text": "fixture"}]})

    client = module.SelectedFathom(
        "fixture", "123", "2026-09-08T22:00:00Z", httpx.MockTransport(respond)
    )
    try:
        with pytest.raises(ValueError, match="selected recording"):
            client.fetch({"meeting_id": "456", "started_at": "2026-09-08T22:00:00Z"})
        assert requests == []
        client.fetch({"meeting_id": "123", "started_at": "2026-09-08T22:00:00Z"})
        assert len(requests) == 2
        with pytest.raises(ValueError, match="repeated transcript"):
            client.client.get("recordings/123/transcript")
        assert len(requests) == 2
    finally:
        client.close()


@pytest.mark.parametrize(
    "method,path",
    [
        ("POST", "webhooks"),
        ("DELETE", "webhooks/1"),
        ("GET", "recordings/456/transcript"),
        ("GET", "recordings/123/media"),
    ],
)
def test_unselected_reads_and_all_mutations_blocked(method, path):
    client = module.SelectedFathom(
        "fixture",
        "123",
        "2026-09-08T22:00:00Z",
        httpx.MockTransport(
            lambda _: pytest.fail("Forbidden request reached transport")
        ),
    )
    try:
        with pytest.raises(ValueError):
            client.client.request(method, path)
    finally:
        client.close()


def test_model_transport_always_denied():
    with pytest.raises(RuntimeError, match="not authorized"):
        module.deny_models({})


def test_selected_metadata_lookup_excludes_unrelated_results(monkeypatch):
    monkeypatch.setenv("CB_FATHOM_API_KEY", "fixture")

    def response(request):
        assert request.url.path.endswith("/meetings")
        assert request.url.params["include_transcript"] == "false"
        assert request.url.params["created_after"]
        return httpx.Response(
            200,
            json={
                "items": [
                    {"recording_id": 456, "title": "Unrelated metadata"},
                    {
                        "recording_id": 123,
                        "title": "Selected fixture",
                        "recording_start_time": "2026-09-08T22:00:00Z",
                        "transcript": "MUST NOT RETURN",
                    },
                ]
            },
        )

    result = module.lookup_selected(
        "123",
        "2026-09-08T00:00:00Z",
        "2026-09-10T00:00:00Z",
        httpx.MockTransport(response),
    )
    assert result["recording_id"] == "123" and result["metadata_only"]
    assert "transcript" not in result and "Unrelated" not in str(result)


def test_metadata_lookup_rejects_broad_window_before_network(monkeypatch):
    monkeypatch.setenv("CB_FATHOM_API_KEY", "fixture")
    with pytest.raises(ValueError, match="three days"):
        module.lookup_selected(
            "123",
            "2026-01-01T00:00:00Z",
            "2026-09-10T00:00:00Z",
            httpx.MockTransport(lambda _: pytest.fail("No network allowed")),
        )


def test_call_url_resolves_to_distinct_api_recording_id(monkeypatch):
    monkeypatch.setenv("CB_FATHOM_API_KEY", "fixture")

    def response(request):
        assert request.url.path.endswith("/meetings")
        return httpx.Response(
            200,
            json={
                "items": [
                    {
                        "recording_id": 987,
                        "url": "https://fathom.video/calls/123",
                        "recording_start_time": "2026-09-08T22:00:00Z",
                    }
                ]
            },
        )

    result = module.lookup_selected(
        "123",
        "2026-09-08T00:00:00Z",
        "2026-09-10T00:00:00Z",
        httpx.MockTransport(response),
    )
    assert result["recording_id"] == "987"
    assert result["selected_call_url"] == "https://fathom.video/calls/123"


def test_only_matching_terminal_notifications_can_be_skipped():
    from types import SimpleNamespace
    from uuid import uuid4

    stage_id, job_id = uuid4(), uuid4()
    stage = SimpleNamespace(id=stage_id, job_id=job_id, state="succeeded")
    outbox = SimpleNamespace(stage_id=stage_id, generation=2)
    event = {"schema_version": 1, "job_id": str(job_id), "generation": 2}
    assert module.terminal_duplicate(stage, outbox, event)
    stage.state = "queued"
    assert not module.terminal_duplicate(stage, outbox, event)
    stage.state = "succeeded"
    assert not module.terminal_duplicate(stage, None, event)
    assert not module.terminal_duplicate(
        stage, outbox, {**event, "job_id": str(uuid4())}
    )
    assert not module.terminal_duplicate(stage, outbox, {**event, "generation": 3})
