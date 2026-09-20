import hashlib
import json
from types import SimpleNamespace

import pytest
from community_brain.jobs.api import create_app
from community_brain.jobs.archive import MeetingArchive
from community_brain.jobs.auth import Principal
from fastapi.testclient import TestClient


@pytest.fixture
def archive(tmp_path):
    key = "a" * 64
    data = b"# Original\n<script>literal</script>\n"
    (tmp_path / "files").mkdir()
    (tmp_path / "files" / key).write_bytes(data)
    item = {
        "id": key,
        "name": "community-post.md",
        "origin": "output",
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }
    raw = json.dumps(
        {
            "scope": "community",
            "meetings": [{"date": "2025-02-02", "artifacts": [item]}],
        }
    ).encode()
    (tmp_path / "manifest.json").write_bytes(raw)
    return MeetingArchive(tmp_path, hashlib.sha256(raw).hexdigest())


def client(archive):
    principals = {
        "reader": Principal(
            "reader", "community", frozenset(["jobs:read", "artifacts:read"])
        ),
        "other": Principal(
            "reader", "other", frozenset(["jobs:read", "artifacts:read"])
        ),
        "collector": Principal(
            "collector", "community", frozenset(["sources:upload:chat"])
        ),
    }
    return TestClient(
        create_app(SimpleNamespace(), principals.__getitem__, archive=archive)
    )


def test_archive_authentication_scope_and_original_bytes(archive):
    c = client(archive)
    path = "/api/v1/meeting-artifacts/" + "a" * 64 + "/content"
    for url in ["/api/v1/meetings", path]:
        assert c.get(url).status_code == 401
        assert (
            c.get(url, headers={"Authorization": "Bearer collector"}).status_code == 403
        )
        assert c.get(url, headers={"Authorization": "Bearer other"}).status_code == 404
    r = c.get(path, headers={"Authorization": "Bearer reader"})
    assert r.status_code == 200 and r.content == archive.read("a" * 64)
    assert r.headers["x-content-type-options"] == "nosniff"
    assert (
        c.get("/api/v1/meetings", headers={"Authorization": "Bearer reader"}).json()[
            "items"
        ][0]["date"]
        == "2025-02-02"
    )


@pytest.mark.parametrize("corruption", ["changed", "missing", "symlink"])
def test_archive_fails_closed_for_unavailable_or_changed_files(
    archive, corruption, tmp_path
):
    path = archive.root / "files" / ("a" * 64)
    path.unlink()
    if corruption == "changed":
        path.write_bytes(b"changed")
    elif corruption == "symlink":
        other = tmp_path / "other"
        other.write_bytes(b"private")
        path.symlink_to(other)
    r = client(archive).get(
        "/api/v1/meeting-artifacts/" + "a" * 64 + "/content",
        headers={"Authorization": "Bearer reader"},
    )
    assert r.status_code == 409 and "private" not in r.text


def test_manifest_pin_and_unlisted_path_denial(archive):
    with pytest.raises(ValueError):
        MeetingArchive(archive.root, "0" * 64)
    with pytest.raises(KeyError):
        archive.read("../manifest.json")
