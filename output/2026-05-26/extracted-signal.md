## general

This was a group coaching/community call hosted by Brandon Hancock with regular members including Patrick Chouinard, Bastian Venegas Arevalo, Tom Welsh, Scott Rippey, Morgan Cook, Juan Torres, and others. The session opened with a community question from Hiral (Prakrit) about building an AI-powered vocabulary learning app for her son, followed by project updates from each member. Topics ranged from agentic AI setups (Hermes vs. OpenClaw), PDF extraction pipelines, local model infrastructure, and client work.

Patrick Chouinard shared a pre-release of his "Community Brain" distribution repository — a RAG-based knowledge base fed by weekly meeting recaps — and discussed replacing his OpenClaw setup with Hermes, an agentic AI framework he connected to Codex, Discord, Tavily, Firecrawl, and Honcho. Brandon Hancock shared his "deep work" workflow of running parallel Codex work-tree sessions overnight. Scott Rippey presented multiple projects: an AI news digest newsletter, a parking payment app that generated $5k for a client in its first weekend, a Milanote replacement called Lightwell Board, an Ironclaw local AI assistant, and a video generation GitHub repo using Remotion, ElevenLabs, and Higgs Field.

Morgan Cook (celebrating his birthday) demonstrated SignPy, a lobby display board running on a Raspberry Pi, and discussed automating Google Workspace workflows for a foundation client. Juan Torres showed his AI photo booth application with image transformation, CloudFront delivery, QR code download, and a data observability dashboard. Alex Roca discussed plans to make his studio booking app multi-tenant after getting interest from additional clients. Bastian Venegas Arevalo reported pitching a healthcare center on a patient-journey state machine and appointment chatbot, framing it as a partnership rather than a flat software sale.

## insights

- **Spec-driven development requires a foundation first** (Brandon): It works best when you already have clarity on infrastructure (framework, database, deployment). Without that, it loops endlessly without forward progress.
- **For word-lookup apps with many AI-generated components**, use sequential and parallel LLM calls with structured outputs rather than a single chat call; each call takes the word as input and produces a structured JSON object.
- **Choose smaller, faster models for high-frequency, simple tasks** (Patrick): For single-word lookups, use Gemini Flash or GPT-4o Mini/Nano instead of large frontier models — dramatically lower latency and cost with no quality loss.
- **Structured outputs + a cheap TTS model** can generate pronunciation audio with stress markers, avoiding the need for a separate pronunciation database (Bastian's suggestion to Hiral).
- **PDF extraction pipeline upgrade** (Brandon): Convert each PDF page to an image, then pass the full image to a multimodal model (e.g., Gemini Flash) with a prompt to produce markdown. Results are dramatically better than text-only extractors like Dockling, especially for tables, flowcharts, and mixed content.
- **Adversarial code review via the Codex plugin for Claude Code** consistently finds issues that Claude alone misses, because different models have different biases (Patrick).
- **"Deep work" overnight sessions** (Brandon): Queue up 5 parallel Codex work-tree sessions each night, each running 5–7 self-critiquing iterations on a specific goal. Wake up, review, and merge — effectively doubling productive hours.
- **Hermes advantages over OpenClaw**: cleaner API key management, built-in identity isolation, Kanban dashboard, recursive self-updating skills, bounded system prompt to prevent bloat, and native Codex integration as a sub-agent tool.
- **AI as a foot in the door for consulting** (Brandon): Clients present one surface-level problem; untangling it reveals much larger systemic work. The first engagement is rarely the last.
- **Solve rich people's / high-margin problems**: A healthcare center with large monthly revenue can easily justify AI tooling costs; a hair salon cannot. ROI framing (show them the money they're losing) is more persuasive than feature lists.
- **When building multi-tenant from a single-tenant app**, build a brand-new project with organizations as a first-class concept from day one rather than retrofitting — avoids breaking existing customers.
- **Newsletter monetization playbooks** exist openly from Sean Puri (Milk Road) and Sam Parr (The Hustle) and the Beehive founder — worth studying before monetizing an AI news digest.
- **Hermes recursively builds and prunes its own skills** based on usage, keeping the system prompt within a character limit and removing stale skills automatically (Morgan's summary).
- **Wake-word + termination-word pattern with a meeting transcription API** (Patrick/Fieldy): Poll the transcript every 5 minutes; if a wake word is detected, treat the next sentence as a command to the agent.

## qa

**Q (Tom Welsh):** Should I use a Recap Flow to scan large PDFs and retrieve data from them?
**A (Patrick Chouinard):** No — Recap Flow is built specifically not to digest documents. Everything else is made for that. Use Ollama for embeddings; front-load the PDF extraction separately.

**Q (Hiral/Prakrit):** I built a vocabulary app prototype but lost momentum when I shifted to spec-driven development. When is it worth it, and what should I do next?
**A (Brandon Hancock):** Spec-driven development needs a clear infrastructure foundation first. Since you already have a mock-up and some specs, go back through ShipKit's master plan phases, point to your existing work and screenshots, let it fill gaps, and get a roadmap. Then execute phase by phase. The app is fundamentally sequential/parallel LLM calls producing structured outputs — not RAG.

**Q (Hiral/Prakrit):** The app is slow. How do I fix latency?
**A (Patrick Chouinard):** Use a smaller, faster model — Gemini Flash or GPT-4o Mini/Nano. Don't use a large frontier model for single-word lookups; it costs more and gives no better result.

**Q (Scott Rippey):** Is Hermes actually productive for you outside of coding?
**A (Patrick Chouinard):** Yes — every morning it emails asking for your daily goal, then an hour later sends a ping with research it did, things it prepped, and jobs it scheduled. It interacts via Discord channels to keep context separated per topic.

**Q (Brandon Hancock):** Any cons to Hermes?
**A (Patrick Chouinard):** The cons are the same as any independent agent — you must isolate it properly for security. But Hermes is more organized than OpenClaw: single place for API keys, clear warnings not to paste keys in chat, and a cleaner setup overall.

**Q (Tom Welsh):** For OCRing scanned PDFs, should I use Tesseract?
**A (Brandon Hancock):** No — convert each page to an image and pass it to Gemini (a cheap multimodal model) with a prompt to produce markdown. Results are far better, especially for mixed text/graphics. Tesseract is text-only and struggles with complex layouts.

**Q (Juan Torres):** Do you use specific prompting to convert flowchart images into Mermaid diagrams in markdown?
**A (Brandon Hancock):** For our medical protocol use case, we convert decision trees into nested markdown bullet lists (not Mermaid), because the output needs to be readable plain text for end users. The whole page — text and graphic — goes into Gemini at once.

**Q (Morgan Cook):** Do you spawn parallel agents to process each PDF page?
**A (Brandon Hancock):** It's simpler than that — convert page to image, base64 encode it, make one LLM call per page, get markdown back. Then do smart chunking. The complexity is handling edge cases like tables split across pages.

**Q (Alex Roca):** I want to make my studio booking app multi-tenant. Any recommendations?
**A (Brandon Hancock):** Build a brand-new project with organizations as a first-class concept from the start — don't retrofit the existing app. Once the new version works with dummy orgs, port the existing customer over. Retrofitting risks breaking your current live customer.

**Q (Biggi Fraley):** Have you found it necessary to add an additional memory layer to Hermes?
**A (Patrick Chouinard):** Yes — I added Honcho (honcho.dev) as an additional memory layer.

## tools

- **Hermes** — Agentic AI framework replacing OpenClaw; Patrick uses it with Codex, Discord, Tavily, Firecrawl, and Honcho
- **OpenClaw (Open Claw)** — Previous agentic AI setup; discussed as less secure and harder to configure than Hermes
- **Codex (OpenAI)** — Used as a sub-agent tool within Hermes for coding tasks; also used for overnight deep-work sessions
- **Claude Code / Cloud Code** — Primary coding environment for Brandon and Scott; used for all development work
- **Ollama** — Local model runner; recommended for embeddings (e.g., nomic-embed) in PDF/RAG pipelines
- **Dockling (Docklink)** — PDF text extractor; discussed as limited for complex documents with images/tables
- **MarkItDown (Microsoft)** — Markdown extraction tool for standard documents; mentioned by Bastian as a good option
- **landing.ai** — API-based PDF extraction; Bastian recommends for complex or handwritten documents in production
- **Gemini Flash** — Cheap multimodal model used to convert PDF page images to markdown; Brandon's current approach
- **Tavily** — Web search API connected to Patrick's Hermes instance
- **Firecrawl** — Web scraping API connected to Patrick's Hermes instance
- **Honcho (honcho.dev)** — Memory layer added to Hermes by Patrick; also suggested by Morgan Cook
- **Open Web UI** — Interface for Patrick's Community Brain; works with local models or OpenAI API keys
- **ShipKit** — Course/framework by Brandon; Hiral was using it; includes master plan, prep phases, and chat templates
- **Supabase** — Database backend mentioned for ShipKit stack and multi-tenant app design
- **Vercel** — Deployment platform; Brandon uses Vercel log drain for monitoring
- **Remotion** — React-based video generation framework; core of Scott's video-generator repo
- **ElevenLabs** — Voice synthesis; Scott uses it for his AI news digest audio and video generation (Jarvis voice clone)
- **Higgs Field** — AI video/scene generator used in Scott's video-generator repo
- **FFmpeg** — Audio leveling and video processing in Scott's video-generator pipeline
- **Pixel Precise** — Tool for color sampling and annotation in Scott's video workflow
- **Milanote** — Visual organization tool Scott is building a replacement for (Lightwell Board)
- **Resend** — Email delivery service used by Scott for AI news digest and by Juan for event image delivery
- **Twilio** — SMS/text messaging for Scott's parking app; noted as painful to get compliant
- **Stripe** — Payment processing for Scott's parking app; supports Apple Pay, Google Pay automatically
- **Claude Managed Agents** — Anthropic's cloud agentic task runner; Scott exploring for client use cases with rubric-based iteration
- **Granola** — AI meeting note-taker Scott used to record and break down the 9-hour Anthropic live stream
- **Fieldy (Fidy)** — AI note-taker with API; Patrick connected it to Hermes with wake-word/termination-word pattern
- **Discord** — Patrick uses it as the interface for Hermes, with separate channels per topic to avoid context overlap
- **Google Clasp** — CLI tool for syncing Google Apps Script; Morgan uses it for Google Workspace automation
- **n8n** — Workflow automation; Scott built a Claude Code skill that ingests n8n documentation so the agent can build nodes correctly
- **Wavespeed** — AI inference provider Juan uses for image-to-image transformation in his photo booth app
- **Stable Diffusion / cDream 4.5** — Image-to-image model Juan uses for photo booth style transformations
- **AWS CloudFront** — CDN with signed URLs used by Juan for secure image delivery in his photo booth app
- **ORGO.ai** — Cloud full-computer-use machines with API; Elijah recommended for running Hermes agents in the cloud
- **Raspberry Pi** — Morgan runs his SignPy lobby display board on one; Juan considering for AI booth
- **Mac Studio / Mac Mini** — Local hardware discussed for running large local models; Tom considering a 6-unit rack
- **NVIDIA DGX Spark** — Mentioned as an alternative to Mac Studio rack for local AI inference
- **tmux (C-Mux)** — Terminal multiplexer Brandon recommends for managing multiple parallel agent sessions
- **CC Usage** — Tool to track Claude token usage; Brandon's team hitting ~$15k/week without subscription
- **Perplexity** — Mentioned briefly by Tom in context of PDF/document research setup
- **Linear** — Issue tracker Adam uses for managing bug tickets
- **Nano Banana** — Image generation tool Scott integrated into Lightwell Board

## links

- **https://github.com/hopchouinard/community-brain-distribution** — Patrick's pre-release Community Brain distribution repo (install via install.md with Claude Code)
- **https://github.com/clara-patchou-ai** — Hermes's own GitHub profile/repo, created autonomously by the agent including graphics
- **https://github.com/openai/codex-plugin-cc** — Official OpenAI Codex plugin for Claude Code; includes adversarial code review, code review, and rescue skills
- **https://github.com/scott-rippey/video-generator** — Scott's video generation repo using Remotion, ElevenLabs, Higgs Field, and FFmpeg
- **https://honcho.dev/** — Memory layer service Patrick added to Hermes
- **https://wavespeed.ai/dashboard** — Juan's AI inference provider for image transformation in the photo booth app
- **https://crows.org/** — Association of Old Crows (DoD/EW professional association); Brandon suggested as a potential customer for Tom's membership database
- **https://anthropic.skilljar.com/claude-code-in-action** — Anthropic Claude Code in Action course/resource (shared by Mitch McCauley in chat)
- **https://www.youtube.com/watch?v=S9EGx6ik-18&t=1924s** — YouTube video shared by Mitch McCauley, directed at Patrick Chouinard
- **https://www.youtube.com/watch?v=QQEgIo4Juxg&list=...** — YouTube video shared by Juan Torres (Bastian's channel reference)
- **https://www.youtube.com/results?search_query=alex+ziskind+mac+studio+rack** — Alex Ziskind's YouTube channel covering Mac Studio rack builds and interconnects
- **https://www.linkedin.com/posts/bethany-lyons-...** — LinkedIn post about patient state machine; Adam shared with Bastian as a potential lead

## decisions

- **Hiral** will restart her vocabulary app using ShipKit's prep phases, referencing her existing specs and mock-up screenshots, and use sequential/parallel LLM calls with structured outputs instead of a monolithic chat approach.
- **Hiral** will use a small/fast model (Gemini Flash or GPT-4o Mini) for word-lookup LLM calls to reduce latency and cost.
- **Patrick** will fully test the Community Brain distribution repo before a wider release and will try a new anonymizer on the chat log tonight.
- **Patrick** will extract his two gigabytes of ChatGPT chat logs, chunk and embed them, and integrate them into Hermes's memory.
- **Brandon** will add the Codex adversarial code review step as the final iteration in his overnight deep-work sessions.
- **Brandon** will try Scott's video-generator repo for personalized cold-outreach video clips.
- **Morgan** will set up Hermes on a VPS server (was in progress on his birthday).
- **Morgan** will look into ORGO.ai as a cloud alternative for running Hermes agents.
- **Scott** will share his developer guide documents (Anthropic Day breakdown, Boris video breakdown, personal process guide) with anyone who emails him.
- **Scott** will share his n8n Claude Code skill (with documentation ingestion) with anyone who requests it via email.
- **Scott** will add Biggi Fraley, Tom Welsh, Alex Wilson, and others to his AI News Digest email list.
- **Scott** will consider adding Google AdSense to the AI News Digest site and research newsletter monetization playbooks (Milk Road, The Hustle, Beehive).
- **Alex Roca** will build a brand-new multi-tenant version of his studio booking app (with organizations as a first-class concept) rather than retrofitting the existing one.
- **Juan Torres** will implement Vercel/AWS log drain with alerting to Slack/email for his photo booth application.
- **Bastian** will keep the group updated on the healthcare center partnership negotiation outcome.
- **Tom Welsh** will investigate the Old Crows Association as a potential customer for his military membership database app.