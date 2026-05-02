📝 SUMMARY

Patrick Chouinard led this week's call covering member projects including a RAG pipeline for transcripts, a wearable data intelligence system, and a membership platform. Key topics included multi-model workflows, authentication strategies, and visual polish for non-technical demos.

💡 KEY INSIGHTS

Multi-model workflows reduce bias: use Claude for architecture, Codex for creation and adversarial review, and Gemini for research. Each catches the others' blind spots.

For RAG processing conversational transcripts, standard chunking fails because topics shift non-linearly. Heavy pre-processing including topic re-aggregation delivers 99.9% of the value.

Adding a three-sentence personality block to Claude.md or agent.md makes AI assistants push back on bad ideas with wit, improving feedback retention versus corporate responses.

When demoing to non-technical customers, visual polish matters more than backend scaffolding. Users fixate on aesthetics and miss architectural value if the interface looks unfinished.

For small closed systems with invited users, OTP or magic-link login beats passwords. Since you verified their email during invitation, magic links are simpler and more secure. Use Resend rather than Supabase's built-in email to avoid throttling.

Google Cloud Platform's developer-centric complexity works well with AI agents handling CLI commands, sidestepping UX problems.

Adversarial review using a different model finds bugs same-model review misses. Using Codex to break Claude-generated code, then feeding findings back to Claude, is an effective finishing step.

❓ KEY Q&A

Q: Claude Code has slowed down. How are others balancing it?
A: Run it offline during off-hours. For intensive work, Codex 5.5 is currently extremely fast and comparable to Opus quality. Mixing models improves quality since each has different biases.

Q: How do you add personality to your coding model?
A: Add a three-sentence block to Claude.md at the profile level. It applies globally and works in agent.md for Codex or other system prompts.

Q: Should old technical content be weighted differently in RAG?
A: Include timestamps for date-range filtering rather than discarding older content. The goal is answering trend questions, not just current encyclopedia usage.

Q: What embeddings and vector database are you using?
A: Nomic via Ollama for free embeddings and LanceDB for the vector database. Thorough pre-processing lowers embedding quality requirements. Add summary tokens using Gemma 4.30b.

Q: Best authentication for a small closed system?
A: Use OTP or magic-link rather than passwords. Since you're inviting users, their emails are already verified. Use Resend rather than Supabase's built-in email to avoid throttling.

Q: Do I need dev/staging/prod before showing to customers?
A: For non-technical customers, prioritize front-end visual polish over backend infrastructure. They fixate on aesthetics if it looks unfinished. Backfill infrastructure after securing customers.

Q: How does GCP compare to Azure?
A: Both are complex, but GCP's developer-centric design means Claude or Codex can navigate it effectively via CLI. At small scale, Google Cloud Workers handles scaling automatically via ADK.

🛠️ TOOLS AND CONCEPTS MENTIONED

Superpower — Development methodology plugin covering brainstorming through adversarial review and git hygiene. Creates an autonomous pipeline with Codex.

Claude Code — Primary coding agent for architecture, currently experiencing slowdowns.

Codex 5.5 — Fast coding model for creation and adversarial review of Claude-generated code.

N8N — Pipeline orchestration for transcript pre-processing.

Nomic — Free embedding model via Ollama.

LanceDB — Vector database with easy installation.

Google ADK Python 2.0 beta — Agent Development Kit for Vertex AI backends.

Resend — Email provider recommended over Supabase to avoid throttling.

OTP or Magic Link — Preferred authentication for small invited-user systems.

📎 SHARED RESOURCES

https://github.com/googleworkspace/cli — Google Workspace CLI
https://github.com/obra/superpowers — Superpower methodology plugin
https://www.lennysnewsletter.com/ — Software tool discounts
https://github.com/HKUDS/CLI-Anything — CLI tools
https://www.amazon.com/Explosive-Growth-Learned-Growing-Startup-ebook/dp/B0777FDL2H — Explosive Growth startup book
https://www.atapworldwide.org/ — ATAP Worldwide security association

🔄 FOLLOW-UPS WORTH EXPLORING

Patrick will evaluate Claude Design before Thursday's training and report back.

Patrick will meet with Cohere regarding multimodal embeddings for audio/video RAG.

Patrick will open-source the Community Brain preprocessing pipeline.

Juan will demo the AI photo booth frontend with QR code delivery next week.

Ty will publish the Propria personal intelligence system repository.

Andrew will investigate Terraform once his project stabilizes.

Tom will implement OTP using Resend and blur personal data in screen shares.