📝 SUMMARY

This week's call centered on advanced AI-assisted development workflows, highlighted by Patrick's strategy of using Claude Fable exclusively for architecture and specification while delegating implementation to Opus. Members shared updates on cemetery management systems, predictive appliance monitoring, AI photo booths, and automated CRM data generation. Discussion covered autonomous AI network traversal, multi-model orchestration, token exhaustion workarounds, and government software sales strategies.

💡 KEY INSIGHTS

Reserve Claude Fable for architecture, specification generation, and code review—not implementation. When prompting Fable for specifications destined for Opus, explicitly state they are "for Opus" to trigger more granular detail.

Fable can autonomously discover and traverse network resources when given root access, including SSH-ing into VMs and synthesizing data across 160-plus repositories without explicit instructions.

Maximize output quality by chaining GPT-5.5 Pro via web chat for PRD generation, then Fable for architecture, Opus or Sonnet for implementation, and Fable again for PR review.

Fable can generate interactive training curricula that launch personalized, adaptive learning experiences in Claude Code, onboarding non-technical users through live model interaction.

Claude Code can control Android emulators visually via screenshots to generate demo data and test applications without touching production.

For predictive maintenance, reading electrical power signatures against manufacturer baselines and 7-day rolling averages predicts appliance failures before they occur, outperforming threshold-only systems.

When Fable tokens exhaust, GPT-5.5 Pro via web chat on the $100 Pro plan serves as an unlimited substitute for high-level prompting and specification work.

For government software sales like cemetery management, financial penalties and compliance deadlines motivate buyers more than features; hire local sales representatives to attend city council meetings rather than relying on remote pitches.

When structuring businesses as LLC versus S-Corp, use AI to research and prepare detailed questions before consulting human accountants to reduce billable hours.

❓ KEY Q&A

Marc asked if Patrick lets Claude and Codex compete for correct code. Patrick clarified that Fable handles architecture, Opus executes, and Fable reviews the PR—each model operates at its strength rather than competing.

Paul asked where cemetery operators share information that AI could research. Morgan explained that while research helps, the primary trigger for government buyers is financial penalties when they cannot fulfill burial requests, forcing budget prioritization.

Juan asked about attending city council meetings to pitch the cemetery app. Morgan recommended finding a local sales representative to attend on his behalf since the target city is in another state.

Patrick asked Juan what he uses for infrastructure monitoring. Juan currently uses CloudWatch for EC2. Patrick recommended Prometheus with Alert Manager for the physical photo booth hardware, noting that Alert Manager publishes alerts to webhooks, N8N, Discord, or other channels.

Juan asked if OpenRouter coordinates work between multiple models in a pipeline. Patrick explained that OpenRouter uses a fusion approach internally. For true pipeline orchestration with separate stages, use GitHub as the handoff mechanism between model sessions.

Ty asked what makes Fable different from standard models. He noted that Fable's harness keeps iterating through failures rather than stopping at early attempts, making it superior for cybersecurity, debugging, and complex architecture.

Paul asked if Patrick's AI-guided training could onboard non-technical people. Patrick confirmed that the live model adapts training in real time based on the learner's context, creating genuinely personalized experiences.

🛠️ TOOLS AND CONCEPTS MENTIONED

Claude Fable for high-level architecture and review only
Claude Opus and Sonnet for implementation and coding
GPT-5.5 Pro via web chat for unlimited PRD generation when API tokens exhaust
OpenAI Codex, Gemini CLI, Perplexity, Copilot, and Ollama as fallback tools
Claude Code as the primary coding harness
Hermes as a personal AI assistant system on Linux VMs
Prometheus and Alert Manager for infrastructure monitoring and alerting
CloudWatch for AWS EC2 monitoring
N8N for workflow automation and webhook processing
Aurora Serverless 2 for AWS database needs
LanceDB for deterministic AI data layers
Omnigent as a multi-model harness for switching between AI models
CMUX and Warp as terminal multiplexers and applications
Android Emulator controlled by Claude Code for visual automation
Wavespeed for desktop image transformation testing
Linga POS for point-of-sale integrations
Microsoft Copilot Studio for agent building with adaptive cards

📎 SHARED RESOURCES

https://github.com/scott-rippey/Telegram-Google-Voice-Agent
Scott Rippey's Google Voice agent running through Telegram via N8N

https://prometheus.io/
Monitoring platform for infrastructure

https://github.com/omnigent-ai/omnigent.git
Multi-model harness repository

https://fathom.video/customize
Fathom notetaker configuration

🔄 FOLLOW-UPS WORTH EXPLORING

Patrick will extract and share his 3-page Fable repository analysis prompt that enabled autonomous traversal of 160 repos.

Ryan will re-send his demo video to Paul for introduction to a New Zealand contact with 400 stores.

Morgan will deploy Class to Curb from staging to production and notify Paul for Australian school introductions.

Morgan will locate a local sales representative to attend city council meetings for the cemetery app.

Juan will implement Prometheus and Alert Manager for monitoring physical photo booth mini PCs.

Ty will task Fable with building an automated account-switching pipeline to manage token usage across multiple model accounts.

Ty will investigate and potentially fix Omnigent memory and crash issues.

Ryan will configure his new Mac Mini as a Hermes-style personal AI assistant with phone and appointment capabilities.