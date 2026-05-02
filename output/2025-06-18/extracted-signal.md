## general

This was a weekly group coaching call hosted by Brandon Hancock for a community of AI developers and builders. The session opened with announcements: a rescheduled Crew AI call with Joe (moved to Friday), an upcoming guest speaker session with Dan Martell (an AI business incubator operator, tentatively July 1st), and Brandon's new project called Shipkit — a template-driven system to help developers launch AI applications faster. Brandon also highlighted the LangChain Interrupt 2025 conference playlist as a recommended resource.

The bulk of the call was structured as a round-robin where each member shared project updates and asked questions. Topics ranged from RAG architecture and chunking strategies, ADK (Google Agent Development Kit) agent design, Supabase vector stores, LangChain vs. LangGraph vs. ADK comparisons, browser-based agents, eval strategies, LinkedIn growth tactics, and freelance pricing models. Several members demoed live projects including a legal RAG assistant, a grant proposal generator, a Telegram bot, a machine learning pipeline agent, and a real-time voice agent built with LiveKit and Gemini.

The call also featured a substantive side discussion on whether AI will replace developers, with perspectives ranging from "teams will shrink but not disappear" to observations from the Cursor AI founder about the gap between current capabilities and million-line codebases. Brandon and community members shared thoughts on the emerging opportunity for one-person developer shops charging $5K–$20K for custom AI solutions.

A recurring theme was the importance of looking at your data at every step of a RAG pipeline, using semantic chunking over fixed chunking, and leveraging Context7 (an MCP server providing access to ~19,000 library docs) to dramatically improve AI-assisted coding accuracy.

## insights

- **Semantic chunking over fixed chunking**: Fixed chunking with no overlap is easy but often produces substantially worse RAG results; inspecting chunk boundaries and splitting semantically is worth the extra effort, especially given large modern context windows.
- **Large context windows reduce the need for RAG in some workflows**: Andrew Nanton noted that as context windows have grown, he's moved away from RAG toward assembling larger pieces of context manually for his use case.
- **For ADK tool calls, always return dictionaries and include a docstring**: Brandon flagged that returning a string instead of a dict can cause silent failures in ADK, and the docstring is how the agent understands what the tool does.
- **Don't default to multi-agent for simple RAG**: Brandon advised that basic vector store queries don't need a full agent — a direct LLM call with RAG context is often sufficient; agents are warranted when you need planning, loops, and dynamic tool calling.
- **Context7 MCP server is a cheat code for AI-assisted development**: By pointing Cursor to the Context7 remote URL, the agent can look up accurate, up-to-date docs for ~19,000 libraries on demand, dramatically reducing hallucinated API usage.
- **Spec docs + implementation plans + fresh context windows = reliable agentic development workflow**: Andrew Nanton described settling into a groove of maintaining spec and implementation plan documents, starting fresh context windows per step, and having the LLM write tests.
- **LLMs default to what they know**: Andrew observed that choosing FastAPI over FastHTML was pragmatic — LLMs have millions of lines of FastAPI training data and essentially none for FastHTML, so the path of least resistance produces better results.
- **Manus AI's browser agent technique**: Bastian shared that Manus overlays CSS to delimit every interactive element on a page before the agent acts, giving the vision model a cleaner signal — more costly but significantly more reliable than raw HTML parsing.
- **ADK's biggest current limitation**: Brandon identified the inability to insert a pure code step (no agent, no tool call) as ADK's main weakness compared to LangGraph, though ADK's Flows partially address this.
- **ADK state management is excellent**: Brandon praised ADK's global state accessible through context across agents and tools as one of its strongest features.
- **RAG is the most monetizable AI skill right now**: Brandon noted that ~90% of freelance AI projects he's seen are RAG-based, and the fire chief documentation project and internal search engine project were both RAG.
- **Value-based pricing beats hourly for consulting**: Al Cole advised using "three whys" (why anything, why custom, why now) to help clients quantify the value of a solution, then pricing against that value rather than hours — especially important because prior learning isn't captured in hours logged.
- **LinkedIn growth hack**: Posting a tangible free asset (cursor rules, templates, workflows) and asking people to comment a keyword to receive it creates a viral comment loop that the algorithm amplifies far more than link posts or opinion pieces.
- **Lovable-to-Next.js migration via git submodule**: Brandon's current technique is adding the Lovable project as a git submodule, having Cursor reference it to recreate components in Next.js, then deleting the submodule when done.
- **Showing intermediate agent progress to non-technical clients matters**: Bastian noted that non-tech users expect step-by-step status updates during long agentic workflows; a polling-based status system (pending → processing → complete) dramatically improves perceived reliability.

## qa

**Q (alexrojas):** I'm building a RAG application for legal documents and currently using fixed chunking. Should I switch to semantic chunking, and does it make a big difference?
**A (Andrew Nanton / Brandon Hancock):** Andrew said that given large context windows today, it's worth looking at your chunks and splitting semantically at natural boundaries rather than fixed sizes, because shearing a chunk mid-context is very costly. Brandon agreed and suggested inspecting the data at every step; fixed chunking with no overlap will likely give substantially worse performance with very little effort needed to improve it.

**Q (alexrojas):** My RAG app uses Next.js and Supabase. I want to add ADK agents but the stack feels incompatible. What stack should I use to be more ADK-friendly?
**A (Brandon Hancock):** For basic RAG queries you don't need agents at all — a direct LLM call to your vector store returning context is sufficient. Agents are for planning, dynamic tool calling, and multi-step loops. For the Supabase integration, Brandon showed a `match_artifact_sections` database function using pgvector and RPC calls, and pointed to his existing Supabase YouTube video as a reference.

**Q (Marc Juretus):** In ADK, my tool is being called but returns nothing. What's wrong with the return format?
**A (Brandon Hancock):** ADK tool functions should always return a dictionary, not a string. They also need a docstring explaining what the tool does — that's how the agent understands the tool's purpose. The function parameters should also have type annotations.

**Q (Marc Juretus / Al Cole):** Will AI replace developers?
**A (Brandon Hancock / Al Cole / Mitch):** Brandon's view: teams will shrink but developers won't disappear because someone needs to be accountable, manage code, and answer questions. AI is progressing from static sites → CRUD → more complex backend infrastructure. Al noted that the Cursor AI founder said they're ~6 months from handling million-line codebases. Mitch cited a researcher (described as a father of LLMs) who believes generative text models are a tool for higher-level intelligence, not a replacement for it.

**Q (Andrew Nanton):** Are people having success with Claude Code, Codex, or other agentic coding systems vs. Cursor?
**A (Brandon Hancock / Bastian Venegas):** Brandon hasn't found a compelling reason to leave Cursor — he prefers actively seeing and iterating on code rather than spinning off background jobs. Bastian noted that Codex works better with an `agents.md` file (like cursor rules for agents), supports multiple parallel solution variants, and has internet/package access. Both agreed the use case for fully autonomous background coding agents hasn't clicked yet for their workflows.

**Q (Juan Torres):** My agentic system works on CSV files. How do I give it access to a PostgreSQL database?
**A (Brandon Hancock):** Keep it simple — create straightforward tool functions for the SQL operations you need (create, update, read rows) and add them to your Crew AI agent. A full MCP server is overkill for a single tool. If using an ORM it's even easier. Al Cole added a follow-up question about whether data is one-time or needs change-triggered reprocessing, which Juan confirmed is one-time.

**Q (AbdulShakur Abdullah):** What's the best way to grow on LinkedIn?
**A (Brandon Hancock):** Build a tangible free asset (e.g., cursor rules, a template, a workflow), post about it, and ask people to comment a specific keyword to receive it. This creates a comment loop the algorithm amplifies. Linking externally (e.g., to YouTube) does reduce reach. Summarizing bigger creators' content and tagging them is another growth lever.

**Q (Robert):** When developing with Cursor AI and AI tools, what's the right term to use on a resume?
**A (Brandon Hancock):** "AI-driven development" or "agentic development" are both reasonable terms to describe the skill.

**Q (Bastian Venegas):** Have you tried Convex for RAG applications?
**A (Brandon Hancock):** Not yet for RAG specifically. Convex looks great for chat and regular databases, but Brandon hasn't confirmed it supports custom document embedding workflows (inserting your own vectors from processed documents). That uncertainty has kept him on Supabase. If Bastian tries it and confirms RAG support, Brandon would consider switching.

**Q (Al Cole):** Does anyone have bad experiences with LangChain/LangGraph?
**A (Brandon Hancock / Marc Juretus):** Brandon found LangChain's most valuable parts were React agents and RAG/chunking; most other abstractions felt like overkill vs. direct LLM calls. LangGraph added more power but required significant setup for graph/state management. Marc's group found Crew AI much simpler for their YouTube summarization workflow after struggling with LangChain. Brandon acknowledged his views are from ~a year ago and wants to revisit given the Interrupt conference demos.

## tools

- **Chunky** — Python library for semantic chunking; alexrojas exploring it for legal RAG app vs. fixed-size chunks
- **Supabase** — Primary vector store and database stack; used with pgvector, RPC functions, and Drizzle ORM for RAG applications
- **Google ADK (Agent Development Kit)** — Core agentic framework discussed throughout; multiple members building with it
- **Crew AI** — Multi-agent framework; Brandon has upcoming call with Joe from Crew AI; used by Juan Torres for vendor extraction
- **LangChain / LangGraph** — Discussed as alternative agentic frameworks; Al Cole exploring LangSmith for evals
- **Context7** — MCP server providing access to ~19,000 library docs; demonstrated live pulling Google ADK and Next.js docs into Cursor
- **Cursor** — Primary AI-assisted coding IDE used by most members; discussed vs. Claude Code/Codex
- **Lovable** — Vite-based AI app builder; Brandon showed git submodule technique to port projects to Next.js
- **Next.js** — Primary frontend framework; used by alexrojas, AK (Dharma House), and Brandon
- **Vercel AI SDK** — Used for chat/streaming functionality in Next.js AI applications
- **FastAPI** — Andrew Nanton's backend choice for local file processing app; preferred because LLMs know it well
- **Tauri** — Rust-based Electron alternative Andrew Nanton is using for a desktop application
- **Azure Document Intelligence** — Andrew using it to parse large multi-section documents into JSON hierarchy
- **Railway** — Deployment platform; Aleksandr deployed Telegram bot; Mitch considering for Python backend
- **Firebase / Google Cloud Storage (GCS)** — AK (Dharma House) using for artifact storage in grant proposal app
- **Drizzle ORM** — Used with Supabase to manage migrations and create database functions as code
- **spaCy (en_core_web_sm)** — 15MB NER model Juan Torres using in hybrid LLM + ML vendor name extraction system
- **GenSpark AI** — Agentic browser tool Paul Miller is using for scraping retail sites with bot detection
- **LiveKit** — Voice agent platform Bastian used to build real-time multimodal agent with phone number support
- **Gemini Live API** — Used by Bastian for real-time voice agent with built-in Google Search tool
- **Perplexity Labs** — Abdul mentioned as potential agentic browser/search tool (paid tier)
- **Firecrawl** — Web scraping/crawling service; Brandon attempted to recreate it for browser agent, gave up
- **LangSmith** — LangChain's eval and prompt management platform; Al Cole exploring after Interrupt conference
- **Timescale / PGAI** — Postgres extension bringing AI/embedding capabilities into the database; Al Cole researching for enterprise partner opportunity
- **EDB (EnterpriseDB)** — Enterprise Postgres company building AI agent factory; Al Cole evaluating as partner ecosystem
- **Convex** — Database platform with TypeScript-native API; Bastian following T3 chat migration to it
- **DataButton** — Y Combinator startup with template-based app building; Jake mentioned as comparable to Shipkit concept
- **Manus AI** — Browser agent that uses CSS overlay + vision model to identify page elements reliably
- **Claude Code / OpenAI Codex** — Autonomous background coding agents; discussed as alternatives to Cursor

## links

- **LangChain Interrupt 2025 playlist** — YouTube playlist with ~11 videos on enterprise agentic applications (Uber, JP Morgan, Andrew Ng); Brandon dropped in chat and plans to make a summary video
- **Context7 MCP server** — `https://context7.com` (remote MCP URL) — Brandon shared the one-line config to add to `.cursor/mcp` for access to 19,000 library docs
- **Brandon's Supabase YouTube video** — Existing video on building RAG with Supabase; referenced as directly applicable to alexrojas's legal RAG project
- **Y Combinator interview with Michael Truel (Cursor AI founder)** — Al Cole referenced this recent interview about Cursor's current capabilities and roadmap toward million-line codebases
- **David Shapiro YouTube channel** — Post-labor economics content; Brandon mentioned as interesting viewing on AI's economic impact
- **GenSpark AI** — `https://genspark.ai` — Paul Miller shared in chat; agentic browser for scraping sites with bot detection
- **Lovable-to-Next.js migration template** — Brandon dropped as a file in the group chat; work-in-progress prompt template for porting Lovable projects
- **Bastian's two Interrupt conference links** — Two specific videos from the Interrupt playlist dropped in chat: one by Andrew Ng on evals, one dedicated eval talk

## decisions

- **Brandon** will connect alexrojas with a video editor contact (Abdul) via DM after the call
- **Brandon** will follow up with the potential elderly companion voice agent client after the call
- **Brandon** will work on a summary/breakdown video of the LangChain Interrupt 2025 playlist, targeting the next day
- **Brandon** will lock down the Dan Martell guest speaker session for approximately July 1st and post an update to the community
- **Brandon** will continue building Shipkit (AI application template library) and post an update later in the week, including early access to prompts/templates for community members
- **Brandon** will create a video on migrating from Lovable to Next.js once the template/prompt is fully flushed out
- **alexrojas** will try semantic chunking in Chunky and compare results against fixed 500-token chunks
- **AK (Dharma House)** will deploy the grant proposal app to Vercel before the Friday client presentation
- **AK (Dharma House)** will add React Markdown rendering to replace raw markdown output (Brandon shared code snippet in school/chat)
- **AK (Dharma House)** will prepare two additional scoped options (V0.5 and V1) to present alongside the POC on Friday
- **Bastian** will investigate whether Convex supports custom document embedding/RAG workflows and report back to Brandon
- **AbdulShakur** will try the "comment a keyword to get the free asset" LinkedIn tactic and report results
- **Robert** will create a LinkedIn post using the giver/asset method and tag Brandon for feedback
- **Al Cole** will begin hands-on work with LangGraph/LangSmith and share learnings with the group