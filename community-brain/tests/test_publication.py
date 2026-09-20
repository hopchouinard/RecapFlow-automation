from pathlib import Path
import subprocess

import pytest

from community_brain.jobs.publication import build_bundle, validate_bundle
from community_brain.processing.pipeline import PipelineFailure

ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture
def corpus(tmp_path):
    path = tmp_path / "fixture"
    subprocess.run(
        [str(ROOT / "scripts/build-distribution-fixture.sh"), str(path)],
        check=True,
        capture_output=True,
        timeout=60,
    )
    return path / "lancedb/nomic-v1"


def test_consumer_package_roundtrip_and_determinism(corpus, tmp_path):
    a = build_bundle(corpus, tmp_path / "a", "vfixture", "2026-09-09T00:00:00Z")
    b = build_bundle(corpus, tmp_path / "b", "vfixture", "2026-09-09T00:00:00Z")
    assert a == b
    assert a["session_count"] == 2 and a["chunk_count"] == 3
    assert validate_bundle(tmp_path / "a") == a
    archive = tmp_path / "a/corpus-vfixture.tar.gz"
    archive.write_bytes(archive.read_bytes() + b"corruption")
    with pytest.raises(PipelineFailure, match="checksum"):
        validate_bundle(tmp_path / "a")


def test_no_overwrite_of_candidate(corpus, tmp_path):
    build_bundle(corpus, tmp_path / "a", "vfixture", "2026-09-09T00:00:00Z")
    with pytest.raises(PipelineFailure, match="immutable_release_conflict"):
        build_bundle(corpus, tmp_path / "a", "vfixture", "2026-09-09T00:00:00Z")


def test_disabled_publication_rejects_injected_publisher_before_work(tmp_path):
    from community_brain.jobs.publication import PublicationHandlers

    class Publisher:
        def publish(self, *args):
            pytest.fail("disabled publication must never contact publisher")

    handler = PublicationHandlers(
        None,
        tmp_path,
        tmp_path,
        "http://unused.invalid",
        allow_network_publish=False,
        release_publisher=Publisher(),
    )
    with pytest.raises(PipelineFailure, match="network_publication_not_enabled"):
        handler.distribution("fixture")
    assert not (tmp_path / "releases").exists()
