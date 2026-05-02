## general

This was a group coaching call for an AI-focused community, hosted primarily by Brandon Hancock with co-hosts Paul Miller and Patrick Chouinard. The session opened with Brandon announcing a new call structure: weekly posts in the community platform would collect questions and wins in advance, and the call order would follow those submissions. Brandon also shared plans to shift his YouTube channel toward a podcast-style format documenting the EMS Soap SaaS journey.

The dominant topic of the session was Claude.ai's newly released "Claudebot" (later renamed due to trademark issues), with multiple members sharing hands-on experiments. Patrick Chouinard gave the most detailed demo, showing how he had set up a dedicated Ubuntu VM with its own Google account, GitHub account, Obsidian vault, and Telegram/email interface to run the agent securely as a "service account." Other members discussed compliance (SOC 2 and HIPAA via Vanta), email provider choices for Supabase Auth, voice AI platforms, and developer tooling including the GSD framework and RAG/embedding strategies.

The round-robin portion covered individual projects: Marc Juretus building a fitness app (Sanford Fitness) with AI workout suggestions; Ryan C building a fully automated social media content pipeline for a billionaire client; Scott Rippey demoing a developer project-management tool called Clarity; Glenn Marcus walking through the GSD (Get Stuff Done) spec-driven development framework; and Juan Torres reporting his first week using Claude Code for an accounting-firm vendor-extraction agent. The call closed with discussion of Dario Amodei's essay on AI's "technological adolescence" and a brief debate on whether current models constitute AGI.

## insights

- **Patrick Chouinard:** The performance advantage of Claudebot over raw Claude is not model intelligence—it's the scaffolding and tool layer. "As smarter as nothing to do with the intelligence of the pure LLM—it's scaffolding and tools, and they nailed the scaffolding and tools."
- **Patrick Chouinard:** Treat Claudebot like a new employee: give it its own email, calendar, GitHub account, and Google Drive. Never give it access to your personal accounts.
- **Patrick Chouinard:** To get a "window into the agent's brain," instruct it to mirror all its memory, to-dos, and notes into an Obsidian vault synced to a GitHub repo you can read at any time.
- **Patrick Chouinard:** For security, run Claudebot on an isolated VM in a dedicated VLAN with firewall rules; communicate with it only via Telegram and email. Prompt injection on a shared machine could leak everything on the file system.
- **Patrick Chouinard:** Instruct the agent that its accounts and tools belong to *it*, not to you—otherwise it defaults to acting on your behalf and loses the autonomous framing.
- **Brandon Hancock:** SOC 2 Type 1 is a point-in-time snapshot of compliance; Type 2 proves sustained compliance over 90–120 days and is the gold standard enterprises require.
- **Brandon Hancock:** When choosing a compliance platform (Vanta vs. Drata), prioritize integrations with your actual tech stack—automated evidence collection saves weeks of manual screenshot work.
- **Brandon Hancock:** Compliance is a moat: it's expensive and time-consuming, so competitors can't copy you overnight. Regulated, artifact-producing workflows are among the best SaaS niches for 2026.
- **Brandon Hancock:** Before writing a single line of code for a new app idea, use Claude Code with only a `todos.md` and a `context.md` to prototype the logic through prompts—let AI "pretend to be the application" until the workflow is fully articulated.
- **Brandon Hancock:** For AI agency work, the fastest path to revenue is picking one platform (e.g., LiveKit or Bland AI), building two or three implementations to earn case studies, creating tutorials, and then offering productized services. "Money likes fast movers."
- **Brandon Hancock:** When pitching AI services, lead with concrete case studies and numbers from adjacent industries rather than hand-wavy capability lists—this pre-handles objections before they're raised.
- **Brandon Hancock:** To track per-user API usage and enforce limits, create a `usage` table in the database keyed to user ID and action type, then hydrate a client-side context provider with that data so any component can check limits.
- **Brandon Hancock:** Vercel AI SDK tool calls (propose/confirm/edit) are the right pattern for letting an AI suggest structured data (e.g., a workout) that the user can approve or modify before it's saved.
- **Glenn Marcus (GSD framework):** GSD front-loads all product-manager-style questioning into a spec phase, then executes tasks in a RALF loop with file-system memory—making sessions interruptible and resumable without context loss.
- **Scott Rippey:** Claudebot's SQLite memory layer combined with BM25 keyword search and vector embeddings is why users feel the agent "knows them"—it's a hybrid retrieval system, not just a chat history.
- **Brandon Hancock:** When something cool and open-source ships (Claudebot, GSD), clone the repo and ask Claude Code to teach you how the core loops work—best practices are right there in the code.

## qa

**Q (Prem):** What vendor are you using for SOC 2 and HIPAA compliance, and what does it cost?
**A (Brandon Hancock):** We chose Vanta over Drata primarily because Vanta had a Supabase integration. The raw cost for SOC 2 + HIPAA with both a Type 1 and Type 2 audit was $20,000; we got $4,000 off through our TinySeed accelerator discount. The annual subscription after that is roughly $10–12K. The audits themselves are one-time; you'll pay for a second audit the following year.

**Q (Prem):** Do you have to do SOC 2 Type 1 before you can get Type 2?
**A (Brandon Hancock):** SOC 1 is for banks; SOC 2 is for tech companies. Within SOC 2, Type 1 is a point-in-time snapshot ("Brandon was compliant on January 1st"), while Type 2 proves sustained compliance over 90–120 days. Type 2 is the gold standard. If a company's website just says "SOC 2" without specifying Type 2, they're probably only Type 1.

**Q (Prem):** Is the compliance process significantly more complicated if you actually store HIPAA data versus using zero data retention?
**A (Brandon Hancock):** It's always going to be hard regardless—half the work has nothing to do with your actual code. You have to write incident response plans, document how you detect anomalous activity, and create dozens of policies. ZDR reduces scope but doesn't eliminate the process. We're pursuing full storage capability because it unlocks feedback loops to improve our AI models and is required by enterprise customers.

**Q (Morgan Cook):** What email provider should I use instead of Supabase's built-in email (which throttles at 30/day)?
**A (Brandon Hancock / Ty Wells):** Both Mailgun and Resend work well. Ty Wells uses Resend and finds it reliable, easy to integrate, and reasonably priced with no spam issues. Jake Maymar noted that if your client controls their own domain hosting (e.g., Wix), some providers won't work and you may be forced to use SendGrid—so confirm the hosting situation first.

**Q (Ama):** I want to build a personal execution system—a simple daily task view that only intervenes with AI suggestions when I repeatedly fail to complete something. How should I start?
**A (Brandon Hancock):** Don't build the app yet. Create an empty folder, open Claude Code in it, and make two files: `todos.md` (your pretend database) and `context.md` (instructions for how the agent should behave). Have Claude pretend to be the application and run through scenarios until the decision tree is fully articulated—when does it break a task down, when does it send a reminder, what triggers intervention? Once that sandbox works the way you want, converting it to actual code is straightforward.

**Q (Raghav Ram):** For an idea that doesn't fit an existing ShipKit template, do we just create a new directory and start Claude Code there?
**A (Brandon Hancock):** Yes, but the point of the exercise I described to Ama is to clarify *what* you want to build before writing any code. Start with an empty project, use Claude Code with only markdown files, and prototype the logic through prompts. Once the system is working as intended in that sandbox, you can then scaffold it into a proper application—the Worker SaaS template would be a good fit for Ama's use case once the decision tree is defined.

**Q (Marc Juretus):** How do I throttle users' AI chat usage (token limits) based on their login in a Supabase + Railway app?
**A (Brandon Hancock):** Create a `usage` table in Supabase with columns for user ID, action type (message sent, workout generated, etc.), and timestamp. Then build a context provider in your Next.js app that hydrates with the user's usage data on login. Any component can then call `useUser()` to check how many messages or actions the user has consumed and block or warn accordingly. You can also surface this to users as "5 of 50 messages used."

**Q (Paul Miller):** Is Bland AI your preferred voice platform, or would you use something else?
**A (Brandon Hancock):** Bland is the one I've seen no-coders successfully implement. Bastian has gone deepest with LiveKit, which likely has the most customization. If I were starting an AI agency in 2026 focused on voice, I'd pick one platform—LiveKit or Bland—become the trusted implementer, build a few projects for free to get case studies, create YouTube tutorials, and then offer productized services. That playbook could realistically generate $300K+ this year.

**Q (Hemal Shah):** For Claudebot security, should you install it on a separate machine rather than your personal computer?
**A (Patrick Chouinard):** Never run it on your personal machine. At minimum use WSL or a Docker container. Ideally, run it on a dedicated VM in an isolated VLAN with firewall rules limiting which ports it can communicate through. Claudebot has file system access, so a prompt injection attack could exfiltrate everything on the machine. Communicate with it only via Telegram and email.

**Q (Brandon Hancock):** Does Claudebot use hooks to save to the Obsidian vault after every action, or did you just tell it in chat?
**A (Patrick Chouinard):** I just told it in chat: "duplicate everything you write to your memory to the Vault." It now knows the Vault is its own Obsidian Vault and does it consistently. No hooks required—just be very specific that the Vault belongs to *it*, not to you.

**Q (Jake Maymar):** How do you manage multiple email accounts with Claude Code?
**A (Jake Maymar / Brandon Hancock):** Jake uses Composio, which sets up a Gmail MCP server for each email account. You then tell Claude Code "go look at my personal email" or "go look at my company email" and it handles the routing. Composio is SOC 2 compliant, which makes it reasonable to grant access.

## tools

- **Claudebot / Claude.ai (renamed due to trademark)** — Agentic AI assistant running on a local/VM environment; main topic of discussion; multiple members demoing setups
- **Claude Code** — Anthropic's CLI coding agent; used by nearly all members for development; discussed as the engine Claudebot delegates coding tasks to
- **Vanta** — Compliance automation platform chosen for SOC 2 + HIPAA; selected over Drata due to Supabase integration
- **Drata** — Alternative compliance platform to Vanta; mentioned as the other main player in the space
- **Supabase** — Backend-as-a-service (Postgres + auth); used by multiple members; discussed in context of email throttling and compliance integrations
- **Railway** — Container hosting platform; Brandon migrating off it because Vanta lacks a Railway integration
- **Google Cloud Platform (GCP)** — Brandon migrating Docker workloads to GCP for Vanta compliance integration
- **Resend** — Transactional email provider; recommended by Ty Wells as reliable replacement for Supabase's built-in email
- **Mailgun** — Transactional email provider; mentioned alongside Resend as a solid alternative
- **SendGrid** — Email provider; came up as a fallback when client domain is hosted on Wix
- **Vercel AI SDK** — Used for tool calls (propose/confirm/edit patterns) in AI chat interfaces
- **Terraform** — Infrastructure-as-code tool; Brandon using it to manage GCP resources (PubSub, Cloud Run, service accounts)
- **Proxmox** — Hypervisor Patrick uses to run his dedicated Ubuntu VM for Claudebot
- **Ubuntu Server / Ubuntu Desktop** — Patrick's VM OS for Claudebot; planning to move to desktop for full browser GUI capability
- **Telegram** — Communication channel between Patrick and his Claudebot agent
- **Obsidian** — Note-taking app; Patrick has Claudebot mirror all its memory to an Obsidian vault in a GitHub repo
- **Brave API** — Search API Patrick gave Claudebot for "unknown unknowns" discovery in its daily AI news digest
- **Perplexity API** — Deep-dive research API Patrick gave Claudebot; used for detailed topic analysis in the daily digest
- **Notebook LM** — Google's AI notebook tool; Patrick uses an MCP integration to push Claude Code session summaries into it for training artifacts
- **Notion** — Project management tool; Marc using it with a roadmap and Claude pulling backlog items
- **Bland AI** — Voice AI platform; mentioned as the most accessible for no-coders building voice agents
- **LiveKit** — Voice AI platform; described as having the most customization; Bastian cited as the deepest user in the community
- **WAPI** — Voice AI platform; Hemal's colleague migrated from Bland to WAPI; mentioned as an emerging alternative
- **Keragon** — HIPAA-compliant workflow automation platform (described as "N8N for healthcare"); integrates with Epic, Cerner, and other EHRs
- **Composio** — MCP server manager for email accounts; Jake uses it to give Claude Code access to multiple Gmail accounts
- **Voyage AI** — Embedding model provider with Anthropic partnership; mentioned by Scott and Glenn as alternative to OpenAI embeddings; owned by MongoDB; offers 200M free tokens
- **ChunkHound** — Local codebase indexing tool; Glenn uses it to augment Claude Code sessions with semantic search instead of grep/regex; recommends Voyage AI
- **Cohere** — Re-ranking layer in Juan's multi-layer RAG pipeline (Layer 2)
- **Tiktoken** — Token counting library; Bastian recommended it for measuring token usage and pre-validating payload sizes before embedding
- **GSD (Get Stuff Done) framework** — Open-source Claude Code prompt framework for spec-driven development; Glenn demoed it; features PM-style interviewing, phase planning, and RALF loop execution
- **Suno** — AI music generation tool; Ryan mentioned using it to generate a song ("One Shot Scott")
- **Limitless** — Wearable recording device; Scott and Ty use it to capture conversations and automatically extract project notes
- **Whisper Flow** — Voice-to-text tool; Ty used it to dictate a Claudebot setup prompt during the call
- **Amazon Rekognition** — AWS image/video recognition service; Ryan fighting re-indexing issues with it for a social media client
- **Eleven Labs** — Voice AI platform; briefly mentioned in context of voice agent options
- **GLM 4.7** — Chinese open-source LLM; discussed as a cost-effective alternative model for Claudebot (15–20x cheaper than Claude)
- **Kimi K2 / 2.5** — New model that dropped during the call; Juan flagged it; Brandon noted he needed to watch the video
- **TinySeed** — SaaS accelerator Brandon is part of; provided a $4K discount on Vanta
- **Dan Martell** — Referenced as an example of a SaaS expert with a strong YouTube/content presence
- **Extreme Ownership (book)** — Brandon recommended Chapter 3 to Paul for managing the CEO/CTO dynamic

## links

- **Patrick's Training Harness GitHub repo** — Public repo of Claude skills/commands that document coding sessions and push artifacts to Notebook LM; Patrick shared the link in chat during the call
- **Keragon** — HIPAA-compliant healthcare integration platform; Jake shared the link in chat (connects to Epic, Cerner, and other EHRs)
- **Dario Amodei's essay on AI's "technological adolescence"** — Jake shared the link in chat; essay opens with a reference to the film *Contact* and discusses AI's societal trajectory
- **ChunkHound** — Glenn shared the link in chat; local codebase RAG/indexing tool that recommends Voyage AI for embeddings
- **Brandon's Pokemon AI video generator video** — Referenced by Brandon as an example of building a Claude Code–only application using only prompt files and no traditional code; available on his YouTube channel
- **Claude Code Anonymous group** — Mentioned by Brandon; founded by the Claudebot creator; members call themselves the "Black Eyed Club" for sleep deprivation from coding sessions

## decisions

- **Brandon Hancock** will wait at least one week before connecting personal accounts to Claudebot, to avoid potential security incidents from early-release vulnerabilities
- **Brandon Hancock** will upload the Fathom call recording so Marc can use it as context for building the usage/query tracking table and context provider
- **Brandon Hancock** will share the Vercel AI SDK tool-call documentation link with Marc to help implement the propose/confirm/edit workout pattern
- **Brandon Hancock** will post the new Zoom link and weekly community post structure so members know to submit questions and wins before each call
- **Brandon Hancock** will be on every fourth call going forward; Paul Miller, Patrick Chouinard, and Tom Welsh will host the intervening calls
- **Patrick Chouinard** will migrate his Claudebot from Ubuntu Server (headless) to Ubuntu Desktop so it has full browser/GUI capability for tasks like browsing the school community
- **Patrick Chouinard** will continue expanding the public Training Harness repo and share updates with the community
- **Patrick Chouinard** will explore giving Claudebot the ability to code tools *for itself* (not for humans) to extend its own capabilities
- **Scott Rippey** will talk to Patrick offline to harden his Claudebot security setup after going "YOLO" with his personal machine
- **Scott Rippey** will sync with Ty Wells to compare their developer project-management tool ideas (Clarity vs. Ty's project)
- **Ryan C** will email Brandon about the offer to have a separate strategy conversation (carried over from the previous week)
- **Ty Wells** will post a Claudebot setup prompt to the community once his sub-agents finish running, so others can replicate his setup
- **Jake Maymar** will continue investigating Keragon to understand how its MCP/integration layer actually works under the hood
- **Juan Torres** will send his email address to Brandon in the chat so Brandon can locate his account for a discount
- **Glenn Marcus** will clone the GSD repo and explore integrating pieces of it into his ShipKit workflow