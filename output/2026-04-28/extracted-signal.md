## general

This coaching call was led by Patrick Chouinard and covered several member project updates alongside a community question about Claude Code performance. Patrick opened by presenting progress on his "Community Brain" project — a RAG pipeline built in N8N that ingests and pre-processes two and a half years of coaching call transcripts to enable architectural, insight-level queries rather than simple document retrieval. The preprocessing pipeline uses Claude Sonnet for the heavy lifting (topic re-aggregation and signal extraction), with lighter models handling later stages.

Ty Wells demonstrated Propria, his personal real-time intelligence system that aggregates signals from wearable devices (Limitless), fitness trackers (Whoop), Gmail, Git, shell, browser, Obsidian, and a custom-built wearable prototype with camera and microphone. He also showed a cybersecurity coaching curriculum with GPT Image 2-generated diagrams. Tom Welsh presented a membership management system for a military regimental association, built in Cursor with a Supabase/Vercel backend, featuring a double-authentication "welfare gate" for sensitive member data. Juan Torres discussed his AI photo booth project, which now includes Docker containerization and a QR code delivery feature for guests.

Andrew Nanton shared his experience migrating from Azure/Office 365 to Google Workspace and the Google Cloud/Vertex AI stack, using Google's ADK Python 2.0 beta. The group also discussed the Superpower development methodology plugin, multi-model workflows as a quality improvement strategy, and briefly touched on Lenny's Newsletter discounts and Shipkit vs. Superpower usage.

## insights

- **Multi-model workflows improve quality**: Using different models for different phases (Claude for architecture/ideation, Codex for creation and code review, Gemini for research/retrieval) reduces bias because each model catches the blind spots of the others. — Patrick Chouinard
- **Adding personality to AI assistants improves retention**: A short 3-sentence personality block in Claude.md makes the AI push back on bad ideas with wit, and users remember the feedback far better than flat, corporate-sounding responses. — Patrick Chouinard
- **RAG on conversational transcripts requires heavy pre-processing**: Standard chunking-by-size fails for conversation data because topics start, stop, and resume non-linearly. 99.9% of the value in Patrick's pipeline is in the pre-processing (topic re-aggregation, signal extraction), not the embedding itself.
- **Adversarial code review with a different model finds bugs that same-model review misses**: Using a Codex skill to attempt to break code produced by Claude, then feeding findings back to Claude in a loop, is an effective finishing step in a development pipeline. — Patrick Chouinard
- **Google Cloud Enterprise strips functionality vs. Pro**: Gemini Enterprise lacks document creation, NotebookLM Enterprise can't create video or slide decks — significantly less capable than the Pro tier. Anthropic is currently preferred for enterprise use. — Patrick Chouinard
- **Google Cloud's developer-centric design makes it easier for AI agents to navigate**: The complexity that makes GCP hard for humans to use directly is less of a problem when Claude or Codex handles CLI commands. — Andrew Nanton
- **For customer demos, visual polish matters more than backend scaffolding**: Non-technical customers will fixate on aesthetics and miss the value of the underlying architecture ("the fridge paradox"). — Patrick Chouinard
- **OTP/magic-link login is preferable to passwords for small closed systems**: Users forget passwords; since invited emails are already verified, a code sent to that email is both simpler and more secure. — Ty Wells
- **Use your own email provider (e.g., Resend) rather than Supabase's built-in email**: Supabase throttles outgoing emails, which can cause OTP codes to arrive too late to be useful. — Ty Wells
- **Superpower + Codex adversarial review is a complete development pipeline**: Brainstorm → spec → implementation plan → autonomous implementation → adversarial review → correction loop, all without constant human intervention. — Patrick Chouinard
- **Weighting older technical content by recency is important for knowledge bases**: Business/sales advice from 2 years ago may still be evergreen, but technical tool guidance (e.g., LangChain discussions) can be obsolete quickly. — Andrew Nanton

## qa

**Q (Juan Torres):** Claude Code has slowed down significantly over the last two months to the point where I'm relying more on Cursor. How are others balancing Claude Code with other tools?

**A (Patrick Chouinard):** I run Claude Code offline in the background during off-hours when it's most performant, then monitor it remotely. For intensive back-and-forth, Codex 5.5 is extremely fast right now and is comparable to Opus in quality for many tasks. Mixing models also improves overall quality since each model has different biases.

**Q (Juan Torres):** How do you add personality to your coding model?

**A (Patrick Chouinard):** Add a short 3-sentence personality block to your Claude.md at the profile level. It applies globally to all interactions. The same block can go in agent.md for Codex (in the .codex folder) and in the personalization/system prompt layer of other tools.

**Q (Andrew Nanton):** Should technical content from two years ago be weighted differently in the community brain RAG system, since so much has changed?

**A (Patrick Chouinard):** The goal isn't to use it as a current encyclopedia for "how do I do X today," but to answer questions like "how did AI coding change over the past two years?" — a trend and evolution view that can't be found anywhere else. Timestamps are included so date-range filtering is possible.

**Q (Andrew Nanton):** What are you using for embeddings and the vector database?

**A (Patrick Chouinard):** Nomic (free embedding model via Ollama) for embeddings — zero cost — and LanceDB for the vector database. Because the pre-processing is so thorough, the embedding quality requirements are lower. A small summary token is added on top of each chunk using Gemma 4.30b, which is very cheap.

**Q (Tom Welsh):** What's the best approach to authentication for a small closed system with only ~5 users?

**A (Ty Wells / Patrick Chouinard):** Use OTP/magic-link login rather than passwords — users forget passwords constantly, and since you're inviting them you already know their email is valid. Also use your own email provider like Resend rather than Supabase's built-in email, which has throttling limits that can delay OTP codes.

**Q (Adam):** Do I need to set up dev/staging/prod environments and optimize UI before showing this to customers?

**A (Patrick Chouinard / Tom Welsh):** It depends on the customer. For non-technical customers ("the fridge crowd"), visual polish matters — they'll fixate on how it looks and mentally check out if it looks unfinished. Get the front end looking good first; backfill the backend infrastructure after you have a paying customer.

**Q (Patrick Chouinard):** How do you find Google Cloud Platform admin compared to Azure?

**A (Andrew Nanton):** Both are terrible, but GCP's developer-centric design means Claude/Codex can navigate it very effectively via CLI, which largely sidesteps the UX problem. Azure CLI is also good for this. At small scale, Google Cloud Workers handles most scaling needs automatically via ADK.

**Q (Andrew Nanton):** Is there value in moving a RAG system to multimodal embeddings (audio/video)?

**A (Patrick Chouinard):** Not enough personal experience yet with multimodal embeddings, but Cohere is the top provider in that space. Patrick has a call with them scheduled and will report back.

## tools

- **Claude Code** — Primary coding agent; noted to have slowed down recently, used for architecture and planning phases
- **Codex (OpenAI, 5.5)** — Used for fast code creation, code review, and adversarial review of Claude-generated code
- **Cursor** — IDE used by Tom Welsh and Juan Torres as an alternative when Claude Code is slow
- **Gemini / Vertex AI** — Used for research/retrieval tasks and by Andrew Nanton for his ADK-based application backend
- **Kimi K2 (2.5/2.6)** — Used by Patrick for constructing output messages in the community brain pipeline; 2.5 chosen over 2.6 for single-prompt tasks
- **Gemma 4.30b** — Used for cheap summary token generation on top of embedding chunks
- **N8N** — Pipeline orchestration tool used by Patrick to build the transcript pre-processing workflow
- **Nomic** — Free embedding model run via Ollama; used for zero-cost vector embeddings
- **LanceDB** — Vector database used in Patrick's community brain project; easy to install via Claude Code
- **Ollama** — Local model runner used to host GPT4All/OSS models and Nomic embeddings
- **Open WebUI** — Interface for querying the local vector database and OSS models
- **OpenRouter** — API routing used by Patrick for Sonnet 4.6 calls during expensive pre-processing phases
- **Superpower** — Development methodology plugin (skills-based) for Claude Code, Codex, etc.; covers brainstorming through code review and git hygiene
- **Shipkit** — Project template tool; still used by Patrick and Don for starting new projects
- **Supabase** — Backend database and auth used by Tom Welsh and Ty Wells
- **Vercel** — Deployment platform for Tom Welsh's membership application
- **Resend** — Email delivery provider used by both Tom Welsh and Ty Wells for reliable OTP/transactional email
- **Limitless** — Wearable audio capture device used by Ty Wells; being replaced by a custom-built device (Meta acquired and is sunsetting it in September)
- **Fieldy** — Wearable audio capture device used by Patrick Chouinard
- **Whoop** — Fitness wearable whose data feeds into Ty Wells' Propria system
- **Telegram** — Delivery channel for Ty Wells' Propria personal intelligence system alerts
- **Obsidian** — Note-taking tool integrated as a signal source in Propria
- **GPT Image 2** — Used by Ty Wells to generate textbook-style diagrams for cybersecurity curriculum; described as significantly better than alternatives
- **Nano Banana** — Image generation tool compared unfavorably to GPT Image 2 by Ty Wells
- **Google ADK (Python 2.0 beta)** — Agent Development Kit used by Andrew Nanton for his application backend
- **Google Cloud Workers** — Used by Andrew Nanton to handle longer-running agentic processes
- **Terraform** — Infrastructure-as-code tool suggested by Juan Torres for managing cloud infrastructure
- **Proxmox** — Self-hosted virtualization platform used by Ty Wells; offered for processing power
- **Excalibur MCP** — MCP tool used by Patrick for diagram creation (had crisscrossing arrows issue)
- **Fathom** — Meeting recording and note-taking bot present in the call
- **Fireflies.ai** — Meeting recording and note-taking bot present in the call
- **Linear** — Project management tool mentioned by Andrew Nanton as a worthwhile Lenny's Newsletter discount
- **Whisperflow** — Tool obtained via Lenny's Newsletter discount, mentioned by Andrew Nanton
- **Granola** — Tool obtained via Lenny's Newsletter discount, mentioned by Andrew Nanton
- **Lenny's Newsletter** — Subscription newsletter offering software tool discounts
- **Clerk** — Auth provider mentioned in chat as an alternative for authentication
- **Docker** — Used by Juan Torres to containerize frontend and backend of his AI booth project separately
- **GitHub Copilot** — Patrick mentioned planning to test Superpower with it
- **Claude Design** — New Anthropic tool mentioned; Patrick scheduled to train on it Thursday
- **Gemini Enterprise / NotebookLM Enterprise** — Discussed critically; stripped-down vs. Pro tier

## links

- https://github.com/googleworkspace/cli — Google Workspace CLI, shared by Patrick Chouinard in chat
- https://github.com/HKUDS/CLI-Anything — Shared by Biggi Fraley in chat; no explicit context given
- https://www.amazon.com/Explosive-Growth-Learned-Growing-Startup-ebook/dp/B0777FDL2H — "Explosive Growth" startup book, shared by Biggi Fraley in chat
- https://app.fireflies.ai/live/01KQ61WA1GE2APXHABGBJ2NYDX?ref=live_chat — Fireflies.ai real-time notes for this session
- https://github.com/obra/superpowers — Superpower development methodology plugin repository, shared by Juan Torres
- https://www.lennysnewsletter.com/ — Lenny's Newsletter subscription page with software discounts, shared by Fitz
- https://www.atapworldwide.org/ — ATAP Worldwide (physical security industry association), shared by Andrew Nanton as a potential client networking resource for Ty Wells

## decisions

- **Patrick Chouinard** will complete the community brain preprocessing pipeline and open-source the full project on GitHub, including all prompts, preprocessed data, and the vector database, once it is deployable.
- **Patrick Chouinard** will evaluate Claude Design before Thursday, when he is scheduled to train on it, and report back to the group next week.
- **Patrick Chouinard** will have a call with Cohere about multimodal embeddings and report findings to the group in a couple of weeks.
- **Patrick Chouinard** shared his personality block prompt in the chat for members to add to their Claude.md / agent.md files.
- **Juan Torres** will use Claude Code for architecture/planning and switch to Gemini or Codex 5.5 for iterative editing to work around Claude Code slowdowns.
- **Juan Torres** will demo the AI photo booth frontend with QR code delivery feature at next week's call.
- **Tom Welsh** will implement OTP/magic-link login and use Resend (rather than Supabase's built-in email) for authentication in his membership system.
- **Tom Welsh** will blur personal data (phone numbers, email addresses) visible in his screen share before the session recording is published.
- **Ty Wells** will publish a public GitHub repository for Propria once it is ready.
- **Ty Wells** will connect with Adam offline to show him the security company module in his ERP system.
- **Adam** will focus on front-end visual polish before customer demos rather than backend infrastructure setup.
- **Andrew Nanton** will look into Terraform for infrastructure management once his project iteration stabilizes.