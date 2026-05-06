📝 SUMMARY

This week's roundtable featured Patrick Chouinard's Community Brain RAG indexing 68 call sessions, Juan Torres's AI photo-booth app, and Morgan Cook's Raspberry Pi kiosk. The group debated Claude Code versus Codex, with several planning migrations due to quality concerns and billing quirks.


💡 KEY INSIGHTS

Data preparation beats model selection in RAG. Patrick spent only $0.75 of $30 on cleaning/chunking versus embedding models, with minimal difference when underlying data was solid.

Hybrid retrieval (BM25 + vector) significantly outperformed single methods for conversational transcript queries.

Small local models reach 75-80% of frontier quality with strong retrieval infrastructure, though Gemma 4 struggled with complex logic despite 30B parameters.

Enterprise Claude Code requires organizational settings.json to supersede personal configs, and seeded CLAUDE.md files explaining constraints.

Mentioning competitor agent names (OpenClaw, Hermes) switches billing from subscription to API tokens.

Superpower framework now bridges Claude Code, GitHub Copilot, and Codex for workflow portability.

Model default preferences are the new SEO. If technology isn't in training-weighted defaults, it effectively doesn't exist for AI-assisted development.


❓ KEY Q&A

Q: What replaced ShipKit?
A: Claude Superpowers, now cross-compatible with Claude Code, GitHub Copilot, and Codex.

Q: Where did Patrick source Community Brain data?
A: Fathom meeting recordings and transcripts.

Q: How do you harden Claude Code for enterprise?
A: Deploy organizational settings.json and seeded CLAUDE.md explaining constraints.

Q: How does Gemma 4 perform for RAG?
A: Excellent for summarization and function calling, but fails at complex retrieval logic.

Q: Is Morgan's Raspberry Pi kiosk a touchscreen?
A: No, display-only with QR code interaction layer.

Q: Are there AI development books recommended?
A: None found in Community Brain. Only business titles like 12 Months to $1 Million and Building a Second Brain were mentioned previously.

Q: Is the Codex plugin for Claude Code stable?
A: Patrick runs auto-review mode where Codex corrects Claude iterations, revealing frequent Claude errors.


🛠️ TOOLS AND CONCEPTS MENTIONED

Community Brain RAG Stack: OpenWebUI, Ollama, LanceDB, and hybrid retrieval querying 130+ hours of transcripts.

Claude Code vs Codex: Several planning to switch to Codex $100/month tier due to Claude Code quality degradation.

Claude Superpowers: Consistent workflows across Claude Code, GitHub Copilot, and Codex.

Lightpanda: Playwright alternative in Zig using ~1/10th memory by skipping graphical rendering, ideal for Raspberry Pi.

Raspberry Pi Kiosk: Chrome in frameless kiosk mode with QR code interaction layer.

Fathom: Meeting transcription service.


📎 SHARED RESOURCES

https://www.atapworldwide.org/ — ATAP networking resource for talent acquisition professionals
https://fathom.video/users/sign_in — Meeting transcription service used for the Community Brain data
https://lightpanda.io/ — Lightweight browser automation tool
https://github.com/lightpanda-io/browser — GitHub repo for Lightpanda
https://amplifying.ai/research/claude-code-picks/report — Research on Claude Code's default technology preferences
https://crowdpics.ai — Ty Wells' event photo app similar to Juan's project


🔄 FOLLOW-UPS WORTH EXPLORING

Patrick will package Community Brain system for download by next week.

Several members including Patrick and Paul are switching from Claude Max to Codex $100/month and will report comparative performance.

Morgan will share Raspberry Pi kiosk scripts and ISO duplication processes with Juan and Paul.

Patrick will gather Superpowers usability data from 100-user enterprise pilot.

Patrick will scrub competitor agent names from transcripts to avoid API billing triggers.