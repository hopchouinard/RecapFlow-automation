## general

This was a weekly group coaching/community call hosted by Brandon Hancock, focused on AI agent development and members sharing project updates. Brandon opened with a live demo of a voice agent he built using Google's Agent Development Kit (ADK) combined with Gemini's voice models, integrated with Google Calendar — demonstrating real-time voice commands to query, create, move, and delete calendar events.

The session then moved through a round-robin of member updates. Topics ranged from framework fatigue (jumping between LangChain, LangGraph, CrewAI, Agno, Amazon Bedrock, AutoGen), to specific project builds including a vehicle routing optimizer, an economics calculator deployed via FastAPI and Lovable, a Reddit sentiment analysis tool for healthcare/pharma, a WhatsApp conflict-mediation bot, and a news-to-infographic agent. Brandon also shared commentary on Google's ecosystem momentum ahead of Google I/O, and the group discussed sales qualification frameworks (BANT, Spin Selling) in the context of selling AI tools to enterprise clients.

Toward the end, members discussed tooling choices (Cursor vs. Windsurf vs. Claude Code), prompt engineering tips for avoiding TypeScript `any` errors, and a brief look at CodeRabbit as a code review tool. Brandon closed with recommendations for upcoming content: voice agent tutorial, video generation with Veo, and a deeper dive into ADK artifacts and versioning.

## insights

- **Framework-hopping builds adaptability**: Jumping between LangChain, CrewAI, Agno, etc. may feel unfocused, but the meta-skill of learning fast and adapting quickly is itself highly valuable in the current AI landscape.
- **ADK is not a ReAct agent**: Google's Agent Development Kit follows a plan-and-act model (not reason-act loop). If you want looping behavior, you must explicitly implement workflows — a common source of confusion for developers coming from CrewAI or LangChain.
- **Google's ecosystem is converging**: Brandon highlighted that Google ADK now provides voice, video, image generation, and agent orchestration in one platform — reducing the fragmentation that previously required stitching together Pinecone, LangChain, and separate agent frameworks.
- **Agent authentication is an emerging pain point**: Getting agents to authenticate with third-party services (e.g., Google Calendar) on behalf of users is a real unsolved UX problem; Auth0 is one potential solution.
- **Vibe coders create a business opportunity for engineers**: People with no coding background are building apps that are 60% complete — engineers can monetize by helping them finish. Brandon noted he already landed a contract doing exactly this.
- **BANT framework for qualifying AI consulting clients** (Brandon): Budget, Authority, Need, Timeline — if any one of these is missing, the deal is unlikely to close regardless of how good the product is.
- **Profitable businesses are bad prospects**: Paul Miller observed that companies making lots of money have no urgency to adopt efficiency tools, even if the operational staff wants them. Urgency and leadership buy-in matter more than operational pain.
- **Separate calculation logic from UI in vibe-coded apps**: Paul moved critical formula logic out of Lovable into a FastAPI backend he controls directly, then let Lovable handle UI — resulting in reliable, maintainable output.
- **Prompt with "explain" before "fix"**: Jake found that asking the AI to explain an error before fixing it dramatically improved results, especially for interconnected TypeScript issues like unexpected `any` errors.
- **Add project rules to prevent `any` in TypeScript**: Tom confirmed that adding a Cursor rule to avoid `any` types eliminated ~95% of those lint errors proactively.
- **Reasoning models in ReAct agents**: Using O3 Mini or DeepSeek R1 as the backing model for a ReAct agent is feasible but increases latency per loop iteration; the trade-off is potentially fewer incorrect actions.
- **ADK artifact versioning**: ADK supports artifact versioning, making it easy to roll back generated documents — particularly useful for report-building or document-generation agents.
- **Distribution strategy for niche apps**: Brandon suggested Michael's conflict-mediation WhatsApp bot should target marriage counselors and therapists as referral partners rather than going direct-to-consumer, since those professionals see the target customers daily.

## qa

**Q (Marc Juretus):** I'm getting a "poetry configuration is invalid" error when following your first agent for Vertex AI project. I thought I followed the readme verbatim.
**A (Brandon Hancock):** The project was updated to avoid Poetry. The readme now uses a standard Python virtual environment (`python -m venv .venv`) instead. Follow the updated readme and it should resolve the issue.

**Q (Marc Juretus):** Is a $299 NVIDIA GPU worth it for running Hugging Face models locally?
**A (Brandon Hancock / Tom Welsh):** Brandon deferred on hardware questions; Tom noted he's running an RTX 4080 in a $6,000 machine. Implied consensus: a low-end GPU won't cut it for serious local model inference — cloud alternatives (like virtual GPU instances) are a practical workaround.

**Q (Brandon Hancock):** What was Lovable doing wrong with your formula calculations, Paul?
**A (Paul Miller):** He wasn't a Next.js developer, so he was prompting his way to fixes and spending credits iteratively. Rather than continue debugging inside Lovable, he extracted the calculation logic into a FastAPI Python backend he could control directly, then pointed Lovable at the API for UI rendering only.

**Q (Sam):** Has anyone tried using reasoning models (like O3 Mini or DeepSeek R1) as the backing model for a ReAct agent?
**A (Brandon Hancock):** Yes, it's possible — they used O3 Mini with CrewAI. The reasoning step is essentially an expanded chain-of-thought before each action, so it still works within a ReAct loop. The main trade-off is that each iteration takes longer, though you may get more correct actions per attempt.

**Q (Brandon Hancock):** Are you bulk-processing posts for sentiment analysis or calling OpenAI per post?
**A (Jake Maymar):** Initially per-post, then switched to bulk processing with grouping via Regex to improve speed. GPT-4o Mini makes the cost essentially negligible for the volume he's processing.

**Q (Brandon Hancock):** What's the cost to run those bulk Reddit sentiment operations?
**A (Jake Maymar):** Essentially free — GPT-4o Mini is cheap enough that the entire operation runs at near-zero cost, and the infrastructure (Supabase free tier, Redis free tier) is also free in the sandbox environment.

**Q (AbdulShakur Abdullah):** What's the difference between BANT and Spin Selling?
**A (AbdulShakur Abdullah):** Spin Selling front-loads information gathering — Situation, Problem, Implication, Need-Payoff — to lead the prospect to articulate the value themselves before you present a solution. BANT is more of a qualification checklist. Spin Selling is more conversational and diagnostic; BANT is more of a gate-check.

## tools

- **Google Agent Development Kit (ADK)** — Brandon's primary focus; used to build the voice + calendar agent demo
- **Gemini 2.5 Pro / Gemini voice models** — Backing model for Brandon's voice agent demo
- **Google Calendar API** — Integrated with the ADK voice agent for CRUD operations on calendar events
- **Google AI Studio** — Used by AbdulShakur to test image generation prompts
- **Gemini 2.0 Flash Preview Image Generation** — AbdulShakur's chosen image generator for infographic agent
- **Vertex AI** — Marc attempting to deploy his first ADK agent; had Poetry config issues
- **LangChain / LangGraph** — Mentioned as prior frameworks members have used or are using
- **CrewAI** — Marc ~40% through a project; Brandon used it with O3 Mini for reasoning agents
- **Agno (formerly Phidata)** — Mentioned as part of Marc's course curriculum
- **Amazon Bedrock** — Current module in Marc's Saturday/Sunday course
- **AutoGen** — Upcoming module in Marc's course
- **FastAPI** — Paul used it to build a reliable calculation backend, deployed to DigitalOcean
- **Lovable** — Paul used it for frontend UI; got 60% there but had calculation accuracy issues
- **Next.js** — Brandon's go-to frontend framework; noted AI models are well-trained on it
- **here.com** — Tom using their routing API (free tier) for vehicle route optimization
- **TimeFold** — Python module Tom found for vehicle routing optimization; requires Java
- **Cursor** — Preferred IDE/AI coding tool for most members; noted for multi-file context
- **Windsurf** — Alternative to Cursor; Jake returned to it after OpenAI acquisition
- **Claude Code** — Jake tried it; found it overdoes changes and ignores rules; better on native Linux
- **Auth0** — Brandon planning a video on agent authentication using Auth0
- **Supabase** — Used by Jake (Reddit tool) and Michael (WhatsApp bot) for Postgres database
- **Redis** — Jake using it for caching Reddit post data
- **DigitalOcean (Droplet)** — Paul deployed his FastAPI backend here for ~$5/month
- **Cloudflare Workers** — Michael deploying his WhatsApp bot backend here
- **Twilio** — Michael using it as the WhatsApp messaging interface
- **Drizzle ORM** — Michael implemented it for his Supabase/Postgres database layer
- **WhatsApp Business API** — Distribution platform for Michael's conflict-mediation bot
- **OpenAI GPT-4o Mini** — Jake's model for Reddit sentiment analysis; near-zero cost
- **GPT Image 1 (OpenAI)** — Mentioned; requires identity verification to use via API; ~$0.02/image
- **Veo 2 (Google)** — Lucas accidentally ran up $800 in charges; Brandon planning a video on it
- **N8N** — Referenced as the benchmark for democratizing agent creation for non-developers
- **Tele.tv** — Brandon recommended to Maksym as a recording/editing platform to replace Loom
- **Loom** — Maksym had been using it; ran out of subscriptions across accounts
- **OBS** — Maksym considering it as a Loom alternative for recording
- **Adobe Premiere** — Maksym considering for video editing
- **CodeRabbit** — Bastian planned to demo it as an AI code review tool (deferred to next week)
- **UV** — Mentioned as a fast Python package manager; Brandon prefers plain venv for tutorials
- **Poetry** — Caused issues for Marc; Brandon moved away from it in his ADK project readme
- **Pinecone** — Mentioned as an example of the old fragmented AI stack
- **Azure Agent Foundry** — Mentioned as Microsoft's agent framework; described as demo-heavy but lacking substance
- **Oracle Cloud** — Michael just started a job there focused on Gen AI use cases for growth-stage tech companies
- **Replit** — Mentioned in context of a podcast featuring its founder

## links

- **Brandon's ADK voice + Google Calendar agent (GitHub repo)** — Shared in chat during the demo; members told to follow the readme to set up their own Google Calendar API connection
- **Alex Hormozi BANT article** — Brandon shared a link in chat during the sales qualification discussion; covers Budget, Authority, Need, Timeline framework
- **Spin Selling** — Referenced as a book on consultative sales methodology (no URL, book reference)
- **Juan Torres's LinkedIn article** — Analysis of a paper on AI model problem-solving speed doubling every ~7 months; reviewed with San Diego ML group
- **Podcast: Replit founder + Brett Weinstein episode** — Brandon recommended a ~3-hour listen covering optimistic vs. pessimistic AI futures (specific podcast name not confirmed in transcript)
- **Lenny's Podcast: "Inside Devon" episode with Scott** — Michal recommended the episode featuring the Devin AI founder
- **Greg Eisenberg's content** — Referenced as a podcast/show format Brandon would emulate (live building sessions)
- **Google I/O conference** — Paul noted it starts in 7 days from the call date (approximately May 20, 2025)

## decisions

- **Brandon** will publish the ADK voice agent tutorial video this week, including the Google Calendar integration demo
- **Brandon** will follow up with a video on Veo 2 (Google's video generation) after the voice agent video
- **Brandon** will reach out to Auth0 about sponsoring an agent authentication video
- **Brandon** will DM Marc after the call with follow-up questions about his project
- **Marc** will retry the Vertex AI first-agent project tonight following the updated readme (using `python -m venv` instead of Poetry)
- **Marc** will focus on Google ADK going forward and attempt to build a fantasy football roster management agent
- **Paul** will continue refining his FastAPI-backed economics calculator and get it in front of government/economist users
- **Tom** will continue working on polyline routing display for his vehicle routing optimizer
- **AbdulShakur** will switch from OpenAI image generation to Google's Gemini image generation for his infographic agent and report back on quality
- **Maksym** will record a HIPAA-compliant deployment tutorial video this week using Tele.tv instead of Loom
- **Maksym** will share his YouTube video link with Brandon when published
- **Jake** will add a Cursor project rule to avoid TypeScript `any` types and report back on results
- **Jake** will send Brandon screenshots from his Reddit sentiment tool filtered for AI/agent-related discussions
- **Michael** will send Brandon a link to his WhatsApp conflict-mediation bot for testing
- **Michael** will demo his app with a screen share next week
- **Bastian** will demo CodeRabbit as a code review tool next week
- **Brandon** will watch Google I/O (starting in ~7 days) and make videos on announcements immediately