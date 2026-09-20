from types import SimpleNamespace

import pytest

from community_brain.jobs import runtime


@pytest.mark.parametrize("configured", [False, True])
def test_worker_manual_input_does_not_require_fathom(monkeypatch, configured):
    for name, value in {
        "CB_ENABLE_MODEL_CALLS": "true",
        "CB_ENABLE_NETWORK_PUBLICATION": "false",
        "CB_OPENROUTER_API_KEY": "fixture",
        "CB_CORPUS_ROOT": "/fixture",
        "CB_PIPELINE_CONFIG_DIR": "/fixture/config",
        "OLLAMA_BASE_URL": "http://fixture.invalid",
        "CB_NATS_URL": "nats://fixture.invalid",
        "CB_NATS_STREAM": "fixture",
        "CB_NATS_SUBJECT": "fixture",
    }.items():
        monkeypatch.setenv(name, value)
    if configured:
        monkeypatch.setenv("CB_FATHOM_API_KEY", "fixture-fathom")
    else:
        monkeypatch.delenv("CB_FATHOM_API_KEY", raising=False)
    # Undo the legacy ingestion environment bridge after main() returns.
    monkeypatch.setenv("OPENROUTER_API_KEY", "before")
    closed = []
    adapter = SimpleNamespace(close=lambda: closed.append(True))
    constructors = []

    def fathom(key):
        constructors.append(key)
        return adapter

    monkeypatch.setattr(runtime, "Fathom", fathom)
    monkeypatch.setattr(runtime, "make_store", lambda: object())
    monkeypatch.setattr(
        runtime,
        "PublicationHandlers",
        lambda *a: SimpleNamespace(indexing=None, git=None, distribution=None),
    )
    served = []

    async def serve(store, worker, *args):
        served.append(worker.fathom)

    monkeypatch.setattr(runtime, "serve", serve)
    runtime.main()
    assert served == [adapter if configured else None]
    assert constructors == (["fixture-fathom"] if configured else [])
    assert closed == ([True] if configured else [])
