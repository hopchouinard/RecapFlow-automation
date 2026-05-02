## general

This was a group coaching/community call hosted by Brandon Hancock for the ShipKit community — a course and template platform for AI-assisted full-stack development. The call followed a round-robin format where each participant shared project updates, wins, and questions, with Brandon and others providing feedback and advice.

The session opened with discussion of a Cloudflare outage affecting many participants, followed by excitement about Google's newly released Gemini 3 model and the "Antigravity" IDE (Google's new agentic coding environment). Brandon shared his plans to build a Pokemon "Natural Geographic" AI video generator as a demonstration project for ShipKit's Worker SaaS template. The call covered a wide range of member projects including Tom's Python/SQLAlchemy backend migration, Ty's holiday SMS raffle promotion, Patrick's GitHub Copilot training automation, Paul's exploration of Dokploy for self-hosted deployment, Morgan's dashcam data processing concept, and Garron's multi-agent conversation tracker app.

A recurring theme was the tension between rapidly evolving AI tools (Antigravity, Gemini 3, Trigger.dev) and maintaining disciplined, structured development workflows. Brandon repeatedly emphasized the value of ShipKit's "digital twin" markdown file as a north star for keeping AI agents aligned during complex refactors. The roadmap for ShipKit content was also discussed, with LangGraph/LangChain and voice agent templates identified as upcoming priorities.

## insights

- **Gemini 3 is speed-competitive with GPT-5** but the real differentiator is response speed — Dave noted it was on par quality-wise but much faster, making iteration cycles significantly shorter.
- **Antigravity's agentic memory is purely emergent** — it learns rules as you use it rather than from explicit configuration, which is a paradigm shift from tools like Cursor that use explicit rules files.
- **Antigravity uses its own "task" concept** that may conflict with ShipKit's task-based workflow naming; Brandon flagged this needs testing before recommending it for ShipKit workflows.
- **The "digital twin" markdown file is critical for complex agent refactors** — Brandon explained it gives the AI a stable north star to compare against current code state, preventing context-window drift during multi-file changes.
- **For client website work, being proactive beats reactive intake forms** — Brandon advised Abdul to come to client calls with pre-built options (using AI to generate variations) rather than asking open-ended questions.
- **Standardizing a repeatable process before scaling client work** is key: if you nail the workflow for one customer, the next one takes a fraction of the time.
- **ADK (Google Agent Development Kit) deployment to Agent Engine is still immature** — great for local development but not ready for scaling to 100+ concurrent users; Trigger.dev is the recommended deployment path.
- **Pre-processing ("seed data") before expensive AI calls saves significant cost** — Patrick used Perplexity to check for fresh news before triggering full Gemini CLI research runs, avoiding redundant expensive calls.
- **Dokploy provides a self-hosted Vercel-equivalent** on any VPS for ~$10/month, with Docker-based orchestration, reverse proxy, SSL, and GitHub CI/CD — Hostinger and DigitalOcean have both invested in it.
- **For video content, story matters more than production quality** — Mitch noted that certain audiences watch purely for narrative, not polish, and that meme culture and "pattern interrupts" drive virality.
- **Vibe-coded applications are likely contributing to infrastructure instability** — the group speculated that the surge of AI-assisted developers pushing insecure code is increasing attack surface across major platforms.
- **N8N workflows can be exported as JSON and ported to Trigger.dev** by passing the JSON to ShipKit's Task Orchestrator prompt to generate Trigger.dev-compliant tasks.

## qa

**Q (abdulshakur.abdullah):** Do you see a future for ShipKit given that AI agents keep getting better and tools like Antigravity can build entire projects?

**A (Brandon Hancock):** Yes — ShipKit's value comes from multiple pillars: AI docs, task/workflow automation, prompt engineering applied to software, project templates that encode best practices, and the course itself that helps people understand *why* tools connect the way they do. No single AI tool replaces all of that.

**Q (abdulshakur.abdullah):** For small client website contracts, is it worth building an automated form-to-Lovable pipeline, or should I just do it manually?

**A (Brandon Hancock):** Rather than a passive intake form, be proactive — hop on a 30-minute call, give clients prep items beforehand (e.g., find 5 competitor sites you like), and use ChatGPT agent mode to generate options on their behalf during the call. White-glove experience beats self-serve forms for small contracts.

**Q (abdulshakur.abdullah):** Would an Animal Farm-style political satire video concept go viral, or would it get flagged?

**A (Mitch):** Pick one side, not both — mixing both will dilute your page's audience vector. Separate pages for each political angle would work better. Also study TikTok's content graph to understand whether your niche is a primary node or a gateway to something else, since that affects how the algorithm distributes your content.

**Q (Garron Selliken):** My multi-agent app works in AI Studio but keeps breaking when I try to refactor it in Cursor. Should I start over in Antigravity or keep trying to fix the existing codebase?

**A (Brandon Hancock):** With only a router + 3 sub-agents, the structure is portable enough to start fresh. Use the AI Studio working version to update your digital twin markdown file first, then have the coding tool make your code match the twin. Also try one more branch in the existing repo first — give it a chance to migrate before abandoning it.

**Q (Garron Selliken):** Once I have the agent app working locally, how do I deploy it to 150 beta users?

**A (Brandon Hancock):** ADK's Agent Engine deployment is still immature for scale. The recommended path is Trigger.dev — it handles long-running jobs, has built-in observability, and the Worker SaaS template in ShipKit already shows LLM chat patterns you can extend to agents. LangGraph is the alternative for more complex orchestration needs, coming in January/February.

**Q (Mitch):** Are the Pokemon Natural Geographic channels using ElevenLabs for narration?

**A (Brandon Hancock):** Unknown — creators don't disclose their stacks. Still experimenting with VO for video generation; the voice component is the part that still needs work.

**Q (Paul Miller):** Has anyone else explored Dokploy for self-hosting Next.js apps instead of Vercel?

**A (Paul Miller, Tom Welsh, Morgan Cook):** Paul introduced it — it's a Docker-based self-hosted platform that replicates Vercel functionality on any VPS, with reverse proxy, SSL, GitHub CI/CD, and clustering. Hostinger and DigitalOcean have invested in it. Tom plans to use his Dungbeetle project as a test case. Morgan noted Coolify is a competitor but Paul found Dokploy's UX more intuitive.

**Q (Brandon Hancock to Patrick):** What vector store are you using locally for your accumulated research data?

**A (Patrick Chouinard):** Milvus on SQLite — simple, just enough to get the framework in place. May migrate later, but the priority right now is establishing the architecture, not optimizing the storage layer.

## tools

- **Gemini 3 (Google)** — New flagship model; discussed for speed advantage over GPT-5 and availability in Cursor and Gemini CLI
- **Antigravity (Google)** — New agentic IDE released day-of-call; discussed as a parallel-workflow coding environment competing with Cursor
- **Cursor** — Primary IDE used by most members; Gemini 3 already available as a model option
- **Claude Code** — Used by Paul (replacing Cursor to reduce costs), Ty (for SMS integration docs), and Patrick (for code development)
- **GPT-5 / GPT-5.1** — Referenced as quality benchmark; used by Patrick via OpenRouter for cross-research insights
- **Trigger.dev** — Recommended deployment platform for long-running agent jobs; ShipKit Worker SaaS template built on it
- **Supabase** — Database/auth platform used by multiple members; Brandon and Ty noted accumulating many active projects on it
- **Dokploy** — Self-hosted Vercel alternative using Docker; Paul introduced it as a way to avoid vendor lock-in
- **Coolify** — Mentioned by Morgan as a Dokploy competitor for self-hosted deployment
- **Lovable** — No-code/AI app builder; discussed for Abdul's client website projects
- **N8N** — Workflow automation tool; Mitch using it for video pipeline, noted memory issues with binary data; Brandon described JSON export path to Trigger.dev
- **Perplexity** — Used by Patrick as a pre-processor to check for fresh news before triggering expensive Gemini CLI research
- **Gemini CLI** — Used by Patrick for deep AI research workflows in his Neuro Elix project
- **GitHub Copilot** — Patrick trains 350 developers on it; new agent management features (markdown-based agents with parallel handoffs) discussed
- **SQL Alchemy** — Tom's Python ORM for his Dungbeetle backend, replacing DrizzleKit
- **DrizzleKit** — TypeScript-only ORM Tom removed from his frontend after committing to a Python backend
- **LangGraph / LangChain** — Upcoming ShipKit content; described as the enterprise agent standard
- **Google AI Studio** — Garron used it to prototype his multi-agent app; generated a working functional mockup
- **Google ADK (Agent Development Kit)** — Framework Garron is using for his conversation tracker agents; deployment to Agent Engine flagged as immature
- **ElevenLabs** — Voice synthesis platform; discussed for potential use in AI video narration
- **VO (Veo, Google)** — Video generation model Brandon is experimenting with for Pokemon video project
- **OpenRouter** — API aggregator Patrick uses to access GPT-5.1 for insight synthesis
- **Milvus** — Local vector database Patrick is using on SQLite for accumulated research storage
- **Warp** — Terminal/IDE tool Patrick uses alongside Claude Code for development
- **Confluence / Atlassian** — Patrick's internal documentation platform; his agents auto-update training material there
- **Dropbox** — Mitch using it as file storage in his N8N video pipeline via API
- **FFMPEG** — Discussed for extracting image frames from dashcam video to reduce AI processing costs
- **Hostinger / DigitalOcean** — VPS providers mentioned as Dokploy-compatible hosts; both have invested in Dokploy
- **smsevil.eu** — Custom SMS server Ty uses for his Bahamas mobile recharge business (not Twilio)
- **Vercel** — Current hosting platform many members use; Dokploy discussed as a self-hosted alternative
- **Auth0** — Mentioned by Scott as an auth option for client projects alongside Supabase Auth

## links

- No explicit URLs were shared in the transcript. Paul mentioned posting a YouTube video and a Dokploy resource to the School community forum, but no URL was provided.

## decisions

- **Brandon** will experiment with Antigravity + ShipKit task templates over the next few days to determine if naming conflicts exist and how they can synergize.
- **Brandon** will build a Pokemon Natural Geographic AI video generator using the Worker SaaS template as the next ShipKit demonstration project, targeting completion before Thanksgiving.
- **Brandon** will bump ShipKit to a larger server to address the loading/spinning wheel issue Abdul reported.
- **Tom** will use his Dungbeetle project as a test case for migrating from Vercel to Dokploy.
- **Tom** will try throwing his Traveling Salesman Problem at Gemini 3 and report back.
- **Garron** will update his digital twin markdown file using the AI Studio working prototype, then use it as a north star to refactor his Cursor codebase before considering a full migration to Antigravity.
- **Garron** will share a demo of his agent app with Brandon to determine whether Trigger.dev or LangGraph is the right deployment path.
- **Patrick** will verify whether Gemini 3 is accessible in Gemini CLI via the preview activation (contradicting what Brandon had read about it requiring a $200 plan).
- **Brandon** will connect with Paul in early 2026 to discuss conference strategy for a planned ShipKit event.
- **Brandon** will research Trigger.dev's agent-specific deployment examples further to provide better guidance to Garron.
- **Mitch and Brandon** will collaborate on the Pokemon video generator project, with Mitch advising on meme culture angles and pattern interrupts.
- **abdulshakur.abdullah** will send Brandon a screenshot if the ShipKit loading issue recurs on a non-restricted network.
- **Paul** will keep Brandon posted on his Dokploy journey as he goes deeper into self-hosted infrastructure.