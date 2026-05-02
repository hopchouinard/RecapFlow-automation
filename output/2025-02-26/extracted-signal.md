## general

This was a group coaching call hosted by Brandon Hancock, with approximately 24 participants joining from various time zones. The session followed a round-robin format where each participant shared a win, a problem, or a project update, with Brandon and others offering feedback and advice. The call covered a wide range of topics including client acquisition, AI tooling, freelance pricing strategy, content creation, and technical architecture.

Brandon opened by announcing a new program he is launching called the "AI Authority Accelerator," an 8-week group coaching program designed to help developers build an AI personal brand on YouTube and LinkedIn in order to land their first paid client. He also previewed a 5-day email masterclass on AI personal branding. The second major throughline was the excitement around Claude 3.7's release, with multiple participants sharing early impressions of its coding performance, particularly when used with Cursor's agent mode.

Technical updates ranged from Maksym's near-launch of an automotive dealership application to Aaron's deep dive into hexagonal architecture and Neo4j for his personal AI assistant "Eleanor," to Cyril's work on medical handwriting extraction using transformer models. Business and freelance topics included Tom Welsh landing a potential consulting engagement from a cold introduction on a train, Sherif working through niche selection for an AI education business, and Adam landing a Shopify development project through a prior relationship.

## insights

- **Tom Welsh (and reinforced by Paul Miller):** Handing a business card with two hands and letting the other person take it — rather than pushing it on them — signals that the card has value. Cold introductions in real life (e.g., on a train) can directly convert to paid engagements.
- **Brandon Hancock:** Never do work for free if you can avoid it. Clients need skin in the game or scope creeps infinitely and feedback quality drops. Even a nominal charge changes the dynamic.
- **Brandon Hancock:** When entering a client engagement, you wear two hats: AI implementer and AI consultant. Always be surfacing the next problem they'll face — this is how McKinsey never runs out of work.
- **Brandon Hancock:** AI without systems is just more manual work. Build the foundation (task manager, database, automations) before layering in AI agents.
- **Brandon Hancock:** We are currently in a short window of arbitrage — talented developers can build things in a fraction of the time they used to, but clients haven't fully recalibrated their pricing expectations yet.
- **Jake Maymar:** Clients consistently overestimate what agents can do and want to automate everything at once. Force them to articulate the problem in one sentence before scoping anything.
- **Andrew Nanton:** The more you remove human oversight from an agentic pipeline, the higher the risk of a bad outcome. Intermediate checkpoints and human-in-the-loop design are critical, especially for clients who have already been burned.
- **Brandon Hancock:** When building RAG or memory systems, start with the simplest working version (vector store only) before adding caching layers and graph databases. Complexity should be earned by a working baseline failing to meet requirements.
- **Paul Miller:** Imposter syndrome is normal at the start. Tom Welsh is a living example of someone who had the same doubts six months ago and is now cold-pitching on trains.
- **Brandon Hancock:** "Just-in-time learning" — learn the exact skill you need right when you need it — beats trying to master everything upfront and never shipping.
- **Brandon Hancock:** When comparing AI models for a production application, cost matters enormously at scale. A cheaper model that delivers equivalent results can save hundreds of dollars over thousands of requests.
- **Jake Maymar:** Running Linux (dual boot) noticeably improves local model performance compared to Windows.
- **Brandon Hancock:** Vertical AI SaaS applications — where an expert's domain knowledge is encoded into a trained model and wrapped in a clean UI — represent the next major wave of opportunity.

## qa

**Q (Pavan Vemuri):** Are the Cursor agent features (including Claude 3.7 agent mode) only available on the pro version?
**A (Brandon Hancock):** Likely yes for the agent functionality, though you can pass your own API key for individual chat requests. As a developer, if the tool lets you do more work per hour than it costs, it's a net win regardless of the subscription price.

**Q (Adam Hanson):** I'm hitting my compute hours limit on Neon (the database). Should I just upgrade or switch databases?
**A (Brandon Hancock):** For finishing the course project, just upgrade temporarily. For production client work, the real fix is switching from a polling architecture (server checking the database every few seconds) to a queue-based push architecture, which dramatically reduces database hits. Happy to walk through the structural code change on a one-on-one call.

**Q (Adam Hanson):** I'm getting a deprecation warning on `pgTable` in my newer Drizzle ORM version (0.37) compared to the course project (0.36). Is this a big deal?
**A (Brandon Hancock):** It's a versioning issue — minor version bumps in packages can introduce breaking changes. Pinning your drizzle-orm to version 0.36 in package.json and running npm install will resolve the squiggly warning without breaking your code.

**Q (Nate Ginn):** I have a working Python script that extracts data from my EHR, processes it, and exports to Google Sheets. How do I add an AI review step without rebuilding everything?
**A (Brandon Hancock):** Use CrewAI Flows — a step-by-step pipeline where each step listens for the previous one to complete. You can add a single LLM call (self.llm) in a new step that takes the processed data and reviews it for correctness. You can also enforce structured output types so the LLM returns validated data objects. Alternatively, n8n (self-hosted) would be a great fit here since it keeps patient data on-premise and supports local models.

**Q (Sherif Abushadi):** I feel like it's disingenuous to cold-email people offering AI help when I have zero customers. How do I get past this?
**A (Brandon Hancock):** Pick one niche — even if it's not the perfect choice — and go get one client at a low or nominal rate. The goal is self-discovery: can you deliver, and what are you actually good at? The imposter syndrome dissolves once you've shipped something real. Momentum matters more than the perfect decision right now.

**Q (Mike Simko):** I want to scrape LinkedIn and build an org chart that reveals informal power structures within a company. What data structure would you recommend?
**A (Brandon Hancock):** Model it as Department → Level (with a priority/rank number) → People (array). This lets you infer hierarchy even though LinkedIn doesn't make reporting relationships explicit. You'll also need a separate object for horizontal/cross-functional roles. Draw it visually first, asking for each object: what does it have, and who does it belong to?

**Q (Richard):** My B-roll agent has a function that's supposed to cache images from my website for use in videos, but it doesn't seem to be working. Should I use Supabase or blob storage?
**A (Brandon Hancock):** You probably don't need to cache at all. Every image on your website already has a URL. Most video generation tools accept either a URL or a base64-encoded image directly — you should be able to just pass the existing URL. Send a Loom walkthrough and I can pinpoint the exact issue.

## tools

- **Claude 3.7 (Anthropic)** — New model praised by Paul Miller and Brandon as a major coding productivity boost; base 3.7 (non-thinking) recommended for coding tasks.
- **Cursor** — AI code editor; agent mode with Claude 3.7 highlighted as a game-changer for faster iteration; discussed in context of pro plan features.
- **Claude Code (Anthropic preview)** — Terminal-based agentic coding tool from Anthropic; currently at capacity/waitlist; Paul Miller shared access credentials with Brandon.
- **CrewAI** — Multi-agent framework; Brandon demonstrated Flows for step-by-step pipelines; Mike Simko asked about enterprise licensing for embedding in a SaaS product.
- **n8n** — Workflow automation tool; recommended by Brandon for Nate's EHR data pipeline, especially for self-hosting to keep patient data on-premise.
- **Neo4j** — Graph database; Aaron (The Dharma House) using it for relational memory in his Eleanor assistant; Mike Simko researching it for org chart visualization.
- **Supabase** — Postgres-based backend; mentioned by Aaron as a vector store adapter and by Adam in context of database options.
- **Chroma** — Vector database; Aaron using it as primary vector store for Eleanor while keeping Supabase as a future adapter.
- **V0 (Vercel)** — Used by Brandon to build internal operations systems for a wedding venue client.
- **Notion / Airtable** — Mentioned by Brandon as foundational tools in the "skill stack" for any AI consulting engagement.
- **Make / Zapier** — Mentioned as automation glue tools alongside Notion/Airtable for building client systems.
- **Neon** — Serverless Postgres database used in Brandon's full-stack AI marketing platform course; Adam hitting compute hour limits on free tier.
- **Drizzle ORM** — TypeScript ORM; version mismatch (0.36 vs 0.37) causing deprecation warnings discussed with Adam.
- **Gemini 2.0 (experimental thinking model)** — Used by Andrew in a mental health AI hackathon sponsored by Google; performed well on structured scoring tasks.
- **MSTY** — Mac GUI for AI models; Andrew recommended it for sending the same prompt to multiple models simultaneously for quick comparison.
- **Replit** — Web-based IDE with natural language coding; Adam's friend at HubSpot enthusiastic about it; group discussed its business success.
- **Perplexity / Deep Research** — Suggested by Richard as a way to find obscure medical datasets that don't surface easily in standard Google searches.
- **Zinflow (n8n reference)** — Aaron mentioned it as a sub-agent component for task scheduling and execution monitoring in Eleanor.
- **Shopify** — Adam building a store rebuild for a returning client as a freelance project.
- **Excalidraw** — Whiteboard tool used by Brandon during the call for diagramming data structures; recommended for visual architecture planning.
- **OpenRouter** — Brandon mentioned as a planned update to the full-stack AI marketing platform course to replace direct OpenAI calls and enable model fallbacks.
- **Clerk / Stripe** — Also flagged for updates in the course alongside OpenRouter, targeted for mid-April.
- **Deep Seek** — Jake mentioned running it locally on Linux for improved performance.

## links

- **AI Authority Accelerator landing page / email masterclass** — Brandon dropped a link in chat for a 5-day email masterclass on building an AI personal brand; the group coaching program launches March 30th.
- **Design Patterns playlist (YouTube)** — Brandon shared a free YouTube playlist on object-oriented design patterns (singleton, etc.); described as "saved me in my master's class." Shared in chat for Maksym and the group.
- **Snow Leopard (book)** — Recommended by Brandon to Sherif for niche selection and content strategy; described as "the best book for picking a niche."
- **Blazing Zebra (YouTube channel)** — Suggested by Richard as a resource for finding obscure data sources; has a video specifically on locating datasets.
- **My First Million podcast episode on Replit** — Brandon referenced an episode discussing Replit's business growth from YC rejection to billion-dollar valuation; said he'd share the link.
- **MSTY tool** — Andrew dropped a link in chat for the Mac multi-model comparison GUI.

## decisions

- **Brandon Hancock** will connect Mike Simko directly to a CrewAI sales team contact; Mike to send a paragraph DM with context.
- **Brandon Hancock** will post the N8n full-stack developer job opportunity (shared by Mike Simko) to the community forum for broader visibility.
- **Brandon Hancock** will review Richard's B-roll agent image-caching issue after Richard sends a Loom video walkthrough.
- **Brandon Hancock** will review Nate Ginn's EHR data pipeline code after Nate sends a Loom video, with the goal of adding a CrewAI/LLM review step.
- **Brandon Hancock** will hop on a one-on-one call with Adam Hanson to walk through switching the marketing platform course project from a polling to a queue-based database architecture.
- **Brandon Hancock** will update the full-stack AI marketing platform course (OpenRouter, Clerk, Stripe) targeting mid-April, after the AI Authority Accelerator launch.
- **Pavan Vemuri** will prepare an Excalidraw whiteboard showing current state, goal state, and end goals for his automotive AI research agent, to be reviewed at the start of the next call (Tuesday).
- **Sherif Abushadi** committed to picking a niche this week and testing content ideas on LinkedIn before the next call.
- **Brandon Hancock** will plan a community networking/project showcase session after the AI Authority Accelerator launch (post-March 30th).
- **Maksym Liamin** will write stress tests targeting 2,000 concurrent users before the Friday launch of the automotive dealership application.
- **Brandon Hancock** will share a video about Replit's founder story in the community channel.
- **Paul Miller** will share Claude Code access credentials with Brandon via DM.
- **Aaron (The Dharma House)** will simplify Eleanor's architecture by getting the vector store working end-to-end before adding the cache layer and Neo4j graph, aiming for a working beta by end of March.