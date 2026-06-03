📝 SUMMARY

Patrick Chouinard hosted this week's call, covering project updates, technical deep-dives, and enterprise AI strategy. Key discussions included maximizing slash goal loops, Claude versus Codex strengths, Patrick's Hermes home lab, and Dmitry Avramenko's major bank contract win using Evonix. A critical theme was the distinction between agents, skills, and deterministic workflows in regulated environments, with consensus that business users typically need reliable skills rather than fully autonomous agents.

💡 KEY INSIGHTS

Slash /goal requires explicit, verifiable success conditions and excels at small, measurable tasks with numeric or binary validation, not large multi-feature builds.

Claude delivers imaginative UI/UX but struggles with validation, while Codex behaves like a senior engineer with clean code and strong validation but poor visuals. Combine both: Claude for creative work, Codex for validation.

Most business users requesting an "agent" actually need a deterministic skill or workflow. True agents determine their own next steps, creating unpredictability that is difficult to control in production.

Skills should remain atomic and role-specific, with agents as orchestrators rather than universal toolboxes. Loading multiple MCP servers can consume roughly 20 percent of context window before work begins, so minimize them aggressively.

Token cost unpredictability represents a growing enterprise risk, as model updates can silently increase costs 2-3x for identical workloads. Per-step cost tracing (Tokonomics) is becoming mandatory for ROI justification.

Deterministic Python or Chromium code often outperforms agentic web browsing for scraping regulatory sites, offering greater reliability, lower cost, and easier maintenance.

Hermes, OpenClaw, and similar harnesses are valuable for development and learning but unsuitable for enterprise deployment in regulated environments due to security concerns.

❓ KEY Q&A

Q: What are the best practices for using /goal with PRDs?
A: /goal requires explicit validation criteria for every requirement, not just the PRD. Analyze the PRD to generate quantifiable validation methods, then feed those to /goal. Reserve it for small, completable tasks with deterministic outputs.

Q: How do Claude and Codex compare for development work?
A: Claude excels at imagination and UI/UX but hallucinates and fails at self-validation. Codex produces clean, senior-engineer-quality code with strong validation but generates poor visual interfaces. Use Claude for creative and frontend work, Codex for validation and review.

Q: Can Hermes or OpenClaw be deployed in production corporate environments?
A: No. These tools are designed for personal learning and home labs. The Singapore government has issued warnings against granting such tools identity-level permissions. For production, build custom harnesses or use enterprise-grade solutions like Claude Code with proper security reviews.

Q: How do you land major contracts in regulated industries like banking?
A: Combine domain expertise with consistent thought leadership. Dmitry Avramenko secured a bank contract through a former colleague who became a CIO, plus a LinkedIn presence featuring deeply researched AI content in a distinctive literary voice. Being perceived as a genuine industry thinker rather than simply posting AI tips made the critical difference.

Q: What is the ideal scope for an agent and how many skills should it have?
A: Skills are atomic units; agents are orchestrators. Each agent profile should contain only the skills required for its specific role. Avoid universal skill libraries in production. Disable write access unless explicitly required.

Q: What is GRILL with Docs?
A: A skill by Matt Pocock that reads your documents first, then asks clarifying questions to build a canonical dictionary of terms. Install with npx skills@latest. Use RequestUserInput to present multi-choice questions rather than free-text answers to conserve tokens.

🛠️ TOOLS AND CONCEPTS MENTIONED

/goal: An agentic coding loop in Claude Code, Codex, and Hermes requiring carefully defined validation criteria.

Claude Code versus Codex: Complementary harnesses. Claude is imaginative and UI-focused; Codex is validation-focused and senior-engineer-like. Best used together.

GRILL with Docs: Skill by Matt Pocock that reads documents then asks clarifying questions to build a canonical dictionary. Install via npx skills@latest.

Hermes: Patrick Chouinard's home lab DevOps and network operator agent harness. Currently in read-only learning mode. Not recommended for enterprise deployment.

Evonix: Dmitry Avramenko's SDLC agent platform used to build agentic AML systems for banking clients. Features adversarial review and deterministic workflow steps.

Proxmox: Open-source virtualization platform for home labs, supporting VMs and LXC containers.

RTK (Rust Token Killer): Token efficiency tool claiming 95 percent savings by proxying OS commands. Available at rtk-ai.app.

DBOS: Workflow engine for creating deterministic, non-LLM-driven workflow steps as an alternative to purely agentic sequencing.

LangFuse: Tool for token cost tracing and Tokonomics, enabling per-step cost attribution.

MCP servers: Model Context Protocol servers that consume significant context window on startup, often using 20 percent of available context before work begins.

Gemini Omni: Google's new multimodal video, audio, image, and text generation tool.

Google ADK 2.0: Agent Development Kit with significant architectural changes from version 1.0, including graph-linear structure and database storage migration requirements.

Cowork: Recommended as the first enterprise-appropriate agent deployment option, noted for stability, auditing, and enterprise tooling.

📎 SHARED RESOURCES

labs.google/fx/tools/flow — Google Flow AI tool for creative workflows

rtk-ai.app — RTK token efficiency tool

github.com/rtk-ai/rtk — RTK GitHub repository

github.com/hopchouinard/community-brain-distribution — Patrick's community brain RAG distribution repository (preliminary runtime with vector DB)

dbos.dev — DBOS workflow engine for deterministic steps

youtube.com/watch?v=tK32trvj_b4 — OpenAI updated Agents SDK for Python and TypeScript with skills and sandbox support

npx skills@latest add https://github.com/ranvier2d2/skills-share.git — Bastian's skills repository including goal-planner, codex-goal-planner-skill-orchestrator, and excalidraw-mermaid-safe

neurosciencenews.com/ai-aphasia-llms-28956 — Article comparing LLM limitations to aphasia and broken brain analogies

x.com/Teknium — Recommended follow for updates on Hermes model and harness

🔄 FOLLOW-UPS WORTH EXPLORING

Patrick Chouinard will package and publish a de-personalized version of the community brain RAG project, removing home infrastructure dependencies, once personal circumstances stabilize.

Ty Wells will update the group on his scheduled VC call and has committed to pre-recording demo videos when unable to attend live.

Bastian Venegas Arevalo will publicly share his HTML rendering skill repository upon completing current work commitments.

Ryan will investigate Gemini Omni capabilities for video production use cases and resume work on the paused lead generation application.

Ola Oyo will connect with Scott Rippey regarding Google ADK 2.0 migration strategies.

Dmitry Avramenko and Maksym Liamin plan to connect offline to discuss overlapping project interests.

Rod Morrison will upgrade his data science team's Cursor plans pending CRO confirmation of active usage.