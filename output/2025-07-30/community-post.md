📝 SUMMARY

This coaching call covered the full spectrum of modern AI development, from tactical cost-saving workflows to existential discussions about superintelligence. Brandon Hancock led the group through demonstrations of Agent Development Kit (ADK) templates, Convex as a real-time backend alternative, and strategies for managing spiraling AI tooling costs. Members shared practical implementations including Ty Wells' Agent Hub for orchestrating multiple agents, Patrick Chouinard's automated training generation from release notes, and Bastian Venegas' integration of the Limitless AI pen with Convex. The conversation shifted toward strategic career positioning, with debates on whether the group represents the true cutting edge or if a hidden tier of developers exists, concluding with sobering predictions about the 2027 AI timeline and the "post-labor economics" era.

💡 KEY INSIGHTS

Brandon argued that the bottleneck for any paid community or product is attention, not the product itself, advising AbdulShakur to build a free audience first through YouTube and LinkedIn before monetizing a prompt library. Patrick and Brandon predicted a new job category emerging: "AI slop to production-ready" engineers who clean up vibe-coded MVPs into enterprise-grade applications, suggesting this will be a lucrative six-figure consulting niche. Mitch revealed a cost-arbitrage strategy of using Cursor to generate task documents and PRDs, then executing the actual coding in Warp to save on Cursor token limits, while Paul demonstrated pointing Claude Code to Kimi K2 via Base10.co to reduce API costs by 80%. Ty emphasized that despite the group's advanced tooling knowledge, most enterprises remain years behind, creating a massive opportunity for micro-SaaS solutions that replace $30,000 legacy software. Brandon warned that the window for securing capital through AI consulting may close within three years as superintelligence emerges, referencing the "AI 2027" paper and David Shapiro's "Post Labor Economics" framework.

❓ KEY Q&A

Ty asked how to manage scattered projects and notes with contextual awareness so that AI could surface relevant past work when needed. AbdulShakur suggested Otter.ai for transcription with AI search capabilities, while Jake recommended the "Second Brain" approach using Obsidian, and Brandon endorsed Notion with Thomas Frank's methodology for structured databases.

Gopal raised a technical issue regarding CrewAI Enterprise deployments returning HTTP 500 errors when attempting to retrieve inputs. Brandon diagnosed this as likely a YAML configuration or folder structure mismatch, offering to connect Gopal directly with the CrewAI team for resolution.

AbdulShakur questioned whether to charge for a prompt library community or keep it free to encourage sharing. Brandon advised keeping the library free to maximize adoption and instead monetizing through adjacent premium content like advanced prompt engineering courses, using the "give everything away for free" strategy to build trust and authority first.

Tom asked for clarification on using Gemini CLI alongside Cursor. Brandon explained he previously used Gemini CLI in terminal tabs to bypass Cursor's three-tab limit, though now that Cursor supports five to six tabs, he primarily uses the native interface unless Cursor experiences outages.

🛠️ TOOLS AND CONCEPTS MENTIONED

Limitless AI pen: A wearable device that records conversations and transcribes them via API, demonstrated by Bastian as part of his personal knowledge management stack.

Otter.ai: Voice transcription service with AI-powered action item extraction and conversation search, noted by AbdulShakur as superior to his legacy Noda app lifetime deal.

Obsidian and Second Brain: Personal knowledge management methodologies discussed by Jake and Brandon for organizing complex information.

Notion: Brandon's preferred tool for life management, utilizing databases and templates for task tracking and content organization.

ADK (Agent Development Kit): Google's framework for multi-agent workflows, which Brandon showcased through ShipKit templates featuring real-time timeline visualization of agent activities.

Gemini CLI: Google's command-line interface for AI coding assistance, previously used by Brandon to parallelize development work when Cursor had stricter tab limits.

Opal: Google's natural language workflow builder that generates agentic flows without code, discussed by Paul and AbdulShakur as a potential N8N competitor requiring personal Google accounts and US VPN access.

Convex: A real-time backend alternative to Supabase with TypeScript-native schema definitions and file storage, demonstrated by Bastian for his Limitless integration project.

CrewAI: An agentic framework for Python that Gopal struggled to deploy in Enterprise mode due to input configuration issues.

LangChain and LangGraph: Marc's chosen frameworks for building fantasy football agents, with Brandon noting LangGraph's stability for production use despite steeper complexity.

Kimi K2: A Chinese open-source model praised by Juan and Paul for matching OpenAI's premium performance at 80% lower cost, accessible via Base10.co hosting.

OpenAI Agents: New browser-based agent capabilities demonstrated by Ty for automated shopping on Shields.com, including cart building and checkout assistance.

MCP (Model Context Protocol) Servers: Jake highlighted Sequential Thinking for breaking complex tasks into sub-tasks, while Brandon recommended Context7 for documentation and Time tools for preventing date hallucinations.

Warp: An AI-enhanced terminal Mitch uses to execute Cursor-generated task documents without burning Cursor credits.

Claude Code: Anthropic's terminal-based coding agent, noted to require the $200/month Pro plan for unlimited usage to avoid per-session charges.

Lovable: A no-code/low-code builder Ty used to construct an Agent Hub and mobile applications without touching traditional codebases.

Strands Agents: AWS's agent framework that Asako is documenting through blog posts and tutorials as part of her developer advocate portfolio.

A2A (Agent-to-Agent protocol): Mentioned by Ty and Brandon as the future standard for connecting disparate AI agents in distributed systems.

📎 SHARED RESOURCES

GitHub repository containing Brandon's task templates for Fathomstack and NexJS projects, available for 24 hours post-call for community members to download.

Thomas Frank's Notion crash course on YouTube for learning database structures and second brain methodologies.

Base10.co: Hosting platform for Kimi K2 that provides API endpoints with significantly lower costs than Anthropic or OpenAI.

AI 2027: A research paper and video analysis predicting artificial superintelligence emergence by 2027, shared by Brandon regarding the timeline for securing capital before labor disruption.

David Shapiro's "Post Labor Economics": Content channel and books exploring economic models when traditional labor value collapses due to AI automation.

🔄 FOLLOW-UPS WORTH EXPLORING

Brandon will interview the creator of Presentify and other productivity tools this weekend; community members should submit questions about serial entrepreneurship and indie app development.

Asako is developing AWS Strands Agents tutorials and seeking feedback on blog posts covering multi-agent implementations and A2A protocols.

Patrick is building a "Rosetta Stone" translation matrix between agentic frameworks (Claude Code, CrewAI, LangGraph, ADK) to map equivalent concepts like sub-agents, tasks, and instructions across platforms.

Ty is recruiting alpha testers for his Agent Hub, a centralized interface for orchestrating multiple custom agents with MCP server integration.

Brandon will test OpenAI Agents during his upcoming vacation for travel planning and reservation booking, reporting back on real-world utility versus traditional travel planning methods.

The group plans to investigate whether Docker's new model hosting capabilities (similar to Ollama) will provide a viable local alternative to cloud API costs for development work.