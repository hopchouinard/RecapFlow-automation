📝 SUMMARY

This coaching call covered a wide spectrum of agentic AI projects, from clinical trial search engines and infrastructure cost calculators to automated video ad generation and voice-based audiobook production. The session heavily featured architectural discussions around Google's Agent Development Kit (ADK) for enterprise and startup deployments, rapid prototyping strategies using no-code tools like Lovable, and practical solutions for data security and analytics in AI applications. Members shared progress on client work, discussed tooling preferences for AI-assisted development, and troubleshooted specific implementation challenges ranging from Next.js deployments to sensitive data handling in screen recordings.

💡 KEY INSIGHTS

AbdulShakur Abdullah shifted his clinical trials API agent architecture from having the agent write direct API calls to using a Python program for the calls while the agent handles natural language prompting and parameter extraction, simplifying the implementation significantly.

Brandon Hancock emphasized that ADK's Loop Agents with customizable exit_loop criteria are ideal for research tasks that require iterative tool calling until sufficient data is gathered, rather than single-shot attempts.

Jake Maymar explained his strategy for winning larger enterprise contracts by forming temporary teams from individual LLCs and S-corps, allowing them to pitch as a company rather than individuals and access bigger budgets.

Paul Miller demonstrated converting a complex client spreadsheet into a functional web application using Lovable in approximately 2.5 hours of actual build time, using Claude to analyze the spreadsheet logic first and generate the initial prompt.

Brandon noted that ADK costs approximately $0.11 per hour of runtime, making it significantly more cost-effective than alternatives for deployed agents, while Crew AI Enterprise remains preferable for clients requiring on-premise installations and strict governance controls.

Richard Collier shared his "60% automation" philosophy for video generation, where AI handles scriptwriting, image generation via Flux, and initial video assembly, leaving manual work for sound effects, music, and final polish to ensure quality.

Michal Simko implemented a message mediation system that classifies inputs (pass, rephrase, block, comment) but Brandon suggested splitting this into two distinct LLM calls: a router for classification and a specialist agent for response generation, preventing prompt bloat.

❓ KEY Q&A

AbdulShakur asked how to handle iterative research where the agent should stop when no new trials are found rather than at a max iteration. Brandon explained that ADK supports exit_loop functions that check state (such as number of resources found) and can trigger escalation to stop the loop dynamically.

Jake asked about current recommendations for AI coding tools given his struggles with Next.js TypeScript progress bars. Brandon recommended Cursor ($20/month) for its agent capabilities, while AbdulShakur mentioned experimenting with RueCode via OpenRouter using Qwen3, and Jake noted Klein's effectiveness with ESLint errors.

Sam asked about securely using AI coding tools within enterprise environments with strict data governance. Brandon suggested testing Cursor with a private Azure OpenAI API key and deployment configuration, though Bastian Venegas noted this may limit agent functionality to "ask" mode rather than full agent iteration.

Sagar asked how to architect agentic teams for financial services operations with dynamic workflow selection. Brandon recommended ADK's workflow agents (sequential, loop, parallel) orchestrated by a root agent that delegates to sub-agents based on task type, noting this provides better dynamic routing than static sequential flows.

Paul asked how to track client usage and measure success of his infrastructure calculator tool. Brandon recommended PostHog for product analytics, funnel tracking, and session replay to understand user behavior without building custom analytics.

Andrew asked for tools to record screen demos while protecting sensitive client information. Brandon recommended Screen Studio for Mac, which allows users to add masks over sensitive data before export, keeping everything local until the final video is ready.

Michal asked how to structure prompts for his message mediator as he adds more scenarios. Brandon advised refactoring into a two-stage process: first a router LLM classifies the intent, then a second specialist LLM handles the specific response type, keeping each prompt focused and manageable.

🛠️ TOOLS AND CONCEPTS MENTIONED

ADK (Agent Development Kit): Google's open-source framework featuring sequential agents, loop agents, parallel agents, and exit_loop functionality for complex workflow orchestration.

MCP (Model Context Protocol): Protocol for sharing tools across different agent repositories, most valuable when multiple departments need to share code; Brandon recommended direct tool calls for V1 implementations instead.

Lovable: No-code application builder used by Paul to rapidly prototype a financial calculator from spreadsheet logic.

PostHog: Analytics platform recommended for tracking user funnels, session replays, and product analytics in AI applications.

Screen Studio: Mac-based screen recording software with sensitive data masking capabilities for secure client demonstrations.

Cursor/Windsurf/RueCode/Klein: AI coding assistants discussed for different use cases; Cursor favored for agent capabilities, RueCode noted as expensive but capable, Klein praised for ESLint handling.

Flux: Image generation model used by Richard for creating cartoon-style video assets.

11 Labs: Voice generation service used for custom animated voices in advertising and character voices in audiobooks.

N8N: Workflow automation platform mentioned by Jake for enterprise implementations.

Vercel AI SDK: Recommended library for Next.js applications making LLM calls, particularly important for handling stateless cloud deployments and timeouts.

Join Keys: Database concept for creating conversation identifiers by concatenating user IDs, suggested for Michal's messaging app pairing system.

📎 SHARED RESOURCES

https://github.com/google/adk-samples (Brandon's ADK examples repository containing 11 examples from basic implementations to complex workflows including sequential, stateful, and loop agents)

https://platform.openai.com/docs/guides/prompt-engineering (OpenAI's official prompt engineering guide, specifically noted for its recommendation to place critical instructions at both beginning and end of long context windows)

https://posthog.com (Product analytics platform recommended for tracking user behavior and feature adoption)

https://screenstudio.com (Screen recording software with privacy masking features for sensitive data)

https://sdk.vercel.ai/docs (Vercel AI SDK documentation for building AI applications in Next.js)

🔄 FOLLOW-UPS WORTH EXPLORING

AbdulShakur to implement ADK loop agents with exit_loop criteria based on resource count or data saturation for the clinical trial search functionality, moving away from max-iteration limits.

Jake to share detailed case study once contracts are signed, covering client acquisition methods, LLC teaming structure results, and technical architecture of the won projects.

Sagar to report back findings from the upcoming AWS event regarding enterprise agent implementations and any relevant announcements for the group's financial services use cases.

Richard to explore reinforcement learning feedback loops (thumbs up/down) for his video generation pipeline and test Gemini's ability to analyze video content and suggest sound effect timing automatically.

Michal to deploy his messaging application to Vercel immediately to identify potential timeout issues in a stateless environment before the codebase grows larger, and to implement join keys for conversation pairing logic.

Brandon to release the ADK Masterclass crash course featuring simplified V3 examples covering sequential, stateful, and loop agent patterns.