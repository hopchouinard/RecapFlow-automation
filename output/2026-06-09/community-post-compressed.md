📝 SUMMARY

This week's coaching call covered project updates from Ty Wells (ShipSafe agent governance), Juan Torres (AI Photo Booth), and Ryan C (digital signage SaaS). The session delivered feedback on go-to-market strategies, technical architecture, and early-stage operations, plus discussion of Anthropic's new Fable model.

💡 KEY INSIGHTS

🔹 Agent governance requires a "full circle" approach combining cost metering, security, authentication, and controls over non-reversible actions. Missing any element renders the system ineffective.

🔹 "Guarded surfaces" are client-defined protection thresholds (e.g., spending limits, database deletion). Each discrete protection counts as one pricing unit regardless of size or complexity.

🔹 Highly capable products need 3–5 concrete, relatable use cases upfront to help non-technical users see immediate value.

🔹 Homepage headlines must instantly communicate simple, memorable outcomes. Boiling complex capability into specific benefits prevents visitor bounce.

🔹 Personally execute the first several service deployments to iron out operations, build SOPs, and validate the model before hiring technicians.

🔹 Bring an observer to early field events to capture customer feedback while you handle operations.

🔹 Selling to intermediaries with existing relationships (event companies, venues) often outperforms direct sales for new hardware services.

🔹 Changing Claude Code's reasoning effort level mid-run invalidates cache. Stick with one level per session.

🔹 Anthropic's Fable (Mythos) excels at macro architectural thinking over micro bug fixes, uses ~2× Opus tokens, and moves to paid-only around June 22nd.

🔹 When introducing AI to non-technical professionals, sell the elimination of tedious tasks rather than "AI" as a concept.

❓ KEY Q&A

Q: Could ShipSafe function as a marketplace for existing agents?
A: Yes. ShipSafe acts as a gateway protection layer that works with any agent type through middleware when communicating with external services.

Q: What defines a "guarded surface" in ShipSafe pricing?
A: Client-defined actions requiring protection (e.g., spends over $100, database deletion). Each distinct protection counts as one surface regardless of complexity.

Q: What is the AI Booth Technician's role?
A: Physical installation, monitoring via web app, content moderation, troubleshooting inference engine issues, and equipment retrieval.

Q: Should Juan hire immediately or deploy personally first?
A: Deploy personally for the first several events to prove the concept, document SOPs, and iron out problems before hiring.

Q: Is Ryan's node builder custom or framework-based?
A: Custom-built, featuring nodes for images, reviews, HTML embeds, and custom slides.

Q: Has anyone tested Anthropic's Fable/Mythos model?
A: Yes, available with usage limits reset, free until approximately June 22nd, then API/token-only for Fable 5.

🛠️ TOOLS AND CONCEPTS MENTIONED

ShipSafe and Hermes — Middleware providing cost metering, security, authentication, and governance for AI agents. Hermes connects agents through the ShipSafe gateway.

Anthropic Fable (Mythos) — Reasoning model excelling at macro-level architectural tasks rather than specific bug fixes. Uses approximately twice the tokens of Opus.

Claude Code — Development tool where changing reasoning effort level mid-run invalidates cache.

Nanobanana — AI image generation with fixed per-image pricing.

Cursor — AI coding assistant used for debugging remote hardware via console logs.

AWS CloudWatch and EC2 — Infrastructure monitoring and hosting for AI Photo Booth backend.

Chrome Kiosk — Display mode for retail digital signage mini PCs.

MCP (Model Context Protocol) — Framework referenced in ShipSafe architecture.

intent-html-renderer — Claude plugin for generating HTML presentations via GitHub.

skills.sh — Platform suggested for mapping ShipSafe use cases to popular skills.

📎 SHARED RESOURCES

https://shipsafe.franklabs.io/platform — ShipSafe platform demo and landing page.

https://github.com/ranvier2d2/skills-share/tree/main/skills/intent-html-renderer — Bastian's Claude plugin for generating HTML presentations and reports.

🔄 FOLLOW-UPS WORTH EXPLORING

Ty Wells will simplify ShipSafe messaging using the "explain it to a 10-year-old" rule and add concrete use-case examples with specific headline benefits.

Juan Torres will personally execute the first several AI Booth deployments, bring a friend to observe customer interactions, and contact San Diego venues within two weeks to arrange free installations.

Ryan C will use the Fable/Mythos model aggressively before the June 22nd cutoff for his taxi app and security reviews, and will email Paul Miller details about his digital signage platform for potential Australian retail introductions.

Paul Miller will share his email for Ryan to send platform details and will facilitate connections with Australian liquor and retail channels following his upcoming Sydney trip.