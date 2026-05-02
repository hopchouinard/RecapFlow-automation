## general

This was a weekly group coaching call hosted by Brandon Hancock, focused on AI development, automation consulting, and personal branding for developers. The session followed a round-robin format where participants shared project updates, asked technical questions, and received feedback from Brandon and other community members.

Major topics included: Adam's upcoming proposal to a law firm for workflow automation (Make.com integrations with QuickBooks, OneDrive, and a payment gateway called LawPay); Mitch's interest in building a quick demo app for content calendar visualization; a discussion on LinkedIn growth tactics using lead magnets and Screen Studio; Gemini Flash 2.0's capabilities and pricing; and a deep dive into RAG architecture from multiple participants including Aaron ("The Dharma House"), Jake, and Pavan. Brandon also previewed upcoming community features including a job/collaboration matching post and a new subscription-based pro plan.

Several participants shared live demos or work-in-progress projects: Jake showed a healthcare RAG application with dosage lookup and source citation; Juan Torres shared short-form LinkedIn/YouTube videos on banking data concentration; Mike Simko worked through a web scraping issue live with Brandon; Maksym described a car dealership AI sales assistant nearing a 255-dealership launch; and Nate Ginn discussed a medical scribe project. Paul Miller raised a broader question about how to get technical teams to adopt AI tools, which sparked a discussion involving Dmitry, Jake, and Richard.

## insights

- **Brandon:** LinkedIn posts offering a free resource via DM ("comment this word and I'll DM you") dramatically outperform standard tip-list posts because comments boost algorithmic reach; this strategy feels like "cheating."
- **Brandon:** Screen Studio (Mac only) auto-zooms and positions camera during screen recordings, enabling polished 3-minute demo videos without a video editor.
- **Brandon:** Content should evoke one of two things: strong emotion (anger/excitement) or actionable value. "Interesting" is the worst middle ground — it competes with cat videos.
- **Brandon:** Riding trending topics (e.g., DOGE/government efficiency) as a data scientist is a fast path to views; tie your expertise to what's already in the news.
- **Brandon:** For RAG systems, as context windows grow (Gemini Flash 2.0 at 1M tokens for $0.10), the case for traditional vector stores weakens; a well-maintained blob document may outperform chunked embeddings for many use cases.
- **Brandon:** When building agentic pipelines, introduce cheap intermediate LLM calls (e.g., a grammar/spelling fix step before a database lookup) rather than treating the pipeline as all-or-nothing.
- **Brandon:** Context window management for small local models: summarize conversation history when approaching the token limit and reinsert the summary as an updated system message (rolling window approach).
- **Paul Miller:** When automating a process that reduces someone's workload, that person must be brought on board — they can undermine adoption if they feel threatened.
- **Paul Miller:** Spreadsheets as a source of truth carry ongoing risk; clients tend to let data quality degrade after initial cleanup, undermining the automation.
- **Dmitry:** AI is forcing teams toward all A-players; average performers who don't adopt new tools will become liabilities. Teams will get smaller but more capable.
- **Brandon:** Incentives for one-time course sales are misaligned with ongoing updates; subscription models (monthly new full-stack projects) better align creator and consumer interests.
- **Brandon:** The flywheel for developer consultants: do client work → document it on YouTube → attract new clients who see your expertise AND students who want to replicate it.
- **Richard:** Providing SOPs showing *how* to use AI tools gives hesitant team members a concrete starting point and often unlocks adoption.
- **Brandon:** Decoupling (single responsibility principle) is critical as projects scale — your search function shouldn't know about Azure; it should call a RAG service that handles that detail.
- **Brandon:** Partnerships work when both parties bring something distinct: a developer with a tool + a content creator with an audience is a proven model (e.g., Typeshare + Dickie & Cole).

## qa

**Q (Adam):** I'm pricing this law firm automation project around $6–7K based on the fact that the employee doing this manually costs the business ~$3–4K/month. Does that sound reasonable?
**A (Brandon):** Tying the price to actual cost savings is the right framing. Consider anchoring higher (~$10K) and offering a discount if they start this week to create urgency. Be ready with a negotiation fallback — ask which part concerns them rather than just dropping the price.

**Q (Adam):** Should the client have their own Make.com account that I build into and then hand off?
**A (Brandon):** Yes, that's the right approach — build inside their account, hand it off, and return for maintenance. That protects you from scope creep and gives the client ownership.

**Q (Jake):** Do you also automate the DM replies when someone comments a keyword on LinkedIn?
**A (Brandon):** Not yet automated on LinkedIn — LinkedIn requires a connection to DM, and tools like Hypefury didn't fully support it. Twitter automation works better, but LinkedIn performs far better organically, so manual copy-paste is currently worth it.

**Q (Pavan):** When I run `crewai chat` it can't find my OpenAI API key from my `.env` file, but `crewai run` works fine. Why?
**A (Brandon):** This is a bug — the chat mode isn't loading the `.env` file properly. Workaround: export the key directly in your terminal (`export OPENAI_API_KEY=...`). Brandon noted he's adding a `load_dotenv()` fix to the codebase.

**Q (Mitch):** For a quick demo app (landing page → signup → dashboard with a GPT-powered content calendar), what's the fastest stack?
**A (Brandon):** Use Bolt or Lovable for the frontend connected to Supabase (handles both auth and database in one place). Alternatively, Neon for the database plus Clerk for auth. Someone built exactly this type of project in a weekend — Brandon committed to finding and sending the video.

**Q (Paul Miller):** How do you get technical people inside an existing organization to adopt AI tools?
**A (Dmitry):** Reframe the team standard — everyone needs to be an A-player now. Give them time and permission to learn, but non-adopters need to go. A smaller, smarter team will outperform a larger average one.
**A (Jake):** Focus on passion — people who are genuinely excited will adopt naturally. Some will even spin off their own ventures, which is fine.
**A (Brandon):** Provide the tools (Cursor Pro, open router access) and frame it as promotion — they go from engineer to "manager of junior AI engineers." Remove friction by paying for the tools; the ROI on a few hundred dollars versus their hourly rate is obvious.

**Q (Maksym):** Azure's content moderation is blocking forensic psychiatry documents. How are you handling it?
**A (Maksym):** Fallback to Claude 3.5 Haiku for flagged content. Also reaching out to Azure for Startups to request a relaxed moderation policy.

**Q (Maksym):** What books should I read to strengthen my backend fundamentals?
**A (Brandon):** *Design Patterns* (Gang of Four), *Clean Code*, and *Refactoring*. Also recommended: a YouTube playlist by a creator who covers every design pattern — Brandon shared the link in chat. For scaling, *Designing Data-Intensive Applications* is highly applicable to what Maksym is building next.

**Q (Pavan):** What's the practical difference between CrewAI open source and CrewAI Enterprise?
**A (Brandon):** Functionality is nearly one-to-one. Enterprise adds observability (cost tracking, run history), permissioning, and other features needed for production enterprise deployments. The only open-source features not yet in Enterprise are the chat interface and auto-training. Pricing tiers limit execution volume in Enterprise.

## tools

- **Make.com** — proposed automation platform for law firm workflow (connecting LawPay, QuickBooks, OneDrive, spreadsheets)
- **LawPay** — payment gateway used by the law firm client; PDFs exported from it will be parsed in the automation
- **QuickBooks** — accounting software to be auto-updated via Make.com in Adam's law firm project
- **Tabs 3** — practice management software used firm-wide; identified as a more complex future integration
- **OneDrive / Microsoft Suite** — primary document storage for the law firm; spreadsheets are the source of truth
- **Gemini Flash 2.0 (Google)** — discussed extensively; 1M token context window at $0.10 input cost, hooked up to YouTube, Google Maps, Search; Brandon making a YouTube video on five use cases
- **Gemini Advanced** — personal Google AI subscription with tool integrations; Brandon shared free promo codes (4 months free)
- **Screen Studio** — Mac screen recording tool with auto-zoom and camera positioning; recommended for quick LinkedIn demo videos
- **Hypefury** — social scheduling tool; Brandon tried it for LinkedIn DM automation but it didn't fully support the workflow
- **CrewAI (open source)** — multi-agent framework used by multiple participants for building agent workflows
- **CrewAI Enterprise** — hosted/managed version of CrewAI with observability, permissioning, and enterprise features
- **Lovable / Bolt** — no-code/low-code frontend builders recommended for rapid app prototyping
- **Supabase** — recommended for combined auth + database in quick-build projects
- **Neon** — alternative Postgres database option for projects using Clerk for auth
- **Clerk** — authentication service recommended alongside Neon
- **Cursor** — AI coding IDE; Brandon recommended the Pro plan for developer teams
- **Open Router** — API aggregator for experimenting with multiple LLM models; recommended for dev teams
- **Chroma** — local vector store used by Aaron for RAG; falling back to Qdrant Cloud
- **Qdrant / Qdrant Cloud** — vector database used as source of truth in Aaron's RAG project; experiencing library issues via LangChain
- **LangChain** — used by Aaron for RAG pipeline; encountering Qdrant import issues
- **Docling** — document parsing library Brandon recommended for ingesting content into agent workflows
- **Playwright** — browser automation tool that came up in Nate's web scraping work
- **Crawl4AI** — web scraping library used in Brandon's tutorial and referenced by Nate and Mike
- **Appify** — pre-built scraping tools marketplace; recommended for quickly scraping specific sites without custom code
- **Devin** — AI software engineer tool; Brandon noted it's ~$500/month, useful for delegating GitHub issues
- **Windsurf** — AI coding tool Nate used to scaffold a full project directory from prompts
- **Docker** — used by Maksym to containerize the medical document processing app
- **Azure (OpenAI / Blob Storage)** — hosting environment for Maksym's projects; content moderation causing issues
- **Claude (Anthropic)** — used as fallback model when Azure moderation blocks GPT-4o Mini in Maksym's forensic psychiatry app
- **Ollama / local LLMs** — Jake running small open-source models locally for the healthcare RAG app
- **Vercel** — deployment platform referenced in context of Brandon's YouTube transcription project
- **GitHub** — used for sharing code; Brandon shared newsletter agent repo; Nate made his first public commit
- **Tick Token** — token counting library mentioned for implementing rolling context window summarization
- **Weaviate / v0** — mentioned briefly by Asako in context of her hackathon matching platform frontend

## links

- **Brandon's newsletter agent GitHub repo** — shared in chat; contains `agents.yaml` with writing best practices for content generation
- **Jake Tran YouTube channel** — faceless documentary channel on "dangerous ideas" (money, power, war, crime); shared as content style reference for Juan
- **"Dave" data freelancer YouTube channel** — data scientist turned consultant documenting client work on YouTube; shared as role model for Juan's content strategy
- **Two YouTube videos on fast full-stack app building** — shared by Brandon for Mitch; one specifically shows building a content-calendar-style app over a weekend
- **Docling library link** — dropped in chat by Brandon for Aaron's document ingestion use case
- **Gemini Advanced promo codes** — Brandon shared codes in chat giving 4 months free (2 remaining at time of sharing)
- **Design patterns YouTube playlist** — creator who covers every Gang of Four design pattern; Brandon said it got him through a college class (link shared in chat)
- **Gemini Flash 2.0 SEO analysis prompt** — Brandon's upcoming video example; shared in chat for Nate's competitive research use case
- **Outreach campaign prompt example** — shared for Nate; originally aimed at YouTube channel outreach but adaptable to Google Maps/local business search
- **Juan's LinkedIn video on banking data concentration** — shared on screen during the call; short-form video with data app demo
- **Juan's RAG YouTube short** — second video shared; summarizes a "Mastering RAG" meetup

## decisions

- **Brandon** will add `load_dotenv()` to the CrewAI chat mode codebase to fix the environment variable loading bug reported by Pavan.
- **Brandon** will find and send Mitch the specific YouTube video of someone building a content-calendar-style app in a weekend.
- **Brandon** will record and publish a YouTube video on five Gemini Flash 2.0 use cases (targeting Thursday release).
- **Brandon** will send Miguel a Zoom link for a 1:1 call to debug his CrewAI Enterprise task ordering issue (Miguel to email brandon@crewai.com with availability).
- **Brandon** will create a community post/form to match AI developers seeking work, employers seeking AI developers, and developers seeking build partners.
- **Brandon** will plan a future call session where Aaron presents whiteboard drawings of his personal executive AI assistant architecture for group feedback.
- **Adam** will send his law firm proposal tomorrow and will DM Brandon with the outcome.
- **Juan** will experiment with DOGE/government efficiency themed data science content this week to ride the trending topic.
- **Maksym** will migrate document inputs from local files to S3 or Azure Blob Storage as the next infrastructure step.
- **Nate** will reach out to Maksym about a potential work visa sponsorship arrangement.
- **Asako** will share her hackathon matching platform with event organizers to test for traction.
- **Mike** will iterate through different models on Open Router to find one with a larger input context window for his scraping/LLM pipeline.