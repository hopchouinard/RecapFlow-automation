## general

This was a recurring group coaching/peer-learning call focused on AI-assisted development, attended by Marc Juretus, Patrick Chouinard, Paul Miller, mdcatc (Morgan), Ryan C, Ty Wells, and Juan Torres. The session opened with banter about exhausted AI token quotas across Claude (Fable/Opus), OpenAI Codex, GPT-5.5 Pro, Gemini CLI, and Perplexity before transitioning into structured project updates from each participant.

Members shared progress on a wide range of independent projects: Morgan's cemetery management application and school carpool logistics app (Class to Curb); Ryan's personal finance Mac OS app, estate agency website and CRM, and a newly purchased Mac Mini for a personal AI assistant; Ty's predictive appliance monitoring system ("Q") using electrical power signatures, a golf tee-time locator PWA, and a cashless POS integration for a Bahamas beach resort client; Juan's AI photo booth image-to-image transformation service with multi-model pipeline and AWS infrastructure monitoring; and Paul's AI-driven data insight layer for his 10-year-old CRM/Salesforce automation company, plus an Android emulator-based demo data generation system.

The most technically dense discussion centered on Patrick's strategy of using Claude's "Fable" (Claude 4/Opus-level) model exclusively for architecture, specification, and code review — never for writing code directly — while delegating implementation to Claude Opus/Sonnet. He described a landmark session where he pointed Fable at 160 repositories, fed it all past Claude Code JSONL session files, and let it autonomously traverse his network (including SSH-ing into his Hermes VM and pulling webhook conversation history) to produce a comprehensive architectural analysis and months-long development roadmap. The group also discussed a multi-model workflow: GPT-5.5 Pro for high-level prompting and PRD generation → Fable for architecture → Opus/Sonnet for coding → Fable for PR review.

The call closed with a discussion of terminal multiplexers (CMUX, Warp), the Omnigent multi-model harness tool, Prometheus/AlertManager for infrastructure monitoring, and business topics including LLC/S-Corp structure for Juan's startup and sales strategy for Morgan's cemetery app.

## insights

- **Patrick's core workflow insight:** Use Fable (high-capability model) exclusively for architecture and spec generation, not code writing. Tell Fable explicitly that the specs are "for Opus" so it adds more detail — the model produces more thorough output when told a lesser model will execute it.
- **Negative/contextual prompting works:** Telling a model it is creating output for a less capable model causes it to add more granular detail, resulting in smoother downstream code execution with fewer rollbacks.
- **Fable's autonomous traversal capability:** When given access to a root directory and past session files, Fable can independently discover network inventory, SSH into connected VMs, read memory/state, connect to webhooks, and synthesize all of it — without being explicitly told those resources exist.
- **Multi-model pipeline for maximum value:** GPT-5.5 Pro (web chat, unlimited on $100/month Pro plan) → Fable for architecture → Opus/Sonnet for implementation → Fable for PR review. Each model is used at its comparative advantage.
- **AI-guided training for AI:** Patrick's Fable session auto-generated a Claude Code training curriculum stored as project files; loading the project and saying "hi" launches an interactive, choose-your-own-path training experience guided by the live model.
- **Fable for install.md generation:** Fable can generate plain-language install scripts (install.md) for each service/connector that Claude Code can then execute autonomously, reducing support burden for configuration tasks.
- **Android emulator automation:** Claude Code can control Android emulators visually (screenshot-based), enabling automated demo data generation and app testing without touching core production systems.
- **Ty's predictive maintenance insight:** Reading electrical power signatures against a manufacturer-spec baseline and a 7-day rolling baseline enables trend-based failure prediction — superior to threshold-only alerting used by most commercial smart-home systems.
- **Use GPT-5.5 Pro web chat as a Fable substitute** when Fable tokens are exhausted; it is not accessible via API at reasonable cost but is effectively unlimited through the web UI on a Pro plan.
- **For sales of government-facing software (Morgan):** Penalties and compliance deadlines are stronger motivators than feature benefits for government buyers; finding a local sales rep who understands the product vision is preferable to the developer doing sales.
- **Ty on LLC/S-Corp:** Use AI to prepare detailed questions and understand the landscape before paying for professional tax/legal advice — then verify AI output with a human accountant.

## qa

**Q (Marc):** It sounds like you're letting Claude and Codex fight each other out for the correct code — can you explain that?
**A (Patrick):** The workflow is to have Fable do all the architecture and spec work, then have Opus execute the code. They're not fighting exactly — Fable architects, Opus implements, and Fable reviews the PR. Each model does what it's best at.

**Q (Paul):** Where do people who run cemeteries share information with peers — could AI do deep research to find the hot buttons that would motivate them to act?
**A (Morgan/mdcatc):** That's a good idea, but the core problem is government accountability — nobody claims responsibility. The real trigger may be financial penalties when they can't fulfill burial requests, which would force budget prioritization.

**Q (Juan):** Is it possible to attend city council meetings to pitch the cemetery app directly?
**A (Morgan/mdcatc):** The target city is in a different state, so attending in person isn't currently feasible. That's why he's looking for a local sales representative who can attend on his behalf.

**Q (Patrick):** Juan, what are you using for monitoring and alerting at the infrastructure level?
**A (Juan):** CloudWatch for the EC2 instance, but not yet for the physical mini PCs at the photo booth.
**A (Patrick, follow-up):** Prometheus and Alert Manager — Prometheus is the monitoring platform, Alert Manager is an add-on that can publish alerts to webhooks, N8N, Discord, or any channel.

**Q (Juan):** Is there an OpenRouter tool that coordinates work between multiple models in a pipeline?
**A (Patrick):** The OpenRouter fusion approach amplifies one model using others internally — it's one question in, one answer out. It doesn't support splitting work across models where each does a separate stage. For that, Patrick uses GitHub as the handoff mechanism, treating each model as an independent team member.

**Q (Ty):** What's the difference between Fable's capability and a standard model — why does it solve things others can't?
**A (Ty, self-answered with group agreement):** Fable's key differentiator is its "harness" — it doesn't stop at the first or second failure. It keeps iterating until it finds a solution, which is why it excels at cybersecurity, debugging, and architecture problems that other models give up on.

**Q (Paul):** Could the AI-guided training Patrick built be a way to onboard non-technical people into AI workflows quickly?
**A (Patrick):** Yes — because you're talking to a live model, it adapts the training in real time based on what the learner shares about their own context, making it a genuinely personalized learning experience.

## tools

- **Claude / Fable (Anthropic)** — Primary high-capability model used for architecture, spec generation, code review, and deep analysis across all participants' projects
- **Claude Opus / Sonnet** — Used for code implementation after Fable produces architecture specs
- **OpenAI Codex** — Patrick's secondary coding environment; also token-exhausted
- **GPT-5.5 Pro (OpenAI)** — Used via web chat (unlimited on $100/month Pro plan) to generate PRDs and prompts for Fable when Fable tokens are low
- **Gemini CLI** — Patrick's fallback when all other token budgets are exhausted; described as "desperate times"
- **Perplexity** — Mentioned as an additional token reserve
- **GitHub Copilot** — Mentioned as another token reserve
- **Ollama (local models)** — Jokingly cited as the final fallback indicating true token desperation
- **N8N** — Mentioned as a webhook/automation target for Prometheus Alert Manager; also referenced in Scott's chat link for Google Voice agent
- **Prometheus** — Recommended by Patrick for infrastructure monitoring of Juan's physical photo booth hardware
- **Alert Manager** — Prometheus add-on for publishing alerts to Discord, webhooks, N8N, etc.
- **CloudWatch (AWS)** — Juan's current monitoring tool for EC2 instances
- **Aurora Serverless 2 (AWS)** — Juan's database for the photo booth application
- **LanceDB** — Referenced by Paul as part of Patrick's data architecture pattern (deterministic base layer for AI data analysis)
- **Databricks / Snowflake** — Internal data services Patrick is connecting to Claude Code at his workplace
- **Wavespeed** — Juan uses the desktop version to test image transformation styles before deploying to his photo booth app
- **Hermes** — Patrick's personal AI assistant/agent system running on a Linux VM; accessed autonomously by Fable during the repo analysis session
- **Claude Code** — Anthropic's coding harness; used by Patrick for development and training delivery
- **Linga POS** — Point-of-sale software Ty resells; client wants cashless integration for a Bahamas beach resort
- **CMUX** — Terminal multiplexer Ty is using and forking to fix OAuth and microphone issues
- **Warp** — Terminal application Patrick switched to from CMUX
- **Omnigent (omnigent.ai)** — Multi-model harness/orchestration tool shared by Ty; described as a chat interface for switching between models, with some memory/crash issues
- **OpenRouter** — Discussed as a fusion-model approach (multiple models improving one answer), not a pipeline orchestrator
- **Mac Mini** — Ryan purchased one to run a local AI personal assistant (same setup as Patrick's Hermes and Scott's phone-calling agent)
- **Fathom** — Meeting notetaker bot present in the call
- **Android Emulator** — Paul used Claude Code to control multiple Android emulators as virtual users to generate demo data for his CRM app
- **Microsoft Copilot Studio** — Marc is working in "Copilot Studio hell" building an agent with adaptive cards and topic flows
- **PHP** — Morgan's original Class to Curb carpool system was built in PHP ~15 years ago

## links

- `https://github.com/scott-rippey/Telegram-Google-Voice-Agent` — Scott Rippey's repo: running a Google Voice agent in N8N from Telegram
- `https://prometheus.io/` — Prometheus monitoring platform, shared by Juan after Patrick's recommendation
- `https://github.com/omnigent-ai/omnigent.git` — Omnigent multi-model harness GitHub repo, shared by Ty
- `https://fathom.video/customize` — Fathom notetaker settings page (auto-posted by Fathom bot)

## decisions

- **Patrick** will dig out his 3-page Fable repo-analysis prompt from his conversation history, clean it up minimally, and post it to the group forum.
- **Ryan** will re-send the demo video (previously sent to Paul) to the top of Paul's inbox so Paul can share it with a New Zealand contact who has 400 stores.
- **Paul** will follow up with Ryan if he cannot locate the video in his inbox.
- **Morgan (mdcatc)** will deploy the Class to Curb application from staging to production as his next step, then notify Paul so Paul can introduce it to Australian private schools.
- **Morgan** will look for a local sales representative in the target state to attend city council meetings and pitch the cemetery application.
- **Juan** will investigate Prometheus and Alert Manager for monitoring the physical mini PCs in his photo booth setup.
- **Ty** will give Fable the task of building an automated account-switching pipeline (GPT-5.5 Pro → Fable → Opus → Fable PR review) to manage token usage across multiple accounts.
- **Ty** will investigate and potentially fix the Omnigent memory/crash issues using Fable, and share findings with the group.
- **Patrick** will investigate Omnigent after the call.
- **Ryan** will set up his new Mac Mini (now desk-mounted) with the same Hermes-style personal AI assistant configuration used by Patrick and Scott, including phone-call and appointment-booking capabilities.