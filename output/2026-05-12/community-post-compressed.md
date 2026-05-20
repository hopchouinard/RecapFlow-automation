📝 SUMMARY

This week's call covered agentic development workflows including dual-AI validation, full-stack testing innovations, and regulatory SDLC requirements. Patrick Chouinard shared red-team strategies using Claude Code alongside OpenAI Codex for adversarial validation, plus updates on a community RAG system. Ty Wells demoed a user feedback hub and Isotope testing framework, while Morgan Cook showcased a digital signage engine and Elena presented a multi-cloud disaster recovery agent. The session wrapped with deep Q&A on Claude Code architecture, email automation safety guardrails, and targeting the right customer segment for AI consulting.

💡 KEY INSIGHTS

Red-team across providers. Validate Claude Code output using OpenAI Codex (or vice versa) rather than the same model. Different biases mean flaws invisible to one may be caught by the other.

Codex as adversarial harness. Prompt Codex to "destroy the application" when reviewing Claude Code output, then feed failure reports back for remediation. Codex subscriptions include GPT Image 2, useful for agentic image generation without separate API costs.

Security hygiene for AI skills. Avoid downloading skills from external repositories due to supply chain risks. Instead, use Claude Code's built-in skill creator to generate skills from completed work, or recreate them from reference.

Agent design principles. Split agent responsibilities by context and single goals rather than human work logic. Giving one agent opposing objectives creates instability. It is acceptable for agents to have uneven workloads.

Code generation vs artifact generation. When accuracy matters (like drawing precise graphics), ask AI to write code that generates the artifact rather than generating the artifact directly. AI evaluates code correctness better than visual correctness.

Process before automation. AI amplifies broken processes. Clean up workflows before adding AI, then convert stable processes to deterministic scripts that run without AI for speed and reliability.

Vertical slicing. Build features end-to-end (back to front) rather than completing all database work before UI work. This confirms connectivity early and surfaces integration issues before wasting tokens.

Forced adoption tactics. Intentionally leave known bugs in ERP replacements to prevent employees from defaulting back to the legacy system while it remains available.

Claude Code power commands. Use /goal for long-running autonomous tasks that iterate until testable outcomes (watch token consumption), and /insights to analyze your usage patterns and workflow efficiency.

Superpower plugin workflow. Covers full SDLC from brainstorming to code review, available in the Anthropic marketplace for Claude Code, Codex, and GitHub Copilot.

Consulting target market. Medium-sized companies scaling rapidly represent the sweet spot for AI consulting. Large enterprises default to PwC/Deloitte; startups lack budget. Frontline employees who know exactly what is broken are more valuable for AI adoption than top-down framework mandates.

❓ KEY Q&A

Q: Have you compared Plan mode between Codex and Claude?
A: I do not use native plan mode — I use the Superpower plugin's "brainstorming" feature instead. It goes deeper than standard Plan Mode without the token consumption of Ultra Plan, and works in both tools.

Q: I thought I saw a video on running Claude inside of Codex — you said you are running them separately?
A: It is actually Codex inside Claude via a plugin, but limited to specific tasks like adversarial review. I built a complete separate harness that runs them as distinct validation layers at every SDLC step.

Q: What is your differentiator between your digital signage app and the vast majority of digital wall applications?
A: Garbage in, beauty out. The system takes any raw input — even a photo of a paper poster — and automatically reformats it into beautiful, animated slides with QR codes and countdown timers without manual design work.

Q: Are you deploying the Fire Stick app directly to the device, through ADB, or putting something in the Amazon store?
A: Direct to device was the plan, but newer Fire Stick models (beyond plain HD) block sideloading. You will need to publish to the Amazon Appstore, and avoid using "Fire" in the product name or Amazon will require notarized documents and may still block approval.

Q: Is there any recommendation on tools for building a social media content automation pipeline?
A: Consider the Claude Agent SDK rather than a standalone Python app. Since the workflow is multi-step with approvals, use it as a full agent. For one-shot tasks, any inference platform works.

Q: How have you configured your email agent?
A: I do not fully automate replies — the 0.1% failure risk is too high. I feed emails to Claude via mailbox connectors, add context, and have it draft replies. I write my raw response and Claude reformulates it to be politically correct while preserving the message.

Q: How do you use project tracking alongside AI-assisted development?
A: We use Jira with Superpower on top. Requests split into independent vertical work streams, then flow through brainstorming → spec → implementation plan → sub-agent implementation, with Codex validation at each phase. Jira updates automatically via the Atlassian MCP server.

Q: For the disaster recovery tool, is the ideal customer enterprise or startup?
A: Medium-sized companies making the jump to enterprise infrastructure. Large enterprises use Deloitte/PwC; startups lack budget.

Q: What is a Claude Code agent, and how does the sub-agent model work?
A: A Claude Code session is itself an agent. During implementation, it spawns sub-agents — separate processes with fresh context windows inheriting only necessary context. This keeps the main window clean and each sub-agent focused. Skills and MCP connectors are available to all agents.

Q: Where can I find good templates or starting points for skills?
A: Do not download from external sources due to supply chain risks. Use the built-in skill creator: after completing a process, tell Claude Code "look at what we just did and create a skill from it." It generates proper structure and syntax.

Q: Can Playwright MCP run tests against a locally running app?
A: Yes. Install the Playwright MCP server, provide the localhost URL, and Claude can instruct it to spawn a browser, navigate, and execute tests locally without manual intervention.

🛠️ TOOLS AND CONCEPTS MENTIONED

Claude Code — Primary agentic coding harness for spec-driven development and sub-agent spawning.

OpenAI Codex — Used as parallel validation/red-teaming layer against Claude Code; includes GPT Image 2 in its subscription.

Superpower — Plugin covering full SDLC (brainstorming, spec, implementation, code review) available in the Anthropic marketplace for Claude Code, Codex, and GitHub Copilot.

Isotope — Ty Wells's testing package capturing UI screenshots, database state before/after, and endpoint logs for full-stack visibility.

MCP (Model Context Protocol) — Connectors enabling Claude to interact with external systems (AWS, GCP, Atlassian, Playwright).

Playwright MCP — Allows Claude to spawn browsers and execute UI tests against local or remote applications.

Skills — Reusable capabilities stored in .claude/skills folder, invoked via natural language context rather than explicit commands.

/goal command — Claude Code feature for long-running autonomous tasks that iterate until testable outcomes are achieved.

/insights command — Generates usage reports and workflow improvement suggestions for Claude Code.

AWS Bedrock and Strands — Powering Elena's multi-cloud disaster recovery agent system.

Vertical slicing — Development approach building features end-to-end rather than layering horizontally.

Red-teaming — Adversarial validation using competing AI systems to expose flaws.

📎 SHARED RESOURCES

crowdpics.ai — Ty Wells's digital signage product.

deepseek-claude-code.vercel.app — Instructions for routing Claude Code to DeepSeek as a fallback when Claude is unavailable.

github.com/obra/superpowers — Superpower plugin repository.

fathom.video/customize — Fathom AI notetaker settings.

🔄 FOLLOW-UPS WORTH EXPLORING

Patrick finalizing the community brain RAG system packaging for agent-assisted deployment, including source material and pre-chunked data.

Evaluating security skill repositories from established security companies for community reference while maintaining supply chain safety.

Ty packaging Isotope for broader community reuse across projects.

Morgan sourcing older Amazon Fire Stick HD units via eBay before sideloading capability disappears from newer models.

Hemal prototyping social media automation using Claude Agent SDK versus building a standalone Python application.

Elena integrating Superpower into her workflow and refining DR system cost estimation accuracy.

Connection between Ty and Elijah regarding custom ERP replacement strategies and technical stack details.