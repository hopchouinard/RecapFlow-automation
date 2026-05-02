## general

This was a community coaching call hosted by Brandon Hancock, bringing together a group of AI developers and builders to share project updates, ask technical questions, and discuss the broader AI landscape. The session opened with informal discussion about personal knowledge management tools before moving into structured Q&A and round-robin project updates.

Brandon shared updates on several ShipKit templates he has been building, including one based on Google's Agent Development Kit (ADK), and announced an upcoming video on AI development workflows and task templates. He also shared a GitHub repo containing a task template as a freebie for attendees. A planned interview with the creator of Presentify (a serial indie developer) was announced, with the group invited to submit questions.

The round-robin segment covered a wide range of projects: Ty Wells demonstrated an Agent Hub built in Lovable with Supabase backend and multi-agent orchestration; Bastian Venegas showed a Convex-based app integrating the Limitless AI pendant API; Mitch demonstrated a content management/video generation app; Patrick Chouinard presented a GitHub Copilot-driven pipeline for auto-generating training materials from release notes; Asako shared her work building AWS Strands Agents content; and Paul Miller discussed integrating PipeDrive CRM with N8N and MongoDB. The session closed with a wide-ranging philosophical discussion about AI's trajectory, the window of opportunity for developers, and the concept of post-labor economics.

The group also discussed cost management strategies for AI coding tools, the merits of Convex vs. Supabase, Kimi K2 as a low-cost Claude Code alternative, the OpenAI Operator agent for browser automation, and the sequential thinking MCP server as a way to boost weaker models.

## insights

- Brandon's core workflow heuristic: treat yourself as a manager, not a coder — your job is review, clarify, and approve; never write a line of code yourself.
- Use social media as a testing bed before investing in courses or consulting: if a tweet or YouTube video gets traction, double down; if not, move on.
- Dan Coe's value ladder principle: tweet → YouTube video → small course → consulting, each validated by the previous level's traction.
- For building a personal brand/content strategy, pick one platform (e.g., AWS) and go deep rather than covering all AI tools — specificity creates authority and opens doors.
- Sequential thinking MCP server can elevate a weaker model (e.g., GPT-4o mini) to perform closer to a stronger model (o3) by breaking complex tasks into smaller sub-tasks iteratively.
- Mitch's cost-saving workflow: use Cursor to generate task documents and rules, then send those to Warp (which has more lenient token limits) to execute the actual coding tasks.
- When building multi-agent workflows, test each agent in isolation with fixed inputs/outputs before chaining them — don't single-shot the entire pipeline.
- Kimi K2 can be used as the backend model for Claude Code, reducing costs by approximately 80% compared to using Anthropic directly.
- Brandon's view on ADK: excellent for simple sequential agent handoffs, but still buggy for complex stateful workflows; LangGraph remains the most production-stable option currently.
- Patrick's observation: AI tools like Lovable enable non-engineers to create apps that appear production-ready but aren't — creating a new job category of senior developers who refactor "AI slop" into real production code.
- Brandon's strategic framing: there is a 2–3 year window to capitalize on AI before autonomous systems reduce the need for human labor; the priority is securing capital and building personal brand now.
- Ty's analogy: training yourself like an LLM — consuming knowledge outside your current scope expands what you can build and comprehend.
- Jake's community insight: surrounding yourself with people who have an abundance mindset (willing to share knowledge) is the most effective way to keep pace with rapid AI change.
- For N8N workflows involving long-running jobs, use a job status table in the database (with attempt count, status, error messages) and have the front end poll for updates rather than waiting synchronously.

## qa

**Q (Tom Welsh):** Can you explain more about using Gemini CLI plus Cursor together — it looked like you could use Cursor to interrogate Gemini CLI?
**A (Brandon Hancock):** The main limitation of Cursor was a three-tab parallel limit. The workaround was opening Gemini CLI or Claude Code in the terminal alongside Cursor to run five or six tasks in parallel, making you more of a manager than a coder. Now that Cursor has raised its tab limit, the terminal approach is less necessary unless Cursor has issues.

**Q (Paul Miller):** Have you played with Opal yet?
**A (Brandon Hancock / Paul Miller):** Brandon had not tried it yet. Paul described it as a tool where you give it a task and it maps out how to set up an agentic flow to deliver it without code — it shows the prompts it creates as you build. It requires a personal (not business) Google account and currently requires a US VPN to access.

**Q (AbdulShakur Abdullah):** Why did you make the School community free?
**A (Brandon Hancock):** It was a long-term relationship play — the $99 cost has paid for itself many times over in connections and opportunities. For anyone wanting to build a paid community, the real bottleneck is top-of-funnel attention, not the community itself. Getting eyeballs (via YouTube, LinkedIn, etc.) is the hardest and most important skill first.

**Q (AbdulShakur Abdullah):** How is the ADK template different from Greg Eisenberg's idea validator?
**A (Brandon Hancock):** The idea validator concept is not the core value — the value is that it's a copy-and-paste ADK clone showing how to use the framework, with a multi-agent system fully set up and a real-time timeline showing what each agent is doing.

**Q (Jake Maymar):** What are your thoughts on Convex?
**A (Bastian Venegas / Brandon Hancock):** Convex simplifies the React backend by making everything real-time and type-safe — state changes appear instantly without page refreshes, and all database logic lives in a dedicated convex folder using TypeScript. It's similar to Supabase but with a different developer experience. Brandon noted it lacks a blob store (or has limited file storage), which was a blocker for him previously, though Bastian showed it does have a file storage section in the dashboard.

**Q (Juan Torres):** Has anyone used Kimi K2?
**A (Brandon Hancock / Paul Miller):** Brandon had not used it in production but heard strong praise from Maxim, who used it for voice agent decision-making as the only open-source model fast enough and smart enough to match Claude or OpenAI. Paul confirmed you can point Claude Code at a Kimi K2 host instead of Anthropic, reducing costs by roughly 80%.

**Q (Gopal Seshadri):** I'm getting HTTP 500 errors deploying a flow to CrewAI Enterprise, and the inputs endpoint returns an empty array.
**A (Brandon Hancock):** The empty inputs array suggests the crew is not configured properly to expose its required inputs. The usual culprits are incorrect project folder structure or silent failures during deployment where a key is expected but not provided. Brandon reviewed the code live and identified that hard-coded inputs in the main file may not be properly declared to CrewAI Enterprise's API. Bastian also suggested checking the YAML config file. Brandon offered to connect Gopal with someone on the CrewAI team.

**Q (Marc Juretus):** Should I keep building with LangChain/LangGraph or invest time in ADK now?
**A (Brandon Hancock):** For production stability, LangGraph is the best option right now. ADK has the best developer experience and is excellent for simple sequential agent handoffs, but is still buggy for complex stateful workflows. Brandon expects ADK to be the go-to option in about two months as they continue improving it.

**Q (Jake Maymar):** Is Notion hard to read complex documents in, or am I using it wrong?
**A (Brandon Hancock):** Mostly a power-user issue. Key shortcuts: Command+Enter opens a page full screen, Command+Backslash closes the sidebar, Command+Left Bracket goes back, and Command+P searches everything. Using collapsible H1 sections also helps manage long documents. Mitch added that downloading the desktop app (rather than using the browser) enables additional customization.

**Q (Ty Wells):** Where are we relative to the rest of the world in terms of AI adoption and capability?
**A (Brandon Hancock / Jake Maymar / Tom Welsh / Patrick Chouinard):** The group consensus was that they are cutting-edge but not bleeding-edge. Most chief AI officers being hired at major institutions are old-school CTOs, not actual AI practitioners — meaning the group has a real practical advantage. Patrick noted that tools like Lovable are enabling non-engineers to create apps that look production-ready but aren't, creating demand for skilled developers to fix "AI slop." Brandon framed it as a 2–3 year window to capitalize before AI autonomy reduces the need for human labor.

## tools

- **Limitless AI pendant** — Bastian building an app that fetches transcriptions and extracts to-dos/reminders via the Limitless API
- **Convex** — Bastian demonstrated it as a real-time, type-safe React backend alternative to Supabase; getting significant traction via Theo's YouTube channel
- **Chef (by Convex)** — Convex's own scaffolding tool, similar to Lovable, for bootstrapping Convex-based apps
- **Otter.ai** — Mentioned by AbdulShakur as a voice/meeting recording tool with AI features for action items and search
- **Noda app** — AbdulShakur's current recording tool, acquired via lifetime deal as an Otter alternative
- **Airtable** — Ty using it as a database for voice-captured notes via Siri shortcut
- **Obsidian** — Mentioned as a second-brain/note-taking tool; Jake referenced a plugin ecosystem for it
- **Notion** — Brandon and Brandon Hancock's go-to second brain; Brandon walked Jake through keyboard shortcuts and database usage
- **AppSumo** — Mentioned as a source of lifetime software deals; group noted AI has reduced the appeal of such deals
- **Google ADK (Agent Development Kit)** — Brandon building ShipKit templates around it; demonstrated multi-agent system with real-time timeline
- **Gemini CLI** — Used as a parallel coding terminal alongside Cursor to run multiple tasks simultaneously
- **Claude Code** — Discussed as an alternative to Cursor; requires $200/month plan for unlimited use; Bastian shared `/cost` command to check session costs
- **Cursor** — Primary AI coding IDE for most participants; Brandon spending ~$220/month; raised parallel tab limit recently
- **Warp** — Terminal tool with AI agent mode; Mitch using it to run coding tasks with more lenient token limits than Cursor
- **Kiro (Amazon)** — Amazon's new AI coding tool with spec/rules system; Mitch finding it effective; Asako on waitlist
- **Kimi K2** — Chinese open-source model; Juan using it free via web; Paul using it as Claude Code backend at ~80% cost reduction vs Anthropic
- **Base10.co** — Platform Maxim used to host Kimi K2 for voice agent inference; requires ~10 H100s
- **OpenAI Operator** — Browser automation agent; Ty demonstrated using it to research fishing gear and build a shopping cart on Shields.com
- **Opal (Google)** — New Google tool for building agentic workflows without code via natural language; requires personal Google account and US VPN
- **N8N** — Workflow automation platform; Paul using it with PipeDrive; group discussed upcoming natural language workflow-building feature
- **LangChain / LangGraph** — Marc using LangChain for fantasy football agents; Brandon recommending LangGraph for production agentic workflows
- **CrewAI Enterprise** — Gopal troubleshooting HTTP 500 deployment errors; Brandon and Bastian helped diagnose
- **Strands Agents (AWS)** — Asako building content around it; described as simpler than LangChain/CrewAI with just system prompt + tools + model
- **Lovable** — No-code/vibe-coding platform; Ty building Agent Hub and a mobile app entirely within it; Mitch using it for front-end
- **Supabase** — Used by Ty for storage, relational database, and auth in his Lovable app
- **PipeDrive** — Paul's CRM; integrating with N8N and MongoDB for AI-enhanced sales workflows
- **MongoDB** — Paul using it as a parallel data store for CRM analysis workflows
- **GitHub Copilot** — Patrick building entire training generation pipeline using Copilot agent mode with MCP servers
- **Perplexity MCP** — Patrick using it within GitHub Copilot for web research in his training generation workflow
- **Sequential Thinking MCP server** — Jake recommending it as a way to make weaker models perform like stronger ones by breaking tasks into sub-tasks
- **Context7 MCP** — Brandon using it in Cursor as one of his two primary MCP servers
- **Time MCP server** — Brandon using it to give Cursor accurate current time for web searches and task logging
- **Docker Models** — Jake mentioned Docker releasing an Ollama-like feature for running local models inside Docker containers
- **Presentify** — Screen annotation/pointer tool; Brandon arranging an interview with its creator for the YouTube channel
- **AgentOps** — Bastian referenced their framework translation tool for scaffolding agentic workflows across different frameworks
- **Pydantic** — Brandon recommended using Pydantic validation in LangChain structured outputs to enforce output format via regex or field constraints
- **Drizzle ORM** — Referenced in context of Convex's TypeScript schema feeling similar to Drizzle
- **PlanetScale** — Mentioned as infrastructure underlying Convex
- **Thomas Frank (YouTube)** — Brandon recommended his Notion crash course for learning databases and second brain setup
- **David Shapiro (YouTube)** — Brandon recommended his channel on post-labor economics and AI's societal impact

## links

- Brandon's GitHub repo with task template (shared in chat, available for ~24 hours from call date) — free task template for Next.js/full-stack AI projects
- Theo's YouTube video on Convex — Brandon shared in chat; Theo going "all in" on Convex recently
- Kimi K2 web interface (kimi.ai or similar) — Juan shared link in chat for free access to Kimi K2 model
- Base10.co — Platform for hosting Kimi K2 via API; shared by Brandon
- Claude Code cost tracking CLI tool — Patrick shared a link in chat; install and run `/cost` to see token usage by model and session
- Thomas Frank Notion crash course YouTube video — Brandon shared in chat for learning Notion second brain setup
- AI 2027 YouTube video — Brandon shared in chat; narrated walkthrough of the AI 2027 paper on superintelligence timeline
- AgentOps framework translation repo — Bastian shared in chat; maps equivalent components across agentic frameworks (CrewAI, LangGraph, Claude Code, etc.)
- Asako's blog post on multi-agents with Strands Agents — shared in chat
- Asako's LinkedIn post on A2A with Strands Agents — shared in chat

## decisions

- Brandon will record a video tomorrow on task templates and AI development workflows (targeting Thursday release)
- Brandon will record a video on the ADK ShipKit template once a remaining bug is fixed
- Brandon will conduct a one-on-one interview with the creator of Presentify this weekend and publish it on YouTube
- Brandon will post a poll in the School community after the call for members to submit questions for the Presentify creator interview
- Brandon will post the call recording to School after walking his dogs
- Brandon will reach out to Cursor about an affiliate or sponsorship arrangement given his high usage and community influence
- Brandon will try OpenAI Operator during his upcoming vacation to St. John's and report back
- Brandon will look into the Claude Code $200/month plan based on Jake's recommendation about Swarms usage
- Gopal Seshadri will DM Brandon on School with his email so Brandon can connect him with someone on the CrewAI team
- Marc Juretus will explore Docker MCP containers and Notion for organizing his generated markdown files
- Marc Juretus will build 10 apps using LangChain/LangGraph to build his portfolio before revisiting ADK
- Asako will continue building AWS Strands Agents content and consider starting a YouTube channel in addition to blog posts
- Paul Miller will DM Brandon about Kiro
- Patrick Chouinard will test CrewAI and/or ADK as the next phase for his training generation pipeline after finalizing prompts in GitHub Copilot
- Patrick Chouinard will continue building his agentic framework translation matrix (Rosetta Stone across CrewAI, LangGraph, Claude Code, GitHub Copilot, Gemini CLI)
- Mitch will add a theme reference page to his Lovable project setup process
- Brandon will add cursor rules to the GitHub task template repo soon