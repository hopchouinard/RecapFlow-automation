## Meeting Purpose

[A coaching call for AI developers to share progress, challenges, and insights.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=80.0)

## Key Takeaways

  - [**Automate Evaluation to Eliminate Bottlenecks:** Build self-improving AI systems by defining clear scoring functions (rubrics) and evaluation suites. This forces you to articulate success criteria, enabling the AI to run infinite experiments and eliminate human bottlenecks.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=132.0)
  - [**Use the Right Tools for the Job:**](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=900.0)
      - [**Stripe CLI:** Automates key management, solving "key hell" and preventing stale data by keeping the source of truth in Stripe.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=960.0)
      - [**Terraform:** Defines infrastructure as code (IaC), providing a single source of truth for cloud architecture that AI agents can manage.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=2719.0)
      - [**Codex:** Excels at long-running, autonomous jobs without requiring constant human intervention.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=749.0)
  - [**Prioritize Security & Governance for AI Assistants:** For personal AI assistants (e.g., Ironclaw), prioritize security and auditable governance over features. Use a smart router to blend local (Ollama) and frontier (Sonnet) models, with all actions requiring human approval via Telegram or Discord.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=6321.0)
  - [**Adopt a "Person-in-the-Box" Mindset:** Frame business automation as building an AI "person" (e.g., a Customer Success Manager) by codifying all SOPs into agent playbooks. The "machine" is the playbook, not the output; fix the playbook to improve results.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=7080.0)

## Topics

### The "Eliminate Yourself" Framework

  - [**Goal:** Build systems that operate autonomously by removing humans from the evaluation loop.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=132.0)
  - [**Method:**](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=187.0)
    1.  [**Define a Scoring Function:** Create a clear rubric for success, including pass/fail criteria and a point-based system for quality.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=660.0)
    2.  [**Build an Evaluation Suite:** Create a diverse set of inputs to test the system.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=720.0)
    3.  [**Enable Self-Experimentation:** Let the AI (e.g., Codex) run infinite iterations, using the scoring function to identify weaknesses and refine its prompts.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=720.0)
  - [**Application 1: SOAP Narrative Generation**](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=143.0)
      - [**Problem:** Automating the creation of medical SOAP narratives for reimbursement.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=804.0)
      - [**Solution:** A multi-step AI system with self-evaluating feedback loops.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=232.0)
      - [**Result:** Observable quality improvements in narratives over time.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=376.0)
  - [**Application 2: Software Development Lifecycle**](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=299.0)
      - [**Problem:** Automating feature development from a high-level request.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=299.0)
      - [**Solution:** An AI agent that creates a work tree, builds a dev environment, and runs a test suite.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=299.0)
      - [**Challenge:** The test suite is the hardest part to build, as it requires codifying all product knowledge into user stories.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=440.0)
  - [**Model Recommendation:** GPT-4o for non-thinking consumer apps.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=866.0)

### Project Updates & Learnings

  - [**Ty Wells: FaceGate Authentication SDK**](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=1892.0)
      - [**Problem:** Shared devices (e.g., kiosks, tablets) lack a secure, multi-user biometric login.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=1947.0)
      - [**Solution:** A drop-in SDK for web apps using Face ID and liveness checks.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=1892.0)
      - [**Key Feature:** QR code offload to a phone for devices without cameras.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=1990.0)
      - [**Security:** Stores only encrypted mathematical vectors, not images.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=2340.0)
      - [**Accuracy:** 99.7%—sufficient for time/attendance but not for high-security tasks.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=2035.0)
  - [**Morgan Cook: Cemetery Management Platform**](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=4987.0)
      - [**Problem:** A government client is unresponsive, blocking progress on a compliance-critical project.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=4987.0)
      - [**Solution:** Shift focus to acquiring new clients to avoid being blocked.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=5172.0)
      - [**Strategy:** Offer free/discounted licenses to early adopters for feedback.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=5404.0)
      - [**Tactic:** Use "lumpy mail" (physical packages) to bypass gatekeepers and reach decision-makers directly.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=5342.0)
  - [**Scott Rippey: AI News Briefing & Ironclaw Guide**](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=6644.0)
      - [**AI News Briefing:** An automated system that pulls RSS feeds, uses Haiku for RAG to avoid repeats, and generates a daily audio summary with an Eleven Labs "Jarvis" voice.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=6644.0)
      - [**Ironclaw Guide:** A white paper detailing a secure, auditable personal AI assistant setup using a Mac Mini.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=6321.0)
      - [**Architecture:** A smart router blends local models (Ollama) with frontier models (Sonnet), with all actions requiring human approval.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=6842.0)
      - [**Communication:** Discord is recommended over Telegram for better memory management via channels.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=6991.0)
  - [**Patrick Chouinard: Research Pipeline & Personality Kit**](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=2979.0)
      - [**Research Pipeline:** A research pipeline built with Claude Code is now being implemented in production for a client who discovered it on GitHub.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=2979.0)
      - [**RecapFlow:** Integrating an auto-research loop into RecapFlow, a tool that analyzes meeting transcripts to create structured recaps.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=3245.0)
      - [**Personality Kit:** A script to deploy a consistent personality schema (behavior, output type, constraints) across all local AI CLIs (Claude, Gemini, Copilot) for a more engaging experience.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=3180.0)
  - [**Juan Torres: Image-to-Image Generation App**](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=2441.0)
      - [**Project:** A diffusion image-to-image generation app with a robust AWS backend.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=2463.0)
      - [**Learning:** The project highlighted the need for Infrastructure as Code (IaC) to manage the complex AWS architecture.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=2719.0)
      - [**Action:** Use Claude to generate Terraform files from the existing AWS setup to create a single source of truth.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=2880.0)

### Tooling & Workflow Insights

  - [**Stripe Implementation:**](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=960.0)
      - [**Problem:** Manual key management ("key hell") and stale data.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=960.0)
      - [**Solution:** Use the Stripe CLI to automate key management and keep the source of truth in Stripe.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=1123.0)
  - [**Mobile AI Ideation:**](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=1344.0)
      - [**Workflow:** Use Claude Code on a phone to create new tasks from voice memos.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=1344.0)
      - [**Enhancement:** Use Whisperflow to transcribe longer thoughts, providing more context for the AI.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=4008.0)
  - [**AI Hardware:**](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=5880.0)
      - [**VR Coding:** Meta Quest 3 with Immersed provides a productive, multi-screen VR coding environment.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=5880.0)
      - [**Wearable Recorders:**](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=5707.0)
          - [**Fildy:** Excellent for day-to-day context gathering with a sensitive mic.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=5707.0)
          - [**Plod:** Better for specific meetings, with a desktop app that can record audio even when other note-takers are blocked.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=5707.0)

## Next Steps

  - [**Morgan Cook:**](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=4987.0)
      - [Contact Utah cemeteries using "lumpy mail" to bypass gatekeepers.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=5342.0)
      - [Offer free/discounted licenses to secure early adopters for feedback.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=5404.0)
  - [**Scott Rippey:**](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=5870.0)
      - [Rework the Ironclaw guide to recommend Discord for communication.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=6991.0)
      - [Share the revised guide with the community.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=7011.0)
  - [**Ty Wells:**](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=1409.0)
      - [Provide a public demo of the FaceGate SDK for testing.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=2240.0)
  - [**Juan Torres:**](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=2441.0)
      - [Use Claude to generate Terraform files for the AWS infrastructure.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=2880.0)
  - [**Elijah Stambaugh:**](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=7080.0)
      - [Develop the "embed" and "equip" consulting programs, focusing on codifying client SOPs into agent playbooks.](https://fathom.video/share/CkxG8VhZt3QN-snTxC4DuT8VWARaYPS5?tab=summary&timestamp=7200.0)

