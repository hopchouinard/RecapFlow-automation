## general

This was a small, informal coaching/show-and-tell session with Patrick Chouinard hosting, attended by Scott Rippey, Ty Wells, Juan Torres, Ryan C, and Morgan Cook (late). Patrick opened by sharing that he had recently lost his mother and noted that Claude had been remarkably useful in managing the administrative burden of the funeral process — forms, emails, and reminders — compressing what took two months for his father's passing into roughly 48 hours. He also described an ongoing 48-hour agentic loop using Claude Code's `/loop` command to refactor several disconnected tool repos into a single, well-structured project called Agent Ops, a harness for his Hermes-based home lab infrastructure.

Scott Rippey presented his AI-powered video production pipeline, which he used to launch a new YouTube channel called "Building With Reason." The pipeline chains Claude Code, Higgsfield (Nano Banana for images, Kling for animation), ElevenLabs (voice cloning with V3 engine), HeyGen (avatar generation), Remotion, and FFmpeg into a fully automated production workflow. He also teased a forthcoming demo of a model-agnostic code quality, security review, and observability system with a dashboard and git-hook integration.

Ty Wells shared two projects: an "intent queue" system that captures development intent when context is below 40% and replays it at the start of a fresh Claude session, and a conceptual "CodeTalk" project (working name) for having voice conversations about a codebase while mobile — using PipeCat — to generate intent capsules without directly modifying code. The group then had an extended discussion about Hermes and the Hermes Workspace UI, with Patrick demonstrating its Kanban board, Conductor agent-swarm feature, memory management, profiles/routing, MCP integration, and SSO via Authentik and Tailscale. Infrastructure topics including Proxmox, PBS, TrueNAS, and Infisical also came up in depth. Morgan Cook closed the session by sharing AirLLM, a Python library that loads large models layer-by-layer to run on memory-constrained consumer hardware.

## insights

- **Patrick:** Claude reduced the administrative workload of managing a parent's estate from ~2 months to ~48 hours by handling forms, emails, reminders, and reusing prior documentation — a surprising but highly practical use case for AI.
- **Patrick:** Running a human-validated `/loop` with an inner Codex validation loop at each iteration produces well-structured, well-documented code and surfaces issues that would otherwise only appear in production — at the cost of more tokens and slower iteration.
- **Scott:** When generating images via Claude Code into Nano Banana, having Claude write the prompts (rather than prompting the model directly in a UI) produces far more consistent and controllable results, including character consistency across regenerations.
- **Scott:** ElevenLabs V3 engine with a quick clone eliminates the intonation and sentence-ending issues present in V2 pro clones, making voice generation essentially hands-off once the script is ready.
- **Scott:** Using Kling video clips over HeyGen jump cuts (which occur every 2–3 minutes) creates a seamless viewing experience without visible edits.
- **Scott:** Building a gate/pre-check step into an agentic pipeline before presenting output to the human eliminates common recurring glitches and reduces back-and-forth.
- **Scott:** AI benchmarks are often measuring basic or poorly chosen tasks; real-world performance diverges significantly from published numbers.
- **Ty:** Capturing intent while context is "hot" (under 40% used) and queuing it as terse micro-language capsules allows cold-starting a new session without losing momentum or needing to re-explain state.
- **Ty:** A voice-based conversational interface to a codebase (read-only, no changes) is a useful pattern for mobile ideation — generating intent capsules that can later be fed into Claude Code.
- **Patrick:** Hermes supports multiple named agent profiles (default, workspace, reviewer, QA, orchestrator) that can each have distinct memory, personality, and behavior — enabling lightweight agent swarms from a single installation.
- **Patrick:** Running Hermes (or any agent platform) inside a Proxmox VM rather than on bare metal allows state snapshots, easy recovery, and live migration between nodes — significantly reducing recovery time after failures.
- **Patrick:** Using a single reverse proxy as the only Tailscale ingress point, with internal FQDNs mapped to individual machines, means Tailscale only ever sees one target while all internal services remain accessible by name.
- **Patrick:** With 512 GB of unified memory, the value isn't running frontier-class models — it's having enough headroom for a large context window alongside a 70B parameter model.
- **Morgan:** AirLLM loads LLM layers sequentially (one at a time) rather than all at once, allowing 32B+ models to run on consumer hardware with limited RAM.

## qa

**Q (Juan Torres):** Which model are you using for image generation?
**A (Scott Rippey):** All images go through Higgsfield using the Nano Banana model — thumbnails, characters, and reference images before animation. Kling is used for the video/animation layer.

**Q (Juan Torres):** How do you add the animated B-roll scenes — do you prompt a video model directly with a description?
**A (Scott Rippey):** The script is used as the reference. After reviewing the script manually, Scott directs Claude Code to generate specific scenes (e.g., "AI agent hitting a stop sign"). Claude Code calls Nano Banana for a reference image, then sends it to Kling with a prompt to animate it. Previews are rendered at 1080p for approval before final 4K output.

**Q (Juan Torres):** Does Claude Code have CLI access to Higgsfield?
**A (Scott Rippey):** Mostly MCP, though CLI is used where it works better depending on the integration.

**Q (Patrick Chouinard):** Why are you doing a dual-boot Windows/Ubuntu setup instead of using WSL?
**A (Juan Torres):** WSL runs on top of Windows and consumes extra CPU overhead. The goal is a clean Ubuntu environment without Windows processes running in the background, since Windows is too unreliable for the use case.

**Q (Juan Torres):** How does Proxmox work — do you set it up in BIOS?
**A (Patrick Chouinard):** Proxmox is itself a Linux-based OS. You install it from a USB ISO (downloaded from their website), boot from it, and it becomes the host. You then create VMs through its web interface or CLI. Claude Code can SSH into the machine and handle the full setup — templates, VM spawning, network service configuration — all as infrastructure as code.

**Q (Juan Torres):** How does the reverse proxy / Tailscale setup work — is it like a bastion server?
**A (Patrick Chouinard):** Yes, effectively. Tailscale connects to a single reverse proxy machine. That proxy maps internal FQDNs (e.g., `hermes.patchotech.lab`) to specific internal machines. All ingress flows through the proxy; individual machines are never directly exposed via Tailscale.

**Q (Scott Rippey):** Does Hermes support router-style classification — routing certain request types to different models automatically?
**A (Patrick Chouinard):** Yes, through "profiles." Each profile can have its own model, memory, personality, and behavior. Out-of-the-box profiles include default, workspace, reviewer, QA, and orchestrator, and custom ones can be built.

**Q (Scott Rippey):** Does Hermes do any sandboxing?
**A (Patrick Chouinard):** Not that he's aware of, but since all services run as back-end infrastructure (not executing local bash or code directly), sandboxing is less critical. The recommendation is to run it inside a VM anyway for state management.

**Q (Juan Torres):** Can Hermes leverage remote inference (e.g., a Mac running Ollama) rather than running models on the same machine?
**A (Patrick Chouinard):** Yes. Hermes supports both Ollama and LM Studio as inference backends via their APIs, so the inference box can be a separate machine on the network. Scott added that Ollama only runs GGUF models, while LM Studio also supports MLX — relevant for Apple Silicon users.

## tools

- **Claude Code** — Primary agentic coding environment used across all projects; `/loop` and `/goal` commands used for long-running autonomous tasks
- **Higgsfield** — $50/month platform providing API access to multiple AI models (Nano Banana, Kling); used as the hub for Scott's video pipeline
- **Nano Banana** — Image generation model accessed via Higgsfield; used for all still images, character creation, and animation reference frames
- **Kling** — Video/animation model accessed via Higgsfield; used to animate reference images and cover HeyGen jump cuts
- **ElevenLabs** — Voice cloning and TTS; V3 engine used for natural-sounding voice generation from script text
- **HeyGen** — Avatar video generation; takes a single uploaded photo and syncs it to audio to produce a talking-head video
- **Remotion** — Programmatic video composition; used to attach intros/outros and assemble final video
- **FFmpeg** — Audio/video processing; used for auto-leveling audio within the pipeline
- **Hermes** — Local AI agent framework; discussed as a replacement for OpenWebUI/IronClaw with multi-profile, memory, and skill support
- **Hermes Workspace** — Open-source UI layer on top of Hermes providing chat, dashboard, Kanban, Conductor (agent swarm), memory management, and cron scheduling
- **Proxmox** — Bare-metal hypervisor/OS for running VMs and LXC containers; Patrick's primary home-lab infrastructure platform
- **Proxmox Backup Server (PBS)** — Lightweight backup service for automated VM snapshots with configurable retention policies
- **TrueNAS** — NAS OS; suggested as shared storage backend for Proxmox to enable live VM migration between nodes
- **Tailscale** — Zero-config VPN; used for secure remote access to home-lab services
- **Authentik** — Open-source SSO/identity provider; used to front Hermes Workspace with OpenID-based authentication
- **Traefik** — Reverse proxy; used as the single Tailscale ingress point routing internal FQDNs to individual machines
- **Infisical** — Secrets management/vault; integrated with Hermes so API keys are never stored in local files
- **Ollama** — Local model runner (GGUF models); can serve as a remote inference backend for Hermes
- **LM Studio** — Local model runner supporting both GGUF and MLX models; alternative inference backend for Hermes
- **PipeCat** — Voice agent framework; Ty is using it for the CodeTalk voice-to-codebase project
- **AirLLM** — Open-source Python library that loads LLM layers sequentially to run large models on memory-constrained consumer hardware
- **Whisperflow** — Local speech-to-text; Patrick uses it for voice dictation instead of Hermes's built-in option
- **ChatGPT (voice mode)** — Ty uses it while driving to brainstorm and generate PRDs before feeding them into Claude Code
- **GitHub Copilot** — Mentioned briefly as a partial existing solution for conversational code interaction
- **WSL (Windows Subsystem for Linux)** — Discussed as an alternative to dual-boot; rejected by Juan due to overhead on top of Windows

## links

- **https://www.youtube.com/@BuildingwithReason** — Scott Rippey's new AI-focused YouTube channel featuring Pixar-style avatar videos
- **https://www.youtube.com/@ClaudiusPapirusYT** — YouTube channel written in Claude's voice; shared by Patrick as a related example of AI-persona content
- **https://github.com/outsourc-e/hermes-workspace** — Open-source Hermes Workspace UI project; provides web dashboard, Kanban, Conductor, memory management on top of Hermes
- **https://github.com/lyogavin/airllm** — AirLLM GitHub repo; Python library for running large models layer-by-layer on consumer hardware with limited RAM

## decisions

- **Patrick** will contact Brandon next week to ensure he is invited to the session (he was missed two weeks in a row).
- **Scott** will share his Claude PRD-generation project setup with Ty via email.
- **Scott** will investigate Hermes and Hermes Workspace as a potential replacement for his IronClaw setup.
- **Ty** will continue developing the CodeTalk (voice-to-codebase) project using PipeCat and local models on Proxmox.
- **Scott** will build his own version of a voice-based codebase conversation tool (inspired by Ty's CodeTalk concept).
- **Scott** will re-demo the video pipeline repo and the code quality/security observability system when a larger group is present (waiting for Brandon specifically).
- **Juan** will consider using Proxmox instead of dual-boot for his AI photo booth computers.
- **Ty** will reconnect his Synology NAS and explore running PBS on it.
- **Morgan** will share the AirLLM GitHub link in the chat (completed during the session) and test the library.
- **Patrick** will complete the Authentik migration in front of Hermes Workspace (was mid-migration during the call).