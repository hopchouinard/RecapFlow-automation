## general

This was a weekly coaching call for the AI Developer Accelerator community, hosted by Brandon Hancock. The session followed a round-robin format where members shared project updates, wins, and technical challenges. Brandon opened with announcements about an upcoming ADK (Agent Development Kit) tutorial featuring a YouTube thumbnail cloner/generator, and a recently released three-hour ADK masterclass video.

The call featured a wide range of projects and backgrounds: Maksym demonstrated a live WhatsApp-based car sales assistant deployed for a Nissan dealership in Mexico; Paul discussed a property/real estate calculator app built with Lovable; AbdulShakur shared progress on a pharma business intelligence tool and pivoted toward an automated bio-news-to-infographic pipeline; Om Kundalini presented an eight-year geospatial art project mapping world mythologies and constellations onto Earth's terrain; Ty Wells demoed a high school graduation seating reservation system; Andrew Nanton raised a notable legal case involving AI-generated victim impact statements; Gaurav shared a Crawl4AI scraping issue; Premkumar described an ETL challenge involving 2,000 unstructured energy-savings PDFs; and Aaron (The Dharma House) discussed migrating a multi-agent executive assistant from LangChain to Google ADK.

Technical discussions covered database tooling (Neon, Drizzle ORM, Supabase, SQLite), AI coding environments (Cursor, Windsurf, Kline/Claude Code), HIPAA-compliant deployments on Azure/AWS, MCP server stability, voice-to-text prompting tools, and the architecture of Google ADK agents. The call ran approximately two and a half hours.

## insights

- **Maksym on cost efficiency:** Switching from Anthropic Claude to GPT-4.1 (via direct OpenAI API, not Azure) cut daily API costs from ~$40/day to ~$10/day while handling ~3,000 daily conversations — a 75% cost reduction.
- **Maksym on speed vs. evaluation:** For a real-time WhatsApp sales tool, response speed is the primary constraint; formal evals and staging environments were deprioritized in favor of fast production iteration with rapid user feedback loops.
- **Brandon on Supabase vs. Neon:** Supabase adds meaningful complexity (row-level security, RLS policies) that is unnecessary for simple CRUD apps; Neon is the recommended starting point for straightforward Postgres needs. Supabase becomes the right choice when vector stores are needed.
- **Tom on Drizzle ORM portability:** Switching between Postgres databases with Drizzle only requires changing the dialect in the config — no SQL rewrites needed. This database-agnosticism is a major selling point.
- **Ty on Supabase + Lovable RLS bug:** Lovable 2.0 combined with Supabase's `security definer` and RLS policies can create infinite recursion loops — a known instability in that pairing.
- **Brandon on ADK architecture:** Google ADK's root/core agent is primarily a delegator, not a ReAct-style reasoner. For ReAct-like behavior, use "agents as tools" patterns where sub-agents are called as tool calls from the root agent.
- **Brandon on ADK evals:** ADK has built-in eval functionality that acts like unit tests for agents — you specify an input and expected sequence of actions, and it validates agent behavior.
- **Jake on Claude Max:** Claude Max ($100/month via claude.ai) handled complex interdependent ESLint/TypeScript errors without needing explicit clean-code rules in the prompt — it applied best practices automatically.
- **Tom on Windsurf as a linting escape hatch:** When Cursor gets stuck in circular linting error loops, switching the codebase to Windsurf to resolve the errors, then returning to Cursor, is a practical workaround.
- **Aaron on the competitive landscape:** A VC at the InfoBip conference noted that Copilot was expected to dominate AI coding tools, yet Cursor and Windsurf emerged as major competitors — reinforcing that small focused agents/tools can disrupt incumbents.
- **AbdulShakur on customer discovery:** Doing customer discovery early revealed that pharma business development teams preferred expensive curated databases over public data sources — saving months of misdirected development.
- **Brandon on feature flags:** For production systems without staging environments, feature flags (exposing new functionality to a subset of users) are a safer alternative to direct production deploys.

## qa

**Q (Juan Torres):** Which vector database are you using, how do you connect to WhatsApp, and how did you find your client?
**A (Maksym Liamin):** Supabase for both SQL and vector storage, with Voyage AI for embeddings. WhatsApp is connected directly via Meta's WhatsApp for Business API (no Make or n8n) deployed on Cloudflare Workers. The client came through a personal connection — a former executive at the dealership group.

**Q (Jake Maymar):** What exactly does Drizzle do that Neon can't do on its own?
**A (Brandon Hancock):** Neon is just the hosted Postgres database. Drizzle is an ORM (Object Relational Mapper) that sits between your application code and the database — it lets you define your schema in TypeScript, handles migration file generation, and converts raw database responses into typed objects your code can use. You push schema changes with a single command instead of writing raw SQL migrations manually.

**Q (Jake Maymar):** Is the ADK eval system a human-in-the-loop thing?
**A (Brandon Hancock):** No — think of it as unit tests for agents. You define an input and the expected sequence of steps the agent should take, and ADK validates whether the agent followed that sequence. It's automated, not human-reviewed.

**Q (Jake Maymar):** Is anyone doing HIPAA-compliant deployments, and what's involved?
**A (Maksym Liamin / Andrew Nanton):** Maksym has implemented HIPAA-compliant deployments on Azure and AWS — he recommends sticking to those two providers (not DigitalOcean or GCP) because the routing and protection configuration is complex. Andrew clarified that HIPAA is fundamentally insurance legislation; once a patient signs a HIPAA release, they control their own data. Supabase charges ~$600–700/month for HIPAA compliance, which is why Maksym and Andrew use Azure-hosted Postgres instead.

**Q (Ty Wells):** Should MCP server instructions go in user rules or project rules in Cursor?
**A (Brandon Hancock):** Project rules is the right place since MCP availability is project-specific. The reason reminders are needed at all is that agents burn through context windows quickly and the model may forget it has access to those tools. A one- or two-sentence reminder in project rules should prevent that.

**Q (Gaurav Shukla):** I'm getting a Unicode/encoding error when scraping with Crawl4AI — how do I fix it?
**A (Brandon Hancock):** The error is caused by a special character or emoji on the target webpage that breaks the decoder. The workaround is to pre-process/sanitize the raw HTML before passing it to the extraction step. As a practical shortcut, switch to Firecrawl — it handles these edge cases more robustly and has a generous free tier (3,000 credits for $19).

**Q (Premkumar):** What's the right approach to extract and standardize data from 2,000 PDFs with inconsistent table formats?
**A (Brandon Hancock / AbdulShakur):** Brandon suggested a wide-table approach — extract everything into a very wide schema (potentially 100+ columns) first, then use LLMs iteratively to reduce and normalize columns. AbdulShakur recommended first clustering PDFs by structural similarity (similar headers = same group), building separate narrow tables per cluster, then unioning them — this avoids hallucinated data and keeps each extraction step manageable.

**Q (Aaron / The Dharma House):** Can the ADK root agent be as dynamic as a full LangChain ReAct agent, or does it need to be broken into sub-agent logic?
**A (Brandon Hancock):** ADK's root agent is primarily a delegator, not a ReAct reasoner. To get ReAct-like behavior, use the "agents as tools" pattern — the root agent calls sub-agents as tool calls, which approximates the reason-then-act loop. The right architecture depends on seeing a whiteboard of the specific system.

## tools

- **Google ADK (Agent Development Kit)** — Primary focus of Brandon's recent tutorials; praised for combining chatbot and workflow agent capabilities with easy deployment
- **Fathom** — AI meeting recorder; mentioned briefly at the start of the call
- **GPT-4.1 (OpenAI)** — Used by Maksym's car sales bot; cited for instruction-following quality and speed vs. Claude
- **Supabase** — Used by Maksym for SQL + vector storage; discussed extensively re: RLS complexity, HIPAA pricing (~$600–700/month), and Lovable 2.0 compatibility issues
- **Voyage AI** — Embedding model used by Maksym for vector search in the car sales assistant
- **WhatsApp Business API (Meta)** — Direct integration used by Maksym's dealership bot without middleware
- **Cloudflare Workers** — Deployment target for Maksym's WhatsApp bot backend
- **Lovable** — No-code/low-code app builder; Brandon recommended it for UI; Lovable 2.0 noted as having stability issues with older projects
- **Neon** — Serverless Postgres database; recommended as the simplest hosted DB option with the best free tier
- **Drizzle ORM** — TypeScript ORM for schema management and migrations; recommended alongside Neon
- **Clerk** — Authentication tool; mentioned as part of Brandon's recommended stack for new apps
- **LightLLM (LiteLLM)** — Unified interface to all LLM providers; mentioned as simplifying multi-model agent development
- **OpenRouter** — Single marketplace to purchase tokens for any LLM model
- **Cursor** — Primary AI coding IDE used by Brandon and several members; annual subscription mentioned
- **Windsurf** — AI coding IDE; used as a fallback when Cursor gets stuck in linting loops; OpenAI acquisition discussed
- **Kline (Cline)** — AI coding agent; Michal switched to it after repeated manual rebuilds; memory bank feature highlighted
- **Claude 3.7 / Claude Max** — Anthropic model; Claude Max ($100/month) praised by Jake for autonomous clean-code behavior
- **Firecrawl** — Web scraping API; recommended over Crawl4AI for reliability; $19 for 3,000 credits
- **Crawl4AI** — Open-source web crawler; Gaurav encountered Unicode decoding errors with it
- **Browserlist / Browserbase** — Web scraping alternatives to Firecrawl; noted as more expensive
- **Resend** — Email sending API used by Ty for bulk graduation seat assignment emails; default rate limit of 20/2s, bumped to 50/2s on request
- **Twilio** — Messaging API; Michal using it for WhatsApp integration in his project
- **N8N** — Workflow automation platform; mentioned in context of HIPAA compliance costs
- **Azure AI Document Intelligence** — Used by Premkumar to extract text from energy-savings PDFs
- **Power BI** — Target visualization tool for Premkumar's PDF data pipeline
- **Upstash** — In-memory database / rate limiting tool; mentioned as useful MCP integration for production apps
- **PostHog** — Product analytics; mentioned as having an MCP integration in Cursor
- **Whisperflow** — Voice-to-text tool for dictating prompts; keyboard shortcut hold-to-speak; Windows-focused
- **MacWhisper** — Mac equivalent of Whisperflow for voice-to-text prompting
- **Limitless** — AI wearable/recorder; Paul received his device and is testing it
- **Otter AI** — AI meeting transcription; Paul mentioned using it previously
- **Kit (formerly ConvertKit)** — Email marketing platform recommended by Brandon for newsletter/lead capture; free tier includes one sequence and one automation
- **Descript (referenced as "TeleTV" / "Teletubby")** — Video editing tool recommended by Brandon for self-editing YouTube content (Brandon said "TeleTV," likely meaning Descript or similar)
- **Stable Diffusion** — Image generation model; Jake running it locally on-prem for POC demos
- **Docker / Docker Compose** — Jake using it to run local LLM inference and serve models for POC demonstrations
- **Firebase** — Aaron using it as a vector store within his Google ADK multi-agent system
- **Vertex AI** — Google cloud ML platform; Brandon mentioned an upcoming ADK + Vertex tutorial
- **InfoBip** — Twilio competitor for messaging APIs; Aaron attended their developer conference
- **Google NotebookLM** — Alex planning a tutorial video on it as his first YouTube content piece
- **HRSA website** — Federal community health clinic database that Gaurav was attempting to scrape

## links

- Brandon shared his ADK masterclass video (YouTube, ~3.5 hours) — referenced but URL not captured in transcript
- Brandon shared his in-progress ADK YouTube thumbnail cloner repository — shown on screen, ~95% complete, URL not captured
- Andrew shared a news article about an AI-generated victim impact statement used in an Arizona court case — dropped in Zoom chat, URL not captured in transcript
- AbdulShakur noted a shorter version of the Windsurf founder story from YC — shared in chat, URL not captured
- Brandon shared a Windsurf founder interview (~1 hour) — dropped in Zoom chat, URL not captured
- Brandon shared the Cursor MCP integrations directory — shown on screen, URL not captured
- Andrew shared a link to the HRSA data download page (Excel/API export of community clinic data) — dropped in Zoom chat for Gaurav, URL not captured
- Brandon shared a link to the Drizzle ORM documentation/example — shown on screen during explanation

## decisions

- **Brandon** will release a new ADK tutorial (YouTube thumbnail cloner using OpenAI image generation) by Thursday of the current week
- **Brandon** will release a second ADK tutorial covering Vertex AI integration later in the week
- **Maksym** will explore implementing a staging environment and feature flags for the dealership WhatsApp bot
- **Maksym** will connect with Jake offline to discuss HIPAA-compliant deployment architecture on Azure/AWS
- **AbdulShakur** will build an automated bio-news-to-infographic pipeline using ADK, drawing inspiration from Brandon's thumbnail cloner project, and aims to demo it at next week's call
- **Paul** will demo his property/real estate calculator app at next week's call
- **Ty** will demo multiple apps he is building at the next call
- **Om Kundalini** will reach out to Richard Collier (community member) for help with AI video generation for his geospatial mythology project
- **Brandon** will connect Om with video editors and thumbnail designers via DM if requested
- **Gaurav** will switch from Crawl4AI to Firecrawl to resolve the Unicode encoding issue, and will DM Brandon if problems persist
- **Gaurav** will post the Cursor student free-tier announcement in the community Slack/School
- **Premkumar** will reach out to Juan Torres (community member) for data science guidance on the PDF ETL pipeline
- **Alex** will have his YouTube channel setup complete and aim to publish his first video (likely a Google NotebookLM tutorial) before the next call
- **Alex** will DM Brandon if he wants referrals to video editors and thumbnail designers
- **Aaron** will set up a whiteboard session with Brandon to map out the ADK architecture for his nonprofit executive assistant multi-agent system