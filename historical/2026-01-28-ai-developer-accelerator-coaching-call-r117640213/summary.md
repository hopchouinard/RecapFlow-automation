## Meeting Purpose

[Coaching call for AI developers to share progress and get feedback.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=1014.0)

## Key Takeaways

  - [**Claudebot (now Moltbot) is a powerful agent, but requires strict security isolation.** Run it in a dedicated VM with its own "service accounts" (email, calendar, GitHub) to prevent data leaks.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=1276.0)
  - [**SOC 2 & HIPAA compliance is a major moat, but a huge time sink.** It costs \~$20k/year and requires weeks of manual work, making it a key differentiator for SaaS businesses.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=1765.0)
  - [**Productize your AI skills by building a portfolio.** Create a few free projects to establish expertise, then offer them as a productized service (e.g., voice agents via LiveKit/Bland.ai).](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=4729.0)
  - [**Use AI for rapid prototyping and idea validation.** Before coding, use tools like GSD (for deep planning) or a simple Claude Code sandbox (for quick tests) to refine concepts.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=2572.0)

## Topics

### Claudebot (Moltbot) & Agent Security

  - [**Core Challenge:** Claudebot's file system access is a major security risk.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=1393.0)
  - [**Solution: Service Accounts & Isolation**](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=1276.0)
      - [**Dedicated VM:** Run the agent in an isolated Ubuntu VM (desktop version for GUI apps).](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=1338.0)
      - [**Service Accounts:** Create a separate Google account for the agent with its own email, calendar, and Google Drive.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=1298.0)
      - [**GitHub:** Give the agent its own GitHub account with read-only access to your repos. It works on clones and submits pull requests for review.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=1365.0)
      - [**Memory Vault:** Instruct the agent to sync all internal thoughts to an Obsidian vault in its GitHub repo, providing a transparent "window into its brain."](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=1646.0)
  - [**Use Cases & Demos**](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=1231.0)
      - [**Daily AI News Digest:** Patrick's agent uses Brave and Perplexity APIs to email a daily news summary, including source citations and token costs.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=5418.0)
      - [**Training Harness:** A Claude Code skill that auto-documents development sessions, generating summaries and artifacts for creating courses.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=5656.0)
      - [**Remote Coding:** Scott coded an entire app via WhatsApp, demonstrating the agent's ability to run tasks in the background on a remote machine.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=1480.0)

### Compliance (SOC 2 & HIPAA)

  - [**Purpose:** Enables data storage for feedback loops and unlocks enterprise customers.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=2123.0)
  - [**Vendor:** Vanta was chosen over Drata for its Supabase integration.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=1782.0)
  - [**Cost:** \~$20,000 for the first year (SOC 2 Type 1 & 2, HIPAA audits).](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=1882.0)
  - [**Process:** A time-intensive "video game" of completing \~65 tests and creating policies.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=2002.0)
  - [**Key Distinction:**](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=2298.0)
      - [**Type 1:** Point-in-time compliance.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=2318.0)
      - [**Type 2:** Gold standard, showing continuous compliance over 90-120 days.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=2318.0)

### Project Demos & Strategy

  - [**Sanford Fitness (Marc):** A fitness app with an AI coach.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=3391.0)
      - [**Token Throttling:** Track user usage in a `query_usage` Supabase table and hydrate a client-side context provider to enforce limits.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=3481.0)
      - [**AI Interaction:** Use Vercel AI SDK tool calls (`proposeWorkout`, `confirmWorkout`) to enable the AI to perform structured actions.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=3725.0)
  - [**AI Content Platform (Ryan):** A custom platform for a billionaire client to automate content creation (scraping, scripting, avatar video, editing, posting).](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=5054.0)
  - [**Clarity (Scott):** A developer tool to track projects, link GitHub repos, and manage meeting notes.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=7423.0)
      - [**Strategy:** Validate the idea by offering it free or at cost to the community to gather feedback before building a full SaaS.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=7674.0)
  - [**GSD Framework (Glenn):** A spec-driven development tool that acts as a thorough product manager.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=9824.0)
      - [**Process:** Asks detailed questions to build a complete spec before coding.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=10129.0)
      - [**Benefit:** High upfront investment in planning → near-autonomous execution.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=10343.0)

### Tooling & Resources

  - [**Email for Supabase Auth:** Use Mailgun or Resend for production email.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=3107.0)
  - [**Token Tracking:** Use `tiktoken` for accurate token counting.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=8432.0)
  - [**Healthcare Integrations:** Keragon is an N8N-like tool for HIPAA-compliant workflows.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=8781.0)
  - [**RAG:** Scott's `NeuralSpark` app processes PDFs within Supabase functions, avoiding a separate service.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=7981.0)

## Next Steps

  - [**Patrick:** Continue developing the Moltbot agent, focusing on self-coding capabilities.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=6127.0)
  - [**Scott & Ty:** Sync to discuss their developer tool projects.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=7573.0)
  - [**Ty:** Post the Moltbot setup prompt in the community once complete.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=10754.0)
  - [**Brandon:** Explore the GSD framework and Keragon for potential use cases.](https://fathom.video/share/ERuvaFFLnLabxHNUheseNesJy64FauVX?tab=summary&timestamp=9816.0)

