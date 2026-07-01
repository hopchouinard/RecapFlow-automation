## general

This was a group coaching/show-and-tell call for an AI-focused community, facilitated by Patrick Chouinard and Paul Miller, with a guest appearance by Brandon Hancock. The session opened with Brandon sharing business updates on his EMS software startup — including a conference booth, a growing sales pipeline (~$100K in deals), cold outreach via personalized Loom videos, and an upcoming meeting with a PE firm exploring distribution and acquisition. He also introduced a new gadget purchase: Even Realities smart glasses with Claude Code and Codex integrations.

Members then took turns sharing their own projects. Ty Wells demonstrated a custom app he built to recover a lost Limitless wearable device by cross-referencing Garmin GPS data with Limitless life-log timestamps — and then used the same app to find it again the next day. He also showed an "Omaha Tee Times" golf booking aggregator and a voice-driven coding agent running on Proxmox via LiveKit that lets him code hands-free from his phone. Patrick Chouinard presented AgentOps, a homelab management harness built on top of Hermes, featuring MCP CLI connectors, Infisical secret management, NATS as an enterprise service bus, automated PR review loops using Claude Code + Codex + GitHub Copilot, and a Loop Forge pipeline that converts conversational intent into structured GitHub issues for background processing.

Paul Miller discussed his CTO's adoption of AI to audit and refactor 10 years of legacy code, and a new enterprise logistics client struggling with undefined internal processes. Dave Gottschalk introduced his "Payback Owned" data-ownership economy concept. Ryan C shared work on a Kratom business website/CRM, an AI-forward CRM for UK estate agents, a custom real-estate photo enhancement pipeline using Higgsfield/NanoBanana, and a lead-capture app that photographs vans and auto-generates outreach emails. Juan Torres showed a hardware AI photo booth (mirror booth) with a multi-model diffusion pipeline, touch interface, and CloudWatch observability, sparking an extended business-model brainstorm around franchise/vending-machine and wedding-venue partnership models. Scott Rippey demonstrated a YouTube channel with an AI avatar, a Google Workspace agent via Telegram/n8n, and a custom Claude Code security review hook system that runs multi-model adversarial reviews (Claude Opus, Claude Sonnet, Codex) on every git push and stores results in Supabase. Bastian Venegas Arevalo closed by presenting Pixir, an Elixir-based agentic harness designed to run sub-agents with dramatically reduced memory overhead compared to native Codex sub-agents, using WebSockets and prefix caching for cost efficiency.

## insights

- **Brandon on cold outreach feedback loops:** Send personalized Loom videos to prospects, then extract the exact language customers use on discovery calls and fold it back into the next pitch deck iteration — over time you articulate their problems better than they can, which dramatically improves conversion.
- **Brandon on sniper vs. spray outreach:** With a finite addressable market (e.g., 18,000 EMS agencies), high-value, hyper-personalized outreach beats mass email blasting — burning the market with low-quality touches is an irreversible mistake.
- **Brandon on reviewer bottleneck:** When AI accelerates code production 10x, the human review cycle becomes the new bottleneck. Sandboxed ephemeral environments (e.g., Supabase branches) and parallel feature development are the solution.
- **Brandon on working backwards from revenue goals:** Calculate exactly how many daily outreaches are needed to hit target revenue within a defined timeframe; this converts an abstract goal into a simple daily checklist and removes timeline anxiety.
- **Brandon on deflationary AI margins:** As AI model costs fall over time, businesses built on AI-generated outputs (images, video, code) see margins improve automatically — the capability is locked in at today's price, but costs drop in 6–8 months.
- **Brandon on hardware + software moats:** Combining physical hardware with software (as Juan and Ryan are doing) creates a significantly deeper competitive moat than pure software plays.
- **Brandon on the vending machine / franchise model for Juan's photo booth:** Prove the unit economics yourself first (10 events), then give hardware to wedding venues for free and take a revenue share — aligns incentives and removes geographic scaling constraints.
- **Patrick on stress-driven creativity:** Stress correlates with increased creative output; Claude Code serves as a relaxation mechanism as much as a productivity tool.
- **Patrick on automated PR review loops:** Instructing Claude Code to "push a PR, then monitor it for 30 minutes and resolve every comment" creates a fully automated code review cycle when combined with Codex and GitHub Copilot as reviewers.
- **Scott on adversarial model review:** You should not use the same model that wrote the code to review it — using Codex as an adversarial reviewer against Claude-written code catches edge cases neither model would self-identify.
- **Ty on creative problem-solving with AI:** Cross-referencing Garmin GPS data with Limitless life-log timestamps to locate a lost wearable is a practical example of composing existing data sources with a quickly built custom app to solve real-world problems.
- **Scott on data as the primary asset:** The most valuable thing an AI-augmented developer accumulates is their own structured data (documentation, review history, app context) — the AI models are commodities, but the data is proprietary.
- **Biggi (from chat):** Prediction from AI Engineer World's Fair — developers will move coding environments off laptops within 6 months as always-on agents require persistent compute.

## qa

**Q (Dave Gottschalk):** How do you get the first meeting through cold outreach — specifically, you sent a Loom video to someone's email and they just responded wanting a demo?
**A (Brandon Hancock):** Yes — the email identifies who I am, how I found them (e.g., saw their ambulance on the road), names the specific problem they're likely facing, says I made a video showing how we solve it and what we estimate it could save them, and ends with a single low-friction CTA to hop on a call. The Loom video itself covers: 30-second app demo, proof from similar agencies, and a personalized savings estimate. Yesware tracks opens and link clicks so I know who engaged.

**Q (Juan Torres):** Did you have any problems with Claude Code refusing to do web scraping for collecting emails, citing ethics?
**A (Brandon Hancock):** Claude Opus has been a stickler about it, but Claude Haiku has not raised issues. The data I'm scraping is all publicly available (state registries, websites) — it may be that the model distinguishes between public official/business data and private individual data.

**Q (Juan Torres):** What infrastructure are you using for your app?
**A (Brandon Hancock):** Supabase as the core backend. AWS strictly for accessing Claude (Anthropic models via Bedrock). Google Cloud for Gemini access and running backend jobs (similar to a RAG pipeline). Supabase handles HIPAA and SOC2 compliance as paid add-ons (~$300–$400/month each).

**Q (Brandon Hancock to Patrick):** For Hermes, are you using OpenAI or a different model/router?
**A (Patrick Chouinard):** OpenAI on the $100/month subscription. He has $100/month on both OpenAI and Anthropic. Claude Code is used for building; Hermes runs on OpenAI; Codex and GitHub Copilot monitor PRs.

**Q (Brandon Hancock to Scott):** Is the security review hook running at a global level, per customer, or per repo?
**A (Scott Rippey):** Fully customizable — model selection, review settings, everything is configurable per repo or globally via the Supabase database that the hooks read from.

**Q (Brandon Hancock to Bastian):** What model does Pixir connect to, and how?
**A (Bastian Venegas Arevalo):** Currently OpenAI only, using the user's existing OpenAI subscription — chosen because it's the most universally held subscription. Anthropic was avoided because Claude can sometimes restrict or ban API usage in certain contexts.

**Q (Brandon Hancock to Juan):** What are the unit economics of the photo booth — how many events to break even?
**A (Juan Torres):** Hasn't fully modeled it yet, but estimates break-even within a couple of events on hardware. Acknowledged that time investment also needs to be factored in. Ryan C added that at his friend's wedding, a comparable (but far simpler) iPad-in-a-box photo booth charged £600/day.

## tools

- **Even Realities smart glasses** — Brandon purchased these; AR display glasses with Claude Code and Codex integrations, microphone, companion ring controller, and Limitless-style meeting transcription
- **Claude Code** — Primary coding agent used by Brandon, Patrick, Scott, Ty, and others for building, reviewing, and iterating on projects
- **Codex (OpenAI)** — Used by Patrick for Loop Forge workflow automation and by Scott as an adversarial PR reviewer
- **GitHub Copilot** — Used by Patrick alongside Codex to post automated PR analysis comments
- **Limitless (wearable)** — Ty's wearable device; its life-log timestamps were used to locate the lost device via GPS cross-reference
- **Garmin GPS** — Ty cross-referenced Garmin activity data with Limitless logs to pinpoint where the device was lost on a golf course
- **BlueFi (iOS app)** — Ty used this iOS app to run Bluetooth-based GPS tracking in the browser on his phone
- **LiveKit** — Ty built a voice-driven coding agent session using LiveKit, allowing hands-free interaction with his codebase from a phone
- **Proxmox** — Patrick's homelab hypervisor; hosts Hermes and other VMs/containers managed by AgentOps
- **Hermes** — Patrick's self-hosted AI agent framework (OpenAI-backed); serves as the automated management layer for his homelab; Scott also adopted it after abandoning Ironclaw
- **Infisical** — Patrick's secret management system ("poor man's Vault") used to handle API key rotation for all homelab agents
- **NATS (N-A-T-S)** — Patrick uses this as a personal enterprise service bus / message broker to route data between all homelab services (Prometheus, Grafana, Authentik, etc.)
- **Authentik** — Patrick's self-hosted authentication/SSO layer for homelab services
- **Traefik** — Patrick's reverse proxy for homelab, mentioned as part of the AgentOps connectivity stack
- **Uptime Kuma** — Patrick's server monitoring tool, one of the services publishing data to the NATS service bus
- **Cloudflare Pages** — Patrick deploys documentation and project sites here; a Claude Code skill automates project creation, DNS CNAME setup on Hostinger, and deployment in one shot
- **Hostinger** — Patrick's primary domain registrar; subdomains are auto-created via Claude Code skill
- **LanceDB** — Paul Miller is using this for organizing and searching retail audit/notes data; Patrick also uses it for the community brain knowledge base
- **Supabase** — Used by Brandon for HIPAA-compliant backend with ephemeral branching for sandboxed feature development; used by Scott as the database/dashboard backend for his security review hook system
- **AWS** — Brandon uses it solely to access Anthropic's Claude models via Bedrock
- **Google Cloud** — Brandon uses it for Gemini access and backend job processing
- **Apify** — Brandon uses it as a tool call within his Claude agent for LinkedIn scraping when direct contact info isn't available
- **Yesware** — Brandon uses this email tracking tool to monitor open rates, link clicks, and engagement on cold outreach emails
- **Instantly** — Mentioned by Brandon as a mass cold email tool he deliberately avoids in favor of high-value personalized outreach
- **Loom** — Brandon records personalized Loom videos as the core of his cold outreach strategy
- **Higgsfield** — Ryan uses this for AI image generation in his real-estate photo enhancement pipeline
- **NanoBanana** — Ryan uses this (via Higgsfield) for property photo enhancement; also mentioned in context of Juan's image pipeline
- **n8n** — Scott built a Google Workspace agent using n8n, triggered from Telegram
- **Telegram** — Scott uses it as the interface for his Google Workspace voice/text agent (calendar, email, tasks, contacts, business card scanning)
- **OpenAI Whisper** — Scott uses Whisper for voice-to-text transcription within his Telegram-to-Google-Workspace agent
- **HeyGen** — Mentioned by Scott as one of the tools in his AI avatar video generation pipeline
- **ElevenLabs** — Mentioned by Scott as the voice synthesis component in his video pipeline
- **Pixir (Bastian's project)** — Elixir-based agentic harness providing sub-agents-as-a-service with dramatically reduced memory usage vs. native Codex sub-agents; uses WebSockets and prefix caching
- **T3 Code** — Bastian uses this as a client for his Pixir harness; has a mobile app that shows real-time agent file activity
- **Zed editor** — Mentioned by Bastian as a lightweight editor compatible with his ACP client protocol
- **CodeRabbit** — Mentioned by Scott as the inspiration for his custom security review hook; his system improves on it by triggering on commits/pushes rather than only PRs
- **Canva** — Mentioned in chat by Bastian as an existing service that handles photo album printing/mailing via API, relevant to Juan's monetization discussion
- **Lulu** — Mentioned in chat by David as a drop-ship quality printing API option for Juan's photo album monetization idea
- **Fathom** — Noted in chat log as the AI notetaker present in the meeting
- **Fireflies.ai** — Also present in the meeting as a recording/notetaking bot

## links

- **https://www.evenrealities.com/** — Even Realities smart glasses product page, shared by Brandon Hancock
- **https://www.yesware.com/** — Yesware email tracking tool, shared by Brandon Hancock in context of cold outreach monitoring
- **https://infisical.com/** — Infisical secret management platform, shared by Juan Torres confirming Patrick's reference
- **https://agentops.patchoutech.com/** — Patrick Chouinard's AgentOps documentation site, built and deployed via Claude Code skill
- **https://github.com/hopchouinard/community-brain-distribution** — Patrick's public repo for the community knowledge base / brain distribution project, shared for Paul Miller
- **https://github.com/hopchouinard/RecapFlow-automation** — Patrick's public repo for recap/transcript automation, shared for Paul Miller
- **https://pixir.dev/** — Bastian's Pixir agentic harness project site
- **https://github.com/scott-rippey/video-generator** — Scott's public repo for his AI video generation pipeline (Higgsfield + ElevenLabs + HeyGen)
- **https://github.com/scott-rippey/Telegram-Google-Voice-Agent** — Scott's public repo for the Telegram-to-Google-Workspace n8n agent
- **https://www.youtube.com/@BuildingwithReason** — Patrick Chouinard's YouTube channel
- **https://x.com/wshxnv/status/2067327251335835852** — Tweet shared by Bastian about an OpenAI Hackathon winner who built an MCP connector turning ChatGPT into a Codex interface, enabling GPT-5.5 Pro for planning with Codex execution and doubled rate limits
- **https://x.com/thsottiaux** — Tibo's Twitter/X profile; OpenAI employee who manages the usage reset feature (two resets/day, now lasting a month), shared by Bastian
- **https://app.fireflies.ai/live/01KWA3HCY1864N2MJYQ2J5Q4CS?ref=live_chat** — Fireflies.ai real-time notes link for this session, posted automatically by the bot
- **https://youtube.com/@thekoerneroffice** — Chris Koerner's YouTube channel on offline business ideas (inflatable movie theaters, etc.), shared by Biggi Fraley in context of Juan's photo booth business model
- **https://youtu.be/N__nWSLeiaU** — Example AI roast video, shared by Adam in context of Juan's photo booth interactive roast feature idea

## decisions

- **Brandon Hancock** will send Juan Torres his phone number and connect him with his friends who own a wedding venue to explore a pilot partnership for the AI photo booth.
- **Brandon Hancock** will follow up with Paul Miller around 5:30 PM the next day to continue their discussion.
- **Brandon Hancock** will prepare a pitch deck for the PE firm meeting the following morning after the call.
- **Juan Torres** will record a video of the photo booth in action and send photos/video to Brandon Hancock for the wedding venue introduction.
- **Juan Torres** will build out the voting/roast feature and photo album/printing integration concepts discussed during the call.
- **Patrick Chouinard** will share the AgentOps documentation site link (agentops.patchoutech.com) and GitHub repos with the group.
- **Scott Rippey** will share his video generator GitHub repo and Telegram-Google-Workspace agent repo with the group (completed during the call).
- **Scott Rippey** will share the security review hook system plumbing with Patrick Chouinard so he can integrate similar review capabilities into Hermes.
- **Bastian Venegas Arevalo** will open-source the Pixir agentic harness approximately one week after the call.
- **Brandon Hancock** will explore the Hermes setup more deeply after the call, having already completed initial installation.
- **Ty Wells** will do presentations on his projects in the next couple of weeks.
- **Sri Ram Kavali** (chat) needs to be granted access to the Skool course after purchasing ShipKit — flagged in chat but no explicit owner assigned.