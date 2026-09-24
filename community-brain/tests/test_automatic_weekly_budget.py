"""Production weekly policy rejects malformed allowance before any paid request."""
import importlib.util
from pathlib import Path
from types import SimpleNamespace

import httpx
import pytest

ROOT = Path(__file__).resolve().parents[2] / 'deploy/community-brain/automatic'

@pytest.fixture(params=['indexing_budget', 'bounded_worker'])
def guard(request, monkeypatch):
    spec = importlib.util.spec_from_file_location('weekly_' + request.param, ROOT / (request.param + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if request.param == 'bounded_worker':
        monkeypatch.setattr(module.OpenRouter, '__call__', lambda *_: 'paid-request-allowed')
        call = lambda: module.BoundedProvider('fixture')(None)
    else:
        call = lambda: module.allowance('fixture')
    return module, call

def response(guard, monkeypatch, **changes):
    data = dict(limit=5, limit_reset='weekly', limit_remaining=5,
                is_management_key=False, include_byok_in_limit=True)
    data.update(changes)
    monkeypatch.setattr(guard[0].httpx, 'get', lambda *a, **kw:
        SimpleNamespace(raise_for_status=lambda: None, json=lambda: {'data': data}))

@pytest.mark.parametrize('remaining', [5, 4.9, .001])
def test_current_week_and_reset_allowance(guard, monkeypatch, remaining):
    response(guard, monkeypatch, limit_remaining=remaining)
    assert guard[1]()

@pytest.mark.parametrize('changes', [
    {'limit':2, 'limit_reset':None}, {'limit':10}, {'limit':None},
    {'limit_reset':'daily'}, {'limit_reset':'monthly'}, {'limit_reset':None},
    {'limit_remaining':0}, {'limit_remaining':-1}, {'limit_remaining':5.01},
    {'limit_remaining':float('nan')}, {'limit_remaining':float('inf')},
    {'limit_remaining':True}, {'limit_remaining':'5'}, {'limit_remaining':None},
    {'is_management_key':True}, {'include_byok_in_limit':False},
])
def test_policy_mismatch_fails_closed(guard, monkeypatch, changes):
    response(guard, monkeypatch, **changes)
    with pytest.raises((guard[0].llm.LLMOutcomeUnknown if hasattr(guard[0], 'llm') else guard[0].OutcomeUnknown)):
        guard[1]()

def test_provider_failure_fails_closed(guard, monkeypatch):
    def unavailable(*a, **kw): raise httpx.ReadTimeout('fixture')
    monkeypatch.setattr(guard[0].httpx, 'get', unavailable)
    with pytest.raises((guard[0].llm.LLMOutcomeUnknown if hasattr(guard[0], 'llm') else guard[0].OutcomeUnknown)):
        guard[1]()

def test_weekly_reset_does_not_reset_job_request_ceiling(monkeypatch):
    spec = importlib.util.spec_from_file_location('weekly_ceiling', ROOT / 'bounded_worker.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    monkeypatch.setattr(module, 'CEILING', 1)
    monkeypatch.setattr(module.OpenRouter, '__call__', lambda *_: 'allowed')
    provider = module.BoundedProvider('fixture')
    guard = (module, lambda: provider(None))
    response(guard, monkeypatch, limit_remaining=1)
    assert guard[1]() == 'allowed'
    response(guard, monkeypatch, limit_remaining=5)
    with pytest.raises(module.OutcomeUnknown, match='ceiling'):
        guard[1]()

def test_indexing_journal_records_weekly_policy(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location('weekly_journal', ROOT / 'indexing_budget.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    monkeypatch.setattr(module, 'allowance', lambda _: {'limit_remaining':5})
    journal = tmp_path / 'journal.jsonl'
    with module.audited_indexing(SimpleNamespace(), 'fixture', journal):
        pass
    import json
    header = json.loads(journal.read_text().splitlines()[0])
    assert header['limit_usd'] == 5 and header['limit_reset'] == 'weekly'
    assert 'lifetime_limit_usd' not in header
