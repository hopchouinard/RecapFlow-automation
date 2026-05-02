📝 SUMMARY

This coaching call covered a wide range of topics from career navigation to technical implementation. Cyril discussed a revoked job offer due to HR policy conflicts despite strong internal support, and sought advice on building a policy chatbot and breaking into FAANG internships. Brandon shared updates on Google's Agent Development Kit (ADK), demonstrating why its deployment-first architecture and stateful multi-agent workflows are outpacing frameworks like Pydantic AI. Michal showcased a WhatsApp conflict-resolution chatbot built with Twilio, while Fernando explored converting a coaching workbook into a web application. The group also debated the practical value of MCP (Model Context Protocol) versus traditional function calling, tested OpenAI's new model lineup (4.5, 4.1, o4 mini), and Brandon advised Alex on launching a Spanish-language AI YouTube channel.

💡 KEY INSIGHTS

Brandon argued that Google's ADK is rapidly gaining traction because it is built for deployment from the ground up, unlike Pydantic AI which requires manual containerization and FastAPI setup. He noted ADK's Agent Engine offers serverless-style pricing around 11 cents per hour when agents run, with built-in state management and session persistence that other frameworks lack.

For Cyril's company policy chatbot project, Brandon explained that RAG is unnecessary because most company policies fit within 30,000 tokens. He recommended using the Vercel AI SDK with a simple prompt containing the full policy document, which simplifies architecture significantly.

Regarding FAANG internships, Brandon and Juan emphasized that referrals are currently the primary pathway in the current market. Paul suggested an alternative route: working at a major customer's company that uses Apple's or Google's tools, then leveraging that domain expertise to apply back to the tech giant.

When Michal demonstrated his WhatsApp chatbot, Brandon advised decoupling the messaging logic from Twilio specifically. He recommended creating a generic messaging service that could be tested via a web interface first, then swapping in Twilio for production without changing core logic.

For Fernando's workbook-to-app conversion, Brandon recommended Lovable paired with Supabase over Firebase Studio, citing current authentication and database connection issues in Firebase Studio. He suggested chunking the workbook into sections and using AI to guide users through sequential completion.

Bastian demonstrated that MCP (Model Context Protocol) enables complex multi-step medical analysis with tool chaining, but clarified it is more powerful yet harder to implement than traditional function calling. He suggested it shines when you need reusable tool servers with prompt layers, not for simple two-tool scenarios.

Brandon advised Alex on YouTube content strategy: hire editors on Upwork ($25-30/hour), use OBS for recording, start with listicles and how-to videos for practice reps, and expect exponential growth only after consistent posting over six months.

❓ KEY Q&A

Q: Cyril asked how to build a chatbot for company FAQ/policy documents and whether this requires RAG or blockchain.
A: Brandon explained that for most company policies, you do not need RAG or complex infrastructure. Since the entire policy likely fits within 30,000 tokens, you can use the Vercel AI SDK with a simple system prompt containing the full policy text, keeping message history per session.

Q: Cyril asked how to pass CV screening for FAANG internships without referrals or elite university credentials.
A: Brandon noted that currently, knowing someone inside is almost mandatory for big tech hiring. Juan shared a case of a friend who transitioned from startup to Google after proving herself, while Paul suggested working at a major customer of Apple/Google first to gain domain expertise that makes you attractive to hire back.

Q: Paul asked why ADK is better than CrewAI or Pydantic AI for agent development.
A: Brandon highlighted ADK's deployment advantages: Agent Engine handles infrastructure automatically, state is shared across agents natively, and deployment costs are consumption-based (roughly 11 cents/hour) rather than constant fees. He noted CrewAI's "flows" feature (alternating agents and code) is currently missing in ADK, but ADK's native Google Cloud integration and session management make it more production-ready.

Q: Fernando asked how to convert a lengthy Google Docs workbook into a client-facing app.
A: Brandon recommended Lovable with Supabase for authentication and database, suggesting he chunk the workbook into sections and guide users through sequential completion, storing progress in the database. He advised waiting for Lovable's upcoming version release which may simplify the process further.

Q: Juan asked about using agentic systems to automate research newsletters for labor unions.
A: Brandon suggested positioning it as a high-value custom service rather than a SaaS product, using Instantly for cold outreach to union directors. He recommended offering a pilot at reduced cost to secure a testimonial, then charging setup fees plus monthly retainers.

Q: Andrew asked about OpenAI's new models (4.5, 4.1, o4 mini) and whether the large context windows are useful.
A: Brandon praised 4.5 as his favorite writing model for consistent style adherence. Bastian noted 4.1 performs better as an agent than 4.0, while o4 mini excels at tool usage and long sequences. Andrew shared OpenAI's prompt engineering tip: wrap large context in XML or Markdown tags and repeat instructions at both the top and bottom of the prompt.

Q: Aaron asked whether ADK supports project management or task orchestration patterns.
A: Brandon indicated ADK's sample repository includes a RAG-based customer service agent that could serve as a foundation, but noted there is no specific project management sample yet. He suggested the stateful multi-agent patterns in ADK could support such workflows.

🛠️ TOOLS AND CONCEPTS MENTIONED

Agent Development Kit (ADK) - Google's framework for building and deploying agents with native state management and Agent Engine for serverless deployment.

CrewAI - Alternative agent framework noted for its "flows" feature allowing alternation between agents and code, though requiring separate deployment infrastructure.

Pydantic AI - Framework mentioned as requiring manual containerization and FastAPI setup for deployment, lacking built-in session management.

Vercel AI SDK - Recommended for simple chatbot implementations where the full context fits in the prompt window.

Lovable - No-code/low-code application builder recommended over Firebase Studio for Fernando's workbook app due to current Firebase Studio limitations.

Firebase Studio - Google's no-code builder mentioned as having current issues with database connections and authentication.

Twilio - Messaging API used by Michal for WhatsApp integration.

ngrok - Tool used for local webhook testing with Twilio.

Supabase - Recommended database and authentication solution for web applications.

MCP (Model Context Protocol) - Protocol for connecting AI assistants to tool servers; demonstrated by Bastian for medical diagnosis with tool chaining.

OpenAI Models - 4.5 (praised for writing), 4.1 (agent capabilities), o4 mini (tool usage), o3 (coding).

Instantly - Cold outreach platform recommended for Juan's union research business development.

Make - Automation platform suggested for integrating AI with Go High Level workflows.

Screen Studio - Mac-specific screen recording software recommended for single-take videos.

OBS - Open-source recording software Brandon uses for YouTube content.

📎 SHARED RESOURCES

github.com/google/adk-samples - Google ADK sample projects including multi-agent travel planner and customer service implementations.

vercel.com/ai - Vercel AI SDK documentation for building chat interfaces.

lovable.dev - Application builder platform for converting documents to web apps.

youtube.com/@Instantlyai - Channel recommended for cold outreach and custom service business strategies.

youtube.com/watch?v=... (Dave Elbert MCP crash course) - Video on Model Context Protocol implementation for Python developers.

🔄 FOLLOW-UPS WORTH EXPLORING

Whether Google ADK will implement code workflows similar to CrewAI's flows to match LangGraph capabilities, which would enable alternating between agent steps and pure code execution without agent overhead.

Testing the scalability of MCP versus traditional function calling in production environments, specifically whether the complexity overhead justifies the benefits for tool reuse across multiple agents.

Implementation results of Fernando's workbook application using Lovable and Supabase, particularly regarding user authentication and progressive form completion.

Pilot results of Juan's agentic research newsletter system for labor unions, including pricing model validation and client acquisition via cold outreach.

Progress on Alex's Spanish-language AI YouTube channel, including content strategy adjustments based on initial video performance.