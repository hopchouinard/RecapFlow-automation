"""RetryConfig threading: pipeline -> Stage B/C -> _call_llm (v5 D14).

Closes the documented v2 TODO in ingestion/pipeline.py. The mock boundary
(extractor._call_llm / session_extractor._call_llm) keeps positional
compatibility: without retry_config the call is exactly (model=, prompt=).
"""
from __future__ import annotations

import json
from unittest.mock import patch

from community_brain.ingestion.config_loader import RetryConfig
from community_brain.ingestion.extractor import extract_chunk_metadata
from community_brain.ingestion.session_extractor import extract_session_themes

RETRY = RetryConfig(
    retry_attempts=5,
    retry_backoff_seconds=[1, 2, 3, 4, 5],
    inter_session_delay_seconds=0,
)


def test_session_extractor_threads_retry_config():
    captured = {}

    def _fake(model, prompt, retries=3, backoff_schedule=None):
        captured["retries"] = retries
        captured["backoff_schedule"] = backoff_schedule
        return json.dumps({"themes": ["a"]})

    with patch(
        "community_brain.ingestion.session_extractor._call_llm", side_effect=_fake
    ):
        res = extract_session_themes(
            input_text="text", model="m", prompt_template="p", retry_config=RETRY
        )
    assert res.status == "success"
    assert captured["retries"] == 5
    assert captured["backoff_schedule"] == [1, 2, 3, 4, 5]


def test_session_extractor_without_retry_config_uses_defaults():
    captured = {}

    def _fake(model, prompt, retries=3, backoff_schedule=None):
        captured["retries"] = retries
        captured["backoff_schedule"] = backoff_schedule
        return json.dumps({"themes": []})

    with patch(
        "community_brain.ingestion.session_extractor._call_llm", side_effect=_fake
    ):
        extract_session_themes(input_text="text", model="m", prompt_template="p")
    assert captured["retries"] == 3
    assert captured["backoff_schedule"] is None


def test_chunk_extractor_threads_retry_config():
    captured = {}

    def _fake(model, prompt, retries=3, backoff_schedule=None):
        captured["retries"] = retries
        captured["backoff_schedule"] = backoff_schedule
        return "not json"  # extraction fails downstream; only threading matters

    with patch("community_brain.ingestion.extractor._call_llm", side_effect=_fake):
        extract_chunk_metadata(
            chunk_text="t",
            entity_registry_names=[],
            speaker_alias_names=[],
            model="m",
            prompt_template="p",
            retry_config=RETRY,
        )
    assert captured["retries"] == 5
    assert captured["backoff_schedule"] == [1, 2, 3, 4, 5]
