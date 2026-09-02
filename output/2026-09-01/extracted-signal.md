# general

This is a recurring builder/founder coaching call led by Brandon Hancock, with Patrick Chouinard hosting and a rotating group of participants (Paul Miller, Bastian Venegas Arevalo, Hemal Shah, Elijah Stambaugh, Juan Torres, Shakur, Ty Wells, Daniel Zivkovic, Scott Rippey, Varun Sharma, Morgan, and others) sharing project updates. Brandon opened with a business update on his startup EMS SOAP (EMS/ambulance documentation AI), describing a slow enterprise sales cycle, a new capital raise in progress, a cost-optimization strategy tied to falling LLM prices (GLM 5.3, DeepSeek), and a new side project, Listio (an AI lead-magnet/landing-page builder for YouTube creators), being built under a self-imposed 30-day, thousand-customer-first challenge using cold outreach via Instantly.

Patrick shared deep detail on his personal "agentic OS" — a Proxmox/Hermes-based infrastructure with a markdown-based planning repo ("Pachu Plan"), an "InfraKnowledge" knowledge graph, a self-updating task dashboard fed by commit/PR analysis, and a move toward using T3 Code as a universal interface across Claude Code and Codex sessions. Several others (Shakur, Ty Wells) shared parallel "personal OS"/dashboard builds and debated the value of graphical dashboards vs. simpler JSON/email-based systems.

The rest of the call was a round-robin of project updates and peer coaching: Hemal Shah got detailed architecture advice from Brandon on building and evaluation-testing an e-commerce AI co-pilot (adversarial test sets, orchestrator vs. sequential LLM calls, model selection); Juan Torres demoed a viral AI-photo-booth promo video and got a full go-to-market/fundraising playbook (cold outreach, landing page, referral programs, C-Corp/VC readiness) from Brandon and Paul; Paul Miller described a VC-backed AI dev studio pivot and an agentic BI/reporting system built on LanceDB/DuckDB/Cerebras; Scott Rippey demoed a custom Mac IDE/agent harness ("Blackbox") with an agentic browser, iOS simulator, and phone companion app, plus a new HYROX training SaaS partnership; Daniel Zivkovic introduced himself and his EMS-adjacent product; Shakur discussed automated outreach experiments (Google review reply service) that weren't converting yet and got feedback on offer/copy design; Varun Sharma got career-positioning advice from Brandon (building a public "challenge" YouTube series to create social proof for a job search) and a ShipKit-specific question on task-template/spec-driven prompting was answered in depth.

# insights

- **Cost curves are a strategic weapon, not just a savings**: Brandon Hancock's rule for AI products — as models get 10x cheaper (e.g., GLM 5.3 dropping EMS SOAP's per-call cost from $0.50–0.80 back toward $0.05), reinvest the savings into 10x more product value (integrity checks, live QA) rather than just pocketing margin; expect this reset cycle every 6–8 months.
- **Model switching can yield 100x cost reduction at equal quality**: Brandon found DeepSeek v4 Flash did the same classification task as a frontier model for $3 instead of $350 — a rare case of a model swap delivering "same intelligence, 100x cheaper."
- **Distinguish "agent" from "LLM with tools"**: Brandon's definition — a true agent takes input, reasons, and takes action in a loop; a pipeline of sequential (even parallel) LLM calls that just streams an answer quickly is not "agentic," it's just a series of LLM calls. Terminology matters for architecture decisions.
- **"Loop engineering" / iterative agent workflows**: Run an agent through repeated cycles of hypothesis → experiment → analyze results → propose fix → re-test, letting AI have full autonomy over many iterations (Brandon has run loops for 12+ hours). Journal every experiment to a markdown file so context survives compaction.
- **Adversarial test-set-first development**: Before building any conversational/agentic system, generate ~100 adversarial synthetic conversations across "easy," "confusing," and "prompt-injection" buckets to create an evaluation set with expected outcomes — this prevents wasted engineering cycles (Hemal lost two weeks skipping this step).
- **Start with the simplest architecture and let failure data drive complexity**: Brandon's default approach — try one agent with many tools first, measure failure modes, then justify adding an orchestrator/sub-agents only once evidence shows it's needed.
- **Chinese/open models for cheap experimentation, American models for production-facing/regulated work**: Brandon uses GPT-5.5 (no thinking) or Gemini 3.6 as fast/cheap American responders for HIPAA-constrained products, but recommends Chinese models (GLM, DeepSeek, Qwen) for internal experimentation/testing where cost matters more than compliance.
- **"A thousand customers before a single line of code"**: Brandon's self-imposed rule — if you can't find and contact 1,000 potential customers for an idea, it's not worth building.
- **Specialize sub-agents, don't overload the primary agent**: Patrick's chief-of-staff pattern — the default/main agent should become an expert on the user and delegate execution to specialized sub-agents (researcher, coder, operator) that carry the tools/knowledge for their domain, keeping the main agent's context lean.
- **Meta-review of the process itself, not just the output**: Brandon independently converged on Patrick's idea of building a layer that reviews the agentic workflow/skills used (not just the code produced) after each task, to identify systemic gaps in the SDLC skill chain.
- **Observability is essential for non-deterministic systems**: Juan Torres advocates a lightweight Flask/containerized "data web app" to log every agent-to-agent transformation (including debug-mode reasoning traces) for QA on non-deterministic pipelines — cheaper and more flexible than building it into production logging.
- **One domain per cold-outreach campaign, never your primary domain**: Instantly's rule of thumb — 1 domain + 5 email accounts ≈ 150 sends/day; burner domains take ~2 weeks to warm up before outreach can start.
- **Emulation before innovation**: When directing AI to write outreach copy or execute unfamiliar tasks, find someone who has already succeeded at it and have the AI copy their playbook almost verbatim rather than "being creative," to constrain output quality.
- **YouTube/content-building is the highest-leverage skill for engineers**: Brandon's philosophy — "I'd rather have a million people know me and be an average engineer than be the world's best engineer and have three people know me." A single viral, in-public technical challenge video can outperform thousands of job applications for career switching.
- **VC due diligence increasingly tests defensibility**: Paul Miller notes that in 2026, VCs are explicitly testing whether a competitor could clone your app in a weekend — physical/hardware products, proprietary datasets, and domain-expert judgment are much harder to clone than pure software.
- **C-Corp caution**: Daniel Zivkovic flagged a warning (via Eric Ries) that standard Delaware C-Corp/VC paperwork can legally strip founders of control (cited Twilio's founder being ousted) — worth reviewing before agreeing to it for fundraising.
- **Judgment-at-scale is AI's moat gap**: Brandon argues AI can't yet replace domain-expert judgment across thousands of edge cases (e.g., what a veteran EMS chief would decide), which is where defensible long-term products should focus versus quick cash-play apps.

# qa

**Q (Elijah Stambaugh):** How do you structure the "knowledge spine" — the idea that your chief-of-staff agent knows where to go and how to get information, and that Hermes is stripped down to that role?
**A (Patrick Chouinard):** It's not Hermes itself that's stripped down — Hermes hosts multiple profiles/sub-agents. The default profile is the chief of staff; every time a role is removed from it and given to a specialist sub-agent (researcher, coder), that sub-agent gets all the tools/skills/knowledge for its job, while the chief of staff keeps only an understanding of the sub-agent's role, not the raw context. The actual knowledge lives in a separate "InfraKnowledge" project of markdown files that feeds a knowledge graph determining implementation order and parallelizable packages.

**Q (Juan Torres):** Regarding the CI/CD agentic pipeline — are logs/observability generated as artifacts for each agent in the pipeline, and what kind of logs are you generating to see through the whole system?
**A (Patrick Chouinard):** Yes — there's an entire monitoring/observability backend (Prometheus, Grafana, Loki) fed by every application, and AgentOps is responsible for reading and understanding that observability data. It runs on just a few mini PCs/desktops, not a real data center.

**Q (Shakur):** What's the benefit of a big visual dashboard linking everything together versus a simpler approach (e.g., a JSON file plus a daily email of tasks/blockers), which is what he chose to reduce complexity?
**A (Patrick Chouinard):** If you're only managing emails/meetings, a simple system is fine (and is what he uses for work). But once you have many sub-tools, CLIs, and MCPs running across infrastructure that you don't touch daily, you need visualization just to remember what exists and avoid rebuilding the same thing multiple times — the dashboard is purely an aggregator/launcher, with the GUI intentionally built last.

**Q (Hemal Shah):** For an e-commerce AI co-pilot with multiple capabilities (Q&A, buy, search), should the architecture be an orchestrator with sub-agents per capability, or a planner/executor style?
**A (Brandon Hancock):** Don't decide up front — treat it as a science experiment. Generate ~100 adversarial test conversations, start with the simplest possible architecture (one agent, many tools), run the eval set, identify failure modes, then iteratively test more complex architectures (orchestrator + sub-agents, 1-to-many-to-1 patterns) using a "loop engineering" auto-loop, using cheap Chinese models for iteration and reserving GPT-5.5/Gemini for production.

**Q (Hemal Shah):** Any model recommendation for running this experiment loop if it has to be American models (has both GPT-5.6 and Opus 5 subscriptions)?
**A (Brandon Hancock):** Use a strong thinking model (e.g., 5.6/Opus-tier, slower is fine since it runs overnight) for the experimenting/orchestrating agent, but use the cheapest fast model for the actual user-facing responder — Gemini 3.6 Flash if speed matters, or GPT-5.5 (no thinking) as the American responder option.

**Q (Hemal Shah):** Does loop engineering just mean crafting a prompt that keeps going until a criterion is met?
**A (Brandon Hancock):** Yes — tell the AI to run the loop a few times with you reviewing each cycle first (to correct its judgment), then let it run autonomously (e.g., overnight) once you trust its direction, having it log every experiment to a markdown file so it can recover context after compaction.

**Q (Juan Torres, re: cost management):** Would it be useful to build a simple "data web application" test client to visualize agent transactions/transformations for stress-testing non-deterministic systems?
**A (Brandon/Hemal exchange, clarified by Juan):** Yes — register each adversarial input as a row, capture sequential agent outputs (agent 1→2→3) with an optional debug mode showing full LLM reasoning (extra tokens, not for production), and connect it to the same database rather than building something separate — containerize it so it can be toggled on for dev/test only.

**Q (Paul Miller):** Given Brandon's Google exposure, is EMS SOAP leveraging Google's startup credit program?
**A (Brandon Hancock):** Yes, they received AWS and Google credits via Tiny Seed, though amounts were tied to how much was raised; plans to ask for more once the next funding round closes. Also noted AWS/Claude-via-Bedrock has been extremely painful to use (rate limits, support tickets, timeouts) compared to OpenAI/Google.

**Q (Brandon Hancock, to Daniel Zivkovic):** LanceDB is understood, but what is DuckDB being used for — is it a vector store?
**A (Daniel Zivkovic / Paul Miller):** No, DuckDB sits on top / alongside as a columnar, file-based search database — treat it like a big database for fast structured queries, not a vector store; used to pre-format data per metric category for fast agentic querying.

**Q (Brandon Hancock):** Which specific model is Paul using with Cerebras for fast queries?
**A (Paul Miller):** Believes it's a Qwen model, though he's using about nine models total across the system, plus separate RunPod-hosted models for backend data processing.

**Q (Juan Torres):** Do you have a literature/methodology for the outreach campaign (identifying 1,000 ICPs and then running the email campaign)?
**A (Brandon Hancock):** Detailed step-by-step: use Grok to iteratively find and manually judge sample ICPs (10–20 at a time) across a few cities until the AI understands what's wanted, then scale the search query pattern (state/city/venue-type) and let AI find leads for free before paying for tools like Apify; buy 3–5 burner domains, set up Instantly (~2 weeks warm-up), follow Instantly's own YouTube channel for cold email best practices, keep emails short with one CTA pointing to a Calendly.

**Q (Daniel Zivkovic, chat, re: niche choice):** Given healthcare software is notoriously bad/bureaucratic (Epic, Cerner), how did you choose the EMS niche and who is your ICP, given you'd never compete directly with the giants?
**A (Brandon/Raul via Brandon):** They aren't competing with EMR giants like Epic/Cerner — the product helps EMS providers (fire departments, hospitals, ambulance companies) write the documentation (via ePCR) required for reimbursement after patient transport. The niche came from his co-founder Raul, an actual EMS chief, hiring Brandon as a freelancer to build v1, which grew into a partnership; distribution was the missing piece, now being solved via a distribution-partner deal and cold outreach.

**Q (Shakur):** For the automated Google-review-reply outreach product that's getting zero replies, what could be wrong?
**A (Brandon Hancock, Daniel, Varun collectively):** Consider whether the offer itself delivers obvious/high ROI (compare against Daniel's parallel "rebuild your website" offer which is converting); increase follow-up emails (money is in the follow-up, aim for multiple touches); make AI-written copy sound human by feeding it voice-transcribed examples of natural phrasing; A/B test subject lines and copy variants to isolate what's broken (email vs. offer vs. volume); constrain the AI by having it emulate a proven playbook rather than acting unconstrained.

**Q (Varun Sharma):** Given Google has lagged behind frontier labs (Gemini/ADK less hyped than Claude agents), should he pivot his personal-brand strategy of specializing in the "Google stack"?
**A (Brandon Hancock):** Keep the strategy directionally, but pivot tactics — rather than applying to jobs the traditional way, build public "challenge" content (citing an AWS scaling-challenge YouTube video that likely generated many job offers) that proves engineering skill through a live, transparent problem-solving journey (e.g., "how can I handle 1,000 customer queries with AI for under a dollar"), give away all code/prompts, and treat it as a repeatable, time-boxed content format.

**Q (Varun Sharma):** Within ShipKit's task templates, is there a way to replicate the deep "self-reflection" thinking style in a single prompt?
**A (Brandon Hancock):** No single-prompt shortcut — instead, break the SDLC into discrete skills/artifacts: plan mode (condensed research) → detailed task template (12 sections forcing specs for data model, UI, etc.) → a dedicated "poke holes" skill that critiques the plan → execution → review, with each step in the pipeline generating or updating a saved artifact.

# tools

- **T3 Code** – IDE/interface aggregating Claude Code and Codex sessions across machines; Patrick and Shakur are heavy users; Bastian has a PR in progress for ACP (Agent Client Protocol) integration.
- **Hermes** – Patrick's multi-profile personal agent framework (chief-of-staff default profile plus specialist sub-agents).
- **AgentOps** – Patrick's custom CLI/MCP exposing his Proxmox infrastructure to his agent framework, including observability.
- **InfraKnowledge** – Patrick's markdown-based knowledge graph project tracking infra inventory, policy, and package dependencies.
- **Prometheus / Grafana / Loki** – Patrick's self-hosted observability stack for his agentic infrastructure.
- **PI.dev (Py.dev)** – Open-source customizable agent framework Patrick is adapting specifically for code review/security/red-teaming.
- **GLM 5.3 / 5.3 Flash** – Chinese LLM used by Brandon for classification and (soon) as EMS SOAP's default model due to 10x cost drop.
- **DeepSeek v4 Flash** – Used by Brandon for cheap large-scale classification (~$3 vs $350 with a pricier model).
- **Gemini 3.5/3.6/3.7** – Google models Brandon uses for classification/small tasks; 3.6/3.7 had a temporary 50% cost discount.
- **GPT-5.5 / 5.6** – American models used by Brandon as fast/no-thinking responders and as thinking models for complex agent orchestration.
- **Grok / GrokBot / Grok 4.6** – Used by Brandon for lead-finding/ICP research; Paul Miller uses GrokBot as a marketing "team" interface (LinkedIn connector, funnel building).
- **Instantly** – Cold email outreach platform central to EMS SOAP's, Listio's, and Juan's go-to-market strategy.
- **OpenRouter** – Discussed as a model routing option, though HIPAA/BAA constraints limit its use for EMS SOAP.
- **AWS Bedrock (Claude)** – Criticized by Brandon for rate-limit/support pain when running Claude models at scale.
- **Cerebras** – Fast-hosted-inference platform Paul Miller uses for real-time chat over his BI data.
- **LanceDB** – Vector/word-content store Paul uses to classify sales conversations; also used by Daniel Zivkovic.
- **DuckDB** – Columnar query layer Paul and Daniel use as an "intelligence layer" atop LanceDB.
- **RunPod** – GPU cloud servers Paul used to process 11 years of historical business data.
- **Kit / ConvertKit** – Referenced by Brandon as the existing (limited) lead-magnet tool creators use, motivating Listio.
- **Listio.ai** – Brandon's new side-project: AI tool to auto-generate lead-magnet landing pages for YouTube creators.
- **Luna (Google model)** – Considered then dropped by Brandon for the YouTube-scraper classification task due to cost.
- **Fable / Sol / Opus / Sonnet 5.5** – Multiple models orchestrated inside Scott Rippey's multi-engine code review/security system.
- **Claude Design** – Used by Brandon and Scott to rapidly generate UI/landing pages from backend specs.
- **CMUX IDE** – Mentioned by Brandon/Paul as an alternative interface for running Claude/Codex sessions.
- **Clerky** – Recommended tool for setting up a Delaware C-Corp and cap table for fundraising.
- **Tiny Seed** – Accelerator/fund Brandon used to raise money for EMS SOAP; recommended to Juan for pre-seed funding.
- **Y Combinator (YC)** – Alternative accelerator option discussed for Juan's AI Booth Studio.
- **SerpAPI** – Recommended by Paul as a cheaper alternative to Google Place API for building venue/lead lists.
- **DaVinci Resolve** – Video editing tool Juan used to create his AI Boot Studio promo video.
- **PostLitit / PurelyMail** – Email tools mentioned/used by Shakur for his automated cold-outreach experiment.
- **vidIQ** – Chrome extension Brandon uses to spot outlier/viral YouTube videos for content strategy.
- **CC Usage (ccusage)** – CLI tool to track daily token usage across Codex/Claude/Grok, referenced by Varun and used by Scott/Brandon as a personal productivity metric.
- **Blackbox (cc-blackbox-app)** – Scott Rippey's custom Mac IDE/agent harness with decision logging, agentic browser, iOS simulator, and companion mobile app.
- **Supabase** – Database backend used by Scott for his HYROX/Acceler8 Training app; point-in-time recovery and dev/staging/prod separation discussed.
- **Fathom Design** – Tool Scott used to generate the 3D database visualization model.
- **ShipKit** – Brandon's existing product/course teaching agent-driven rapid app development, referenced repeatedly as a place to eventually add new skills/templates.
- **Anthropic "Building Effective Agents" guide** – Referenced by Daniel Zivkovic as a starting point for agent architecture.

# links

- https://www.youtube.com/@AndrejKarpathy – Patrick's shared "daily follow" YouTube channel recommendation.
- https://www.youtube.com/@NateBJones – Patrick's shared "daily follow" YouTube channel recommendation.
- https://www.zalak-patel.com/ – Example portfolio website shared by Ryan C.
- https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md – "unslop" skill Morgan recommends for cleaning up Opus responses.
- https://github.com/scott-rippey/cc-blackbox-app – Scott Rippey's repo for his custom Mac IDE/agent harness ("Blackbox"), shared for free use.
- https://github.com/ccusage/ccusage – Token usage tracking tool shared by Varun Sharma.
- https://github.com/dzivkovi/video-intel/... (intelligence-layer.md) – Daniel Zivkovic's write-up on using DuckDB as an "intelligence layer" atop LanceDB.
- https://www.cerebras.ai/infcamp... – Cerebras link shared by Brandon Hancock in reference to Paul's stack.
- https://serpapi.com/ – SerpAPI, recommended by Paul Miller for cheap Google Place data for TAM research.
- https://www.instagram.com/alyssamcelheny/ – Instagram of the HYROX champion partner in Scott Rippey's new fitness SaaS project.
- https://www.youtube.com/@InstantlyAI/videos – Instantly's YouTube channel, Brandon's recommended resource for cold outreach best practices.
- https://youtu.be/c9WCcD4fH6c – Video Brandon shared as inspiration for Juan's outreach/ICP-finding approach.
- https://apply.tinyseed.com/ – Tiny Seed accelerator application page, shared for Juan's fundraising.
- https://www.clerky.com/welcome... – Clerky, recommended for setting up a C-Corp.
- https://youtu.be/7VKliOQXQ9M – Video shared by Daniel Zivkovic warning against Delaware C-Corp structures (Lean Startup author), citing the Twilio founder example.
- https://www.shipkit.ai/ – Brandon Hancock's ShipKit product link.
- https://chromewebstore.google.com/detail/vidiq-vision-for-youtube/... – vidIQ Chrome extension link shared by Daniel Zivkovic.
- https://www.youtube.com/@Itssssss_Jack – YouTuber ("Jack Roberts") referenced by Brandon for good Claude Design tutorials.
- https://www.anthropic.com/engineering/building-effective-agents – Anthropic's agent-building guide, shared by Daniel Zivkovic for Hemal Shah.
- https://lnkd.in/p/g8e5p6cH – LinkedIn article Ty Wells shared (his own presentation/post).
- ILoveMarketing.com (Dean Jackson) – Referenced by Daniel Zivkovic as a resource for email marketing ideas for Juan.

# decisions

- Brandon Hancock will connect with Patrick Chouinard (Thursday afternoon) to go deeper on Patrick's review-cycle/multi-model code-review idea for potential incorporation into EMS SOAP's SDLC.
- Bastian Venegas Arevalo will invite Patrick Chouinard to a GitHub repo containing his ACP integration PR for T3Code.
- Juan Torres will buy 3–5 burner domains and set up Instantly cold-outreach campaigns per ICP (wedding venues, convention centers, country clubs) for AI Boot Studio.
- Juan Torres will build a landing page (via Claude Design + Vercel) pointing to a Calendly for AI Boot Studio bookings.
- Juan Torres will pursue pre-seed funding applications (Tiny Seed, YC) and set up a C-Corp via Clerky in preparation for VC fundraising.
- Scott Rippey will release his iOS companion app (via TestFlight) within a day or two and continue developing the HYROX/Acceler8 Training app with his partners Joe and Alyssa.
- Scott Rippey will formalize a partnership agreement (deliverables, equity split) with his HYROX training co-founders.
- Varun Sharma will produce and share his first public "challenge" YouTube video within roughly three weeks as part of a personal-brand-building push.
- Shakur will revamp his automated Google-review-reply outreach offer (lower price, add a dashboard, increase send volume, take manual control) since the AI-run experiment has yielded no replies.
- Shakur will try running PI.dev/GLM 5.3 debug mode despite prior cost concerns, per Patrick's suggestion.
- Brandon Hancock will keep the group updated on the EMS SOAP fundraising round and, once funded, resume regular YouTube content and update ShipKit with newer techniques/skills.
- Scott Rippey will share his GitHub repo (cc-blackbox-app) publicly and keep it free/open for others to test.
- Morgan committed (in chat) to building a prospect list (450 leads for Class2Curb.com) using the outreach method discussed on the call.