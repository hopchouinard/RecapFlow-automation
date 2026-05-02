## general

This was a weekly group coaching/community call hosted by Paul Miller in Brandon's absence (Brandon was on vacation). The session followed a familiar format: an open Q&A period at the start, followed by a round-robin update from each participant. Roughly 15 participants joined from across time zones (US, Europe, Australia).

The call opened with discussion of two major model releases that had just dropped: OpenAI's new open-source model and Claude Opus 4.1. Participants shared early impressions of running the OpenAI model locally on consumer hardware. The round-robin then covered a wide range of topics including Claude Code rate limits and token burn rates, RAG tooling (Llama Index, GraphRAG with Kuzu), N8N for client prototyping, eval strategies, Cursor alternatives, and the broader question of whether AI tooling subsidies are sustainable.

Several participants shared project updates: Abdul is building an ICP-generation workflow for a Korean client in the environmental/pharma space; Mitch is building a VO3 video generation pipeline; Patrick demonstrated a ChatGPT agent-mode workflow that autonomously read and categorized the School community board; Andrew is working on GraphRAG with Kuzu and Llama Index; Al is pursuing property management and digital marketing automation clients; and Adam attended networking events to find leads. New members Abhi and Stephen introduced themselves, with Abhi exploring Google ADK for L1/L2 support automation and Stephen working on an observability platform.

The session closed with a broader discussion about the AI "bubble," the sustainability of current pricing models, the trajectory of local/open-weight models, and recommended sources for staying current (Simon Willison, Cole Medin, Prompt Engineer/Mohamed).

## insights

- **Don't try to correct Claude Code more than twice when it goes off the rails** — Andrew's rule of thumb: if it starts doing weird things, zero out the context window and start a fresh session with a clean design document and implementation plan.
- **Spend the majority of time in planning mode before writing a single line of code** — Andrew keeps Claude Code in plan mode (Shift+Tab), feeds it documentation, asks clarifying questions, and only exits planning when fully satisfied. This burns far fewer tokens than letting it code freely.
- **Ask the model to ask you clarifying questions** — prompting with "ask me any necessary clarifying questions" surfaces assumptions you haven't thought through and prevents downstream hallucinations and detours.
- **Maintain a living implementation plan file** — Andrew keeps a design doc (overall architecture), an implementation plan (next steps), and a development log. The model deletes completed items from the plan and adds them to the log, preserving context across sessions.
- **N8N is powerful for client POCs but can break catastrophically at scale** — Jake: individual nodes must be tested; debugging 200+ node workflows is very hard. Best used as a prototype/sell tool, not necessarily production.
- **Showing a client a quick N8N POC can backfire on scope** — demonstrating something in 15 minutes gives clients the impression the whole project is trivial, leading to runaway scope expansion. Jake and Bastian both noted this tension.
- **LLM-as-judge with rubrics (0–5 or boolean) is the practical starting point for evals** — Bastian: start manually, then move to LLM-as-judge. Hallucination may not be the most critical metric depending on the use case and whether users can self-detect it.
- **Clients often won't pay for evals** — Jake: they want quality output but resist paying for the evaluation work that ensures it. Framing evals as a billable line item is a recurring challenge.
- **Split token usage across multiple free/cheap tools to avoid hitting limits** — Patrick's workflow: GitHub Copilot for proto-prompt autocomplete → Gemini CLI for documentation generation → Claude Code only for actual task execution → Cursor for targeted debugging. Stays on $20/month across all tools.
- **N8N workflows are JSON; this opens a path to auto-converting prototypes into production Python code** — Al and Patrick identified that N8N's JSON export could serve as a machine-readable spec for generating equivalent Python services via Cursor/Claude Code.
- **Context7 crawls GitHub repos, not arbitrary URLs** — Bastian confirmed it requires a GitHub repo link and builds its own documentation from that; it won't accept llm.txt or standard documentation URLs directly.
- **The "free lunch" era of AI tooling is ending** — multiple participants noted that even $200/month plans likely don't cover actual compute costs, and pricing will need to rise or efficiency must improve dramatically.
- **Local/open-weight models are becoming plausible for basic tasks** — Andrew: GLM 4.5 Air (44GB) one-shot coded Space Invaders on a 64GB MacBook. Patrick: give it another year and most routine LLM tasks may run locally, reserving cloud models for complex work.
- **For client-facing demos, UI/UX quality signals credibility** — Paul: clients judge you by the front end. Using Lovable for a polished UI backed by FastAPI is a fast path to looking professional.
- **When a session gets on the wrong track in WSL/Docker environments, restart rather than debug** — Sam: if Claude Code starts on the wrong track in a WSL session, it's often faster to restart the whole session than to try to recover.

## qa

**Q (AbdulShakur):** Has anyone had success editing Opal flows after the initial one-shot prompt? I can't get it to add new logic without breaking things.
**A (Paul Miller):** I found it really good for generating prompts rather than iterative editing. The engine is solid for initial generation but editing is limited.

**Q (Jake):** Andrew, are you still using Claude Code? Are you seeing the rate limiting issues?
**A (Andrew):** Yes, still using it — it suits my workflow because I do other things in the background and need something autonomous. But I do see it going off the rails and doing nonsense. My rule: don't tell it more than twice it's wrong — just zero out the context and start over with a fresh session and design document.

**Q (Al):** Is there a way to understand your Claude Code burn rate before the new limits kick in?
**A (Jake/Bastian):** The dashboard used to show remaining requests clearly (like Cursor did) but that's gone. The new limits officially kick in around the 27th of the month. On the $20 plan, heavy usage burns through in about four days.

**Q (Al):** How hard would it be to convert N8N JSON exports into a Python equivalent using Cursor/Claude Code?
**A (Patrick/Jake/Andrew):** N8N is pure JSON, so it's feasible. Patrick suggested using the JSON as a spec fed into a prompt that translates it into a proper coding spec for Cursor or Claude Code. Andrew found a GitHub repo attempting this but it hadn't been touched in months. Jake noted N8N has an MCP that understands all nodes (similar to Context7) but it's currently broken for him.

**Q (Andrew):** Is there a danger that showing clients a quick N8N POC makes them think the whole project is trivial?
**A (Jake):** Yes — you show a simple POC to demonstrate feasibility, not the full complexity. Executives don't want to see 500 nodes; they want the solution. The risk is scope creep when they say "if it's that easy, can we add X, Y, Z?" The POC also creates client ownership and buy-in, which is valuable, but you have to manage expectations carefully.

**Q (Andrew):** What tools or strategies do you use for evals?
**A (Jake/Bastian):** Jake: evals are "secret sauce" — start with hallucination checks, use LLM-as-judge, do spot-check manual reviews, then hand data to the client for their own review (and charge for it if they want comprehensive coverage). Bastian: use rubrics (0–5 or boolean), start manually, then LLM-as-judge. First figure out what's actually valuable to users — hallucination may not be the top priority if users can self-detect it. Build in phases so you can iterate based on real user feedback.

**Q (Neel):** Has anyone tried building a RAG over their own code examples to improve vibe coding results?
**A (Andrew/Bastian):** Andrew: he manually provides specific documentation pages or saves trimmed markdown files in the repo and references them with @mentions. For libraries, Context7 works well. Bastian: recommended Repoprompt, which has an MCP server that runs locally, connects to any IDE, and handles context management and semantic search across the codebase better than Cursor's built-in search.

**Q (Neel):** For a data science portfolio project, should I use Streamlit/Gradio or Next.js for the UI?
**A (Jake/Marc/Paul/Prem):** Jake: Streamlit feels limiting; recommends Lovable for a polished front end. Marc: Next.js is easy with Cursor — just scaffold it via CLI and prompt Cursor to build pages consuming your FastAPI endpoints. Paul: commercially, UI/UX quality signals credibility to clients; Lovable + FastAPI backend is a fast path. Prem: Cursor-generated Next.js UI exceeded what any graphic designer produced, with minimal manual intervention.

**Q (Neel):** Has anyone moved away from Cursor to alternatives like Kiro or Trae?
**A (Asako/Mitch/Patrick):** Asako: Kiro gives very detailed plans before coding, making it easier to correct direction early, but it generates overly defensive production-grade code for simple mockups. Mitch: Kiro's PRD/requirements/design/task workflow is excellent; Warp is also good and lenient on usage. Patrick: uses GitHub Copilot + Gemini CLI for planning/documentation, then Claude Code for execution, and Cursor only for targeted debugging — stays on $20/month total.

**Q (StephenAmstutz):** Where do you go for reliable news about upcoming model releases?
**A (Paul/Andrew):** Simon Willison's blog (simonwillison.net), Cole Medin's YouTube channel, Prompt Engineer (Mohamed). Paul cautioned that most YouTube coverage is just reading off press releases — look for people who actually benchmark and test. Also recommended going back through previous call summaries in the School community.

## tools

- **OpenAI open-source model (20B)** — Just released; participants tested it in LM Studio; ran at 33 tokens/sec on two GTX 1080 Ti GPUs; 128K context window; tool calls tested with Perplexity MCP server
- **LM Studio** — Used by Andrew to run the new OpenAI open-source model locally
- **Claude Opus 4.1** — Tested by Andrew in Claude Code; described as incremental improvement with small gains across most evals
- **Claude Code** — Primary agentic coding tool for Andrew and others; rate limiting and context drift discussed at length
- **Cursor** — IDE used by multiple participants; token burn rate increasing significantly; $20/month plan depleting in ~4 days of heavy use
- **Opal (Google)** — Agent-building tool using prompting/visual flows; AbdulShakur used it to build an ICP-generation workflow; editing after initial generation is unreliable
- **TLDraw** — Diagramming tool similar to Excalidraw; Bastian mentioned it has a new Gemini-powered feature similar to Opal, funded by Google credits
- **N8N** — No-code workflow automation platform; used for client POCs, prototyping, and production workflows; SOC 2 Type 1/2 and HIPAA compliant (paid tier); JSON-based architecture discussed
- **Context7** — MCP that fetches up-to-date documentation from GitHub repos; used to feed library docs into Claude Code; requires GitHub repo URL, not arbitrary web URLs
- **Llama Index** — RAG-focused Python framework; Andrew using it for GraphRAG; TypeScript implementation lags Python; has Notebook LM-equivalent and RAG-as-MCP starter projects
- **Kuzu** — Embedded graph database (like SQLite for graphs); Andrew using it with Llama Index for GraphRAG; no server required, file-on-disk
- **BAML** — New framework focused on structured data extraction from LLMs; mentioned by Andrew as worth watching
- **Pydantic AI** — Agentic RAG framework; Jake used it briefly; Andrew looked at it but didn't get far
- **Convex** — Backend-as-a-service with built-in RAG, real-time sync, and agent credits; used by Jake and Bastian; has an MCP server
- **Google ADK (Agent Development Kit)** — Used by Abhi for L1/L2 support automation POC and by Neel for a data drift detection portfolio project
- **Gemini CLI** — Used by Patrick and Neel as a near-unlimited-token tool for documentation generation and planning; known issue with string replacement/deletion in files
- **GitHub Copilot** — Used by Patrick for proto-prompt autocomplete in his layered token-saving workflow
- **ChatGPT agent mode** — Used by Patrick to autonomously scrape and categorize the School community board; 40 uses/month on $20 plan; supports scheduled tasks; works best under 30 minutes per run
- **Perplexity MCP server** — Tested with the new OpenAI open-source model for tool calls by Patrick
- **Apify** — Mentioned by Paul for scraping Google reviews to research client industries (e.g., property management competitors)
- **Repoprompt** — Tool with a local MCP server for context management and semantic search across codebases; Bastian recommended it as better than Cursor's built-in search
- **Kiro (AWS)** — Agentic IDE with structured PRD/requirements/design/task workflow; multiple participants on waitlist; Asako and Mitch have access; generates production-grade code
- **Warp** — Terminal/IDE alternative; Mitch using it; lenient on usage limits as Warp pays the API costs
- **OpenCode** — Console-based coding tool similar to Claude Code; Mitch testing it with O3 using his own API keys
- **Trae (T-R-A-E)** — AI coding assistant mentioned by Neel; link shared in chat; not yet tested by the group
- **Lovable** — AI-powered front-end builder; recommended by Jake and Paul for polished client-facing UIs
- **Next.js** — Frontend framework; Marc and Prem use it with Cursor for rapid UI generation on top of FastAPI backends
- **Supabase** — Used by Marc for database and authentication in Next.js apps; also used by Mitch as backend with webhooks to Google Cloud Functions
- **LangGraph** — Mentioned as a production-grade alternative to N8N for complex agentic workflows; Brandon is a fan
- **Crew AI** — Multi-agent framework; Marc uses it for fantasy sports summaries; mentioned as common in job postings
- **Open Router** — API aggregator; used by some participants to access Claude and other models; rate limiting observed
- **Streamlit / Gradio** — Python UI frameworks for data science demos; discussed as alternatives to Next.js for portfolio projects
- **GLM 4.5 Air** — Open-weight model (44GB); Andrew referenced Simon Willison's eval where it one-shot coded Space Invaders on a 64GB MacBook
- **Kimi-K2** — Open-source model from Moonshot AI; Jake mentioned it as exciting but requiring very powerful hardware
- **VO3 (Google)** — Video generation model; Mitch building a pipeline around it; API costs ~$1 per 5-second clip; Chinese alternatives emerging
- **ComfyUI** — Mentioned by Paul as promising for video generation workflows

## links

- **simonwillison.net** — Simon Willison's blog; recommended as a reliable, hands-on source for AI model evaluations and news
- **N8N-to-code MCP/converter (GitHub repo)** — Andrew found a repo attempting to convert N8N JSON flows to code; shared in chat but noted it hasn't been updated in months (specific URL not captured in transcript)
- **AbdulShakur's prompt-maker prompt** — Shared in chat; a meta-prompt that iteratively extracts intent through back-and-forth conversation before generating a final prompt
- **Trae AI tool** — Link shared by Neel in chat (specific URL not captured in transcript)
- **GLM 4.5 Air Space Invaders eval** — Simon Willison's post showing the model one-shotting Space Invaders; Andrew posted link in chat (specific URL not captured)
- **Ed Zitron video on AI bubble** — AbdulShakur dropped a link in chat; Zitron argues foundation model companies are heavily subsidizing user costs and the economics are unsustainable

## decisions

- **AbdulShakur** will post his Korean client opportunity (seeking US contacts in environmental/pharmaceutical industries for customer discovery calls) to the School community board.
- **AbdulShakur** will share his prompt-maker prompt in the chat for others to use.
- **Al Cole** will research using N8N JSON exports as a spec to generate Python equivalents — identified as a potential side project.
- **Al Cole** will use Apify to scrape Google reviews of property management companies to better understand client pain points before his first meetings this week.
- **Al Cole** will nail down scope with his property management client before proceeding, given the scope keeps shifting with each email exchange.
- **Marc Juretus** will explore N8N as a tool for building client-facing prototypes, in addition to his current code-first approach.
- **Patrick Chouinard** will investigate accessing ChatGPT agent mode via API rather than the web interface for his community-monitoring workflow.
- **Patrick Chouinard** will continue posting findings as GitHub repos with Markdown rather than blog posts, as it serves the community better.
- **Neel More** will try Lovable for the front-end UI of his data drift detection portfolio project.
- **Neel More** will look into OpenCode (Mitch's suggestion) as a Cursor alternative.
- **StephenAmstutz** will review previous call summaries in the School community to get up to speed on tools and discussions.