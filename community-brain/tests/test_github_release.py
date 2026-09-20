import httpx
import pytest

from community_brain.jobs.github_release import GitHubRelease
from community_brain.jobs.storage import digest
from community_brain.processing.pipeline import OutcomeUnknown, PipelineFailure


def test_failed_upload_stays_draft_then_retry_reconciles_assets(tmp_path):
    for name in ("corpus-vfixture.tar.gz", "corpus-manifest.json", "sha256sum.txt"):
        (tmp_path / name).write_text(name)
    release = {
        "id": 123,
        "tag_name": "vfixture",
        "target_commitish": "a" * 40,
        "draft": True,
        "assets": [],
    }
    failed = []
    uploaded = []
    published = []

    def respond(request):
        if request.method == "GET":
            return httpx.Response(200, json=release)
        if request.url.host == "uploads.github.com":
            name = request.url.params["name"]
            if len(uploaded) == 1 and not failed:
                failed.append(True)
                return httpx.Response(503)
            uploaded.append(name)
            asset = {
                "name": name,
                "digest": "sha256:" + digest(request.content),
                "id": len(uploaded),
            }
            release["assets"].append(asset)
            return httpx.Response(201, json=asset)
        if request.method == "PATCH":
            published.append(True)
            release["draft"] = False
            return httpx.Response(200, json=release)
        raise AssertionError("unexpected release creation")

    publisher = GitHubRelease(
        "fixture/distribution", "a" * 40, "fixture", httpx.MockTransport(respond)
    )
    try:
        with pytest.raises(OutcomeUnknown):
            publisher.publish(tmp_path, "vfixture")
        assert release["draft"] and not published
        receipt = publisher.publish(tmp_path, "vfixture")
        assert (
            receipt["release_id"] == 123 and len(uploaded) == 3 and len(published) == 1
        )
        publisher.publish(tmp_path, "vfixture")
        assert len(uploaded) == 3 and len(published) == 1
        (tmp_path / "sha256sum.txt").write_text("different")
        with pytest.raises(PipelineFailure, match="asset_conflict"):
            publisher.publish(tmp_path, "vfixture")
    finally:
        publisher.close()


@pytest.mark.parametrize("invalid", ["missing", "extra", "symlink"])
def test_invalid_local_assets_rejected_before_any_network(tmp_path, invalid):
    for name in ("corpus-vfixture.tar.gz", "corpus-manifest.json", "sha256sum.txt"):
        (tmp_path / name).write_text("fixture")
    if invalid == "missing":
        (tmp_path / "sha256sum.txt").unlink()
    elif invalid == "extra":
        (tmp_path / "private.txt").write_text("must not upload")
    else:
        (tmp_path / "sha256sum.txt").unlink()
        (tmp_path / "sha256sum.txt").symlink_to(tmp_path / "corpus-manifest.json")

    def forbidden(_):
        pytest.fail("local validation must precede remote operations")

    publisher = GitHubRelease(
        "fixture/distribution", "a" * 40, "fixture", httpx.MockTransport(forbidden)
    )
    try:
        with pytest.raises(PipelineFailure, match="invalid_release_assets"):
            publisher.publish(tmp_path, "vfixture")
    finally:
        publisher.close()


def test_final_remote_state_must_confirm_published_release(tmp_path):
    for name in ("corpus-vfixture.tar.gz", "corpus-manifest.json", "sha256sum.txt"):
        (tmp_path / name).write_text(name)
    release = {
        "id": 1,
        "tag_name": "vfixture",
        "target_commitish": "a" * 40,
        "draft": True,
        "assets": [
            {"name": p.name, "digest": "sha256:" + digest(p.read_bytes())}
            for p in tmp_path.iterdir()
        ],
    }

    def respond(request):
        # Simulate a publish acknowledgement whose final read still shows draft.
        return httpx.Response(200, json=release)

    publisher = GitHubRelease(
        "fixture/distribution", "a" * 40, "fixture", httpx.MockTransport(respond)
    )
    try:
        with pytest.raises(OutcomeUnknown, match="identity requires reconciliation"):
            publisher.publish(tmp_path, "vfixture")
    finally:
        publisher.close()


def test_existing_tag_commit_is_authoritative_over_release_branch_label(tmp_path):
    for name in ("corpus-vfixture.tar.gz", "corpus-manifest.json", "sha256sum.txt"):
        (tmp_path / name).write_text(name)
    release = {
        "id": 1,
        "tag_name": "vfixture",
        "target_commitish": "main",
        "draft": False,
        "assets": [
            {"name": p.name, "digest": "sha256:" + digest(p.read_bytes())}
            for p in tmp_path.iterdir()
        ],
    }

    def read_only(request):
        assert request.method == "GET"
        return httpx.Response(200, json=release)

    publisher = GitHubRelease(
        "fixture/distribution",
        "a" * 40,
        "fixture",
        httpx.MockTransport(read_only),
        tag_verifier=lambda _: "a" * 40,
    )
    try:
        assert publisher.publish(tmp_path, "vfixture")["commit"] == "a" * 40
        publisher.tag_verifier = lambda _: "b" * 40
        with pytest.raises(PipelineFailure, match="commit_conflict"):
            publisher.publish(tmp_path, "vfixture")
    finally:
        publisher.close()
