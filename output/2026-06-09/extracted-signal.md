## general

This coaching call brought together a group of builders and entrepreneurs to share project updates and discuss AI tooling. The session was facilitated by Paul Miller and covered three main project presentations: Ty Wells walked through his "ShipSafe" agent governance platform (also referencing a component called "Hermes"), Juan Torres updated the group on his AI Photo Booth deployment plans, and Ryan C demonstrated his digital signage SaaS product for retail screens. The call also touched on the newly released Anthropic "Fable" (Mythos) model and broader AI industry observations.

Ty Wells opened by explaining the architecture of ShipSafe, a middleware layer designed to sit between AI agents and the services they interact with, providing cost controls, security, authentication, and governance over non-reversible actions. The group gave feedback on the need for simpler, more tangible marketing examples to help non-technical users understand the value proposition. Bastian Venegas Arevalo framed it as a "harness enforced via MCP," which Ty confirmed was partially correct but incomplete.

Juan Torres described his AI Photo Booth project — an event-based service that produces AI-transformed images alongside standard photos — as nearly ready for field deployment. The group debated whether he should hire a technician immediately or do the first several events himself to iron out operational issues and build documented SOPs. Paul Miller and Ryan C both advised proving the concept personally first, then scaling via B2B partnerships with event venues and catering companies.

Ryan C demonstrated his digital signage platform, which runs on mini PCs attached to retail screens and is managed via a cloud dashboard. He showed features including remote OTA updates, heartbeat monitoring, diagnostic log capture, a node-based flow builder for screen content, and CRM integration for estate agents. The group discussed potential AI-generated content features and the challenge of reaching large retail chain decision-makers. The session closed with a brief discussion of Anthropic's Fable/Mythos model release, Apple's WWDC updates, and Huawei's 3D chip developments.

## insights

- **Ty Wells:** A complete agent governance layer must be a "full circle" — cost metering, security, authentication, and non-reversible action controls all need to be connected, or the system is effectively useless.
- **Ty Wells:** "Guarded surfaces" are self-defined by the client — they represent any action the user wants to require approval for (e.g., spending over a threshold, deleting a database). The number of guarded surfaces is the pricing unit.
- **Paul Miller / Ryan C:** When a product is highly capable and flexible, users struggle to know where to start. Seeding 3–5 concrete, relatable use cases (e.g., a homepage slider) is critical for conversion.
- **Ryan C:** The most important part of a homepage is the headline hook — if visitors don't immediately understand the value, they bounce. Boiling complex capability down to simple, memorable outcomes is "marketing gold."
- **Ryan C / Paul Miller:** For a new service business, do the first several deployments yourself before hiring anyone. This lets you iron out problems, build a strong SOP, and avoid costly hiring mistakes before the model is proven.
- **Paul Miller:** Don't attend early field events alone — bring someone who can step back and observe customer interactions while you handle the operational side. It's too hard to talk and listen simultaneously.
- **Paul Miller:** A more powerful go-to-market than selling direct to end customers is selling to intermediaries (e.g., event companies, venue operators) who already have the customer relationships and can resell or bundle your product.
- **Bastian Venegas Arevalo:** If you change the reasoning effort level mid-run in Claude Code, your cache is invalidated — stick with the same effort level throughout a session to save tokens.
- **Paul Miller:** The new Fable/Mythos model performs better on macro-level, holistic tasks (e.g., "rethink the whole app architecture") than on micro-level, specific bug fixes. Start with "high" reasoning effort rather than maximum to balance cost and quality.
- **Andrew Nanton:** When introducing AI to non-technical professionals, the most effective entry point is asking "what are the most tedious parts of your job?" — those are the best candidates for AI intervention.
- **Paul Miller:** Selling AI is often more effective when you don't call it AI — instead, talk about eliminating the specific painful, time-consuming tasks people already hate.
- **Ryan C:** Fable/Mythos consumes approximately 2× the tokens of Opus; the free/subsidized access window closes around June 22nd, after which it becomes token-only.

## qa

**Q (Paul Miller):** Could ShipSafe also function as a marketplace where people bring their agents into an existing stack and environment and run them through it?
**A (Ty Wells):** Yes — whatever agent you build, it runs through the protection layer when communicating. The layer is the gateway; the agent type doesn't matter.

**Q (Paul Miller):** What is the definition of a "guarded surface" in the pricing model?
**A (Ty Wells):** A guarded surface is something you self-define as needing protection — for example, any spend over $100, or any action like deleting a database. Each distinct thing you want to guard counts as one surface. They vary by business.

**Q (Juan Torres):** How do you quantify guarded surfaces for pricing given they can be different sizes?
**A (Ty Wells):** There's no size quantification — each surface is simply one discrete thing you define as needing protection. You need something else guarded, that's two. That's how the count works.

**Q (Paul Miller):** What's the nature of the people who would partner with Juan to handle field deployment of the AI Booth?
**A (Juan Torres):** The role is an "AI Booth Technician" — someone who physically installs the TV stand and hardware, monitors processes via a data web application (including deleting inappropriate images, triggering re-uploads if the inference engine stops), and retrieves the setup after the event.

**Q (Paul Miller):** Is the first challenge for the AI Booth getting people to use it at events, or is it scaling the network of nodes?
**A (Juan Torres):** The immediate plan is to offer it for free at initial events — install it, hand out business cards, and let the value speak for itself. The longer-term B2B model (selling to venue operators or event companies) is a future step once the concept is proven.

**Q (Andrew Nanton):** Is Ryan's node builder built from scratch or on top of something?
**A (Ryan C):** (Answered implicitly by demonstration) — it is custom-built; Ryan did not reference an underlying framework, and described it as his own flow builder with image, review, HTML embed, and custom slide nodes.

**Q (Juan Torres):** Have you thought about using HTML-generating nodes (e.g., from a Claude plugin) to let users design their own screens?
**A (Ryan C):** It's not a bad idea, but the priority is keeping it idiot-proof for non-technical clients. The approach would be to link it with Nanobanana for image generation with a fixed per-image cost, rather than open-ended token spend, and offer it as a bolt-on (e.g., five screen generations per month). Currently doing this manually with a Google subscription.

**Q (Paul Miller):** Has anyone been playing with the new Fable/Mythos model from Anthropic?
**A (Ty Wells):** Yes — turned it on a couple of hours ago, noticed the usage limits had been reset. It's available free until around June 22nd, after which it moves to API/token-only access for Fable 5.

## tools

- **ShipSafe (shipsafe.franklabs.io)** — Ty Wells' agent governance platform providing cost metering, security, auth, and non-reversible action controls for AI agents.
- **Hermes** — Ty Wells' agent component that connects through the ShipSafe gateway and metering proxy.
- **Claude / Anthropic Fable (Mythos)** — New Anthropic model discussed; available free until ~June 22nd, then token-only; 2× token cost of Opus; strong on macro-level reasoning tasks.
- **Claude Code** — Used by Bastian and others for development; cache invalidation behaviour with reasoning effort changes noted.
- **ChatGPT (extended thinking)** — Used by Adam to attempt student loan repayment optimization; struggled with the task.
- **Nanobanana** — AI image generation service Ryan C uses for producing retail screen content; mentioned as preferred for cost predictability over open-ended token spend.
- **Cursor** — Ryan C feeds captured console logs into Cursor for AI-assisted debugging of his digital signage mini PCs.
- **CloudWatch (AWS)** — Juan Torres uses it to monitor EC2 instance memory, CPU, and RAM for his AI Booth application.
- **EC2 (AWS)** — Juan Torres' AI Booth backend runs on a single EC2 instance in a staging environment with VPC subnets and encryption.
- **Google Gemini / Google subscription** — Ryan C uses it to generate initial screen content from client website imagery.
- **WordPress / Wix** — Mentioned as tools Ryan C's clients have used to build poor-quality websites, creating upsell opportunities.
- **Chrome Kiosk** — The display mode used on Ryan C's digital signage mini PCs.
- **MCP (Model Context Protocol)** — Bastian framed ShipSafe as a "harness enforced via MCP"; Ty confirmed it was part of the picture.
- **skills.sh** — Bastian suggested Ty map ShipSafe use cases to popular skills from this platform for marketing purposes.
- **intent-html-renderer (GitHub/skills-share)** — Bastian's Claude plugin for generating HTML presentations/reports; shared with Juan Torres.
- **Apple WWDC / M5 chip / AirPods** — Discussed in the context of Apple's AI updates and hardware roadmap; underwhelming reception from the group.
- **Huawei 3D chip** — Discussed as a significant Chinese semiconductor innovation circumventing US sanctions.

## links

- **https://shipsafe.franklabs.io/platform** — Ty Wells' ShipSafe platform demo/landing page, shared in chat.
- **https://github.com/ranvier2d2/skills-share/tree/main/skills/intent-html-renderer** — Bastian's intent-html-renderer skill for generating HTML presentations via Claude; shared with Juan Torres.

## decisions

- **Ty Wells** will work on simplifying the ShipSafe presentation — applying the "explain it to a 10-year-old" rule and adding concrete, relatable use-case examples (e.g., homepage slider with 5 headline benefits).
- **Juan Torres** will do the first several AI Booth deployments himself (rather than hiring immediately) to prove the concept, document the SOP, and iron out operational issues before bringing on a technician.
- **Juan Torres** will bring a friend or companion to the first events so someone can observe customer interactions while he handles operations.
- **Juan Torres** will contact venues he knows in San Diego within approximately two weeks to arrange the first free AI Booth installations.
- **Juan Torres** will review the intent-html-renderer GitHub plugin shared by Bastian.
- **Ryan C** will use the Fable/Mythos model aggressively before the June 22nd cutover, including attempting to build his taxi app and running security reviews on existing code.
- **Ryan C** will email Paul Miller details about his digital signage platform for potential Australian retail contacts Paul has.
- **Paul Miller** will connect Ryan C with relevant contacts in Australia (liquor/retail channels) after an offline discussion; Paul is traveling to Sydney the following week.
- **Paul Miller** will share his email in the chat for Ryan C to send over the digital signage information.