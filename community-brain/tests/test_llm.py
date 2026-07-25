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


def test_call_llm_uses_backoff_schedule(monkeypatch):
    """5xx retries sleep per the configured schedule, not 2**attempt."""
    import time as _time

    import httpx as _httpx

    from community_brain.llm import call_llm

    sleeps: list[int] = []
    monkeypatch.setattr(_time, "sleep", lambda s: sleeps.append(s))

    calls = {"n": 0}

    class _Fail:
        status_code = 500

        def raise_for_status(self):  # pragma: no cover - not reached on 5xx
            raise AssertionError("raise_for_status should not run on the 5xx path")

        def json(self):  # pragma: no cover
            return {}

    class _OK:
        status_code = 200

        def raise_for_status(self):
            return None

        def json(self):
            return {"choices": [{"message": {"content": "ok"}}], "usage": {}}

    def _fake_post(url, headers=None, json=None, timeout=None):
        calls["n"] += 1
        return _Fail() if calls["n"] <= 2 else _OK()

    monkeypatch.setattr(_httpx, "post", _fake_post)
    out = call_llm("hi", model="m", retries=3, backoff_schedule=[7, 11, 13])
    assert out == "ok"
    assert sleeps == [7, 11]


def test_call_llm_default_backoff_is_exponential(monkeypatch):
    import time as _time

    import httpx as _httpx

    from community_brain.llm import call_llm

    sleeps: list[int] = []
    monkeypatch.setattr(_time, "sleep", lambda s: sleeps.append(s))

    calls = {"n": 0}

    class _Fail:
        status_code = 500

        def raise_for_status(self):  # pragma: no cover
            raise AssertionError

        def json(self):  # pragma: no cover
            return {}

    class _OK:
        status_code = 200

        def raise_for_status(self):
            return None

        def json(self):
            return {"choices": [{"message": {"content": "ok"}}], "usage": {}}

    def _fake_post(url, headers=None, json=None, timeout=None):
        calls["n"] += 1
        return _Fail() if calls["n"] <= 2 else _OK()

    monkeypatch.setattr(_httpx, "post", _fake_post)
    call_llm("hi", model="m", retries=3)
    assert sleeps == [1, 2]
