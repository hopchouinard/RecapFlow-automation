📝 SUMMARY

A technically rich call spanning terminal tooling, agentic architecture, and practical Claude workflows. Patrick showcased his Claude Code plugin ecosystem — including a status bar plugin and CMUX integration — and shared a detailed Cowork folder structure for building persistent Claude memory across sessions. The group converged on a key insight for production agentic systems: standard SDLC principles apply directly, with one critical addition — designing explicitly for LLM non-determinism through idempotency and retry-safe patterns. Paul demonstrated Stagehand for authenticated browser automation, Morgan shared progress on a cemetery data visualization app, and the group explored tools from Pencil.dev for AI-assisted UI design to 1CLI for agent API key management. The emerging theme: Claude Code workflows are maturing rapidly from individual productivity tools into multi-machine, multi-agent operational infrastructure.

💡 KEY INSIGHTS

Cowork as a PM layer, Claude Code as a coding layer
Patrick separates conceptual and planning work (Cowork) from implementation (Claude Code). Cowork builds persistent context over time, reducing re-explanation overhead across sessions.

The IDE is now just a markdown viewer
Patrick no longer uses VS Code or Cursor as a primary workspace — only as a file viewer for markdown and generated output. All active work happens inside CMUX.

Stay below 60% context window usage
Experienced users deliberately keep context below 60% even when 1 million tokens are available. Output quality degrades in the middle of very long contexts — more tokens does not always mean better results.

Back up your Cowork sessions
Cowork session data is stored locally and can be corrupted by power outages mid-session. Patrick is building a backup system. Anyone using Cowork seriously should be aware of this risk.

Plugin marketplace pattern for Claude Code
A marketplace can be added with a single command and individual plugins installed from it — enabling composable, shareable Claude Code extensions across the community.

Claudebernetes — managing Claude at scale
Patrick is exploring a Kubernetes-like system for managing Claude Code skills, hooks, MCP configurations, and CLAUDE.md snippets across machines and users. He now runs 60+ Claude Code instances across home lab and work environments.

Treat agents like non-deterministic users
The most durable mental model for agentic architecture: treat the AI agent as a non-deterministic user. All patterns for handling unpredictable human users — input validation, idempotency, audit logs, role-based access — apply directly to agents.

MCP still has a role, but not for everything
MCP servers remain valuable for direct, real-time bidirectional integration (like Pincel.dev for UI design), but CLI-based tool access is often simpler and sufficient for most agent-tool interactions.

❓ KEY Q&A

Q: Is CMUX a version of tmux?
A: No. CMUX is built on Ghostty and inspired by tmux's multiplexing concept, but is a distinct product with its own CLI and modern architecture.

Q: Does CMUX work on Windows or Linux?
A: CMUX is Mac-focused. For Windows and Linux users, tmux inside WSL is the closest equivalent. Patrick's status line plugin now supports Windows, though it was the most time-consuming part of development.

Q: What is the recommended Cowork workspace structure?
A: Patrick recommends a top-level folder with this layout:
CLAUDE.md — working memory (your profile, stack, active projects — acts as a pointer, not a container)
memory/glossary.md — terms, acronyms, internal language
memory/people/ — profiles of collaborators
memory/projects/ — one file per project (status, stack, decisions)
memory/context/ — anything else Claude should retain

Q: What is a production-readiness checklist for an agentic solution?
A: Standard SDLC principles apply directly — security, access roles, pipeline design, message bus architecture, and transition management. Treat the agent as a non-deterministic actor, analogous to an unpredictable user. The key agentic-specific addition: design explicitly for non-determinism. LLMs are stateless, introducing failure modes like retry loops and duplicate actions. Address these with idempotency, retry-safe design, deduplication, and explicit state management. The Vectara awesome-agent-failures repo documents real examples of what goes wrong when this is ignored.

Q: When should you use Stagehand and what are the risks?
A: Stagehand suits complex browser interactions — logging in, capturing session cookies, making authenticated API calls, and extracting structured data. Paul completed a working integration in roughly one hour. Caution: cookie capture patterns can resemble man-in-the-middle attacks and may be flagged by security scanners. Use a proxy service to protect your IP reputation, especially with enterprise targets.

Q: What is 1CLI and how does it differ from AWS Secrets Manager?
A: 1CLI is a gateway layer between agents and external APIs. Agents use placeholders instead of real keys; 1CLI substitutes real credentials at runtime. More focused on agent-to-API key management than general secrets storage. From the same team that builds ChartDB.

Q: Is Sonnet a viable substitute for Opus when Opus is unavailable?
A: Yes. Sonnet with high-effort mode is nearly equivalent to Opus for most tasks. The main difference: Opus includes a 1-million-token context window by default, while Sonnet's 1-million-token context incurs additional cost.


🛠️ TOOLS AND CONCEPTS MENTIONED

CMUX — GPU-accelerated terminal multiplexer built on Ghostty. Modern replacement for tmux workflows.
Ghostty — The underlying terminal emulator on which CMUX is built.
Claude Code — Anthropic's agentic coding tool. Supports Sonnet and Opus; includes 1M token context.
Cowork — Claude's persistent workspace feature. Stores memory across sessions in a structured local folder.
CC-StatusLine — Patrick's plugin showing model, tokens, context %, MCP/hooks count, and Git info in a status bar.
Stagehand (BrowserBase) — Open-source AI browser automation. Handles authentication, cookie capture, and API data extraction.
1CLI / OneCLI — API key gateway for agents. Agents use placeholders; gateway substitutes real credentials at runtime.
Pincel.dev — Free Figma alternative with a Claude Code MCP server for real-time UI design.
D3.js — Data visualization library used for radial trees, circle packs, and hierarchical diagrams.
ShadCN + Next.js — UI component library and React framework used in Morgan's Heritage Plot cemetery application.
Astro + Cloudflare Pages — Static/hybrid site framework deployed on Cloudflare's free tier.
Fieldy — Wearable AI recorder with webhook integration. New E3 version just released.
Limitless — Competing AI wearable recorder.
LightPanda — Headless browser built for AI agents. Mentioned but not yet tested.
Playwright CLI — Suggested as an alternative to Stagehand for browser automation.
Awesome Agent Failures (Vectara) — GitHub repo cataloging real-world agentic AI system failures.
Non-determinism in agentic systems — Key architectural challenge requiring idempotency and retry-safe design patterns.
Meta-skills / Skills Library — Reusable library of Claude prompting skills composable across projects (concept from IndieDevDan).

📎 SHARED RESOURCES

Patrick's Claude Code Plugin Marketplace
https://github.com/hopchouinard/patchoutech-plugins
Install via: /plugin marketplace add hopchouinard/patchoutech-plugins

CC-StatusLine Plugin (status bar for Claude Code)
https://github.com/hopchouinard/CC-StatusLine
Shows model version, token usage, context window %, active MCP/hooks, and Git info.
Install via: /plugin install cc-statusline@patchoutech-plugins

CMUX Plugin for Claude Code
https://github.com/hopchouinard/cmux-plugin
Makes Claude Code aware it is running inside CMUX. Enables live progress bars, notifications, browser split panes, and auto-renaming workspaces from Git project name.
Install via: /plugin install cmux@patchoutech-plugins

CMUX Terminal
https://cmux.dev
GPU-accelerated terminal multiplexer built on Ghostty. Increasingly the primary interface for running Claude Code with multiple simultaneous sessions.

Cowork Getting Started Docs
https://support.claude.com/en/articles/13345190-get-started-with-cowork
Official setup guide. Patrick shared a recommended folder structure for bootstrapping persistent Claude memory across sessions.

Stagehand by BrowserBase
Open-source AI browser automation. Used to authenticate to live websites, capture session cookies, make API calls, and extract structured JSON data.

1CLI (OneCLI) — API Key Gateway
https://github.com/onecli/onecli
Gateway between AI agents and external APIs. Agents use placeholders; real credentials are substituted at runtime. Simplifies key rotation and centralizes access management.

Pencil.dev — Figma Alternative with Claude Code MCP
https://pencil.dev
Free UI design tool with an MCP server that lets Claude Code build interfaces in real time.

Awesome Agent Failures (Vectara)
https://github.com/vectara/awesome-agent-failures
Curated list of documented agentic AI system failures. Useful for production readiness planning around non-determinism, retries, and duplication.

IndieDevDan — Meta-Skills Library Video
https://www.youtube.com/watch?v=_vpNQ6IwP9w&t=2s
Covers building a reusable library of meta-skills for Claude. Patrick flagged this as a next project direction.

Fieldy AI (Wearable AI Recorder)
https://www.fieldy.ai/blog/introducing-offline-storage-record-without-your-phone
AI wearable recorder with webhook API and active developer program. New E3 version recently released. Unlimited plan recommended — the minute-limited tier depletes quickly.

Paul Getting Roasted by Theo (T3Chat Livestream)
https://vimeo.com/1174263912/5f3e603b06?fl=pl&fe=sh
Entertaining but substantive. Paul challenged Theo on whether creators should make content about when NOT to use their promoted tools.

🔄 FOLLOW-UPS WORTH EXPLORING

Claudebernetes / Claude Code profile management — Patrick is designing a Kubernetes-like system for managing Claude Code skills, hooks, MCP configs, and CLAUDE.md snippets across machines. Worth a dedicated demo when it matures.

Cowork backup system — Patrick is building a backup mechanism for locally-stored Cowork sessions. Relevant to anyone using Cowork seriously.

Cowork bootstrapper skill — Patrick has a skill in development that interviews users to build their initial Cowork context. Tested internally; planned for eventual publication.

CMUX plugin install issue (Ty) — Ty reported the plugin was not installing. Patrick asked Ty to post error messages in the Skool community chat for debugging.

Google Workspace CLI integration — Patrick flagged this as his next plugin wrapper project.

LightPanda headless browser — Mentioned but untested. Worth evaluating and reporting back.

Juan's AI image diffusion pipeline — Early-stage agentic image-to-image transformation pipeline using LoRA models. Worth a follow-up demo.

Brandon presenting next week — Scheduled for the next call.

