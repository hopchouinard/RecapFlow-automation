## general

This was a coaching/community call for the ShipKit community, hosted by Brandon Hancock. The session followed a round-robin format where members shared project updates, demos, and asked questions. Brandon opened by sharing that he had been accepted into TinySeed for a startup based on the RAG template, and that a passport emergency had disrupted his travel plans.

Participants covered a wide range of projects: Patrick Chouinard was building a custom GPT to identify which ShipKit template to use for a given project, and was also leading an enterprise AI platform evaluation at his company. Scott Rippey demonstrated a parallelized morning summary agent built with the Anthropic TypeScript SDK and Google APIs. Ryan C showed a social media automation platform with AI image editing via Nano Banana. Maksym Liamin shared updates on WhatsApp-based automotive sales tools for Nissan, Mazda, and Infinity, plus a new iMessage personal assistant product. Tiran Dagan presented four projects: a resume analyzer (CV Refinery), an emergency preparedness planner, a consulting report-to-interactive-site converter, and a trip planning tool (SherpaCow). Ty Wells showed a predictive analytics platform for SMBs, a remote cloud-based coding agent accessible from mobile, and a Fire Stick-based family photo display with face recognition.

The call also included discussions on enterprise AI model evaluation strategy, voice agent latency trade-offs, LinkedIn outreach for B2B sales, SOC 2 / CASA 2 certification, local model recommendations, and ShipKit onboarding improvements.

## insights

- Patrick Chouinard: Claude Code outperforms Gemini CLI for web search + scraping tasks because it can mix web search and web fetch (scraping) in the same workflow.
- Patrick Chouinard: Enterprise AI agreements typically come with a shared token pool across all users, making unlimited usage practical; binding to a single provider long-term is risky given how fast the market moves.
- Brandon Hancock: The generator-evaluator loop pattern (worker generates, evaluator critiques with feedback, loop repeats) produces high-quality agentic outputs for nebulous tasks, at the cost of speed.
- Scott Rippey: Splitting parallel agent calls into separate context windows prevents context overflow and timeout issues that occur when one large call tries to process too much data at once.
- Brandon Hancock: The textbook SaaS approach is to validate the service manually first (prove it delivers value), then build software to automate it — not the reverse.
- Brandon Hancock: For enterprise/B2B sales, a long-play LinkedIn strategy (20 connection requests/day, consistent thought leadership content, no immediate pitch) compounds significantly over a year.
- Tiran Dagan: When using ShipKit's ideation prompts, feeding an existing PRD into the AI and asking it to answer the prompts on your behalf produces richer, more surprising outputs than answering from scratch.
- Brandon Hancock: Committing frequently via a simple Claude command ("commit this to GitHub") removes friction and preserves rollback points — critical when AI agents make unexpected changes.
- Ty Wells: Running four parallel Claude Code projects with sub-agents can burn through $300+ in a single evening — but the volume of work completed justifies it.
- Brandon Hancock: Planning thoroughly before coding means slower initial progress but much faster velocity past the 50% mark of a project.
- Maksym Liamin: Voice agent model selection is a hard trade-off — smarter models have too much latency; fast models can't reliably do tool calls. Kimi K2 (quantized, hosted) was their current production choice.
- Ty Wells: GPT-4o mini on ElevenLabs achieves ~45ms latency while still supporting tool calls — a viable balance point for voice agents.

## qa

**Q (Brandon Hancock):** What happens when the output from all your parallel tasks exceeds the context window?
**A (Scott Rippey):** I hard-coded rules to limit data scope (e.g., only look back 7 days, use meeting summaries not full transcripts, only scan knowledge base titles). Splitting into separate parallel calls also gives each its own context window, so no single call gets overloaded.

**Q (Brandon Hancock):** Are you using Vercel AI SDK or the Anthropic SDK directly?
**A (Scott Rippey):** The Anthropic TypeScript SDK directly — not the agent SDK, not Vercel. It's a standard Next.js app deployed via GitHub to Netlify.

**Q (Brandon Hancock):** For the voice side of your automotive product, are sales agents being replaced or is this supplementary?
**A (Maksym Liamin):** Still supplementary. The client-facing voice agent is in mid-beta, handling 300–500 leads per week out of full capacity. Full rollout is likely a year away.

**Q (Brandon Hancock):** What's the latency on your voice agent and which model are you using?
**A (Ty Wells):** About 45ms using GPT-4o mini on ElevenLabs — it balances tool call reliability and low latency.

**Q (Maksym Liamin):** Have you heard of CASA 2 certification from Google, and do you have contacts who can help?
**A (Brandon Hancock):** Not specifically CASA 2, but for similar certifications (SOC 2), Vanta is the recommended platform (~$7k) plus ~$7k for the auditor. SOC 1 is a point-in-time test; SOC 2 requires 6 months of continuous monitoring logs. Glenn also dropped tips in chat about finding an actual vendor.

**Q (Patrick Chouinard):** Have you considered selling CV Refinery to consulting firms, who spend enormous time reformatting CVs for RFP submissions?
**A (Tiran Dagan):** That's a great idea — in consulting you pick the team that's available and then have to convince the client they're the right fit. The tool could consume the client's RFP requirements and reformat the CV to match, which is exactly the problem. Will pursue this angle.

**Q (Elijah):** When you say "cursor dot" in the ShipKit setup instructions, is that doing something important?
**A (Brandon Hancock):** No — it just tells Cursor to open the folder. You can open any IDE manually and point it at the folder. There's nothing magic about that command.

**Q (Brandon Hancock):** Is there a way to build a Windows desktop application through Claude Code?
**A (Ty Wells / Brandon Hancock / Tiran Dagan):** Ty built a Rust launcher via Claude Code, deployed through GitHub Actions, which then runs a web-view kiosk. Brandon suggested Electron for cross-platform desktop apps or compiled Python (PyInstaller). Tiran suggested a configured VM image for easy redeployment.

## tools

- **Claude Code** — Primary coding agent used by most participants; Patrick found it superior to Gemini CLI for mixed web search + scraping workflows.
- **Gemini CLI** — Used by Brandon/Patrick for parallel custom deep-research agents with Google Search access; being superseded by Claude Code for some use cases.
- **Trigger.dev** — Referenced as a platform for parallelization and evaluator-loop agentic workflows; Scott used a screenshot of it as context when building his own parallel implementation.
- **Anthropic TypeScript SDK** — Scott's core SDK for building his morning summary agent and chat interface; not the agent SDK.
- **ElevenLabs** — Voice synthesis used by Ty Wells for his remote coding agent's audio playback; also used by Maksym for voice agents.
- **Nano Banana 3 Pro** — Image generation/retouching model integrated into Ryan C's social media platform for in-app image editing.
- **Cloudflare R2** — Used by Ryan C as a media bucket to avoid overloading Supabase storage.
- **Supabase** — Database, auth, and blob store used across multiple participants' projects as the core backend.
- **Netlify** — Deployment platform used by Scott and Ryan C (GitHub → Netlify pipeline).
- **N8N** — Scott uses it for customer project back-end automations, but not in his current agent application.
- **Appify** — Brandon plans to use it for LinkedIn scraping to seed data for his parallel Gemini CLI research pipeline.
- **Linked Helper** — LinkedIn automation tool mentioned by Elijah; community member Dawn Davis uses it to automate podcast guest outreach.
- **Whisperflow** — Voice-to-text tool used by Scott and Ryan C to talk to Claude instead of typing.
- **Limitless** — Wearable note-taking device Brandon uses; mentioned in context of walking around talking to himself to capture notes.
- **Vanta** — SOC 2 compliance platform Brandon plans to use starting January 2026; estimated ~$7k.
- **PyInstaller** — Python-to-executable tool for Windows/Linux, shared by Tiran Dagan in chat for Ty's kiosk use case.
- **Electron** — Suggested by Brandon for building cross-platform desktop applications.
- **Kimi K2** — Open-source LLM used by Maksym in production for voice agents due to low latency and tool call support.
- **OpenCoder** — Open-source Claude Code equivalent for local/open models, recommended by Patrick for running local models.
- **Qwen3 Coder** — Local model recommended by Patrick for running on 24GB RAM machines via OpenCoder.
- **Anti-Gravity (Windsurf)** — IDE Brandon uses ~10% of the time for visual/UI tasks with Gemini 2.5 Pro; praised for agentic memory that improves over time.
- **AWS Rekognition** — Used by Ty Wells in his Fire Stick photo display app for automatic face tagging.
- **Dropbox API** — Used by Tiran Dagan in his photo gallery tool; noted as extremely slow, requiring Supabase caching.
- **Google Maps API** — Integrated into Tiran Dagan's SherpaCow trip planner for place search and directions.
- **Magnet** — Mac window management app recommended by Brandon (~$3); enables keyboard shortcuts to snap windows.
- **Amphetamine** — Mac utility recommended by Brandon to keep the computer awake during long work sessions.
- **Presentify** — Mac app recommended by Brandon (~$8) for screen presentations.
- **Fabric** — Skills/pattern framework mentioned by Ty Wells as used in his VPS-based remote coding agent.
- **PECAN AI** — Existing ML prediction platform that inspired Ty Wells's SMB-focused predictive analytics tool.
- **SAP** — Suggested by Tiran Dagan as a bridge integration target for Ty's analytics platform given SAP's SMB market push.

## links

- No explicit URLs were shared verbally or in chat that were captured in the transcript with full links. (Patrick shared a link to OpenCoder and Tiran shared PyInstaller in chat, but the actual URLs were not read aloud or transcribed.)

## decisions

- Patrick Chouinard will publish his custom GPT template-selector code to the ShipKit community Discord in addition to adding it to his own GPT.
- Brandon Hancock will redo the ShipKit onboarding experience after returning from travel, including a "which template should I use?" feature.
- Brandon Hancock will try Claude Code for the parallel web-search/scraping research pipeline (instead of Gemini CLI) based on Patrick's recommendation.
- Brandon Hancock will explore using Appify for LinkedIn scraping as a seed step before kicking off Gemini CLI deep-research agents.
- Brandon Hancock will send the Linked Helper tool information to his business partner for LinkedIn outreach automation.
- Brandon Hancock will start the Vanta SOC 2 certification process on January 1, 2026.
- Brandon Hancock will share the video production SaaS GitHub repository with Elijah as it is being built out (before the full walkthrough video is ready in January).
- Tiran Dagan will explore Patrick's suggestion of targeting consulting firms as a customer segment for CV Refinery.
- Maksym Liamin will test GPT-4o mini on ElevenLabs and the GPT real-time model for voice agent use cases based on Ty Wells's and Carlos Aguilar's recommendations.
- Brandon Hancock will download and test the Claude Code usage/status VS Code extension that Bastian shared via WhatsApp.