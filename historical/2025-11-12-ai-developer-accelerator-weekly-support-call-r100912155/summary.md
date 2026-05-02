## Meeting Purpose

[Weekly support call for AI developers to share updates and get feedback.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1633.0)

## Key Takeaways

  - [**Alex Rojas pivoted a client project from complex hardware to a simpler, cloud-based software solution** after a scope review revealed the initial proposal was underpriced. The new plan uses a Trigger.dev pipeline to process car inspection photos with cloud AI, replacing a local YOLO model.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1182.0)
  - [**Patrick Chouinard demoed a powerful Gemini CLI workflow** that uses parallel Bash scripts to create a daily AI news report. This "fan-out" pattern enables massive, low-cost data gathering, such as scraping all US ambulance companies for \~$20.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=3180.0)
  - [**Brandon Hancock's Trigger.dev SaaS template is launching by Sunday.** It automates audio processing (Whisper transcription, AI summaries) and demonstrates advanced workflows like dynamic prompt branching and real-time progress streaming.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1479.0)
  - [**Juan Torres's SOC 2-compliant AI agent extracts vendor names with \~95% accuracy** using a fine-tuned 8B parameter model on an economical A10 GPU, proving that effective, compliant solutions don't require complex model training.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=2604.0)

## Topics

### Alex Rojas: Client Project Pivot

  - [**Initial Proposal:** Hardware-based computer vision arc for car damage detection.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1281.0)
  - [**Problem:** Scope review (with Mitch & Brandon) revealed the proposal was significantly underpriced.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1890.0)
  - [**Solution:** Pivoted to a software-first approach using operator phones for photos.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1711.0)
      - [**Original Tech Stack:** Local YOLOv8 nano model → Next.js app → Supabase.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1711.0)
      - [**Recommended Tech Stack (Brandon):** Cloud-based for simplicity, speed, and intelligence.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1964.0)
          - [Use Trigger.dev to capture photos at a high frequency (e.g., 4 frames/sec).](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=2040.0)
          - [Send frames in parallel to a cloud image model (e.g., Gemini) for damage reports.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1964.0)
          - [Aggregate individual reports into a final summary.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=2078.0)
  - [**Contract Advice (Jake):**](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=2173.0)
      - [Use AI (e.g., Claude) to draft contracts, specifying the role ("I am the contractor") to ensure proper legal framing.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=2237.0)
      - [Prioritize short, clear contracts.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=2262.0)
      - [Protect background IP by defining its transfer terms and costs for future products.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=2325.0)
      - [Avoid signing under pressure; review all terms carefully.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=2404.0)

### Brandon Hancock: Trigger.dev SaaS Template Demo

  - [**Purpose:** A SaaS template demonstrating a full AI workflow using Trigger.dev.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1479.0)
  - [**Launch:** By Sunday.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1486.0)
  - [**Workflow:**](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1492.0)
    1.  [**Upload:** File → Supabase Blob Store.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1492.0)
    2.  [**Trigger:** Supabase event → Trigger.dev pipeline.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1512.0)
    3.  [**Process:** Download file, extract audio, transcribe chunks with Whisper.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1512.0)
    4.  [**Summarize:** A separate workflow uses dynamic prompts based on content type (meeting, YouTube) to generate summaries.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1553.0)
    5.  [**Query:** Real-time chat with the processed content.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1583.0)
  - [**Key Feature:** All progress updates and chat responses stream in real-time, showcasing Trigger.dev's capabilities.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1583.0)

### Patrick Chouinard: Gemini CLI for Parallel Research

  - [**Project:** A daily AI news aggregator built entirely with Bash scripts and the Gemini CLI.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=3180.0)
  - [**Core Concept:** The "fan-out" pattern.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=3420.0)
      - [A Bash script executes multiple `gemini-p` commands in parallel.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=3364.0)
      - [Each command acts as an independent agent researching a specific topic.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=3371.0)
  - [**Result:** Enables massive, low-cost data gathering.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=3431.0)
      - [**Example:** Scraping all US ambulance companies could be done for \~$20.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=3431.0)
  - [**Best Practice:** Use Gemini 2.5 Flash for speed and cost efficiency, reserving 2.5 Pro for complex analysis.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=3483.0)
  - [**Future Work:** Developing a course on Copilot CLI, noting its advanced sub-agent capabilities.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=3514.0)

### Juan Torres: SOC 2 Compliant AI Agent

  - [**Project:** An AI agent for extracting vendor names from documents.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=2604.0)
  - [**Architecture:** AWS-hosted, SOC 2 compliant.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=2535.0)
  - [**Method:** Uses a fine-tuned 8B parameter model with strategic prompting.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=2604.0)
      - [**Result:** Achieves \~95% accuracy.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=2620.0)
      - [**Significance:** Proves that complex model training is not always necessary for high-accuracy, compliant solutions.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=2604.0)
  - [**Hardware:** Runs on a single A10 GPU, chosen for its cost-effectiveness at the current scale.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=2661.0)

### Mario Polanco: Home Customizer & AI Avatar Platform

  - [**Project 1: Home Customizer**](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5119.0)
      - [**Goal:** Allow clients to customize finishes (walls, floors) on mini-home templates.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5119.0)
      - [**Recommended Tech:** Gemini's Nano Banana image generation API.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5280.0)
      - [**Workflow Levels:**](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5327.0)
        1.  [**Simple:** Image + prompt → single output.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5332.0)
        2.  [**Refined:** Generate multiple images → use a grading AI to select the best one.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5332.0)
        3.  [**Interactive:** Implement a user feedback loop for iterative refinement.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5377.0)
  - [**Project 2: AI Avatar Platform**](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5412.0)
      - [**Goal:** Create an AI platform with interactive avatars for course creators.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5412.0)
      - [**Key Tool:** HeyGen, which now offers a live Zoom feature with an integrated knowledge base.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5412.0)
      - [**Recommendation:** Use HeyGen's native knowledge base for real-time RAG to avoid latency from custom tools.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5541.0)
      - [**Architecture:** Use a background job (e.g., Trigger.dev) to sync course content from Supabase to HeyGen's knowledge base.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5628.0)

### Mitch McCauley: N8N Issues & AI Tools

  - [**N8N Workflow Issues:**](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5989.0)
      - [**Problem:** Workflows fail silently when run in parallel (e.g., \>20 executions).](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=6049.0)
      - [**Symptom:** Data passed between nodes becomes `undefined`, preventing debugging.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=6060.0)
      - [**Diagnosis:** Likely an N8N platform limitation, as single runs are successful.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=6190.0)
      - [**Recommendation:** Migrate to Trigger.dev for more robust parallel processing and better debugging tools.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=6454.0)
  - [**AI Tooling Insights:**](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=6536.0)
      - [**ChatGPT + Canva:** Powerful for generating pitch decks from voice notes.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=6536.0)
      - [**Cursor:** Used to create a Python script for blurring faces in videos.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=6620.0)
          - [**Suggestion:** Blur the entire head for better privacy, not just the face.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=6704.0)

### Other Updates

  - [**Hemal Shah:** Exploring Cursor CLI and GitHub Actions for a cost-effective code review pipeline, replacing the more expensive CodeRabbit.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=2884.0)
  - [**Ana P:** Developing a WhatsApp chatbot for a coffee farm to query GCP data.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=4325.0)
      - [**Security Concern:** WhatsApp's suitability for business data.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=4380.0)
      - [**Feedback:** WhatsApp offers end-to-end encryption for message content, but metadata (sender, time) is exposed. Authentication via a phone number whitelist is a simple first step.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=4574.0)
  - [**Ty Wells:** Seeking feedback on a security scanning tool.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5664.0)
      - [**Features:** Scans repos for OWASP Top 10 vulnerabilities and provides AI-generated fixes.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5779.0)
      - [**Marketing Suggestion:** Use a "CodeRabbit" approach (e.g., funny poems in PR comments) for persistent, low-cost marketing.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5829.0)
  - [**Alex Wilson:** Using Algo Expert to prepare for a pre-exam, a standard requirement for tech company interviews.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=4707.0)

## Next Steps

  - [**Brandon:**](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1489.0)
      - [Launch Trigger.dev SaaS template by Sunday.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1489.0)
      - [Create a community GitHub repo for sharing code and projects.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=4950.0)
  - [**Alex Rojas:**](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1182.0)
      - [Finalize client proposal using the cloud-based Trigger.dev architecture.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=1964.0)
  - [**Ty Wells:**](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5664.0)
      - [Share the security scanning tool link for feedback.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5664.0)
  - [**Mitch:**](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5976.0)
      - [Evaluate migrating N8N workflows to Trigger.dev.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=6454.0)
  - [**Mario:**](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5092.0)
      - [Begin prototyping the home customizer using the Nano Banana API.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=5277.0)
  - [**Patrick:**](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=3514.0)
      - [Continue developing the Copilot CLI course.](https://fathom.video/share/bTmDJKuoLW7kEfyszAsGfe8U35QbzNqc?tab=summary&timestamp=3514.0)

