"""Paired prompt artifacts must not drift (v5 D15).

docs/inference-guidelines.md is the canonical system-prompt body; the
prompts/ file is the copy-paste deploy artifact whose body must contain
the guidelines verbatim. The v5 grounding rules live in BOTH.
"""
from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

GUIDELINES = REPO_ROOT / "docs" / "inference-guidelines.md"
DEPLOY_ARTIFACT = REPO_ROOT / "prompts" / "community-brain-v4-openwebui-system-prompt.md"


def test_deploy_artifact_embeds_guidelines_verbatim():
    guidelines = GUIDELINES.read_text(encoding="utf-8")
    artifact = DEPLOY_ARTIFACT.read_text(encoding="utf-8")
    assert guidelines.strip() in artifact, (
        "prompts/community-brain-v4-openwebui-system-prompt.md must contain "
        "docs/inference-guidelines.md verbatim — update BOTH in the same commit"
    )


def test_guidelines_contain_v5_grounding_rules():
    guidelines = GUIDELINES.read_text(encoding="utf-8")
    assert "Flagged-unresolved chunks may be surveyed" in guidelines
    assert "never the raw chunk_id" in guidelines
