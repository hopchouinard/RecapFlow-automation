## general

This extended five-part session functioned as an open coaching/mastermind call where builders shared parallel work on agentic infrastructure, go-to-market execution, and personal-brand/career strategy. A recurring throughline was "agentic OS" architecture: Patrick Chouinard walked through his home-lab setup (T3 code, Hermes chief-of-staff agent, InfraKnowledge knowledge graph, AgentOps, and a Prometheus/Grafana/Loki observability stack), which sparked a friendly debate with Shakur and Ty Wells over whether a graphical dashboard is necessary or whether a simpler JSON file/email-digest/mental model suffices — the consensus landing on "it depends on scale and how often you touch the system." Scott Rippey later extended this theme with his own custom-built Mac IDE ("Blackbox") featuring a 3D database visualizer, an agentic browser, and an iOS companion app, all built by prompting Claude/Fathom Design rather than hand-coding UI.

A second major thread was go-to-market and fundraising mechanics for member businesses. Juan Torres received detailed, iterative coaching from Brandon Hancock on building ICP databases (via Grok, SerpAPI, and manual judgment loops), running cold email through Instantly with burner domains, and choosing between VC funding (TinySeed, YC, Clerky/Delaware C-Corp setup) versus a self-funded deposit/referral model for his hardware product. Scott Rippey introduced a new HYROX-training SaaS partnership (builder + coach + athlete-influencer, profit-split three ways), and Daniel Zivkovic pitched his EMS/EPCR documentation startup, seeking a distribution partner. Paul Miller described his pivot from bootstrapped founder to VC-backed AI dev-studio model, showcasing an agentic reporting stack (LanceDB + DuckDB + Cerebras + RunPod) built on 11 years of sales data.

Throughout, Brandon Hancock repeatedly emphasized experimentation discipline: build evaluation sets before choosing agent architecture, log every experiment to survive context compaction, use cheap Chinese/flash models for scale and premium models only where necessary, and treat rapidly falling model costs as a strategic "reset button" for margins (illustrated by EMS Soap's cost curve and Patrick's RecapFlow dropping from $1.50 to $0.15/call on GLM 5.3 Flash). Career and content strategy closed out the call: Brandon advised Varun Sharma to stop chasing vendor-specific positioning and instead build a public "challenge video" case study (modeled on a viral AWS scalability video) to demonstrate skill at scale, tying into his own YouTube outlier-analysis strategy (vidIQ) and his evolving Shipkit task-template SDLC methodology (plan → task template → adversarial "poke holes" review → execute → review, each stage its own skill). The call ended with informal chat-log exchanges on model/tool recommendations, a live demo of Juan's promo video, and a cautionary link from Daniel Zivkovic about Delaware C-Corp incorporation risk.

## insights

- **Patrick Chouinard**: Runs almost all coding through T3 code, aggregating Claude Code/Codex sessions per project across remote Proxmox VMs, with a custom dashboard fed by a "skill" that reads every commit/PR merge to track ~35 packages across 7 underlying projects.
- **Patrick Chouinard**: Structures Hermes as a multi-profile system — a default "chief of staff" delegates to specialized sub-agents (researcher, operator, coder) that each carry only the tools/knowledge needed, keeping the main agent's context light.
- **Patrick Chouinard**: "InfraKnowledge" is a markdown-only project describing infra inventory, roles, and dependencies, compiled into a knowledge graph to sequence and parallelize work.
- **Brandon Hancock**: Enterprise sales cycles run ~5 months; line up committed customers *before* finishing compliance work (SOC 2/HIPAA), not after — a lesson from EMS Soap.
- **Brandon Hancock**: Switching a classification task to DeepSeek v4 Flash cut cost 100x ($350→$3) at equivalent quality, illustrating rapid AI cost deflation as a strategic lever.
- **Shakur**: Deliberately skipped a graphical dashboard for his own agent OS, using a JSON file + daily email digest instead — prioritizing simplicity.
- **Patrick Chouinard**: Argues a dashboard becomes necessary once you have many parallel tools/CLIs/MCPs and limited daily engagement, to avoid silently rebuilding the same functionality twice.
- **Patrick Chouinard**: Proposes a dedicated Pydantic AI-based review/red-team harness rather than reusing the coding model to review itself — a distinct "debugging specialist."
- **Brandon Hancock**: For multi-capability agents, don't guess architecture — generate ~100 adversarial synthetic conversations (bucketed by user type) to build an eval set before choosing single-agent vs. orchestrator+sub-agents.
- **Brandon Hancock**: "Loop engineering" = run the plan→critique→execute→review loop manually with AI 2-3 times to align, log every experiment to a markdown journal (survives context compaction), then let it run autonomously overnight (real cost: ~$400 in one run).
- **Brandon Hancock**: Use cheap Chinese/flash models (Gemini 3.6, GLM) for large-scale experimentation/classification; use GPT-5.5 (no-thinking) for fast, American, production-facing responses; Claude/Opus on AWS Bedrock is throttled and support is painful at scale.
- **Brandon Hancock**: Terminology distinction — an LLM with tool calls is not an "agent"; a true agent reasons and acts autonomously in an unsupervised loop.
- **Juan Torres**: Proposes a lightweight Flask/Docker observability web app logging each agent's row-by-row input/output for non-deterministic pipelines, with an optional debug mode surfacing unused reasoning tokens.
- **Paul Miller**: Enterprise AI dev costs haven't dropped like consumer/prototype costs — heavy onboarding and edge cases remain the moat, reshaping how VCs think about defensibility ("can this be cloned over a weekend?").
- **Brandon Hancock**: To build an ICP database, use Grok to find 10-20 leads per city, manually apply judgment 3-5 times per city to train the tool, then codify a "rulebook" (Apify, scraping sub-agents) to scale.
- **Brandon Hancock**: Never use a primary domain for cold outreach — use burner domains (2-week warmup via Instantly); keep copy to one screen with exactly one CTA.
- **Brandon Hancock**: Capital becomes the bottleneck within 4-6 months for hardware-scaling businesses since manufacturing cost (not CAC) constrains growth; apply early to TinySeed/YC. A Delaware C-Corp (via Clerky, ~$800-1000) is essentially mandatory for VC funding.
- **Brandon Hancock**: Alternative to VC: pre-order/deposit model (first 100 customers pay unit cost to "jump the line") plus referral incentives (20-30% profit share for 6 months) to self-fund growth.
- **Brandon Hancock**: Always ask "if this goes perfectly, what does it look like at the limit?" before committing to a revenue split or partnership structure.
- **Scott Rippey**: The ideal startup trifecta is builder + domain expert + distribution/audience partner; visualizing a DB schema as an interactive 3D model (via Claude→Fathom Design) beats reading schema text.
- **Scott Rippey**: Turn on point-in-time recovery before real customers hit a Supabase DB; keep dev/staging/prod mirrored with a manual promotion pipeline.
- **Daniel Zivkovic**: Domain expertise in unsexy, bureaucratic industries (EMS/healthcare documentation) is a strong wedge because incumbent software quality is poor.
- **Brandon Hancock**: Before building an offer, validate the actual ROI (target 10x); no response to cold outreach is itself feedback — isolate whether it's the email, volume, or offer.
- **Brandon Hancock**: For long-running autonomous work, break goals into "gates" with self-determined success criteria; the agent loops plan→critique→act→review within each gate before advancing, preventing premature "I'm done" claims.
- **Varun Sharma**: "The money is in the follow-up" — expect 4-5 follow-ups per lead; seed AI outreach prompts with voice-transcribed, personal examples to avoid robotic tone.
- **Brandon Hancock**: A/B test subject lines first to isolate open-rate issues, then test 20+ copy variants to isolate reply-rate issues.
- **Brandon Hancock**: For career positioning, a single well-executed public technical case study (~2hr video, 800K views) can outweigh thousands of job applications; frames his own content around AI/code/business overlap ("profitable AI developer").
- **Brandon Hancock**: Uses vidIQ "outlier" analysis to detect overperforming video formats and intentionally repurposes them rather than inventing from scratch ("imitate before innovate").
- **Brandon Hancock**: Current Shipkit SDLC pipeline — Claude plan mode → task-template skill → adversarial "poke holes" review skill → execution → completion-review skill — every stage its own skill with a persistent artifact.
- **Daniel Zivkovic (chat)**: Harvey (legal AI tool) runs a customized Kimi K3, suggesting Chinese models are moving into more "secure" inference environments — it's about the inference provider, not just the model.

## qa

**Q (Brandon Hancock):** How many parallel projects does your dashboard track?
**A (Patrick Chouinard):** 35 packages across 7 underlying projects, including Hermes.

**Q (Elijah Stambaugh):** Is your "knowledge spine" just Hermes stripped down, and is it markdown or a database?
**A (Patrick Chouinard):** No — Hermes is multi-profile; the knowledge spine is a separate project (InfraKnowledge) made entirely of markdown files, loaded into a knowledge graph to sequence work.

**Q (Juan Torres):** Are logs/observability visible via artifacts from each agent in the pipeline?
**A (Patrick Chouinard):** Yes — a full Prometheus/Grafana/Loki stack, fed by every application and exposed to AgentOps, runs on just a few mini PCs.

**Q (Shakur):** What's the actual benefit of a big dashboard versus a simple JSON file + email digest?
**A (Patrick Chouinard):** For simple email/meeting management a simple approach suffices, but with many parallel tools/CLIs/MCPs and limited daily engagement, visualization prevents silently rebuilding the same functionality twice.

**Q (Hemal Shah):** Orchestrator+sub-agents or planner/executor for a multi-capability e-commerce co-pilot?
**A (Brandon Hancock):** Don't decide upfront — build a 100-conversation adversarial eval set, start with the simplest architecture, and iterate toward complexity based on measured failure rates.

**Q (Hemal Shah):** Model recommendations if I want American models instead of Chinese?
**A (Brandon Hancock):** Use a strong thinking model overnight for research; for production, use GPT-5.5 (no-thinking) if it must be American, or Gemini 3.6/Flash if cost/speed matters more.

**Q (Brandon Hancock):** Is DuckDB a vector store, and are you running two vector stores?
**A (Paul Miller):** No — DuckDB is a file-based columnar query layer on top of LanceDB, which handles vector/word content.

**Q (Juan Torres):** What's the methodology to carry out an ICP outreach campaign?
**A (Brandon Hancock):** Use Grok to find 10-20 ICPs per city, apply manual judgment 3-5 times per city, codify a rulebook, then scale via Instantly with burner domains.

**Q (Juan Torres):** Why pursue VC funding if they don't take shareholding here?
**A (Paul Miller):** The VC prep process (TAM, differentiation, cost structure) is valuable even outside direct investment, e.g., for negotiating with manufacturing partners.

**Q (Brandon Hancock, to Scott):** If the HYROX app goes perfectly, what does it look like at the limit?
**A (Scott Rippey):** ~1,000 users = ~$40k/month (~$500k/yr); profits split evenly three ways after costs, between Scott, Joe, and Alyssa.

**Q (Scott Rippey):** Are you using Supabase — what's your setup?
**A (Brandon Hancock/Scott Rippey):** Yes — turn on point-in-time recovery before going live, and keep separate dev/staging/prod environments.

**Q (Brandon Hancock, re: Google review auto-reply offer):** What's the actual financial impact of answering every Google review?
**A (Shakur):** Honestly unsure — hadn't validated the ROI before building the offer.

**Q (Brandon Hancock):** How do I get "loop deep work" (gated autonomous looping) working instead of my agent saying "I'm done" prematurely?
**A (Brandon Hancock, self-answer):** Break goals into gates with self-determined success/failure criteria; loop plan-critique-act-review within each gate, and feed back corrections when it falsely claims completion.

**Q (Varun Sharma):** For the review step, do you use a different model, or is it adversarial?
**A (Shakur):** Currently the same model with a dedicated review prompt for simplicity; long-term plan is a different model (e.g., Claude calling Codex) for adversarial review.

**Q (Varun Sharma):** I've positioned around the Google/Gemini stack, but Google lags frontier labs — should I pivot?
**A (Brandon Hancock):** Stack positioning still works, but the real leverage is public proof of skill — do a scalable technical "challenge" video modeled on a viral AWS case study.

**Q (Varun Sharma):** Is there a way to get deep self-reflection within a single prompt like Shipkit's task templates?
**A (Brandon Hancock):** No — every SDLC step (plan, task template, adversarial review, execution, completion review) is its own dedicated skill/prompt, not combined into one.

## tools

- **T3 code** – harness aggregating Claude Code/Codex sessions by project, run remotely via VM.
- **Hermes** – Patrick's multi-profile "chief of staff" agent framework.
- **CMUX / Cursor** – prior IDE tools; Cursor canceled after SpaceX acquisition.
- **Grok / GrokBot (4.6)** – used for ICP research, lead-list building, LinkedIn data pulls.
- **Instantly (instantly.ai)** – cold outreach platform; requires burner domains, ~2-week warmup.
- **listio.ai / Listio** – Brandon's YouTube lead-magnet SaaS side project.
- **GLM 5.3 / 5.3 Flash** – low-cost model; cut Patrick's RecapFlow cost from $1.50 to $0.15/call; also cited for EMS Soap cost reset.
- **DeepSeek v4 Flash** – 100x cost reduction for classification tasks.
- **Luna model (Google)** – considered, then replaced by DeepSeek.
- **OpenRouter** – alternative inference provider; compliance/HIPAA constraints discussed (AWS Bedrock raised as HIPAA-compliant alternative for Chinese models).
- **Kimi K (K3)** – Chinese model; noted as basis for Harvey's legal AI via a secure inference provider.
- **ShipKit / Shipkit.ai** – Brandon's task-template/skill-based SDLC workflow system.
- **Prometheus, Grafana, Loki** – observability stack in Patrick's home lab.
- **AgentOps** – CLI/MCP exposing infra to the agent framework.
- **InfraKnowledge** – markdown-based infra knowledge graph project.
- **Proxmox** – VM virtualization backend.
- **Pydantic AI** – open-source framework Patrick plans to customize for review/red-teaming.
- **ACP (Agent Client Protocol)** – Bastian has a working PR for T3 code integration; offered to share repo with Patrick.
- **LanceDB** – vector/word-content DB (Paul Miller's reporting stack; also used by Daniel Zivkovic).
- **DuckDB** – columnar query layer atop LanceDB ("intelligence layer"); Daniel shared his own implementation via GitHub.
- **Cerebras** – fast-hosted inference for real-time chat front end (link: cerebras.ai/infcamp).
- **RunPod** – GPU hosting for backend model processing.
- **Postgres** – master data store feeding Paul's stack.
- **GPT-5.5 (no-thinking)** – fast, affordable American production model.
- **Gemini 3.6 / 3.6 Flash / 3.7 Flash** – used for classification/quick tasks; 3.7 Flash praised in chat.
- **Claude / Opus (AWS Bedrock)** – criticized for rate limits/throttling.
- **DaVinci Resolve** – used by Juan Torres to edit his promo video.
- **Flask / Docker** – proposed for an observability/test web app.
- **EMSO** – Brandon's expert-judgment-extraction project (moat example).
- **TryAIBooth / AIBooth** – burner-domain service for outreach.
- **Vercel** – fast landing-page deployment.
- **Calendly** – single CTA link on outreach/landing pages.
- **SerpAPI (serpapi.com)** – pulls Google Places data for lead lists (cheaper than Google API keys).
- **Clerky** – Delaware C-Corp/cap-table setup service (~$800-1000).
- **TinySeed** – pre-seed accelerator (batch opens Sept 1-9).
- **Y Combinator (YC)** – alternative funding, more capital, later disbursement.
- **Fable** – multi-model orchestration (Opus, Sonnet 5.5, Sol) with global rules, used by Scott Rippey.
- **Supabase** – DB backend; point-in-time recovery and dev/staging/prod separation discussed.
- **Fathom Design** – used with Claude to generate 3D DB visualization.
- **Blackbox** – Scott Rippey's custom Mac IDE/agent harness (agentic browser, iOS simulator, SQLite usage tracking); GitHub repo shared (cc-blackbox-app).
- **TestFlight** – testing Scott's companion iOS app.
- **Cloudflare** – secure sync between IDE and iOS app.
- **CC Usage (ccusage)** – tracks daily token usage across Claude/Codex/Grok; GitHub link shared.
- **PureMail** – cheap email service for Shakur's cold-outreach tool.
- **vidIQ** – YouTube outlier/viral-format analysis plugin (Chrome extension link shared).
- **Google ADK / Gemini API / Google Cloud** – referenced re: Varun's technical stack positioning.
- **Fireflies.ai / Fathom / Sembly** – meeting notetaker bots present in the call.
- **poteto's "unslop" skill** / **matt's "/wait-what"** – Claude/Cursor plugin skills shared in chat for cleaning up Opus responses.

## links

- https://www.youtube.com/@AndrejKarpathy — Patrick's daily-follow recommendation.
- https://www.youtube.com/@NateBJones — Patrick's daily-follow recommendation.
- https://www.zalak-patel.com/ — portfolio website example shared by Ryan C.
- https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md — "unslop" skill for cleaning Opus responses (Morgan).
- https://www.anthropic.com/engineering/building-effective-agents — Anthropic's "start simple" agent guidance (Daniel Zivkovic, for Hemal Shah).
- https://www.cerebras.ai/infcamp — Cerebras inference platform link (Brandon Hancock).
- https://github.com/dzivkovi/video-intel/blob/.../intelligence-layer.md — Daniel Zivkovic's DuckDB-as-intelligence-layer implementation.
- https://youtu.be/c9WCcD4fH6c — video shared by Brandon Hancock during Juan Torres's segment.
- https://serpapi.com/ — Google Places data tool for ICP research (Paul Miller).
- https://www.youtube.com/@InstantlyAI/videos — Instantly's YouTube channel, cited as cold-outreach "bible."
- https://apply.tinyseed.com/ — TinySeed application link (Brandon Hancock).
- https://www.clerky.com/welcome — Clerky C-Corp setup link (Brandon Hancock).
- https://youtu.be/7VKliOQXQ9M — Y Combinator/Lean Startup author video warning against Delaware C-Corps (Daniel Zivkovic).
- https://www.instagram.com/alyssamcelheny/ — HYROX athlete/marketing partner reference (Brandon Hancock).
- https://github.com/ccusage/ccusage — CC Usage token-tracking tool (Varun Sharma).
- https://github.com/scott-rippey/cc-blackbox-app — Scott Rippey's Blackbox IDE repo.
- https://chromewebstore.google.com/detail/vidiq-vision-for-youtube/... — vidIQ Chrome extension (Daniel Zivkovic).
- https://www.shipkit.ai/ — Brandon Hancock's Shipkit product.
- https://lnkd.in/p/g8e5p6cH — Ty Wells's LinkedIn article/presentation (posted twice).
- https://www.youtube.com/@Itssssss_Jack — YouTube channel with Claude Design videos (Daniel Zivkovic/Brandon Hancock).
- https://youtu.be/W4EwfEU8CGA — AWS scalability "challenge video" case study referenced as the model for public technical proof-of-skill content (Brandon Hancock).

## decisions

- **Patrick Chouinard** to build a new T3 code server modeled on his home-lab infra (Proxmox VMs + thin Mac client) and demo his Grafana-based observability app to Juan Torres once production-ready.
- **Shakur** to set up additional Linux laptops linked into T3 code as separate machines; Patrick to share progress with Shakur.
- **Brandon Hancock and Patrick Chouinard** to hold a follow-up call to discuss the Pydantic-based review/red-teaming harness idea.
- **Brandon Hancock** committed to a 13-day deadline to launch v1 of listio.ai, then a one-week wait to gauge Instantly campaign traffic before further development.
- **Bastian Venegas Arevalo** to invite Patrick Chouinard to a GitHub repo containing his ACP integration PR for T3 code.
- **Hemal Shah** to build a 100+ conversation adversarial eval set before finalizing his co-pilot's architecture, and report results back in the community.
- **Juan Torres** to send Brandon the AI Boots Studio promo video, purchase 3-5 burner domains and begin email warmup, build ICP-specific contact lists (~1,000 per ICP), set up Instantly, build a landing page (Claude + Vercel + Calendly), pursue TinySeed/YC applications, set up a Delaware C-Corp via Clerky, and consider a referral/deposit pre-funding model.
- **Paul Miller** to keep the group posted on his upcoming product launch and new VC-backed dev-studio arrangement.
- **Scott Rippey and partners (Joe, Alyssa)** to finalize a formal partnership agreement for the HYROX SaaS product ("Acceler8 Training") before/during a 2-3 week build trip in Michigan.
- **Scott Rippey** to release his GitHub repo/library for the 3D DB visualization tool and Blackbox IDE, ship the companion iOS app after TestFlight testing, and keep both free for the community.
- **Shakur** to reclaim manual control of send limits on his Google-review-reply tool, lower its price, and add a user-facing dashboard.
- **Daniel Zivkovic and co-founder Raul** to continue pursuing a distribution partnership for their EMS documentation product.
- **Varun Sharma** to revamp the AI cold-outreach experiment (follow-up cadence, tone) and produce a first "challenge video" within ~3 weeks per Brandon's advice.
- **Patrick Chouinard and Daniel Zivkovic** to schedule a Thursday-afternoon call, with Daniel to watch the YC Delaware incorporation-risk video first.