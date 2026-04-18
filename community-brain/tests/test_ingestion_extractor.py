"""Tests for Stage C chunk extraction (LLM mocked)."""

from __future__ import annotations

import json
from unittest.mock import patch

from community_brain.ingestion.extractor import (
    ExtractionResult,
    extract_chunk_metadata,
)


def _mock_llm_response(payload: dict) -> str:
    return json.dumps(payload)


def test_extract_chunk_metadata_success() -> None:
    payload = {
        "entities": ["LangGraph"],
        "new_entities_seen": [],
        "new_speakers_seen": [],
        "speech_acts": ["comparison", "recommendation"],
        "stance": "positive",
        "certainty": "asserted",
        "chunk_local_markers": ["emphasized"],
        "decisions": [],
        "action_items": [],
        "external_refs": ["https://langchain.com/docs/langgraph"],
        "references_prior": False,
    }

    with patch("community_brain.ingestion.extractor._call_llm", return_value=_mock_llm_response(payload)):
        result = extract_chunk_metadata(
            chunk_text="...",
            entity_registry_names=["LangGraph"],
            speaker_alias_names=["Alex Rojas", "Sam"],
            model="google/gemini-3.1-flash-lite-preview",
            prompt_template="...prompt...",
        )

    assert isinstance(result, ExtractionResult)
    assert result.status == "success"
    assert result.entities == ["LangGraph"]
    assert "comparison" in result.speech_acts
    assert result.stance == "positive"
    assert result.certainty == "asserted"
    assert result.external_refs == ["https://langchain.com/docs/langgraph"]
    assert result.error is None


def test_extract_chunk_metadata_invalid_json_marks_failed() -> None:
    with patch("community_brain.ingestion.extractor._call_llm", return_value="not json"):
        result = extract_chunk_metadata(
            chunk_text="...",
            entity_registry_names=[],
            speaker_alias_names=[],
            model="m",
            prompt_template="p",
        )

    assert result.status == "failed"
    assert "json" in (result.error or "").lower()


def test_extract_chunk_metadata_llm_exception_marks_failed() -> None:
    def _raise(*_a, **_k):
        raise RuntimeError("llm unavailable")

    with patch("community_brain.ingestion.extractor._call_llm", side_effect=_raise):
        result = extract_chunk_metadata(
            chunk_text="...",
            entity_registry_names=[],
            speaker_alias_names=[],
            model="m",
            prompt_template="p",
        )

    assert result.status == "failed"
    assert "llm unavailable" in (result.error or "")


def test_extract_chunk_metadata_strips_markdown_code_fences() -> None:
    """LLMs sometimes wrap JSON in ```json ... ``` fences; the extractor must handle that."""
    payload = {
        "entities": ["X"],
        "new_entities_seen": [],
        "new_speakers_seen": [],
        "speech_acts": [],
        "stance": None,
        "certainty": "asserted",
        "chunk_local_markers": [],
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
    }
    fenced = f"```json\n{json.dumps(payload)}\n```"
    with patch("community_brain.ingestion.extractor._call_llm", return_value=fenced):
        result = extract_chunk_metadata(
            chunk_text="...",
            entity_registry_names=["X"],
            speaker_alias_names=[],
            model="m",
            prompt_template="p",
        )
    assert result.status == "success"
    assert result.entities == ["X"]


def test_extract_chunk_metadata_missing_fields_filled_with_defaults() -> None:
    """LLM returns partial JSON; extractor fills missing fields with safe defaults."""
    payload = {"entities": ["X"]}
    with patch("community_brain.ingestion.extractor._call_llm", return_value=_mock_llm_response(payload)):
        result = extract_chunk_metadata(
            chunk_text="...",
            entity_registry_names=["X"],
            speaker_alias_names=[],
            model="m",
            prompt_template="p",
        )
    assert result.status == "success"
    assert result.entities == ["X"]
    assert result.speech_acts == []
    assert result.stance is None
    assert result.certainty == "asserted"
    assert result.chunk_local_markers == []
    assert result.decisions == []
    assert result.action_items == []
    assert result.external_refs == []
    assert result.references_prior is False


def test_extract_chunk_metadata_prompt_includes_context() -> None:
    """The prompt sent to the LLM includes the chunk text, entities, speakers."""
    captured: dict[str, str] = {}

    def _capture(model: str, prompt: str) -> str:
        captured["model"] = model
        captured["prompt"] = prompt
        return json.dumps({
            "entities": [],
            "new_entities_seen": [],
            "new_speakers_seen": [],
            "speech_acts": [],
            "stance": None,
            "certainty": "asserted",
            "chunk_local_markers": [],
            "decisions": [],
            "action_items": [],
            "external_refs": [],
            "references_prior": False,
        })

    with patch("community_brain.ingestion.extractor._call_llm", side_effect=_capture):
        extract_chunk_metadata(
            chunk_text="the chunk body content",
            entity_registry_names=["LangGraph", "Codex"],
            speaker_alias_names=["Alex Rojas"],
            model="test-model",
            prompt_template="SYSTEM PROMPT TEMPLATE",
        )

    assert captured["model"] == "test-model"
    assert "SYSTEM PROMPT TEMPLATE" in captured["prompt"]
    assert "the chunk body content" in captured["prompt"]
    assert "LangGraph" in captured["prompt"]
    assert "Alex Rojas" in captured["prompt"]


def test_extract_chunk_metadata_invalid_stance_defaults_to_none() -> None:
    payload = {
        "entities": [],
        "new_entities_seen": [],
        "new_speakers_seen": [],
        "speech_acts": [],
        "stance": "feral",  # not a valid Literal value
        "certainty": "asserted",
        "chunk_local_markers": [],
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
    }
    with patch(
        "community_brain.ingestion.extractor._call_llm",
        return_value=_mock_llm_response(payload),
    ):
        result = extract_chunk_metadata(
            chunk_text="x",
            entity_registry_names=[],
            speaker_alias_names=[],
            model="m",
            prompt_template="p",
        )
    assert result.status == "success"
    assert result.stance is None


def test_extract_chunk_metadata_invalid_certainty_defaults_to_asserted() -> None:
    payload = {
        "entities": [],
        "new_entities_seen": [],
        "new_speakers_seen": [],
        "speech_acts": [],
        "stance": None,
        "certainty": "dubious",
        "chunk_local_markers": [],
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
    }
    with patch(
        "community_brain.ingestion.extractor._call_llm",
        return_value=_mock_llm_response(payload),
    ):
        result = extract_chunk_metadata(
            chunk_text="x",
            entity_registry_names=[],
            speaker_alias_names=[],
            model="m",
            prompt_template="p",
        )
    assert result.status == "success"
    assert result.certainty == "asserted"


def test_extract_chunk_metadata_empty_chunk_text() -> None:
    """Empty chunk_text should still be parseable — edge case that can happen
    if the chunker changes in the future or a malformed artifact slips through."""
    payload = {
        "entities": [],
        "new_entities_seen": [],
        "new_speakers_seen": [],
        "speech_acts": [],
        "stance": None,
        "certainty": "asserted",
        "chunk_local_markers": [],
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
    }
    with patch("community_brain.ingestion.extractor._call_llm", return_value=_mock_llm_response(payload)):
        result = extract_chunk_metadata(
            chunk_text="",
            entity_registry_names=[],
            speaker_alias_names=[],
            model="m",
            prompt_template="p",
        )
    assert result.status == "success"
