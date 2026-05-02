📝 SUMMARY

This coaching call covered the intersection of AI-assisted development and enterprise deployment, with Patrick navigating corporate vibe coding adoption while balancing cybersecurity requirements against business user demands. Marc shared progress on N8N workflow automations deployed to Railway, while Brandon provided updates on ShipKit's prompt-driven development approach. The group troubleshooted technical challenges ranging from webhook data limits and Supabase security configurations to ADK integration patterns and Next.js deployment strategies. Additional topics included voice assistant architecture, job search advice for developers, and strategies for managing AI tool adoption in regulated environments.

💡 KEY INSIGHTS

Patrick is managing the tension between business users wanting lovable, IDE-free development experiences and cybersecurity teams requiring controlled, secure tooling. Brandon suggested implementing standardized pipelines with critique patterns where security requirements are encoded into automated review cycles, allowing business users to prototype while ensuring compliance guardrails exist.

Marc demonstrated how foundational knowledge of frameworks like LangChain translates to faster adoption of no-code tools like N8N, enabling rapid prototyping for real estate automation use cases including Google Drive webhooks that trigger AI-generated email responses.

Brandon emphasized that enterprise AI adoption requires structured onboarding rather than giving business users unrestricted access to tools like Cursor. He recommended starting developers with supervised environments and standardized templates before expanding to broader vibe coding practices.

Paul noted that consulting firms and enterprise clients are increasingly requesting vibe coding capabilities, creating pressure to deliver AI-assisted development while maintaining security standards.

Juan resolved a critical infrastructure challenge by deploying Tailscale VPN binaries on restricted Oculus servers without administrative permissions, enabling secure connections for agentic IDE development on A100 GPUs.

Tom is architecting a multi-tenant asset management platform with database-per-organization isolation for enterprise clients, while using shared databases for lower-tier offerings.

Brandon recommended against using raw Google Cloud Platform for solo developers, suggesting managed services like Supabase or Neon for databases, Clerk or WorkOS for authentication, and Vercel for Next.js hosting to reduce operational complexity.

❓ KEY Q&A

Q: How can we integrate vibe coding practices in a corporate environment where cybersecurity wants control but business users want lovable experiences?
A: Brandon recommended implementing a critique pattern where security requirements are encoded into automated review cycles. He suggested looking at DoD Platform One and Big Bang as reference architectures for standardized CI/CD pipelines that restrict allowable tech stacks while enabling rapid development. Paul suggested using business analysts as intermediaries to facilitate Shark Tank-style pitch sessions where ideas are vetted before development begins.

Q: What are the data limits for webhooks when sending large JSON objects to trigger AI workflows?
A: Brandon advised against sending large data payloads through webhooks. Instead, send minimal identifiers (like job IDs) and move the data assembly logic into the backend job itself. While REST protocols can handle several hundred kilobytes to potentially a megabyte, Vercel has default limits around 1-4 megabytes for serverless functions.

Q: Are Supabase security warnings about unrestricted databases a concern when using Drizzle ORM?
A: No. Brandon clarified that Supabase security warnings apply specifically to using the Supabase client directly in frontend code, which allows users to potentially access entire tables. Using Drizzle ORM with structured API endpoints and proper authentication checks before database queries eliminates this risk.

Q: How should I integrate ADK into an existing Django application for context-aware property management features?
A: Brandon recommended embedding ADK directly within the Django application rather than running it as a separate service. This eliminates deployment complexity and allows direct access to Django's ORM for user context. He suggested creating sessions with initial state containing user IDs and relevant context, then using root_agent.run() to process requests within the Django request/response cycle.

Q: What is the best hosting approach for a Next.js application migrating from WordPress?
A: Brandon strongly recommended Vercel for Next.js hosting due to automatic server-side rendering optimization, SEO benefits, and simple custom domain configuration. For email services, he suggested Mailgun. He noted that Vercel's hobby tier is free for single projects and includes essential features.

Q: How can I handle LinkedIn profile data scraping for my application while remaining GDPR compliant?
A: The group discussed using services like Appify or Serper for public profile data, emphasizing that scraping only publicly available information that users voluntarily display should satisfy GDPR requirements. Brandon suggested using deep research to verify compliance approaches for specific use cases.

🛠️ TOOLS AND CONCEPTS MENTIONED

N8N: Workflow automation platform discussed for rapid prototyping and business automation without heavy backend coding. Marc deployed instances to Railway and Digital Ocean for webhook-based automations.

ShipKit: Brandon's prompt-driven development course and template system for building AI applications. Features include prep templates, critique patterns, and standardized workflows for converting templates into custom applications.

ADK (Agent Development Kit): Google's framework for building agentic applications. Discussed extensively regarding integration into Django, routing patterns using orchestrators with phases, and deployment strategies.

Supabase: Database and authentication platform. Discussed regarding security models, row-level security warnings, and as an alternative to Vercel Postgres or raw Google Cloud databases.

Railway: Deployment platform used by Marc for hosting N8N instances with easy webhook accessibility.

Platform One / Big Bang: DoD reference architectures for secure CI/CD pipelines and standardized deployment templates that Brandon suggested as models for corporate AI governance.

Tailscale: VPN solution Juan used to create secure connections to restricted servers without administrative permissions.

Limitless.ai: Wearable device for recording conversations and meetings. Paul uses it for productivity tracking and follow-up automation.

LiveKit: Voice assistant infrastructure recommended by Brandon for building customer support voice applications, offering a middle ground between no-code tools and custom implementations.

Drizzle ORM: TypeScript ORM used by multiple participants with Supabase to ensure type-safe database queries and avoid security issues associated with direct Supabase client usage.

MCP (Model Context Protocol): Discussed regarding security compliance and standardization challenges in enterprise environments.

📎 SHARED RESOURCES

ShipKit.ai: Brandon's platform for prompt-driven application development with templates for RAG, chat, and ADK agents.

Platform One / Big Bang: DoD repository and documentation for secure CI/CD pipelines and standardized deployment frameworks. Brandon shared links to these resources for Patrick's corporate governance research.

ADK Browser Agent Repository: Google ADK example showing orchestrator patterns with phased agent routing, recommended by Brandon for complex workflow implementations.

Supabase Documentation: Referenced for authentication setup with Google and GitHub providers, including middleware configuration for Next.js applications.

LiveKit Documentation: Voice assistant platform documentation recommended for building ERP/CRM-integrated customer support systems.

📎 SHARED RESOURCES

ShipKit.ai: Brandon's platform for prompt-driven application development with templates for RAG, chat, and ADK agents.

Platform One / Big Bang: DoD repository and documentation for secure CI/CD pipelines and standardized deployment frameworks. Brandon shared links to these resources for Patrick's corporate governance research.

ADK Browser Agent Repository: Google ADK example showing orchestrator patterns with phased agent routing, recommended by Brandon for complex workflow implementations.

Supabase Documentation: Referenced for authentication setup with Google and GitHub providers, including middleware configuration for Next.js applications.

LiveKit Documentation: Voice assistant platform documentation recommended for building ERP/CRM-integrated customer support systems.

🔄 FOLLOW-UPS WORTH EXPLORING

Patrick's corporate vibe coding implementation: Monitoring how the 6,000-employee organization balances business user autonomy with cybersecurity requirements using standardized pipelines and critique patterns.

Juan's LLM infrastructure: Completion of the API bridge between external applications and the on-premise Oculus GPU servers, including authentication and rate limiting strategies.

Ola's Django ADK integration: Resolution of Google Workspace policy conflicts preventing Vertex AI API access, and implementation of context-aware property management features.

Alex's job search: Follow-up on connections made through the community for consulting firm opportunities and small company roles in the Colorado Springs area.

Never2Nervous's SaaS factory: Migration from raw Google Cloud infrastructure to Supabase/Next.js stack to resolve persistent authentication routing issues.

Hemal's chat application: Implementation of the orchestrator pattern with phase-based routing for travel booking workflows, and standardization of the JSON communication protocol between UI and API layers.

Voice assistant architecture: Evaluation of LiveKit versus Gemini Live for customer support implementations requiring ERP/CRM integration.