## general

This coaching call brought together roughly a dozen members of an ongoing AI development community for their regular weekly roundtable. The session was hosted by Paul Miller with Patrick Chouinard co-facilitating, and covered a range of personal projects, tool evaluations, and broader industry observations. The meeting had a casual, show-and-tell format with participants dropping in and out (Ty Wells joined from a golf course mid-round).

Patrick Chouinard led the most substantial technical presentation, demonstrating a "Community Brain" RAG system he built to index and query 68 sessions (approximately 130+ hours) of the community's own coaching call transcripts. He walked through his architecture choices, embedding model comparisons, and retrieval strategies. Juan Torres followed with a live demo of an AI photo-booth application that transforms event photos into stylized AI-generated images, intended for deployment at social events. Morgan Cook presented a Raspberry Pi-based digital signage kiosk system he built over a weekend, designed to push AI-generated HTML slides to displays at venues.

Marc Juretus shared progress on an AI-driven paper-trading investment agent using the Alpaca API, and separately noted challenges with a Microsoft Copilot Studio/ServiceNow integration project at work. Tom Welsh described ongoing work integrating a military association membership system across WordPress, Xero, and Stripe. Adam discussed attending a local OpenClaw meetup and his work integrating Zoho CRM into a SaaS product. The group also had a broader conversation about the shift from Claude Code to Codex, the Superpower framework as a bridge between the two, and AI model regulation concerns raised by Ty Wells.

## insights

- **Pre-processing data is the highest-value step in a RAG pipeline.** Patrick found that chunking and re-embedding cost only $0.75 of a $30 total spend across 68 sessions — the real value is in the pre-processed, cleaned data, not the embeddings themselves.
- **Embedding model choice matters less than data quality.** Patrick tested Nomic 1.5, Nomic 2, and Gemini Embedding V2 and found almost no retrieval gain when the underlying data preparation was solid.
- **Hybrid retrieval (BM25 + vector) outperforms either method alone** for conversational transcript data, according to Patrick's testing.
- **A small local model (GPT-4o-mini/OSS) with strong retrieval infrastructure can reach ~75–80% of a frontier model's quality** at a fraction of the cost and size — Patrick benchmarked GPT-OSS at ~75% of Opus performance on his RAG queries.
- **Gemma 4 excels at function calling and chunk-level summarization but struggles to follow complex retrieval logic**, even at the 30B parameter level (Patrick's finding).
- **Enterprise Claude Code deployment requires configuration hardening**: a `settings.json` at the org level can supersede personal settings, and a seeded `CLAUDE.md` can explain constraints to users rather than just blocking them.
- **Mentioning certain competitor agent names (OpenClaw/Hermes) in a Claude Code session context triggers a switch from subscription mode to API token billing** — a practical gotcha for anyone processing transcripts through Claude Code (Patrick, confirmed in private chat).
- **The Superpower framework now works across Claude Code, GitHub Copilot, and Codex**, making it a viable harness for switching between models without losing workflow structure (Patrick).
- **Claude Code quality appears to be degrading** — Patrick noted Codex was constantly correcting Claude's output in auto-review mode, and Paul Miller reported nearly maxing his $200/month plan with unsatisfying results.
- **A model's default tech stack preferences are effectively the new SEO**: if a technology isn't in the model's training-weighted defaults, it effectively doesn't exist for AI-assisted development (Patrick, referencing the amplifying.ai report).
- **AI security findings (e.g., Claude finding 18-year-old bugs) are often sensationalized**: the compute cost to replicate such runs would exceed enterprise rate limits for any individual user (Patrick).
- **Raspberry Pi kiosk systems can run Chrome in a frameless kiosk mode**, pulling content from a manifest and updating without network dependency for playback — a low-cost, robust digital signage solution (Morgan Cook).
- **QR codes as the interaction layer for display-only kiosks** keep the hardware simple while still enabling user engagement (Morgan Cook).

## qa

**Q (Fitz):** Is anyone still using ShipKit or has something superseded it?
**A (Paul Miller):** I use Claude Superpowers instead. (Tom Welsh confirmed several others mentioned Superpowers the previous week.)

**Q (Fitz):** Hey Patrick, can I assume the data for your RAG is from a community notetaker?
**A (Patrick Chouinard):** It's actually Fathom (the meeting recording/transcription service).

**Q (Juan Torres):** How do you do configuration hardening for Claude Code?
**A (Patrick Chouinard):** You can deploy a `settings.json` at the organizational level that supersedes the personal one. For the pilot, he also included a seeded `CLAUDE.md` that constrained users further but explained the reasons, so they wouldn't try to bypass it.

**Q (Paul Miller):** Have you looked at Gemma 4 yet?
**A (Patrick Chouinard):** Yes — it's great for chunk-level summarization and function calling, but it cannot follow complex retrieval logic even at 30B parameters, performing about half as well as GPT-OSS on that task.

**Q (Morgan Cook):** Is the Raspberry Pi kiosk a touchscreen?
**A (Morgan Cook):** No — it's display-only, meant to be mounted 10–15 feet up. Interaction happens via QR codes that link to external URLs.

**Q (Juan Torres):** Have you thought of utilizing touchscreens with your kiosk setup for data input or forms?
**A (Morgan Cook):** The device is intentionally display-only. Any interaction is handled through QR codes; the kiosk itself has no input capability.

**Q (Adam):** The Zoho CRM MCP — is that for development or for getting at customer data?
**A (Paul Miller):** More for development, but it exposes quite a lot. The main challenge is token limits on what you can pull through the API. Recommended starting with the API first.

**Q (Tom Welsh):** Does anyone have recommendations for AI app development books, preferably on Audible?
**A (Patrick Chouinard, via live RAG query):** After querying the community brain database, no books specifically covering AI development were ever mentioned in the coaching calls. The only books referenced were *12 Months to $1 Million*, *The War of Art*, and *Building a Second Brain* — none of which are AI development guides. Paul Miller suggested using Patrick's search app to find what has been discussed on the topic over the past year.

**Q (Paul Miller):** Is the Codex plugin for Claude Code stable?
**A (Patrick Chouinard):** He's been running it in auto-review mode — every coding iteration gets sent to Codex for review, corrections are applied, and it loops until clean. It's been his current harness, though it revealed that Claude was wasting tokens being repeatedly corrected by Codex.

## tools

- **Claude Code** — Primary AI coding tool being used by Patrick and others; enterprise deployment with configuration hardening discussed
- **Codex (OpenAI)** — Being evaluated/adopted as an alternative to Claude Code; has a $100/month mid-tier plan; discussed as having more generous limits
- **Claude Superpowers** — Framework/harness that works across Claude Code, GitHub Copilot, and Codex; discussed as the SDD framework being deployed at Patrick's workplace
- **OpenWebUI** — Local container UI Patrick uses to run his Community Brain RAG system, connected to a local Ollama instance
- **Ollama** — Local model runner used by Patrick for embedding and inference
- **Nomic Embed (1.5 and 2)** — Embedding models tested by Patrick for the RAG pipeline
- **Gemini Embedding V2** — Google embedding model tested by Patrick; found minimal gain over Nomic with good data prep
- **Gemma 4 (including 30B)** — Used by Patrick for chunk-level summarization; poor at complex retrieval logic
- **BM25** — Keyword search component of Patrick's hybrid retrieval system
- **LanceDB** — Vector database Patrick is using for the Community Brain; plans to share packaged version
- **ChromaDB / Pinecone** — Alternative vector databases mentioned as targets for community members who want to re-embed Patrick's prepared data
- **Open Router** — Used by Patrick to access multiple models during pre-processing
- **Sonnet 4.6** — Used by Patrick for pre-processing full transcripts; noted as currently slow
- **Kimi 2.5** — Used alongside Sonnet for pre-processing large transcript contexts
- **Fathom** — Meeting transcription/recording service; source of all historical transcript data for Patrick's RAG
- **Alpaca API** — Paper trading API Marc is using; provides $100K simulated funds for agent testing
- **Microsoft Copilot Studio** — Marc's work project; building a ServiceNow-connected agent
- **ServiceNow** — Connected to Copilot Studio agent; incident submission works out of the box, request submission does not
- **SharePoint** — Connected to Copilot Studio agent; experiencing 6-second context lag
- **Azure AI Search** — Proposed solution to the SharePoint lag issue in Marc's project
- **Zoho CRM** — Adam integrating it into his SaaS product; Paul noted it has a usable MCP and API
- **Zoho Helpdesk** — Paul built a Claude-powered reporting system to analyze ticket quality and customer behavior patterns
- **Clerk** — Authentication provider used by Juan for his AI photo-booth app
- **AWS EC2** — Juan's current hosting for the staging environment of his photo-booth app
- **AWS CloudFront** — Handling front-end egress for Juan's app
- **Raspberry Pi** — Morgan's hardware platform for the digital signage kiosk system
- **Chrome (kiosk mode)** — Browser Morgan uses on the Pi, running frameless/skinless for display
- **Lightpanda** — Suggested by Bastian as a Playwright alternative using Zig, no graphical rendering, ~1/10th the memory; potentially useful for Raspberry Pi automations
- **Playwright** — Browser automation tool; Lightpanda raised as a lighter alternative
- **WordPress** — Tom's military association website runs on it; exploring WordPress APIs
- **Xero** — Accounting system in Tom's membership integration; Stripe pushes payments to it
- **Stripe** — Payment processor for Tom's military association; feeds into Xero
- **T3 Code** — Used by Bastian with Codex for remote development work
- **Tailscale** — Mentioned by Bastian as a common way to connect to remote Claude/Codex instances
- **Kindle Direct Publishing** — Morgan helping a client publish a book through it
- **Google Apps Script** — Morgan working on automation for the foundation project
- **Crowdpics.ai** — Ty Wells shared this as a similar/related project to Juan's photo-booth app (Ty built it last year)

## links

- **https://www.atapworldwide.org/** — ATAP (Association of Talent Acquisition Professionals) shared by Andrew Nanton as a potential client networking resource for Ty Wells
- **https://fathom.video/users/sign_in** — Fathom meeting transcription service; source of Patrick's RAG training data
- **https://fathom.video/customize** — Fathom settings customization page (shared by Fathom notetaker bot)
- **https://lightpanda.io/** — Lightpanda browser: Playwright alternative written in Zig, no graphical rendering, ~1/10th memory usage; shared by Bastian Venegas
- **https://github.com/lightpanda-io/browser** — GitHub repo for Lightpanda browser; shared by Bastian Venegas
- **https://amplifying.ai/research/claude-code-picks/report** — Report on Claude Code's preferred/default tech stack choices across categories (auth, observability, email, etc.); shared by Patrick Chouinard
- **https://crowdpics.ai** — Ty Wells' previously built event photo app; shared as a comparable project to Juan's AI photo-booth

## decisions

- **Patrick Chouinard** will package the Community Brain RAG system (LanceDB vector database + raw prepared material + deployment instructions) for community members to download and use, targeting completion by next week's session.
- **Patrick Chouinard** will add a pre-processing step to remove competitor agent name references from transcripts before passing them to Claude Code, to avoid triggering API token billing mode.
- **Patrick Chouinard** is planning to cancel his Claude Max subscription and switch to the $100/month Codex tier, given Superpower now provides equivalent harness functionality on Codex.
- **Paul Miller** committed to switching to Codex to resolve a nav map bug that Claude Code has been unable to fix after four days.
- **Paul Miller** will reinstall the Codex plugin for Claude Code and attempt to resolve the loading error he encountered.
- **Morgan Cook** will share his Raspberry Pi kiosk setup scripts and ISO duplication process with Juan Torres and Paul Miller for their respective use cases (event display and conference screens).
- **Juan Torres and Morgan Cook** agreed to connect on LinkedIn to continue the conversation about integrating the kiosk display system with Juan's photo-booth app.
- **Paul Miller** will DM Morgan Cook about using the Raspberry Pi kiosk system for the conference he sponsors.
- **Patrick Chouinard** will gather real-world data on Superpower's usability at scale in a constrained corporate environment, given the enterprise Claude Code pilot with 100 users is now live.