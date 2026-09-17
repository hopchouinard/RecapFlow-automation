📝 SUMMARY

This week's call packed a lot into two hours: deep dives from Patrick Chouinard on his Beacon/Clara research pipeline, Astra-driven website rebuild, and skill-management philosophy; a business-growth discussion with Juan Torres on his AI photo booth; Rod Morrison's return with questions on operationalizing agent workflows; a live demo of Ty Wells' interactive pitch app for his Bahamas ERP/CRM platform; and an introduction from new member Lisa Jetton. The second half turned into a rich round-robin on personal infrastructure — Proxmox setups, T3 Code environments, multi-orchestrator stacks, and an open-source visual LLM project — plus updates from Ryan C and Morgan. Beyond the specifics, the recurring theme (voiced by Patrick near the end) was that the group itself serves as a weekly "context upgrade": a fast-moving AI landscape is impossible for any one person to track alone, and this community is how we keep up. If you missed it live, the recaps below are worth your time.


💡 KEY INSIGHTS

Split your agent stack by concern: Patrick's "Beacon" does raw web research with zero personal context, then hands off to "Clara," which knows everything about him and turns it into a personalized morning briefing delivered via TTS/Discord.

Archive everything your agents produce. Patrick keeps full transcripts + audio of every briefing so he can feed prior outputs back in and continuously improve — a self-optimizing loop.

Let agents run autonomously with a clear role. Patrick had Astra (acting as "lead of a dev team") dispatch sub-agents and run ~17 hours on a website rebuild, only checking in when needed.

Heavy agent building burns tokens fast — Patrick and Ty both blew through $200-tier subscriptions within a week. Budget for it.

Turn your existing prompt templates into skills: decompose long templates into an "uber skill" that orchestrates sub-skills, add YAML frontmatter, and define which are callable vs slash commands.

Keep a permanent, account-level tech stack definition so Claude and your agents stop recommending inconsistent tools and default to your approved stack.

Embed business context into your tooling: Patrick's "Grill with Docs" tool cut spec-generation clarifying questions from ~70-80 down to ~15-20 — a major token and time saver.

Size work to the context window. Patrick's "Wayfinder" splits big projects into phases that fit one session, keeping the orchestrator's context small and reserving the big windows for the model doing the actual building.

Match model to task complexity: Sonnet for simple, well-scoped work; Opus for complex multi-system integration — with Fable routing automatically based on complexity.

Code-review with a different model family than the one that built the code (build with Claude, review with GPT, or vice versa) rather than assuming one model is universally better.

Consider GLM 5.3 on OpenRouter — Patrick reports quality between Sonnet and Opus at a fraction of the cost.

Benchmark before you buy: Paul suggests testing your preferred Claude models against a range of OpenRouter alternatives to find the cheapest model matching your quality bar. In regulated environments, note Patrick uses Claude + Copilot on AWS at his financial institution job since OpenRouter isn't viable there — and Rod flagged rising client scrutiny of AI tool compliance and data governance.

Build for analytics when pitching: Ty turned his ERP pitch into an interactive in-app slideshow specifically to capture click and engagement data static slides can't provide.

Try "UI in reverse": mock the UI first with no backend logic, then have an agent write code to satisfy the UI's implied contracts, then run an adversarial agent loop to confirm correctness. Ty used it across ~7 agents and ~1,400 screen iterations in about 5 hours.

Vertical + local beats generic SaaS: Ty's "The Island" ERP consolidates ~$50k of separate subscriptions into one platform built around Bahamas-specific compliance that US/EU/Canadian software doesn't cover.

Avoid lock-in in your homelab: Patrick Chouinard runs three Proxmox servers with Linux VMs and LXC containers, Mac workstation + Linux backend, all orchestrated by a Hermes agent.

Layer your memory: Patrick pairs OnShow as a dynamic memory layer with T3's basic memory — a $100 free credit covered ~six months of daily use.

Explore specialized harnesses: Patrick is testing Pi (open source) as a modifiable code-review harness, and Scott's "CC Black Box" IDE (open-sourced, Mac-only) ships with built-in simulators for driving Claude Code workflows — a nicer alternative to Cursor/VS Code.

Ship fast and SEO can follow quickly: Ryan C's estate agency site with CRM-like backend outranked long-established international competitors in local SEO within a week or two of launch.

Expect rapid prototyping, rapid discarding: as Morgan put it, the pace of AI-driven work means most completed work becomes "rapid prototype, rapid trash."

Old projects can be reborn with open models: Paul Miller is reinventing his 12-year visual shelf-recognition project using open-source visual LLMs to automate training data gathering and fine-tuning, comparing models and running fine-tunes on a Mac Mini or cloud GPU pods.

And the meta-lesson from Patrick: "There's too much for a single person to be aware of all the time... this group is basically how I do my Context Upgrade every week."


❓ KEY Q&A

Here are the Q&A highlights from this week's call:

Q (Juan Torres): As your news-generation agent accumulates many days of reports, do you worry about hitting model context limits, or would you use larger-context models to compensate?
A (Patrick): Execution is handled by a cheap model (Luna, ~900k-1M token context via Hermes) for news aggregation. Re-analyzing old news has limited value, so there's no need to vectorize or hold everything in context — the archive is mainly kept so he can replay the audio, not for reasoning over historical news.

Q (Rod Morrison): Is anyone still using ShipKit, and how?
A (Patrick): Not for building directly, but ShipKit templates are reformatted into skills — decomposed into an orchestrating "uber skill" plus sub-skills, with YAML frontmatter and defined calling conventions. Brendan is reportedly working on a similar ShipKit-to-skills conversion.

Q (Rod Morrison): Are skills hosted in Claude directly or on GitHub — do you have an internal marketplace?
A (Patrick): They use a private internal marketplace on Azure DevOps (migrating eventually to GitHub). It works with Claude Code and GitHub Copilot but not yet with Cowork/Claude AI features requiring a GitHub repo, which they're now setting up.

Q (Rod Morrison): Are you using Obsidian for that "department memory" concept?
A (Patrick): No — Obsidian doesn't scale to organization-level use since it lacks synchronization, diffing, and rollback. Instead they store context documents in a Git repo that syncs to everyone's machine each morning, invisible to end users.

Q (Rod Morrison): What models do people use once a spec is well-defined — just run Sonnet high?
A (Patrick): It's not one-size-fits-all; Fable evaluates task complexity. Sonnet handles simpler tasks fine, while complex, multi-system integration work goes to Opus. Splitting work into small enough pieces lets Sonnet handle a lot more than expected.

Q (Juan Torres): Do you combine Hermes with OpenRouter for personal projects, and can OpenRouter access top-tier Claude models?
A (Patrick): Yes, he's a heavy OpenRouter user for personal projects since AWS is more complex to configure for casual use. Hermes operates the OpenRouter API automatically. OpenRouter can access top Claude models, but at full pay-per-use pricing rather than subscription rates.

Q (Paul Miller): With the interactive pitch app, were you able to capture engagement data like viewers and click-throughs?
A (Ty Wells): Yes — that was the whole point of building it as an app instead of a slideshow. Shared links are tracked, giving him analytics a static slideshow couldn't provide, and people were still clicking through it live during the call.

Q (Lisa Jetton): What's the broader vision for your platform — is it like a brokerage connecting clients with infrastructure and funnels?
A (Ty Wells): The platform ("The Island") consolidates around $50,000 of previously separate subscriptions into one system for his Bahamas-based companies, built for local regulatory compliance needs not addressed by existing software. The launch date to release it to clients was today.

Q (Lisa Jetton): What harnesses/toolkits do people use, and how do they coordinate between tools?
A (Paul Miller): Many in the group started with ShipKit about a year ago but have since moved on. Paul now uses the T3 stack with multiple Claude and OpenAI subscriptions, using orchestrators to manage a program of work across projects and a separate focus per application stack.

Q (Patrick Chouinard): Did you deploy T3 code servers, or just install it locally?
A (Paul Miller): Not yet deployed — currently on his Mac Mini and Linux home servers. He plans to use the Mac for day-to-day work and a GPU-equipped box for overnight/slower tasks.

Q (Lisa Jetton): Has Patrick dabbled with ECC and compared it to Pi?
A (Patrick Chouinard): No, he hasn't tried ECC.

Q (Lisa Jetton): Have you configured Hermes's implicit learning/self-adopting skills, or stuck with defaults?
A (Patrick Chouinard): He uses OnShow as a dynamic memory layer alongside Hermes's basic memory, and found it very cost-effective — a $100 credit lasted ~6 months of near-daily use, with ~$79 still remaining.

Q (Paul Miller): Is Morgan (mdcatc) using GPT-6 yet?
A (mdcatc): Not yet — he only has the $20 Pro subscription (not the $100 tier) and hasn't had time to test it, though he plans to try it for small tasks.


🛠️ TOOLS AND CONCEPTS MENTIONED

Beacon – Patrick's custom research agent that scans the web daily for AI news contextualized to his projects.

Clara – Patrick's primary personal agent that contextualizes Beacon's raw reports and reformats them as a spoken briefing.

TTS model + Discord – Converts Clara's briefing text to audio and delivers it via Discord.

Traefik + Tailscale – Reverse proxy and VPN mesh used to expose Patrick's internal briefing archive externally and on mobile.

Hermes – Personal infrastructure/orchestration agent ("chief of staff") used by Patrick and Lisa; Ryan and Scott added telephone-calling capability.

Astra – Agentic coding tool used by Patrick and Ty for large autonomous build tasks; has usage tiers (light/medium/high).

Fable (4.8, 5, 5.1) – Orchestrator/build tool; Ryan reverted to 4.8 after finding 5 unusable; Patrick uses 5.1 for a training app.

ShipKit – Source of template prompts converted into reusable "skills"; an earlier-generation markdown-based tool the group used about a year ago.

Wayfinder – Patrick's process for splitting large projects into phase-sized contexts before "Grill with Docs."

Grill with Docs – Proprietary internal tool embedding business context to cut spec clarification questions.

Azure DevOps (ADO) – Private repository/marketplace hosting internal skills at Patrick's workplace.

GitHub / GitHub Copilot – Target migration platform for skills; used alongside Claude Code at work.

AWS (including Bedrock, API/MCP gateway) – Corporate backend infrastructure for Claude and Copilot at Patrick's employer.

OpenRouter – Multi-model API platform used for personal projects and benchmarking cost-effective models.

GLM 5.3 – Model on OpenRouter noted as quality between Sonnet and Opus at a fraction of the cost.

Claude Code / Sonnet / Opus – Claude family models discussed for task-complexity-based routing and separating build from review.

Codex – Used by Patrick alongside OpenRouter and Claude for personal work.

Cursor – IDE currently used by Juan; also referenced as a less favored alternative to CC Black Box.

Matt Pocock skills/methodology – Out-of-the-box skill framework (implement, simplify, code-review workflow) referenced by Rod.

Google Startup School / GCP – Program Rod mentioned signing up for.

Holochain – P2P/distributed tech (2D hash graph) mentioned by Lisa as her prior work background.

Arch Linux ecosystem / Omarky / CachyOS / Fedora – Linux distros Lisa discussed for her AI systems setup.

Perplexity Windows agent stack – Agent operating loop (model, harness, orchestrator, scheduler, local tools/MCP servers) mentioned in Beacon's briefing content.

Proxmox – Patrick's virtualization platform hosting Linux VMs and LXC containers across three home servers.

T3 Stack / T3 Code – Used by Paul and Patrick for application development and as a coding harness, split into dev/staging/prod zones.

OnShow – Paid dynamic memory layer service used alongside Hermes/T3 memory.

Agent Ops – Patrick's custom-built plugin/add-on for network monitoring.

Pi – Open-source agent being tested by Patrick as a specialized code-review harness.

ECC – Harness/toolkit mentioned by Lisa for comparison (not tested by Patrick).

CC Black Box – Scott's open-sourced Mac-only IDE with built-in simulators for driving Claude Code workflows.

Higgsfield – Video/image generation tool Ryan has been experimenting with.

GPT (Pro subscription) – Morgan's $20/mo tier; hasn't tested GPT-6 yet.

Raspberry Pi (router) – Used by Paul as a router for remote support and media streaming.

OMI / Omi.me – Wearable recording device mentioned by Ty Wells in chat.

Granola.ai – Computer-based meeting notetaker recommended by Ryan C as an alternative to a physical device.

Fieldy – Recording device (shop.fieldy.ai) shared by Patrick Chouinard in chat.

Fathom – Meeting notetaker/recorder used to capture and summarize the call.

Otter.ai – Meeting notetaker used by Lisa Jetton to transcribe the call.


📎 SHARED RESOURCES

Session recording (Fathom):
https://fathom.video/share/sTLHaj9eU9y5J4Uhc492BZpG1PCE6kyg

"The Island" — Ty Wells' interactive ERP/CRM pitch app:
https://islandflow.ai/overview#scene=cool-breeze&view=explore

CC Black Box — Scott's open-sourced IDE:
ccblackbox.app

Photo-magnets interview (referenced by Biggi Fraley):
https://www.youtube.com/watch?v=N0NceZbY2_4

Granola.ai — meeting notetaker:
https://www.granola.ai/

Fieldy — recording device:
https://shop.fieldy.ai/home

Juan Torres' Instagram demo post:
https://www.instagram.com/p/DcgyPGKNJls/

Savills New Zealand — example real-estate site shared by Paul Miller:
https://www.savills.co.nz/


🔄 FOLLOW-UPS WORTH EXPLORING

Open questions, follow-ups and commitments to revisit next week:

Patrick to expose the Beacon Morning Briefing archive externally via Traefik reverse proxy + Tailscale for mobile/remote access.

Juan to create a bespoke image-to-image style for a target venue, then email the venue director with a demo and free pilot offer.

Juan to build a landing page for his photo-booth application.

Juan to identify and join local country club/venue networks for outreach opportunities.

Juan to prepare a portable demo kit (phone + iPad) with a pre-recorded fallback demo for in-person venue visits.

Rod to evaluate GLM 5.3 on OpenRouter, establish Claude-based benchmarks, and run comparative OpenRouter model tests.

Ty and team to run a postmortem on the ERP platform launch the following morning.

Lisa Jetton to evaluate available harness options (T3 stack, Hermes, OpenRouter) and report back to the group next week.

Lisa Jetton to deploy T3 code servers on her Mac Mini and Linux server.

Paul Miller to deploy T3 code servers across his Mac Mini and Linux home servers, splitting day-to-day vs. overnight/GPU-based tasks.

Patrick Chouinard to continue developing Pi as a specialized harness for code review.

Morgan (mdcatc) to clean up and update his "World of Morgan portal" to showcase his work.

Ryan C to share his fitness-tracking app once development is complete.