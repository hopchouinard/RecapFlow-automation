## general

This was a weekly group coaching/mastermind call hosted by Brandon Hancock, covering member project updates, technical Q&A, and tool discussions. The session followed a round-robin format where each participant shared a win, an interesting project, or a problem they needed help with. Brandon opened with observations from Google I/O, noting upgrades to existing tools (video/image generation, Gemini APIs) and excitement about Firebase Studio finally integrating properly with Firebase.

Topics spanned a wide range of AI and software engineering subjects: Supabase row-level security challenges, local RAG/vector store architecture, Google ADK multi-agent development, voice agent emotion handling, ETL pipelines on AWS MWAA, YouTube channel launches, grant-writing agent architecture, client pricing and NDA negotiation, and career advice for someone pivoting into agentic AI roles. Several members demonstrated live screen shares of their projects.

Bastian Venegas contributed several technical suggestions throughout, including recommending the Graffiti MCP server for GraphRAG, embedding model options, and a Vercel open-source UI repo for ADK. Jake Maymar offered client relationship and pricing wisdom. The call ended with Brandon committing to more ADK tutorial videos and wrapping up a current freelance client project.

## insights

- **Brandon on Supabase complexity:** Row-level security in Supabase has three distinct layers — row-level security, role security, and app-level authentication — and getting all three aligned is a significant time sink even for experienced developers.
- **Brandon on AI-accelerated development:** A project that would have taken weeks a year ago can now be completed in days using Lovable, Gemini 2.5 Pro, and Cursor-based rules.
- **Brandon on scaling philosophy:** Avoid over-engineering infrastructure prematurely. Shipping on a $5/month server and scaling naturally beats spending weeks on Kubernetes orchestrations before anyone has used the product.
- **Brandon on RAG vs. artifacts:** RAG is optimal when many users query the same document repeatedly. For one-time document processing (e.g., generating a single grant from uploaded PDFs), passing the full document as an artifact to a long-context model (Gemini handles 1M+ tokens) is simpler and more appropriate.
- **Brandon on agent architecture:** Agents don't need to know anything about RAG internals. They only need a tool call; all embedding, querying, and chunking logic lives in the backing FastAPI service.
- **Brandon on client pricing:** A standard RAG chatbot with custom UI/auth is roughly an $8K project. A project requiring the developer to also act as an AI adoption consultant — learning the client's domain and codifying their process — warrants pricing in the $20K–$30K range.
- **Brandon on exclusivity clauses:** Any NDA that restricts future work in the same domain should command a premium price, framed as compensation for limiting earning potential.
- **Jake on client culture:** How a client treats you at the very beginning of a relationship is almost always how they will treat you throughout — factor this into pricing and engagement decisions.
- **Maksym on infrastructure cost:** Running a WhatsApp bot for 3,400 users on a $5 Cloudflare Worker with free-tier credits from Supabase, Voyage AI, and Azure demonstrates that infrastructure costs can be near-zero at meaningful scale.
- **Brandon on job-seeking strategy:** Rather than guessing which AI frameworks to learn, look at active job postings for target roles and work backwards from the specific tools listed.
- **Bert on ADK learning:** Publicly signaling ADK upskilling on LinkedIn (even during a job search gap) generated recruiter inbound within a short period, validating the market demand for the skill.
- **Brandon on video content cadence:** For a new YouTube channel, publish as frequently as possible — the first few videos are the hardest, and the goal is to keep producing until something gains traction.

## qa

**Q (Marc Juretus):** If I want to store agent conversation outputs locally in a vector database and query them as a tool from multiple agents, what's the best approach?
**A (Brandon Hancock):** Use ChromaDB as a local vector store, then wrap it in a FastAPI service exposing two endpoints — query and add. Create two tools in your agent framework that call those endpoints. The agent only passes raw text strings; all embedding and retrieval logic lives inside the FastAPI service.

**Q (Marc Juretus):** For front-end interfaces, do you always use Next.js over Streamlit?
**A (Brandon Hancock):** Streamlit works for local testing, but the moment you need anything more advanced you'll have to restart with Next.js anyway. Every AI tool understands Next.js well, so it's worth going there from the start.

**Q (Jake Maymar):** We're using OpenAI Advanced Voice but it says emotions rather than performing them consistently. Any suggestions?
**A (Maksym Liamin / Brandon Hancock):** Sesame is significantly better than ElevenLabs or OpenAI for emotional voice transfer. Richard (a community member) had the most success with OpenAI but Sesame is worth testing. Brandon also suggested Simon Høiberg's YouTube channel for knowledge-base and persona-replication techniques.

**Q (asako):** How would you make the dashboard more conversational so users can ask the AI to modify generated output?
**A (Brandon Hancock):** Add a co-pilot sidebar — a chat panel that receives the original input and output as context. The user submits feedback, and an apply button overwrites the output. Avoid LLM tool calls for this; keep it simple with a manual apply action.

**Q (asako):** What's the best way to add text highlighting and commenting to a dashboard?
**A (Brandon Hancock / Maksym Liamin):** Use Tiptap, a rich text editor framework that supports highlighting, underlining, custom nodes, and comments. For PDF-specific highlighting, React PDF Highlighter is another option (Maksym shared a link).

**Q (Aaron / The Dharma House):** For a grant-writing agent MVP, should I use RAG or artifacts for document ingestion?
**A (Brandon Hancock):** Use artifacts, not RAG. RAG is designed for repeated queries against the same document by many users. Grant writing requires reading everything once and acting on it holistically. Gemini's 1M-token context window can hold even large PDFs. The hard part is iteratively extracting meaningful information with sequential/loop agents before the writing agent begins.

**Q (Aaron / The Dharma House):** I'm getting a binary file error when uploading PDFs through ADK Web. Is native file upload supported?
**A (Brandon Hancock / Bastian Venegas):** Files need to be passed as byte streams with an explicit MIME type (e.g., `application/pdf`). In a before-model callback, filter message parts for `inline_data` with the correct MIME type, then either save locally for later tool use or add directly as an artifact. Bastian noted that native UI upload through ADK Web may not be fully supported yet and may require CLI or a custom front-end.

**Q (Neel More):** As someone with 20 years of MLOps experience pivoting into agentic AI, should I focus on LangChain, Crew AI, or ADK?
**A (Brandon Hancock):** For landing corporate jobs, LangChain is best because it exposes the underlying concepts — embeddings, chunking, vector stores, agent patterns — that employers want. For an AI architect role specifically, pair AI knowledge with a cloud infrastructure platform; Azure is currently winning commercially. Microsoft's Azure AI Fundamentals certificate is a good starting point.

**Q (Nate Ginn):** I want to scan a Google Sheet daily for empty billing code rows and send myself an alert. What's the best approach?
**A (Brandon Hancock / Bastian Venegas):** Use a cron job in N8N — it runs 24/7 and the workflow is roughly four nodes: trigger on schedule, pull Google Sheet, filter for empty rows, send email via SendGrid or Mailgun. No AI required for this use case.

## tools

- **Google ADK (Agent Development Kit)** — Primary agent framework discussed throughout; multiple members building production projects with it
- **Firebase Studio** — Google announced it now properly connects to Firebase; Brandon excited to test the rollout
- **Gemini 2.5 Pro** — Brandon's current favorite model for client projects; used inside Lovable
- **Gemini 2.5 Flash** — Suggested for video analysis tasks (Paul's camera footage project) due to native video input support
- **Lovable** — Used by Brandon to rapidly scaffold full-stack AI applications for clients
- **Cursor** — Used for writing agent instructions via dictation and iterating on code; Brandon uses it with project rules
- **Supabase** — Brandon building a client project with it; noted complexity of row-level security + role security layers
- **ChromaDB** — Recommended as the easiest local vector store for RAG setups
- **FastAPI** — Recommended for wrapping a local vector store as a queryable service for agents
- **LangChain / LangGraph** — Discussed as best framework for job seekers targeting corporate AI roles
- **Crew AI** — Marc converting a fantasy football app from Crew AI to Google ADK
- **Google ADK sequential/loop agents** — Discussed for grant-writing pipeline and YouTube short generation
- **Apache Airflow / AWS MWAA** — Juan demonstrated a successfully deployed ETL pipeline; noted MWAA is expensive for small data volumes
- **AWS RDS (PostgreSQL)** — Juan's cloud database, connected to Airflow via shared VPC
- **N8N** — Recommended for Nate's billing alert automation; cron job + Google Sheets + email in ~4 nodes
- **Reolink NVR** — Paul's camera system; exploring API access to automate video search
- **Sesame** — Recommended for emotionally expressive voice agents; described as significantly better than ElevenLabs
- **ElevenLabs** — Mentioned as voice provider Maksym's team uses; compared unfavorably to Sesame for emotion
- **OpenAI Advanced Voice** — Jake's current voice implementation; inconsistent emotion expression
- **Tiptap** — Rich text editor framework recommended for adding highlighting/commenting to dashboards
- **React PDF Highlighter** — Open-source library for PDF text highlighting and commenting
- **Graffiti MCP server** — Bastian shared a repo implementing GraphRAG as an MCP server
- **Voyage AI** — Maksym using free credits for embeddings in his WhatsApp bot
- **Azure Document Intelligence** — Maksym's team uses it to process uploaded documents
- **Azure OpenAI** — Used by Maksym's team for summarization
- **Cloudflare Workers** — Maksym's $5/month backend for a 3,400-user WhatsApp bot
- **Mistral OCR** — Mentioned by Aaron's collaborators for parsing complex documents including schematics
- **Google Lyria 2** — Google's new AI music generation model announced at Google I/O
- **Suno** — Alexander (new member) exploring integration with his Telegram music bot
- **Med-Gemma** — Google's specialized medical LLM announced at Google I/O; can be run locally for HIPAA-sensitive use cases
- **Notebook LM** — Alex's first YouTube tutorial topic (Spanish-language channel)
- **OBS** — Used by Alex and Juan for screen recording tutorials
- **CapCut** — Alex using it for video editing
- **SendGrid / Mailgun** — Mentioned as email delivery options for automated alerts
- **Selenium** — Used in an ADK browser-agent demo video Brandon referenced
- **BrowserBase** — Suggested as a replacement for Selenium in browser-agent workflows
- **Vertex AI** — Discussed as an alternative deployment path for ADK agents; Neel has 4 years of experience with it
- **Azure AI Fundamentals certificate** — Recommended for Neel as a structured learning path
- **Excalidraw** — Brandon mentioned using mockups with Lovable to scaffold UIs faster

## links

- Asako shared a link to her bilingual AI podcast website (Japanese/English) — dropped in chat during the call
- Alex shared a link to his new Spanish-language YouTube channel (Notebook LM tutorial) — dropped in chat
- Bastian shared a link to the Graffiti GraphRAG MCP server repository — dropped in chat
- Bastian shared a link to a Vercel open-source UI repo compatible with ADK — dropped in chat
- Bastian shared a link to React PDF Highlighter library — dropped in chat
- Brandon shared a link to an ADK browser-agent tutorial video (using Selenium) — dropped in chat
- Brandon shared a link to Simon Høiberg's YouTube channel for persona/knowledge-base replication — dropped in chat
- Brandon shared a link to Med-Gemma (Google's medical LLM) — dropped in chat
- Brandon shared a link to Google Lyria 2 — dropped in chat
- Brandon shared a link to an ADK thumbnail-generation repo demonstrating MIME-type file upload via callbacks — referenced during screen share

## decisions

- Brandon will send Alex a Loom video review of his first YouTube video with feedback on content, title, and optimization — tomorrow afternoon; Alex to DM Brandon as a reminder
- Brandon will create an ADK + MCP tutorial video by end of the week
- Brandon will continue producing ADK tutorial videos covering additional use cases (targeting 8+ new videos) once the current freelance project wraps
- Brandon will connect with Bert (Robert Chirwa) on LinkedIn
- Paul will build an API over his Reolink NVR and develop an AI-powered video search tool using Gemini Flash for video analysis
- Paul will notify the group when the neighbor-dumping investigation tool is working and demo it
- Marc will convert his fantasy football Crew AI app to Google ADK with a sequential agent architecture
- Maksym will demo the Nissan voice agent (appointment confirmation) once a production version is ready
- Maksym will record a step-by-step YouTube video documenting his document-processing app deployment (Next.js + Python worker + Azure)
- Juan will publish a video documenting his AWS MWAA + RDS ETL pipeline project once finalized
- Aaron (The Dharma House) will attempt the PDF upload fix in ADK using explicit MIME type (`application/pdf`) in a before-model callback
- Aaron will have a budget conversation with the grant-writing client before proceeding further with architecture decisions
- Nate will build an N8N cron job workflow to scan his Google Sheet for empty billing rows and send email alerts
- Neel will research active job postings for AI architect roles to identify which specific tools and frameworks to prioritize studying