📝 SUMMARY

This week's intimate coaching session covered remarkable practical applications of AI, from compressing months of estate administration into 48 hours using Claude, to fully automated video production pipelines, and sophisticated home lab infrastructure orchestration. Patrick Chouinard shared how agentic coding and local AI frameworks are transforming both personal administrative tasks and complex infrastructure management, while Scott Rippey demonstrated an end-to-end automated video generation workflow and Ty Wells introduced innovative approaches to capturing development intent and voice-based codebase interaction.

💡 KEY INSIGHTS

Claude can reduce emotionally difficult administrative burdens dramatically — Patrick compressed two months of estate paperwork into 48 hours by having Claude manage forms, emails, and reminders while reusing prior documentation.

For agentic coding, running a human-validated /loop with an inner Codex validation layer at each iteration produces significantly better structured and documented code, surfacing issues pre-production rather than post-deployment, though at higher token cost and slower speed.

In creative workflows, having Claude write prompts for image generation models produces far more consistent and controllable results than prompting directly in a UI, including maintaining character consistency across regenerations.

ElevenLabs V3 engine with quick cloning eliminates the intonation and sentence-ending artifacts present in V2, making voice generation essentially hands-off once scripts are prepared.

Using video generation (Kling) to cover avatar jump cuts creates seamless viewing experiences without visible edits every 2–3 minutes.

Building a gate or pre-check step into agentic pipelines before human review eliminates recurring glitches and reduces back-and-forth iterations.

Capturing development intent as terse micro-language capsules when context drops below 40% allows cold-starting fresh Claude sessions without losing momentum or requiring state re-explanation.

Voice-based conversational interfaces to codebases (read-only, no changes) enable productive mobile ideation, generating intent capsules that can later feed into Claude Code.

Hermes supports lightweight agent swarms through multiple named profiles (default, workspace, reviewer, QA, orchestrator) each with distinct memory, personality, and behavior from a single installation.

Running agent platforms inside Proxmox VMs rather than bare metal enables state snapshots, easy recovery, and live migration between nodes, significantly reducing recovery time after failures.

Using a single reverse proxy as the only Tailscale ingress point, with internal FQDNs mapped to individual machines, keeps Tailscale exposure minimal while maintaining internal service accessibility.

With 512 GB of unified memory, the primary value lies not in running frontier-class models but in maintaining large context windows alongside 70B parameter models.

AirLLM enables running 32B+ models on consumer hardware by loading LLM layers sequentially rather than all at once, bypassing RAM limitations.

❓ KEY Q&A

Q: Which model are you using for image generation?
A: All images go through Higgsfield using the Nano Banana model for thumbnails, characters, and reference images. Kling handles the video and animation layer.

Q: How do you add animated B-roll scenes?
A: The script serves as reference. After manual review, Claude Code generates specific scene descriptions, calls Nano Banana for reference images, then sends them to Kling for animation. Previews render at 1080p for approval before final 4K output.

Q: Why use dual-boot Windows/Ubuntu instead of WSL?
A: WSL runs on top of Windows consuming extra CPU overhead. A clean Ubuntu environment without background Windows processes provides better reliability for intensive tasks.

Q: How does Proxmox work?
A: Proxmox is a Linux-based OS installed from USB ISO. Once installed as the host, you create VMs via web interface or CLI. Claude Code can SSH in and handle complete setup including templates, VM spawning, and network configuration as infrastructure as code.

Q: How does the reverse proxy and Tailscale setup work?
A: It functions like a bastion server. Tailscale connects to a single reverse proxy machine that maps internal fully qualified domain names to specific internal machines. All ingress flows through this proxy while individual machines remain unexposed.

Q: Does Hermes support automatic request routing to different models?
A: Yes, through profiles. Each profile can have distinct models, memory, personality, and behavior. Built-in profiles include default, workspace, reviewer, QA, and orchestrator, with support for custom configurations.

Q: Does Hermes do sandboxing?
A: Not currently, though since services run as back-end infrastructure rather than executing local bash or code directly, sandboxing is less critical. Running inside a VM is recommended for state management regardless.

Q: Can Hermes leverage remote inference rather than local models?
A: Yes, Hermes supports both Ollama and LM Studio as inference backends via their APIs, allowing the inference machine to be separate from the Hermes host. Note that Ollama runs GGUF models while LM Studio also supports MLX for Apple Silicon.

🛠️ TOOLS AND CONCEPTS MENTIONED

Claude Code — Agentic coding environment with /loop and /goal commands for long-running autonomous tasks.

Higgsfield — $50/month platform providing API access to multiple AI models including Nano Banana and Kling.

Nano Banana — Image generation model used for still images, character creation, and animation reference frames.

Kling — Video and animation model used to animate reference images and create seamless B-roll.

ElevenLabs — Voice cloning and text-to-speech platform, with V3 engine providing natural-sounding voice generation.

HeyGen — Avatar video generation that syncs uploaded photos to audio for talking-head videos.

Remotion — Programmatic video composition for attaching intros, outros, and assembling final videos.

FFmpeg — Audio and video processing tool used for auto-leveling audio within pipelines.

Hermes — Local AI agent framework with multi-profile support, memory, and skill integration.

Hermes Workspace — Open-source UI layer providing chat, dashboard, Kanban boards, Conductor agent swarms, memory management, and cron scheduling.

Proxmox — Bare-metal hypervisor and OS for running VMs and LXC containers.

Proxmox Backup Server — Lightweight backup service for automated VM snapshots with configurable retention.

TrueNAS — NAS operating system suggested as shared storage backend for Proxmox to enable live VM migration.

Tailscale — Zero-configuration VPN for secure remote access to home-lab services.

Authentik — Open-source SSO and identity provider used for OpenID-based authentication.

Traefik — Reverse proxy used as the single Tailscale ingress point routing internal FQDNs to individual machines.

Infisical — Secrets management vault integrated with Hermes to keep API keys out of local files.

Ollama — Local model runner for GGUF models serving as remote inference backend.

LM Studio — Local model runner supporting both GGUF and MLX models for Apple Silicon.

PipeCat — Voice agent framework used for voice-to-codebase conversation projects.

AirLLM — Python library loading LLM layers sequentially to run large models on memory-constrained consumer hardware.

Whisperflow — Local speech-to-text used for voice dictation.

📎 SHARED RESOURCES

https://www.youtube.com/@BuildingwithReason — Scott Rippey's new AI-focused YouTube channel featuring Pixar-style avatar videos.

https://www.youtube.com/@ClaudiusPapirusYT — YouTube channel written in Claude's voice, shared as an example of AI-persona content.

https://github.com/outsourc-e/hermes-workspace — Open-source Hermes Workspace UI project providing web dashboard, Kanban, Conductor, and memory management.

https://github.com/lyogavin/airllm — AirLLM GitHub repository for running large models layer-by-layer on consumer hardware.

🔄 FOLLOW-UPS WORTH EXPLORING

Scott will share his Claude PRD-generation project setup with Ty via email and investigate Hermes Workspace as a potential replacement for his IronClaw setup.

Ty will continue developing the CodeTalk voice-to-codebase project using PipeCat and local models on Proxmox, and will reconnect his Synology NAS to explore running Proxmox Backup Server on it.

Scott will build his own version of a voice-based codebase conversation tool inspired by Ty's concept, and will re-demo the video pipeline repo plus the code quality and security observability system when a larger group is present.

Juan will consider using Proxmox instead of dual-boot for his AI photo booth computers to simplify management.

Patrick will complete the Authentik migration in front of Hermes Workspace and ensure Brandon receives invitations to future sessions.

Morgan will test the AirLLM library and share findings with the group.