# Chapter 10 — Prompt Engineering

**Category:** Operations
**Reading time:** 6 minutes

---

## Prompt Chain Architecture

The system uses a sequential 4-prompt chain where each step's output feeds the next. This is intentional — rather than sending the raw 150KB transcript to a single prompt, the chain progressively distills the content:

```
Raw merged content (~150KB)
    → Extract Signal (~20KB) — 85% reduction
    → Community Post (~15KB) — structured and polished
    → Compressed Post (~12KB) — 30-40% further reduction
    → Weekly Invite (~1.5KB) — single focused output
```

Each step has a clear, narrow job. This produces better results than a single "do everything" prompt.

## Prompt 1: Extract Signal

**Goal:** Reduce noise, keep only high-value information.

**Key instruction:** "Extract only the information that would still be useful to a community member reading it one week later."

This temporal framing is powerful — it automatically filters out time-sensitive reactions ("that's cool!", "lol"), greetings, and small talk while preserving tools, links, insights, and open questions.

**Output structure:**
- Shared Resources (title, URL, why it matters)
- Key Q&A (question, answer, synthesis)
- Key Insights (ideas, tips, mental models)
- Tools and Concepts (with context)
- Follow-Ups Worth Revisiting (open threads)

**Rules that matter most:**
- "Do not force content into a section if nothing valuable is present" — prevents padding
- "Rewrite messy chat language into clear professional language" — handles transcript artifacts

## Prompt 2: Community Post

**Goal:** Transform extracted signal into a copy-paste-ready community post.

**Critical constraint:** Plain text output for Skool compatibility.

```
IMPORTANT: This post will be published on Skool, which does NOT render markdown.
Output PLAIN TEXT only. Do NOT use markdown syntax like # headers, ** bold **,
- bullet lists, or [links](url). Instead use emoji for section headers.
```

**Emoji section headers:**
- 📎 SHARED RESOURCES
- ❓ KEY Q&A
- 💡 KEY INSIGHTS
- 🛠️ TOOLS AND CONCEPTS MENTIONED
- 🔄 FOLLOW-UPS WORTH EXPLORING
- 📝 SUMMARY

The "omit any section that has little or no useful content" rule is important — not every call covers every category.

## Prompt 3: Compress Post

**Goal:** Reduce length by 30-40% while preserving all high-value content.

This is the simplest prompt. The key instruction is what NOT to remove: "Do not remove important resources or key takeaways." The LLM's job is to cut redundancy, tighten language, and merge overlapping points.

The plain text constraint is reinforced: "Keep the same emoji-based section headers and plain text formatting as the input."

## Prompt 4: Weekly Invite

**Goal:** Generate a unique weekly call invite that references last week's content.

This is the most constrained prompt. It defines a rigid 4-part structure:

1. **Opening hook** (LLM-generated) — playful, references specific content
2. **Standard section** (verbatim) — reproduced exactly, including emoji
3. **Flavor bridge** (LLM-generated) — references unresolved topics
4. **Closing section** (verbatim except date) — Zoom link and date

**Tone rules:**
- Playful, welcoming, energetic
- No negative call-outs
- No inside jokes that exclude non-attendees
- First names only when referencing open questions

The standard section and closing are provided verbatim in the prompt. The LLM must reproduce them exactly — this is enforced by explicit instruction: "must be reproduced EXACTLY (no modifications to wording or emoji)."

## Model Configuration

All prompts use identical settings:

| Setting | Value | Rationale |
|---------|-------|-----------|
| Model | Claude Sonnet 4.6 | Best balance of quality and cost for content generation |
| Temperature | 0.3 | Consistent output while allowing fresh weekly invites |
| Max tokens | 8192 | Sufficient for even the longest community posts |

## Iterating on Prompts

To modify a prompt:

1. Edit the system message in the relevant LLM node (in n8n UI or in the workflow JSON)
2. If editing JSON, re-import and re-link credentials
3. Reprocess a test meeting to verify the changes
4. Compare old vs. new output

The sequential chain makes prompt iteration safe — changing Prompt 3 doesn't affect Prompts 1 or 2. Each step can be tuned independently.

## Common Prompt Issues

**Markdown leaking into output:** Add explicit "Do NOT use markdown" instructions. LLMs default to markdown formatting — you must actively suppress it.

**Weekly invite modifying the standard section:** Strengthen the verbatim instruction. Adding "EXACTLY" in caps and repeating it helps.

**Extracted signal too verbose:** Tighten the "one week later" framing or add explicit length guidance.

**Missing sections in community post:** This is usually correct behavior — the "omit empty sections" rule is working. Only investigate if sections with genuine content are being dropped.
