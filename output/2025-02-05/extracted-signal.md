## general

This was a community coaching call hosted by Brandon Hancock, with approximately 19 participants. The session followed a round-robin format where members shared project updates, asked for feedback, and helped each other troubleshoot technical and business challenges. Brandon opened with updates on a series of DeepSeek-related videos he had been producing over the weekend, covering model selection for developers and agent performance testing.

The call covered a wide range of topics including sales funnel design for AI consulting businesses, nonprofit grant automation, mental health app development, music education platforms, resume optimization with CrewAI, web scraping tools, distributed systems architecture, and deploying containerized AI applications to Azure. Several members were at early stages of building AI-powered businesses targeting professional services, healthcare, and nonprofits, while others were deeper into technical implementation.

Brandon consistently pushed members toward simplicity in their go-to-market approach — favoring content creation (LinkedIn/YouTube) and a free discovery call over complex funnels, Udemy courses, or elaborate websites. He also celebrated a significant win from Tom Welsh, who landed a five-figure monthly retainer in the oil industry for a cybersecurity/risk dashboard built with Python, FastAPI, and AI models.

## insights

- **Simplify the sales funnel to its core**: Brandon argued that for early-stage AI consultants, the entire funnel should be social media content → free 30-minute strategy call with a calendar link. Everything else (websites, Udemy courses, newsletters) is friction that delays learning what customers actually want.
- **Give away solutions for free to attract paying clients**: Posting content that solves real problems for your target audience demonstrates authority. Customers who can't or won't do it themselves will pay you to do it for them. Brandon cited community member Alexandra's YouTube channel as a model example.
- **Niche down on ICP before building content**: Mike Simko pointed out that doctors and engineers may not be active on LinkedIn, so platform choice should follow where the ICP actually spends time (Reddit, Facebook groups, YouTube).
- **Use forums and webinars to surface pain points**: Paul Miller described using AI to scan discussion forums for the top complaints of a target industry (e.g., law firm admins). Eureka Vanterpool added that monitoring webinar chats is another low-effort way to identify real pain points.
- **Content flywheel**: Start with one real customer's problems, post solutions publicly, and the audience will surface more problems — creating a self-reinforcing content engine.
- **For CrewAI prompt quality, add examples**: Brandon explained that agents need at least one good and one bad example with reasoning to avoid arbitrary outputs. Two contrasting examples are usually sufficient before risking overfitting.
- **AgentOps for crew observability**: Brandon recommended AgentOps (free tier: 100 traces) as a better way to inspect agent conversation history than reading raw terminal output.
- **Large context windows change what's possible**: OpenAI's O3 Mini supports 200K input and 100K output tokens, enabling near-single-shot refactoring of entire codebases — a capability Brandon called a paradigm shift.
- **Use Claude as a dev advisor before touching an IDE**: Paul Miller recommended pasting existing code into a Claude Project, describing the project, and asking Claude to act as an internal dev advisor — especially useful for non-coders inheriting legacy code.
- **Proactive agents vs. reactive agents**: Brian Major raised the idea of agents that initiate actions (e.g., calendar reminders) rather than waiting for prompts — Brandon flagged this as something on his roadmap for "flows."
- **Percentage-based pricing for grant automation**: Brandon suggested that for nonprofit grant work, charging a percentage of funds raised is a compelling model — you win only when the client wins.
- **Build your own solution first**: Paul Miller's "eat your own dog food" principle — using AI tools on your own projects — was highlighted as both a learning accelerator and a reminder to solve your own problems.
- **Distributed systems require explicit job ownership**: When scaling to multiple workers, you must define which worker picks up a job and what happens when a node fails — Brandon recommended AWS SQS with dead letter queues or Azure equivalents as a clean solution.

## qa

**Q (Adam James):** What is the difference between CrewAI and n8n, and which should I use for a RAG-based mental health notes app?
**A (Brandon Hancock):** The choice depends on what you're building. For your case with existing PHP code and a need to add voice transcription, the more immediate priority is getting the code into a tool like Cursor or Lovable and rebuilding it yourself rather than paying more to the existing developer. Brandon offered to connect Adam with talented community members who could help.

**Q (Adam James):** Can I take my existing PHP code, upload it to Cursor or Lovable, and make changes myself — including adding a voice/scribe feature?
**A (Paul Miller / Brandon Hancock):** Yes. Paul recommended pasting the code into a Claude Project and using Claude as a dev advisor to understand what exists and what's possible. Brandon added that OpenAI's O3 Mini with its 200K context window could potentially ingest the entire project for a single-shot refactor. For the voice feature specifically, Brandon pointed to a YouTube video showing Lovable + Clerk + Supabase + Make as a viable no-code/low-code stack.

**Q (Mike Simko):** In the CrewAI resume optimization crew, the matching score seems too high even for mismatched CVs and job descriptions. How do I improve it?
**A (Brandon Hancock):** The crew is missing examples. Without a good example and a bad example (with reasoning), the scoring is arbitrary. Brandon recommended copying the prompt structure from his newsletter crew — which includes process, rules, example input, and example output — and asking an LLM to rewrite the resume crew's prompts in the same style.

**Q (Shima):** How many examples should I include in a prompt, and how do you avoid overfitting?
**A (Brandon Hancock):** One example is usually enough for modern models. Two contrasting examples (one good, one bad) is typically the ceiling before you risk overfitting. The key is to run the task, check the output, and iteratively add examples with explanations only when the output is wrong. Using voice dictation to update prompts quickly speeds up iteration.

**Q (Shima):** What evaluation metrics or tools should I use to assess AI-generated post recommendations at scale, especially for a CI/CD pipeline?
**A (Brandon Hancock / Bastian Venegas):** Brandon recommended Galileo as the most talked-about evaluation tool in production AI circles. He also showed Typeshare's headline reviewer as an example of a methodology-driven scoring framework (audience, outcome, specificity). Bastian added that building a rubric with a 0–5 scale where each level builds on the prior one (like a staircase) is easy for models to follow and can be output as JSON for automated grading.

**Q (Victor):** When a new customer purchases, they appear in the customers table but not the subscriptions table. What's wrong?
**A (Brandon Hancock):** Stripe changed their webhooks approximately two months after the course was released. Brandon acknowledged he needs to update that section of the course. He also suggested the database schema may not match the actual database instance — a missing push — and recommended checking which specific table is failing to narrow down the issue.

**Q (Maksym Liamin):** My job processing system has jobs getting stuck in "running" state. Do I need a full queue service like AWS SQS, or can I keep it simple?
**A (Brandon Hancock):** It depends on scale. For ~10 concurrent users, a single persistent Docker container with simple retry logic is fine. For thousands of users, a proper queue (SQS with dead letter queues, or Azure equivalent) is necessary. Brandon also suggested AWS Step Functions or Lambda + SQS as clean options. Since Maxim's jobs are short-lived (2–4 seconds), a full worker pool may be overkill — but as soon as multiple nodes are involved, job ownership and failure handling become real distributed systems problems that need explicit design.

## tools

- **LinkedIn Sales Navigator** — Adam planning to use for lead generation once content engine is running
- **Miro** — Adam used to present his sales funnel flowchart and automation diagram to the group
- **Udemy** — Adam building a beginner AI/ChatGPT course; discussed limitations on email capture from within the platform
- **Perplexity** — Paul used live on the call to research top AI challenges for small law firms
- **DeepSeek** — Brandon produced multiple videos on it over the weekend; discussed model performance in agent contexts
- **CrewAI** — Core framework discussed throughout; Mike demoed the resume optimization crew example from GitHub
- **AgentOps** — Recommended by Brandon for observability into CrewAI agent runs; free tier includes 100 traces
- **Lovable** — Mentioned as a no-code/low-code frontend builder; Eureka and Adam James both using or exploring it
- **Cursor** — Recommended as an IDE for AI-assisted coding, especially for inheriting and refactoring existing codebases
- **Claude (Anthropic)** — Paul recommended using Claude Projects as a dev advisor by pasting in existing code
- **OpenAI O3 Mini** — Brandon highlighted its 200K input / 100K output token window for near-single-shot project refactoring
- **Supabase** — Mentioned as part of a no-code SaaS stack (Lovable + Clerk + Supabase + Make)
- **Make (formerly Integromat)** — Referenced as an automation layer in no-code SaaS builds
- **Clerk** — Mentioned as an auth solution in the Lovable-based SaaS stack
- **Playwright** — Nate used for browser automation/scraping; noted Google triggers CAPTCHAs, DuckDuckGo does not
- **DuckDuckGo** — Recommended over Google for Playwright-based scraping to avoid CAPTCHA issues
- **Crawl4AI** — Brandon's preferred tool for single-page web scraping; discussed combining with Surfer for multi-page workflows
- **Apify** — Paul recommended for Google Places data extraction as a faster alternative to custom scraping
- **Browser Base** — Brandon recommended for scraping behind login walls (requires a web driver, not just a scraper)
- **WinSurf** — Nate using it as an AI coding assistant to iteratively fix his scraping tool
- **Galileo** — Recommended by Brandon as a leading tool for LLM output evaluation in production
- **Typeshare** — Brandon showed its headline reviewer as an example of a methodology-driven content scoring framework; he previously worked there
- **Ship30for30** — Writing course referenced as a source of content methodology (audience, outcome, specificity framework)
- **Open WebUI** — Bastian running it in Docker as a chat interface connected to his custom backend
- **Super Whisper** — Bastian demoed this Mac/iOS speech-to-text tool; noted it supports custom templates and local models; ~$8/month
- **Mistral Small (24B)** — Bastian running locally; noted as fast and capable for non-heavy use cases
- **Llama 3.2 (various sizes)** — Tom benchmarking on new Mac M4 Max; used as a standard benchmark model
- **Open Router** — Jake using it to access DeepSeek models via API; noted it has become very slow
- **Azure App Service** — Bastian successfully deployed a containerized CrewAI + React app; estimated $12/month for 1 CPU / 2GB RAM
- **Docker** — Maksym and Bastian both using Docker heavily for local development and deployment
- **WhatsApp + Webhooks** — Maksym's car dealership sales tool uses WhatsApp as the customer-facing interface
- **Supabase (blob store)** — Maksym using it to store and retrieve car images, mapped via LLM to user queries
- **AWS SQS / Lambda** — Brandon recommended as a scalable queue architecture with dead letter queues for Maksym's job processing
- **Python FastAPI** — Tom's tech stack for his oil industry cybersecurity dashboard
- **UV** — Bastian noted challenges using UV (Python package manager) inside Docker containers on Azure

## links

- **Alexandra's YouTube channel** — Brandon shared as a model example of content-led funnel for AI automation services; she builds AI receptionists for restaurants and other niches
- **Resume Optimization Crew (CrewAI GitHub, by Tony)** — Mike demoed this example; Brandon flagged it needs prompt improvements (examples, rules, process)
- **Brandon's newsletter CrewAI crew (GitHub)** — Referenced as the best example of prompt structure with examples, rules, and process; recommended as a template for improving other crews
- **Typeshare headline reviewer** — Shown live as an example of a scoring methodology for content evaluation
- **Agent hackathon (virtual, space mission theme)** — Rob shared a link in chat for a weekend hackathon open to anyone
- **Agent project challenge (February–March)** — Rob shared a link for a challenge accepting up to 10 agent project submissions with potential cash prizes
- **Venture capital group investing in autonomous agent startups** — Rob shared a link; offering $50K–$100K checks; Brandon noted the apply button may be broken; Adam and Alex are active on X/LinkedIn

## decisions

- **Adam (Gold Flamingo)** will post daily LinkedIn content this week focused on solving specific problems for professional services firms, rather than building a Udemy course or website first
- **Juan Torres** committed to publishing LinkedIn content this week on banking industry AI insights rather than continuing to over-prepare
- **Brandon Hancock** will update the Stripe webhook section of the AIMP course to reflect changes Stripe made after the course was released
- **Brandon Hancock** will send Adam James a link to a YouTube video demonstrating a SaaS build using Lovable + Clerk + Supabase + Make
- **Brandon Hancock** will connect Adam James with talented community members who could help rebuild his mental health notes app with multi-tenancy and voice features
- **Brandon Hancock** will share his ChatGPT ghost-writer prompt/link with Jake Maymar to help him produce LinkedIn content
- **Brandon Hancock** will reach out to Tony (creator of the resume optimization crew) with feedback on improving the prompts
- **Brandon Hancock** plans to add voice functionality to "flows" as an upcoming feature
- **Bastian Venegas** will write a post/tutorial about deploying CrewAI with a chat interface to Azure
- **Maksym Liamin** will share more detail with Brandon about his job processing architecture for a deeper system design discussion
- **Rob Brennan** plans to apply to the autonomous agent startup VC fund the following day and will report back on results
- **Paul Miller** will share the Perplexity output on law firm AI challenges as a PDF in the community post