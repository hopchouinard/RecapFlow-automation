from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient

# Patch search before importing the app
with patch("community_brain.query.retrieval_server.search_chunks") as mock_search:
    mock_search.return_value = [
        {
            "chunk_id": "2025-09-02-chunk-001",
            "session_date": "2025-09-02",
            "topic": "AI Tools",
            "summary": "Discussion about Codex.",
            "text": "[00:02:29] Patrick: Did anybody try codex?",
            "speakers_in_chunk": '["Patrick Chouinard"]',
            "_distance": 0.15,
        }
    ]
    from community_brain.query.retrieval_server import app

client = TestClient(app)


class TestHealthEndpoint:
    def test_health(self):
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"


class TestQueryEndpoint:
    @patch("community_brain.query.retrieval_server.search_chunks")
    def test_returns_chunks(self, mock_search):
        mock_search.return_value = [
            {
                "chunk_id": "2025-09-02-chunk-001",
                "session_date": "2025-09-02",
                "topic": "AI Tools",
                "summary": "Discussion about Codex.",
                "text": "[00:02:29] Patrick: Did anybody try codex?",
                "speakers_in_chunk": '["Patrick Chouinard"]',
                "_distance": 0.15,
            }
        ]
        response = client.post(
            "/query",
            json={"question": "What about Codex?", "top_k": 5},
        )
        assert response.status_code == 200
        data = response.json()
        assert "chunks" in data
        assert len(data["chunks"]) == 1
        assert data["chunks"][0]["chunk_id"] == "2025-09-02-chunk-001"
        assert data["chunks"][0]["topic"] == "AI Tools"
        assert "score" in data["chunks"][0]

    @patch("community_brain.query.retrieval_server.search_chunks")
    def test_empty_results(self, mock_search):
        mock_search.return_value = []
        response = client.post(
            "/query",
            json={"question": "Something obscure", "top_k": 5},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["chunks"] == []

    @patch("community_brain.query.retrieval_server.search_chunks")
    def test_with_filters(self, mock_search):
        mock_search.return_value = []
        response = client.post(
            "/query",
            json={
                "question": "test",
                "top_k": 3,
                "filter_date": "2025-09-02",
                "filter_speaker": "Patrick",
            },
        )
        assert response.status_code == 200
        mock_search.assert_called_once()
        call_kwargs = mock_search.call_args
        assert call_kwargs[1]["filter_date"] == "2025-09-02" or call_kwargs[0][0] == "test"
