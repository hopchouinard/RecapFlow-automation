## general

This was a weekly group coaching call hosted by Brandon Hancock, bringing together roughly a dozen participants at various stages of building AI-powered applications. The session followed a round-robin format where each participant shared project updates, asked technical questions, and received feedback from the group. Topics ranged from RAG architecture and vector stores to browser automation, personal branding, and AI tooling.

Alex Rojas demonstrated a working RAG-based legal application focused on civil rights law in Mexico City, built with Next.js and Supabase, and discussed chunking strategies and PDF parsing challenges. Abdul Shakur shared a sentiment analysis project concept and a card game landing page he launched via Replit. Marc Juretus discussed migrating from ChromaDB to Supabase for vector storage and integrating ADK with a Next.js frontend. New participants Matias (Buenos Aires), Zain K, Jaylen Davis, and Andrian Georgiev each introduced themselves and received tailored feedback on their projects and goals.

Brandon provided architectural guidance throughout, covering background worker patterns for document processing, Drizzle ORM for schema management, task-driven AI development with living template documents, and personal branding strategy. The call closed with Brandon announcing a structural change for future sessions: a pre-call Typeform for questions to make the format more efficient.

## insights

- **Browser automation agents are unreliable for deterministic tasks**: Brandon advised Matias to use standard Playwright/web drivers for repetitive LinkedIn actions (sending invites, scraping messages) rather than browser agents, which struggle with large HTML contexts and blow up context windows. Get out of the browser as fast as possible and hand off to agents only for reasoning tasks.
- **Separate chunking/embedding from your web application**: Long-running Python jobs (Dockling, Chunky) will time out on Vercel. The recommended pattern is a background worker (Docker container or Railway service) that polls a database for pending jobs, processes documents, and saves chunks back — keeping the Next.js app thin.
- **Supabase pgvector eliminates the need for a separate vector store**: One line of schema (`vector` column type via pgvector extension) lets you store embeddings directly alongside relational data. Using ChromaDB separately creates synchronization problems and extra operational overhead.
- **Drizzle ORM provides structured, versioned database migrations**: Rather than manually editing tables in Supabase's UI, defining schema in Drizzle creates a migration history, enforces `ON DELETE CASCADE` for related chunks, and exports TypeScript types usable throughout the application.
- **Living task-template documents dramatically improve AI coding speed**: Brandon described a feedback loop where every time Cursor produces a wrong result, the master task-template document is updated. Starting at ~70% accuracy, the template reaches ~95% after iterative refinement, enabling near one-shot task completion.
- **GraphRAG is only worth adding when documents have meaningful domain-specific relationships** (e.g., medical ontologies, legal hierarchies). For general or loosely related documents, plain vector search is sufficient. GraphRAG and vector search can run in parallel with weighted scoring. (Bastian Venegas)
- **Exponential backoff outperforms fixed delays for API rate limiting**: Using exponential backoff allows more API calls within a given time window compared to a fixed wait between calls. (Bastian Venegas)
- **For a static legal corpus, chunking is a one-time cost**: If documents update only a few times per year, the complexity of a streaming background worker is less critical — chunk once and append on reform updates.
- **Context7 MCP tool brings live library docs into Cursor**: Connecting Context7 as an MCP server allows Cursor to pull the latest framework documentation (e.g., LangGraph) at query time, overcoming the problem of LLMs hallucinating outdated API patterns.
- **Personal branding compounds faster than job applications**: Brandon's advice to Andrian — pick one framework (LangGraph), produce one YouTube video + one LinkedIn post per week for six months, and you become the recognized expert, attracting consulting and job opportunities inbound rather than outbound.
- **Zoom in before zooming out on big AI goals**: When a goal is too large and undefined (e.g., "build a Cortana-like second brain"), it leads to aimless wandering. Pick one sub-component (email assistant, Notion assistant), ship it, then chain agents together. (Brandon to Zain)
- **Limitless pendant + Otter AI combination accelerates sales cycles**: Paul Miller reported closing three customers in four weeks (down from a six-month average) by capturing all meeting notes via Limitless and Otter AI, then immediately following up with structured summaries.

## qa

**Q (Marc Juretus):** If I push something to production, would I actually use ChromaDB, or should I use Supabase?
**A (Brandon Hancock):** Chroma does have a paid hosted version, but if you're already using Supabase for your database and auth, it's already there — why add another service to manage? Using Supabase pgvector keeps everything in one place, lets you use `ON DELETE CASCADE` to keep chunks in sync, and avoids synchronizing state across two services.

**Q (Marc Juretus):** When I'm looping through documents and saving to a vector store, do I just change the pointer from ChromaDB to Supabase?
**A (Brandon Hancock):** It's not really a pointer change — you define a schema in Drizzle with a `vector` column type, run migrations, and then insert chunks just like any other database row. The embedding is just a column of numbers in your normal Postgres table.

**Q (Marc Juretus):** How do I serve ADK so that my Next.js frontend can consume it?
**A (Brandon Hancock):** ADK is a long-running agentic process, not an instant API response. You wrap it inside a FastAPI endpoint that receives the message, appends it to the conversation, and kicks off the ADK workflow. The frontend then polls or streams to get the current status. Brandon shared a voice agent GitHub repo as a working example of a static HTML/JS client talking to a backend ADK agent.

**Q (Juan Torres):** Does Supabase have infrastructure for running the chunking system as well, or just embeddings?
**A (Brandon Hancock):** Supabase edge functions are Node-only and can't run long Python jobs. You're essentially stuck with a separate background worker — a Python application that polls the database for pending jobs, chunks and embeds documents, and saves results back. There's no current workaround for long-running Python inside Supabase itself.

**Q (Alex Rojas):** Is Drizzle sitting in between Supabase and Next.js, managing all the SQL?
**A (Brandon Hancock):** Yes. Drizzle is an ORM that takes your schema file, generates migration files on changes, and applies them to your Postgres database. It also exports TypeScript types so you can use them safely throughout your application. It's about order and versioning, not about deployment.

**Q (Bastian Venegas):** Is there a real use case where plain vector RAG fails and GraphRAG is required?
**A (Bastian Venegas / Brandon Hancock):** GraphRAG adds value when the corpus has meaningful domain-specific relationships (e.g., medication families treating specific conditions in medical data, or hierarchical legal structures). For general or loosely related documents, plain vector search works fine. The two approaches can run in parallel with weighted scoring to combine results.

**Q (Mitch):** For Limitless, do you buy just the lapel or the lapel plus a membership?
**A (Paul Miller / Brandon Hancock):** You can buy them separately or together. There's a monthly subscription option if you don't want to commit to a year upfront. Brandon confirmed the USB-C pendant lasts about two days per charge.

**Q (Andrian Georgiev):** What should my six-month goal be given my background in project management and interest in LangGraph?
**A (Brandon Hancock):** Pick LangGraph as your focus, produce one YouTube tutorial and one LinkedIn post per week for six months. After six months of consistent output, you'll likely be the top independent LangGraph content creator on the internet. That leads to consulting opportunities, job offers, and inbound interest — without the traditional job application grind.

## tools

- **LocalGPT** — Open-source RAG project by Mohamed (Prompt Engineering YouTube channel); version 2 releasing mid-July with improved search and validation
- **Dockling (Docling)** — IBM open-source library for parsing PDFs and multiple file types; runs on Mac MLX, GPU, or CPU; used for document chunking in RAG pipelines
- **Chunky** — Semantic chunking library; Alex used it at 500-character chunks with Gemini 768 embeddings for his legal RAG app
- **Supabase** — Postgres database with pgvector extension used as a combined relational + vector store for RAG applications
- **Drizzle ORM** — TypeScript ORM used to define schemas, generate migrations, and export types for Next.js + Supabase applications
- **Cursor** — AI-powered IDE used by multiple participants for vibe-coding and task-driven development with living template documents
- **Claude Code** — Anthropic's agentic coding tool; Sam explored it over the weekend, noted strength in autonomous test writing and CI integration
- **Google ADK (Agent Development Kit)** — Google's framework for building multi-agent applications; discussed for integrating with Next.js via FastAPI
- **FastAPI** — Python web framework used to wrap ADK agents and expose endpoints to Next.js frontends
- **Railway** — Deployment platform for background worker Python services; noted as lacking GPU, so slower for ML workloads vs. Google Compute Engine
- **Fathom** — Meeting recording tool used by Brandon; noted a bug where it only captured screen share instead of video on one call
- **Limitless Pendant** — Wearable AI recording device; Paul credited it with reducing his sales cycle from six months to five weeks
- **Otter AI** — Used alongside Limitless for Zoom call transcription and note capture
- **ConvertKit** — Email marketing / CRM platform recommended by Brandon for Abdul's card game waitlist over embedded Substack
- **Mailgun** — Email sending service mentioned as an alternative for managing waitlist signups (~$6–12/month or free tier for ~1,000 emails/month)
- **Replit** — Used by Abdul to build the card game landing page
- **Lovable** — AI app builder; Paul noted it goes off on tangents; recommended for rapid prototyping with good initial prompts
- **Playwright** — Browser automation library used by Matias for deterministic LinkedIn connection-sending
- **Browser Use** — Browser agent tool tested by Matias; noted as very heavy and unreliable for deterministic tasks
- **Context7** — MCP tool providing access to ~13,000 code repository docs; recommended for pulling latest LangGraph docs into Cursor
- **Looker Studio** — Google BI tool used by Mitch to replace a $10,000/month data warehousing and reporting setup
- **RAGanything** — LightGraph-based RAG wrapper supporting images, PDFs, and videos with hybrid/global/chunk retrieval modes; Sam mentioned it
- **Neo4j** — Graph database noted as a leader for GraphRAG use cases
- **Pythagora AI** — VS Code-based AI coding tool with built-in planning phase; Paul flagged it as worth investigating (sponsored video caveat noted)
- **Zen Browser** — Firefox-based browser Mitch switched to from Arc; noted higher battery usage but more customizable sidebar
- **Arc Browser** — Browser Mitch switched away from; noted it doesn't allow exporting bookmarks
- **N8N** — Automation platform mentioned by Andrian as having limitations for full agent exploration
- **LangGraph** — LangChain's graph-based agent framework; Andrian's chosen framework; noted as used by Fortune 500 companies

## links

- **LocalGPT v2 video (Prompt Engineering channel by Mohamed)** — Paul shared in chat; covers RAG validation, Dockling integration, and version 2 preview
- **Brandon's RAG + Supabase video** — Referenced as the recommended starting point for setting up vector stores in Supabase
- **ADK quickstart / static client example** — Brandon dropped in chat; shows a static HTML/JS client connecting to an ADK backend agent
- **Brandon's voice agent GitHub repo** — Shared in chat as a cleaner example of a static client talking to a backend ADK agent with streaming
- **topiclaunch.com** — Jaylen Davis's live platform allowing YouTube fans to propose and fund video topics
- **Andre Karpathy "Coding 3.0" video** — Alex shared in chat; covers the vibe-coding concept and where software development is heading
- **Context7 MCP documentation** — Referenced for adding latest LangGraph docs to Cursor; Brandon showed it live
- **LangGraph creator on YouTube (James)** — Bastian dropped in chat; ~75K subscribers, focused on LangChain/LangGraph tutorials
- **Flow (drawing app) feature request page** — Brandon showed as inspiration for Jaylen; demonstrates user-driven feature voting for product development
- **RAGanything GitHub/docs** — Sam shared; LightGraph-based RAG wrapper supporting multiple file types and hybrid retrieval modes

## decisions

- **Brandon** will create a Typeform for participants to submit questions before each call, restructuring future sessions into a Q&A first half and round-robin project updates second half.
- **Brandon** will finish the first ShipKit template within approximately two days and share it with Mitch (and other interested beta testers) via DM.
- **Brandon** will produce a tutorial video on connecting a Next.js application to a deployed ADK backend as one of his next major videos.
- **Brandon** will work on a "RAG as a service" project after ShipKit ships — a developer tool that accepts any file type and returns embeddings/chunks for any database.
- **Brandon** will talk to the Google ADK team the following day (Wednesday).
- **Alex Rojas** will meet with his lawyer friend this week to gather pain-point feedback before adding contract-generation functionality to his legal RAG app.
- **Alex Rojas** will investigate the background worker + Dockling pattern Brandon demonstrated for handling PDF chunking at deployment.
- **Juan Torres** offered to serve as a guinea pig for Alex's contract-generation feature, testing server and equipment lending contracts under Mexican law.
- **Marc Juretus** will migrate from ChromaDB to Supabase pgvector, using Brandon's video and Supabase documentation as references.
- **Marc Juretus** will reach out to Bastian Venegas for a one-on-one Supabase walkthrough.
- **Abdul Shakur** will replace the embedded Substack signup form on his card game site with a Supabase database + ConvertKit integration for waitlist management.
- **Matias** will shift his LinkedIn automation approach away from browser agents for deterministic tasks (sending invites) and focus agents only on message classification and response drafting.
- **Zain K** will post his ADK hackathon project and ping Brandon if he needs further help.
- **Andrian Georgiev** will add Context7 as an MCP server in Cursor to get up-to-date LangGraph documentation.
- **Paul Miller** will post the LocalGPT video link and the Pythagora AI video link in the group chat for others to review.
- **Mitch** will purchase the Limitless pendant after hearing Paul's and Brandon's endorsements.
- **Brandon** will consider switching from Arc to Zen Browser after Mitch's recommendation, pending further feedback.