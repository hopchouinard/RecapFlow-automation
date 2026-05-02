## general

This was a group coaching call hosted by Brandon Hancock, running approximately three hours with a large cohort of developers and entrepreneurs. The session followed a round-robin format where each participant shared project updates, wins, and problems they were working through. Brandon opened with updates on his own EMS Soap project (which recently received pre-seed investment from TinySeed) and announced that weekly calls would be winding down to roughly monthly cadence so he could focus full-time on EMS Soap.

The call covered a wide range of technical topics including Claude Code workflows, skills/agents architecture, RAG pipeline migrations, deployment strategies, and model selection for consumer-facing AI apps. Several participants demonstrated live projects including Paul Miller's Territory Compass route optimization SaaS, Alex Rojas's music studio booking app, and Ty Wells's multi-project Engram memory dashboard. Brandon also shared tips on using work trees for parallel UI prototyping, Google Ads setup via Claude Code, and the importance of building feedback loops into AI-powered client tools.

Business and go-to-market topics were prominent throughout: Brandon recommended the books *Software as a Science* (Dan Martell) and *The Unicorn Project* / *The Phoenix Project* (Gene Kim) as frameworks for thinking about SaaS sales and software development discipline. Participants discussed pricing strategies, partnership structures, customer acquisition via Loom outreach, and the value of finding a domain-expert co-founder. Brandon shared the story of how his co-founder Raul (an EMS chief in Florida) found him through YouTube, reinforcing the recurring theme of building public presence as a developer.

Patrick Chouinard gave a detailed walkthrough of his methodology for building an agent army to manage home-lab network infrastructure using Claude Code, MCP servers, and skills — emphasizing spec-first development and writing documentation optimized for the agent to consume. Scott Rippey shared a Claude Code prompt optimizer tool and research on recursive language models. The call closed with Ty Wells demonstrating an internal project management dashboard that tracks memory, flaws, credentials, and cross-project insights across 25 simultaneous projects.

## insights

- **Brandon Hancock:** When you find your "lottery project," go 100% all-in immediately — the AI-enabled window to build and ship is estimated at roughly two to three years before AI does everything autonomously.
- **Patrick Chouinard:** Write documentation optimized for the AI agent to consume later, not for human readability — use front-matter YAML as an index so the agent can find files without wasting tokens reading everything.
- **Patrick Chouinard:** Keep a scratch file of every prompt you type before sending it to an agent; when you notice you've copy-pasted the same prompt five times, that's your signal to make a skill out of it.
- **Patrick Chouinard:** Ask the agent to create its own documentation schema — "I want you to create a schema optimized for yourself to understand when you come back" — rather than specifying the schema yourself.
- **Brandon Hancock:** For creative/UI work, spin up five work trees with the same prompt and let each take a different approach; pick the best result and kill the rest. Gemini (via anti-gravity) produced the best UI design but had implementation errors that Claude Code then fixed.
- **Brandon Hancock:** Anti-gravity/Gemini is better than Claude Code at UI/UX design but weaker at actual coding; use it for prototyping UIs, then clean up with Claude Code.
- **Brandon Hancock:** For consumer-facing AI chat apps, prioritize Time to First Token (TTFT) over throughput; Gemini 2.5 Flash and Gemini 3 Flash on minimal thinking mode are strong choices for low-latency WhatsApp/messaging use cases.
- **Brandon Hancock:** For parallel API calls in AI apps, use `Promise.all` to fetch availability, room info, and other data simultaneously — doing them sequentially multiplies latency unnecessarily.
- **Brandon Hancock:** Avoid caching calendar/availability data in booking systems because stale cache causes double-booking; just make fast parallel API calls instead.
- **Brandon Hancock:** The secret sauce of a knowledge-based AI workflow tool is being a "prompt factory" — store every system prompt, user input, and output, then iterate backwards from the ideal final artifact to improve each upstream step.
- **Brandon Hancock:** Build in a feedback button on AI-generated outputs from day one; it gives you training data to improve prompts and sets customer expectations that the system improves with use.
- **Brandon Hancock:** Start a YouTube channel as a developer — Brandon's co-founder found him through YouTube videos, leading directly to a funded startup.
- **Andrew Nanton:** Giving the LLM less prescriptive instruction and instead asking "what are the pros and cons of doing X?" leads to better outcomes and personal learning.
- **Paul Miller:** Built a full production SaaS (Territory Compass) in two months part-time without writing a single line of code — all via prompts and the env file.
- **Brandon Hancock:** The peer community in an accelerator program (TinySeed) is often more valuable than the money itself — access to track records and warm intros from similar companies is the real asset.
- **Brandon Hancock:** When building agent systems, every loop that opens should close by writing documentation that sets the next agent run up for better success.
- **Scott Rippey:** Using Context7 in Claude Code prompts and structuring prompts with JSON/Python constraints significantly reduces iteration cycles and produces more one-shot results.

## qa

**Q (Elijah):** When Claude Code reads across skill files to decide which to use, isn't that essentially a form of RAG?
**A (Brandon Hancock):** It's closer to a tool call. Claude Code, during its planning phase, matches intent against available skills — if a skill's first paragraph matches what it's trying to do, it goes down that path. It's intent-matching against a skill index rather than vector similarity search.

**Q (Elijah):** Does ShipKit's RAG query support role-level permissions so not everyone can query all documents?
**A (Brandon Hancock):** Yes — look at the RPC function called `match_text_chunk`. You just add one line to filter by user ID and organization ID. It's a one-line change to support what Paul described as multi-level security.

**Q (Juan Torres):** Why did Paul choose DocPloy over other deployment platforms?
**A (Paul Miller):** DocPloy is more logical and user-friendly than alternatives. In comparisons it usually wins. It's an alternative to Vercel/AWS/Azure for managing your full back-end ecosystem, and you can create a DocPloy skill so Claude Code can handle DevOps work for you.

**Q (Prem):** Is anti-gravity worth switching to from Cursor?
**A (Brandon Hancock):** Use it one out of 100 requests, mainly for UI/UX prototyping. Its UI understanding is better than Claude Code's, but its actual coding quality is not. Best use: spin up a work tree with anti-gravity for design exploration, then have Claude Code fix the implementation errors.

**Q (Prem):** My Claude Code context seems to be running out faster lately — is that normal?
**A (Brandon Hancock):** Yes, conversation compaction happens more with larger tasks, but it doesn't matter much as long as your underlying task document exists outside the conversation. The overarching goal is documented somewhere that doesn't get compressed.

**Q (Lan):** If I start with the chat ShipKit template but later need RAG, do I have to rebuild?
**A (Brandon Hancock):** For adding something like worker SaaS, you can reference the other repo in AI Docs and ask Claude Code to add the new functionality — it's additive. But RAG is a fundamentally different starting point (multiple apps sharing one database), so if you know you'll need RAG, start with the RAG template. Wait a day for the updated version since the Google text-embedding model deprecates tomorrow.

**Q (Raghav):** Are the ShipKit idea-to-development templates valid for any project or only the specific ShipKit project types?
**A (Brandon Hancock):** They're tied to the underlying template because the template constrains what tech stack and patterns the AI assumes. For a non-standard project, start with the chat template (simplest), build what you need, then run the cleanup script to remove unused functionality.

**Q (Alex Rojas):** Should I use Redis caching for calendar availability in my WhatsApp booking bot to reduce latency?
**A (Brandon Hancock):** No — skip the cache because stale data causes double-booking. Instead, make all three API calls in parallel using `Promise.all`. Each call takes ~0.3s; in parallel the total is still 0.3s vs ~0.9s sequentially.

**Q (Juan Torres):** Does EMS Soap need to be HIPAA or SOC 2 compliant since it handles medical records?
**A (Brandon Hancock):** Currently no, because the system is designed as an "AI calculator" — non-HIPAA information goes in and out. They actively ask users not to submit patient-identifying information since it's not needed for compliant documentation. They're pursuing compliance to unlock more features and reduce friction.

**Q (Maksym Liamin):** How did you find your co-founder and structure the partnership?
**A (Brandon Hancock):** Raul found Brandon through YouTube. They had hard conversations upfront about work ethic and expectations before signing anything. Brandon recommends a 50/50 split when both partners are essential — without the developer the business dies, without the domain expert/salesperson it also dies. Have explicit conversations about expected work hours before committing.

## tools

- **Claude Code** — Primary AI coding agent used by most participants; discussed for skills, work trees, agent orchestration, and the new "co-work" feature for knowledge workers
- **Claude Code Co-work** — New Claude Code wrapper for knowledge workers; Patrick used it to reclassify 30,000 Google Drive documents in ~15 minutes
- **Cursor** — IDE used alongside Claude Code for debugging; Patrick uses it as the IDE while Claude Code generates code
- **WindSurf** — IDE used by Morgan Cook; recently added native skills support matching Cursor's model
- **anti-gravity** — AI coding tool used as an alternative to Cursor; better at UI/UX design but weaker at code quality than Claude Code
- **OpenCode** — Open-source coding agent; Bastian uses it to run GLM 4.7 for code reviews and as a Claude Code alternative
- **GLM 4.7** — Chinese LLM; ~$24 for 3 months, near Claude Sonnet 4.5 capability, used as a cost-effective backup for code review during Claude cooldown periods
- **Gemini 2.5 Flash / Gemini 3 Flash** — Recommended for low-latency consumer-facing AI apps; minimal thinking mode for WhatsApp-style responses
- **OpenRouter** — Used to compare model latency (TTFT) and throughput metrics when selecting models for production apps
- **Lemon Squeezy** — Payment processor for one-off digital products; Morgan evaluating it as simpler alternative to Stripe for managing many small products
- **Stripe** — Payment processing; used in Alex Rojas's booking app; discussed as more complex to manage many products vs. Lemon Squeezy
- **Supabase** — Database platform used in ShipKit RAG template; Brandon migrating from old text-embedding model to new one
- **DocPloy** — Self-hosted deployment platform (alternative to Vercel/AWS); Paul runs Territory Compass as a Docker swarm of 6 apps on a VPS
- **Clerk** — Authentication service used in Territory Compass; Paul built a Claude Code skill for it
- **Vanta** — SOC 2/HIPAA compliance platform; Brandon signed a $16K contract after joining TinySeed
- **Notebook LM** — Used by Bastian for research and generating podcasts/slides; Paul described using multiple Notebook LMs as free RAG back-ends via an agentic front-end
- **Perplexity** — Added by Bastian as an agent and tool for web research within his multi-agent system
- **Exa** — Web search provider used alongside Perplexity for high-volume queries
- **N8N** — Workflow automation; Patrick building a secure self-hosted N8N server on a VLAN as the end goal of his home-lab infrastructure project
- **Proxmox** — Hypervisor; Patrick's phase 2 target after completing Ubiquiti network agent
- **Ubiquiti Dream Machine** — Home-lab network hardware Patrick is building an AI agent to manage
- **Appify** — Scraping platform; suggested by Paul for Marc's TV/movie release feed
- **Rapid API** — Marc using it to pull TV/movie release data; finding releases are behind
- **Deepgram** — Voice transcription API; Brandon recommended it for Scott's construction estimator tool so the client can talk through a job
- **HeyGen** — AI avatar generation; Ryan building a content automation system using it for a Florida client
- **Suno AI** — Music generation AI; Alexander integrating it into his Telegram music bot
- **Trigger.dev** — Background job processing; Andrew mentioned Inngest as an alternative for teams needing to run their own workers
- **Inngest** — Alternative to Trigger.dev for self-hosted background job workers; Andrew recommended for data privacy use cases
- **TinySeed** — Pre-seed accelerator Brandon's EMS Soap joined; provides funding, coaching, and peer community
- **Vroom / OR-tools** — Route optimization APIs used in Paul's Territory Compass for the traveling salesperson problem
- **Warp Terminal** — Terminal app used by Lan during live GitHub auth troubleshooting
- **Context7** — Documentation tool Scott uses heavily in Claude Code prompts for better one-shot results
- **Bolt** — Used by Ryan to quickly scaffold informational websites before refining in Claude Code
- **Screenly** — Ryan's digital signage SaaS product for real estate agents and brick-and-mortar businesses
- **Alembic** — Python database migration tool; Juan mentioned using it or raw SQL for his ETL pipeline migration
- **AWS EC2** — Juan using it for microservices hosting; discussed AMI migration for scaling instances

## links

- **Software as a Science** (Dan Martell) — Book on B2B SaaS sales, avatars, funnels, and sales call frameworks; Brandon uses it religiously for EMS Soap; dropped Amazon link in chat
- **The Unicorn Project** (Gene Kim) — Novel about senior engineering thinking, reducing technical debt, and repeatability; Brandon currently reading it; Brandon Hancock mentioned it as inspiration alongside The Phoenix Project
- **The Phoenix Project** (Gene Kim) — One of two books that inspired ShipKit; recommended as less technical entry point vs. The Unicorn Project
- **Steve Yegge blog / "Beads" project** — Andrew shared a post by ex-Google engineer Steve Yegge (collaborating with Gene Kim) on agentic programming and the premise that code is cheap; described as alpha-level, written in Go
- **Inngest (I-N-N-G-E-S-T)** — Andrew shared as alternative to Trigger.dev for self-hosted background job workers: https://www.inngest.com
- **Muhammad's RAG YouTube channel** — Paul referenced a PhD data scientist's channel on advanced/agentic RAG approaches for multi-document contexts; shared post in community
- **PRD best practices post** — Paul shared a post about adding a "core intent" paragraph to AI-generated PRDs so the AI dev tool doesn't lose sight of the application's purpose
- **Notebook LM as RAG back-end post** — Paul shared a post describing using multiple Notebook LMs as free RAG libraries with an agentic front-end
- **Territory Compass I/O** — Paul's live SaaS app for traveling salesperson route optimization: territoriocompass.io (requires Clerk authentication)
- **ShipKit community repo** — Patrick's skills and Shipkit Mentor GPT prompt are in the community GitHub repo under his username (op-chouinard directory)
- **Scott's Claude Code Prompt Optimizer** — Scott shared a setup file with JSON/Python-structured prompt optimization instructions in the Zoom chat
- **Recursive language models article + GitHub repos** — Scott shared research on recursive LLMs as a context-solving technique, with GitHub repos for experimentation; dropped in Zoom chat
- **OpenRouter** — Used live to compare model TTFT and throughput: https://openrouter.ai
- **GLM 4.7 benchmark post** — Juan shared a post in chat showing GLM 4.7 benchmarks near Claude Sonnet 4.5 level

## decisions

- **Brandon Hancock** will wind down weekly coaching calls to approximately one per month, announced with weekend notice; plans to add community admins to Zoom so peer-hosted calls can continue on other days
- **Brandon Hancock** will record a video this week walking through the migration from Google `text-embedding` to `text-embedding-v2` for existing ShipKit RAG users
- **Brandon Hancock** will send a Discord message and email when the updated RAG template (with new embedding model) is merged and ready to pull
- **Brandon Hancock** will call Maksym this weekend to discuss investment/fundraising options for Maksym's automotive AI product
- **Brandon Hancock** will reach out to Andrew Nanton to get his input on EMS Soap's grading feature, given Andrew's extensive SOAP note writing background
- **Paul Miller** will write up his help-center feature as a skill and share screenshots with the community so others can replicate it
- **Paul Miller** will update the help center's changelog section to translate GitHub commit history into customer-friendly language explaining what changed and why
- **Patrick Chouinard** will continue building out his Claude Code network admin agent (phase 1: Ubiquiti Dream Machine), with phases 2–4 covering Proxmox, network services (DNS/DHCP), and eventually a coordinator agent over all sub-agents
- **Marc Juretus** will demo his energy rate monitoring/alerting app next week after Brandon committed to "bullying" him for a demo
- **Morgan Cook** will report back on Lemon Squeezy approval process and usability for managing many one-off digital products
- **Ryan** will ask his brewery contact what price point he'd be willing to pay for the Screenly digital signage product
- **Scott Rippey** will drop his Claude Code Prompt Optimizer, Prompt Architect, and recursive language model article links into the Zoom chat for the group
- **Lan** will create a video documenting the hurdles of pulling down the ShipKit repo on Mac for other new users
- **Alex Rojas** will switch from caching + Grok to parallel API calls with Gemini 2.5 Flash or Gemini 3 Flash (minimal thinking mode) for his WhatsApp booking bot
- **Alex Rojas** will send Loom videos to adjacent local businesses (gyms, other studios) highlighting friction points on their current booking websites as a lead generation strategy
- **Brandon Hancock** will review and merge the developer's text-embedding migration code before sending the announcement email