## general

This was a weekly group coaching call hosted by Brandon Hancock, with roughly a dozen participants sharing project updates and asking technical questions. The session opened with Brandon announcing an upcoming MCP (Model Context Protocol) tutorial, noting he had shifted from skepticism to enthusiasm about MCP after seeing how major platforms like Notion and GitHub now ship their own MCP servers, eliminating the need to hand-code tool wrappers for every API endpoint.

Participants took turns presenting their work: Alex is building a WhatsApp-based RAG chatbot for a music venue in Mexico; AbdulShakur launched his first YouTube video on his "Prompt Worrier" channel; Marc has been deepening his understanding of vector stores and wants to deploy his first cloud-hosted chatbot; Paul demoed a housing-cost modeling web app aimed at New Zealand economists and government officials; Ty shared a hackathon project (an AI skill-set matchmaker) built under duress with Bolt.new; Juan presented an article on Gemini's diffusion model architecture; Bastian used Selenium, Docling, and an LLM to scrape and analyze 1,000+ government PDFs to expose a permit violation next door; Jake is wrestling with chaotic 800-page invoices for data extraction; Alexander is running a deployed Telegram music-effects bot; Mauri (first-time attendee) described a pharmaceutical geographic-expansion agent system built from 17 custom GPTs; Nate recovered a downed website using Windsurf's SWE-1 model; and Robert is transitioning from data engineering to AI engineering using ADK.

Throughout the call Brandon provided architectural guidance: recommending structured SQL/Airtable over RAG for the venue chatbot, Supabase with Drizzle ORM over manual table creation, the Vercel AI SDK for structured chat outputs, Docling for PDF chunking, Agent Development Kit for multi-agent orchestration, and Cloudflare Workers or Railway for webhook hosting. The call closed with Brandon committing to several upcoming videos including a Cursor tips-and-tricks post, a freelance project retrospective, and a WhatsApp integration tutorial.

## insights

- Brandon (on MCP): Once major SaaS platforms ship their own MCP servers, every API endpoint is instantly available as a tool — no hand-coding required. MCP is most valuable when integrating with common third-party APIs (Notion, GitHub, Google Drive), not for simple custom tool calls.
- For small, structured datasets (e.g., a venue's band schedule), a plain SQL or Airtable database beats RAG. RAG adds complexity without benefit when the data fits on a notepad.
- Maksym: WhatsApp Cloud API does not support push notifications without a lengthy approval process; the user must message first, then the bot can respond instantly. Cloudflare Workers ($5/month) can handle thousands of users and is recommended for hosting the webhook backend.
- Brandon: Supabase + Drizzle ORM is the recommended stack for vector stores in production — Drizzle handles migrations as code, avoiding the fragile manual SQL approach shown in older tutorials.
- Docling is the best-in-class tool for chunking PDFs because it respects document structure (headers, paragraphs) rather than blindly splitting on token count. It can process files up to 16,000 pages (Andrew confirmed).
- Andrew: Docling supports swappable OCR engines (Tesseract, OCR Mac, etc.); switching engines can meaningfully improve results on scanned documents.
- Andrew: Azure Document Intelligence offers structured-output customization and a web playground for testing — worth evaluating for complex, heterogeneous invoice layouts.
- Brandon: Add chat/conversational UI last in a data-visualization app; structured outputs are tightly coupled to the visualization schema, so UI changes force chat rewrites.
- Bastian: Supabase supports database branching/cloning, which is the safe way to test schema migrations without risking production data.
- Brandon: Anthropic's Prompt Generator tool produces well-structured XML prompts; Claude prefers XML while Gemini and ChatGPT tend to prefer JSON for consistent structured output (AbdulShakur).
- Andrew: In Cursor, `/generate cursor rule` auto-generates a project-specific rule to prevent recurring mistakes across chat sessions — a significant productivity cheat code.
- Brandon: Publishing content (YouTube + LinkedIn) is the highest-leverage activity for developers seeking freelance or contract AI work. One video led Alex to a paid government coaching engagement.
- Brandon (content advice): Frame content around "you" (what's in it for the viewer), not "I" — audience-centric framing consistently outperforms personal-journey framing.
- Bastian: When deploying yt-dlp to cloud providers, the server IP is often flagged by YouTube; passing authenticated cookies from a personal account is a workaround, but Brandon warned that sharing cookies risks session hijacking.

## qa

**Q (Alex):** For a WhatsApp chatbot that answers questions about bands at a venue, should I use a RAG query against a vector store?
**A (Brandon):** No — use a structured SQL or Airtable database keyed by date, with band info and an itinerary per date. The data volume is too small to need RAG. The agent just looks up today's or the upcoming weekend's entry and answers from that.

**Q (Alex):** How do I connect the WhatsApp front end to the backend?
**A (Maksym):** Use the Meta WhatsApp Cloud API directly — no Twilio needed if you have a real phone number. Host your webhook handler on Cloudflare Workers; it's $5/month and scales easily. Study the OpenAI and Meta AI WhatsApp bots as UX references for what good streaming and template messages look like.

**Q (Marc):** Why use MCP instead of just writing custom tool functions?
**A (Brandon):** When a platform ships its own MCP server, every endpoint is pre-wrapped as a tool. You skip writing and maintaining wrappers; if the API changes, your code is unaffected. You still don't always need it — for fully custom internal tools, hand-coded functions are fine.

**Q (Marc):** For a production vector store, what stack do you recommend?
**A (Brandon):** Supabase (Postgres with pgvector) plus Drizzle ORM. Drizzle generates and applies migrations programmatically, so you never manually paste SQL into the Supabase editor. Watch the linked YouTube video but substitute Drizzle for the manual table creation shown there.

**Q (Paul):** What's the best way to add a chat interface that updates my housing-cost calculator's charts?
**A (Brandon):** Use the Vercel AI SDK with structured outputs — define the schema you want returned (chart data + narrative answer) and the model will populate it. Treat the chat as an input layer that calls your existing calc API as a tool and returns structured data to drive the UI. Build chat last, after the visualization schema is stable, to avoid rework.

**Q (Ty):** I can't get the Supabase MCP working in Cursor — it only gives me the query tool and it's unreliable.
**A (Brandon):** Switch from `@modelcontextprotocol/server-postgres` to `@supabase/mcp-server-supabase` in your `mcp.json`. Create a Supabase access token (not the DB URI) and pass that. Brandon shared a screenshot showing it listing all tables successfully with that config.

**Q (Juan):** What ETL/pipeline services do people use on AWS instead of running jobs locally?
**A (Paul):** Amazon SQS (Simple Queue Service) is a well-established message-queuing option. AWS Glue is another, though both are proprietary; open-source alternatives exist if vendor lock-in is a concern.

**Q (Mauri):** I have 17 custom GPTs for pharmaceutical analysis. How do I orchestrate them so one question triggers all relevant agents and produces a single report?
**A (Brandon):** Use a multi-agent orchestration framework — Agent Development Kit (ADK), CrewAI, or LangGraph. In ADK, create a root agent that delegates to sub-agents in a sequential workflow: categorize drug → analyze feasibility → generate report. Each agent stores results to shared memory for the next. If code-free is preferred, N8N achieves the same pattern visually.

**Q (Robert):** Is there a video showing how to use Cursor to scaffold an ADK agent and generate the instruction/prompt?
**A (Brandon):** Not yet, but it's now on the to-do list. In the meantime, use Anthropic's Prompt Generator to create the system prompt, then paste it into your agent. A friend's channel will also be releasing a full-stack ADK + Cloud Run tutorial within two weeks.

## tools

- **MCP (Model Context Protocol)** — Brandon announced an upcoming tutorial; praised for giving agents instant access to all endpoints of platforms like Notion, GitHub, Google Drive without hand-coding tool wrappers.
- **Notion MCP** — Used by Brandon as the primary example in his upcoming MCP tutorial.
- **WhatsApp Cloud API (Meta)** — Discussed as the backend for Alex's venue chatbot; Maksym recommended it over Twilio for direct integration.
- **Cloudflare Workers** — Maksym's top recommendation for hosting WhatsApp webhook handlers; ~$5/month, scales globally.
- **Railway** — Brandon's alternative to Cloudflare Workers for hosting Python webhook applications via Docker containers.
- **Airtable / Google Sheets** — Suggested as easy-to-update structured data stores for the venue band schedule, editable by non-developers.
- **Supabase** — Recommended as the all-in-one backend (auth, blob store, Postgres + pgvector) for production AI apps with vector stores.
- **Drizzle ORM** — Recommended over manual SQL or Prisma for managing Supabase schema migrations as code.
- **Docling** — Praised as the best PDF chunking tool; respects document structure; confirmed to handle 16,000-page files; supports swappable OCR engines.
- **Chroma** — Marc used it locally as a vector store while learning vector database concepts.
- **Upstash** — Marc used it (via Langchain) as a hosted vector store in a learning exercise.
- **Vercel AI SDK** — Brandon recommended it for adding structured-output chat to Paul's Next.js housing-cost app.
- **Agent Development Kit (ADK)** — Google's multi-agent orchestration framework; central to Marc's and Robert's projects; Brandon highlighted an active hackathon with large prize pool.
- **N8N** — AbdulShakur experimented with Greg Eisenberg's LinkedIn vibe-marketing N8N workflow; Brandon suggested it as a no-code alternative to ADK for Mauri.
- **Bolt.new** — Ty used it (reluctantly, as hackathon requirement); reported heavy hallucination and poor Supabase integration.
- **Windsurf (SWE-1 model)** — Nate praised SWE-1 for staying focused on requested changes; Andrew had the opposite experience, finding it over-architected simple tasks.
- **Cursor** — Widely used IDE; Andrew shared the `/generate cursor rule` tip; Brandon recommended Gemini 2.5 Pro as the best model to use inside it.
- **Gemini 2.5 Pro** — Brandon's current favorite model in Cursor, now included in the Pro plan at no extra cost.
- **Claude / Anthropic** — Andrew's preferred model for coding tasks; Anthropic was experiencing a major outage during the call.
- **Anthropic Prompt Generator** — Tool that takes a brain-dump description and produces a well-structured XML system prompt; Brandon just discovered it and plans a video.
- **TeleTV** — Brandon's top recommendation for YouTube video recording/editing for full-length videos.
- **Screen Studio** — Recommended for short-form (under 3 min) screen recordings on Mac.
- **Descript** — Mentioned as another solid video editing option.
- **Selenium** — Bastian used it to automate a Chrome browser for scraping a government permit website with no API.
- **yt-dlp** — Alexander and Bastian both used it for YouTube audio/video downloading; Bastian warned cloud IPs are often blocked by YouTube.
- **FFmpeg** — Alexander uses it (via Python) for audio effects (reverb, speed changes) in his Telegram music bot.
- **Surya + Marker** — Andrew mentioned this PDF OCR library pair as an alternative to Docling for markdown output.
- **Azure Document Intelligence** — Andrew recommended it for structured extraction from complex documents; has a web playground and custom output modes; HIPAA-compliant.
- **Amazon SQS** — Paul suggested it as a message-queuing ETL pipeline option on AWS in response to Juan's question.
- **Excalidraw** — Brandon used it live for whiteboarding; Mauri asked about AI-assisted diagram generation; Brandon mentioned Mermaid-to-Excalidraw conversion.
- **DigitalOcean** — Nate accidentally deleted his droplet by canceling his account, taking down his website.
- **Lovable** — Paul used it to build his web front end; plans to migrate to Cursor for cost and code-proximity reasons.
- **CrewAI / LangGraph** — Mentioned alongside ADK as multi-agent orchestration alternatives for Mauri's pharmaceutical agent system.
- **Salesforce AgentForce** — Mauri attended an AgentForce Congress in Paris where he built an agent via conversational prompting.

## links

- **WhatsApp Cloud API Docs** — Brandon dropped in chat for Alex; official Meta documentation for building WhatsApp bots.
- **Brandon's Supabase YouTube tutorial** — Shared with Marc; covers setting up Supabase as a vector store (note: uses manual table creation, superseded by Drizzle approach).
- **Brandon's real-estate offer-letter AI video** — Shared with Paul as inspiration for structured-output chat updating a form/UI.
- **Google ADK Hackathon** — Brandon shared the signup link; month-long competition with large prize pool for ADK-based apps.
- **Brandon's ADK crash course video** — Dropped for Mauri and Robert as the starting point for learning Agent Development Kit.
- **N8N coaching YouTube channel (Brandon's friend)** — Shared as a no-code alternative resource for Mauri to build her multi-agent pharmaceutical system.
- **Anthropic Prompt Generator** — Brandon dropped the link for Mauri and Robert; tool for generating structured system prompts from a plain-language description.
- **Brandon's AI Personal Brand / Authority video** — Shared with Robert; covers LinkedIn + YouTube strategy for AI developers seeking freelance work.
- **Brandon's AI personal brand email sequence / Notion masterclass** — Linked in chat as a deeper companion to the personal brand video.
- **Friend's YouTube channel (full-stack ADK + Cloud Run tutorial forthcoming)** — Brandon dropped it for Robert; upcoming video on deploying ADK agents via Cloud Run.
- **Gemini Diffusion / MDLM paper** — Juan shared the research paper reviewed with the San Diego X Group; covers masked diffusion language models vs. autoregressive LLMs.
- **"Prompt Worrier" YouTube channel** — AbdulShakur's new channel; first video published this week.
- **Greg Eisenberg's N8N LinkedIn vibe-marketing video** — AbdulShakur referenced it as the inspiration for his N8N experiments.

## decisions

- Brandon will review Alex's submitted video immediately after the call.
- Brandon will produce a WhatsApp integration tutorial video (webhook setup, backend connection).
- Alex will build the venue chatbot using a structured database (SQL/Airtable) instead of RAG, and will make a video tutorial once complete.
- Brandon will schedule a 15-minute 1:1 session with Marc (Calendly link sent) to walk through deploying a basic chatbot to the cloud.
- Brandon will publish a community-aggregated Cursor tips-and-tricks post tomorrow, to be turned into a video.
- Brandon will make a video on how to use Cursor effectively to scaffold agents and generate prompts (prompted by Robert's request).
- Brandon will publish a freelance project retrospective video covering his end-to-end workflow and AI tools used.
- Brandon will make a video on the Anthropic Prompt Generator tool.
- Ty will not enter the official Bolt.new hackathon at the end of the month due to negative experience with the tool.
- Ty will try switching his Supabase MCP config in Cursor from the Postgres server package to the Supabase-specific MCP server package using an access token.
- Nate will try Cursor with Gemini 2.5 Pro and report back next week.
- Robert will start a LinkedIn series called "Eight Weeks Later" next week, documenting his ADK learning journey since Google Next.
- Robert will have a first AI agent MVP ready to demo by next week's call.
- Alexander will prepare a demo of his Telegram music bot for next week's call.
- Juan will present at the San Diego software engineering group on June 25th (topic TBD between agentic systems workshop or another format).
- Brandon will reach out to community member Cyril to connect with Jake regarding complex invoice PDF extraction.