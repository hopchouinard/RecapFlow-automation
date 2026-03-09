# Zoom Chat Summarizer — n8n Workflow Design

## Overview

An n8n workflow that watches a Google Drive folder for Zoom chat `.txt` files, runs a 3-step LLM prompt chain via OpenRouter (Claude Sonnet 4.6), and saves the outputs back to Google Drive. Each step saves its output immediately for resilience.

## Trigger

- **Google Drive Trigger** node polls a configured folder for new `.txt` files
- Filename format: `YYYY-MM-DD-zoom-chat.txt` (e.g., `2026-03-06-zoom-chat.txt`)

## Workflow Flow

```
Google Drive Trigger (new .txt file)
  → Google Drive: Download File (read content)
  → Set: Extract date from filename
  → Google Drive: Create subfolder (e.g., "2026-03-06/")
  → HTTP Request: OpenRouter Prompt 1 (extract signal)
      → Google Drive: Save "extracted-signal.md"
      ↘ on error: Set error flag, stop chain
  → HTTP Request: OpenRouter Prompt 2 (community post)
      → Google Drive: Save "community-post.md"
      ↘ on error: Set error flag, stop chain
  → HTTP Request: OpenRouter Prompt 3 (compress)
      → Google Drive: Save "community-post-compressed.md"
      ↘ on error: Set error flag, stop chain
```

## Nodes Detail

### 1. Google Drive Trigger
- Polls a specific Google Drive folder for new files
- Filters for `.txt` files
- Requires Google Drive OAuth2 credentials configured in n8n

### 2. Google Drive: Download File
- Downloads the detected file content as text
- Passes raw chat text to the next node

### 3. Set: Extract Date from Filename
- Parses the date prefix from the filename (e.g., `2026-03-06` from `2026-03-06-zoom-chat.txt`)
- Stores as `{{ $json.datePrefix }}` for subfolder creation

### 4. Google Drive: Create Folder
- Creates a subfolder named `{{ $json.datePrefix }}` inside the same parent folder as the input file

### 5–7. HTTP Request: OpenRouter LLM Calls (x3)
- **Endpoint:** `https://openrouter.ai/api/v1/chat/completions`
- **Model:** `anthropic/claude-sonnet-4.6`
- **Auth:** OpenRouter API key in Authorization header
- Each prompt step:
  - **Prompt 1 (Extract Signal):** System prompt instructs extraction of links, Q&A, insights, tools, follow-ups from raw chat
  - **Prompt 2 (Community Post):** System prompt formats Prompt 1 output into a polished community post
  - **Prompt 3 (Compress):** System prompt condenses Prompt 2 output by 30–40%

### 8–10. Google Drive: Upload File (x3)
- After each successful LLM call, immediately saves the output to the date subfolder:
  - `extracted-signal.md`
  - `community-post.md`
  - `community-post-compressed.md`

### Error Handling
- Each LLM call has an error output branch
- On failure, an error flag is set and the chain stops
- All prior outputs are already saved to Drive, so no work is lost
- The workflow execution log in n8n shows where the failure occurred

## Output Structure

```
[Google Drive Watch Folder]/
└── 2026-03-06/
    ├── extracted-signal.md
    ├── community-post.md
    └── community-post-compressed.md
```

## Credentials Required

1. **Google Drive OAuth2** — for trigger, file read, folder creation, file uploads
2. **OpenRouter API Key** — for LLM calls via HTTP Request nodes

## Prompts

### Prompt 1: Extract Signal
Extracts structured information from raw Zoom chat: shared resources, Q&A pairs, key insights, tools/concepts mentioned, and follow-ups worth revisiting. Ignores greetings, jokes, filler.

### Prompt 2: Community Post
Transforms extracted signal into a polished, skimmable community post with sections for resources, Q&A, insights, tools, follow-ups, and a summary paragraph.

### Prompt 3: Compress
Condenses the community post by 30–40% while preserving all high-value information, links, Q&A, and key takeaways.

Full prompt text is defined in the user's spec and will be embedded directly in each HTTP Request node body.
