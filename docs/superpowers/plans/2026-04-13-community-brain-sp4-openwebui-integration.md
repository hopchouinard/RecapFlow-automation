# Community Brain SP4: Open WebUI Integration — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Wire the Community Brain LanceDB retrieval pipeline into Open WebUI via a Filter function so users can query coaching call transcripts through a chat interface with source citations.

**Architecture:** An Open WebUI Filter intercepts user messages in its `inlet` method, calls the existing SP3 FastAPI retrieval server (`host.docker.internal:8999`) with API key auth and a 3s timeout, then injects retrieved chunks as a tagged system message. The filter handles three states: sources found (inject context), no relevant sources (inject disclaimer), retrieval failure (inject unavailable notice). A launchd service keeps the retrieval server running.

**Tech Stack:** Python 3.12, httpx, Open WebUI Filter API (Pydantic Valves), launchd

**Spec:** `docs/superpowers/specs/2026-04-13-community-brain-sp4-openwebui-integration.md`

---

## File Map

| Action | Path | Responsibility |
|--------|------|---------------|
| Create | `community-brain/src/community_brain/openwebui/__init__.py` | Package init |
| Create | `community-brain/src/community_brain/openwebui/community_brain_filter.py` | Open WebUI Filter function (self-contained, copy-pasteable) |
| Create | `community-brain/tests/test_filter.py` | Unit tests for filter logic |
| Create | `community-brain/scripts/start-retrieval-server.sh` | Shell script for launchd to start the retrieval server |
| Create | `community-brain/scripts/com.communitybrain.retrieval.plist` | launchd service definition |

---

### Task 1: Community Brain Filter Function (TDD)

**Files:**
- Create: `community-brain/src/community_brain/openwebui/__init__.py`
- Create: `community-brain/tests/test_filter.py`
- Create: `community-brain/src/community_brain/openwebui/community_brain_filter.py`

- [ ] **Step 1: Create package init**

Create `community-brain/src/community_brain/openwebui/__init__.py`:

```python
"""Open WebUI integration for Community Brain."""
```

- [ ] **Step 2: Write failing tests**

Create `community-brain/tests/test_filter.py`:

```python
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

        # Should have a system message at position 0
        assert result["messages"][0]["role"] == "system"
        content = result["messages"][0]["content"]
        assert CONTEXT_TAG in content
        assert "[Source 1]" in content
        assert "AI Tools and New Tech Adoption" in content
        assert "Did anybody try the new codex?" in content
        # User message should still be last
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
        f.valves.min_score = 0.50  # Only chunk-001 (0.56) should pass

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
        assert "[Source 2]" not in content  # 0.40 < 0.50 threshold

    def test_no_chunks_above_min_score_injects_disclaimer(self):
        f = Filter()
        f.valves.api_key = "test-key"
        f.valves.min_score = 0.99  # Nothing passes

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

        # Should have exactly ONE system message with the context tag
        context_messages = [
            m for m in result["messages"]
            if m["role"] == "system" and CONTEXT_TAG in m["content"]
        ]
        assert len(context_messages) == 1
        # And it should be fresh, not the stale one
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

        # Base system message should still be there
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
```

- [ ] **Step 3: Run tests to verify they fail**

```bash
cd /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/community-brain
source .venv/bin/activate
pytest tests/test_filter.py -v
```

Expected: FAIL — `ModuleNotFoundError: No module named 'community_brain.openwebui.community_brain_filter'`

- [ ] **Step 4: Implement the filter**

Create `community-brain/src/community_brain/openwebui/community_brain_filter.py`:

```python
"""Community Brain RAG Filter for Open WebUI.

Intercepts user messages, retrieves relevant coaching call transcript
chunks from the Community Brain retrieval server, and injects them as
context for the LLM.

Install: Copy this file's content into Open WebUI → Functions → Create Filter.
"""

from __future__ import annotations

import json
import logging
from typing import Optional

import httpx
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

CONTEXT_TAG = "[COMMUNITY_BRAIN_CONTEXT]"


class Filter:
    """Open WebUI Filter that injects Community Brain transcript context."""

    class Valves(BaseModel):
        retrieval_url: str = Field(
            default="http://host.docker.internal:8999/query",
            description="Community Brain retrieval server endpoint",
        )
        api_key: str = Field(
            default="",
            description="API key for the retrieval server (required)",
        )
        top_k: int = Field(
            default=5,
            description="Number of transcript chunks to retrieve",
        )
        timeout_seconds: float = Field(
            default=3.0,
            description="HTTP timeout for retrieval calls (seconds)",
        )
        min_score: float = Field(
            default=0.2,
            description="Minimum similarity score to include a chunk (0-1)",
        )
        enabled: bool = Field(
            default=True,
            description="Enable/disable transcript retrieval",
        )

    def __init__(self):
        self.valves = self.Valves()

    def _strip_prior_context(self, messages: list[dict]) -> list[dict]:
        """Remove any prior Community Brain context messages."""
        return [
            m for m in messages
            if not (m.get("role") == "system" and CONTEXT_TAG in m.get("content", ""))
        ]

    def _build_sources_message(self, chunks: list[dict]) -> str:
        """Format retrieved chunks into a system prompt with source citations."""
        parts = [
            f"{CONTEXT_TAG}\n"
            "You are Community Brain, an AI assistant with access to coaching call "
            "transcripts from the AI Developer Accelerator community. Answer questions "
            "using ONLY the retrieved sources below. Cite sources as [1], [2], etc.\n\n"
            "If the sources don't contain relevant information, say so honestly rather "
            "than making up an answer.\n\n"
            "## Retrieved Sources\n"
        ]

        for i, chunk in enumerate(chunks, 1):
            speakers = ", ".join(chunk.get("speakers", []))
            parts.append(
                f"\n[Source {i}] Date: {chunk['session_date']} | "
                f"Topic: {chunk['topic']}\n"
                f"Speakers: {speakers}\n"
                f"Summary: {chunk['summary']}\n"
                f"Transcript:\n{chunk['text']}\n\n---"
            )

        return "\n".join(parts)

    def _build_no_sources_message(self) -> str:
        """Message when no relevant chunks found."""
        return (
            f"{CONTEXT_TAG}\n"
            "No relevant coaching call sources were found for this question. "
            "Answer based on your general knowledge and clearly state that you "
            "are not drawing from transcript sources."
        )

    def _build_unavailable_message(self) -> str:
        """Message when retrieval server is unreachable or errored."""
        return (
            f"{CONTEXT_TAG}\n"
            "Community Brain retrieval is currently unavailable. Do not answer "
            "questions about coaching call content. Instead, inform the user that "
            "transcript search is temporarily unavailable and suggest they try "
            "again shortly."
        )

    def _retrieve_chunks(self, question: str) -> tuple[str, list[dict]]:
        """Call the retrieval server. Returns (status, chunks).

        status is one of: "ok", "no_results", "error"
        """
        try:
            with httpx.Client(timeout=self.valves.timeout_seconds) as client:
                response = client.post(
                    self.valves.retrieval_url,
                    json={"question": question, "top_k": self.valves.top_k},
                    headers={"X-API-Key": self.valves.api_key},
                )
                response.raise_for_status()

            data = response.json()
            chunks = data.get("chunks", [])

            # Filter by min_score
            chunks = [c for c in chunks if c.get("score", 0) >= self.valves.min_score]

            if not chunks:
                return "no_results", []
            return "ok", chunks

        except (httpx.TimeoutException, httpx.ConnectError, httpx.HTTPStatusError) as e:
            logger.warning("Community Brain retrieval failed: %s", e)
            return "error", []
        except Exception as e:
            logger.error("Unexpected retrieval error: %s", e)
            return "error", []

    def inlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        """Pre-process: inject retrieved transcript context into the message list."""
        if not self.valves.enabled:
            return body

        messages = body.get("messages", [])

        # Strip any prior context (idempotent replacement)
        messages = self._strip_prior_context(messages)

        # Extract the user's latest question
        user_messages = [m for m in messages if m.get("role") == "user"]
        if not user_messages:
            body["messages"] = messages
            return body

        question = user_messages[-1]["content"]

        # Retrieve chunks
        status, chunks = self._retrieve_chunks(question)

        # Build the appropriate system message
        if status == "ok":
            context_content = self._build_sources_message(chunks)
        elif status == "no_results":
            context_content = self._build_no_sources_message()
        else:
            context_content = self._build_unavailable_message()

        # Insert context at position 0
        context_message = {"role": "system", "content": context_content}
        messages.insert(0, context_message)

        body["messages"] = messages
        return body
```

- [ ] **Step 5: Run tests to verify they pass**

```bash
cd /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/community-brain
source .venv/bin/activate
pytest tests/test_filter.py -v
```

Expected: All 11 tests PASS.

- [ ] **Step 6: Run full test suite**

```bash
pytest tests/ -v
```

Expected: All tests PASS (~96 total).

- [ ] **Step 7: Commit**

```bash
cd /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation
git add community-brain/src/community_brain/openwebui/__init__.py community-brain/src/community_brain/openwebui/community_brain_filter.py community-brain/tests/test_filter.py
git commit -m "feat(sp4): add Open WebUI Community Brain filter function

Filter intercepts user messages, retrieves transcript chunks from
the SP3 retrieval server, and injects them as tagged system context.
Three-state handling: sources found, no results, retrieval failure.
Idempotent context replacement across multi-turn and regenerate.
11 tests passing."
```

---

### Task 2: Retrieval Server Background Service

**Files:**
- Create: `community-brain/scripts/start-retrieval-server.sh`
- Create: `community-brain/scripts/com.communitybrain.retrieval.plist`

- [ ] **Step 1: Create the start script**

Create `community-brain/scripts/start-retrieval-server.sh`:

```bash
#!/bin/bash
# Start the Community Brain retrieval server.
# Called by launchd via com.communitybrain.retrieval.plist.

set -euo pipefail

PROJECT_DIR="/Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/community-brain"
VENV_PYTHON="${PROJECT_DIR}/.venv/bin/python"
LOG_DIR="${HOME}/Library/Logs/CommunityBrain"

mkdir -p "${LOG_DIR}"

export RETRIEVAL_HOST="${RETRIEVAL_HOST:-0.0.0.0}"
export RETRIEVAL_PORT="${RETRIEVAL_PORT:-8999}"
# RETRIEVAL_API_KEY must be set in the launchd plist or environment

cd "${PROJECT_DIR}"
exec "${VENV_PYTHON}" -m community_brain.query.retrieval_server
```

- [ ] **Step 2: Create the launchd plist**

Create `community-brain/scripts/com.communitybrain.retrieval.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.communitybrain.retrieval</string>

    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>/Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/community-brain/scripts/start-retrieval-server.sh</string>
    </array>

    <key>EnvironmentVariables</key>
    <dict>
        <key>RETRIEVAL_HOST</key>
        <string>0.0.0.0</string>
        <key>RETRIEVAL_PORT</key>
        <string>8999</string>
        <key>RETRIEVAL_API_KEY</key>
        <string>CHANGE_ME_BEFORE_LOADING</string>
    </dict>

    <key>RunAtLoad</key>
    <true/>

    <key>KeepAlive</key>
    <true/>

    <key>StandardOutPath</key>
    <string>/Users/pchouinard/Library/Logs/CommunityBrain/retrieval-server.log</string>

    <key>StandardErrorPath</key>
    <string>/Users/pchouinard/Library/Logs/CommunityBrain/retrieval-server.err</string>
</dict>
</plist>
```

- [ ] **Step 3: Make start script executable and test manually**

```bash
chmod +x /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/community-brain/scripts/start-retrieval-server.sh
```

Test the start script directly (kill any existing server first):

```bash
RETRIEVAL_API_KEY=test-sp4-key /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/community-brain/scripts/start-retrieval-server.sh &
SERVER_PID=$!
sleep 2

# Health check
curl -s http://localhost:8999/health
# Expected: {"status":"ok"}

# Auth required
curl -s -X POST http://localhost:8999/query -H "Content-Type: application/json" -d '{"question":"test"}' | python3 -m json.tool
# Expected: {"detail":"Invalid or missing API key"}

# Auth works
curl -s -X POST http://localhost:8999/query -H "Content-Type: application/json" -H "X-API-Key: test-sp4-key" -d '{"question":"Codex tools","top_k":2}' | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'Chunks: {len(d[\"chunks\"])}')"
# Expected: Chunks: 2

kill $SERVER_PID
```

- [ ] **Step 4: Install launchd service**

First, edit the plist to set a real API key:

```bash
# Generate a key
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
```

Edit `RETRIEVAL_API_KEY` in the plist with the generated key. Then:

```bash
cp /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/community-brain/scripts/com.communitybrain.retrieval.plist ~/Library/LaunchAgents/

launchctl load ~/Library/LaunchAgents/com.communitybrain.retrieval.plist
```

Verify it started:

```bash
launchctl list | grep communitybrain
# Expected: PID listed, exit status 0

curl -s http://localhost:8999/health
# Expected: {"status":"ok"}
```

- [ ] **Step 5: Verify Docker can reach the server**

```bash
docker run --rm curlimages/curl:latest curl -s http://host.docker.internal:8999/health
# Expected: {"status":"ok"}
```

- [ ] **Step 6: Commit**

```bash
cd /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation
git add community-brain/scripts/start-retrieval-server.sh community-brain/scripts/com.communitybrain.retrieval.plist
git commit -m "feat(sp4): add launchd service for retrieval server

start-retrieval-server.sh: wrapper script for launchd.
com.communitybrain.retrieval.plist: auto-starts on login, restarts
on crash, binds 0.0.0.0:8999 with mandatory API key auth."
```

---

### Task 3: Open WebUI Configuration (Manual)

**Note:** This task is manual (UI interactions in Open WebUI). No code files created.

- [ ] **Step 1: Install the filter in Open WebUI**

1. Open http://localhost:3000 in a browser
2. Navigate to **Workspace** → **Functions** → **Create Function**
3. Set the function name to `community_brain_filter`
4. Set the type to **Filter**
5. Copy the entire contents of `community-brain/src/community_brain/openwebui/community_brain_filter.py` and paste it into the code editor
6. Click **Save**

- [ ] **Step 2: Configure Valves**

1. Click the gear icon on the `community_brain_filter` function
2. Set the Valves:
   - `retrieval_url`: `http://host.docker.internal:8999/query`
   - `api_key`: (the same key from the launchd plist)
   - `top_k`: `5`
   - `timeout_seconds`: `3.0`
   - `min_score`: `0.2`
   - `enabled`: `true`
3. Click **Save**

- [ ] **Step 3: Enable the filter**

Option A (per-model): Navigate to **Workspace** → **Models** → select `gemma4:e4b` → **Filters** → add `community_brain_filter`

Option B (global): Navigate to **Workspace** → **Functions** → toggle the `community_brain_filter` to enabled globally

- [ ] **Step 4: Verify filter is active**

Start a new chat with gemma4:e4b and ask: "What was discussed about Codex and Google image generation tools?"

Expected: The response should contain source citations like [1], [2] and reference specific transcript content.

---

### Task 4: End-to-End Validation

**Note:** All steps are manual tests through the Open WebUI chat interface.

- [ ] **Step 1: Test retrieval with citations**

New chat → "Tell me about Codex and Google image generation tools discussed in the coaching calls"

Verify:
- Response references specific transcript content
- Source citations [1], [2], etc. are present
- Topics and dates are mentioned

- [ ] **Step 2: Test vector storage query**

New chat → "What tools for vector storage were discussed?"

Verify:
- Response mentions pgvector, Postgres, Supabase
- Source citations present

- [ ] **Step 3: Test multi-turn context refresh**

In the same chat as Step 2, follow up with: "What about GPU benchmarks?"

Verify:
- Response shifts to GPU/benchmark content
- Does NOT repeat vector storage sources from the prior turn

- [ ] **Step 4: Test regenerate idempotency**

Click the "Regenerate" button on the last response.

Verify:
- Response regenerates with fresh retrieval
- No duplicate or stale context (answer should be similar but not have doubled sources)

- [ ] **Step 5: Test retrieval server down**

Stop the retrieval server:

```bash
launchctl unload ~/Library/LaunchAgents/com.communitybrain.retrieval.plist
```

Ask a question in Open WebUI: "What about AI tools?"

Verify:
- Response acknowledges transcript search is unavailable
- Does NOT hallucinate coaching call content

Restart the server:

```bash
launchctl load ~/Library/LaunchAgents/com.communitybrain.retrieval.plist
```

- [ ] **Step 6: Test wrong API key**

In Open WebUI Functions UI, change the `api_key` valve to `wrong-key`. Ask a question.

Verify:
- Response acknowledges retrieval is unavailable

Restore the correct key afterward.

- [ ] **Step 7: Test filter disabled**

In Open WebUI Functions UI, set `enabled` to `false`. Ask a question about coaching calls.

Verify:
- Response is a generic LLM answer with no transcript sources

Re-enable the filter afterward.

- [ ] **Step 8: Measure latency**

Ask 3 questions and note the time-to-first-token:

1. "Codex and image gen tools" (targeted)
2. "What tools for vector storage?" (broader)
3. "GPU benchmarks on September 2" (with implicit date filter)

Target: < 2s to first token for each.

- [ ] **Step 9: Commit spec and plan updates**

```bash
cd /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation
git add docs/superpowers/specs/2026-04-13-community-brain-sp4-openwebui-integration.md docs/superpowers/plans/2026-04-13-community-brain-sp4-openwebui-integration.md
git commit -m "docs(sp4): add Open WebUI integration spec and plan

SP4 wires the Community Brain retrieval pipeline into Open WebUI
via a Filter function with fail-closed design, idempotent context
injection, and mandatory API key auth."
```

---

## Verification Summary

SP4 is complete when:

| Check | Status |
|-------|--------|
| All unit tests pass (~96) | |
| Retrieval server starts automatically via launchd | |
| API key auth enforced (request without key → 403) | |
| Filter installed and enabled in Open WebUI | |
| "Codex and image gen tools" returns relevant chunks with citations | |
| "What tools for vector storage?" returns pgvector discussion | |
| Multi-turn chat: context refreshes per turn (no stale chunks) | |
| Regenerate: context replaced, not duplicated | |
| Retrieval server down → user sees "retrieval unavailable" message | |
| Wrong API key → user sees "retrieval unavailable" message | |
| No relevant chunks → user sees "no sources found" disclaimer | |
| Query latency < 2s end-to-end | |
| Filter toggle works (disable → no retrieval context) | |
| Committed and pushed | |
