📝 SUMMARY

This week's coaching call brought together builders and entrepreneurs to share project updates and strategic challenges. Paul Miller facilitated presentations covering Ty Wells' agent governance platform ShipSafe, Juan Torres' AI Photo Booth nearing field deployment, and Ryan C's digital signage SaaS for retail screens. The session delivered practical feedback on go-to-market strategies, technical architecture decisions, and early-stage operational tactics, alongside discussion of Anthropic's new Fable model and broader industry developments.

💡 KEY INSIGHTS

🔹 Agent governance requires a "full circle" approach combining cost metering, security, authentication, and controls over non-reversible actions to be effective. A system missing any of these elements is effectively useless.

🔹 "Guarded surfaces" are self-defined by the client as any action requiring protection thresholds, such as spending limits or database deletion. Each discrete protection need counts as one pricing unit regardless of complexity or size.

🔹 Highly capable products need 3–5 concrete, relatable use cases seeded upfront to help non-technical users understand where to start and see immediate value.

🔹 Your homepage headline must immediately communicate simple, memorable outcomes. Boiling complex capability down to specific benefits is marketing gold; if visitors don't instantly understand the value, they bounce.

🔹 For new service businesses, personally execute the first several deployments to iron out operational problems, build documented SOPs, and validate the model before hiring technicians.

🔹 Bring an observer to early field events to watch customer interactions while you handle operations. It is too difficult to simultaneously troubleshoot and listen to user feedback.

🔹 Selling to intermediaries who already have customer relationships, such as event companies or venue operators, often outperforms direct-to-consumer sales for new hardware services.

🔹 Changing Claude Code's reasoning effort level mid-run invalidates your cache and wastes tokens. Stick with the same effort level throughout a session.

🔹 Anthropic's Fable (Mythos) model excels at macro-level architectural thinking rather than micro bug fixes, consumes approximately 2× the tokens of Opus, and will move from free access to token-only around June 22nd.

🔹 When introducing AI to non-technical professionals, ask about their most tedious tasks rather than leading with technology. Sell the elimination of painful, time-consuming work rather than selling "AI" as a concept.

❓ KEY Q&A

Q: Could ShipSafe function as a marketplace where people bring their existing agents to run through the platform?
A: Yes. ShipSafe acts as a gateway protection layer that works with whatever agent you build. The agent type does not matter; it runs through the middleware when communicating with external services.

Q: What defines a "guarded surface" in the ShipSafe pricing model?
A: Guarded surfaces are self-defined by the client as any action requiring protection, such as any spend over $100 or deleting a database. Each distinct thing you want to guard counts as one surface.

Q: How do you quantify guarded surfaces given they can be different sizes?
A: There is no size quantification. Each surface is simply one discrete protection you define. If you need something else guarded, that counts as a second surface regardless of complexity.

Q: What is the role of the AI Booth Technician Juan is considering hiring?
A: The technician physically installs the TV stand and hardware, monitors processes via a data web application, deletes inappropriate generated images, triggers re-uploads if the inference engine stops, and retrieves the setup after the event.

Q: Should Juan hire immediately or deploy the AI Booth himself first?
A: Do the first several deployments personally to prove the concept, document strong SOPs, and iron out problems before hiring. This avoids costly hiring mistakes before the model is proven.

Q: Is Ryan's node builder for digital signage custom or built on an existing framework?
A: It is custom-built, featuring nodes for images, reviews, HTML embeds, and custom slides.

Q: Has anyone tested the new Fable/Mythos model from Anthropic?
A: Yes, it is currently available with usage limits reset, free until approximately June 22nd, after which it becomes API and token-only access for Fable 5.

🛠️ TOOLS AND CONCEPTS MENTIONED

ShipSafe and Hermes — Middleware layer providing cost metering, security, authentication, and governance controls for AI agents. Hermes is the agent component connecting through the ShipSafe gateway.

Anthropic Fable (Mythos) — New reasoning model excelling at macro-level tasks like architectural rethinking rather than specific bug fixes. Uses approximately twice the tokens of Opus.

Claude Code — Development tool with noted behavior that changing reasoning effort level mid-run invalidates cache.

Nanobanana — AI image generation service used for cost-predictable content creation with fixed per-image pricing.

Cursor — AI coding assistant used for debugging remote signage hardware via captured console logs.

AWS CloudWatch and EC2 — Infrastructure monitoring and hosting for the AI Photo Booth backend, tracking memory, CPU, and RAM.

Chrome Kiosk — Display mode used on retail digital signage mini PCs.

MCP (Model Context Protocol) — Framework referenced as part of the ShipSafe architecture approach.

intent-html-renderer — Claude plugin for generating HTML presentations and reports via GitHub.

skills.sh — Platform suggested for mapping ShipSafe use cases to popular skills for marketing purposes.

📎 SHARED RESOURCES

https://shipsafe.franklabs.io/platform — ShipSafe platform demo and landing page.

https://github.com/ranvier2d2/skills-share/tree/main/skills/intent-html-renderer — Bastian's Claude plugin for generating HTML presentations and reports.

🔄 FOLLOW-UPS WORTH EXPLORING

Ty Wells will simplify ShipSafe messaging using the "explain it to a 10-year-old" rule and add concrete, relatable use-case examples such as homepage sliders with specific headline benefits.

Juan Torres will personally execute the first several AI Booth deployments rather than hiring immediately, bring a friend to observe customer interactions during early events, and contact San Diego venues within approximately two weeks to arrange free installations.

Ryan C will use the Fable/Mythos model aggressively before the June 22nd cutoff, including attempting to build his taxi app and running security reviews, and will email Paul Miller details about his digital signage platform for potential Australian retail introductions.

Paul Miller will share his email in the chat for Ryan to send platform details and will facilitate connections with Australian liquor and retail channels following his upcoming Sydney trip.