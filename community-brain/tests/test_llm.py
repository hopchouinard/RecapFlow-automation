import json
import httpx
import pytest
from unittest.mock import patch
from community_brain.llm import call_llm, call_llm_json, LLMError


@pytest.fixture(autouse=True)
def _mock_api_key(request):
    """Provide a fake OPENROUTER_API_KEY for all tests by default.

    Tests that specifically test the missing-key behavior can override this
    by patching _get_api_key to return None within their test body.
    """
    if "no_mock_api_key" in request.keywords:
        yield
        return
    with patch("community_brain.llm._get_api_key", return_value="fake-key-for-tests"):
        yield


class TestCallLlm:
    def test_returns_content_string(self):
        mock_response = httpx.Response(
            200,
            json={
                "choices": [{"message": {"content": "Hello from LLM"}}],
                "usage": {"prompt_tokens": 10, "completion_tokens": 5},
            },
            request=httpx.Request("POST", "https://openrouter.ai/api/v1/chat/completions"),
        )
        with patch("community_brain.llm.httpx.post", return_value=mock_response):
            result = call_llm("Say hello")
        assert result == "Hello from LLM"

    @pytest.mark.no_mock_api_key
    def test_raises_on_missing_api_key(self):
        with patch("community_brain.llm._get_api_key", return_value=None):
            with pytest.raises(LLMError, match="OPENROUTER_API_KEY"):
                call_llm("test")

    def test_retries_on_error(self):
        fail_response = httpx.Response(
            500,
            text="Internal Server Error",
            request=httpx.Request("POST", "https://openrouter.ai/api/v1/chat/completions"),
        )
        ok_response = httpx.Response(
            200,
            json={
                "choices": [{"message": {"content": "success"}}],
                "usage": {"prompt_tokens": 10, "completion_tokens": 5},
            },
            request=httpx.Request("POST", "https://openrouter.ai/api/v1/chat/completions"),
        )
        with patch("community_brain.llm.httpx.post", side_effect=[fail_response, ok_response]):
            with patch("community_brain.llm.time.sleep"):
                result = call_llm("test")
        assert result == "success"


class TestCallLlmJson:
    def test_parses_json_response(self):
        json_content = json.dumps([
            {"topic_title": "Test Topic", "start_timestamp": "00:01:00",
             "end_timestamp": "00:05:00", "summary": "A test topic."}
        ])
        mock_response = httpx.Response(
            200,
            json={
                "choices": [{"message": {"content": json_content}}],
                "usage": {"prompt_tokens": 10, "completion_tokens": 20},
            },
            request=httpx.Request("POST", "https://openrouter.ai/api/v1/chat/completions"),
        )
        with patch("community_brain.llm.httpx.post", return_value=mock_response):
            result = call_llm_json("segment this")
        assert isinstance(result, list)
        assert result[0]["topic_title"] == "Test Topic"

    def test_strips_markdown_code_fences(self):
        json_content = '```json\n[{"topic_title": "Test"}]\n```'
        mock_response = httpx.Response(
            200,
            json={
                "choices": [{"message": {"content": json_content}}],
                "usage": {"prompt_tokens": 10, "completion_tokens": 10},
            },
            request=httpx.Request("POST", "https://openrouter.ai/api/v1/chat/completions"),
        )
        with patch("community_brain.llm.httpx.post", return_value=mock_response):
            result = call_llm_json("test")
        assert result[0]["topic_title"] == "Test"
