# Chapter 9 — Testing & Debugging

**Category:** Operations
**Reading time:** 6 minutes

---

## Testing Approaches

The system supports three testing strategies, from fully synthetic to fully realistic.

### 1. Pure File Drop (Synthetic)

The simplest test — no API calls, no external dependencies. Place two files in the watch directory:

```bash
# Create fake test files
echo "Test chat content" > ~/n8n/watch/2025-01-01-zoom-chat.txt
echo "Test transcript content" > ~/n8n/watch/2025-01-01-transcript.txt
```

The second file triggers the Merged Call Summarizer. This tests the rendezvous logic, merge formatting, LLM chain, and output file creation.

**Limitation:** The LLM output won't be meaningful since the input is trivial. Good for testing plumbing, not prompt quality.

### 2. Real Fathom Data (Semi-Realistic)

Uses real transcript data from the Fathom API paired with a real chat log:

1. Run "Fathom: List Recordings" with the meeting date
2. Note the `recording_id` from the output
3. Run "Fathom: Fetch Transcript" with that ID and date
4. Drop the matching chat log into `~/n8n/watch/`

This tests the full pipeline with real content. Ideal for prompt tuning.

### 3. Automated End-to-End (Production)

Activate the Fathom Transcript Poller and the Merged Call Summarizer. After the next real meeting:

1. Automator syncs the chat log to the VM
2. Fathom Poller detects the new recording and fetches the transcript
3. Whichever arrives second triggers the full pipeline
4. Outputs appear in `~/n8n/output/YYYY-MM-DD/`

## Triggering the File Watcher

The Local File Trigger watches for `add` events. When testing, you may need to force a new event:

```bash
# Remove and re-create a file to generate an "add" event
docker exec n8n sh -c 'cat /home/node/watch/FILE.txt > /tmp/backup.txt && rm /home/node/watch/FILE.txt'
sleep 3
docker exec n8n cp /tmp/backup.txt /home/node/watch/FILE.txt
```

Simply touching a file (`touch FILE.txt`) does not trigger an `add` event — the file must be removed and re-created.

**Important:** When using "Listen for event" in the n8n UI test mode, click the trigger node first, then create the file event. The trigger must be listening before the event occurs.

## Common Issues

### "Module 'fs' is disallowed"

Code nodes cannot use `require()` by default. Ensure `NODE_FUNCTION_ALLOW_BUILTIN=fs,path` is set in `docker-compose.yml` and the container has been restarted.

### "Unknown node type" for Local File Trigger

The Local File Trigger is disabled by default since n8n 2.0. Ensure `NODES_EXCLUDE=[]` is set in `docker-compose.yml`.

### Credential links reset after import

Every `n8n import:workflow` resets credential references to placeholder values. You must re-link credentials in the n8n UI after each import. This is expected behavior.

### Fathom recording not found

The `/meetings` endpoint returns paginated results (default 10). If searching for an old recording, filter by date:

```
GET /meetings?created_after=YYYY-MM-DDT00:00:00Z&created_before=YYYY-MM-DDT23:59:59Z
```

### Type mismatch on recording_id

Fathom's `recording_id` may arrive as a different type (string vs. number) depending on context. Always compare using `String()`:

```javascript
const meeting = meetings.find(m => String(m.recording_id) === String(recordingId));
```

### Merge node failures

n8n 2.10.4's Merge node with `mergeByPosition` mode requires match fields even when logically unnecessary. Avoid Merge nodes — use sequential flows with `$('NodeName').item.json` references instead.

### Output folder ENOENT

If the output folder is deleted or renamed while the workflow is running, file save nodes will fail. The "Create Output Folder" node runs early in the pipeline, so this only happens if the folder is externally modified during execution. Re-create the folder and re-trigger.

## Inspecting Outputs

```bash
# List output files for a specific date
docker exec n8n ls -la /home/node/output/2025-09-02/

# Read a specific output
docker exec n8n cat /home/node/output/2025-09-02/2025-09-09-weekly-invite.md

# Check if watch directory has pending files
docker exec n8n ls /home/node/watch/

# Check Fathom poll state
docker exec n8n cat /home/node/.n8n/fathom-last-poll.txt
```

## Reprocessing a Meeting

To reprocess a meeting (e.g., after prompt changes):

1. Delete the output folder: `docker exec n8n rm -rf /home/node/output/YYYY-MM-DD`
2. Ensure both files exist in `~/n8n/watch/`
3. Activate the Merged Call Summarizer's trigger (or trigger manually)
4. Re-create one of the files to generate an `add` event
