## general

This was a weekly group coaching call hosted by Brandon Hancock, focused on AI development, coding projects, and community updates. The session followed a round-robin format where participants shared wins, project updates, or problems they needed help with. Attendees included developers and community members from Australia, New Zealand, Europe, and the Americas.

Brandon opened with two major announcements: an upcoming YouTube video series on Google Gemini agent use cases, and a new program called the "AI Authority Accelerator" — an eight-week group coaching program designed to help developers build an AI-focused personal brand on YouTube and LinkedIn and land at least one paid opportunity. The rest of the session covered individual project updates ranging from LLM model comparisons, CrewAI deployments, database architecture, video content creation, and a hackathon project.

A first-time attendee, Joh Leonhardt, introduced himself as a community leader and representative of an AI-focused technology company (Trideca, part of the Supernis group) based in Melbourne, actively hiring for AI roles including "co-pilot change managers" and developers skilled in LangChain, LangGraph, and Microsoft AI Foundry. Brandon offered to connect community members with Joh's hiring needs.

Technical discussions covered topics including: choosing between O3 Mini, Claude Sonnet 3.5, and Gemini Flash for coding tasks; using OpenRouter for production-grade LLM routing; setting LLMs in CrewAI via the crew file; building a website audit tool using screenshots and multimodal AI; and integrating Firecrawl with CrewAI for web research in newsletter agents.

## insights

- **Brandon:** Most developers are technically strong but weak at marketing — analogous to a bodybuilder who only trains their upper body. Building a personal brand is the missing leg.
- **Brandon:** O3 Mini is his default LLM for coding; GPT-4o is used only when image processing is needed. Flash models are best for general everyday non-technical use cases; OpenAI models outperform for high-skill professional tasks (engineering, law, medicine).
- **Brandon:** OpenRouter is recommended for production applications — it adds a small tax per LLM call but provides fallback models and safeguards against outages. It should be considered required for production-grade apps.
- **Reuben:** Blocking dedicated "deep work" coding days (no browsing, no YouTube) is necessary to avoid the trap of learning without building.
- **Paul:** Comparing deep-thinking models (O3, Gemini, Perplexity) with identical prompts revealed O3 Advanced is best for grand-scale problem solving because it challenges the framing of the question itself.
- **Paul:** Merging all Python library files into a single text file (with delimiters) allows you to stay within Google AI Studio's 10-context-file limit while still giving the model full library context.
- **Maksym:** Running unit and integration tests before moving to the next phase caught unclosed database pool connections — a problem that would have caused scaling failures under concurrent load.
- **Brandon:** Before automating any outbound process (e.g., website audit reports), validate it manually 100 times first. Automating something that doesn't work just scales the failure.
- **Brandon:** For YouTube thumbnails, text should be large enough to read on a mobile phone; four words or fewer is ideal. The thumbnail's job is to communicate the outcome, not showcase design artistry.
- **Brandon:** When recording a technical tutorial video, give a roadmap outline at the start and limit each file/section to three key points to avoid 30-minute tangents on a single file.
- **Brandon:** Niche specificity defines audience size — "how to web scrape the Federal Reserve" attracts a highly engaged but small audience; broadening to "how to scrape government data" expands reach.
- **Asako:** Gemini 2.0 Flash can natively summarize web page content from URLs without needing a separate web scraper tool.
- **Bastian:** MCP (Model Context Protocol) is now available in both Cursor and Windsurf; it enables bidirectional communication with AI agents, including natural language error messages that guide the agent to self-debug.
- **Brandon:** For a website audit tool, use a web driver (e.g., Puppeteer) to take screenshots, pass them to a multimodal model (GPT-4o), and output results as styled HTML — then print to PDF for client delivery.

## qa

**Q (Reuben):** If we were building something similar to what was built in the course today, would we go through the same process or rely more on AI to build components?

**A (Brandon):** Landing pages and UI shells can be done faster now with tools like Lovable, Bolt, V0, and improved Shadcn components. But core business logic — especially automating existing human workflows — still requires you to be the expert. One major change: use OpenRouter for production apps so you have model fallbacks and aren't at the mercy of a single provider.

**Q (Paul):** Are people using O3 Mini or Gemini Flash as the base model in Cursor for large multi-file projects?

**A (Brandon):** O3 Mini (200k token context window) is his default for coding. Flash is great for general queries but not as strong for actual code generation. For cross-codebase architectural questions, Flash's large context could help with retrieval but won't reason well about merging two projects.

**Q (Philip):** How can a CrewAI newsletter agent be set up to automatically collect articles from the internet on a weekly schedule rather than requiring manual input?

**A (Brandon):** Add a research task before the outlining task in the crew. If you already have links, pass them as a comma-separated string input alongside the brain dump. Use Firecrawl for internet search/scrape functionality — it integrates well with CrewAI and provides generous free credits.

**Q (Pavan):** What is the best way to set a non-default LLM in CrewAI — via YAML, environment variables, or code?

**A (Brandon):** Preferred method is to define the LLM object directly in the crew file (specifying model, API base, version), then pass it to each agent. This makes it immediately visible which model is in use. Under the hood CrewAI uses LiteLLM, so the same model string format used in LiteLLM docs applies directly.

**Q (Philip):** How would you build a website audit tool that takes screenshots, analyzes them with AI, and outputs a PDF report for cold outreach?

**A (Brandon):** Use Puppeteer (or potentially Browser Use) to open the target website and take screenshots. Pass screenshots to GPT-4o (multimodal). Give the agent a UX scorecard prompt — you can generate the scorecard itself by asking GPT to clone an existing audit tool's scoring logic. Output as styled HTML, then print to PDF. Start by doing this manually 100 times before automating.

**Q (Philip):** Do you offer consulting sessions?

**A (Brandon):** Not currently due to time constraints. Will send an email announcement when that changes.

## tools

- **Google Gemini / Google AI Studio** — Brandon building use cases with Gemini agents; Paul using it to analyze Python library codebases
- **Grok 3 (xAI)** — Just released; noted for deep search, reasoning ("brain power"), and coding features; API coming in weeks
- **O3 Mini (OpenAI)** — Brandon's default coding LLM; Maksym switched to it after finding it superior to Claude Sonnet 3.5 for test writing
- **GPT-4o (OpenAI)** — Used for image/multimodal processing; recommended for website audit screenshot analysis
- **OpenRouter** — Recommended for production LLM routing; provides model fallbacks and uptime safeguards
- **CrewAI** — Primary multi-agent framework discussed throughout; used for newsletter agents, deployed APIs, and more
- **Firecrawl** — Web search/scrape tool that integrates with CrewAI; recommended for newsletter research tasks
- **Cursor** — AI coding IDE; discussed in context of model selection and MCP support
- **Windsurf** — AI coding IDE; mentioned as also supporting MCP protocol
- **MCP (Model Context Protocol)** — Bidirectional API protocol for AI agents; available in Cursor and Windsurf; discussed by Bastian
- **Supabase** — Used as database with built-in auth for Maksym's dealership project
- **Clerk** — Auth tool Maksym prefers for its organization/sync features; considered as fallback
- **Azure PostgreSQL** — Database hosting for Maksym's second project with Andrew
- **LangChain / LangGraph / LangSmith / LangFlow** — Mentioned by Joh as key skills needed for corporate AI development roles
- **Microsoft AI Foundry / Copilot** — Mentioned by Joh as required for enterprise/corporate AI deployments
- **Lovable / Bolt / V0** — No-code/low-code tools for rapid landing page and UI generation
- **Shadcn** — UI component library; noted as having improved for rapid app scaffolding
- **LiteLLM** — Underlying library CrewAI uses for LLM routing; same model string format applies
- **Puppeteer** — Web driver for taking website screenshots; recommended for website audit tool
- **Browser Use** — Agent-based browser automation tool; discussed as potential alternative to Puppeteer for screenshot capture
- **Hagen (HeyGen?)** — Video generation tool used at hackathon to generate voice-over video from article summaries
- **Pika / Runway** — Video generation tools Asako plans to evaluate and compare
- **Sora (OpenAI)** — Video generation tool; Brandon noted limited real-world utility so far
- **Canva** — Used by Juan to create animated workflow diagrams for YouTube video
- **Instantly** — Outbound email tool with domain warm-up and open/click tracking; recommended for cold outreach campaigns
- **Perplexity** — Compared alongside O3 and Gemini for deep-thinking/research tasks by Paul
- **Gemini 2.0 Flash** — Used at hackathon by Asako; can summarize web pages from URLs natively without a scraper

## links

- **Brandon's Google Gemini use cases repository** — Shared in chat; contains built examples of Gemini agent use cases (URL not captured in transcript)
- **Firecrawl integration links for CrewAI** — Two links shared in chat by Brandon for scraping/search with CrewAI (URLs not captured)
- **Supernis group website** — Global corporate group that includes Trideca (Joh's company); shown on screen with clickable company map (URL not captured)
- **Website audit tool example** — Shared by Philip in chat as inspiration for building an AI-powered website audit/report tool (URL not captured)

## decisions

- **Brandon** will record and publish a YouTube video on five Google Gemini agent use cases by end of the week.
- **Brandon** will send an email this week with a form for community members to indicate if they are looking for work or looking to hire, to facilitate connections.
- **Brandon** will send out full details and announcements about the AI Authority Accelerator program early next week; program kicks off late March/early April.
- **Brandon** will connect Joh Leonhardt with suitable developers in the community once Joh sends over role details via DM.
- **Joh** will send Brandon information about open roles at Trideca/Supernis for community referrals.
- **Paul** will write and post a comparison of deep-thinking models (O3, Gemini, Perplexity) with findings from his testing.
- **Paul** will share his script for merging Python library files into single context files for Google AI Studio.
- **Reuben** will map out his application architecture (pages, models, data flow) and share it with Brandon for feedback before building.
- **Reuben** will send Brandon a message explaining his business goals to determine if the AI Authority Accelerator is a fit.
- **Maksym** will conduct stress testing with ~100 concurrent users on his application before launch.
- **Juan** will revise his YouTube thumbnail to use larger, fewer words of text and send Brandon an updated version.
- **Juan** will send Brandon the video hook/intro script for review before publishing.
- **Bastian** will reach out to Brandon about setting up a landing page/lead magnet for his upcoming CrewAI deployment video.
- **Philip** will build an MVP website audit tool manually (screenshots → GPT-4o → HTML report → PDF) and report back to the group.