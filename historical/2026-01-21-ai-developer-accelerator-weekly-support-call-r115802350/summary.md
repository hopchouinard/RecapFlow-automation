## Meeting Purpose

[Weekly support call for AI developers to share progress and get feedback.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=977.0)

## Key Takeaways

  - [**Automated Training Creation:** Patrick built a system that generates a full training course (NotebookLM, slides, video) from a single Claude Code project by auto-extracting patterns from the dev conversation.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=3667.0)
  - [**Advanced RAG Architecture:** Scott implemented a 3-layer RAG system in NeuralSpark, using a Recursive Language Model (RLM) to have the LLM intelligently "hunt" for information, solving context rot and improving accuracy.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=3054.0)
  - [**Enterprise AI Consulting:** A new business opportunity was identified: helping companies securely adopt agentic AI (e.g., Claude Code, Cowork) to bypass productivity-crippling internal IT policies.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=5684.0)
  - [**Agentic Workflow Updates:** Brandon is releasing new Shipkit videos and commands (e.g., `worktree`, `task review`) to optimize agentic development, enabling parallel feature work.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=774.0)

## Topics

### The Future of Work: System Creators vs. Task Doers

  - **Morgan's Workflow:** Automated a non-programmer's task (creating product sheets) from days to \<10 minutes using skills in the Windsurf IDE.
      - [**Process:** Markdown → HTML (styled) → PDF + `meta.json` for product pages.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=1157.0)
  - [**Brandon's Cowork Example:** Resolved a complex Excel matching problem (50 parts x 50 centers) in 5 minutes by pasting the problem description and file into Cowork.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=664.0)
  - [**Consensus:** The future workforce will be system creators and managers, not task doers. People must "level up" to think at a systems level, as AI will automate individual tasks.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=1238.0)

### Advanced Agentic Workflows & Tools

  - [**Brandon's Mobile Workflow:**](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=1756.0)
      - [Uses Claude's mobile app to kick off development while away from a computer.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=1756.0)
      - [**Process:** Voice idea → "Create a new task using template.md" → Claude creates a new Git branch.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=1860.0)
      - [**On Desktop:** Uses `git worktree` to check out and work on multiple branches in parallel.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=2147.0)
      - **Result:** This workflow enabled building 6 features in \<2 days.
  - [**Paul's Reporting App:**](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=6158.0)
      - [**Goal:** Build an app to summarize large Postgres datasets.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=6202.0)
      - [**Solution:** Use the Shipkit chat template and inject data dynamically.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=6240.0)
      - [**Advanced Option:** Run parallel `generateText` calls for different data sources, then feed the summaries into a final `streamText` call.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=6313.0)
  - [**Voice Agent Recommendation:** Bland was suggested as an easy, affordable no-code tool for building voice agents that can schedule meetings via Google Calendar.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=2243.0)

### Enterprise AI Adoption & Consulting

  - [**Paul's CTO Agreement:** Secured approval to use an agentic approach for all new, standalone projects.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=5324.0)
  - [**Enterprise IT Bottleneck:** Many companies are limited to basic chat wrappers due to IT security fears, preventing employees from using powerful agentic tools.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=6103.0)
  - [**Business Opportunity:** Offer consulting to help companies securely adopt agentic AI.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=5684.0)
      - [**Service:** Build a secure, ring-fenced cloud environment (e.g., AWS, GCP) for internal AI tools.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=5886.0)
      - [**Value Prop:** Address the real risk (80% of data leaks are internal staff) and provide a best-practice solution, enabling productivity.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=5940.0)

### Project Updates & Demos

  - [**Scott's NeuralSpark (RAG System):**](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=3054.0)
      - [**Goal:** Solve context rot in RAG systems with a 3-layer architecture.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=3097.0)
      - [**Layer 1 (Vector Search):** Standard chunking and embeddings.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=3060.0)
      - [**Layer 2 (Re-ranking):** Uses Cohere to score and re-rank the top 50 results.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=3115.0)
      - [**Layer 3 (RLM):** The LLM intelligently "hunts" for information using tool calls, reversing the traditional RAG flow. This improves accuracy and scales better with large datasets.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=3134.0)
  - [**Patrick's Automated Training System:**](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=3667.0)
      - [**Goal:** Automate training creation from development work.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=3667.0)
      - [**Process:** A Claude Code skill extracts patterns from dev conversations (e.g., PRD analysis, feature decomposition).](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=3691.0)
      - [**Output:** A NotebookLM with the full dev history, a RAG chatbot, and auto-generated artifacts (slides, audio, graphics).](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=3929.0)
      - [**Business Model:** "Build Once, Sell Twice" by productizing the dev process itself.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=4402.0)
  - [**Ty's NGraph (DevOps Tool):**](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=8427.0)
      - [**Goal:** A personal DevOps tool to manage knowledge across multiple projects.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=8451.0)
      - [**Features:**](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=8551.0)
          - [**Cross-Project Memory:** Stores identity and preferences to avoid re-contextualizing.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=8551.0)
          - [**Flaw Tracking:** Finds and reproduces Claude Code failure patterns from internal projects and external sources (Reddit, GitHub).](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=8587.0)
          - [**Subscription Management:** Scans Gmail/CC statements to track tool usage and identify unused subscriptions.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=8702.0)

### Shipkit & Community Updates

  - [**Shipkit Updates:** Brandon is releasing new Shipkit videos and commands to optimize agentic development.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=774.0)
      - [**New Commands:** `worktree`, `task review`.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=774.0)
      - [**RAG Update:** Code for the RAG pipeline update is included; the video is coming soon.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=960.0)
  - [**Community Management:** Paul and Patrick will take over managing the community during Brandon's absence.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=299.0)

## Next Steps

  - [**Brandon:**](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=774.0)
      - [Fix the Shipkit RAG pipeline.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=776.0)
      - [Record a video demo of the mobile-to-desktop workflow.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=2062.0)
      - [Create a Shipkit affiliate code for Elijah's "Refining Education" community.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=7746.0)
  - [**Patrick:**](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=3616.0)
      - [Test the Claude Code + Ollama integration for parallel research tasks.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=9121.0)
      - [Finalize the automated training NotebookLM and create a marketing video.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=4819.0)
  - [**Scott:**](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=3325.0)
      - [Demo the NeuralSpark RLM architecture in the next meeting.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=3325.0)
  - [**Ryan:**](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=7632.0)
      - [Email Brandon to schedule a business strategy session.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=7632.0)
  - [**Juan:**](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=2550.0)
      - [Email Brandon to request the previous Shipkit pricing.](https://fathom.video/share/sxZYeYETzRBytiqGWDB8JP9zm-WePxXf?tab=summary&timestamp=2597.0)

