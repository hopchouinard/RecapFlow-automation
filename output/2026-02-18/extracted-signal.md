## general

This was a weekly community coaching/peer-learning call hosted by Paul Miller (filling in for the regular host Brandon, who was occupied with an EMS development project). Patrick Chouinard had hosted the previous two weeks. The call followed a round-robin format where each participant shared what they had built or shipped that week, what blockers they encountered, and any insights worth sharing with the group.

Topics ranged from technical demonstrations — Patrick's news pipeline admin dashboard, Scott's Claude Code mobile interface, Ty's hallucination-detection tool (Lucid), Ana's Congressional trading tracker, and Morgan's cemetery management system — to broader discussions about AI model developments (Claude Sonnet 4.6, OpenClaw's creator joining OpenAI), security concerns around agentic systems, and business development strategies for freelance AI engineers.

The group also had a substantive side conversation about repository management: how to cleanly separate licensed ShipKit code from a client-shared codebase, with solutions proposed around dual GitHub repos, `.gitignore` discipline, and packaging Claude artifacts as NPM packages. The call closed with warm discussion about the value of the community itself, which the regulars described as one of the most useful recurring calls they attend.

## insights

- **Prompt injection is a real risk with email-connected agents**: if an agent reads email without filtering rules (e.g., "only process email from myself"), a malicious sender can embed instructions that the agent will execute. (Patrick Chouinard)
- **Prefer deterministic pipelines over agents wherever possible**: Patrick's news pipeline uses Brave for search results and Perplexity Sonar Pro for enrichment — no agentic layer — because deterministic steps are more reliable and cheaper. Add agentic behavior only where it genuinely adds value.
- **Prototype with Claude Code, ship with the Agent SDK**: Patrick's workflow is to build and iterate quickly in Claude Code, then convert the stable result into a production Claude Agent using the Anthropic Agent SDK.
- **Use NPM packages to distribute Claude artifacts (skills, hooks, primers)**: packaging Claude Code skills as NPM dependencies makes them easy to install, version, and — critically — remove from a project without polluting Git history.
- **Dual-repo pattern for licensed code**: maintain a private repo with full history (including licensed/proprietary tooling) and a public/client-facing repo that receives clean, history-stripped pushes via a script. Claude Code can write that sync script.
- **The `/insights` slash command in Claude Code** analyzes the last month of usage, surfaces workflow recommendations, and can auto-generate skills or hooks to improve your setup. (Patrick Chouinard — described as a "knowledge bomb")
- **Walking away from broken code is often the right move**: the brain continues working on problems subconsciously; returning fresh often solves what hours of tired debugging cannot. A practical heuristic: three Ctrl-Z's and you're done for the night. (Marc Juretus)
- **Rewriting lost code often produces a better result**: the second attempt benefits from knowing what didn't work, leading to a cleaner, faster implementation. (Morgan Cook)
- **Business development: do what's authentically you**: cold calling, cold email, in-person networking, and video content all work — but only if you're comfortable with the medium. Forcing an unnatural channel produces poor results. (Scott Rippey)
- **OpenClaw went viral before it was ready for general use**: the security and configuration complexity was not communicated, leading to widespread misconfigurations. The concept is directionally correct, but the release was premature. (Scott Rippey)
- **Current LLMs are fundamentally predictive (transformer-based), not AGI**: the hype around model releases often outpaces actual capability jumps; improvements are real but incremental. (Scott Rippey)
- **AI adoption lags most in large, slow-moving organizations** (hospitals, government): small, agile businesses adopt faster. The bottleneck is mindset and change management, not technology. (Paul Miller)

## qa

**Q (Juan Torres):** Is Brave Search better than Tavily for news generation?
**A (Patrick Chouinard):** They serve different purposes. Tavily is more like Perplexity — it writes AI-generated output. Brave is used purely as a Google-style search: give it a subject, get back URLs and brief excerpts. That's all Patrick needs before handing the links to Perplexity Sonar Pro for full article enrichment. Using Brave's free plan keeps costs low.

**Q (Juan Torres):** What agentic system is driving Patrick's news pipeline?
**A (Patrick Chouinard):** None, intentionally. The pipeline is deterministic: a list of subjects → Brave (find sources) → Perplexity Sonar Pro (write enriched article). The only "agentic" element is the feedback loop — upvoting/downvoting articles — which over time adjusts which subjects are searched and which sources are trusted.

**Q (Morgan Cook):** What's the best way to structure a project so that licensed ShipKit code (skills, Claude artifacts) can be shared with collaborators without exposing the licensed material or its Git history?
**A (Scott Rippey / Patrick Chouinard / Bastian Venegas):** Several approaches: (1) Use a dual-repo setup — private repo retains full history; a script (Claude Code can write it) pushes to a public repo with no version history. (2) Use `.gitignore` to exclude documentation/AI folders from the shared repo. (3) Package the licensed Claude artifacts as an NPM dependency — easy to install and easy to remove, and it keeps the licensed code isolated from the project's own Git history.

**Q (Paul Miller):** Have you tried Tailscale instead of Cloudflare Tunnel for securing the Claude Code mobile interface?
**A (Scott Rippey):** Tailscale is a VPN; Cloudflare Tunnel creates an HTTPS tunnel — different approaches. Scott chose Cloudflare because he didn't need a full VPN and wanted HTTPS access. Both are valid; Tailscale is useful for team environments with multiple servers.

**Q (Juan Torres):** Is this mobile Claude Code interface actually used for development, or just for capturing ideas?
**A (Scott Rippey):** Both. Scott uses it to start building when away from his computer — drafting PRDs on his phone and then kicking off Claude Code to begin scaffolding. He always finishes on his desktop, but the mobile interface lets him capture momentum when an idea strikes.

**Q (Ty Wells):** Does Lucid work only against a GitHub repository, or can it evaluate code in real time during generation?
**A (Ty Wells):** It runs via CLI during code generation — evaluating, identifying hallucinated sections, and rewriting them before delivering the final output. There's also a web interface at trylucid.dev where you can paste any function and check it manually.

**Q (Juan Torres):** Have you had issues with Yahoo Finance's open-source library changing and breaking your code?
**A (Ana P):** Somewhat — the data is incomplete, especially for mutual funds, and the library is not perfectly stable. However, Ana is only extracting industry classifications and a small subset of metadata, so the exposure is limited. It's free, which justifies the trade-off for a personal project.

## tools

- **OpenClaw** — Agentic assistant framework; Marc set it up on a Google Cloud VM; Patrick used it to scaffold his news pipeline; creator recently hired by OpenAI
- **Claude Code** — Primary coding agent used by most participants for prototyping and production work
- **Anthropic Agent SDK** — Patrick uses it to convert Claude Code prototypes into production agents
- **Perplexity Sonar Pro** — Used by Patrick for article enrichment (writing full articles with citations from a URL)
- **Brave Search API** — Used by Patrick as a low-cost search layer to find source URLs for given topics
- **Cloudflare Tunnel** — Used by Scott to securely expose his Claude Code mobile interface over HTTPS
- **Tailscale** — Mentioned by Paul and Juan as a VPN alternative for securing self-hosted services
- **Google Cloud (GCP / Cloud Run)** — Marc runs OpenClaw on a GCP VM; Ana deployed her Congressional trading tracker on Cloud Run
- **Cursor** — Tom's primary coding environment; he has not yet switched to Claude Code
- **ShipKit** — Brandon's licensed toolkit (skills, Claude artifacts); Morgan's project uses it and needs to be separated before sharing
- **GoCardless** — Tom evaluated it for direct-debit subscription payments for a military regiment site; lower fees than Stripe for high volumes
- **Stripe** — Mentioned by Tom as the fallback for one-off donations where GoCardless (direct debit only) doesn't fit
- **Quiver Quants API** — Ana uses it to pull US Congressional stock disclosure data for her investment tracker
- **Yahoo Finance** — Ana uses it to enrich ticker data (industry classifications) in her Congressional trading app
- **D3.js** — Morgan uses it for hierarchy diagrams in the cemetery management system
- **GeoJSON / JSON-GIS** — Morgan is importing GIS plot boundary data into the cemetery system
- **Apify** — Recommended by Scott and Paul for web scraping (e.g., supermarket pricing for Ana's meal planner); has pre-built actors
- **Lucid (trylucid.dev)** — Ty's own tool for detecting and correcting hallucinated code during LLM generation; patent pending
- **NPM** — Patrick proposed packaging Claude artifacts as NPM packages for clean distribution and removal
- **Netlify** — Mentioned by Scott as an alternative deployment option for the Claude Code mobile interface
- **Claude Desktop** — Scott uses it with MCP for PRD (product requirements document) creation
- **OpenRouter** — Patrick uses it as part of his news pipeline; budget tracked in the admin dashboard
- **Jobs API (Indeed-sourced)** — Marc connected it to OpenClaw to fetch job listings by title and email results

## links

- **Patrick's security hardening guide for OpenClaw/self-hosted agents** — Patrick shared a link in chat (URL not captured in transcript) documenting steps he took to secure his own instance
- **trylucid.dev** — Ty's hallucination-detection tool with benchmark results and a live code-checking interface
- **Scott's Claude Code Mobile GitHub repo** — Public repo shared in chat; includes setup instructions for Google login, Cloudflare Tunnel, and environment variables (exact URL not captured)
- **Scott's "Build a Better Voice" brand-voice framework** — A prompt/file Scott offered to share in chat; helps AI systems learn a user's authentic writing voice through a ~45-minute guided session

## decisions

- **Patrick** will publish a meeting summary to the community (School platform).
- **Paul** will try to add resource links mentioned during the call into the video description/comments for viewers who don't have chat access.
- **Scott** will share his "Build a Better Voice" brand-voice framework prompt in the group chat.
- **Scott** will continue updating the public Claude Code Mobile GitHub repo as he fixes issues (background reconnection, browser session persistence).
- **Ana** will reach out to Patrick for nutrition/fitness feedback on her MIND diet meal planner app ("Mindy").
- **Ana** will look into Apify for scraping supermarket pricing data for the grocery optimization feature of her meal planner.
- **Ana** will consider adding historical performance charts (candlestick/time-series) to her Congressional trading tracker, per suggestions from Tom and Juan.
- **Ty** will message Brandon to ask about a contact (Maxim) who may be able to serve as an academic endorser for Ty's arXiv paper on Lucid.
- **Ana** will connect Ty with her contact (PhD in Electrical Engineering and Image Processing) who may be able to endorse Ty's academic paper.
- **Juan** will explore creating YouTube content focused on AI ops / cloud deployment (EC2, middleware, LLM deployment) as a niche content and client-acquisition strategy.
- **Patrick and Scott** will schedule a one-on-one (they have been trying for weeks and keep missing each other).
- **Brandon** is expected to return as host next week.