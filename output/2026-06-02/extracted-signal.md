## general

This was a community coaching call for an AI/development group, hosted by Patrick Chouinard in place of the regular host (Brandon Hancock), who is on a hiatus working on an EMS project. Patrick and Paul Miller have been covering the weekly calls while Brandon attends once per month. The session had a relatively small attendance and moved through a mix of project updates, technical Q&A, and open discussion.

The main technical threads of the call were: the use of `/goal` (slash goal) agentic coding loops and how to use them effectively with PRDs and validation criteria; a comparison of Claude vs. Codex for different tasks; Patrick's ongoing project to use Hermes as a home lab DevOps/network operator agent; and Dmitry Avramenko's update on landing a major bank contract using his Evonix SDLC agent system to build an agentic AML platform. The call also touched on Proxmox home lab setup, token efficiency tools, and the broader question of deploying agents in corporate/regulated environments.

A significant portion of the latter half of the call was devoted to a nuanced discussion about agents vs. skills vs. deterministic code in production settings, with contributions from Patrick, Dmitry, Bastian, and Maksym. The consensus was that most business users actually need skills and deterministic workflows rather than true agents, and that ROI justification and token cost traceability are becoming critical concerns in enterprise AI deployments.

Ryan (One Stop Creative Agency) shared updates on a retail screen software business, SEO page generation, and several web/e-commerce projects. Rod Morrison discussed using Claude Code for data science rapid prototyping and forensic infrastructure analysis. Maksym Liamin described his automotive SaaS serving major brands in Latin America. Elijah Stambaugh discussed his approach to AI consulting engagements, focusing on human-in-the-loop workflows and business process analysis before introducing agentic tooling.

## insights

- **Slash `/goal` requires a verifiable success condition to be useful.** Without something quantifiable to validate against, it will consume tokens and produce nothing meaningful. (Patrick Chouinard, Bastian Venegas Arevalo)
- **`/goal` is best suited for small, well-scoped tasks with deterministic outputs** — e.g., building a single tool, a calculation with a numeric target — not large multi-feature applications.
- **Claude is imaginative and produces good UI/UX; Codex behaves like a senior engineer** — clean code, strong validation, but poor visual output. Use them together. (Patrick, Ola Oyo, Adam)
- **Most business users who say they want an "agent" actually want a skill or a simple workflow.** True agents determine their own next step, which is unpredictable and hard to control. (Patrick, Bastian)
- **Skills are the atomic unit; agents are orchestrators of skills.** Each agent profile should have only the skills it needs for its specific role — no universal skill libraries in production. (Patrick, Dmitry)
- **MCP servers consume significant context window on startup.** Three to five MCP servers can consume ~20% of context before any work begins. Minimize them aggressively. (Dmitry)
- **Deterministic Python/Chromium code is often preferable to agentic web browsing** for scraping regulatory sites — more reliable, cheaper, and easier to maintain when sites change. (Dmitry)
- **Token cost unpredictability is a growing enterprise problem.** Model updates (e.g., Opus 4.6 → 4.7) can silently increase costs 2–3× for the same workload. ROI justification is becoming mandatory. (Dmitry)
- **Hermes and OpenClaw are development/learning tools, not enterprise-deployable products** — especially not in regulated environments like banking. Singapore government has issued warnings about giving these tools identity-level permissions. (Dmitry, Patrick)
- **Tokonomics — per-step cost tracing in agentic workflows — will become a requirement** for enterprise AI deployments as organizations demand ROI proof. (Dmitry)
- **Local LLMs are viable for personal assistant use cases** (Qwen-4, Qwen-3, Gemma-4) but context window limitations (8–12k) make them impractical for application development today. (Patrick)
- **When building for corporate clients, go to the actual end users, not just the decision-makers**, to understand day-to-day problems. Directors describe what they think they want; workers show what they actually need. (Maksym)
- **Elon Musk's "algorithm" applied to AI:** Make requirements less dumb → Delete the step → Simplify → Accelerate → Automate last. (Maksym, citing Tesla process)
- **Teach users one layer at a time:** skills first, then once they understand why and how to call them, introduce agents that automate that orchestration. (Patrick)
- **LinkedIn thought leadership with AI-assisted writing can generate real enterprise leads.** Dmitry's AI-written posts (in Neal Stephenson's style) were read by a CIO contact who later became a client. (Dmitry)
- **Anthropic's new Claude Code Workflows feature mirrors what Dmitry built in Evonix** — deterministic workflow steps with adversarial multi-angle review. (Dmitry)
- **LLM calls within a single session can route through multiple cloud providers** (Amazon, Google TPUs, NVIDIA) — a major compliance concern for banks handling sensitive data. (Dmitry)

## qa

**Q (Juan Torres):** What are the best tools for end-to-end PRD execution — specifically `/goal`, Ralphie, and similar agentic loops?
**A (Patrick Chouinard):** `/goal` needs a highly detailed prompt with explicit validation criteria — the PRD alone is not enough. First use a prompt to analyze the PRD and generate ways to validate every requirement, then feed that to `/goal`. It works best for small, completable tasks, not large multi-feature applications. For visual/UI work, consider using skills instead.

**Q (Juan Torres):** What is GRILL with docs?
**A (Bastian Venegas Arevalo):** It's a skill by Matt Pocock. It reads your documents first, then asks clarifying questions to build a canonical dictionary of terms for the implementation. Install with `npx skills@latest`. Use `RequestUserInput` to get multi-choice questions instead of free-text answers to save tokens.

**Q (Ola Oyo):** What's your experience comparing Claude and Codex results?
**A (Patrick Chouinard / Ola Oyo / Adam):** Claude is imaginative and produces good UI/look-and-feel but can hallucinate and struggles to validate its own output. Codex behaves like a senior engineer — clean code, strong validation — but produces terrible UI. Best practice is to use both: Claude for creative/UI work, Codex for validation and code review.

**Q (Elijah Stambaugh):** What system do you use for building agents, and would you deploy Hermes in a production corporate environment?
**A (Dmitry Avramenko):** No — not Hermes, not OpenClaw, not in a regulated environment. These tools are for non-technical users and operate inefficiently with unknown security posture. Singapore government just warned against them. For production, build your own harness or use Claude Code directly. For corporate, the security review overhead for anything touching an LLM is enormous.

**Q (Rod Morrison):** Would `/goal` be useful for building standalone HTML prototypes with customer data?
**A (Patrick Chouinard):** Be careful — "pretty" is subjective and not a quantifiable validation target. `/goal` works well when the success criterion is numeric or binary (e.g., accuracy within a range). For data science tasks with measurable outputs, it's excellent. For visual presentation, use skills with templates instead.

**Q (Ola Oyo):** When Hermes orchestrates DevOps, does it modify infrastructure directly or use Infrastructure as Code?
**A (Patrick Chouinard):** Currently read-only/learning mode after ~1.5 weeks. When it does act, it can write Ansible scripts, Docker Compose files, or use N8N for orchestration. It also has SSH access internally. The harness is inspired by Codex so it has full capability, but write access is being introduced gradually.

**Q (Juan Torres):** How did Dmitry land the bank contract, and how do you break into banking?
**A (Dmitry Avramenko):** A combination of reconnecting with a former colleague who had become CIO-level, plus consistent LinkedIn presence with deeply researched AI posts (written by his LinkedIn agent in Neal Stephenson's style). Financial industry background was also essential. Being seen as a genuine thought leader — not just posting AI tips — made the difference.

**Q (Patrick Chouinard):** How do you think about agent scope — how big should an agent be, and how many skills are too many?
**A (Patrick Chouinard / Dmitry):** Skills are atomic. Each agent profile should have only the skills required for its specific role. A coordinating agent holds high-level routing skills; execution agents have the minimum permissions needed. MCP servers are expensive on context — avoid loading them unless necessary. From a security standpoint, disable write access unless explicitly required for the task.

## tools

- **Google ADK (Agent Development Kit) 2.0** — Ola Oyo asked about migrating from ADK 1.0; noted significant changes including graph-linear structure and database storage migration
- **Vertex AI** — mentioned in context of Google ADK migration; Google warned users about disconnection if not actively using it
- **Gemini Omni** — Patrick described it as Google's new multimodal video/audio/image/text generation tool, now powering video creation in Gemini; demonstrated at Google I/O keynote
- **Google Flow** — Ola Oyo shared link to `labs.google/fx/tools/flow` in chat as a related Google AI tool
- **Claude Code (Anthropic)** — primary coding harness used by most participants; discussed for `/goal`, skills, and agentic workflows
- **Codex (OpenAI)** — used as a senior-engineer-style validator and code reviewer; noted as superior to Claude for validation but poor at UI
- **/goal (slash goal)** — agentic coding loop available in Claude Code, Codex, Hermes, and others; discussed extensively for PRD execution
- **GRILL with Docs** — skill by Matt Pokok; reads documents and asks clarifying questions to build canonical implementation terminology; install via `npx skills@latest`
- **Hermes** — AI agent harness discussed as a personal/home-lab orchestrator; Patrick using it as DevOps/network operator; cautioned against enterprise deployment
- **OpenClaw** — mentioned as another agent harness; noted as less stable than Hermes; Singapore government warned against it
- **Cursor (with Composer 2.5/Kimi K2)** — Rod Morrison used Composer 2.5 to rebuild an executive dashboard; noted it consumed 51% of monthly quota for one task
- **Proxmox** — open-source virtualization platform Patrick uses for home lab; discussed as VMware alternative that remains free; supports VMs, LXC containers, CLI management
- **N8N** — internal workflow automation server Patrick uses; Hermes can leverage it for orchestration tasks
- **Prometheus + Grafana** — Patrick's monitoring stack for home lab; alerts feed into Hermes via internal listener
- **Ubiquiti** — networking equipment Patrick uses; noted improved API for home network appliances enabling agent integration
- **Supabase / Postgres** — mentioned as backend database options in Patrick's deployment decision logic for Hermes
- **Vercel** — mentioned as deployment target Hermes can push to for web apps
- **Discord** — Patrick uses private Discord server for infrastructure alerts from Hermes
- **RTK (Rust Token Killer)** — token efficiency tool Rod Morrison shared; claims 95% token savings; proxies OS commands; `rtk-ai.app`
- **DBOS** — workflow engine Dmitry is adopting for deterministic workflow steps in Evonix; mentioned as alternative to non-deterministic LLM-driven sequencing
- **LangFuse** — Dmitry switching to it for token cost tracing and Tokonomics (per-step cost attribution in agentic workflows)
- **Evonix (Avantix)** — Dmitry's own SDLC agent platform; used to build an agentic AML platform for a bank; features adversarial review, Technique Engine, deterministic workflows
- **Shipkit** — product by Brandon Hancock; questions about licensing/distribution directed to Brandon directly
- **Resend** — Ryan mentioned using it to build a custom email marketing backend (MailChimp alternative) for a taxi tour company
- **USPS shipping API** — Ryan integrating it into a US e-commerce platform for label generation
- **BigQuery / Cloud Run / GCP** — Rod Morrison used Claude to spider GCP infrastructure for forensic analysis of undocumented projects
- **Orgo.ai** — Elijah mentioned it; founder in San Francisco; builds on "computer use" philosophy with full Linux desktop/Chrome virtual machine
- **OpenAI Agents SDK** — Bastian shared in chat; updated to support skills and sandbox out of the box for Python and TypeScript
- **Pi (agent harness)** — Dmitry mentioned wanting to move to Pi from Claude Code; noted OpenAI subscription can be used within Pi
- **Cowork** — Patrick recommended as the first enterprise-appropriate agent deployment; noted for stability, auditing, and enterprise tooling
- **Shadcn** — referenced in Bastian's `intent-html-renderer` skill as a component library option
- **Excalidraw / Mermaid** — referenced in Bastian's shared skill set (`excalidraw-mermaid-safe`)

## links

- `https://labs.google/fx/tools/flow` — Google Flow AI tool, shared by Ola Oyo for Ryan re: video/creative tools
- `https://www.rtk-ai.app/` — RTK (Rust Token Killer) website, shared by Rod Morrison; token efficiency tool
- `https://github.com/rtk-ai/rtk` — RTK GitHub repository, shared by Rod Morrison
- `https://github.com/hopchouinard/community-brain-distribution` — Patrick's community brain RAG distribution repo; preliminary runtime with vector DB and config; operator/ingestion side still in development
- `https://www.dbos.dev/` — DBOS workflow engine, shared by Patrick in chat during Dmitry's discussion of deterministic workflows
- `https://www.youtube.com/watch?v=tK32trvj_b4&list=PLOXw6I10VTv9zUbhqqaT62O9AFjlndmjn&index=1` — Bastian shared: OpenAI updated Agents SDK for Python/TypeScript with skills and sandbox support
- `https://x.com/Teknium` — Bastian recommended following Teknium on X for updates on the Hermes model/harness
- `npx skills@latest add https://github.com/ranvier2d2/skills-share.git` — Bastian's skills repository; recommended skills include `goal-planner`, `codex-goal-planner-skill-orchestrator`, `excalidraw-mermaid-safe`, `semantic-image-director`, `intent-html-renderer`
- `https://neurosciencenews.com/ai-aphasia-llms-28956/` — Adam shared article comparing LLM limitations to aphasia/broken brain analogy
- `evonix-sdlc-agents.pdf` — Dmitry's PDF on his SDLC agent architecture, shared by Juan Torres in chat

## decisions

- **Patrick Chouinard** will continue developing Hermes as a home lab network operator/DevOps agent, gradually increasing its write access as it proves reliable in read-only/learning mode.
- **Patrick Chouinard** will package and de-personalize the community brain RAG project (removing home infrastructure dependencies) and publish it properly once family situation stabilizes; issues should be filed in the GitHub repo in the meantime.
- **Patrick Chouinard** will get back to the `.md → HTML` skill/project after focusing on Claude Code training for non-technical users.
- **Ty Wells** will record a demo video in advance for future calls when he is unavailable (e.g., on the golf course) so it can be played during the session.
- **Ty Wells** will update the group on his VC call (scheduled for Friday) at the next Tuesday session.
- **Bastian Venegas Arevalo** will share his HTML rendering skill repo publicly once he finishes wrapping up current work; shared install command in chat as a preview.
- **Ola Oyo** will reach out to Scott Rippey on the community platform for advice on Google ADK 2.0 migration.
- **Juan Torres** will look into Proxmox for his mini PC instead of dual-booting or buying old data center hardware.
- **Ryan (One Stop Creative Agency)** will investigate Gemini Omni for video production use cases.
- **Ryan (One Stop Creative Agency)** will return to the lead generation application project, which has been untouched for three weeks.
- **Dmitry Avramenko** will DM Maksym Liamin offline to discuss topics related to their respective projects.
- **Rod Morrison** will upgrade his data science team members beyond the $20 Cursor plan once the CRO confirms they are actively using the tools.