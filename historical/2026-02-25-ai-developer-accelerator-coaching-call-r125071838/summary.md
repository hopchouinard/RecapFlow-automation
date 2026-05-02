## Meeting Purpose

[Review AI projects, discuss development workflows, and strategize business models.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=874.0)

## Key Takeaways

  - [**Prioritize Business Model over Code:** For Jaylen's TopicLaunch, a recurring subscription for creator communities ($50–$99/mo) is a more stable and scalable model than one-off video requests.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=2287.0)
  - [**Secure AI Agents for Production:** Use isolated environments (e.g., Ubuntu VMs, Docker) and strict access controls (e.g., email whitelists, no outbound sending) to prevent prompt injection and unauthorized actions.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=1695.0)
  - [**Solve AI's Reliability Problem:** Ty's Usai project addresses the core challenge of AI-generated code: ensuring semantic correctness, not just syntactic validity, through a formal verification layer.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=3960.0)
  - [**Capitalize on Regulatory Pain Points:** Morgan's cemetery management system solves a critical compliance issue for Utah counties, creating a "painkiller" product with a clear path to multi-state SaaS.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=9487.0)

## Topics

### Business Strategy & Monetization

  - [**TopicLaunch (Jaylen):** A platform for creators to monetize video requests.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=2225.0)
      - [**Feedback:** The current one-off transaction model is unstable.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=2294.0)
      - [**Recommendation:** Pivot to a recurring subscription for creator communities.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=2294.0)
          - [**Value Prop:** A private space for fans to suggest and vote on video ideas.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=2294.0)
          - [**Pricing:** $50–$99/month per creator.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=2294.0)
          - [**Rationale:** Provides predictable revenue and incentivizes creator engagement.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=2294.0)
  - [**Cemetery Management System (Morgan):** A multi-tenant SaaS for cemeteries.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=8470.0)
      - [**Problem:** Utah counties are non-compliant with a Freedom of Information Act law, creating a critical pain point.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=8476.0)
      - [**Solution:** A system to manage plots, records, and compliance, with a visual D3.js diagram of cemetery layouts.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=8470.0)
      - [**Business Model:** A "painkiller" product with a clear path to multi-state SaaS.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=9487.0)
      - [**Urgency:** The market is ripe for rapid acquisition. A dedicated salesperson should be building a lead list of 100+ contacts now.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=9518.0)
      - [**Moat:** Compliance requirements (HIPAA, SOC 2) are a high barrier to entry for competitors.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=9900.0)

### AI Agent Security & Architecture

  - [**OpenClaw Agent Setup:** Two approaches for secure, autonomous agents.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=1695.0)
      - [**Patrick's Production-Grade Setup:**](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=1695.0)
          - [**Environment:** Dedicated Ubuntu VM on Proxmox.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=1864.0)
          - [**Access Control:** Email whitelisted to sender; calendar is agent-owned.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=1790.0)
          - [**Context Management:** Uses Discord channels to segment context and control token costs.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=1830.0)
      - [**Brandon's "Poor Man's" Setup:**](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=1695.0)
          - [**Environment:** Docker container on a local machine.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=1982.0)
          - [**Access Control:** Limited to a single Slack channel; no email or outbound sending.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=1712.0)
          - [**Rationale:** Prevents unauthorized actions (e.g., mass emails) by forcing human review of output.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=2026.0)
  - [**Marc's OpenClaw Use Cases:**](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=2873.0)
      - [**Trainer Email Automation:** Sends pre-formatted emails with calendar availability via a Telegram command.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=2873.0)
      - [**Job Search Agent:** Emails job listings from an API based on a category.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=2909.0)

### AI-Assisted Development Workflows

  - [**Morgan's WSL Discovery:**](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=8391.0)
      - [**Problem:** Claude Code was inefficient on Windows PowerShell, wasting tokens on syntax corrections.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=8391.0)
      - [**Solution:** Switched to WSL (Windows Subsystem for Linux).](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=8391.0)
      - [**Result:** Eliminated syntax errors and improved efficiency.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=8391.0)
  - [**Brandon's High-Velocity Workflow:**](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=3615.0)
      - [**Goal:** Maximize token generation and minimize human idle time.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=3615.0)
      - [**Tools:**](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=927.0)
          - [**Meta Quest 3:** For unlimited virtual screens to run 15+ Claude Code instances.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=931.0)
          - [**Warp:** A terminal emulator for rapid window management.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=5100.0)
          - [**Codex:** For high-precision, long-running tasks (e.g., 90-slide presentations).](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=4711.0)
  - [**Code Anvil Mobile (Scott):**](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=5942.0)
      - [**Project:** A mobile UI for a local Claude Code instance, secured by a Cloudflare tunnel.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=5942.0)
      - [**Purpose:** Allows remote task initiation and progress checks without full desktop access.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=5942.0)
      - [**Status:** Public repo available tomorrow.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=6280.0)

### New AI Projects & Concepts

  - [**Usai (Ty):** A formal verification layer for AI output.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=3960.0)
      - [**Problem:** AI models hallucinate (30–40% error rate).](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=3960.0)
      - [**Solution:** A "spell check for logic" that verifies semantic correctness, not just syntactic validity.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=3960.0)
      - [**Status:** Provisional patent filed.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=4006.0)
  - [**Fitness App (Marc):** A functional app built with AI assistance.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=204.0)
      - [**Key Feature:** A "dictate workout" function that parses natural language (e.g., "3 sets tricep pull downs for 50") and logs it to the database.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=253.0)
  - [**SOP System (Scott):** A planned system for AI-assisted SOP creation and management.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=6381.0)
      - [**Rationale:** The future workforce will have fewer humans and more agents, increasing the need for structured processes.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=6429.0)
      - [**Functionality:** Generates, versions, and allows querying of SOPs.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=6381.0)

## Next Steps

  - [**Jaylen:** Evaluate a subscription model for TopicLaunch to create a more stable revenue stream.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=2287.0)
  - [**Morgan:** Finalize the cemetery management system MVP, then launch a rapid go-to-market sprint with a dedicated salesperson.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=9510.0)
  - [**Scott:** Merge the `Code Anvil Mobile` update to the public repo by tomorrow.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=6280.0)
  - [**Ty:** Connect with Brandon offline to discuss the Usai project and AI reliability testing.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=4378.0)
  - [**Brandon:**](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=10140.0)
      - [Introduce Morgan to investors (e.g., TinySeed) once the first paying customer is secured.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=10140.0)
      - [Meet with Paul on Friday to advise on scaling multiple AI projects.](https://fathom.video/share/jswfHjC_6f-Bzuyej2xaNU1EyS4amJZz?tab=summary&timestamp=7399.0)

