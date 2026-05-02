📝 SUMMARY

This coaching call covered the full spectrum of AI engineering workflows, from migrating no-code prototypes to production stacks to architecting enterprise RAG systems. Members discussed practical implementation challenges including entity extraction from unstructured data, maintaining date freshness in deployed agents, and selecting between frameworks like Crew AI and ADK for specific use cases. The conversation explored prompt management strategies, HIPAA-compliant AI tooling, and modern deployment patterns using FastAPI and Cloud Run.

💡 KEY INSIGHTS

Mitch shared his progression from Airtable to building a proper software stack, using Lovable for UI prototyping before migrating to Cursor and Next.js, while keeping the backend in Python with FastAPI to avoid TypeScript complexity. Brandon emphasized that Lovable is best used only for "zero to one" prototyping, recommending a quick transition to Cursor for Next.js development since Lovable generates Vite projects that hit limitations with server-side logic.

Paul Miller advocated for maintaining backend control through Python and FastAPI rather than JavaScript-based backends, noting that while AI can generate frontend code, controlling the backend architecture remains critical for long-term stability.

Juan is architecting a RAG system for tabular data using eight NVIDIA 100 GPUs, considering LlamaIndex but also exploring direct SQL query tools. Brandon suggested that for structured data, custom SQL tools often outperform pure vector similarity searches, allowing agents to generate precise queries rather than relying on embedding similarity.

Alex resolved a date-staleness issue in his Railway-deployed voice agent by identifying that hardcoded dates captured at deployment time never update. Brandon recommended using either dynamic tool calls for date retrieval or ADK's before_model_callback to inject current timestamps before each LLM request.

Al and Andrew discussed prompt management and evaluation strategies, with Andrew recommending Langfuse for versioning and testing prompts against evaluation suites, and highlighting LLM Guard for local NER-based anonymization of sensitive data before external API calls.

Brandon clarified the positioning between Crew AI and ADK, noting that Crew AI excels at standardized multi-agent workflows where multiple agents collaborate simultaneously on single tasks, while ADK currently handles sequential tool calling better than true parallel multi-agent collaboration, though ADK offers superior chat-based interaction capabilities.

❓ KEY Q&A

Q: How should I extract vendor names from unstructured description text in database columns - use an agentic system or NER machine learning models?
A: Sam and Al recommended starting with Named Entity Recognition using spaCy or similar lightweight models. Brandon suggested using GPT-4.1-nano with structured outputs, first extracting existing business names to create a reference set, then processing row-by-row to a staging CSV for validation before database updates to prevent data corruption.

Q: Why does my ADK agent on Railway show the wrong date unless I redeploy?
A: The issue stems from hardcoded date strings captured at deployment time. Brandon recommended moving date retrieval to a runtime tool call or implementing ADK's before_model_callback to dynamically inject the current date into prompts before each LLM interaction.

Q: Should I use MCP servers or direct API calls for Google Calendar integration?
A: For simple integrations with fewer than five tools, Brandon recommended direct API calls over third-party MCP servers due to security concerns regarding token handling. For comprehensive Google Workspace integration requiring twenty or more tools, building a custom FastMCP server would be appropriate, though caution is advised with unofficial servers.

Q: How should I architect a RAG system for 400-500 council meeting minutes PDFs to track political promises versus actions?
A: Brandon recommended Docling for PDF extraction paired with a HybridChunker to preserve document structure. Andrew suggested evaluating Chonkie AI for visualizing chunking strategies. For search architecture, Brandon noted that parallel RAG requests with metadata filtering allow a single vector store to serve multiple query types, while Paul considered MongoDB for hybrid vector and keyword search approaches.

Q: What differentiates Crew AI from ADK in practical applications?
A: Crew AI dominates standardized workflow automation with true multi-agent collaboration on single tasks, while ADK excels at conversational interfaces and sequential tool execution but currently lacks native support for parallel multi-agent task collaboration.

🛠️ TOOLS AND CONCEPTS MENTIONED

A2A Protocol: Google's Agent-to-Agent communication standard enabling inter-agent collaboration across different frameworks, currently in v0.2 with authentication improvements expected in v1.0.

ADK (Agent Development Kit): Google's agent framework praised for simplicity and chat capabilities, with new FastAPI deployment options and upcoming Agent Engine UI features.

Chonkie AI: Open-source chunking library with visualization tools for optimizing RAG document segmentation and testing different chunking strategies.

Crew AI: Framework optimized for multi-agent workflow automation where agents collaborate on shared tasks, with upcoming enterprise features and tool integrations.

Docling: Document extraction tool recommended for converting PDFs to clean markdown while preserving structural elements like headings and tables.

FastAPI: Python web framework preferred for backend development to maintain separation from frontend TypeScript complexity.

FastHTML: Lightweight UI prototyping framework that combines frontend and backend without separate JavaScript bundles.

GoHighLevel: All-in-one CRM platform with built-in AI features, automation pipelines, and communication tools, recommended for small to medium businesses.

Langfuse: Open-source prompt management and evaluation platform offering versioning, testing suites, and HIPAA-compliant cloud hosting for educational users.

LLM Guard: Open-source library for local Named Entity Recognition, data anonymization, and guardrail implementation before external API calls.

Lovable: AI-powered UI generation tool recommended for rapid prototyping from zero to one, with intentional migration to Cursor/Next.js for production features.

MCP (Model Context Protocol): Standard for connecting agents to external tools, with security considerations regarding third-party server authentication handling.

Railway: Deployment platform used for hosting containerized ADK agents with persistent execution environments.

Supabase: PostgreSQL database platform frequently paired with Lovable for data persistence before migration to production environments.

📎 SHARED RESOURCES

Brandon's upcoming A2A tutorial video demonstrating interoperability between ADK, LangGraph, and Crew AI agents using the Agent-to-Agent protocol.

Brandon's upcoming ADK deployment video covering FastAPI integration, API endpoint exposure, and Cloud Run deployment strategies.

Al's Google ADK event artifacts from the Boston developer session, including presentation materials and hands-on labs covering Spanner integration and social graph agent scenarios.

Alex's referenced video showcasing Google ADK data analyst sub-agent implementations for SQL query generation and data visualization.

Andrew's recommendation of the Chonkie AI repository for advanced document chunking with visualization capabilities.

🔄 FOLLOW-UPS WORTH EXPLORING

Testing the new ADK FastAPI deployment method versus traditional Agent Engine deployment for production agent hosting.

Evaluating A2A protocol adoption patterns once v1.0 releases with standardized authentication mechanisms.

Benchmarking LlamaIndex against direct SQL tool approaches for Juan's tabular data RAG system on high-GPU infrastructure.

Investigating the "liquid glass" UI design pattern implementation in Lovable for modern interface aesthetics.

Building a comprehensive Google Workspace MCP server for enterprise use versus relying on scattered third-party authentication servers.

Measuring cost efficiency of GPT-4.1-nano for large-scale entity extraction tasks compared to traditional NER models.

Exploring Crew AI's response to ADK competition and their roadmap for visual workflow builders.