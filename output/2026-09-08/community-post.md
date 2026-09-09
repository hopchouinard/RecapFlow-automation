📝 SUMMARY

This week's call packed a lot into one session, moving from practical debugging and cost-saving tactics to career mentorship and, finally, a genuinely thought-provoking discussion about staying active thinkers in an AI-curated world. Members shared hard-won lessons on RAG debugging and model selection, live demos of home-built observability tooling, and real numbers on cutting production costs by switching models. A recurring theme throughout was that technical skill alone isn't enough — whether you're hunting for paid AI work, scaling a business, or getting better answers from your tools, the edge comes from combining technology with domain knowledge, relationships, and deliberate intent. The conversation closed on a memorable framing: with models this capable, humans — not AI — are now the bottleneck on connecting insights, so it's on us to configure our tools to challenge us rather than comfort us. Whether you attended live or not, there's something here worth stealing for your own work.


💡 KEY INSIGHTS

Set smart-model baselines first — otherwise you can't tell if failures come from the model, retrieval, or prompt.

Check your RAG retrieval before blaming the LLM: junk in, junk out.

Long agent sessions re-send the entire growing context (500k–800k+ tokens) each response, burning limits fast — one-shot requests are cheaper than always-on agents.

Switching a production workflow fully to GLM 5.3 cut per-run cost from ~$0.80–$1.10 to ~$0.09 with no perceptible quality drop.

Use OpenRouter's independent task-based model rankings (coding, agentic, etc.) as a starting point for comparisons.

Build observability around your AI usage: track tokens, session status, and unresolved attention across agents — treat LLM usage like infrastructure needing monitoring.

GPT's computer-use can functionally replace a QA hire — it finds bugs and proposes fixes for another model to implement.

Astra (GPT-6/Codex) beat Fable on a multi-hour admin planning task, and is less restrictive for security audits.

Pair "accounting-precision" models for admin work with a second model for peer review and blind-spot checking.

Market insights: coding-only skills are oversaturated; pair code with an outside domain or passion.

Best niches are ones nobody yet associates with AI — SEO, marketing, and dashboards are commoditized.

Hunt for past workflow blockers that weren't cost-effective to fix — AI removes that barrier, and your firsthand pain points are validated opportunities.

Legacy late-90s internal software in factories and small franchises is a real, underexploited modernization market.

Leverage existing business-network connections over purely technical ones — devs already crowd the technical space.

Practical lead-gen: use a LinkedIn bot to surface top SMB pain points, match them to your skills, then build demos and content around them.

Beware "Instagrammified" AI success stories — survivorship bias and hidden networks are everywhere.

Personal branding buys credibility and easier interviews, not direct revenue; inbound lead quality drops as the space saturates.

Validate AI hype by having AI transcribe and benchmark claims against real content, including paid sessions.

Idea generation: narrate daily frustrations to ChatGPT instead of brainstorming — most demos came from this.

Run a daily evolving news conversation with ChatGPT, or set your feed as an "anti-pattern": the 10 things you should know but don't, to avoid tunnel vision.

Configure assistants to be confrontational or "brutal" — never agreeable — to avoid yes-man behavior.

A feed only stays useful if you interact with it; interaction is what builds memory and context.

Architecture pattern: a cheap dispatcher with full context/memory routes tasks to a smarter, trimmed-context tier — cost meets capability.

Invert the human→AI harness: treat humans as an expensive, low-parallelism resource used only for judgment calls.

"Before writing was difficult, now reading is difficult" — design interfaces to reduce cognitive load when consuming AI output.

The real leverage: HGI, not AGI — humans connecting the dots across disparate information remains the limiting factor.


❓ KEY Q&A

Q: Any recommendation on Qwen vs GLM 5.3 for a RAG agent, since GLM 5.3 keeps flipping answers across test iterations? (Hemal Shah)

A: Check OpenRouter's independent model ranking by task as a starting point. (Paul Miller)

Q: Is your RAG actually returning relevant content? Did it ever work with a more expensive model to establish a baseline? (Daniel Zivkovic)

A: Ran 10 iterations, spent $100 on Gemini and hit the cost cap before finishing all 50 tests; used Qwen as a non-deterministic LLM judge instead. (Hemal Shah)

Q: Why doesn't Hermes show the weekly usage bar like other harnesses? (Juan Torres)

A: Hermes isn't tied to a subscription directly — it either uses Codex capacity or connects to GLM via OpenRouter API, which has no subscription bar. (Patrick Chouinard)

Q: Did you do anything with the "Pi" agent mentioned last week? (Paul Miller)

A: No — spent the time token-maxing Astra and Fable instead. Pi will likely be built later via a custom harness connecting Claude Code and Codex through T3 Code. (Patrick Chouinard)

Q: Did you try OpenAI's new model? (Paul Miller)

A: No — community feedback suggests GPT-6/Astra is great for coding but overdoes "thinking." He continues using Fable 5.1 at medium thinking paired with GPT for peer review. (Daniel Zivkovic)

Q: How do you handle a customer whose accountant insists on a specific chart-of-accounts setup? (Paul Miller)

A: The business advisor asks about business type first and configures the chart of accounts accordingly — the front end guides requirement-gathering while the back end is already built. (Ty Wells)

Q: ~10% of my RAG tool's code is from ShipKit — can I get security help without violating sharing rules? (Tim Hildenbrandt)

A: Post on the community forum without sharing raw code publicly. Ryan C offered to run it through "Scott's CC security review suite" via email/DM, since Tim's membership level doesn't allow board messaging yet. (Paul Miller / Ryan C)

Q: Have you asked Claude how to host your app securely, using a paid subscription with full codebase context? (Paul Miller)

A: Yes, but got conflicting answers — Opus and Fable each created new conflicts. (Tim Hildenbrandt)

Q: Kris, is this a hobby, or do you need to make money? (Daniel Zivkovic)

A: I'd like to make money; struggling to find where I fit even after 38 years in IT. (Kris Larson)

Q: Have you thought about a business association or local chamber of commerce? (Paul Miller)

A: Yes, looked into the Rochester Chamber of Commerce, but access is harder/costlier and someone's already doing similar work there. (Kris Larson)

Q: Have you thought about plugging your system directly into venues' social media during events? (Patrick Chouinard, to Juan)

A: Great idea for later once trust is built. Meanwhile, he emails images to venue planners and social coordinators to post themselves. (Juan Torres)

Q: What is Fieldy? (Daniel Zivkovic)

A: A pendant recorder that records ambiently 24/7 (alternatives: Omi, Limitless). It doesn't record raw audio but tracks trends, and is queried by Hermes via WebSocket. (Patrick Chouinard / Ty Wells)

Q: Does it distinguish speakers? (Daniel Zivkovic)

A: Not exact diarization, but it differentiates between Patrick talking, someone else talking, and media being consumed. (Patrick Chouinard)

Q: Which ambient recording system would you recommend? (Daniel Zivkovic)

A: Fieldy — it's true passive 24/7 recording, versus manually-triggered tools like Plaud, Granola, or Pocket. (Patrick Chouinard)

Q: Is the personalized news feed built via memory or an installed skill? (Daniel Zivkovic)

A: Nothing special — just a ChatGPT scheduled task. Personalization comes from ongoing daily conversation. (Patrick Chouinard)

Q: Can I keep my $20 ChatGPT plan, or do I need the $100 plan to use Astra for Hermes? (Ryan C)

A: If you touch Astra, yes, you need the $100 plan. (Patrick Chouinard)

Q: How does Agent Deck's UI relate to human cognitive effort? (Kris Larson, paraphrased)

A: It's built to make efficient use of the human's cognitive "tokens" — reducing reading and cognitive load. Writing used to be the hard part; now reading and consuming AI output is. (Patrick Chouinard)


🛠️ TOOLS AND CONCEPTS MENTIONED

Here are the key tools, frameworks and concepts mentioned on this week's call, with a quick note on each:

Codex (OpenAI) / "Astra" – Coding agent/model tier. Praised for coding bursts, computer-use QA, and less-restrictive security auditing, but inconsistent for deep "thinking" tasks. Requires the $100 plan.

Claude / "Fable" (Opus, Sonnet, Claude Code, Fable 5.1) – Anthropic's model family, used for coding, review, and business/creative thinking.

Opus 5 – Used to implement fixes identified through computer-use QA.

GLM 5.3 / GLM 5.3 Flash – Chinese model tested for RAG and adopted for production workflow, cutting costs roughly 90%.

Qwen – Chinese model used as a non-deterministic LLM-as-judge.

Gemini – Expensive model tried first for RAG baseline testing.

OpenRouter – Model aggregator/marketplace with a task-based ranking index.

AgentDeck – Patrick's observability dashboard/harness for tracking multiple AI agent sessions and reducing cognitive load when consuming AI output.

Hermes – Patrick's personal "infrastructure operator" agent system; ingests Fieldy, email, and other data.

Luna – Cheap default dispatcher agent profile within Hermes, holding full context and memory.

T3 Code – Harness that runs Claude Code and Codex under Patrick's monitored setup.

Prometheus / Alertmanager / Loki / Grafana / NATS / Authentik / Traefik – The backend monitoring and infrastructure stack behind Patrick's home lab.

ShipKit – Starter repo Tim Hildenbrandt used as a base for his RAG tool.

Ollama – Local small-model runtime powering Tim's local-only RAG setup.

Scott's CC Security Review Suite – Security/performance review package offered by Ryan C.

Every.to – Paid AI newsletter/community Daniel follows for early model reviews.

Compound Engineering Framework – Coding/SDLC framework (via Every.to) that Daniel uses for development work.

Jcodemunch / CMUX (jcodemunch.com) – Tool/agent that reduced coding usage for Tim and Ty.

GrokBot – Used with a LinkedIn connector to identify SMB pain points for lead generation.

ChatGPT (voice mode / computer-use / scheduled tasks) – Used for morning news discussion, "news radar" tasks, and tested for automated video editing.

Fieldy (.AI) – Ambient necklace recorder for continuous life/context logging (~$150/year).

Omi (Omi.me) – Alternative ambient note-taking device.

Limitless – Another note-taking device (subscription expiring).

Plaud / Granola (granola.ai) / Pocket – Manually-triggered note-taking apps, rejected in favor of Fieldy's ambient recording.

EC2 / Auto Scaling Group / Load Balancer (AWS) – Infrastructure Juan Torres needs for scaling his photo-automation app.

Custom Chrome extension – Built by Ty Wells to capture browsing session context.

Kindle text-to-speech – Used to have curated weekly news read aloud.

Cloudflare – Being explored for a personal publishing platform.

Apple Mac Studio M5 Ultra (512GB RAM) – Hardware recommendation surfaced by AI, relevant to local inference work.

Fathom – Meeting notetaker bot used on this call.

Fireflies.ai – Meeting notetaker/recording bot used on this call.


📎 SHARED RESOURCES

🔗 Links & Resources From the Call

Daniel Zivkovic

Forward Deployed Engineering guide:
https://magmainc.ca/guides/forward-deployed-engineering-model/

Video watching skill repo (transcribe/benchmark YouTube videos):
https://github.com/dzivkovi/video-intel/

"GIFT" link (Every.to community content):
https://www.youtube.com/live/JTvE7v_rMIw?si=L8qR-DoLltWTwM0u

Every.to pricing page:
https://every.to/pricing-all-plans

AIE World Fair conference playlist:
https://www.youtube.com/playlist?list=PLDyBmFH9HlVc

Patrick Chouinard

Inspiration video for the Astra accounting/tax-research task (Nate B. Jones' "recipe card" prompting concept):
https://www.youtube.com/watch?v=ix8SsXjBc7M

Fieldy ambient recorder product page:
https://shop.fieldy.ai/home

Paul Miller

Jcodemunch / CMUX tool:
https://jcodemunch.com/

Biggi Fraley

Interview referenced re: photo magnets bolt-on idea:
https://www.youtube.com/watch?v=N0NceZbY2_4

Ryan C

Granola — computer-based ambient note-taking alternative:
https://www.granola.ai/

Ty Wells

Ambient recorder device: Omi.me

Mentioned without links

Kris Larson referenced a LinkedIn post about developers not sleeping due to the "opportunity cost" of vibe coding, and Brandon Godosi's interview (via Chris Koerner on X) as an example of rapid AI-consulting income growth.


🔄 FOLLOW-UPS WORTH EXPLORING

Hemal Shah will post his RAG/Chinese-model question in the community forum for further offline review.

Paul Miller will check OpenRouter's model index and share it as a resource for model comparisons.

Patrick Chouinard will continue expanding AgentDeck's observability coverage across more VMs/harness installations.

Patrick Chouinard will have Fable 5.1 continue a large upgrade to Hermes' backend capacity.

Ty Wells will launch his ERP/business-advisor product to clients on the 15th, with a 10am webinar.

Ryan C will locate Tim Hildenbrandt on the community board and DM him to arrange a security review.

Tim Hildenbrandt will reach out to Ryan C via email/message once accessible, and try Astra for less-restrictive security auditing.

Kris Larson will continue posting questions on the community forum and exploring niche/business-association networking.

Juan Torres will build a target list of venue planners/coordinators and launch an outreach campaign plus in-person visits with free trials.

Juan Torres will evaluate adding printing capability to his currently fully digital photo-automation app.

Ryan C will test ChatGPT's computer-use/agent capability for video editing and report back to the group.

Shakur will continue optimizing outreach workflow and evaluate CRM/agentic OS adoption.

Patrick Chouinard will continue running daily Hermes jobs against Fieldy transcripts to surface new AI solution ideas, sharing outcomes weekly.

Patrick Chouinard will blog about using ChatGPT as a personalized morning newspaper.

Patrick Chouinard will continue developing a Cloudflare-based personal publishing platform for AI-assisted content.