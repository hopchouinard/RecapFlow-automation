📝 SUMMARY

This week's call covered practical debugging, cost-saving tactics, career mentorship, and a thought-provoking discussion about staying active thinkers in an AI-curated world. Members shared lessons on RAG debugging and model selection, live demos of home-built observability tooling, and real numbers on cutting production costs by switching models. A recurring theme: technical skill alone isn't enough — the edge comes from combining technology with domain knowledge, relationships, and deliberate intent. The conversation closed on a memorable framing: with models this capable, humans — not AI — are the bottleneck on connecting insights, so it's on us to configure our tools to challenge us rather than comfort us.

💡 KEY INSIGHTS

Set smart-model baselines first — otherwise you can't tell if failures come from the model, retrieval, or prompt.

Check RAG retrieval before blaming the LLM: junk in, junk out.

Long agent sessions re-send the entire growing context (500k–800k+ tokens) each response — one-shot requests are cheaper than always-on agents.

Switching a production workflow to GLM 5.3 cut per-run cost from ~$0.80–$1.10 to ~$0.09 with no perceptible quality drop.

Use OpenRouter's independent task-based model rankings as a starting point for comparisons.

Build observability around AI usage: track tokens, sessions, and unresolved attention — treat LLM usage like infrastructure needing monitoring.

GPT's computer-use can functionally replace a QA hire — it finds bugs and proposes fixes for another model to implement.

Pair "accounting-precision" models for admin work with a second model for peer review and blind-spot checking.

Coding-only skills are oversaturated — pair code with an outside domain; the best niches are ones nobody yet associates with AI.

Hunt for past workflow blockers that weren't cost-effective to fix — AI removes that barrier, and firsthand pain points are validated opportunities.

Legacy late-90s internal software in factories and small franchises is a real, underexploited modernization market.

Leverage existing business-network connections over purely technical ones — devs already crowd the technical space.

Beware "Instagrammified" AI success stories — survivorship bias and hidden networks are everywhere.

Narrate daily frustrations to ChatGPT instead of brainstorming — most demo ideas came from this.

Configure assistants to be confrontational or "brutal," never agreeable, to avoid yes-man behavior.

Architecture pattern: a cheap dispatcher with full context/memory routes tasks to a smarter, trimmed-context tier.

Invert the human→AI harness: humans are an expensive, low-parallelism resource used only for judgment calls.

"Before writing was difficult, now reading is difficult" — design interfaces to reduce cognitive load when consuming AI output.

The real leverage: HGI, not AGI — humans connecting the dots remains the limiting factor.

❓ KEY Q&A

Q: Qwen vs GLM 5.3 for a RAG agent, since GLM 5.3 keeps flipping answers? (Hemal Shah)
A: Check OpenRouter's independent task-based rankings as a starting point. (Paul Miller) Hemal ran 10 iterations, hit a $100 Gemini cost cap before finishing 50 tests, and used Qwen as a non-deterministic LLM judge.

Q: Why doesn't Hermes show a weekly usage bar? (Juan Torres)
A: Hermes isn't subscription-tied — it uses Codex capacity or GLM via OpenRouter API. (Patrick Chouinard)

Q: Anything built with the "Pi" agent from last week? (Paul Miller)
A: No — token-maxing Astra and Fable instead; Pi may come later via a custom harness connecting Claude Code and Codex through T3 Code. (Patrick Chouinard)

Q: Did you try OpenAI's new model? (Paul Miller)
A: Community says GPT-6/Astra is great for coding but overdoes "thinking." Still using Fable 5.1 at medium thinking paired with GPT for peer review. (Daniel Zivkovic)

Q: How do you handle a customer whose accountant insists on a specific chart of accounts? (Paul Miller)
A: The business advisor asks about business type first and configures accordingly — the front end guides requirements while the back end is already built. (Ty Wells)

Q: ~10% of my RAG tool's code is ShipKit — can I get security help without violating sharing rules? (Tim Hildenbrandt)
A: Post on the forum without raw code; Ryan C offered to run Scott's CC security review suite via email/DM since Tim's membership level doesn't allow board messaging yet. (Paul Miller / Ryan C)

Q: Asked Claude how to host your app securely? (Paul Miller)
A: Yes, but Opus and Fable each gave conflicting answers. (Tim Hildenbrandt)

Q: Is this a hobby, or do you need to make money? (Daniel Zivkovic)
A: I'd like to make money; struggling to find where I fit even after 38 years in IT. (Kris Larson) Paul suggested a chamber of commerce; Kris found the Rochester Chamber costly and already covered by someone similar.

Q: Plugged your system into venues' social media during events? (Patrick Chouinard, to Juan)
A: Great idea later once trust is built; meanwhile he emails images to venue planners to post themselves. (Juan Torres)

Q: What is Fieldy? (Daniel Zivkovic)
A: A pendant recorder that records ambiently 24/7 (alternatives: Omi, Limitless). No raw audio, but tracks trends and is queried by Hermes via WebSocket. It can differentiate speakers roughly but not full diarization. Recommended over manually-triggered tools like Plaud, Granola, or Pocket. (Patrick Chouinard / Ty Wells)

Q: Is the personalized news feed built via memory or a skill? (Daniel Zivkovic)
A: Just a ChatGPT scheduled task — personalization comes from ongoing daily conversation. (Patrick Chouinard)

Q: Can I keep my $20 ChatGPT plan to use Astra for Hermes? (Ryan C)
A: No, you need the $100 plan. (Patrick Chouinard)

Q: How does Agent Deck's UI relate to human cognitive effort? (Kris Larson)
A: It's built to efficiently use the human's cognitive "tokens" — writing used to be the hard part; now consuming AI output is. (Patrick Chouinard)

🛠️ TOOLS AND CONCEPTS MENTIONED

Codex (OpenAI) / "Astra" – Coding agent/model. Great for coding bursts, computer-use QA, and less-restrictive security auditing; requires the $100 plan.

Claude / "Fable" (Opus, Sonnet, Claude Code, Fable 5.1) – Anthropic's models for coding, review, and business/creative thinking; Opus 5 implements fixes found via computer-use QA.

GLM 5.3 / GLM 5.3 Flash – Adopted for production workflow, cutting costs ~90%.

Qwen – Used as a non-deterministic LLM-as-judge.

Gemini – Expensive model tried first for RAG baseline testing.

OpenRouter – Model aggregator with task-based ranking index.

AgentDeck – Patrick's observability dashboard for tracking agent sessions and reducing cognitive load.

Hermes – Patrick's "infrastructure operator" agent system; ingests Fieldy, email, and other data.

Luna – Cheap default dispatcher agent profile within Hermes, holding full context/memory.

T3 Code – Harness running Claude Code and Codex under Patrick's monitored setup.

Prometheus / Alertmanager / Loki / Grafana / NATS / Authentik / Traefik – Backend monitoring/infrastructure stack behind Patrick's home lab.

ShipKit – Starter repo Tim used for his RAG tool.

Ollama – Local model runtime powering Tim's local-only RAG setup.

Scott's CC Security Review Suite – Security review package offered by Ryan C.

Every.to – Paid AI newsletter/community for early model reviews; also source of the Compound Engineering Framework.

Jcodemunch / CMUX (jcodemunch.com) – Tool that reduced coding usage for Tim and Ty.

GrokBot – Used with a LinkedIn connector to identify SMB pain points for lead gen.

ChatGPT (voice mode / computer-use / scheduled tasks) – Morning news discussion, "news radar," and tested for automated video editing.

Fieldy (.AI) – Ambient necklace recorder for continuous life/context logging (~$150/year).

Omi (Omi.me) and Limitless – Alternative ambient note-taking devices.

Plaud / Granola / Pocket – Manually-triggered note-taking apps, rejected in favor of Fieldy.

EC2 / Auto Scaling Group / Load Balancer (AWS) – Infrastructure Juan needs to scale his photo-automation app.

Custom Chrome extension – Ty Wells' browsing-context capture tool.

Kindle text-to-speech, Cloudflare, Apple Mac Studio M5 Ultra (512GB RAM) – News reading aloud, publishing platform exploration, and local-inference hardware.

Fathom / Fireflies.ai – Meeting notetakers used on this call.

📎 SHARED RESOURCES

Daniel Zivkovic
Forward Deployed Engineering guide: https://magmainc.ca/guides/forward-deployed-engineering-model/
Video watching skill repo: https://github.com/dzivkovi/video-intel/
"GIFT" link (Every.to community content): https://www.youtube.com/live/JTvE7v_rMIw?si=L8qR-DoLltWTwM0u
Every.to pricing: https://every.to/pricing-all-plans
AIE World Fair conference playlist: https://www.youtube.com/playlist?list=PLDyBmFH9HlVc

Patrick Chouinard
Nate B. Jones' "recipe card" prompting video (inspiration for the Astra accounting task): https://www.youtube.com/watch?v=ix8SsXjBc7M
Fieldy product page: https://shop.fieldy.ai/home

Paul Miller
Jcodemunch / CMUX: https://jcodemunch.com/

Biggi Fraley
Interview re: photo magnets bolt-on idea: https://www.youtube.com/watch?v=N0NceZbY2_4

Ryan C
Granola: https://www.granola.ai/

Ty Wells
Ambient recorder device: Omi.me

Mentioned without links
Kris Larson referenced a LinkedIn post about developers losing sleep over vibe-coding "opportunity cost," and Brandon Godosi's interview (via Chris Koerner on X) as an example of rapid AI-consulting income growth.

🔄 FOLLOW-UPS WORTH EXPLORING

Hemal Shah will post his RAG/Chinese-model question in the community forum.

Paul Miller will check and share OpenRouter's model index as a comparison resource.

Patrick Chouinard will expand AgentDeck's observability coverage, have Fable 5.1 continue a large Hermes backend upgrade, keep running daily Hermes jobs against Fieldy transcripts (sharing outcomes weekly), blog about ChatGPT as a personalized morning newspaper, and continue his Cloudflare-based publishing platform.

Ty Wells launches his ERP/business-advisor product on the 15th with a 10am webinar.

Ryan C will DM Tim Hildenbrandt to arrange a security review, and test ChatGPT's computer-use for video editing.

Tim Hildenbrandt will reach out to Ryan C via email once accessible, and try Astra for security auditing.

Kris Larson will keep posting on the forum and exploring niche/business-association networking.

Juan Torres will build a venue-planner outreach list with free trials and in-person visits, and evaluate adding printing to his photo-automation app.

Shakur will continue optimizing outreach and evaluate CRM/agentic OS adoption.