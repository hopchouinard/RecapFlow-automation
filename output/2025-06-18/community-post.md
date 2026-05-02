📝 SUMMARY

This coaching call covered advanced RAG implementation strategies, framework comparisons between ADK and LangGraph, and practical business advice for AI developers. Brandon Hancock announced upcoming guest speaker Dan Martell and his new Shipkit project for AI application templates. Members shared progress on diverse projects including legal document analysis, grant proposal generation, voice agents, and ML pipeline automation. Key technical discussions centered on chunking strategies, vector database selection, and agent evaluation frameworks.

💡 KEY INSIGHTS

Andrew Nanton argued that with larger context windows, semantic chunking boundaries matter more than ever, and manual inspection of data at every workflow step is crucial for RAG quality. He noted that fixed chunking with no overlap often shears important context, while semantic boundaries preserve meaning even when retrieving larger chunks.

Brandon emphasized that RAG applications often don't require full multi-agent architectures. Straight LLM calls with context retrieval are sufficient unless complex planning, action verification, and iteration loops are needed. He recommended using Supabase RPC functions for vector similarity searches with metadata filtering for multi-tenant document access.

Al Cole advised shifting from hourly billing to value-based pricing by asking "why anything, why your solution, and why now" to quantify client revenue impact. He suggested wrapping high-value projects in quarterly managed services subscriptions rather than one-time fees to capture ongoing value and build annuities.

Brandon recommended Context 7 as an MCP server to give Cursor access to over 19,000 library documentations, dramatically improving code generation accuracy for frameworks like Next.js, Tailwind, and ADK.

Bastian Venegas noted that Manus AI uses visual assessment with CSS overlays to help agents identify clickable elements, reducing confusion from raw HTML parsing. This technique allows vision models to see bounded components rather than interpreting thousands of lines of HTML.

Andrew described his workflow as increasingly specification-driven, using LLMs to write implementation plans and tests while he reviews as a senior engineer overseeing interns. He falls back to familiar stacks like FastAPI and TypeScript because LLMs have more training data on common frameworks, making implementation smoother despite theoretical advantages of niche tools.

❓ KEY Q&A

Q: Alex asked whether he should switch from Next.js/Superbase to a Python-based stack to be more ADK-friendly for his legal RAG application.
A: Brandon advised staying with the current stack for simple RAG queries, explaining that agents are only necessary when requiring planning, action, and iteration loops. He recommended using Supabase RPC functions for vector similarity searches and filtering by metadata to isolate specific documents.

Q: Marc asked why his ADK tool returns empty responses when calling his embedding function, despite working locally.
A: Brandon identified that ADK tools should return dictionaries rather than strings, and need proper docstrings for the agent to understand their purpose. He also recommended adding type hints for better agent comprehension and ensuring the callback updates state correctly.

Q: Andrew asked whether anyone had success with overtly agentic coding systems like Claude Code or Codex compared to Cursor.
A: Brandon noted that while Claude Code resembles Devin in spinning off background jobs, he prefers Cursor for active iteration and seeing code changes in real-time. Bastian added that Codex now supports multiple versions and agents.md files for better context, but requires setup similar to cursor rules.

Q: Juan asked how to connect his CrewAI agentic system to a PostgreSQL database for processing rows.
A: Brandon recommended simple tool calls over full MCP servers for this use case, creating PostgreSQL tools for CRUD operations that CrewAI agents can invoke directly. Al suggested considering whether the data requires real-time triggers or one-time ETL processing.

Q: AK asked how to price his grant proposal MVP and position follow-up versions.
A: Brandon suggested 100 to 200 dollars per hour as standard for AI development, with 6K projects typically including deployment and database components. Al recommended value-based pricing tied to the client's grant revenue percentage rather than hours worked, using the three whys framework to quantify value.

Q: Robert asked about LinkedIn strategy regarding external links versus native content.
A: Brandon confirmed that linking externally reduces reach, recommending instead the giver method of offering free assets via comments to drive engagement. He suggested building authority by summarizing insights from larger brands and tagging them for reciprocal sharing.

🛠️ TOOLS AND CONCEPTS MENTIONED

Chunky: Library for semantic chunking of documents, discussed for legal text processing and evaluating against fixed-size chunking.

Context 7: MCP server providing Cursor access to over 19,000 library documentations including ADK, Next.js, and Tailwind via structured text files.

ADK (Agent Development Kit): Google's agent framework with strong state management but limited native code-step capabilities compared to LangGraph. Supports callbacks for before and after agent execution.

LangGraph: LangChain's framework for agent cycles and state management, preferred when atomic code execution is required between agent steps or when working with finite state machines.

Supabase RPC: Remote Procedure Call functions for executing raw SQL queries with vector similarity search and metadata filtering, used for multi-tenant RAG applications.

Semantic Chunking: Strategy of splitting documents at logical boundaries rather than fixed sizes to preserve context, particularly important for legal and medical documents.

Evals: Evaluation frameworks for AI agents, with Andrew Ng recommending planning for human evals, LLM-as-judge, and production user data analysis early in the development cycle.

Agentic Browser: Tools like GenSpark and Manus AI that navigate websites programmatically. Manus uses visual CSS overlays to identify clickable elements rather than parsing raw HTML.

Convex: Database and npm package using Rust under the hood with real-time UI updates, discussed as potential alternative to Supabase for chat applications though RAG capabilities remain unverified.

PGAI: Timescale and EDB's Postgres extension for automating embeddings and model hosting within SQL databases, creating shadow tables for vector storage.

LiveKit: Platform for building real-time voice agents with phone number integration, interrupt capabilities, and low latency suitable for elderly care applications.

Shipkit: Brandon's upcoming project providing copy-paste templates for chat, RAG, and agentic applications to accelerate development from idea to production.

📎 SHARED RESOURCES

LangChain Interrupt 2025 playlist on YouTube featuring talks from Andrew Ng, Uber, and JP Morgan on enterprise agent building and evaluation strategies.

Context 7 MCP server configuration for Cursor integration, enabling access to 19,000 plus library documentations via single URL setup.

Brandon Hancock's Lovable to Next.js migration template and prompt for converting Vite-based projects to Next.js using git submodules.

Supabase vector search function code example using Drizzle ORM for creating database functions with similarity thresholds and metadata filtering.

React Markdown library for rendering agent outputs as formatted documents rather than displaying raw markdown in user interfaces.

🔄 FOLLOW-UPS WORTH EXPLORING

Testing Convex's RAG and vector store capabilities to verify if it supports custom document embeddings beyond automatic text table embeddings, particularly for PDF processing workflows.

Exploring Perplexity Labs' agentic browsing features for web scraping use cases and comparing reliability against GenSpark and Browserbase for retail site data extraction.

Revisiting LangGraph for projects requiring atomic code execution steps between agent workflows, given ADK's current limitations in pure code execution without tool calls.

Implementing visual CSS overlay techniques similar to Manus AI for browser agents to improve element identification accuracy and reduce context window consumption.

Evaluating EDB and Timescale partner programs for enterprise RAG consulting opportunities, particularly for help desk and support ticket automation use cases.

Creating structured output streaming for Canvas-like document editing interfaces in grant proposal applications, enabling real-time collaboration between users and agents.