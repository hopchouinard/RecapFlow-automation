# Merged Call Recap + Weekly Invite — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace the chat-only summarizer with a merged workflow that combines Zoom chat logs and Fathom transcripts, adds a weekly invite generator, and includes a Fathom API poller + manual lookup workflows.

**Architecture:** Four n8n workflow JSON files. The Fathom poller and manual lookup workflows fetch transcripts and save them to `~/n8n/watch/`. The merged summarizer workflow detects when both a chat log and transcript are present for the same date, merges them, runs a 4-step LLM chain, and saves 5 output files. All workflows use the existing n8n Docker container with local filesystem access.

**Tech Stack:** n8n (Docker), Fathom API (`api.fathom.ai`), OpenRouter API (Claude Sonnet 4.6), local filesystem

---

### Task 1: Build Workflow — Fathom Transcript Poller

**Files:**
- Create: `workflows/fathom-transcript-poller.json`

**Step 1: Create the workflow JSON with these nodes:**

- **Schedule Trigger** — `n8n-nodes-base.scheduleTrigger`
  - ID: `b1000000-0000-4000-8000-000000000001`
  - Position: [0, 300]
  - Rule: every 15 minutes
  - Parameters:
    ```json
    {
      "rule": {
        "interval": [{ "field": "minutes", "minutesInterval": 15 }]
      }
    }
    ```

- **Code: Read Last Poll Time** — `n8n-nodes-base.code`
  - ID: `b1000000-0000-4000-8000-000000000002`
  - Position: [250, 300]
  - jsCode:
    ```javascript
    const fs = require('fs');
    const pollFile = '/home/node/.n8n/fathom-last-poll.txt';
    let lastPoll;
    try {
      lastPoll = fs.readFileSync(pollFile, 'utf8').trim();
    } catch (e) {
      // Default to 24 hours ago
      const d = new Date();
      d.setHours(d.getHours() - 24);
      lastPoll = d.toISOString();
    }
    return { json: { lastPoll } };
    ```

- **HTTP Request: List Meetings** — `n8n-nodes-base.httpRequest`
  - ID: `b1000000-0000-4000-8000-000000000003`
  - Position: [500, 300]
  - Method: GET
  - URL: `https://api.fathom.ai/external/v1/meetings`
  - Query parameters: `created_after={{ $json.lastPoll }}`
  - Authentication: genericCredentialType → httpHeaderAuth
  - Headers: `X-Api-Key` (from credential)
  - Parameters:
    ```json
    {
      "method": "GET",
      "url": "https://api.fathom.ai/external/v1/meetings",
      "sendQuery": true,
      "queryParameters": {
        "parameters": [
          { "name": "created_after", "value": "={{ $json.lastPoll }}" }
        ]
      },
      "authentication": "genericCredentialType",
      "genericAuthType": "httpHeaderAuth"
    }
    ```
  - Credentials:
    ```json
    {
      "httpHeaderAuth": {
        "id": "PLACEHOLDER",
        "name": "Fathom API Key"
      }
    }
    ```

- **Code: Check for New Recordings** — `n8n-nodes-base.code`
  - ID: `b1000000-0000-4000-8000-000000000004`
  - Position: [750, 300]
  - jsCode:
    ```javascript
    const items = $json.items || [];
    if (items.length === 0) {
      return [];
    }
    // Output one item per recording
    return items.map(meeting => ({
      json: {
        recording_id: meeting.recording_id,
        title: meeting.title,
        recording_start_time: meeting.recording_start_time,
        recording_end_time: meeting.recording_end_time
      }
    }));
    ```

- **HTTP Request: Fetch Transcript** — `n8n-nodes-base.httpRequest`
  - ID: `b1000000-0000-4000-8000-000000000005`
  - Position: [1000, 300]
  - Method: GET
  - URL: `=https://api.fathom.ai/external/v1/recordings/{{ $json.recording_id }}/transcript`
  - Authentication: same genericCredentialType → httpHeaderAuth
  - Parameters:
    ```json
    {
      "method": "GET",
      "url": "=https://api.fathom.ai/external/v1/recordings/{{ $json.recording_id }}/transcript",
      "authentication": "genericCredentialType",
      "genericAuthType": "httpHeaderAuth"
    }
    ```
  - Credentials: same Fathom API Key

- **Code: Format and Save Transcript** — `n8n-nodes-base.code`
  - ID: `b1000000-0000-4000-8000-000000000006`
  - Position: [1250, 300]
  - jsCode:
    ```javascript
    const fs = require('fs');
    const transcript = $json.transcript || [];
    const startTime = $('Code: Check for New Recordings').item.json.recording_start_time;
    const datePrefix = startTime.substring(0, 10);

    // Format transcript entries
    const formatted = transcript.map(entry => {
      const speaker = entry.speaker?.display_name || 'Unknown';
      const timestamp = entry.timestamp || '00:00:00';
      return `[${timestamp}] ${speaker}: ${entry.text}`;
    }).join('\n');

    const filename = `${datePrefix}-transcript.txt`;
    const filePath = `/home/node/watch/${filename}`;
    fs.writeFileSync(filePath, formatted, 'utf8');

    // Check if matching chat log exists
    const chatFile = `/home/node/watch/${datePrefix}-zoom-chat.txt`;
    const bothPresent = fs.existsSync(chatFile);

    return {
      json: {
        datePrefix,
        transcriptFile: filePath,
        chatFile,
        bothPresent,
        formatted
      }
    };
    ```

- **IF: Both Files Present** — `n8n-nodes-base.if`
  - ID: `b1000000-0000-4000-8000-000000000007`
  - Position: [1500, 300]
  - Conditions:
    ```json
    {
      "options": {},
      "conditions": {
        "options": { "caseSensitive": true, "leftValue": "" },
        "combinator": "and",
        "conditions": [
          {
            "id": "1",
            "operator": { "type": "boolean", "operation": "true" },
            "leftValue": "={{ $json.bothPresent }}",
            "rightValue": ""
          }
        ]
      }
    }
    ```

- **Execute Workflow: Trigger Summarizer** — `n8n-nodes-base.executeWorkflow`
  - ID: `b1000000-0000-4000-8000-000000000008`
  - Position: [1750, 200]
  - Parameters:
    ```json
    {
      "source": "parameter",
      "workflowId": "={{ $env.MERGED_SUMMARIZER_WORKFLOW_ID || '' }}",
      "options": {}
    }
    ```
  - Note: The workflow ID must be set after import. User will update this value in the n8n UI to point to the merged summarizer workflow ID.
  - Connected from IF node's true output (index 0)

- **Code: Update Last Poll Time** — `n8n-nodes-base.code`
  - ID: `b1000000-0000-4000-8000-000000000009`
  - Position: [1750, 400]
  - jsCode:
    ```javascript
    const fs = require('fs');
    const pollFile = '/home/node/.n8n/fathom-last-poll.txt';
    fs.writeFileSync(pollFile, new Date().toISOString(), 'utf8');
    return { json: { updated: true } };
    ```
  - Note: This node receives from BOTH the IF true branch (after Execute Workflow) AND the IF false branch, so it always updates the timestamp.

**Step 2: Wire the connections:**

```json
{
  "Schedule Trigger": {
    "main": [[{ "node": "Code: Read Last Poll Time", "type": "main", "index": 0 }]]
  },
  "Code: Read Last Poll Time": {
    "main": [[{ "node": "HTTP Request: List Meetings", "type": "main", "index": 0 }]]
  },
  "HTTP Request: List Meetings": {
    "main": [[{ "node": "Code: Check for New Recordings", "type": "main", "index": 0 }]]
  },
  "Code: Check for New Recordings": {
    "main": [[{ "node": "HTTP Request: Fetch Transcript", "type": "main", "index": 0 }]]
  },
  "HTTP Request: Fetch Transcript": {
    "main": [[{ "node": "Code: Format and Save Transcript", "type": "main", "index": 0 }]]
  },
  "Code: Format and Save Transcript": {
    "main": [[{ "node": "IF: Both Files Present", "type": "main", "index": 0 }]]
  },
  "IF: Both Files Present": {
    "main": [
      [{ "node": "Execute Workflow: Trigger Summarizer", "type": "main", "index": 0 }],
      [{ "node": "Code: Update Last Poll Time", "type": "main", "index": 0 }]
    ]
  },
  "Execute Workflow: Trigger Summarizer": {
    "main": [[{ "node": "Code: Update Last Poll Time", "type": "main", "index": 0 }]]
  }
}
```

**Step 3: Set workflow metadata:**

```json
{
  "id": "2",
  "name": "Fathom Transcript Poller",
  "active": false,
  "settings": { "executionOrder": "v1" },
  "pinData": {},
  "tags": []
}
```

**Step 4: Validate the JSON**

Run: `python3 -c "import json; json.load(open('workflows/fathom-transcript-poller.json')); print('Valid')"`

---

### Task 2: Build Workflow — Fathom List Recordings (Manual)

**Files:**
- Create: `workflows/fathom-list-recordings.json`

**Step 1: Create the workflow JSON with these nodes:**

- **Manual Trigger** — `n8n-nodes-base.manualTrigger`
  - ID: `c1000000-0000-4000-8000-000000000001`
  - Position: [0, 300]
  - Parameters: `{}`

- **Code: Set Date Parameter** — `n8n-nodes-base.code`
  - ID: `c1000000-0000-4000-8000-000000000002`
  - Position: [250, 300]
  - jsCode:
    ```javascript
    // ╔══════════════════════════════════════════╗
    // ║  CHANGE THIS DATE BEFORE RUNNING         ║
    // ╚══════════════════════════════════════════╝
    const targetDate = '2025-09-02';

    return {
      json: {
        targetDate,
        createdAfter: `${targetDate}T00:00:00Z`,
        createdBefore: `${targetDate}T23:59:59Z`
      }
    };
    ```

- **HTTP Request: List Meetings by Date** — `n8n-nodes-base.httpRequest`
  - ID: `c1000000-0000-4000-8000-000000000003`
  - Position: [500, 300]
  - Method: GET
  - URL: `https://api.fathom.ai/external/v1/meetings`
  - Query parameters: `created_after={{ $json.createdAfter }}`, `created_before={{ $json.createdBefore }}`
  - Authentication: genericCredentialType → httpHeaderAuth
  - Parameters:
    ```json
    {
      "method": "GET",
      "url": "https://api.fathom.ai/external/v1/meetings",
      "sendQuery": true,
      "queryParameters": {
        "parameters": [
          { "name": "created_after", "value": "={{ $json.createdAfter }}" },
          { "name": "created_before", "value": "={{ $json.createdBefore }}" }
        ]
      },
      "authentication": "genericCredentialType",
      "genericAuthType": "httpHeaderAuth"
    }
    ```
  - Credentials:
    ```json
    {
      "httpHeaderAuth": {
        "id": "PLACEHOLDER",
        "name": "Fathom API Key"
      }
    }
    ```

- **Code: Format Recording List** — `n8n-nodes-base.code`
  - ID: `c1000000-0000-4000-8000-000000000004`
  - Position: [750, 300]
  - jsCode:
    ```javascript
    const items = $json.items || [];
    if (items.length === 0) {
      return { json: { message: 'No recordings found for this date.' } };
    }

    return items.map(meeting => {
      const start = new Date(meeting.recording_start_time);
      const end = new Date(meeting.recording_end_time);
      const durationMin = Math.round((end - start) / 60000);

      return {
        json: {
          recording_id: meeting.recording_id,
          title: meeting.title || meeting.meeting_title || 'Untitled',
          start_time: meeting.recording_start_time,
          duration_minutes: durationMin,
          url: meeting.share_url || meeting.url
        }
      };
    });
    ```

**Step 2: Wire connections:**

```json
{
  "Manual Trigger": {
    "main": [[{ "node": "Code: Set Date Parameter", "type": "main", "index": 0 }]]
  },
  "Code: Set Date Parameter": {
    "main": [[{ "node": "HTTP Request: List Meetings by Date", "type": "main", "index": 0 }]]
  },
  "HTTP Request: List Meetings by Date": {
    "main": [[{ "node": "Code: Format Recording List", "type": "main", "index": 0 }]]
  }
}
```

**Step 3: Set workflow metadata:**

```json
{
  "id": "3",
  "name": "Fathom: List Recordings",
  "active": false,
  "settings": { "executionOrder": "v1" },
  "pinData": {},
  "tags": []
}
```

**Step 4: Validate the JSON**

Run: `python3 -c "import json; json.load(open('workflows/fathom-list-recordings.json')); print('Valid')"`

---

### Task 3: Build Workflow — Fathom Fetch Transcript (Manual)

**Files:**
- Create: `workflows/fathom-fetch-transcript.json`

**Step 1: Create the workflow JSON with these nodes:**

- **Manual Trigger** — `n8n-nodes-base.manualTrigger`
  - ID: `d1000000-0000-4000-8000-000000000001`
  - Position: [0, 300]
  - Parameters: `{}`

- **Code: Set Recording ID** — `n8n-nodes-base.code`
  - ID: `d1000000-0000-4000-8000-000000000002`
  - Position: [250, 300]
  - jsCode:
    ```javascript
    // ╔══════════════════════════════════════════╗
    // ║  CHANGE THIS ID BEFORE RUNNING            ║
    // ║  Get it from "Fathom: List Recordings"    ║
    // ╚══════════════════════════════════════════╝
    const recordingId = 12345;

    return { json: { recordingId } };
    ```

- **HTTP Request: Fetch Transcript** — `n8n-nodes-base.httpRequest`
  - ID: `d1000000-0000-4000-8000-000000000003`
  - Position: [500, 300]
  - Parameters:
    ```json
    {
      "method": "GET",
      "url": "=https://api.fathom.ai/external/v1/recordings/{{ $json.recordingId }}/transcript",
      "authentication": "genericCredentialType",
      "genericAuthType": "httpHeaderAuth"
    }
    ```
  - Credentials:
    ```json
    {
      "httpHeaderAuth": {
        "id": "PLACEHOLDER",
        "name": "Fathom API Key"
      }
    }
    ```

- **HTTP Request: Get Meeting Details** — `n8n-nodes-base.httpRequest`
  - ID: `d1000000-0000-4000-8000-000000000004`
  - Position: [500, 500]
  - Note: Runs in parallel with transcript fetch — both connected from Set Recording ID
  - Parameters:
    ```json
    {
      "method": "GET",
      "url": "https://api.fathom.ai/external/v1/meetings",
      "sendQuery": true,
      "queryParameters": {
        "parameters": [
          { "name": "include_transcript", "value": "false" }
        ]
      },
      "authentication": "genericCredentialType",
      "genericAuthType": "httpHeaderAuth"
    }
    ```
  - Credentials: same Fathom API Key

- **Code: Find Meeting and Extract Date** — `n8n-nodes-base.code`
  - ID: `d1000000-0000-4000-8000-000000000005`
  - Position: [750, 500]
  - jsCode:
    ```javascript
    const recordingId = $('Code: Set Recording ID').item.json.recordingId;
    const meetings = $json.items || [];
    const meeting = meetings.find(m => m.recording_id === recordingId);

    if (!meeting) {
      throw new Error(`Meeting with recording_id ${recordingId} not found`);
    }

    return {
      json: {
        datePrefix: meeting.recording_start_time.substring(0, 10),
        title: meeting.title || meeting.meeting_title || 'Untitled',
        recording_start_time: meeting.recording_start_time
      }
    };
    ```

- **Merge** — `n8n-nodes-base.merge`
  - ID: `d1000000-0000-4000-8000-000000000006`
  - Position: [1000, 300]
  - Parameters:
    ```json
    {
      "mode": "combine",
      "mergeByFields": {},
      "options": {},
      "combinationMode": "mergeByPosition"
    }
    ```
  - Input 1: Transcript data (from HTTP Request: Fetch Transcript)
  - Input 2: Meeting date info (from Code: Find Meeting and Extract Date)

- **Code: Format and Save Transcript** — `n8n-nodes-base.code`
  - ID: `d1000000-0000-4000-8000-000000000007`
  - Position: [1250, 300]
  - jsCode:
    ```javascript
    const fs = require('fs');

    // Transcript comes from input 1, date from input 2
    const transcript = $json.transcript || $input.all()[0]?.json?.transcript || [];
    const dateInfo = $input.all()[1]?.json || $input.all()[0]?.json || {};
    const datePrefix = dateInfo.datePrefix || $json.datePrefix;

    if (!datePrefix) {
      throw new Error('Could not determine date prefix');
    }

    const formatted = transcript.map(entry => {
      const speaker = entry.speaker?.display_name || 'Unknown';
      const timestamp = entry.timestamp || '00:00:00';
      return `[${timestamp}] ${speaker}: ${entry.text}`;
    }).join('\n');

    const filename = `${datePrefix}-transcript.txt`;
    const filePath = `/home/node/watch/${filename}`;
    fs.writeFileSync(filePath, formatted, 'utf8');

    const chatFile = `/home/node/watch/${datePrefix}-zoom-chat.txt`;
    const bothPresent = fs.existsSync(chatFile);

    return {
      json: {
        datePrefix,
        transcriptFile: filePath,
        chatFile,
        bothPresent,
        message: bothPresent
          ? `Transcript saved. Chat log found — ready for merge!`
          : `Transcript saved. Waiting for chat log: ${chatFile}`
      }
    };
    ```

**Step 2: Wire connections:**

Note: Code: Set Recording ID fans out to TWO parallel nodes (transcript fetch and meeting details). They converge at the Merge node.

```json
{
  "Manual Trigger": {
    "main": [[{ "node": "Code: Set Recording ID", "type": "main", "index": 0 }]]
  },
  "Code: Set Recording ID": {
    "main": [[
      { "node": "HTTP Request: Fetch Transcript", "type": "main", "index": 0 },
      { "node": "HTTP Request: Get Meeting Details", "type": "main", "index": 0 }
    ]]
  },
  "HTTP Request: Fetch Transcript": {
    "main": [[{ "node": "Merge", "type": "main", "index": 0 }]]
  },
  "HTTP Request: Get Meeting Details": {
    "main": [[{ "node": "Code: Find Meeting and Extract Date", "type": "main", "index": 0 }]]
  },
  "Code: Find Meeting and Extract Date": {
    "main": [[{ "node": "Merge", "type": "main", "index": 1 }]]
  },
  "Merge": {
    "main": [[{ "node": "Code: Format and Save Transcript", "type": "main", "index": 0 }]]
  }
}
```

**Step 3: Set workflow metadata:**

```json
{
  "id": "4",
  "name": "Fathom: Fetch Transcript",
  "active": false,
  "settings": { "executionOrder": "v1" },
  "pinData": {},
  "tags": []
}
```

**Step 4: Validate the JSON**

Run: `python3 -c "import json; json.load(open('workflows/fathom-fetch-transcript.json')); print('Valid')"`

---

### Task 4: Build Workflow — Merged Call Summarizer

**Files:**
- Create: `workflows/merged-call-summarizer.json`
- Note: This replaces `workflows/zoom-chat-summarizer.json` (keep the old file for reference)

**Step 1: Create the workflow JSON with the trigger and rendezvous nodes:**

- **Local File Trigger** — `n8n-nodes-base.localFileTrigger`
  - ID: `e1000000-0000-4000-8000-000000000001`
  - Position: [0, 300]
  - Same config as existing workflow:
    ```json
    {
      "triggerOn": "folder",
      "path": "/home/node/watch",
      "events": ["add"],
      "options": {
        "usePolling": true,
        "awaitWriteFinish": true,
        "depth": 0,
        "ignoreInitial": true
      }
    }
    ```

- **Code: Validate and Check Partner** — `n8n-nodes-base.code`
  - ID: `e1000000-0000-4000-8000-000000000002`
  - Position: [250, 300]
  - jsCode:
    ```javascript
    const fs = require('fs');
    const path = require('path');

    const filePath = $json.path;
    const filename = path.basename(filePath);

    // Must be .txt and match expected patterns
    if (!filename.endsWith('.txt')) return [];

    const dateMatch = filename.match(/^(\d{4}-\d{2}-\d{2})/);
    if (!dateMatch) return [];

    const datePrefix = dateMatch[1];
    const watchDir = '/home/node/watch';

    // Determine what type of file arrived and check for partner
    let fileType;
    let partnerFile;
    if (filename.includes('-zoom-chat')) {
      fileType = 'chat';
      partnerFile = `${watchDir}/${datePrefix}-transcript.txt`;
    } else if (filename.includes('-transcript')) {
      fileType = 'transcript';
      partnerFile = `${watchDir}/${datePrefix}-zoom-chat.txt`;
    } else {
      return []; // Unknown file type
    }

    const bothPresent = fs.existsSync(partnerFile);

    if (!bothPresent) {
      // Partner not here yet — stop and wait
      return [];
    }

    // Both files present — read them
    const chatFile = fileType === 'chat' ? filePath : `${watchDir}/${datePrefix}-zoom-chat.txt`;
    const transcriptFile = fileType === 'transcript' ? filePath : `${watchDir}/${datePrefix}-transcript.txt`;

    const chatText = fs.readFileSync(chatFile, 'utf8');
    const transcriptText = fs.readFileSync(transcriptFile, 'utf8');

    return {
      json: {
        datePrefix,
        chatText,
        transcriptText,
        chatFile,
        transcriptFile
      }
    };
    ```

- **Code: Merge Content** — `n8n-nodes-base.code`
  - ID: `e1000000-0000-4000-8000-000000000003`
  - Position: [500, 300]
  - jsCode:
    ```javascript
    const mergedText = `# MEETING TRANSCRIPT\n\n${$json.transcriptText}\n\n# ZOOM CHAT LOG\n\n${$json.chatText}`;

    return {
      json: {
        ...$json,
        mergedText
      }
    };
    ```

- **Code: Create Output Folder** — `n8n-nodes-base.code`
  - ID: `e1000000-0000-4000-8000-000000000004`
  - Position: [750, 300]
  - jsCode:
    ```javascript
    const fs = require('fs');
    const datePrefix = $json.datePrefix;
    const outputDir = `/home/node/output/${datePrefix}`;
    if (!fs.existsSync(outputDir)) {
      fs.mkdirSync(outputDir, { recursive: true });
    }
    return { json: { ...$json, outputDir } };
    ```

- **Code: Save transcript.txt** — `n8n-nodes-base.code`
  - ID: `e1000000-0000-4000-8000-000000000005`
  - Position: [1000, 300]
  - jsCode:
    ```javascript
    const fs = require('fs');
    const outputDir = $json.outputDir;
    fs.writeFileSync(`${outputDir}/transcript.txt`, $json.transcriptText, 'utf8');
    return { json: { ...$json } };
    ```

**Step 2: Add LLM nodes (Extract Signal, Community Post, Compress Post):**

These follow the same pattern as the existing workflow but with updated prompts.

- **LLM: Extract Signal** — `@n8n/n8n-nodes-langchain.chainLlm`
  - ID: `e1000000-0000-4000-8000-000000000006`
  - Position: [1250, 300]
  - Parameters:
    ```json
    {
      "promptType": "define",
      "text": "={{ $json.mergedText }}",
      "hasOutputParser": false,
      "messages": {
        "messageValues": [
          {
            "type": "SystemMessagePromptTemplate",
            "message": "You are analyzing the transcript and Zoom chat log of a weekly AI community call.\n\nYour job is to extract only the information that would still be useful to a community member reading it one week later.\n\nFocus especially on:\n- links and shared resources\n- useful question-and-answer pairs\n- practical insights and recommendations\n- tools, platforms, frameworks, and concepts mentioned\n- open questions or follow-ups worth revisiting\n\nReturn your analysis in the following structure:\n\n# Extracted Chat Signal\n\n## Shared Resources\nFor each useful link or resource, provide:\n- Title\n- URL if present\n- Why it matters\n\n## Key Q&A\nFor each useful question-and-answer pair, provide:\n- Question\n- Answer\n- Short synthesis if multiple people contributed\n\n## Key Insights\nList the most useful ideas, recommendations, warnings, practical tips, or mental models shared in the chat.\n\n## Tools and Concepts Mentioned\nList important tools, frameworks, products, or concepts mentioned, with a short explanation of why they mattered.\n\n## Follow-Ups Worth Revisiting\nList unresolved questions, open threads, or topics that would be worth revisiting in a future call.\n\nRules:\n- Ignore greetings, jokes, reactions, filler, emojis, and casual banter\n- Ignore duplicate content unless repetition adds meaning\n- Do not invent missing context\n- Do not force content into a section if nothing valuable is present\n- Keep only high-value signal\n- Rewrite messy chat language into clear professional language without changing meaning\n\nNow analyze the following meeting transcript and chat log:"
          }
        ]
      }
    }
    ```

- **OpenRouter Chat Model 1** — `@n8n/n8n-nodes-langchain.lmChatOpenRouter`
  - ID: `e1000000-0000-4000-8000-000000000007`
  - Position: [1250, 500]
  - Parameters:
    ```json
    {
      "model": "anthropic/claude-sonnet-4.6",
      "options": { "maxTokens": 8192, "temperature": 0.3 }
    }
    ```
  - Credentials:
    ```json
    { "openRouterApi": { "id": "PLACEHOLDER", "name": "OpenRouter account" } }
    ```

- **Code: Save extracted-signal.md** — `n8n-nodes-base.code`
  - ID: `e1000000-0000-4000-8000-000000000008`
  - Position: [1500, 300]
  - jsCode:
    ```javascript
    const fs = require('fs');
    const outputDir = $('Code: Create Output Folder').item.json.outputDir;
    const signalText = $json.text;
    fs.writeFileSync(`${outputDir}/extracted-signal.md`, signalText, 'utf8');
    return { json: { signalText, outputDir, datePrefix: $('Code: Create Output Folder').item.json.datePrefix } };
    ```

- **LLM: Community Post** — `@n8n/n8n-nodes-langchain.chainLlm`
  - ID: `e1000000-0000-4000-8000-000000000009`
  - Position: [1750, 300]
  - Parameters:
    ```json
    {
      "promptType": "define",
      "text": "={{ $json.signalText }}",
      "hasOutputParser": false,
      "messages": {
        "messageValues": [
          {
            "type": "SystemMessagePromptTemplate",
            "message": "You are preparing a polished community post based on extracted insights from a weekly AI community call (transcript and chat log combined).\n\nYour audience is community members who may not have attended live but want the most useful value from the call.\n\nTurn the extracted material below into a concise, polished, community-friendly post.\n\nUse the following structure:\n\n# Community Call Highlights\n\n## Shared Resources\nPresent the most useful links and resources in a clean, easy-to-scan way.\n\n## Key Q&A\nPresent the most useful question-and-answer pairs clearly and concisely.\n\n## Key Insights\nSummarize the strongest practical or strategic takeaways.\n\n## Tools and Concepts Mentioned\nList important tools, frameworks, and concepts with short explanations.\n\n## Follow-Ups Worth Exploring\nList open questions or topics worth revisiting if relevant.\n\n## Summary\nWrite one short paragraph summarizing the overall value and themes of the call.\n\nRules:\n- Keep the post concise and skimmable\n- Preserve only the strongest value\n- Use polished, natural, professional language\n- Do not invent any information not present in the extracted analysis\n- Omit any section that has little or no useful content\n- Make the result feel ready to post with minimal editing\n\nHere is the extracted analysis:"
          }
        ]
      }
    }
    ```

- **OpenRouter Chat Model 2** — `@n8n/n8n-nodes-langchain.lmChatOpenRouter`
  - ID: `e1000000-0000-4000-8000-000000000010`
  - Position: [1750, 500]
  - Same parameters and credentials as Model 1

- **Code: Save community-post.md** — `n8n-nodes-base.code`
  - ID: `e1000000-0000-4000-8000-000000000011`
  - Position: [2000, 300]
  - jsCode:
    ```javascript
    const fs = require('fs');
    const outputDir = $('Code: Create Output Folder').item.json.outputDir;
    const communityPostText = $json.text;
    fs.writeFileSync(`${outputDir}/community-post.md`, communityPostText, 'utf8');
    return { json: { communityPostText, outputDir, datePrefix: $('Code: Create Output Folder').item.json.datePrefix } };
    ```

- **LLM: Compress Post** — `@n8n/n8n-nodes-langchain.chainLlm`
  - ID: `e1000000-0000-4000-8000-000000000012`
  - Position: [2250, 300]
  - Parameters:
    ```json
    {
      "promptType": "define",
      "text": "={{ $json.communityPostText }}",
      "hasOutputParser": false,
      "messages": {
        "messageValues": [
          {
            "type": "SystemMessagePromptTemplate",
            "message": "Condense the community post below by about 30 to 40 percent while preserving all high-value information.\n\nGoals:\n- make it easier to skim\n- remove repetition\n- keep links, useful Q&A, and strongest insights\n- preserve a professional, community-friendly tone\n\nDo not remove important resources or key takeaways.\n\nHere is the draft post:"
          }
        ]
      }
    }
    ```

- **OpenRouter Chat Model 3** — `@n8n/n8n-nodes-langchain.lmChatOpenRouter`
  - ID: `e1000000-0000-4000-8000-000000000013`
  - Position: [2250, 500]
  - Same parameters and credentials as Model 1

- **Code: Save community-post-compressed.md** — `n8n-nodes-base.code`
  - ID: `e1000000-0000-4000-8000-000000000014`
  - Position: [2500, 300]
  - jsCode:
    ```javascript
    const fs = require('fs');
    const outputDir = $('Code: Create Output Folder').item.json.outputDir;
    const compressedText = $json.text;
    fs.writeFileSync(`${outputDir}/community-post-compressed.md`, compressedText, 'utf8');
    return { json: { compressedText, outputDir, datePrefix: $('Code: Create Output Folder').item.json.datePrefix } };
    ```

**Step 3: Add the Weekly Invite LLM step (new):**

- **Code: Calculate Next Tuesday** — `n8n-nodes-base.code`
  - ID: `e1000000-0000-4000-8000-000000000015`
  - Position: [2750, 300]
  - jsCode:
    ```javascript
    const datePrefix = $json.datePrefix;
    const callDate = new Date(datePrefix + 'T12:00:00Z');
    const dayOfWeek = callDate.getDay();
    const daysUntilTuesday = (2 - dayOfWeek + 7) % 7 || 7;
    const nextTuesday = new Date(callDate);
    nextTuesday.setDate(callDate.getDate() + daysUntilTuesday);

    const months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
    const day = nextTuesday.getUTCDate();
    const suffix = day === 1 || day === 21 || day === 31 ? 'st' : day === 2 || day === 22 ? 'nd' : day === 3 || day === 23 ? 'rd' : 'th';
    const formattedDate = `${months[nextTuesday.getUTCMonth()]} ${day}${suffix}`;
    const inviteDate = `${nextTuesday.getUTCFullYear()}-${String(nextTuesday.getUTCMonth()+1).padStart(2,'0')}-${String(day).padStart(2,'0')}`;

    return {
      json: {
        compressedText: $json.compressedText,
        outputDir: $json.outputDir,
        formattedDate,
        inviteDate,
        datePrefix
      }
    };
    ```

- **LLM: Weekly Invite** — `@n8n/n8n-nodes-langchain.chainLlm`
  - ID: `e1000000-0000-4000-8000-000000000016`
  - Position: [3000, 300]
  - Parameters:
    ```json
    {
      "promptType": "define",
      "text": "={{ 'Next call date: Tuesday ' + $json.formattedDate + ' at 6PM ET\\n\\nHere is last week\\'s community post:\\n\\n' + $json.compressedText }}",
      "hasOutputParser": false,
      "messages": {
        "messageValues": [
          {
            "type": "SystemMessagePromptTemplate",
            "message": "You are writing a weekly invite post for an AI community coaching call. Your job is to create a post that encourages members to submit their questions in advance.\n\nYou will be given the compressed community post from the most recent call. Use it to add unique flavor to this week's invite.\n\nThe post MUST follow this exact structure:\n\n1. Opening hook (1-3 sentences) — A playful, attention-grabbing opener that references a specific highlight, tool, insight, or unresolved question from last week's call. Make it intriguing enough that someone who missed last week wants to catch up.\n\n2. Standard section — Copy EXACTLY as written below, including the emoji:\n\n📞 HOW THE CALLS WORK\nThe calls can run 2+ hours.\nWe want to make sure we're respecting everyone's time. Especially those of you who actually show up.\n\nHere's the structure:\n👉 Reply to this post with your questions before the call\n👉 If you submit a question and you're on the call, you go first\n👉 We work through questions in the order they came in\n👉 Then we open it up for everyone else\n\nIf you can't make the call but want your question answered, drop it in the comments. We'll get to it. But priority goes to people who are there.\n\nThe goal is simple: if you're taking the time to show up, you shouldn't have to wait behind questions from people who aren't even on the call.\n\n3. Flavor bridge (1-3 sentences) — Reference 2-3 specific unresolved questions, follow-ups, or topics from last week that people might want to continue. Mention people by first name only if they had open questions. Frame it as a warm invitation, not a call-out.\n\n4. Closing section — Copy EXACTLY as written below, but replace [DATE] with the provided date:\n\n🔗 ZOOM LINK (save this)\nhttps://us06web.zoom.us/j/81995207847?pwd=Xe6u6LmIQOmCP5VTnOwWYjDBfZNKGB.1\n\n📅 WHEN\nTuesday [DATE] at 6PM ET\n\nLooking forward to seeing you on the call!\n\nRules:\n- Tone: playful, welcoming, energetic — like a community leader who genuinely enjoys these calls\n- Do NOT call out anyone negatively or use inside jokes that would confuse non-attendees\n- Do NOT invent information not present in the community post\n- Keep the opening hook and flavor bridge fresh and different each week\n- The standard section and closing section must be reproduced EXACTLY (no modifications to wording or emoji)\n- Total post length should feel like a quick, easy read — not a wall of text"
          }
        ]
      }
    }
    ```

- **OpenRouter Chat Model 4** — `@n8n/n8n-nodes-langchain.lmChatOpenRouter`
  - ID: `e1000000-0000-4000-8000-000000000017`
  - Position: [3000, 500]
  - Same parameters and credentials as Model 1

- **Code: Save weekly-invite.md** — `n8n-nodes-base.code`
  - ID: `e1000000-0000-4000-8000-000000000018`
  - Position: [3250, 300]
  - jsCode:
    ```javascript
    const fs = require('fs');
    const outputDir = $json.outputDir || $('Code: Create Output Folder').item.json.outputDir;
    const inviteDate = $('Code: Calculate Next Tuesday').item.json.inviteDate;
    const inviteText = $json.text;
    fs.writeFileSync(`${outputDir}/${inviteDate}-weekly-invite.md`, inviteText, 'utf8');
    return { json: { inviteText, outputDir, inviteDate } };
    ```

**Step 4: Wire ALL connections:**

```json
{
  "Local File Trigger": {
    "main": [[{ "node": "Code: Validate and Check Partner", "type": "main", "index": 0 }]]
  },
  "Code: Validate and Check Partner": {
    "main": [[{ "node": "Code: Merge Content", "type": "main", "index": 0 }]]
  },
  "Code: Merge Content": {
    "main": [[{ "node": "Code: Create Output Folder", "type": "main", "index": 0 }]]
  },
  "Code: Create Output Folder": {
    "main": [[{ "node": "Code: Save transcript.txt", "type": "main", "index": 0 }]]
  },
  "Code: Save transcript.txt": {
    "main": [[{ "node": "LLM: Extract Signal", "type": "main", "index": 0 }]]
  },
  "OpenRouter Chat Model 1": {
    "ai_languageModel": [[{ "node": "LLM: Extract Signal", "type": "ai_languageModel", "index": 0 }]]
  },
  "LLM: Extract Signal": {
    "main": [[{ "node": "Code: Save extracted-signal.md", "type": "main", "index": 0 }]]
  },
  "Code: Save extracted-signal.md": {
    "main": [[{ "node": "LLM: Community Post", "type": "main", "index": 0 }]]
  },
  "OpenRouter Chat Model 2": {
    "ai_languageModel": [[{ "node": "LLM: Community Post", "type": "ai_languageModel", "index": 0 }]]
  },
  "LLM: Community Post": {
    "main": [[{ "node": "Code: Save community-post.md", "type": "main", "index": 0 }]]
  },
  "Code: Save community-post.md": {
    "main": [[{ "node": "LLM: Compress Post", "type": "main", "index": 0 }]]
  },
  "OpenRouter Chat Model 3": {
    "ai_languageModel": [[{ "node": "LLM: Compress Post", "type": "ai_languageModel", "index": 0 }]]
  },
  "LLM: Compress Post": {
    "main": [[{ "node": "Code: Save community-post-compressed.md", "type": "main", "index": 0 }]]
  },
  "Code: Save community-post-compressed.md": {
    "main": [[{ "node": "Code: Calculate Next Tuesday", "type": "main", "index": 0 }]]
  },
  "Code: Calculate Next Tuesday": {
    "main": [[{ "node": "LLM: Weekly Invite", "type": "main", "index": 0 }]]
  },
  "OpenRouter Chat Model 4": {
    "ai_languageModel": [[{ "node": "LLM: Weekly Invite", "type": "ai_languageModel", "index": 0 }]]
  },
  "LLM: Weekly Invite": {
    "main": [[{ "node": "Code: Save weekly-invite.md", "type": "main", "index": 0 }]]
  }
}
```

**Step 5: Set workflow metadata:**

```json
{
  "id": "5",
  "name": "Merged Call Summarizer",
  "active": false,
  "settings": { "executionOrder": "v1" },
  "pinData": {},
  "tags": []
}
```

**Step 6: Validate the JSON**

Run: `python3 -c "import json; json.load(open('workflows/merged-call-summarizer.json')); print('Valid')"`

---

### Task 5: Import All Workflows into n8n

**Step 1: Copy workflow files into the container**

Run:
```bash
docker cp workflows/fathom-transcript-poller.json n8n:/tmp/fathom-transcript-poller.json
docker cp workflows/fathom-list-recordings.json n8n:/tmp/fathom-list-recordings.json
docker cp workflows/fathom-fetch-transcript.json n8n:/tmp/fathom-fetch-transcript.json
docker cp workflows/merged-call-summarizer.json n8n:/tmp/merged-call-summarizer.json
```

**Step 2: Import each workflow**

Run:
```bash
docker exec n8n n8n import:workflow --input=/tmp/fathom-transcript-poller.json
docker exec n8n n8n import:workflow --input=/tmp/fathom-list-recordings.json
docker exec n8n n8n import:workflow --input=/tmp/fathom-fetch-transcript.json
docker exec n8n n8n import:workflow --input=/tmp/merged-call-summarizer.json
```

Expected: Each command prints a success message or the imported workflow ID.

**Step 3: Verify in n8n UI**

- Open http://localhost:5678
- Navigate to Workflows
- Confirm all 4 new workflows appear:
  - Fathom Transcript Poller
  - Fathom: List Recordings
  - Fathom: Fetch Transcript
  - Merged Call Summarizer
- Open each and verify nodes are connected correctly

---

### Task 6: Configure Fathom API Credentials

**Step 1: Get Fathom API key**

- Go to https://fathom.video/customize#api-access-header (User Settings → API Access)
- Generate an API key
- Copy the key

**Step 2: Create credential in n8n**

- In n8n UI, go to Credentials → Add Credential
- Type: Header Auth
- Name: `Fathom API Key`
- Header Name: `X-Api-Key`
- Header Value: paste the API key
- Save

**Step 3: Link credentials to workflows**

- Open each Fathom workflow (Poller, List Recordings, Fetch Transcript)
- Click each HTTP Request node
- In the credential dropdown, select "Fathom API Key"
- Save the workflow

**Step 4: Link OpenRouter credentials to Merged Call Summarizer**

- Open the Merged Call Summarizer workflow
- Click each OpenRouter Chat Model node (1-4)
- Select the existing OpenRouter credential
- Save

---

### Task 7: Wire Execute Workflow IDs

**Step 1: Get the Merged Call Summarizer workflow ID**

- In the n8n UI, open the Merged Call Summarizer workflow
- Note the workflow ID from the URL (e.g., `http://localhost:5678/workflow/abc123` → ID is `abc123`)

**Step 2: Update the Fathom Transcript Poller**

- Open the Fathom Transcript Poller workflow
- Click the "Execute Workflow: Trigger Summarizer" node
- Set the Workflow ID to the Merged Call Summarizer's ID
- Save

**Step 3: (Optional) Update the Fathom Fetch Transcript workflow**

- If you want the manual fetch to also auto-trigger the summarizer, add an Execute Workflow node after the "Code: Format and Save Transcript" node with the same workflow ID
- Otherwise, the Local File Trigger on the summarizer will pick up the transcript file automatically

---

### Task 8: Test with Real Fathom Data

**Step 1: Test Fathom API connectivity**

- Open "Fathom: List Recordings" workflow
- In the "Code: Set Date Parameter" node, change `targetDate` to `'2025-09-02'`
- Click "Test Workflow"
- Expected: List of recordings for that date with recording_id, title, duration

**Step 2: Fetch the transcript**

- Note the `recording_id` from Step 1's output
- Open "Fathom: Fetch Transcript" workflow
- In the "Code: Set Recording ID" node, set `recordingId` to the value from Step 1
- Click "Test Workflow"
- Expected: Transcript saved to `/home/node/watch/2025-09-02-transcript.txt`

**Step 3: Verify transcript file**

Run:
```bash
docker exec n8n head -20 /home/node/watch/2025-09-02-transcript.txt
```

Expected: Formatted transcript lines like `[00:01:29] shakur: How's it going, Tom?`

**Step 4: Drop matching chat log**

Copy a chat log file for the same date to `~/n8n/watch/`:
```bash
cp /path/to/chat-file ~/n8n/watch/2025-09-02-zoom-chat.txt
```

Expected: The Merged Call Summarizer triggers automatically (Local File Trigger detects the new file, finds the transcript already present, runs the full chain).

**Step 5: Verify outputs**

Run:
```bash
docker exec n8n ls -la /home/node/output/2025-09-02/
```

Expected:
```
transcript.txt
extracted-signal.md
community-post.md
community-post-compressed.md
2025-09-09-weekly-invite.md
```

(September 2nd 2025 was a Tuesday, so next Tuesday is September 9th.)

**Step 6: Review the weekly invite**

Run:
```bash
docker exec n8n cat /home/node/output/2025-09-02/2025-09-09-weekly-invite.md
```

Verify:
- Has a playful opening hook referencing last week's content
- Standard "HOW THE CALLS WORK" section is reproduced exactly
- Has a flavor bridge mentioning specific topics/people
- Closing has correct Zoom link and date "Tuesday September 9th at 6PM ET"

---

### Task 9: Update CLAUDE.md

**Files:**
- Modify: `CLAUDE.md`

**Step 1: Add new workflows to the Workflows section**

Add documentation for the 3 new workflows (Fathom Transcript Poller, Fathom Manual Lookup, Merged Call Summarizer) and update the existing Zoom Chat Summarizer entry to note it's been replaced.

**Step 2: Add Fathom API to the credentials/environment section**

Document the Fathom API credential setup and the polling schedule.
