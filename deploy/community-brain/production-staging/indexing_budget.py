"""Private durable request journal for the approved US$2 lifetime key."""

import hashlib
import json
import os
from contextlib import contextmanager
from pathlib import Path

import httpx
from community_brain import llm


def allowance(key):
    try:
        response = httpx.get(
            "https://openrouter.ai/api/v1/key",
            headers={"Authorization": "Bearer " + key},
            timeout=20,
        )
        response.raise_for_status()
        value = response.json()["data"]
        if not (
            value["limit"] == 2
            and value["limit_reset"] is None
            and 0 < value["limit_remaining"] <= 1.95618285 + 1e-9
            and value["is_management_key"] is False
            and value["include_byok_in_limit"] is True
        ):
            raise ValueError("unexpected allowance")
        return {k: value[k] for k in ("limit", "limit_remaining", "limit_reset")}
    except Exception as exc:
        raise llm.LLMOutcomeUnknown(
            "production allowance uncertain or exhausted"
        ) from exc


@contextmanager
def audited_indexing(store, key, journal_path, ceiling=32):
    """Reopening a previous exercise is forbidden, even after a clean response."""
    if not 1 <= ceiling <= 32:
        raise ValueError("invalid request ceiling")
    original = llm.httpx.post
    count = 0
    journal = Path(journal_path)
    with journal.open("x") as stream:
        os.chmod(journal, 0o600)

        def record(value):
            stream.write(json.dumps(value, sort_keys=True) + "\n")
            stream.flush()
            os.fsync(stream.fileno())

        record({"state": "exercise", "ceiling": ceiling, "lifetime_limit_usd": 2})

        def post(url, **kwargs):
            nonlocal count
            if url != llm.OPENROUTER_URL or count >= ceiling:
                raise llm.LLMOutcomeUnknown(
                    "unexpected endpoint or request ceiling reached"
                )
            remaining = allowance(key)
            count += 1
            record(
                {
                    "state": "intent",
                    "request": count,
                    "allowance": remaining,
                    "model": kwargs["json"]["model"],
                    "request_sha256": hashlib.sha256(
                        json.dumps(kwargs["json"], sort_keys=True).encode()
                    ).hexdigest(),
                }
            )
            try:
                response = original(url, **kwargs)
                response.raise_for_status()
                body = response.json()
                path, sha, _ = store.storage.put(json.dumps(body).encode())
                record(
                    {
                        "state": "response",
                        "request": count,
                        "path": path,
                        "sha256": sha,
                        "usage": body.get("usage"),
                    }
                )
                return response
            except Exception as exc:
                raise llm.LLMOutcomeUnknown(
                    "indexing outcome requires reconciliation"
                ) from exc

        llm.httpx.post = post
        try:
            yield
        finally:
            llm.httpx.post = original
