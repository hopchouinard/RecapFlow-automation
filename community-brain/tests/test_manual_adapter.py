import importlib.util
from pathlib import Path
from types import SimpleNamespace

import lancedb
import pytest


@pytest.fixture
def adapters(monkeypatch):
    root = (
        Path(__file__).resolve().parents[2]
        / "deploy/community-brain/production-staging"
    )
    monkeypatch.syspath_prepend(str(root))
    modules = {}
    for name in ("manual_worker", "manual_host"):
        spec = importlib.util.spec_from_file_location(name, root / f"{name}.py")
        modules[name] = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modules[name])
    return modules


@pytest.mark.parametrize("state", ["partial", "complete"])
def test_index_adapter_covers_new_rows_and_preserves_partial_state(
    tmp_path, adapters, state
):
    table = lancedb.connect(str(tmp_path / "lancedb/nomic-v1")).create_table(
        "chunks", [{"chunk_id": "old", "bm25_text": "preserved fixture"}]
    )
    table.create_fts_index("bm25_text")

    def indexing(job):
        table.add([{"chunk_id": "new", "bm25_text": "new meeting fixture"}])
        return {"state": state, "chunks_failed": int(state == "partial")}

    result = adapters["manual_worker"].complete_fts(
        SimpleNamespace(indexing=indexing), tmp_path, "fixture"
    )
    assert result["state"] == state and result["fts_indexed_rows"] == 2
    fresh = lancedb.connect(str(tmp_path / "lancedb/nomic-v1")).open_table("chunks")
    assert fresh.index_stats("bm25_text_idx")["num_unindexed_rows"] == 0
    assert fresh.search("new", query_type="fts").to_list()[0]["chunk_id"] == "new"


def test_api_staging_refuses_broad_collector_and_extra_permissions(adapters):
    import json

    host = adapters["manual_host"]
    identities = [
        {"subject": subject, "scope": "community-brain", "permissions": sorted(perms)}
        for subject, perms in host.PERMISSIONS.items()
    ]
    host.validate_identities({"CB_SERVICE_IDENTITIES": json.dumps(identities)})
    identities[0]["permissions"] = ["sources:upload"]
    with pytest.raises(AssertionError):
        host.validate_identities({"CB_SERVICE_IDENTITIES": json.dumps(identities)})


def test_processing_ceiling_stops_before_provider(adapters, monkeypatch):
    module = adapters["manual_worker"]
    monkeypatch.setattr(
        module.OpenRouter, "__call__", lambda *args: pytest.fail("provider called")
    )
    provider = module.ManualProvider("fixture")
    provider.calls = 20
    with pytest.raises(module.OutcomeUnknown, match="ceiling"):
        provider({})


def test_selected_fathom_metadata_only_and_exactly_one_transcript(adapters):
    import httpx

    requests = []

    def respond(request):
        requests.append(request)
        if request.url.path.endswith("/meetings"):
            assert all(
                request.url.params[name] == "false"
                for name in (
                    "include_transcript",
                    "include_summary",
                    "include_action_items",
                )
            )
            return httpx.Response(
                200,
                json={
                    "items": [
                        {
                            "recording_id": "181075701",
                            "recording_start_time": "2026-09-08T21:54:33Z",
                        }
                    ]
                },
            )
        assert request.url.path.endswith("/recordings/181075701/transcript")
        return httpx.Response(
            200,
            json={
                "transcript": [
                    {
                        "speaker": {"display_name": "Fixture"},
                        "timestamp": "00:00:00",
                        "text": "Synthetic test",
                    }
                ]
            },
        )

    client = adapters["manual_worker"].SelectedFathom(
        "fixture", "181075701", "2026-09-08T21:54:33Z", httpx.MockTransport(respond)
    )
    try:
        identity = {"meeting_id": "181075701", "started_at": "2026-09-08T21:54:33Z"}
        assert "Synthetic test" in client.fetch(identity)
        with pytest.raises(ValueError, match="already requested"):
            client.fetch(identity)
        with pytest.raises(ValueError, match="mismatch"):
            client.fetch({**identity, "meeting_id": "other"})
        assert sum(r.url.path.endswith("/transcript") for r in requests) == 1
    finally:
        client.close()
