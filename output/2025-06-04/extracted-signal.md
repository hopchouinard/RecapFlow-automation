## general

This was a group coaching call hosted by Brandon Hancock, structured as a round-robin where participants shared project updates, wins, and problems for group feedback. The call opened with informal discussion about Python dependency management tools (UV, pip, Poetry) and Cursor's `.cursor` rules deprecation before moving into the main session.

Participants covered a wide range of topics: Marc troubleshot a Windows-specific MCP server error; Andrew discussed prompt engineering strategies and Gemini vs. Claude performance in Cursor; Tom shared experiments with VM automation and AI-based military aircraft identification; Juan sought advice on pricing a complex on-premise LLM deployment project; Sam asked about pricing structure for an internal AI report-drafting tool; Maksym gave updates on his Nissan dealership WhatsApp AI tool, including a new financing recommendation engine; Bastian demonstrated an agentic document extraction tool by Andrew Ng; Alex asked about Make vs. N8N for a government sentiment analysis workflow and Supabase vs. Firebase; Elad sought help with ADK artifacts and runner initialization; Abdul asked about YouTube content strategy and shared factory.ai; Kanav presented a multi-agent marketing platform built for local businesses; Aleksandr showed a Telegram bot with music downloading from Spotify/SoundCloud/YouTube; Richard shared the napkin.ai diagramming tool and discussed an AI playbook SaaS concept; Robert reflected on lessons from Brandon's videos about AI-assisted development workflows; and Neel asked about the evolution from Claude artifacts to Cursor and ADK vs. LangGraph.

Brandon provided guidance throughout on pricing freelance AI projects, ADK architecture, artifact handling workarounds, framework selection, and content creation strategy. The session ran approximately two hours.

## insights

- **Windows users hitting MCP errors** should check that NPX is pointing to the correct Node executable path rather than assuming the MCP server itself is broken (tip from Bastian).
- **Fast MCP library** simplifies local MCP server setup significantly — just wrap tools with a decorator instead of manually handling request/response logic (Brandon).
- **ADK Web ignores the runner entirely** — to set initial state when using `adk web`, use agent callbacks with an "initialized" flag to avoid re-running setup on every call (Brandon).
- **ADK artifacts require reading the file as a byte stream** and using `Part.from_bytes()` before calling `save_artifact()` — the seemingly correct approach without this step silently fails (Brandon).
- **ADK now has a function to wrap an agent as a FastAPI endpoint**, removing the need to manually build API routes for deployment (Brandon, discovered live).
- **Telling a looping LLM to "ultra think"** can unstick it when it's going in circles — document the loop pattern first, then invoke the phrase (Richard).
- **Narrow, focused prompts produce far better results** than broad requests in both Gemini and Claude; breaking work into small sequential tasks reduces errors dramatically (Andrew, Brandon).
- **Having the AI write a plan to a separate file** before executing, then iterating on that plan with multiple LLMs, is a highly effective technique for complex tasks (Andrew).
- **For freelance AI projects with businesses, charge tens of thousands upfront** — businesses expense it, see ROI, and the work is genuinely complex; don't undercharge because AI makes you faster (Brandon).
- **Structure freelance contracts in milestones**: ~15-20% deposit to start, payment on delivery, two-week testing window for small fixes, then hourly for anything beyond scope (Brandon).
- **Get foot in the door with a simple V1**, then grow the product — there is always a phase two once businesses see AI working (Tom, Brandon).
- **Vector stores are only needed when data volume exceeds the LLM's context window** or when querying the same corpus repeatedly; for single-shot web scraping, just use Gemini 2.5's large context window (Brandon).
- **ADK is recommended over LangGraph for most developers starting out** — easier to spin up, sequential/loop/parallel agent primitives cover 90% of use cases, and the team is responsive to feedback (Brandon).
- **The master plan → task document → chat workflow in Cursor** keeps the AI contextualized, prevents scope drift, and allows real-time task check-off (Brandon).
- **Use voice input (double-tap Command on Mac) in Cursor** to narrate context and instructions rather than typing, dramatically increasing speed (Brandon).
- **For YouTube content**, consistency beats home runs — one to two videos per week over a long period compounds; start with a welcome video, then a listicle, then how-tos (Brandon).
- **Napkin.ai** generates professional diagrams and infographics from prompts for free, useful for client proposals and presentations (Richard).

## qa

**Q (Marc):** I'm getting a "not implemented" error when trying to run MCP servers on Windows — tried Airbnb MCP, Google Maps MCP, and a local filesystem one, all fail the same way. What's going on?
**A (Brandon/Bastian):** This is likely a Windows-specific issue where NPX isn't running from the correct location. Bastian pointed out you can specify the exact Node executable path in your config to fix it. Also, add logging to your MCP server so you can see exactly where it's failing.

**Q (Andrew):** Gemini in Cursor sometimes undoes its own changes and loops — is this a prompting style issue?
**A (Brandon):** Likely yes — when failures happen, it's usually on broader requests. Brandon's approach is to always give Gemini very small, singular tasks and pass in screenshots/doodles for UI work rather than asking it to solve large problems at once.

**Q (Juan):** A potential client wants to deploy LLMs on rented NVIDIA servers (Oculus co-working space), with RAG, fine-tuning, and training. How should I price this?
**A (Brandon):** Go into discovery mode first — this could be straightforward (hosting models + chat UI) or extremely complex (fine-tuning pipeline). Don't price until you understand the minimum V1 requirements per category. Fine-tuning is a separate, harder scope; consider using Unsloth for that component.

**Q (Sam):** For an internal AI report-drafting tool, should I mark up usage costs (per chain run) in addition to passing through infrastructure costs?
**A (Brandon):** For an internal business tool, charge a large fixed upfront fee (around $20K as a rough starting point without full scope), then hourly for ongoing work. Break into milestones with a deposit, delivery payment, and two-week testing window. The prompt engineering/process extraction work is often harder than the build itself and should be factored in.

**Q (Alex):** Make vs. N8N for a simple Google Form → sentiment analysis → Google Sheets flow?
**A (Brandon):** Make is fine for simple single-shot LLM calls with no logic. N8N is better the moment you need any conditional logic. For calling Ollama locally, use Ollama serve + Ngrok to expose it as an API endpoint — this works in both tools via HTTP request.

**Q (Alex):** Supabase vs. Firebase for vector stores and general use?
**A (Brandon):** Brandon prefers Supabase for its Postgres/SQL structure and schema enforcement. Firebase's NoSQL document model leads to data redundancy and more developer-managed state as apps grow. Neon is a valid alternative if you don't need Supabase's auth/blob features. For under thousands of users, Supabase's $25/month plan is more than sufficient.

**Q (Elad):** When I run `adk web`, my runner initialization and artifact service don't seem to apply. How do I set initial state?
**A (Brandon):** `adk web` only looks at the root agent — it ignores the runner. Use an agent callback on the root agent instead. Check if an "initialized" key exists in state; if not, set all initial state values and flip the flag to true so it doesn't re-run.

**Q (Elad):** Should I drop ADK and switch to CrewAI or LangChain/LangGraph for my research assistant MVP?
**A (Brandon):** No — what you're building will work with ADK. The key missing piece is wrapping ADK in a FastAPI endpoint for deployment; Google recently added a function that does this automatically, making it much simpler than before.

**Q (Alex):** For agents that scrape the web, should results go into a vector database?
**A (Brandon):** Only use vector stores when your data volume exceeds the LLM context window or when you need to query the same corpus repeatedly. For single-shot web scraping (e.g., "what's trending on Reddit today"), just pass the results directly into Gemini 2.5's large context window — no vector store needed.

**Q (Kanav):** ADK vs. LangGraph — which should I use for a multi-agent marketing platform that needs both chat and workflow automation?
**A (Brandon):** ADK is the recommendation for new projects — it supports hybrid chat + workflow (sequential/loop/parallel agents), is easy to spin up, and covers 90% of use cases. LangGraph is better for very complex branching graph workflows. Since Kanav already has LangGraph experience from an internship, either is valid, but ADK is preferred for starting fresh.

**Q (Neel):** Have you moved away from the Claude artifacts approach shown in your older videos toward Cursor?
**A (Brandon):** Yes — Cursor is now the full workspace. The core principles (North Star/master plan document, breaking into small tasks) carried over, but everything now lives in an AI docs folder in the project rather than being copy-pasted from Claude's web interface.

**Q (Abdul):** How do you plan your YouTube content strategy without getting stuck in analysis paralysis?
**A (Brandon):** Pick your avatar, make a one-minute welcome video, then a listicle (five tips/tools), then how-to videos solving a single specific problem. Consistency over time beats trying to make viral videos. One to two videos per week indefinitely wins because everyone else quits.

## tools

- **UV (uv)** — Python dependency/environment manager; discussed as preferred alternative to conda and pip for project work
- **Cursor** — AI code editor; central tool for the session, discussed extensively for prompting strategies, `.cursor` rules, and workflow
- **Fast MCP** — Library simplifying MCP server creation with tool decorators; recommended by Brandon as easier than manual setup
- **Google ADK (Agent Development Kit)** — Google's agent framework; heavily discussed for building chat + workflow agents, artifacts, and deployment
- **Gemini 2.5 Pro/Flash** — Google LLM; Brandon's current preferred model in Cursor for coding tasks due to large context window
- **Claude (Anthropic)** — LLM; Andrew and Tom noted generally better results for focused tasks vs. Gemini
- **N8N** — Workflow automation platform; recommended over Make for any flow requiring logic, supports Ollama via HTTP
- **Make (Make.com)** — Workflow automation platform; suitable for simple single-shot LLM calls without branching logic
- **Ollama** — Local LLM runner; used by Alex via Ngrok to expose local models as API endpoints for N8N/Make
- **Ngrok** — Tunnel tool; used to expose local Ollama server as a public API endpoint
- **Supabase** — Postgres-based BaaS; Brandon's preferred database platform for vector stores and structured data
- **Neon** — Serverless Postgres alternative to Supabase when auth/blob features aren't needed
- **Firebase/Firestore** — Google NoSQL BaaS; discussed as less preferred than Supabase for growing applications due to schema-less complexity
- **Drizzle ORM** — TypeScript ORM; mentioned as Brandon's preferred tool for pushing schemas to Postgres
- **LangGraph / LangChain** — Agent orchestration framework; discussed as enterprise-established alternative to ADK, better for complex branching graphs
- **CrewAI** — Workflow-based agent framework; described as good for sequential workflows but not chat-based interactions
- **Firecrawl** — Web scraping tool; mentioned as returning results in markdown format for agent use
- **Unsloth** — Open-source fine-tuning library; recommended by Brandon for fine-tuning LLMs locally on large CSV datasets
- **Railway** — Cloud deployment platform; Aleksandr using it to host his Telegram bot
- **Napkin.ai** — Free diagram/infographic generator from text prompts; shared by Richard for use in client proposals and presentations
- **Factory.ai** — AI coding agent platform (recently opened from enterprise beta); shared by Abdul, uses "droids" for product/coding/reliability tasks
- **Agentic document extraction tool (by Andrew Ng's team)** — Demonstrated by Bastian; uses spatial coordinate-based extraction, processes complex documents including handwriting, ~$0.03/page
- **Azure Document Intelligence** — Microsoft document OCR/layout service; Andrew used it for handwritten document processing
- **Perplexity** — AI search tool; mentioned by Tom in context of aircraft image identification tests
- **DeepSeek** — LLM; Brandon asked if anyone had tried the latest coding model; Tom expressed interest in running it via Ollama
- **VMware** — Virtualization platform; Tom used Cursor to script automated VM builds
- **WhatsApp Business API** — Meta's messaging API; Maksym's tool runs on it; Alex noted painful approval process
- **Streamlit** — Python web framework; Marc moving away from it toward FastAPI + Next.js
- **FastAPI** — Python API framework; discussed for wrapping ADK agents as deployable API endpoints
- **Next.js** — React framework; Marc building toward it; Brandon uses it for client projects
- **Vercel** — Deployment platform for Next.js; mentioned by Brandon as his deployment target
- **Go High Level** — CRM/automation platform; mentioned as what most local service businesses actually need
- **Lovable / Replit** — No-code/low-code app builders; mentioned by Richard as options for building his SaaS concept

## links

- **Fast MCP library** — Dropped in chat by Brandon; simplifies MCP server creation with decorators
- **Cursor tips community post (31 comments)** — Brandon's community post collecting crowd-sourced Cursor workflow tips; Brandon shared link in chat
- **Medium article on web architecture/bottlenecks** — Shared by Tom previously; covers scaling, caching layers, load balancing from a practical perspective
- **Google ADK A2A (Agent-to-Agent) framework** — Brandon pulled up the GitHub/docs page; noted it's not yet at v1 stability
- **Google ADK FastAPI deployment example** — Brandon found a new ADK doc page showing a function to convert an ADK app to a FastAPI endpoint; shared in chat with Elad
- **Google ADK WebSocket deployment example** — Found during live search on ADK docs; shared as alternative deployment reference
- **Unsloth** — Open-source fine-tuning library; Brandon pulled up and shared link during Juan's discussion
- **Supabase pricing page** — Brandon shared screen showing $25/month plan includes 100GB storage
- **Sandeep's YouTube channel** — Example student channel from AI Authority Accelerator; shared by Brandon as model for Abdul's welcome/listicle/how-to progression
- **Brandon's ADK YouTube playlist** — Newly created playlist; Brandon shared the link during Robert/Neel discussion
- **Factory.ai** — Shared by Abdul during screen share; AI coding agent platform with product/coding/reliability droids
- **Next Wave podcast episode featuring Factory.ai** — Referenced by Abdul as having a live demo building a DocuSign clone
- **Napkin.ai** — Shared by Richard; free diagram generation tool for presentations and proposals
- **Agentic document extraction playground (Andrew Ng's team)** — Demonstrated by Bastian with sample insurance and medical documents; has API access

## decisions

- **Brandon** will send Elad a DM with the artifact byte-stream code snippet that makes `save_artifact()` work correctly in ADK.
- **Brandon** will make a video on ADK artifacts — acknowledged it's painful and poorly documented.
- **Brandon** will make a video on deploying ADK applications (FastAPI wrapper + hosting on Google Agent Engine), likely next week.
- **Brandon** will make a video on browser agents, building on the screenshot tool work shown during the call.
- **Brandon** will make a community-driven Cursor tips video giving shout-outs to contributors from the 31-comment community post.
- **Brandon** will make a video on the A2A framework covering stable core principles, noting full implementation details are still in flux.
- **Elad** will try the new ADK FastAPI deployment approach and DM Brandon with results before Brandon gets to it.
- **Richard** will write a short community post about Napkin.ai with a screenshot showing it's free.
- **Marc** will try Bastian's suggested fix (specifying the Node executable path for NPX) to resolve the Windows MCP error.
- **Aleksandr** will make his GitHub repository private before pushing cookies/credentials, and will redeploy to Railway to fix the cookie issue.
- **Juan** will go into discovery mode with the potential client to clarify minimum V1 requirements before pricing the project.
- **Sam** will structure his freelance contract with milestone payments and a two-week testing window; will have the client record Loom videos of their processes.
- **Maksym** will send a CYA email explicitly stating he is not responsible for verifying legal/regulatory compliance of the financing recommendation feature before it goes live.
- **Abdul** will start with a one-minute welcome video for his "vibe marketing in regulated environments" YouTube channel this week.
- **Tom** will try DeepSeek's latest coding model via Ollama on his local machines.