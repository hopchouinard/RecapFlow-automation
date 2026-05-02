## general

This was a group coaching call hosted by Brandon Hancock, with roughly a dozen participants sharing project updates in round-robin format. The session opened with Brandon announcing the launch of his "AI Authority Accelerator" program, which he built using Lovable and Cursor, and noted six of twenty slots had been filled. The call then moved through individual updates covering a wide range of AI-enabled projects and business development topics.

Participants demonstrated or discussed: an executive assessment web app (Jake Maymar), a psychiatric report generation workflow (Andrew Nanton), a post-learning survey analytics tool called Lens (Patrick Hutchinson), an AI companion for small business owners (Asako and Aaron/The Dharma House), a lead qualification pipeline using Perplexity's Sonar API (Paul Miller), a sales training tool for a Latin American car dealership group built in Flutter (Maksym Liamin), a Telegram-to-Jira automation via N8N (Steve), and a deep-research article generator using Perplexity (Tom Welsh). Brandon also briefly highlighted OpenAI's newly released production agents feature at the end of the call.

Brandon provided go-to-market coaching throughout, emphasizing niche focus, ICP definition, building authority through public demos, and the "divide and conquer" pattern for LLM-based document generation. Cyril shared a positive job interview experience and received advice on preparing for a technical coding interview.

## insights

- **Brandon on Lovable:** Building a full landing page in Lovable took ~3 hours vs. a full week with a traditional UX/UI designer iterating on mockups — the tool lets you rapidly cycle through design options (A/B/C) in minutes, posing a major threat to UI/UX design roles.
- **Jake on client engagement:** Shipping a POC immediately rather than going through Figma mockups gets clients "skin in the game" faster, accelerates feedback loops, and creates excitement that drives feature requests and referrals.
- **Brandon on divide-and-conquer LLM pattern:** For long-form report generation, splitting the output structure into isolated per-section prompts (each focused on one chunk) produces better results than asking one prompt to generate everything — then rejoin all sections at the end.
- **Andrew on LLM model selection:** Claude 3.5 is "rock solid" for coding tasks; Claude 3.7 had some issues for Jake. Cheaper models (o1-mini, o3-mini) are worth trying for simple fixes to preserve credits.
- **Andrew on non-technical audiences:** Most non-technical professionals only know ChatGPT and use it like Google. The fastest way to engage them is to ask "what are the most tedious parts of your day?" — mundane tasks are often the best AI fit and immediately surface pain points.
- **Brandon on positioning:** "If you're everything to everyone, you're almost nothing." Picking a specific niche and solving their concrete problems publicly creates a flywheel — showcased solutions attract similar customers organically.
- **Bastian on spotting automation opportunities:** Look for "export buttons" in any software a business uses — they signal workflow breaks where data must be manually carried between tools, which are prime automation targets.
- **Paul on lead qualification:** Using Perplexity's Sonar Pro API to pre-qualify a pool of ~2,000 companies cost approximately $10 USD — far cheaper than building a full agent pipeline, and it surfaces LinkedIn and job-site data without direct scraping.
- **Brandon on sales vs. operations:** Automations closer to revenue generation (leads, sales) command higher fees than operational cost-cutting automations — prioritize accordingly when pitching clients.
- **Brandon on agent design:** Agents need a "human-in-the-loop inbox" — the agent does as much as possible, then requests human approval before sending, rather than acting fully autonomously. LangChain's Agent Inbox was cited as a reference implementation.
- **Brandon on cold outreach:** Instantly.ai has strong AI integrations and recent YouTube tutorials that make cold email outreach look "like cheating" in terms of ease and results.
- **Brandon on whiteboard interviews:** Talk through your thinking out loud during technical interviews — interviewers care more about reasoning process than a correct answer. Using precise OOP vocabulary (abstract class, concrete class, interface) signals real engineering fluency.

## qa

**Q (Sagar):** How does using AI tools and wrapping them together work on the production side?
**A (Jake):** Build a POC first to validate direction and save time. Once core features are stable and the client is happy, then move to proper scalable architecture. The POC approach keeps clients engaged and invested early.

**Q (Brandon):** What models are people using in Windsurf, and is Cascade Base worth trusting?
**A (Jake/Andrew):** Both primarily use Claude — Jake prefers 3.5 as "rock solid," Andrew sticks with 3.7 for his report generation work. Cheaper o1/o3-mini models are worth trying for simple fixes. Neither has fully trusted Cascade Base yet.

**Q (Andrew):** Is the divide-and-conquer report generation pattern unique to his work, or is it a recognized pattern?
**A (Brandon):** It's a recognized pattern — "divide, conquer, rejoin." Brandon referenced a CrewAI example where a book outline is split into chapters, each generated independently, then rejoined. LangChain's markdown header text splitter can help automate the splitting step.

**Q (Sagar):** How should a software agency that does "anything and everything" with AI create meaningful social media content?
**A (Brandon):** Pick a specific niche first. Generic posts about tools like MCP are meaningless to most audiences. Document real solutions you build for real clients and share them publicly — outcome-driven content for a specific audience acts as a magnet for similar clients.

**Q (Patrick):** What kind of data comes out of School.so webhooks, and would anyone be willing to test integrations?
**A (Brandon):** School's webhooks are very limited — Brandon gave it a "B minus" for course features overall (no per-module comments, limited API). He switched to Mighty Networks for his new program, which has more integrations and allows per-lesson comments.

**Q (Jake):** What was the pricing/cost structure for the Perplexity Sonar API lead qualification workflow?
**A (Paul):** Processing ~2,000 companies cost approximately $10 USD using the Sonar (non-Pro) tier. Sonar Pro allows up to 150 calls per minute for deeper enrichment.

**Q (Cyril):** What advice do you have for a junior developer technical interview?
**A (Brandon):** Focus on OOP vocabulary (abstract class, concrete class, interface) to signal real engineering knowledge. Practice easy-to-medium LeetCode-style problems using AlgoExpert (Clement's course). Most importantly, talk through your thinking out loud — interviewers want to see your reasoning process, not just a correct answer.

**Q (Brandon):** For Steve's Telegram/Jira automation, what's the best way to start getting clients and building authority?
**A (Brandon):** Use your warm network first — offer to build automations for free or low cost to build a portfolio. Post demos on LinkedIn with the N8N template as a lead magnet. Each completed automation makes the next one easier to sell, and you can charge progressively more as you accumulate proof.

## tools

- **Lovable** — Used by Brandon to build the AI Authority Accelerator landing page in ~3 hours; also used by Jake for UI components and animations in his assessment app
- **Cursor** — Used by Patrick to build a services overview page in ~6 minutes; discussed as a potential markdown/document editor for LLM-driven report generation
- **Windsurf** — Discussed by Andrew and Jake as their primary coding IDE; question raised about which AI models to use within it
- **Claude 3.5 / 3.7 (Anthropic)** — Primary LLM used by Jake and Andrew for coding tasks in Windsurf/Cursor
- **Supabase** — Backend database used by Jake for his assessment app
- **Next.js AI SDK** — Used by Jake to handle AI response generation (GPT-4o Mini) in the assessment app
- **GPT-4o Mini** — The model Jake used for generating improvement suggestions in his assessment app
- **Tavus** — AI avatar/video interview tool integrated by Patrick to turn surveys into conversational AI interviews via webhooks
- **LangChain (markdown header text splitter)** — Mentioned by Andrew as a tool for splitting markdown documents by header for chunked LLM processing
- **CrewAI** — Referenced by Brandon for divide-and-conquer document generation workflows; noted upcoming MCP tool support
- **Perplexity Sonar / Sonar Pro API** — Used by Paul to enrich and pre-qualify a list of ~2,000 B2B leads at very low cost (~$10)
- **LinkedIn Sales Navigator** — Used by Paul to build the initial pool of target companies and contacts
- **ABoot** — Tool Paul used to extract LinkedIn data using his Sales Navigator credentials
- **MongoDB** — Database Paul used to store and process the lead list before Perplexity enrichment
- **Pipedrive** — CRM used by Paul's SaaS company to manage the sales funnel
- **Apollo** — Mentioned by Paul as an alternative lead enrichment tool he evaluated but did not use
- **Firecrawl** — Mentioned by Paul as having a new LLM-style site crawl API, but noted it's experimental and cost is unclear
- **Instantly.ai** — Recommended by Brandon for AI-powered cold email outreach; described as having strong AI integrations
- **N8N** — Automation platform used by Steve to build the Telegram-to-Jira workflow
- **Telegram** — Chat interface used by Steve as the front end for his project manager automation bot
- **Jira** — Task management system Steve's automation connects to for issue creation and assignment
- **Mighty Networks** — Course platform Brandon switched to for AI Authority Accelerator; noted better integrations and per-lesson comments vs. School.so
- **School.so** — Previous course platform Brandon used; noted limited webhooks and no per-module comment support
- **HubSpot** — Mentioned by Brandon as the typical CRM for tech startups, suggested as a key integration target for the AI companion product
- **Slack / Notion / Gmail** — Mentioned by Brandon as the core integration targets for a startup-focused AI executive assistant
- **Linear / Monday / Asana** — Mentioned by Brandon as task management tools to integrate depending on whether the startup is software-focused or not
- **Superhuman** — Mentioned by Bastian as a possible tool Cursor uses for AI-assisted email responses
- **LangChain Agent Inbox** — Referenced by Brandon as a reference implementation for human-in-the-loop agent email workflows
- **OpenAI Agents (new release)** — Briefly demonstrated by Brandon; described as a simplified production agent framework with web search, document search, and computer use capabilities
- **AlgoExpert** — Recommended by Brandon and Bastian for Cyril to prepare for technical coding interviews; noted a current discount
- **Screen Studio** — Recommended by Brandon as a Mac tool for recording clean demo videos with auto-zoom for LinkedIn posts
- **MCP (Model Context Protocol)** — Discussed by Sagar, Bastian, and Jake as an emerging standard; Bastian noted it can run locally without a hosted server; CrewAI support coming soon
- **Manus** — Mentioned by Brandon as a new AI tool he applied for access to; invited group members to share access if they get it first
- **Flutter** — Used by Maksym to build the car dealership sales training app; noted it ran smoothly on launch day with 500 users

## links

- No explicit URLs were shared in the transcript text (Brandon mentioned dropping links in chat for the AI Authority Accelerator website, Instantly.ai YouTube videos, and the new OpenAI agents release, but the actual URLs were not captured in the transcript)

## decisions

- **Brandon** will stop sending daily launch emails for AI Authority Accelerator after the current push and return to a normal cadence of roughly one email every other week
- **Brandon** will get a new monitor and commit to using his standing desk (per chiropractor's orders, agreed on-call)
- **Bastian** will send Andrew information about a draft-writing or pre-processing tool relevant to his report generation workflow
- **Jake** will continue refining the assessment app and work toward making it a white-label executive tool for resale
- **Patrick** will continue conversations with course creators to validate assumptions using a Mom Test approach, focusing on testimonials and pulse-check features
- **Asako and Aaron (The Dharma House)** will target tech-enabled startups as their ICP, prioritizing Slack, Notion, Gmail, and HubSpot integrations, and focus initial value proposition on reducing executive email time
- **Aaron (The Dharma House)** will fix the remaining bug in the RAG/graph backend and aims to have a functional front-end and back-end demo ready by end of the week
- **Paul** will review the Instantly.ai YouTube videos Brandon shared for cold email outreach strategy
- **Maksym** will explore look-alike markets beyond automotive (e.g., high-ticket manufacturing/engineering sales) using ChatGPT to identify opportunities
- **Cyril** will purchase AlgoExpert (currently discounted) and practice easy-to-medium algorithm problems before his technical interview; Brandon will send over additional Python/whiteboard resources
- **Steve** will post his Telegram/Jira automation demo on LinkedIn with the N8N template as a lead magnet, and will use his warm network to find initial clients willing to have automations built for free or low cost
- **Brandon** will share the OpenAI agents release video link with the group