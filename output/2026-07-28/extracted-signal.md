## general

This coaching call brought together a cohort of founders and developers running an EMSO (EMS software) startup, side projects, and freelance work, with each participant giving a progress update to Brandon Hancock, who hosted and coached the group. Brandon opened with a personal update on smart glasses (Even Realities) and a candid business update on EMSO — the company is pivoting its ideal customer profile (ICP) from fire departments ("whales," slow-moving and bureaucratic) to private ambulance companies ("tunas"), driven by cash-flow pressure, while using an instantly-outreach + Loom-based sales motion. Patrick Chouinard discussed enterprise Claude Code rollout (pivoting from a 250-person pilot to 2,500 users), a self-improving internal support-knowledge-base skill built on Claude, and a "training generator" skill that auto-produces onboarding/training material and tracks user progress.

Other presenters included Alireza (Agent Tax, a cross-agent task/source-of-truth platform), Andrew Nanton (ADK, BAML, Herdr, LlamaParse tooling and questions about local models/Superpowers), Ty Wells (a fully agent-automated ERP/support pipeline and a golf tee-time app, TTL.golf), Scott Rippey (a deep-dive demo of a multi-model, multi-agent Claude Code security-review system with a Supabase/Vercel dashboard), Juan Torres (a physical AI photo-booth event product, first live field test), Morgan/mdcatc (Class2Curb, a school pickup/dismissal app, and a cemetery-mapping "Heritage Plot" product), and Ryan (AI-driven real estate video/website generation business in the UK, plus a security-review pass on his own apps). Throughout, Brandon coached each presenter on business-model framing, ICP selection, sales cadence (Loom outreach, case studies before revenue), and productizing/monetizing internal tools, while Patrick and others gave technical feedback on AI architecture choices (cross-model reviews, plugin marketplaces, local models, HTML-based presentations).

## insights

- Brandon Hancock's "whale/minnow/tuna" sales-segmentation framework (learned at CrewAI): whales are huge slow contracts (year+ to close), minnows are small deals not worth much individual attention (handle via automated outreach), tunas are mid-size accounts ($20-40k) that close in months — most orgs should focus limited selling time on tunas.
- When a startup is burning cash, changing your ICP/avatar contradicts standard growth advice (e.g., Alex Hormozi's "don't change avatars until saturated"), but speed-to-revenue can override that heuristic if the current avatar's sales cycle is too slow to survive on.
- Providing prospects with "sales-enablement" material (case studies, ROI calculators, one-pagers) that they can hand up their own chain of command (medic → chief → city council) turns customers into internal champions — a two-front strategy targeting both department heads and legislative/budget bodies can accelerate adoption.
- Patrick Chouinard: never use the same model family to review code/plans that generated them — cognitive biases carry through; cross-vendor review (e.g., Claude output reviewed by Codex/GPT) surfaces different classes of issues.
- Patrick Chouinard: local/small models (e.g., GPT-OSS-20B, Qwen 9B) aren't meant to compete with frontier models like Opus — they're useful for stable, low-cognition, 24/7 background tasks where you don't want to burn premium tokens and want deterministic behavior.
- Patrick's "generate training" skill works because it leverages artifacts (specs, plans) already produced by structured workflows (e.g., Superpowers) — enforcing a brainstorm→spec→plan pipeline pays off later because those documents become reusable inputs for training, docs, and presentations.
- Brandon Hancock: most rework in AI-assisted coding comes from under-specified plans, not from the coding agent itself — adding a "poke holes" review step after planning (testing assumptions before execution) reduces downstream cleanup significantly.
- Scott Rippey: model-authored findings are phrased inconsistently across runs/models, so dedup/context systems need fuzzy matching on title+body, not exact string match, or false-positive dismissals silently fail to suppress re-flagged issues.
- Scott Rippey: feeding dismissed/false-positive reasoning back into future review prompts (not just a suppression list) makes the specialist agents smarter over time and prevents bad findings from being regenerated and paid for repeatedly.
- Brandon Hancock's recurring go-to-market principle: pick a business model that's B2B over B2C when possible (more money per relationship), and if going B2C, prefer many small recurring payments over few large ones for resilience.
- Brandon Hancock: a great business partnership pairs a technical builder with a distribution/audience figurehead — product without distribution is worthless, distribution without product can't be monetized (citing Dan Martell and the Ben Affleck AI-company sale).
- Multiple founders (Brandon, Morgan/mdcatc) flagged the same regret: not doing outreach/pipeline-building early enough while the product was still imperfect — sales cycles in institutional/government-adjacent markets are long, so relationship-building should start well before the product is "ready."
- Case studies are more valuable than early revenue: giving away a product free to a handful of customers in exchange for measurable before/after results creates sales collateral that makes every future sales conversation about outcomes rather than features.
- Brandon Hancock's "promise, proof, next steps" structure for Loom/sales videos: state the outcome you'll deliver, show proof you've done it before, give a clear call to action — avoid backstory or long preambles.
- Discipline pattern shared by multiple members (Brandon, Ty, Juan, Morgan): gate further coding behind sales/outreach milestones (e.g., "no more code until 5 Looms sent" or "10 customers signed") to force market validation over endless feature-building.
- Ryan/Juan: low-competence inputs (e.g., amateur real estate photos) could be standardized via a simple "good vs bad example" checklist/pamphlet rather than needing complex AI tooling — sometimes the simplest fix is giving humans a clear visual spec.
- Patrick Chouinard: interactive HTML/JS presentations (via Claude Design) outperform PowerPoint for outreach decks — animations, transitions, and interactivity are far easier to generate this way than hand-building PowerPoint transitions.

## qa

**Q (Brandon Hancock):** For a real-world organization at scale, how are other agencies thinking about giving engineers effectively unlimited AI budgets without it being scary for a CEO?
**A (Patrick Chouinard):** They started with an arbitrary budget, raised it incrementally as users requested more (via usage data from Slash Insights and a custom skill), and eventually most users plateaued — only ~5% needed more, so the enterprise plan is sized around real usage data rather than guesswork.

**Q (Brandon Hancock):** Did your engineers actually see a real productivity bump from Claude, or is it more spin like some critics claim?
**A (Patrick Chouinard):** Yes — for heavy Cloud Code users they have real data showing engineering work that would have required a team of three for a year was done by one person in three months, giving a clear ROI.

**Q (Juan Torres):** Do you think a knowledge graph would enhance the Q&A support system you built?
**A (Patrick Chouinard):** Not really right now — the goal isn't knowledge search, just adding organization-specific specificity on top of Claude's own self-knowledge; latency needs to stay under a second, and they don't yet have enough supplemental information to justify a knowledge graph (they plan to connect to ServiceNow/RAG later instead).

**Q (Brandon Hancock):** What model is running under the hood of your Claude support skill — did you go open source, Google, etc.?
**A (Patrick Chouinard):** No separate model at all — it's built entirely as a skill inside the Claude desktop app itself, so people ask Claude questions about Claude.

**Q (Brandon Hancock):** How are you doing the cross-model review — is it a Claude sub-agent kicking off Codex, or a separate manual step?
**A (Patrick Chouinard):** It's a slash command (`/codex review`) inside Claude Code using the official OpenAI Codex plugin, which automatically feeds the last artifact produced (spec, plan, or code) to Codex for review.

**Q (Brandon Hancock, to Alireza):** Is Agent Tax essentially a Kanban/tracking layer that sits on top of any coding agent/harness, handling orchestration on top of orchestrators?
**A (Alireza):** Roughly yes — it's a "space"-based source of truth where teams organize projects/tasks, claim and track work across sessions and computers via MCP/plugins, so someone can ask "what's the status of that task?" weeks later and get full session history and progress.

**Q (Andrew Nanton):** Is Superpowers still worth using now that Opus 5 exists, or has it become redundant/token-heavy?
**A (Patrick Chouinard):** Still very much worth using — it's a small team that quickly re-optimized for Opus 5, and its value is enforcing a full brainstorm→spec→plan→build workflow whose artifacts (specs/plans) get reused for training generation, docs, and presentations.

**Q (Andrew Nanton):** Any recommendations on local models — when/where do they actually make sense versus Opus?
**A (Patrick Chouinard):** Local models will never replace Opus for day-to-day AI work, but they're great for background/24-7 jobs needing light cognition without burning tokens — e.g., GPT-OSS-20B or Qwen 9B for stable, low-cost automated tasks.

**Q (Ty Wells, re: WhatsApp agent-driven support pipeline):** What happens if a request is destructive or out of scope, like "delete the data"?
**A (Ty Wells):** A classifier flags anything beyond scope/an existing intent document as needing manual approval via Telegram before it's ever executed — new features require sign-off, fixes proceed automatically with safeguards in the build session.

**Q (Brandon Hancock, to Scott Rippey):** Are you running the security review agents on paid API tokens or on your existing Claude/Codex subscriptions?
**A (Scott Rippey):** It's built to support either, but currently runs entirely on his existing Codex and Anthropic subscription plans, with a Node CLI as the deterministic local orchestrator and Supabase/Vercel for tracking, so there's no marginal API cost.

**Q (Juan Torres, to Scott Rippey):** Could this security-review system also serve as an AI FinOps/governance tool at an organizational level (e.g., for Patrick's enterprise rollout)?
**A (Patrick Chouinard):** Yes — beyond tracking credits, it could encode enterprise-specific validation (governance, methodology compliance) on top of code review, essentially extending code quality checks into organizational policy checks.

## tools

- Claude Code — primary coding agent used throughout by nearly all participants for development and reviews.
- Claude Security (Cloud Security) — new Anthropic marketplace plugin for security scanning; Patrick found it token-expensive and less efficient than his own custom prompts.
- Superpowers — third-party public Claude plugin enforcing brainstorm→spec→plan→build workflow; widely used by Patrick, Andrew, Brandon.
- Codex plugin for Claude Code (openai/codex-plugin-cc) — official OpenAI plugin letting Claude Code invoke Codex for cross-model review of specs/plans/code.
- Codex CLI — used directly (outside the plugin) by Scott Rippey for adversarial cross-vendor security review.
- Fable — Claude-family sub-agent used by Andrew and Patrick for dispatching independent review/testing sessions.
- Agent Tax (agent-task.com) — Alireza's cross-agent task/orchestration and "source of truth" platform demoed on the call.
- ADK — Google's agent development kit; mentioned by Andrew as something he's been enjoying.
- BAML — a prompt/schema DSL Andrew tried; noted as still in flux.
- Herdr (H-E-R-D-R) — terminal/agent orchestration tool Andrew uses instead of Tmux for managing multiple agents.
- LlamaParse (Llama Index) — PDF-to-markdown parser Andrew switched to from Docling for speed/reliability.
- GPT-OSS-20B / Qwen 9B — local models Patrick uses for stable, low-token background tasks (e.g., Community Brain, Hermes-related jobs).
- Hermes — an agent/install system Scott is setting up for Patrick and later for Ryan as a personal assistant.
- ServiceNow — enterprise helpdesk platform Patrick's org plans to connect as a RAG knowledge source.
- Supabase — backend/Postgres database used by Scott's security dashboard, Ty's app stack, and referenced generally for hosting.
- Vercel / Next.js — hosting/frontend stack for Scott's security-review dashboard.
- Instantly — cold outreach/email warm-up tool used by Brandon's EMSO team for "minnow" leads.
- Loom — video recording tool used heavily for async sales outreach by Brandon, Morgan, and others.
- Even Realities smart glasses — AI-assisted prescription glasses with real-time transcription/cheat-code overlays, demoed by Brandon.
- Tesla (self-driving) — mentioned as enabling Brandon to multitask with agent sessions while driving.
- TTL.golf — Ty Wells' golf tee-time/organizing app (like Golf Now) demoed on the call.
- WhatsApp (as agent interface) — Ty's support/ERP pipeline monitors WhatsApp messages to trigger automated fixes.
- Telegram — used by Ty's system to send manual-approval prompts to himself.
- ChatGPT ads — newly available ad platform Brandon suggested for Ty's golf app player acquisition.
- Higgsfield CLI — video generation CLI integrated with Claude Code, used by Ryan for AI real estate video b-roll.
- Nanobanana — image generation model Ryan uses for stills before feeding into Seedance.
- Seedance — video generation model Ryan uses to animate stills (via Higgsfield CLI).
- Google Omni (aka Flow) — Google's motion graphics/video model recommended by Ryan/Biggi for advanced animated outputs.
- Remotion — programmatic video/animation framework mentioned by Ryan as complementary to Higgsfield/Omni.
- Claude Design — Anthropic tool Patrick recommended to Brandon for converting PowerPoint decks into interactive HTML slides.
- GSAP — animation library Ryan used for scroll-based website effects (e.g., private jet company redesign).
- CodeRabbit — competitor code-review tool discussed as a comparison point for Scott's security review system.
- WorkOS — enterprise auth/integration suggested by Patrick as a paid-tier feature for Scott's product.
- Zendesk — support tool Ty replaced with his own agent-driven WhatsApp pipeline.

## links

- https://class2curb.com/ / class2curb.ai — Morgan's (mdcatc) school pickup/dismissal SaaS product website, shared twice in chat.
- https://ttl.golf — Ty Wells' golf tee-time/organizer app, shared in chat.
- https://www.evenrealities.com/ — website for the smart glasses Brandon demoed.
- https://www.mdt.mt.gov/business/grants-ems.aspx — EMS grant program link Andrew shared for Brandon's EMSO business (Montana DOT grants page).
- https://github.com/openai/codex-plugin-cc — the official OpenAI Codex plugin for Claude Code, shared by Patrick.
- https://github.com/hopchouinard/patchoutech-plugins — Patrick's personal Claude plugin marketplace repo, source of his status line plugin.
- https://omnigent.ai/ — link shared by Patrick in chat (context: agent-related tool, tied to discussion of AI agent platforms).
- https://www.youtube.com/@BuildingwithReason — Scott Rippey's YouTube channel, plugged by Patrick as now on his weekly watch list.
- agent-task.com — Alireza's Agent Tax product domain, referenced during his demo.
- West GA __ EMSSOAP.mp4 — a Loom-style sales video file Brandon shared in chat for Biggi/Morgan to review as an example outreach video.

## decisions

- Alireza Mounesisohi will record/share demo videos of Agent Tax in action so Brandon and the group can better understand its use case and differentiation from plain Claude Code/Codex.
- Brandon Hancock will help promote Agent Tax by trying it out and giving feedback, once his own startup workload frees up.
- Ty Wells will follow up (had already begun) on his ERP/quoting system rollout and continue golf-course outreach for TTL.golf, leveraging his personal network of courses.
- Scott Rippey committed to considering building a freemium/plugin version of his CC security review tool to start market conversations and gather feedback, per Brandon's suggestion.
- Scott Rippey and Patrick discussed adding an enterprise governance/compliance rule layer to the security review tool.
- Juan Torres will send Brandon a promotional video of his AI photo-booth product once finished, for Brandon to share with a potential venue/event-rental partner contact.
- Morgan (mdcatc) will follow up with a contact (event rental equipment business owner in San Diego) that Morgan offered to introduce to Juan for potential partnership.
- Morgan will validate his cost/time-savings assumptions (salary vs. hourly staff) with real customers before finalizing Class2Curb's pricing pitch.
- Morgan committed to producing daily Loom outreach videos (3–5/day) before allowing himself to continue coding, following Brandon's/Dan Martell-style discipline suggestion.
- Ryan will email Brandon example real estate AI videos (to brandon@brandonhancock.com) so Brandon can show them to his sister (a US real estate agent) as a potential test case/lead.
- Ryan will draft a "good vs. bad" photo checklist/pamphlet concept for standardizing input photos from less-skilled photographers, to explore scaling his AI real estate video service into the US market.
- Patrick Chouinard will send Brandon the link to his Codex-review plugin and status line plugin repo.
- Brandon Hancock will try Claude Design to convert his PowerPoint sales presentations into interactive HTML slides, per Patrick's recommendation.
- Brandon Hancock will finish recording several outstanding outreach Looms immediately following the call.