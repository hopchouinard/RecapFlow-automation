## general

This call opened with informal banter about heavy token/usage burn across Codex ("Astra") and Claude ("Fable") plans before moving into a round-robin of technical and business updates. Hemal Shah sought help debugging a RAG agent tested against Chinese models (GLM 5.3, Qwen), prompting Daniel Zivkovic's now-recurring advice to establish a baseline with an expensive model before optimizing for cost, and to verify retrieval quality before blaming the LLM ("junk in, junk out"). Patrick Chouinard demoed his self-built observability tool, "AgentDeck," for monitoring multiple concurrent AI harnesses (Claude, Codex, Hermes, T3 Code) and described a personal home-lab monitoring stack, while also sharing that switching a production workflow entirely to GLM 5.3 cut per-run costs by ~90%. Ty Wells discussed using GPT's computer-use feature as an automated QA replacement ahead of an ERP product launch on the 15th, and Tim Hildenbrandt, a new member, raised concerns about sharing code that partially derives from the ShipKit repo, prompting Ryan C to offer a security review.

The second major thread was a mentoring conversation with Kris Larson, a 38-year IT veteran trying to find paid opportunities in the AI/vibe-coding space. The group (Daniel, Paul Miller, Patrick, Ty, Tim, Ryan C, Shakur, Juan Torres) converged on a consistent message: coding skill alone is commoditized, and the real opportunity lies in pairing technical ability with an existing business network, an outside passion, or an underserved niche (e.g., outdated legacy software in factories, previously "not worth automating" workflow blockers). Ryan C and Paul emphasized in-person hustle and leveraging non-technical relationships over comparing oneself to survivorship-biased success stories online. Alongside this, Juan Torres discussed scaling his event photo-automation business (with Patrick suggesting live social-media integration and Biggi Fraley suggesting photo magnets as a higher-margin add-on), and Ryan C shared a real-estate SEO win plus interest in computer-use agents for video editing.

The call's final arc turned reflective and philosophical, focused on how humans should consume AI-curated information without becoming passive. Patrick, Daniel, and Ty each described deliberately configuring their AI assistants to challenge rather than flatter them, and to surface a personalized "what you don't know you need to know" feed rather than a purely tailored echo chamber. Patrick detailed his Hermes agent architecture (a cheap "Luna" dispatcher routing to a smarter "Astra" tier), his use of an ambient Fieldy recorder to mine daily conversation for new business ideas, and his design philosophy behind AgentDeck as a tool that flips the usual human→AI relationship, treating human attention as a scarce resource AI should conserve rather than consume. This culminated in his "HGI, not AGI" framing — humans, not the models, are now the bottleneck on connecting disparate insights — and closed with lighter, personal chat.

## insights

- Long agent sessions burn through weekly token limits fast because every response re-sends the entire growing context (500k–800k+ tokens); one-shot architecture requests are cheaper than leaving an agent running continuously. (Patrick Chouinard)
- Always establish a baseline with the smartest/most expensive model first to confirm an approach can work before optimizing for cost — otherwise failures can't be attributed to model, retrieval, or prompt. (Daniel Zivkovic)
- "Junk in, junk out" — verify the RAG system is retrieving relevant content before blaming the LLM. (Daniel Zivkovic)
- OpenRouter maintains an independent ranking/index of models by task (coding, agentic, etc.), a good starting point for model comparisons. (Paul Miller)
- Switching a production workflow ("Recap Flow") entirely to GLM 5.3 dropped per-run cost from ~$0.80–$1.10 to ~$0.09 with no perceptible quality loss. (Patrick Chouinard)
- Built "AgentDeck" as a pure observability layer tracking token usage, session status, and unresolved-attention notifications across Claude, Codex, Hermes, and T3-Code sessions on multiple hosts. (Patrick Chouinard)
- Even businesses not fully "doing AI" could benefit from token/agent observability tooling — treating LLM usage like infrastructure needing monitoring. (Juan Torres)
- Distinguishes "accounting-style precision" (structured admin/finance tasks) from true creative/exploratory thinking; pairs Fable 5.1 (medium thinking) with GPT for peer review/blind-spot checking. (Daniel Zivkovic)
- Contrary to general consensus that Fable is better at "thinking," Astra (GPT-6/Codex) outperformed Fable on a multi-hour government/estate admin task, running independently ~3 hours to produce a full plan. (Patrick Chouinard)
- GPT's computer-use capability is strong enough to functionally replace a hired QA person — it finds bugs and proposes fixes, handed to Opus 5 to implement. (Ty Wells)
- His ERP concept differentiates by embedding a business advisor from day one, vetting ideas before software setup and continuously re-advising as goals/data change. (Ty Wells)
- For security auditing, Astra is less restrictive/picky than Fable, which stops more often during review tasks. (Patrick Chouinard)
- Uses AI to watch/transcribe YouTube videos (including paid Every.to sessions) as a human-in-the-loop benchmark to validate AI/model hype claims. (Daniel Zivkovic)
- The market is oversaturated for coding-only skills; survival requires pairing coding with an outside passion/business domain. (Daniel Zivkovic)
- Real opportunity lies in leveraging existing business-network connections rather than pure technical connections, since experienced developers already flood that space. (Paul Miller)
- The best niches are ones nobody yet associates with AI; commoditized categories (SEO, marketing, dashboards) are saturated. (Patrick Chouinard)
- Look for past workflow "blockers" that were previously not cost-effective to fix — AI removes that cost barrier, creating validated opportunities from firsthand pain points. (Ty Wells)
- Many businesses (factories, small franchises) still run outdated late-90s internal software and pay for modernization — an underexploited market. (Tim Hildenbrandt)
- Beware comparing yourself to "Instagrammified" AI success stories — survivorship bias and hidden pre-existing networks/luck are common. (Ryan C)
- Personal branding/thought leadership mainly yields easier interviews and credibility, not direct revenue; even large-following creators see inbound lead quality drop as the space saturates. (Daniel Zivkovic)
- Practical lead-gen method: use a LinkedIn-connected bot to identify top SMB pain points, match to skill set/location, then build demos/content/videos around those niches. (Paul Miller)
- Uses daily verbal conversations with ChatGPT — narrating daily frustrations rather than brainstorming — to surface AI solution ideas organically; most weekly demos originate this way. (Patrick Chouinard)
- Hermes architecture: "Luna" is a cheap default dispatcher with full context/memory; specific tasks route to a trimmed-context "Astra" tier for more intelligence, balancing cost and capability. (Patrick Chouinard)
- Uses a Fieldy ambient pendant recorder that Hermes analyzes daily to surface new ideas and answer "what did we discuss earlier" via WebSocket. (Patrick Chouinard)
- Feeds multiple context streams (Chrome extension, emails, screen recordings, TikTok) into his own agent, manually tagging context cues to improve advisory accuracy. (Ty Wells)
- Daily "news radar" trick: ask ChatGPT to determine what news matters based on everything it knows, then hold an evolving daily conversation thread rather than a static digest. (Patrick Chouinard)
- Accumulating a feed without interacting with it degrades in usefulness — interaction is what builds and refines memory/context. (Patrick Chouinard)
- Configures news feed as an "anti-pattern" — asks AI to surface the 10 things he should know but doesn't, to avoid tunnel vision from purely personalized feeds. (Ty Wells)
- Uses a base system prompt instructing AI to be "confrontational" and "never agree," avoiding yes-man behavior. (Patrick Chouinard)
- Similarly configures AI assistants to be "brutal" rather than agreeable. (Daniel Zivkovic)
- Runs a weekly Friday-evening curation workflow pulling from sources like the Toronto Star into a "weekend paper" read aloud via Kindle. (Daniel Zivkovic)
- Uses ChatGPT each morning as a replacement newspaper, discussing news conversationally as his first activity of the day. (Patrick Chouinard)
- The real leverage of AI comes from a human "connecting the dots" across disparate information — AI won't self-assemble insights; frames this as "HGI, not AGI" (human general intelligence as the limiting factor). (Patrick Chouinard)
- "Agent Deck" is designed to invert the typical human→AI harness: letting AI efficiently communicate with humans, treating human-in-the-loop as an expensive, low-parallelism resource used only for judgment calls. (Patrick Chouinard)
- "Before writing was difficult, now reading is difficult" — interfaces should reduce human cognitive load when consuming AI output. (Patrick Chouinard)

## qa

**Q (Hemal Shah):** Any recommendation on Qwen vs GLM 5.3 for a RAG agent, since GLM 5.3 keeps flipping answers across test iterations?
**A (Paul Miller):** Check OpenRouter's independent model ranking by task as a starting point.

**Q (Daniel Zivkovic):** Is your RAG actually returning relevant content? Did it ever work with a more expensive model to establish a baseline?
**A (Hemal Shah):** 10 iterations, $100 spent on Gemini, hit the cost cap before finishing all 50 tests; used Qwen as a non-deterministic LLM judge instead.

**Q (Juan Torres):** Why doesn't Hermes show the weekly usage bar like other harnesses?
**A (Patrick Chouinard):** Hermes isn't tied to a subscription directly — it either uses Codex capacity or connects to GLM via OpenRouter API, which has no subscription bar.

**Q (Paul Miller):** Did you do anything with the "Pi" agent mentioned last week?
**A (Patrick Chouinard):** No — spent the time token-maxing Astra and Fable instead; Pi will likely be built later via a custom harness connecting Claude Code and Codex through T3 Code.

**Q (Paul Miller):** Did you try OpenAI's new model?
**A (Daniel Zivkovic):** No — community feedback suggests GPT-6/Astra is great for coding but overdoes "thinking," so he continues using Fable 5.1 at medium thinking paired with GPT for peer review.

**Q (Paul Miller):** How do you handle a customer whose accountant insists on a specific chart-of-accounts setup?
**A (Ty Wells):** The business advisor asks about business type first and configures the chart of accounts accordingly; the front end guides requirement-gathering while the back end is already built.

**Q (Tim Hildenbrandt):** ~10% of my RAG tool's code is from ShipKit — can I get security help without violating sharing rules?
**A (Paul Miller / Ryan C):** Post on the community forum without sharing raw code publicly; Ryan C offered to run it through "Scott's CC security review suite" via email/DM since Tim's membership level doesn't allow board messaging yet.

**Q (Paul Miller):** Have you asked Claude how to host your app securely, using a paid subscription with full codebase context?
**A (Tim Hildenbrandt):** Yes, but got conflicting answers between Opus and Fable, each creating new conflicts.

**Q (Daniel Zivkovic):** Kris, is this a hobby, or do you need to make money?
**A (Kris Larson):** I'd like to make money; struggling to find where I fit even after 38 years in IT.

**Q (Paul Miller):** Have you thought about a business association or local chamber of commerce?
**A (Kris Larson):** Yes, looked into the Rochester Chamber of Commerce, but access is harder/costlier and someone's already doing similar work there.

**Q (Patrick Chouinard, to Juan):** Have you thought about plugging your system directly into venues' social media during events?
**A (Juan Torres):** Great idea for later once trust is built; meanwhile he emails images to venue planners/social coordinators to post themselves.

**Q (Daniel Zivkovic):** What is Fieldy?
**A (Patrick Chouinard / Ty Wells):** A pendant recorder that records ambiently 24/7 (alternatives: Omi, Limitless); doesn't record raw audio but tracks trends, queried by Hermes via WebSocket.

**Q (Daniel Zivkovic):** Does it distinguish speakers?
**A (Patrick Chouinard):** Not exact diarization, but differentiates Patrick talking, someone else talking, and media being consumed.

**Q (Daniel Zivkovic):** Which ambient recording system would you recommend?
**A (Patrick Chouinard):** Fieldy, because it's true passive 24/7 recording versus manually-triggered tools like Plaud, Granola, or Pocket.

**Q (Daniel Zivkovic):** Is the personalized news feed built via memory or an installed skill?
**A (Patrick Chouinard):** Nothing special — just a ChatGPT scheduled task; personalization comes from ongoing daily conversation.

**Q (Ryan C):** Can I keep my $20 ChatGPT plan, or do I need the $100 plan to use Astra for Hermes?
**A (Patrick Chouinard):** If you touch Astra, yes, you need the $100 plan.

**Q (Kris Larson, paraphrased):** How does Agent Deck's UI relate to human cognitive effort?
**A (Patrick Chouinard):** It's built to make efficient use of the human's cognitive "tokens" — reducing reading/cognitive load, since writing used to be the hard part and now reading (consuming AI output) is.

## tools

- **Codex (OpenAI) / "Astra"** – Coding agent/model tier; heavily used, praised for coding bursts, computer-use QA, less-restrictive security auditing, but inconsistent for deep "thinking" tasks; requires the $100 plan.
- **Claude / "Fable" (Opus, Sonnet, Claude Code, Fable 5.1)** – Anthropic model family used for coding, review, and business/creative thinking.
- **Opus 5** – Used to implement fixes identified by computer-use QA.
- **GLM 5.3 / GLM 5.3 Flash** – Chinese model tested for RAG and adopted for production workflow, cutting costs ~90%.
- **Qwen** – Chinese model used as a non-deterministic LLM-as-judge.
- **Gemini** – Expensive model tried first for RAG baseline testing.
- **OpenRouter** – Model aggregator/marketplace with task-based ranking index.
- **AgentDeck / "Agent Deck"** – Patrick's observability dashboard/harness for tracking multiple AI agent sessions and minimizing human cognitive load when consuming AI output.
- **Hermes** – Patrick's personal "infrastructure operator" agent system; ingests Fieldy, email, and other data.
- **Luna** – Cheap default dispatcher agent profile within Hermes holding full context/memory.
- **T3 Code** – Harness running Claude Code and Codex under Patrick's monitored setup.
- **Prometheus / Alertmanager / Loki / Grafana / NATS / Authentik / Traefik** – Backend monitoring/infrastructure stack behind Patrick's home lab.
- **ShipKit** – Starter repo Tim Hildenbrandt used as a base for his RAG tool.
- **Ollama** – Local small-model runtime for Tim's local-only RAG setup.
- **Scott's CC Security Review Suite** – Security/performance review package offered by Ryan C.
- **Every.to** – Paid AI newsletter/community Daniel follows for early model reviews.
- **Compound Engineering Framework** – Coding/SDLC framework (via Every.to) Daniel uses for development work.
- **Jcodemunch / CMUX** (jcodemunch.com) – Tool/agent that reduced coding usage for Tim and Ty.
- **GrokBot** – Used with a LinkedIn connector to identify SMB pain points for lead generation.
- **ChatGPT (voice mode / computer-use / scheduled tasks)** – Used for morning news discussion, "news radar" tasks, and tested for automated video editing.
- **Fieldy (.AI)** – Ambient necklace recorder for continuous life/context logging (~$150/year).
- **Omi (Omi.me)** – Alternative ambient note-taking device.
- **Limitless** – Another note-taking device (subscription expiring).
- **Plaud / Granola (granola.ai) / Pocket** – Manually-triggered note-taking apps, rejected in favor of Fieldy's ambient recording.
- **EC2 / Auto Scaling Group / Load Balancer (AWS)** – Infrastructure Juan Torres needs for scaling his photo-automation app.
- **Chrome extension (custom)** – Built by Ty Wells to capture browsing session context.
- **Kindle (text-to-speech)** – Used to have curated weekly news read aloud.
- **Cloudflare** – Being explored for a personal publishing platform.
- **Apple Mac Studio M5 Ultra (512GB RAM)** – Hardware recommendation surfaced by AI, relevant to local inference work.
- **Fathom** – Meeting notetaker bot used in this call.
- **Fireflies.ai** – Meeting notetaker/recording bot used in this call.

## links

- https://magmainc.ca/guides/forward-deployed-engineering-model/ — Daniel Zivkovic's "Forward Deploying Engineering" article/model guide.
- https://github.com/dzivkovi/video-intel/ — Daniel Zivkovic's "video watching skill" repo for transcribing/benchmarking YouTube videos.
- https://www.youtube.com/watch?v=ix8SsXjBc7M — Patrick Chouinard's inspiration video for the Astra accounting/tax-research task (Nate B. Jones' Astra "recipe card" prompting concept).
- https://www.youtube.com/live/JTvE7v_rMIw?si=L8qR-DoLltWTwM0u — Daniel Zivkovic's "GIFT" link, tied to Every.to community content.
- https://every.to/pricing-all-plans — Every.to pricing page, referenced by Daniel Zivkovic.
- https://jcodemunch.com/ — Paul Miller's shared link for Jcodemunch/CMUX tool.
- https://www.youtube.com/playlist?list=PLDyBmFH9HlVc — AIE World Fair conference playlist, shared by Daniel Zivkovic for Kris Larson.
- https://www.youtube.com/watch?v=N0NceZbY2_4 — Biggi Fraley's interview referenced re: photo magnets bolt-on idea.
- https://www.granola.ai/ — Ryan C's suggested computer-based ambient note-taking alternative.
- https://shop.fieldy.ai/home — Fieldy ambient recorder product page, shared by Patrick Chouinard.
- Omi.me — Ty Wells' ambient recorder device link.
- LinkedIn post referenced by Kris Larson about developers not sleeping due to "opportunity cost" of vibe coding (no URL given).
- Brandon Godosi interview (via Chris Koerner on X), referenced by Kris Larson as an example of rapid AI-consulting income growth (no URL given).

## decisions

- Hemal Shah to post his RAG/Chinese-model question in the community forum for further offline review.
- Paul Miller to check OpenRouter's model index and share it as a resource for model comparisons.
- Patrick Chouinard to continue expanding AgentDeck's observability coverage across more VMs/harness installations.
- Patrick Chouinard to have Fable 5.1 continue a large upgrade to Hermes' backend capacity.
- Ty Wells to launch his ERP/business-advisor product to clients on the 15th, with a 10am webinar.
- Ryan C to locate Tim Hildenbrandt on the community board and DM him to arrange a security review.
- Tim Hildenbrandt to reach out to Ryan C via email/message once accessible, and try Astra for less-restrictive security auditing.
- Kris Larson to continue posting questions on the community forum and exploring niche/business-association networking.
- Juan Torres to build a target list of venue planners/coordinators and launch an outreach campaign plus in-person visits with free trials.
- Juan Torres to evaluate adding printing capability to his currently fully digital photo-automation app.
- Ryan C to test ChatGPT's computer-use/agent capability for video editing and report back to the group.
- Shakur to continue optimizing outreach workflow and evaluate CRM/agentic OS adoption.
- Patrick Chouinard to continue running daily Hermes jobs against Fieldy transcripts to surface new AI solution ideas, sharing outcomes weekly.
- Patrick Chouinard to blog about using ChatGPT as a personalized morning newspaper.
- Patrick Chouinard to continue developing a Cloudflare-based personal publishing platform for AI-assisted content.