📝 SUMMARY

This coaching call covered the full spectrum of AI-assisted development from individual productivity hacks to enterprise consulting strategies. Ty Wells introduced Cursor's new background agent capabilities for asynchronous coding, while Brandon Hancock unveiled ShipKit, a CLI tool for rapidly scaffolding AI applications. The community dove deep into technical architecture decisions including MCP server performance, voice AI infrastructure with LiveKit, and secure deployment patterns for regulated industries. Al Cole led a strategic discussion on enterprise AI consulting frameworks, with Brandon sharing his flywheel methodology for converting implementation work into marketing content. Members shared wins including Tom Welsh's asset management system and Andrew Nanton's document processing pipeline, while troubleshooting specific technical blockers around ADK agent-to-agent communication and NetSuite automation.

💡 KEY INSIGHTS

Ty Wells described a paradigm shift in development workflows using Cursor's background agents, allowing him to kick off scaffolding tasks via Slack while away from his computer, effectively treating AI like a "senior developer" that works asynchronously. He emphasized the importance of detailed planning before delegating to agents to minimize interpretation errors.

Brandon Hancock introduced ShipKit, a CLI-based project launcher designed to spin up production-ready AI applications (chat apps, RAG systems, agentic apps) with pre-configured templates and rules. He demonstrated converting a chat template into an LM Arena-style model comparison app in 25 minutes using iterative task templates.

Brandon shared his systematic approach to Cursor rules management: rather than fixing errors once, he documents each mistake as a new rule to prevent recurrence, building a reusable "training set" that improves AI performance over time. He noted this iterative process reduced his manual intervention from one in three files to one in twenty.

Bastian Venegas identified LiveKit as a comprehensive solution for voice AI applications requiring phone integration, noting its ability to handle low-latency requirements and SIP trunking for actual phone numbers—critical for healthcare and enterprise use cases where web-only interfaces are insufficient.

Andrew Nanton highlighted the cost efficiency of Claude Code's Max plan ($200/month) for intensive development periods, suggesting it can be more economical than per-token API pricing when building complex applications like his Azure Document Intelligence wrapper.

Brandon outlined a consulting flywheel strategy for Al Cole: implement solutions for friends/network contacts, then immediately convert those implementations into public case studies and lead magnets. This creates a feedback loop where action generates marketing content, which generates new opportunities.

❓ KEY Q&A

Cyril asked about automating Oracle NetSuite for delivery and internal systems. Brandon recommended Apache Airflow for enterprise-grade automation, noting NetSuite's API credentials are cumbersome but well-documented in older AI models. Juan added that DAG files can be deployed on AWS or local servers, though AWS can become expensive.

Matias reported persistent 503 network errors when connecting ADK host and agent locally despite successful message passing. Brandon suggested forking his working repository to isolate whether the issue stems from code differences or version mismatches, noting ADK is evolving rapidly and breaking changes are common.

Maxim observed that switching voice agents from traditional tool schemas to MCP servers improved latency significantly. He theorized that MCP's router pre-selects tools rather than passing all schemas to the LLM. Brandon noted this was surprising as MCP requires an additional network hop, suggesting the performance gain might come from JSON-RPC efficiency or reduced context window usage.

Al asked about structuring enterprise consulting engagements for AI maturity. Brandon advised defining concrete transformations (e.g., "I help developers become AI developers") and creating packaged service offerings with clear price points. He emphasized giving away implementation templates as lead magnets to demonstrate value before contracting.

Juan inquired about secure AI deployment options for sensitive data requiring no egress traffic. Brandon recommended Azure's private virtual cloud for OpenAI access, warning that choosing on-premise GPU solutions (like Oculus) might limit future model flexibility if requirements change to include Gemini or other providers.

Nate asked about SEO optimization for his self-built website. Brandon recommended using Chrome's Lighthouse tool to audit performance and accessibility, ensuring static text rendering for scrapers, and maintaining consistent meta tags. He suggested driving initial traffic through paid ads to signal relevance to search engines.

🛠️ TOOLS AND CONCEPTS MENTIONED

Cursor: AI code editor with new background agent capabilities for asynchronous task execution and Slack integration. Ty uses it for remote scaffolding while away from his machine.

ShipKit: Brandon's CLI tool for launching AI projects (chat apps, RAG, agentic apps) with pre-built templates and standardized rules to avoid starting from scratch.

Lovable: Visual development platform recommended for static websites and rapid UI prototyping, with suggestions to pair with N8N for dynamic content workflows.

Gemini CLI / Claude Code: Terminal-based coding agents. Brandon noted Gemini CLI lacks interactive loops for long-running jobs, while Andrew praised Claude Code's Max plan for cost-effective intensive development.

Apache Airflow: Workflow orchestration platform recommended for NetSuite automation using directed acyclic graphs (DAGs) to handle complex enterprise logic.

ADK (Agent Development Kit): Google's agent framework. Discussion covered new planning capabilities for multi-step reasoning and deployment challenges with agent-to-agent communication.

MCP (Model Context Protocol): Standard for connecting AI assistants to data sources. Maxim noted performance improvements when using MCP servers for voice agent tool management compared to traditional schema passing.

LiveKit: Open-source platform for voice and video applications, highlighted for its phone integration capabilities (SIP trunking) and low-latency performance suitable for healthcare applications.

LangSmith: Evaluation and tracing platform for LLM applications. Juan mentioned using it with Crew AI for context window assessment, while Brandon noted ADK currently lacks equivalent evaluation feedback loops.

ShadCN: UI component library for React/Next.js applications, recommended for maintaining design consistency through centralized CSS variables and component variants.

Lighthouse: Chrome DevTools feature for auditing website performance, accessibility, and SEO metrics.

Mobbin: UI/UX design reference library showing screenshots of popular apps for inspiration, suggested by Paul for improving interface design.

CodeRabbit: AI-powered code review tool that integrates with GitHub and project management platforms like Linear or Jira.

📎 SHARED RESOURCES

github.com/brandonhancock/shipkit (Brandon's CLI tool for AI project scaffolding)

youtube.com/@t3dotgg (Theo's channel, recommended for full-stack development insights)

youtube.com/@mattberman (Matt Berman's channel on prompt engineering)

youtube.com/@webdevcody (Web development tutorials and AI coding workflows)

youtube.com/@programmaticengineer (Brett's channel for inspirational engineering stories)

github.com/livekit (Voice AI platform with phone integration capabilities)

mobbin.com (UI/UX design patterns and screenshots for application inspiration)

docs.livekit.io/agents/overview/ (LiveKit documentation for voice agents)

cloud.google.com/agent-development-kit (Google ADK documentation and new planning features)

🔄 FOLLOW-UPS WORTH EXPLORING

Brandon committed to creating a video demonstrating ADK deployment with FastAPI and React frontend, addressing Marc's request for a simplified Next.js integration pattern.

Matias will test Brandon's ADK repository to isolate the 503 connection error and verify if it stems from version mismatches or configuration differences.

Maxim plans to evaluate LiveKit for his voice agent infrastructure, specifically testing custom API key integration to host models closer to his Mexico-based users and reduce latency during peak hours.

Al will develop concrete service packages for his AI consulting practice, with a target of launching marketing efforts at the upcoming AWS Summit in New York City.

Juan needs to finalize secure deployment architecture decisions with his client, weighing the cost benefits of on-premise GPU clusters against cloud-native solutions like Azure OpenAI Service or AWS Bedrock.

Brandon will investigate Jules (Google's async coding agent) and CodeRabbit for automated code review workflows, comparing them against Cursor's native capabilities for CI/CD integration.