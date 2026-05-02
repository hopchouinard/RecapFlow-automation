## Meeting Purpose

[To share project updates, demo new tools, and discuss AI development strategies.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=2987.0)

## Key Takeaways

  - [**Brandon's EMS Soap startup is funded.** It uses the Shipkit RAG template to automate EMS billing, proving the template's real-world value.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=2987.0)
  - [**Dmitry is building an agentic orchestrator.** It automates the full SDLC and has already attracted interest from CIOs and a potential reseller.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=3226.0)
  - [**Gemini 3 Flash Preview is a top production model.** It's faster and cheaper than GPT-4.1, excelling at complex, single-shot instructions.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=8941.0)
  - [**New tools accelerate development.** `git worktrees` enable parallel feature work, while `Graphite` and `Render.com` solve complex merging and hosting issues.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=3394.0)

## Topics

### Startup & Funding Updates

  - [**Brandon's EMS Soap:** A startup automating EMS billing reports.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=2995.0)
      - [**Origin:** Grew from a simple GPT built by a co-founder (an EMS chief).](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=3045.0)
      - [**Funding:** Secured a seed round from Tiny Seed in November.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=3060.0)
          - [**Requirement:** $500 MRR for several months.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=9698.0)
      - [**Business Model:** High-margin token sales (costing dollars, sold for hundreds).](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=3180.0)
  - [**Dmitry's Agentic Orchestrator:** A platform for autonomous AI development.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=3226.0)
      - [**Traction:** 6k LinkedIn post views → 3 CIO inquiries, 1 reseller interest, 1 partnership call with Genom.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=3253.0)
      - [**Demo:** "Raj," a production incident agent, investigated a real bug in GitHub Actions logs, identified the root cause (`max_turns` limit), and confirmed a fix was deployed.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=12127.0)

### New Development Workflows & Tools

  - [**`git worktrees` for Parallel Development:**](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=5885.0)
      - [**Problem:** Standard AI dev creates large, untraceable PRs with multiple features.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=5901.0)
      - [**Solution:** Use `git worktrees` to isolate each feature in its own branch and directory.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=5973.0)
      - [**Benefit:** Enables parallel work and clean, single-feature PRs.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=5973.0)
      - [**Bottleneck:** Parallel database migrations (e.g., Drizzle) conflict due to journal file ordering.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=3496.0)
  - [**`Graphite` for Merge Conflicts:**](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=3548.0)
      - [**Solution:** A tool (acquired by Cursor) that manages complex merges, ideal for agent-driven parallel work.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=3548.0)
  - [**`Render.com` & `Railway` for Hosting:**](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=5510.0)
      - [**Problem:** Supabase Edge Functions have a 3-6 minute WebSocket timeout, breaking long-running audio streams.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=5465.0)
      - [**Solution:** Use stateless services like `Render.com` or `Railway` for persistent WebSocket connections.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=5510.0)
  - [**`Deepgram` for Audio Transcription:**](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=5100.0)
      - [**Finding:** More accurate and cheaper than OpenAI Whisper for streaming audio.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=5100.0)
      - [**Benefit:** Offers specialized models (e.g., medical) at no extra cost.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=5726.0)
  - [**`GLM 4.4.7` for Cost-Effective Coding:**](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=6678.0)
      - [**Finding:** A powerful, open-source Chinese model available via OpenRouter for \~$8/quarter.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=6678.0)
      - [**Use Case:** Ideal for non-sensitive coding tasks to save on Claude/Cursor costs.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=6723.0)

### Project Demos & Feedback

  - [**HP's Live Call Coach:**](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=4980.0)
      - [**Function:** A Chrome extension providing real-time coaching during calls.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=4980.0)
      - [**Tech Stack:** Supabase (backend), Deepgram (STT), Vercel (frontend).](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=5100.0)
  - [**Ryan's Screenly:**](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=7854.0)
      - [**Function:** A digital signage SaaS for businesses.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=7854.0)
      - [**Key Features:** Node-based flow builder, QR code lead generation, custom Windows kiosk software.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=8124.0)
  - [**Tiran's Preparedness Site:**](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=8548.0)
      - [**Function:** An AI-driven site for generating personalized emergency preparedness plans.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=8569.0)
      - [**Tech Stack:** Dakota (scraper), PlantUML (diagrams), custom async workflow service.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=8548.0)
  - [**Patrick's Fieldy Integration:**](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=7027.0)
      - [**Function:** An N8N pipeline processing audio from a Fieldy wearable.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=7138.0)
      - [**Innovation:** Used Cloud Code to generate network scripts (VLANs, firewall rules) for a secure local N8N server.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=7262.0)
  - [**Hemal's Image Editing Project:**](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=10516.0)
      - [**Goal:** Automate adding dimensions to product images.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=10516.0)
      - [**Recommended Workflow:**](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=10606.0)
        1.  [**Generate:** Use Gemini 3 Pro Image Preview.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=10606.0)
        2.  [**Critique:** Use a cheaper model (e.g., Gemini 2.5) to validate the output.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=11207.0)
        3.  [**Upscale:** Use a separate, cheaper upscaling model if needed.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=10845.0)

## Next Steps

  - [**Brandon:**](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=3394.0)
      - [Record a Shipkit module on the `git worktrees` workflow.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=3394.0)
      - [Update the Shipkit RAG template for a deprecated Google embedding model.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=3139.0)
      - [Connect Ryan with the brewery contact for a potential Screenly client.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=8223.0)
      - [Unblock HP and Pranav from the school group.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=5768.0)
  - [**Dmitry:**](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=3226.0)
      - [Connect with Tiran to discuss the agentic orchestrator.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=3226.0)
  - [**HP:**](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=4971.0)
      - [Email Brandon to get unblocked from the school group.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=5768.0)
      - [Investigate `Render.com` and `Railway` to fix the WebSocket timeout.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=5510.0)
  - [**Patrick:**](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=7572.0)
      - [Connect with Dmitry to discuss agentic SDLC.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=7572.0)
  - [**Ryan:**](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=7839.0)
      - [Email Brandon to connect with the brewery contact.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=8223.0)
  - [**Tiran:**](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=8548.0)
      - [Connect with Dmitry to discuss the agentic orchestrator.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=3226.0)
      - [Test the Gemini 3 Flash Preview model for the preparedness site.](https://fathom.video/share/fs9ycJM9u4wEzxbgKy7_C_vpgMwiFs1L?tab=summary&timestamp=8941.0)

