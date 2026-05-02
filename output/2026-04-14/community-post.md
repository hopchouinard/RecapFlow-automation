📝 SUMMARY

This week's round-table call brought together members from Quebec, Australia, New Zealand, Mexico, Ohio, and California for an open discussion on enterprise AI deployment, local infrastructure, and real-world project updates. With lighter attendance due to U.S. tax week, the group dove deep into Microsoft's evolving AI stack including the new Anthropic partnership bringing Claude into Copilot, strategies for local LLM hosting via Proxmox, and Andrej Karpathy's LLM Wiki method for knowledge management. Members shared significant wins including Ty Wells's user-driven development feedback loop, David's event-planning RFQ automation platform, Morgan Cook's cemetery management GIS project, and Elijah Stambaugh's victory in the Ohio state round of the Presidential AI Challenge. Patrick also previewed an upcoming open-source community project to capture and navigate the group's collective digital intelligence, slated for release within two weeks.

💡 KEY INSIGHTS

Layered model orchestration is the immediate cost strategy. Not every task requires frontier intelligence; use cheaper models like Codex for cleanup while reserving advanced models for complex reasoning.

Copilot Studio and Power Automate represent a dead-end investment for production agents. For Microsoft shops needing longevity, Azure Foundry is the recommended path, especially with the Anthropic partnership embedding Claude across Excel, Word, PowerPoint, and desktop Copilot.

Google Enterprise vs. Google Pro shows a stark capability gap. Gemini Enterprise is currently described as unusable compared to the consumer tier, with kneecapped Notebook LM functionality and workarounds required for basic Google Doc generation.

Finding the right use case remains harder than building the solution. The most effective discovery technique is asking clients what weekly tasks they lose the most time on, rather than what they think AI should do.

Meeting transcripts serve as goldmines for business analysis. Intent, challenges, and inefficiencies surface naturally from transcript review, making them primary discovery tools for consultants.

Enterprise AI coding is fundamentally different from vibe coding. The SDLC is shifting toward Markdown-based development, with context sharing between Claude instances currently requiring human mediation.

C-suite advocates are the most powerful adoption accelerators. A technically-minded executive consuming significant token volumes opens every organizational door.

For production systems with legal implications, avoid self-hosted open-source agent frameworks. Claude Managed Agents are recommended over OpenClaw or Iron Claw for compliance-sensitive deployments.

Karpathy's LLM Wiki prompt can function as a RAG preprocessor. Enriching metadata before chunking into vector databases shows promising early results for knowledge organization.

The tablet-as-peripheral pattern eliminates proprietary hardware. Commodity Fire tablets serve effectively as customer displays, signature pads, kitchen displays, and check-in terminals.

❓ KEY Q&A

Q: Has anyone deployed an employee assistant agent connecting to SharePoint, Service Manager, or Salesforce using Copilot Studio or Azure Foundry?
A: While not yet deployed, the guidance is clear: Copilot Studio's drag-and-drop Power Automate approach is not the future paradigm. Azure Foundry is the better investment, with the Anthropic partnership potentially unlocking managed agents within the Microsoft ecosystem.

Q: Is Mythos anywhere near general release?
A: Sub-parts will begin unlocking in two to three months. The full model is currently available to select corporate clients only.

Q: If I want to run multiple OpenClaw instances, do I need Docker?
A: For splitting context, use Discord channels instead—same engine, different contexts. Only use Docker on Linux VMs if you need true isolation for separate clients, hosted on your own hardware like an old laptop running Proxmox.

Q: Are you using Claude Agent SDK or OpenClaw for your second-brain project?
A: Claude Agent SDK. OpenClaw raised security concerns for this use case.

Q: How do you quickly identify the right AI use case when engaging a business client?
A: Do not ask what they think AI should do. Ask where they lose the most time every week—what tasks they cannot avoid but hate. Removing that specific pain point creates immediate buy-in.

🛠️ TOOLS AND CONCEPTS MENTIONED

Claude and Claude Code — Primary coding and enterprise AI assistant for agentic development.

Claude Managed Agents — Anthropic's managed platform recommended for production and legal-consequence use cases over self-hosted alternatives.

Azure Foundry — Microsoft's enterprise AI platform recommended over Copilot Studio for longevity and model variety.

Copilot Studio — Microsoft's low-code agent builder; currently considered insufficient for serious enterprise agent work.

OpenClaw and Claw-code — Self-hosted open-source Claude agent frameworks; discussed with security caveats for production use.

Proxmox — Hypervisor for local LLM infrastructure; sufficient for running isolated agent instances on commodity hardware.

Obsidian — Markdown-based note-taking app used with Karpathy's prompt to build navigable knowledge wikis.

Notebook LM — Google's AI notebook tool; excellent in Pro tier but kneecapped in Enterprise.

Ghost — Free CLI-only Postgres database at ghost.build designed for agents to spin up, use, and destroy schemas.

LanceDB — Embedded vector database requiring no server installation; packages directly with applications.

N8N — Automation platform used for workflow orchestration.

Fire Tablet — Commodity Amazon tablet used as low-cost peripheral displays, signature pads, and check-in terminals.

Telegram and Discord — Messaging platforms used for mobile agent control and context splitting respectively.

📎 SHARED RESOURCES

Andrej Karpathy's LLM Wiki Gist — https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

Anthropic Claude Managed Agents Documentation — https://platform.claude.com/docs/en/managed-agents/overview

Ghost Database for Agents — https://ghost.build/

OpenAI Codex Plugin — https://github.com/openai/codex-plugin-cc

Claw-code Repository — https://github.com/ultraworkers/claw-code

Nate B. Jones YouTube Channel (AI Business Strategy) — https://www.youtube.com/@NateBJones

Perplexity Workflow for Business Ideas — https://www.youtube.com/watch?v=7gtw-6eOmnY

AI Arbitrage Gap Video — https://www.youtube.com/watch?v=BiqG3it0gY0&t=357s

One Stop Creative Agency — https://onestopcreativeagency.co.uk/

OpenClaude Repository (note: not the one primarily discussed) — https://github.com/Gitlawb/openclaude

Fathom Notetaker Settings — https://fathom.video/customize

🔄 FOLLOW-UPS WORTH EXPLORING

Ty Wells will set up local LLM infrastructure on his gaming PC using Proxmox with Patrick's guidance.

Patrick Chouinard will release the community intelligence project as an open-source GitHub repository within one to two weeks.

David will demo his event-planning RFQ automation platform to the group next week.

Alex Rojas will explore Claude Managed Agents and report findings back to the group.

Morgan Cook will share her recently completed NDA-protected project once cleared, likely next week.

Elijah Stambaugh will update the group Thursday on advancement to the White House round of the Presidential AI Challenge (June 7–10 dates).

Patrick will announce a guest appearance by Brendan via the community site for next week or the week after.

Paul Miller will post the Nate B. Jones channel link to the community.