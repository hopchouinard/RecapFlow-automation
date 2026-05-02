📝 SUMMARY

This coaching call covered a wide range of practical AI development topics, from troubleshooting MCP server issues on Windows to pricing strategies for complex enterprise deployments. Brandon shared updates on the A2A framework's current instability and upcoming video content, while community members discussed Cursor workflows, Python dependency management with UV, and framework choices between ADK and LangGraph. The call featured detailed troubleshooting for ADK artifacts and state management, advice on scoping and pricing multi-component AI projects (RAG, fine-tuning, and model hosting), and discoveries of new tools like Napkin AI for presentations and MultiOn AI for document extraction.

💡 KEY INSIGHTS

Brandon emphasized that the A2A (Agent-to-Agent) framework is not yet stable, as Google is still working toward a version 1 release, meaning implementation details around security and abuse prevention are still being finalized. He recommended using FastMCP for easier MCP server creation rather than building manual request handlers.

Andrew noted that Gemini in Cursor sometimes "chases its tail" more than Claude, particularly on broader tasks, though its large context window is valuable for complex file analysis. Richard shared a technique for unstuck models: telling them to "ultra-think" when caught in loops, which helps reset their reasoning.

For pricing AI projects, Brandon advised Juan to enter discovery mode before quoting, separating the infrastructure deployment (straightforward) from fine-tuning work (complex and scope-dependent). For Sam's internal tool project, Brandon recommended fixed milestone pricing around $20K for businesses with ROI, plus hourly rates ($120-150) for post-launch adjustments, with a two-week testing window included.

Tom observed that image recognition for military aircraft identification performed poorly across all major models (Gemini, Perplexity, Claude) when given limited context, suggesting scaling and context issues remain problematic for specialized visual tasks.

Brandon strongly recommended ADK over LangGraph for developers starting fresh, citing easier agent spin-up and sufficient workflow primitives (sequential, parallel, loop agents) for 90% of use cases, though LangGraph remains viable for complex branching workflows and enterprise environments.

❓ KEY Q&A

Marc asked about persistent "NotImplemented" errors when running MCP servers on Windows. Brandon suggested enabling detailed logging in the server to trace the error, while Bastian recommended checking if NPX is running from the proper location and pointing to the specific Node executable.

Juan asked how to price a project involving LLM deployment, RAG, and fine-tuning on rented NVIDIA hardware. Brandon advised clarifying whether the client needs simple model hosting, RAG per user, or actual fine-tuning pipelines, as the complexity varies dramatically. He suggested engaging a separate ML engineer for the fine-tuning component and starting with discovery to avoid underpricing.

Elad asked why ADK Web wasn't recognizing his runner's initial state and artifacts. Brandon explained that ADK Web only looks for the root agent, not the runner, and recommended using callbacks (specifically before_agent callbacks) to initialize state. For artifacts, he shared a workaround: reading files as byte streams and using types.Part.from_bytes() before saving to the artifact service.

Alex asked about Make versus N8N for simple automation flows. Brandon recommended Make for single-shot LLM calls with no logic, but N8N for anything requiring conditional logic or local model calls via Ollama.

Kanav asked whether to use ADK or LangGraph for a multi-agent marketing tool with web scraping. Brandon recommended ADK for its hybrid chat-and-workflow capabilities, allowing users to chat with an agent that delegates to research agents, then returns results.

🛠️ TOOLS AND CONCEPTS MENTIONED

MCP (Model Context Protocol) - Protocol for connecting AI assistants to data sources and tools; discussed Windows compatibility issues and the FastMCP Python library for simplified server creation.

UV - Python dependency manager and virtual environment tool, preferred by several members over pip and conda for its speed and simplicity.

A2A (Agent-to-Agent) Framework - Google's protocol for agent interoperability, currently unstable and pre-v1, with core principles solidifying but security implementations still in development.

ADK (Agent Development Kit) - Google's framework for building agentic applications; praised for easy setup and hybrid chat/workflow capabilities but noted to have deployment complexity requiring FastAPI wrappers.

Cursor Rules - The .cursorrules file approach is deprecated in favor of granular /rules folder organization, though some find the new system over-engineered compared to single-file configurations.

Napkin AI - Tool for generating presentation graphics and diagrams from text prompts, currently free, useful for client proposals and infographics.

MultiOn AI - Agentic document extraction service by Andrew Ng's team, capable of processing complex forms and handwritten documents spatially, priced at approximately three cents per page.

Factory AI - Newly opened coding agent platform (previously enterprise-only) that uses specialized "droids" for product planning, knowledge management, coding, and reliability.

Sloth - Open-source fine-tuning library for LLMs that works with local CSV training data and recent model architectures.

Supabase vs Firebase - Brandon prefers Supabase for its PostgreSQL structure and schema management via Drizzle ORM, while Firebase/Firestore is document-based and better for rapid prototyping but harder to maintain at scale.

📎 SHARED RESOURCES

FastMCP Library - Python library that simplifies MCP server creation using decorators around tool functions, recommended for avoiding manual request handling setup.

Brandon's ADK Crash Course Playlist - YouTube playlist compiling ADK tutorial videos, recently created to organize the growing catalog of content.

Cursor Tips Community Post - Community-generated thread with 31+ comments containing workflow tips for Cursor, including plan-and-approval prompts and task document strategies.

Tom's Medium Article on Web Architecture - Article discussing scaling bottlenecks and web architecture considerations, referenced for practical infrastructure insights.

ADK FastAPI Deployment Docs - Official Google documentation showing how to wrap ADK applications in FastAPI endpoints for production deployment, replacing older manual endpoint setup methods.

Napkin AI - napkin.ai for automated presentation graphics generation.

🔄 FOLLOW-UPS WORTH EXPLORING

Brandon committed to creating videos on ADK deployment using FastAPI, A2A framework fundamentals, and browser agent implementations. He also plans a community-driven video synthesizing the 31+ Cursor tips from the forum thread.

Marc to test Bastian's NPX path fix for Windows MCP issues and report back on whether enabling detailed server logs reveals the root cause of the NotImplemented error.

Juan to clarify client requirements regarding RAG versus fine-tuning scope before finalizing project pricing, and to investigate bringing on a dedicated ML engineer for the training pipeline component.

Aleksandr to resolve Railway deployment cookie issues by ensuring environment variables are properly configured rather than hardcoded in GitHub repositories.

Elad to test the callback-based state initialization approach for ADK Web and the byte-stream method for artifact handling, reporting results to Brandon.

Community interest in benchmarking Factory AI against existing coding tools like Cursor and Replit once access is obtained.