📝 SUMMARY

This week's roundtable featured Patrick Chouinard demonstrating his Community Brain RAG system that indexes 68 sessions of call transcripts, Juan Torres showcasing an AI photo-booth app for events, and Morgan Cook presenting a Raspberry Pi digital signage kiosk built over a weekend. The group also debated the shifting landscape between Claude Code and Codex, with several members planning migrations due to quality concerns and billing quirks.


💡 KEY INSIGHTS

Data preparation beats model selection in RAG pipelines. Patrick found that cleaning and chunking transcripts cost only $0.75 of a $30 total spend, while embedding model choice (Nomic vs Gemini) showed minimal difference when underlying data was solid.

Hybrid retrieval is essential for conversational data. Combining BM25 keyword search with vector search significantly outperformed either method alone when querying call transcripts.

Small local models can reach 75-80% of frontier quality. With strong retrieval infrastructure, GPT-4o-mini and open-source alternatives approached Opus-level results at a fraction of the cost, though Gemma 4 struggled with complex retrieval logic despite its 30B parameters.

Enterprise Claude Code requires configuration hardening. Deploy organizational settings.json files to supersede personal configs, and use seeded CLAUDE.md files to explain constraints rather than just blocking users.

Watch for billing mode triggers. Mentioning competitor agent names like OpenClaw or Hermes in Claude Code sessions switches from subscription to API token billing.

The Superpower framework now bridges Claude Code, GitHub Copilot, and Codex. This allows workflow portability as members evaluate switching between coding agents.

Model default preferences are the new SEO. If a technology isn't in a model's training-weighted defaults, it effectively doesn't exist for AI-assisted development.


❓ KEY Q&A

Q: What replaced ShipKit for the group?
A: Most have moved to Claude Superpowers, which now works across Claude Code, GitHub Copilot, and Codex.

Q: Where did Patrick source the data for his Community Brain RAG?
A: Fathom meeting recordings and transcripts, not a manual notetaker.

Q: How do you harden Claude Code for enterprise deployment?
A: Deploy a settings.json at the organizational level to supersede personal settings, and include a seeded CLAUDE.md that constrains users while explaining the reasoning.

Q: How does Gemma 4 perform for RAG tasks?
A: Excellent for chunk-level summarization and function calling, but it cannot follow complex retrieval logic even at 30B parameters.

Q: Is Morgan's Raspberry Pi kiosk a touchscreen?
A: No, it is display-only mounted 10-15 feet up. Interaction happens via QR codes linking to external URLs.

Q: Are there any AI development books recommended by the community?
A: After querying the Community Brain database, no AI development books were found in past calls. The only books mentioned were business and productivity titles like 12 Months to $1 Million and Building a Second Brain.

Q: Is the Codex plugin for Claude Code stable?
A: Patrick runs it in auto-review mode where Codex corrects every Claude iteration until clean, revealing that Claude has been generating code requiring frequent correction.


🛠️ TOOLS AND CONCEPTS MENTIONED

Community Brain RAG Stack: Patrick's system using OpenWebUI, Ollama, LanceDB, and hybrid retrieval (BM25 + vector) to query 130+ hours of call transcripts.

Claude Code vs Codex: The group is actively comparing these coding agents, with several planning to switch to Codex's $100/month tier due to perceived quality degradation in Claude Code.

Claude Superpowers: A framework that provides consistent workflows across Claude Code, GitHub Copilot, and Codex.

Lightpanda: A Playwright alternative written in Zig that uses roughly 1/10th the memory by skipping graphical rendering, suggested for Raspberry Pi automations.

Raspberry Pi Kiosk: Morgan's digital signage system running Chrome in frameless kiosk mode, using QR codes as the interaction layer to keep hardware simple.

Fathom: The meeting transcription service providing the source data for the Community Brain RAG.


📎 SHARED RESOURCES

https://www.atapworldwide.org/ — ATAP networking resource for talent acquisition professionals

https://fathom.video/users/sign_in — Meeting transcription service used for the Community Brain data

https://lightpanda.io/ — Lightweight browser automation tool

https://github.com/lightpanda-io/browser — GitHub repo for Lightpanda

https://amplifying.ai/research/claude-code-picks/report — Research on Claude Code's default technology preferences

https://crowdpics.ai — Ty Wells' event photo app similar to Juan's project


🔄 FOLLOW-UPS WORTH EXPLORING

Patrick will package the Community Brain system (LanceDB database + prepared data + deployment instructions) for community download by next week.

Several members including Patrick and Paul are switching from Claude Max to Codex $100/month plans and will report back on comparative performance.

Morgan will share Raspberry Pi kiosk scripts and ISO duplication processes with Juan and Paul for event display use cases.

Patrick will gather real-world usability data on Superpowers at scale from his enterprise pilot with 100 users.

Patrick will implement pre-processing to scrub competitor agent names from transcripts before Claude Code processing to avoid triggering API billing mode.