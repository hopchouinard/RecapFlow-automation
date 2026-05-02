📝 SUMMARY

This coaching call centered on advanced implementations of AI coding workflows, with Patrick sharing an enterprise-scale documentation automation system built using Shipkit templates that generated 20,000 lines of documentation across 12 subprojects. Brandon introduced OpenAI's new Agent Kit from Dev Day, comparing it favorably to N8N for deployment ease but noting limitations in multi-agent orchestration. Members discussed cost optimization strategies for AI development tools, deployment solutions for Google ADK on Cloud Run, and the business implications of rapid AI-assisted development for both new consultants and established SaaS companies.

💡 KEY INSIGHTS

Patrick detailed an automated workflow using Shipkit templates that creates Jira tickets, GitHub branches, documentation, and pull requests automatically, processing 20,000 lines of documentation per project across 12 subprojects in three days using GitHub Copilot. He emphasized extracting value from Shipkit's prompt engineering patterns rather than just building the sample applications.

Brandon reviewed OpenAI's Agent Kit from Dev Day, rating it 10/10 for deployment ease (one-click publish) but 7/10 for agentic capabilities due to its limitation to left-to-right workflows without true agent-to-agent delegation. He compared it to "N8N meets OpenAI" and noted it generates TypeScript code under the hood.

Hemal shared a solution for Google ADK deployment limitations by deploying the ADK API server to Cloud Run instead of Agent Engine, enabling the use of run and run SSE endpoints with parts and blobs that Agent Engine currently restricts.

Patrick described his methodology for training 100 developers next week, demonstrating the difference in code quality when using AI with versus without instruction files (equivalent to Cursor rules), emphasizing that training materials must be updated constantly as AI tools evolve weekly.

Alex warned about unexpected costs with Google Vertex AI RAG engine and Vector Store, having accumulated a $700 bill from embedding 20,000 pages due to Cursor repeatedly deleting and recreating vector stores during development. Brandon recommended using Supabase for vector storage instead due to significantly lower costs.

Al announced his new role running the global services team at Kong, an API gateway company, explaining how API gateways provide rate limiting, caching, and PII masking for AI applications. He noted that enterprises are struggling to match the development speed of small AI-enabled teams.

Ty demonstrated an N8N workflow validation tool that analyzes JSON workflows for security issues, generates client presentations via Gamma API, and creates hashed verification badges to certify workflow validity.

❓ KEY Q&A

Patrick asked Brandon whether Shipkit templates could be used in private repositories and converted into Custom GPTs for planning phases to save Cursor tokens. Brandon confirmed this is allowed as long as the templates remain private and protected.

Hemal asked about best practices for vibe coding with legacy monolith applications. Brandon advised adapting the AI docs to the specific tech stack rather than using the default Next.js/TypeScript assumptions, treating it as a continual improvement process where mistakes inform updated rules.

Paul asked for recommendations on AI tools to break down long interview videos into social media clips. Brandon suggested Riverside's Magic Clips feature, which automatically identifies and extracts highlight segments from podcasts and interviews.

Joel asked about hidden costs and subscription requirements beyond the Shipkit purchase. Brandon explained the core stack requires Vercel (free tier available, $20 for advanced features), Supabase (free tier available, $20 for expanded limits), and Cursor ($20/month, though users can rotate between Cursor, Windsurf, and Cloud Code to stay within free tiers). He noted AI development costs vary from $100-300 per project depending on speed versus cost optimization strategies.

Mario asked about using Claude Code instead of Cursor for Shipkit given his existing Max plan. Brandon explained that Claude Code lacks Cursor rules support, requiring sub-agents instead, but that Shipkit would release converted rules for Claude Code sub-agents within two days.

🛠️ TOOLS AND CONCEPTS MENTIONED

Shipkit: A template and rules system for AI-assisted development, currently focused on Next.js/TypeScript stacks but being expanded to support Windsurf and Cloud Code variants.

OpenAI Agent Kit: A new visual workflow builder for creating AI agents, featuring one-click deployment and guardrails for PII checking, moderation, and jailbreak detection, though limited to sequential rather than recursive agent workflows.

Google ADK (Agent Development Kit): Google's framework for building AI agents, currently with deployment limitations on Agent Engine that require workarounds using Cloud Run for full API functionality.

Cloud Run: Google's container platform used by Hemal to deploy ADK applications with streaming capabilities not available in Agent Engine.

Cursor Rules: Configuration files that constrain AI behavior to specific tech stacks and best practices; being adapted into sub-agent configurations for Claude Code compatibility.

Trigger.dev: A background job processing service for Next.js applications, recommended for handling long-running AI workflows beyond Vercel's five-minute function limit.

Supabase: PostgreSQL database with vector storage capabilities, recommended over Google Vertex AI for RAG applications due to cost efficiency.

Riverside: Video recording and editing platform with Magic Clips feature for automated highlight extraction.

Gamma: AI presentation generation tool with API capabilities, recently released version 3.0.

T3 OSS: Environment variable validation library used to prevent deployment failures from missing configuration keys.

Kong: API gateway platform providing rate limiting, caching, and security filtering for AI model interactions.

📎 SHARED RESOURCES

OpenAI Dev Day video featuring Sam Altman demonstrating Agent Kit and ChatGPT apps: youtube.com/openai (referenced by Brandon)

Riverside.fm: Video platform with automated clip generation capabilities recommended for content repurposing.

Brandon at shipkit.ai: Email address for support regarding course access and billing issues.

Trigger.dev: Service for background job processing in Next.js applications.

T3 OSS: GitHub repository for environment variable validation in TypeScript projects.

🔄 FOLLOW-UPS WORTH EXPLORING

Windows setup instructions for Shipkit are currently being refined based on community feedback, with PowerShell-specific modifications needed for several setup commands.

A general purpose Shipkit template for non-Next.js stacks (legacy applications, Python projects) is on the roadmap but requires significant adaptation of the current AI docs system.

Claude Code sub-agent configurations converting Cursor rules into specialist agents (TypeScript agent, Python agent, Next.js agent) are in development and expected within 48 hours.

Comparison testing between Gamma and Canva for AI-generated presentations, particularly regarding API capabilities and output quality for client deliverables.

Investigation into OpenAI Agent Kit as a potential Shipkit template, given its TypeScript code generation and deployment advantages for RAG applications.

Cost analysis strategies for rotating between multiple AI coding platforms (Cursor, Windsurf, Cloud Code, Claude Code) to minimize token expenses while maintaining development velocity.