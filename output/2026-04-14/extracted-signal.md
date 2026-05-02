## general

This was a weekly coaching/community call hosted by Patrick Chouinard, with participants joining from Quebec, Australia, New Zealand, Mexico, Ohio, and California (San Francisco area). The session had a lighter attendance than usual, attributed partly to U.S. tax week. The format was open round-table: each participant shared what they were working on, asked questions, or flagged items of interest to the group.

Major topics included enterprise AI agent deployment on Microsoft Azure (Copilot Studio, Foundry, and the new Anthropic/Microsoft partnership bringing Claude into Copilot), local LLM infrastructure using Proxmox, the Karpathy LLM Wiki gist as a knowledge-organization and idea-filtering tool, and the evolving SDLC in an AI-assisted coding environment. Several members shared project updates: Ty Wells demonstrated a user-driven development feedback loop, David shared an event-planning RFQ automation platform, Morgan Cook reported progress on a cemetery management GIS project, and Elijah Stambaugh announced that he and his high-school-aged son won the Ohio state round of the Presidential AI Challenge.

Patrick also teased an upcoming community project—a system to capture and make navigable the collective "digital intelligence" of the group—planned as an open-source GitHub release within one to two weeks. Discussions touched on the gap between Google Enterprise and Google Pro/consumer Gemini offerings, the limitations of Copilot Studio/Power Automate versus Azure Foundry, and the philosophical shift from writing code to directing AI agents as the new developer role.

The call closed with a mention of a potential future guest appearance by someone named Brendan, to be announced via the community site.

## insights

- **Layered model tiers are the near-term cost strategy**: Not every task requires peak intelligence; cheaper models like Codex can handle cleanup work, while frontier models handle complex reasoning. Patrick expects multi-tier model orchestration to become standard.
- **Copilot Studio / Power Automate is a dead-end investment**: Patrick strongly advised against building production agents in Copilot Studio as it stands; Azure Foundry is the recommended path for enterprise Microsoft shops needing longevity.
- **The Anthropic–Microsoft partnership is a significant unlock**: Claude is now embedded across Copilot (Excel, Word, PowerPoint, desktop) and CoWork functionality is being brought into Copilot desktop, making the full Claude ecosystem available inside Microsoft's enterprise stack.
- **Google Enterprise vs. Google Pro is a stark disparity**: Gemini Enterprise is described as "unusable" compared to the consumer/Pro tier—Notebook LM Enterprise is kneecapped, and even generating a Google Doc requires a workaround script. Enterprises evaluating Google should be aware of this gap.
- **Finding the right use case is harder than building the solution**: Patrick noted that once you have the problem context, modern models can solve almost anything—the real bottleneck is identifying which pain point is worth solving. His technique: ask clients what tasks they lose the most time on each week, not what they think AI should do.
- **Meeting transcripts are a goldmine for business analysis**: Any intent, challenge, unaddressed need, or inefficiency can surface from transcript analysis—Patrick recommended this as a primary discovery tool for consultants.
- **Enterprise AI coding is fundamentally different from vibe coding**: Sharing context between Claude instances currently requires human copy-paste ("sneaker net" / "USB-stick middleware"), and the SDLC is being reinvented around Markdown-based development.
- **C-suite advocates are the most powerful enterprise AI accelerators**: Once a technically-minded executive is onboarded, every other door opens quickly. Patrick's C-suite trainee consumed $3,000 in tokens in a single month.
- **For production systems with legal implications, avoid self-hosted open-source agent frameworks**: Patrick recommended Claude Managed Agents (Anthropic's managed offering) over OpenClaw, Iron Claw, or similar self-hosted variants for anything with legal or compliance consequences.
- **Karpathy's LLM Wiki prompt can serve as a RAG preprocessor**: Patrick is experimenting with a modified version of Karpathy's gist to enrich metadata before chunking content into a vector database, with promising early results.
- **Tablet-as-peripheral pattern**: Ty Wells demonstrated using commodity Fire tablets as front-facing customer displays, signature pads, kitchen displays, and check-in terminals—eliminating proprietary hardware dependencies entirely.

## qa

**Q (Marc Juretus):** Has anyone deployed an employee assistant agent at work connecting to systems like SharePoint, Service Manager, or Salesforce—particularly using Copilot Studio or Azure Foundry?
**A (Patrick Chouinard):** We haven't deployed yet but are a Microsoft shop. Copilot Studio's drag-and-drop Power Automate approach is not the paradigm moving forward. Foundry is the better investment. Watch the Anthropic partnership closely—if they bring managed agents into the Microsoft ecosystem as they seem to be doing, that will be the big unlock.

**Q (Marc Juretus):** Is Mythos anywhere near being released to the general public?
**A (Paul Miller):** They've said they'll start unlocking sub-parts in the next two to three months. The full model is apparently being given to certain corporate clients now, but not the general public.

**Q (Alex Rojas):** If I want to run more than one OpenClaw instance on my machine, do I need Docker?
**A (Patrick Chouinard):** For splitting context, use Discord channels instead—same agent engine, different context per channel, with shared or individual memory. If you genuinely need isolated agents for separate clients (e.g., on a Mac Mini), then yes, go Docker on Linux VMs. Avoid hosting on someone else's hardware; an old laptop running Proxmox is sufficient.

**Q (Alex Rojas):** Paul, are you using Claude Agent SDK or OpenClaw agents for your second-brain project?
**A (Paul Miller):** Claude Agent SDK. I wanted more control and felt uncomfortable with OpenClaw on the security side.

**Q (Patrick Chouinard):** Andrew, are you using Google Pro or Google Enterprise?
**A (Patrick Chouinard [self-answering after Andrew's response]):** Google Pro is incredible; Gemini Enterprise is pure hell—unusable, feature-limited, Notebook LM Enterprise is kneecapped, and you can't even generate a Google Doc natively. The disparity between Pro and Enterprise is enormous right now.

**Q (Elijah Stambaugh):** How do you quickly identify the right AI use case when engaging a business client?
**A (Patrick Chouinard):** Don't ask what they think AI should do—ask where they lose the most time every week, what tasks they can't avoid but hate. That's usually not top of mind for them as an AI opportunity, but removing their worst weekly pain point creates immediate buy-in and opens every door after.

## tools

- **Claude / Claude Code** – Primary coding and enterprise AI assistant; discussed extensively for agentic coding and enterprise deployment
- **Claude Managed Agents** – Anthropic's managed agent platform; recommended for production/legal-consequence use cases over self-hosted alternatives
- **Copilot Studio** – Microsoft's low-code agent builder; discussed as insufficient for serious enterprise agent work
- **Azure Foundry** – Microsoft's enterprise AI platform; recommended over Copilot Studio for longevity and model variety
- **OpenClaw / openclaude** – Self-hosted open-source Claude agent framework; discussed with security caveats for production use
- **Proxmox** – Hypervisor for local LLM infrastructure; Patrick has triggered multiple community installations
- **Obsidian** – Markdown-based note-taking app; used with Karpathy's prompt to build navigable knowledge wikis
- **Notebook LM** – Google's AI notebook tool; praised in consumer/Pro tier, criticized as kneecapped in Enterprise
- **Gemini (Google)** – LLM discussed for conversational continuity and YouTube integration via Gems feature
- **ChatGPT** – Discussed as superior for voice-based interaction; Patrick uses a heavily customized system prompt
- **N8N** – Automation platform used by Elijah Stambaugh for the Presidential AI Challenge project with Gemini 2.5 Flash
- **Ghost (ghost.build)** – Free CLI-only Postgres database designed for agents to spin up, use, and destroy schemas
- **LanceDB** – Embedded vector database Patrick is using for RAG; no server installation required, packages with the app
- **Telegram** – Used for mobile-based agent control (approving PRs, initiating plans) in Ty Wells's feedback loop
- **Discord** – Recommended over Telegram for splitting agent context across channels
- **Gusto** – Payroll platform integrated into Ty Wells's ERP/staff management system
- **FileMaker Pro** – Legacy database platform David had deep experience with before AI-assisted development
- **Perplexity** – Mentioned in a shared workflow video for identifying business ideas
- **Fathom** – AI meeting notetaker present in the call
- **Read.ai** – AI meeting summarizer present in the call
- **MeetGeek** – AI meeting notetaker (Dudley's) present in the call
- **ShipKit** – Starter kit/framework Elijah's new partner purchased to onboard into the community's stack
- **Fire tablet (Amazon)** – Used by Ty Wells as a low-cost peripheral display/signature pad/check-in terminal

## links

- https://onestopcreativeagency.co.uk/ – Ryan's one-stop creative agency site (shared by Patrick)
- https://github.com/Gitlawb/openclaude – OpenClaude repo (shared by Elena; Patrick clarified this was not the one he meant)
- https://github.com/ultraworkers/claw-code – Claw-code repo; the one Patrick was actually referencing
- https://youtu.be/VFYnD1WREdU?si=F51POhFXfXlYeqiR – YouTube video shared by Paul Miller (context: OpenClaw/agent discussion)
- https://github.com/openai/codex-plugin-cc – OpenAI Codex plugin repo shared by Patrick
- https://platform.claude.com/docs/en/managed-agents/overview – Anthropic's Claude Managed Agents documentation
- https://www.youtube.com/@NateBJones – Nate B. Jones YouTube channel; covers death of SaaS and AI business strategy
- https://www.youtube.com/watch?v=BiqG3it0gY0&t=357s – Video shared by Alex Rojas on AI closing the arbitrage gap
- https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f – Andrej Karpathy's LLM Wiki gist; prompt for ingesting content into an Obsidian vault as a navigable wiki
- https://ghost.build/ – Ghost: free CLI-only Postgres database built for agent use
- https://www.youtube.com/watch?v=7gtw-6eOmnY – Free Perplexity workflow for identifying business ideas (shared by Morgan Cook, directed at David)
- https://fathom.video/customize – Fathom notetaker settings link (auto-posted by bot)

## decisions

- **Ty Wells** will reach out to Patrick to set up his local LLM infrastructure on his gaming PC using Proxmox.
- **Patrick Chouinard** will continue building his community intelligence project (a navigable digital knowledge base of the group's collective output) and plans to release it as an open-source GitHub repo within one to two weeks.
- **Patrick Chouinard** will show his C-suite trainee how to instantiate CoWork as a full agent with personality, memories, contacts, and projects in their next weekly session.
- **David (David's iPhone)** will demo his event-planning RFQ automation platform to the group next week.
- **Alex Rojas** will explore Claude Managed Agents and report back to the group on his findings.
- **Morgan Cook** will share her NDA-protected completed project with the group once the NDA clears, likely next week.
- **Patrick Chouinard** will keep the community posted on the community site regarding a guest appearance by Brendan (either next week or the week after).
- **Elijah Stambaugh** will update the group Thursday on whether he and his son advance to the White House round of the Presidential AI Challenge (June 7–10).
- **Paul Miller** will post the Nate B. Jones channel link to the community (Biggi Fraley provided the name in chat; Patrick shared the URL).