## Meeting Purpose

[Review AI projects, discuss industry trends, and share development strategies.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=766.0)

## Key Takeaways

  - [**AI-Driven Scope Creep:** AI's speed enables rapid development, but this often leads to "app creep" as clients demand more features faster. Managing this requires strict focus on critical business objectives and OKRs.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=5354.0)
  - [**Career Shifts:** AI will automate procedural knowledge work, increasing demand for roles requiring subjective judgment (e.g., cybersecurity, skilled trades) and for business analysts who can define the right problems to solve.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=1540.0)
  - [**Local AI Hubs:** Repurposing gaming PCs with Proxmox and Docker creates powerful, secure local AI hubs. This strategy solves data sovereignty concerns and provides a cost-effective development environment.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=6591.0)
  - [**New Development Patterns:** Patrick's "Claude Speak" plugin demonstrates a new paradigm: using cheap TTS models (e.g., GPT-4-0 Mini) to enable real-time agent interaction, freeing up expensive creation tokens for the primary LLM.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=1064.0)

## Topics

### The Challenge: AI-Driven Scope Creep

  - [**Problem:** AI's speed accelerates development, but clients quickly become accustomed to success and demand more complex features, leading to "app creep" and unsustainable project growth.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=4789.0)
  - [**Example (Jake):** A successful project led to escalating demands (e.g., single-tenant → multi-tenant), making the final 10% of development feel "impossible" due to inherent hard problems.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=4740.0)
  - [**Example (Juan):** Non-technical clients may misattribute issues, requiring developers to proactively manage expectations and maintain focus on the project's core objectives.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=3855.0)
  - [**Solution (Patrick):** Reframe scope creep as a business opportunity. Use AI to automate communication (e.g., Claude rewriting emails) to manage client emotions and focus on solving their problems.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=4276.0)

### Career Impact & Future Skills

  - [**AI's Impact:** AI will automate procedural knowledge work, but the ability to structure ideas and workflows remains a critical human skill.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=1681.0)
  - [**In-Demand Roles:**](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=1540.0)
      - [**Cybersecurity:** Defending against AI-powered threats.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=1629.0)
      - [**Skilled Trades:** Plumbing, carpentry, and electrical work for data center infrastructure.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=1651.0)
      - [**Business Analysts:** Defining the right problems to solve, a skill often missing in new graduates.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=1734.0)
  - [**Future Workday:** A personal AI agent will become a standard tool, tuned to a user's specific needs and deficits.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=2242.0)

### Solution: Local AI Hubs for Security & Cost Control

  - [**Problem:** Public cloud LLMs raise data privacy and sovereignty concerns for sensitive projects.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=6577.0)
  - [**Solution:** Repurpose a gaming PC as a local AI hub for secure, cost-effective development.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=6591.0)
      - [**Platform:** Proxmox for infrastructure management.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=7053.0)
      - [**Virtualization:** Docker for running multiple LLM instances.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=6824.0)
      - [**Networking:** TailScale or TwinGate for secure remote access.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=7148.0)
  - [**Example (Alex):** Running a 7B parameter Qwen model on a GeForce RTX 2070 GPU with PopOS Linux.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=6654.0)
  - [**Example (Paul):** Using DocPloy to manage Docker containers with direct CUDA access.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=6824.0)

### Project Demos & Updates

  - [**Patrick's "Lab" Ecosystem:**](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=945.0)
      - [**Goal:** Centralize and track all personal AI projects.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=945.0)
      - [**"Claude Speak" Plugin:** Uses GPT-4-0 Mini TTS to give Claude Code a voice, enabling real-time attention-grabbing and freeing up expensive creation tokens.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=1064.0)
      - [**LabSync (in dev):** Automates publishing projects to the marketplace and website from a single source.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=1154.0)
  - [**Ty's "FaceGate" Project:**](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=2689.0)
      - [**Goal:** Web-native face ID authentication for time and attendance.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=2746.0)
      - [**Use Case:** Guards using a single shared device for clocking in/out.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=2760.0)
      - [**Status:** Live for testing; feedback link to be added.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=2689.0)
  - [**Scott's AI News Digest:**](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=2884.0)
      - [**Goal:** Consolidate AI news from multiple RSS feeds.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=2994.0)
      - [**Tech:** Claude Haiku for summarization; RAG for semantic search on a public blog.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=2940.0)
  - [**Ryan's Hedge Fund Software:**](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=3338.0)
      - [**Goal:** Replace an outdated expense system for a London hedge fund.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=3343.0)
      - [**Challenge:** Navigating compliance (ISO, HIPAA, SOC 2) for a finance-specific SaaS product.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=3371.0)
      - [**Strategy:** Target the hedge fund niche, which pays high prices (e.g., £600/user/month).](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=3712.0)

### Technical Deep Dive: RAG & Native App Dev

  - [**RAG Alternatives:** RAG remains the standard for large datasets.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=5961.0)
      - [**Enhancements:** Add layers like re-rankers (e.g., Cohere) for better results.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=6174.0)
      - **Context Window vs. RAG:** Use large context windows for small datasets (\<1000 documents) to avoid RAG overhead.
  - [**Native App Development:**](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=6201.0)
      - [**Challenge:** Building Android/iOS apps with offline sync.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=6201.0)
      - [**Recommendation:** Use Claude Code with existing, well-maintained GitHub repos for Xcode/Swift to accelerate development.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=6272.0)

## Next Steps

  - [**Ty:** Add a feedback link to the FaceGate site and share the URL.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=2689.0)
  - [**Scott:** Share the AI News Digest blog URL and add emails to the digest list.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=2937.0)
  - [**Ryan:** Research compliance requirements (ISO, HIPAA, SOC 2) for the hedge fund project.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=3371.0)
  - [**Alex:** Share the local AI hub setup guide with Ty.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=6751.0)
  - [**All:** Explore the "Everything Cloud Code" project link for new skills and plugins.](https://fathom.video/share/qoW1vQ6RNbHoxkaUEWxwUFVDoprb5NKc?tab=summary&timestamp=7334.0)

