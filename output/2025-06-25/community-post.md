📝 SUMMARY

This coaching call covered advanced RAG implementation strategies, production deployment architectures, and personal productivity workflows using AI. Paul announced a collaboration with Mohamed from the Prompt Engineering channel on LocalGPT v2, while Alex showcased a legal RAG application for Mexican law using semantic chunking and Supabase. The group discussed practical deployment patterns for document processing, including the necessity of Python background workers for PDF chunking and the advantages of Supabase pgvector over separate vector databases like ChromaDB. Several members shared projects ranging from LinkedIn automation to sentiment analysis tools, with Brandon providing architectural guidance on deterministic vs. agentic workflows. The call also explored personal AI assistant strategies for neurodivergent productivity and a new platform for crowdsourcing YouTube video topics.

💡 KEY INSIGHTS

Paul is collaborating with Mohamed (Prompt Engineering channel) on LocalGPT v2, an open-source RAG project scheduled for mid-July release that focuses on improved search validation and accuracy testing frameworks. The project uses Dockling for document processing and can run locally or point to external LLMs.

Alex demonstrated a production legal RAG application covering Mexican civil rights law from Constitution to local statutes, using Chunky for semantic chunking at 500 characters per chunk with Gemini 768 embeddings. He emphasized the importance of converting PDFs to TXT for deployment to avoid processing timeouts.

Brandon argued for using Supabase pgvector instead of ChromaDB in production environments to avoid synchronization issues between separate services. He demonstrated how Drizzle ORM manages vector embeddings alongside regular database tables with cascade deletion support.

For document processing pipelines, Brandon recommended deploying Python background workers on GPU-enabled instances (like Google Compute Engine) rather than serverless platforms like Railway, as PDF chunking often exceeds Vercel's timeout limits.

Matias presented a LinkedIn automation project using Playwright. Brandon advised using deterministic scripts for simple browser tasks (clicking connect buttons) and reserving agentic workflows only for classification and response generation tasks, recommending users "get out of the browser as quickly as possible."

Addressing Zain's challenge with ADHD and building a personal AI assistant, Brandon recommended zooming in on one specific use case (such as email management) rather than attempting to build a comprehensive "Cortana" system immediately. He suggested using MCP tools to connect Notion, Gmail, and Zoom for context gathering.

Brandon shared his "AI Task Template" methodology for standardizing AI-assisted development, creating living documents that iterate based on errors to improve task generation for database schema changes, backend routes, and frontend components.

Jaylen introduced TopicLaunch, a platform allowing fans to propose and fund video topics for YouTubers. Brandon suggested pivoting to a creator-paid model with audience voting/upvoting features, similar to how Flow app handles feature requests.

Andrian received advice to specialize in LangGraph specifically, creating weekly tutorial content to establish authority in that framework rather than remaining generalist, as LangGraph dominates enterprise agent development.

❓ KEY Q&A

Marc asked whether ChromaDB or Supabase is better for production vector storage. Brandon recommended Supabase pgvector to avoid managing separate services and synchronization issues, showing how Drizzle ORM handles vector columns alongside relational data with proper cascade deletion.

Marc asked about ADK deployment architecture for Next.js applications. Brandon explained that ADK requires wrapping in FastAPI endpoints due to its long-running agentic nature,不同于 standard REST APIs, and suggested using polling or streaming to check message status rather than expecting immediate responses.

Juan asked Alex if his legal RAG could generate contracts like service or equipment lending agreements. Alex confirmed this is planned functionality requiring a separate contract corpus and distinct agent flows for research versus contract generation.

Bastian asked Alex about rate limiting strategies for the Gemini API. Bastian suggested exponential backoff rather than fixed delays between calls, allowing more API requests within time windows while handling throttling gracefully.

Bastian asked whether Alex's vector database is static or receives updates. Alex explained it receives initial bulk chunking with occasional updates for legal reforms, not daily changes, making the processing overhead manageable.

Alex asked Brandon about Drizzle's role between Next.js and Supabase. Brandon clarified that Drizzle serves as an ORM generating migrations and type-safe database schemas, enforcing structure that direct Supabase table creation lacks.

Matias asked for feedback on using agents for LinkedIn connection requests and message responses. Brandon advised using deterministic Playwright scripts for the repetitive connection workflow and reserving agents only for message classification and draft generation, extracting data from the browser quickly to minimize agent context window usage.

Zain asked about building an integrated AI assistant for ADHD management. Brandon recommended starting with one narrow domain (email assistant), mastering MCP integrations for context, and expanding outward rather than attempting a full "Cortana" system immediately.

Jaylen asked for feedback on TopicLaunch, a crowdsourced video funding platform. Brandon suggested a pivot where creators pay for the tool and audiences vote/upvote for free, creating a signal-to-noise filter and more sustainable business model than fan-funded thresholds alone.

Andrian asked about positioning himself in the AI job market. Brandon advised specializing narrowly in LangGraph, creating weekly content (tutorials and LinkedIn posts) to become the authoritative voice for that specific framework, which dominates enterprise use cases.

🛠️ TOOLS AND CONCEPTS MENTIONED

LocalGPT — Open-source RAG project by Mohamed (Prompt Engineering) focused on local document search with version 2 adding improved validation frameworks and Dockling integration.

Dockling — IBM's open-source document processing library supporting multiple file types with MLX acceleration on Apple Silicon, praised for extracting clean chunks without random cutoffs.

Chunky — Semantic chunking library used by Alex to process legal documents at 500-character chunks, identified as the "sweet spot" for his use case.

Supabase pgvector — Postgres extension for vector storage recommended over separate vector databases to maintain data consistency and simplify cascade deletions.

Drizzle ORM — TypeScript ORM used with Supabase to manage database schemas, migrations, and type safety across applications.

ADK (Agent Development Kit) — Google's framework for building agentic applications, discussed in context of wrapping long-running processes in FastAPI endpoints for web deployment.

MCP (Model Context Protocol) — Protocol for connecting AI agents to external tools like Notion, Gmail, and Zoom for context gathering.

Playwright — Browser automation tool recommended for deterministic LinkedIn scraping and interaction workflows.

Replit — Platform used by AbdulShakur to build a card game landing page quickly.

ConvertKit — Email marketing service recommended for managing waitlists and email sequences with better analytics than embedded Substack forms.

RAGAnything — Graph-based RAG wrapper using LightGraph to create knowledge graphs on top of embeddings, supporting multiple retrieval modes (global, hybrid, chunk).

Claude Code — Anthropic's command-line coding tool discussed by Sam for autonomous test writing and background code improvement.

Limitless — AI wearable device praised by Paul and Brandon for capturing conversations and generating sales follow-ups, with noted quirks about unsolicited "coaching" feedback.

Pythagora AI — VS Code extension mentioned by Paul that structures app development through a planning phase before coding.

Context 7 — MCP server providing access to 13,000+ code repositories for bringing up-to-date documentation into Cursor.

📎 SHARED RESOURCES

LocalGPT GitHub repository and video by Mohamed (Prompt Engineering channel) — Paul shared links to the open-source RAG project and upcoming version 2 features including search validation techniques.

Andrej Karpathy video on "Coding 3.0" and vibe coding — Alex shared this resource explaining the theory behind AI-assisted software development.

Brandon's ADK deployment example — Static website example showing how to connect a frontend to ADK backend agents using FastAPI.

Brandon's voice agent tutorial — Example project demonstrating streaming connections between web clients and ADK agents.

Supabase vector documentation — Official docs for setting up pgvector in Supabase.

Bastian's LangChain/LangGraph content link — Reference to existing creator in the space with 76k subscribers but low engagement, indicating opportunity for better content.

Flow app feature request system — Example of crowdsourced product development that Brandon suggested Jaylen emulate for YouTube content.

🔄 FOLLOW-UPS WORTH EXPLORING

LocalGPT version 2 release scheduled for mid-July — Paul to update the group on features from his collaboration with Mohamed.

ShipKit template release — Brandon is completing three templates and example projects for full-stack AI application development, available for beta testing.

RAG as a Service concept — Brandon identified a market gap for a developer tool that handles document chunking and embedding generation across formats (PDF, video, text) without requiring users to manage Python workers and vector databases.

GraphRAG validation — Bastian and Sam discussed graph-based RAG for specific domains (legal, medical) but noted the challenge remains determining when vector search alone is insufficient versus requiring knowledge graph relationships.

Context 7 LangGraph version update — Andrian to request updated LangGraph v4 documentation through Context 7 MCP to improve Cursor's code generation accuracy for the latest framework version.

ADK Web deployment tutorial — Brandon committed to creating a video specifically covering Next.js frontend integration with deployed ADK backends.

Deterministic vs. Agentic workflow boundaries — Further exploration needed on where to draw the line between scripted browser automation (Playwright) and agentic reasoning (ADK/LangGraph) for business process automation.