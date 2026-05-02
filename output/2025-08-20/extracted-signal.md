## general

Brandon Hancock returned from a vacation that included scuba diving and night snorkeling, and opened the session with updates before handing the floor to community members for round-robin project updates. He announced that ShipKit — his new AI application starter kit with a CLI, six templates (simple and SaaS variants for chat, RAG, and agent apps), and an accompanying course — was launching the following day. He also shared that he had attended a Google AI agent competition in San Francisco and had a video going live the next day covering the new agentic coding paradigm in Cursor.

The bulk of the session was community members sharing project updates: Marc demoed a fantasy sports lineup app built with LangFlow, FastAPI, Supabase, and Next.js; Andrew shared LangExtract and BAML as tools for structured extraction from long documents; Paul described an N8N-based political briefing tool for local body elections; Sam reported on a deployed customer-facing chatbot and unexpected user behavior discovered through LangSmith traces; Alex (Mexico) showed a geo-referenced news monitoring platform called Deep River; Al Cole reported landing two freelance AI automation gigs through in-person networking; Temitayo described accidentally wiping a production database and recovering via email; Juan Torres discussed overflow client work including a RAG system for a Brazilian surgeon; Mitch worked through Google Cloud Functions and webhook triggering challenges; Patrick shared a structured personality trait system for AI agents using YAML-weighted traits; and Jake discussed scaling concerns for a communication tool built on Convex and Next.js.

Brandon provided technical guidance throughout, including recommendations on React Markdown for streaming agent responses, ADK non-streaming workflows, UV for Python dependency management, Linear for developer task management, PostHog and Sentry for production monitoring, database connection pooling, and Redis for read-heavy workloads.

## insights

- Brandon: ADK works very well for non-streaming workflows (create session, send message, done); streaming adds significant complexity and is not recommended for most use cases right now.
- Brandon: At the Google AI competition, using templates, tasks, and AI agents to do the work allowed him to complete a project while others coding "like it was 2020" did not finish — the agentic paradigm is a real productivity multiplier.
- Brandon: The hardest part of freelance AI work is landing the client, not building the product. Once you have the deal, you can subcontract the build (e.g., N8N developer at $30–40/hr) and focus on account management and sales.
- Brandon: For scaling applications, the database is almost always the first thing to break — improper indexing and unmanaged concurrent connections are the most common failure modes at 10K+ users.
- Brandon: Building a "custom AI newsletter" tailored to a specific industry (e.g., logistics monitoring) is a proven monetization path: charge a high upfront customization fee (~$6K–$8K) and a recurring monthly fee per seat.
- Al Cole: Organic in-person networking at business meetups — presenting yourself as a builder when others are only doing AI strategy — is generating real leads with no outbound effort.
- Patrick: Defining AI personality traits with explicit YAML configuration blocks (weight, behavioral definition, linguistic style) significantly improves model adherence to personality, especially with GPT-5, compared to simple adjective-based prompts.
- Patrick: Standard voice in ChatGPT adheres more faithfully to detailed personality prompts than Advanced Voice, which tends to impose its own personality on top of the system prompt.
- Andrew: LangExtract is best suited for very long plain-text documents where precise character-level citations of extracted information are needed; it handles its own chunking internally.
- Sam: Watching LangSmith traces of real user sessions reveals unexpected use cases that users never communicated — essential for understanding actual product usage.
- Brandon: For proof-of-concept client work, N8N is an excellent rapid prototyping tool before committing to a custom LangChain/LangFlow/ADK implementation.
- Brandon: Using UV for Python dependency management resolves the version conflict issues that commonly plague LangChain projects.
- Temitayo: Always set up automated database backups before going to production — recovering from an accidental full database wipe required mass-emailing all users to re-register.

## qa

**Q (Hemal Shah):** Are there libraries for dynamically generating UI widgets (e.g., calendar pickers) from agent responses, rather than just rendering markdown text?
**A (Brandon Hancock):** The approach is to use structured outputs from the agent to signal what widget type is needed, then wrap the chat message renderer in a switch statement that loads the appropriate UI component per author or event type. The agent's response is still ultimately a string passed back as context; the structured output just tells the front end which component to render.

**Q (Alex Wilson):** You use Gemini a lot now — what are you doing for projects you used to do with Claude?
**A (Brandon Hancock):** Still 90% Claude (Claude 4.0 / Claude 4 Thinking). Gemini 2.5 Pro on max settings is used only for huge context problems that need the million-token context window.

**Q (Marc Juretus):** What do you use for task/to-do management on projects?
**A (Brandon Hancock):** For ideas and big projects: Notion. For daily actions: paper. For collaborative developer work: Linear (free tier), which integrates with GitHub and automatically updates issue timelines when branches are checked out.

**Q (Mitch):** I'm trying to trigger a Google Cloud Function via webhook in local development — should I use Ngrok?
**A (Brandon Hancock):** At the stage where you're relying on cloud-native services like EventArc or Cloud Tasks, local testing becomes impractical because those services don't exist locally. The standard approach is to maintain a development environment in the cloud, test there until it works, then promote changes to production. Cloud Functions (60-minute timeout) combined with Cloud Tasks for queuing is the recommended architecture for your use case.

**Q (Juan Torres):** A surgeon's RAG system has poor retrieval due to highly specialized medical terminology — what's the likely fix?
**A (Brandon Hancock):** The hypothesis is context engineering and routing: create embeddings of the specialized terminology and use a dedicated agent to correlate user queries to the correct documents. Also check whether mixing multiple vector databases is causing the agent to not know which database to query.

**Q (Jake Maymar):** What are the main things to watch for when scaling from 100 to 10,000 users?
**A (Brandon Hancock):** The front end (Next.js) is rarely the issue. The database breaks first — ensure proper indexing and use connection pooling (e.g., PgBouncer/Supabase pooler) to stay under connection limits. Add PostHog for usage metrics and Sentry for front-end error alerting so issues surface automatically rather than going unnoticed.
**A (Al Cole, addendum):** If the app is read-heavy, Redis as a caching layer can handle millions of ops/second and dramatically offload the primary database.

**Q (Brandon Hancock):** When would you use LangExtract vs. just passing a document to Gemini with structured output?
**A (Andrew Nanton):** LangExtract is specifically valuable for very long documents and when you need precise citations (character-level start/end positions) of where extracted information came from. BAML is better for high-volume, consistent structured extraction (e.g., 1,000 receipts) where you need guaranteed schema adherence across many runs.

## tools

- **N8N** — Visual workflow automation; used by Paul and Al for rapid proof-of-concept AI pipelines; self-hosted on a DigitalOcean droplet alongside MongoDB
- **LangFlow** — Python-based visual node editor; Marc rewrote his fantasy app backend in it after ADK issues
- **FlowWise** — TypeScript/Node.js visual workflow tool; mentioned as recently acquired by Workday and releasing v3
- **Google ADK (Agent Development Kit)** — Google's agent framework; Brandon recommends for non-streaming workflows; used with Agent Engine
- **Google Opal** — Google's visual agent builder (described as early/rough); mentioned as similar to N8N
- **LangExtract** — Google library for structured extraction from long plain-text documents with character-level citations
- **BAML** — Structured extraction framework; more developer-oriented; good for high-volume consistent schema extraction
- **Kuzu** — Embedded graph database; mentioned in context of BAML tutorials for graph RAG
- **LangSmith** — LangChain observability/tracing platform; Sam uses it to monitor real user traces; Marc had dependency conflicts integrating it with LangFlow
- **Cursor** — AI-first IDE; primary coding tool for Brandon and most participants (~99% usage)
- **Claude Code** — Anthropic's agentic coding tool; Brandon plans a video on Claude Code subagents
- **Supabase** — Postgres backend-as-a-service; used by Marc for the fantasy app; recommended by Brandon for automatic 24-hour backups
- **Neon** — Serverless Postgres; recommended as alternative to self-hosted DB with built-in backups
- **Linear** — Developer project management tool (Trello for devs); integrates with GitHub; Brandon uses it for collaborative work on free tier
- **Notion** — Used for long-term project planning and ideas
- **PostHog** — Product analytics/telemetry; recommended by Brandon for tracking user behavior at scale
- **Sentry** — Error monitoring; recommended for front-end error alerting in production
- **Redis** — In-memory data store; Al recommends for read-heavy workloads to offload primary database
- **Convex** — Real-time database platform; Jake is using it and ramping up
- **Google Cloud Functions / Cloud Run** — Serverless compute; Mitch is deploying Python backend here
- **Google Cloud Tasks** — Task queue for triggering Cloud Functions asynchronously
- **EventArc** — Google Cloud event routing; mentioned as trigger mechanism for Cloud Functions
- **React Markdown** — Library for rendering streaming agent responses as formatted markdown in real time
- **UV** — Python dependency/package manager; recommended to resolve LangChain version conflicts
- **Ngrok** — Tunnel tool for exposing local servers; discussed but superseded by cloud-native dev environment approach
- **NotebookLM** — Google tool; Patrick uses it to generate audio/video overviews of his documentation for YouTube
- **ShipKit** — Brandon's new product launching the next day; CLI-based AI app starter kit with six templates and a course
- **FastAPI** — Python web framework; Marc's fantasy app backend
- **Next.js** — React framework; used by Marc, Jake, and others for front ends
- **MongoDB** — Document database; Paul uses it alongside N8N on his droplet
- **Contabo** — VPS provider; Temitayo was hosting his database there (no automatic backups)
- **LangChain** — Python AI framework; noted for frequent dependency conflicts
- **Mailgun** — Email service; mentioned as a ShipKit integration template
- **GitHub** — Version control; Linear integrates with it; Alex Wilson hooks Claude projects to it for screenplay assets
- **Azure DevOps** — Marc's workplace project management tool; similar board to Linear
- **ChatGPT (GPT-5)** — Patrick uses it with custom personality system prompts via OpenAI Projects; notes GPT-5 is more sensitive to personality design
- **Perplexity** — AI assistant; Patrick notes it works well with his personality prompts via voice
- **Deep River** — Friend's geo-referenced news monitoring platform (shown by Alex/Mexico); screens open media every half-second and maps events geographically

## links

- LangExtract GitHub repository — Andrew shared; Google library for structured extraction from long documents with HTML visualization
- BAML + Kuzu tutorial — Andrew shared; guide on using BAML for structured extraction to build knowledge graphs
- Brandon's upcoming YouTube video on agentic Cursor paradigm — shared in chat; already recorded, going live the next day with ShipKit pre-launch
- Brandon's "AI Authority Accelerator" YouTube video — shared in chat for Alex Wilson; covers building an AI personal brand
- Notion masterclass linked alongside the AI Authority Accelerator video
- Lenny's Newsletter deal page — Al Cole mentioned; ~$200 gives access to ~20 platforms including Linear
- Patrick's YouTube channel (Clara Forge playlist) — Patrick shared in chat; NotebookLM-generated audio/video overviews of his AI personality project documentation
- ShipKit landing page — Brandon demonstrated live; shows templates, CLI demo, and course modules

## decisions

- Brandon will send Alex (Mexico) a video editor contract/expectations document after the call
- Brandon will send Mitch updated code samples the next morning covering Google Cloud Functions and task queue patterns
- Brandon will manually send Fitz early access to ShipKit templates and prep files once the email automation is connected
- Paul committed to building a demo of his political briefing N8N tool to show the following week
- Brandon will hold off on ShipKit purchases until the following day (~18–20 hours) to ensure email sequences, bonuses, and instant access are properly configured
- Juan Torres will reach out to Maxim (community member) about subcontracting the Brazilian surgeon's RAG project
- Brandon will look into the Cursor CLI to potentially cover it in a future session, based on community request
- Patrick will share his YouTube channel link in the chat for the group to review
- Temitayo will migrate from self-hosted Contabo VPS database to Supabase or Neon to get automatic backups
- Brandon suggested Marc use Excalidraw to map out his next app idea before building, and offered to review it on a future call