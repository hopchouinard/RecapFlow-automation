## general

This was a group coaching call hosted by Brandon Hancock, structured as a round-robin update session with questions addressed first. The call opened with pre-session discussion among Marc Juretus, Paul Miller, and Patrick Chouinard about N8N, Railway deployments, and the challenge of integrating vibe coding practices into corporate environments. Brandon then addressed submitted questions before moving through individual participant updates.

Brandon shared progress on his upcoming ShipKit course, describing a prompt-driven approach to app development that includes templates for RAG, chat, and ADK agent patterns. The session covered a wide range of technical topics including N8N automation workflows, Supabase security, ADK (Agent Development Kit) integration with Django and FastAPI, webhook data limits, authentication issues, and hosting options for Next.js applications. Several participants shared project updates ranging from GPU stress-testing infrastructure to a YouTube content funding platform to an asset management SaaS.

The call also touched on career topics, with one participant (Alex Wilson) actively job searching and receiving leads from other community members. Brandon was candid about the financial stress of freelancing and course creation, contrasting it with the stability of employment. The session ran approximately two hours.

## insights

- **N8N as a rapid prototyping tool**: Prior framework knowledge (LangChain, CrewAI) makes low-code tools like N8N significantly easier to use and extend; the combination allows quick client-ready prototypes without writing libraries from scratch.
- **Webhook best practice**: Send only IDs through webhooks rather than large JSON blobs; move the data-assembly logic into the first step of the background job to avoid payload size limits.
- **Supabase RLS warnings are often irrelevant**: If you're using Drizzle ORM through structured API endpoints, the "unrestricted database" warning from Supabase does not apply — it only matters when using the Supabase client directly in the browser.
- **Vibe coding in enterprise requires guardrails first**: Giving business users tools like Lovable without developer-built templates, instruction files, and approved tech stacks will result in a thousand incompatible tech stacks. Developers must build the supervised environment before non-technical users can safely vibe code.
- **Generate-critique agent pattern**: Running an agent to generate output and immediately following with a critique agent, cycling several times, is an effective way to surface and satisfy stakeholder requirements (e.g., cybersecurity specs) without lengthy requirement-gathering sessions.
- **Platform One / Big Bang (US DoD)**: The government solved the "every developer doing different things" problem by certifying a small number of CI/CD pipeline templates and requiring all apps to pass through them — a model applicable to large corporate environments.
- **ADK inside Django vs. as a separate service**: Embedding ADK directly in a Django application avoids the need to recreate ORM models and handle cross-service authentication; once a session is created, calling `root_agent.run` is all that's needed.
- **Supabase pre-signed URLs for blob security**: Before generating a pre-signed URL for a blob, verify the requesting user is authorized — this is the key security check when using Supabase storage.
- **Next.js + Vercel for SEO**: Plain React apps render everything through JavaScript, making pages invisible to crawlers; Next.js with Vercel serves static pages properly, which is critical for any externally-facing marketing site.
- **WorkOS for enterprise auth**: For applications needing organization-level SSO and SAML, WorkOS is a strong recommendation over Clerk or raw Supabase auth.
- **LiveKit for voice agents**: Preferred over ADK's voice module for production voice assistants because function calls inside ADK voice get unwieldy; LiveKit supports phone integration and custom agents.
- **ADK orchestrator phase pattern**: Structuring the orchestrator prompt with explicit phases (e.g., "Phase 1: gather information, route to agents A/B/C; Phase 2: execute, route to agents D/E") is the recommended way to implement conditional routing in multi-agent ADK workflows.
- **Freelancing financial reality**: Brandon noted candidly that freelancing/course creation is more stressful than employment — income uncertainty is real and underreported in developer communities.

## qa

**Q (Marc Juretus):** Once N8N is deployed on Railway, what charges are associated with it?
**A (Paul Miller):** Paul runs his on DigitalOcean for a flat $20/month. N8N doesn't need much RAM or disk; the main consideration is whether you want a co-located Postgres instance.

**Q (Mitch):** Is there a general guideline for how much data can be sent via a webhook, specifically with Supabase?
**A (Brandon Hancock):** Best practice is to send only IDs and move the data-assembly logic into the background job. REST can handle hundreds of kilobytes; Next.js/Vercel has a 1–4 MB default limit. Supabase may have its own limit, but sending IDs sidesteps the issue entirely.

**Q (Mitch):** Supabase keeps warning me that my database is unrestricted. Should I be worried?
**A (Brandon Hancock):** No — that warning applies when you expose the Supabase client directly to users, allowing arbitrary queries. Since you're using Drizzle ORM through structured API endpoints, the warning is irrelevant. There's no way to turn the warning off, but you're safe.

**Q (Patrick Chouinard):** How do you integrate vibe coding in a corporate environment where business users want a Lovable-style experience but cybersecurity wants control?
**A (Brandon Hancock / Paul Miller):** Developers need to first build the guardrails — approved templates, instruction files, and CI/CD pipelines — before non-technical users can safely vibe code. The US DoD's Platform One / Big Bang approach (certifying a small set of pipeline templates) is a useful model. Paul suggested using business analysts and a "Shark Tank"-style pitch process to filter and focus ideas before any development begins.

**Q (Ola Oyo):** How do I make ADK context-aware of the specific user when embedding it in a Django application?
**A (Brandon Hancock):** When creating an ADK session, set initial state (user ID, name, etc.) at session creation time. Then pass that context in every message. Once the session exists, you just call `root_agent.run` — no separate deployment needed since it's embedded in Django.

**Q (Ola Oyo):** I'm getting policy errors trying to use Vertex AI or Google AI Studio API keys under a Google Workspace organization. What should I do?
**A (Brandon Hancock):** Set `VERTEX=false` in your environment variables and use a Google AI Studio API key directly. If organizational policies block it, create a personal Google Cloud account and add $5 in billing — it will last a very long time and bypasses workspace restrictions.

**Q (Prem):** Should I use Clerk or Supabase auth for user and organization management?
**A (Brandon Hancock):** If you specifically need organization-level management that Supabase doesn't yet offer, Clerk is reasonable. However, also evaluate WorkOS — it supports enterprise SSO, SAML, and organizations, and has received strong community feedback. Supabase does have a Clerk integration if you want both.

**Q (Jake Maymar):** How do I scrape LinkedIn public profile data in a GDPR-compliant way?
**A (Brandon Hancock):** The LinkedIn API becomes very restrictive when accessing other users' data. Apify is one option for scraping public data. For GDPR, the key questions are what data you store and whether users can request deletion. Brandon suggested running a ChatGPT deep research query on the specific compliance question.

**Q (Jake Maymar):** How do I make MCPs GDPR-compliant?
**A (Brandon Hancock):** Strip away the "MCP" framing — it's just a function call wrapped for agent access. The compliance question is really about what data the underlying function stores and whether logs can be deleted on request (a core GDPR requirement).

**Q (Never2Nervous / Lewis):** I've been stuck for three weeks on an OAuth routing issue with Google and GitHub login in my Next.js app using raw Google Cloud. What's wrong?
**A (Brandon Hancock):** The likely issue is that the OAuth response contains tokens and redirect instructions in the header/URL, but without proper middleware to consume them, nothing happens and you loop. Supabase includes pre-built middleware that handles this correctly. Recommendation: switch to Supabase auth, which makes Google/GitHub OAuth a matter of pasting credentials and setting redirect URLs.

**Q (Hemal Shah):** Is there a standard JSON structure for chat request/response between a UI and a FastAPI backend when building an AI chatbot?
**A (Brandon Hancock):** The two most common patterns are SSE (server-sent events) streaming small chunks with `content` and `author` fields, and plain JSON objects with the same fields. ADK's source code is a good reference for how to implement both. You can also use ADK's `serve API` command to auto-expose FastAPI endpoints around your agent.

**Q (Hemal Shah):** What's the best tool for a production voice assistant that integrates with ERP/CRM systems?
**A (Brandon Hancock):** LiveKit is the current recommendation — it supports custom agents, phone integration, and is developer-friendly. For Google-stack projects, use the Gemini Live library directly rather than ADK's voice module, as function calls inside ADK voice become unwieldy.

## tools

- **N8N** — Low-code automation platform; used for webhook-triggered workflows, Google Drive integrations, and email automation; deployed on Railway and DigitalOcean.
- **Railway** — Cloud hosting platform; used by Marc to deploy N8N and a LangChain/Next.js app with minimal configuration.
- **DigitalOcean** — Cloud hosting; Paul runs N8N on a $20/month droplet.
- **Supabase** — Backend-as-a-service; discussed extensively for database hosting, authentication (OAuth providers), blob storage, and row-level security.
- **Drizzle ORM** — TypeScript ORM used with Supabase; noted as making Supabase's RLS warnings irrelevant.
- **Next.js** — Full-stack React framework; recommended as the standard for all new web applications due to SSR, SEO benefits, and AI training data coverage.
- **Vercel** — Hosting platform for Next.js; recommended for its seamless deployment, custom domain support, and static page optimization.
- **Google ADK (Agent Development Kit)** — Google's agentic framework; discussed for Django integration, multi-agent orchestration, session management, and voice.
- **Gemini Live** — Google's real-time voice API; recommended over ADK's voice module for production voice assistants.
- **LiveKit** — Voice agent platform; recommended for production voice assistants with phone integration and custom agent support.
- **LangChain / LangGraph** — Agentic frameworks; noted as most in-demand in enterprise job postings; planned addition to ShipKit.
- **Tailscale** — VPN service; Juan used it to create a secure connection to a remote server without admin permissions.
- **Vertex AI** — Google Cloud ML platform; used by Juan for GPU/LLM inference testing; discussed for hosting models securely.
- **Clerk** — Authentication and user management service; discussed for organization-level user management features.
- **WorkOS** — Enterprise authentication platform; recommended for SAML, SSO, and organization management at scale.
- **Neon** — Serverless Postgres database; mentioned as a generous free-tier alternative to Vercel Postgres.
- **Mailgun** — Email delivery service; recommended for transactional emails in Next.js apps.
- **Apify** — Web scraping platform; discussed as an option for GDPR-compliant LinkedIn public profile scraping.
- **Limitless.ai** — Wearable/app that records meetings and calls; Paul uses it; Brandon noted Bastion is building N8N workflows around its API.
- **ShipKit** — Brandon's upcoming course/boilerplate product; prompt-driven app development with templates for RAG, chat, and ADK agents.
- **Bland** — No-code voice agent platform; mentioned as an alternative for voice assistants.
- **Platform One / Big Bang** — US DoD CI/CD pipeline framework; referenced as a model for enterprise vibe coding governance.
- **Lovable** — No-code/vibe coding tool for business users; referenced in the corporate vibe coding discussion.
- **Cursor** — AI-powered IDE; referenced in the context of corporate developer tooling and vibe coding.
- **ChatGPT** — Used by Adam's daughter for class scheduling optimization; also used by Never2Nervous for user journey testing.
- **Firebase** — Google's BaaS; cited as the source of major data leak incidents due to unrestricted client access patterns.
- **Elastic Beanstalk** — AWS deployment service; mentioned by Juan as a potential deployment target for his client's application.
- **Upload Thing** — Blob storage service; mentioned as an alternative to Supabase storage.
- **Topiclaunch.com** — Jaylen's platform for fans to fund YouTube video topics; demonstrated during the call.

## links

- **Platform One / Big Bang (US DoD)** — Brandon dropped a link in chat to the government's CI/CD pipeline framework presentation; public documentation available for non-DoD access.
- **Google ADK examples repository (Python)** — Brandon shared the ADK GitHub repository showing orchestrator phase patterns and browser agent examples.
- **ADK browser agent YouTube video** — Google's YouTube video demonstrating a browser agent with multi-phase orchestration prompts; shared as a reference for Hemal's routing question.
- **Next.js + Supabase tutorial playlist** — Brandon referenced a YouTube playlist (not his own) walking through Next.js with Supabase authentication as a resource for Never2Nervous.
- **LiveKit** — https://livekit.io — Voice agent platform recommended for production voice assistants.
- **Topiclaunch.com** — Jaylen Davis's live platform for fan-funded YouTube content.
- **ShipKit.ai** — Brandon's upcoming course/boilerplate product site.

## decisions

- **Brandon** will check with his wife (a consultant at UHY) about open developer positions that might suit Alex Wilson's background.
- **Brandon** will send an updated round of ShipKit prep template prompts to members via email within the next day or so, including a new roadmap-generation prompt.
- **Brandon** plans to add a LangChain/LangGraph template to ShipKit after launch.
- **Brandon** plans to create a TypeScript course, a Python course, and a vanilla Next.js course approximately in October, post-ShipKit launch.
- **Brandon** plans to create a desktop app course for ShipKit after the current launch.
- **Brandon** will review Adam's pull request fixing deprecated Gemini preview model references in the ADK tutorial repository.
- **Juan Torres** will create a YouTube video documenting the GPU stress-testing and LLM inference setup, potentially seeking GPU credits from server providers.
- **Juan Torres** will build a secure proxy/API bridge between the on-premise Oculus server (hosting the LLM) and the external-facing application deployment.
- **Ola Oyo** will try creating a personal Google Cloud account with $5 billing to bypass Google Workspace organizational policy restrictions on AI Studio API keys.
- **Ola Oyo** will embed ADK directly into the Django application rather than running it as a separate service.
- **Never2Nervous (Lewis)** will migrate authentication from raw Google Cloud OAuth to Supabase auth to resolve the persistent routing loop issue.
- **Adam** will use Next.js (rather than React + Flask) for the fractional business development agency website to gain SSR and SEO benefits.
- **Jaylen Davis** will explore adding a subscription-based community voting/thumbs-up feature to Topiclaunch as an alternative or complement to the current funding model.
- **Alex Wilson and Never2Nervous (Lewis)** will connect via the community platform so Lewis can refer Alex's resume to his Big Four consulting firm.
- **Hemal Shah** will use the ADK browser agent repository as a reference for implementing phase-based conditional routing in his multi-agent workflow.
- **Hemal Shah** will investigate LiveKit as the voice assistant platform for his customer support use case.