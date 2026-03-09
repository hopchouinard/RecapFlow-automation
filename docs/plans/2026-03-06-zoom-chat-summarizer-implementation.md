# Zoom Chat Summarizer Workflow — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build an n8n workflow that watches Google Drive for Zoom chat files, runs a 3-step LLM prompt chain via OpenRouter, and saves outputs back to Drive with error resilience.

**Architecture:** Single n8n workflow with sequential LLM calls. Each LLM step saves its output to Google Drive immediately after success. Error branches on each LLM node stop the chain while preserving prior outputs. All credentials use placeholders — user links them in UI.

**Tech Stack:** n8n v2.10.2, Google Drive API (OAuth2), OpenRouter API (HTTP Request), Claude Sonnet 4.6

---

### Task 1: Build the workflow JSON — Trigger and File Reading

**Files:**
- Create: `workflows/zoom-chat-summarizer.json`

**Step 1: Create the base workflow JSON with these nodes:**

- **Google Drive Trigger** — `n8n-nodes-base.googleDriveTrigger`
  - Event: file created
  - Folder: placeholder (user sets in UI)
  - Poll interval: every 5 minutes
  - Filter: `.txt` files

- **Google Drive: Download File** — `n8n-nodes-base.googleDrive`
  - Operation: download
  - File ID: `{{ $json.id }}` from trigger

- **Set: Extract Date** — `n8n-nodes-base.set`
  - Extract date from filename using expression: `{{ $json.name.match(/^\d{4}-\d{2}-\d{2}/)?.[0] ?? 'unknown-date' }}`
  - Store as `datePrefix`
  - Pass through `parentFolderId` from trigger
  - Pass through file content as `chatText`

- **Google Drive: Create Folder** — `n8n-nodes-base.googleDrive`
  - Operation: create folder
  - Folder name: `{{ $json.datePrefix }}`
  - Parent: `{{ $json.parentFolderId }}`

**Step 2: Verify JSON is valid**

Run: `docker exec n8n node -e "JSON.parse(require('fs').readFileSync('/tmp/workflow.json','utf8')); console.log('Valid JSON')"`

---

### Task 2: Add Prompt 1 — Extract Signal

**Files:**
- Modify: `workflows/zoom-chat-summarizer.json`

**Step 1: Add HTTP Request node for OpenRouter Prompt 1**

- Node: `n8n-nodes-base.httpRequest`
- Name: `LLM: Extract Signal`
- Method: POST
- URL: `https://openrouter.ai/api/v1/chat/completions`
- Authentication: generic header auth (placeholder credential)
  - Header: `Authorization`, Value: `Bearer {{credential}}`
- Body (JSON):
  ```json
  {
    "model": "anthropic/claude-sonnet-4.6",
    "messages": [
      {
        "role": "user",
        "content": "You are analyzing the raw Zoom chat of a weekly AI community call.\n\nYour job is to extract only the information that would still be useful to a community member reading it one week later.\n\nFocus especially on:\n- links and shared resources\n- useful question-and-answer pairs\n- practical insights and recommendations\n- tools, platforms, frameworks, and concepts mentioned\n- open questions or follow-ups worth revisiting\n\nReturn your analysis in the following structure:\n\n# Extracted Chat Signal\n\n## Shared Resources\nFor each useful link or resource, provide:\n- Title\n- URL if present\n- Why it matters\n\n## Key Q&A\nFor each useful question-and-answer pair, provide:\n- Question\n- Answer\n- Short synthesis if multiple people contributed\n\n## Key Insights\nList the most useful ideas, recommendations, warnings, practical tips, or mental models shared in the chat.\n\n## Tools and Concepts Mentioned\nList important tools, frameworks, products, or concepts mentioned, with a short explanation of why they mattered.\n\n## Follow-Ups Worth Revisiting\nList unresolved questions, open threads, or topics that would be worth revisiting in a future call.\n\nRules:\n- Ignore greetings, jokes, reactions, filler, emojis, and casual banter\n- Ignore duplicate content unless repetition adds meaning\n- Do not invent missing context\n- Do not force content into a section if nothing valuable is present\n- Keep only high-value signal\n- Rewrite messy chat language into clear professional language without changing meaning\n\nNow analyze the following Zoom chat log:\n\n{{ $json.chatText }}"
      }
    ]
  }
  ```
- Connect from: Create Folder node
- Error handling: `continueErrorOutput` enabled

**Step 2: Add Set node to extract LLM response text**

- Name: `Set: Signal Output`
- Value: `{{ $json.choices[0].message.content }}`
- Store as `signalText`
- Pass through `datePrefix` and `subfolderId`

**Step 3: Add Google Drive Upload for extracted-signal.md**

- Operation: upload
- File name: `extracted-signal.md`
- Parent folder: subfolder ID from create folder step
- Content: `{{ $json.signalText }}`

---

### Task 3: Add Prompt 2 — Community Post

**Files:**
- Modify: `workflows/zoom-chat-summarizer.json`

**Step 1: Add HTTP Request node for OpenRouter Prompt 2**

- Node: `n8n-nodes-base.httpRequest`
- Name: `LLM: Community Post`
- Same OpenRouter config as Prompt 1
- Body messages content:
  ```
  You are preparing a polished community post based on extracted Zoom chat insights from a weekly AI community call.

  Your audience is community members who may not have attended live but want the most useful value from the chat.

  Turn the extracted material below into a concise, polished, community-friendly post that complements:
  - the meeting video
  - the transcript summary
  - the Fathom recap

  Use the following structure:

  # Community Chat Highlights

  ## Shared Resources
  Present the most useful links and resources in a clean, easy-to-scan way.

  ## Key Q&A
  Present the most useful question-and-answer pairs clearly and concisely.

  ## Key Insights
  Summarize the strongest practical or strategic takeaways.

  ## Tools and Concepts Mentioned
  List important tools, frameworks, and concepts with short explanations.

  ## Follow-Ups Worth Exploring
  List open questions or topics worth revisiting if relevant.

  ## Summary
  Write one short paragraph summarizing the overall value and themes of the chat discussion.

  Rules:
  - Keep the post concise and skimmable
  - Preserve only the strongest value
  - Use polished, natural, professional language
  - Do not invent any information not present in the extracted analysis
  - Omit any section that has little or no useful content
  - Make the result feel ready to post with minimal editing

  Here is the extracted chat analysis:

  {{ $json.signalText }}
  ```
- Error handling: `continueErrorOutput` enabled

**Step 2: Add Set node + Google Drive Upload for community-post.md**

- Same pattern as Task 2
- Store as `communityPostText`
- Save as `community-post.md` in subfolder

---

### Task 4: Add Prompt 3 — Compressed Post

**Files:**
- Modify: `workflows/zoom-chat-summarizer.json`

**Step 1: Add HTTP Request node for OpenRouter Prompt 3**

- Node: `n8n-nodes-base.httpRequest`
- Name: `LLM: Compress Post`
- Body messages content:
  ```
  Condense the community post below by about 30 to 40 percent while preserving all high-value information.

  Goals:
  - make it easier to skim
  - remove repetition
  - keep links, useful Q&A, and strongest insights
  - preserve a professional, community-friendly tone

  Do not remove important resources or key takeaways.

  Here is the draft post:

  {{ $json.communityPostText }}
  ```
- Error handling: `continueErrorOutput` enabled

**Step 2: Add Set node + Google Drive Upload for community-post-compressed.md**

- Same pattern
- Save as `community-post-compressed.md` in subfolder

---

### Task 5: Wire Error Branches

**Step 1: Add error output connections on each LLM HTTP Request node**

- Each LLM node's error output connects to a `Stop and Error` node (or a `NoOp` node that halts the chain)
- This ensures: if Prompt 1 fails → chain stops, nothing saved; if Prompt 2 fails → signal already saved; if Prompt 3 fails → signal + community post already saved

---

### Task 6: Import and Verify

**Step 1: Copy workflow into container**

```bash
docker cp workflows/zoom-chat-summarizer.json n8n:/tmp/workflow.json
```

**Step 2: Import into n8n**

```bash
docker exec n8n n8n import:workflow --input=/tmp/workflow.json
```
Expected: workflow imported successfully

**Step 3: Verify in n8n UI**

- Open http://localhost:5678
- Navigate to Workflows
- Confirm "Zoom Chat Summarizer" appears
- Open it and verify all nodes are connected correctly
- User links Google Drive OAuth2 and OpenRouter API key credentials in the UI

---

### Task 7: Commit

**Step 1: Commit workflow file**

```bash
git add workflows/zoom-chat-summarizer.json docs/plans/
git commit -m "feat: add zoom chat summarizer n8n workflow"
```
