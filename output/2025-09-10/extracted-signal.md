## general

This was a group coaching/community call hosted by Brandon Hancock, centered on members sharing project updates and getting technical feedback. The session opened with Brandon demoing ShipKit, his AI application starter kit, which includes a RAG template, a course platform built on top of that template, and a roadmap-driven development workflow. He explained that ShipKit generates phase-by-phase roadmaps to guide users from blank templates to real-world applications, and that walkthroughs are being recorded to show the full process including errors and recovery.

The bulk of the call was a round-robin of member updates. Topics ranged from building a robotic process agent to automate a 75-page government trucking registration form (David), to deploying a full AWS infrastructure with GPU instances for a private LLM and RAG system (Juan), to building a food ordering platform for Bahamian restaurants (Ty), to creating a 3D product scanning pipeline for supermarket shelf analysis (Paul). Several members also discussed AI news, tooling preferences, and presentation strategies for non-technical audiences.

Secondary threads included a discussion of Cursor's recent slowdowns and cost management, the tradeoffs between local and cloud-hosted embedding models, MCP server recommendations, and how to merge context across multiple AI chat sessions. Patrick shared his experience using GitHub's SpecKit to scaffold a NotebookLM-style podcast generator in about three hours. Mitch discussed B2B lead generation for a leather eyepatch business and a potential media/AI services opportunity from a conference connection.

The call closed with Brandon noting he needed to record more ShipKit course content and would send outstanding documents to Alex after the call.

## insights

- **Context is the bottleneck, not the model**: Brandon repeatedly emphasized that AI can solve almost any problem if given sufficient, well-structured context. Poor results usually trace back to insufficient context, not model capability.
- **Separate concerns in browser/RPA agents**: When building agents that interact with web pages, splitting tasks across multiple agents (one to read the page, one to find elements, one to enter data and submit) prevents context window exhaustion and erratic behavior.
- **Cold boot vs. warm boot tradeoff**: Scaling GPU instances to zero saves significant cost when idle, but the first request after idle can take 3–5 minutes to process. Teams must decide whether their users can tolerate that latency.
- **Open-source embeddings work locally but complicate cloud deployment**: Running open-source embedding models locally is straightforward, but deploying to the cloud requires solving scaling, queuing, and infrastructure questions that vendor APIs handle automatically.
- **Google Gemini is currently the only option for multi-modal (image/video) embeddings**: If a RAG application needs to embed images or video, Gemini is the only viable choice at this time; OpenAI only supports text-based embeddings well.
- **Cursor rules: automatic vs. manual application is a cost/quality tradeoff**: Explicitly setting rules produces higher-quality code but inflates the context window and increases billing; "apply intelligently" is cheaper but less consistent.
- **For non-technical AI audiences, frame the AI as a brilliant intern with zero context** (Patrick): Ask what you'd tell a new hire to get something done—that framing unlocks practical prompting behavior even for people who have never used AI tools.
- **"Put a lot in, expect a little back"** (Andrew): If you give the AI rich, detailed input and expect modest output, you'll usually be satisfied. Expecting a lot from minimal input leads to disappointment.
- **Topological sorting / queues can replace AI for deterministic sequencing problems**: For logistics problems with clear dependencies (e.g., school pickup sequencing), classical data structures may be simpler and more reliable than AI.
- **Vendor lock-in is acceptable while learning**: Brandon advised that being locked to OpenAI or Gemini for embeddings is fine while building and learning; switching to open-source can come later when infrastructure expertise is in place.
- **ShipKit's prep templates work best inside an existing project**: The prep workflow is designed to analyze an existing codebase; starting from a blank folder works but loses some of the contextual benefit.
- **ADK state management drives cost**: Passing large amounts of state into every ADK conversation cycle is the primary driver of unexpectedly high Gemini API bills; keeping agents single-purpose and prompts concise reduces cost significantly.

## qa

**Q (David):** I'm building an RPA agent to fill out a 75-page dynamic government form. I've recreated a mock of the site for testing. How do I handle the human-in-the-loop parts (e.g., QR code scanning, photo capture) in a testing environment, and how do I score and train the agent on its output?

**A (Brandon):** Use Google's Agent Development Kit (ADK) with a loop agent architecture. One agent reviews the page and determines answers; a second browser agent (using Selenium as a web driver) finds the HTML element IDs; a third agent enters the data and submits. Breaking it into three agents prevents context window exhaustion. Start with the mock environment, then switch to the real site. The ADK GitHub repo linked to a Google YouTube video shows how to wire Selenium as a tool.

---

**Q (Juan):** When creating a browser agent, do you build it through ADK or use an external tool?

**A (Brandon):** The "browser agent" is just an ADK agent that has browser-control tools (scrape page, click button, find element, take screenshot) backed by a Selenium instance that's already authenticated. The ADK GitHub repository has these tools pre-built. The key is keeping each agent's responsibility narrow to avoid hitting context limits.

---

**Q (Hemal):** Gemini Flash seems much more expensive than GPT-4o Mini for my data reconciliation project. Is there a cheaper alternative within ADK?

**A (Brandon):** Gemini 2.5 Flash is actually one of the lower-cost models comparatively; the difference you're seeing is likely because GPT-4o Mini is extremely cheap rather than Flash being expensive. If cost is still a concern, try Gemini 2.5 Flash Lite for maximum speed at lowest cost. Also, review how much data you're passing into state each cycle—large state is the main cost driver in ADK.

---

**Q (James):** I'm trying to add the Context7 MCP server to Gemini CLI but keep getting errors even though `mcp list` finds it. What's wrong?

**A (Brandon):** You likely have unnecessary headers in your JSON config (lines 5–8 in the example shown). Context7 doesn't require an API key or headers to function. Remove those lines and the trailing comma, save, and refresh. Context7 is free to use without authentication.

---

**Q (James):** How do people combine context from multiple AI chat sessions when working on a project?

**A (Brandon):** There's no merge button. The workaround is to ask each chat to export everything discussed "in maximum detail so another engineer has full context," save that as a markdown file in an AI docs/scratch folder, then open a new session and feed it both files. James had independently arrived at the same solution by creating dated "learnings" files.

---

**Q (Andrew):** I'm giving a presentation on AI to a non-technical audience. What topics should I make sure to cover?

**A (Brandon):** Focus on building prompt templates as SOPs—show how a single well-crafted prompt can replace a repeatable work task and be handed to any employee. Patrick added: frame the AI as the smartest intern who just started and has zero context; ask what you'd tell that intern, and remember the intern's superpower is that it will tell you what it doesn't know if you ask. Paul added: help people choose the right model first—many people have bad AI experiences because they're using a free or outdated chatbot.

---

**Q (Morgan):** Besides Context7, Git, and Supabase, what MCP servers are people using?

**A (Brandon):** The time MCP server is heavily used because AI handles time poorly natively. Sequential thinking MCP (forces chain-of-thought reasoning) is valuable for complex problems but burns context quickly. For larger teams, Slack and Linear MCPs would be useful additions.

---

**Q (Alex):** I've been using the ShipKit AI docs folder outside of a project to build from scratch using the prep templates. Is that the right approach?

**A (Brandon):** The prep templates are designed to work best inside an existing ShipKit template project because they analyze the existing codebase to understand capabilities. However, Alex's approach of using prep to build from scratch is working, which is good news. Going forward, the intended flow is: run `shipkit-ai [project-name]`, which scaffolds a working template with AI docs already included, then run through prep templates 01–09 to generate the roadmap, then build phase by phase.

## tools

- **ShipKit** – Brandon's AI application starter kit with RAG, chat, and ADK templates plus roadmap-driven development workflow; main product being demoed and built throughout the call.
- **Google Agent Development Kit (ADK)** – Used for building multi-agent workflows; recommended for the RPA browser agent and data reconciliation projects.
- **Selenium** – Recommended as the web driver for the browser agent inside ADK to control and interact with web pages.
- **Cursor** – Primary IDE used by most members; noted to have become significantly slower recently and to have high API costs when rules are applied explicitly.
- **Claude Code** – Used by Andrew for local AI coding tasks; noted to have had degraded performance over the past six weeks.
- **Gemini CLI** – Google's open-source CLI tool; James was trying to add MCP servers to it; noted to require Gemini 2.5 Pro for consistent results.
- **Context7 MCP** – MCP server for up-to-date library documentation; James was troubleshooting its integration with Gemini CLI.
- **Sequential Thinking MCP** – Forces chain-of-thought reasoning in agents; useful for complex problems but consumes context window quickly.
- **Time MCP** – MCP server that gives AI accurate time awareness; Brandon uses it heavily daily.
- **Google ADK Web** – Browser-based UI for ADK; Hemal praised its out-of-box file upload and chat capabilities as a potential production UI.
- **Gemini 2.5 Flash / Flash Lite** – Google's cost-efficient models; recommended for ADK projects where cost is a concern.
- **Beautiful Soup** – Mentioned as a Python web scraping library in the context of the government RPA project.
- **AWS EC2 with A10 GPU** – Juan is deploying a 7B/20B parameter model on this instance for a client RAG application.
- **AWS Elastic Beanstalk** – Used by Juan's client for deploying the front-end application.
- **AWS RDS with pgvector** – PostgreSQL with vector extension used for RAG retrieval in Juan's AWS deployment.
- **AWS Activate** – Startup program offering $1,000+ in AWS credits; Juan's client saved $1,000 by applying.
- **Infracost (AWS pricing tool)** – Tool Juan shared for estimating EC2, RDS, and Elastic Beanstalk costs before committing.
- **RoboFlow** – Used by Paul's company for training computer vision models for shelf analysis; noted to require heavy manual training.
- **YOLO model** – Computer vision model Paul's team is building an advanced version of for product shelf placement detection.
- **Apple Reality Kit / Photogrammetry** – Apple library used by Paul to convert product photos into 3D objects for augmented reality.
- **Gaussian Splats** – 3D capture technique mentioned by Jake for creating walkable 3D environments and motion capture.
- **HeyGen** – AI avatar platform; noted to lack real-time emotion but useful for pre-rendered video with controlled speech.
- **Unreal Engine** – Used by some creators to build real-time AI avatar "puppets" for YouTube channels.
- **Bolt** – Low-code AI app builder; mentioned in context of a previous painful hackathon experience; Ty noted it now integrates Claude Code CLI, Gemini CLI, and Codex.
- **GitHub SpecKit** – GitHub's spec-based project planning tool; Patrick used it with Claude Code to scaffold a podcast generator in ~3 hours.
- **NotebookLM** – Google's podcast/audio generation tool; Patrick built his own alternative because NotebookLM has no API.
- **Instantly** – Cold email outreach platform used by Mitch for B2B lead generation for his eyepatch business.
- **Apify** – Web scraping tool used by Mitch to build lead lists.
- **LinkUp** – Deep research tool used for personalizing cold outreach emails with reverse person research.
- **n8n (NADN)** – Workflow automation platform; Mitch built automation workflows with it; Brandon noted it as a complement/alternative to ADK for pure automation use cases.
- **Shopify** – Mitch set up a storefront for his leather eyepatch business.
- **Futurpedia** – AI news resource mentioned by a member as a recommendation for staying current.
- **Matt Wolfe (YouTube)** – AI news YouTube channel recommended by Brandon for staying current.
- **Theo (YouTube)** – Developer-focused YouTube channel recommended by Brandon; posts daily.
- **Lenny's Newsletter** – AI/product newsletter mentioned by Hemal as a resource they already use.
- **Fabric** – Open-source AI tool; Patrick identified Daniel Miessler as its creator when recommending his YouTube video.
- **Pydantic** – Python library mentioned by Brandon for building pure automation pipelines without full agent frameworks.
- **Beware Toga** – Python GUI library recommended by Andrew for building simple local desktop interfaces; noted to use native widgets and work well with LLM-generated code.
- **Google LangExtract** – Project Andrew mentioned for language extraction tasks requiring large context windows.
- **CliftonStrengths** – Personality assessment framework; Mitch demonstrated using ChatGPT to analyze strengths, blind spots, and team dynamics from assessment results.
- **Twilio** – Implied SMS platform; Ty mentioned using his own SMS server instead due to non-local number costs in the Bahamas.

## links

- **Google ADK GitHub repository** – Referenced for browser agent tool examples (scrape page, click button, find element, take screenshot) and Selenium integration; Brandon sent it in chat but URL not captured verbatim.
- **Google YouTube video on ADK browser agent setup** – Linked by Brandon in chat to help David with the RPA browser agent architecture; URL not captured verbatim.
- **AWS Activate startup credits program** – Juan shared the link; allows startups to apply for $1,000+ in AWS credits. URL not captured verbatim.
- **AWS/cloud instance cost estimation tool** – Juan shared a link to a tool for pricing EC2, RDS, and Elastic Beanstalk instances. URL not captured verbatim.
- **Beware Toga Python GUI library** – Andrew said he would drop the link in chat; a Python-native GUI framework. URL not captured verbatim.
- **Context7 MCP server documentation** – Brandon pulled up the official setup page during the call to help James troubleshoot JSON configuration. URL not captured verbatim.
- **OpenAI RAG white paper** – Jake shared a link about OpenAI's new model training approach intended to reduce hallucinations; too many tabs made it slow to retrieve. URL not captured verbatim.
- **Daniel Miessler YouTube video on building an AI assistant with Claude Code** – Patrick shared the link; Miessler is also the creator of the Fabric tool. URL not captured verbatim.
- **"AI Life Copilot" YouTube video** – Paul shared a link to a video of someone using Claude Code to manage their entire business life rather than to write software. URL not captured verbatim.
- **"AI Engineering Bible" (Kindle Unlimited)** – Brandon mentioned this free/Kindle Unlimited book as a cheaper alternative to the Chip Huyen AI Engineering book Juan referenced. URL not captured verbatim.
- **ADK context compression documentation** – Tom shared a Perplexity-sourced link in chat suggesting ADK does support context compression; shared for James's question. URL not captured verbatim.
- **Unreal Engine AI avatar example** – Jake shared a link demonstrating real-time AI puppet/avatar creation in Unreal Engine. URL not captured verbatim.
- **Clearly.ai avatar example** – Juan shared a link to an avatar demonstration. URL not captured verbatim.

## decisions

- **Brandon** will send the RAG walkthrough video to the group tonight after the call.
- **Brandon** will send outstanding ShipKit documents to Alex after his next call.
- **Brandon** will add a pure-automation (background worker / Pydantic pipeline) template to ShipKit, inspired by Mitch's n8n workflow use case.
- **Brandon** will hop on a call with Mitch to go deeper into the n8n-to-application conversion workflow.
- **David** will use the ADK browser agent architecture with Selenium, starting on the mock URS environment, then switching to the real FMCSA site.
- **David** will share project updates the following week.
- **James** will remove the headers and trailing comma from his Context7 MCP JSON config in Gemini CLI and test whether it resolves the errors.
- **Patrick** will share information about Claude for Financial Services with the group once he has details (within legal limits).
- **Jake** will connect with Paul offline to share 3D asset creation techniques relevant to Paul's product scanning pipeline.
- **Jake** will reach out to Brandon via email with specifics on the full-stack developer role he is looking to fill.
- **Mitch** will meet with the ex-head of media for Valuetainment and his business partner the following day to explore an AI media services opportunity.
- **Mitch** will report back to the group on how the B2B eyepatch email campaign and the new client conversation develop.
- **Members** are encouraged to experiment with Cursor's automatic vs. manual rule application over the next week and report back their preference.
- **Ty** will keep the group updated on restaurant onboarding and revenue progress for his Bahamian food ordering platform.