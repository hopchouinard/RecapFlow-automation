📝 SUMMARY

This coaching call covered advanced AI agent architectures for enterprise automation, cost optimization strategies for cloud GPU infrastructure, and practical workflows for non-technical AI adoption. Brandon Hancock demonstrated ShipKit's RAG template evolution into a course platform, while members discussed browser automation for government forms, AWS infrastructure scaling, and lead generation automation. Key themes included managing AI context windows through separation of concerns, evaluating emerging AI coding tools like SpecKit and Gemini CLI, and bridging the gap between AI prototypes and production deployment.

💡 KEY INSIGHTS

Brandon argued that AI can solve almost any problem with the right context, emphasizing that context engineering is the current bottleneck rather than model capability.

Patrick suggested framing AI as "the most intelligent intern who just started work with zero context" for non-technical audiences, noting that asking the AI what it doesn't know yields better results than assuming knowledge.

Paul emphasized building a "master prompt" that defines job context and responsibilities before using AI professionally, ensuring the model understands the user's role and objectives.

Andrew noted that AI follows a simple rule: "If you put a lot into it, expect a little back; if you put little in, expect a bad time," highlighting the importance of detailed prompting.

Brandon recommended breaking complex agent workflows into separate specialized agents (loop agent, browser agent, entry agent) to prevent context window explosion when automating multi-page government forms.

Ty demonstrated a 5% transaction fee business model for a restaurant ordering system, replacing phone orders with tablet-based automation while keeping costs low for small businesses.

Mitch revealed that many professional services (like CliftonStrengths analysis) are "two or three prompts away" from being automated, showing how AI can replicate personality assessments when given proper context.

❓ KEY Q&A

Q: David asked how to implement human-in-the-loop testing for a robotic process agent automating a 75-page dynamic government application when no test environment exists.
A: Brandon recommended creating a browser agent using Selenium WebDriver controlled by an AI agent in a loop pattern. He advised separating concerns across multiple agents: one to analyze page content and generate answers, another to locate HTML elements, and a third to enter data and submit, preventing context window overload. He referenced Google's Agent Development Kit repository for implementation examples.

Q: James asked how to combine contexts from multiple AI chat sessions when hitting limitations in tools like Gemini CLI or Cursor.
A: Brandon described a manual export workflow: prompting each chat to "export everything discussed in maximum detail," saving outputs to markdown files in an "AI docs/scratch" folder, then starting a new session with instructions to read those files for consolidated context.

Q: Alex asked whether ShipKit's prep templates should reside inside or outside the project directory.
A: Brandon explained the templates perform best inside existing projects (particularly Next.js or ShipKit templates) because they analyze the current codebase to provide relevant guidance. He demonstrated how the system generates a phase-by-phase roadmap (01-09) that users iterate through to build applications incrementally.

Q: Morgan asked about modernizing a 15-year-old school pickup logistics app that used browser polling, specifically how to handle sequencing when one parent picks up children from multiple classrooms.
A: Brandon suggested implementing either a queue system or topological sorting to manage dependencies (e.g., ensuring all children from a car are ready before releasing the next vehicle). He noted this could be solved with data structures rather than necessarily requiring AI.

Q: Patrick asked if anyone had experience with Claude for Financial Services, Anthropic's enterprise offering with proprietary MCPs for financial data.
A: Brandon expressed curiosity about the pricing model, speculating it likely requires custom quotes in the tens or hundreds of thousands monthly. Patrick noted it includes governance, auditing, and financial data feed integrations beyond standard Claude Enterprise.

🛠️ TOOLS AND CONCEPTS MENTIONED

ShipKit: Brandon's AI application development platform with RAG templates and automated roadmaps

Agent Development Kit (ADK): Google's framework for building AI agents with state management and web interfaces

Browser Agent: AI agent equipped with Selenium WebDriver tools to navigate and interact with web pages programmatically

Separation of Concerns: Architectural pattern splitting complex automation into specialized agents (analysis, location, data entry) to avoid context limits

SpecKit: GitHub's spec-based code generation tool that works with Claude Code and Gemini CLI

Beware Toga: Python GUI framework for building native desktop applications across platforms

Topological Sorting: Algorithm for determining order of operations based on dependencies, suggested for logistics sequencing

Warm Boot vs Cold Boot: Cloud infrastructure concepts distinguishing between pre-warmed instances (faster, costlier) and on-demand scaling (slower, cheaper)

MCP (Model Context Protocol): Standard for connecting AI assistants to external tools and data sources

Context7: MCP server providing library documentation access for AI coding assistants

Sequential Thinking: MCP server enforcing chain-of-thought reasoning for complex problem solving

RAG Evaluation: Framework for testing retrieval-augmented generation accuracy in production environments

Pydantic: Python data validation library suggested for pure automation workflows without agent overhead

Gaussian Splats: 3D scanning technology mentioned for creating photorealistic assets and environments

📎 SHARED RESOURCES

Beware Toga: Python native widget GUI framework recommended by Andrew for local application development

Matt Wolfe: YouTube channel recommended by Brandon for AI news updates

Theo: YouTube content creator providing daily AI education videos

Futurpedia: AI news and resource platform mentioned by Alex

SpecKit: GitHub's specification-based code generation tool tested by Patrick with Claude Code

AI Engineering Bible: Kindle Unlimited book recommended by Brandon for theoretical AI engineering foundations

AI Engineering by Chip Huyen: Book discussed by Juan for teaching machine learning engineering concepts

Fabric: Daniel Miesler's project mentioned by Patrick for building AI assistants

LinkUp: Lead research tool used by Mitch for personalized email outreach

Appify: Web scraping platform used to build lead lists for B2B campaigns

Instantly: Email outreach automation platform for cold email sequences

AWS Cost Calculator: Tool used by Juan to budget EC2 GPU instance costs

AWS Activate: Startup credits program providing up to $1,000+ for AWS infrastructure costs

Unreal Engine: Platform mentioned by Jake for creating real-time AI avatars and digital puppets

Heijen: Avatar video generation platform discussed for creating AI-powered character videos

🔄 FOLLOW-UPS WORTH EXPLORING

Evaluating RAG systems for production environments, including community-contributed evaluation workflows for different RAG architectures

Testing GitHub's SpecKit against ShipKit templates for AI application development workflows

Investigating OpenAI's new RAG training methodology (referenced white paper) and its implications for hallucination reduction

Claude for Financial Services enterprise features, pricing models, and proprietary MCP integrations for financial data

Compression strategies for ADK conversation state to reduce token costs when using Gemini Flash versus GPT-4o mini

Converting n8n-style automation workflows into deployed Pydantic-based background workers for pure automation without chat interfaces

Real-time AI avatar generation using Unreal Engine versus Heijen for business applications

Community contributions to ShipKit templates for specialized RAG implementations and evaluation frameworks