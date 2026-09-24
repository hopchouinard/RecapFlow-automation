"""Approved exclusions must never broaden to substantive or successful rows."""

import hashlib
import importlib.util
import sys
from pathlib import Path

import pytest

scripts = (
    Path(__file__).resolve().parents[2] / "deploy/community-brain/preserved-rehearsal"
)
sys.path.insert(0, str(scripts))
try:
    spec = importlib.util.spec_from_file_location(
        "build_preserved_candidate", scripts / "build_candidate.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
finally:
    sys.path.pop(0)


def data():
    rows = [
        {
            "chunk_id": str(i),
            "session_id": "2026-05-05",
            "content_type": "prepared_transcript",
            "extraction_status": "failed",
            "full_text": "---",
        }
        for i in range(13)
    ]
    approved = [
        {
            "chunk_id": r["chunk_id"],
            "session_id": r["session_id"],
            "full_text_sha256": hashlib.sha256(b"---").hexdigest(),
        }
        for r in rows
    ]
    return rows, approved


def test_only_exact_failed_dividers_selected():
    rows, approved = data()
    successful = {**rows[0], "chunk_id": "keep", "extraction_status": "success"}
    assert module.validate_exclusions(rows + [successful], approved) == rows


@pytest.mark.parametrize("change", ["text", "id", "session", "status", "type"])
def test_refuses_exclusion_drift(change):
    rows, approved = data()
    key, value = {
        "text": ("full_text", "Meeting content"),
        "id": ("chunk_id", "unapproved"),
        "session": ("session_id", "2026-06-01"),
        "status": ("extraction_status", "success"),
        "type": ("content_type", "community_post"),
    }[change]
    rows[0][key] = value
    with pytest.raises(AssertionError):
        module.validate_exclusions(rows, approved)
