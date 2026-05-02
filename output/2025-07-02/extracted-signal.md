## general

This was a group coaching call hosted by Brandon Hancock, structured around a Q&A-first format before moving to round-robin project updates. The session opened with an informal discussion about Cursor's new background agent feature (accessible via Slack), which Ty Wells highlighted as a game-changer for running coding tasks remotely while away from the computer. Brandon then shared a preview of his upcoming "ShipKit" project — a CLI-based scaffolding tool with six to eight templates for chat, RAG, and agentic applications — before the group moved into questions and individual updates.

Topics covered spanned a wide range of technical and business concerns: Oracle NetSuite automation using Apache Airflow, Google ADK agent-to-agent communication errors, MCP server performance, voice AI latency issues with ElevenLabs and Twilio, Cursor billing confusion, Claude Code vs. Cursor workflows, CodeRabbit for automated PR review, HIPAA-compliant infrastructure options, SEO optimization with Lighthouse, and AI consulting go-to-market strategy. The call also touched on LangGraph vs. ADK for enterprise agentic systems, and the value of Langsmith for agent evaluation.

Individual project updates included Tom Welsh demoing a fully AI-built asset management system with 12,000 synthetic users deployed on Vercel/Neon, Andrew Nanton sharing a FastAPI tool for processing large PDFs with Azure Document Intelligence, Maksym Liamin announcing he left his bank job and is relocating to Mexico City while scaling a voice agent product to 4,800 active users, and a new member (Patrick/Chouinpa) describing an internal AI training pipeline at an investment firm using GitHub Copilot and Obsidian.

Brandon closed by committing to produce a video on ADK's new FastAPI + React frontend integration and noted he would be pausing the older AI Marketing Platform course in favor of ShipKit.

## insights

- **Cursor background agents via Slack**: Cursor released a feature allowing agents to be kicked off remotely and communicated with via Slack, enabling async development while away from the computer — described by Ty as a workflow game-changer.
- **Lovable → Cursor handoff workflow**: Ty's recommended pattern is to use Lovable for initial scaffolding, Supabase integration, and session management, then switch to Cursor (or background agents) for feature development.
- **Starting from a working template is the hard part**: Brandon emphasized that 90% of the difficulty in AI-assisted development is having a working baseline — once you have something working, AI can extend it rapidly.
- **Cursor rules as an iterative archive**: Every time AI makes a mistake, add a rule to prevent recurrence. Over time this builds a reusable rule set that dramatically reduces errors across projects. Tom Welsh independently keeps a Git repo of rules.
- **MCP tools may be faster due to JSON-RPC**: Maksym observed that switching from inline tool schemas to MCP servers noticeably reduced latency in voice agents, possibly related to JSON-RPC efficiency, though the exact mechanism wasn't fully resolved.
- **Indexing is the #1 database performance issue at scale**: Brandon explained that without indexing, queries are O(N) linear scans; indexing reduces this to O(log N). Problems won't appear with small datasets but become critical at scale.
- **Don't use Cursor's "max context window" option carelessly**: Andrew burned through significant API costs using this feature; it is described as extremely expensive and not worth it for most use cases.
- **Usage-based pricing in Cursor should be turned off** unless intentional — Tom pointed out the setting, which Brandon had left on and was unknowingly being charged through.
- **AI consulting flywheel**: Brandon's recommended go-to-market for consultants — implement something for a friend/client, immediately turn it into a lead magnet on LinkedIn/YouTube, give away the "how," and let inbound opportunities compound.
- **Enterprise AI consulting requires a concrete playbook**: Vague "use AI" advice fails; clients need specific templates, step-by-step implementation guides, and clear transformation narratives (e.g., "I help X achieve Y").
- **ADK vs. LangGraph tradeoff**: ADK offers simplicity and speed; LangGraph offers granular control at the cost of complexity. ADK is currently missing a robust feedback loop for agent evaluation (Langsmith fills this gap for LangGraph).
- **HIPAA compliance is expensive and complex**: Tools like Fathom ($700/month) and Fireflies offer HIPAA-compliant note-taking; infrastructure compliance can start at $500/month with managed platforms.
- **Brainstorm 3/6/12-month roadmap with clients before building**: One late-stage requirement change (e.g., "we want Gemini") can invalidate entire infrastructure decisions made earlier.
- **Static rendering improves SEO**: In Next.js, minimizing `use client` ensures content is rendered at compile time and visible to search engine scrapers.

## qa

**Q (Alexrojas):** How reliable has Cursor's remote background agent been for you — can you intervene mid-task like you can in normal Cursor?
**A (Ty Wells):** It just came out, so I haven't tried it yet, but I plan it out in detail so there's little room for interpretation. I treat it like a senior developer and just wait for it to complete.

**Q (Juan Torres):** Have you integrated Langsmith to assess context window usage when comparing models?
**A (Brandon Hancock):** Not yet in ShipKit, but there is Sentry for frontend and PostHog planned. Langsmith would definitely be one to add.

**Q (AbdulShakur Abdullah):** Is there an interactive platform that tells you which part of the dev kit to use based on what you want to build?
**A (Brandon Hancock):** Not yet — the core question is just: chat app, RAG app, or agentic app? Once you pick, you can mix in other templates. The hard part is always having something working to start from.

**Q (Jake Maymar):** Can you fine-tune or extend the RAG template with techniques like chain of density?
**A (Brandon Hancock):** Yes — once the vector store and embeddings are set up, you can add layers after the query. You can go as complex as you want, including breaking queries into subcomponents and running parallel queries.

**Q (Cyril I):** Should I use NetSuite's built-in workflow tools or go external?
**A (Brandon Hancock):** NetSuite's built-in tools have limitations since it's primarily a CRM/accounting tool. We used Apache Airflow externally, which gave full control. NetSuite does expose APIs but setting up credentials is painful.

**Q (Cyril I):** What does Apache Airflow actually provide?
**A (Brandon Hancock):** It lets you produce DAGs (directed acyclic graphs) — nodes that perform actions and pass results to the next node, similar to Make.com but enterprise-grade.

**Q (Matias Coca):** I'm getting a 503 network communication error in ADK web UI even though the agents are connecting and completing tasks. What's wrong?
**A (Brandon Hancock):** 503 usually means a server is unresponsive, which is odd for localhost. Try cloning my exact repo and running it — if it works, something in your server's event-sending is wrong. Also make sure you're on the exact same package versions since ADK is changing rapidly.

**Q (Maksym Liamin):** Is MCP faster because it pre-selects the tool before passing it to the LLM, rather than passing all tools?
**A (Brandon Hancock):** My understanding is MCP still returns all tool names, descriptions, and parameters — same as a normal agent. If anything I'd expect it to be slower due to the network hop. The speed improvement might be related to JSON-RPC efficiency, but the exact reason isn't fully clear.

**Q (Maksym Liamin):** Can LiveKit accept your own API keys so you can host the LLM closer to your users (e.g., in Mexico via Azure)?
**A (Brandon Hancock):** Yes — you can use OpenAI Realtime via Azure, and LiveKit has an Azure partner spotlight showing exactly this setup. Bastian confirmed LiveKit is open source and can be deployed anywhere via Docker, including a Brazil server he tested with low latency.

**Q (Al Cole):** Is Lovable a good platform for a consulting website with periodic blog updates?
**A (Ty Wells / Brandon Hancock):** Yes — use Lovable for the frontend and a CMS tool for blog content. The CMS handles posts separately so you never need to redeploy the app for new content. Avoid putting a database behind it in Lovable since that's where it gets complex.

**Q (Juan Torres):** Can you use Gemini CLI the same way as Claude Code inside Cursor?
**A (Brandon Hancock):** Yes, you can use it in the terminal at the bottom of Cursor. Gemini CLI is great for budget developers — very cheap per task — but it's single-shot, not an interactive loop, which limits its use for long-running background jobs.

**Q (Andrew Nanton):** What's the Jules tool and how does it work?
**A (Andrew Nanton):** Jules is a Google background agent (currently free) that connects to GitHub, checks out your code into a VM, makes changes, and sends a pull request when done. It's the async agent workflow Brandon was looking for.

**Q (Neel More):** Do you write cursor rules yourself or use AI to generate them?
**A (Brandon Hancock):** You need one good example written with your own brain power, then AI can analyze your style and generate new rules from errors. The key is: every time something goes wrong, add a rule. Over time you build a reusable archive.

**Q (Jake Maymar):** Do you have templates for unit testing in Cursor?
**A (Brandon Hancock):** Not formally yet — the principle is the same as rules: write one good test with clear reasoning for why, then have AI generate the next ones. It will surface edge cases you hadn't considered.

**Q (Al Cole):** What's the best go-to-market approach for an AI consulting practice starting from scratch?
**A (Brandon Hancock):** Use friends/existing contacts as free or discounted case studies. Every successful implementation becomes a lead magnet — post the "what" on LinkedIn to get people excited, give away the "how" as a free template, and let inbound compound. The flywheel is: action → marketing → new opportunities → more action.

**Q (Juan Torres):** For a secure, private LLM deployment, should I use Oculus data centers or a cloud provider?
**A (Brandon Hancock / Paul Miller):** Depends on egress requirements. Azure gives access to OpenAI with no data leaving the VPC. AWS Bedrock gives access to Claude, Gemini, DeepSeek, Meta models — all locked down. Oculus may be cheaper per GPU but has a primitive UX and single-point-of-failure risk. Most importantly: ask the client about their 3/6/12-month roadmap before choosing infrastructure.

## tools

- **Cursor** — AI code editor; central tool discussed for local development, background agents, and rule-based workflows
- **Cursor Background Agents (via Slack)** — New Cursor feature allowing remote agent kickoff and communication through Slack while away from computer
- **Lovable** — Used for rapid UI prototyping, Supabase integration, and session management before handing off to Cursor
- **Supabase** — Database and auth platform; used for authentication setup and CRUD in Next.js projects
- **Neon** — Postgres database provider; Tom Welsh migrated from Supabase to Neon for his asset management app
- **Apache Airflow** — Enterprise workflow orchestration tool recommended for NetSuite automation via DAGs
- **Google ADK (Agent Development Kit)** — Google's agentic framework; discussed for multi-agent A2A communication and new FastAPI + React frontend integration
- **LiveKit** — Voice AI platform supporting phone number registration, web-to-phone routing, and open-source Docker deployment
- **ElevenLabs** — Voice AI provider; Maksym noted latency issues during peak hours due to US-hosted models
- **Twilio** — Used alongside ElevenLabs for voice agent phone call routing
- **Gemini CLI** — Google's CLI tool for AI-assisted coding; praised for low cost but limited to single-shot (non-interactive loop) prompts
- **Claude Code** — Anthropic's terminal-based coding agent; Andrew used it via Cursor IDE connection with Claude Max subscription
- **Jules** — Google's async background coding agent; connects to GitHub, runs in a VM, submits PRs
- **CodeRabbit** — Automated PR review tool; free tier available as Cursor extension with limits; integrates with Linear/Jira
- **Azure Document Intelligence** — Used by Andrew to convert PDFs to JSON; has 2,000-page limit that his FastAPI wrapper overcomes
- **FastAPI** — Python web framework; used for Andrew's PDF processing tool and discussed for ADK backend integration
- **Langsmith** — LangChain's observability and evaluation platform; discussed for agent tracing and building eval datasets
- **LangGraph** — LangChain's agentic framework; compared to ADK; praised for enterprise control, criticized for complexity
- **Crew AI** — Multi-agent framework; Brandon used it internally at Crew AI for automated documentation generation from changelogs
- **ShadCN** — UI component library; Brandon's go-to for consistent, theme-able components across all projects
- **Tailwind CSS** — Utility CSS framework; used with ShadCN for global styling via two config files
- **Vercel** — Deployment platform; Tom's asset management app is hosted here; noted limitations with Puppeteer/server functions
- **Browserless.io** — Headless browser service; Tom used it as a Puppeteer alternative for PDF export on Vercel
- **Obsidian** — Note-taking tool used by Tom for project planning docs and by Patrick as an MCP-connected memory store in VS Code
- **Notion** — Used by Tom for writing project initiation documents fed into Cursor as context
- **GitHub Copilot** — Enterprise-mandated AI coding tool at Patrick's investment firm; agent mode with Claude Sonnet 4 noted as improving
- **Mobbin** — UI/UX screenshot library for design inspiration; discussed for finding consistent screen design patterns
- **Lighthouse** — Google's built-in browser tool for SEO, performance, and accessibility auditing
- **Ahrefs** — SEO keyword research tool mentioned by Nate for improving website ranking
- **Google Analytics** — Mentioned for tracking website traffic sources
- **Presidio** — Microsoft's PII detection library used in Andrew's anonymization endpoint
- **AWS Bedrock** — Discussed as a secure, model-agnostic alternative for private LLM deployment
- **Palantir** — Enterprise data platform; Jake's healthcare client uses it; noted as very expensive
- **Fathom** — AI meeting note-taker; HIPAA-compliant tier costs $700/month
- **Fireflies** — AI meeting note-taker; HIPAA-compliant and cheaper than Fathom
- **WorkOS** — Enterprise authentication platform; recommended for Tom's asset management app for SSO/directory integration
- **PostHog** — Analytics and feature flagging; planned for ShipKit templates
- **Sentry** — Frontend error monitoring; planned for ShipKit templates
- **Drizzle ORM** — Tom used it to migrate schema from Supabase to Neon
- **UV** — Python package manager used for ADK project setup
- **Vertex AI** — Google's AI platform; used for the RAG template because it's the only provider supporting video chunking/embedding

## links

- Brandon's ShipKit project (screen-shared, no public URL shared yet) — upcoming CLI scaffolding tool with chat, RAG, and agentic templates
- [LiveKit](https://livekit.io) — Voice AI platform with Azure partner spotlight for secure deployment; dropped in chat during voice agent discussion
- [CodeRabbit](https://coderabbit.ai) — Automated PR review tool; free Cursor extension tier discussed; pricing shown at ~$24/month
- [Theo T3 YouTube channel](https://youtube.com/@t3dotgg) — Recommended as top AI/full-stack developer to follow; Brandon credited Theo with helping launch his career
- Google ADK new features blog post (tagged Brandon on Friday, shared in chat) — Covers new React frontend + FastAPI backend integration and planning/multi-step agent capabilities
- LangChain email agent course (watched by Brandon on drive to diving trip) — Recommended specifically for module 3 on agent evaluation with Langsmith
- Brandon's LinkedIn lead magnet post ("99% of developers are making the same mistake") — Shared as a live example of the content flywheel strategy
- Brandon's AI Authority Accelerator video (sent to Al Cole in chat) — Covers personal brand building and lead magnet strategy for consultants
- Andrew's FastAPI PDF processing repo (dropped in chat) — FastAPI tool for large PDF processing with Azure Document Intelligence, filtering, and anonymization; "expect breaking changes"
- [Mobbin](https://mobbin.com) — UI/UX screenshot library for design inspiration; Paul Miller shared the link
- HIPAA-compliant infrastructure platform Jake shared (link dropped in chat, starts at $500/month, built on AWS) — Managed HIPAA/SOC2 compliant infrastructure wrapper
- [Jules by Google](https://jules.google) — Async background coding agent connecting to GitHub; Andrew mentioned it as free currently

## decisions

- **Brandon** will publish a video this week on ADK's new FastAPI + React frontend integration, as promised to Marc Juretus.
- **Brandon** will pause/unpublish the AI Marketing Platform course so new buyers aren't directed to outdated content.
- **Brandon** will turn off usage-based pricing in Cursor settings after Tom Welsh pointed out the setting.
- **Brandon** will add the CodeRabbit Cursor extension this week to get automated PR review.
- **Matias Coca** will clone Brandon's exact ADK repo and run it to isolate whether his 503 error is version-related or code-related.
- **Matias Coca** will verify he is using the exact same package versions as Brandon's ADK project.
- **Jake Maymar** will post a community link about Claude Code with Swarms (Spark 2) for others to explore.
- **Al Cole** will watch Brandon's AI Authority Accelerator video starting the next morning to inform his consulting go-to-market strategy.
- **Al Cole** will target the AWS Summit in New York City (~2 weeks out) as his consulting practice launch event.
- **Brandon** will add a Typeform for pre-submitting questions before the next call (was not completed this week due to the diving trip).
- **Tom Welsh** will post his asset management app update to the community channel.
- **Juan Torres** will discuss infrastructure options (Oculus vs. cloud providers) with his client and present the tradeoffs before committing to a deployment path.
- **Maksym Liamin** will investigate LiveKit's Azure partner integration as a solution for reducing voice agent latency during peak hours in Mexico.
- **Brandon** will investigate whether Langsmith tracing can be mixed into ADK projects after Juan Torres confirmed he successfully integrated it with Crew AI.