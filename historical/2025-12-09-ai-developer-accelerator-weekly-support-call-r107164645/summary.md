## Meeting Purpose

[A weekly sync for AI developers to share progress, get feedback, and collaborate.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=1134.0)

## Key Takeaways

  - [**Enterprise AI Adoption:** Patrick is evaluating enterprise licenses for major platforms (OpenAI, Anthropic, Gemini) to build a multi-provider strategy, using a Cloud Code agent for horizontal market analysis.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=754.0)
  - [**Agentic Workflow Optimization:** Scott is parallelizing agents in his personal assistant to solve context window limits and improve performance, inspired by Trigger.dev patterns.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=1170.0)
  - [**AI-Powered Business Scaling:** Maksym is scaling automotive AI solutions (WhatsApp chatbots, voice agents) to new clients (Mazda, Infinity), while Ryan is automating his social media agency to 10-20x revenue.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=2725.0)
  - [**ShipKit Onboarding Overhaul:** Brandon will revamp ShipKit's onboarding to help users select the right project template, addressing a key pain point identified by the community.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=688.0)

## Topics

### Enterprise AI Strategy & Market Analysis

  - [Patrick is evaluating enterprise licenses for OpenAI, Anthropic, Gemini, and Perplexity to build a multi-provider strategy.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=754.0)
      - [**Rationale:** Avoid vendor lock-in by dynamically routing token spend to the best-performing model for any given task.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=824.0)
  - [He is building a Cloud Code agent for horizontal market analysis.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=941.0)
      - [This agent tracks provider news, model releases, and market sentiment to generate an "evolution curve" of the AI landscape.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=951.0)
      - [**Finding:** Cloud Code's web search and fetch capabilities are more powerful for this task than Gemini CLI.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=871.0)
  - [A new internal process uses this analysis to validate business requirements.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=1059.0)
      - [Each requirement is assigned a confidence score.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=1076.0)
      - [The score updates daily based on agent findings; falling below a threshold triggers a strategy change.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=1076.0)

### Agentic Workflow Optimization

  - [Scott is optimizing his personal assistant by parallelizing agents.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=1170.0)
      - [**Problem:** A single agent for a morning summary was slow and hit context window limits.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=1592.0)
      - [**Solution:** Inspired by Trigger.dev, he now runs three agents (Core Summary, Follow-up Check, Relationship Check) in parallel.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=1240.0)
      - [**Implementation:** Built internally using the Anthropic TypeScript SDK and Google APIs, not Trigger.dev.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=1760.0)
      - [**Context Window Management:** Solved by setting hard-coded rules (e.g., analyze only the last 7 days of emails) and using summaries instead of full transcripts.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=1592.0)

### AI-Powered Business Scaling

  - [**Maksym (Automotive AI):**](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=2725.0)
      - [Onboarded Mazda and Infinity as clients for his WhatsApp chatbots and voice agents.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=2725.0)
      - [**Solutions:**](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=2735.0)
          - [**Salesperson-facing:** A WhatsApp bot for field sales with pricing, credit, and media info.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=2735.0)
          - [**Client-facing:** A public WhatsApp/voice agent for direct customer inquiries.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=2762.0)
      - [**New CRM Feature:** A simple WhatsApp-based lead tracking system solves low CRM adoption by sales teams, providing real-time activity data to management.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=2948.0)
      - [**Side Project:** A B2C iMessage assistant for calendar, email, and document queries, now in beta.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=3120.0)
  - [**Ryan (Social Media Automation):**](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=2024.0)
      - [Building a social media automation app to scale his agency's revenue 10-20x.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=2598.0)
      - [**Stack:** Netlify, Supabase, Cloudflare R2, Claude, and Nano Banana 3 Pro.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=2299.0)
      - [**Feature:** Integrated image retouching and generation using Nano Banana 3 Pro, allowing users to edit images directly in the app.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=2046.0)
      - [**Blocker:** A recent Claude Code backend change broke the image generation API, halting progress.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=2006.0)
  - [**Tiran (Consulting & Personal Tools):**](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=6092.0)
      - [**CV Refinery:** Analyzes a resume against a job description, suggesting improvements to pass ATS filters.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=6138.0)
          - [**New Idea (from Patrick):** Repurpose for consulting firms to automate CV reformatting for RFPs.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=6548.0)
      - [**Prepper Tool:** Generates detailed emergency preparedness plans (supplies, maps, skills) based on user inputs.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=6232.0)
          - [**Insight:** ShipKit's prompts significantly improved the product's architecture and UI.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=6232.0)
      - [**Consulting Report Generator:** Converts markdown reports into interactive web applications with drill-down graphics, disrupting the traditional deliverable format.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=6348.0)
      - [**Sherpa Cow:** A trip planner using a workflow-based UI for flexible itineraries with fixed sequences and parallel options.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=6635.0)
      - [**Dropbox Photo Gallery:** A one-day project that creates a website from a Dropbox folder, caching photos in Supabase and using AI for face recognition.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=6864.0)

### ShipKit & Development Workflow

  - [**Onboarding Overhaul:** Brandon will revamp ShipKit's onboarding to help users select the right project template and accommodate different learning styles.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=7282.0)
  - [**Development Workflow:**](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=7450.0)
      - [**Brandon's Method:** 90% Cloud Code for logic, 10% Anti-Gravity with Gemini 3 Pro for visual tasks.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=7526.0)
      - [**Ryan's Blocker:** A broken API call in Claude Code, possibly due to an uncommitted change.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=2006.0)
      - [**Recommendation:** Use AI-assisted Git commits (e.g., a `git workflow commit` command) to maintain a clean history and enable easy rollbacks.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=2360.0)
  - [**Local Models:**](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=5076.0)
      - [**Tool:** OpenCoder was recommended as an open-source alternative to Claude Code for running local models.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=5199.0)
      - [**Model:** Quen3 Coder was suggested, with a smaller quantization to fit within 24GB of RAM.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=5076.0)
  - [**Voice Models:**](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=5270.0)
      - [**Trade-off:** Latency vs. tool-calling capability.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=5270.0)
      - [**Recommendations:**](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=5270.0)
          - [**GPT-4.0 mini:** A good balance (\~45ms latency) per Ty.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=5312.0)
          - [**GPT Real-time:** OpenAI's new model specifically for voice agents.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=5373.0)

## Next Steps

  - [**Brandon:**](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=7276.0)
      - [Revamp ShipKit onboarding to guide template selection.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=7282.0)
      - [Build and record the "Worker SaaS to Video Production App" walkthrough (Jan 2026).](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=7317.0)
      - [Share the GitHub repo for the video app build with Elijah as it progresses.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=7394.0)
  - [**Patrick:**](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=577.0)
      - [Publish the code for the template-selection agent to the community.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=577.0)
  - [**George:**](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=3415.0)
      - [Begin building the policy automation tool using the Worker SaaS template.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=3525.0)
  - [**Elijah:**](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=5882.0)
      - [Coordinate a tutorial for Brandon's partner on using Linked Helper for LinkedIn outreach.](https://fathom.video/share/W1mbkPMSEJHSHJhdFXkyBHynCTtVRZ7D?tab=summary&timestamp=5882.0)

