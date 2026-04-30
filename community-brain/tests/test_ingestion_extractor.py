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


def _v2_defaults() -> dict:
    """Minimal v2 required fields to include in test payloads."""
    return {
        "topic_label": "Test topic",
        "speakers_mentioned": [],
        "keywords": [],
        "has_question": False,
        "has_answer": False,
        "has_unresolved_question": False,
        "has_insight": False,
    }


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
        **_v2_defaults(),
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
        **_v2_defaults(),
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
    """LLM returns minimal JSON with only v2 required booleans; optional list/string
    fields are absent and the extractor fills them with safe defaults."""
    payload = {"entities": ["X"], **_v2_defaults()}
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
            **_v2_defaults(),
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
        **_v2_defaults(),
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
        **_v2_defaults(),
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
        **_v2_defaults(),
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


def test_extract_chunk_metadata_rejects_non_list_entities() -> None:
    payload = {
        "entities": "not a list",  # wrong type
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
    assert result.status == "failed"
    assert "entities" in (result.error or "").lower()


def test_extract_chunk_metadata_rejects_string_references_prior() -> None:
    """The LLM must return a real bool, not a string like 'false' which
    would truthy-convert to True."""
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
        "references_prior": "false",  # string, not bool
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
    assert result.status == "failed"
    assert "references_prior" in (result.error or "")


# ---------------------------------------------------------------------------
# v2 contract tests
# ---------------------------------------------------------------------------

def test_extractor_v2_parses_response_with_new_fields() -> None:
    """v2 LLM response shape includes topic_label, speakers_mentioned,
    keywords, and has_* flags. Extractor parses without error."""
    v2_payload = {
        "topic_label": "Sales funnel optimization",
        "entities": ["Adam James", "Gold Flamingo", "LinkedIn"],
        "speakers_mentioned": ["Andrej Karpathy"],
        "keywords": ["funnel", "outreach", "law firms"],
        "speech_acts": ["question", "recommendation"],
        "stance": "positive",
        "certainty": "asserted",
        "chunk_local_markers": ["emphasized"],
        "decisions": [],
        "action_items": ["Adam will draft a sample funnel by Friday"],
        "external_refs": [],
        "references_prior": False,
        "has_question": True,
        "has_answer": False,
        "has_unresolved_question": True,
        "has_insight": True,
    }
    with patch(
        "community_brain.ingestion.extractor._call_llm",
        return_value=_mock_llm_response(v2_payload),
    ):
        result = extract_chunk_metadata(
            chunk_text="Adam discussed his sales funnel approach.",
            entity_registry_names=[],
            speaker_alias_names=[],
            model="test-model",
            prompt_template="test prompt: {CHUNK_TEXT}",
        )
    assert result.status == "success"
    assert result.topic_label == "Sales funnel optimization"
    assert "Adam James" in result.entities
    assert result.speakers_mentioned == ["Andrej Karpathy"]
    assert "funnel" in result.keywords
    assert result.has_question is True
    assert result.has_answer is False
    assert result.has_unresolved_question is True
    assert result.has_insight is True


def test_extractor_v2_response_without_new_entities_seen_succeeds() -> None:
    """v2 response shape drops new_entities_seen / new_speakers_seen.
    The extractor must NOT raise on their absence."""
    v2_payload = {
        "topic_label": "Topic",
        "entities": [],
        "speakers_mentioned": [],
        "keywords": [],
        "speech_acts": [],
        "stance": None,
        "certainty": "asserted",
        "chunk_local_markers": [],
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
        "has_question": False,
        "has_answer": False,
        "has_unresolved_question": False,
        "has_insight": False,
    }
    with patch(
        "community_brain.ingestion.extractor._call_llm",
        return_value=_mock_llm_response(v2_payload),
    ):
        result = extract_chunk_metadata(
            chunk_text="content",
            entity_registry_names=[],
            speaker_alias_names=[],
            model="test-model",
            prompt_template="test: {CHUNK_TEXT}",
        )
    assert result.status == "success"
    # pipeline.py compat: removed fields default to empty list
    assert result.new_entities_seen == []
    assert result.new_speakers_seen == []


def test_extractor_v2_missing_required_field_fails() -> None:
    """If the v2 response is missing one of the new required fields
    (e.g., has_question), the extractor should report status=failed."""
    incomplete = {
        "topic_label": "Topic",
        "entities": [],
        "speakers_mentioned": [],
        "keywords": [],
        "speech_acts": [],
        "stance": None,
        "certainty": "asserted",
        "chunk_local_markers": [],
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
        # has_question intentionally missing
        "has_answer": False,
        "has_unresolved_question": False,
        "has_insight": False,
    }
    with patch(
        "community_brain.ingestion.extractor._call_llm",
        return_value=_mock_llm_response(incomplete),
    ):
        result = extract_chunk_metadata(
            chunk_text="content",
            entity_registry_names=[],
            speaker_alias_names=[],
            model="test-model",
            prompt_template="test: {CHUNK_TEXT}",
        )
    assert result.status == "failed"
    assert "has_question" in (result.error or "")


# ---------------------------------------------------------------------------
# HIGH 2 — required v2 string/list field validation
# ---------------------------------------------------------------------------

def test_extractor_v2_missing_topic_label_fails() -> None:
    """LLM response missing topic_label must produce status=failed."""
    payload = {
        # topic_label intentionally omitted
        "entities": [],
        "speakers_mentioned": [],
        "keywords": ["x"],
        "speech_acts": [],
        "stance": None,
        "certainty": "asserted",
        "chunk_local_markers": [],
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
        "has_question": False,
        "has_answer": False,
        "has_unresolved_question": False,
        "has_insight": False,
    }
    with patch(
        "community_brain.ingestion.extractor._call_llm",
        return_value=_mock_llm_response(payload),
    ):
        result = extract_chunk_metadata(
            chunk_text="content",
            entity_registry_names=[],
            speaker_alias_names=[],
            model="test-model",
            prompt_template="test",
        )
    assert result.status == "failed"
    assert "topic_label" in (result.error or "")


def test_extractor_v2_missing_speakers_mentioned_fails() -> None:
    """LLM response missing speakers_mentioned must produce status=failed."""
    payload = {
        "topic_label": "Some topic",
        "entities": [],
        # speakers_mentioned intentionally omitted
        "keywords": ["x"],
        "speech_acts": [],
        "stance": None,
        "certainty": "asserted",
        "chunk_local_markers": [],
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
        "has_question": False,
        "has_answer": False,
        "has_unresolved_question": False,
        "has_insight": False,
    }
    with patch(
        "community_brain.ingestion.extractor._call_llm",
        return_value=_mock_llm_response(payload),
    ):
        result = extract_chunk_metadata(
            chunk_text="content",
            entity_registry_names=[],
            speaker_alias_names=[],
            model="test-model",
            prompt_template="test",
        )
    assert result.status == "failed"
    assert "speakers_mentioned" in (result.error or "")


def test_extractor_v2_missing_keywords_fails() -> None:
    """LLM response missing keywords must produce status=failed."""
    payload = {
        "topic_label": "Some topic",
        "entities": [],
        "speakers_mentioned": [],
        # keywords intentionally omitted
        "speech_acts": [],
        "stance": None,
        "certainty": "asserted",
        "chunk_local_markers": [],
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
        "has_question": False,
        "has_answer": False,
        "has_unresolved_question": False,
        "has_insight": False,
    }
    with patch(
        "community_brain.ingestion.extractor._call_llm",
        return_value=_mock_llm_response(payload),
    ):
        result = extract_chunk_metadata(
            chunk_text="content",
            entity_registry_names=[],
            speaker_alias_names=[],
            model="test-model",
            prompt_template="test",
        )
    assert result.status == "failed"
    assert "keywords" in (result.error or "")


# ---------------------------------------------------------------------------
# MEDIUM — speakers_spoke exclusion
# ---------------------------------------------------------------------------

def test_extractor_speakers_spoke_passed_in_prompt() -> None:
    """speakers_spoke names passed to extract_chunk_metadata must appear in
    the SPEAKERS_SPOKE block sent to the LLM, so the model can exclude them
    from speakers_mentioned."""
    captured: dict[str, str] = {}

    def _capture(model: str, prompt: str) -> str:
        captured["prompt"] = prompt
        return json.dumps({
            "topic_label": "Test",
            "entities": ["Adam James"],
            "speakers_mentioned": [],  # Adam excluded because he's in speakers_spoke
            "keywords": ["test"],
            "speech_acts": [],
            "stance": None,
            "certainty": "asserted",
            "chunk_local_markers": [],
            "decisions": [],
            "action_items": [],
            "external_refs": [],
            "references_prior": False,
            "has_question": False,
            "has_answer": False,
            "has_unresolved_question": False,
            "has_insight": False,
        })

    with patch("community_brain.ingestion.extractor._call_llm", side_effect=_capture):
        result = extract_chunk_metadata(
            chunk_text="Adam James described the sales approach.",
            entity_registry_names=["Adam James"],
            speaker_alias_names=["Adam James"],
            model="test-model",
            prompt_template="test prompt",
            speakers_spoke=["Adam James"],
        )

    assert result.status == "success"
    # SPEAKERS_SPOKE block must appear in the prompt sent to the LLM
    assert "SPEAKERS_SPOKE" in captured["prompt"]
    assert "Adam James" in captured["prompt"]
    # The mock response puts Adam in entities but NOT in speakers_mentioned
    # (simulating correct model behaviour given the prompt context)
    assert "Adam James" in result.entities
    assert "Adam James" not in (result.speakers_mentioned or [])
