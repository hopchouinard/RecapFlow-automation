# Chapter 8 — Workflow: Merged Call Summarizer

**Category:** Workflows
**Reading time:** 7 minutes

---

## Purpose

The core workflow. Merges a Zoom chat log and Fathom transcript, runs a 4-step LLM prompt chain, and produces five output files including a weekly community invite. Replaces the original chat-only summarizer.

**Workflow file:** `workflows/merged-call-summarizer.json`
**n8n Workflow ID:** 5

## Node Flow

```
Local File Trigger (/home/node/watch)
    → Code: Validate and Check Partner
    → Code: Merge Content
    → Code: Create Output Folder
    → Code: Save transcript.txt
    → LLM: Extract Signal          ← OpenRouter Chat Model 1
    → Code: Save extracted-signal.md
    → LLM: Community Post          ← OpenRouter Chat Model 2
    → Code: Save community-post.md
    → LLM: Compress Post           ← OpenRouter Chat Model 3
    → Code: Save community-post-compressed.md
    → Code: Calculate Next Tuesday
    → LLM: Weekly Invite           ← OpenRouter Chat Model 4
    → Code: Save weekly-invite.md
```

**18 nodes total:** 8 Code nodes, 4 LLM Chain nodes, 4 OpenRouter Chat Model sub-nodes, 1 Local File Trigger, 1 implicit entry via Execute Workflow.

## The Rendezvous Pattern

The "Validate and Check Partner" node is the heart of the design:

```javascript
// Determine what type of file arrived
if (filename.includes('-zoom-chat')) {
  partnerFile = `${watchDir}/${datePrefix}-transcript.txt`;
} else if (filename.includes('-transcript')) {
  partnerFile = `${watchDir}/${datePrefix}-zoom-chat.txt`;
}

// If partner isn't here yet, stop and wait
if (!fs.existsSync(partnerFile)) {
  return [];  // Empty array = workflow stops
}

// Both present — read both and proceed
```

Returning an empty array (`[]`) from a Code node stops the workflow without error. This is how the "wait for partner" behavior works — the workflow simply doesn't continue until both files exist.

## The Merge

Both files are concatenated with clear section headers:

```
# MEETING TRANSCRIPT

[00:01:29] shakur: How's it going, Tom?
[00:01:30] Patrick Chouinard: Hey, hello.
...

# ZOOM CHAT LOG

<raw chat log content>
```

This merged text is what the first LLM processes.

## LLM Prompt Chain

### Step 1: Extract Signal

**Input:** Merged transcript + chat log (~100-200KB for a 2-hour call)
**Output:** Structured analysis with sections for Resources, Q&A, Insights, Tools, Follow-Ups

The prompt instructs the LLM to focus on information that would be useful one week later — filtering out greetings, filler, and casual banter. It explicitly handles the dual-source nature: "You are analyzing the transcript and Zoom chat log of a weekly AI community call."

### Step 2: Community Post

**Input:** Extracted signal from Step 1
**Output:** Polished, ready-to-post community recap

Critical: The prompt explicitly instructs **plain text output** for Skool compatibility:

> "Output PLAIN TEXT only. Do NOT use markdown syntax like # headers, ** bold **, - bullet lists, or [links](url). Instead use emoji for section headers."

Section headers use emoji: 📎 SHARED RESOURCES, ❓ KEY Q&A, 💡 KEY INSIGHTS, 🛠️ TOOLS AND CONCEPTS, 🔄 FOLLOW-UPS, 📝 SUMMARY.

### Step 3: Compress Post

**Input:** Community post from Step 2
**Output:** 30-40% shorter version preserving all high-value content

Same plain text constraint. Maintains the emoji section headers from Step 2.

### Step 4: Weekly Invite

**Input:** Compressed post + calculated next Tuesday date
**Output:** Community invite post with unique flavor from last week's content

The prompt defines a rigid structure:
1. **Opening hook** — playful reference to last week's content
2. **Standard section** — reproduced exactly (HOW THE CALLS WORK, rules, etc.)
3. **Flavor bridge** — references specific unresolved topics/people
4. **Closing** — Zoom link and date

Tone rules: playful and welcoming, no negative call-outs, no inside jokes that exclude non-attendees.

## Next Tuesday Calculation

```javascript
const callDate = new Date(datePrefix + 'T12:00:00Z');
const dayOfWeek = callDate.getDay();
const daysUntilTuesday = (2 - dayOfWeek + 7) % 7 || 7;
```

The `|| 7` ensures that if the call is on a Tuesday, the invite targets the *next* Tuesday (7 days later), not the same day.

Date formatting includes ordinal suffixes: "September 9th", "March 3rd", "January 21st".

## LLM Configuration

All four LLM steps use identical settings:

| Setting | Value |
|---------|-------|
| Model | `anthropic/claude-sonnet-4.6` |
| Max tokens | 8192 |
| Temperature | 0.3 |
| Provider | OpenRouter |

Temperature 0.3 provides consistent, focused output while allowing enough variation to keep weekly invites fresh.

## Output Files

All saved to `/home/node/output/YYYY-MM-DD/`:

| File | Size (typical) | Purpose |
|------|---------------|---------|
| `transcript.txt` | ~150KB | Formatted raw transcript |
| `extracted-signal.md` | ~20KB | Structured signal extraction |
| `community-post.md` | ~15KB | Full community post (plain text) |
| `community-post-compressed.md` | ~12KB | Compressed version |
| `YYYY-MM-DD-weekly-invite.md` | ~1.5KB | Next week's invite |
