## general

This was a weekly group coaching and peer-learning call hosted by Brandon Hancock, bringing together developers and entrepreneurs working on AI-powered applications. The session followed a round-robin format where each participant shared project updates, asked technical questions, and received feedback from the group.

Topics spanned a wide range: Mitch walked through a video/image generation pipeline built on Airtable that he is now migrating to a proper software stack; Juan Torres discussed deploying LLMs and RAG infrastructure on an on-premises data center with NVIDIA H100 GPUs; Alex Rojas debugged a date-staleness issue in a deployed voice agent; Al Cole introduced himself and shared artifacts from a Google ADK event in Boston; Ty Wells demonstrated a POS and asset-management SaaS he is building for his own businesses; Paul Miller discussed a potential acquisition of his SaaS company and a RAG project over Auckland city council meeting minutes; Marc Juretus showed a customer-service agent backed by a Postgres database for a fictional arcade game store; Andrew Nanton shared tools for prompt management, evals, and HIPAA-compliant data anonymization; and Robert discussed his journey learning ADK from scratch.

Brandon also previewed upcoming content: an A2A (agent-to-agent) tutorial video nearly finished, a future video on deploying ADK agents via a new FastAPI-style endpoint, and a planned Cursor tips-and-tricks video. The call closed with a discussion of CRM recommendations and a preview of an upcoming interview with the Crew AI team.

## insights

- **Airtable as a prototyping layer has real limits**: Once a workflow is validated in Airtable, migrating to a proper stack (FastAPI backend + Next.js frontend) is the natural next step for scalability.
- **Lovable is best used as a zero-to-one tool**: Brandon recommends using Lovable to quickly mock up a full UI/UX, then exporting to a Git repo and moving to Cursor + Next.js as fast as possible, because Lovable's Vite-based output hits walls when you need server actions and proper data fetching.
- **Data model documentation before coding**: Before touching code, defining even a simple, high-level data model (name, description, no UUIDs needed) is enough to guide Lovable and avoid rework.
- **Chunker selection is one of the most important RAG decisions**: Default token-count chunking almost never produces good results. Match the chunker type (document, recursive, semantic, late chunking) to the structure of the source data.
- **For tabular/SQL data, RAG is not always necessary**: Custom SQL read tools given to an LLM agent can outperform RAG for structured database queries; RAG is most valuable for similarity searches over unstructured text.
- **Use structured outputs + external CSV validation before writing LLM-extracted data to a database**: Run the LLM extraction, save results to a CSV first, validate manually, then do a batch SQL write — avoids hard-to-roll-back errors at scale.
- **Hard-coded date strings in agent system prompts go stale on deployment**: The fix is either (a) move `get_current_time` to a tool call the agent invokes at runtime, or (b) use a `before_model_callback` to dynamically inject the current date into the prompt on every request.
- **MCP server trust matters**: Brandon advises only using MCP servers from verified sources (e.g., official GitHub orgs or the vendor itself) because third-party MCP servers have access to your auth tokens.
- **For building your own MCP server over Google Workspace**: Use FastMCP, pass credentials via environment variable, and reference existing community implementations as a starting point rather than building from scratch.
- **OpenAI embeddings are the pragmatic choice for deployed RAG apps**: Open-source embedding models are free locally but require a separately deployed model in production; OpenAI embeddings are cheap and universally accessible.
- **A2A protocol is early (v0.2) but directionally important**: It abstracts agent-to-agent communication the same way tool calls abstract function execution. The key missing piece is robust authentication; once that lands at v1.0, adoption is expected to accelerate significantly.
- **Crew AI still leads for pure deterministic multi-agent workflows**: ADK is stronger for chat + tool-call agents; Crew AI is stronger when you need multiple agents collaborating on a single task in a structured left-to-right pipeline.
- **LLM Guard runs locally before data leaves your system**: Named entity recognition and anonymization happen on-device via spaCy, making it a useful pre-processing step before sending data to any external LLM, including HIPAA-sensitive workflows.
- **Prompt management and evals should be treated empirically**: Tools like Langfuse let you version prompts, build test suites, and measure pass rates across model updates — giving a data-driven way to refine prompts over time.
- **Identity shift required for experienced developers adopting AI-assisted coding**: Letting go of the habit of writing every line manually is as much a mindset change as a technical one; the productivity delta is enormous once that shift happens.

## qa

**Q (Mitch):** How far do you document the database and valid values before wireframing?
**A (Brandon Hancock):** Just keep data models at a high level — name, a quick description, the core fields. No UUIDs or technical detail needed. Lovable will use dummy data anyway; all you're trying to validate is whether the workflow feels right in the UI.

**Q (Mitch):** What are the pros and cons of keeping a project in Lovable connected to Supabase versus moving it out?
**A (Brandon Hancock):** Lovable generates a Vite project, not Next.js, so you hit walls quickly when you need server actions or proper client/server component separation. The goal is to use Lovable to go from zero to one, get a Git repo, then move to Cursor and Next.js as fast as possible.

**Q (Juan Torres):** For extracting vendor names from a description column, is it better to use an agentic system or a named entity recognition ML model?
**A (Brandon Hancock / Sam / Al Cole / Andrew Nanton):** An LLM call with structured outputs (e.g., GPT-4.1-nano) works well and is very cheap. Extract existing known business names as few-shot examples, use structured output to return only the name or "N/A," save results to a CSV first for manual validation, then batch-write to the database. NER via spaCy or a lightweight ML model is also viable if the format is formulaic; LLM prompting is better when the format is variable or requires inference.

**Q (Alex Rojas):** My deployed voice agent always returns the date it was deployed rather than today's date. How do I fix it?
**A (Brandon Hancock):** The date is being hard-coded into the system prompt at deploy time. Move `get_current_time` into the tool list so the agent calls it at runtime, and delete the static date string from the prompt. Alternatively, use a `before_model_callback` to dynamically inject the current date into the message history on every LLM request.

**Q (Robert / Alex Rojas):** Would it have been better to use an MCP server for Google Calendar instead of building custom API tool calls?
**A (Brandon Hancock):** There is no official Google MCP server for Calendar, only third-party ones. Third-party MCP servers have access to your auth tokens, so trust is a concern. For a small set of tools (create, list, delete, edit event), a direct tool call is simpler and produces less code. If the goal is to connect the full Google Workspace, then building a FastMCP server with credentials passed via environment variable makes sense.

**Q (Al Cole):** Is it worth building a prompt management application to gather, tag, version, and evaluate prompts across models?
**A (Andrew Nanton):** No need to build one — Langfuse is open-source, deployable locally, and supports prompt versioning and eval test suites. BrainTrust has a more polished UI. PromptLayer is another option. Pick one and use it rather than building from scratch.

**Q (Paul Miller):** What architecture and tooling would you recommend for RAG over ~500 Auckland council meeting-minutes PDFs?
**A (Brandon Hancock / Andrew Nanton):** Use Docling for PDF extraction. Choose a chunker matched to the document structure — the hybrid chunker or recursive chunker are good starting points; Chonky AI (open-source) has a visualizer to help evaluate chunking quality. Use OpenAI embeddings for simplicity in deployment. Consider metadata tags to scope vector searches. You can also chain calls: first retrieve relevant chunks, identify which source documents they came from, then do a second LLM call that reads the full document for deeper context.

**Q (Marc Juretus):** When I read a Claude-generated PDF into ChromaDB with LangChain, I get a lot of blank lines and backslash-N characters. Is there a specific PDF format required?
**A (Brandon Hancock):** The issue is likely the LangChain document processor or the PDF generator (QPDF). Try Docling instead, which is purpose-built for document extraction. Also check your ChromaDB version, as older versions can cause parsing issues. If you're generating the content yourself, saving directly as Markdown is cleaner and avoids PDF parsing problems entirely.

**Q (Nate Ginn):** What simple CRM would you recommend that ideally has a chat/AI component?
**A (Brandon Hancock / Ty Wells / Paul Miller):** GoHighLevel ($100/month) includes CRM, email, SMS, pipelines, automation, and is adding AI employees. Pipedrive is simpler, has a strong API that makes it easy to build custom AI interfaces on top, and has good UX — though costs stack up with add-ons. ATTIO was also mentioned as an option.

**Q (Andrew Nanton):** Do you think A2A is going somewhere, and is there a role for it in Crew AI?
**A (Brandon Hancock):** A2A is early (v0.2) but logically sound — it abstracts agent-to-agent communication the same way tool calls abstract functions. The critical missing piece is authentication. Once v1.0 ships with proper handshakes, adoption should rise sharply, especially for inter-company agent communication. Crew AI's multi-agent collaboration model is one of the use cases A2A is designed to enable at a larger scale.

## tools

- **Airtable** — Used by Mitch as a prototyping layer for a video/image generation pipeline before migrating to a real stack.
- **FastAPI** — Paul Miller's preferred Python backend; Brandon also referenced new ADK FastAPI-style deployment endpoint.
- **Google ADK (Agent Development Kit)** — Central framework discussed throughout; used for building multi-agent systems, voice agents, and customer-service bots.
- **Lovable** — AI-powered UI builder used to go from zero to one on front-end mockups before moving to Cursor + Next.js.
- **Cursor** — Primary IDE for AI-assisted coding after exporting from Lovable; used with Next.js projects.
- **Next.js** — Preferred front-end framework; recommended over Lovable's default Vite output for production apps.
- **Supabase** — Database backend connected directly through Lovable; also used via MCP tool in Cursor.
- **Railway** — Deployment platform Alex Rojas used to host his voice agent.
- **Google Imagen API** — Used by Mitch to generate images from shot descriptions in his video pipeline.
- **LlamaIndex** — Juan Torres's candidate framework for building RAG infrastructure over tabular/CSV data.
- **Docling** — Document extraction library recommended for processing PDFs before chunking and embedding for RAG.
- **Chonky AI** — Open-source chunking library with a visual chunking demo; shared by Andrew Nanton as an alternative to naive token chunking.
- **ChromaDB** — Vector database Marc Juretus used for RAG; Brandon noted version can affect parsing behavior.
- **MongoDB** — Paul Miller's preferred document database for hybrid RAG (vector + document search).
- **LangChain** — Used by Marc Juretus for embeddings and document loading into ChromaDB.
- **OpenAI Embeddings** — Recommended by Brandon as the pragmatic choice for deployed RAG applications due to low cost and universal accessibility.
- **GPT-4.1-nano** — Suggested by Brandon for high-volume, low-cost LLM extraction tasks like named entity recognition over large datasets.
- **Langfuse** — Open-source prompt management and eval platform; Andrew Nanton received a free year of the HIPAA-compliant cloud version with a .edu address.
- **LLM Guard** — Open-source library for anonymizing/de-anonymizing PII in documents using spaCy NER before sending data to external LLMs.
- **LiteLLM** — LLM proxy/router Andrew Nanton used alongside Langfuse for multi-model eval comparisons; integrates with LLM Guard.
- **spaCy** — NLP library used by LLM Guard for local named entity recognition.
- **FastMCP** — Framework for building custom MCP servers; recommended for wrapping Google Workspace APIs.
- **Google AppSheet** — Google's internal app-builder (included in Workspace); mentioned by Alex Rojas as a Lovable-like tool for Google-integrated workflows.
- **Google Cloud Spanner** — Used in a Google ADK lab Al Cole attended to store and query a social graph for an event-planner agent demo.
- **Spring AI** — Java/Spring Boot AI integration Marc Juretus demonstrated at work for enriching employee records with LLM-generated data.
- **Streamlit** — Mentioned by Al Cole as the basis of his current ChatGPT-style prototype; Andrew Nanton mentioned FastHTML as an alternative.
- **FastHTML** — Python-based full-stack web framework (no separate front-end/back-end) Andrew Nanton experimented with as a Streamlit alternative.
- **Monster UI** — Tailwind component library for FastHTML mentioned by Andrew Nanton.
- **GoHighLevel** — CRM platform recommended by Brandon for small/medium businesses; includes email, SMS, pipelines, and AI employee features.
- **Pipedrive** — CRM recommended by Paul Miller for its simplicity, UX, and accessible API for custom AI integrations.
- **ATTIO** — CRM mentioned by Ty Wells as an alternative he evaluated.
- **Claude / Anthropic API** — Andrew Nanton uses a HIPAA-compliant Anthropic API account for healthcare-related LLM work.
- **Azure OpenAI (GPT-4.1)** — Andrew Nanton uses an Azure deployment with a BAA for HIPAA-compliant GPT access.
- **Docker** — Marc Juretus runs a Postgres database in Docker for his arcade-store agent demo.
- **Crew AI** — Multi-agent framework discussed in context of ADK comparison and an upcoming interview Brandon is conducting with the Crew AI team.
- **A2A Protocol** — Google's agent-to-agent communication protocol; Brandon just completed a tutorial video covering it with ADK, LangGraph, and Crew AI agents.
- **Google Firebase Studio** — Mentioned briefly in contrast to AppSheet (external vs. internal app building).
- **AI Studio (Google)** — Robert used it with large context windows (uploaded manuals + personal notes) to assist with an online certification.

## links

- **Chonky AI chunking library** — Andrew Nanton dropped a link in chat; open-source chunking library with a visual chunking demo. (URL not captured verbatim in transcript.)
- **Google ADK event presentation and lab artifacts** — Al Cole offered to share slides and lab walkthroughs from a Boston Google ADK half-day event in the AI Developer Accelerator community channel.
- **Alex Rojas's Google ADK data analyst video** — Alex posted a link in chat to a video covering a data-scientist sub-agent example in ADK relevant to Juan's SQL query use case. (URL not captured verbatim.)

## decisions

- **Brandon Hancock** will publish the A2A tutorial video (covering ADK, LangGraph, and Crew AI agents) the following day (Wednesday).
- **Brandon Hancock** will publish a video on deploying ADK agents via the new FastAPI-style endpoint late the following week, including Cloud Run deployment.
- **Brandon Hancock** will publish a Cursor tips-and-tricks video covering the latest Cursor update, incorporating community-submitted tips.
- **Brandon Hancock** will conduct a Crew AI team interview on Friday, asking about new tools/integrations, use cases for entrepreneurs, and (at Paul Miller's suggestion) where Crew AI sits relative to ADK.
- **Al Cole** will share Google ADK event presentation slides and lab artifacts in the AI Developer Accelerator community channel.
- **Alex Rojas** will fix the stale-date bug by moving `get_current_time` to a tool call and/or implementing a `before_model_callback`, referencing the ADK Masterclass for the callback example.
- **Alex Rojas** will investigate building a FastMCP server wrapping Google Workspace APIs, using existing community MCP server implementations as reference.
- **Robert** will build an ADK customer-service agent MVP and demo it on the following week's call.
- **Marc Juretus** will try Docling (instead of LangChain's PDF loader) to resolve the blank-line/backslash-N parsing issue with his RAG pipeline, and will check his ChromaDB version.
- **Paul Miller** will use Docling with a hybrid or recursive chunker and OpenAI embeddings for his Auckland council meeting-minutes RAG project.
- **Andrew Nanton** will share links to Chonky AI and FastHTML/Monster UI resources in the group chat.
- **Brandon Hancock** will send his calendar link to the participant (Lee) who missed the scheduled time due to a timezone mix-up, to reschedule later in the week.