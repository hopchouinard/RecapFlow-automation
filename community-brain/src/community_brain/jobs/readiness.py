"""Read only the host's public projection; never expose management internals."""

from datetime import datetime, timezone
import json
from pathlib import Path


MAX_AGE_SECONDS = 180
MANAGEMENT_MAX_AGE_SECONDS = 7200
RUNNER_STATES = {
    "idle",
    "worker_running",
    "stage_completed",
    "needs_input",
    "paused",
    "attention_required",
    "awaiting_checkpoint",
    "checking",
}


def fresh(value, now, age):
    try:
        stamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return (
            stamp.utcoffset() is not None
            and -30 <= (now - stamp).total_seconds() <= age
        )
    except (AttributeError, TypeError, ValueError):
        return False


def processing_readiness(root, enabled, *, now=None):
    result = {"state": "unavailable", "ready": False}
    if not enabled:
        return {"state": "disabled", "ready": False}
    if root is None:
        return result
    now = now or datetime.now(timezone.utc)
    try:
        value = json.loads((Path(root) / "checkpoints.json").read_text())["processing"]
        if not isinstance(value, dict) or not fresh(
            value.get("checked_at"), now, MAX_AGE_SECONDS
        ):
            return result
        if any(
            type(value.get(k)) is not bool
            for k in (
                "paused",
                "attention",
                "boot_reconciled",
                "checkpoint_pending",
                "management_attention",
                "credentials_expired",
            )
        ):
            return result
        runner = value.get("runner")
        if runner not in RUNNER_STATES:
            return result
        if (
            value["attention"]
            or value["management_attention"]
            or runner == "attention_required"
        ):
            state = "attention_required"
        elif value["paused"] or not value["boot_reconciled"] or runner == "paused":
            state = "paused"
        elif value["credentials_expired"] or value.get("renewal") == "failed":
            state = "credentials_require_review"
        elif not fresh(
            value.get("management_checked_at"), now, MANAGEMENT_MAX_AGE_SECONDS
        ):
            state = "unavailable"
        elif value.get("renewal") not in {"completed", "not_due"}:
            state = "unavailable"
        elif value["checkpoint_pending"] or runner == "awaiting_checkpoint":
            state = "awaiting_checkpoint"
        elif runner == "needs_input":
            state = "needs_input"
        elif runner in {"worker_running", "stage_completed"}:
            state = "busy"
        elif runner == "idle":
            state = "ready"
        else:
            state = "unavailable"
        return {"state": state, "ready": state in {"ready", "busy"}}
    except (OSError, ValueError, TypeError, KeyError):
        return result
