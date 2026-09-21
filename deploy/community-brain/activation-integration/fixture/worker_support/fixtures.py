"""Synthetic providers/configuration only; never mounted in production."""

import json
from pathlib import Path
from community_brain.processing.pipeline import CANON


def fake_model(request):
    if request["expect"] == "prep.chunk":
        content = (
            "<!--SEGMENT\ntopic: sample\nspeakers: A\nkeywords: fixture\nsummary: fixture\n-->\n"
            + "A useful substantive sentence. " * 10
        )
    elif request["expect"].startswith("signal."):
        content = "\n\n".join("## " + s + "\nBody" for s in CANON)
    else:
        content = "Plain content"
    return {"choices": [{"message": {"content": content}, "finish_reason": "stop"}]}


def _fake_extract_response(model, prompt, **_kwargs):
    """Distinguish Stage B (themes) from Stage C (chunk metadata) by prompt content."""
    if "SESSION_INPUT:" in prompt:
        return json.dumps({"themes": ["agent frameworks", "embeddings"]})
    return json.dumps(
        {
            "entities": ["LangGraph"],
            "new_entities_seen": [],
            "new_speakers_seen": [],
            "speech_acts": ["comparison"],
            "stance": "positive",
            "certainty": "asserted",
            "chunk_local_markers": ["emphasized"],
            "decisions": [],
            "action_items": [],
            "external_refs": [],
            "references_prior": False,
            # v2 fields required by extractor
            "topic_label": "Agent frameworks comparison",
            "speakers_mentioned": [],
            "keywords": ["LangGraph", "agent", "framework"],
            "has_question": False,
            "has_answer": False,
            "has_unresolved_question": False,
            "has_insight": True,
        }
    )


def _write_min_configs(base: Path) -> Path:
    """Write minimal valid configs to `base` and return its path."""
    base.mkdir(parents=True, exist_ok=True)
    (base / "chunking.yaml").write_text(
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
    (base / "extraction-config.yaml").write_text(
        """
session_themes:
  prompt_file: session-themes-v1.md
  model: test-model
chunk_extraction:
  prompt_file: chunk-extraction-v1.md
  model: test-model
        """,
        encoding="utf-8",
    )
    (base / "speaker-aliases.yaml").write_text(
        'version: "x"\naliases:\n  Alex Rojas: [alexrojas]\npending: []\n',
        encoding="utf-8",
    )
    (base / "entity-registry.yaml").write_text(
        (
            'version: "x"\n'
            "entities:\n"
            "  LangGraph:\n"
            "    type: framework\n"
            "    aliases: [langgraph]\n"
            "pending: []\n"
        ),
        encoding="utf-8",
    )
    prompts = base / "extraction-prompts"
    prompts.mkdir(exist_ok=True)
    (prompts / "session-themes-v1.md").write_text(
        "session themes prompt", encoding="utf-8"
    )
    (prompts / "chunk-extraction-v1.md").write_text(
        "chunk extraction prompt", encoding="utf-8"
    )
    return base


def _mock_ollama_embed(model, input):
    return {"embeddings": [[0.0] * 768 for _ in input]}
