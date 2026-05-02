📝 SUMMARY

This coaching call covered a wide range of advanced AI implementations across enterprise evaluation, agentic workflows, and production SaaS applications. Patrick shared his methodology for evaluating major AI enterprise platforms at scale, while Scott demonstrated parallel agent architectures for personal automation. Ryan showcased a social media management platform with integrated AI image editing, and Maxim discussed voice agent deployments for automotive clients. The group also explored compliance automation, remote coding infrastructure, and various technical approaches for managing context windows and latency in production systems.

💡 KEY INSIGHTS

Patrick is leading an enterprise AI evaluation across OpenAI, Anthropic, Gemini, and Perplexity, maintaining flexible agreements with multiple providers rather than binding to a single vendor. He emphasized that enterprise agreements include tools and assets not available in public versions, and recommended using token pools shared across users rather than individual limits.

Scott detailed his implementation of parallel agent workflows using the Anthropic TypeScript SDK (not the Vercel AI SDK), running course summaries, follow-up checks, and relationship checks simultaneously to avoid context window limitations. He noted that splitting tasks into parallel calls with specific constraints (like date ranges) prevents timeouts and reduces overhead.

Ryan demonstrated a social media automation platform built with Next.js, Supabase, and Cloudflare R2, integrating Nano Banana for image retouching and generation directly within the application. He uses a layered prompt system combining system prompts, frameworks, and client-specific brand context.

Maxim discussed his work with Mazda and Infinity deploying WhatsApp chatbots and voice agents for both sales teams and end customers. He noted the trade-off between latency and tool-calling capability in voice models, currently using Kimi K2 in production but considering GPT-4o mini based on latency benchmarks.

Brandon emphasized the value of task-based development with artifact documentation for each change, recommending automated git commit workflows to preserve progress when AI goes rogue. He also highlighted the generate-critique pattern for quality assurance, where one agent generates output and another evaluates it with feedback loops.

Tiran showcased several projects including CV Refinery for resume optimization against specific job descriptions, a prepper planning tool, and a system converting markdown consulting reports into interactive HTML applications. Patrick suggested CV Refinery could be particularly valuable for consulting firms needing to reformat CVs for RFPs.

❓ KEY Q&A

Q: How can I build a Windows application using Claude Code?
A: Tiran suggested PyInstaller for converting Python to Windows executables, while Brandon recommended Electron for cross-platform desktop applications. Ty mentioned successfully building a Rust application through Claude Code and deploying via GitHub Actions.

Q: How do you handle context window limits when running parallel agent tasks?
A: Scott explained he implements hard-coded rules and date constraints (e.g., only last 7 days of emails, summary-only transcripts) to ensure parallel outputs never exceed context limits. He also noted that splitting tasks gives each agent its own context window.

Q: What is the best approach for voice agents requiring both low latency and tool calls?
A: Maxim noted the trade-off between speed and capability, with faster models often failing at tool calls. Ty reported success with GPT-4o mini on 11labs achieving approximately 45ms latency while maintaining tool-calling reliability. Carlos mentioned OpenAI's GPT Real-time as another option specifically designed for voice applications.

Q: How do enterprise AI agreements differ from consumer plans?
A: Patrick clarified that enterprise agreements provide unlimited token pools shared across all users, include additional tools and assets not in public versions, and offer different pricing structures. He recommended maintaining agreements with multiple providers simultaneously to avoid vendor lock-in given rapid market changes.

🛠️ TOOLS AND CONCEPTS MENTIONED

Claude Code - Anthropic's CLI coding tool, used by Patrick for horizontal search agents and by Ty for remote VPS coding environments
OpenCoder - Open source alternative to Claude Code for running local models
Anthropic TypeScript SDK - Scott's chosen framework for agent implementation (distinct from the Agent SDK)
Trigger.dev - Workflow orchestration platform discussed for parallel agent execution and background tasks
Gemini CLI - Google's command-line tool with search capabilities, though Patrick noted Claude Code performs better for research
Nano Banana - Image generation and editing API integrated into Ryan's social media platform
Cloudflare R2 - Object storage used by Ryan for media files to avoid Supabase storage limits
PyInstaller - Tool for converting Python scripts to Windows executables
Vanta - Compliance automation platform recommended for SOC 2 and security certifications
Linked Helper - LinkedIn automation tool mentioned for outreach workflows
Appify - Web scraping service Brandon plans to use for LinkedIn data extraction
Generate-Critique Pattern - Agent architecture where one agent generates output and another evaluates quality with feedback loops
Parallel Agent Pattern - Running multiple specialized agents simultaneously with an aggregator combining results

📎 SHARED RESOURCES

OpenCoder - Open source Claude Code alternative available on GitHub
PyInstaller - Package for converting Python applications to standalone executables
Vanta - Compliance and security certification platform (vanta.com)
Linked Helper - LinkedIn automation and outreach tool
Appify - Web scraping and data extraction platform
Trigger.dev - Background job and workflow orchestration platform

🔄 FOLLOW-UPS WORTH EXPLORING

Results of Patrick's enterprise platform evaluations comparing OpenAI, Anthropic, Gemini, and Perplexity enterprise features and performance
Testing GPT-4o mini versus Kimi K2 for voice agent applications with tool-calling requirements
Progress on Ryan's broken Netlify/Claude Code build issue and the resolution approach
Maxim's experience obtaining CASA 2 certification for Google OAuth restricted permissions
Brandon's LinkedIn scraping workflow using Appify combined with Gemini CLI for deep research
Scott's implementation of quality assurance loops (generate-critique pattern) in his morning summary workflow
Ty's Windows kiosk application deployment using Rust and Docker on VPS infrastructure