## general

This was a weekly group coaching/peer-learning call for a community of AI practitioners and developers. The session was facilitated by Patrick Chouinard and included regular members Ty Wells, Marc Juretus, Ryan C, Morgan Cook, Juan Torres, Tom Welsh, Ana P, Elena, Andrew Nanton, and Elijah Stambaugh. Each participant gave a brief update on what they had been working on, followed by open discussion and Q&A.

Topics ranged from hands-on AI development projects (fine-tuning small models, building agentic DevOps pipelines, deploying Claude Code remotely via Tmux and the Claude mobile app) to product and business discussions (Heritage Plot gravesite app, a lead-capture SaaS idea using Meta glasses, video streaming quality issues on a social platform). The call also covered tooling choices for static sites (Astro, Svelte, Cloudflare), second-brain infrastructure (Obsidian vs. Notion), and Azure privacy concerns for a document-processing product targeting expert witnesses.

Two extended discussions stood out: Patrick's detailed walkthrough of his infrastructure-as-context approach—using Claude Code as an operator to provision and manage Docker containers and Ubuntu VMs, with remote access via Tmux and the Claude `/remote-control` slash command—and a closing conversation about how to teach AI interaction skills to younger or non-technical audiences, emphasizing full-context conversation over short queries.

The call ended with a discussion on second-brain tooling, where Patrick advocated for Obsidian with a terminal plugin running Claude Code inside the vault, synced via GitHub, as a low-friction alternative to Notion or a Supabase backend.

---

## insights

- **AI-generated code quality is improving but hallucination remains ~30%**, causing bugs that propagate through codebases; developers report spending more time fixing AI code than writing it. (Ty Wells)
- **The top real-world use of AI among developers is debugging/stack-trace analysis**, not code generation—because writing code was never the bottleneck. (Ana P)
- **Claude Code works better with CLIs than with MCP servers**; Patrick found Claude far more effective using tools like Wrangler (CLI) than MCP equivalents.
- **Building everything as CLI rather than UI reduces front-end testing burden** and makes components easier to chain together. (Ty Wells)
- **"Infrastructure as context"**: instead of scripts, give Claude Code an architecture document describing how to provision a machine; Claude then builds and manages the infrastructure and retains full context for future changes. (Patrick Chouinard)
- **Claude's `/remote-control` slash command + Tmux** allows a persistent, remotely accessible Claude Code session on any machine, accessible from the Claude mobile app—one session per machine, but workaround is one container per project. (Patrick Chouinard)
- **Personal side projects consistently outperform client work as product ideas**; the problems you solve for yourself are the ones others also have. (Morgan Cook)
- **Older users tend to onboard to AI faster than younger users** because they are trained in full-context conversation, whereas younger users default to short query-style interaction (Google-trained behavior). (Patrick Chouinard)
- **Teach AI interaction as collaboration, not querying**: express context, goals, constraints, and desired output clearly—politeness is technically functional, not social. (Patrick Chouinard)
- **For non-technical stakeholders, use ego as currency**: don't convince them your solution is secure—guide them to conclude it themselves. (Patrick Chouinard)
- **When training small models for proof-of-concept**, use a tiny model (e.g., Gemma 1B) to reduce cost, speed up iteration, and expose training edge cases more clearly than a large model would. (Patrick Chouinard, Morgan Cook)
- **Obsidian + Claude Code terminal plugin + GitHub sync** is a low-friction, free second-brain setup that gives Claude full access to your notes without blowing context or requiring a vector database. (Patrick Chouinard)
- **Dashboards tend to cut the piece of information you need most**; querying Claude Code directly against your data store is more reliable than maintaining a dashboard. (Patrick Chouinard)
- **Time-to-market for software is now extremely fast; the new bottleneck is the other business pillars** (marketing, legal, client decision cycles). (Tom Welsh, Morgan Cook)
- **The generation born talking to computers is now at a disadvantage** talking to AI, because AI has upgraded to human-style conversation while they optimized for short queries. (Patrick Chouinard)

---

## qa

**Q (Marc Juretus):** Has anyone trained their own models, and what did you use?
**A (Juan Torres):** I've deployed LLMs on EC2 with GPU/CPU tuning but never done fine-tuning or LoRA. (Patrick Chouinard added: use a very small model like Gemma 1B—faster, cheaper, proves the point without overspending.)

**Q (Juan Torres):** Why do you need to fine-tune or train a model at all?
**A (Marc Juretus):** Mostly proof of concept and to be able to say I've done it. There's no strong efficiency argument; a workflow could do the same thing.

**Q (Morgan Cook):** Are you using Astro and Wrangler for Cloudflare deployments?
**A (Patrick Chouinard):** Yes. Wrangler as CLI is more effective with Claude than using an MCP server. Claude handles all the Cloudflare configuration. Every site I've shared is an Astro site hosted on Cloudflare.

**Q (Morgan Cook):** Are you pushing to Cloudflare from your workstation or via GitHub CI/CD?
**A (Patrick Chouinard):** From a local VM on my Proxmox server. I avoid GitHub Actions when I can to avoid paying for it if my own infrastructure can do the job.

**Q (Ana P):** How does the Limitless/Fieldy → Secure Claw → Telegram workflow actually work?
**A (Ty Wells):** The wearable device has a webhook trigger. That hits Secure Claw (my version of OpenClaw), which has access to all my projects and multiple terminal sessions. It passes the message to the relevant project to plan and build the feature. If it needs input, it messages me on Telegram and waits.

**Q (Ana P):** Is there good material on agent development lifecycle (AGLC), and would ShipKit help?
**A (Patrick Chouinard):** AGLC is largely a marketing term—it's SDLC applied to agents. ShipKit is well-structured training that teaches SDLC in a way that transfers directly to agent development with minimal stretch. Consider proposing it to your company as training material so they finance it.

**Q (Andrew Nanton):** Clients are comfortable with OneDrive but resist other Azure services even within the same tenant. Is this a real security difference or perception?
**A (Patrick Chouinard):** Technically and contractually, it's the same—same tenant, same privacy contract. It's a perception issue. Use analogies (walled home office, tunnel between two houses) rather than technical arguments. Don't convince them it's secure; guide them to conclude it themselves.

**Q (Andrew Nanton):** Any experience with Azure Content Understanding vs. Azure Document Intelligence?
**A (Ty Wells):** Dropped a comparison graphic in the chat for reference.

**Q (Elijah Stambaugh):** What's the right infrastructure for a "second brain" that gives AI context across all your work?
**A (Patrick Chouinard):** Don't over-engineer it. Use Obsidian (free, Markdown-native) with the terminal plugin to run Claude Code inside your vault. Sync the vault to GitHub for free. Claude Code has access to all your notes and can answer questions just-in-time without a vector store or Supabase backend.

**Q (Elijah Stambaugh):** How do you teach AI interaction skills to students or younger people who default to short queries?
**A (Patrick Chouinard / Morgan Cook):** Have them practice explaining a project to another student out loud—whatever they say is exactly what they should type into Claude. The skill gap is description vs. querying. You can also record the conversation with a tool like Fathom and dump the transcript directly into Claude to show them how it works.

---

## tools

- **Claude Code** – Primary agentic coding tool used by multiple participants; discussed for DevOps provisioning, remote control via mobile, and running inside Obsidian vaults
- **Claude `/remote-control` slash command** – New Claude Code feature enabling remote session access from the Claude mobile app; Patrick built a multi-container setup around it
- **Tmux** – Used by Patrick to keep Claude Code sessions alive on remote VMs after disconnecting
- **Dockling** – Used by Marc to RAG 58 documents for a simulated ISP customer service chatbot
- **Google Colab** – Used by Marc to train a small model on resume and movie-preference data
- **Hugging Face** – Used by Marc to save and serve the model trained in Google Colab
- **Vertex AI** – Marc used it for a customer churn prediction model; noted it was expensive
- **Astro** – Static site framework recommended by Claude and used by Patrick for all his published sites and documentation
- **Svelte** – Recommended as an intermediate step between Astro and full React/Next.js for interactive components
- **Wrangler** – Cloudflare CLI tool; Patrick prefers it over MCP for Claude Code deployments
- **Cloudflare (Pages, R2, D1, Stream)** – Hosting and storage platform used by Patrick and Ryan; Ryan using Cloudflare Stream for adaptive video quality
- **Cloudflare Stream** – Ryan implementing it for multi-resolution video streaming (~$5/month for 1,000 minutes)
- **FFmpeg** – Patrick suggested using it with Claude Code scripts for video transcoding/resolution management
- **Proxmox** – Patrick's local hypervisor for spinning up Ubuntu VMs
- **Docker** – Used by Patrick to containerize Claude Code instances, one per project
- **Prometheus / Grafana / Alert Manager** – Patrick deployed a full monitoring stack connected to Discord for alerts
- **Obsidian** – Markdown-based note-taking app; recommended as second-brain tool with Claude Code terminal integration
- **Notion** – Discussed as an alternative to Obsidian; noted as improving with Opus 4.6 and agents but not Markdown-native
- **GitHub** – Used by Patrick to sync Obsidian vaults and version-control VM configurations
- **Kiro CLI** – Juan used it for agentic DevOps / natural-language AWS resource creation; found Claude Code + AWS CLI more effective
- **AWS CLI** – Juan gave Claude Code AWS CLI permissions to provision EC2 instances and configure networking agentically
- **Limitless (wearable device)** – Ty's always-on recording device with trigger word; feeds into Secure Claw workflow; Meta acquired the company and stopped selling the device
- **Fieldy** – Alternative wearable to Limitless shown by Patrick; has a webhook but limited API
- **Secure Claw** – Ty's personal fork/extension of OpenClaw for agentic task execution
- **OpenClaw / Daniel Meisler's PAI** – Original personal AI infrastructure framework that inspired Secure Claw and others
- **Fabric** – Daniel Meisler's tool for prompt patterns and YouTube summarization, mentioned by Morgan and Tom
- **Telegram** – Used by Ty's agent to send status updates and receive instructions while away from desk
- **Vanta.js** – JavaScript library Juan used for the animated 3D globe background on his landing page
- **ShipKit** – AI development training platform discussed as a structured way to learn agent development lifecycle
- **Azure Document Intelligence / Content Understanding** – Andrew using these for PDF processing in his expert witness document tool
- **AZ CLI (Azure CLI)** – Andrew found giving this to LLMs far more effective than navigating Azure's enterprise AI portal
- **Supabase** – Discussed as a potential (but over-engineered) vector + file store for a second brain
- **Fathom** – Mentioned as a recording tool that could capture student conversations for AI input in classroom settings
- **Meta glasses** – Ryan planning to buy them to capture van/business photos while driving for lead generation
- **Notion AI** – Elijah noted it has improved significantly with Opus 4.6 and now includes agents

---

## links

- **Daniel Meisler's Personal AI Infrastructure (PAI / OpenClaw)** – GitHub repo shared by Patrick in chat; described as the original OpenClaw implementation and worth reading in full
- **Vanta.js** – Juan shared the link in chat; JavaScript library for animated 3D backgrounds
- **YouTube video: Claude Code inside Obsidian vault** – Patrick posted a link; attributed to Greg Eisenberg, demonstrating the terminal plugin workflow
- **Two Obsidian CLI tools** – Andrew shared links: one for interacting with Obsidian from the command line, one for headless vault sync without running the application
- **intel.patchutech.com** – Patrick's personal AI news aggregation pipeline site, now being adapted for a client deployment

---

## decisions

- **Marc Juretus** will take the Google AI Generative Leader exam the Saturday after next (~$99 fee)
- **Marc Juretus** will build a movie-preference model using Google Colab and Hugging Face (100 thumbs-up/down data points) as a proof-of-concept fine-tuning exercise
- **Marc Juretus** will explore deploying a fine-tuned model to an EC2 instance as a next step after the Colab/Hugging Face experiment
- **Patrick Chouinard** will put the link to last week's recording (Brandon's seed funding discussion) in the chat for Elena
- **Patrick Chouinard** will leave a verbal note in the video for Brandon about Morgan's Heritage Plot project status
- **Morgan Cook** will continue having his marketing contact research pricing and target market for Heritage Plot before moving forward
- **Ryan C** will investigate using FFmpeg with Claude Code as a fallback if Cloudflare Stream implementation doesn't work for multi-resolution video
- **Ryan C** will order Meta glasses (~£400) to prototype a lead-capture workflow (photo → AI research → outreach email)
- **Juan Torres** will share the link to his landing page in the community for feedback
- **Ty Wells** will drop a link to his "website as application" (no-scroll viewport) example in the chat for Juan
- **Patrick Chouinard** will consider revamping his personal website to reduce scrolling based on Ty's suggestion
- **Elijah Stambaugh** will try Obsidian with the terminal plugin running Claude Code inside the vault as an alternative to his current Notion + Supabase exploration