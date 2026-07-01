📝 SUMMARY

This week's show-and-tell call featured deep dives into production AI implementations across software development, business operations, and hardware ventures. Brandon Hancock shared progress on his EMS startup including a $100K sales pipeline and personalized cold outreach systems, while demonstrating new Even Realities smart glasses with Claude Code integration. Patrick Chouinard unveiled AgentOps, a comprehensive homelab automation harness using Hermes, NATS, and multi-model PR review loops. Scott Rippey presented adversarial security review hooks using Claude and Codex, Ty Wells showcased creative problem-solving by recovering a lost wearable via GPS cross-referencing and voice-driven coding agents, Juan Torres demoed an AI photo booth hardware venture with franchise potential, and Bastian Venegas Arevalo introduced Pixir, an Elixir-based agentic framework optimized for memory efficiency. The session centered on practical strategies for revenue generation, automated code review pipelines, and building defensible businesses at the intersection of physical hardware and AI.

💡 KEY INSIGHTS

Cold Outreach Feedback Loops: Send personalized Loom videos to prospects, then extract exact language from discovery calls to refine your next pitch deck. Over time you articulate their problems better than they can, dramatically improving conversion.

Sniper vs Spray Outreach: With finite addressable markets like 18,000 EMS agencies, high-value hyper-personalized outreach beats mass email blasting. Burning the market with low-quality touches is irreversible.

The Reviewer Bottleneck: When AI accelerates code production 10x, human review becomes the bottleneck. Solve this with sandboxed ephemeral environments like Supabase branches and parallel feature development.

Work Backwards from Revenue: Calculate exactly how many daily outreaches are needed to hit target revenue within a defined timeframe. This converts abstract goals into simple daily checklists and removes timeline anxiety.

Deflationary AI Margins: Businesses built on AI-generated outputs see margins improve automatically as model costs fall. You lock in capability at today's price while costs drop in 6 to 8 months.

Hardware Plus Software Moats: Combining physical hardware with software creates significantly deeper competitive moats than pure software plays, particularly relevant for vending machine or franchise models.

Adversarial Model Review: Never use the same model that wrote the code to review it. Using Codex as an adversarial reviewer against Claude-written code catches edge cases neither model would self-identify.

Data as Primary Asset: The most valuable thing an AI-augmented developer accumulates is their own structured data including documentation, review history, and app context. AI models are commodities but your data is proprietary.

Automated PR Loops: Instruct Claude Code to push a PR then monitor it for 30 minutes resolving every comment, creating a fully automated cycle when combined with Codex and GitHub Copilot as reviewers.

❓ KEY Q&A

Q: How do you get the first meeting through cold outreach using Loom videos?
A: The email identifies who you are, how you found them, names their specific problem, mentions you made a video showing the solution and estimated savings, and ends with one low-friction CTA. The Loom itself includes a 30-second app demo, proof from similar agencies, and a personalized savings estimate. Yesware tracks opens and clicks to gauge engagement.

Q: What infrastructure are you using for your EMS app?
A: Supabase as the core backend with HIPAA and SOC2 compliance add-ons. AWS strictly for accessing Anthropic models via Bedrock. Google Cloud for Gemini access and backend job processing. Supabase ephemeral branching enables sandboxed feature development.

Q: Is the security review hook running globally or per repository?
A: Fully customizable. Model selection, review settings, and all parameters are configurable per repo or globally via a Supabase database that the hooks read from.

Q: What model does Pixir connect to and how?
A: Currently OpenAI only, using the user's existing OpenAI subscription. This was chosen because it is the most universally held subscription, avoiding potential API restrictions that can occur with Claude.

Q: What are the unit economics of the AI photo booth?
A: Break-even estimated within a couple of events on hardware costs alone, though time investment must also be factored. Comparable simpler iPad-based booths charge around £600 per day.

🛠️ TOOLS AND CONCEPTS MENTIONED

Even Realities — AR smart glasses with Claude Code and Codex integrations, microphone, and companion ring controller for meeting transcription and hands-free coding.

Claude Code — Primary coding agent used across the community for building, reviewing, and iterating on projects.

Codex — OpenAI coding model used for workflow automation and as an adversarial PR reviewer against Claude-generated code.

Hermes — Self-hosted AI agent framework used as an automated management layer for homelab operations.

Pixir — Elixir-based agentic harness providing sub-agents-as-a-service with dramatically reduced memory overhead compared to native Codex sub-agents, using WebSockets and prefix caching.

NATS — Enterprise-grade message broker used as a personal service bus to route data between homelab services.

Infisical — Secret management platform handling API key rotation for homelab agents.

Supabase — Backend platform with ephemeral branching for sandboxed development, used for HIPAA-compliant healthcare apps and security review databases.

LiveKit — Real-time voice and video platform used to build hands-free coding agents accessible from mobile phones.

Loom — Video messaging platform central to high-converting cold outreach strategies.

Yesware — Email tracking tool monitoring opens, link clicks, and engagement on cold outreach campaigns.

Higgsfield and NanoBanana — AI image generation tools used for real estate photo enhancement pipelines.

n8n — Workflow automation platform used to build Google Workspace agents triggered via Telegram.

LanceDB — Vector database used for organizing retail audit data and community knowledge bases.

📎 SHARED RESOURCES

https://www.evenrealities.com/ — Even Realities smart glasses product page

https://www.yesware.com/ — Yesware email tracking tool

https://infisical.com/ — Infisical secret management platform

https://agentops.patchoutech.com/ — Patrick Chouinard's AgentOps documentation site

https://github.com/hopchouinard/community-brain-distribution — Community knowledge base repository

https://github.com/hopchouinard/RecapFlow-automation — Recap and transcript automation repository

https://pixir.dev/ — Bastian's Pixir agentic harness project site

https://github.com/scott-rippey/video-generator — AI video generation pipeline using Higgsfield, ElevenLabs, and HeyGen

https://github.com/scott-rippey/Telegram-Google-Voice-Agent — Telegram-to-Google-Workspace n8n agent

https://www.youtube.com/@BuildingwithReason — Patrick Chouinard's YouTube channel

https://youtube.com/@thekoerneroffice — Chris Koerner's YouTube channel on offline business models

🔄 FOLLOW-UPS WORTH EXPLORING

Brandon Hancock will connect Juan Torres with wedding venue owners to pilot the AI photo booth partnership model.

Scott Rippey will share his security review hook system plumbing with Patrick Chouinard for potential integration into Hermes.

Bastian Venegas Arevalo will open-source the Pixir agentic harness approximately one week following the call.

Juan Torres will build out voting, roast features, and photo album printing integration concepts for the photo booth, plus record demonstration videos.

Ty Wells will present his Limitless recovery and voice coding projects in upcoming sessions.

Patrick Chouinard will share AgentOps repositories and documentation with the broader group.

The community will monitor whether developers begin moving coding environments off laptops within six months as predicted at AI Engineer World's Fair, driven by always-on agent requirements.