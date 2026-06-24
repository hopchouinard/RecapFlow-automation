📝 SUMMARY

This week's session covered practical AI applications: compressing months of estate paperwork into 48 hours with Claude, fully automated video production pipelines, and sophisticated home lab orchestration via Proxmox. Topics included agentic coding with validation loops, voice-based codebase interaction, and local AI infrastructure management.

💡 KEY INSIGHTS

Claude compressed two months of estate paperwork into 48 hours by managing forms, emails, and reminders while reusing prior documentation.

For agentic coding, human-validated /loop with inner Codex validation at each iteration produces better structured code and surfaces issues pre-production, though at higher token cost and slower speed.

Claude-written prompts for image generation (via Higgsfield/Nano Banana) produce more consistent results than direct UI prompting, maintaining character consistency across regenerations.

ElevenLabs V3 with quick cloning eliminates V2 intonation artifacts, making voice generation hands-off once scripts are prepared.

Video generation (Kling) covering avatar jump cuts creates seamless viewing experiences without visible edits.

Gate or pre-check steps in agentic pipelines eliminate recurring glitches and reduce back-and-forth iterations.

Capture development intent as terse micro-language capsules when context drops below 40% to cold-start fresh Claude sessions without losing momentum.

Voice-based conversational interfaces to codebases (read-only) enable mobile ideation, generating intent capsules for later use in Claude Code.

Hermes supports agent swarms via named profiles (default, workspace, reviewer, QA, orchestrator) with distinct memory and behavior.

Proxmox VMs enable state snapshots, easy recovery, and live migration, reducing recovery time versus bare metal.

Single reverse proxy as the only Tailscale ingress point with internal FQDN mapping minimizes exposure while maintaining accessibility.

512 GB unified memory primarily enables large context windows alongside 70B models rather than frontier-class models.

AirLLM runs 32B+ models on consumer hardware by loading layers sequentially rather than all at once.

❓ KEY Q&A

Q: Which model for image generation?
A: Higgsfield using Nano Banana for stills and characters; Kling handles video and animation.

Q: How to add animated B-roll?
A: Claude Code generates scene descriptions from scripts, calls Nano Banana for reference images, then sends to Kling. Previews render at 1080p before final 4K output.

Q: Why dual-boot Windows/Ubuntu instead of WSL?
A: Clean Ubuntu avoids Windows CPU overhead and background processes for better reliability on intensive tasks.

Q: How does Proxmox work?
A: Linux-based host OS installed from USB ISO. Create VMs via web UI or CLI. Claude Code can SSH in to handle complete infrastructure-as-code setup including templates and networking.

Q: How does the reverse proxy and Tailscale setup work?
A: Functions as a bastion server. Single Tailscale connection to reverse proxy maps internal FQDNs to specific machines. All ingress flows through proxy while individual machines remain unexposed.

Q: Does Hermes support automatic request routing to different models?
A: Yes, via profiles with distinct models, memory, and behavior. Built-in profiles: default, workspace, reviewer, QA, and orchestrator.

Q: Does Hermes do sandboxing?
A: Not currently. Since services run as back-end infrastructure rather than executing local code directly, sandboxing is less critical. VM isolation recommended regardless.

Q: Can Hermes leverage remote inference?
A: Yes, supports Ollama and LM Studio via APIs, allowing separate inference machines. Ollama runs GGUF; LM Studio also supports MLX for Apple Silicon.

🛠️ TOOLS AND CONCEPTS MENTIONED

Claude Code — Agentic coding environment with /loop and /goal commands for long-running autonomous tasks.

Higgsfield — $50/month platform providing API access to Nano Banana and Kling.

Nano Banana — Image generation for stills, characters, and animation reference frames.

Kling — Video and animation model for animating reference images and creating B-roll.

ElevenLabs — Voice cloning and TTS platform with V3 engine for natural voice generation.

HeyGen — Avatar video generation syncing photos to audio for talking-head videos.

Remotion — Programmatic video composition for intros, outros, and final assembly.

FFmpeg — Audio/video processing for auto-leveling within pipelines.

Hermes — Local AI agent framework with multi-profile support, memory, and skill integration.

Hermes Workspace — Open-source UI providing chat, dashboard, Kanban, Conductor swarms, memory management, and cron scheduling.

Proxmox — Bare-metal hypervisor and OS for VMs and LXC containers.

Proxmox Backup Server — Lightweight backup service for automated VM snapshots.

TrueNAS — NAS OS as shared storage backend for Proxmox live migration.

Tailscale — Zero-config VPN for secure remote access to home-lab services.

Authentik — Open-source SSO and identity provider for OpenID authentication.

Traefik — Reverse proxy as single Tailscale ingress point routing internal FQDNs.

Infisical — Secrets management vault integrated with Hermes.

Ollama — Local GGUF model runner as remote inference backend.

LM Studio — Local model runner supporting GGUF and MLX for Apple Silicon.

PipeCat — Voice agent framework for voice-to-codebase conversation.

AirLLM — Python library loading LLM layers sequentially to run large models on consumer hardware.

Whisperflow — Local speech-to-text for voice dictation.

📎 SHARED RESOURCES

https://www.youtube.com/@BuildingwithReason — Scott Rippey's AI-focused YouTube channel with Pixar-style avatar videos.

https://www.youtube.com/@ClaudiusPapirusYT — YouTube channel written in Claude's voice as AI-persona content example.

https://github.com/outsourc-e/hermes-workspace — Open-source Hermes Workspace UI with dashboard, Kanban, Conductor, and memory management.

https://github.com/lyogavin/airllm — AirLLM repository for running large models layer-by-layer on consumer hardware.

🔄 FOLLOW-UPS WORTH EXPLORING

Scott will share his Claude PRD-generation setup with Ty and investigate Hermes Workspace as a replacement for IronClaw.

Ty will continue developing CodeTalk voice-to-codebase using PipeCat and local models on Proxmox, and explore running Proxmox Backup Server on his Synology NAS.

Scott will build a voice-based codebase conversation tool and re-demo the video pipeline plus security observability system to a larger group.

Juan will consider Proxmox instead of dual-boot for AI photo booth computers.

Patrick will complete the Authentik migration via Hermes Workspace and ensure Brandon receives session invitations.

Morgan will test AirLLM and share findings.