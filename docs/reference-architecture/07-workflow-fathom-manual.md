# Chapter 7 — Workflow: Fathom Manual Lookup

**Category:** Workflows
**Reading time:** 5 minutes

---

## Purpose

Two utility workflows for manually fetching transcripts from the Fathom API. Used for testing, backfilling historical meetings, or debugging. These workflows are never activated — they run only when manually triggered from the n8n UI.

## Workflow A: List Recordings

**Workflow file:** `workflows/fathom-list-recordings.json`
**n8n Workflow ID:** 3

### Node Flow

```
Manual Trigger
    → Code: Set Date Parameter
    → HTTP Request: List Meetings by Date
    → Code: Format Recording List
```

### Usage

1. Open the workflow in n8n
2. Click the "Code: Set Date Parameter" node
3. Change `targetDate` to your desired date (e.g., `'2025-09-02'`)
4. Click "Test Workflow"
5. Check the output of the last node for a list of recordings

### Output Format

Each recording shows:

| Field | Description |
|-------|-------------|
| `recording_id` | Unique ID needed for Workflow B |
| `title` | Meeting title from calendar |
| `start_time` | When the recording started |
| `duration_minutes` | Computed from start/end times |
| `url` | Shareable Fathom link |

## Workflow B: Fetch Transcript

**Workflow file:** `workflows/fathom-fetch-transcript.json`
**n8n Workflow ID:** 4

### Node Flow

```
Manual Trigger
    → Code: Set Recording ID
    → HTTP Request: Get Meeting Details
    → Code: Find Meeting and Extract Date
    → HTTP Request: Fetch Transcript
    → Code: Format and Save Transcript
```

### Usage

1. Run Workflow A to get the `recording_id`
2. Open this workflow in n8n
3. Click "Code: Set Recording ID"
4. Set `recordingId` to the value from Workflow A
5. Set `targetDate` to the same date (needed to filter the meetings API)
6. Click "Test Workflow"
7. Check the output — it tells you whether the matching chat log was found

### Why Two Separate Workflows?

n8n doesn't natively support interactive "pick from a list" mid-workflow. The two-step approach is simple: list recordings, note the ID, fetch the transcript. For occasional testing use, this is more reliable than a complex single workflow.

### Design Note: Sequential Over Parallel

The original design used parallel HTTP requests (transcript fetch + meeting details simultaneously) merged via an n8n Merge node. This failed in n8n 2.10.4 — the Merge node's `mergeByPosition` mode requires match fields that don't apply to this use case. The fix was to make the flow purely sequential, using `$('NodeName').item.json` references to access data from earlier nodes. Simpler and more reliable.

## Backfilling Historical Meetings

To process an old meeting:

1. Run List Recordings with the meeting date
2. Run Fetch Transcript with the recording ID
3. Drop the matching chat log into `~/n8n/watch/YYYY-MM-DD-zoom-chat.txt`
4. The Merged Call Summarizer's Local File Trigger will detect the new file, find the transcript, and run the full pipeline
