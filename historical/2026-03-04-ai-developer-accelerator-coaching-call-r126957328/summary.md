## Meeting Purpose

[Share AI dev progress, solve technical challenges, and discuss strategy.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=1091.0)

## Key Takeaways

  - [**Agentic DevOps is a game-changer.** Patrick's setup uses Claude Code as a remote operator on VMs, enabling secure, mobile-based infrastructure management and refactoring projects in minutes.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=4054.0)
  - [**Side projects are the new R\&D.** Personal tools built to solve individual problems (e.g., Ryan's lead-gen app, Patrick's news pipeline) are proving to have unexpected commercial value.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=4868.0)
  - [**Teach AI as a collaborator.** The key skill for new users is providing full context, not just asking questions. Analogies (e.g., the "walled office" for Azure tenants) are essential for communicating with non-technical clients.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=5556.0)
  - [**Obsidian + Claude Code is a powerful "second brain."** This stack combines Obsidian's markdown simplicity with Claude Code's contextual awareness for efficient, AI-powered knowledge management.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=6761.0)

## Topics

### Agentic DevOps & Infrastructure Management

  - [**Patrick's Remote Operator Setup**](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=4054.0)
      - [**Problem:** Claude's remote control feature is limited to one session per machine.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=728.0)
      - [**Solution:** Use a Claude Code template to provision and harden new Ubuntu VMs.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=4080.0)
      - [**Workflow:**](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=4468.0)
        1.  [Start a Claude Code session in a `tmux` instance on the new VM.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=4468.0)
        2.  [Enable remote control (`/remote-control`).](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=4488.0)
        3.  [Disconnect from `tmux`, leaving the Claude session active.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=4468.0)
      - [**Result:** A secure, remote operator on each VM, accessible via the Claude mobile app.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=4146.0)
      - [**Benefit:** Enables secure, mobile-based infrastructure management (e.g., built a Prometheus/Grafana stack from a barbershop).](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=4380.0)
  - [**Juan's Agentic DevOps Experiment**](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=3788.0)
      - [Used Claude Code with AWS CLI permissions to provision EC2 instances, security groups, and networking.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=3788.0)
      - [Found it more effective than the Kuro CLI for agentic DevOps.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=3788.0)

### AI-Powered Workflows & Tools

  - [**Ryan's Lead-Gen App**](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=2950.0)
      - [**Idea:** Use Meta glasses to photograph company vans while driving.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=2979.0)
      - [**Workflow:** Image → AI research (directors, etc.) → Outreach email generation.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=2998.0)
      - [**Goal:** Create a SaaS product for cold-callers, starting with a mobile app and Meta glasses integration.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=2979.0)
  - [**Ty's On-Site Feature Builder**](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=2506.0)
      - [**Workflow:** Limitless device captures on-site requirements → Secure Claw (Ty's OpenClaw fork) builds the feature → Telegram notifications enable remote guidance.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=2506.0)
      - [**Result:** Features are nearly complete by the time Ty returns to his desk.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=2523.0)
  - [**Marc's Resume Ranker**](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=1114.0)
      - [Built a proof-of-concept HR tool using Dockling for RAG and a custom model to rank resumes.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=1114.0)
      - [**Recommendation:** Use small models (e.g., Gemma 1B) for learning, as they are cheaper and faster, and expose training edge cases more clearly.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=1351.0)

### Client Communication & Education

  - [**Andrew's Privacy Challenge**](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=5267.0)
      - [**Problem:** Expert witness clients are hesitant about using Azure services outside of Office 365, despite contractual security.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=5329.0)
      - [**Solution:** Use analogies to explain security.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=5556.0)
          - [**"Walled Home Office":** The Azure tenant is a secure office; M365 is the desk, other services are the closet.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=5556.0)
          - [**"Front/Garage Door":** Different entry points to the same secure storage.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=5659.0)
  - [**Elijah's AI Education Challenge**](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=6221.0)
      - [**Problem:** How to teach AI to new users, especially those accustomed to short queries.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=6221.0)
      - [**Solution:** Frame AI as a collaborator.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=6362.0)
          - [**Exercise:** Have students explain a project to each other, then use that full explanation as the prompt.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=6488.0)
          - [**Focus:** Automate tasks not worth mastering (e.g., CV writing), where AI provides a better outcome and explains its process.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=6650.0)

### Dev Stack & Tooling

  - [**Morgan's Static Site Stack**](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=1853.0)
      - [**Stack:** Astro + Wrangler (Cloudflare CLI) for a static site with potential D1/R2 integration.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=1853.0)
      - [**Rationale:** Astro is a fast, static-first framework. Wrangler is more effective with Claude Code than a GUI.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=1887.0)
      - [**Tip:** Use Svelte for interactive components without the full complexity of a Next.js app.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=2031.0)
  - [**Ryan's Video Transcoding**](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=2880.0)
      - [**Problem:** 4K video streaming is slow for clients with poor internet.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=2880.0)
      - [**Current Solution:** Cloudflare Stream for adaptive bitrate streaming.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=2880.0)
      - [**Alternative:** Use FFmpeg scripts, generated by Claude Code, for local, custom transcoding.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=3088.0)
  - [**Elijah's "Second Brain" Infrastructure**](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=6761.0)
      - [**Problem:** Choosing an infrastructure for a personal knowledge base.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=6761.0)
      - [**Recommendation:** Obsidian + Claude Code.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=6885.0)
          - [**Stack:** Obsidian (markdown notes) + Terminal plugin (to run Claude Code) + Git sync (for version control).](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=6885.0)
          - [**Benefit:** Claude Code has contextual access to the vault, acting as a dynamic query engine.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=7521.0)
          - [**Rationale:** Avoids the friction of complex databases like Supabase.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=6868.0)

## Next Steps

  - [**Marc:** Take the Google AI Generative Leader exam.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=586.0)
  - [**Ryan:** Implement Cloudflare Stream for adaptive video streaming; consider FFmpeg as an alternative.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=2880.0)
  - [**Andrew:** Use analogies to explain Azure security to clients.](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=5556.0)
  - [**Elijah:** Evaluate the Obsidian + Claude Code stack for a personal "second brain."](https://fathom.video/share/VWARzTMXLUisMc9247LdSrQNH4rsFipQ?tab=summary&timestamp=6761.0)

