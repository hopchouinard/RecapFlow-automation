## general

This was a weekly group coaching/community call hosted by Patrick Chouinard, standing in for the regular host Brendan who was traveling in Japan. Patrick ran the session as a round-robin update format where each participant shared what they had been working on and fielded questions from the group. The call covered a wide range of AI-assisted development topics including tool selection, platform comparisons, and individual project progress.

Key themes included the Claude Code vs. Cursor debate, ShipKit template usage, and how non-technical founders can best leverage AI development tools. Several participants were building SaaS products or internal tools using AI-assisted coding workflows, and the group exchanged practical advice on architecture, package management, and IDE configuration.

Patrick also demoed his own personal "Career Knowledge Graph" project — a RAG-backed application that decomposes a CV into structured entities stored in a vector database, enabling dynamic CV regeneration tailored to specific job descriptions or RFPs. This sparked broader discussion about second-brain concepts, vector stores, and agentic background processing using Claude Code.

The session closed with reminders that Brendan would also be absent the following week, with Patrick hosting again before Brendan's return.

## insights

- Patrick (quoting his work context): Tying an enterprise to a single AI platform for an extended period is too risky right now; a mixture of providers is more prudent.
- Patrick: AI doesn't replace headcount — it multiplies it. A team of 3–4 people with AI can do what 20 people did before, but you still need each role (developer, evangelist, etc.).
- Garron: Non-technical founders with domain expertise should focus on being the evangelist and product visionary, not the coder — the learning curve to build production-quality software is too steep relative to the opportunity cost.
- Prem: ShipKit enabled him to launch his first SaaS application in three months; without it the timeline would have been far longer.
- Paul: Working outside ShipKit's guardrails quickly revealed how much the framework's rules were keeping development on track — basic issues multiplied without them.
- Patrick: When combining RAG and chat functionality, start from the more complex template (RAG) and add simpler features on top, rather than the reverse.
- Patrick: For IDE/tool selection, Claude Code's rolling 5-hour usage window is more forgiving for beginners than Cursor's fixed monthly cap, which resets only at month-end.
- Patrick: The Claude Code VS Code/Cursor extension lacks feature parity with the terminal version — multi-agent scenarios in particular require the terminal.
- Patrick: Including official documentation repos as Git submodules inside a project lets Claude always reference the latest docs without relying on external services like Context7 (which is better suited for API references).
- Patrick: Claude Code can be run headless as a background task processor for local automation — useful as a lightweight alternative to spinning up an EC2 instance for DevOps scripting.
- Ryan: Using a third-party social scheduling API (Postbone/Publer) as a middleware layer insulates an app from frequent direct API changes by Meta and other platforms.
- Morgan: Mixing package managers (npm and pnpm) in the same project creates conflicting lock files and dependency resolution errors — pick one and document it explicitly in the package file.
- Patrick: For a vector database to be genuinely useful, the hard work is designing the entity taxonomy, metadata, and filtering logic — that thinking is where the real value lies, regardless of the tool used.

## qa

**Q (Lan):** If I want to build an application with both chat and RAG functionality, should I use both ShipKit templates or just one?
**A (Patrick Chouinard):** Start from the more complex template — RAG — because it already includes basic chat functionality. Then add features like multi-model support on top. The key is to front-load as much intent and context as possible in your first prompt when defining the application.

**Q (Lan):** I use Anti-Gravity IDE. Can I copy the agent setup from the Claude agents template directly into Anti-Gravity, or should I switch tools?
**A (Patrick Chouinard):** The Cursor template is the closest fit since Anti-Gravity is a VS Code fork. You can use Claude Code in Anti-Gravity's terminal and get full Claude Code functionality that way. Build your markdown/planning artifacts with Claude Code in the terminal, then use Anti-Gravity for editing and debugging on top of what Claude Code produces.

**Q (Lan):** Should I use Claude Code in the terminal or the VS Code/Anti-Gravity extension?
**A (Patrick Chouinard / Ryan):** The extension is fine for basic scenarios but lacks feature parity — multi-agent workflows break in the extension. For anything involving multiple agents, use the terminal. Ryan confirmed his 16-agent setup would not work in the extension.

**Q (Lan):** Does the email for the IDE need to match the GitHub email for ShipKit?
**A (Patrick Chouinard):** Yes, for ShipKit they need to match.

**Q (Hemal Shah):** What is the advantage of Claude Code over using Cursor directly, beyond cost?
**A (Patrick Chouinard):** The scaffolding inside Claude Code is more advanced — the number of subagents it can manage simultaneously, custom commands, and skills system are ahead of what Cursor currently offers. Cursor is catching up, but Claude Code is the most complete agentic environment right now.

**Q (Jake Maymar):** Is there a way to expose local Claude Code processing to a web application, e.g., via ngrok?
**A (Patrick Chouinard):** You could, but it becomes a security concern and requires building your own agent scaffolding. For local background processing it works well headless. NetworkChuck has a YouTube video showing Claude Code integrated into an N8N workflow for this kind of messaging/task pattern.

**Q (Juan Torres):** Would using an EC2 instance as an IAM-privileged "oracle" to control AWS CLI resource creation be a good architecture for agentic cloud management?
**A (Prem / Patrick Chouinard):** Avoid adding an EC2 just for this — it introduces another layer requiring patching and management. Instead, wrap the needed AWS CLI commands as Claude skills, give them to a local agent, and run it as a headless Claude Code process or cron job. Paul added that Boto and AWS CLI control language can be used to build a dashboard/agent that manages spinning resources up and down.

**Q (Prem):** What is the difference between your documentation submodule approach and using Context7 as an MCP?
**A (Patrick Chouinard):** Context7 is best for API references to existing systems. The submodule approach is for building *on top of* a tool (e.g., Claude Code, ShipKit, SpecKit) — you include the tool's own documentation repo as a Git submodule, and an agent keeps it updated on project load so you always have the latest docs. You then instruct Claude to build according to those docs and best practices.

## tools

- **Claude Code** — Primary agentic coding tool; discussed for terminal use, headless background processing, multi-agent workflows, and cost model (rolling 5-hour window).
- **Cursor** — IDE used by several participants alongside Claude Code; discussed re: monthly token cap and extension limitations.
- **Anti-Gravity** — VS Code fork IDE used by Lan and mentioned by Brendan; discussed re: ShipKit template compatibility.
- **ShipKit** — Brandon's project template/framework; referenced as the foundation multiple participants used to launch SaaS apps faster.
- **Claude Code VS Code Extension** — GUI overlay for Claude Code within IDEs; noted as lacking full feature parity, especially for multi-agent use.
- **Open Router** — Multi-model API router; Patrick integrated it into his Career Knowledge Graph app to support multiple models.
- **Google AI Studio** — Garron used it to mock up a prototype of his real estate coaching app.
- **AWS Rekognition** — Ryan integrated it for facial recognition in his social media automation app to tag team members in uploaded photos.
- **Postbone** — Social media scheduling API middleware; Ryan's original integration layer to avoid direct Meta API management.
- **Publer** — Replacement/addition to Postbone; allows longer post lengths and custom thumbnail uploads for Reels.
- **Trigger.dev** — Morgan mentioned wanting to test its agent workflow capabilities for a project.
- **N8N** — Workflow automation tool; Patrick referenced a NetworkChuck video showing Claude Code integrated into an N8N pipeline.
- **Vercel AI SDK** — Mentioned by Hemal as what Brandon uses in some ShipKit projects; noted as a starting point for chatbot templates.
- **Granola** — AI note-taking tool; Ryan used it to record a 75-question client onboarding session.
- **Limitless** — AI wearable/recording device; Patrick noted it was acquired by Meta with ~1 year of service remaining.
- **Starlink** — Garron mentioned connectivity issues while traveling in Mexico in a van.
- **GitHub Actions** — Patrick uses it in his Career Knowledge Graph project to build and deploy to Cloudflare.
- **Cloudflare** — Hosting target for Patrick's Astro static site generated from his Career Knowledge Graph backend.
- **Astro** — Static site framework Patrick is using for the public-facing personal website component of his project.
- **Context7 MCP** — API reference MCP server; Patrick contrasted it with his Git submodule documentation approach.
- **AWS CLI / Boto** — Discussed by Juan and Paul for agentic cloud resource management within a VPC.
- **Microsoft Copilot** — Marc mentioned his company uses the Microsoft (not GitHub) version.
- **Next.js 15/16** — Morgan asked if anyone had moved to Next.js 16 yet; group was still on 15.
- **pnpm / npm** — Package manager discussion; Morgan resolved a conflict caused by mixing both in one project.

## links

- No explicit URLs were shared in the transcript.

## decisions

- Patrick Chouinard will host the call again next week (Brendan still traveling).
- Garron Selliken will connect with Prem (and potentially others in the community) to explore a technical co-founder / partnership arrangement for his real estate CRM app.
- Prem will send Garron his email/contact details and share what he has built so far.
- Ty Wells committed to preparing a demo or "Christmas bonus" presentation for the following week's call.
- Paul Miller committed to sharing a demo of his Travelling Salesperson app at the next call.
- Patrick Chouinard will look up and share in chat the NetworkChuck YouTube video showing Claude Code integrated into an N8N workflow.
- Paul Miller will look up and share in chat the specific AWS CLI/stack component for managing instance lifecycle and post it in the group chat.
- Morgan Cook plans to use a personal (non-client) app as a sandbox to test Next.js 16 before adopting it on client projects.
- Ryan will build in a thumbnail uploader for the Publer integration in his social media automation app.
- Ryan will trim down the number of questions in his brand discovery quiz (currently ~75).