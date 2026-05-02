## Meeting Purpose

[Weekly support and project updates for AI developer accelerator members.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=1475.0)

## Key Takeaways

  - [**Partnerships bridge skill gaps:** Non-technical founder Garron Selliken is partnering with technical developer Prem to build a real estate CRM, combining Garron's industry knowledge with Prem's ShipKit expertise to avoid the high overhead of a traditional startup.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=1589.0)
  - [**Claude Code is the preferred dev tool:** Its superior agent scaffolding and cost-effective, revolving 5-hour free window are preferred over Cursor's fixed monthly fee and less mature VS Code extension.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=2776.0)
  - [**AI automates complex tasks:** Ryan demoed a social media app using AWS Rekognition for facial tagging and a voice-driven quiz for automated brand discovery, while Patrick is building a "CV knowledge graph" to auto-tailor resumes for job descriptions.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=3939.0)
  - [**Automate cloud ops with local agents:** Instead of a dedicated EC2 instance, a local Claude Code agent using AWS CLI skills is recommended for managing cloud resources, as it avoids the security and maintenance overhead of another server.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=5707.0)

## Topics

### Project Updates & Demos

  - [**Ryan's Social Media Automation App:**](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=3939.0)
      - [**New Features:**](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=3945.0)
          - [**Facial Recognition:** Integrates AWS Rekognition to scan uploaded images and tag team members, which informs AI-generated post content.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=3952.0)
          - [**Real Estate Mode:** Connects to property management systems to auto-pull listings and photos for post creation.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=3960.0)
          - [**Automated Brand Discovery:** Replaced manual onboarding with a voice-driven quiz that populates the AI's brand voice and context.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=4210.0)
      - [**Backend:** Uses Publer for social media API integration and the Anthropic SDK for content generation.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=4364.0)
      - [**Status:** First paying client is live; the goal is to scale onboarding to 100+ clients/month.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=4140.0)
  - [**Patrick's "CV Knowledge Graph":**](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=6057.0)
      - [**Goal:** Eliminate manual CV updates for RFPs and job applications.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=6100.0)
      - [**Functionality:**](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=6119.0)
          - [**Import:** Parses a CV into structured entities (experience, skills) and stores them in a vector database.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=6130.0)
          - [**Intake Chat:** Enables conversational updates to the database, auto-formatting new entries.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=6190.0)
          - [**Job Output (WIP):** Will match a job description against the database to generate a tailored CV.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=6251.0)
          - [**Publish (WIP):** Builds a static website from the data via GitHub Actions.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=6288.0)
      - [**Tech:** Combines ShipKit's RAG template with OpenRouter for multi-model selection, optimizing cost and performance.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=6342.0)
  - [**Ty's Kiosk App:**](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=2297.0)
      - [**Breakthrough:** Successfully reverse-engineered the middleware layer for hardware communication (e.g., bill acceptors).](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=2302.0)
      - [**Status:** Now ready to develop hardware-specific features.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=2302.0)
  - [**Morgan's React Dependency Fix:**](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=4832.0)
      - [**Problem:** A project had conflicting `package-lock.json` files from mixed use of NPM and PNPM.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=4847.0)
      - [**Solution:** Standardized on PNPM and explicitly defined package versions to resolve dependency conflicts.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=4847.0)
      - [**Rationale:** PNPM is preferred by Claude and used internally by Vercel, suggesting it may simplify deployment.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=4944.0)

### Development Strategy & Tooling

  - [**Partnerships for Non-Technical Founders:**](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=1589.0)
      - [**Problem:** Garron Selliken, a non-technical founder, built a real estate CRM prototype but faces a high learning curve to build a production app.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=1589.0)
      - [**Solution:** Partner with a technical developer (Prem) to leverage ShipKit expertise.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=2076.0)
      - [**Rationale:** This model avoids the high overhead of a traditional startup (e.g., Garron's prior venture had $200k/month overhead).](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=1743.0)
  - [**ShipKit Template Usage:**](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=2428.0)
      - [**Combining Chat & RAG:** Start with the more complex RAG template, then add chat functionality.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=2499.0)
          - [**Method 1:** Use Claude Code to reference the simple chat project and integrate its code.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=2896.0)
          - [**Method 2:** Place the simple chat project in the `AI Docs/refs` folder to provide it as context for the RAG agent.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=2935.0)
      - [**IDE Compatibility:** ShipKit templates are built for Cursor and Claude Code.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=2776.0)
          - [**Recommendation:** Use Claude Code in your IDE's terminal for full feature parity. The VS Code/Cursor extension is less mature and may break with multi-agent workflows.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=3540.0)
          - [**GitHub Sync:** The IDE email must match the GitHub email for ShipKit to function correctly.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=3070.0)
  - [**Automating Cloud Architecture:**](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=5256.0)
      - [**Problem:** Juan Torres proposed using a dedicated EC2 instance as an "oracle" to manage AWS resources via the CLI.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=5256.0)
      - [**Alternative:** A local Claude Code agent running headless.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=5707.0)
      - [**Rationale:** Avoids the security and maintenance overhead of another server.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=5590.0)
      - [**Implementation Tip:** Include the AWS CLI documentation repo as a submodule to give the agent the best context for building skills.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=5772.0)

## Next Steps

  - [**Garron Selliken:** Connect with Prem to discuss a technical partnership for the real estate CRM.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=2066.0)
  - [**Ryan:** Trim the brand discovery quiz to reduce client onboarding friction.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=4210.0)
  - [**Juan Torres:** Research building a local Claude Code agent with AWS CLI skills for cloud resource management.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=5256.0)
  - [**Patrick Chouinard:** Host the next weekly support call.](https://fathom.video/share/6kxoxY7iK1RG4oZ6tyvsD54tQrfj6zsW?tab=summary&timestamp=6893.0)

