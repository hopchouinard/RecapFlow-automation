# Chapter 2 — Architecture Overview

**Category:** Philosophy & Framing
**Reading time:** 6 minutes

---

## System Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        Workstation (local)                         │
│                                                                 │
│  Zoom → ~/Documents/Zoom/<date> <time> <meeting>/              │
│           │                                                     │
│           ▼                                                     │
│  Automator Folder Action                                        │
│           │                                                     │
│           ▼                                                     │
│  sync-zoom-chats.sh                                             │
│    • Extracts YYYY-MM-DD from folder name                       │
│    • Renames to YYYY-MM-DD-zoom-chat.txt                        │
│    • rsync over SSH to VM                                       │
└──────────────────────────┬──────────────────────────────────────┘
                           │ rsync / SSH
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│              VM: n8n-automation.patchoutech.lab                  │
│                                                                 │
│  ~/n8n/watch/                                                   │
│    ├── YYYY-MM-DD-zoom-chat.txt      ← from Mac                 │
│    └── YYYY-MM-DD-transcript.txt     ← from Fathom poller       │
│                                                                 │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │                   Docker Compose                           │  │
│  │                                                            │  │
│  │  ┌──────────────────────┐    ┌──────────────────────────┐  │  │
│  │  │    n8n container     │    │   PostgreSQL (n8n_db)     │  │  │
│  │  │    :5678             │◄──►│   postgres:17             │  │  │
│  │  │                      │    │                          │  │  │
│  │  │  Workflows:          │    └──────────────────────────┘  │  │
│  │  │  • Fathom Poller     │                                  │  │
│  │  │  • Fathom List       │                                  │  │
│  │  │  • Fathom Fetch      │         External APIs            │  │
│  │  │  • Merged Summarizer │────────►  Fathom AI              │  │
│  │  │                      │────────►  OpenRouter (Claude)    │  │
│  │  └──────────────────────┘                                  │  │
│  └────────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ~/n8n/output/YYYY-MM-DD/                                       │
│    ├── transcript.txt                                           │
│    ├── extracted-signal.md                                       │
│    ├── community-post.md                                        │
│    ├── community-post-compressed.md                             │
│    └── YYYY-MM-DD-weekly-invite.md                              │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow

The system has two independent input paths that converge at the summarizer:

### Path A: Chat Log (immediate)

1. Zoom call ends → Zoom saves chat to `~/Documents/Zoom/<folder>/`
2. Automator Folder Action detects new folder
3. `sync-zoom-chats.sh` extracts the date, renames the file, rsyncs to VM
4. File lands in `~/n8n/watch/YYYY-MM-DD-zoom-chat.txt`
5. n8n Local File Trigger fires → checks for transcript → waits if absent

### Path B: Transcript (delayed, 5-60 minutes)

1. Fathom processes the meeting recording
2. Fathom Transcript Poller (every 15 min) detects new recording via API
3. Fetches transcript, formats as plain text
4. Saves to `~/n8n/watch/YYYY-MM-DD-transcript.txt`
5. Checks for chat log → if present, triggers Merged Call Summarizer

### Convergence

Whichever file arrives second finds the first and triggers the pipeline:

```
Chat log + Transcript
    → Merge (# MEETING TRANSCRIPT + # ZOOM CHAT LOG)
    → LLM: Extract Signal
    → LLM: Community Post (plain text)
    → LLM: Compress Post (plain text)
    → LLM: Weekly Invite (next Tuesday's date)
```

## Correlation Strategy

Both files are matched by their `YYYY-MM-DD` prefix:

| Source | Filename Pattern | Date Source |
|--------|-----------------|-------------|
| Workstation sync | `YYYY-MM-DD-zoom-chat.txt` | Zoom folder name |
| Fathom poller | `YYYY-MM-DD-transcript.txt` | `recording_start_time` field |

This works because both dates originate from the same meeting's start time — Zoom uses it for the folder name, Fathom records it as metadata.

## Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Workflow engine | n8n 2.10.4 (Docker) | Visual workflow automation |
| Database | PostgreSQL 17 | n8n workflow/credential storage |
| Transcript source | Fathom API | Meeting transcription |
| LLM inference | OpenRouter → Claude Sonnet 4.6 | Content generation |
| File sync | rsync over SSH | Workstation → VM file transfer |
| Trigger (Workstation) | Automator Folder Action | Detect new Zoom recordings |
| Community platform | Skool | Where posts are published |
