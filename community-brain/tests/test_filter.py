import json
from unittest.mock import patch, MagicMock

import httpx

from community_brain.openwebui.community_brain_filter import Filter


CONTEXT_TAG = "[COMMUNITY_BRAIN_CONTEXT]"

MOCK_QUERY_RESPONSE = {
    "chunks": [
        {
            "chunk_id": "2025-09-02-chunk-001",
            "session_date": "2025-09-02",
            "topic": "AI Tools and New Tech Adoption",
            "summary": "Group discusses Codex in Cursor.",
            "text": "[00:02:29] Patrick: Did anybody try the new codex?",
            "speakers": ["Patrick Chouinard", "Shakur"],
            "score": 0.56,
        },
        {
            "chunk_id": "2025-09-02-chunk-038",
            "session_date": "2025-09-02",
            "topic": "Business Alignment",
            "summary": "Discussion about Google image gen.",
            "text": "[00:46:58] Paul: That's very cool.",
            "speakers": ["Paul Miller"],
            "score": 0.40,
        },
    ]
}


def _make_body(user_content: str, extra_messages: list[dict] | None = None) -> dict:
    """Build a minimal chat-completion request body."""
    messages = extra_messages or []
    messages.append({"role": "user", "content": user_content})
    return {"model": "gemma4:e4b", "messages": messages}


class TestFilterInit:
    def test_valves_have_defaults(self):
        f = Filter()
        assert f.valves.retrieval_url == "http://host.docker.internal:8999/query"
        assert f.valves.top_k == 5
        assert f.valves.timeout_seconds == 3.0
        assert f.valves.min_score == 0.2
        assert f.valves.enabled is True

    def test_valve_api_key_default_empty(self):
        f = Filter()
        assert f.valves.api_key == ""


class TestInletSuccess:
    def test_injects_context_on_success(self):
        f = Filter()
        f.valves.api_key = "test-key"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = MOCK_QUERY_RESPONSE
        mock_response.raise_for_status = MagicMock()

        with patch("community_brain.openwebui.community_brain_filter.httpx.Client") as MockClient:
            MockClient.return_value.__enter__ = MagicMock(return_value=MockClient.return_value)
            MockClient.return_value.__exit__ = MagicMock(return_value=False)
            MockClient.return_value.post.return_value = mock_response

            body = _make_body("What about Codex?")
            result = f.inlet(body, __user__={"id": "test"})

        assert result["messages"][0]["role"] == "system"
        content = result["messages"][0]["content"]
        assert CONTEXT_TAG in content
        assert "[Source 1]" in content
        assert "AI Tools and New Tech Adoption" in content
        assert "Did anybody try the new codex?" in content
        assert result["messages"][-1]["role"] == "user"
        assert result["messages"][-1]["content"] == "What about Codex?"

    def test_sends_api_key_header(self):
        f = Filter()
        f.valves.api_key = "my-secret"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"chunks": []}
        mock_response.raise_for_status = MagicMock()

        with patch("community_brain.openwebui.community_brain_filter.httpx.Client") as MockClient:
            MockClient.return_value.__enter__ = MagicMock(return_value=MockClient.return_value)
            MockClient.return_value.__exit__ = MagicMock(return_value=False)
            MockClient.return_value.post.return_value = mock_response

            body = _make_body("test")
            f.inlet(body, __user__={"id": "test"})

            call_kwargs = MockClient.return_value.post.call_args
            assert call_kwargs[1]["headers"]["X-API-Key"] == "my-secret"


class TestInletMinScore:
    def test_filters_chunks_below_min_score(self):
        f = Filter()
        f.valves.api_key = "test-key"
        f.valves.min_score = 0.50

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = MOCK_QUERY_RESPONSE
        mock_response.raise_for_status = MagicMock()

        with patch("community_brain.openwebui.community_brain_filter.httpx.Client") as MockClient:
            MockClient.return_value.__enter__ = MagicMock(return_value=MockClient.return_value)
            MockClient.return_value.__exit__ = MagicMock(return_value=False)
            MockClient.return_value.post.return_value = mock_response

            body = _make_body("Codex?")
            result = f.inlet(body, __user__={"id": "test"})

        content = result["messages"][0]["content"]
        assert "[Source 1]" in content
        assert "[Source 2]" not in content

    def test_no_chunks_above_min_score_injects_disclaimer(self):
        f = Filter()
        f.valves.api_key = "test-key"
        f.valves.min_score = 0.99

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = MOCK_QUERY_RESPONSE
        mock_response.raise_for_status = MagicMock()

        with patch("community_brain.openwebui.community_brain_filter.httpx.Client") as MockClient:
            MockClient.return_value.__enter__ = MagicMock(return_value=MockClient.return_value)
            MockClient.return_value.__exit__ = MagicMock(return_value=False)
            MockClient.return_value.post.return_value = mock_response

            body = _make_body("test")
            result = f.inlet(body, __user__={"id": "test"})

        content = result["messages"][0]["content"]
        assert CONTEXT_TAG in content
        assert "No relevant coaching call sources" in content


class TestInletFailure:
    def test_timeout_injects_unavailable(self):
        f = Filter()
        f.valves.api_key = "test-key"

        with patch("community_brain.openwebui.community_brain_filter.httpx.Client") as MockClient:
            MockClient.return_value.__enter__ = MagicMock(return_value=MockClient.return_value)
            MockClient.return_value.__exit__ = MagicMock(return_value=False)
            MockClient.return_value.post.side_effect = httpx.TimeoutException("timeout")

            body = _make_body("test")
            result = f.inlet(body, __user__={"id": "test"})

        content = result["messages"][0]["content"]
        assert CONTEXT_TAG in content
        assert "retrieval is currently unavailable" in content

    def test_connection_error_injects_unavailable(self):
        f = Filter()
        f.valves.api_key = "test-key"

        with patch("community_brain.openwebui.community_brain_filter.httpx.Client") as MockClient:
            MockClient.return_value.__enter__ = MagicMock(return_value=MockClient.return_value)
            MockClient.return_value.__exit__ = MagicMock(return_value=False)
            MockClient.return_value.post.side_effect = httpx.ConnectError("refused")

            body = _make_body("test")
            result = f.inlet(body, __user__={"id": "test"})

        content = result["messages"][0]["content"]
        assert CONTEXT_TAG in content
        assert "retrieval is currently unavailable" in content

    def test_http_403_injects_unavailable(self):
        f = Filter()
        f.valves.api_key = "wrong-key"

        mock_response = MagicMock()
        mock_response.status_code = 403
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "403", request=MagicMock(), response=mock_response
        )

        with patch("community_brain.openwebui.community_brain_filter.httpx.Client") as MockClient:
            MockClient.return_value.__enter__ = MagicMock(return_value=MockClient.return_value)
            MockClient.return_value.__exit__ = MagicMock(return_value=False)
            MockClient.return_value.post.return_value = mock_response

            body = _make_body("test")
            result = f.inlet(body, __user__={"id": "test"})

        content = result["messages"][0]["content"]
        assert CONTEXT_TAG in content
        assert "retrieval is currently unavailable" in content


class TestInletIdempotency:
    def test_strips_prior_context_before_injecting(self):
        f = Filter()
        f.valves.api_key = "test-key"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = MOCK_QUERY_RESPONSE
        mock_response.raise_for_status = MagicMock()

        stale_system_msg = {
            "role": "system",
            "content": f"{CONTEXT_TAG}\nOld stale context from prior turn",
        }

        with patch("community_brain.openwebui.community_brain_filter.httpx.Client") as MockClient:
            MockClient.return_value.__enter__ = MagicMock(return_value=MockClient.return_value)
            MockClient.return_value.__exit__ = MagicMock(return_value=False)
            MockClient.return_value.post.return_value = mock_response

            body = _make_body("new question", extra_messages=[stale_system_msg])
            result = f.inlet(body, __user__={"id": "test"})

        context_messages = [
            m for m in result["messages"]
            if m["role"] == "system" and CONTEXT_TAG in m["content"]
        ]
        assert len(context_messages) == 1
        assert "Old stale context" not in context_messages[0]["content"]
        assert "[Source 1]" in context_messages[0]["content"]

    def test_preserves_non_context_system_messages(self):
        f = Filter()
        f.valves.api_key = "test-key"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"chunks": []}
        mock_response.raise_for_status = MagicMock()

        base_system_msg = {
            "role": "system",
            "content": "You are a helpful assistant.",
        }

        with patch("community_brain.openwebui.community_brain_filter.httpx.Client") as MockClient:
            MockClient.return_value.__enter__ = MagicMock(return_value=MockClient.return_value)
            MockClient.return_value.__exit__ = MagicMock(return_value=False)
            MockClient.return_value.post.return_value = mock_response

            body = _make_body("test", extra_messages=[base_system_msg])
            result = f.inlet(body, __user__={"id": "test"})

        non_context_system = [
            m for m in result["messages"]
            if m["role"] == "system" and CONTEXT_TAG not in m["content"]
        ]
        assert len(non_context_system) == 1
        assert non_context_system[0]["content"] == "You are a helpful assistant."


class TestInletDisabled:
    def test_disabled_passes_through(self):
        f = Filter()
        f.valves.enabled = False

        body = _make_body("test")
        original_messages = list(body["messages"])
        result = f.inlet(body, __user__={"id": "test"})

        assert result["messages"] == original_messages
