# Chapter 6 — Workflow: Fathom Transcript Poller

**Category:** Workflows
**Reading time:** 5 minutes

---

## Purpose

Polls the Fathom API every 15 minutes for new meeting recordings. When a new recording is found, fetches the transcript, formats it as plain text, and saves it to the watch directory. If the matching chat log is already present, triggers the Merged Call Summarizer.

**Workflow file:** `workflows/fathom-transcript-poller.json`
**n8n Workflow ID:** 2

## Node Flow

```
Schedule Trigger (every 15 min)
    → Code: Read Last Poll Time
    → HTTP Request: List Meetings (Fathom API)
    → Code: Check for New Recordings
    → HTTP Request: Fetch Transcript
    → Code: Format and Save Transcript
    → IF: Both Files Present
        ├── True → Execute Workflow (Merged Summarizer) → Update Poll Time
        └── False → Update Poll Time
```

## Key Nodes

### Schedule Trigger

Fires every 15 minutes. This interval balances responsiveness (Fathom typically processes transcripts within 5-60 minutes) against API rate limits (60 requests/minute).

### Code: Read Last Poll Time

Reads the last successful poll timestamp from `/home/node/.n8n/fathom-last-poll.txt`. If the file doesn't exist (first run), defaults to 24 hours ago.

```javascript
const fs = require('fs');
const pollFile = '/home/node/.n8n/fathom-last-poll.txt';
let lastPoll;
try {
  lastPoll = fs.readFileSync(pollFile, 'utf8').trim();
} catch (e) {
  const d = new Date();
  d.setHours(d.getHours() - 24);
  lastPoll = d.toISOString();
}
return { json: { lastPoll } };
```

### HTTP Request: List Meetings

Calls `GET https://api.fathom.ai/external/v1/meetings?created_after=<lastPoll>`. Returns paginated results (default 10 items). Only new meetings since the last poll are returned.

### Code: Check for New Recordings

Extracts the `items` array from the API response. Returns an empty array (stopping the workflow) if no new recordings exist. Otherwise, outputs one item per recording with `recording_id`, `title`, and timestamps.

### Code: Format and Save Transcript

Transforms the Fathom transcript JSON into readable plain text:

```
[00:01:29] shakur: How's it going, Tom?
[00:01:30] Patrick Chouinard: Hey, hello.
```

Saves to `/home/node/watch/YYYY-MM-DD-transcript.txt` and checks if the matching chat log exists.

### IF: Both Files Present

Branches based on whether both files are present. True branch triggers the summarizer via Execute Workflow. Both branches converge at the poll time update to ensure the timestamp is always updated, preventing reprocessing.

## State Management

The poller persists a single piece of state: the last poll timestamp, stored as an ISO 8601 string in a plain text file. This survives container restarts (the file is in the mounted `data` volume).

## Error Behavior

If the Fathom API is unreachable or returns an error, the workflow fails silently — the poll timestamp is not updated, so the next cycle will retry the same time range. No data is lost.
