"""Tests for the YAML config loader."""

from __future__ import annotations

from pathlib import Path

import pytest

from community_brain.ingestion.config_loader import (
    ExtractionConfig,
    load_chunking_config,
    load_extraction_config,
)


def test_load_chunking_config_from_yaml(tmp_path: Path) -> None:
    config_file = tmp_path / "chunking.yaml"
    config_file.write_text(
        """
schema_version: "1.0"
chunking:
  transcript_segment_max_tokens: 1500
  post_max_tokens: 2500
  session_themes_input_max_tokens: 3000
extraction:
  retry_attempts: 3
  retry_backoff_seconds: [2, 8, 32]
  inter_session_delay_seconds: 30
        """,
        encoding="utf-8",
    )

    chunking, retry = load_chunking_config(config_file)

    assert chunking.schema_version == "1.0"
    assert chunking.transcript_segment_max_tokens == 1500
    assert chunking.post_max_tokens == 2500
    assert chunking.session_themes_input_max_tokens == 3000

    assert retry.retry_attempts == 3
    assert retry.retry_backoff_seconds == [2, 8, 32]
    assert retry.inter_session_delay_seconds == 30


def test_load_extraction_config_from_yaml(tmp_path: Path) -> None:
    config_file = tmp_path / "extraction-config.yaml"
    config_file.write_text(
        """
session_themes:
  prompt_file: session-themes-v1.md
  model: google/gemini-3.1-flash-lite-preview
chunk_extraction:
  prompt_file: chunk-extraction-v1.md
  model: google/gemini-3.1-flash-lite-preview
        """,
        encoding="utf-8",
    )

    config = load_extraction_config(config_file)

    assert isinstance(config, ExtractionConfig)
    assert config.session_themes_prompt_file == "session-themes-v1.md"
    assert config.session_themes_model == "google/gemini-3.1-flash-lite-preview"
    assert config.chunk_extraction_prompt_file == "chunk-extraction-v1.md"
    assert config.chunk_extraction_model == "google/gemini-3.1-flash-lite-preview"


def test_load_chunking_config_missing_file_raises(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        load_chunking_config(tmp_path / "does-not-exist.yaml")


def test_load_extraction_config_missing_file_raises(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        load_extraction_config(tmp_path / "does-not-exist.yaml")


def test_load_chunking_config_missing_required_key_raises(tmp_path: Path) -> None:
    config_file = tmp_path / "chunking.yaml"
    config_file.write_text(
        """
schema_version: "1.0"
chunking:
  transcript_segment_max_tokens: 1500
  # post_max_tokens missing on purpose
  session_themes_input_max_tokens: 3000
extraction:
  retry_attempts: 3
  retry_backoff_seconds: [2, 8, 32]
  inter_session_delay_seconds: 30
        """,
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="post_max_tokens"):
        load_chunking_config(config_file)


def test_load_chunking_config_rejects_empty_yaml(tmp_path: Path) -> None:
    path = tmp_path / "chunking.yaml"
    path.write_text("", encoding="utf-8")
    with pytest.raises(ValueError, match="mapping"):
        load_chunking_config(path)


def test_load_chunking_config_rejects_non_dict_top_level(tmp_path: Path) -> None:
    path = tmp_path / "chunking.yaml"
    path.write_text("- just a list\n", encoding="utf-8")
    with pytest.raises(ValueError, match="mapping"):
        load_chunking_config(path)


def test_load_chunking_config_rejects_non_list_backoff(tmp_path: Path) -> None:
    path = tmp_path / "chunking.yaml"
    path.write_text(
        """
schema_version: "1.0"
chunking:
  transcript_segment_max_tokens: 1500
  post_max_tokens: 2500
  session_themes_input_max_tokens: 3000
extraction:
  retry_attempts: 3
  retry_backoff_seconds: "oops"
  inter_session_delay_seconds: 30
        """,
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="retry_backoff_seconds"):
        load_chunking_config(path)


def test_load_chunking_config_rejects_backoff_shorter_than_attempts(tmp_path: Path) -> None:
    path = tmp_path / "chunking.yaml"
    path.write_text(
        """
schema_version: "1.0"
chunking:
  transcript_segment_max_tokens: 1500
  post_max_tokens: 2500
  session_themes_input_max_tokens: 3000
extraction:
  retry_attempts: 5
  retry_backoff_seconds: [2, 8]
  inter_session_delay_seconds: 30
        """,
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="retry_backoff_seconds"):
        load_chunking_config(path)


def test_load_chunking_config_rejects_string_for_int_field(tmp_path: Path) -> None:
    path = tmp_path / "chunking.yaml"
    path.write_text(
        """
schema_version: "1.0"
chunking:
  transcript_segment_max_tokens: "oops"
  post_max_tokens: 2500
  session_themes_input_max_tokens: 3000
extraction:
  retry_attempts: 3
  retry_backoff_seconds: [2, 8, 32]
  inter_session_delay_seconds: 30
        """,
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="transcript_segment_max_tokens"):
        load_chunking_config(path)


def test_load_extraction_config_rejects_int_for_string_field(tmp_path: Path) -> None:
    path = tmp_path / "extraction-config.yaml"
    path.write_text(
        """
session_themes:
  prompt_file: 123
  model: m
chunk_extraction:
  prompt_file: chunk-extraction-v1.md
  model: m
        """,
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="prompt_file"):
        load_extraction_config(path)
