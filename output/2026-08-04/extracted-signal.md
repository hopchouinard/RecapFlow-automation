## general

This coaching-call session brought together a distributed group of AI builders/consultants (Ty Wells, Morgan/mdcatc, Patrick Chouinard, Juan Torres, Alex Roca, Adam, Ryan C, Paul Miller hosting) to share weekly progress. Ty Wells demoed a "terrain/skin" system he built that lets any existing application's UI be completely reskinned (via a separate front-end layer hitting the same back-end APIs) without touching underlying code or endpoints — showing this applied to a Zendesk-replacement ticketing system, an ERP, and Uptime Kuma. Morgan (mdcatc) discussed rebuilding a driver for an obsolete Dymo label printer in Python (bypassing CUPS) as a way to salvage e-waste, plus updates on Class2Curb (school carpool product) and Heritage Plot. Patrick Chouinard described a new team-level knowledge management architecture at his employer, using Git/Azure DevOps as an "agentic memory" layer ("SharePoint for Agents") that merges individual and team knowledge with Claude-driven conflict resolution, and shared community resources on Codex-based code review plugins. Juan Torres reported a successful AI Booth photo-booth event, discussed scaling/fundraising strategy with Paul Miller, and exchanged personal-branding tips with Alex Roca. Alex Roca gave an update on his Claude Code corporate-training consulting business in Mexico and sought advice on deal-closing/contract-staging strategy for a real estate client. Adam and others discussed a hardware opportunity around obsolete penny-rounding cash registers.

## insights

- **Ty Wells:** A UI "reskin" layer can be built entirely on the front end, reusing existing back-end APIs/ACLs unchanged — meaning any application (ticketing system, ERP, monitoring tool) can get a completely new interface in under an hour without touching the underlying code or endpoints.
- **Ty Wells:** This reskinning approach is especially useful for multi-tenant products where different clients want different UI complexity — e.g., hiding technical detail from less sophisticated users while giving power users a denser view.
- **Morgan (mdcatc):** Software has become so cheap to produce that old, unsupported hardware (e.g., printers with dead drivers) can be given new life by having AI reverse-engineer the communication protocol and write a fresh driver/CLI — a viable "half day project" pattern for reviving e-waste.
- **Morgan (mdcatc):** AI can close the loop on hardware calibration by literally being shown a photo of physical output (e.g., a printed label) and asked to adjust its own resolution/positioning calculations — no manual tuning needed.
- **Morgan (mdcatc):** Much commercial software is bloated with unused features baked in for sales-checkbox reasons; custom-built software avoids that bloat because it's built specifically for the actual use case.
- **Patrick Chouinard:** Enterprise knowledge management should be built bottom-up at the team level (units of ~20-30 people) before attempting a "corporate brain," rather than starting with a top-down system ontology that stalls for months without shipping anything.
- **Patrick Chouinard:** Treat organizational knowledge like an object-oriented programming construct — objects with embedded assumptions and interfaces — rather than a monolithic corpus to be queried.
- **Patrick Chouinard:** Agentic memory should function as *behavioral* memory feeding context into an agent's actions/recommendations, not as a RAG system meant to be directly queried for facts.
- **Patrick Chouinard / Morgan:** Both found that heavily-specified, overly prescriptive prompts produce worse results from Opus/Claude/Fable than giving the model a clearly-described *problem* and letting it determine its own solution — mirrors classic consulting advice: describe the problem, not the solution, to avoid "commitment bias" locking the AI into a suboptimal literal interpretation.
- **Ryan C (chat):** Opus 5 was described as having "Fable level of quirks without the level of intelligence" — team consensus was to stick with Claude 4.8 rather than switch.
- **Paul Miller:** For consulting engagements, it's valuable to gate a full project behind a smaller, easily-approved "proof of concept" phase — this builds trust, lets the client's actual budget authority get comfortable, and creates a natural on-ramp to a bigger signed contract.
- **Paul Miller:** When evaluating an engagement, look beyond the code deliverable to the client's operational capability — who will support the app after delivery, is the business process stable, what other roles/skills does the client team need to bring.
- **Juan Torres:** High-end event/venue coordinators can become unpaid "salespeople" for a novel AI product once they see it work firsthand — offering one free/discounted showcase to a well-connected coordinator can generate outsized word-of-mouth reach.
- **mdcatc:** The main barrier to reviving/repurposing old hardware isn't feasibility, it's people lacking the technical knowledge — AI removes that gatekeeping requirement.

## qa

**Q (Morgan/mdcatc, to Ty Wells):** Your interface is sitting on its own server, hitting the original interface — is that how you're doing that?
**A (Ty Wells):** Yes. There are two approaches — subdomain the reskin app, or point it directly at the original's API endpoints; either way the back end and its endpoints stay untouched, and the skin just consumes the same APIs.

**Q (Patrick Chouinard):** You mentioned your reskin work was based on an open repo — for the Uptime Kuma reskin specifically, can I take a peek?
**A (Ty Wells):** Yes — there's an NPX installer at the bottom of the coast.algome.ai page; you can run it directly against any repo to generate a reskinned view.

**Q (Paul Miller):** How did you work out the hierarchical relationships in that reskinned UI?
**A (Ty Wells):** No extra work was needed — the hierarchy/data structure is already fully built into the underlying app; the reskin just presents that existing data differently, without changing any endpoints.

**Q (Paul Miller):** Once you build a hierarchy of team/corporate knowledge, how do you think you'll serve it back to people who want to query it?
**A (Patrick Chouinard):** It's not meant to be queried like a database/RAG — it's meant to be used transparently as context inside the co-work/Claude Code agent interactions, functioning as behavioral memory (e.g., "last time you did this, it was done that way") rather than a lookup system.

**Q (Alex Roca):** How does the Codex-as-reviewer plugin actually work — do I just install it and point it at a GitHub repo?
**A (Patrick Chouinard):** It's a legitimate plugin built by OpenAI specifically for Codex. Once set up, it creates a hook so that every time Claude Code finishes a coding activity, it sends the output to Codex via a headless call; Codex runs an adversarial code review against a dedicated system prompt, sends back a report, and Claude reads and acts on that report.

**Q (Alex Roca):** I've had five calls with a real estate client who's shared sensitive financial data, and I've already started building parts of the solution on spec — should I show them progress before any contract/payment, or wait?
**A (Paul Miller):** Show something tangible, but frame it explicitly as a paid proof-of-concept phase (not the full application) before the main project — this gives them confidence in your capability while creating a smaller, easier-to-approve financial commitment that primes them for the larger signed engagement; also get a draft contract in front of the actual budget-signing stakeholder now.

**Q (mdcatc):** I don't love Opus 5's responses — they're often strange, and I have to re-read to understand what it's answering. Any advice?
**A (Patrick Chouinard):** Trim your prompts/skills — Opus 5 needs far less context and instruction than Opus 4.8 did; be descriptive about the *problem* you want solved, not about *how* you want it solved, and it performs far better.

## tools

- **Claude Code / Claude (Opus 4.8 vs Opus 5)** — primary coding agent used across projects; group consensus favored 4.8 over Opus 5 for quality of responses.
- **Codex (OpenAI) + codex-plugin-cc** — used as an automated adversarial code reviewer hooked into Claude Code's output.
- **CMUX** — used by Ty Wells to manage/rotate between multiple Anthropic subscription accounts automatically.
- **Fable** — an AI tool Patrick Chouinard used to analyze and produce a 33-step stabilization plan for his home lab, and to architect the knowledge-management system; also referenced by Ryan C as his preferred model choice.
- **Uptime Kuma** — open-source uptime monitoring tool Ty Wells used as a demo target for his UI-reskinning system.
- **Azure DevOps (Git)** — used by Patrick's team as the backbone for team-level knowledge repos and CI-based "publish" pipelines.
- **ChatGPT** — used by Patrick to talk through and crystallize a vision document for the knowledge management project.
- **NotebookLM** — recommended by Paul Miller to Juan Torres for synthesizing Y Combinator pitch videos into pitching guidance.
- **Class2Curb** — Morgan's product for school carpool-line management, discussed as ready for outside feedback/clients.
- **Heritage Plot** — Morgan's mapping project, updated with scalar vector graphs over satellite imagery.
- **AI Booth** — Juan Torres's AI-powered photo booth application demoed at events.
- **ShipKit** — mentioned by Alex Roca as part of his tooling/workflow (context implies a starter-kit/boilerplate tool for client builds).
- **Python (direct-to-device CLI/UDP printing)** — used by Morgan to rewrite printer drivers without CUPS.
- **Next.js** — backend/dashboard framework Alex Roca is using for the real estate client project.
- **Y Combinator (as a resource, not a tool per se)** — recommended as a source of pitch-training material for fundraising.

## links

- https://coast.algome.ai — Ty Wells's "terrain" showcase platform where you can test/generate UI reskins of applications or point at a repo/URL.
- http://ttl.golf — Ty Wells's golf-related project where he applied and kept the new reskinned interface.
- https://data-terrain-showcase.vercel.app/t/the-holding-pool-ws8r19 — Ty Wells's reskin demo run against Morgan's Class2Curb site.
- https://class2curb.com/ — Morgan's carpool-pickup product site, shared for referrals.
- https://github.com/openai/codex-plugin-cc — OpenAI's official Codex plugin for Claude Code, used for automated code review.
- https://www.linkedin.com/posts/juan-torres-ai-engineering_i-made-a-game-its-called-ai-booth-activity... — Juan Torres's LinkedIn post about his AI Booth project.
- https://www.linkedin.com/posts/juan-torres-ai-engineering_economics-finance-datascience-activity... — additional Juan Torres LinkedIn post shared in chat.
- https://www.linkedin.com/posts/juan-torres-ai-engineering_datascience-ai-agenticsystems-activity... — additional Juan Torres LinkedIn post shared in chat.
- https://www.score.org/ — resource suggested to Juan Torres by Adam for business advice.
- https://fathom.video/customize — Fathom Notetaker bot info link (meeting tooling, incidental).
- https://fireflies.ai/privacy / Fireflies live notes link — Fireflies.ai Notetaker bot info (meeting tooling, incidental).

## decisions

- Ty Wells to launch "Island Flow" to clients in the Bahamas on September 15th, using the reskinned/custom-terrain UI approach.
- Patrick Chouinard and his manager/team to continue building out the team-level knowledge management system (Git/Azure DevOps based) and expand it toward merging into corporate-level knowledge later.
- Morgan (mdcatc) to wait for clients before further developing Class2Curb and Heritage Plot, but keep both ready to demo.
- Paul Miller to DM Juan Torres with ideas on scaling/transportation and potential industry partners (e.g., casinos, convention centers) for the AI Booth business.
- Juan Torres to look into applying for seed funding and to investigate a possible Y Combinator showcase in San Diego this year.
- Alex Roca to prepare a draft contract for his real estate client's key stakeholder and to hold off further sharing until formal sign-off, structuring the engagement into a paid initial "phase one" plus recurring bi-weekly champion calls over three months.
- Alex Roca to start bringing a media/photography person to his in-person workshops to create promotional reels for LinkedIn/Instagram, following Juan Torres's suggestion.
- Patrick Chouinard to spend the coming weekend rewriting scanner driver software for Mac (inspired by Morgan's printer-driver project).
- Adam to consider bringing the obsolete penny-rounding cash register hardware problem to the group/Claude for a potential low-risk exploratory solution.