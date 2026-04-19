# Plan B — n8n Ingestion Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Wire the live n8n Merged Call Summarizer and a new Transcript-Only Summarizer into the Plan A retrieval server, so coaching-call artifacts land in LanceDB automatically.

**Architecture:** Two n8n workflows plus one new FastAPI endpoint and one prompt rewrite. Workflow 1 (live weekly) gets a parallel prep-prompt branch and a final `/ingest` POST added to the existing chain; Workflow 2 is brand-new and iterates the 65-session historical corpus sequentially with a JSON state file for resume safety. The retrieval server gains `GET /speaker-aliases-block` to render the speaker registry into prompt-template-ready markdown.

**Tech Stack:** Python 3.11 + FastAPI + LanceDB + pyarrow (server side); n8n 2.15 + OpenRouter Chat Model nodes + Code nodes (fs) + HTTP Request nodes (workflow side); Docker Compose orchestration on the VM.

**Spec:** [docs/superpowers/specs/2026-04-19-plan-b-n8n-ingestion-integration-design.md](../specs/2026-04-19-plan-b-n8n-ingestion-integration-design.md) — read this first if you're new to the feature.

---

## File map

| Action | Path | Purpose |
|---|---|---|
| Modify | `community-brain/src/community_brain/ingestion/registries.py` | Add `render_alias_block()` pure function |
| Modify | `community-brain/src/community_brain/query/retrieval_server.py` | Add `GET /speaker-aliases-block` route |
| Modify | `community-brain/tests/test_registries.py` | Unit tests for `render_alias_block` |
| Create | `community-brain/tests/test_retrieval_server_aliases_block.py` | Route tests |
| Modify | `docker-compose.yml` | Add `./n8n-state/` bind mount on the `n8n` service |
| Create | `n8n-state/.gitkeep` | Ensure directory exists at checkout |
| Modify | `.gitignore` | Exclude `n8n-state/backfill-state.json` (runtime state, not code) |
| Modify | `workflows/merged-call-summarizer.json` | Extract Signal prompt rewrite + prep-prompt branch + `/ingest` POST |
| Create | `workflows/transcript-only-summarizer.json` | Brand new Workflow 2 |
| Modify | `CLAUDE.md` | Document new workflow + update "Current status" |

Runtime-only action (not a file change):
- One-time `rsync ./historical/ n8n-automation:~/n8n/historical/` from the Mac Mini to populate the VM's backfill corpus.

---

## Task dependency overview

```
Task 1 (render_alias_block)  ──▶  Task 2 (route)  ──▶  Task 3 (deploy)
                                                              │
                                                              ▼
                                                       Tasks 4–5 (rsync + compose mount)
                                                              │
                                       ┌──────────────────────┴────────────────────┐
                                       ▼                                           ▼
                              Workflow 1 (Tasks 6–9)                    Workflow 2 (Tasks 10–16)
                                       │                                           │
                                       └───────────────────┬───────────────────────┘
                                                           ▼
                                                      Task 17 (docs)
```

Tasks 1–3 must land before either workflow; Tasks 4–5 should land before Workflow 2 but can land in parallel with Workflow 1 design. Tasks 6–9 and 10–16 are independent of each other.

---

## Task 1: `render_alias_block()` pure function

**Purpose:** deterministic markdown formatter that turns a `SpeakerRegistry` into the pre-rendered block the prep-prompt expects. No I/O. Testable with `tmp_path` fixtures that write YAML files.

**Files:**
- Modify: `community-brain/src/community_brain/ingestion/registries.py`
- Modify: `community-brain/tests/test_registries.py`

### Steps

- [ ] **Step 1: Write the failing tests**

Add to the end of `community-brain/tests/test_registries.py`:

```python
def test_render_alias_block_empty_registry(tmp_path: Path) -> None:
    from community_brain.ingestion.registries import render_alias_block

    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(path, {}, [])
    reg = load_speaker_registry(path)

    block = render_alias_block(reg)

    # Header is always emitted so the prompt's "if not in this list" clause
    # remains syntactically anchored even with zero canonical entries.
    assert block.startswith("## SPEAKER_ALIASES")
    assert "pass the raw name through unchanged" in block
    # No canonical entries -> no bullet lines
    assert "\n- " not in block


def test_render_alias_block_populated_registry(tmp_path: Path) -> None:
    from community_brain.ingestion.registries import render_alias_block

    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(
        path,
        {
            "Alex Rojas": ["alexrojas", "Alex R"],
            "Sam": ["sam", "Samantha"],
        },
        pending=["SomeNewPerson"],
    )
    reg = load_speaker_registry(path)

    block = render_alias_block(reg)

    # Canonical entries appear sorted alphabetically for determinism
    assert block.index("- Alex Rojas") < block.index("- Sam")
    # Each canonical name lists its aliases in yaml order
    assert "- Alex Rojas — aliases: alexrojas, Alex R" in block
    assert "- Sam — aliases: sam, Samantha" in block
    # Pending entries MUST NOT leak into the rendered block
    assert "SomeNewPerson" not in block


def test_render_alias_block_canonical_with_no_aliases(tmp_path: Path) -> None:
    """A canonical name with an empty alias list renders without the em-dash tail."""
    from community_brain.ingestion.registries import render_alias_block

    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(path, {"Solo Speaker": []}, [])
    reg = load_speaker_registry(path)

    block = render_alias_block(reg)
    assert "- Solo Speaker" in block
    assert "— aliases:" not in block
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd community-brain
./.venv/bin/pytest tests/test_registries.py -k render_alias_block -v
```

Expected: 3 FAILED with `ImportError: cannot import name 'render_alias_block'`.

- [ ] **Step 3: Implement `render_alias_block`**

Add to `community-brain/src/community_brain/ingestion/registries.py`, after the existing `load_speaker_registry` function:

```python
_ALIAS_BLOCK_HEADER = """## SPEAKER_ALIASES

The following canonical speaker names are known. When normalizing speakers
in the transcript, map any of the listed raw variants to the canonical form.
If a speaker is NOT in this list, pass the raw name through unchanged AND
list them under "=== UNRESOLVED SPEAKERS ===" at the end of your output.
"""


def render_alias_block(registry: SpeakerRegistry) -> str:
    """Render a SpeakerRegistry as a pre-rendered markdown block for
    {{SPEAKER_ALIASES_BLOCK}} prompt-template substitution.

    Pending entries are deliberately excluded: the prep-prompt must not
    pretend unreviewed aliases are canonical.
    """
    lines = [_ALIAS_BLOCK_HEADER]
    for canonical in sorted(registry.aliases.keys()):
        raws = registry.aliases[canonical]
        if raws:
            lines.append(f"- {canonical} — aliases: {', '.join(raws)}")
        else:
            lines.append(f"- {canonical}")
    return "\n".join(lines)
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_registries.py -k render_alias_block -v
```

Expected: 3 PASSED.

- [ ] **Step 5: Run the full test suite to confirm no regressions**

```bash
./.venv/bin/pytest tests/ -q --ignore=tests/test_end_to_end.py --ignore=tests/test_retrieval_server_ingest.py
```

Expected: 255 passed (was 252; +3 from Task 1).

- [ ] **Step 6: Commit**

```bash
git add community-brain/src/community_brain/ingestion/registries.py community-brain/tests/test_registries.py
git commit -m "$(cat <<'EOF'
feat(ingestion): add render_alias_block for prompt-template substitution

Pure markdown formatter that turns the current SpeakerRegistry into the
block the prep-prompt expects behind {{SPEAKER_ALIASES_BLOCK}}. Pending
entries are excluded on purpose -- unreviewed aliases must not look
canonical to the LLM.

Adds three unit tests: empty registry, populated with aliases, canonical
with no aliases (edge case renders without the em-dash tail).

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 2: `GET /speaker-aliases-block` FastAPI route

**Purpose:** expose the Task 1 formatter as an HTTP endpoint so n8n can fetch the block at prompt-build time.

**Files:**
- Modify: `community-brain/src/community_brain/query/retrieval_server.py`
- Create: `community-brain/tests/test_retrieval_server_aliases_block.py`

### Steps

- [ ] **Step 1: Write the failing tests**

Create `community-brain/tests/test_retrieval_server_aliases_block.py`:

```python
"""Tests for GET /speaker-aliases-block endpoint."""

from __future__ import annotations

from pathlib import Path

import yaml
from fastapi.testclient import TestClient

from community_brain.query import retrieval_server as server_mod


def _write_speaker_yaml(path: Path, aliases: dict[str, list[str]], pending: list[str]) -> None:
    path.write_text(
        yaml.safe_dump({"version": "test", "aliases": aliases, "pending": pending}),
        encoding="utf-8",
    )


def test_get_speaker_aliases_block_returns_rendered_block(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(tmp_path))

    _write_speaker_yaml(tmp_path / "speaker-aliases.yaml", {"Alex Rojas": ["alexrojas"]}, [])

    client = TestClient(server_mod.app)
    response = client.get("/speaker-aliases-block")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/plain")
    assert "## SPEAKER_ALIASES" in response.text
    assert "- Alex Rojas — aliases: alexrojas" in response.text


def test_get_speaker_aliases_block_empty_registry(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(tmp_path))

    _write_speaker_yaml(tmp_path / "speaker-aliases.yaml", {}, [])

    client = TestClient(server_mod.app)
    response = client.get("/speaker-aliases-block")

    assert response.status_code == 200
    # Header still present; no bullet lines
    assert "## SPEAKER_ALIASES" in response.text
    assert "\n- " not in response.text


def test_get_speaker_aliases_block_401_when_api_key_enabled_and_missing_header(
    monkeypatch, tmp_path: Path
) -> None:
    monkeypatch.setenv("RETRIEVAL_API_KEY", "secret-test-key")
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(tmp_path))
    _write_speaker_yaml(tmp_path / "speaker-aliases.yaml", {}, [])

    client = TestClient(server_mod.app)
    response = client.get("/speaker-aliases-block")

    assert response.status_code == 401


def test_get_speaker_aliases_block_200_when_api_key_enabled_and_header_matches(
    monkeypatch, tmp_path: Path
) -> None:
    monkeypatch.setenv("RETRIEVAL_API_KEY", "secret-test-key")
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(tmp_path))
    _write_speaker_yaml(tmp_path / "speaker-aliases.yaml", {}, [])

    client = TestClient(server_mod.app)
    response = client.get("/speaker-aliases-block", headers={"X-API-Key": "secret-test-key"})

    assert response.status_code == 200
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
./.venv/bin/pytest tests/test_retrieval_server_aliases_block.py -v
```

Expected: 4 FAILED with 404 responses (route doesn't exist yet).

- [ ] **Step 3: Implement the route**

In `community-brain/src/community_brain/query/retrieval_server.py`:

Add import near the other fastapi.responses imports (add if the module isn't already imported):

```python
from fastapi.responses import PlainTextResponse
```

Add import for the render function near the other ingestion imports:

```python
from community_brain.ingestion.registries import (
    load_speaker_registry,
    render_alias_block,
)
```

Add the route (place it after `@app.get("/health")` and before `@app.post("/query")`):

```python
@app.get("/speaker-aliases-block", response_class=PlainTextResponse)
def speaker_aliases_block(_key: str | None = Depends(_verify_api_key)) -> str:
    """Return the current speaker-alias registry as a markdown block for
    {{SPEAKER_ALIASES_BLOCK}} prompt-template substitution.

    Reads config/speaker-aliases.yaml on every call (~1 ms) so operators can
    edit the yaml and see changes on the next call without restarting the
    server.
    """
    registry = load_speaker_registry(_config_dir() / "speaker-aliases.yaml")
    return render_alias_block(registry)
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_retrieval_server_aliases_block.py -v
```

Expected: 4 PASSED.

- [ ] **Step 5: Run the full test suite for no regressions**

```bash
./.venv/bin/pytest tests/ -q --ignore=tests/test_end_to_end.py --ignore=tests/test_retrieval_server_ingest.py
```

Expected: 259 passed (was 255; +4 from Task 2).

- [ ] **Step 6: Commit**

```bash
git add community-brain/src/community_brain/query/retrieval_server.py community-brain/tests/test_retrieval_server_aliases_block.py
git commit -m "$(cat <<'EOF'
feat(retrieval): add GET /speaker-aliases-block endpoint

New read-only endpoint returns the current speaker-alias registry
rendered as a markdown block, ready for {{SPEAKER_ALIASES_BLOCK}}
prompt-template substitution by n8n workflows. Reads the yaml on every
call so operators can edit the registry without restarting the server.

Covered: unpopulated registry, populated registry, auth-enabled paths
(401 without header, 200 with matching X-API-Key).

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 3: Deploy to VM + smoke test

**Purpose:** push the endpoint to the live VM so Workflows 1 and 2 can call it.

### Steps

- [ ] **Step 1: Push to origin/main**

```bash
git push origin main
```

- [ ] **Step 2: Pull on VM**

```bash
ssh n8n-automation 'cd ~/n8n && git pull --ff-only origin main'
```

Expected: Fast-forward summary listing the registries.py and retrieval_server.py changes.

- [ ] **Step 3: Rebuild the image (code change requires rebuild)**

```bash
ssh n8n-automation 'cd ~/n8n && docker compose build retrieval-server 2>&1 | tail -3'
```

Expected: `Image n8n-retrieval-server Built`.

- [ ] **Step 4: Recreate the container**

```bash
ssh n8n-automation 'cd ~/n8n && docker compose up -d retrieval-server'
```

Expected: `Container community_brain_retrieval Recreated` and `Started`.

- [ ] **Step 5: Health check**

```bash
sleep 6
ssh n8n-automation 'curl -s -w "\nHTTP %{http_code}\n" http://127.0.0.1:8999/health'
```

Expected: `{"status":"ok"}` + `HTTP 200`.

- [ ] **Step 6: Smoke test the new endpoint from the VM**

```bash
ssh n8n-automation 'curl -s -w "\nHTTP %{http_code}\n" http://127.0.0.1:8999/speaker-aliases-block'
```

Expected: body starts with `## SPEAKER_ALIASES`, contains the instruction paragraph, and either (a) has no bullet lines (if the registry is empty) or (b) has `- CanonicalName — aliases: ...` lines for each populated entry. HTTP 200.

- [ ] **Step 7: Smoke test that n8n container can reach the endpoint via compose DNS**

```bash
ssh n8n-automation 'docker exec n8n wget -qO- http://retrieval-server:8999/speaker-aliases-block | head -c 200'
```

Expected: same body header (`## SPEAKER_ALIASES`). Confirms Workflow 1 and 2 will be able to call this from their HTTP Request nodes.

No commit — this task is deployment-only.

---

## Task 4: rsync historical/ to VM

**Purpose:** one-time operational step to make the 65-session backfill corpus available to Workflow 2.

### Steps

- [ ] **Step 1: Confirm size on Mac Mini**

```bash
du -sh /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/historical/
ls /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/historical/ | wc -l
```

Expected: ~10M, 65 folders.

- [ ] **Step 2: rsync to VM**

Run from the Mac Mini:

```bash
rsync -av --delete /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/historical/ n8n-automation:~/n8n/historical/
```

Expected: transfer summary showing all 65 folders + 3 files each (meta.json, summary.md, transcript.md) copied. `--delete` keeps the VM copy exactly in sync; safe here because this is a one-shot setup.

- [ ] **Step 3: Verify on VM**

```bash
ssh n8n-automation 'ls ~/n8n/historical/ | wc -l'
ssh n8n-automation 'ls ~/n8n/historical/ | head -3'
```

Expected: `65` and three folder names.

- [ ] **Step 4: Confirm the n8n container sees them via its output/watch mount siblings**

`historical/` is NOT currently mounted into the n8n container. Workflow 2 reads it via the n8n container's own filesystem — we'll add a volume mount in Task 5. Skip to Task 5; nothing to verify inside the container yet.

No commit — this task is data-transfer-only.

---

## Task 5: Add `./historical/` and `./n8n-state/` bind mounts to the n8n service

**Purpose:** expose the historical corpus to n8n (so Workflow 2 can read transcripts) and create a dedicated writable path for `backfill-state.json`.

**Files:**
- Modify: `docker-compose.yml`
- Create: `n8n-state/.gitkeep`
- Modify: `.gitignore`

### Steps

- [ ] **Step 1: Edit docker-compose.yml**

In `docker-compose.yml`, find the `n8n` service's `volumes:` block (currently lists `./data`, `./watch`, `./output`). Add two entries so the final block reads:

```yaml
    volumes:
      - ./data:/home/node/.n8n
      - ./watch:/home/node/watch
      - ./output:/home/node/output
      - ./historical:/home/node/historical:ro
      - ./n8n-state:/home/node/n8n-state
```

Notes:
- `./historical` is read-only (`:ro`) — Workflow 2 only reads it.
- `./n8n-state` is read-write — Workflow 2 reads and writes `backfill-state.json` here.

- [ ] **Step 2: Create the n8n-state directory**

```bash
mkdir -p /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/n8n-state
touch /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/n8n-state/.gitkeep
```

- [ ] **Step 3: Gitignore the runtime state file**

Append to `.gitignore`:

```
# Workflow runtime state (not source)
n8n-state/backfill-state.json
```

- [ ] **Step 4: Commit the compose + gitignore changes**

```bash
git add docker-compose.yml n8n-state/.gitkeep .gitignore
git commit -m "$(cat <<'EOF'
infra(docker): mount ./historical ro and ./n8n-state rw into the n8n service

Workflow 2 (Transcript-Only Summarizer) needs read access to the
historical corpus and a writable path for backfill-state.json. The
community-brain/config/ volume is retrieval-server-owned and not the
right fit; a dedicated ./n8n-state/ directory keeps n8n's workflow state
cleanly separated from the retrieval server's registries.

backfill-state.json itself is gitignored -- it is runtime state, not
source.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

- [ ] **Step 5: Push**

```bash
git push origin main
```

- [ ] **Step 6: Deploy on VM**

```bash
ssh n8n-automation 'cd ~/n8n && git pull --ff-only origin main'
ssh n8n-automation 'mkdir -p ~/n8n/n8n-state'
ssh n8n-automation 'cd ~/n8n && docker compose up -d n8n'
```

Expected: `Container n8n Recreated Started`.

- [ ] **Step 7: Verify mounts inside the n8n container**

```bash
ssh n8n-automation 'docker exec n8n ls -la /home/node/historical/ | head -5'
ssh n8n-automation 'docker exec n8n ls -la /home/node/n8n-state/'
```

Expected: historical/ shows session folders; n8n-state/ shows the .gitkeep file. Both are readable; n8n-state writable (implicit from the compose mount, no `:ro`).

- [ ] **Step 8: Verify write access**

```bash
ssh n8n-automation 'docker exec n8n sh -c "echo test > /home/node/n8n-state/.write-test && cat /home/node/n8n-state/.write-test && rm /home/node/n8n-state/.write-test"'
```

Expected: `test` on stdout, no errors.

---

## Task 6: Rewrite the Extract Signal prompt for canonical headings

**Purpose:** current Extract Signal prompt emits non-canonical headings. Rewrite the system message so its output parses against the retrieval server's strict taxonomy.

**Files:**
- Modify: `workflows/merged-call-summarizer.json`

### Steps

- [ ] **Step 1: Locate the Extract Signal node's system message**

The "LLM: Extract Signal" node is a `chainLlm` typeVersion 1.9 node at `workflows/merged-call-summarizer.json:55-74`. Its System Message Prompt Template is in `parameters.messages.messageValues[0].message` (look for the messageTemplate with `"type": "SystemMessagePromptTemplate"`).

The current system message ends with a "CRITICAL: output sections in EXACTLY this order" directive listing the old six headings. We need to replace those headings.

- [ ] **Step 2: Rewrite the prompt**

Replace the full system message text with the following. Keep all other node properties unchanged (id, name, position, model references, credentials).

```text
You are analysing a merged coaching-call transcript (chat log + spoken transcript). Extract the signal — the information that would help a future reader understand what was discussed, who said what, and what artefacts or resources were referenced.

Emit a markdown document with exactly six H2 sections, in the order listed below. Every heading must be the literal lowercase single-word slug shown. Do not invent new sections. Omit a section entirely if there is no content for it.

## general

A 2–4 paragraph narrative overview of what the session covered. Factual, not promotional. Capture the main throughline, which projects/topics came up, and who presented.

## insights

Bullet points of the most valuable takeaways, patterns, or heuristics surfaced during the call. Each bullet is self-contained (understandable without the surrounding context). Attribute the speaker when it matters.

## qa

Pairs of questions and answers. Format:
**Q (Questioner):** ...
**A (Answerer):** ...

Include only Q/A exchanges where both sides had real content — skip throwaway clarifying questions.

## tools

Bullet list of tools, products, frameworks, platforms, or services that were mentioned or demonstrated. One line per tool. Include a 5–15 word note on the context in which it came up.

## links

Bullet list of URLs, repositories, documents, or external resources shared during the call. One line per resource. Include a brief descriptor.

## decisions

Bullet list of commitments, action items, or decisions made during the call — things someone said they would do, or that the group agreed on. Phrase each as an actor + action.

CRITICAL: output the sections in EXACTLY this order: general, insights, qa, tools, links, decisions. Do not re-order, do not merge, do not rename. Use lowercase single-word slugs as shown.
```

- [ ] **Step 3: Re-import the workflow into n8n** (if editing the JSON directly) **OR edit the System Message in the n8n UI and re-export**

Two equivalent paths:

**Path A — edit JSON + re-import:**
```bash
# JSON edit done in Step 2 above. Copy to VM and re-import:
scp workflows/merged-call-summarizer.json n8n-automation:/tmp/merged-call-summarizer.json
ssh n8n-automation 'docker cp /tmp/merged-call-summarizer.json n8n:/tmp/workflow.json'
ssh n8n-automation 'docker exec n8n n8n import:workflow --input=/tmp/workflow.json'
```

Then in the n8n UI: re-link the OpenRouter credential on all four Chat Model nodes (import resets credential links per MEMORY.md).

**Path B — UI edit + export:**
Open n8n at `http://<vm>:5678`, open Merged Call Summarizer, edit the System Message on the "LLM: Extract Signal" node, Save. Then export: Click the `⋯` menu on the workflow → "Download" → overwrite `workflows/merged-call-summarizer.json` on the Mac Mini.

**Recommended: Path B** for this single-field edit (avoids the credential-relink hassle). Use Path A when structurally editing the JSON (later tasks).

- [ ] **Step 4: Manual verification — trigger a dry run**

In the n8n UI, with the file-pair for a known-good session already in `./watch/`, click "Test workflow" on the Merged Call Summarizer. When it reaches "Save extracted-signal.md", check `./output/<date>/extracted-signal.md` via:

```bash
ssh n8n-automation 'grep -n "^## " ~/n8n/output/<YYYY-MM-DD>/extracted-signal.md'
```

Replace `<YYYY-MM-DD>` with the test session's date. Expected: heading slugs `## general`, `## insights`, `## qa`, `## tools`, `## links`, `## decisions` in that order (any may be omitted if the LLM judged the section empty).

If any non-canonical heading appears ("Summary", "Key Insights", etc.), the prompt rewrite didn't take — re-export and verify.

- [ ] **Step 5: Commit the workflow JSON**

```bash
git add workflows/merged-call-summarizer.json
git commit -m "$(cat <<'EOF'
feat(workflows): rewrite Extract Signal prompt for canonical headings

The retrieval server's ingestion parser requires a strict section
taxonomy (general, insights, qa, tools, links, decisions). The previous
prompt emitted human-friendly headings (Summary, Key Insights, ...) that
fail parse at /ingest. This rewrite keeps the same semantic groupings
but uses the canonical lowercase slugs and adds an explicit
CRITICAL-order anchor so the LLM doesn't reshuffle.

Verified against a live weekly session: all six headings present in the
correct order, extracted-signal.md now parses through the server's
strict taxonomy.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 7: Add prep-prompt parallel branch to Workflow 1

**Purpose:** produce `prepared-transcript.md` so `/ingest` receives the third artifact type.

**Files:**
- Modify: `workflows/merged-call-summarizer.json`

The branch has 3 nodes: HTTP GET for the alias block, LLM Chain for prep-prompt, Code node for file save. It forks from "Code: Create Output Folder" (already has `transcriptText` + `outputDir` in `$json`) and rejoins the main flow via a Merge node before the final `/ingest` POST.

### Steps

- [ ] **Step 1: In n8n UI, open Merged Call Summarizer; add the new nodes**

Add these three nodes (drag from the node palette), positioned below the existing Extract Signal chain:

1. **HTTP Request: Get Speaker Aliases**
   - Type: `HTTP Request` (n8n-nodes-base.httpRequest, typeVersion 4.2)
   - Method: GET
   - URL: `http://retrieval-server:8999/speaker-aliases-block`
   - Response format: "Text"
   - Timeout: 10000 (10s)
   - Connect input from "Code: Create Output Folder"

2. **LLM: Prep-Prompt**
   - Type: `Basic LLM Chain` (@n8n/n8n-nodes-langchain.chainLlm, typeVersion 1.9)
   - Connect a new **OpenRouter Chat Model** sub-node (typeVersion 1) with the same credentials as the other four in this workflow; set `model` to `anthropic/claude-sonnet-4.6`.
   - System Message Prompt Template: paste the full content of `community-brain/config/extraction-prompts/prep-prompt-v1.md` as the template text. In n8n, the `{{SPEAKER_ALIASES_BLOCK}}` placeholder will be expression-substituted — edit it to reference the previous HTTP node's output: replace the literal `{{SPEAKER_ALIASES_BLOCK}}` inside the prompt text with an n8n expression `{{ $('HTTP Request: Get Speaker Aliases').item.json.data }}` (or the exact field name the HTTP node emits its text body as — verify in Test Step).
   - Human Message: `{{ $json.transcriptText }}` (the raw transcript, already carried through from Validate)
   - Connect main input from "HTTP Request: Get Speaker Aliases"

3. **Code: Save prepared-transcript.md**
   - Type: Code (n8n-nodes-base.code, typeVersion 2)
   - JavaScript code:

```javascript
const fs = require('fs');
const outputDir = $json.outputDir;
const content = $json.text || $json.output || $json.response;
if (!content) {
  throw new Error('Prep-prompt produced no content; refusing to write empty prepared-transcript.md');
}
fs.writeFileSync(`${outputDir}/prepared-transcript.md`, content, 'utf8');
return { json: { ...$json } };
```

Connect from "LLM: Prep-Prompt".

- [ ] **Step 2: Set up rejoin at `/ingest`**

Later tasks add the final `/ingest` POST node. For now, ensure both branches (the existing Extract Signal chain ending at "Code: Save weekly-invite.md" AND the new prep-prompt chain ending at "Code: Save prepared-transcript.md") leave their output wires disconnected — Task 8 will add a Merge node to rejoin them.

- [ ] **Step 3: Export the workflow to JSON and save**

In the n8n UI: `⋯` menu on the workflow → "Download". Save to `workflows/merged-call-summarizer.json` on the Mac Mini, overwriting the existing file.

- [ ] **Step 4: Manual verification — trigger a run, confirm `prepared-transcript.md` lands**

Trigger the workflow from n8n UI on a known-good `./watch/` file pair. When it completes:

```bash
ssh n8n-automation 'ls -la ~/n8n/output/<YYYY-MM-DD>/ | grep prepared-transcript'
ssh n8n-automation 'head -30 ~/n8n/output/<YYYY-MM-DD>/prepared-transcript.md'
```

Expected: file exists, ~1–10 KB depending on transcript length. Content begins with `=== SESSION ===`, contains `<!--SEGMENT` blocks with `topic:`, `speakers:`, `keywords:`, `summary:` headers, and transcript lines prefixed by `[HH:MM:SS]`.

If the alias block is stale (e.g. a known speaker doesn't match its canonical name), check the HTTP Request node's Last Output tab in n8n to confirm the block was fetched successfully — prep-prompt only works if the block substitution ran.

- [ ] **Step 5: Commit**

```bash
git add workflows/merged-call-summarizer.json
git commit -m "$(cat <<'EOF'
feat(workflows): add prep-prompt parallel branch to Workflow 1

New branch forks from Code: Create Output Folder, does
HTTP GET /speaker-aliases-block, runs the prep-prompt via a new chainLlm
node against the raw transcript, and writes prepared-transcript.md.
Does not touch the existing Extract Signal / Community Post / Compress /
Weekly Invite chain.

The merge + /ingest POST that bundles this with the existing artifacts
lands in the next commit.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 8: Add `/ingest` POST + error-log fallback to Workflow 1

**Purpose:** close the loop — once both branches complete, POST the three artifact paths to the retrieval server.

**Files:**
- Modify: `workflows/merged-call-summarizer.json`

### Steps

- [ ] **Step 1: In n8n UI, add the Merge node**

Add:

- **Merge: Rejoin Branches**
  - Type: Merge (n8n-nodes-base.merge, typeVersion 3)
  - Mode: "Pass through" (or equivalent — the default that passes the first branch's `$json` through works, since both branches carry `datePrefix` and `outputDir` from upstream).

Connect:
- Input 1: from "Code: Save weekly-invite.md" (last node of the existing chain)
- Input 2: from "Code: Save prepared-transcript.md"

- [ ] **Step 2: Add the HTTP Request: POST /ingest node**

- **HTTP Request: POST /ingest**
  - Type: HTTP Request (typeVersion 4.2)
  - Method: POST
  - URL: `http://retrieval-server:8999/ingest`
  - Authentication: None (Plan B leaves auth disabled; future task will flip to X-API-Key when server auth is enabled)
  - Body content type: JSON
  - Specify Body: Using JSON, expression:

```javascript
{{
  ({
    session_id: $json.datePrefix,
    session_date: $json.datePrefix,
    session_title: `Weekly call ${$json.datePrefix}`,
    artifact_paths: {
      prepared_transcript: `/data/output/${$json.datePrefix}/prepared-transcript.md`,
      extracted_signal:    `/data/output/${$json.datePrefix}/extracted-signal.md`,
      community_post:      `/data/output/${$json.datePrefix}/community-post.md`
    },
    force_reextract: false
  })
}}
```

  - Timeout: 600000 (10 min)
  - Retry on failure: enabled
    - Max tries: 2 (original + 1 retry)
    - Wait between tries: 60000 ms (60s)
    - Retry only on 4xx/5xx responses
  - On Error: "Continue on Error" (so downstream error-logging still runs)

Connect input from "Merge: Rejoin Branches".

- [ ] **Step 3: Add the error-log fallback node**

- **Code: Log Ingest Error**
  - Type: Code (typeVersion 2)
  - Connects from "HTTP Request: POST /ingest"
  - JS:

```javascript
const fs = require('fs');
const outputDir = `/home/node/output/${$json.datePrefix}`;
const err = $input.first().error;
if (!err) {
  // POST /ingest succeeded. No log needed; pass through.
  return { json: { ...$json, ingest_status: 'ok' } };
}
const ts = new Date().toISOString();
const body = `[${ts}] /ingest failed after retry\n` +
             `status: ${err.httpCode || 'n/a'}\n` +
             `message: ${err.message}\n` +
             `response: ${JSON.stringify(err.response || {}, null, 2)}\n`;
fs.writeFileSync(`${outputDir}/ingest-error.log`, body, 'utf8');
return { json: { ...$json, ingest_status: 'failed', ingest_error: err.message } };
```

Note: the exact property name for n8n's error object on "Continue on Error" is `$input.first().error` in recent n8n versions; if the engineer finds it's different in this deployment, adjust to match.

- [ ] **Step 4: Export the workflow JSON and save to `workflows/merged-call-summarizer.json`**

- [ ] **Step 5: Manual live-call verification**

Wait for or arrange one live weekly call (or reuse a recent known-good file pair in `./watch/` if one's available). Trigger the workflow. After completion:

```bash
# Artifacts on disk
ssh n8n-automation 'ls -la ~/n8n/output/<YYYY-MM-DD>/'
# Expected: 6 files -- transcript.txt, extracted-signal.md, community-post.md,
#                      community-post-compressed.md, <YYYY-MM-DD>-weekly-invite.md,
#                      prepared-transcript.md. If /ingest failed, a 7th:
#                      ingest-error.log.

# Server-side view
ssh n8n-automation 'curl -s http://127.0.0.1:8999/sessions | python3 -m json.tool | head -40'
# Expected: the new session appears with chunk_counts for all 3 types.

# Vector search check
printf '{"question":"<a phrase from the session>","top_k":3}' | \
  ssh n8n-automation "curl -s http://127.0.0.1:8999/query \
    -H 'Content-Type: application/json' --data-binary @-" | head -c 600
# Expected: top result has ground_truth.session_id matching the new session.
```

- [ ] **Step 6: Commit**

```bash
git add workflows/merged-call-summarizer.json
git commit -m "$(cat <<'EOF'
feat(workflows): wire Workflow 1 /ingest POST + error-log fallback

Merge node rejoins the existing Extract Signal chain and the new
prep-prompt branch, then POSTs the three artifact paths to /ingest with
a 10-min timeout and one retry on non-2xx. On persistent failure the
workflow continues (artifacts stay on disk as the weekly deliverable)
and a Code node writes ingest-error.log into the session's output dir.

Closes the Workflow 1 extension -- a live weekly session now lands in
LanceDB automatically.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 9: Verify Workflow 1 end-to-end on the VM

**Purpose:** exit criterion for Phase 3.

### Steps

- [ ] **Step 1: Confirm the latest workflow JSON is deployed on the VM**

The live n8n instance reads its workflows from its own database (`./data/` mount), not from the `workflows/` folder. Either (a) the UI edits in Tasks 6–8 already persisted to the live instance, or (b) the JSON was imported via `docker exec n8n n8n import:workflow`. Confirm which:

```bash
ssh n8n-automation 'docker exec n8n n8n export:workflow --id=5 --output=/tmp/live-wf.json && docker cp n8n:/tmp/live-wf.json /tmp/live-wf.json && cat /tmp/live-wf.json | python3 -c "import json,sys; d=json.load(sys.stdin); print([n[\"name\"] for n in d[\"nodes\"]])"'
```

Expected output includes: `Code: Save prepared-transcript.md`, `HTTP Request: Get Speaker Aliases`, `LLM: Prep-Prompt`, `HTTP Request: POST /ingest`, `Code: Log Ingest Error`, `Merge: Rejoin Branches`. If any are missing, the UI changes didn't persist; re-import from `workflows/merged-call-summarizer.json`.

- [ ] **Step 2: Drop a known file pair in `./watch/` and run end-to-end**

Pick a recent historical session (ensure NOT already ingested — check `/sessions` first). Copy its transcript to `./watch/<YYYY-MM-DD>-transcript.txt` and manually compose a minimal chat log at `./watch/<YYYY-MM-DD>-zoom-chat.txt` (e.g. two lines of placeholder text). Trigger the workflow from n8n UI.

- [ ] **Step 3: Capture the full session summary**

```bash
# Save the ingest response for record
ssh n8n-automation "curl -s http://127.0.0.1:8999/sessions/<YYYY-MM-DD> | python3 -m json.tool"
# Expected: chunk_counts {prepared_transcript: N, extracted_signal: M, community_post: K},
#           session_themes populated, unresolved_question_count reasonable.
```

- [ ] **Step 4: Exit criterion**

If:
- All 6 output files are on disk (no `ingest-error.log`)
- `/sessions/<YYYY-MM-DD>` returns the session with chunk_counts across all 3 types
- A vector `/query` for a phrase known to be in the session returns that session in the top results
- No regressions in prior sessions (`/sessions` still shows earlier entries like `2026-04-14-FULLTEST`)

then Phase 3 is DONE. Move to Task 10.

If any criterion fails, debug before continuing to Workflow 2 — the two workflows share the same `/ingest` path and the same prompt format contracts.

No commit — this task is verification only.

---

## Task 10: Draft the transcript-only Community Post prompt

**Purpose:** Workflow 2 needs a Community Post prompt that works on transcript alone (no chat log context). This is a writing task — draft it carefully, review the result.

**Files:**
- The prompt text is drafted here and embedded inline in the Workflow 2 JSON in Task 12. No standalone file.

### Steps

- [ ] **Step 1: Read the live Community Post prompt for voice/style anchor**

Open `workflows/merged-call-summarizer.json` and find the "LLM: Community Post" node's System Message. Note: it references chat-log context ("based on member reactions in chat", "threads members started", etc.). Our transcript-only version has to drop those cues.

- [ ] **Step 2: Draft the new prompt**

Use this as the starting point. Tune the voice to match the live community-post style (which the user has calibrated over many weekly runs):

```text
You are writing a polished community-post recap of a historical coaching call that took place on {{session_date}}. The only input you have is the spoken transcript — there is no chat log for this session. Produce a markdown document that a community member would find useful when scanning the archive weeks or months later.

Structure your post to mirror the voice of the live weekly recap: warm but information-dense, focused on what was discussed and what listeners would want to revisit. Do NOT invent chat-log banter, "someone mentioned in chat" references, or reactions you cannot verify from the transcript alone.

Required structure:

📝 SUMMARY

Two paragraphs. What the call covered, who presented, the main throughline.

💡 KEY INSIGHTS

Bullet list of the most valuable takeaways. Each bullet is self-contained and understandable out of context. Attribute speakers by canonical name where it matters.

🛠️ TOOLS & CONCEPTS

Bullet list of tools, products, frameworks, or concepts introduced or discussed. Brief context line per item.

🔗 RESOURCES

Links, repositories, documents, videos that were referenced during the call. Descriptor per item.

🎯 FOLLOW-UPS

Things participants said they would do, decisions made, or open questions flagged for a future call.

Keep total length between 400 and 800 words. Write in present tense where referring to ideas, past tense for specific interactions ("Alexandra explained ...", "Patrick shared ..."). Do not include timestamps. Do not include any text above 📝 SUMMARY or below the last 🎯 FOLLOW-UPS bullet.
```

- [ ] **Step 3: Review by reading aloud**

Read the draft top-to-bottom, checking:
- No residual chat-log assumptions
- No placeholder text (`<description>`, `<item>`, etc.)
- Voice matches the live community-post style
- Section headings match the live style (emoji + uppercase) so retrieval queries across both live and historical corpora hit consistent surface text
- Transcript-only cues are explicit (attribute by canonical name)

Hold this prompt text for Task 12; no file is committed yet.

---

## Task 11: Create Workflow 2 skeleton — trigger, state load, folder iteration

**Purpose:** build the outer loop of Workflow 2. Per-session LLM calls are added in Task 12.

**Files:**
- Create: `workflows/transcript-only-summarizer.json` (write via n8n UI, then export)

### Steps

- [ ] **Step 1: In n8n UI, create a new empty workflow named "Transcript-Only Summarizer"**

Start with these nodes (left-to-right):

1. **Manual Trigger** (n8n-nodes-base.manualTrigger, typeVersion 1). No parameters.

2. **Code: Load State File**
   - Type: Code (typeVersion 2)
   - JS:

```javascript
const fs = require('fs');
const path = '/home/node/n8n-state/backfill-state.json';
let state = { schema_version: '1', last_updated: null, completed: [], failed: [] };
if (fs.existsSync(path)) {
  try {
    state = JSON.parse(fs.readFileSync(path, 'utf8'));
  } catch (e) {
    throw new Error(`Failed to parse ${path}: ${e.message}. Backup the file and restart.`);
  }
}
const completedIds = new Set((state.completed || []).map(s => s.session_id));
return { json: { state, completedIds: Array.from(completedIds) } };
```

3. **Code: List Historical Folders**
   - Type: Code (typeVersion 2)
   - JS:

```javascript
const fs = require('fs');
const path = require('path');

const historicalDir = '/home/node/historical';
const completedSet = new Set($json.completedIds);

const folders = fs.readdirSync(historicalDir, { withFileTypes: true })
  .filter(d => d.isDirectory())
  .map(d => d.name)
  .filter(name => /^\d{4}-\d{2}-\d{2}/.test(name));  // must start with YYYY-MM-DD

const sessions = [];
for (const folder of folders) {
  const folderPath = `${historicalDir}/${folder}`;
  const transcriptPath = `${folderPath}/transcript.md`;
  const metaPath = `${folderPath}/meta.json`;
  if (!fs.existsSync(transcriptPath)) continue;

  const datePrefix = folder.slice(0, 10);  // YYYY-MM-DD
  let meta = {};
  if (fs.existsSync(metaPath)) {
    try { meta = JSON.parse(fs.readFileSync(metaPath, 'utf8')); } catch {}
  }
  const recordingId = meta.recording_id ? String(meta.recording_id) : null;

  // Session id: YYYY-MM-DD unless that's already in completed -- then disambiguate
  let sessionId = datePrefix;
  if (completedSet.has(sessionId) && recordingId) {
    sessionId = `${datePrefix}-r${recordingId}`;
  }

  sessions.push({
    session_id: sessionId,
    session_date: datePrefix,
    session_title: meta.meeting_title || meta.title || `Historical call ${datePrefix}`,
    folder_path: folderPath,
    transcript_path: transcriptPath,
    recording_id: recordingId,
  });
}

// Skip already-completed
const pending = sessions
  .filter(s => !completedSet.has(s.session_id))
  .sort((a, b) => a.session_date.localeCompare(b.session_date));

// Return one item per session (n8n will iterate in SplitInBatches)
return pending.map(s => ({ json: s }));
```

4. **Split In Batches**
   - Type: n8n-nodes-base.splitInBatches, typeVersion 3
   - Batch Size: 1
   - Connect input from "Code: List Historical Folders"

Per-session processing nodes (Task 12) connect from "Split In Batches" output #0 (the current item). The "done" output (#1) connects to a summary node (Task 14).

- [ ] **Step 2: Test the skeleton with a dry state file**

On the VM:
```bash
ssh n8n-automation 'cat > ~/n8n/n8n-state/backfill-state.json <<EOF
{"schema_version":"1","last_updated":null,"completed":[],"failed":[]}
EOF'
```

In n8n UI, pin the output of each skeleton node and trigger the workflow. Verify:
- "Code: Load State File" returns `{ state: ..., completedIds: [] }`
- "Code: List Historical Folders" returns ~65 items, one per historical session
- "Split In Batches" is configured to emit one at a time

- [ ] **Step 3: Export and save to `workflows/transcript-only-summarizer.json`**

- [ ] **Step 4: Commit**

```bash
git add workflows/transcript-only-summarizer.json
git commit -m "$(cat <<'EOF'
feat(workflows): add Transcript-Only Summarizer skeleton

Manual Trigger + state file load + historical/ folder enumeration + meta
parsing + session-id disambiguation + SplitInBatches for iteration. No
per-session LLM processing yet -- that lands in the next commit.

The outer loop is deliberately small and inspectable: a dry run with an
empty state file enumerates all 65 historical sessions and passes them
one at a time to the next stage.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 12: Add per-session processing to Workflow 2

**Purpose:** for each session item from the SplitInBatches output, read transcript, fetch alias block, run 3 LLMs, write 3 artifacts.

**Files:**
- Modify: `workflows/transcript-only-summarizer.json`

### Steps

- [ ] **Step 1: Add per-session nodes in n8n UI**

Connect these after the SplitInBatches output #0 (current item):

1. **Code: Read Transcript**
   - JS:

```javascript
const fs = require('fs');
const transcriptText = fs.readFileSync($json.transcript_path, 'utf8');
// Create the output folder if it doesn't exist
const outputDir = `/home/node/output/${$json.session_id}`;
fs.mkdirSync(outputDir, { recursive: true });
return { json: { ...$json, transcriptText, outputDir } };
```

2. **HTTP Request: Get Speaker Aliases** (identical config to Workflow 1's version — same URL, method, text response).

3. **LLM: Prep-Prompt**
   - chainLlm typeVersion 1.9 + OpenRouter Chat Model sub-node (same model as Workflow 1: `anthropic/claude-sonnet-4.6`)
   - System Message: same prep-prompt-v1 text as Workflow 1, with the same `{{SPEAKER_ALIASES_BLOCK}}` substitution pattern pointing at this branch's HTTP Request output.
   - Human Message: `{{ $json.transcriptText }}`

4. **Code: Save prepared-transcript.md** — identical to Workflow 1's version.

5. **LLM: Extract Signal**
   - chainLlm + OpenRouter Chat Model
   - System Message: the canonical-heading Extract Signal prompt from Task 6 (paste identical text).
   - Human Message: `{{ $json.transcriptText }}`

6. **Code: Save extracted-signal.md**:

```javascript
const fs = require('fs');
fs.writeFileSync(`${$json.outputDir}/extracted-signal.md`, $json.text || $json.output, 'utf8');
return { json: { ...$json } };
```

7. **LLM: Community Post (historical)**
   - chainLlm + OpenRouter Chat Model
   - System Message: the full text drafted in Task 10.
   - Human Message: `{{ $json.transcriptText }}`

8. **Code: Save community-post.md**:

```javascript
const fs = require('fs');
fs.writeFileSync(`${$json.outputDir}/community-post.md`, $json.text || $json.output, 'utf8');
return { json: { ...$json } };
```

- [ ] **Step 2: Test with ONE historical session**

Before wiring up /ingest (Task 13), verify this stage on its own:

In n8n UI, temporarily pin the "Code: List Historical Folders" output to return only the first session. Trigger the workflow. Verify on the VM:

```bash
ssh n8n-automation 'ls -la ~/n8n/output/2025-02-02/ 2>/dev/null || ls -la ~/n8n/output/2025-02-02-r45179632/'
```

Expected: `prepared-transcript.md`, `extracted-signal.md`, `community-post.md`. Inspect each briefly to confirm plausible content.

- [ ] **Step 3: Export and commit**

```bash
git add workflows/transcript-only-summarizer.json
git commit -m "$(cat <<'EOF'
feat(workflows): add Workflow 2 per-session artifact generation

Per-session chain: read transcript + HTTP GET alias block + prep-prompt
LLM + extract-signal LLM + transcript-only community-post LLM, with
three Code nodes writing the markdown artifacts to
./output/<session_id>/. Same prompts as Workflow 1 for prep + signal;
new transcript-only community-post drafted in Task 10.

/ingest POST + state file update land in the next commit.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 13: Add `/ingest` POST, state-file update, and inter-session wait to Workflow 2

**Files:**
- Modify: `workflows/transcript-only-summarizer.json`

### Steps

- [ ] **Step 1: Add the /ingest POST node (same config as Workflow 1)**

- **HTTP Request: POST /ingest (Workflow 2)**
  - Method: POST
  - URL: `http://retrieval-server:8999/ingest`
  - Body (JSON expression):

```javascript
{{
  ({
    session_id: $json.session_id,
    session_date: $json.session_date,
    session_title: $json.session_title,
    artifact_paths: {
      prepared_transcript: `/data/output/${$json.session_id}/prepared-transcript.md`,
      extracted_signal:    `/data/output/${$json.session_id}/extracted-signal.md`,
      community_post:      `/data/output/${$json.session_id}/community-post.md`
    },
    force_reextract: false
  })
}}
```

  - Timeout: 600000 (10 min)
  - Retry: max 2 tries, 60s wait, non-2xx only
  - On Error: Continue on Error

Connect from "Code: Save community-post.md".

- [ ] **Step 2: Add the "Code: Update State File" node**

Connect from "HTTP Request: POST /ingest (Workflow 2)":

```javascript
const fs = require('fs');
const path = '/home/node/n8n-state/backfill-state.json';
const tmp = `${path}.tmp`;

let state = JSON.parse(fs.readFileSync(path, 'utf8'));
state.completed = state.completed || [];
state.failed = state.failed || [];
state.last_updated = new Date().toISOString();

const err = $input.first().error;
if (err) {
  state.failed = state.failed.filter(e => e.session_id !== $json.session_id);
  state.failed.push({
    session_id: $json.session_id,
    failed_at: state.last_updated,
    reason: err.message || 'unknown',
  });
} else {
  const body = $input.first().json;
  state.failed = state.failed.filter(e => e.session_id !== $json.session_id);
  state.completed.push({
    session_id: $json.session_id,
    completed_at: state.last_updated,
    chunks_written: (body && body.chunks_written) || 0,
  });
}

// Atomic write
fs.writeFileSync(tmp, JSON.stringify(state, null, 2), 'utf8');
fs.renameSync(tmp, path);

return { json: { ...$json, ingest_status: err ? 'failed' : 'ok' } };
```

- [ ] **Step 3: Add the Wait node**

- **Wait: Inter-session Delay**
  - Type: n8n-nodes-base.wait, typeVersion 1
  - Wait amount: 30 seconds

Connect from "Code: Update State File". Connect its output back to the SplitInBatches node's input — this is how n8n implements a loop: the "done" item comes back around.

- [ ] **Step 4: Wire the SplitInBatches "done" output (#1) to the summary node** (placeholder — Task 14 adds the node)

For now, leave it disconnected; Task 14 fills it in.

- [ ] **Step 5: Export and commit**

```bash
git add workflows/transcript-only-summarizer.json
git commit -m "$(cat <<'EOF'
feat(workflows): wire /ingest POST + state file + inter-session wait in Workflow 2

Per-session completion: POST /ingest (10-min timeout, 1 retry at 60s),
append to backfill-state.json's completed[] or failed[] depending on
HTTP result (atomic write via tmp+rename), wait 30s, loop.

State file semantics:
- completed entries never re-run automatically
- failed entries re-run on next invocation (transient failures retry;
  persistent failures repeat into the log for operator attention)
- Same session_id in failed gets overwritten on each attempt

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 14: Add end-of-run summary to Workflow 2

**Files:**
- Modify: `workflows/transcript-only-summarizer.json`

### Steps

- [ ] **Step 1: Add the summary node after SplitInBatches "done" output**

- **Code: Summary Report**
  - Connect from SplitInBatches output #1 ("done")
  - JS:

```javascript
const fs = require('fs');
const state = JSON.parse(fs.readFileSync('/home/node/n8n-state/backfill-state.json', 'utf8'));

const totalCompleted = (state.completed || []).length;
const totalFailed = (state.failed || []).length;
const recentFailures = (state.failed || [])
  .slice(-5)
  .map(f => `  - ${f.session_id}: ${f.reason}`)
  .join('\n') || '  (none)';

const summary = `Backfill run complete.

Completed (cumulative): ${totalCompleted}
Failed (cumulative):    ${totalFailed}
Last-updated:           ${state.last_updated}

Recent failures:
${recentFailures}
`;

console.log(summary);
return { json: { summary, totalCompleted, totalFailed } };
```

- [ ] **Step 2: Manual verification with a tiny run**

Edit the state file on the VM to make only 3 sessions eligible:

```bash
ssh n8n-automation 'python3 -c "
import json
with open(\"/home/pchouinard/n8n/n8n-state/backfill-state.json\") as f:
    s = json.load(f)
# Clear state
s[\"completed\"] = []
s[\"failed\"] = []
with open(\"/home/pchouinard/n8n/n8n-state/backfill-state.json\", \"w\") as f:
    json.dump(s, f, indent=2)
"'
```

Temporarily modify "Code: List Historical Folders" to `return pending.slice(0, 3);` (3 sessions only) for a quick sanity run. Trigger the workflow. Verify:
- 3 output folders appear under `./output/`
- Each folder has prepared-transcript.md + extracted-signal.md + community-post.md
- `backfill-state.json` has 3 entries in `completed`
- `/sessions` returns 3 new sessions with their correct chunk_counts
- Summary node's console output reads `Completed (cumulative): 3`

Revert the `slice(0, 3)` hack; re-export; commit.

- [ ] **Step 3: Export and commit**

```bash
git add workflows/transcript-only-summarizer.json
git commit -m "$(cat <<'EOF'
feat(workflows): add end-of-run summary report to Workflow 2

Terminal node reads the final backfill-state.json and prints cumulative
completed/failed counts plus the last 5 failure reasons. Logged to
n8n's execution history for operator review.

Verified on a 3-session dry run: state file updated correctly, all three
sessions landed in /sessions with full chunk_counts, summary output
accurate.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 15: Resume test — confirm Workflow 2 skips already-completed sessions

**Purpose:** prove the state file works across process boundaries.

### Steps

- [ ] **Step 1: With 3 sessions already in state.completed from Task 14, trigger Workflow 2 again**

Do NOT edit the state file. Trigger Workflow 2 from the UI.

- [ ] **Step 2: Verify the List step filters them out**

Check "Code: List Historical Folders" output: it should return the remaining 62 sessions, not 65.

- [ ] **Step 3: Halt the run after ~5 new sessions (simulate interruption)**

After about 5 new sessions complete (watch the state file or the execution view in n8n):

```bash
ssh n8n-automation 'docker exec n8n pkill -TERM -f "n8n.*workflow"' || echo "n8n handles SIGTERM cleanly or the workflow just finishes — observe what actually happens"
```

(n8n's exact interruption mechanics vary by version; easier path: just "Stop execution" from the UI after 5 sessions.)

- [ ] **Step 4: Verify state file reflects the 8 completions**

```bash
ssh n8n-automation 'cat /home/pchouinard/n8n/n8n-state/backfill-state.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(f\"completed: {len(d[\\\"completed\\\"])}\")"'
```

Expected: `completed: 8` (3 from Task 14 + 5 from Task 15).

- [ ] **Step 5: Resume — trigger the workflow again**

- [ ] **Step 6: Verify it picks up at session 9, not session 1**

Check the first session id emitted from "Code: List Historical Folders" — should be a date AFTER the 8th completed.

Optional: let the run continue for another 2-3 sessions to confirm forward progress, then stop it again. (Full 65-session backfill is Plan C scope per the spec; this plan's exit criterion is "resume works".)

No commit — verification only.

---

## Task 16: Validate Workflow 2 against the five spec query types (single-session reality check)

**Purpose:** sanity-check that the ingested historical chunks are actually queryable in the way the spec §10 Phase 6 query taxonomy expects. Full validation against all 5 query types across the 65-session corpus is Plan C; here we just prove one session produces reasonable retrieval behavior.

### Steps

- [ ] **Step 1: Pick one ingested historical session with known content**

From the state file, pick a session id that you're familiar with enough to form a target query.

- [ ] **Step 2: Run one query per type and spot-check**

```bash
SESSION_ID=<your picked session id>
for Q in \
  "how did approaches evolve over time" \
  "what tools were compared and what was said about each" \
  "what were the open questions participants raised" \
  "what did Brandon recommend about thumbnails" \
  "what decisions were made and what follow-ups flagged"
do
  echo "=== $Q ==="
  printf '{"question":"%s","top_k":3}' "$Q" | \
    ssh n8n-automation "curl -s http://127.0.0.1:8999/query \
      -H 'Content-Type: application/json' --data-binary @-" | \
    python3 -c "import json,sys; d=json.load(sys.stdin); [print(c['ground_truth']['chunk_id'], c['similarity']) for c in d['chunks'][:3]]"
  echo
done
```

Expected: each query returns 3 chunks, at least one of which should be from `$SESSION_ID` for a query specifically about that session's content. This is NOT a pass/fail gate for Plan B — it's a sanity check that ingestion didn't produce junk.

No commit — verification only.

---

## Task 17: Update documentation

**Purpose:** make Plan B's changes discoverable to the next operator.

**Files:**
- Modify: `CLAUDE.md`

### Steps

- [ ] **Step 1: Update the workflows section**

In `CLAUDE.md`, find the "## Workflows" section. Add a new subsection for the Transcript-Only Summarizer (placed after the Merged Call Summarizer section) and update the Merged Call Summarizer description to mention the new prep-prompt step and `/ingest` POST.

Insert after the existing "### Merged Call Summarizer" block, and BEFORE "### Fathom Transcript Poller":

```markdown
### Transcript-Only Summarizer (`workflows/transcript-only-summarizer.json`) — Backfill

Manual trigger. Iterates `./historical/<folder>/` session directories, reads `transcript.md` + `meta.json` per session, runs 3 LLM calls (prep-prompt, Extract Signal, transcript-only Community Post), writes 3 artifacts to `./output/<session_id>/`, then POSTs to `/ingest` on the retrieval server. State tracked in `./n8n-state/backfill-state.json`: `completed` entries are skipped, `failed` entries retry on next run.

Used for the one-time historical backfill. ~3 min per session; 30s inter-session delay. Resume-safe — kill the run anytime, restart, it picks up where it left off.
```

Also update the "### Merged Call Summarizer" description to mention the new prep-prompt branch:

Find the line that starts `Watches \`./watch/\` for Zoom chat logs and Fathom transcripts.` and after the existing step list, append:

```
Plan B (2026-04-19) added a parallel prep-prompt branch that writes `prepared-transcript.md` and a final `HTTP POST /ingest` to the retrieval server with all three artifact paths (prepared_transcript, extracted_signal, community_post). On `/ingest` failure the workflow logs to `./output/<date>/ingest-error.log` and still reports success (markdown artifacts always hit disk).
```

- [ ] **Step 2: Update "Current status"**

In `CLAUDE.md`'s "## Current status" section, update the "What's NOT yet done" list to reflect Plan B's completion:

- Remove the bullet about "Plan B — n8n workflow extensions. Two workflows to build..."
- Add under a new "Plan B — COMPLETE." heading, analogous to the existing "Plan A — COMPLETE." section, noting which commits landed the change

- [ ] **Step 3: Commit**

```bash
git add CLAUDE.md
git commit -m "$(cat <<'EOF'
docs(root): document Plan B workflows + update current status

Adds Transcript-Only Summarizer to the Workflows section. Updates the
Merged Call Summarizer description to mention the new prep-prompt
branch and /ingest POST. Marks Plan B complete in the Current Status
section.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
git push origin main
```

---

## Out of scope for this plan

Per spec §10, the following are explicitly NOT part of Plan B and should NOT be attempted by the implementer:

1. Fathom `summary.md` ingestion / deep-link citation UX.
2. Entity-registry block endpoint (parallel to speaker-aliases; add when a prompt needs it).
3. `/ingest` async / job-queue architecture.
4. `RETRIEVAL_API_KEY` enforcement across the stack.
5. Extracting workflow prompts out of JSON into standalone markdown files.
6. Stage B/C registry promotion UI or endpoints.
7. Open WebUI filter changes.
8. **Full 65-session backfill execution.** Plan B exits when Workflow 2 is proven on a small subset (Tasks 14–15). Plan C runs the full backfill.
9. Re-extraction of the `2026-04-14-FULLTEST` smoke-test session from pre-Plan-B validation.

If you hit any of these while working tasks 1–17, stop and escalate.

---

## Plan self-review notes

Covered each spec section in a task. No placeholders scanned clean. Function/endpoint names match across tasks (`render_alias_block`, `GET /speaker-aliases-block`, `backfill-state.json`). Rebuild step included after the first image-affecting change (Task 3). State-file path consistent (`/home/node/n8n-state/backfill-state.json`) everywhere it's referenced. Auth handling matches the existing `_verify_api_key` pattern so future `RETRIEVAL_API_KEY` flip works without route edits.

---

## References

- Spec: [docs/superpowers/specs/2026-04-19-plan-b-n8n-ingestion-integration-design.md](../specs/2026-04-19-plan-b-n8n-ingestion-integration-design.md)
- Plan A spec: [docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md](../specs/2026-04-18-community-brain-ingestion-pipeline-design.md)
- DEPLOYMENT runbook: [community-brain/docs/DEPLOYMENT.md](../../community-brain/docs/DEPLOYMENT.md)
- Current Workflow 1: [workflows/merged-call-summarizer.json](../../workflows/merged-call-summarizer.json)
- Prep-prompt template: [community-brain/config/extraction-prompts/prep-prompt-v1.md](../../community-brain/config/extraction-prompts/prep-prompt-v1.md)
