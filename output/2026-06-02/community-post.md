📝 SUMMARY

This week's call featured Patrick Chouinard hosting in Brandon Hancock's absence, delivering a mix of project updates, technical deep-dives, and enterprise AI strategy discussions. Key threads included maximizing slash goal loops for development tasks, the complementary strengths of Claude versus Codex, Patrick's Hermes home lab project, and Dmitry Avramenko's major bank contract win using the Evonix platform. A significant portion explored the critical distinction between agents, skills, and deterministic workflows in regulated corporate environments, with consensus that most business users actually need reliable skills rather than fully autonomous agents.

💡 KEY INSIGHTS

Slash /goal requires explicit, verifiable success conditions to avoid burning tokens on vague objectives. It excels at small, measurable tasks with numeric or binary validation targets, not large multi-feature builds.

Claude produces imaginative UI/UX but struggles with validation, while Codex behaves like a senior engineer with clean code and strong validation but poor visual output. The most effective approach combines both: Claude for creative work, Codex for code review and validation.

Most business users requesting an "agent" actually need a deterministic skill or workflow. True agents determine their own next steps, creating unpredictability that is difficult to control in production environments.

Skills should remain atomic and role-specific, with agents acting as orchestrators rather than universal toolboxes. Loading multiple MCP servers can consume roughly 20 percent of context window before work begins, so minimize them aggressively.

Token cost unpredictability represents a growing enterprise risk, as model updates can silently increase costs two to three times for identical workloads. Per-step cost tracing, or Tokonomics, is becoming mandatory for ROI justification.

Deterministic Python or Chromium code often outperforms agentic web browsing for scraping regulatory sites, offering greater reliability, lower cost, and easier maintenance when sites change.

Hermes, OpenClaw, and similar harnesses are valuable development and learning tools but are not suitable for enterprise deployment in regulated environments like banking due to security and permission concerns.

❓ KEY Q&A

Q: What are the best practices for using /goal with PRDs?
A: /goal requires more than just a PRD; it needs explicit validation criteria for every requirement. First analyze the PRD to generate quantifiable validation methods, then feed those to /goal. Reserve it for small, completable tasks with deterministic outputs rather than entire applications.

Q: How do Claude and Codex compare for development work?
A: Claude excels at imagination and UI/UX design but can hallucinate and fails at self-validation. Codex produces clean, senior-engineer-quality code with strong validation but generates poor visual interfaces. Use Claude for creative and frontend work, then employ Codex for validation and code review.

Q: Can Hermes or OpenClaw be deployed in production corporate environments?
A: No. These tools are designed for personal learning and home labs, not regulated enterprise settings. The Singapore government has issued warnings against granting such tools identity-level permissions. For production, build custom harnesses or use enterprise-grade solutions like Claude Code with proper security reviews.

Q: How do you land major contracts in regulated industries like banking?
A: Combine domain expertise with consistent thought leadership. Dmitry Avramenko secured a bank contract through a former colleague who became a CIO, plus a LinkedIn presence featuring deeply researched AI content written in a distinctive literary voice. Being perceived as a genuine industry thinker rather than simply posting AI tips made the critical difference.

Q: What is the ideal scope for an agent and how many skills should it have?
A: Skills are atomic units; agents are orchestrators. Each agent profile should contain only the skills required for its specific role. Avoid universal skill libraries in production. From a security standpoint, disable write access unless explicitly required for the specific task.

Q: What is GRILL with Docs?
A: It is a skill by Matt Pocock that reads your documents first, then asks clarifying questions to build a canonical dictionary of terms for implementation. Install with npx skills@latest. Use RequestUserInput to present multi-choice questions rather than free-text answers to conserve tokens.

🛠️ TOOLS AND CONCEPTS MENTIONED

/goal (slash goal): An agentic coding loop available in Claude Code, Codex, and Hermes that executes iterative tasks. Requires carefully defined validation criteria to be effective.

Claude Code versus Codex: Complementary AI coding harnesses. Claude is imaginative and UI-focused; Codex is validation-focused and senior-engineer-like. Best used together for creative and validation phases respectively.

GRILL with Docs: A skill by Matt Pocock that reads documents then asks clarifying questions to build a canonical dictionary of terms for implementation. Install via npx skills@latest.

Hermes: Patrick Chouinard's home lab DevOps and network operator agent harness. Currently in read-only learning mode for infrastructure management. Not recommended for enterprise deployment.

Evonix: Dmitry Avramenko's SDLC agent platform used to build agentic AML (anti-money laundering) systems for banking clients. Features adversarial review and deterministic workflow steps.

Proxmox: Open-source virtualization platform used for home labs as a free alternative to VMware, supporting VMs and LXC containers.

RTK (Rust Token Killer): Token efficiency tool claiming 95 percent savings by proxying OS commands. Available at rtk-ai.app.

DBOS: Workflow engine for creating deterministic, non-LLM-driven workflow steps as an alternative to purely agentic sequencing.

LangFuse: Tool for token cost tracing and Tokonomics, enabling per-step cost attribution in agentic workflows.

MCP servers: Model Context Protocol servers that consume significant context window on startup, often using 20 percent of available context before work begins.

Gemini Omni: Google's new multimodal video, audio, image, and text generation tool demonstrated at Google I/O.

Google ADK 2.0: Agent Development Kit with significant architectural changes from version 1.0, including graph-linear structure and database storage migration requirements.

Cowork: Recommended as the first enterprise-appropriate agent deployment option, noted for stability, auditing, and enterprise tooling.

📎 SHARED RESOURCES

labs.google/fx/tools/flow — Google Flow AI tool for creative workflows

rtk-ai.app — RTK (Rust Token Killer) token efficiency tool

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

Ryan will investigate Gemini Omni capabilities for video production use cases and resume work on the lead generation application that has been paused.

Ola Oyo will connect with Scott Rippey regarding Google ADK 2.0 migration strategies.

Dmitry Avramenko and Maksym Liamin plan to connect offline to discuss overlapping project interests.

Rod Morrison will upgrade his data science team's Cursor plans pending CRO confirmation of active usage.