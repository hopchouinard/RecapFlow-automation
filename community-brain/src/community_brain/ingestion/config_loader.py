"""YAML config loader for the ingestion pipeline."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class ChunkingConfig:
    """Chunking and retry tunables (from chunking.yaml)."""
    schema_version: str
    transcript_segment_max_tokens: int
    post_max_tokens: int
    session_themes_input_max_tokens: int
    retry_attempts: int
    retry_backoff_seconds: list[int]
    inter_session_delay_seconds: int


@dataclass(frozen=True)
class ExtractionConfig:
    """Active extraction prompt versions (from extraction-config.yaml)."""
    session_themes_prompt_file: str
    session_themes_model: str
    chunk_extraction_prompt_file: str
    chunk_extraction_model: str


def load_chunking_config(path: Path) -> ChunkingConfig:
    """Load chunking.yaml and return a typed config object."""
    if not path.exists():
        raise FileNotFoundError(f"Chunking config not found: {path}")
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    chunking = data["chunking"]
    extraction = data["extraction"]
    return ChunkingConfig(
        schema_version=data["schema_version"],
        transcript_segment_max_tokens=chunking["transcript_segment_max_tokens"],
        post_max_tokens=chunking["post_max_tokens"],
        session_themes_input_max_tokens=chunking["session_themes_input_max_tokens"],
        retry_attempts=extraction["retry_attempts"],
        retry_backoff_seconds=list(extraction["retry_backoff_seconds"]),
        inter_session_delay_seconds=extraction["inter_session_delay_seconds"],
    )


def load_extraction_config(path: Path) -> ExtractionConfig:
    """Load extraction-config.yaml and return a typed config object."""
    if not path.exists():
        raise FileNotFoundError(f"Extraction config not found: {path}")
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    return ExtractionConfig(
        session_themes_prompt_file=data["session_themes"]["prompt_file"],
        session_themes_model=data["session_themes"]["model"],
        chunk_extraction_prompt_file=data["chunk_extraction"]["prompt_file"],
        chunk_extraction_model=data["chunk_extraction"]["model"],
    )
