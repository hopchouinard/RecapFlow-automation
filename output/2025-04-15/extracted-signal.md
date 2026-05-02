## general

This coaching call was a weekly group check-in led by Brandon Hancock, with participants including Juan Torres, Tom Welsh, Maksym Liamin, Aaron (The Dharma House), Michal Simko, Paul Miller, Bastian Venegas, and Nate Ginn. Brandon opened with announcements about GPT-4.1, Firebase Studio, and an upcoming Google Agent Development Kit tutorial before going around the room for individual updates.

Topics ranged from product development (a sales companion app, a WhatsApp-based health coaching agent, a heart failure monitoring app built at a Harvard hackathon) to content creation strategies, agentic system design, and tooling comparisons. Several participants discussed challenges around deployment, rate limits, and choosing the right AI framework for their projects.

A recurring theme was Google's accelerating dominance across the AI stack — Firebase Studio, Gemini's video capabilities, the Agent Development Kit, and Firebase's new AI workflows were all discussed. Brandon expressed strong conviction that Google is currently the best-positioned company to win the AI infrastructure race due to its vertical integration.

The group also touched on a practical framework for identifying which business workflows are best suited for agentic automation, and Brandon shared real-world examples from his consulting experience at Crew.ai.

## insights

- GPT-4.1 is particularly strong for agentic use cases — instruction-following, speed, and cost — but not recommended as a general chat or coding model.
- Google is vertically integrated across models, infrastructure, developer tools, and productivity suites, making it a strong bet to dominate AI application development.
- Firebase Studio's strategy of exposing developers to Firebase's AI workflows (Gen Kit) through a free builder tool is a clever top-of-funnel move to drive cloud AI adoption.
- Gemini Flash 2.0 can process a 20-minute video for roughly 200 tokens of input cost, making AI-powered video metadata extraction extremely cheap (potentially ~$0.10 per video).
- The best workflows to automate with agents are high-frequency, low-complexity tasks — not rare, complex ones. The cost of the human doing the task (salary) is a third dimension to consider.
- Real enterprise AI use cases are not dramatic full-automation plays; they are boring, repetitive tasks like competitive price monitoring reports that previously consumed significant human hours.
- When evaluating agents, guardrails can be implemented as pre- and post-LLM call checks, not just system prompt rules — this prevents the model from being invoked at all for disallowed inputs.
- For video content creation, documenting work-in-progress as a diary first gives better raw material for storytelling in later videos (Juan's insight about his own workflow gap).
- Weekly LinkedIn summary posts function as a public professional journal and help nurture existing networks (Brandon's suggestion to Juan).
- OpenRouter may be a practical workaround for Anthropic API rate limits, as it likely load-balances across providers without exposing the user to per-provider caps.
- Lovable is currently superior to Firebase Studio for app building; Firebase Studio improves significantly when switched to Gemini 2.5 Pro but then incurs costs.
- Building a V0 prototype with a simple custom GPT and sharing it with friends for structured eval feedback is a valid and fast way to validate agent behavior before investing in a full framework.

## qa

**Q (Maksym Liamin):** Has anyone gotten increased rate limits for Anthropic Claude? We're running out of input tokens and considering switching to Azure or AWS Bedrock.
**A (Brandon Hancock):** Check OpenRouter — it likely handles load balancing across providers under the hood, so you probably won't hit the same per-account rate limits. The markup is a small percentage on top of credits purchased, not per-call.

**Q (Juan Torres):** Is there a comprehensive guide or framework for deciding which workflows benefit most from agentic systems versus a direct ETL pipeline?
**A (Brandon Hancock):** The key dimensions are complexity and frequency. High-frequency, low-complexity tasks give the best ROI to automate first. A third dimension is the cost of the human currently doing it — automating a task done by a $120K/year employee is far more valuable than one done at minimum wage.

**Q (Michal Simko):** What does Brandon mean by "guardrails" — is it just rules in the system prompt?
**A (Brandon Hancock):** No — guardrails in agent frameworks are actual pre- and post-LLM call checks. A pre-guardrail intercepts the input before the model is ever called and blocks disallowed topics entirely. A post-guardrail checks the output after the model responds. This is more robust than relying solely on system prompt instructions.

**Q (Michal Simko):** What are bigger organizations actually using AI agents for in practice?
**A (Brandon Hancock):** Mostly boring, high-frequency internal tasks — for example, competitive price monitoring where one person's job was to manually survey competitor pricing every week and produce a report. That kind of task is now being replaced by agents at a fraction of the cost. It's not dramatic full-automation; it's eliminating repetitive knowledge-worker busywork.

**Q (Nate Ginn):** If I drop my existing website code into Lovable, can it pick up where I left off?
**A (Brandon Hancock):** Lovable works best starting fresh. The recommended approach is to upload screenshots of your existing design and have it recreate or build from those. It generates a Git repository you can then deploy anywhere or continue editing in Cursor.

**Q (Paul Miller):** Should I wait before jumping into Firebase Studio given your B-minus rating?
**A (Brandon Hancock):** Yes, wait for now. Lovable runs circles around it currently. Firebase Studio does improve with Gemini 2.5 Pro, but that costs money. The more interesting Firebase opportunity is the underlying AI workflows (Gen Kit) that Firebase Studio exposed — those are worth watching separately.

## tools

- **GPT-4.1** — Brandon highlighted it as a strong model specifically for agentic tasks; released the day before the call.
- **Firebase Studio** — Google's new app builder; rated B-minus currently, compared unfavorably to Lovable for app generation.
- **Google Agent Development Kit (ADK)** — Google's framework for building and deploying agents; Brandon described it as essentially "CrewAI but for Google"; tutorial forthcoming.
- **Gemini Flash 2.0** — Recommended for cheap video processing and structured metadata extraction from video files.
- **Gemini 2.5 Pro** — Mentioned as an upgrade option within Firebase Studio that improves output quality but adds cost.
- **Firebase Gen Kit (AI Workflows)** — Firebase's built-in AI workflow feature for structured LLM calls within Firebase apps; Brandon discovered it while exploring Firebase Studio.
- **Harpa AI** — Chrome extension for summarizing YouTube videos; Juan published a tutorial video about it.
- **OpenRouter** — Suggested as a workaround for Anthropic rate limits; likely load-balances across providers.
- **Lovable** — Highly praised AI app builder; Brandon's top recommendation for spinning up full-stack web apps quickly.
- **CrewAI** — Michal's planned framework for his WhatsApp agent V2; referenced as a comparison point for Google ADK.
- **Twilio** — Michal is studying its SDK for WhatsApp integration in his agent project.
- **WhatsApp API** — Used by both Maksym (sales companion) and Bastian (heart failure app) for patient/customer-facing interactions.
- **Manus AI** — Bastian used remaining credits to have it research and improve his hackathon project code.
- **Windsurf** — Used by Bastian for code integration during the hackathon; also mentioned by Juan for data web app development.
- **Tempo Labs** — Agentic IDE for JavaScript environments with Figma integration; Juan is experimenting with it for UI-heavy projects.
- **Google Maps API** — Tom is learning it for a routing project.
- **N8N** — Mentioned by Michal as a no-code process automation tool used in enterprise contexts.
- **OBS** — Bastian is using OBS with green screen filters for his upcoming YouTube channel launch.
- **Fast API** — Bastian used it for the backend of his hackathon heart failure app.
- **Vite (Vanilla React)** — Bastian's frontend stack for the hackathon project.
- **Google AI Studio** — Brandon demonstrated using it for structured output testing with video inputs.
- **A2A (Agent-to-Agent Protocol)** — Google's new protocol released that weekend; Brandon asked if anyone had tested it yet; described as a complement to MCP.
- **MCP (Model Context Protocol)** — Referenced as the existing standard that A2A may complement.

## links

- No explicit URLs were shared in the transcript. Juan shared a YouTube channel link in the chat (a yoga channel using AI-generated images), but the URL was not stated aloud and cannot be reconstructed from the transcript.

## decisions

- Brandon will publish a Google Agent Development Kit tutorial later that week or early the following week.
- Brandon will publish a Lovable tutorial/video the following week.
- Maksym will investigate OpenRouter as a solution to Anthropic rate limits.
- Maksym will look into Gemini Flash 2.0 for automated video metadata extraction as a complement or alternative to hiring a human labeler.
- Michal will watch Brandon's upcoming Agent Development Kit video before finalizing his V2 tech stack choice.
- Michal will prepare a demo of his WhatsApp agent for the following week's call.
- Juan will begin documenting his development process as a diary to improve his YouTube video storytelling structure.
- Juan will consider doing weekly LinkedIn summary posts as a public professional journal to nurture his network.
- Bastian will record his YouTube channel welcome video that evening or the following morning.
- Nate will sign up for Lovable and explore using it (potentially with his wife's design input) to rebuild his website.
- Brandon offered to build a real-world use case video around Nate's medical EHR/billing data cleaning scenario; Nate to send a dummy example for a future session.
- Brandon committed to cranking out real-world agentic use case content focused on Google's stack over the coming months.