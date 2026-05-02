## general

This was a group coaching/community call for a cohort of AI-assisted developers and entrepreneurs, hosted by Brandon Hancock (returning from a trip to Japan) with Patrick Chouinard having held down the fort in his absence. The session followed a round-robin format where each participant shared updates on their current projects, tools, and learnings.

Topics ranged from AI coding tool preferences (Claude Code, Cursor, Codex CLI, WindSurf) and model selection strategies, to live project demos including a parking management app, a tourism discount pass app, an AI-powered prompt library called Prompt Weaver, a software cloning tool, an AI police body cam video automation pipeline, and a social media management platform. Brandon also shared broader strategic thinking about building software that is tightly coupled to monetary outcomes as a business model heuristic.

Patrick demonstrated his "Prompt Weaver" project and a set of ShipKit skills he built to automate the implementation loop, including dependency analysis, confidence checks, and task memory backfilling. Brandon shared lessons on model selection for production applications, specifically praising Gemini 2.0 Flash with low thinking as a cost-effective alternative to GPT-4.1 for instruction-following tasks in live apps.

The call also touched on local model development using Go and the Wails framework as an alternative to Electron and Python for distributing desktop apps, the use of LLM Guard for local PII redaction, Doppler for API key management, and Trigger.dev for long-running background jobs. Brandon closed with advice on pricing client work, avoiding equity-for-work arrangements, and the importance of task-based development for maintaining context across large codebases.

---

## insights

- **Build software closest to the money**: Brandon's rule of thumb — if turning off your service causes someone to lose money, you have a sticky, high-value product. Standardized, repeatable workflows with a monetary outcome at the end are the best targets.
- **Use different models for development vs. production**: Claude/Opus is great for coding; Gemini 2.0 Flash (low thinking) is cheaper and nearly as good for production instruction-following tasks in live apps.
- **Claude Code's UltraThink command**: Typing `UltraThink` in Claude Code triggers extended reasoning before implementation — useful as a final confidence check before executing complex tasks.
- **Task-based development beats plan-based development**: Named task files with checkboxes and decision logs make it trivial to resume work after context resets, crashes, or compaction events. Plans in Cursor/Claude Code are hard to find and don't capture enough context.
- **Separate "thinker" and "doer" sessions for large codebases**: Create the task in one session (with UltraThink), implement in a second session. This prevents the model from burning context on planning during implementation.
- **Branching and dev/prod environments are a major anxiety reducer**: Scott noted that finally setting up proper GitHub branching with separate Supabase instances and Stripe test mode dramatically reduced the risk of breaking production.
- **Go + Wails is a strong alternative to Electron + Python for local desktop apps**: Go compiles to a single cross-platform executable, LLMs reason about it well due to its explicitness, and it handles local file system access more cleanly than Electron. (Andrew Nanton)
- **Replicate makes running custom ML models very cheap**: Face tracking/diarization models run for ~$0.03 per clip. (Mitch)
- **Don't sell yourself short as a vibe coder**: Brandon's advice — frame your offer around delivering results, not disclosing your toolchain. Clients care about outcomes, not how you achieved them.
- **Never do work for equity promises**: Brandon strongly advised getting paid upfront for development work; equity-for-work arrangements almost always result in not getting paid.
- **Local models calling cloud models as tools via MCP**: Patrick is experimenting with a small local model that uses larger cloud models (GPT, Gemini, Claude) as function calls for tasks beyond its capability — useful for privacy-sensitive applications.
- **Trigger.dev is best for tasks over one minute or multi-step workflows with retry risk**: For sub-minute, linear AI pipelines, it may be overkill. (Brandon)
- **Doppler solves the API key management problem across multiple projects and machines**: Free for solo developers, supports branching environments with different keys. (Morgan)
- **Posting task documents as working memory**: Patrick's approach of backfilling every decision and rationale into the task document means any session can be resumed by anyone with full context.

---

## qa

**Q (Marc Juretus):** Do you find yourself using Hugging Face models in development, or are you mostly writing code to accomplish what you want?
**A (Brandon Hancock):** I haven't used Hugging Face models myself. The only custom model I use is DeepGram's medical model for speech-to-text, which understands medical acronyms and terminology without autocorrecting them.

**Q (Marc Juretus):** Why use Opus over Sonnet in Claude Code?
**A (Brandon Hancock):** I default to Opus because it gets to answers faster and handles longer, more complex tasks. It doesn't cost that much more within Claude Code's pricing structure.

**Q (Brandon Hancock):** Has Codex CLI gotten faster in your experience compared to when GPT models felt slow?
**A (Andrew Nanton):** It's been pretty fast for me, but since tasks run for 10+ minutes anyway, an extra 10 seconds isn't noticeable. I'm also less sensitive to latency because I split attention across multiple things while it runs.

**Q (Brandon Hancock):** Why use Wails/Go instead of Electron for your local desktop app?
**A (Andrew Nanton):** I needed clean, rapid access to the local file system. Electron requires jumping through hoops for that, and distributing Python cross-platform is a nightmare. Go compiles to a single executable for every platform, and LLMs write it well because it's explicit and backward-compatible.

**Q (Elijah):** If I build software for a client using ShipKit, what do I need to do to deliver it to them? And can I sell things I build with ShipKit?
**A (Brandon Hancock):** Yes, you can sell what you build. The only rule is to add the AI docs to the .gitignore so they're not in the client's repo. For delivery, same thing — just keep the AI docs out. And don't undersell yourself; frame it as delivering a result, not disclosing that you're a vibe coder.

**Q (Brandon Hancock):** What is Trigger.dev actually best used for?
**A (Brandon Hancock):** Long-running background jobs (anything over a minute) and sequential multi-step workflows where you want retry logic and queuing. For sub-minute, linear AI pipelines where you'd rather just tell the user to try again on failure, it's overkill.

**Q (Brandon Hancock):** Why not just focus on scaling the social media app to beyond 30K/month instead of starting new projects?
**A (Ryan):** Partly ADHD — hard to focus on one thing. The screen project came up organically when a competitor tried to sell the solution to one of his existing clients, and he realized he could do it cheaper. The social media app is the primary focus; other projects are opportunistic.

---

## tools

- **Claude Code** — Primary AI coding agent used by Brandon and others; supports parallel tasks, background jobs, plan mode, and UltraThink for extended reasoning
- **Claude Desktop** — Used by Scott as a daily AI assistant companion alongside Claude Code
- **Cursor** — AI-powered IDE used by Marc and others; $20/month plan; supports Claude models
- **GitHub Copilot** — Marc uses the $10/month plan as a secondary coding assistant
- **Codex CLI** — OpenAI's CLI coding agent; Andrew finds it catches environment details (e.g., mise en place) that Claude sometimes misses
- **WindSurf** — IDE used by Morgan; ~$15–20/month; recently added token usage display; offers some models (GPT-4.1) free
- **Warp** — Terminal/IDE Morgan mentioned as an alternative to WindSurf for testing
- **Supabase** — Database backend used across multiple projects; Ty spins up a new instance per cloned app
- **Netlify** — Used by Scott for hosting and managing environment variables across dev/prod branches
- **Stripe** — Payment processing used in Scott's parking app; test mode used for development
- **Twilio** — SMS/text alert service integrated into Scott's parking app; awaiting campaign approval
- **DeepGram** — Speech-to-text with a custom medical model used in Brandon's EMS SOAP report startup
- **Trigger.dev** — Background job orchestration platform for long-running and multi-step workflows
- **PostHog** — Product analytics platform; Brandon recommended it for tracking QR scan locations and user lifecycle in Scott's tourism app
- **Replicate** — Platform for running custom ML models via API; Mitch uses it for face tracking/diarization at ~$0.03/clip
- **ElevenLabs** — Used by Mitch for transcription (low error rate, fast speed) in his video pipeline
- **Sora** — AI video generation tool used by Mitch to generate video clips
- **Hugging Face** — Model hub; Andrew uses narrow models from it for OCR, layout, embeddings, and PII detection
- **LLM Guard** — Local PII/PHI redaction library using small Hugging Face models; Andrew has a working repo setup
- **Wails** — Go framework for building cross-platform desktop apps with a web frontend (v3 in alpha); alternative to Electron
- **Go (Golang)** — Language Andrew is using for local desktop app development; compiles to single cross-platform executable
- **Doppler** — API key/secrets manager; free for solo devs; supports multiple environments and team sharing (Morgan)
- **Phi-4 (Microsoft)** — Local model Tom used as an AI judge to evaluate other local models on real-world tasks
- **Nano Banana** — AI image generation tool Ryan uses for retail screen content; handles text well
- **Ponder** — Early-stage AI video editing tool Ryan alpha-tested; allows chat-based editing instructions
- **Gemini 2.0 Flash** — Brandon is testing this as a production model replacement for GPT-4.1; cheaper, nearly same quality with low thinking mode
- **GPT-4.1** — Brandon's previous go-to production model for instruction following; 1M token context window
- **Playwright** — Browser automation; Tom used it to scrape Nike's infinite scroll page after Claude Web solved it where Claude Code in Cursor could not
- **ShipKit** — Brandon's project framework/template system used by the community to build and ship apps

---

## links

- **Firephoto app** (Ty Wells) — Ty dropped a link in chat to his fire photo project; URL not captured in transcript
- **Wails framework** — Andrew mentioned W-A-I-L-S; Go-based desktop app framework; no URL captured but described as findable
- **Patrick's ShipKit skills** — Patrick mentioned he posted his implementation loop skills to the community repo; no URL captured
- **Tom's Medium post** — Tom wrote a post about using Phi-4 as an AI judge for local models on real-world questions; URL not captured but described as on Medium
- **Mitch's Replicate model link** — Mitch shared a link in chat to the face tracking/diarization model on Replicate; URL not captured in transcript

---

## decisions

- **Scott Rippey** will connect with Bastian offline about lessons learned from building a parking app
- **Scott Rippey** will attend the 10 a.m. ShipKit call the next day to discuss PostHog analytics integration for the Baja tourism app
- **Patrick Chouinard** will attend the ShipKit call the next day to share his Prompt Weaver and skills work
- **Elijah** will try to attend the next day's ShipKit call to discuss pricing and planning for his client project
- **Andrew Nanton** will send Brandon a link to his LLM Guard repo setup for local PII redaction
- **Brandon Hancock** will add `UltraThink` as a manual confidence-check step before implementation in his workflow (already doing manually; Patrick has it in a skill)
- **Ty Wells** will consider documenting his billion-dollar company journey publicly on X with a progress bar
- **Mitch** is planning to go all-in on his AI video business around February–March, potentially leaving his day job after a planned vacation
- **Ryan** will complete the comment-response generation feature for his social media app that evening and onboard his first client in the first week of January