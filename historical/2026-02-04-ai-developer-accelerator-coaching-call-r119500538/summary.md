## Meeting Purpose

[To share AI development progress, discuss challenges, and exchange best practices.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=488.0)

## Key Takeaways

  - [**Secure Agents with "Digital Coworker" Isolation:** To mitigate risk, treat agents like coworkers by giving them their own isolated accounts (Gmail, GitHub) and using SSH tunnels for access. This prevents them from accessing your personal data and forces all work through auditable pipelines like GitHub PRs.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=3967.0)
  - [**Iterate with AI, Automate with Code:** Use AI to quickly prototype complex workflows. Once a process is deterministic, convert it to a local script (e.g., JavaScript) to eliminate token costs and reduce execution time from minutes to seconds.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=2415.0)
  - [**Build "Software on Demand":** Replace costly SaaS subscriptions by building custom tools for specific needs. This approach creates highly valuable, single-user software that perfectly fits a business's unique requirements.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=5057.0)
  - [**Navigate Corporate AI with Governance:** In regulated environments like banking, AI success hinges on governance. Start by building a RAG system on internal policies, aligning with approved cloud providers, and framing AI as an "assisted developer" to gain buy-in.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=5964.0)

## Topics

### The OpenClaw Security Framework

  - [Patrick shared a framework for securely operating OpenClaw, documented on a site built with Claude Code.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=3853.0)
  - [**Core Principle:** Treat the agent as a "digital coworker" with its own isolated identity.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=3967.0)
      - [**Accounts:** Dedicated Gmail, calendar, and GitHub accounts for the agent.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=3978.0)
      - [**Access:** No public web panel; use SSH tunnels for maintenance.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=4057.0)
      - [**Workflows:** All code and artifacts are pushed via GitHub PRs, requiring human approval.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=3998.0)
      - [**Memory:** Externalized to an Obsidian vault for full auditability.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=4087.0)
  - [**Tech Stack:**](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=4179.0)
      - [**VM:** Low-resource Linux VM (4GB RAM, 50GB disk, 2 cores).](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=4179.0)
      - [**Models:** OpenClaw uses Claude for orchestration; Claude Code is a tool for coding tasks.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=4225.0)

### Frank Labs: AI Team Augmentation

  - [Ty demoed Frank Labs, a platform providing AI "employees" (e.g., SDRs, support) to augment business teams.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=1194.0)
  - [**Key Features:**](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=1265.0)
      - [**Hybrid Model:** Uses Mistral 7B (local EC2) for general tasks and GPT-4o for complex functions.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=1528.0)
      - [**Guardrails:** A "council" of independent agents provides self-checking for security and prompt injection.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=1699.0)
      - [**Lead Gen Stack:** Perplexity, Hunter, Apollo, and Clay are used as tools for lead enrichment.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=2251.0)

### Iterating with AI, Automating with Code

  - [Morgan shared a workflow for building a deterministic process:](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=2415.0)
    1.  [**Prototype:** Use Claude skills to define and test a process (e.g., MD → HTML → PDF).](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=2415.0)
    2.  [**Convert:** Once deterministic, have Claude convert the skill's logic to a local script (e.g., JavaScript).](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=2478.0)
    3.  [**Automate:** The skill now calls the script, eliminating token costs and reducing execution time from minutes to seconds.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=2567.0)

### Navigating Corporate AI Adoption

  - [Juan noted friction when introducing agentic workflows to teams with traditional development methods.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=2746.0)
  - [**Advice for Corporate Roles (Anna's banking role):**](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=5964.0)
      - [**Governance:** This is the bedrock of AI in finance (e.g., SOC 2 compliance).](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=6077.0)
      - [**Alignment:** Build a RAG system on internal policies and align with approved hyperscalers (AWS, Azure).](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=6240.0)
      - [**Strategy:** Frame AI as an "assisted developer" to gain buy-in and offer services to security teams to build rapport.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=3126.0)

### "Software on Demand" Philosophy

  - [Ty demonstrated this by replacing SaaS subscriptions with custom-built tools:](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=5057.0)
      - [**Ticketing System:** Built a custom system to replace Zendesk.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=5067.0)
      - [**Invoicing:** Building a custom tool to replace FreshBooks.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=5091.0)
  - [**Rationale:** Building exactly what is needed for a single user often provides more value than adapting a generic SaaS product.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=5156.0)

### Deploying with AI

  - [Raghav asked how to use AI for cloud deployments.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=7933.0)
  - [**Recommendation:** Use a simple platform like Vercel.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=8041.0)
  - [**Process:**](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=7933.0)
    1.  [**Initial Setup:** Ask Claude Code for step-by-step guidance on setting up the Vercel CLI.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=8199.0)
    2.  [**Automation:** Use a cron job or pre-commit hook to automatically update all CLIs before deployment.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=8238.0)

## Next Steps

  - [**Morgan:** Share the Claude conversation template for multi-tenancy with Paul Gallovich and Shah Martinez.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=842.0)
  - [**Patrick:** Post GitHub profile link in the School community.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=4962.0)
  - [**Raghav:** Use Claude Code to guide the Vercel CLI setup for deployment automation.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=8199.0)
  - [**Anna:** Join the San Diego Machine Learning Group for advice on the recommendation system project.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=5859.0)
  - [**All:** Explore the OpenClaw security framework and "Software on Demand" philosophy.](https://fathom.video/share/yWxzySKYx7E-_Up3x26syxPBmvL67-r_?tab=summary&timestamp=3853.0)

