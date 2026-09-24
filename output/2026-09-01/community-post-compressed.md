📝 SUMMARY

This extended five-part session was an open coaching/mastermind call covering agentic infrastructure, go-to-market execution, and career strategy. The recurring theme was "agentic OS" architecture: Patrick Chouinard's home-lab walkthrough (chief-of-staff agent, knowledge graph, observability stack) sparked a dashboard-vs-simplicity debate with Shakur and Ty Wells, while Scott Rippey demoed his custom "Blackbox" Mac IDE, including a 3D database visualizer — all built by prompting AI. On the business side, Juan Torres received iterative GTM coaching from Brandon Hancock on ICP databases and cold email plus guidance weighing VC vs self-funded growth; Scott pitched a HYROX-training SaaS partnership, Daniel Zivkovic sought distribution for his EMS documentation startup, and Paul Miller shared his pivot to a VC-backed AI dev-studio model. A strong throughline was experimentation discipline: build evaluation sets before choosing architectures, log everything, use cheap models at scale and premium models only where needed, and treat falling model costs as a margin reset (RecapFlow dropped from $1.50 to $0.15/call). The call closed on career/content strategy — Brandon advising Varun Sharma to build a public challenge-video case study — plus tool recommendations, a promo video demo, and a caution on Delaware C-Corp incorporation risk.

💡 KEY INSIGHTS

Patrick Chouinard's Hermes agent works as a chief-of-staff delegating to specialized sub-agents (researcher, operator, coder), each carrying only the tools/knowledge needed to keep the main agent's context light.

His T3 code setup aggregates Claude Code and Codex sessions per project across remote Proxmox VMs, with a dashboard tracking ~35 packages across 7 projects via a skill that reads every commit and PR merge.

InfraKnowledge is markdown-only documentation of infra inventory, roles, and dependencies, compiled into a knowledge graph to sequence and parallelize work.

Dashboards become necessary once you run many parallel tools/CLIs/MCPs with limited daily engagement — otherwise you silently rebuild the same functionality twice.

Patrick proposes a dedicated Pydantic AI-based review/red-team harness instead of a coding model reviewing itself — a distinct "debugging specialist."

Brandon Hancock: enterprise sales cycles run ~5 months, so line up committed customers before finishing compliance work (SOC 2/HIPAA), not after.

Switching a classification task to DeepSeek v4 Flash cut cost 100x ($350 to $3) at equivalent quality — rapid AI cost deflation is a strategic lever.

For multi-capability agents, don't guess architecture: generate ~100 adversarial synthetic conversations bucketed by user type to build an eval set before choosing single-agent vs orchestrator-plus-sub-agents.

His "loop engineering": manually run plan → critique → execute → review 2-3 times, log every experiment to a markdown journal (survives context compaction), then run autonomously overnight (one run cost ~$400).

Model strategy: cheap flash/Chinese models (Gemini 3.6, GLM) for large-scale experimentation; GPT-5.5 no-thinking for fast production responses; Claude/Opus on AWS Bedrock is throttled with painful support at scale.

Terminology matters: an LLM with tool calls is not an agent — a true agent reasons and acts autonomously in an unsupervised loop.

For long-running autonomous work, break goals into "gates" with self-determined success criteria; the agent loops plan → critique → act → review within each gate before advancing, preventing premature "I'm done" claims.

His Shipkit SDLC pipeline: Claude plan mode → task-template skill → adversarial "poke holes" review skill → execution → completion-review skill — every stage is its own skill with a persistent artifact.

ICP database method: use Grok to find 10-20 leads per city, manually apply judgment 3-5 times per city to train the tool, then codify a rulebook (Apify, scraping sub-agents) to scale.

Cold outreach: never use a primary domain — burner domains with 2-week warmup via Instantly; one screen of copy, exactly one CTA. A/B test subject lines first (open rates), then 20+ copy variants (reply rates).

Capital becomes the bottleneck in 4-6 months for hardware-scaling businesses (manufacturing cost, not CAC, constrains growth) — apply early to TinySeed/YC; a Delaware C-Corp via Clerky (~$800-1000) is essentially mandatory for VC funding.

VC alternative: pre-order/deposit model (first 100 customers pay unit cost to jump the line) plus referral incentives (20-30% profit share for 6 months) to self-fund growth.

Before any partnership or revenue split, ask: "if this goes perfectly, what does it look like at the limit?"

Shakur deliberately skipped a graphical dashboard for his agent OS, using a JSON file plus a daily email digest instead — simplicity first.

Juan Torres proposed a lightweight Flask/Docker observability app logging each agent's row-by-row input/output for non-deterministic pipelines.

Paul Miller: enterprise AI dev costs haven't dropped like consumer/prototype costs — heavy onboarding and edge cases remain the moat, reshaping how VCs assess defensibility ("can this be cloned over a weekend?").

Scott Rippey: the ideal startup trifecta is builder + domain expert + distribution/audience partner; visualizing a DB schema as an interactive 3D model (Claude → Fathom Design) beats reading schema text. He also recommends enabling point-in-time recovery before real customers hit a Supabase DB, with dev/staging/prod via manual promotion.

Daniel Zivkovic: domain expertise in unsexy, bureaucratic industries (EMS/healthcare documentation) is a strong wedge because incumbent software quality is poor.

Varun Sharma: "the money is in the follow-up" — expect 4-5 follow-ups per lead; seed AI outreach prompts with voice-transcribed personal examples to avoid a robotic tone.

Brandon's career tip: one well-executed public technical case study (~2hr video, 800K views) can outweigh thousands of job applications — frame content around the AI/code/business overlap. He uses vidIQ "outlier" analysis to detect overperforming video formats — "imitate before innovate."

From chat: Harvey (legal AI) runs a customized Kimi K3, suggesting Chinese models are entering more "secure" inference environments — it's about the inference provider, not just the model.

❓ KEY Q&A

Q (Brandon Hancock): How many parallel projects does your dashboard track?
A (Patrick Chouinard): 35 packages across 7 underlying projects, including Hermes.

Q (Elijah Stambaugh): Is your "knowledge spine" just Hermes stripped down — markdown or a database?
A (Patrick): No — Hermes is multi-profile; the knowledge spine is a separate project (InfraKnowledge), entirely markdown files loaded into a knowledge graph.

Q (Juan Torres): Are logs/observability visible via artifacts from each agent?
A (Patrick): Yes — a full Prometheus/Grafana/Loki stack fed by every application, exposed to AgentOps, running on a few mini PCs.

Q (Shakur): Dashboard vs simple JSON file + email digest?
A (Patrick): For simple email/meeting management, simple suffices; with many parallel tools and limited daily engagement, visualization prevents rebuilding the same functionality twice.

Q (Hemal Shah): Orchestrator+sub-agents or planner/executor for a multi-capability e-commerce co-pilot?
A (Brandon Hancock): Don't decide upfront — build a 100-conversation adversarial eval set, start simple, iterate toward complexity based on measured failure rates.

Q (Hemal Shah): American model recommendations?
A (Brandon): Strong thinking model overnight for research; for production, GPT-5.5 (no-thinking) if it must be American, or Gemini 3.6/Flash if cost/speed matters more.

Q (Brandon Hancock): Is DuckDB a vector store — are you running two vector stores?
A (Paul Miller): No — DuckDB is a file-based columnar query layer on top of LanceDB, which handles vector/word content.

Q (Juan Torres): Methodology for an ICP outreach campaign?
A (Brandon): Grok for 10-20 ICPs per city, manual judgment 3-5 times per city, codify a rulebook, scale via Instantly with burner domains.

Q (Juan Torres): Why pursue VC funding if they don't take shareholding here?
A (Paul): The VC prep process (TAM, differentiation, cost structure) is valuable even outside investment, e.g., negotiating with manufacturing partners.

Q (Brandon, to Scott): If the HYROX app goes perfectly, what does it look like at the limit?
A (Scott Rippey): ~1,000 users = ~$40k/month (~$500k/yr); profits split evenly between Scott, Joe, and Alyssa.

Q (Scott Rippey): Are you using Supabase — what's your setup?
A (Brandon/Scott): Yes — point-in-time recovery before going live; separate dev/staging/prod.

Q (Brandon): How do I get "loop deep work" working instead of my agent claiming "I'm done" prematurely?
A (Brandon, self-answer): Break goals into gates with self-determined success/failure criteria; loop plan-critique-act-review within each gate, and feed back corrections when it falsely claims completion.

Q (Varun Sharma): For the review step, a different model or adversarial?
A (Shakur): Currently the same model with a dedicated review prompt; long-term plan is a different model (e.g., Claude calling Codex) for adversarial review.

Q (Varun Sharma): I've positioned around the Google/Gemini stack, but Google lags frontier labs — should I pivot?
A (Brandon): Stack positioning still works, but real leverage is public proof of skill — a scalable technical "challenge" video modeled on a viral AWS case study.

Q (Varun Sharma): Can deep self-reflection happen within a single prompt like Shipkit's task templates?
A (Brandon): No — every SDLC step (plan, task template, adversarial review, execution, completion review) is its own dedicated skill/prompt.

🛠️ TOOLS AND CONCEPTS MENTIONED

T3 code – harness aggregating Claude Code/Codex sessions by project, run remotely via VM.
Hermes – Patrick's multi-profile "chief of staff" agent framework.
CMUX / Cursor – prior IDE tools; Cursor canceled after SpaceX acquisition.
Grok / GrokBot (4.6) – ICP research, lead lists, LinkedIn data pulls.
Instantly (instantly.ai) – cold outreach platform; burner domains, ~2-week warmup.
listio.ai / Listio – Brandon's YouTube lead-magnet SaaS side project.
GLM 5.3 / 5.3 Flash – low-cost model; cut RecapFlow from $1.50 to $0.15/call; also cited for EMS Soap cost reset.
DeepSeek v4 Flash – 100x cost reduction for classification tasks.
Luna model (Google) – considered, then replaced by DeepSeek.
OpenRouter – alternative inference provider; AWS Bedrock raised as HIPAA-compliant alternative for Chinese models.
Kimi K (K3) – Chinese model; basis for Harvey's legal AI via a secure inference provider.
ShipKit / Shipkit.ai – Brandon's task-template/skill-based SDLC workflow system.
Prometheus, Grafana, Loki – observability stack in Patrick's home lab.
AgentOps – CLI/MCP exposing infra to the agent framework.
InfraKnowledge – markdown-based infra knowledge graph project.
Proxmox – VM virtualization backend.
Pydantic AI – open-source framework Patrick plans to customize for review/red-teaming.
ACP (Agent Client Protocol) – Bastian has a working PR for T3 code integration; offered to share the repo.
LanceDB – vector/word-content DB (Paul Miller's reporting stack; also used by Daniel Zivkovic).
DuckDB – columnar query layer atop LanceDB ("intelligence layer").
Cerebras – fast-hosted inference for real-time chat front end.
RunPod – GPU hosting for backend model processing.
Postgres – master data store in Paul's stack.
GPT-5.5 (no-thinking) – fast, affordable American production model.
Gemini 3.6 / 3.6 Flash / 3.7 Flash – classification/quick tasks; 3.7 Flash praised in chat.
Claude / Opus (AWS Bedrock) – criticized for rate limits/throttling at scale.
DaVinci Resolve – Juan Torres's promo video editing.
Flask / Docker – proposed observability/test web app.
EMSO – Brandon's expert-judgment-extraction project (moat example).
TryAIBooth / AIBooth – burner-domain service for outreach.
Vercel – fast landing-page deployment.
Calendly – single CTA link on outreach/landing pages.
SerpAPI – pulls Google Places data for lead lists (cheaper than Google API keys).
Clerky – Delaware C-Corp/cap-table setup (~$800-1000).
TinySeed – pre-seed accelerator (batch opens Sept 1-9).
Y Combinator (YC) – alternative funding; more capital, later disbursement.
Fable – multi-model orchestration (Opus, Sonnet 5.5, Sol) with global rules, used by Scott Rippey.
Supabase – DB backend; point-in-time recovery and dev/staging/prod separation discussed.
Fathom Design – used with Claude to generate 3D DB visualization.
Blackbox – Scott Rippey's custom Mac IDE/agent harness (agentic browser, iOS simulator, SQLite usage tracking); repo shared.
TestFlight – testing Scott's companion iOS app.
Cloudflare – secure sync between IDE and iOS app.
CC Usage (ccusage) – tracks daily token usage across Claude/Codex/Grok.
PureMail – cheap email service for Shakur's cold-outreach tool.
vidIQ – YouTube outlier/viral-format analysis plugin.
Google ADK / Gemini API / Google Cloud – referenced re: Varun's stack positioning.
Fireflies.ai / Fathom / Sembly – meeting notetaker bots in the call.
poteto's "unslop" skill / matt's "/wait-what" – Claude/Cursor plugin skills shared in chat.

📎 SHARED RESOURCES

YouTube channels to follow (Patrick's daily picks):
https://www.youtube.com/@AndrejKarpathy
https://www.youtube.com/@NateBJones

Portfolio & content examples:
https://www.zalak-patel.com/ — portfolio website example (Ryan C.)
https://youtu.be/W4EwfEU8CGA — AWS scalability "challenge video" case study, the model for public proof-of-skill content (Brandon Hancock)
https://www.youtube.com/@Itssssss_Jack — YouTube channel with Claude Design videos (Daniel Zivkovic / Brandon Hancock)
https://chromewebstore.google.com/detail/vidiq-vision-for-youtube/... — vidIQ Chrome extension (Daniel Zivkovic)

AI tools & engineering:
https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md — "unslop" skill for cleaning Opus responses (Morgan)
https://www.anthropic.com/engineering/building-effective-agents — Anthropic's "start simple" agent guidance (Daniel Zivkovic, for Hemal Shah)
https://www.cerebras.ai/infcamp — Cerebras inference platform (Brandon Hancock)
https://github.com/dzivkovi/video-intel/blob/.../intelligence-layer.md — Daniel's DuckDB-as-intelligence-layer implementation
https://github.com/ccusage/ccusage — CC Usage token-tracking tool (Varun Sharma)
https://github.com/scott-rippey/cc-blackbox-app — Scott Rippey's Blackbox IDE repo
https://youtu.be/c9WCcD4fH6c — video shared by Brandon Hancock during Juan Torres's segment

Sales & outreach:
https://serpapi.com/ — Google Places data tool for ICP research (Paul Miller)
https://www.youtube.com/@InstantlyAI/videos — Instantly's channel, cited as the cold-outreach "bible"

Startup & fundraising:
https://apply.tinyseed.com/ — TinySeed application (Brandon Hancock)
https://www.clerky.com/welcome — Clerky C-Corp setup (Brandon Hancock)
https://youtu.be/7VKliOQXQ9M — YC / Lean Startup author video warning against Delaware C-Corps (Daniel Zivkovic)

Other:
https://www.shipkit.ai/ — Brandon Hancock's Shipkit product
https://lnkd.in/p/g8e5p6cH — Ty Wells's LinkedIn article/presentation
https://www.instagram.com/alyssamcelheny/ — HYROX athlete / marketing partner reference (Brandon Hancock)

🔄 FOLLOW-UPS WORTH EXPLORING

Patrick Chouinard: build a new T3 code server modeled on his home-lab infra (Proxmox VMs + thin Mac client), then demo his Grafana-based observability app to Juan Torres once production-ready.

Shakur: set up additional Linux laptops linked into T3 code as separate machines; Patrick to share progress.

Brandon Hancock and Patrick Chouinard: follow-up call on the Pydantic-based review/red-teaming harness idea.

Brandon Hancock: 13-day deadline to launch v1 of listio.ai, then a one-week wait to gauge Instantly campaign traffic before further development.

Bastian Venegas Arevalo: invite Patrick to his GitHub repo with the ACP integration PR for T3 code.

Hemal Shah: build a 100+ conversation adversarial eval set before finalizing his co-pilot's architecture, and report results back to the community.

Juan Torres: send Brandon the AI Boots Studio promo video, buy 3-5 burner domains and begin warmup, build ICP-specific contact lists (~1,000 per ICP), set up Instantly, build a landing page (Claude + Vercel + Calendly), pursue TinySeed/YC applications, set up a Delaware C-Corp via Clerky, and consider a referral/deposit pre-funding model.

Paul Miller: keep the group posted on his product launch and new VC-backed dev-studio arrangement.

Scott Rippey and partners (Joe, Alyssa): finalize a formal partnership agreement for the HYROX SaaS product ("Acceler8 Training") before/during a 2-3 week build trip in Michigan.

Scott Rippey: release his 3D DB visualization library and Blackbox IDE repo, ship the companion iOS app after TestFlight testing, and keep both free for the community.

Shakur: reclaim manual control of send limits on his Google-review-reply tool, lower its price, and add a user-facing dashboard.

Daniel Zivkovic and co-founder Raul: continue pursuing a distribution partnership for their EMS documentation product.

Varun Sharma: revamp the AI cold-outreach experiment (follow-up cadence, tone) and produce a first "challenge video" within ~3 weeks per Brandon's advice.

Patrick Chouinard and Daniel Zivkovic: schedule a Thursday-afternoon call, with Daniel watching the YC Delaware incorporation-risk video first.