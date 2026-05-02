## general

This was a weekly group coaching/community call hosted by Brandon Hancock, who opened with a personal announcement that he had officially left his job to pursue entrepreneurship full-time. He shared a demonstration of how OpenAI's new image generation capabilities had replaced roughly $1,000 worth of branding work he had planned to outsource, reducing the cost to his $20/month subscription. The call then moved into a round-robin format where each member shared updates on their projects and received feedback from the group.

Topics covered included Juan Torres's successful data engineering workshop (scraping Federal Reserve data, building ETL pipelines, and presenting to 15–20 attendees), Sagar Passi's Crew AI demo for financial services clients and questions about agentic frameworks for digital twins, Parker Rex's experience building multi-agent systems and his perspective on the OpenAI Agents SDK, and Bastian Venegas's experiments with OpenAI image generation and a GraphRAG/Neo4j knowledge graph built from over 1GB of Notion documents. Paul Miller discussed competitive pressures on his traditional SaaS business and explored Google Gemini 2.5 Pro for coding. Maksym Liamin shared updates on his WhatsApp-based car dealership bot and interest in the Limitless AI pendant. Nate Ginn discussed a potential business partnership change and ideas for automating medical records sharing. Andrew Nanton offered advice on document generation workflows using LangChain's Markdown chunking library.

Brandon closed with a preview of upcoming YouTube content including OpenAI Agents, Lovable, MCP integrations, and Azure's agent framework (Microsoft Foundry), and encouraged members to post topic suggestions in the community (referred to as "school").

## insights

- Brandon observed that OpenAI's new image generation replaced ~$1,000 of planned branding/thumbnail work for under $20, illustrating AI's deflationary effect on creative services in real time.
- Parker Rex framed the OpenAI Agents SDK as the "Stripe-ification of AI" — packaging previously disparate, hard-to-configure tools into a coherent, well-documented product with built-in logging and observability.
- Parker noted that browser agents are currently "bar tricks" — useful stepping stones but unlikely to have durable business applications once proper APIs exist; the main exception he found valuable was multi-step SEO audits.
- Brandon identified three distinct lead types that can emerge from a technical presentation: potential employers ("hire me"), potential coaching clients ("teach me"), and project clients ("do this for me").
- Andrew Nanton argued that for complex document generation, a minimum viable first draft — even an imperfect one — dramatically reduces friction; the value is overcoming "static friction," not producing a perfect output.
- Maksym Liamin's lesson from Azure deployment: avoid the graphical web interface entirely and work exclusively via CLI.
- Paul Miller noted that effective lead generation requires deep pre-qualification (industry, company size, strategic intent) rather than generic scraping, and that adding research-backed insights to cold outreach dramatically improves differentiation.
- Brandon suggested that cold outreach with agentic research components is about to become significantly more effective, pointing to Instantly's YouTube channel as a demonstration.
- Bastian found that GraphRAG (combining vector embeddings with the Leiden algorithm for community detection) via Neo4j is well-suited for making large personal knowledge bases (e.g., Notion) queryable by agents.
- Brandon noted that the Limitless pendant's API exposes a "life log" that could be used to build an agent that automatically converts spoken commitments into tasks or drafted emails.

## qa

**Q (Sagar Passi):** What frameworks besides Crew AI are available for building agentic teams, specifically for a digital twin use case in financial services?
**A (Brandon Hancock):** For production today, Crew AI or LangGraph are the two best options. Amazon Bedrock already has multi-agent features. Microsoft Azure Foundry is close to launching tooling that will make enterprise agent deployment significantly easier — particularly for connecting knowledge bases and external tools like email — and may become the dominant solution within weeks.

**Q (Sagar Passi):** Is it worth continuing down the Crew AI path, or should we do a bake-off between frameworks?
**A (Brandon Hancock):** Right now, Crew AI or LangGraph are the practical choices for a client recommendation. Azure Foundry and Bedrock aren't ready yet. Keep an eye on Azure Foundry specifically — when their tooling integration launches, it will likely win.

**Q (Juan Torres):** How do you convert the authority from a technical presentation into actual client leads?
**A (Brandon Hancock):** Every person in the room has a different problem. Some are thinking "hire him," some are thinking "teach me," and some want a specific project done. The key is following up individually with every attendee and asking directly how you can help. A soft close at the end of the presentation — "if you're looking to learn this or implement it in your business, reach out" — also helps bridge the gap.

**Q (Nate Ginn):** Could Bastian's GraphRAG/knowledge graph approach work for an EHR database, connecting patient records, chart notes, prescriptions, and uploaded documents?
**A (Bastian Venegas):** Yes — healthcare data is inherently hierarchical and relational (patients → resources → procedures), which maps naturally to a graph structure. The built-in hierarchy can be embedded directly into the system.

**Q (Juan Torres):** Could the Limitless pendant's life log be stored in a vectorized database and used to give AI-powered advice?
**A (Brandon Hancock):** The pendant does have an API that exposes the life log. The next logical step would be an agent that monitors the life log and takes tentative actions — drafting emails, creating tasks — based on spoken commitments. Brandon said he wants to build this when he has more time.

**Q (Juan Torres):** Why did Maksym choose Azure over AWS?
**A (Maksym Liamin):** Primarily because they received $5,000 in free Azure credits. Azure also natively hosts OpenAI models, which aligns with their existing stack.

## tools

- **OpenAI Image Generation (GPT-4o)** — Used by Brandon and Bastian to create YouTube thumbnails and branding assets, replacing expensive freelance work.
- **Crew AI** — Sagar presented it to financial services clients for multi-agent orchestration; discussed as a framework for building digital twins.
- **LangGraph** — Mentioned by Brandon as a production-ready alternative to Crew AI for multi-agent workflows.
- **Amazon Bedrock** — Mentioned as having existing multi-agent features, though not yet fully polished for enterprise deployment.
- **Microsoft Azure Foundry** — Brandon highlighted it as an upcoming enterprise agent framework with easy knowledge base and tooling integration; expected to become dominant.
- **OpenAI Agents SDK** — Parker Rex discussed it as a major improvement that packages multi-agent tooling with logging and observability.
- **Dagger** — Mentioned by Sagar as a company building MCP-related tooling; attended their event.
- **Google Gemini 2.5 Pro (AI Studio)** — Paul Miller praised it for coding tasks, recommending using it directly in AI Studio with large code blocks rather than via Cursor.
- **Sora** — Bastian tried it for video generation; found Runway Gen 4 to be significantly better.
- **Runway Gen 4** — Bastian recommended it over Sora for video generation quality.
- **Neo4j** — Bastian used it as the graph database backend for his GraphRAG knowledge graph built from Notion documents.
- **GraphRAG / Leiden algorithm** — Bastian implemented Microsoft's two-phase RAG combining graph relationships and embeddings for a personal knowledge base.
- **Limitless AI pendant** — Brandon demonstrated it live; records ambient conversations, transcribes in near real-time, and exposes a life log API.
- **Notebook LM** — Paul mentioned using it for competitive research and building business cases.
- **Instantly** — Brandon recommended their YouTube channel for demonstrations of AI-powered cold email campaigns.
- **LangChain Markdown splitter** — Andrew Nanton recommended it for chunking documents by header hierarchy for report generation workflows.
- **Google Colab** — Juan used a Colab notebook for his Federal Reserve data scraping workshop.
- **GitHub** — Juan's workshop included (attempted) uploading of datasets to a GitHub repository as the "load" step of an ETL pipeline.
- **WhatsApp bot** — Maksym's car dealership product; majority of user inputs are voice messages rather than text.

## links

- **Instantly YouTube channel** — Brandon recommended it, specifically their video "Watch me start and sell a service in 10 hours" demonstrating AI-powered cold email lead generation; shared in chat to Paul.
- **Microsoft Azure Foundry demo video** — Brandon referenced a video showing easy knowledge base and tooling hookup in Azure's agent framework; said he shared it in chat but had difficulty locating it during the call.
- **Limitless API documentation** — Brandon showed the life log API endpoint live on screen, demonstrating near-real-time transcription access.
- **Tom's traveling salesman problem post** — Brandon referenced a post in the community ("school") about solving the 49-city traveling salesman problem as a brain teaser; no URL provided.

## decisions

- Brandon Hancock will offer a one-on-one brainstorming call with Sam this week to scope Sam's resource consent document automation project for New Zealand property development.
- Parker Rex will message Brandon via DM after the call to continue their conversation.
- Brandon Hancock will send Paul Miller the Instantly YouTube video link (completed during the call).
- Andrew Nanton will find and post the LangChain Markdown chunking library name/link in the group chat.
- Bastian Venegas will have the updated GraphRAG/Neo4j knowledge graph (with proper entity-based relationships rather than hierarchical document structure) ready to demo next week.
- Brandon Hancock will begin publishing YouTube content on a regular cadence starting next week, with OpenAI Agents, Lovable, and MCP integrations as the first topics.
- Brandon Hancock will increase his daily activity in the community ("school") to a minimum of 30 minutes per day.
- Brandon Hancock will send a poll to the group next week asking for content topic suggestions.
- Maksym Liamin is considering purchasing a Limitless pendant to test as an input device for their car dealership sales bot.
- Paul Miller is expecting delivery of his Limitless pendant within approximately one week.