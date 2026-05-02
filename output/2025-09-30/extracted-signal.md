## general

This was a weekly coaching call for members of the ShipKit community, hosted by Brandon Hancock. The session opened with a brief discussion about scheduling — participants noted that the current call time (6 p.m. Eastern / 11 p.m. UK) is difficult for European and Asia-Pacific members, and Brandon committed to running a poll to find better times. Brandon shared that ShipKit had recently launched, that he had been iterating on it live with members, and that he was significantly less stressed after a brutal build sprint.

The bulk of the session was a round-robin where each participant shared project updates and asked questions. Topics ranged from agent architecture design (LangGraph vs. Google ADK, context window limits, when to split agents), freelance client management (discovery documents, milestone billing, testing periods), wireframing tools, mass email outreach, and cloud infrastructure decisions (Railway vs. GCP, EC2 partitioning for GPU/CPU workloads). Brandon also previewed upcoming ShipKit content: a beginner Next.js/TypeScript tutorial and a base template for Next.js apps with background jobs.

A recurring theme was the urgency of the current AI opportunity window — Brandon emphasized that the gap between those who can build AI-powered products and those who cannot is closing, and encouraged members to ship projects and share their work publicly (especially on LinkedIn). The call also featured a humorous story from Jake about a chaotic client project with deeply flawed vibe-coded software, including a "forgot password" feature that exposed other users' accounts.

Near the end, the group went deep on Google ADK vs. LangGraph for production agent deployment. Brandon gave a candid assessment: ADK is excellent for local development but currently has broken streaming on Vertex AI and a painful dual-endpoint problem in production. He recommended using Google's Generative AI library for now and watching ADK closely, predicting Google will fix the deployment issues and ultimately dominate the AI infrastructure stack.

## insights

- **Agent architecture rule of thumb (Brandon):** Keep agents to five tasks or fewer — if an agent needs more than one "virtual hand," split it into sub-agents. Root agent + sequential agents covers ~80% of use cases.
- **Context windows are the root problem in multi-agent systems:** Giving each agent a single purpose and single function is analogous to keeping software files under a few hundred lines — it's just good engineering.
- **Wireframes are living documents:** A wireframe is a hypothesis. Expect it to change as soon as you start building. The value is getting ideas out of your head and into a screenshottable format you can pass to Cursor.
- **Excalidraw keyboard shortcuts accelerate diagramming:** Knowing keys 1–6 to switch between shapes/arrows/text means you can diagram faster than pen and paper, and the output is immediately AI-ingestible.
- **Paid discovery documents prevent tire-kickers (Brandon):** Charging for an initial "AI discovery" or "strategy" document — even a small amount — aligns incentives and filters out clients who aren't serious. If the client proceeds, the fee can be credited toward the project.
- **Rename "requirements document" to "strategy" or "project initiation document" (Prem/Tom):** The old terminology carries baggage; reframing it as a strategy document makes it easier to sell as a standalone service.
- **Always get some money upfront (Brandon):** Even a $1,000 project kickoff fee ensures the client is mentally committed and aligns incentives before any work begins.
- **Include a two-week testing period at project close (Brandon):** Explicitly scoping a post-delivery testing window prevents clients from surfacing "bugs" months later and expecting free fixes.
- **The way a project begins is how it will go (Jake):** If there's friction or red flags at the start of a client engagement, expect that pattern to continue throughout.
- **Asana MCP dramatically compressed weekly reporting (Mitch):** Hooking Claude to the Asana MCP with a template reduced a ~2-hour weekly update task to ~15 minutes.
- **Google ADK is excellent locally, broken in production (Brandon):** Vertex AI Agent Engine currently lacks streaming support and has a dual-endpoint problem (local vs. cloud paths differ), making it unsuitable for multi-tenant production apps right now.
- **Google Generative AI library is the safer bet today (Brandon):** For most business use cases — sequential AI calls with tool use — the Gen AI library works perfectly and avoids ADK's deployment pain.
- **Most businesses don't actually need agents (Brandon):** "You really just need four AI calls in a sequence." Agents are often over-engineered for what companies actually require.
- **Google is positioned to dominate the AI infrastructure stack (Brandon):** They own compute, have multimodal embeddings (the only provider supporting video RAG), and have cheap agent execution pricing — execution is the only missing piece.
- **Sharing technical work on LinkedIn creates inbound opportunities (Brandon):** Documenting cloud architecture decisions, trade-offs, and implementation details publicly attracts high-value consulting and employment opportunities.
- **Code quality matters even in the vibe-coding era (Brandon):** AI can generate working code, but building it in a scalable, maintainable way remains a scarce and valuable skill.
- **Railway is fine for MVPs; GCP/cloud is needed for scale (Brandon):** Railway's single-service model breaks down when multiple customers are processing heavy workloads simultaneously (e.g., Dockling document processing needs GPU).
- **Multi-tenant org setup is simpler than it sounds (Brandon):** Adding organization support is mostly two new tables (organizations + roles) and filtering data by org on each page request. Complexity only grows when users belong to multiple orgs.

## qa

**Q (Sam):** What are good tips for deciding agent architecture — specifically when to move from a supervisor/router pattern to distinct sequential flows?

**A (Brandon):** Keep agents to five tasks or fewer. If an agent needs more than one "virtual hand," split it. The root cause of agent failures is context window overflow, so give everything a single purpose. If your prompt is over ~200 lines or covers more than five phases, start splitting. Typically you end up with a root agent that delegates, or a root agent plus sequential sub-agents — that covers 80% of use cases.

---

**Q (Hemal):** What wireframing tool do you recommend for simple box-and-arrow diagrams?

**A (Brandon):** Excalidraw. It has a great free tier, keyboard shortcuts (numbers 1–6) for switching between shapes, and output you can screenshot and drop directly into Cursor. It's what Brandon uses for everything including agent architecture diagrams.

---

**Q (Pedro):** I'm building a B2B lead generator for non-profits and want to send ~100 personalized emails per week. What do you recommend?

**A (Brandon):** For application-level email (triggered from your app), Mailgun is solid. For higher-volume cold outreach and automation, Instantly is excellent — their YouTube channel has step-by-step tutorials including examples of starting a business with direct outreach in a day. Mitch on the call is a resident Instantly expert for additional guidance.

---

**Q (Morgan):** How should I handle a new freelance client where I'm worried about follow-through? Should I charge for the requirements/discovery phase?

**A (Brandon):** Yes — frame it as a paid "AI discovery" or strategy document. This filters out tire-kickers and ensures commitment. If they proceed with you, apply the fee toward the project. Always get at least some money upfront (e.g., a $1,000 kickoff) to align incentives. Also include a defined two-week testing period at project close so you're not obligated to fix "bugs" indefinitely.

**A (Prem/Tom):** Rename it from "requirements document" to "strategy" or "project initiation document" — the old terminology doesn't sell as well. Make clear that the document has standalone value (a third party could use it), which justifies charging for it separately.

---

**Q (Mark):** I want to expose local apps without deploying to Railway. Is Cloudflare the right tool?

**A (Brandon):** For simply exposing localhost to the internet, ngrok is simpler — $8/month gets you three endpoints. You just run two commands and your app is accessible from anywhere. Cloudflare Tunnel works too but involves more setup steps.

---

**Q (Mark):** What third-party email provider can I use instead of Gmail credentials for sending from my LangGraph apps?

**A (Morgan/Bastian):** If you have a Hostinger account, you can use their SMTP. Cloudflare can also handle DNS and email routing. Superhuman is a great email client but it still sits on top of Gmail.

---

**Q (Prem):** Why did ShipKit move from Railway to Google Cloud for background job processing?

**A (Brandon):** Railway runs a single service with no auto-scaling. For CPU/GPU-intensive tasks like document processing with Dockling, one large job blocks all other customers. GCP with a proper queue (Cloud Tasks/Pub-Sub) scales horizontally. Idle cost on GCP is ~$3/month — cheaper than Railway — and it's built for real multi-tenant production workloads.

---

**Q (Prem):** Is there a plan to add a simple line-of-business (CRUD) template to ShipKit, not AI-specific?

**A (Brandon):** Yes — the next two base templates planned are: (1) a basic Next.js application with a simplified background worker, and (2) a Vex-based template. These will let members spin up real-world apps quickly without needing the full AI stack.

---

**Q (Prem):** Does ShipKit support multi-tenant organization setups (org → multiple users)?

**A (Brandon):** Not currently in the template, but it's not a large lift. You need two additional tables: organizations and roles within an organization. Every page query then filters by the user's org. Complexity increases only when users can belong to multiple orgs simultaneously.

---

**Q (Hemal):** When should a client choose ChatGPT Enterprise / OpenAI's vector store versus building a custom RAG solution?

**A (Brandon):** It depends on what file types and modalities you need. OpenAI's vector store doesn't support multimodal embeddings (e.g., video). Google is currently the only provider with true multimodal embeddings, meaning you can query across PDFs, images, and video. If you need that breadth, build your own RAG on Google. If text-only documents are sufficient and you want simplicity, OpenAI's built-in vector store is fine.

---

**Q (Tom):** For enterprise Active Directory / SSO integration, is there an affordable option beyond WorkOS ($125/org/month)?

**A (Brandon):** Clerk covers many auth scenarios but doesn't do true Active Directory. For real AD/SSO, you're essentially forced into enterprise-tier pricing with WorkOS, Okta, or Auth0. Supabase has SSO but requires connecting to one of those providers anyway.

---

**Q (Hemal):** Should I continue going deep on Google ADK for my company's AI rollout, or pause and wait for LangGraph?

**A (Brandon):** For production deployment today, use Google's Generative AI library — it handles sequential workflows and tool calls perfectly. ADK is great locally but has two blocking issues in production: no streaming on Vertex AI Agent Engine, and different API endpoints for local vs. cloud. These are on Google's roadmap to fix. Once fixed, ADK will likely be the clear winner. For now, avoid ADK in production multi-tenant scenarios.

---

**Q (Jake):** What would trigger Google to prioritize fixing ADK's production issues?

**A (Brandon):** Developer complaints are already on the roadmap. The fixes are coming — it's a question of timing (could be weeks or months). Google has every structural advantage (owns compute, cheapest execution costs, best multimodal models) and just needs to execute on deployment UX. More developers voicing the pain points helps accelerate prioritization.

## tools

- **ShipKit** — Brandon's course/template platform being discussed and iterated on live throughout the call
- **LangGraph** — Agent orchestration framework; Sam's preferred tool; discussed as more production-ready for cloud deployment than ADK currently
- **Google ADK (Agent Development Kit)** — Google's agent framework; praised for local dev experience, criticized for broken streaming and dual-endpoint issues in Vertex AI production
- **Vertex AI / Agent Engine** — Google's cloud deployment target for ADK agents; currently lacks streaming support and has rate-limit issues
- **Google Generative AI Library** — Recommended as the safer production choice over ADK for sequential AI workflows today
- **Excalidraw** — Wireframing/diagramming tool; Brandon's go-to for agent architecture and app design before coding
- **Cursor** — AI-powered code editor; Brandon's primary coding environment; mentioned his bill reached thousands of dollars building ShipKit
- **Claude Sonnet 4.5 / Claude 4.5 Max** — Anthropic model; Brandon's current primary model in Cursor; Max mode gives 1M token context window
- **Grok (xAI)** — Released a 1M-token model; Brandon tried it as a free alternative to manage Cursor costs
- **Instantly** — Cold email outreach platform; recommended for Pedro's B2B lead generation; their YouTube channel cited as a tutorial resource
- **Mailgun** — Email API; recommended for application-level transactional email sending
- **Asana MCP** — MCP connector for Asana; Mitch used it with Claude to automate weekly account update emails, saving ~2 hours
- **Obsidian** — Note-taking app with markdown; Mitch discussed using it with Hugo to publish blog articles from local notes
- **Hugo** — Static site generator; mentioned in context of converting Obsidian markdown to blog posts
- **Fabric** — Open-source AI tool by Daniel Miessler for structuring personal knowledge/markdown; Patrick and Morgan referenced it
- **Limitless** — Wearable/AI memory device; Mitch mentioned someone connecting it via MCP to Claude Code to recall past conversations
- **Whisper Flow** — Voice-to-text tool; Brandon mentioned it as part of a future where users talk to AI agents connected to all their data
- **Railway** — Cloud hosting platform; discussed as great for MVPs but lacking auto-scaling for production multi-tenant workloads
- **ngrok** — Tunnel service; recommended for exposing localhost apps without full deployment; ~$8/month for 3 endpoints
- **Cloudflare / Cloudflare Tunnel** — DNS and tunnel service; discussed as an alternative to ngrok for local app exposure
- **Mailgun / Hostinger SMTP** — Email sending infrastructure alternatives to using personal Gmail credentials
- **Superhuman** — Premium email client; Bastian's recommendation; sits on top of Gmail
- **WorkOS** — Enterprise SSO/Active Directory provider; $125/org/month; discussed as expensive but necessary for enterprise auth
- **Clerk** — Auth platform; discussed as covering most auth needs but not true Active Directory
- **Supabase** — Database/auth platform; has SSO but requires connecting to Okta/Auth0 for AD
- **Redis / Upstash** — Key-value store for agent memory/session state; Jake recommended Upstash as an easy managed Redis service
- **Replit** — Online IDE; Jake observed a client's code changing in real time as another collaborator edited it simultaneously
- **Elastic Beanstalk** — AWS service; Juan's team using it to unify frontend and backend microservices into a near-production environment
- **EC2** — AWS compute; Juan deployed an LLM inference engine on a GPU instance, separate from the agentic system on CPU
- **Dockling** — Document processing library; mentioned as CPU/GPU-intensive, requiring GPU for full OCR — reason ShipKit moved off Railway
- **Gemini CLI** — Google's CLI AI tool; mentioned as part of the future where developers interact with AI via command line
- **NetworkChuck** — YouTube channel; Mitch referenced a video on the Obsidian → Hugo → blog publishing workflow
- **GMT mini PC** — 128GB LPDDR5X unified memory mini PC with AMD GPU; Juan purchased for ~$2,000 to run local LLMs (up to 7B parameter models)

## links

- No explicit URLs were shared in the transcript. The following resources were referenced by name without links:
- **Instantly YouTube channel** — Recommended for cold email tutorials and real-world outreach walkthroughs
- **NetworkChuck video on Obsidian + Hugo blogging workflow** — Referenced by Mitch; not linked
- **Daniel Miessler / Fabric GitHub** — Open-source personal AI framework; referenced by Patrick and Morgan; not linked
- **YouTube channel reviewing mini PCs / local model hardware** — Mentioned by Bastian in chat; not linked in transcript

## decisions

- **Brandon** will run a poll (via Discord) to find better call times, with at least one ShipKit call time shifting to be more Europe-friendly (targeting ~2 p.m. Eastern / 7 p.m. UK).
- **Brandon** will set up a Discord server for the ShipKit community to improve async communication.
- **Brandon** will build and release a beginner Next.js + TypeScript tutorial video for ShipKit members.
- **Brandon** will build a base ShipKit template for a standard Next.js application with a background job worker.
- **Brandon** will add video timestamp-saving functionality to ShipKit so members can resume where they left off.
- **Brandon** will add Windows-specific keyboard shortcut callouts to ShipKit tutorial content (flagged by Tom).
- **Brandon** will investigate and share a Cloudflare Tunnel tutorial link with Mark for local app exposure.
- **Brandon** offered to review Paul's app plan before Paul signs the client contract (Paul to ping Brandon the next day).
- **Brandon** will reach out to the Google ADK team to ask about the streaming/deployment fix timeline and advocate for prioritization.
- **Paul** will contact Brandon the next day for a pre-contract app plan review.
- **Morgan** will proceed with a paid discovery/strategy document for his new document-scanning client, with IP retained until paid in full.
- **Mitch** will update the group next week on his digital personal assistant project and client outreach results.
- **Pedro** will report back next week on results from Instantly once his email accounts are warmed up.
- **Adam** will present his AI demo (ChatGPT + Google Maps scraping → Google Sheets → Relay → LinkedIn leads) to his audience the following day.
- **Juan** will share more about his cloud architecture work on LinkedIn (encouraged by Brandon to document and post publicly).
- **Sam** will follow up with his accountant lead and update his client project roadmap.
- **Hemal** will use Google's Generative AI library (not ADK) for his company's initial AI rollout, and revisit ADK once deployment issues are resolved.
- **Jake** will keep the group updated on the chaotic client project (vibe-coded app with security flaws).