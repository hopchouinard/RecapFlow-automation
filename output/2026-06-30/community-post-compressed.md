📝 SUMMARY

This week's show-and-tell covered production AI implementations across software, operations, and hardware. Brandon Hancock shared his EMS startup's $100K pipeline and Even Realities glasses integration. Patrick Chouinard demoed AgentOps using Hermes and NATS for homelab automation. Scott Rippey presented adversarial security review hooks, Ty Wells showcased voice-driven coding and GPS recovery techniques, Juan Torres unveiled an AI photo booth venture, and Bastian Venegas Arevalo introduced Pixir, an Elixir-based agentic framework. The session focused on revenue generation, automated code review pipelines, and defensible hardware-software businesses.

💡 KEY INSIGHTS

Cold Outreach Loops: Send personalized Loom videos to prospects, then extract exact language from discovery calls to refine pitches. For finite markets like 18,000 EMS agencies, hyper-personalized outreach beats mass blasting and prevents irreversible market burn.

Reviewer Bottleneck: When AI accelerates code production 10x, human review becomes the constraint. Solve with sandboxed ephemeral environments like Supabase branches and parallel feature development.

Revenue Math: Calculate daily outreach targets needed to hit revenue goals within a defined timeframe, converting abstract targets into simple daily checklists that remove timeline anxiety.

Deflationary Margins: AI-powered businesses see margins improve automatically as model costs fall. You lock in capability at today's price while costs drop over 6 to 8 months.

Hardware-Software Moats: Physical hardware combined with software creates deeper competitive moats than pure software plays, particularly for vending or franchise models.

Adversarial Review: Never use the same model to write and review code. Using Codex to review Claude-generated code catches edge cases neither model would self-identify.

Data Assets: The most valuable accumulated resource is structured personal data including documentation, review history, and app context. Models are commodities; your data is proprietary.

Automated PR Cycles: Instruct Claude Code to push a PR and monitor it for 30 minutes resolving comments, creating a fully automated loop when combined with Codex and GitHub Copilot as reviewers.

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

Even Realities — AR smart glasses with Claude Code integration, microphone, and ring controller for transcription and hands-free coding.

Claude Code — Primary coding agent for building, reviewing, and iterating.

Codex — OpenAI model used for workflow automation and adversarial PR review against Claude-generated code.

Hermes — Self-hosted AI agent framework for homelab operations.

Pixir — Elixir-based agentic harness providing sub-agents-as-a-service with reduced memory overhead via WebSockets and prefix caching.

NATS — Enterprise message broker for homelab service routing.

Infisical — Secret management platform for API key rotation.

Supabase — Backend platform with ephemeral branching for sandboxed development and HIPAA compliance.

LiveKit — Real-time voice and video platform for hands-free mobile coding agents.

Loom — Video messaging platform for high-converting cold outreach.

Yesware — Email tracking tool monitoring opens and engagement.

Higgsfield and NanoBanana — AI image generation tools for real estate photo enhancement.

n8n — Workflow automation platform for Google Workspace agents triggered via Telegram.

LanceDB — Vector database for retail audit data and knowledge bases.

📎 SHARED RESOURCES

https://www.evenrealities.com/ — Even Realities smart glasses

https://www.yesware.com/ — Yesware email tracking tool

https://infisical.com/ — Infisical secret management platform

https://agentops.patchoutech.com/ — AgentOps documentation site

https://github.com/hopchouinard/community-brain-distribution — Community knowledge base repository

https://github.com/hopchouinard/RecapFlow-automation — Recap and transcript automation repository

https://pixir.dev/ — Pixir agentic harness project site

https://github.com/scott-rippey/video-generator — AI video generation pipeline using Higgsfield, ElevenLabs, and HeyGen

https://github.com/scott-rippey/Telegram-Google-Voice-Agent — Telegram-to-Google-Workspace agent

https://www.youtube.com/@BuildingwithReason — Patrick Chouinard's YouTube channel

https://youtube.com/@thekoerneroffice — Chris Koerner's YouTube channel on offline business models

🔄 FOLLOW-UPS WORTH EXPLORING

Brandon Hancock will connect Juan Torres with wedding venue owners to pilot the AI photo booth partnership model.

Scott Rippey will share his security review hook plumbing with Patrick Chouinard for potential Hermes integration.

Bastian Venegas Arevalo will open-source the Pixir agentic harness approximately one week following the call.

Juan Torres will build voting, roast features, and photo album printing for the booth, plus record demonstration videos.

Ty Wells will present his Limitless recovery and voice coding projects in upcoming sessions.

Patrick Chouinard will share AgentOps repositories and documentation with the broader group.

The community will monitor whether developers begin moving coding environments off laptops within six months as predicted at AI Engineer World's Fair.