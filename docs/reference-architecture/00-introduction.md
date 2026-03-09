# Chapter 0 — Introduction

**Category:** Philosophy & Framing
**Reading time:** 5 minutes

---

## What This Is

A reference architecture for building an automated community call processing pipeline using n8n, the Fathom API, and LLM prompt chains. The system watches for Zoom meeting artifacts (chat logs and transcripts), merges them, and produces polished community content — all without human intervention beyond the initial setup.

## The Problem

Running a weekly community coaching call generates two valuable artifacts:

1. **The Zoom chat log** — links, questions, tool recommendations, and real-time reactions shared by participants during the call
2. **The meeting transcript** — the full spoken conversation captured by Fathom, an AI notetaker

Separately, each artifact tells half the story. The chat log captures what people shared in writing. The transcript captures what was said out loud. But the real value lives at the intersection — a question asked in chat that gets answered verbally, a tool demo on screen that sparks a flurry of links in chat, an open thread that nobody resolved.

Manually merging these, extracting signal, writing a community post, and preparing next week's invite takes 2-3 hours per call. This architecture reduces that to zero.

## What Gets Produced

For each weekly call, the pipeline automatically generates five output files:

| File | Purpose |
|------|---------|
| `transcript.txt` | Formatted raw transcript for archival |
| `extracted-signal.md` | High-value signal extracted from both sources |
| `community-post.md` | Polished community recap (plain text for Skool) |
| `community-post-compressed.md` | Condensed version for easy scanning |
| `YYYY-MM-DD-weekly-invite.md` | Next week's call invite with unique flavor |

## Who This Is For

Anyone running recurring community calls, team standups, or coaching sessions who wants to automate the post-call content pipeline. The specific tools (n8n, Fathom, Zoom, Skool) are interchangeable — the patterns and architecture apply broadly.

## How This Document Is Organized

The chapters follow the build order — from infrastructure decisions through implementation details to operational concerns:

- **Chapters 0-2**: Philosophy, goals, and design decisions
- **Chapters 3-5**: Infrastructure and deployment
- **Chapters 6-8**: The four n8n workflows in detail
- **Chapters 9-10**: Testing, debugging, and operations
- **Chapter 11**: Lessons learned and future directions
