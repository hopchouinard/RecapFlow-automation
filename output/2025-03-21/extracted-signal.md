## general

This coaching call brought together a group of AI builders, developers, and entrepreneurs for a round-robin update session facilitated by Brandon Hancock. Brandon opened with two personal announcements: he had recently acquired a Limitless AI pendant (a wearable life-logging device), and his final week at Crayi was approaching as he prepares to go full-time as an independent builder and content creator. The group then worked through individual updates, with each member sharing project progress and receiving feedback from the broader group.

Topics spanned a wide range of technical and professional ground: Juan Torres discussed an upcoming data science presentation in San Diego covering Federal Reserve web scraping, linear regression, and AI agents. Sam raised questions about LLM inference speeds for a high-traffic production system. Paul Miller shared his use of Gemini Deep Research for competitive intelligence and explored GraphRAG architectures for government document analysis. AK (Aaron) demonstrated her Eleanor AI companion project, a RAG-based executive assistant with multi-database architecture. Jake Maymar showed a rebuilt leadership assessment platform with activity tracking and scoring. Andrew Nanton demonstrated a PyQT-based report generation tool using Claude 3.7 with thinking mode. Maksym Liamin discussed deploying a HIPAA-compliant application on Azure. Cyril shared success stories from technical interviews using coaching frameworks from Brandon. Steve demoed a voice-based interview agent built in n8n. Sherif Abushadi walked through a market intelligence content pipeline built in n8n with Airtable, Open Router, and Gemini Flash.

The session had a strong community feel, with members offering each other technical suggestions, moral support around career transitions, and architectural advice. Brandon's impending departure from full-time employment was a recurring emotional thread, with multiple members offering encouragement.

## insights

- **Limitless pendant as an executive coaching tool**: Brandon described using the device's life log each evening to get AI-generated feedback on his day — e.g., it flagged that he was inconsistent across coaching calls and suggested scripting. This pattern (record → reflect → improve) could be applied to leadership development tools.
- **Positioning matters more than features**: Jake's assessment tool failed with early users when framed as a generic assessment, but gained traction immediately after being repositioned around a leadership transformation outcome. The website is the vehicle; the transformation is the product.
- **LLM context window size ≠ quality**: Andrew noted that even with Gemini's large context window, the sweet spot for quality results was still around 30,000 tokens. Jamming more in degrades output quality.
- **Chunking strategy is critical for RAG on messy documents**: Andrew found that preserving heading/subheading context as metadata per chunk (e.g., via Microsoft Document Intelligence or Dockling) and using semantic chunking boundaries made a significant difference in retrieval quality.
- **GraphRAG as an architecture for relational document stores**: Brandon pointed Paul toward the GraphRAG technique (Microsoft and IBM videos) as a way to handle both vector search and relational data across large document collections.
- **Thinking models change the calculus on verification tasks**: Andrew found that Claude 3.7 with thinking mode handled verification tasks (checking that quotes in a report actually appear in the source transcript) that previously required deterministic tool-use approaches. Jake suggested temperature=0 with a simpler model as an alternative.
- **Pseudo-XML tags in Anthropic prompts**: Andrew emphasized that wrapping source material and templates in XML-style tags (e.g., `<template>...</template>`) and placing source material before the prompt instruction significantly improved Claude's output quality.
- **Open Router for model benchmarking and fallback**: Brandon recommended using Open Router's real-time model rankings to compare throughput, uptime, and cost, and using its fallback functionality to chain multiple model providers for resilience.
- **Mistral (Misty) for side-by-side model comparison**: The group identified Mistral as a tool for testing the same prompt across multiple models in parallel, useful for finding the fastest/cheapest model for categorization or intent tasks.
- **n8n workflow design principle**: Sherif advised keeping workflow logic visible at the surface level rather than burying business rules inside sub-networks, so that clients and future-you can understand what the system does. Segment workflows by frequency of change.
- **Poor man's fine-tuning via few-shot examples**: Brandon suggested that before going down a reinforcement learning path, passing 20 high-quality labeled examples plus a larger CSV into a GPT assistant's knowledge base may get you 90–95% of the way there.
- **S-corps offer significant tax advantages** for independent builders; Jake flagged this as worth exploring for anyone making the jump to self-employment.
- **Asking clarifying questions in technical interviews** (about inputs, expected outputs, and direction) signals strong engineering thinking and consistently impressed interviewers, per Cyril's experience.

## qa

**Q (Sam):** I'm looking at inference speeds for LLM APIs for a high-traffic production intent engine. Groq is fast but are there options in the middle?
**A (Brandon):** Use Open Router to browse real-time model rankings for throughput and uptime. Also use Mistral (Misty) to test multiple models side-by-side with the same prompt. For categorization/intent, Gemini Flash or an open-source model like Llama or Mistral are likely your best bets on speed and cost. Open Router also supports fallback chains across providers.

**Q (Paul):** Given Gemini 2's large context window, do you still need to chunk documents carefully, or can you just throw everything in?
**A (Andrew):** Quality still degrades past roughly 30,000 tokens even with large context windows. The best approach is to preserve heading/subheading context as metadata per chunk (using tools like Microsoft Document Intelligence or Dockling), use semantic chunking to find natural boundaries, and combine vector stores with a graph layer for relational data. Brandon added that the GraphRAG technique (Microsoft/IBM) is worth studying for this use case.

**Q (Paul):** How do you handle a large collection of government PDFs where you want to extract both structured data (votes, decisions) and conversational/topical content?
**A (AK):** She uses three databases: Chroma for vector storage of documents and conversations, Supabase/Postgres for structured data, and a graph database for relational data. Every 25 conversation turns, the system summarizes and stores a node in the graph, with the rest chunked and embedded into the vector store. Brandon suggested looking at OpenAI's agent/assistant framework architecture, where all agents operate on a single shared message history object, to avoid dependency hell between agents.

**Q (Andrew):** When verifying that quotes in a generated report actually appear in the source transcript, is it better to use an LLM or deterministic tooling?
**A (Jake):** Setting temperature to zero with a simpler model and a 128k context window can make the LLM behave almost deterministically — useful for verification tasks. Andrew noted that thinking models (Claude 3.7) have worked well for this even at temperature=1 (required for thinking mode), but he's been doing heavy validation to compensate.

**Q (Sherif):** When building a supervised learning layer to mimic a user's tagging and note-taking behavior, do you train one model for all outputs or separate models per task?
**A (Brandon/Jake):** Brandon recommended starting with a "poor man's approach" — few-shot prompting with 20 high-quality labeled examples plus a larger CSV in a GPT assistant's knowledge base — before committing to reinforcement learning. Jake suggested keeping each task as a very simple, focused component and running on free-tier models (like Gemini) where possible to keep costs down.

**Q (Rodrigo):** Is Open Router / Misty considered a "wrapper"?
**A (Brandon):** It's more of a unified interface for interacting with multiple models. Under the hood it may use something like LiteLLM. Open Router charges a small markup (2–5%) on top of model costs in exchange for access to all models and providers.

## tools

- **Limitless Pendant** — Wearable AI life-logging device Brandon demonstrated; records conversations throughout the day and allows end-of-day Q&A on your life log.
- **Open Router** — Used for real-time LLM model benchmarking (throughput, uptime, cost) and fallback chaining across providers.
- **Mistral / Misty** — Side-by-side multi-model testing tool; mentioned for comparing LLM outputs on the same prompt in parallel.
- **Gemini Deep Research** — Google Gemini tool for deep competitive research; Paul used it to generate a 20-page competitor analysis report by scraping 50–100 sources.
- **Notebook LM** — Google tool Paul uses to create a focused, hallucination-resistant Q&A layer on top of curated document sets (legislation, policy documents).
- **n8n** — Low-code workflow automation platform; Steve and Sherif both built production agents with it (interview agent and market intelligence pipeline respectively).
- **Airtable** — Used by Sherif as the admin/inbox interface for his market intelligence pipeline; client interacts with articles, tags, and notes here.
- **Windsurf** — AI-powered IDE; Jake built his leadership assessment platform almost entirely with it; Andrew used it to generate PyQT 6 GUI code.
- **Cursor** — AI-powered IDE; used by multiple members; AK noted it sometimes makes unreported file changes that are hard to track.
- **Supabase** — Postgres-based backend; used by Jake (had a policy issue that Windsurf helped fix) and AK (as structured data fallback).
- **Chroma** — Vector database AK uses for conversation and document embeddings in the Eleanor project.
- **Neo4j** — Graph database referenced for relational data layer in AK's multi-database architecture.
- **LangChain** — Andrew uses its markdown header chunking utility to split report templates by section for parallel LLM processing.
- **Claude 3.7 (Anthropic)** — Andrew's primary model for report generation and verification; uses thinking mode and pseudo-XML prompting style.
- **Microsoft Document Intelligence** — Mentioned by Andrew as a tool for layout-aware chunking that preserves heading/subheading context as metadata.
- **Dockling** — Alternative to Microsoft Document Intelligence for context-preserving document chunking.
- **LiteLLM** — Mentioned as a possible underlying library powering tools like Misty for unified LLM API access.
- **PyQT 6** — Python GUI framework Andrew used (via Windsurf) to build a desktop interface for his report generation tool.
- **Gemini Flash (via Open Router)** — Sherif switched to this from OpenAI for his market intelligence pipeline, reducing costs from ~$10–15/day to near zero.
- **Perplexity** — Mentioned as a comparison point for deep research; Jake uses it for Git command lookups and other quick technical queries.
- **Boot.dev** — Gamified programming learning platform Mitch is using to study Python, HTTP servers, Git, and OOP.
- **Each Chart (Lempod-style LinkedIn automation)** — Brandon recommended this ~$40/month tool for auto-DMing LinkedIn commenters with lead magnet links.
- **Serper** — Web scraping/search API Sherif uses to fetch articles based on keywords for his market intelligence pipeline.
- **Azure App Service / ACR** — Maksym's chosen deployment path: build Docker image locally, push to Azure Container Registry, deploy via Azure App Service.
- **GraphRAG** — Microsoft/IBM technique combining vector search with graph databases for large document collections; Brandon recommended it to Paul.

## links

- No explicit URLs were shared in the transcript (links were mentioned as being pasted into chat but their content was not read aloud or confirmed on the transcript).

## decisions

- **Brandon** will shoot post-call DMs to several members with follow-up resources and action items.
- **Juan** will share highlights or a sneak peek of his Federal Reserve notebook in the community channel before his Wednesday presentation.
- **Juan** will investigate using Google Gemini 1.5 Flash (free tier, 1,500 requests/day) as the LLM API for workshop attendees who need to run the AI agent.
- **Paul** will write up a post about his Gemini Deep Research workflow and what he got out of it for competitive analysis.
- **Paul** will DM AK to discuss potential collaboration on the government document RAG project, which has commercial interest.
- **AK** will connect with Paul via the School community DM to explore the document intelligence project further.
- **Brandon** will schedule a whiteboard architecture session with AK (targeting late next week) to work through multi-agent coordination patterns; session will be recorded for the group.
- **Bastian** will share his Cursor/Windsurf global rules prompt with the group (via Gist, HackMD, or email) since it exceeds Zoom's character limit for chat.
- **Brandon** will onboard Steve into Mighty Networks and send him a message after the call.
- **Sherif** will continue building out the market intelligence pipeline and share a demo/update as the project progresses toward content generation.
- **Mitch** will share his project notes (assigned homework from Brandon) in the community.
- **Brandon** will provide Mitch with a programming learning roadmap/resource list tailored to his goals if Mitch shares what he wants to master.