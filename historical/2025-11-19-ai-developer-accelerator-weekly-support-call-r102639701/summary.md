## Meeting Purpose

[Weekly support call for AI developer projects and community updates.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=1201.0)

## Key Takeaways

  - [**Gemini 3 is a game-changer:** Its speed is a major advantage over GPT-5, enabling rapid prototyping. The Antigravity IDE, while powerful, has a steep learning curve and lacks in-diff editing.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=782.0)
  - [**DocPloy offers Vercel-like self-hosting:** This tool provides a platform-agnostic, cost-effective alternative to vendor lock-in, enabling deployment on a private VPS.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=3973.0)
  - [**The "Digital Twin" workflow is critical for AI-assisted development:** Maintaining a master markdown file that mirrors the code's structure and logic is essential for preventing context loss and ensuring AI agents make accurate changes.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=6840.0)
  - [**Shipkit's roadmap is driven by community demand:** The next major additions are LangGraph/LangChain support (for enterprise agents), followed by voice agent templates.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=2580.0)

## Topics

### Gemini 3 & Antigravity IDE

  - [Google's Gemini 3 model and the Antigravity IDE were the primary topic.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=693.0)
  - [**Performance:** Gemini 3 is significantly faster than GPT-5, making it ideal for rapid prototyping.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=818.0)
  - [**Antigravity IDE:**](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=818.0)
      - [**Pro:** Enables parallel development on multiple projects via an "inbox" system.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=1031.0)
      - [**Con:** Has a steep learning curve and lacks in-diff editing, which forces a less efficient workflow of copying/pasting code.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=903.0)
  - [**Shipkit's Future:** The platform remains relevant by focusing on its core pillars:](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=1047.0)
      - [AI-powered documentation.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=1062.0)
      - [Standardized task templates.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=1062.0)
      - [Pre-built project scaffolds.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=1062.0)
      - [A course on AI development fundamentals.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=1108.0)

### Project Updates & Challenges

  - [**Tom Welsh (Dung Beetle Project):**](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=1241.0)
      - [Migrated the ORM from DrizzleKit (frontend) to SQLAlchemy (Python backend).](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=1245.0)
      - [**Rationale:** Centralizes database management on the Python backend, which is the source of truth for the application's logic.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=1274.0)
      - [**Benefit:** Improves security by routing all database access through an authenticated API.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=1317.0)
  - [**Ty Wells (Holiday Promo App):**](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=2158.0)
      - [Built a holiday raffle app for a mobile recharge company.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=2158.0)
      - [**Features:** SMS entry, a public winner's page, and a claim page that overlays a winning image on a user's selfie.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=2188.0)
      - [**Stack:** Supabase for the backend and a custom SMS server (smsevil.eu).](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=2365.0)
  - [**Patrick Chouinard (Internal Automation):**](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=4815.0)
      - [Automated internal processes using GitHub Copilot agents.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=4815.0)
      - [**Workflow:** An agent parses VS Code release notes → generates internal Confluence docs, team messages, and committee meeting agendas.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=4888.0)
      - [**Key Technique:** Uses YAML front matter in markdown files to manage agent handoffs, creating a powerful, self-evolving system.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=4857.0)
  - [**Morgan Cook (Dashcam Data Project):**](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=5676.0)
      - [**Goal:** Make dashcam footage usable by processing GIS data to create searchable maps and reports.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=5940.0)
      - [**Workflow:** A Raspberry Pi auto-connects to the dashcam's Wi-Fi, syncs files, and uploads them for processing.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=5830.0)
      - [**Business Use Case:** Enables delivery companies to monitor driver routes for efficiency and compliance.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=5859.0)
  - [**Garron Selliken (Agent App Refactor):**](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=6286.0)
      - [Struggled with context loss and debugging while refactoring a multi-agent app.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=6286.0)
      - [**Solution:** Brandon recommended using the "Digital Twin" workflow—a master markdown file that defines the app's structure—to prevent context loss and guide the AI.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=6875.0)
      - [**Deployment Plan:** Use Trigger.dev for production, as the ADK's native Agent Engine is not scalable for 150+ users.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=7040.0)

### New Tools & Strategies

  - [**DocPloy (Self-Hosting):**](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=3973.0)
      - [A tool for self-hosting Next.js apps on a private VPS, offering a Vercel-like experience without vendor lock-in.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=3973.0)
      - [**Benefit:** Provides full control over infrastructure, enabling multi-cloud clustering and significant cost savings.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=4044.0)
  - [**AI-Assisted Website Development:**](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=1690.0)
      - [**Strategy:** Use AI to generate multiple design and copy variations, providing a "white glove" experience for clients.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=1793.0)
      - [**Value-Add:** Paul Miller demonstrated building a simple CMS with Claude Code to give clients control over dynamic content (e.g., articles, pricing).](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=1977.0)
  - [**AI Video Generation:**](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=1511.0)
      - [**Brandon's Project:** A "Pokemon shorts generator" built on the Shipkit Worker SaaS template.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=1511.0)
      - [**Mitch's Insight:** To go viral, use a "pattern interrupt" (e.g., a gruff narrator, meme culture) and optimize for a specific audience.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=3132.0)

## Next Steps

  - [**Tom Welsh:** Test DocPloy by migrating the Dung Beetle project from Vercel.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=4523.0)
  - [**Brandon Hancock:**](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=4688.0)
      - [Investigate DocPloy for future Shipkit infrastructure templates.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=4688.0)
      - [Build the Pokemon shorts generator on the Worker SaaS template.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=1511.0)
  - [**Garron Selliken:**](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=6217.0)
      - [Refactor the agent app using the "Digital Twin" workflow.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=6875.0)
      - [Prepare for production deployment using Trigger.dev.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=7040.0)
  - [**Abdulshakur Abdullah:** Implement the "white glove" AI-assisted workflow for new website contracts.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=2047.0)
  - [**Paul Miller:** Continue evaluating DocPloy and share findings with the group.](https://fathom.video/share/CVV7H_oteWyjWdnCGf5Bvo5iyjLnAGpk?tab=summary&timestamp=4360.0)

