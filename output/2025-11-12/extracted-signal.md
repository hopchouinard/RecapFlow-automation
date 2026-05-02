## general

This was a weekly group coaching call for an AI/software development community, hosted by Brandon Hancock. The session opened with casual weather conversation among participants from Quebec, Georgia, and Mexico before moving into structured member updates. Brandon briefly demoed a work-in-progress "worker SaaS" product built on Next.js, Supabase, and Trigger.dev that processes video uploads, transcribes them via Whisper, and enables AI-powered chat with the content.

Members took turns sharing project updates and receiving feedback. Alex Rojas discussed a client project for a car last-mile delivery company, pivoting from a hardware/computer-vision arc to a software-first approach using YOLO v8 models run on phones and a Next.js/Supabase stack. Patrick Chouinard demonstrated an AI-powered daily news aggregation pipeline built entirely in Bash using Gemini CLI, with an Astro frontend and a public GitHub repo. Juan Torres shared progress on an AWS-hosted AI solution using an 8B parameter model for vendor name extraction. Other members covered topics including contract/IP strategy, code review tooling, security scanning SaaS, WhatsApp API integration for a GCP-backed coffee farm client, image generation for mini-home configurators, and N8N workflow debugging.

The call also touched on interview preparation resources (AlgoExpert, NeetCode), the Trigger.dev platform as a replacement for N8N in complex pipelines, and the Gemini CLI's ability to run hundreds of parallel search agents cheaply. Brandon credited Patrick for inspiring an upcoming video and podcast segment on Gemini CLI search workflows.

## insights

- **Always start with the dumbest, simplest solution** before building complex AI pipelines — Brandon lost two days over-engineering something a co-founder solved trivially. Ask "what would I do if AI didn't exist?"
- **Bounce pricing and scope off peers before committing to a client** — Alex underpriced a hardware+software hybrid by roughly 2x; a second opinion would have caught it early.
- **Transparency with clients about scope mistakes builds trust** — Alex's honest "I screwed up, here's the revised plan" was received positively and kept the deal alive.
- **Gemini CLI can run as hundreds of parallel agents simultaneously**, each with Google search access, making it extremely powerful for fan-out research tasks (e.g., find every ambulance company in every U.S. city for ~$20).
- **Force Gemini CLI to use 2.5 Flash, not 2.5 Pro**, for search-heavy pipelines — Pro is slower and burns through quota much faster (Patrick Chouinard).
- **Local/on-device models are slower and less capable than cloud APIs**; prefer cloud APIs (e.g., Gemini video/image models) unless privacy is a hard requirement.
- **For image/video AI tasks, generate multiple outputs and have AI pick the best one** to compensate for non-determinism, rather than showing the user a single potentially flawed result.
- **Background IP clauses are the most critical contract element** for freelance developers — ensure your reusable code/frameworks are explicitly carved out (Jake Maymar).
- **Don't sign contracts under pressure** — clients pushing "just sign it so we can move forward" is a red flag; sleep on it (Jake Maymar).
- **When a client wants to transfer or sell IP, say yes but at a cost** — frame it as a transfer fee rather than a flat refusal (Jake Maymar).
- **Prompting an LLM with the right context (e.g., "I am the contractor") changes the lens** of contract review outputs (Jake Maymar).
- **Asking AI "is there a better way to do this?" before accepting a large code change** can surface dramatically simpler solutions (Hemal Shah, validated by Brandon).
- **CodeRabbit's strategy of leaving persistent comments (even poems) in repos** is effective infinite marketing — developers keep seeing the brand long after trials end.
- **Trigger.dev is preferable to N8N for complex multi-step pipelines** — N8N's logging and parallel execution limits become painful at scale.

## qa

**Q (Jake Maymar):** If I already have a RAG setup with WebSockets and Supabase real-time subscriptions, is it easy to migrate to Trigger.dev, or should I start over?
**A (Brandon Hancock):** Trigger.dev is great when the events originate inside Trigger (e.g., file upload → parse → images). For your case, since you're already writing to the database and reading from it via sockets, that's probably good enough — don't change it. Use Trigger.dev in phase two when things get more complex.

**Q (Jake Maymar):** Is there a meaningful difference between Resend and Mailgun for transactional email?
**A (Brandon Hancock):** Not really for simple use cases. Mailgun works fine for "event happened → send email," which covers both customer confirmations and internal alerts. If your needs are that straightforward, either works.

**Q (Jake Maymar):** What's the best WYSIWYG/markdown editor for a forum-style app?
**A (Brandon Hancock):** Tiptap — it's the most capable, supports real-time collaboration, AI injection, highlighting, and essentially anything you'd want to do.

**Q (Alex Rojas):** What template/format should I use for the client proposal, and what contract terms should I watch for?
**A (Jake Maymar):** Use Claude with a prompt that specifies "I am the contractor." Keep the contract as short as possible while retaining legal protections. The key clause is background IP — make sure your reusable code is carved out. If they want to transfer IP to a new product, charge for it. Don't sign under pressure.
**A (Brandon Hancock):** Happy to share my last contract template directly — just email me.

**Q (Ana P):** How secure is WhatsApp for transmitting business data from a GCP-hosted AI agent?
**A (Ty Wells):** WhatsApp is end-to-end encrypted for message content; only metadata (who you're talking to, when) is exposed. The content itself is not visible server-side.
**A (Juan Torres):** You can also restrict how your GCP server communicates with the WhatsApp API at the code/network level, enforcing HTTPS/SSL for compliance.
**A (Brandon Hancock):** Simplest security layer is a whitelist of approved phone numbers that can interact with the agent.

**Q (Juan Torres):** What security vulnerabilities does Ty's scanning app test for?
**A (Ty Wells):** OWASP Top 10 plus custom checks, run on AWS Lambda. Currently also validates basic functionality: login, Google auth, email/password auth, scan execution, and returns a vulnerability report with remediation prompts.

**Q (Mario Polanco):** How would you approach building a home configurator where clients can pick finishes/colors for mini homes?
**A (Brandon Hancock):** Level 1 — take an image and pass a prompt to an image editing model (Gemini Imagen/Nano Banana) and see if it works. Level 2 — generate four variations, have AI pick the best one. Level 3 — loop: generate, grade, decide if it needs another pass. Start with level 1 for the demo. The Gemini image editing docs cover ~80% of what you need.

**Q (Hemal Shah):** Have you tried Cursor CLI for CI/code review pipelines, and how does it compare to other CLIs?
**A (Brandon Hancock):** Haven't used Cursor CLI in the cloud — background agents fought me hard. Whatever prompt you build is model-agnostic, so also try Gemini CLI (free, up to 1,000+ requests/day) as a second check in the same pipeline.

## tools

- **Trigger.dev** — Brandon's core pipeline tool for async video processing, transcription, and AI summaries; recommended as N8N replacement
- **Supabase** — used as blob store, database, and real-time subscription layer across multiple member projects
- **Next.js** — frontend/backend framework used by Brandon's SaaS demo and Alex's car inspection app
- **Whisper** — used inside Trigger.dev pipeline to transcribe chunked audio from uploaded videos
- **Gemini CLI** — Patrick's tool for running hundreds of parallel AI search agents via Bash scripts; Brandon expanding into fan-out research patterns
- **Gemini 2.5 Flash** — recommended model for Gemini CLI search pipelines (faster, cheaper than Pro)
- **Gemini Imagen / "Nano Banana"** — Google's image generation/editing model; recommended for Mario's home configurator and discussed for Alex's car damage detection
- **RoboFlow** — platform Alex planned to use for training YOLO v8 car damage detection model
- **YOLO v8** — object detection model Alex is training for aesthetic car damage identification on mobile phones
- **Astro** — static site framework Patrick used for the frontend of his AI news aggregation site
- **N8N** — workflow automation tool Mitch is using for video generation pipelines; hitting parallel execution and logging limits
- **CodeRabbit** — AI code review tool Hemal tested; noted as expensive for large teams, but praised for its persistent in-repo marketing strategy
- **Cursor** — primary IDE used by most members; Hemal exploring its CLI for GitHub Actions code review pipelines
- **Gemini CLI (code review use)** — Brandon suggested as a free alternative/complement to Cursor CLI for automated code review prompts
- **Claude** — used by Jake for contract drafting and review with contractor-perspective prompting
- **ChatGPT** — Rod used it for Mexico market rate research; Mitch used it with Canva integration for pitch decks
- **Canva (ChatGPT integration)** — Mitch demoed creating pitch decks via voice note → ChatGPT → Canva; noted as impressive
- **Warp** — terminal used by Morgan; noted for AI-assisted PowerShell command generation and built-in file editor
- **Ollama** — local model runner Patrick's Terminal Intelligence scripts use for shell-command assistance
- **AlgoExpert** — Brandon's top recommendation for data structures, algorithms, and systems design interview prep
- **NeetCode** — secondary recommendation for coding interview practice
- **HeyGen** — AI avatar platform Mario is using for cloning course creators; recently added knowledge base and live Zoom integration
- **Mobin** — UI inspiration SaaS (~$20/month) with high-res PNG screenshots of mobile/web apps, useful for component generation prompts
- **21st.dev** — UI component inspiration tool mentioned in context of Ty's security scanning app UI
- **GitHub Copilot CLI** — Patrick is developing a course on it; noted for sub-agent support similar to Claude Code, with Agent HQ coming
- **Mailgun** — email service Brandon uses for transactional and internal alert emails
- **Resend** — email alternative Jake is evaluating; Brandon sees no major functional difference for simple use cases
- **Tiptap** — recommended WYSIWYG/markdown editor for Jake's forum; noted as most capable with collaboration and AI features
- **Tmux** — mentioned as a tool Mitch used for split-window terminal workflows inside Warp
- **Make (Integromat)** — referenced for comparison; has on-exception/catch nodes that N8N may lack
- **AWS Lambda** — Ty's security scanning app runs on Lambda to avoid directly touching scanned sites
- **BigQuery / GCP ADK** — Ana's planned stack for the coffee farm client's data querying agent
- **WhatsApp Business API / Meta for Developers** — Ana is integrating for the coffee farm stakeholder chatbot

## links

- **Patrick's AI news aggregation site** — public static site showing daily AI research reports with IDE-like source viewer (URL shared verbally, not captured in transcript)
- **Patrick's GitHub repo (AI news pipeline)** — public repo for the Bash + Gemini CLI + Astro pipeline (shared in chat during call, URL not captured in transcript)
- **Patrick's "Terminal Intelligence" repo** — shared in chat; Bash scripts and aliases for querying a local Ollama model as a shell-command assistant
- **Ty's security scanning app** — link dropped in chat by Ty; allows free scanning of two repos for OWASP and custom security vulnerabilities
- **Gemini image editing documentation** — Brandon referenced a single-page doc covering ~80% of image editing API usage; shared during Mario's segment (URL not captured)
- **Mobin** — https://www.mobin.design (referenced by Bastian for UI inspiration; exact URL not confirmed in transcript)
- **AlgoExpert** — https://www.algoexpert.io — Brandon's top recommendation for interview prep, mentioned he has purchased it three times
- **Clement's YouTube channel (AlgoExpert founder)** — referenced by Bastian/Brandon as a high-quality resource for algorithms content (URL not captured)

## decisions

- **Brandon** will create a shared GitHub repository for the ShipKit community to contribute code, targeting Thursday for setup and invites
- **Brandon** will send Alex his last contract template via email as a starting reference
- **Brandon** will record a deep-dive video on Gemini CLI search workflows, crediting Patrick Chouinard, followed by a Google podcast-style segment in November
- **Brandon** will finalize the Trigger.dev worker SaaS template (including setup scripts and test templates) and release it to members by Sunday
- **Alex Rojas** will proceed with a software-first approach for the car inspection client: YOLO v8 model trained in RoboFlow, running on operator phones, with photos pushed to Supabase via a Next.js app
- **Alex Rojas** will use AI docs to write a detailed proposal/spec before finalizing the client agreement
- **Hemal Shah** will explore Gemini CLI as a free parallel option alongside Cursor CLI for the GitHub Actions code review pipeline, and will report findings back to the group
- **Hemal Shah** will keep Brandon posted on Cursor CLI pipeline results
- **Patrick Chouinard** will consider starting a YouTube channel, potentially using AI-generated avatar content to publish at scale without being on camera
- **Mario Polanco** will start with a single image + prompt proof-of-concept using Gemini image editing API before committing to the home configurator contract
- **Juan Torres and Alex Rojas** will connect offline to discuss vision model options for Juan's potential construction-sector lead
- **Mitch** will investigate whether switching from N8N to Trigger.dev resolves the parallel execution and logging issues in his video generation pipeline
- **Ana P** will research WhatsApp end-to-end encryption details and GCP network-level security controls before proceeding with the coffee farm WhatsApp integration