"""Tests for the YAML config loader."""

from __future__ import annotations

from pathlib import Path

import pytest

from community_brain.ingestion.config_loader import (
    ChunkingConfig,
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

    config = load_chunking_config(config_file)

    assert isinstance(config, ChunkingConfig)
    assert config.schema_version == "1.0"
    assert config.transcript_segment_max_tokens == 1500
    assert config.post_max_tokens == 2500
    assert config.session_themes_input_max_tokens == 3000
    assert config.retry_attempts == 3
    assert config.retry_backoff_seconds == [2, 8, 32]
    assert config.inter_session_delay_seconds == 30


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
