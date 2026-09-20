📝 SUMMARY

This week's two-hour call covered Patrick Chouinard's Beacon/Clara research pipeline, Astra-driven website rebuild, and skill-management philosophy; Juan Torres' AI photo booth business discussion; Rod Morrison's questions on operationalizing agent workflows; Ty Wells' live demo of his interactive Bahamas ERP/CRM pitch app; and new member Lisa Jetton's introduction. The second half became a round-robin on personal infrastructure — Proxmox, T3 Code, multi-orchestrator stacks, and an open-source visual LLM project. The recurring theme (per Patrick): the group is a weekly "context upgrade" — no one person can track the fast-moving AI landscape alone.

💡 KEY INSIGHTS

Split your agent stack by concern: Patrick's "Beacon" does raw web research with zero personal context, then hands off to "Clara," which knows everything about him and delivers a personalized morning briefing via TTS/Discord.

Archive everything agents produce. Patrick keeps full transcripts + audio of every briefing to feed prior outputs back in — a self-optimizing loop.

Let agents run autonomously with a clear role: Patrick's Astra (acting as "lead of a dev team") dispatched sub-agents for ~17 hours on a website rebuild, checking in only when needed.

Heavy agent building burns tokens fast — Patrick and Ty both blew through $200-tier subscriptions within a week. Budget for it.

Turn prompt templates into skills: decompose long templates into an orchestrating "uber skill" plus sub-skills, add YAML frontmatter, and define which are callable vs slash commands.

Keep a permanent, account-level tech stack definition so agents stop recommending inconsistent tools.

Embed business context into tooling: Patrick's "Grill with Docs" cut spec-generation clarifying questions from ~70-80 down to ~15-20.

Size work to the context window: Patrick's "Wayfinder" splits projects into phases that fit one session, keeping orchestrator context small.

Match model to complexity: Sonnet for simple work, Opus for complex multi-system integration, with Fable routing automatically.

Code-review with a different model family than the builder (Claude builds, GPT reviews, or vice versa).

Consider GLM 5.3 on OpenRouter — Patrick reports quality between Sonnet and Opus at a fraction of the cost. Benchmark alternatives before you buy (Paul). Note: in regulated environments, OpenRouter isn't viable — Patrick uses Claude + Copilot on AWS at his financial institution, and Rod flagged rising client scrutiny of AI compliance and data governance.

Build for analytics when pitching: Ty's interactive pitch app captures click/engagement data static slides can't.

Try "UI in reverse": mock the UI first with no backend, have an agent code to satisfy the UI's implied contracts, then run an adversarial agent loop. Ty used ~7 agents and ~1,400 screen iterations in ~5 hours.

Vertical + local beats generic SaaS: Ty's "The Island" ERP consolidates ~$50k of subscriptions into one Bahamas-compliance-focused platform.

Avoid homelab lock-in: Patrick runs three Proxmox servers (Linux VMs + LXC), Mac workstation + Linux backend, orchestrated by Hermes.

Layer memory: OnShow as dynamic memory + T3 basic memory — a $100 credit covered ~6 months of daily use.

Explore specialized harnesses: Patrick is testing Pi (open source) as a code-review harness; Scott's "CC Black Box" IDE (open-sourced, Mac-only) has built-in simulators for Claude Code workflows.

Ship fast and SEO follows: Ryan C's estate agency site outranked established competitors in local SEO within a week or two.

As Morgan put it: rapid AI-driven work means most output is "rapid prototype, rapid trash."

Old projects can be reborn: Paul Miller is reinventing his 12-year visual shelf-recognition project with open-source visual LLMs, fine-tuning on a Mac Mini or cloud GPUs.

Meta-lesson from Patrick: "There's too much for a single person to be aware of all the time... this group is basically how I do my Context Upgrade every week."

❓ KEY Q&A

Q (Juan): As your news agent accumulates reports, do you worry about context limits?
A (Patrick): Execution uses a cheap model (Luna, ~1M token context via Hermes). Re-analyzing old news has limited value — the archive is for replaying audio, not reasoning over history.

Q (Rod): Is anyone still using ShipKit?
A (Patrick): Not for building, but templates are reformatted into skills (uber skill + sub-skills, YAML frontmatter). Brendan is doing a similar conversion.

Q (Rod): Skills hosted in Claude or GitHub?
A (Patrick): Private internal marketplace on Azure DevOps (migrating to GitHub). Works with Claude Code and Copilot; Cowork/Claude AI features needing a GitHub repo are being set up.

Q (Rod): Using Obsidian for "department memory"?
A (Patrick): No — it doesn't scale organizationally (no sync, diffing, rollback). They use a Git repo that syncs to everyone's machine each morning, invisible to end users.

Q (Rod): Models once a spec is defined — just Sonnet high?
A (Patrick): Fable evaluates complexity: Sonnet for simple tasks, Opus for multi-system integration. Splitting work small lets Sonnet handle more than expected.

Q (Juan): Combine Hermes with OpenRouter, and can it access top Claude models?
A (Patrick): Yes, he's a heavy OpenRouter user (AWS is too complex for casual use); Hermes operates it automatically. Top Claude models are available at pay-per-use pricing, not subscription rates.

Q (Paul): Did the pitch app capture engagement data?
A (Ty): Yes — that was the point. Tracked shared links provide analytics static slides couldn't; people were still clicking through live during the call.

Q (Lisa): Is your platform like a brokerage connecting clients to infrastructure?
A (Ty): "The Island" consolidates ~$50k of subscriptions into one Bahamas-compliance platform; launched to clients today.

Q (Lisa): What harnesses do people use?
A (Paul): Many started with ShipKit a year ago but moved on. He now uses the T3 stack with multiple Claude/OpenAI subscriptions, orchestrators managing programs of work across projects.

Q (Patrick): Did you deploy T3 code servers?
A (Paul): Not yet — Mac Mini and Linux home servers; plans day-to-day on Mac, GPU box for overnight tasks.

Q (Lisa): Compared ECC to Pi?
A (Patrick): Hasn't tried ECC.

Q (Lisa): Configured Hermes's implicit learning, or defaults?
A (Patrick): Uses OnShow as dynamic memory alongside Hermes basic memory — a $100 credit lasted ~6 months, ~$79 remaining.

Q (Paul): Is Morgan using GPT-6 yet?
A (mdcatc): Not yet — $20 Pro tier only, plans to test on small tasks.

🛠️ TOOLS AND CONCEPTS MENTIONED

Beacon – Patrick's research agent scanning the web daily for AI news contextualized to his projects.
Clara – Patrick's personal agent turning Beacon's reports into spoken briefings.
TTS model + Discord – Converts briefing text to audio and delivers it.
Traefik + Tailscale – Reverse proxy and VPN mesh exposing his briefing archive externally/mobile.
Hermes – Personal infrastructure/orchestration agent ("chief of staff"); Ryan and Scott added telephone-calling capability.
Astra – Agentic coding tool used for large autonomous builds; light/medium/high usage tiers.
Fable (4.8, 5, 5.1) – Orchestrator/build tool; Ryan reverted to 4.8 (found 5 unusable); Patrick uses 5.1.
ShipKit – Earlier-generation tool; templates converted into reusable skills.
Wayfinder – Patrick's process for splitting projects into phase-sized contexts.
Grill with Docs – Internal tool embedding business context to cut spec clarification questions.
Azure DevOps – Hosts internal skills marketplace at Patrick's workplace.
GitHub / Copilot – Target skills migration platform; used alongside Claude Code at work.
AWS (Bedrock, API/MCP gateway) – Corporate backend for Claude and Copilot at Patrick's employer.
OpenRouter – Multi-model API for personal projects and cost benchmarking.
GLM 5.3 – Model on OpenRouter, quality between Sonnet and Opus, fraction of the cost.
Claude Code / Sonnet / Opus – Task-complexity routing; separating build from review.
Codex – Used by Patrick alongside OpenRouter and Claude.
Cursor – Juan's IDE; less favored than CC Black Box.
Matt Pocock skills/methodology – Skill framework (implement, simplify, code-review) referenced by Rod.
Google Startup School / GCP – Program Rod signed up for.
Holochain – P2P/distributed tech (2D hash graph); Lisa's prior background.
Arch Linux ecosystem / Omarky / CachyOS / Fedora – Distros Lisa discussed.
Perplexity Windows agent stack – Agent loop (model, harness, orchestrator, scheduler, local tools/MCP servers).
Proxmox – Patrick's virtualization across three home servers.
T3 Stack / T3 Code – Used by Paul and Patrick for dev and as a coding harness; dev/staging/prod zones.
OnShow – Paid dynamic memory layer.
Agent Ops – Patrick's custom network-monitoring plugin.
Pi – Open-source agent Patrick is testing as a code-review harness.
ECC – Harness mentioned by Lisa (untested by Patrick).
CC Black Box – Scott's open-sourced Mac-only IDE with Claude Code simulators.
Higgsfield – Video/image generation tool Ryan is experimenting with.
GPT (Pro) – Morgan's $20/mo tier; GPT-6 untested.
Raspberry Pi (router) – Paul's router for remote support and media streaming.
OMI / Omi.me – Wearable recorder mentioned by Ty.
Granola.ai – Meeting notetaker recommended by Ryan C.
Fieldy – Recording device shared by Patrick.
Fathom – Meeting notetaker used for this call's recording/summary.
Otter.ai – Meeting transcriber used by Lisa.

📎 SHARED RESOURCES

Session recording (Fathom):
https://fathom.video/share/sTLHaj9eU9y5J4Uhc492BZpG1PCE6kyg

"The Island" — Ty Wells' interactive ERP/CRM pitch app:
https://islandflow.ai/overview#scene=cool-breeze&view=explore

CC Black Box — Scott's open-sourced IDE:
ccblackbox.app

Photo-magnets interview (referenced by Biggi Fraley):
https://www.youtube.com/watch?v=N0NceZbY2_4

Granola.ai:
https://www.granola.ai/

Fieldy:
https://shop.fieldy.ai/home

Juan Torres' Instagram demo post:
https://www.instagram.com/p/DcgyPGKNJls/

Savills New Zealand — example real-estate site shared by Paul Miller:
https://www.savills.co.nz/

🔄 FOLLOW-UPS WORTH EXPLORING

Patrick to expose the Beacon Morning Briefing archive externally via Traefik + Tailscale for mobile/remote access.

Juan to create a bespoke image-to-image style for a target venue, then email the venue director with a demo and free pilot offer; build a landing page; join local country club/venue networks; prepare a portable demo kit (phone + iPad) with a pre-recorded fallback.

Rod to evaluate GLM 5.3 on OpenRouter, establish Claude benchmarks, and run comparative model tests.

Ty and team to run a postmortem on the ERP launch the following morning.

Lisa to evaluate harness options (T3, Hermes, OpenRouter) and report back; deploy T3 code servers on her Mac Mini and Linux server.

Paul to deploy T3 code servers across his Mac Mini and Linux servers, splitting day-to-day vs. overnight/GPU tasks.

Patrick to continue developing Pi as a code-review harness.

Morgan to clean up and update his "World of Morgan portal" to showcase his work.

Ryan C to share his fitness-tracking app once complete.