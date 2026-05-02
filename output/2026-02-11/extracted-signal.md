## general

This was a roundtable coaching/peer-group call where members shared project updates, discussed AI tooling, and exchanged advice on client work and business strategy. Patrick Chouinard facilitated most of the session after the scheduled host (Paul Miller) arrived late. The group consisted of recurring members including Marc Juretus, Ty Wells, Scott Rippey, Jake Maymar, Ryan C, Morgan Cook, Paul Miller, and Raghav Ram.

The primary technical thread running through the session was OpenClaw (formerly ClawedBot), an open-source AI agent framework. Patrick, Ty, and Scott all described their personal deployments of it, covering architecture decisions around memory layers, security isolation, messaging interfaces (Telegram, Discord, WhatsApp), and model routing via OpenRouter. A secondary thread covered members' individual app projects: Marc's fitness app and Stock School app, Scott's developer productivity tool "Clarity," Ryan's social platform and upcoming e-commerce build, and Patrick's AI news monitoring and briefing system deployed on Databricks.

The latter portion of the call shifted toward business strategy, prompted by Paul Miller's new logistics-sector client engagement. The group discussed value-based pricing, the importance of understanding business problems before proposing AI solutions, and how to position themselves as business-first consultants rather than AI-first vendors. Jake Maymar shared a story about completing months of expected Jira backlog work in 30 minutes using Claude, which sparked discussion about managing client expectations and pricing for value rather than time.

Morgan Cook contributed a technical debugging segment covering a Drizzle DB connection pool issue, a Sharp library cross-platform incompatibility between Windows development and Vercel (Linux) deployment, and a Supabase/Vercel IPv4 limitation that blocked a planned multi-tenant Postgres role architecture.

## insights

- **Patrick:** Any hosting platform used with an AI agent must have a CLI so the agent can manage deployments autonomously and monitor/correct errors without human UI interaction.
- **Patrick:** Claude Code deployed on Databricks entirely on its own — including configuration, permissions, and documentation — for a platform Patrick had never used before, demonstrating agents can operate beyond the developer's own expertise.
- **Patrick (on OpenClaw security):** The platform will never be truly hardened; the correct approach is to isolate it aggressively — give it its own email, GitHub account, calendar, and API keys with strict spending caps — so the "blast radius" of any mistake is minimized.
- **Patrick:** Splitting an AI agent's conversations into dedicated channels (Discord or Telegram groups) keeps context windows short and precise, reducing token burn and improving response quality.
- **Patrick:** Layered memory architecture — global identity/personality, channel-specific memory, and per-conversation context — allows the agent to receive only what it needs to know, improving both economy and precision.
- **Patrick:** Using OpenRouter to route day-to-day tasks to cheaper models (Qwen 3, Kimi 2.5) and reserving Claude Opus calls via Claude Code headless mode (using an existing subscription) dramatically reduces costs without sacrificing capability for complex tasks.
- **Ty:** Building your own secure version of the agent framework from scratch (using NanoClaw or OpenClaw as a reference) is preferable to loading third-party skills from unknown authors.
- **Scott:** Value-based pricing eliminates the awkward situation of having to fake that work took longer than it did; price the solution's value, not the hours.
- **Jake:** Completing a large Jira backlog in 30 minutes with Claude caused a client to panic about payment timelines — a reminder that over-delivering without expectation-setting can create friction.
- **Jake:** The key question to anchor a client stakeholder is "how does this make me look good inside my company?" — ego and internal optics often drive decisions more than technical merit.
- **Paul:** Clients want to know you understand their business problem first; leading with AI capabilities before demonstrating business understanding undermines trust.
- **Paul:** Pre-meeting deep research (using AI) on the people and company you're meeting with is a high-leverage workflow — knowing their competitive landscape, pain points, and personnel before walking in.
- **Patrick:** Whenever the unit cost of work drops, it creates the possibility to do work that was previously too expensive — AI doesn't just speed things up, it expands the scope of what's worth doing.
- **Morgan:** A silent failure in Drizzle DB was caused by a missing `prepare: false` flag on the connection stream; the connection pool was resetting and dropping prepared transactions without throwing errors.
- **Morgan:** Sharp (image processing library) requires both Linux and Windows binaries listed as optional dependencies in `package.json`, plus a `vercel.json` with `pnpm install --include=optional`, when developing on Windows and deploying to Vercel.
- **Morgan:** Vercel's IPv4-only support blocks the use of dedicated Postgres roles for multi-tenant architectures in Supabase; the Postgres superuser connection string must be used instead until IPv6 is supported.
- **Patrick:** Compiling your own project-specific documentation (from docs, articles, GitHub issues, Reddit) and growing it over time reduces AI coding errors by roughly an order of magnitude compared to relying solely on Context7.

## qa

**Q (Marc):** What use case does OpenClaw open up that something like APScheduler wouldn't handle?
**A (Patrick):** APScheduler fires at fixed times; OpenClaw makes decisions. For example, it monitors Montreal's light rail system and decides whether to wake Patrick up early based on compounding traffic effects — not just current conditions, but predicted downstream impact. It also manages a GitHub project, proposes daily ideas, and can be redirected mid-day via a simple text message.

**Q (Marc):** What's a good alternative to Supabase for authentication and Postgres hosting?
**A (Paul):** Clerk is elegant for authentication with a capable free tier. For hosting, Docploy manages Docker deployments and security and can spin up a Postgres database alongside your app.

**Q (Jake):** How do you route tasks to Claude Opus specifically from within OpenClaw without violating terms of service?
**A (Patrick):** A script calls `claude -p` (Claude Code in headless/non-interactive mode) with the prompt. Claude Code uses the existing subscription OAuth — you're not sharing credentials with a third party — so it's within ToS and leverages already-paid tokens.

**Q (Raghav):** I have meetings with business owners coming up. Is there a standard template or structured way to gather information from them using AI?
**A (Patrick/Ty):** Record everything — use a tool like Fathom, Plaud, or Zoom/Teams transcription. Once you have a transcript, any analysis or template-filling is a prompt away. Don't search for templates; ask the AI to build one tailored to your specific situation on the spot. Also do deep research on the attendees before the meeting so you walk in knowing their business, competitors, and pain points.

**Q (Jake):** I completed months of expected work in 30 minutes. Do I tell the client, or wait?
**A (Scott):** Move to value-based pricing so the question never arises — you're pricing the solution's value, not the time spent. That removes the incentive to fake elapsed time.

**Q (Ryan):** I'm building a MailChimp-like email system into a client's site using N8N cloud, but costs will be high. Any suggestions?
**A (Scott):** Run N8N locally on a secured virtual environment instead of the cloud instance. Good hosting options exist that work well with self-hosted N8N and will eliminate the per-execution cost at scale.

## tools

- **OpenClaw (formerly ClawedBot)** — Open-source AI agent framework; central topic of discussion for personal assistant deployments
- **NanoClaw** — Simpler, lighter starting point for building a personal AI agent; mentioned as an alternative entry point to OpenClaw
- **Claude Code** — Anthropic's agentic coding tool; used in headless mode as a sub-tool called by OpenClaw for complex tasks
- **Cursor** — AI-powered IDE; mentioned as a comparison point to Claude Code (Claude in Cursor vs. Claude Code)
- **OpenRouter** — API routing service; used by Patrick to switch between cheap models (Qwen 3, Kimi 2.5) for day-to-day agent tasks
- **Cloudflare Pages** — Static site hosting; Patrick hosts his personal site there with free storage and CLI-based deployment
- **Railway** — PaaS hosting; Marc runs his fitness app backend on it
- **Vercel** — Frontend hosting; Marc uses it for Stock School front-end; Morgan encountered Sharp/IPv4 issues deploying there
- **Google Cloud** — Backend hosting; Marc uses it for the Stock School app backend
- **Databricks Apps** — Patrick deployed an Astro static site to it as a proof-of-concept; Claude Code handled the entire setup
- **Proxmox** — Hypervisor; Patrick runs OpenClaw in a dedicated VM on his Proxmox server
- **Discord** — Messaging platform; Patrick migrated from Telegram to Discord for multi-channel AI agent interaction
- **Telegram** — Messaging platform; Ty uses it as the interface for his secure AI agent; Patrick previously used it
- **WhatsApp** — Messaging platform; Scott initially used it for OpenClaw; Ty uses it for a group-chat assistant
- **GitHub Projects** — Patrick uses it for his AI agent's task/project tracking and backlog management
- **Obsidian** — Note-taking/knowledge base app; Patrick syncs his agent's memory/journal into an Obsidian vault via GitHub
- **Remotion** — React-based video creation library; Scott used it to generate an animated promo video for Clarity from app data
- **Suno** — AI music generation; Scott used it to create background music for the Remotion-generated promo video
- **Context7** — Documentation retrieval tool for AI coding; mentioned as useful for new projects but less efficient than custom docs for established ones
- **Drizzle ORM** — TypeScript ORM; Morgan hit a connection pool bug (`prepare: false` missing) causing silent transaction failures
- **Sharp** — Node.js image processing library; Morgan encountered Windows/Linux binary incompatibility when deploying to Vercel
- **Supabase** — BaaS platform; Marc uses it for auth and Postgres; Morgan hit IPv4 multi-tenant role limitations with it on Vercel
- **Clerk** — Authentication service; Paul recommended it as an alternative to Supabase auth
- **Docploy** — Docker deployment management interface; Paul uses it to manage hosting and spin up Postgres instances
- **N8N** — Workflow automation; Ty uses it for invoicing; Ryan plans to use it for bulk email; Scott suggested self-hosting to reduce cost
- **FreshBooks** — Invoicing SaaS; Ty replaced it by having his AI agent build a custom invoicing system
- **Stripe** — Payments; Scott integrated it into Clarity with test mode on the dev branch; Jake's friend uses it to gate meeting bookings
- **Jira** — Project management; Jake connected it to Claude to clear a large backlog in ~30 minutes
- **Astro** — Static site framework; Patrick used it for his AI news briefing site deployed to Databricks
- **Fathom / Plaud** — Meeting recording tools; Patrick mentioned both for capturing transcripts of client meetings
- **FinHub** — Financial data API; Marc uses it for real-time stock data in Stock School
- **Grok (xAI)** — AI platform; Marc used it to generate workout demonstration videos for his fitness app
- **Base44** — No-code/AI app builder; Paul mentioned building a budgeting app in it quickly at end of call

## links

No explicit URLs were shared in the transcript.

## decisions

- **Patrick** will continue rebuilding his OpenClaw instance, migrating from Telegram to a dedicated Discord server with multi-channel support and a new channel-specific memory layer.
- **Patrick** will formalize the model-routing overlay (Qwen 3 → Kimi 2.5 → Claude Code headless for Opus) as a reusable layer on top of OpenClaw without modifying the core.
- **Marc** will set up his own OpenClaw/agent instance after being persuaded by the group's use cases.
- **Marc** will investigate Clerk and Docploy as alternatives to Supabase for authentication and database hosting.
- **Scott** will set up a proper dev/main branch workflow for Clarity and begin beta testing with friends at $20/month and $50/month tiers.
- **Ryan** will contact Scott to discuss self-hosting N8N on a virtual environment for his client's bulk email system to reduce costs.
- **Ryan** will reach out to the group when he begins the US Postal Service API and label printer integration for guidance.
- **Raghav** will record his upcoming client meetings (using Fathom, Plaud, or Zoom) and use AI to analyze transcripts and fill any templates rather than searching for pre-built templates.
- **Raghav** will conduct deep AI research on the business owners he is meeting with before the meetings.
- **Morgan** will carry forward his project-specific guides folder (documenting the Drizzle, Sharp, Supabase/IPv4 fixes) into future projects.