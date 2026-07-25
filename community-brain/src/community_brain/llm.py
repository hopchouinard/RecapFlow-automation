"""Thin OpenRouter API client for LLM calls.

Uses the OpenRouter chat completions endpoint with configurable model.
Default model: google/gemini-3.1-flash-lite-preview
"""

from __future__ import annotations

import json
import logging
import os
import re
import time
from pathlib import Path

import httpx
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "google/gemini-3.1-flash-lite-preview"
CONFIG_DIR = Path(__file__).resolve().parent.parent.parent / "config"


class LLMError(Exception):
    """Raised when an LLM call fails."""


def _get_api_key() -> str | None:
    """Get OpenRouter API key from environment."""
    load_dotenv(CONFIG_DIR / ".env")
    return os.environ.get("OPENROUTER_API_KEY")


def _get_model() -> str:
    """Get LLM model from environment or use default."""
    return os.environ.get("COMMUNITY_BRAIN_LLM_MODEL", DEFAULT_MODEL)


def call_llm(
    prompt: str,
    model: str | None = None,
    retries: int = 3,
    backoff_schedule: list[int] | None = None,
) -> str:
    """Call OpenRouter chat completions API and return the response text.

    Args:
        prompt: The user message to send.
        model: Override the default model.
        retries: Number of retry attempts on failure.
        backoff_schedule: Per-attempt sleep seconds (index = attempt). When
            None, falls back to exponential 2**attempt.

    Returns:
        The assistant's response text.

    Raises:
        LLMError: If the API key is missing or all retries fail.
    """
    api_key = _get_api_key()
    if not api_key:
        raise LLMError("OPENROUTER_API_KEY not set in config/.env")

    if model is None:
        model = _get_model()

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
    }

    for attempt in range(retries):
        try:
            response = httpx.post(
                OPENROUTER_URL,
                headers=headers,
                json=payload,
                timeout=120.0,
            )
            if response.status_code >= 500:
                if attempt < retries - 1:
                    if backoff_schedule is not None and attempt < len(backoff_schedule):
                        backoff = backoff_schedule[attempt]
                    else:
                        backoff = 2 ** attempt
                    logger.warning(
                        "LLM API error %d, retrying in %ds",
                        response.status_code, backoff,
                    )
                    time.sleep(backoff)
                    continue
                raise LLMError(f"LLM API error after {retries} retries: {response.status_code}")

            response.raise_for_status()
            data = response.json()

            usage = data.get("usage", {})
            if usage:
                logger.info(
                    "LLM tokens — input: %d, output: %d",
                    usage.get("prompt_tokens", 0),
                    usage.get("completion_tokens", 0),
                )

            return data["choices"][0]["message"]["content"]

        except httpx.HTTPError as e:
            if attempt < retries - 1:
                if backoff_schedule is not None and attempt < len(backoff_schedule):
                    backoff = backoff_schedule[attempt]
                else:
                    backoff = 2 ** attempt
                logger.warning("LLM request failed (%s), retrying in %ds", e, backoff)
                time.sleep(backoff)
            else:
                raise LLMError(f"LLM request failed after {retries} retries: {e}") from e

    raise LLMError("Exhausted retries")


def call_llm_json(
    prompt: str,
    model: str | None = None,
    retries: int = 3,
) -> list | dict:
    """Call LLM and parse the response as JSON.

    Handles markdown code fences that models sometimes wrap responses in.

    Raises:
        LLMError: If JSON parsing fails after retries.
    """
    text = call_llm(prompt, model=model, retries=retries)

    cleaned = text.strip()
    cleaned = re.sub(r"^```(?:json)?\s*\n?", "", cleaned)
    cleaned = re.sub(r"\n?```\s*$", "", cleaned)
    cleaned = cleaned.strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        raise LLMError(f"Failed to parse LLM response as JSON: {e}\nResponse: {text[:200]}") from e
