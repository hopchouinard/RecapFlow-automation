📝 SUMMARY

This coaching call featured major startup wins and advanced technical deep dives. Brandon Hancock announced funding for his EMS billing startup via Tiny Seed, validating that niche B2B AI solutions command premium pricing. The community showcased sophisticated agentic workflows including Dmitry's multi-agent orchestration system, HP's real-time call coaching extension, and Bastian's Elixir-based CLI agent. Discussions covered parallel development strategies using Git worktrees, deepfake security concerns, model selection economics (highlighting Gemini 3 Flash and GLM 4.7), and the shift from agent frameworks like LangChain to direct LLM orchestration.

💡 KEY INSIGHTS

Brandon argued that solving specific enterprise problems "pays stupid well" after securing funding for EMS Soap, which helps fire departments and ambulance companies generate SOAP reports for insurance billing. He noted the same RAG template used in ShipKit underpins his funded startup, demonstrating how core AI infrastructure templates can create vastly different business values when applied to specific verticals.

Dmitry demonstrated autonomous agent orchestration running multiple specialized agents (George for Scrum Master duties, Sarah for coding, Raj for incident management) that can work in parallel. He emphasized that expensive models like Claude 4.5 should handle complex research and spec creation, while cheaper models handle implementation to optimize costs.

Brandon shared his Git worktree workflow for maintaining clean development practices with AI coding. By creating isolated worktrees for each feature branch, he effectively becomes a "team of 10" working in parallel without merge conflicts, though database schema changes still require serial processing.

Tom Welsh and Bastian highlighted escalating deepfake security risks, citing a $25 million bank fraud using AI-generated Zoom calls and a vault heist using WhatsApp video deepfakes of government officials. Tom emphasized that seeing familiar faces on video makes social engineering attacks significantly more believable.

On pricing strategy, Brandon advised that as coding speeds increase (tasks dropping from one week to four hours), developers should pivot from hourly billing to value-based pricing or increased throughput. He suggested framing higher rates as "two of my hours equals eight of someone else's" due to AI acceleration.

For production applications, Brandon recommended Gemini 3 Flash Preview on low thinking settings for best instruction-following performance at lower cost than GPT-4.1, noting it handles 25,000+ token contexts in roughly 15 seconds. Bastian highlighted GLM 4.7 via OpenRouter as a "crazy cheap" alternative for non-sensitive tasks, costing only a few dollars for days of coding.

❓ KEY Q&A

Marc asked about Git worktrees and why he should use them. Brandon explained that traditional AI coding often results in "monster PRs" mixing unrelated features on main. Worktrees create separate directory clones for each branch, allowing parallel feature development with traceable commits and preventing cloud coding agents from competing to edit the same files.

Marc asked about extracting YouTube transcripts without hitting API throttles. The group suggested multiple approaches: using Whisper locally on downloaded MP3s, Appify for scraping, YouTube-DLP libraries, or routing through residential proxy services like Dakota to bypass IP blocks that target cloud providers.

Hemal asked about automating dimension overlays on product images. Brandon recommended a multi-step workflow using Gemini 3 Pro Image (Nano Banana) for generation, followed by a separate critique prompt for validation, creating a pass/fail/warning system so users only manually review problematic outputs rather than thousands of images.

Dmitry asked Brandon about ShipKit's future given his startup commitments. Brandon confirmed he will continue updating ShipKit with real-world learnings (like the Git worktree workflow) but will shift from weekly to intermittent calls, with one major remaining deliverable being the Worker SaaS walkthrough showing how to turn templates into production apps.

🛠️ TOOLS AND CONCEPTS MENTIONED

EMS Soap - Brandon's funded startup for EMS billing and SOAP report generation using AI

ShipKit - Brandon's template library for AI development; the RAG template foundation is used in his funded startup

Git worktrees - Git feature allowing multiple working directories for parallel branch development without switching contexts

Graphite - Merge management tool (recently acquired by Cursor) for handling parallel agent contributions and merge ordering

Deepgram - Speech-to-text service used by HP for real-time call transcription; offers medical-specific models and $200 starter credit

Fieldy - 24-hour continuous recording pendant (similar to discontinued Limitless) feeding into N8N automation workflows

EXA - AI search API used by Bastian for web research capabilities

Gemini 3 Flash Preview / Nano Banana - Google's models recommended for instruction-following and image generation tasks; Flash Preview specifically noted for low-thinking mode performance

GLM 4.7 - Chinese open-source model available via OpenRouter at significantly lower cost than western alternatives

PlantUML - Diagram generation language used by Tiran to visualize JSON workflows as flowcharts

Daytona - Sandboxing service for running agent code in isolated containers with persistent storage

Trigger.dev - Workflow orchestration platform mentioned as alternative to Tiran's custom-built solution

Tiny Seed - Funding source for Brandon's startup; requires $500 MRR and demonstrated traction over multiple months

📎 SHARED RESOURCES

Dmitry's LinkedIn post detailing his agentic orchestrator and autonomous development system

Tiran's GitHub repository containing three microservices for workflow orchestration with webhooks and job management

Deepgram API offering $200 in free credits for speech-to-text integration

Tiny Seed funding application for bootstrapped SaaS founders (new batch opens February)

Render and Railway - Alternative hosting platforms recommended for stateful services and WebSocket connections beyond Vercel/Netlify limitations

Dakota - Residential proxy and scraping service mentioned for bypassing IP-based API restrictions

🔄 FOLLOW-UPS WORTH EXPLORING

Brandon committed to recording a ShipKit module on Git worktrees this Saturday, demonstrating the cloud code command workflow for parallel feature development.

Patrick exploring public content creation around AI-driven software development lifecycle (SDLC) practices, with Brandon encouraging him to document his infrastructure-as-code approach using Claude Code skills for network management.

Dmitry's orchestrator moving from local execution to cloud deployment with remote sub-agents, potentially integrating with Graphite for merge management when scaling to hundreds of parallel agents.

Integration opportunities between Patrick's Fieldy continuous recording hardware and Dmitry's agent system for autonomous task generation from daily conversations.

Hemal's image processing workflow testing with Gemini 3 Pro and validation pipelines for automated dimension overlay on product catalogs.

Potential partnership between Dmitry's agentic Scrum Master and Tiran's contact in the Agile consulting space for federal government implementations.