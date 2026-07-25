📝 SUMMARY

This week's call featured live testing of Ty's session management tool ShipSafe alongside deep dives into autonomous AI training delivery, multi-model orchestration strategies for cost control, and automated DevOps workflows. Patrick demonstrated how Claude Code skills can self-deliver training at scale and autonomously manage pull requests, while Juan prepared for his AI photo booth launch and Ryan shared progress on estate agent CRM and hedge fund tools. The group refined approaches to preventing AI covert actions through personality configuration and routing tasks across Claude, Codex, and GPT models to optimize token spend.

💡 KEY INSIGHTS

Package training as deployable skills. Patrick demonstrated creating self-updating training systems as zip files containing materials, trainer guides, and Claude Code skills that autonomously guide users through exercises—enabling one trainer to scale to thousands without proportional effort.

Place personality blocks at the user level. Adding an "honesty over compliance" configuration to ~/.claude/claude.md (user-level, not project-level) prevents Claude from taking silent, destructive actions like database deletions by forcing it to surface disagreements rather than act covertly.

Orchestrate across models to cut costs. Route planning and orchestration to high-capability models like Claude, then hand off token-heavy grunt work to cheaper models or specialized tools. This maintains output quality while significantly reducing token burn.

Use Firecrawl for research workflows. Firecrawl now offers a generous free tier and runs independently of Claude tokens, making it ideal for web scraping and research without consuming your API budget.

Automate PR management end-to-end. A "PR Babysit" skill can poll open pull requests, respond to CodeRabbit or human reviewer comments, trigger fixes, and auto-merge once clean—eliminating the manual copy-paste loop between review tools and your AI coder.

Target corporate events first for hardware products. For Juan's AI photo booth, corporate events provide the revenue base to subsidize smaller personal events. Getting on venue preferred-supplier lists creates zero-cost distribution where every event becomes a warm lead.

Monetize inventory apps through affiliates. Coupling a photo-based inventory app with Amazon affiliate links for organizational products or restocking items creates natural monetization layers alongside insurance documentation use cases.

Structure wearable capture for downstream agents. Connecting a Fieldy wearable via webhook to a personal Hermes agent ensures conversation summaries are structured for immediate use—such as feeding directly into Claude Code to start projects with full personal context already loaded.

❓ KEY Q&A

Q: How does Ty's local requirements-gathering setup compare to AWS Kiro mobile?
A: Ty built a similar system using local models on his Proxmox server to develop requirements via voice chat, then sends that structured data to Claude for code generation. This keeps context private and minimizes external token usage.

Q: Where should the "honesty over compliance" personality block live?
A: In ~/.claude/claude.md at the user level, not the project level. This applies automatically to every Claude Code session on your machine without manual invocation.

Q: Why switch from Gemini CLI to Antigravity CLI?
A: Gemini CLI is being deprecated; Antigravity CLI is its replacement for Google-backed web search in agentic workflows.

Q: How do you integrate email systems for monitoring without using Google OAuth?
A: Use service tokens specific to the client's email platform rather than OAuth, allowing integration with various systems beyond just Google Workspace.

Q: Why keep cognitive backlog in GitHub Issues instead of Notion?
A: Raw text in GitHub Issues acts as a universal source that any agent or pipeline can listen to without additional integration layers. GitHub plus VS Code covers the workflow without needing external task managers.

🛠️ TOOLS AND CONCEPTS MENTIONED

ShipSafe / FrankLabs — Session management tool adding presenter queues, countdown timers, and polling to any video call via shared URL.

Claude Code — Anthropic's agentic coding tool used for autonomous training delivery, skill creation, PR management, and presentation generation.

Fieldy — Wearable AI capture device connected via webhook to personal agents for structured meeting summarization.

Hermes — Self-hosted personal AI agent (accessible remotely via Tailscale) that processes wearable transcripts and structures outputs for downstream use.

Firecrawl — Web scraping service with a generous free tier that runs independently of Claude tokens, ideal for research-heavy workflows.

Antigravity CLI — Replacement for the deprecated Gemini CLI; recommended for web search tasks in multi-model routing configurations.

Codex CLI — OpenAI's CLI coding agent used alongside Claude in multi-model orchestration setups.

Multi-model Orchestration — Routing tasks between Claude, Codex, and GPT-4o based on task type to optimize cost and capability.

PR Babysit Skill — Claude Code skill that polls pull requests, responds to reviewer comments, triggers fixes, and auto-merges when clean.

Present This Skill — Skill that reads repo documentation, builds an Astro-based HTML site, deploys to Cloudflare, and registers a subdomain on Hostinger from a single command.

LoopForge — Pipeline tool for automated idea-to-project workflows from GitHub Issues cognitive backlogs.

Astro — Static site framework used for generating documentation and presentation websites.

Proxmox — Local server environment for running private LLMs to minimize external token usage and maintain data privacy.

📎 SHARED RESOURCES

ShipSafe Session Demo: https://shipsafe.franklabs.io/session/TTRB7P/queue

Omnigent Repository: https://github.com/omnigent-ai/omnigent.git

Theo on Multi-model Routing: https://x.com/theo/status/2072482460122964067

Patrick's Personality Block Gist: https://gist.github.com/hopchouinard/333cc020bbdc4ccede8ea023c3b6d62c

Healthcare BI Demo Site: https://coralharbourclinic.com/

Fathom Settings: https://fathom.video/customize

🔄 FOLLOW-UPS WORTH EXPLORING

Shakur will share his multi-model Claude.md routing configuration files (including Codex Computer Use, Implementation, and View skills) via GitHub repo or gist.

Patrick will publish both the "Present This" skill (auto-build and deploy presentation sites) and the "PR Babysit" skill to the community forum this week.

Juan will deploy the AI photo booth at a first live event, document the process on video with a dedicated camera operator, and present a polished demo on a future call.

Ryan will share the email-connector code segment with Ty once tested, enabling reuse in the Q business intelligence system.

Ty will fix ShipSafe UX friction so signing up to present automatically joins the live session, and will DM coach access to interested community members.

Patrick will adapt Shakur's shared Claude.md configuration to add Antigravity CLI routing for web search tasks.