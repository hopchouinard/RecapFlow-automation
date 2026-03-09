# Merged Call Recap + Weekly Invite — Design Document

**Date:** 2026-03-08
**Goal:** Replace the current chat-only summarizer with a merged workflow that combines the Zoom chat log and Fathom transcript, then generates a weekly invite post with unique flavor from the previous week's content.

---

## Architecture Overview

Three n8n workflows replace the current single workflow:

1. **Fathom Transcript Poller** — scheduled polling of Fathom API
2. **Fathom Manual Lookup** — two-step manual testing workflow
3. **Merged Call Summarizer** — replaces current chat-only summarizer

### Data Flow

```
Mac Mini (Zoom chat log)              Fathom API (transcript)
        │                                      │
   rsync to VM                          Poller (every 15 min)
        │                              or Manual Lookup
        ▼                                      ▼
~/n8n/watch/YYYY-MM-DD-zoom-chat.txt   ~/n8n/watch/YYYY-MM-DD-transcript.txt
        │                                      │
        └──────── Both present? ───────────────┘
                       │
                       ▼
              Merged Call Summarizer
                       │
        ┌──────┬───────┼────────┬──────────────┐
        ▼      ▼       ▼        ▼              ▼
  transcript  signal  community compressed  weekly-invite
     .txt      .md     post.md   post.md       .md
```

---

## Workflow 1: Fathom Transcript Poller

**Type:** Scheduled (every 15 minutes)

**Flow:**
1. Schedule Trigger fires every 15 minutes
2. Code node reads last poll timestamp from `~/n8n/data/fathom-last-poll.txt` (defaults to 24 hours ago if file doesn't exist)
3. HTTP Request to Fathom API: `GET https://api.fathom.ai/external/v1/meetings?created_after=<last_poll_timestamp>`
4. For each new recording:
   a. HTTP Request to fetch transcript: `GET https://api.fathom.ai/external/v1/recordings/{recording_id}/transcript`
   b. Code node formats transcript entries into plain text: `[HH:MM:SS] Speaker: text`
   c. Code node extracts `YYYY-MM-DD` from `recording_start_time`
   d. Code node saves formatted transcript to `~/n8n/watch/YYYY-MM-DD-transcript.txt`
   e. Code node checks if `~/n8n/watch/YYYY-MM-DD-zoom-chat.txt` exists
   f. If both present: Execute Workflow node triggers Workflow 3 with the date prefix
5. Code node updates `fathom-last-poll.txt` with current timestamp

**Credentials:**
- Fathom API key via generic header auth (`X-Api-Key`)

**Error handling:**
- If Fathom API returns 429 (rate limit), log and skip — next poll will retry
- If API is unreachable, log error and continue — next poll will retry

---

## Workflow 2: Fathom Manual Lookup

**Type:** Manual trigger (two separate sub-workflows or two entry points)

### Step A — List Recordings

**Flow:**
1. Manual Trigger with parameter: `date` (string, format `YYYY-MM-DD`)
2. HTTP Request to Fathom API: `GET https://api.fathom.ai/external/v1/meetings?created_after=YYYY-MM-DDT00:00:00Z&created_before=YYYY-MM-DDT23:59:59Z`
3. Code node formats results as a list: title, recording_start_time, duration (computed from start/end), recording_id
4. Output displayed in execution results — user notes the desired `recording_id`

### Step B — Fetch Transcript

**Flow:**
1. Manual Trigger with parameter: `recording_id` (integer)
2. HTTP Request to Fathom API: `GET https://api.fathom.ai/external/v1/recordings/{recording_id}/transcript`
3. HTTP Request to get meeting metadata: `GET https://api.fathom.ai/external/v1/meetings` filtered to find this recording (for start time)
4. Code node formats transcript to plain text, extracts `YYYY-MM-DD` from `recording_start_time`
5. Code node saves to `~/n8n/watch/YYYY-MM-DD-transcript.txt`
6. Code node checks for matching chat log
7. If both present: Execute Workflow triggers Workflow 3

---

## Workflow 3: Merged Call Summarizer

**Type:** Replaces current `zoom-chat-summarizer.json`

### Entry Points

**Entry A — Local File Trigger:**
- Watches `~/n8n/watch/` for new files
- Code node validates: must be `.txt`, must match `YYYY-MM-DD-zoom-chat.txt` or `YYYY-MM-DD-transcript.txt`
- Extracts `YYYY-MM-DD` prefix
- Checks if the complementary file exists:
  - If chat log arrived → check for `YYYY-MM-DD-transcript.txt`
  - If transcript arrived → check for `YYYY-MM-DD-zoom-chat.txt`
- If both present: proceed to merge
- If only one: save and stop (the other workflow will trigger when the second file arrives)

**Entry B — Execute Workflow:**
- Called by Workflow 1 or 2 with `datePrefix` parameter
- Skips file detection, goes straight to merge

### Processing Chain

```
Merge Step
  → Code: Read both files, format as merged text with headers
  → Code: Create output folder ~/n8n/output/YYYY-MM-DD/
  → Code: Save transcript.txt (formatted raw transcript)

LLM Chain (4 steps, sequential)
  → LLM: Extract Signal (from merged transcript + chat content)
  → Code: Save extracted-signal.md
  → LLM: Community Post (from extracted signal)
  → Code: Save community-post.md
  → LLM: Compress Post (from community post)
  → Code: Save community-post-compressed.md
  → LLM: Weekly Invite (from compressed post + next Tuesday date)
  → Code: Save YYYY-MM-DD-weekly-invite.md (dated for next Tuesday)
```

### Merge Format

The merged text passed to the first LLM looks like:

```
# MEETING TRANSCRIPT

[00:01:29] shakur: How's it going, Tom?
[00:01:30] Patrick Chouinard: Hey, hello.
...

# ZOOM CHAT LOG

<raw chat log content>
```

---

## LLM Prompts

### Prompts 1-3: Extract Signal, Community Post, Compress Post

Same prompts as the current workflow, but updated to reference "transcript and chat log" instead of just "chat log." The Extract Signal prompt's intro changes to:

> You are analyzing the transcript and Zoom chat log of a weekly AI community call.

Everything else remains the same.

### Prompt 4: Weekly Invite (new)

**Input:** Compressed community post text + computed next Tuesday date

**System message:**

> You are writing a weekly invite post for an AI community coaching call. Your job is to create a post that encourages members to submit their questions in advance.
>
> You will be given the compressed community post from the most recent call. Use it to add unique flavor to this week's invite.
>
> The post MUST follow this exact structure:
>
> 1. **Opening hook** (1-3 sentences) — A playful, attention-grabbing opener that references a specific highlight, tool, insight, or unresolved question from last week's call. Make it intriguing enough that someone who missed last week wants to catch up.
>
> 2. **Standard section** (copy exactly as written below):
> ```
> HOW THE CALLS WORK
> The calls can run 2+ hours.
> We want to make sure we're respecting everyone's time. Especially those of you who actually show up.
>
> Here's the structure:
> Reply to this post with your questions before the call
> If you submit a question and you're on the call, you go first
> We work through questions in the order they came in
> Then we open it up for everyone else
>
> If you can't make the call but want your question answered, drop it in the comments. We'll get to it. But priority goes to people who are there.
>
> The goal is simple: if you're taking the time to show up, you shouldn't have to wait behind questions from people who aren't even on the call.
> ```
>
> 3. **Flavor bridge** (1-3 sentences) — Reference 2-3 specific unresolved questions, follow-ups, or topics from last week that people might want to continue. Mention people by first name only if they had open questions. Frame it as an invitation, not a call-out.
>
> 4. **Closing section** (copy exactly, but fill in the date):
> ```
> ZOOM LINK (save this)
> https://us06web.zoom.us/j/81995207847?pwd=Xe6u6LmIQOmCP5VTnOwWYjDBfZNKGB.1
>
> WHEN
> Tuesday [DATE] at 6PM ET
>
> Looking forward to seeing you on the call!
> ```
>
> Rules:
> - Tone: playful, welcoming, energetic — like a community leader who genuinely enjoys these calls
> - Do NOT call out anyone negatively or use inside jokes that exclude non-attendees
> - Do NOT invent information not present in the community post
> - Keep the opening hook and flavor bridge fresh and different each week
> - The standard section and closing section must be reproduced exactly (no modifications)
> - Total post length should feel like a quick, easy read — not a wall of text

---

## Next Tuesday Calculation

Code node logic to find the next Tuesday from the call date:

```javascript
const callDate = new Date(datePrefix + 'T12:00:00Z');
const dayOfWeek = callDate.getDay(); // 0=Sun, 1=Mon, 2=Tue...
const daysUntilTuesday = (2 - dayOfWeek + 7) % 7 || 7; // always next Tue, never same day
const nextTuesday = new Date(callDate);
nextTuesday.setDate(callDate.getDate() + daysUntilTuesday);
```

Format as: `Tuesday [Month] [Day][ordinal] at 6PM ET` (e.g., "Tuesday March 10th at 6PM ET")

---

## Correlation Strategy

- Chat log filename: `YYYY-MM-DD-zoom-chat.txt` (date from Zoom folder name via Mac sync script)
- Transcript filename: `YYYY-MM-DD-transcript.txt` (date from Fathom `recording_start_time`)
- Matched by shared `YYYY-MM-DD` prefix

---

## Credentials

| Service | n8n Credential Type | Auth Method |
|---------|-------------------|-------------|
| Fathom API | Generic Header Auth | `X-Api-Key: <key>` |
| OpenRouter | OpenRouter API | Existing credential (unchanged) |

---

## Output Structure

```
~/n8n/output/YYYY-MM-DD/
  ├── transcript.txt                    (formatted raw transcript)
  ├── extracted-signal.md               (signal from merged content)
  ├── community-post.md                 (polished community post)
  ├── community-post-compressed.md      (compressed for Skool)
  └── YYYY-MM-DD-weekly-invite.md       (next Tuesday's date in filename)
```

---

## Testing

1. **Pure file drop:** Place both `YYYY-MM-DD-zoom-chat.txt` and `YYYY-MM-DD-transcript.txt` in `~/n8n/watch/`. Second file triggers the full chain.
2. **Real Fathom data:** Run Workflow 2 Step A with a date → note recording_id → Run Step B to fetch transcript → drop matching chat log in `watch/`.
3. **Poller test:** Manually trigger Workflow 1 from n8n UI to verify API connectivity and polling logic.

---

## What Does NOT Change

- Mac-side Automator Folder Action and `sync-zoom-chats.sh` script
- rsync delivery of chat logs to `~/n8n/watch/`
- Docker Compose configuration (no new containers or volumes needed)
- OpenRouter credentials and model selection (Claude Sonnet 4.6)
