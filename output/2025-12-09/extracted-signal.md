## general

This was a coaching/community call for ShipKit members, hosted by Brandon Hancock. The session followed a round-robin format where participants shared project updates and asked questions. Brandon opened with a personal update about being accepted into TinySeed and a passport emergency that disrupted travel plans.

The call covered a wide range of projects: Patrick Chouinard's work on enterprise AI platform evaluation and a custom GPT for template selection; Scott Rippey's personal AI morning-summary agent with parallelized sub-agents; Ryan C's social media automation SaaS with AI image editing; Maksym Liamin's WhatsApp-based automotive RAG and voice agents for Nissan, Mazda, and Infinity; George Kurian's plans for compliance/audit automation; Ty Wells' kiosk platform rebuild, predictive analytics SaaS, remote coding agent on a VPS, and a Fire Stick photo-display gift project; and Tiran Dagan's portfolio of tools including a resume analyzer, emergency preparedness planner, consulting report generator, trip planner, and a Picasa-style photo gallery.

Discussion threads included agentic workflow patterns (generator-evaluator loops, parallelization), voice agent model selection, LinkedIn outreach strategy for B2B enterprise sales, local model recommendations, SOC 2 / CASA 2 certification processes, and ShipKit onboarding improvements.

## insights

- **Patrick Chouinard:** Claude Code outperforms Gemini CLI for web search + scraping research pipelines because it can mix web search and web fetch (scraping) in the same workflow. It costs more but produces better results.
- **Patrick Chouinard:** In enterprise AI agreements, you buy a shared token pool across all users rather than per-seat limits, and enterprise versions include tools and assets not present in public versions. Binding to a single provider long-term is risky given the pace of market change.
- **Brandon Hancock:** The generator-evaluator agentic loop (worker generates → evaluator scores pass/fail → feedback loops back) is a reliable pattern for producing high-quality outputs on nebulous tasks, at the cost of speed.
- **Scott Rippey:** Splitting a large monolithic agent call into parallel sub-agents with their own context windows reduces timeout and context-overflow problems, not just latency.
- **Scott Rippey:** Providing a screenshot of a desired workflow pattern (e.g., from Trigger.dev) as visual context when prompting Claude Code is an effective way to communicate architecture intent.
- **Brandon Hancock:** The "service before software" approach — validating a service manually first, then automating it — is the textbook SaaS path and reduces risk significantly (Ryan C's social media agency is cited as the example).
- **Brandon Hancock:** For enterprise B2B, consistent LinkedIn connection-building over a year (20 invites/day, posting as a thought leader, no immediate sales pitch) is a high-ROI long-game strategy.
- **Tiran Dagan:** Feeding an existing PRD into ShipKit's prompts and having the AI answer the framework questions on your behalf (rather than answering them yourself) can surface surprising and valuable new directions.
- **Brandon Hancock:** Creating a Claude command (e.g., `git workflow commit`) that fires in a background terminal window makes committing frictionless and preserves rollback ability without interrupting flow.
- **Maksym Liamin:** Voice agent model selection is a hard trade-off: smarter models have too much latency; fast models can't reliably do tool calls. Kimi K2 is currently used in production for this balance.
- **Ty Wells:** Running four parallel Claude Code projects with sub-agents simultaneously can burn through $300 in a single evening — but the output volume justifies it if the work is well-planned.
- **Brandon Hancock:** Planning upfront (PRD, task artifacts, code-change plans) pays compounding dividends; diving straight into coding leads to context-window exhaustion and hallucination loops at the 50% mark.
- **Patrick Chouinard:** A "horizontal" research pipeline (wide coverage of many topics daily) is the inverse of deep research and is well-suited to tracking a fast-moving market like AI providers.

## qa

**Q (Elijah):** When setting up ShipKit, do you have to use Cursor, or can you use another IDE like VS Code or Windsurf?
**A (Brandon Hancock):** The `cursor .` command just opens the folder in Cursor — it's not doing anything magical. You can open the same folder in any editor manually. Currently 90% of the work is done in Claude Code (terminal), with Windsurf used ~10% of the time for visual/UI tasks using Gemini 2.5 Pro.

**Q (Brandon Hancock):** Scott, what did you do when parallel agent outputs risked exceeding the context window?
**A (Scott Rippey):** Added hard constraints in the prompts (e.g., only look back 7 days, only use meeting summaries not full transcripts, only scan knowledge base titles unless relevant). Splitting into separate parallel calls also gives each sub-agent its own context window, dramatically reducing the risk.

**Q (Brandon Hancock):** Maxim, for voice agents, what's the model you're using and what's the latency trade-off?
**A (Maksym Liamin):** Currently using Kimi K2 in production — GPT models were too slow as of June. The core trade-off is that smarter models have too much latency (~40ms target), while fast models fail at tool calls. Ty Wells added that GPT-4o mini on ElevenLabs achieves ~45ms with reliable tool calls.

**Q (Patrick Chouinard):** Have you considered selling the CV Refinery tool to consulting firms, who spend enormous time reformatting CVs for RFP submissions?
**A (Tiran Dagan):** Loved the idea — coming from consulting, he confirmed the pain is real. The use case is consuming the client's RFP requirements and automatically selecting and presenting the matching CV content in the required format. Called it a "different league" opportunity.

**Q (Maksym Liamin):** Do you know anything about CASA Tier 2 certification from Google (required for OAuth scopes with restricted permissions)?
**A (Brandon Hancock):** Not familiar with CASA 2 specifically, but the analogous process for SOC 2 uses platforms like Vanta (~$7k) plus an auditor (~$7k). SOC 1 is a point-in-time audit; SOC 2 requires six months of continuous monitoring logs. Ryan C added that some findings can be formally accepted/indemnified rather than fixed, saving time and cost.

**Q (Brandon Hancock):** Tiran, do you think AI will disrupt consulting on the thinking/planning side, the deliverable side, or the whole process?
**A (Tiran Dagan):** Both — the report generation (research + analysis) and the deliverable production (converting markdown to interactive HTML dashboards) are both being automated. The human consultants bring domain expertise and client relationships; AI handles the data overlay, market research, and presentation layer.

## tools

- **Claude Code** — Primary agentic coding environment used by most participants; also used for parallel research pipelines and remote VPS-based coding agents
- **Gemini CLI** — Used for parallel web-search research pipelines; Patrick found Claude Code superior for mixing search + scraping
- **Windsurf (Windsurf IDE / "Anti-Gravity")** — Used by Brandon ~10% of the time for visual/UI tasks with Gemini 2.5 Pro; has built-in memory/learning about coding style
- **Trigger.dev** — Referenced as a visual example of parallelization and generator-evaluator loop patterns for agentic workflows
- **Anthropic TypeScript SDK** — Scott's agent app is built directly on this (not Vercel AI SDK or the agent SDK)
- **Vercel AI SDK** — Mentioned as an alternative for parallel `generateText` calls without streaming complexity
- **ElevenLabs** — Used by Ty for voice playback in his remote coding agent; Ty uses GPT-4o mini on ElevenLabs for ~45ms latency with tool calls
- **Kimi K2** — Maksym's current production voice agent model; chosen for latency/tool-call balance
- **GPT-4o mini** — Ty's recommendation for voice agents on ElevenLabs balancing latency and tool calls
- **GPT Realtime API** — Carlos mentioned it as OpenAI's recommended model specifically for voice use cases
- **N8N** — Scott uses it for customer back-end automations but not in his personal agent app
- **Supabase** — Standard database/auth/blob store in ShipKit stack; Tiran uses it for photo caching
- **Netlify** — Deployment platform used by Scott and Ryan
- **Cloudflare R2** — Ryan uses it as a media bucket to avoid overloading Supabase storage
- **Google APIs (Gmail, Calendar, Drive)** — Scott's agent app pulls emails, meetings, and tasks directly via Google APIs
- **WhatsApp Business API** — Maksym's automotive chatbot and CRM reminder system runs over WhatsApp
- **Appify** — Brandon plans to use it for LinkedIn scraping as a seed data source before running Gemini CLI research
- **Linked Helper** — Mentioned by Elijah as a LinkedIn automation tool used by community member Dawn Davis for podcast guest outreach
- **Vanta** — SOC 2 compliance platform Brandon's team plans to use starting January 2026
- **Electron** — Suggested by Brandon as a framework for building cross-platform desktop (Windows/Mac) applications
- **PyInstaller** — Tiran dropped a link in chat; converts Python scripts to Windows/Linux executables
- **Rust + GitHub Actions** — Ty built a launcher application in Rust, compiled and deployed via GitHub Actions, without touching a local environment
- **AWS Rekognition** — Ty uses it for face recognition and auto-tagging in his Fire Stick photo display app
- **Fabric** — Mentioned by Ty as a skills/prompt library used in his VPS-based personal assistant setup
- **Whisperflow** — Voice-to-text tool used by Scott and Ryan to talk to Claude Code instead of typing
- **Limitless (wearable)** — Brandon wears it for ambient note-taking; noted it gets strange looks in public
- **Qwen3 Coder** — Patrick recommended it as a local model; suggested a smaller quantization to fit in 24GB RAM
- **OpenCoder** — Patrick described it as "Claude Code but for open/local models"; recommended for running local models
- **Picasa** — Referenced as the inspiration for Tiran's Dropbox-based photo gallery tool
- **Dropbox API** — Tiran's photo gallery tool reads from Dropbox folders; noted the API is slow, requiring Supabase caching
- **Poke** — iMessage-based personal assistant app from SF that Maksym referenced as inspiration for his B2C side project
- **SAP** — Tiran suggested building a data bridge to SAP as a go-to-market move for Ty's predictive analytics SaaS
- **PECAN AI** — The competitive reference product Ty is building against for his SMB predictive analytics platform
- **Magnet** — Mac window management app Brandon recommends for keyboard-driven screen layout
- **Amphetamine** — Mac utility to keep the computer awake; Brandon recommends it
- **Presentify** — Mac app Brandon recommends buying immediately on a new Mac
- **Claude Code Usage (VS Code extension)** — Bastian shared a VS Code extension in WhatsApp that shows remaining Claude Code session time in the status bar

## links

- No explicit URLs were shared verbally or pasted into the transcript in a retrievable form. (PyInstaller was mentioned as a link dropped in chat by Tiran, and a Claude Code usage VS Code extension screenshot was sent via WhatsApp by Bastian, but no URLs were read aloud.)

## decisions

- **Patrick Chouinard** will publish his custom GPT file (which identifies which ShipKit template to use for a given project) to the community Discord.
- **Brandon Hancock** will redo the ShipKit onboarding experience after returning from travel, including a "which template should I use?" feature and better guidance for different user journeys.
- **Brandon Hancock** will try Claude Code (instead of Gemini CLI) for the parallel web-search research pipeline, based on Patrick's recommendation.
- **Brandon Hancock** will test Appify for LinkedIn scraping as a seed-data step before running Gemini CLI deep-research agents per person.
- **Brandon Hancock** will share the worker SaaS walkthrough GitHub repository with Elijah as it is being built out, ahead of the full video release in January.
- **Brandon Hancock** will start the SOC 2 process with Vanta on January 1, 2026.
- **Elijah** will coordinate an introduction between Brandon's partner and community member Dawn Davis regarding Linked Helper for LinkedIn outreach automation.
- **Tiran Dagan** will rebuild the Prepper tool architecture based on ShipKit prompt outputs and share updates once it is running.
- **Maksym Liamin** will try GPT-4o mini on ElevenLabs and the GPT Realtime API for voice agents, based on Ty's and Carlos's recommendations.
- **Ryan C** will clear his Claude Code conversation context and restart fresh to resolve the hallucination loop breaking his image-editing feature.
- **Ty Wells** will spin up a second Docker container to enable live preview of his kiosk application during development.