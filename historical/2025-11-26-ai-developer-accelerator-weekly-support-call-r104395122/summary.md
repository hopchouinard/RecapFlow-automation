## Meeting Purpose

[A weekly support call for AI developer accelerator members to share projects and discuss technical challenges.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=585.0)

## Key Takeaways

  - [**AI Tooling Strategy:** Use Claude Code for primary development due to its high-context planning mode and generous $100/mo plan. Supplement with Anti-Gravity for browser-based tasks and Codex for messy codebases.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=2382.0)
  - [**Automated Presentation Generation:** Patrick is building "Deck AI Forge," a pipeline that converts text → Markdown → JSON → interactive HTML presentations. This creates a consistent, branded output that is cheaper and more flexible than PowerPoint.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=4758.0)
  - [**High-Confidence Data Extraction:** Juan achieved 95–98% confidence in vendor name extraction by using a validator agent with exclusion lists (e.g., CEO names) and a reference list of known vendors, eliminating manual review.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=5422.0)
  - [**Facebook Content Monetization:** Mitch's AI-generated videos are earning significant revenue by engineering content for "limitless demand" to maximize watch time and ad revenue. The strategy prioritizes quality over quantity.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=7181.0)

## Topics

### AI Tooling & Workflow

  - [**Claude Code vs. Anti-Gravity:**](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=2382.0)
      - [**Claude Code:** Primary tool for 80–90% of development.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=2424.0)
          - [**Pros:** High-context planning mode; generous $100/mo plan with no usage caps.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=2452.0)
          - [**Cons:** Can struggle with messy, vibe-coded projects (Andrew's PySide app).](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=3079.0)
      - [**Anti-Gravity:** Google's agentic IDE.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=1706.0)
          - [**Pros:** Excellent browser experience; effective for web scraping (Marc's custom shopper).](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=1735.0)
          - [**Cons:** Restrictive free tier (50 requests/hr); no planning mode.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=1742.0)
  - [**Codex:** A viable alternative for messy codebases.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=3033.0)
      - [**Pros:** Excels at handling unstructured code.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=3051.0)
      - [**Cons:** Lacks a built-in planning mode, requiring manual prompts to outline steps.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=3160.0)
  - [**Workflow Automation:** Brandon automates one weekly task by creating a new Markdown file with a Standard Operating Procedure (SOP) for an AI agent. This builds a personal "AI workforce" to eliminate busywork.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=3233.0)

### Project Deep Dives

  - [**Automated Presentations (Deck AI Forge):**](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=4758.0)
      - [**Goal:** Automate the creation of consistent, branded, interactive presentations.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=4758.0)
      - [**Problem:** PowerPoint is inconsistent and time-consuming.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=4809.0)
      - [**Solution:** A pipeline that converts text to a structured, self-contained HTML file.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=4758.0)
          - [**Process:** Raw Text → Markdown (for human review) → JSON (standardized format) → HTML (final output).](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=5197.0)
          - [**Rationale:** The JSON intermediate format allows for multiple output types (HTML, PDF) from a single source.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=5197.0)
          - [**Cost:** Uses smaller, cheaper models (GPT 4.1 Mini, Gemini 5 Codex Mini) because the design is template-driven, not AI-generated.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=4931.0)
  - [**High-Confidence Vendor Extraction:**](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=5417.0)
      - [**Goal:** Automate vendor name extraction from general ledger data with high confidence.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=5422.0)
      - [**Problem:** Manual extraction is slow and error-prone.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=5613.0)
      - [**Solution:** A two-agent system (Extractor + Validator) with context engineering.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=5458.0)
          - [**Validator Agent:**](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=5458.0)
              - [Uses an exclusion list (e.g., CEO names) to prevent misidentification.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=5458.0)
              - [Uses a reference list of known vendors to confirm names.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=5547.0)
          - [**Result:** Achieved 95–98% confidence, eliminating the need for manual review.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=5422.0)
  - [**Facebook Video Monetization:**](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=7181.0)
      - [**Goal:** Generate revenue from AI-created Facebook videos.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=7181.0)
      - [**Strategy:** Engineer content for "limitless demand" to maximize watch time and ad revenue.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=7181.0)
          - [**Focus:** Quality over quantity. A single viral video earns significantly more than many low-performing ones because advertisers pay more for placement on successful content.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=8498.0)
      - [**Process:** Manual prompting for each clip (Sora API).](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=7555.0)
      - [**Cost:** \~$7 per 2-minute video using Kling 2.5 (chosen for its permissive content policy), which is significantly cheaper than Sora.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=8226.0)

### Community & Tooling Updates

  - [**Community Repo:** Now live for sharing projects.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=4170.0)
      - [**Patrick's Contributions:**](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=4029.0)
          - [**Bootstrap Scripts:** Automate Git setup (fork, clone, branch) for Mac, Linux, and Windows to lower the barrier to entry.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=4029.0)
          - [**Custom GPT:** A custom GPT file for generating ShipKit prompts.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=4126.0)
  - [**Documentation Strategy:**](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=2483.0)
      - [**Recommendation:** Use GitHub Copilot CLI in the CI/CD pipeline for automated documentation.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=2675.0)
      - [**Initial Draft:** Use the `generate diagram` ShipKit prompt to create a baseline (Patrick generated 18,000 lines this way).](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=2869.0)
      - [**Continuous Update:** A PR hook can analyze code changes and automatically create a new PR to update the corresponding documentation.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=2804.0)
  - [**DocPloy:** A self-hosted Vercel/Supabase alternative.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=3759.0)
      - [**Status:** In production for several clients.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=3884.0)
      - [**Hosting:** Available as a pre-configured VPS on Hostinger.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=3828.0)

## Next Steps

  - [**Brandon:**](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=595.0)
      - [Share the AI video generator source code and tutorial video tomorrow morning.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=595.0)
  - [**Alex:**](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=958.0)
      - [Report back on client reactions to the HTML-based proposals.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=958.0)
  - [**Ty:**](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=2141.0)
      - [Demo the "10X'd" ShipKit project next Tuesday.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=2141.0)
  - [**Patrick:**](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=3953.0)
      - [Demo the "Deck AI Forge" project when ready.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=5317.0)
  - [**Mitch:**](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=6993.0)
      - [Review the AI video generator source code and provide feedback.](https://fathom.video/share/F1hMYU9oGVi5bxhP_PKwgMv7xF1DcRde?tab=summary&timestamp=7956.0)

