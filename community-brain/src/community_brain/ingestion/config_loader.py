"""YAML config loader for the ingestion pipeline."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class ChunkingConfig:
    """Chunking tunables (from chunking.yaml `chunking:` section)."""
    schema_version: str
    transcript_segment_max_tokens: int
    post_max_tokens: int
    session_themes_input_max_tokens: int


@dataclass(frozen=True)
class RetryConfig:
    """Retry policy and inter-session delay (from chunking.yaml `extraction:` section)."""
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


def _require_int(d: dict, key: str, filename: str) -> int:
    """Return d[key] as int, raising ValueError if missing or wrong type."""
    val = d[key]
    if not isinstance(val, int) or isinstance(val, bool):
        raise ValueError(
            f"{filename}: '{key}' must be an int, got {type(val).__name__}"
        )
    return val


def _require_str(d: dict, key: str, filename: str) -> str:
    """Return d[key] as str, raising ValueError if missing or wrong type."""
    val = d[key]
    if not isinstance(val, str):
        raise ValueError(
            f"{filename}: '{key}' must be a string, got {type(val).__name__}"
        )
    return val


def load_chunking_config(path: Path) -> tuple[ChunkingConfig, RetryConfig]:
    """Load chunking.yaml and return (ChunkingConfig, RetryConfig).

    Raises:
        FileNotFoundError: if the file does not exist.
        ValueError: if the YAML is missing required keys, has the wrong top-level
            type, or has type-mismatched values (e.g. non-list backoff, non-int
            retry_attempts, backoff list shorter than retry_attempts).
    """
    if not path.exists():
        raise FileNotFoundError(f"Chunking config not found: {path}")
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        raise ValueError(
            f"{path.name}: expected YAML mapping at top level, "
            f"got {type(data).__name__}"
        )
    try:
        chunking = data["chunking"]
        extraction = data["extraction"]
        if not isinstance(chunking, dict):
            raise ValueError(f"{path.name}: 'chunking' must be a mapping")
        if not isinstance(extraction, dict):
            raise ValueError(f"{path.name}: 'extraction' must be a mapping")

        backoff = extraction["retry_backoff_seconds"]
        if not isinstance(backoff, list) or not all(
            isinstance(x, int) and not isinstance(x, bool) for x in backoff
        ):
            raise ValueError(
                f"{path.name}: 'extraction.retry_backoff_seconds' must be a list of ints"
            )
        retry_attempts = extraction["retry_attempts"]
        if not isinstance(retry_attempts, int) or isinstance(retry_attempts, bool):
            raise ValueError(
                f"{path.name}: 'extraction.retry_attempts' must be an int"
            )
        if len(backoff) < retry_attempts:
            raise ValueError(
                f"{path.name}: 'extraction.retry_backoff_seconds' has {len(backoff)} entries "
                f"but retry_attempts is {retry_attempts}; backoff must have at least "
                f"{retry_attempts} entries"
            )

        chunking_config = ChunkingConfig(
            schema_version=_require_str(data, "schema_version", path.name),
            transcript_segment_max_tokens=_require_int(chunking, "transcript_segment_max_tokens", path.name),
            post_max_tokens=_require_int(chunking, "post_max_tokens", path.name),
            session_themes_input_max_tokens=_require_int(chunking, "session_themes_input_max_tokens", path.name),
        )
        retry_config = RetryConfig(
            retry_attempts=retry_attempts,
            retry_backoff_seconds=list(backoff),
            inter_session_delay_seconds=_require_int(extraction, "inter_session_delay_seconds", path.name),
        )
    except (KeyError, TypeError) as exc:
        raise ValueError(
            f"missing or malformed key in {path.name}: "
            f"{exc.args[0] if exc.args else exc}"
        ) from exc
    return chunking_config, retry_config


def load_extraction_config(path: Path) -> ExtractionConfig:
    """Load extraction-config.yaml and return a typed config object.

    Env-var overrides (applied AFTER YAML parse; empty/unset = use YAML):
      - COMMUNITY_BRAIN_SESSION_THEMES_MODEL
      - COMMUNITY_BRAIN_SESSION_THEMES_PROMPT (prompt file name, e.g. session-themes-v2.md)
      - COMMUNITY_BRAIN_CHUNK_EXTRACTION_MODEL
      - COMMUNITY_BRAIN_CHUNK_EXTRACTION_PROMPT (prompt file name)

    Precedence: env var > YAML value. See docs/migrations/CHANGELOG.md for the
    trade-off around changing models mid-corpus without bumping prompt version.

    Raises:
        FileNotFoundError: if the file does not exist.
        ValueError: if the YAML is missing required keys, has the wrong
            top-level type, or has type-mismatched values.
    """
    if not path.exists():
        raise FileNotFoundError(f"Extraction config not found: {path}")
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        raise ValueError(
            f"{path.name}: expected YAML mapping at top level, "
            f"got {type(data).__name__}"
        )
    try:
        session_themes_prompt = _require_str(data["session_themes"], "prompt_file", path.name)
        session_themes_model = _require_str(data["session_themes"], "model", path.name)
        chunk_extraction_prompt = _require_str(data["chunk_extraction"], "prompt_file", path.name)
        chunk_extraction_model = _require_str(data["chunk_extraction"], "model", path.name)
    except (KeyError, TypeError) as exc:
        raise ValueError(
            f"missing or malformed key in {path.name}: "
            f"{exc.args[0] if exc.args else exc}"
        ) from exc

    # Env-var overrides. Empty string = unset = use YAML.
    session_themes_model = os.environ.get("COMMUNITY_BRAIN_SESSION_THEMES_MODEL") or session_themes_model
    session_themes_prompt = os.environ.get("COMMUNITY_BRAIN_SESSION_THEMES_PROMPT") or session_themes_prompt
    chunk_extraction_model = os.environ.get("COMMUNITY_BRAIN_CHUNK_EXTRACTION_MODEL") or chunk_extraction_model
    chunk_extraction_prompt = os.environ.get("COMMUNITY_BRAIN_CHUNK_EXTRACTION_PROMPT") or chunk_extraction_prompt

    return ExtractionConfig(
        session_themes_prompt_file=session_themes_prompt,
        session_themes_model=session_themes_model,
        chunk_extraction_prompt_file=chunk_extraction_prompt,
        chunk_extraction_model=chunk_extraction_model,
    )
