## general

This was a weekly group coaching/show-and-tell call hosted by Patrick Chouinard, with regular participants including Ty Wells, Juan Torres, Ryan C, Shakur, and Elena. The session opened with Ty Wells live-testing a session management tool he is building (ShipSafe/FrankLabs), which adds polling, presenter queuing, and countdown timers to any video call. Participants interacted with the tool in real time, surfacing UX friction points.

Patrick shared two main concepts from his day job: (1) a self-updating, Claude Code–delivered training system that packages training material, a trainer's guide, and a skill into a deployable zip file, allowing Claude to guide users through exercises autonomously; and (2) a suite of Claude Code skills including a "present this" skill that reads repo documentation, builds an Astro-based HTML site, deploys it to Cloudflare, and registers a subdomain on Hostinger — all from a single command. He also described a "PR Babysit" skill that polls open pull requests, responds to reviewer comments, triggers fixes, and auto-merges once all issues are resolved.

Juan Torres updated the group on his AI photo booth studio project (image-to-image pipeline for events), which passed a load/networking stress test and is nearly ready for its first live deployment. Ryan C covered multiple parallel projects: a redesigned social media manager tool, an Android-based digital signage box, a CRM/AIOS for estate agents with email and WhatsApp integration, and a hedge fund expense management application being built for a financial-director contact in London. Shakur shared several projects in progress: an AI auditing platform, an automated postcard-based client outreach tool, a photo-based inventory app, and an SOP generator that extracts frames and transcripts from videos.

The session closed with a discussion of Claude.md personality blocks at the user level — Patrick shared a gist of his "honesty over compliance" personality configuration — and a broader conversation about multi-model orchestration (routing tasks to Codex, ChatGPT/GPT-4o, and Claude based on task type), Firecrawl for web research, and the Antigravity CLI as a replacement for the deprecated Gemini CLI.

## insights

- **Patrick:** Building Claude Code training as a self-deliverable skill package (zip file with trainer's guide, exercises, and a skill that orchestrates the session) allows one trainer to scale to thousands of users without proportional effort.
- **Patrick:** Connecting a wearable (Fieldy) via webhook to a personal Hermes agent means conversation summaries are structured for downstream use (e.g., feeding directly into Claude Code to start a project) because the agent already has full personal context.
- **Patrick:** Adding a "honesty over compliance, always non-negotiable" personality block to Claude.md at the user level — rather than the project level — appears to prevent the silent, underhanded actions (including database deletions) that many users report, because the model surfaces disagreements rather than acting on them covertly.
- **Juan:** AI is an amplifier of user deficiencies as well as attributes; many reported Claude Code disasters (deleted repos, wiped databases) likely reflect impulsive user behavior rather than model failure alone.
- **Ryan:** For the lesson-plan/worksheet cost problem, orchestrate: use a top model (e.g., Claude) only for planning and orchestration, then hand off token-heavy grunt work to a cheaper model — same output quality, significantly lower cost.
- **Ryan:** Firecrawl has introduced a generous free tier and runs on its own service, so it does not consume Claude tokens for web scraping — a meaningful cost saving for research-heavy workflows.
- **Patrick:** Antigravity CLI is replacing the deprecated Gemini CLI and is worth adding to multi-model Claude.md routing configurations, specifically for web search tasks.
- **Shakur:** Routing tasks from Claude to multiple models (Codex, ChatGPT/GPT-4o, Claude Sonnet) via Claude.md instructions and skills significantly reduced token burn.
- **Patrick:** A "PR Babysit" skill that polls a PR, responds to reviewer comments, fixes issues, and auto-merges when clean eliminates the manual copy-paste loop between code review tools and the AI coder.
- **Ryan (on Juan's photo booth):** Getting onto venue preferred-supplier lists is the highest-leverage distribution strategy — every event at that venue becomes a warm lead with no additional sales effort.
- **Patrick (on Juan's photo booth):** Corporate events provide the revenue base to subsidize smaller personal events; target corporate first to fund the machine.
- **Shakur:** Coupling a photo-based inventory app with Amazon affiliate links (suggesting organizational products or restocking items) and insurance documentation use cases are natural monetization extensions.

## qa

**Q (Elena):** Did you hear about AWS Kiro mobile — they announced you can talk your plan from their mobile app?
**A (Ty Wells):** I built my own version that does exactly that: I chat with local models on my Proxmox server to develop requirements, then send that data to a Claude session which builds the actual code. I haven't used AWS Kiro because I already have my own, and using local models means very few external tokens and the context stays private.

**Q (Juan Torres):** Have you tried using the Q/business intelligence system in your own businesses?
**A (Ty Wells):** Yes, it's running in two of my three businesses, but currently only I can see the output. I want to identify the gaps first before surfacing them to staff — once I tell them they're being monitored, they'll start correcting behavior, so I need the baseline gap data first.

**Q (Ryan C):** How are you tapping into clients' emails for the Q system?
**A (Ty Wells):** Using a service token rather than Google OAuth, so it's not tied to Google specifically. Whatever email system the client uses, you integrate via the appropriate token/connector for that platform.

**Q (Patrick Chouinard):** If we want to use your session management tool, what are the protocols?
**A (Ty Wells):** It's currently gated for coaches. DM me your email and I'll add you as a coach so you can use it anytime.

**Q (Elena):** How do you invoke the personality block — when do you load it into a Claude Code session?
**A (Patrick Chouinard):** It lives in `~/.claude/claude.md` (the user-level file, not a project-level file). Because it's at the user level, it applies automatically every time you use Claude Code on your machine — no manual invocation needed.

**Q (Juan Torres):** Why Antigravity CLI instead of Gemini CLI?
**A (Patrick Chouinard):** Gemini CLI is being deprecated and replaced by Antigravity CLI, so that's the current correct tool to use for Google-backed web search in agentic workflows.

**Q (Juan Torres):** Have you thought about connecting your cognitive backlog (GitHub Issues via MCP) to a task manager like Notion?
**A (Patrick Chouinard):** I tried Notion and Obsidian integrations but stopped — GitHub + VS Code covers everything I need. Keeping ideas as raw text in GitHub means any agent or pipeline (including a LoopForge pipeline I'm building) can listen to that repo as an output source without needing another layer.

## tools

- **ShipSafe / FrankLabs** — Ty's session management tool being live-tested; adds presenter queue, countdown timer, and polling to any video call via a shared URL
- **Claude Code** — Anthropic's agentic coding tool; used by Patrick for training delivery, skill creation, PR babysitting, and presentation site generation
- **GitHub Copilot** — mentioned alongside Claude Code as a tool Patrick trains enterprise users on
- **Fieldy** — wearable AI capture device; Patrick connected it via webhook to his Hermes agent for meeting summarization
- **Hermes (personal agent)** — Patrick's self-hosted personal AI agent, accessible remotely via Tailscale; used to query Fieldy transcripts and structure outputs
- **Tailscale** — used by Patrick to expose his home-hosted Hermes agent securely from anywhere
- **Limitless** — wearable/AI capture device Ty was previously using; being replaced by Omni device (shutting down September)
- **Omni** — Ty's new wearable AI capture device replacing Limitless
- **Proxmox** — Ty's local server running local LLMs for his requirements-gathering voice workflow
- **AWS Kiro** — AWS mobile app for talking through plans/requirements; mentioned by Elena from the AWS NY Summit announcement
- **Datadog** — mentioned by Juan as having gamified cloud architecture monitoring across AWS, Azure, and GCP at the LA AWS Summit
- **Cursor** — IDE with workspace support; Ryan mentioned discovering multi-workspace capability (multiple terminal sessions) recently
- **Fable (Claude)** — Ryan's term for Claude's agentic coding mode; he noted Opus 4.8 vs. GPT-5.6 comparison and token efficiency issues
- **Claude Design** — used by Ryan for UI redesign of his social media manager tool
- **Firecrawl** — web scraping service with a new generous free tier; runs independently of Claude tokens, recommended for research tasks
- **Antigravity CLI** — replacement for the deprecated Gemini CLI; recommended by Patrick for web search in multi-model Claude.md routing
- **Codex CLI** — OpenAI's CLI coding agent; used in Shakur's and Patrick's multi-model orchestration setups
- **ChatGPT / GPT-4o** — used as one of the routed models in Shakur's multi-model Claude.md setup
- **LoopForge** — pipeline tool Patrick is using to build an automated idea-to-project pipeline from his GitHub Issues cognitive backlog
- **Astro** — static site framework (v7) used by Patrick's "present this" skill to generate presentation websites
- **Cloudflare / Wrangler CLI** — used by Patrick's "present this" skill to deploy generated presentation sites
- **Hostinger** — Patrick's DNS provider; his skill auto-creates subdomains pointing to Cloudflare deployments
- **Auth0** — used by Patrick for authentication in his MCP/cognitive backlog app deployed on Vercel
- **Vercel** — deployment platform for Patrick's MCP app; also mentioned as an alternative deployment target
- **CodeRabbit** — AI code review tool that posts PR comments; Patrick's PR Babysit skill responds to its comments automatically
- **GitHub Issues / Gist** — Patrick uses Issues as a "cognitive backlog" for ideas captured via MCP; Gist suggested for sharing single-file configs
- **Meta API (WhatsApp)** — Ryan integrating WhatsApp messaging into his estate agent CRM/AIOS
- **Amazon Affiliate** — suggested by Shakur and Ryan as a monetization layer for the photo inventory app
- **T3 Chat / Theo's Claude.md** — Theo's public post/video on multi-model Claude.md routing; Shakur and Patrick both referenced it

## links

- `https://shipsafe.franklabs.io/session/TTRB7P/queue` — Ty's live session management tool demo link shared during the call
- `https://github.com/omnigent-ai/omnigent.git` — Ty's Omnigent repository shared in chat
- `https://coralharbourclinic.com/` — fictional clinic demo site Ty shared to illustrate the Q/business intelligence box in a healthcare context
- `https://x.com/theo/status/2072482460122964067` — Theo (T3 Chat) tweet/post on multi-model Claude.md routing configuration
- `https://gist.github.com/hopchouinard/333cc020bbdc4ccede8ea023c3b6d62c` — Patrick's Claude.md personality block gist ("honesty over compliance" configuration)
- `https://fathom.video/customize` — Fathom notetaker settings link (appeared in direct message from Fathom bot)

## decisions

- **Ty Wells** will fix the UX friction in ShipSafe so that signing up to present automatically joins the live session (no separate "join session" step required).
- **Ty Wells** will DM Patrick and others their coach-level access to ShipSafe so they can use it in upcoming calls.
- **Patrick Chouinard** will DM Ty to practice using ShipSafe together before the next weekly call.
- **Ty Wells** will switch from polling to webhook-based integration for his new Omni wearable device.
- **Shakur** will create a GitHub repo (or gist) and share his Claude.md multi-model routing files (including Codex Computer Use, Codex Implementation, Codex View skills, and the main Claude.md) with the group via the community platform.
- **Patrick Chouinard** will publish the "present this" skill (auto-build and deploy a documentation/presentation site from a repo) to the community forum this week.
- **Patrick Chouinard** will publish the "PR Babysit" skill to the community forum this week.
- **Patrick Chouinard** will adapt Shakur's shared Claude.md to add Antigravity CLI routing for web search tasks.
- **Juan Torres** will find a first live event to deploy the AI photo booth, document the process on video (with a dedicated camera operator), and share the footage with the group.
- **Juan Torres** will present a polished pitch/demo of the AI photo booth on a future weekly call once it has been deployed at a real event.
- **Ryan C** will share the email-connector code segment with Ty once it is built and tested, so Ty can reuse it in the Q system.