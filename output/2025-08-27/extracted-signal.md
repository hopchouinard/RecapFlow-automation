## general

This was a weekly group coaching call hosted by Brandon Hancock, covering a wide range of member projects and questions centered on AI development, tooling, and deployment. The session opened with informal discussion between Marc Juretus and Paul Miller about N8N workflows and Railway/DigitalOcean hosting costs before Brandon joined and ran a structured round-robin format.

Brandon briefly previewed ShipKit, a prompt-driven course and boilerplate product he is actively building, describing its template-based approach (RAG, chat, ADK agent templates) and its goal of making app development accessible through structured prompts. Members then took turns sharing project updates and asking technical questions covering topics including N8N automation, Supabase security, webhook payload sizing, vibe coding in corporate environments, ADK (Google Agent Development Kit) integration with Django and FastAPI, Next.js hosting, LinkedIn data scraping and GDPR compliance, MCP security, authentication routing bugs, and voice assistant tooling.

Notable member projects discussed included: Marc's N8N webhook demos deployed on Railway; Juan's VPN connectivity solution using Tailscale on a shared GPU server running LLM inference; Tom's asset management SaaS being converted to a multi-tenant product; Jaylen's Topic Launch platform (crowdfunded YouTube content ideas); Ola's property management platform integrating ADK into Django; Hemal's rich-content chatbot with multi-agent routing; and Adam's potential consulting engagement with a hedge fund headhunter.

The call also touched on job searching (Alex Wilson on severance looking for AI-adjacent roles), with community members offering referrals and networking leads. Brandon closed by encouraging members to simplify their tech stacks, use Supabase over raw Google Cloud for early-stage apps, and check out ShipKit when it launches in approximately 25 days.

## insights

- **N8N as a rapid prototyping and client-facing tool**: Marc noted that foundational knowledge from lower-level frameworks (LangChain, CrewAI) makes visual tools like N8N dramatically easier to use and extend. Brandon reinforced that N8N can become the "glue" of a business in just a few hours of setup.
- **Best practice for webhooks is to send IDs, not blobs**: Brandon advised that instead of sending large JSON payloads via webhook, send only identifiers (job ID, user ID) and reconstruct the full data object inside the receiving service, avoiding payload size limits.
- **Supabase's "unrestricted database" warning is a false alarm when using Drizzle**: The warning applies only when using the Supabase client directly in the browser. If all queries go through Drizzle via structured API endpoints, the warning is irrelevant and can be ignored.
- **Supabase pre-signed URLs require authorization checks before generation**: When serving blobs, validate that the requesting user is authorized before generating a pre-signed URL — the URL itself is the access grant.
- **For early-stage apps, avoid raw Google Cloud Platform**: Brandon repeatedly recommended Supabase (auth + database + blob storage), Neon (database), Clerk or WorkOS (auth), and Vercel (hosting) over GCP/Firebase for solo developers, citing simplicity and cost.
- **OAuth callback loops are usually a middleware problem**: When Google/GitHub OAuth redirects back and nothing happens, the likely cause is that middleware is not consuming the token and session information returned in the redirect header. Supabase's built-in middleware handles this automatically.
- **Next.js + Vercel is strongly preferred over React + Flask for public-facing apps**: Server-side rendering in Next.js allows Google to crawl static pages, improving SEO. Pure React apps render everything via JavaScript, making them invisible to crawlers.
- **WorkOS is the recommended enterprise auth option**: For apps needing SAML, SSO, and organization management, Brandon recommended WorkOS over Clerk, noting it is more enterprise-grade though more expensive.
- **ADK agents can be embedded directly inside a Django or FastAPI app**: Rather than deploying ADK as a separate microservice, running it in-process eliminates deployment complexity and lets you call `root_agent.run()` directly, with session state carrying user context.
- **Use a `ref` folder with cloned example projects as AI coding context**: Brandon's cheat code — clone reference projects into a `ref/` folder and tell the AI "I want to steal this pattern from project X and this from project Y, help me combine them."
- **Generate-critique agent pattern improves output quality**: Brandon advocated for a loop where agent one generates output, a second agent critiques it, and the cycle repeats — useful for extracting implicit requirements from stakeholders like cybersecurity teams.
- **Corporate vibe coding requires developer-built guardrails before business users touch tools**: Patrick's situation illustrated that giving business users tools like Lovable without pre-built spec files, instruction templates, and approved tech stacks leads to uncontrolled tech sprawl.
- **LiveKit is a strong choice for production voice assistants**: Brandon walked back his earlier ADK voice tutorial recommendation, suggesting LiveKit instead for voice agents that need to integrate with phones and external systems, noting ADK voice + function calls gets "really weird."
- **GDPR compliance for MCP tools comes down to data storage and deletion rights**: An MCP is just a wrapped function call; the compliance question is what data is logged, stored, and whether users can request deletion within the required timeframe.

## qa

**Q (Marc Juretus):** Once N8N is deployed on Railway, what charges are associated with it?
**A (Paul Miller):** Paul runs N8N on DigitalOcean for a flat $20/month. N8N doesn't need much RAM or disk; the main consideration is whether you want to run a Postgres instance alongside it.

**Q (Mitch):** Is there a general guideline for how much data I can send via a webhook to Supabase?
**A (Brandon Hancock):** Best practice is to send only IDs (job ID, user ID) and reconstruct the full data object inside the backend job. REST protocols can handle hundreds of kilobytes; Next.js/Vercel has a 1–4 MB default limit. Moving the data-assembly logic into the background job means you're sending ~30 characters and the size limit becomes irrelevant.

**Q (Mitch):** Supabase keeps warning me that my database is unrestricted. Should I be worried?
**A (Brandon Hancock):** No. That warning applies when you expose the Supabase client directly to users, allowing them to write arbitrary queries. Since Mitch uses Drizzle through structured API endpoints, users never touch the Supabase client and the warning doesn't apply. Brandon wished there was a button to suppress it.

**Q (Paul Miller):** Will ShipKit provide Python path frontends, not just TypeScript/Next.js?
**A (Brandon Hancock):** ShipKit will stay Next.js-focused because it is the dominant standard for new real-world applications in 2025 and AI models have extensive training data on it. Brandon plans a dedicated TypeScript course and a vanilla Next.js course post-launch (likely October), but recommends making the jump to Next.js since AI handles much of the TypeScript complexity.

**Q (Juan Torres):** I need to create an API/URL connection so external applications can make inference calls to an LLM hosted on-premises. Any guidance?
**A (Brandon Hancock):** Set up a secure proxy that receives external requests, validates an API key in the header, and forwards authenticated requests to the private network. Once the user is authenticated into the application, generalize LLM access rather than issuing per-user API keys.

**Q (Patrick Chouinard):** How do you integrate vibe coding in a corporate environment where business users want a Lovable-style experience but cybersecurity wants control?
**A (Brandon Hancock / Paul Miller):** Brandon suggested using a generate-critique agent loop to extract cybersecurity requirements into prompts, and referenced the US DoD's Platform One / Big Bang CICD pipeline as a model (six approved templates, automated compliance checks). Paul recommended a Dragon's Den / Shark Tank facilitation process: get business users to pitch ideas, filter by ROI criteria, assign BAs to hone requirements, then build the guardrail framework only for the shortlisted use cases rather than the whole stack.

**Q (Ola Oyo):** How do I get ADK to work inside Django and be context-aware of the logged-in user?
**A (Brandon Hancock):** Set initial session state (user ID, name, etc.) when creating the ADK session. Then call `root_agent.run()` directly inside Django — no separate deployment needed. For the Vertex AI authentication issue, set `VERTEX=false` in environment variables and use a Google AI Studio API key instead; if organizational policy blocks it, create a personal GCP account and add $5 in billing.

**Q (Prem):** Should I use Clerk or Supabase Auth for user management, especially given I need organization-level features?
**A (Brandon Hancock):** Clerk is fine and integrates with Supabase. However, Brandon strongly recommended evaluating WorkOS before committing — it has enterprise SSO, SAML, and organization management already built in, and is better suited if the app needs to support large enterprise clients bringing their own identity providers.

**Q (Jake Maymar):** Where should I host a Next.js app if I'm moving off WordPress and SiteGround?
**A (Brandon Hancock):** Vercel. Point it at your GitHub repo and it deploys automatically, handles server-side rendering, and distributes the app properly. The hobby tier is free. Add your custom domain through Vercel's domain settings and update DNS records at your registrar (e.g., Namecheap). For email, use Google Workspace (~$7–8/month) and Mailgun for transactional emails.

**Q (Jake Maymar):** How do I scrape LinkedIn public profile data in a GDPR-compliant way?
**A (Brandon Hancock):** The LinkedIn API is very restrictive for accessing other users' data. Apify was discussed as a potential option. Brandon suggested running a ChatGPT deep research query specifically on GDPR compliance for scraping public LinkedIn data to get a definitive answer before committing to a tool.

**Q (Hemal Shah):** Is there a standard JSON model for chat request/response between a UI and a FastAPI backend when using ADK?
**A (Brandon Hancock):** The two most common patterns are Server-Sent Events (SSE) for streaming — returning chunks with `content` and `author` fields — and a plain JSON object with the same fields for non-streaming. ADK's own source code is a good reference; clone it as a `ref` project and ask the AI to replicate the pattern in your app.

**Q (Hemal Shah):** What voice assistant tooling would you recommend for a customer support agent that integrates with ERP/CRM systems?
**A (Brandon Hancock):** LiveKit — it provides a pre-built library, supports phone integration, and allows custom agent code. Brandon walked back his earlier ADK voice tutorial recommendation, noting that ADK voice combined with function calls becomes problematic. Bland.ai was mentioned as a no-code alternative.

## tools

- **N8N** — Visual workflow automation tool; members used it for webhook-triggered Google Drive/email automations and deployed it on Railway and DigitalOcean.
- **Railway** — Cloud hosting platform; Marc deployed his N8N instance here with minimal configuration.
- **DigitalOcean** — Cloud hosting; Paul runs N8N here for a flat $20/month.
- **Supabase** — Database, auth, and blob storage platform; extensively discussed for security model, RLS warnings, pre-signed URLs, and OAuth provider setup.
- **Drizzle ORM** — Used by Mitch, Tom, and Prem to make structured queries to Supabase, bypassing RLS concerns.
- **Vercel** — Hosting for Next.js apps; recommended for automatic SSR optimization, easy domain setup, and free hobby tier.
- **Clerk** — Authentication and user management; discussed for organization-level features and Supabase integration.
- **WorkOS** — Enterprise auth platform with SAML/SSO and organization management; recommended for enterprise-grade apps.
- **Neon** — Postgres database with a generous free tier; mentioned as a Supabase alternative.
- **Google ADK (Agent Development Kit)** — Google's agentic framework; multiple members building with it, discussed embedding in Django/FastAPI.
- **Vertex AI** — Google Cloud's managed AI platform; Ola had authentication issues using it locally in Docker.
- **Google AI Studio** — Used to generate Gemini API keys as an alternative to Vertex AI authentication.
- **Tailscale** — VPN service; Juan downloaded binaries directly to a shared server's persistent filesystem to establish a secure connection without admin permissions.
- **LangChain / LangGraph** — Agentic frameworks; discussed as most in-demand in enterprise job postings; Brandon noted LangChain will be added to ShipKit.
- **Lovable** — No-code/low-code vibe coding tool for business users; central to Patrick's corporate integration challenge.
- **Cursor** — AI-assisted IDE; discussed in context of corporate vibe coding and Brandon's experience when it broke temporarily.
- **ShipKit** — Brandon's prompt-driven course and boilerplate product under development; includes templates for RAG, chat, and ADK agent apps.
- **Limitless.ai (Limitless device)** — Wearable/app that records meetings; Paul uses it to capture phone calls and coffee meetings for follow-up automation.
- **LiveKit** — Voice agent platform supporting phone integration and custom agent code; recommended over ADK voice for production voice assistants.
- **Bland.ai** — No-code voice agent tool; mentioned as an alternative to LiveKit.
- **Apify** — Web scraping platform; discussed for LinkedIn public profile scraping with GDPR considerations.
- **Mailgun** — Transactional email service; recommended for automated emails from Next.js apps.
- **Firebase** — Google's BaaS; cited as the source of major data leak incidents due to unrestricted client access patterns.
- **Platform One / Big Bang** — US DoD CICD pipeline framework; Brandon referenced it as a model for corporate vibe coding governance.
- **Upload Thing** — Blob storage option mentioned as an alternative to Supabase storage.
- **Topic Launch (topiclaunch.com)** — Jaylen's platform for fans to crowdfund YouTube video topics; demoed on the call.
- **ChatGPT (agent mode)** — Used by one member for automated user journey testing of their SaaS application.
- **Gemini Live** — Google's streaming voice library; recommended over ADK voice for voice assistant use cases.
- **Base44** — Mentioned as a direct competitor to one member's SaaS factory concept.

## links

- **Platform One / Big Bang (DoD CICD framework)** — Brandon dropped a link in chat; public documentation on the US Air Force's approved pipeline templates for developer-built applications.
- **Supabase Next.js tutorial playlist** — Brandon shared a YouTube playlist walking through Next.js + Supabase integration, noting video three covers the authentication setup step.
- **Google ADK browser agent example (YouTube + GitHub repo)** — Brandon shared a Google-produced example demonstrating multi-phase orchestrator prompts with routing between agents; shared in chat as a reference for Hemal's routing workflow.
- **topiclaunch.com** — Jaylen's live platform for crowdfunding YouTube content ideas.
- **shipkit.ai** — Brandon's ShipKit product landing page, referenced for Jaylen and others to check out.

## decisions

- **Brandon** will check with his wife (a consultant at UHY) about potential job openings for Alex Wilson after the call.
- **Lewis (Never2Nervous)** will get Alex Wilson's resume in front of a human contact at his Big Four consulting firm.
- **Adam** will send Brandon a pull request updating deprecated Gemini preview model references in the ADK tutorial repository (already submitted).
- **Brandon** will send members an updated round of ShipKit prep template prompts (including a roadmap-generation prompt) via email within the next day or so.
- **Brandon** will release ShipKit approximately 25 days from the call date, with LangChain templates and a desktop app course planned as post-launch additions.
- **Ola** will try embedding ADK directly inside Django (rather than as a separate service) and will report back next week.
- **Juan** will create a wireframe or diagram of his GPU inference infrastructure setup and potentially record a YouTube video stress-testing the LLM on an A100, seeking GPU credits from the server provider.
- **Hemal** will use the Google ADK browser agent example repository as a reference for implementing multi-phase orchestrator routing in his chatbot.
- **Jaylen** will consider pivoting Topic Launch toward a subscription model (creator pays ~$30/month for community thumbs-up/thumbs-down on topic ideas) based on Brandon's feedback.
- **Tom** will demo the updated multi-tenant version of his asset management app on a future call once he resumes coding after moving house.