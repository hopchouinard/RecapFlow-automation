from types import SimpleNamespace
from unittest.mock import patch

import pytest
from community_brain.ingestion.extractor import extract_chunk_metadata
from community_brain.ingestion.session_extractor import extract_session_themes
from community_brain.jobs.publication import PublicationHandlers
from community_brain.llm import LLMOutcomeUnknown, _stop_uncertain
from community_brain.processing.pipeline import OutcomeUnknown


@pytest.mark.parametrize("stage", ["session", "chunk"])
def test_extractors_propagate_uncertainty_instead_of_marking_ordinary_failure(stage):
    target = "session_extractor" if stage == "session" else "extractor"
    with patch(
        "community_brain.ingestion." + target + "._call_llm",
        side_effect=LLMOutcomeUnknown("uncertain"),
    ), pytest.raises(LLMOutcomeUnknown):
        if stage == "session":
            extract_session_themes(
                input_text="fixture",
                model="fixture",
                prompt_template="{input_text}",
            )
        else:
            extract_chunk_metadata(
                chunk_text="fixture",
                entity_registry_names=[],
                speaker_alias_names=[],
                model="fixture",
                prompt_template="fixture",
            )


def test_job_indexing_translates_uncertainty_and_restores_legacy_context(tmp_path):
    handler = PublicationHandlers(
        None, tmp_path / "corpus", tmp_path / "config", "http://fixture.invalid"
    )
    handler.artifacts = lambda job_id: (
        SimpleNamespace(identity={"local_date": "2026-09-09", "meeting_id": "fixture"}),
        [],
        {
            name: b"fixture"
            for name in [
                "prepared-transcript.md",
                "extracted-signal.md",
                "community-post.md",
            ]
        },
    )

    def uncertain(*args):
        assert _stop_uncertain.get() is True
        raise LLMOutcomeUnknown("uncertain")

    with patch(
        "community_brain.jobs.publication.ingest_session", side_effect=uncertain
    ), pytest.raises(OutcomeUnknown):
        handler.indexing("fixture")
    assert _stop_uncertain.get() is False
