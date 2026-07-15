📝 SUMMARY

This week's call featured live testing of Ty's ShipSafe alongside deep dives into autonomous AI training delivery, multi-model orchestration for cost control, and automated DevOps. Patrick demonstrated Claude Code skills that self-deliver training and autonomously manage pull requests, while Juan prepared his AI photo booth launch and Ryan shared CRM and hedge fund progress. The group refined approaches to preventing AI covert actions through personality configuration and routing tasks across Claude, Codex, and GPT to optimize token spend.

💡 KEY INSIGHTS

Package training as deployable skills. Patrick demonstrated self-updating training systems as zip files with materials and Claude Code skills that autonomously guide users—enabling one trainer to scale to thousands.

Place personality blocks at the user level. Adding "honesty over compliance" to ~/.claude/claude.md prevents silent destructive actions by forcing Claude to surface disagreements rather than act covertly.

Orchestrate across models to cut costs. Route planning to high-capability models like Claude, then hand off token-heavy work to cheaper models or tools to maintain quality while reducing token burn.

Use Firecrawl for research workflows. Its generous free tier runs independently of Claude tokens, ideal for web scraping without consuming API budget.

Automate PR management end-to-end. A "PR Babysit" skill polls open pull requests, responds to reviewer comments, triggers fixes, and auto-merges when clean—eliminating manual copy-paste loops.

Target corporate events first for hardware products. Corporate events provide revenue to subsidize personal events, and venue preferred-supplier lists create zero-cost distribution where every event becomes a warm lead.

Monetize inventory apps through affiliates. Coupling a photo-based inventory app with Amazon affiliate links for restocking items creates natural monetization alongside insurance documentation.

Structure wearable capture for downstream agents. Connecting a Fieldy wearable via webhook to a personal Hermes agent structures conversation summaries for immediate use, such as feeding directly into Claude Code with full context loaded.

❓ KEY Q&A

Q: How does Ty's local requirements-gathering setup compare to AWS Kiro mobile?
A: Ty uses local models on his Proxmox server to develop requirements via voice chat, then sends structured data to Claude for code generation—keeping context private and minimizing external tokens.

Q: Where should the "honesty over compliance" personality block live?
A: In ~/.claude/claude.md at the user level, not project level. It applies automatically to every Claude Code session without manual invocation.

Q: Why switch from Gemini CLI to Antigravity CLI?
A: Gemini CLI is deprecated; Antigravity CLI replaces it for Google-backed web search in agentic workflows.

Q: How do you integrate email systems without Google OAuth?
A: Use service tokens specific to the client's email platform rather than OAuth, enabling integration beyond Google Workspace.

Q: Why keep cognitive backlog in GitHub Issues instead of Notion?
A: Raw text in GitHub Issues is a universal source any agent can listen to without extra integration layers. GitHub plus VS Code replaces external task managers.

🛠️ TOOLS AND CONCEPTS MENTIONED

ShipSafe / FrankLabs — Session management tool adding presenter queues, countdown timers, and polling to video calls via shared URL.

Claude Code — Agentic coding tool for autonomous training delivery, skill creation, PR management, and presentation generation.

Fieldy — Wearable AI capture device connected via webhook to personal agents for structured meeting summarization.

Hermes — Self-hosted personal AI agent (accessible via Tailscale) that processes wearable transcripts for downstream use.

Firecrawl — Web scraping service with a generous free tier that runs independently of Claude tokens.

Antigravity CLI — Replacement for the deprecated Gemini CLI for web search in multi-model routing.

Codex CLI — OpenAI's CLI coding agent used alongside Claude in multi-model orchestration.

Multi-model Orchestration — Routing tasks between Claude, Codex, and GPT-4o to optimize cost and capability.

PR Babysit Skill — Polls pull requests, responds to comments, triggers fixes, and auto-merges when clean.

Present This Skill — Reads repo documentation, builds an Astro site, deploys to Cloudflare, and registers a subdomain from a single command.

LoopForge — Pipeline tool for automated idea-to-project workflows from GitHub Issues.

Astro — Static site framework for documentation and presentation websites.

Proxmox — Local server environment for running private LLMs to minimize token usage and maintain privacy.

📎 SHARED RESOURCES

ShipSafe Session Demo: https://shipsafe.franklabs.io/session/TTRB7P/queue

Omnigent Repository: https://github.com/omnigent-ai/omnigent.git

Theo on Multi-model Routing: https://x.com/theo/status/2072482460122964067

Patrick's Personality Block Gist: https://gist.github.com/hopchouinard/333cc020bbdc4ccede8ea023c3b6d62c

Healthcare BI Demo Site: https://coralharbourclinic.com/

Fathom Settings: https://fathom.video/customize

🔄 FOLLOW-UPS WORTH EXPLORING

Shakur will share his multi-model Claude.md routing configuration files via GitHub repo or gist.

Patrick will publish the "Present This" and "PR Babysit" skills to the community forum this week.

Juan will deploy the AI photo booth at a first live event, document it on video, and present a polished demo on a future call.

Ryan will share the email-connector code with Ty once tested, enabling reuse in the Q business intelligence system.

Ty will fix ShipSafe UX friction so signing up to present automatically joins the live session, and will DM coach access to interested members.

Patrick will adapt Shakur's Claude.md configuration to add Antigravity CLI routing for web search.