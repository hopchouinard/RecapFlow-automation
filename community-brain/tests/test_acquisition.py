import json

import httpx
import pytest
from community_brain.jobs.acquisition import Fathom, ZoomCollector


def test_fathom_identity_pagination_and_format():
    seen = []

    def respond(request):
        seen.append(request)
        if "/transcript" in request.url.path:
            return httpx.Response(
                200,
                json={
                    "transcript": [
                        {
                            "speaker": {"display_name": "A"},
                            "timestamp": "00:01:02",
                            "text": "Hello",
                        },
                        {"text": "Unknown speaker"},
                    ]
                },
            )
        if request.url.params.get("cursor"):
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
        return httpx.Response(200, json={"items": [], "next_cursor": "next"})

    client = Fathom("fixture", httpx.MockTransport(respond))
    try:
        assert (
            client.fetch({"meeting_id": "123", "started_at": "2026-09-08T22:00:00Z"})
            == "[00:01:02] A: Hello\n[00:00:00] Unknown: Unknown speaker"
        )
        assert len(seen) == 3 and all(r.headers["X-Api-Key"] == "fixture" for r in seen)
    finally:
        client.close()


def test_fathom_wrong_meeting_never_fetches_transcript():
    def respond(request):
        assert "/transcript" not in request.url.path
        return httpx.Response(
            200,
            json={
                "items": [
                    {
                        "recording_id": 123,
                        "recording_start_time": "2026-09-09T22:00:00Z",
                    }
                ]
            },
        )

    client = Fathom("fixture", httpx.MockTransport(respond))
    try:
        with pytest.raises(ValueError, match="timestamp mismatch"):
            client.fetch({"meeting_id": "123", "started_at": "2026-09-08T22:00:00Z"})
    finally:
        client.close()


def test_collector_scoped_upload_no_raw_content_in_receipt(tmp_path):
    root = tmp_path / "Zoom"
    root.mkdir()
    folder = root / "Meeting"
    folder.mkdir()
    (folder / "chat.txt").write_text("private chat")

    def respond(request):
        assert str(request.url) == "https://backend.example/api/v1/sources"
        assert json.loads(request.content) == {
            "meeting_id": "meeting-123",
            "kind": "chat",
            "content": "private chat",
        }
        return httpx.Response(201, json={"id": "source", "sha256": "hash"})

    collector = ZoomCollector(
        root, "https://backend.example", "fixture", httpx.MockTransport(respond)
    )
    assert collector.listing() == [{"path": "Meeting/chat.txt", "bytes": 12}]
    assert collector.upload("Meeting/chat.txt", "meeting-123") == {
        "id": "source",
        "sha256": "hash",
    }
    assert (folder / "chat.txt").read_text() == "private chat"


@pytest.mark.parametrize(
    "key",
    [
        "../outside.txt",
        "/etc/passwd",
        "child/../../outside.txt",
        "leaf.txt",
        "escape/outside.txt",
    ],
)
def test_collector_rejects_escape_and_symlinks(tmp_path, key):
    root = tmp_path / "Zoom"
    root.mkdir()
    outside = tmp_path / "outside.txt"
    outside.write_text("private")
    (root / "leaf.txt").symlink_to(outside)
    (root / "escape").symlink_to(tmp_path, target_is_directory=True)
    collector = ZoomCollector(root, "https://backend.example", "fixture")
    with pytest.raises((ValueError, OSError)):
        collector.read(key)
    assert collector.listing() == []


def test_collector_rejects_fifo_without_blocking(tmp_path):
    import os

    os.mkfifo(tmp_path / "fifo.txt")
    collector = ZoomCollector(tmp_path, "https://backend.example", "fixture")
    with pytest.raises(ValueError):
        collector.read("fifo.txt")


def test_selected_chat_hash_rejected_before_upload(tmp_path):
    import hashlib

    (tmp_path / "chat.txt").write_text("selected chat")
    requests = []

    def send(request):
        requests.append(request)
        return httpx.Response(200, json={"id": "source"})

    collector = ZoomCollector(
        tmp_path,
        "https://backend.example",
        "fixture",
        transport=httpx.MockTransport(send),
    )
    with pytest.raises(ValueError, match="hash mismatch"):
        collector.upload("chat.txt", "181075701", expected_sha256="0" * 64)
    assert requests == []
    collector.upload(
        "chat.txt",
        "181075701",
        expected_sha256=hashlib.sha256(b"selected chat").hexdigest(),
    )
    assert len(requests) == 1

@pytest.mark.parametrize('offset,allowed', [(-601,False),(-600,True),(-230,True),(600,True),(601,False)])
@pytest.mark.parametrize('meeting', ['821559116','https://fathom.video/calls/821559116'])
def test_call_url_resolution_and_ten_minute_window(offset, allowed, meeting):
    from datetime import datetime, timedelta, timezone
    import importlib.util
    from pathlib import Path
    spec = importlib.util.spec_from_file_location('selected_fathom_case',Path(__file__).resolve().parents[2]/'deploy/community-brain/automatic/selected_fathom.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    start=datetime(2026,9,15,22,tzinfo=timezone.utc);reads=[]
    def respond(request):
        reads.append(request.url.path)
        if request.url.path.endswith('/meetings'):
            return httpx.Response(200,json={'items':[{'recording_id':183401214,'url':'https://fathom.video/calls/821559116','recording_start_time':(start+timedelta(seconds=offset)).isoformat()}]})
        assert allowed and request.url.path.endswith('/recordings/183401214/transcript')
        return httpx.Response(200,json={'transcript':[{'text':'fixture'}]})
    client=module.SelectedFathom('fixture',meeting,start.isoformat(),httpx.MockTransport(respond))
    try:
        identity={'meeting_id':meeting,'started_at':start.isoformat()}
        if allowed:
            assert 'fixture' in client.fetch(identity)
            assert client.resolved_recording=='183401214'
        else:
            with pytest.raises(ValueError,match='timestamp mismatch'):client.fetch(identity)
            assert len(reads)==1
    finally:client.close()
