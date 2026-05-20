## general

This was a weekly group coaching call hosted by Patrick Chouinard (pchouinard), bringing together a regular cohort of AI-assisted developers and practitioners from various backgrounds and locations. The session followed a round-robin format where each participant shared what they had been working on and could ask questions of the group.

The first portion of the call addressed two career-transition questions: Eric Tsai, a statistician/data scientist with a PhD in Applied Math seeking to pivot into AI engineering, and Fitz, a DevOps/AWS infrastructure professional with similar ambitions. Both received substantive advice about leveraging domain expertise rather than trying to replace it with software engineering skills. The group emphasized that the ability to validate AI-generated output in one's own domain is the most critical skill for the emerging AI engineering role.

The second portion was a series of project showcases. Ty Wells presented three projects: SwingTrack (a golf swing analysis wearable system), ConchPass (a vendor-vetting platform for cruise ship passengers in the Bahamas), and ShipSafe (a cybersecurity MCP tool that checks code for vulnerabilities at generation time). Juan Torres walked through his AI Photo Booth application's complex browser-compatibility and egress architecture using AWS CloudFront. Morgan Cook discussed Google Apps Script automations for a foundation client. Mitch McCauley showed a YouTube content production management UI and raised questions about version control for non-technical teams. Patrick closed by sharing two concepts he is developing: a portable dual-format (HTML+Markdown) artifact file type for agentic workflows, and an adversarial code review skill for a Claude Code training session.

Throughout the call, a recurring meta-discussion emerged around adversarial AI workflows — using Claude for architecture/brainstorming and GPT/Codex for review, keeping context windows separate to avoid pollution, and the emerging need for an SDLC for natural language artifacts, including security concerns around prompt injection in shared skills.

## insights

- **Domain expertise is the most valuable asset for AI engineering transitions.** The ability to evaluate whether AI-generated output is correct in your field (statistics, infrastructure, etc.) is rarer and more valuable than knowing how to call an API. (Patrick Chouinard, Ty Wells)
- **Build projects in your own domain first.** When learning AI-assisted development, start with something you can validate — e.g., a statistician should build an A/B testing tool, not a generic SaaS app. (Patrick Chouinard)
- **AI coding tools are now better than ~90% of software engineers at debugging**, but you still need to understand architecture and structure to guide them effectively. (Patrick Chouinard)
- **Agentic DevOps is an underserved niche.** Everyone is talking about agentic coding, but almost no one is teaching agentic DevOps — a potentially powerful specialization. (Juan Torres)
- **Infrastructure-as-code is a natural fit for AI harnesses.** Claude Code and Codex can handle Terraform, Ansible, and AWS CLI tasks well; the value of an infrastructure engineer is knowing whether what the AI did is secure and correct. (Patrick Chouinard, Tom Welsh, Ty Wells)
- **Adversarial code review should use a different model and a fresh context window.** Using the same model that generated the code introduces bias; using a different model (e.g., Claude generates, GPT reviews) and a separate context avoids context pollution. (Patrick Chouinard)
- **Patrick's workflow: Claude for architecture/brainstorming, GPT/Codex for review.** Claude is a better architect and more creative; GPT follows a plan more precisely once it exists. (Patrick Chouinard)
- **Personality blocks in agent.md/claude.md reduce sycophancy** in AI coding assistants, leading to more honest and useful responses. (Patrick Chouinard)
- **Lovable and similar no-code tools are too hands-off for learning.** Tools like Cursor, Claude Code, and Codex show you the code being generated, which builds understanding organically. (Patrick Chouinard)
- **The Superpower plugin guides users through the full SDLC** — brainstorming, architecture, implementation, code review, Git branching, and PRs — making it useful for those new to AI-assisted development. (Patrick Chouinard)
- **Claude-P sub-agent calls now count against API quota**, not the subscription. $200 of API calls goes fast; Codex's $20/month plan has comparatively generous limits. (Patrick Chouinard, Bastian Venegas)
- **Prompt injection in shared skills is a real security threat.** Natural language artifacts can contain hidden Base64-encoded instructions targeting AI systems; no commercial antivirus equivalent exists yet for this. (Patrick Chouinard)
- **The "cake method" for training:** show the finished result first, then walk through how it was built — avoids waiting for live AI generation during time-limited sessions. (Patrick Chouinard / Ty Wells discussion)
- **For non-technical teams sharing code, GitHub org + forks provides isolation** without adding too much complexity — contributors can't break the main project, and updates can still flow through GitHub's native mechanics. (Patrick Chouinard)
- **Stripe callbacks/webhooks are the most common failure point** when integrating payment processing; test them thoroughly. (Ty Wells)

## qa

**Q (Eric Tsai):** I have 20+ years as a statistician/data scientist. AI engineering job descriptions look like software engineering roles. How do I transition and build confidence to apply by end of year?
**A (Patrick Chouinard):** Your ability to evaluate AI output in your domain is the most valuable skill — don't discount it. Build projects in areas you already understand (e.g., A/B testing tools) so you can validate the AI's work. Learn to guide AI agents architecturally; you won't need to write the nitty-gritty code. Use a tool like Superpower to walk you through the SDLC. Practice is the only path — start with small, completable projects.

**Q (Eric Tsai):** Don't you need to understand software engineering deeply to guide AI on architecture?
**A (Patrick Chouinard):** Yes, you need to understand what a front-end and back-end are and how they communicate, but not the specific implementation details. That understanding comes organically through practice. You become a manager of virtual agents more than a software developer per se.

**Q (Adam):** Have you considered staying closer to mathematics/ML rather than full-stack software development, given your background?
**A (Bastian Venegas):** Yes — classical ML (CNNs, RNNs) applied to audio and video is an area where generative AI struggles and where deep math knowledge creates real competitive advantage. Safety compliance systems (e.g., PPE detection for miners) are a concrete example where domain + ML knowledge is highly valued and well-compensated.

**Q (Fitz):** I come from AWS/DevOps/CI-CD. How do I pivot to AI engineering?
**A (Patrick Chouinard):** Use AI to amplify what you already know. Claude Code and Codex are excellent operators in the CLI world — the infrastructure world. Your value is validating whether what the AI does is secure and follows best practices, which a generic AI developer cannot do. There is also a Google Cloud Platform CLI that recently launched that could be useful.

**Q (Tom Welsh):** For adversarial review, do you use different coding models or different IDEs?
**A (Patrick Chouinard):** Use different models to avoid model bias — if you code with Claude, do the adversarial review with ChatGPT/Codex, and vice versa. Always use a separate conversation to avoid context pollution. GPT is generally better at adversarial review; Claude is better at architecture and brainstorming.

**Q (Juan Torres):** How do you get the two AI systems to read each other's work without sharing context?
**A (Patrick Chouinard):** Open both in the same repo. Give Codex the Git diff/commit list and ask it to do a savage adversarial review. Save that report as a file, then give that file to Claude and say "Codex found these issues." The code is the shared source; the conversation histories remain separate.

**Q (Bastian Venegas):** Why do you use Superpower for brainstorming in Claude rather than Codex?
**A (Patrick Chouinard):** Claude is a better architect and more creative/outside-the-box thinker. Once a plan exists, GPT follows it more precisely. So Claude + Superpower for design, Codex for implementation review.

**Q (Patrick Chouinard):** Is the adversarial review skill concept too complex for an introductory training session?
**A (Ty Wells / Patrick Chouinard discussion):** No — start with the end result (broken code and its consequences), work backwards. Use the "cake method": table-walk the skill construction, then cut to a pre-completed session to show the result, avoiding live wait time. This also lets you demonstrate session renaming and resuming in one go.

**Q (Mitch McCauley):** My non-technical team doesn't use GitHub. How do I manage version control and code sharing with them safely?
**A (Patrick Chouinard):** Create a GitHub org, have them fork your repo, and put an instruction file at the root for AI to help them update their fork. Whatever they break stays in their fork. Adam added: Codex's web interface can handle branch creation, PRs, and pushes automatically, with you as the code owner approving PRs.

**Q (Mitch McCauley):** Is there a security risk in copying skills from external sources?
**A (Patrick Chouinard):** Yes — prompt injection is a real threat. Malicious instructions can be embedded in natural language artifacts in ways that look innocuous to humans but direct AI to take harmful actions (e.g., data exfiltration). Base64-encoded strings can hide instructions entirely. No commercial antivirus equivalent exists yet for natural language artifacts.

## tools

- **Claude Code** — Primary AI coding harness used by most participants for implementation and architecture
- **Codex (OpenAI)** — Used as adversarial reviewer and for plan review; noted for generous usage limits at $20/month
- **Cursor** — IDE with AI integration used by Tom Welsh, Ryan C, and others; supports multiple models
- **Superpower (plugin)** — Patrick's recommended plugin for guiding users through the full SDLC within Claude Code
- **Claude-P** — Sub-agent spawning mechanism in Claude Code; now billed against API quota rather than subscription
- **Stripe** — Payment processing discussed for Marc's nonprofit donation site; has CLI and MCP integration
- **PayPal** — Discussed as alternative to Stripe for donations; Bastian had negative experiences with fund holds
- **Clerk** — Mentioned as a Stripe wrapper that simplifies payment integration
- **Next.js** — Marc's frontend framework for the historic foundation website
- **Sanity.io** — CMS used alongside Next.js for the foundation site's content management
- **Alpaca** — Paper trading platform Marc uses to test his AI stock trader ($100K simulated portfolio)
- **ChatGPT / GPT models** — Used for adversarial review, garden monitoring, and as Claude alternative
- **Ableton Live** — DAW Bastian is building a songwriter co-pilot tool for
- **Lovable** — No-code AI app builder; discussed as too hands-off for learning AI engineering
- **Whimsical** — Juan's whiteboard/diagramming tool for decision trees and architecture diagrams
- **AWS CloudFront** — Juan uses it for media egress from S3, decoupled from EC2 instance for cost efficiency
- **AWS EC2** — Juan's compute layer (T3 x-large) for his AI Photo Booth app
- **Amazon S3** — Data lake for Juan's photo booth images
- **Terraform** — Infrastructure-as-code tool; Juan generates it via Claude Code without writing it manually
- **Flask** — Juan recommends it for data web applications and displaying agentic system outputs
- **Google Apps Script** — Morgan's automation layer for a foundation client using Google Workspace
- **Google Looker / Looker Studio** — Mitch demonstrated it as a dashboard/reporting layer over Google Sheets data
- **Firebase** — Mentioned as a potential database upgrade path for Morgan's Google Workspace client
- **Kling** — Video generation model mentioned by Mitch; noted for occasionally generating celebrity likenesses
- **GPT Image 2 (GPT-2 image model)** — Praised by Ty and Mitch for high-quality realistic image generation
- **Wavespeed** — API aggregator for image/video generation models (GPT Image 2, Gemini, etc.); has its own CLI
- **OpenRouter** — Mitch's considered alternative to Wavespeed for model API access
- **N8N / Zapier** — Mentioned briefly as agentic orchestration tools (Patrick asked if Juan used them)
- **Ngrok** — Juan suggested it for tunneling staging environments to share with team members
- **GitHub Actions** — Recommended for automating local-to-staging deployment pipelines
- **Digital Ocean** — Mitch uses a droplet with a fixed IP for routing data provider requests
- **Synergy** — Morgan shared it as a virtual KVM switch for multi-machine setups
- **Deskflow** — Adam's alternative to Synergy; required switching from Wayland to X11 for clipboard support
- **Mentra Glass** — YC-backed smart glasses with open SDK; Bastian suggested Ty consider it for SwingTrack camera
- **Meta Smart Glasses** — Discussed as potential camera source for SwingTrack wearable
- **ShipSafe** — Ty's cybersecurity MCP tool that checks code for vulnerabilities at generation time
- **SwingTrack** — Ty's golf swing analysis system combining wearables (gyro wristband, cap camera, club reflectors) with AI
- **ConchPass** — Ty's vendor-vetting platform for cruise ship passengers in the Bahamas
- **Anthropic SkillJar** — Mitch shared Anthropic's official Claude Code training course link
- **Google Cloud Platform CLI** — Patrick mentioned a recently released CLI that could help with GCP infrastructure automation
- **Astro** — Mentioned as a long-term solution for markdown-to-HTML rendering
- **HTMX** — Mentioned alongside Astro as a modern alternative to bloated markdown parsers

## links

- https://github.com/googleworkspace/cli — Google Workspace CLI tool Patrick shared for Fitz as an AI harness resource
- https://x.com/MentraGlass — Mentra smart glasses Twitter/X account shared by Bastian for Ty's SwingTrack project
- https://www.ycombinator.com/companies/mentra — YC company page for Mentra (open SDK smart glasses)
- https://shipsafe.franklabs.io/ — Ty's ShipSafe cybersecurity MCP tool
- https://swingtrack-nu.vercel.app/ — Ty's SwingTrack golf swing analysis app
- https://conchpass.com/ — Ty's ConchPass vendor-vetting platform for cruise destinations
- https://symless.com/synergy — Synergy virtual KVM switch; Morgan shared for Adam's multi-monitor setup
- https://cloud.google.com/looker — Google Looker (enterprise BI); Patrick shared for Morgan's dashboard discussion
- https://lookerstudio.google.com/ — Looker Studio (free version); Mitch shared as the tool he demonstrated
- https://arena.ai/leaderboard/text-to-image/pareto — Text-to-image model leaderboard Juan shared for Mitch's image generation research
- https://wavespeed.ai/dashboard — Wavespeed multi-model API platform Juan recommended to Mitch
- https://www.youtube.com/watch?v=S9EGx6ik-18&t=1924s — Theo's video on markdown-to-HTML and related tooling issues; Mitch shared for Patrick
- https://anthropic.skilljar.com/claude-code-in-action — Anthropic's official Claude Code training course; Mitch shared for Patrick's training development

## decisions

- **Patrick Chouinard** will finalize the Community Brain Project packaging to ensure it deploys on Windows, Linux, and Mac.
- **Patrick Chouinard** will complete and open-source a portable dual-format HTML+Markdown artifact file type for agentic workflows once it is tangible enough to share.
- **Patrick Chouinard** will build an adversarial code review skill demo using the "cake method" (pre-completed session + table walkthrough) for an upcoming one-hour Claude Code training session.
- **Patrick Chouinard** will review Ty's ShipSafe tool more deeply, as it overlaps with security evaluation content he is building for training.
- **Ty Wells** will meet with hardware design partners the following day to advance the physical SwingTrack device.
- **Ty Wells** will explore open SDK smart glasses (Mentra, Google Glasses) as a potential camera source for SwingTrack, following Bastian's suggestion.
- **Ty Wells** will invite community members to the cybersecurity school community where ShipSafe is available free of charge — interested members should email him.
- **Juan Torres** will investigate making the AI Photo Booth app available as an iPhone app, prompted by Patrick's interest for a company Christmas party.
- **Mitch McCauley** will present the AI-assisted Amazon data analysis workflow to his team the following day, using a GitHub org + fork structure to isolate non-technical contributors from the main branch.
- **Morgan Cook** will look into Looker Studio as a dashboard layer for the foundation client's Google Sheets data, following Mitch's recommendation.
- **Marc Juretus** will meet with the historic foundation client the following evening to determine whether to reuse their existing payment integration or switch to Stripe/another provider.
- **Brandon Hancock** will host the following week's call and plans to share updated workflows and lessons learned.