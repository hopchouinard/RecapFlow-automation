## general

This was a weekly group coaching call hosted by Brandon Hancock, conducted in a round-robin format where each participant shared project updates or asked for help. The session covered a wide range of AI development topics including agent frameworks, no-code tools, video/audio generation pipelines, and SaaS product development.

Brandon opened by introducing the format and then worked through each participant's update. Topics ranged from connecting agents to the ClinicalTrials.gov API using Google's Agent Development Kit (ADK), to building a real estate subdivision cost calculator in Lovable, to creating AI-generated video ads and audiobooks, to building a WhatsApp message mediation app. Brandon also previewed an upcoming ADK crash course he was finishing.

A recurring theme throughout the call was enthusiasm for ADK as a framework for building agentic applications, with Brandon repeatedly highlighting its affordability, built-in state management, and flexible workflow agent types (sequential, loop, parallel). Comparisons were drawn to Crew AI, LangChain, and other frameworks. Tool discussions also touched on Cursor vs. Windsurf vs. Roo Code for AI-assisted coding, and PostHog for product analytics.

The call ended with Brandon previewing upcoming content: an ADK masterclass and a series of real-world agent example tutorials focused on practical business automation use cases.

## insights

- **ADK (Agent Development Kit) pricing is dramatically cheaper than alternatives**: Brandon noted it costs ~$0.11/hour per agent at runtime, versus Crew AI's session-based ~$40-50/month for 3-5 agents — Google is subsidizing costs because their revenue comes from YouTube/Search, not agents.
- **Loop agents + exit loops in ADK allow research agents to iterate until a condition is met** (e.g., "stop when 5 results are found"), rather than being limited to single-shot tool calls.
- **ADK's built-in state management is a significant advantage**: state can be updated before/after agent calls, by the agent itself, or by tools — removing the need to build custom state management.
- **For long-context prompts (e.g., GPT-4.1 at 1M tokens), repeat critical instructions at both the beginning and end** of the prompt for best instruction-following results — per OpenAI's own prompt guide.
- **GPT-4.1's biggest improvement is instruction following**: it reliably respects explicit constraints like "do not do X," which previous models often ignored.
- **When building V1 agentic systems, keep everything in one repository** and only introduce MCP for tool-sharing once you have multiple separate repositories that need shared tools.
- **For MVP testing with expert/professional users, pre-seed their accounts with data** so testers evaluate the core product loop, not the onboarding experience.
- **A simple thumbs-up/thumbs-down feedback mechanism on generated outputs** (images, clips) is the fastest path to building few-shot training data for improving generative pipelines — Jake Maymar.
- **Using a low-stability setting on a custom ElevenLabs voice creates an animated, attention-grabbing ad voiceover** — Richard Collier's pattern-interrupt technique for Facebook ads.
- **Breaking a large LLM prompt into a router call + specialist call** (classification first, then response generation) keeps prompts manageable and allows each sub-prompt to be highly optimized.
- **Deploying Next.js AI apps to Vercel early** is important because local apps can run indefinitely while Vercel has timeouts and stateless constraints that can break AI applications.
- **Forming teams of individual LLCs to pitch larger clients** allows freelancers to access bigger budgets than any single individual could command — Jake Maymar's business model insight.
- **PostHog provides funnel analytics and session replay at near-zero cost**, enabling product teams to understand user behavior, identify power users skewing data, and predict churn.

## qa

**Q (AbdulShakur):** I'm building an agent to query the ClinicalTrials API using ADK. I was stuck getting the agent to write API calls directly, so I switched to having a Python program make the calls and the agent just prompts it. Is there a better approach?
**A (Brandon):** Look into loop agents and exit loops in ADK. A loop agent can pair a planner agent with a research agent that iterates continuously until a condition is met (e.g., 5 results found). You'd use `toolcontext.state` to track results and call `exit_loop` when criteria are satisfied. The three ADK patterns to study are sequential agents, stateful agents, and loop agents.

**Q (Jake):** Is everyone still using Cursor? Are there open-source models that work well for coding?
**A (AbdulShakur/Brandon):** AbdulShakur mentioned Roo Code with Qwen3 via OpenRouter as a potentially cheap option, though he hadn't gotten it working personally. Brandon said he's addicted to Cursor at $20/month for 500 premium calls, and considers it industry standard. Windsurf has declined in quality for some users. Roo Code is more capable but expensive unless using open-source models.

**Q (Sam):** Has anyone tested GPT-4.1 models, particularly their claimed 1M context window?
**A (Brandon):** The biggest improvement in 4.1 is instruction following — it reliably respects explicit constraints. For long-context use, OpenAI's own prompt guide recommends repeating important instructions at both the beginning and end of the prompt. Brandon hasn't tested the full 1M token limit yet.

**Q (Sam):** Can you use your own Azure API key inside Cursor to avoid rate limits while keeping data in a private Azure network?
**A (Brandon/Bastian):** Yes, Cursor has a model settings page where you can add an Azure API key and deployment info. However, Bastian noted that when using your own API key, Cursor limits the agent feature (the iterative agentic mode) — you can still use the "ask" mode to generate code, just without autonomous iteration.

**Q (Sagar):** For agentic teams in enterprise settings, how do you handle orchestration — choosing between parallel, sequential, or prompt-chaining flows dynamically?
**A (Brandon):** In ADK, you create a root agent that delegates to sub-agents. Each agent has a description, and the root agent automatically selects the best sub-agent for each task. You define workflow types (sequential, loop, parallel) as predetermined patterns; the root agent routes dynamically to them. This isn't real-time selection of workflow type — it's structured delegation to pre-built workflow agents.

**Q (Sagar):** Is MCP the right standard for connecting agents to services like SharePoint?
**A (Brandon):** For V1, no — direct tool calls are simpler and sufficient. MCP becomes valuable when you have multiple separate agent repositories that need to share tools. Build it in one repo first; introduce MCP when you need cross-repository tool sharing.

**Q (Andrew):** Is there a tool that lets testers blur sensitive data regions in screen recordings before sending them?
**A (Brandon):** Screen Studio (Mac only) has a "mask/sensitive data" feature where you can draw a block over a region and set it on a timeline so it appears only during specific timestamps. It's all local until you export, unlike Loom which uploads immediately.

**Q (Michael):** My single LLM prompt is getting too large as I add classification and response logic. How should I restructure it?
**A (Brandon):** Split it into two LLM calls: a router that only classifies the message type (pass, rephrase, comment, block), and then a specialist prompt for each type that handles the response. Each sub-prompt stays small and can be deeply optimized for its specific task.

## tools

- **Google ADK (Agent Development Kit)** — Primary framework discussed; highlighted for loop agents, sequential agents, parallel agents, built-in state, and cheap deployment pricing (~$0.11/hr).
- **Crew AI / Crew AI Enterprise** — Compared to ADK; Enterprise noted for permissions, tracing, and on-premise/factory installations for large clients.
- **Lovable** — No-code app builder used by Paul to build a real estate subdivision cost calculator in ~2.5 hours of actual build time.
- **Cursor** — AI coding IDE; Brandon's preferred tool at $20/month; discussed as industry standard.
- **Windsurf** — AI coding IDE; some users noted quality decline after recent updates.
- **Roo Code** — VS Code plugin for AI coding; more capable than Cline but expensive unless paired with open-source models via OpenRouter.
- **Cline (Klein)** — VS Code AI coding plugin; noted for handling complex ESLint errors well when used with Claude.
- **Claude Desktop** — Used for MCP server connections and as a standalone coding/analysis assistant.
- **N8N** — Workflow automation platform; Jake mentioned heavy use in upcoming client projects.
- **PostHog** — Product analytics tool recommended for funnel analysis, session replay, and user behavior tracking; described as very cheap.
- **ElevenLabs** — TTS platform used by Richard for ad voiceovers with custom voice and low stability settings; also generates sound effects via API.
- **OpenAI TTS (text-to-speech model)** — Used by Richard for multi-character audiobook generation with per-character voice instructions.
- **Flux** — Image generation model used by Richard for cartoon-style ad visuals; noted as affordable.
- **FFmpeg** — Used by Richard for audio stitching in the audiobook pipeline.
- **Gemini / AI Studio (aistudio.google.com)** — Suggested for video analysis to generate time-stamped sound effect placement lists using structured output.
- **Vercel AI SDK** — Recommended for making LLM calls inside Next.js applications; the "approved" approach for deployment.
- **Vercel** — Deployment platform; Brandon warned about timeout and stateless constraints affecting AI apps.
- **Supabase** — Mentioned by Paul as planned backend for auth and user tracking in his Lovable app.
- **Twilio** — Michael's planned SMS/WhatsApp integration for his message mediation app.
- **Loom** — Screen recording tool; discussed for user testing documentation and AI-assisted transcription workflows.
- **Screen Studio** — Mac screen recording app with local sensitive-data masking feature; recommended for testers handling protected information.
- **GitHub Copilot** — Sam's current tool; using "bring your own model" feature pointed at company Azure resources due to data security requirements.
- **OpenRouter** — Mentioned as a way to use Qwen3 with Roo Code to reduce costs.

## links

- **Brandon's ADK examples repository** — Shared in chat; contains 11 examples from basic to workflow agents (sequential, stateful, loop): dropped during AbdulShakur's segment.
- **OpenAI GPT-4.1 prompt guide** — Resource Andrew surfaced the previous week; includes recommendation to repeat instructions at beginning and end for long-context prompts.
- **ADK workflow agents documentation** — `google.github.io/adk` agents section covering sequential, loop, and parallel agent types; Brandon shared during Sagar's segment.
- **ADK FastAPI / UI integration tutorial** — ADK docs page showing how to wrap agents as an API with a chat frontend; Brandon dropped link for Bastian's question.
- **MCP crash course video (Dave/Albert)** — ~1 hour Python-focused MCP tutorial Brandon referenced as one of the best available; dropped in chat the previous week.
- **"AI Guy" YouTube channel** — Faceless AI YouTube channel focused on making money; Brandon shared as inspiration for Richard's video content business.
- **Second AI video/image tutorial YouTube channel** — Broader tutorial channel covering image and video AI tools; shared alongside "AI Guy" for Richard.
- **PostHog website** — `posthog.com`; shared by Brandon during Paul's segment as analytics recommendation.

## decisions

- **AbdulShakur** will explore ADK loop agents, sequential agents, and stateful agents from Brandon's shared repository to improve his ClinicalTrials API agent.
- **AbdulShakur** will send Brandon DMs with progress updates on the ADK project.
- **Jake** will share details on his business model (team-of-LLCs pitch structure) and project specifics with the group once contracts are signed.
- **Jake** will investigate using Cursor with an Azure API key as a cost-effective alternative to his current GitHub Copilot setup.
- **Paul** will connect his Lovable app to Supabase for authentication and user management.
- **Paul** will implement PostHog (or similar analytics) to track user behavior and feature adoption in his subdivision cost calculator.
- **Paul** will post about his Lovable build on Twitter/X.
- **Sagar** will attend an AWS event the following day and report back to the group with any relevant findings.
- **Sagar** will follow up with Brandon on a separate call to discuss specific client requirements and get a more tailored framework recommendation (ADK vs. Crew AI Enterprise).
- **Richard** will test using Gemini via AI Studio to analyze his generated videos and produce time-stamped sound effect placement lists using structured output.
- **Richard** will explore implementing a thumbs-up/thumbs-down feedback system (potentially with Supabase) to improve image and clip generation quality over time.
- **Andrew** will use Screen Studio's sensitive-data masking feature for testers handling protected information, and may purchase copies for Mac-using testers.
- **Andrew** will pre-seed tester accounts with data to reduce onboarding friction during the initial testing phase.
- **Michael** will refactor his LLM prompt into a two-call architecture: a router for classification and specialist prompts for each response type.
- **Michael** will do a deployment test to Vercel before adding more features, to catch timeout/stateless issues early.
- **Michael** will investigate the Vercel AI SDK for making LLM calls in his Next.js application.
- **Brandon** will begin recording the ADK crash course on Wednesday/Thursday, targeting a Friday or Saturday release.
- **Brandon** will shift content focus after the crash course toward real-world business automation example tutorials using ADK and other tools.