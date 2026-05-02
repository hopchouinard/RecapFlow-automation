## general

This was a group coaching call for an AI-focused developer/entrepreneur community, hosted by Brandon Hancock with Patrick Chouinard facilitating. The session followed a round-robin format where each member gave updates on their current projects and received feedback from the group. Participants joined from multiple time zones including Australia (Paul Miller in Melbourne), New Zealand, the UK (Ryan), the US, and elsewhere.

Brandon opened with updates on EMS Soap, his emergency services SaaS, which is on the verge of a strategic partnership that would scale from 7 customers/1,000 users to 200 customers/100,000 users. He also shared observations about the "SaaSpocalypse" — the trend of AI enabling individuals to replicate simple SaaS products — and emphasized the importance of building systems, leveraging Claude Code while it remains subsidized, and building in public to attract opportunities.

Projects demoed or discussed included: Tony's restaurant POS and landing page system (his first paying client); Ty's graduation seating app rebuild, a cybersecurity coaching platform called ShipSafe, a personal intelligence system called Propia, and a "user-driven development" workflow where users narrate bugs via screen recording and Claude Code auto-generates PRs; Juan's image-to-image AI photo booth application built on AWS; Patrick's community knowledge base (vector database of two-plus years of call transcripts using N8N, LanceDB, Ollama, and a multi-model pipeline), plus a conceptual "SideQuest" cognitive service bus for Claude Code; Ryan's LeadCap iOS/Android app integrating with Meta Ray-Ban glasses for cold-call sales prospecting; Morgan's catio craftsman website on Astro/Cloudflare and an Oxytocin Rewire wellness SaaS with multi-model AI backend; Tiran's "Be Prepared" emergency preparedness platform with monitoring, content factory, and e-commerce components; and Adam's SaaS project and charity bank-transfer payment integration.

The session closed with extended discussion on B2B SaaS onboarding for government/institutional clients (Morgan's Heritage Plot cemetery compliance app), hiring strategies for distributed teams, and landing page/funnel optimization advice for Tiran's Be Prepared platform.

## insights

- **SaaSpocalypse is real and happening now**: Brandon demonstrated personally rebuilding a $20/month SaaS using Claude Code in under an hour. Any SaaS without a moat (compliance, network effects, proprietary data, or specialized vertical knowledge) is vulnerable to instant replication.
- **The current AI subsidy window is finite**: Brandon estimated that Claude Code usage at his pace would cost ~$30,000/month at real API prices. The subsidized period is the time to build aggressively and establish market position.
- **Vertical domain expertise is the new moat**: Paul Miller articulated that when code is trivially replicable, the trust, industry language, and domain credibility of the person delivering it becomes the differentiator.
- **Ty's "user-driven development" workflow**: Users record screen + narrate issues via a floating widget → AI analyzes the video, asks clarifying questions, reaches 85% understanding → spawns a Claude Code session → generates a plan → emails Ty for approval → creates a PR. Ty approves from his phone while golfing.
- **Patrick's multi-model pipeline hierarchy**: Use the right cognitive power at the right step. Complex extraction → Claude Sonnet 4.6; high-quality writing → Kimi K2.5; summarization/tagging/compression → Gemma 4B (free, local). This keeps costs very low while maintaining quality.
- **Post-commit hooks for automatic documentation**: Patrick recommended adding a git post-commit hook in Claude Code that auto-generates documentation for each session, then building a skill to compile it into a navigable site — squeezing content creation out of every development action.
- **"Once you've done something twice, skill it"**: Patrick's heuristic for when to formalize a repeating process into a Claude Code skill/template.
- **Building in public creates unexpected opportunities**: Brandon's EMS Soap partnership with Raul (an EMS chief) came from YouTube content. Ryan's first inbound lead came after deploying an SEO agent on his rebuilt website.
- **Pricing is a binary search**: Rather than incrementally raising prices, double the price to find friction faster. Only useful once you have multiple customer conversations per month.
- **For B2B/government SaaS, self-service onboarding doesn't apply**: Contracts, manual invoicing, and check payments are the norm. Admin-controlled account activation is the right model.
- **Morgan's competitor research strategy**: Find public user groups for competing products, harvest the complaints, and make sure your product covers all those pain points before launch.
- **Chamath's 80-90 AI company model**: Build 80% of enterprise SaaS features at 10% of the cost using lean AI-powered teams — a legitimate business model being executed at scale.
- **For consumer SaaS landing pages, minimize friction to the "wow" moment**: Tiran's Be Prepared landing page advice — the hero should be a single address input that immediately generates a report preview, then gate the full report behind email capture.
- **Claude Code remote control**: You can start a remote session with `/remote` in Claude Code and control running sessions from your phone via the Claude mobile app — useful for voice-driven development on the go.

## qa

**Q (Tony):** How can I use one codebase for all my restaurant clients while giving each different features?
**A (Patrick Chouinard):** Separate code, configuration, and content into three distinct buckets. Code is shared and updated once for everyone. Configuration (per-client feature flags) lives in a clients.json file read via an environment variable in Vercel. Content (hours, addresses, menus) varies per client. This is the standard multi-tenant pattern.

**Q (Brandon):** What email service are you using for the graduation seating app?
**A (Ty Wells):** Resend. Had a rate-limit issue last year but they responded quickly and increased the limit. This year used the batch feature to send in groups of ~100 at a time to avoid hitting thresholds.

**Q (Juan):** Have you thought about switching from Resend to AWS SES directly, since Resend is essentially a front-end for SES?
**A (Ty Wells):** Good point — will look into it. Uses Resend across multiple projects including a multi-tenant ERP, so cutting out the middleman would apply broadly.

**Q (Brandon):** What's the reason Claude Sonnet 4.6 was chosen over other models for the extraction step in Patrick's pipeline?
**A (Patrick Chouinard):** Transcript data is not clean, so extraction is cognitively intense. Sonnet 4.6 handles it best. Kimi K2.5 is used for writing (community posts) because it's close to Sonnet quality at lower cost. Gemma 4B handles summarization and tagging locally for free.

**Q (Brandon):** Is Claude Sonnet 4.6 still available in Claude Code?
**A (Patrick Chouinard):** No — 4.6 was dropped from Claude Code. Available options are now Sonnet 4.7, Sonnet 4.6 1M context, or Haiku 4.5. (Morgan Cook later noted you can still invoke 4.6 via `claude --model claude-opus-4-6-[1m]` parameter on Linux with Claude Code v2.1.116.)

**Q (Brandon):** How are you planning to handle the async return of results in the SideQuest cognitive service bus concept?
**A (Patrick Chouinard):** Not a hanging promise — just files. Claude Code dispatches a task (e.g., research to Gemini, or a workflow to N8N), and when the process completes, the result is written as a tangible artifact file that Claude Code can then consume. No tokens spent waiting.

**Q (Morgan):** For B2B SaaS selling to government/institutional clients, is the onboarding process the same as B2C self-service?
**A (Brandon Hancock + Adam):** No. In large B2B, especially government, there is no self-service signup. Accounts are activated manually by admins. Payment is via invoice and check (often above ACH limits). The sales motion is demos, pilot programs, and contracts. Focus on getting to the "aha moment" as fast as possible in the demo, and use a cost/ROI calculator in real time during sales calls.

**Q (Ryan):** What framework did you use to build the iOS/Android app?
**A (Ryan - One Stop Creative Agency):** Expo.dev — handles both iOS and Android from one codebase. Used with Cursor as a visual IDE and Claude Code in the terminal. You can tell Claude to build an EAS test build and it links up with Expo automatically.

**Q (Tiran):** What's the best way to get customers for Be Prepared given the broad target audience?
**A (Brandon Hancock):** Two primary playbooks: SEO (you're sitting on unlimited location-specific data that can generate long-tail content at scale) and Google Ads (~$100/day to test). Third, micro-influencers in the preparedness space. But first, simplify the landing page to a single address input that immediately shows a report preview — that's the minimum friction path to the "wow" moment.

## tools

- **Claude Code** — Primary agentic development environment used by nearly all participants; Brandon hit usage limits spending ~$120 in 30 minutes
- **Resend** — Email delivery service used by Ty for graduation seating app; batch feature used to avoid rate limits
- **AWS SES** — Suggested by Juan as a direct alternative to Resend for email sending
- **N8N** — Workflow automation used by Patrick for the recap/transcript processing pipeline and proposed for SideQuest cognitive service bus
- **LanceDB** — Portable vector database Patrick is using to store community knowledge embeddings, to be published on GitHub
- **OpenWebUI** — Local AI interface Patrick is targeting for querying the community knowledge base
- **Ollama** — Local inference runtime; Patrick uses it with Gemma 4B for embeddings and inference
- **Gemma 4B** — Local model used by Patrick for summarization/tagging steps in the pipeline; runs on most machines
- **Kimi K2.5** — Used by Patrick for community post writing; near-Sonnet quality at lower cost
- **Claude Sonnet 4.6** — Used by Patrick for complex extraction steps in the transcript pipeline
- **Pencil MCP** — Free MCP used by Tony to generate hi-fi UI mockups from design tokens; noted as facing competition from Claude's native design feature
- **Convex** — Database backend used by Tony for his restaurant POS system
- **Stripe** — Payment processing; Tony integrating for online ordering; Ryan integrating for LeadCap subscriptions
- **Supabase** — Database/auth platform; discussed for Tony's project and Ryan's LeadCap; noted for occasional downtime and persistent auth issues on iOS
- **Vercel** — Hosting platform; mentioned in context of a security breach (env vars stored in plaintext if not marked sensitive); Brandon's bill is ~$700/month
- **Cloudflare (Workers/D1/Pages)** — Used by Morgan for catio website; essentially free tier for low-traffic static sites, ~$10-15/month at higher volume
- **Astro** — Static-first frontend framework used by Morgan for catio site and by Patrick for documentation sites
- **Expo.dev** — Cross-platform iOS/Android framework used by Ryan for LeadCap; handles both platforms from one codebase
- **FlutterFlow** — Mentioned as an alternative to Expo for cross-platform mobile; generates Flutter code deployable to all app stores
- **Trigger.dev** — Background job/task runner; Tiran uses it heavily for Be Prepared's monitoring pipeline
- **PostHog** — Product analytics with session replay, funnels, and MCP integration; recommended by Brandon for tracking user journeys
- **Microsoft Clarity** — Free session recording tool mentioned by Tiran as already set up; Brandon confirmed it works well
- **Terraform** — Infrastructure-as-code; Juan implemented it for AWS resource provisioning per Brandon's earlier suggestion
- **Meta Ray-Ban glasses** — Hardware integrated with Ryan's LeadCap app for hands-free photo capture of business signage while driving
- **Remotion** — Video generation library Ryan plans to use for creating marketing/tutorial videos programmatically
- **Codex (OpenAI)** — Used by Patrick for code review and adversarial review within Claude Code via plugin; noted as getting better
- **OpenRouter** — Used by Morgan for routing AI requests to the best available model; Kimi K2.6 appeared on it the day of the call
- **GiveButter** — Nonprofit fundraising platform with free processing tier; shared by Morgan for Adam's charity project
- **Google Workspace CLI** — Brand new CLI (month or two old) shared by Patrick for Morgan's Google Workspace automation project
- **Clockify** — Time tracking SaaS Morgan currently uses but plans to replace with a custom-built CLI-based alternative
- **Chessly / chess learning SaaS** — Brandon scraped a chess learning SaaS and rebuilt it locally with a Claude MCP as a demonstration of the SaaSpocalypse
- **80-90 AI (Chamath's company)** — Builds 80% of enterprise SaaS features at 10% of the cost; discussed as a model for the current AI opportunity
- **ShipSafe** — Ty's cybersecurity coaching platform with real-time scanning and CLI tools for teaching security to beginners
- **Propia** — Ty's personal intelligence system aggregating signals from Limitless, Whoop, email, etc.; communicates via Telegram and builds agents from screen-recorded demonstrations
- **LeadCap** — Ryan's iOS/Android SaaS for cold-call sales teams; uses Meta glasses + AI pipeline to research businesses from photos
- **Be Prepared** — Tiran's emergency preparedness platform with monitoring, content factory, e-commerce, and consulting components
- **Heritage Plot** — Morgan's B2B SaaS for cemetery compliance and searchable burial records targeting 682 US cemeteries
- **EMS Soap** — Brandon's emergency services SaaS; on the verge of a strategic deal to go from 7 to 200 customers

## links

- https://aws.amazon.com/ses/ — AWS Simple Email Service; Juan shared as direct alternative to Resend
- https://www.pencil.dev/ — Pencil MCP for generating hi-fi UI mockups; shared by Patrick in chat
- https://claude.ai/design — Claude's native design feature noted as competing with Pencil MCP
- https://church.thoughtbox.ca/ — "Church of Claude" satirical website shared by Patrick; fully built with Claude, includes scriptures, saints, and speech-to-text
- https://molt.church/ — "Church of Molt" (Mold/Claude bots variant) shared by Adam in response
- https://optimization4all.com/ — Logistics meetup community shared by Adam for Paul Miller's Australian logistics opportunity
- https://github.com/googleworkspace/cli — Google Workspace CLI (brand new); shared by Patrick for Morgan's Google Apps Script/Workspace automation work
- https://github.com/HKUDS/CLI-Anything — CLI tool shared by Biggi in context of Google Workspace CLI discussion
- https://givebutter.com — Nonprofit fundraising platform with free processing tier; shared by Biggi/Morgan for Adam's charity project
- https://spread.givebutter.com/ — GiveButter referral/spread link shared by Morgan
- https://www.amazon.com/Explosive-Growth-... — "Explosive Growth" book by Cliff Lerner; recommended by Brandon to Tiran for growth/SEO strategies
- https://fathom.video/customize — Fathom notetaker settings link (from automated bot message)
- https://go.meetgeek.ai/learn — MeetGeek notetaker info link (from automated bot message)

## decisions

- **Brandon** will revert Claude Code to Sonnet 4.6 (or use the `--model` parameter flag) once current work trees are complete, due to issues with Sonnet 4.7 and image handling
- **Brandon** will share the Fathom transcript/recording link with Tiran after the call
- **Ty** will investigate switching from Resend to AWS SES directly to eliminate the middleman across his projects
- **Ty** will run his ShipSafe security scanner against Morgan's catio website
- **Patrick** will publish the fully embedded LanceDB community knowledge base on GitHub as open source once data preparation and chunking quality is finalized
- **Patrick** will build an Astro documentation site explaining the full community brain pipeline (similar to what he did for the Open Claude Secure Architecture)
- **Patrick** will begin processing the full historical backlog of ~2.5 years of transcripts through the ingestion pipeline
- **Tony** will implement staging and production environments for his restaurant POS system
- **Tony** will investigate point-in-time recovery for his Convex database
- **Tony** will implement provider status page monitoring with automated banners in his application
- **Ryan** will reach out to Tiran via email (tiran@bepreparedsolutions.co) to help with SEO for Be Prepared
- **Ryan** will add annual pricing option to LeadCap (suggested by Patrick in chat)
- **Ryan** will target a one-month launch timeline for LeadCap with optimized load times
- **Morgan** will reach out to Scott for advice on Google Apps Script/Workspace integrations
- **Morgan** will contact Paul Miller via DM about joining his team
- **Paul** will reach out to Morgan about his team-building/hiring process
- **Brandon** will help Paul review candidates when he gets down to a shortlist of ~10
- **Tiran** will simplify the Be Prepared landing page hero to a single address input that generates an immediate report preview, gating the full report behind email capture
- **Tiran** will set up PostHog (or Microsoft Clarity) for session recording and funnel tracking before launch
- **Tiran** will pivot e-commerce to populate shopping carts and redirect to Amazon for the first 3-6 months rather than handling fulfillment directly
- **Tiran** will explore partnering with school information systems for distribution of the Class to Curb carpool product
- **Morgan** will begin outreach to additional cemetery counties for Heritage Plot rather than waiting on the current county's IT migration