## general

This week's call combined the usual project round-robin with a broader infrastructure/tooling discussion, bookended by community-submitted questions relayed via chat (from Elena Romanova on fundraising/patenting, Timothy Tt on production-readiness process, and Tim Hildenbrandt on sharing ShipKit-derived repos with outside collaborators). Patrick Chouinard hosted despite being sick, opening with a deep dive into his personal "Beacon/Clara" research-and-briefing pipeline, his Astra-driven website rebuild, and his skill-management philosophy (ShipKit templates converted into orchestrated "skills," a permanent tech-stack definition, and model routing between Sonnet and Opus based on task complexity). Juan Torres discussed growing his AI photo-booth business toward high-end San Diego venues, prompting live chat suggestions (photo magnets, in-person pitching) from Biggi Fraley and Ryan C. Rod Morrison returned after time away to ask detailed questions about operationalizing agent workflows and skill hosting at his consulting clients, while Ty Wells demoed a fully interactive, analytics-capturing pitch app ("The Island," shared live via islandflow.ai) for his Bahamas-focused ERP/CRM platform launch, and new member Lisa Jetton introduced her background in P2P/Holochain systems and construction-industry agentic work.

The second half of the call shifted into a round-robin on personal infrastructure and harness choices, with Lisa asking the group how to navigate toolkits from scratch. Patrick described his three-server Proxmox setup orchestrated by a Hermes agent and his dev/staging/prod-segmented T3 Code environment; Paul Miller detailed his multi-subscription, multi-orchestrator T3 stack approach and shared an update on reinventing a 12-year-old visual shelf-recognition project for a cola manufacturer using open-source visual LLMs. Ryan C reported abandoning Fable 5 for 4.8, a successful SEO win for an estate-agency site, new telephone-calling capability added to Hermes, and a self-tracking fitness app in progress; Morgan (mdcatc) noted the "rapid prototype, rapid trash" nature of current AI-driven work and planned to tidy up his personal projects portal.

Throughout, the chat log carried a steady stream of tangential tool recommendations (Omi.me, Granola.ai, Fieldy) for personal recording/note-taking, humor about token/subscription burn ("I have 2 $200 plans... and I'm lazy"), and a recurring theme — echoed by Patrick near the end of Part 2 — that the group itself functions as a weekly "context upgrade," letting members stay abreast of a fast-moving landscape no single person can track alone. Several members exited early (Rod, Lisa) citing other commitments, and Paul flagged a compliance-related question from the community board to be addressed on-call.

## insights

- Patrick separates concerns in his personal agent stack: "Beacon" does raw web research with no personal context, then hands off to "Clara," which knows everything about Patrick and reformats the raw report into a personalized morning-briefing monologue, sent to TTS/Discord audio.
- Patrick keeps a full archive (transcript + audio) of every Beacon/Clara briefing so he can feed prior discussions back into ChatGPT and use that feedback to continuously improve future briefings — a self-optimizing loop.
- Patrick had Astra (operating as "lead of a dev team") dispatch sub-agents and run autonomously for ~17 hours on a website rebuild, only checking in with him when needed.
- Heavy token consumption is a recurring theme: Patrick and Ty both burned through Astra/Claude $200-tier subscriptions within a week during heavy building periods; Patrick attributes this partly to a global token-reset event around the 6th.
- Patrick's approach to skills: ShipKit templates are essentially prompts already close to skill format; he decomposes long templates into an "uber skill" that orchestrates sub-skills, adds YAML frontmatter, and defines callable vs slash-command skills.
- Patrick maintains a permanent, account-level tech stack definition so Claude/agents stop recommending inconsistent technologies and instead default to an approved, coherent stack.
- Patrick's team is building a proprietary "Grill with Docs" tool with enough embedded business context that spec-generation dropped from ~70-80 clarifying questions to ~15-20 — a major token/time saver.
- Patrick uses "Wayfinder" ahead of "Grill with docs" to split large projects into phases sized to fit within a single session's context window, keeping the orchestrator's (Fable's) context small while giving the large context window to the model doing actual building (Sonnet/Opus).
- Patrick's model-selection strategy: use Sonnet for simple, well-scoped tasks and reserve Opus for complex, multi-system integration work; Fable evaluates task complexity to route accordingly.
- Patrick deliberately code-reviews with a different model family than the one used to build (e.g., build with Astra/Claude, review with GPT, or vice versa) rather than assuming one model is inherently "better."
- Patrick recommends GLM 5.3 on OpenRouter as a model performing between Sonnet and Opus quality at a fraction of the cost.
- Paul suggested benchmarking preferred Claude models against a range of OpenRouter models (including cost-effective, Bedrock-hosted options for data residency/security) to find the cheapest model matching benchmark quality.
- Patrick keeps OpenRouter/Codex/Claude for personal work but uses Claude+Copilot on an AWS backend at his (financial institution) job, since OpenRouter isn't viable in that regulated environment.
- Rod noted increasing compliance/data-governance scrutiny at client organizations regarding which AI tools and data-handling practices are in use.
- Ty built his ERP pitch as an interactive in-app "slideshow" instead of static slides specifically to capture click/engagement analytics — something a slideshow can't provide.
- Ty developed a "UI in reverse" testing technique: build/mock the UI first without backend logic, then have an agent write code to satisfy the UI's implied contracts, followed by an adversarial agent session that loops to confirm correctness — used across ~7 agents and ~1,400 screen iterations in about 5 hours.
- Ty's ERP platform ("The Island") consolidates ~$50,000 worth of 5-8 separate SaaS subscriptions into one platform tailored to Bahamas-specific regulatory compliance needs not met by US/European/Canadian software.
- Juan's photo-booth AI image-to-image transformation pipeline reportedly outperforms several existing commercial photo-booth apps' AI features in quality and creativity, based on his research.
- Patrick Chouinard runs three Proxmox servers hosting Linux VMs and LXC containers, deliberately avoiding single-OS lock-in, with Mac as workstation and Linux as backend — all orchestrated by a Hermes agent.
- Patrick splits his T3 Code server environments by security frontier (dev, staging, prod), each walled off but able to communicate — described by Paul as "a harness for harnesses."
- Patrick uses OnShow as a dynamic memory layer alongside T3's basic memory; a $100 free credit lasted about six months of near-constant daily use, calling it "dirt cheap."
- Patrick built a custom "Agent Ops" add-on/plugin with full API documentation of his infrastructure, MCP servers, and skills to monitor his network — functioning as his network operator.
- Patrick is experimenting with Pi (open source) as a specialized code-review harness since it can be modified freely.
- Paul Miller uses multiple Claude and OpenAI subscriptions simultaneously with orchestrators managing separate "program of work" layers (project focus vs. application stack focus) built on T3 stack.
- Ryan C found Fable 5 unusable ("It's just dumb, I hate it") and reverted to Fable 4.8, despite trying different skills configurations.
- Ryan C's estate agency website (with CRM-like backend) outranked long-established, internationally known competitor agencies in local SEO within a week or two of launch.
- Ryan and Scott added telephone-calling ability to their Hermes agents, enabling the agent to make calls — described as both useful and "entertaining" to review afterward.
- Scott's "CC Black Box" IDE (open-sourced, Mac-only) includes built-in simulators for driving Claude Code workflows, seen as a nicer alternative to Cursor/VS Code.
- Morgan (mdcatc) noted the pace of AI-driven work means most completed work becomes "rapid prototype, rapid trash" — built and discarded.
- Paul Miller's 12-year visual shelf-recognition project (originally built with an Israeli tech partner for a major cola manufacturer) is being reinvented using open-source visual LLM models to automate training data gathering and fine-tuning, comparing model quality and running fine-tuning on Mac Mini or cloud GPU pods.
- Patrick noted the value of the weekly group call itself: "There's too much for a single person to be aware of all the time... this group is basically how I do my Context Upgrade every week."

## qa

**Q (Juan Torres):** As your news-generation agent accumulates many days of reports, do you worry about hitting model context limits, or would you use larger-context "big gun" models to compensate?
**A (Patrick):** Execution is handled by a cheap model (Luna, ~900k-1M token context via Hermes) for news aggregation; re-analyzing old news has limited value, so there's no need to vectorize or hold everything in context — the archive is mainly kept so he can replay the audio, not for reasoning over historical news.

**Q (Rod Morrison):** Is anyone still using ShipKit, and can you explain how you're using it?
**A (Patrick):** Not for building directly, but ShipKit templates are reformatted into skills — decomposed into an orchestrating "uber skill" plus sub-skills, with YAML frontmatter and defined calling conventions; Brendan is reportedly working on a similar ShipKit-to-skills conversion.

**Q (Rod Morrison):** Are you hosting these skills in Claude directly or on GitHub — do you have your own internal marketplace?
**A (Patrick):** They use a private internal marketplace on Azure DevOps (migrating eventually to GitHub); it works with Claude Code and GitHub Copilot but not yet with Cowork/Claude AI features requiring a GitHub repo, which they're now setting up.

**Q (Rod Morrison):** Are you using Obsidian for that "department memory" concept?
**A (Patrick):** No — Obsidian doesn't scale to organization-level use since it lacks synchronization, diffing, and rollback; instead they store context documents in a Git repo that syncs to everyone's machine each morning, invisible to end users.

**Q (Rod Morrison):** What models do people use once a spec is well-defined — just run Sonnet high?
**A (Patrick):** It's not one-size-fits-all; Fable evaluates task complexity — Sonnet handles simpler tasks fine, while complex, multi-system integration work goes to Opus. Splitting work into small enough pieces lets Sonnet handle a lot more than expected.

**Q (Juan Torres):** Do you combine Hermes with OpenRouter for work outside your main job, and could OpenRouter access top-tier Claude models?
**A (Patrick):** Yes, he's a heavy OpenRouter user for personal projects since AWS is more complex to configure for casual/weekend use; Hermes operates the OpenRouter API automatically. OpenRouter can access top Claude models, but at full pay-per-use pricing rather than subscription rates.

**Q (Paul Miller):** With the interactive pitch app, were you able to capture engagement data — number of viewers, click-throughs, etc.?
**A (Ty Wells):** Yes — that was the whole point of building it as an app instead of a slideshow; shared links are tracked, giving him analytics a static slideshow couldn't provide, and people were still clicking through it live during the call.

**Q (Lisa Jetton):** What's the broader vision for your platform — is it meant to function like a brokerage connecting business clients with infrastructure and funnels?
**A (Ty Wells):** The platform ("The Island") consolidates around $50,000 of previously separate subscriptions into one system for his Bahamas-based companies, built to meet local regulatory compliance needs not addressed by existing software; today was the launch date to release it to clients.

**Q (Lisa Jetton):** What harnesses/toolkits do people use, and how do they navigate coordination between tools, since she's building her stack from the ground up?
**A (Paul Miller):** Many in the group started with Shipkit about a year ago but have since moved on; Paul now uses the T3 stack with multiple Claude and OpenAI subscriptions, using orchestrators to manage a program of work across projects and a separate focus per application stack.

**Q (Patrick Chouinard):** Did Paul deploy T3 code servers, or just have it installed on his workstation?
**A (Paul Miller):** Not yet deployed — currently on his Mac Mini and Linux home servers, planning to use the Mac for day-to-day work and a GPU-equipped box for overnight/slower tasks.

**Q (Lisa Jetton):** Has Patrick dabbled with ECC and compared it to Pi?
**A (Patrick Chouinard):** No, he hasn't tried ECC.

**Q (Lisa Jetton):** Have Patrick/Paul played with configuring or changing Hermes's implicit learning/self-adopting skills (context/memory bloat from ephemeral tasks), or just stuck with defaults?
**A (Patrick Chouinard):** He uses OnShow as a dynamic memory layer alongside Hermes's basic memory; found it very cost-effective (a $100 credit lasted ~6 months of near-daily use, ~$79 still remaining).

**Q (Paul Miller):** Is Morgan (mdcatc) using GPT-6 yet?
**A (mdcatc):** Not yet — he only has the $20 Pro subscription (not the $100 tier) and hasn't had time to test it, though he plans to try it for small tasks.

## tools

- **Beacon** – Patrick's custom research agent that scans the web daily for AI news contextualized to his projects.
- **Clara** – Patrick's primary personal agent that contextualizes Beacon's raw reports and reformats them as a spoken briefing.
- **TTS model + Discord** – Converts Clara's briefing text to audio and delivers it via Discord.
- **Traefik + Tailscale** – Reverse proxy and VPN mesh used to expose Patrick's internal briefing archive externally/on mobile.
- **Hermes** – Personal infrastructure/orchestration agent ("chief of staff") used by Patrick and Lisa; Ryan/Scott added telephone-calling capability.
- **Astra** – Agentic coding tool used by Patrick and Ty for large autonomous build tasks; has usage tiers (light/medium/high).
- **Fable (4.8, 5, 5.1)** – Orchestrator/build tool; Ryan reverted to 4.8 after finding 5 unusable; Patrick uses 5.1 for a training app.
- **ShipKit** – Source of template prompts converted into reusable "skills"; earlier-generation markdown-based tool the group used ~a year ago.
- **Wayfinder** – Patrick's process for splitting large projects into phase-sized contexts before "Grill with Docs."
- **Grill with Docs** – Proprietary internal tool embedding business context to cut spec clarification questions.
- **Azure DevOps (ADO)** – Private repository/marketplace hosting internal skills at Patrick's workplace.
- **GitHub / GitHub Copilot** – Target migration platform for skills; used alongside Claude Code at work.
- **AWS (incl. Bedrock, API/MCP gateway)** – Corporate backend infrastructure for Claude/Copilot at Patrick's employer.
- **OpenRouter** – Multi-model API platform used for personal projects and benchmarking cost-effective models.
- **GLM 5.3** – Model on OpenRouter noted as quality between Sonnet and Opus at a fraction of the cost.
- **Claude Code / Sonnet / Opus** – Claude family models discussed for task-complexity-based routing and build/review separation.
- **Codex** – Used by Patrick alongside OpenRouter/Claude for personal work.
- **Cursor** – IDE currently used by Juan; also referenced as less favored alternative to CC Black Box.
- **Matt Pocock skills/methodology** – Out-of-the-box skill framework (implement, simplify, code-review workflow) referenced by Rod.
- **Google Startup School / GCP** – Program Rod mentioned signing up for.
- **Holochain** – P2P/distributed tech (2D hash graph) mentioned by Lisa as her prior work background.
- **Arch Linux ecosystem / Omarky / CachyOS / Fedora** – Linux distros Lisa discussed for her AI systems setup.
- **Perplexity Windows agent stack** – Agent operating loop (model, harness, orchestrator, scheduler, local tools/MCP servers) mentioned in Beacon's briefing content.
- **Proxmox** – Patrick's virtualization platform hosting Linux VMs and LXC containers across three home servers.
- **T3 Stack / T3 Code** – Used by Paul and Patrick for application development and as a coding harness, split into dev/staging/prod zones.
- **OnShow** – Paid dynamic memory layer service used alongside Hermes/T3 memory.
- **Agent Ops** – Patrick's custom-built plugin/add-on for network monitoring.
- **Pi** – Open-source agent being tested by Patrick as a specialized code-review harness.
- **ECC** – Harness/toolkit mentioned by Lisa for comparison (not tested by Patrick).
- **CC Black Box** – Scott's open-sourced Mac-only IDE with built-in simulators for driving Claude Code workflows.
- **Higgsfield** – Video/image generation tool Ryan has been experimenting with.
- **GPT (Pro subscription)** – Morgan's $20/mo tier; hasn't tested GPT-6 yet.
- **Raspberry Pi (router)** – Used by Paul as a router for remote support and media streaming.
- **OMI / Omi.me** – Wearable recording device mentioned by Ty Wells in chat.
- **Granola.ai** – Computer-based meeting notetaker recommended by Ryan C as an alternative to a physical device.
- **Fieldy** – Recording device (shop.fieldy.ai) shared by Patrick Chouinard in chat.
- **Fathom** – Meeting notetaker/recorder used to capture and summarize the call.
- **Otter.ai** – Meeting notetaker used by Lisa Jetton to transcribe the call.

## links

- Fathom recording of this session: https://fathom.video/share/sTLHaj9eU9y5J4Uhc492BZpG1PCE6kyg
- Ty Wells' interactive ERP/CRM pitch app ("The Island"): https://islandflow.ai/overview#scene=cool-breeze&view=explore
- CC Black Box (Scott's open-sourced IDE): ccblackbox.app
- Photo-magnets interview referenced by Biggi Fraley: https://www.youtube.com/watch?v=N0NceZbY2_4
- Granola.ai (meeting notetaker): https://www.granola.ai/
- Fieldy recording device: https://shop.fieldy.ai/home
- Juan Torres' Instagram demo post: https://www.instagram.com/p/DcgyPGKNJls/
- Savills New Zealand (example real-estate site shared by Paul Miller): https://www.savills.co.nz/

## decisions

- Patrick to expose the Beacon Morning Briefing archive externally via Traefik reverse proxy + Tailscale for mobile/remote access.
- Juan to create a bespoke image-to-image style for a target venue, then email the venue director with a demo and offer a free pilot.
- Juan to build a landing page for his photo-booth application.
- Juan to identify and join local country club/venue networks to find outreach opportunities.
- Juan to prepare a portable demo kit (phone + iPad) with a pre-recorded fallback demo for in-person venue visits.
- Rod to evaluate GLM 5.3 on OpenRouter, establish Claude-based benchmarks, and run comparative OpenRouter model tests.
- Ty and team to run a postmortem on the ERP platform launch the following morning.
- Lisa Jetton will evaluate available harness options (T3 stack, Hermes, OpenRouter) and report back to the group next week.
- Lisa Jetton will deploy T3 code servers on her Mac Mini and Linux server.
- Paul Miller will deploy T3 code servers across his Mac Mini and Linux home servers, splitting day-to-day vs. overnight/GPU-based tasks.
- Patrick Chouinard will continue developing Pi as a specialized harness for code review.
- mdcatc (Morgan) will clean up and update his personal projects portal ("World of Morgan portal") to showcase his work.
- Ryan C will share his fitness-tracking app once development is complete.