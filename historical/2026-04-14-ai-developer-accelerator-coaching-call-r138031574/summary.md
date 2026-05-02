## Meeting Purpose

[A coaching call for AI developers to share progress, challenges, and insights.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=846.0)

## Key Takeaways

  - [**Enterprise AI Strategy:** For Microsoft shops, prioritize Azure Foundry over Copilot Studio. The latter's Power Automate-style agents are outdated, while Foundry offers a modern, Claude-powered path forward.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=853.0)
  - [**Agent Security & Legality:** Use caution with self-hosted agents (e.g., OpenClaw) for corporate or legal tasks. Anthropic's new "Claude Managed Agents" are a safer, enterprise-grade alternative.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=2501.0)
  - [**New Dev Paradigms:** AI is shifting developer roles from coding to strategy and management. New workflows include user-driven development (Ty) and using AI as a "meat-based USB stick" to bridge developer contexts (Patrick).](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=2916.0)
  - [**Idea Management:** Use Andrej Karpathy's "LLM Wiki" prompt in Obsidian to structure AI conversations into a navigable wiki, helping to filter and prioritize project ideas with market value.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=3584.0)

## Topics

### Enterprise AI Strategy: Microsoft vs. Google

  - [**Microsoft Stack:**](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=853.0)
      - [**Copilot Studio:** Avoid for new agent development. Its Power Automate-style agents are an outdated paradigm, especially now that models can generate code directly.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=1367.0)
      - [**Azure Foundry:** The recommended path. It offers a modern platform with more models and features, including Red Hat vulnerability scanning agents.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=1001.0)
      - [**Anthropic Partnership:** Microsoft's deep integration of Claude (Opus, Sonnet) into Copilot and M365 is a major intelligence upgrade. This could soon bring Anthropic's managed agent capabilities (e.g., Co-Work) directly into the Microsoft ecosystem.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=921.0)
  - [**Google Stack:**](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=1184.0)
      - [**Gemini Pro:** Excellent for individual use.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=1184.0)
      - [**Gemini Enterprise:** Currently has significant limitations, lacking feature parity with the Pro version. For example, it cannot generate Google Docs directly, only Markdown.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=1184.0)
  - [**Local Models:**](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=1524.0)
      - [**Rationale:** A cost-effective strategy is to use local, open-source models (e.g., on a Proxmox server) for simple tasks and reserve expensive, powerful models (e.g., Claude Opus) for complex work.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=1524.0)

### New Development Paradigms & Workflows

  - [**User-Driven Development (Ty):**](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=2027.0)
      - [A full-loop feedback system where users narrate issues via a recording widget.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=2040.0)
      - [The system then generates a plan → creates a PR → allows for mobile review and merge.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=2100.0)
      - [**Key Feature:** Captures console logs automatically for debugging.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=2119.0)
  - [**"Meat-Based USB Stick" (Patrick):**](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=2916.0)
      - [A workflow where developers manually copy-paste AI messages between their individual Claude Code instances to share context and solve bugs.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=2916.0)
      - [**Significance:** Highlights how AI-assisted coding is reinventing the Software Development Life Cycle (SDLC) and developer roles.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=2916.0)
  - [**Agent-Driven RFQ/RFP Generation (Alex, David):**](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=2314.0)
      - [**Alex:** Building an agent to scrape government tenders (RFPs) for sales leads.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=2314.0)
      - [**Paul's Insight:** Scrape government meeting minutes for early signals of upcoming projects, providing a competitive advantage.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=2417.0)
      - [**David:** Building an event management platform that automates RFQ creation and negotiation with vendors.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=3262.0)
  - [**C-Suite Adoption:**](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=2716.0)
      - [A C-suite executive, after a Claude Code training, requested a local Python/NPM setup.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=2716.0)
      - [**Significance:** High-level adoption creates a powerful internal advocate, opening doors for broader AI initiatives. This executive's usage already reached $3,000/month on a token-based enterprise plan.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=2765.0)

### Tools & Resources

  - [**Andrej Karpathy's "LLM Wiki" Gist:**](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=3584.0)
      - [A prompt for Claude (or other LLMs) that structures raw conversation logs into a navigable wiki in Obsidian.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=3584.0)
      - [**Use Cases:**](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=3584.0)
          - [**Idea Filtering (Patrick, David):** Helps organize and prioritize project ideas.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=3584.0)
          - [**RAG Preprocessing (Patrick):** Enriching data with metadata before vectorization.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=3709.0)
  - [**Ghost Database:**](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=3990.0)
      - [A CLI-only Postgres database designed for agents to programmatically create, use, and destroy databases on the fly.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=3990.0)
  - [**Memory Palace:**](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=4174.0)
      - [A visual database organization concept that maps data to a mental "palace" for relational recall.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=4221.0)
  - [**LensDB:**](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=4083.0)
      - [A portable, embeddable vector database that can be packaged directly with an application.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=4083.0)

### Business & Strategy Challenges

  - [**Productizing AI Consulting (Elijah):**](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=4587.0)
      - [**Challenge:** Defining a repeatable business model (consulting vs. productized SOWs) when clients have vague needs.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=4651.0)
      - [**Solution:** Focus on identifying and solving the client's biggest pain points, not just the most recent or obvious problems.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=4769.0)
  - [**Cemetery Project (Morgan):**](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=3810.0)
      - [**Progress:** Received a layout map to manually create initial GIS data.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=3810.0)
      - [**Blocker:** Client's IT resources are tied up with a complex billing system migration (Tyler on AWS GovCloud).](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=3827.0)
      - [**Opportunity:** The project serves an underserved niche (680 cemeteries), creating a strong market position.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=3888.0)

## Next Steps

  - [**David:** Demo the automated RFQ/negotiation platform next week.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=3403.0)
  - [**Alex:** Evaluate Anthropic's "Claude Managed Agents" for the RFP scraping project.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=2501.0)
  - [**Morgan:** Share the recently completed NDA project once the NDA is cleared.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=3782.0)
  - [**Patrick:** Continue developing the community intelligence project for a demo in 1–2 weeks.](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=2641.0)
  - [**Elijah:** Await results of the Presidential AI Challenge regional pitch (Thursday, 2 PM).](https://fathom.video/share/SNhR8ov1f1tnosMWN_KML4TMJq2E5jiV?tab=summary&timestamp=4937.0)

