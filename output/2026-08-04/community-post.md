📝 SUMMARY
This week's call featured live demos of a zero-backend-change UI reskinning system, strategies for reviving obsolete hardware with AI-written drivers, and a bottom-up approach to enterprise knowledge management using Git as "agentic memory." Members also strategized on consulting deal structures, fundraising tactics for AI photo booths, and hardware arbitrage opportunities.

💡 KEY INSIGHTS
🔹 Zero-Backend UI Reskinning: Build a separate frontend layer that consumes existing APIs to completely reskin applications without touching endpoints or ACLs. This allows multi-tenant products to show different complexity levels to different users (e.g., hiding technical details from basic users while showing dense data to power users).

🔹 AI Hardware Salvaging: Revive obsolete hardware like label printers by having AI reverse-engineer communication protocols and write fresh Python drivers in a half-day. Calibrate by showing the AI photos of physical output (e.g., a printed label) and asking it to adjust its own calculations rather than manual tuning.

🔹 Git as Agentic Memory: Use Git/Azure DevOps as "SharePoint for Agents"—a behavioral memory layer that feeds context into agent actions rather than serving as a queryable RAG database. Build bottom-up at the team level (20-30 people) before attempting corporate-scale systems.

🔹 Problem Description Over Solution Prescription: Avoid commitment bias by describing problems clearly rather than prescribing solutions. Heavily-specified prompts perform worse with Opus/Claude than allowing the model to determine its own approach.

🔹 Paid Proof-of-Concept Gating: Structure consulting engagements with a small paid POC phase before full projects to build trust with budget stakeholders and create easier approval pathways without giving away free work.

🔹 Operational Capability Assessment: Evaluate client operational readiness (support, process stability, team skills) beyond just the code deliverable.

🔹 Event Coordinator as Sales Channel: High-end venue coordinators can become viral sales agents after experiencing AI products firsthand; one showcase event can generate significant word-of-mouth.

❓ KEY Q&A
Q: How does the UI reskin system work without touching the backend?
A: The reskin sits on its own server (either subdomained or pointing directly at the original API endpoints) and consumes the same back-end APIs. The original endpoints and ACLs remain completely untouched; the new UI simply presents the existing data differently.

Q: How do you handle hierarchical relationships in the reskinned interface?
A: No extra work is needed. The hierarchy and data structure already exist in the underlying application; the reskin just visualizes that existing structure differently without changing any endpoints.

Q: How does the Codex-as-reviewer plugin integrate with Claude Code?
A: It is an official OpenAI plugin (codex-plugin-cc) that creates a hook. When Claude Code finishes a coding activity, it sends the output to Codex via a headless call. Codex performs an adversarial code review against a dedicated system prompt, returns a report, and Claude reads and acts on that feedback.

Q: For enterprise knowledge management, how do you serve the information back to users?
A: It is not designed to be queried like a traditional database or RAG system. Instead, it functions as behavioral memory that provides transparent context inside co-work and Claude Code agent interactions (e.g., "last time you did this, it was done that way").

Q: I have been building on spec for a real estate client who has shared sensitive data. Should I show progress before contract or wait?
A: Show something tangible, but explicitly frame it as a paid proof-of-concept phase rather than the full application. This demonstrates capability while creating a smaller, easier-to-approve financial commitment. Also get a draft contract in front of the actual budget-signing stakeholder immediately.

Q: Opus 5 is giving strange responses that require re-reading. Any advice?
A: Trim your prompts and skills significantly. Opus 5 needs far less context and instruction than Opus 4.8. Be descriptive about the problem you want solved, not about how you want it solved.

🛠️ TOOLS AND CONCEPTS MENTIONED
CMUX — Manages and rotates between multiple Anthropic subscription accounts automatically.

Codex (OpenAI) + codex-plugin-cc — Automated adversarial code reviewer that hooks into Claude Code's output pipeline.

Claude Code — Primary coding environment used across projects; group consensus favors Opus 4.8 over Opus 5 for quality of responses.

Fable — AI model referenced for comparison and used for system architecture and stabilization planning.

Terrain/Skin System — Ty Wells's approach for frontend-only UI reskinning of existing applications by consuming their APIs.

Uptime Kuma — Open-source uptime monitoring tool used as a demo target for the reskinning system.

Azure DevOps/Git as Agentic Memory — Using version control repos and CI pipelines to manage team-level organizational knowledge and conflict resolution.

Class2Curb — Morgan's product for school carpool-line management.

Heritage Plot — Morgan's mapping project using scalar vector graphs over satellite imagery.

AI Booth — Juan Torres's AI-powered photo booth application for events.

NotebookLM — Recommended for synthesizing Y Combinator pitch videos into pitching guidance.

Python (direct-to-device CLI/UDP) — Used to rewrite printer drivers without CUPS for hardware revival.

Next.js — Framework used for real estate client dashboards.

ShipKit — Starter kit/boilerplate tool mentioned for client builds.

📎 SHARED RESOURCES
https://coast.algome.ai — Ty Wells's "terrain" platform for testing and generating UI reskins of applications or repos.

http://ttl.golf — Live example of Ty's reskinned interface kept in production.

https://data-terrain-showcase.vercel.app/t/the-holding-pool-ws8r19 — Demo reskin run against Morgan's Class2Curb site.

https://class2curb.com/ — Morgan's carpool-pickup product site.

https://github.com/openai/codex-plugin-cc — OpenAI's official Codex plugin for Claude Code.

https://www.linkedin.com/posts/juan-torres-ai-engineering_i-made-a-game-its-called-ai-booth-activity... — Juan Torres's AI Booth project post.

https://www.linkedin.com/posts/juan-torres-ai-engineering_economics-finance-datascience-activity... — Additional project insights from Juan Torres.

https://www.linkedin.com/posts/juan-torres-ai-engineering_datascience-ai-agenticsystems-activity... — Agentic systems discussion from Juan Torres.

https://www.score.org/ — Resource for business advice suggested to Juan Torres.

🔄 FOLLOW-UPS WORTH EXPLORING
Ty Wells launching "Island Flow" to clients in the Bahamas on September 15th using the reskinned terrain UI approach.

Patrick Chouinard rewriting scanner driver software for Mac this weekend, inspired by Morgan's printer project.

Adam considering bringing the obsolete penny-rounding cash register hardware problem to the group for a potential low-risk exploratory solution.

Juan Torres investigating seed funding applications and a potential Y Combinator showcase in San Diego.

Alex Roca preparing draft contracts for his real estate client and structuring the engagement as a paid phase-one with bi-weekly champion calls over three months.
