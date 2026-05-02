## Meeting Purpose

[A roundtable on recent AI development projects and tools.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=900.0)

## Key Takeaways

  - [**New Dev Stack:** Patrick demoed a powerful new stack: `CoWork` for project management, `CMUX` for terminal multiplexing, and new `Cloud Code` plugins for status and `CMUX` integration.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=943.0)
  - [**Complex Data Handling:** Morgan's "Heritage Plot" app uses a `Next.js` UI to manage complex cemetery data, including variable plot structures and documents with granular access controls (e.g., public vs. FOIA-only).](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=2497.0)
  - [**Production Readiness:** Agentic systems are just software; production readiness requires standard SDLC practices (security, monitoring) plus specific handling for their non-deterministic nature, treating them like "users."](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=5286.0)
  - [**Key Tools:** `StageHand` (open-source browser automation), `OneCLI` (agent API gateway), and `Pencil.dev` (Figma competitor with strong agent integration) were highlighted as valuable tools.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=1722.0)

## Topics

### Agentic Production Readiness

  - [**Question:** What makes an agentic solution production-ready?](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=5286.0)
  - [**Consensus:** Apply standard SDLC practices (security, access rights, monitoring, pipelines).](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=5348.0)
  - [**Key Insight:** Treat the agent as a non-deterministic actor, like a user, to manage its inherent unpredictability.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=5487.0)
  - [**Resource:** The Vectera repository was shared, which documents a list of agent failures.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=5487.0)

### Patrick's New Dev Stack

  - [**`CoWork` for Project Management:**](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=943.0)
      - [Used as a Project Manager, not a code generator.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=1085.0)
      - [Employs a "workspace" methodology: a top-level directory with a `Cloud.md` file pointing to memory files (people, context, project).](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=1007.0)
      - [**Limitation:** Local sessions are vulnerable to corruption; a backup system is in development.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=960.0)
  - [**`CMUX` Terminal Environment:**](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=1176.0)
      - [A modern, `Ghosty`-based alternative to `TMUX` with GPU acceleration.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=1176.0)
      - [Provides advanced multiplexing, notifications, and browser splits.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=1214.0)
  - [**`Cloud Code` Plugins & Marketplace:**](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=1121.0)
      - [**`CC Status Line`:** Displays `Cloud Code` version, model, token usage, and Git info.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=1121.0)
      - [**`CMUX` Plugin:** Integrates `CMUX` with `Cloud Code`, enabling features like workspace renaming based on project name.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=1176.0)
      - [**Marketplace:** A public repository for installing these plugins.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=1224.0)
  - [**Future Vision: `Cloudbernetties`:**](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=4867.0)
      - [A system to manage and replicate `Cloud Code` skills and profiles across multiple instances, similar to `Kubernetes`.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=4867.0)

### Morgan's "Heritage Plot" App

  - [**Goal:** A cemetery management system for public search and admin operations.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=2497.0)
  - [**Architecture:** `Next.js` + `ShadCN` UI, with D3.js visualizations for plot layouts.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=3725.0)
  - [**Key Features:**](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=2899.0)
      - [**Role-Based Context Switching:** Admins can view the app as a cemetery owner without logging out.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=2899.0)
      - [**Complex Plot Structures:** Handles variable layouts (e.g., stacked caskets, multiple cremations).](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=3107.0)
      - [**Granular Document Access:** Manages public vs. FOIA-only documents, with different access levels (family, government).](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=2801.0)
  - [**Data Strategy:**](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=2605.0)
      - [Using a seed script for development due to unavailable client data.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=2605.0)
      - [Considering an ad-hoc field mechanism to accommodate varied data structures from different cemeteries.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=2648.0)

### Other Project Highlights

  - [**Paul's `StageHand` Automation:**](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=1722.0)
      - [Used `StageHand` (open-source from BrowserBase) to automate complex web scraping.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=1722.0)
      - [**Function:** Logs in, authenticates, and extracts JSON data from a live site.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=1756.0)
      - [**Warning:** The pattern can resemble a man-in-the-middle attack; use proxies to protect IP reputation.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=1959.0)
  - [**Mitch's YouTube Content Agent:**](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=2032.0)
      - [Created a system that fine-tunes prompts by analyzing YouTube ideas and predicting success.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=2035.0)
      - [The approach is inspired by genetic adaptation.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=2068.0)
  - [**Juan's AI Diffusion Pipeline:**](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=4300.0)
      - [Building an AI diffusion pipeline to transform images using LoRAs.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=4300.0)
      - [**Process:** A vision model will analyze an image → generate a prompt → perform image-to-image transformation.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=4315.0)
      - [**Goal:** Gain expertise in diffusion models, a key emerging field.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=4484.0)

## Next Steps

  - [**Patrick:**](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=822.0)
      - [Integrate feedback into the recap flow: move key takeaways to the top and hyperlink summary points.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=822.0)
      - [Continue developing `CoWork` backup system.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=960.0)
      - [Explore the `Cloudbernetties` concept for managing `Cloud Code` skills.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=4867.0)
  - [**Ty:**](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=1581.0)
      - [Install and test the new `CMUX` and `Cloud Code` plugins.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=1581.0)
  - [**Juan:**](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=4459.0)
      - [Consult Mitch on diffusion model techniques for the AI pipeline.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=4459.0)
  - [**All:**](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=1722.0)
      - [Review `StageHand`, `OneCLI`, and `Pencil.dev` as potential tools.](https://fathom.video/share/s11G7iKFseGggFirHWNzB-CXLmNEHdcM?tab=summary&timestamp=1722.0)

