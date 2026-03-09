# Chapter 1 — Design Philosophy

**Category:** Philosophy & Framing
**Reading time:** 5 minutes

---

## Core Principles

### File-Based Rendezvous Over Orchestration

The central design challenge: two inputs arrive at unpredictable times (minutes to an hour apart), but both are required before processing can begin. Rather than building a queue, database, or state machine, the system uses the simplest possible coordination mechanism — the filesystem.

Each input saves a file with a date-prefixed name. After saving, it checks: does the partner file exist? If yes, proceed. If no, stop. When the second file arrives, it finds the first and triggers the pipeline.

This pattern has zero external dependencies, is trivially debuggable (`ls` tells you the full state), and survives container restarts without data loss.

### Save Early, Save Often

Each LLM step saves its output to disk immediately after success. If Prompt 3 fails, the outputs from Prompts 1 and 2 are already preserved. This means partial failures produce partial value rather than total loss.

### Credential Separation

API keys and credentials live exclusively in n8n's encrypted credential store, configured through the UI. Workflow JSON files use placeholder references. This means workflow files can be version-controlled and shared without exposing secrets.

### Local-First, No Cloud Dependencies

The n8n instance runs on a local VM. Files are synced via rsync over SSH on the local network. The only external API calls are to Fathom (for transcripts) and OpenRouter (for LLM inference). If either service is down, the files sit in the watch directory until the next successful poll — nothing is lost.

### Plain Text Output for Platform Compatibility

Community posts target Skool, which does not render markdown. All LLM prompts explicitly instruct plain text output with emoji-based section headers. This ensures copy-paste readiness without manual reformatting.

## Anti-Patterns Avoided

| Anti-Pattern | What We Did Instead |
|-------------|---------------------|
| Polling for both inputs | Rendezvous pattern — each input checks for the other |
| Webhook from external service | API polling — keeps the n8n instance purely local |
| Single monolithic workflow | Four focused workflows with clear responsibilities |
| Markdown output for web platforms | Plain text with emoji formatting |
| Hardcoded credentials in JSON | n8n credential store with placeholder references |
| Complex merge/join nodes | Sequential flow with `$()` node references |

## Design Decisions Log

### Why n8n Over Zapier/Make?

Self-hosted, open source, supports Code nodes with filesystem access, and runs locally. No data leaves the network except for API calls. The visual editor makes prompt iteration fast.

### Why OpenRouter Over Direct API?

Single credential for multiple model providers. Easy to switch models (e.g., Claude Sonnet to GPT-5) without changing workflow structure. Unified billing.

### Why Local File Trigger Over Webhook?

The n8n instance is not exposed to the internet. A webhook would require a tunnel (ngrok, Cloudflare Tunnel), adding complexity and a security surface. File-based triggers work entirely within the local network.

### Why Four Workflows Instead of One?

Separation of concerns. The poller handles API communication. The manual lookup handles testing. The summarizer handles processing. Each can be debugged, modified, and tested independently.
