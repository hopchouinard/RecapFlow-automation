## general

This coaching call brought together roughly a dozen members of what appears to be a recurring AI development community led by Brandon Hancock. The session opened with informal discussion about AI adoption in enterprise settings, then moved into a structured round of member updates. Topics ranged from tooling choices (Claude Code, Windsurf, Co-Work), to workflow automation, RAG pipeline architecture, voice agents, sales AI tools, and the broader question of how AI will reshape work and education.

Patrick Chouinard presented the most technically detailed update: a pipeline he built using Claude Code to generate structured knowledge artifacts from each development conversation, which are then loaded into NotebookLM to produce training material, podcasts, slides, and a queryable RAG chatbot — all as a byproduct of his normal build process. Scott Rippey shared progress on a call-coaching AI SaaS (NeuralSpark / call coach), including a three-layer RAG architecture using vector embeddings, Cohere cross-encoder re-ranking, and a recursive language model (RLM) approach to reduce context rot. Elijah Stambaugh demonstrated a Bible reading app built with ShipKit and discussed the Presidential AI Challenge his son is entering. Ty Wells showed an internal DevOps tool that tracks flaws across multiple projects, stores cross-project memory, and is intended to feed a scaffolding system that builds software on demand.

Brandon used the session to announce upcoming ShipKit video releases covering updated development workflows, Claude Code setup, Git work trees, and a new RAG update. He also fielded questions about using Claude Code on mobile to kick off feature branches from the gym, and gave business strategy advice to several members on monetization, personal branding, and go-to-market approaches.

## insights

- **Patrick Chouinard:** Compressing each AI development conversation into a structured markdown artifact (via a Claude skill) creates training material as a free byproduct of normal work — the artifact can then be loaded into NotebookLM to auto-generate podcasts, slides, and a RAG chatbot without additional effort.
- **Brandon Hancock:** Using Claude Code on mobile (voice → task template → new Git branch) lets you kick off feature development while away from the desk; when you return, branches are ready to test or parallelize via Git work trees.
- **Brandon Hancock:** Spinning up five parallel work-tree instances with different creative prompts (e.g., "professional" vs. "creative") lets AI generate multiple design variants simultaneously; you pick the best and merge it — no need to be creative yourself.
- **Scott Rippey:** A three-layer RAG architecture — (1) vector embedding search, (2) Cohere cross-encoder re-ranking, (3) recursive LLM (RLM) where the model hunts for information via tool calls rather than receiving a large context dump — can significantly reduce context rot and improve answer quality as knowledge bases grow.
- **Brandon Hancock:** The real bottleneck for enterprise AI adoption is IT departments blocking access to capable tools; employees are already using unapproved AI anyway, creating worse security outcomes than a properly ring-fenced approved environment would.
- **Patrick Chouinard:** Running simple sub-agents (web search, summarization) on local models via Ollama (e.g., Qwen 3 Coder 32B Q4) can eliminate token costs for repetitive background tasks while reserving Claude for high-intelligence work; Patrick ran up to 12 parallel instances on a local machine.
- **Brandon Hancock:** The "Build Once, Sell Twice" principle (Jack Butcher) applies directly to Patrick's workflow: the application is the first deliverable, and the documented build process becomes a second sellable product (course/notebook).
- **Elijah Stambaugh:** A client who set a goal of automating one hour per week will have automated a full-time position's worth of work by year-end — framing AI adoption as a small, consistent habit lowers resistance.
- **Brandon Hancock:** Enterprise companies offering only a "ChatGPT wrapper" to employees are forcing bad incentives — employees will route around restrictions using less secure tools (e.g., DeepSeek), making the security argument for restriction self-defeating.
- **Morgan Cook:** Non-technical users can be empowered with AI skills (Claude skills/scripts) that convert their existing workflow outputs (markdown research) into polished deliverables (HTML + CSS + meta JSON), collapsing days of work into minutes without requiring them to understand the underlying code.
- **Brandon Hancock:** The future of work likely splits into "system creators" and "system managers" rather than "task doers" — the people who define templates and automation pipelines will capture most of the economic value.
- **Patrick Chouinard:** Automating part of your job doesn't reduce workload — it expands what's possible, creating more work at a higher level. Patrick noted he has never had more work than since automating his previous core tasks.

## qa

**Q (Hemal Shah):** When you're talking to Claude about your projects while away from your computer, do you upload the project document first, and how does that workflow actually function?
**A (Brandon Hancock):** In the Claude mobile app, you switch to "Code" mode, which connects to your linked Git repository. You then just talk — describing the feature you want — and tell it to create a new task using `template.md`. Claude creates a new branch, plans the work, and starts implementing. When you get home, you ask Claude what branches were started, check them out one at a time, and finish them. For parallel work, you create a Git work tree for each branch and run all tasks simultaneously.

**Q (Alex Wilson):** Can you make a video showing the full workflow of starting work on mobile and then picking it up at the desktop, specifically the GitHub branch review part?
**A (Brandon Hancock):** Yes, I'll add that as a video. The core of it is: when you get back to your desktop, you ask Claude what branches are available, it lists them by name, you check out each one, work on it, merge it in, and delete the branch. For advanced use, create a work tree per branch and run them all in parallel.

**Q (Hemal Shah):** What tools would you recommend for building a voice agent that initiates outbound calls to leads and schedules calendar meetings?
**A (Brandon Hancock):** Bland.ai is the easiest no-code option — it feels like N8N but for voice. You define a workflow to collect name, topic, and preferred time, add a general knowledge base for off-script questions, and connect it to Google Calendar for availability. It's affordable and straightforward to set up.

**Q (Paul Miller):** For building an aggregated reporting app that pulls from Postgres, summarizes data, and potentially applies agentic AI — should I use the ShipKit RAG template or the basic chat template?
**A (Brandon Hancock):** Use the chat template. RAG would be overkill for database data. The pattern is simple: before making the LLM call, do one or more database fetches, format the data, and inject it as a user message. For level two, run three `generateText` calls in parallel (one per data source), then pass all three summaries into a single `streamText` call that formats the final report for the user. Look at the RAG template only to understand how it injects retrieved data into the prompt — the underlying concept is identical.

**Q (Patrick Chouinard):** Has anyone tried connecting Claude Code to Ollama to use local models as sub-agents for background tasks like web search and summarization?
**A (Brandon Hancock / Patrick Chouinard):** Brandon had a bad experience with early Llama models (70% tool-call success rate) but acknowledged Qwen 3 Coder is specifically built for tool calling and agentic work. Patrick confirmed he ran up to 12 parallel instances on a local machine using Qwen 3 Coder 32B Q4, which is sufficient for simple tasks like web search, summarization, and file comparison — freeing Claude for high-intelligence work and avoiding rate limits on background automation pipelines.

**Q (Ryan C):** What's the best path forward for scaling a freelance AI business for small businesses — agency, coaching, or something else?
**A (Brandon Hancock):** Map out 12 months on each path and be brutally honest about monetization and enjoyment. A suggested roadmap: months 1–3, build a portfolio of 5–10 projects; months 4–6, start a YouTube channel showing how you did it and what you built; months 7–9, grow audience and increase inbound leads; months 10–12, productize through coaching (infinite margin, zero cost, highly scalable). Niche down to a specific vertical (e.g., small businesses in your local area or a specific industry) to make marketing easier. Also look at Stephen G. Pope's content on flat marketing funnels.

## tools

- **Claude Code (CLI)** — Primary AI coding tool; multiple members switched to it from Windsurf; used for agentic development, sub-agents, and mobile voice-to-code workflows
- **Claude Desktop App** — Has a "Code" mode that wraps Claude Code in a web interface with local file access; available on all platforms including Windows
- **Co-Work** — Mac-only tool wrapping Claude Code with file system access; discussed as the inspiration for agentic local file workflows
- **Windsurf IDE** — AI coding IDE; Morgan switched away from it due to connectivity issues
- **NotebookLM** — Used by Patrick to host 22 markdown artifacts from a build process, generating podcasts, slides, and a RAG chatbot; Patrick has ~500 notebooks
- **Ollama** — Local model runner; Patrick used it to run Qwen 3 Coder 32B Q4 as a free sub-agent for background automation tasks
- **Qwen 3 Coder 32B (Q4 quantized)** — Local coding/tool-calling model run via Ollama; used as a sub-agent for web search and summarization to avoid token costs
- **Cohere (re-ranking API)** — Used by Scott as layer two of his RAG pipeline for cross-encoder re-ranking of retrieved documents
- **Fathom** — Meeting transcription tool; Brandon used it to capture a problem description and paste the transcript into Co-Work
- **Bland.ai** — No-code voice agent platform recommended for outbound lead-calling and calendar scheduling workflows
- **N8N** — Workflow automation platform; compared to Bland.ai in terms of interface feel; Elijah's son used it for the Presidential AI Challenge newsletter project
- **Vercel AI SDK** — Used in ShipKit templates; `generateText` and `streamText` functions discussed for building aggregated reporting pipelines
- **Git work trees** — Advanced Git feature used by Brandon to run multiple feature branches in parallel; covered in upcoming ShipKit videos
- **OpenRouter** — Mentioned as a way to access open-source models (e.g., OSS models) cheaply without hosting locally
- **ShipKit** — Brandon's one-time-purchase developer toolkit with templates, task templates, and video courses; RAG and workflow updates in progress
- **Garmin S62** — Golf GPS watch; briefly discussed by Ty and Brandon as an off-topic aside

## links

- **Patrick's NotebookLM notebook** — Shared in chat during the call; contains 22 build-process artifacts from Patrick's AI news aggregator project, with podcast, slides, and RAG chatbot
- **Patrick's Claude skill file** — Shared in chat; the skill used to compress a development conversation into a structured knowledge artifact
- **Presidential AI Challenge** — Dropped in chat by Brandon; US government initiative pushing AI in K-12 education, with district-level competitions and prizes including a trip to DC
- **"Build Once, Sell Twice" by Jack Butcher** — Available on Gumroad for ~$10; Brandon recommended it to Patrick as a framework for monetizing the build-process documentation workflow
- **refiningeducation.com** — Elijah's domain for a planned education-focused brand about AI and the future of work
- **Paul's link about Claude Code connectivity** — Shared in chat during Patrick's segment (described as connecting to Claude Code); specific URL not captured in transcript

## decisions

- **Brandon Hancock** will fix the broken RAG pipeline upload process immediately after the call and release updated ShipKit videos (AI coding stack, development workflow, work trees, task review command) by late that night or first thing the following morning, followed by a single consolidated email to members.
- **Brandon Hancock** will add a video demonstrating the mobile-to-desktop Claude Code workflow, including the Git branch review step.
- **Patrick Chouinard** will finalize the NotebookLM notebook with a clean onboarding node, then publish a YouTube video using the notebook as the core deliverable and the video as marketing material pointing to it.
- **Patrick Chouinard** will look at the link Paul shared (Claude Code API connectivity) to explore automating the NotebookLM artifact creation pipeline.
- **Patrick Chouinard** will experiment with running Claude Code backed by Ollama/Qwen 3 Coder as a local sub-agent for the background AI news aggregation pipeline.
- **Brandon Hancock** will DM/email Patrick the link to the "Build Once, Sell Twice" course by Jack Butcher.
- **Brandon Hancock** will contact Patrick before he records his YouTube video to share specific prompts for titles and hooks from the YouTube Authority Accelerator.
- **Scott Rippey** will demo the RLM on/off comparison in NeuralSpark at the next call and report back on model choices and performance differences.
- **Brandon Hancock** will re-forward the School community invite email to Scott.
- **Elijah Stambaugh** will ping Brandon to set up a ShipKit affiliate arrangement (discount code for Elijah's community members, with a share going to Elijah).
- **Ryan C** will email Brandon to schedule a session to map out 2–3 business path options and monetization strategies for his AI freelancing business.
- **Paul Miller** will experiment with the OSS model via OpenRouter over the next few days and post feedback to the community forum.
- **Ryan C (from Northern Ireland)** will reach out to Patrick via DM on the School platform about the AI news aggregation approach for a content generation project.