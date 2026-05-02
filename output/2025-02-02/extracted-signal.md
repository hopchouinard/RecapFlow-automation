## general

This was a group coaching call hosted by Brandon Hancock with members Alexandra Spalato, Tom Welsh, Christopher (Chris) Marin, and Orlando Agostinho. The session followed a round-robin format where each participant shared updates on their current projects and received feedback from the group and Brandon.

Topics spanned client acquisition and pricing strategy (Alexandra), a tourism/accommodation management web app (Tom), an internal AI chat platform for enterprise use (Chris), and early-stage YouTube channel growth (Orlando). Brandon also shared his own content strategy around riding the DeepSeek and O3 Mini wave of interest.

A significant portion of the call was dedicated to YouTube channel optimization, particularly for Orlando's new channel. Brandon walked through thumbnail strategy, title optimization for search, video hook structure, and the economics of hiring a thumbnail editor. Alexandra also received feedback on her thumbnail and title approach as her channel was further along.

The group also discussed AI model comparisons — DeepSeek R1 vs. O3 Mini vs. Claude — for coding tasks, with Brandon sharing a workflow of using O3 Mini for high-level planning and DeepSeek for feature-level implementation.

## insights

- **Brandon:** The closer your solution is to money generation or money saving, the easier it is to sell. Recruiters spending $1K/month on an AI system that replaces a $7K/month hire is a straightforward ROI conversation.
- **Brandon:** When starting a YouTube channel, treat YouTube as a search engine first — match your title to what people are already searching for rather than optimizing for virality.
- **Brandon:** Thumbnails and titles deserve 20–30% of total video production time. If no one clicks, the hours spent making the video are wasted.
- **Brandon:** A thumbnail editor hired for $20–30/thumbnail can realistically double click-through rate, turning a 3% CTR into 6% — the ROI math is straightforward.
- **Brandon:** Hire two thumbnail editors simultaneously on a trial basis, give them identical briefs, and keep whichever produces the better result.
- **Brandon:** Research competitor thumbnails before briefing your editor — steal what's already working and adapt it to your angle.
- **Brandon:** For YouTube hooks: show the before (the problem) and the after (the desired result) within the first 10–15 seconds, then promise to explain how to get there in N simple steps.
- **Brandon:** O3 Mini excels at large-context planning and building from scratch; DeepSeek R1 excels at implementing specific features. Using them in sequence is an emerging best practice.
- **Alexandra:** For reselling AI agents to a client's customers, charge a license fee rather than revenue share — revenue share creates an incentive for the client to replace you once the system scales.
- **Brandon:** When automating work inside a company, set explicit compensation expectations with leadership upfront. Replacing four people's workload without a prior agreement may result in only a token bonus.
- **Brandon:** Use yourself as a case study before you have client testimonials — document your own results using the system you're selling.
- **Brandon:** Any task that costs less than your effective hourly rate should be delegated. If your rate is $100/hr, a $30 thumbnail that saves two hours is an obvious win.
- **Tom:** DeepSeek R1 lacks vision/image input, requiring a hybrid workflow — use Claude for image-based prompting, then pass the output to DeepSeek for implementation.

## qa

**Q (Tom):** Do you have suggestions for React components that could handle a Gantt-style calendar view for managing vehicle/resource allocation across time slots?
**A (Brandon):** Nothing specific came to mind immediately. Before picking a library, define the exact interactions needed (e.g., drag-and-drop, time extension) because many libraries support static data but not interactive manipulation. D3.js was mentioned as a possibility. Brandon offered to follow up if something came to mind.

**Q (Christopher):** Are you running O3 Mini and DeepSeek directly in Cursor/Windsurf, or going straight to the source?
**A (Brandon):** Using them inside Cursor/Windsurf, but the reasoning level they apply (low/medium/high) is unclear — Brandon suspects they may default to medium to save costs. O3 Mini handles large context (200K tokens in, 100K out) extremely well but can struggle on implementation. DeepSeek is weaker on large context but strong on executing a specific, scoped problem.

**Q (Alexandra):** How should I price a personal AI executive assistant system for a client who also plans to resell it?
**A (Brandon):** Pricing is highly dependent on how much the client values their time. A range of $5–7K was discussed as reasonable. The more important structural point: charge a license fee for resale rights rather than revenue share, so the client can't cut you out as the system grows.

**Q (Orlando):** Is there any impact from publishing one versus two videos per week at the early stage?
**A (Brandon):** At this stage, publish as much as possible to improve your craft — titles, hooks, and outlines. The algorithm matters less than getting reps in and learning what resonates. Don't stop; the only way to lose is to quit.

**Q (Orlando):** Is it worth setting a monthly budget for YouTube channel investment?
**A (Brandon):** Yes. A budget of $150–200/month focused on thumbnail editing is the highest-leverage spend. It frees your time for higher-priority work and directly improves the metric (CTR) that determines whether your content gets seen at all.

**Q (Orlando):** Has Brandon tried DeepSeek inside CrewAI?
**A (Brandon):** As of the prior Friday, CrewAI released a new version supporting DeepSeek. Brandon hadn't tested it yet but planned to make a video comparing DeepSeek and O3 Mini inside CrewAI agents.

## tools

- **DeepSeek R1** — Discussed extensively as a coding model; Tom running it locally at 8B size; compared against O3 Mini and Claude for development tasks
- **O3 Mini (OpenAI)** — Compared against DeepSeek for coding; strong on new projects, refactoring, and tests; weaker on adding features to existing apps
- **Claude (Anthropic)** — Previously Tom's primary coding model; used for image/vision tasks where DeepSeek lacks multimodal support
- **Cursor** — AI coding IDE; O3 Mini and DeepSeek R1 available inside it; reasoning level settings unclear
- **Windsurf** — AI coding IDE; Chris tested O3 Mini here with mixed results
- **Make.com** — Automation platform; Orlando built a video around removing DeepSeek's thinking step output inside Make workflows
- **Relevance AI** — Agent-building platform; Alexandra used its LinkedIn scraping tool via API for contact enrichment in outreach workflows
- **CrewAI** — Agent framework; Brandon mentioned a new DeepSeek-compatible version released Friday; planning a comparison video
- **Supabase** — Database/backend platform; Chris using it for his internal AI chat tool, flagged as a security concern internally
- **OpenRouter** — API aggregator; Chris using it as the primary model routing layer in his chat platform
- **V0 (Vercel)** — Used by Tom in early scaffolding of the North Coast 500 project
- **Service M8** — Property management software with a messy API; Alexandra integrating it for a client's voice agent workflow
- **Upwork** — Freelance platform; Brandon recommended for hiring thumbnail editors, noting higher quality than Fiverr at a ~20% premium
- **Fiverr** — Freelance platform; mentioned as an alternative to Upwork for hiring thumbnail editors
- **YouTube Studio** — Brandon walked Orlando through the analytics dashboard live to review impressions and CTR
- **D3.js** — Mentioned as a possible option for building Gantt/time-based chart components in Tom's project
- **Grok** — Orlando mentioned using it; noted as very fast; used with a distilled Llama 3 70B variant
- **Llama 3 (distilled, 70B)** — Model Orlando ran locally via Grok for testing

## links

- No explicit URLs or repositories were shared during the call.

## decisions

- **Orlando** will update the title of his existing DeepSeek/Make video to be search-query-based (e.g., "How to remove DeepSeek's thinking step in Make") to improve discoverability.
- **Orlando** will hire a thumbnail editor (via Upwork or Fiverr) for his next video, targeting $20–30 per thumbnail.
- **Brandon** will share his Upwork hiring script for thumbnail editors and video editors in the pro community within approximately two days.
- **Tom** will subscribe to Orlando's YouTube channel and leave a comment.
- **Alexandra** will watch her own last video (LinkedIn scraping workflow) and share it with Orlando as a reference for using Relevance AI's LinkedIn scraper via API.
- **Alexandra** will consult her sales coach on how to handle the testimonial/proof-of-concept gap when pitching the IT recruiter voice agent package.
- **Alexandra** will send pricing table details to the client (smarthew.ai) and begin work on his personal AI assistant system after receiving his information on Monday.
- **Brandon** will release multiple videos this week focused on DeepSeek and O3 Mini content, then return to building out the AI Authority Accelerator program.
- **Christopher** will continue rolling out his internal AI chat platform to colleagues for feedback before a wider release, and plans to add O3 Mini to the available models.