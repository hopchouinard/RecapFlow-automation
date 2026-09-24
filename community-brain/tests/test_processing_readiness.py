"""Stale or halted automation must not be advertised as ready to process."""

from datetime import datetime, timedelta, timezone
import json

import pytest

from community_brain.jobs.readiness import processing_readiness

NOW = datetime(2026, 9, 20, tzinfo=timezone.utc)


def projection(**changes):
    return {
        "runner": "idle",
        "checked_at": NOW.isoformat(),
        "paused": False,
        "attention": False,
        "boot_reconciled": True,
        "checkpoint_pending": False,
        "management_attention": False,
        "credentials_expired": False,
        "renewal": "not_due",
        "management_checked_at": NOW.isoformat(),
        **changes,
    }


def check(tmp_path, value):
    (tmp_path / "checkpoints.json").write_text(json.dumps({"processing": value}))
    return processing_readiness(tmp_path, True, now=NOW)


@pytest.mark.parametrize(
    "changes,state",
    [
        ({}, "ready"),
        ({"runner": "worker_running"}, "busy"),
        ({"paused": True}, "paused"),
        ({"boot_reconciled": False}, "paused"),
        ({"attention": True}, "attention_required"),
        ({"management_attention": True}, "attention_required"),
        ({"renewal": "failed"}, "credentials_require_review"),
        ({"credentials_expired": True}, "credentials_require_review"),
        ({"checkpoint_pending": True}, "awaiting_checkpoint"),
        ({"runner": "needs_input"}, "needs_input"),
        ({"runner": "checking"}, "unavailable"),
        ({"renewal": "unknown"}, "unavailable"),
    ],
)
def test_current_host_gates(tmp_path, changes, state):
    assert check(tmp_path, projection(**changes)) == {
        "state": state,
        "ready": state in {"ready", "busy"},
    }


@pytest.mark.parametrize(
    "changes",
    [
        {"checked_at": (NOW - timedelta(seconds=181)).isoformat()},
        {"checked_at": (NOW + timedelta(seconds=31)).isoformat()},
        {"checked_at": NOW.replace(tzinfo=None).isoformat()},
        {"management_checked_at": (NOW - timedelta(hours=3)).isoformat()},
        {"boot_reconciled": "true"},
        {"paused": 0},
        {"runner": ["idle"]},
        {"runner": "private arbitrary error"},
        {"checked_at": None},
    ],
)
def test_invalid_or_stale_data_never_reports_ready(tmp_path, changes):
    assert check(tmp_path, projection(**changes)) == {
        "state": "unavailable",
        "ready": False,
    }


def test_missing_projection_and_disabled_mode(tmp_path):
    assert processing_readiness(tmp_path, True, now=NOW)["state"] == "unavailable"
    (tmp_path / "checkpoints.json").write_text("{broken")
    assert processing_readiness(tmp_path, True, now=NOW)["state"] == "unavailable"
    assert processing_readiness(None, False, now=NOW) == {
        "state": "disabled",
        "ready": False,
    }


def test_private_management_details_are_never_returned(tmp_path):
    result = check(
        tmp_path,
        projection(
            attention=True, private_token="do-not-export", error="/private/path"
        ),
    )
    assert result == {"state": "attention_required", "ready": False}
    assert "private" not in json.dumps(result)
