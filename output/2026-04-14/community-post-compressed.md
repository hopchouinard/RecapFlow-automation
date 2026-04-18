📝 SUMMARY

This week's call covered a wide range of practical topics for builders and consultants. Highlights included a deep discussion on Microsoft Copilot Studio versus Azure Foundry for enterprise agent deployment, the shift in software development toward AI-directed workflows, and strategies for identifying the right AI use case with clients. Members shared real project updates across government tender scraping, event management, cemetery software, and ERP systems. The call also celebrated Elijah and his son winning the Ohio Presidential AI Challenge, and Patrick teased an upcoming open-source community intelligence project.


💡 KEY INSIGHTS

Copilot Studio is fine for a version-one proof of concept but is not a long-term investment. Azure Foundry offers more model options, more connectors, and a more viable path for serious enterprise agent development. Plan to start in Copilot Studio and migrate.

Anthropic and Microsoft are deepening their partnership. Claude is now integrated into Copilot desktop, Excel, PowerPoint, Word, and CoWork. Anthropic's managed agent framework entering the Microsoft ecosystem could significantly change what enterprise agents can do.

Google Enterprise is not what you expect. Gemini Pro and Notebook LM are excellent in the consumer tier, but enterprise versions are heavily restricted. Notebook LM Enterprise cannot natively create Google Docs and outputs Markdown via a workaround script instead.

The Microsoft M365 connector is now a full integration, covering email, calendar, Teams, and SharePoint in a single connector — a meaningful upgrade for enterprise context retrieval.

Tiered model architecture is the cost-effective pattern. Not every task needs peak intelligence. Using cheaper models like Codex for routine work alongside more capable models for complex reasoning is the emerging standard.

Local LLMs are worth preparing for now. Running models locally via tools like Proxmox reduces cost and cloud dependency for high-volume or sensitive workloads.

The SDLC is fundamentally changing. Teams are becoming Markdown developers. Context management, PRD creation, and coordinating between Claude instances are now core skills. The role is shifting from writing code to directing AI and managing strategy.

The best AI consulting question is not "what do you want to automate?" Ask clients where they lose the most time each week and what tasks they cannot avoid but wish they could. That pain point is usually the highest-value AI opportunity and builds trust fastest.

Meeting transcripts are an underused business intelligence tool. If you can access them, you can surface intent, unaddressed challenges, and hidden needs without observing operations directly.

For production deployments with legal or compliance implications, avoid self-hosted open-source agent frameworks. Use managed, auditable platforms like Claude Managed Agents instead.

The Karpathy LLM Wiki prompt has a second use case. Beyond personal knowledge management, it can serve as a preprocessor for RAG pipelines, enriching metadata and improving chunking quality before ingestion.

C-suite adoption is a force multiplier. Getting one technically-minded executive using Claude Code directly can cascade into a sustained, organization-wide engagement from a single training session.


❓ KEY Q&A

Q: Has anyone deployed an employee assistant agent connecting to SharePoint, service manager, and similar tools using Copilot Studio or Azure Foundry?

A: Copilot Studio surprised people with its connector breadth — Workday, Salesforce, SharePoint — and indexes quickly. It works well for a version-one demo. For advanced use cases, Azure Foundry is the recommended path. Start with Copilot Studio to show value fast, then plan to migrate to Foundry. Watch for Anthropic's managed agent framework entering the Microsoft ecosystem as a potential major unlock.


Q: Do you need Docker to run multiple OpenClaude instances on the same machine?

A: For completely isolated processes such as separate client environments, yes — use Docker on Linux VMs. For splitting context within a single agent, use Discord channels instead of Telegram. Each channel maintains its own context memory while sharing a common agent backend.


Q: What is the best approach for a portable, self-contained RAG database that travels with an application?

A: Patrick is currently evaluating LanceDB, which requires no separate backend server and can be packaged directly within the application.


Q: How do you help a client identify the right AI use case when they do not know where to start?

A: Ask where they lose the most time each week and what tasks they cannot avoid but wish they could. That pain point is usually not top of mind as an AI opportunity but delivers the most immediate value. Meeting transcripts are especially useful for surfacing hidden needs.


Q: Is Anthropic's rumored large model (Mythos) available to the public?

A: Not yet. Sub-parts are expected to be unlocked in the next two to three months, with the full model going to select enterprise customers first.


🛠️ TOOLS AND CONCEPTS MENTIONED

Claude Managed Agents — Anthropic's official managed agent framework. Recommended over self-hosted alternatives for production and legally sensitive workflows.

Azure Foundry — Microsoft's more capable AI platform for enterprise agent development. Preferred over Copilot Studio for complex or long-term deployments.

Copilot Studio / Power Automate — Microsoft's low-code agent builder. Useful for fast version-one demos but not recommended as a long-term foundation.

Microsoft M365 Connector — Upgraded from SharePoint-only to cover email, calendar, Teams, and SharePoint in a single integration.

CoWork (Anthropic) — Claude's desktop agent feature, now integrated into Microsoft Copilot desktop.

Proxmox — Hypervisor used for self-hosted local LLM infrastructure.

LanceDB — Embedded vector database requiring no separate server. Being evaluated for portable RAG applications.

Ghost (ghost.build) — Free, CLI-only Postgres database designed for agent use. Agents can spin it up, create schemas, load data, and destroy it programmatically.

Karpathy LLM Wiki Gist — Prompt for ingesting content into an Obsidian vault as a navigable wiki. Also being explored as a RAG preprocessor for metadata enrichment.

Obsidian — Free Markdown-based note-taking app used as a local knowledge vault. Compatible with Claude Code, Codex, and the Karpathy wiki prompt.

N8N — Automation platform used in Elijah's Presidential AI Challenge project to build a personalized lesson plan generator.

RecapFlow — Tool Patrick uses to generate detailed community call recaps.

Memory Palace (Mila Djokovic repo) — A concept for relational memory organization in AI agents. Some skepticism noted about benchmark validity.

ShipKit — Developer starter kit mentioned by Elijah.

Gusto — Payroll platform integrated into Ty's ERP system via SMS-based staff management.

Limitless (recording pendant) — Wearable AI recording device. Cannot be brought into enterprise environments due to recording policies.

Nate B. Jones YouTube — Creator covering the death of SaaS and how to reinvent value in an AI-first world.


📎 SHARED RESOURCES

One Stop Creative Agency
https://onestopcreativeagency.co.uk/

OpenClaude GitHub
https://github.com/Gitlawb/openclaude

Claw-Code GitHub
https://github.com/ultraworkers/claw-code

OpenAI Codex Plugin
https://github.com/openai/codex-plugin-cc

Claude Managed Agents Documentation
https://platform.claude.com/docs/en/managed-agents/overview

Nate B. Jones YouTube Channel
https://www.youtube.com/@NateBJones

Alex Rojas — AI Closing the Arbitrage Gap
https://www.youtube.com/watch?v=BiqG3it0gY0&t=357s

Karpathy LLM Wiki Gist
https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

Ghost — Agent-Native Postgres Database
https://ghost.build/

Free Perplexity Workflow for Business Ideas
https://www.youtube.com/watch?v=7gtw-6eOmnY

Paul Miller — OpenClaude YouTube Reference
https://youtu.be/VFYnD1WREdU?si=F51POhFXfXlYeqiR


🔄 FOLLOW-UPS WORTH EXPLORING

Patrick's community intelligence project — Capturing the community's collective digital intelligence as an open-source GitHub repo. Demo expected in one to two weeks.

David's event management platform demo — Automated RFQ creation, vendor selection, negotiation, and SMS-based staff management. Demo planned for next week.

Elijah's Presidential AI Challenge result — Results announced Thursday at 2pm. A regional win advances them to the White House June 7–10 with a $10,000 prize.

Brendan's guest appearance — Patrick is coordinating for next week or the week after. Watch the community site and meeting invite for confirmation.

Karpathy prompt as RAG preprocessor — Patrick is experimenting with a modified version for metadata enrichment before RAG ingestion. Results are promising.

Claude Managed Agents in the Microsoft ecosystem — Anthropic appears to be bringing its managed agent framework into Microsoft Copilot. Worth monitoring closely.

Ty's local LLM setup — Ty plans to work with Patrick to set up Proxmox and local models on his gaming machine. Could be a useful walkthrough for others considering local infrastructure.

Alex's government tender scraping agent — Building an agent to scrape and process government RFPs in Mexico. Paul suggested mining council meeting notes as an early-signal data source.

Mythos model release — Sub-parts expected in two to three months. Worth revisiting when availability is confirmed.