## general

This coaching call was a shorter-than-usual session hosted by Brandon Hancock, who was in the final sprint before launching ShipKit and needed to keep the call focused on Q&A rather than the normal round-robin format. Brandon shared updates on ShipKit's structure — a course platform built using its own RAG template, with project templates for chat applications, RAG pipelines, and ADK agent workflows — and answered questions from community members about deployment, licensing, and agent architecture.

The pre-call conversation touched on the confusion between Microsoft Copilot and GitHub Copilot in enterprise settings, the risks of "vibe coding" spreading unchecked in corporate environments, and Patrick Chouinard's idea to extend SpecKit to automate GitHub issues, pull requests, and commit management for vibe coders who lack software engineering discipline.

After Brandon departed, the group continued with discussions on Supabase environment cloning challenges, Google ADK agent design patterns, Grok 4 and Grok 3 mini evaluations, the open-sourcing of Chef (apparently Bolt-derived), and a deep technical thread on GPU horizontal vs. vertical scaling for self-hosted LLM inference on AWS EC2 instances. Patrick and Bastian also had a detailed exchange on RAG chunking strategies for complex PDFs with merged-cell tables.

Al Cole shared materials from a Google Labs ADK event in Boston he attended, noting that financial services companies are significantly behind in AI adoption. He also described using Claude to generate a presentation outline fed into Gamma to produce 40 slides with minimal cleanup.

## insights

- **Patrick Chouinard:** Vibe coders create code with no understanding of issues, pull requests, or commits — automating that administrative layer (even at 50% quality) is dramatically better than the current zero-percent compliance.
- **Brandon Hancock:** ADK agent prompts work best with explicit phased approaches — tell the agent what to gather in phase one, and instruct it not to proceed until conditions are met. This pattern appears in all official ADK examples.
- **Brandon Hancock:** When building multi-agent systems, maintain a "digital twin" markdown document that maps every agent's name, what state it reads, what state it writes, and what model it uses. This prevents cascading breakage when state changes ripple across agents.
- **Brandon Hancock:** The difference between "agent as tool" and "sub-agent delegation" in ADK: agent-as-tool is a synchronous function call that returns results immediately to the caller; delegation hands off control so the sub-agent becomes the primary interface going forward.
- **Brandon Hancock:** Auto-scaling to zero is the key cost-control mechanism for Google Cloud deployments — a 24/7 running instance can cost $50–$60/day, while scale-to-zero trades a ~30-second cold start for hundreds of dollars in savings.
- **Brandon Hancock:** When an agent seems to "forget" capabilities you've added, the root cause is almost always a context problem — an `agent.md` or similar high-level project overview file fixes this by giving the agent persistent awareness of the project structure.
- **Al Cole:** A fully AI-driven presentation workflow — spec in Claude → outline → Gamma for slide generation — produced 40 usable slides with only ~20 minutes of cleanup, validating the spec-first approach for non-code deliverables.
- **Mitch:** Using Cursor to edit a live Mermaid markdown diagram via voice memo during a client call creates a "wizard" effect and dramatically accelerates collaborative design sessions.
- **Bastian:** For RAG chunking, the most computationally expensive step is the initial OCR and chunking process, not inference. PDFs with complex merged-cell tables are borderline impossible to chunk correctly with traditional OCR — vision-capable agents should handle those pages separately.
- **Paul Miller:** Google Cloud billing alerts are delivered the next day, not in real time, making hard budget caps effectively impossible — unlike AWS, which can stop services at a budget limit. This is a meaningful risk for developers reselling RAG applications.
- **Patrick Chouinard:** SpecKit is not inherently waterfall — if intents are split small enough, the resulting specs and tasks can be quite agile. The key is granularity of the initial intent decomposition.
- **Juan Torres:** CPU offloading and even converting SSD storage into swap memory are viable strategies for extending effective VRAM on constrained EC2 GPU instances when running large diffusion or LLM models.

## qa

**Q (Ty Wells):** I'm trying to clone a Supabase instance — point-in-time recovery gets schema and data, but not edge functions or users, and UUID mismatches make porting data back difficult. Has anyone solved this?
**A (Brandon Hancock):** The recommended approach is to codify everything in setup scripts: `npm run db migrate` to sync schema, setup scripts to recreate buckets and permissions, deploy edge functions via CLI, and `db seed` for test data. For real data migration between environments, you need custom scripts with checks, but there's no clean one-click solution — it's inherently manual work.

**Q (Paul Miller):** Can ShipKit course content be queried via an MCP server from inside Cursor?
**A (Brandon Hancock):** Not yet — everything is currently delivered via Git (AI docs and prompt templates in the repo). An MCP server that lets developers query course content from Cursor would be a compelling addition, but it hasn't been built yet.

**Q (Paul Miller):** How do we avoid bill shock on Google Cloud when reselling RAG applications?
**A (Brandon Hancock):** Everything in ShipKit is designed to auto-scale to zero. Processing cost for RAG is usage-based (roughly $0.60–$0.80 per gigabyte of content processed). For token costs, using smaller/cheaper models vs. Claude Sonnet Max is a lever depending on price sensitivity. A dedicated email on this topic was planned for Thursday.

**Q (Tom Welsh):** Can ShipKit help me add a new risk-tracking module to my existing AssetMS app (TypeScript + Supabase)?
**A (Brandon Hancock):** Yes — since you're already on TypeScript and Supabase, you're in the supported stack. Break the new module into small steps rather than one large task. Send a diagram of what you're thinking and Brandon will advise on how to tackle it.

**Q (Jahangir Jadi):** In ADK, should I use agents-as-tools or sub-agent delegation for a multi-phase pipeline (validate → extract → classify)?
**A (Brandon Hancock):** Use a phased prompt approach on the root agent for sequential steps with conditional halting (e.g., stop and re-prompt if query is invalid). Agent-as-tool is best when you need a synchronous result returned immediately; delegation is best when you want the sub-agent to take over the conversation flow. For a validation gate, the phased prompt pattern on the root agent is the right choice.

**Q (Jahangir Jadi):** Can an agent-as-tool call another tool (tool inception)?
**A (Brandon Hancock):** A tool-agent can make regular tool calls (calling a piece of code). Two levels of agent-as-tool nesting (agent calling agent-as-tool which calls another agent-as-tool) is untested and likely not supported, but hasn't been confirmed either way.

**Q (AlexH):** I'm building ADK agents that collaboratively maintain a quote with up to 100 line items. Should I use ADK state or artifacts, and how do I avoid overloading context windows?
**A (Brandon Hancock):** Break the 100-item quote into logical sub-groups (e.g., by category), give each sub-group its own structured state object, assign one agent per sub-group, and use a composer agent at the end to assemble the final output. Save results to state immediately after each small task. Maintain a digital twin markdown document listing every agent, what state it reads/writes, and what model it uses — this prevents state changes from silently breaking downstream agents.

**Q (Patrick Chouinard):** Is ShipKit licensed per individual developer, or can an enterprise buy one license for a whole dev department?
**A (Brandon Hancock):** ShipKit is designed for individual developers. Bulk/enterprise licensing hasn't been structured yet, but it's worth a DM conversation if there's a concrete opportunity (e.g., training 40 developers at a client site).

**Q (David Stamper):** My orchestrating agent doesn't recognize features I've added later, and I have to argue with it for 15 minutes. How do I fix this?
**A (Brandon Hancock):** This is a context problem. Create an `agent.md` file (or equivalent) with a high-level overview of your project — what it does, core files, and how things connect. This gives the agent persistent awareness without requiring you to re-explain the project at the start of every chat session. You can ask Cursor to generate this file by pointing it at your existing project.

**Q (Elijah):** Is the ShipKit course platform (the learning management system) itself included in ShipKit, or is it just the RAG template?
**A (Brandon Hancock):** Yes — there is a walkthrough showing how to go from the RAG template to a simplified version of the course platform. That walkthrough and the resulting project are included in ShipKit. The course platform was built using ShipKit's own RAG template as proof of concept.

**Q (Paul Miller):** Can the ShipKit RAG/ADK stack be deployed on AWS or Azure instead of Google Cloud?
**A (Bastian):** In theory yes, since it's containerized. However, Google Cloud is used specifically for its multimodal embedding models (video, image, audio), which aren't easily replicated elsewhere. The chunking/OCR pipeline is the most compute-intensive part, not inference. Brandon would likely not offer support for non-GCP deployments given the parameter differences across clouds.

## tools

- **GitHub Copilot** — Discussed as a code assistant being considered for enterprise adoption; contrasted with Microsoft Copilot (office suite AI).
- **Microsoft Copilot** — Discussed as an office productivity AI (PowerPoint, email rewriting) with RAG-against-document agent capability, distinct from GitHub Copilot.
- **SpecKit** — Patrick's tool for generating specs, plans, and tasks from an intent; being considered for extension to automate GitHub issues, PRs, and commits.
- **ShipKit** — Brandon's product in final pre-launch sprint; includes course platform, project templates (chat, RAG, ADK), and AI prompt templates.
- **Supabase** — Backend platform used by multiple members; Ty's question centered on cloning instances across environments including edge functions and users.
- **Google ADK (Agent Development Kit)** — Core framework discussed for building multi-agent workflows; phased prompting and state management patterns demonstrated.
- **Google Cloud Run** — Deployment target for ShipKit RAG backend; auto-scale-to-zero configuration highlighted as cost control mechanism.
- **Cursor** — Primary IDE used by members; Mermaid extension and agent.md patterns demonstrated within it.
- **Mermaid** — Diagramming-as-code format used inside Cursor to visualize agent workflows and code structure; Mitch uses it live with clients via voice memo.
- **Gamma** — Presentation generation tool; Al Cole used it to turn a Claude-generated outline into 40 slides for a financial services presentation.
- **Claude (Anthropic)** — Used by Al Cole to generate presentation outlines; Brandon uses Claude Sonnet Max for speed despite higher cost.
- **Grok 4 / Grok 3 mini** — Discussed by Bastian and Jake; Grok 3 mini noted as 40x cheaper than Grok 4, with built-in tool-calling in reasoning chains and automatic mode selection.
- **NotebookLM** — Patrick uses it to convert video transcripts into podcast-style audio summaries for faster consumption.
- **Vimeo** — Brandon switched to it from another video host to resolve streaming speed issues in the ShipKit course platform.
- **Presentify** — Screen annotation tool (~$10) used by Brandon to draw on top of shared screens during calls.
- **Mermaid Chart (Cursor extension)** — Extension that renders Mermaid diagrams visually inside Cursor.
- **Chef** — Discussed as recently open-sourced; Bastian believes it's based on Bolt/Bolt.new; uses Convex integration via markdown instruction files.
- **Bolt / Bolt.new** — Referenced as the likely open-source base for Chef.
- **AWS EC2 (GPU instances)** — Juan Torres using A10 (24GB VRAM) and A100 (40GB VRAM) instances for self-hosted LLM and diffusion model inference.
- **DigitalOcean** — Mentioned by Paul as a Docker hosting environment he uses alongside Google Cloud and AWS.
- **Docker / Kubernetes** — Discussed as deployment approach for containerized ShipKit stack; Paul uses Docker locally and on DigitalOcean.
- **Document Intelligence** — Jake mentioned using it for PDF processing; noted as "not the most stable."
- **Neo4j** — Jake mentioned wanting to add graph RAG capability using Neo4j to the ShipKit RAG template.

## links

- **Google ADK Labs materials (Google Drive folder)** — Al Cole shared a Drive folder containing keynote slides, lab materials, and presentation from a Google Labs ADK event in Boston; link posted in Zoom chat.
- **Context management with Claude Code (video, ~29 min)** — Patrick shared a link in chat covering context compression, tool inclusion/removal, and sub-agent splitting strategies for Claude Code; described as "extremely well-built."

## decisions

- **Brandon Hancock** will send an email on Thursday covering Google Cloud cost management and bill-shock prevention strategies for ShipKit deployments.
- **Brandon Hancock** will release ShipKit on Saturday the 27th at 6pm; will announce via School notification; may or may not do a live stream depending on launch stability.
- **Brandon Hancock** will return to the normal two-hour coaching call format starting next Tuesday.
- **Brandon Hancock** will make Jake Maymar the call host for the remainder of the session after departing.
- **Brandon Hancock and Patrick Chouinard** will discuss offline the possibility of a bulk/enterprise ShipKit license for Patrick's client (40 developers in training).
- **Al Cole** will upload his financial services AI presentation to the shared Google Drive folder within ~10 minutes of the call.
- **Jahangir Jadi** will share his screen next week to demo his ADK multi-agent pipeline for the group.
- **AlexH** will share diagrams of his quote-management agent architecture next week for Brandon to review.
- **Tom Welsh** will send Brandon a diagram of his planned AssetMS risk-tracking module for architecture feedback.
- **Alex Wilson** will publish a LinkedIn post referencing Brandon and ShipKit; Brandon will repost and encourages continued tagging.
- **Patrick Chouinard** will explore extending SpecKit to handle upstream intent parsing into GitHub issues, pull requests, and commit management (currently a conceptual idea, not yet in implementation).
- **Bastian** will continue investigating GPU chunking/OCR pipeline options for ShipKit's RAG backend, including routing PDF-heavy documents to vision-capable agents rather than traditional OCR.