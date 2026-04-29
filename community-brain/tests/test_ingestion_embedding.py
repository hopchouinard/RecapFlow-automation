"""Tests for batch embedding helper."""

from __future__ import annotations

from unittest.mock import patch, MagicMock

from community_brain.ingestion.embedding import embed_texts


def test_embed_texts_returns_list_of_vectors() -> None:
    mock_response = {"embeddings": [[0.1] * 768, [0.2] * 768]}
    mock_client = MagicMock()
    mock_client.embed.return_value = mock_response

    with patch("community_brain.ingestion.embedding.ollama.Client", return_value=mock_client):
        result = embed_texts(["hello", "world"], ollama_base_url="http://localhost:11434")

    assert len(result) == 2
    assert len(result[0]) == 768
    mock_client.embed.assert_called_once_with(model="nomic-embed-text", input=["hello", "world"])


def test_embed_texts_uses_default_client_when_no_base_url() -> None:
    """When ollama_base_url is None, use the default ollama.embed client."""
    mock_response = {"embeddings": [[0.3] * 768]}

    with patch("community_brain.ingestion.embedding.ollama.embed", return_value=mock_response) as mock_embed:
        result = embed_texts(["hello"], ollama_base_url=None)

    assert result == [[0.3] * 768]
    mock_embed.assert_called_once_with(model="nomic-embed-text", input=["hello"])


def test_embed_texts_empty_input_returns_empty_list() -> None:
    """Empty input must not call ollama (no work to do)."""
    with patch("community_brain.ingestion.embedding.ollama") as mock_ollama:
        result = embed_texts([], ollama_base_url=None)
    assert result == []
    mock_ollama.embed.assert_not_called()
    mock_ollama.Client.assert_not_called()


def test_embed_texts_preserves_input_order() -> None:
    """Vectors in the result correspond positionally to input texts."""
    mock_response = {
        "embeddings": [
            [1.0] * 768,
            [2.0] * 768,
            [3.0] * 768,
        ]
    }
    mock_client = MagicMock()
    mock_client.embed.return_value = mock_response

    with patch("community_brain.ingestion.embedding.ollama.Client", return_value=mock_client):
        result = embed_texts(["a", "b", "c"], ollama_base_url="http://host:11434")

    assert result[0][0] == 1.0
    assert result[1][0] == 2.0
    assert result[2][0] == 3.0


def test_embed_texts_uses_env_override_model(monkeypatch) -> None:
    """COMMUNITY_BRAIN_EMBED_MODEL overrides the default nomic-embed-text."""
    monkeypatch.setenv("COMMUNITY_BRAIN_EMBED_MODEL", "mxbai-embed-large")

    mock_response = {"embeddings": [[0.1] * 1024]}
    mock_client = MagicMock()
    mock_client.embed.return_value = mock_response

    with patch("community_brain.ingestion.embedding.ollama.Client", return_value=mock_client):
        embed_texts(["hello"], ollama_base_url="http://localhost:11434")

    mock_client.embed.assert_called_once_with(model="mxbai-embed-large", input=["hello"])


def test_embed_texts_empty_env_falls_through_to_default(monkeypatch) -> None:
    """Empty env var falls through to nomic-embed-text default."""
    monkeypatch.setenv("COMMUNITY_BRAIN_EMBED_MODEL", "")

    mock_response = {"embeddings": [[0.1] * 768]}
    mock_client = MagicMock()
    mock_client.embed.return_value = mock_response

    with patch("community_brain.ingestion.embedding.ollama.Client", return_value=mock_client):
        embed_texts(["hello"], ollama_base_url="http://localhost:11434")

    mock_client.embed.assert_called_once_with(model="nomic-embed-text", input=["hello"])


def test_transcript_embed_text_includes_enriched_fields():
    from community_brain.ingestion.embedding import build_transcript_embed_text

    result = build_transcript_embed_text(
        topic_label="Sales funnel optimization",
        speakers_spoke=["Brandon Hancock", "Patrick Chouinard"],
        speakers_mentioned=["Andrej Karpathy"],
        entities=["Adam James", "Gold Flamingo"],
        keywords=["LinkedIn", "outreach"],
        summary="Adam discussed his sales funnel approach for law firms.",
    )
    for token in (
        "Sales funnel optimization", "Brandon Hancock", "Patrick Chouinard",
        "Andrej Karpathy", "Adam James", "Gold Flamingo", "LinkedIn",
        "outreach", "Adam discussed",
    ):
        assert token in result, f"Missing token: {token}"


def test_transcript_embed_text_handles_empty_lists():
    from community_brain.ingestion.embedding import build_transcript_embed_text
    result = build_transcript_embed_text(
        topic_label="Topic",
        speakers_spoke=[],
        speakers_mentioned=[],
        entities=[],
        keywords=[],
        summary="Summary text",
    )
    assert "Topic" in result
    assert "Summary text" in result


def test_transcript_embed_text_handles_none_lists():
    from community_brain.ingestion.embedding import build_transcript_embed_text
    result = build_transcript_embed_text(
        topic_label="Topic",
        speakers_spoke=None,
        speakers_mentioned=None,
        entities=None,
        keywords=None,
        summary="content",
    )
    assert "Topic" in result
    assert "content" in result


def test_transcript_embed_text_format_is_six_lines():
    """Layout invariant: topic / speakers / mentions / entities / keywords / summary."""
    from community_brain.ingestion.embedding import build_transcript_embed_text
    result = build_transcript_embed_text(
        topic_label="t", speakers_spoke=["s"], speakers_mentioned=["m"],
        entities=["e"], keywords=["k"], summary="sm",
    )
    lines = result.split("\n")
    assert len(lines) == 6
    assert lines[0].startswith("topic:")
    assert lines[1].startswith("speakers:")
    assert lines[2].startswith("mentions:")
    assert lines[3].startswith("entities:")
    assert lines[4].startswith("keywords:")
    assert lines[5].startswith("summary:")
