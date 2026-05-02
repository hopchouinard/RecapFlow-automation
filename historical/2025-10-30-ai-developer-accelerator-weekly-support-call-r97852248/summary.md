## Meeting Purpose

[Weekly support call for AI developer accelerator members to share project updates and get feedback.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=424.0)

## Key Takeaways

  - [**New Scraper UI:** Tom demoed a new, user-friendly UI for his web scraper, featuring an augmented overlay that lets non-technical users click elements directly on a page to select data for tracking.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=1352.0)
  - [**Critical Document Processing Tool:** Alex's project to automate quoting from complex PDFs was unblocked by Chunker, a SaaS tool that maintains table architecture and text integrity with \~97% accuracy, solving a problem where other tools (like Landing AI) failed.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=5598.0)
  - [**Developer Hiring Shift:** The group discussed a shift from hiring junior developers to prioritizing AI-savvy talent with strong communication skills, reflecting the need for problem-solvers who can leverage AI effectively.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=2862.0)
  - [**Trigger.dev for Real-time Updates:** Trigger.dev was identified as a superior alternative to Supabase RLS for real-time updates, as it avoids exposing client-side environment variables and simplifies background task management.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=4327.0)

## Topics

### Developer Hiring & Team Strategy

  - [**Problem:** Paul's CTO is hesitant to hire a new developer, preferring to first ensure the current team is effectively using AI tools.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=2715.0)
  - [**Discussion:** The group debated the evolving developer hiring landscape.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=2862.0)
      - [**Hiring for AI Proficiency:** Prioritize candidates who know how to use AI tools, as experience now correlates with a larger "context window" (ability to manage multiple agents/tasks).](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=2968.0)
      - [**Hiring for Problem-Solving:** Shift from technical coding tests to evaluating a candidate's ability to understand customer problems and apply business logic.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=3091.0)
      - [**Upskilling Subject Matter Experts:** Jake's strategy is to hire non-technical experts (e.g., in healthcare) and train them on AI, leveraging their deep domain knowledge.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=3025.0)
      - [**Impact on Junior Devs:** The job market is challenging for new CS graduates, who may need to pivot to non-coding roles where their AI skills can automate tasks.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=3342.0)

### Tooling & Workflow Optimization

  - [**Gemini CLI for Research:** Patrick highlighted Gemini CLI for its ability to run parallel research queries from multiple perspectives and save results to files.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=840.0)
      - [**Rate Limit Tip:** Use a personal Gmail account (1,000 queries/day) instead of a corporate Google Cloud account (100 queries/day) to avoid rate limits.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=775.0)
  - [**Claude Code vs. Cursor:** The group discussed the trade-offs between these AI coding assistants.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=5363.0)
      - [**Claude Code:** More cost-effective, especially with the Haiku model, but requires a CLI-heavy workflow.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=2366.0)
      - [**Cursor:** Offers a more integrated GUI, with its new 2.0 release featuring a custom code model and a built-in browser for self-checking.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=2139.0)
  - [**Automated PR Reviews:** For measuring AI's impact on productivity, the group recommended automated PR review tools.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=4801.0)
      - [**Recommendations:** CodeRabbit (Brandon's favorite) and Droids' DocFactory AI.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=4823.0)

### Project Demos & Updates

  - [**Patrick: Prompt Design UI**](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=1038.0)
      - [**Goal:** Create a better UX for designing complex prompts by moving beyond a small chat box.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=1038.0)
      - [**Features:** A two-panel interface (prompt on left, response on right) with a VS Code-like tab-completion for prompts.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=1084.0)
      - [**Future:** A prompt library with "executable functions" to improve other prompts.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=1254.0)
  - [**Tom: Consumer-Friendly Web Scraper**](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=1352.0)
      - [**Goal:** A web scraper for non-technical users to track specific page elements.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=1392.0)
      - [**New UI:** An augmented overlay lets users click elements directly on a page to select them.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=1453.0)
      - [**Backend:** Python with Celery for scalable, asynchronous job processing.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=1522.0)
  - [**Ty: Cybersecurity Repo Scanner**](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=1693.0)
      - [**Goal:** Scan GitHub repos for known security vulnerabilities.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=1693.0)
      - [**Process:** Connects to GitHub → pulls code → runs 40+ static analysis checks against NIST/OWASP standards on AWS Lambda.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=1728.0)
      - [**Output:** Identifies vulnerabilities, links to CVEs, and provides AI prompts (for Claude Code/Cursor) to fix issues.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=1773.0)
  - [**Alex: PDF Quoting Agent**](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=5598.0)
      - [**Goal:** Automate quoting from complex, multi-page plumbing fixture schedules.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=5608.0)
      - [**Key Tool:** Chunker (SaaS) for PDF processing, which maintains table architecture and text integrity with \~97% accuracy.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=5811.0)
      - [**Next Challenge:** Matching raw text line items to a product catalog in Supabase, requiring a mix of exact, fuzzy, and vector search.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=6247.0)
  - [**Garron: ADK Learning Workflow**](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=6494.0)
      - [**Goal:** Overcome the steep learning curve of ADK as a non-technical developer.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=6494.0)
      - [**Solution:** Created an "ADK Canonical Library" by consolidating all relevant documentation, videos, and code examples into a single Cursor repository.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=6554.0)
      - [**Result:** This RAG-powered workflow enabled more progress in 3 days than in the previous 3 months.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=6716.0)

## Next Steps

  - [**Brandon:**](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=4045.0)
      - [Release the Trigger.dev template before the full video tutorial.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=4045.0)
      - [Incorporate Trigger.dev's "streams" feature into the template to demonstrate real-time updates.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=4262.0)
      - [Help Alex promote the co-founder search post in the community.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=6300.0)
  - [**Morgan:**](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=4575.0)
      - [Test Trigger.dev's "subscribe" feature for real-time notifications.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=4003.0)
      - [Share feedback on the Next.js 16 upgrade after testing it in a playground project.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=4575.0)
  - [**Hemal:**](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=4733.0)
      - [Evaluate CodeRabbit and Droids' DocFactory AI for automated PR reviews.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=4801.0)
  - [**Ty:**](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=7273.0)
      - [Ask a contact about their workaround for LiveKit latency issues.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=7273.0)
  - [**Garron:**](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=6880.0)
      - [Demo the ADK prototype next week for feedback on a scalable architecture.](https://fathom.video/share/PqCs_W4SvsvZeGEDfdoey1cqYBy2eES1?tab=summary&timestamp=6880.0)

