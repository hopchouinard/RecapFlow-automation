## general

This coaching call was a Monday session (shifted from the usual Tuesday due to Brandon Hancock's wife's birthday) with a mix of returning members and several first-time attendees. Brandon hosted, and the session followed a round-robin format where participants shared wins, projects, and questions.

Patrick Chouinard led off with two major projects: a research pipeline built using spec-driven development with SpecKit and Gemini CLI, and a prompt library concept built on a simple RAG example. He also introduced the group to a VS Code/Cursor extension called SpecStory, which saves AI chat logs to markdown and can extract cursor rules or GitHub instructions from them. Patrick is using Claude 4.5 to generate training course material from exported SpecKit chat logs.

Ty Wells demonstrated a ShipKit Studio-style web application he built on top of ShipKit's project scaffolding process, adding a GUI for logo generation, wireframing, DB schema visualization, and (in progress) live code deployment via E2B. He also showed a voice-based learning app built on Lovable using Eleven Labs for text-to-speech, which teaches topics at a configurable expertise level and quizzes users. New members Nick Mohler, Glenn Marcus, Ryan (One Stop Creative Agency), and Lan each introduced themselves and received tailored advice. Glenn discussed the Warp terminal's Drive feature for syncing markdown context across sessions. Lan asked about handling 50M-record real estate datasets and brownfield project refactoring. David, a CFO returning after several months, asked about enterprise AI integration with ERP systems like NetSuite.

Brandon closed several threads with recommendations around productized services, awareness-building, PostHog dashboard filtering, Playwright for UI testing, Supabase + PostGIS for geospatial real estate data, and Claude for Financial Services for regulated enterprise environments.

## insights

- **Patrick:** Building individual prompts and sub-agents first, then adding scaffolding around them, is more reliable than asking a model to generate an entire novel workflow it has no training examples for.
- **Patrick:** SpecStory lets you export AI chat logs to markdown and infer cursor rules or GitHub Copilot instructions from real development sessions — useful for both documentation and training material generation.
- **Brandon:** Decomposing repetitive tasks into specialist "skill" agents (e.g., YouTube title generator, hook writer) and chaining them creates compounding leverage; the only irreplaceable parts are high-level creative and domain-specific work.
- **Brandon:** When building AI workflows, always clarify inputs and desired outputs before writing any code or choosing a database — "what are we trying to do with this data?" is the first question.
- **Brandon:** For large geospatial datasets, Postgres + PostGIS extension is strongly preferred over flat files; it indexes lat/long efficiently for neighborhood-level queries across millions of records.
- **Brandon:** The recommended path for new AI workflows: get it working locally with Claude Code agents first, then migrate to a deployed web application — don't start with cloud complexity.
- **Patrick:** In corporate/enterprise settings, start MCP integrations as read-only; never allow write access to ERP systems until the agent has been thoroughly tested.
- **Patrick:** Claude for Financial Services provides contractual data isolation, audit trails, and SOC-compliance features that generic cloud deployments (including Bedrock) may not offer, especially for data residency requirements.
- **Glenn Marcus:** AI represents a "complete reset" — there are no 10-year experts, making it one of the few technology inflection points where everyone competes on a level playing field.
- **Brandon:** Marrying AI with a non-developer vertical (video production, real estate, finance) creates a much smaller competitive market than pure AI development.
- **Ryan:** Building a productized service (social media management + video) with AI automation shifts the business model from hourly billing to scalable outcome delivery.
- **Brandon:** The biggest bottleneck for most developers is not technical skill but awareness — people need to know you exist and what you can do.
- **Ty:** Struggles from a year ago in AI tooling are now baseline assumptions; the pace of improvement means entering now is still very early.

## qa

**Q (Tom Welsh):** What's the difference between specs in SpecKit and tasks in ShipKit?
**A (Patrick Chouinard):** In SpecKit, a spec is the overall specification including user story and requirements; tasks are sub-items within the spec.

**Q (Brandon Hancock):** What is SpecStory and what does it do?
**A (Patrick Chouinard):** It's a VS Code/Cursor extension that saves your AI chat logs to markdown files and lets you infer cursor rules or GitHub Copilot instructions from those logs.

**Q (Brandon Hancock):** How are you using Gemini CLI access — are you on the free tier?
**A (Patrick Chouinard):** Yes, free tier. He was accepted off the waitlist for Gemini 3 access on Gemini CLI without needing the Ultra plan, likely because he runs hundreds of calls per day.

**Q (Prem):** For PostHog, should you use separate projects per environment or one project with environment variables?
**A (Brandon Hancock):** Use one project and filter out localhost traffic at the dashboard level using event property filters. The easiest way is to ask the PostHog MCP to add the filter for you.

**Q (Prem):** Any good resources for getting started with Playwright?
**A (Brandon Hancock):** Watch Web Dev Dan (IndieDevDan) on YouTube — he just released a video on sub-agents each spinning up a Playwright instance for UI testing. Add Playwright as an MCP tool and use it for UI testing and end-to-end test suites.

**Q (Lan):** For a 50M-record real estate dataset, should data be stored as CSV, Parquet, or a relational database?
**A (Brandon Hancock / Patrick Chouinard):** Start with Excel pivot tables and Copilot for exploration. For production, use Postgres with the PostGIS extension for geospatial indexing. Parquet is fine for local processing; pandas can handle large files. For 50M records, Excel will hit limits — chunk the data or move to Power BI / Postgres.

**Q (Lan):** Should I restart my brownfield vibe-coded project from scratch using ShipKit, or refactor the existing one?
**A (Brandon Hancock):** It will eventually become a new project, but the goal is to build it properly for deployment as a web application. Use Supabase (free tier to start), seed the database from your existing files, and add PostGIS for geospatial queries.

**Q (David):** What is the best model for interacting with new APIs in an agentic context?
**A (Brandon Hancock):** Claude Opus 4.5 (Anthropic) is currently the best tool-calling model. Pair it with Claude Code locally, then add MCP servers for each API (e.g., NetSuite). If no MCP exists, ask Claude Code to build one from the API documentation.

**Q (David):** What are the security and architecture considerations for deploying AI agents inside a corporate environment?
**A (Brandon Hancock / Patrick Chouinard / Ryan):** Start read-only on all integrations. Be aware of GDPR and data residency laws — some Bedrock models are not available in all geographic regions. For regulated industries, Claude for Financial Services provides contractual data isolation, audit trails, and SOC compliance. OpenAI also has an enterprise tier that doesn't use data for training. Local/on-prem models are an option but require significant hardware investment and the best tool-calling models (Sonnet, Opus) are proprietary.

## tools

- **SpecStory** — VS Code/Cursor extension that exports AI chat logs to markdown and extracts cursor rules or GitHub instructions
- **Gemini CLI** — Used by Patrick as both a search engine and HTML generation engine for his research pipeline; he has free Gemini 3 access via waitlist
- **Claude Code** — Primary local AI coding agent used throughout; discussed at $100 and $200/month subscription tiers
- **ShipKit** — Brandon's project scaffolding framework; Ty built a GUI wrapper ("ShipKit Studio") on top of it
- **SpecKit** — Spec-driven development framework used by Patrick for internal application building and training course creation
- **Supabase** — Recommended backend for Lan's real estate app; also used by Ty via Lovable's built-in Supabase integration
- **PostGIS** — Postgres extension recommended for geospatial indexing of real estate records by lat/long
- **Eleven Labs** — Text-to-speech API used by Ty in his voice-based learning app (likely V2 model)
- **E2B** — Cloud sandbox service Ty is integrating for live code deployment from his ShipKit Studio app
- **Playwright** — Browser automation/testing tool recommended as an MCP for UI testing and end-to-end test suites
- **PostHog** — Analytics platform; discussed for filtering localhost traffic from dashboards using its MCP
- **Lovable** — No-code web app builder used by Ty to build his learning app; includes built-in Supabase backend
- **Warp (warp.dev)** — Terminal with built-in AI agent; Glenn discussed its Drive feature for syncing markdown context across sessions
- **Fabric** — Daniel Miessler's open-source AI tool, mentioned briefly in context of Kaiya/personal assistant projects
- **Kaiya (KAI)** — Daniel Miessler's personal AI assistant project, referenced by Ty as a project structure tool
- **LangGraph / LangChain** — Mentioned by Brandon as the enterprise-grade agent framework; planned for deeper ShipKit coverage in January
- **Claude for Financial Services** — Anthropic's regulated-industry offering with audit trails, data isolation, and SOC compliance; recommended by Patrick for enterprise ERP integrations
- **Power BI** — Mentioned as the appropriate tool for large-scale data analysis beyond Excel's limits
- **pandas** — Python library recommended for processing large CSV/Parquet files locally with Claude Code
- **FFMPEG** — Mentioned for chunking videos before passing to Gemini API (400MB limit per upload)
- **Nano Banana (Google Imagen/Gemini image model)** — Used by Adam to redesign a hot sauce label; Brandon noted it can replace thumbnail designers for ~$0.14
- **NetSuite** — ERP system David wants to connect to AI agents via MCP; Brandon searched for an existing NetSuite MCP
- **Obsidian** — Nick's current markdown knowledge base tool; he is planning to migrate to Claude Code
- **Web Dev Dan (IndieDevDan)** — YouTube channel cited as top Claude Code educational resource; Scott shared a link

## links

- **SpecStory extension** — Link dropped by Tom Welsh in chat (VS Code/Cursor marketplace)
- **IndieDevDan YouTube video on sub-agents + Playwright** — Referenced by Brandon; Scott posted a link in chat with his own breakdown of slash commands, MCPs, agents, and skills
- **Brandon's AI video generation YouTube video** — Shared in chat for Ryan and Lan; demonstrates decomposing a workflow into 7 prompt steps with a code repo
- **Brandon's AI video generation code repo** — Dropped in chat alongside the YouTube video link
- **Nicholas Cole YouTube channel (ghostwriting)** — Shared by Brandon for Ryan as inspiration for productized writing/social media services
- **Dan Martell coaching call recording (July)** — Brandon offered to drop the link; covers AI software business building strategies
- **Claude Code sandboxing/isolation guide** — Brandon dropped a link showing how to run Claude Code in an isolated sandbox with restricted network access
- **Claude for Financial Services** — Patrick pasted links in chat for the Anthropic enterprise financial services offering
- **NetSuite MCP search results** — Brandon pulled up a live search for existing NetSuite MCP servers during the call

## decisions

- **Patrick** will share his SpecStory + chat log → training material workflow with Brandon in a follow-up call after the session
- **Brandon** will upload the missing video for Section 7 (Generate Transcript deep dive) of the Worker Deep Dive course immediately after the call
- **Ty** will add his ShipKit Studio app to the ShipKit community repository once the E2B code deployment feature is working
- **Brandon** will publish a Black Friday/Cyber Monday deals video to YouTube immediately after the call
- **Scott** will post his Claude Desktop conversation document (breaking down slash commands, MCPs, agents, and skills) to the ShipKit school community
- **Patrick** will demonstrate his MCP concept (using ShipKit chat logs as source material) to Brandon in a separate follow-up call
- **Brandon** plans to build a "Prompt Dojo" SaaS product (prompt practice + grading) as a 2026 project
- **Brandon** will go deeper into LangGraph/LangChain within ShipKit content in January
- **Lan** will explore Excel + Copilot pivot tables as a first step for real estate data analysis before moving to a Postgres/Supabase architecture
- **David** will investigate Claude for Financial Services and the NetSuite MCP as starting points for enterprise ERP agent integration
- **Ryan** will watch Brandon's AI video generation video and explore using the Gemini API for video context extraction in his social media pipeline