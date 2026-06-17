## general

This was a weekly group coaching/check-in call hosted by Paul Miller, with regular participants Patrick Chouinard, Ty Wells, Ryan C, Juan Torres, and Morgan Cook. The session opened with personal notes — Patrick had recently lost his mother and shared how he used Claude to manage the administrative aftermath, compressing roughly two months of estate paperwork into 48 hours. Paul Miller also disclosed his father had passed three weeks prior. The group expressed condolences to both.

The primary technical throughline was the sudden unavailability of the "Fable" (referred to also as "Mythos") model from OpenAI, which had been a key tool for several members. Each participant did a round-robin update on what they were building and how they were coping without Fable. Alternatives discussed included using Claude Opus 4.8 combined with Codex/GPT-5.5, and the emerging "Fusion" architecture concept (ensembling multiple frontier LLMs) shared by Bastian Venegas Arevalo via OpenRouter's blog.

Individual project updates covered: Ryan C's AI-native CRM for UK estate agents (built initially with Fable, now iterated with Opus); Ty Wells's KindMark app — a positive-only character recognition platform; Patrick's AgentOps project — an operator-layer scaffolding on top of his Hermes agent, using NATS messaging, Prometheus, Grafana, Uptime Kuma, and Proxmox for home lab automation; Juan Torres's diffusion model experimentation for an AI photo booth application using WaveSpeed; and Morgan Cook's cemetery software project, stalled on county government timelines.

A recurring theme toward the end of the call was the danger of injecting AI into broken business processes — the consensus being that AI amplifies dysfunction rather than fixing it. Patrick shared his "adversarial system prompt" approach, which configures Claude to act as a challenging business analyst rather than an agreeable assistant, and posted the prompt text in the chat. Ty Wells also shared a novel "intent queue" workflow for preserving context across Claude Code sessions.

## insights

- **Patrick Chouinard:** Using Claude to process funeral home paperwork (scanned documents fed into a project) reduced two months of estate administration to 48 hours; Claude proactively searched government websites for additional required forms and benefits.
- **Patrick Chouinard:** Claude demonstrated unexpected emotional sensitivity in the bereavement context — pacing tasks, telling him when to stop for the night, and flagging only time-sensitive items.
- **Patrick Chouinard:** Keep systems as deterministic as possible; use AI decision-making only where absolutely necessary. Scaffolding development is where value will be for the next few years.
- **Patrick Chouinard:** For terminal/infrastructure/script work, GPT-5.5 (Codex) currently outperforms Claude Opus 4.8; Opus is superior for UI-backed application development.
- **Patrick Chouinard:** His most-requested deliverable is his adversarial system prompt — a short instruction set that makes Claude act as a devil's advocate, asking "what problem are you actually trying to solve?" rather than accepting stated solutions at face value. He places this in Claude.md at the user level so it applies to every session including Claude Code.
- **Patrick Chouinard:** People state their intended solution, not their actual problem. AI by default builds what it's told; an adversarial prompt forces proper problem articulation.
- **Morgan Cook:** If the underlying process is broken, AI amplifies the problem rather than solving it — it makes the dysfunction bigger and more visible, not fixed.
- **Paul Miller:** Combining Opus 4.8 (via Superpowers) with Codex 5.5 in parallel on the same project folder — pushing requirements documents back and forth between them — partially bridges the Fable gap, but does not recover the speed advantage Fable provided.
- **Ty Wells:** Built an "intent queue" system: uses Claude's `/by the way` background command to capture context-rich questions, stores responses locally, and surfaces them as a primed queue at the start of the next session — saving token spend on re-priming.
- **Ty Wells:** The intent queue costs slightly more tokens in the current session but saves tokens in subsequent sessions by eliminating re-priming overhead.
- **Ryan C:** RAG chunking strategy for transcripts differs fundamentally from file chunking — questions and answers can be separated by 30 minutes in a transcript, so a pre-processing pass to reconstruct Q&A into logical blocks is required before traditional chunking.
- **Patrick Chouinard:** Transcript RAG pre-processing is done via an N8N workflow that restructures content by topic/team before final chunking.
- **Patrick Chouinard:** Giving agents financial autonomy is unnecessary when a human is one Discord message away; agents should request funds rather than spend autonomously unless the volume justifies automation.
- **Ryan C:** When marketing a vertical SaaS, use the language your customers already understand (e.g., "CRM") even if the product is architecturally more like an operating system.
- **Patrick Chouinard:** Concern about Fable-class models: over-reliance on highly autonomous models may atrophy the user's own intentional thinking — "intention is a muscle, if you don't practice it, you'll lose it."

## qa

**Q (Juan Torres):** What's the differentiator of Ryan's CRM application versus other CRMs?
**A (Ryan C):** It's AI-native rather than bolt-on: an aggregated inbox pulls all communication channels (email, WhatsApp via Meta API, Rightmove/Zoopla portals), auto-drafts responses, learns from edits and rejections, builds a per-property and per-contact knowledge base via RAG, and integrates prop-tech data APIs for proactive outreach (e.g., sending letters to neighbouring properties after a sale). Most existing CRMs either lack a full API or require users to work through a chat window that runs out of context.

**Q (Juan Torres):** Did Ryan use a RAG methodology similar to Patrick's transcript chunking?
**A (Patrick Chouinard):** The key difference is what's being chunked. Transcripts require a pre-processing pass to reconstruct Q&A pairs that may be separated by 30 minutes before traditional chunking; otherwise retrieval quality degrades. Patrick does this restructuring in an N8N workflow before final chunking.

**Q (Juan Torres):** Have you thought about giving your agents a small credit account (e.g., $200) to spend autonomously?
**A (Patrick Chouinard):** Not for the current home lab context — everything the agent needs (spinning up servers, etc.) is free on Proxmox. If it needs something that costs money, it sends a Discord message and Patrick approves in 30 seconds. He's not opposed to agent spending in principle, just not where a human approval loop is trivially fast.

**Q (Paul Miller):** How are you ranking the quality of image output from different diffusion models?
**A (Juan Torres):** Currently qualitative only — A/B testing specific images with specific prompts and assessing aesthetics manually. He's aware of CLIP as a scoring model but found commercially available diffusion models good enough that heavy pipeline engineering wasn't needed. FinOps tooling in his web app will eventually quantify per-model cost per event once deployed.

**Q (Paul Miller):** Are you seeing clients who expect AI to solve broken business logic problems?
**A (Patrick Chouinard / Morgan Cook):** Universally yes. Patrick: the more AI injected, the less natural intelligence remains. Morgan: AI amplifies a broken process, it doesn't fix it. Patrick's mitigation is his adversarial system prompt that forces clients to articulate the actual problem rather than a presumed solution.

**Q (Paul Miller):** Who is the "bigger" (more confrontational) model — Claude or OpenAI?
**A (Patrick Chouinard):** Claude, when prompted correctly, will tell you directly that something is a bad idea. OpenAI tends toward sassy rather than genuinely confrontational. Claude can be configured to say "nope, that's dumb" in a way that's actually useful for business analysis.

## tools

- **Claude (Anthropic)** — Primary coding and reasoning assistant; used for estate administration, application development, and adversarial business analysis via custom system prompt.
- **Claude Code** — Agentic coding environment; used by Patrick, Ty, Ryan, and others for iterative development; Bastian noted that changing reasoning effort mid-run invalidates the cache.
- **Codex / GPT-5.5 (OpenAI)** — Used for terminal/infrastructure/script work and adversarial code review; Patrick rates it above Opus for CLI tasks.
- **Hermes** — Patrick's custom agent scaffolding; AgentOps is being built on top of it.
- **AgentOps** — Patrick's in-progress operator-layer scaffolding giving Hermes a "nervous system" via NATS messaging and monitoring tools.
- **NATS** — Open-source messaging platform; used as the message bus centralising signals from monitoring tools to Hermes.
- **Uptime Kuma** — Open-source uptime monitoring; feeds alerts into NATS for AgentOps.
- **Prometheus** — Metrics collection; part of Patrick's home lab monitoring stack feeding AgentOps.
- **Grafana** — Visualisation/alerting; part of Patrick's monitoring stack.
- **Alert Manager** — Alerting component integrated into AgentOps via NATS.
- **Proxmox** — Home lab hypervisor; Hermes can spin up VMs without needing to spend money externally.
- **Authentik** — Open-source identity/authentication provider; used for internal auth in AgentOps.
- **Infisical** — Lightweight open-source secrets manager (described as an alternative to HashiCorp Vault); used for API key and secret management in AgentOps.
- **N8N** — Workflow automation; Patrick uses it to pre-process transcripts before RAG chunking.
- **WaveSpeed AI (wavespeed.ai)** — GPU inference provider for diffusion models; Juan uses it for image generation experimentation without owning GPUs.
- **Higgsfield** — AI image/video generation platform; Ryan used its MCP integration with Claude Code to pull imagery directly into his CRM project.
- **Remotion** — Programmatic video generation; Ryan plans to use it for tutorial content in his CRM.
- **Twenty (twenty.com)** — Open-source CRM (positioned as a Salesforce replacement); Paul mentioned it as a reference architecture with MCP/CLI support.
- **OpenRouter** — LLM routing platform; Bastian shared their "Fusion" blog post about ensembling frontier models; Juan uses it primarily for LLMs.
- **Superpowers** — Tool Paul uses alongside Opus 4.8 for requirements document generation; outputs are cross-validated with Codex.
- **Fathom** — AI meeting notetaker present in the session (noted in chat log).
- **Fireflies.ai** — AI meeting recorder/notetaker also present in the session (noted in chat log).
- **Vanta.js** — JavaScript 3D animation library; Juan uses the Halo effect for his photo booth front end.
- **HuggingFace** — Model/LoRA repository; Juan references it for sourcing community LoRAs for diffusion models.
- **KindMark (kindmark.app)** — Ty's own project; positive character-recognition platform for service workers.
- **ShipSafe** — Ty mentioned this (from a prior session) as an agent payment/token recharge system for giving agents spending capacity.

## links

- **https://kindmark.app** — Ty Wells's KindMark app (live demo link shared in chat).
- **https://openrouter.ai/blog/announcements/fusion-beats-frontier/** — Bastian's link to OpenRouter's "Fusion beats frontier" blog post on ensembling multiple LLMs.
- **https://twenty.com/** — Open-source CRM project Paul recommended to Ryan as a reference/foundation.
- **https://www.linkedin.com/posts/brandon-hancock-ai_your-most-valuable-company-knowledge-is-locked-share-7460739158110748672-hISO/** — Patrick's LinkedIn post linking to his podcast episode with Brandon Hancock on RAG and knowledge management.
- **https://app.fireflies.ai/live/01KV46SBKP8RR716VW8FP6CFEZ?ref=live_chat** — Fireflies.ai real-time notes link for this session (auto-posted by the bot).
- **https://wavespeed.ai** — WaveSpeed AI inference platform shared by Juan Torres for diffusion model experimentation.

## decisions

- **Ty Wells** will post his "intent queue" concept plan and implementation write-up to the school/community board for others to use.
- **Patrick Chouinard** will continue developing AgentOps over the next couple of weeks and will publish it publicly once it is secured and stable (not in its current half-built state).
- **Juan Torres** will meet with his collaborator to plan the AI photo booth pilot deployment, targeting a go-live this weekend or the following weekend.
- **Paul Miller** will add a Claude "adversarial/bitchy" entity (using Patrick's system prompt) to his virtual project team to challenge a current client engagement.
- **Ryan C** will watch Patrick's podcast with Brandon Hancock on RAG/chunking methodology.
- **Bastian Venegas Arevalo** asked the group to try the Fusion architecture approach and discuss it at the next meeting; Paul Miller agreed to cover it in the go-around.
- **Group** agreed to reconvene the following Wednesday.