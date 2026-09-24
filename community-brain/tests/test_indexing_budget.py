import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace

import httpx
import pytest
from community_brain.jobs.storage import Storage
from community_brain.llm import LLMOutcomeUnknown

spec = importlib.util.spec_from_file_location(
    "indexing_budget",
    Path(__file__).resolve().parents[2]
    / "deploy/community-brain/production-staging/indexing_budget.py",
)
budget = importlib.util.module_from_spec(spec)
spec.loader.exec_module(budget)


def test_uncertain_request_persists_intent_and_cannot_reopen(tmp_path, monkeypatch):
    monkeypatch.setattr(budget, "allowance", lambda key: {"limit_remaining": 1})

    def lost(*args, **kwargs):
        raise httpx.ReadTimeout("simulated")

    monkeypatch.setattr(budget.httpx, "post", lost)
    journal = tmp_path / "journal.jsonl"
    store = SimpleNamespace(storage=Storage(tmp_path / "files"))
    with (
        budget.audited_indexing(store, "fixture", journal),
        pytest.raises(LLMOutcomeUnknown),
    ):
        budget.httpx.post(budget.llm.OPENROUTER_URL, json={"model": "fixture"})
    assert [json.loads(line)["state"] for line in journal.read_text().splitlines()] == [
        "exercise",
        "intent",
    ]
    assert budget.httpx.post is lost
    with (
        pytest.raises(FileExistsError),
        budget.audited_indexing(store, "fixture", journal),
    ):
        pytest.fail("must not reopen")


def test_ceiling_and_durable_response(tmp_path, monkeypatch):
    monkeypatch.setattr(budget, "allowance", lambda key: {"limit_remaining": 1})
    monkeypatch.setattr(
        budget.httpx,
        "post",
        lambda *a, **kw: SimpleNamespace(
            raise_for_status=lambda: None, json=lambda: {"usage": {"cost": 0.01}}
        ),
    )
    store = SimpleNamespace(storage=Storage(tmp_path / "files"))
    journal = tmp_path / "journal.jsonl"
    with budget.audited_indexing(store, "fixture", journal, ceiling=1):
        budget.httpx.post(budget.llm.OPENROUTER_URL, json={"model": "fixture"})
        with pytest.raises(LLMOutcomeUnknown, match="ceiling"):
            budget.httpx.post(budget.llm.OPENROUTER_URL, json={"model": "fixture"})
    rows = [json.loads(line) for line in journal.read_text().splitlines()]
    assert len(rows) == 3
    assert (
        json.loads(store.storage.read(rows[2]["path"], rows[2]["sha256"]))["usage"][
            "cost"
        ]
        == 0.01
    )


@pytest.mark.parametrize("remaining,limit", [(2, 2), (0, 2), (1, 5)])
def test_allowance_cannot_reset_raise_or_exhaust_cap(monkeypatch, remaining, limit):
    monkeypatch.setattr(
        budget.httpx,
        "get",
        lambda *a, **kw: SimpleNamespace(
            raise_for_status=lambda: None,
            json=lambda: {
                "data": {
                    "limit": limit,
                    "limit_remaining": remaining,
                    "limit_reset": None,
                    "is_management_key": False,
                    "include_byok_in_limit": True,
                }
            },
        ),
    )
    with pytest.raises(LLMOutcomeUnknown):
        budget.allowance("fixture")
