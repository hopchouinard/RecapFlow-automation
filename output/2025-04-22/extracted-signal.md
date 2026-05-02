## general

This was a weekly group coaching call hosted by Brandon Hancock, bringing together a recurring cohort of builders and learners working on AI projects. The session opened with updates from Brandon on recent YouTube releases covering Firebase Studio and Google's Agent Development Kit (ADK), followed by a round-robin format where each participant shared their current projects, challenges, or questions.

Topics ranged widely: Cyril discussed a revoked job offer and asked for advice on building a RAG chatbot and breaking into FAANG internships; Paul asked Brandon to compare ADK against other agent frameworks like CrewAI and Pydantic; Michal demonstrated a WhatsApp conflict-resolution chatbot built with Twilio and ngrok; Fernando shared a personal development workbook he wants to convert into a web app; Juan outlined a plan to sell AI-generated news reports to labor unions; Andrew raised questions about OpenAI's newer model lineup; Bastian demonstrated an MCP-powered medical diagnostic assistant using Claude Sonnet; Aaron (The Dharma House) discussed getting connected to the South Florida builder community; and Alex returned after a hiatus to discuss starting a Spanish-language AI YouTube channel.

Brandon served as the primary advisor throughout, offering architectural suggestions, tool recommendations, and business strategy guidance to each participant. Several new faces joined, attributed to recent YouTube video releases on Firebase Studio and ADK.

## insights

- **Brandon:** ADK gained nearly as many GitHub stars in one week as Pydantic AI accumulated over eight to nine months, driven largely by its built-in deployment story via Agent Engine.
- **Brandon:** ADK's Agent Engine pricing is approximately $0.11–$0.20/hour and only charges when agents are running (idle = no charge), making it significantly more cost-effective than most competing frameworks.
- **Brandon:** The key differentiator of ADK over Pydantic AI is that ADK is "built to be deployed" — sessions, state, and database integration are first-class citizens, whereas Pydantic requires you to build all of that yourself.
- **Brandon:** CrewAI still has two advantages over ADK: (1) Flows, which interleave agents and raw code execution, and (2) an easier onboarding experience, though at $50/month for enterprise.
- **Brandon:** For a simple company FAQ chatbot, RAG is unnecessary — the entire policy document fits within modern model context windows, so a straightforward prompt + message history approach suffices.
- **Brandon:** GPT-3.5 Turbo is worse, slower, and more expensive than GPT-4o Mini — developers should stop using it immediately.
- **Brandon:** GPT-4.5 is currently the best writing/conversational model from OpenAI; GPT-4.1 is better than 4.0 as an agent and follows instructions more reliably.
- **Bastian:** MCP is more powerful than traditional function calling but not easier; it remains largely hype with unclear killer use cases beyond GitHub/Gmail integrations.
- **Bastian:** MCP's real potential may lie in building a dedicated server-side prompt layer that makes a complex agent's tool usage more structured and scalable.
- **Brandon:** When positioning an AI service business, framing it as a custom service (thousands of dollars) is far more lucrative than framing it as a SaaS product (hundreds of dollars).
- **Brandon:** Getting a first client at near-cost or free to obtain a testimonial is the critical unlock for a productized AI service business.
- **Paul:** A path into FAANG is to get a job with one of their largest enterprise customers, then return to the tech company with real-world implementation experience.
- **Juan (via Brandon):** Offering an AI-generated weekly news report to labor unions is a strong productized service because it replaces a known manual workflow with clear existing value.
- **Brandon:** For YouTube, the only way to lose is to stop — growth is exponential, and the algorithm rewards longevity and consistency over time.
- **Brandon:** New YouTube creators should start with listicles and how-to videos, then graduate to longer masterclass-style content once comfortable on camera.

## qa

**Q (Paul):** Why is ADK better than CrewAI or Pydantic? Give the sell job.
**A (Brandon):** CrewAI is easier to start and has Flows (interleaving agents and code), but costs $50/month for enterprise deployment. Pydantic requires you to containerize everything yourself and build your own session and state management. ADK is designed from the ground up for deployment — sessions, state, and database hooks are built in, it runs on Agent Engine at ~$0.11/hour (idle = free), and it comes pre-integrated with Google tools like Search and Vertex Search for RAG. The tradeoff is ADK doesn't yet support running raw code nodes the way LangGraph does.

**Q (Cyril):** What's the best way to build a company FAQ chatbot using RAG?
**A (Brandon):** You don't actually need RAG for this use case. A company's entire policy document fits within modern model context windows (~30,000 tokens), so you can just use the Vercel AI SDK with a large system prompt containing the full policy and maintain a message history per session. No agents required.

**Q (Cyril):** How do you get an internship at FAANG companies?
**A (Brandon/Paul/Juan/Michal):** Brandon: Almost everyone he knows at big tech got in through a referral. The buyer's market means they're in no rush. Startups may offer more learning. Paul: Work for one of their biggest enterprise customers first, then return with real-world experience. Juan: His friend started at a startup, then moved to Google Poland. Michal: Many SF startups require relocation, which is a constraint for remote-only candidates; he offered to follow up on a specific remote-friendly company (Marvik).

**Q (Juan):** Would an AI-generated news report service work for labor unions, and how should it be approached?
**A (Brandon):** Yes — it's a great productized service because it replaces a known manual workflow. Use Instantly for cold outreach. Do the first one near-free to get a testimonial. Charge thousands for setup plus a monthly retainer. Keep it positioned as a custom service, not a SaaS. Add upsells like a dashboard for topic preferences and the ability to chat with collected data.

**Q (Andrew):** What are your thoughts on the new OpenAI models — 4.1, 4.5, o4 Mini?
**A (Brandon/Bastian):** Brandon: 4.5 is his favorite writing model — it follows style instructions consistently across long sessions. 4.1 follows instructions well and he tested it at 40K context successfully. Bastian: o4 Mini is significantly better than o3 Mini for tool usage; 4.1 is better than 4.0 as an agent; 4.5 is the best OpenAI writing model. o3 can run code in its chain of thought, which is impressive.

**Q (Brandon):** Is MCP actually useful or just hype?
**A (Bastian):** It's more powerful but not easier than traditional function calling. The real value may emerge when you build a rich server-side prompt layer that structures how tools are used. Right now most demos only show two tools, which doesn't justify the complexity. It's worth watching but not yet worth a deep tutorial.

**Q (Fernando):** Should I use Firebase Studio or something else to build my workbook app?
**A (Brandon):** Firebase Studio currently has painful issues with database and authentication integration. Lovable is the better alternative for going from prompt to application quickly. Pair it with Supabase for database and user authentication. A tutorial on Lovable + Supabase is planned for mid-May. Alternatively, start with a custom GPT per workbook section as the zero-code option.

**Q (Fernando):** Can I use Go High Level for the workbook app?
**A (Brandon):** Not directly for the workbook itself, but Go High Level + Make (with AI/LLM steps) is a powerful combination for automating pipeline-triggered actions — for example, generating personalized messages or doing research when a contact moves through a pipeline stage.

**Q (Alex):** What tools and approach do you recommend for starting a YouTube channel?
**A (Brandon):** Use OBS for screen recording. Hire a video editor on Upwork ($25–$30/hour) and a thumbnail designer ($30/thumbnail) — don't edit yourself. Get a good microphone (Brandon uses a Deity mic). Start with listicles and how-to videos for practice reps. Copy existing successful videos in your niche as a learning exercise, then compare your output to theirs. Screen Studio is great for single-take recordings on Mac.

## tools

- **Google Agent Development Kit (ADK)** — Primary topic of Brandon's update; multi-agent framework with built-in deployment via Agent Engine
- **Agent Engine (Google)** — ADK's deployment platform; ~$0.11–$0.20/hour, charges only when agents run
- **Firebase Studio** — Mentioned as a no-code app builder; currently has issues with database and auth integration
- **CrewAI** — Compared to ADK; praised for Flows feature and ease of use; $50/month enterprise plan
- **Pydantic AI** — Compared to ADK; criticized for lack of built-in deployment and session management
- **LangGraph** — Mentioned for its ability to interleave code nodes with agent nodes, a feature ADK lacks
- **Vercel AI SDK** — Recommended for building simple chatbots in Next.js without needing full agent frameworks
- **Lovable** — Recommended as the best prompt-to-application builder; new version dropping soon
- **Supabase** — Recommended alongside Lovable for database and user authentication
- **Twilio** — Used by Michal to connect his chatbot to WhatsApp via SDK and webhooks
- **ngrok** — Used by Michal to expose local server for Twilio webhook testing
- **Cloudflare (object storage)** — Michal considering it for mid-term message memory in his chatbot
- **OpenAI GPT-3.5 Turbo** — Flagged as worse, slower, and more expensive than newer models; should be replaced
- **OpenAI GPT-4.5** — Praised as best writing/conversational model by Brandon and Bastian
- **OpenAI GPT-4.1** — Noted as better than 4.0 for agent tasks; 1M token context window; not a reasoning model
- **OpenAI GPT-4o Mini** — Recommended as replacement for 3.5 Turbo; cheaper, faster, and better
- **Claude Sonnet (3.7)** — Used by Bastian in his MCP medical diagnostic demo
- **MCP (Model Context Protocol)** — Demonstrated by Bastian; discussed as powerful but complex and still finding its use case
- **Semantic Scholar** — AI-powered academic search tool used as an MCP tool in Bastian's medical demo
- **Brave Search** — Used as an MCP tool in Bastian's demo for fetching fuller article context
- **Vertex Search (Google)** — Mentioned as ADK's built-in RAG solution
- **Instantly** — Recommended by Brandon for cold email outreach for Juan's union newsletter service
- **Make (Integromat)** — Recommended for combining with Go High Level to add AI automation to pipelines
- **Go High Level** — Fernando's existing agency platform; discussed for automation use cases with Make
- **AWS EC2** — Juan was using it with cron jobs for his data pipeline; transitioning away
- **Apache Airflow (on AWS)** — Juan transitioning to this for orchestrating his ETL data pipeline
- **AWS RDS (PostgreSQL)** — Juan's database for storing pipeline data
- **Pinecone** — Mentioned as an example of the fragmented tooling required when using Pydantic AI for RAG
- **OBS** — Brandon's screen recording tool for YouTube videos
- **Screen Studio** — Recommended for Mac users doing single-take screen recordings
- **Upwork** — Recommended for hiring video editors and thumbnail designers
- **Village Labs** — Mentioned by Michal as a frontier AI startup he had referred Cyril's CV to
- **Marvik** — Mentioned by Michal as a potentially remote-friendly company for Cyril; follow-up promised
- **Limitless AI** — Referenced by Bastian as an example of a personal AI companion that could be integrated with MCP

## links

- **ADK GitHub Samples repository** — Shared by Brandon on screen; collection of real-world ADK multi-agent examples ranked by complexity (URL not captured verbatim but described as the official ADK samples repo)
- **Vercel AI SDK documentation** — Shown by Brandon on screen; recommended for building simple chatbots in Next.js
- **Instantly YouTube channel** — Dropped in chat by Brandon; tutorials on cold outreach and building a service business
- **Dave Ebbert MCP crash course video** — Dropped in chat by Brandon; Python-focused MCP tutorial, praised for clarity but noted as not fully answering when/why to use MCP
- **Lovable + Supabase tutorial video** — Dropped in chat by Brandon for Fernando; walkthrough of building an app with Lovable and Supabase (specific creator not named)
- **Lovable Discord** — Mentioned by Aaron in chat; community resource for getting started with Lovable

## decisions

- **Brandon** will review Paul's menu application documentation next week (this week flagged as too busy)
- **Sam** will send Brandon a DM to schedule a one-on-one call that was previously discussed
- **Michal** will upgrade from GPT-3.5 Turbo to a newer model (GPT-4o or GPT-4o Mini) in his WhatsApp chatbot
- **Michal** will refactor his chatbot to decouple the messaging service from Twilio, enabling easier local testing via a web interface
- **Michal** will add a two-panel UI to his local test interface to simulate two phone numbers side by side
- **Michal** will implement database-backed memory using Supabase as the next development step
- **Michal** will follow up with the Marvik team about a potential remote role for Cyril
- **Juan** will begin reaching out to labor union contacts immediately after the call to pitch the AI news report service
- **Fernando** will watch the Lovable + Supabase tutorial video shared in chat and explore getting started with Lovable
- **Brandon** will publish additional ADK tutorial videos including a masterclass and Vertex Search/RAG walkthrough
- **Brandon** will publish a Lovable + Supabase tutorial video targeting mid-May
- **Alex** will begin working on a Spanish-language AI YouTube channel, starting with listicle and how-to format videos
- **Aaron (The Dharma House)** will attend a local builder meetup on Thursday and continue connecting with the South Florida AI/nonprofit community
- **Aaron** will review ADK videos when released to evaluate applicability to the Eleanor project