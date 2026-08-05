=== SESSION ===
date: Not explicitly stated in transcript (referenced as "today...Tuesday")
duration_estimate: ~91 minutes (00:00:00–01:31:24 timestamp range)
main_themes: AI-assisted software development workflows (Claude, Codex, Fable), UI/UX "reskinning" of existing applications, hardware/legacy-system revival projects, enterprise knowledge management architecture, AI consulting business development (photo booth events, corporate Claude Code training), sales/fundraising strategy discussion

<!--SEGMENT
topic: Introductions and personal catch-up
speakers: Patrick Chouinard, Ty Wells, Paul Miller, Alexandra Spalato, mdcatc
keywords: meeting recording, golf, travel, New Zealand, Australia, time zones, Argentina, Europe, attendance
summary: Casual opening banter covering attendance, travel logistics (Paul Miller returning from Australia to New Zealand), and the time-zone challenges of coordinating a globally distributed group across Europe, Argentina, and the South Pacific. Establishes who is present for the session.
-->

[00:00:00] Patrick Chouinard: This meeting is being recorded.
[00:00:42] Ty Wells: I was outside and I finally made it back to my office. So I went full circle. How's it going?
[00:00:57] Paul Miller: How's the golf game going, Ty?
[00:01:00] Ty Wells: I played Sunday, then had to go back out yesterday to make up for it.
[00:01:21] Ty Wells: Hey, Alexandra.
[00:01:23] Alexandra Spalato: First time I can come to this meeting because I was in Europe and it was always at midnight.
[00:01:33] Alexandra Spalato: <Q>Months that I have not seen Brandon... What is he doing?</Q>
[00:01:53] Patrick Chouinard: <A>He's working on an EMS application — this new business that he just started, and he's going all cylinders. He's here a week a month right now on a special contract.</A>
[00:02:25] Patrick Chouinard: Hey, Mr. Morgan.
[00:02:36] Paul Miller: I'm back from the Western Isle of New Zealand, Australia. Hopefully in New Zealand for the next month — don't want to do any more travel. It's three or four hours each way to fly there.
[00:03:31] Alexandra Spalato: Australia, New Zealand — very difficult on time zones. I'm in Argentina, so I can communicate with Europe and the rest, but Asia and Australia/New Zealand are always problematic.
[00:04:03] Paul Miller: Looks like we've got everyone online. I'm helping host today.

<!--SEGMENT
topic: Ryan's website builds and Codex security review
speakers: Ryan C, Paul Miller, Patrick Chouinard
keywords: Claude, Codex, security review, private jet website, estate agency website, interactive map, digital shelf labels, SEL strips, Scott, Asda
summary: Ryan reports on client website projects built in Claude, including a private jet spec site and an estate agency site with an upcoming interactive property map. He confirms Codex is proving effective as an automated security checker following a peer demo by Scott, and the group briefly discusses retail digital shelf-label technology.
-->

[00:04:46] Paul Miller: <Q>Ryan, how's it all going over there?</Q>
[00:05:08] Ryan C: <A>I built a spec site for a private jet company [tool:Claude] with some video scroll animation, inspired by stuff on Instagram. I also shared an estate agency website I've been building. I'll be building an interactive map for an estate I'm involved in selling, with photography and videography sewn in — still in planning stage.</A>
[00:05:49] Paul Miller: <Q>Will you be developing that in Claude or Codex [tool:Codex]?</Q>
[00:05:58] Ryan C: <A>All in Claude. I only used Codex as a security checker at the end, part of Scott's CC security review — he finally went through it last week. It's pretty good, catching a lot of stuff I wouldn't have caught otherwise.</A>
[00:06:30] Paul Miller: I'm still chasing the retailer guys about the screen/digital label project.
[00:06:49] Ryan C: They're doing digital labels now — shelf edge labels (SELs), shelf edge label strips [tool:digital shelf labels]. ▶ At scale (hundreds of stores, hundreds of units per store) the per-unit price becomes reasonable.
[00:08:17] Patrick Chouinard: ▶ Scott posted an independent interactive HTML file documenting his CC security review presentation as a comment on last week's recap post [link:Scott's HTML documentation of CC security review] — worth downloading and reviewing.

<!--SEGMENT
topic: Ty's terrain reskinning demo — support and ERP systems
speakers: Ty Wells, Paul Miller, mdcatc, Juan Torres
keywords: terrain, reskin, Zendesk replacement, ERP system, CMUX, intent capsules, Anthropic accounts, front-end UI, ACLs, dashboard
summary: Ty demonstrates his self-built system ("the field") that queues coding jobs across multiple Anthropic accounts using "intent capsules," then showcases a UI reskinning technique ("terrain") that lets him restyle an existing Zendesk-replacement support app and a full ERP system without touching backend code or endpoints. He built the ERP reskin in under an hour.
-->

[00:09:39] Ty Wells: I'm using CMUX [tool:CMUX] here — these are my Anthropic subscription accounts, tracked because I needed a way to automatically move between accounts instead of doing it manually. I have "intent capsules" that build a terse interpretation of what I want done, built at peak context, so a cold session produces exactly what I want.
[00:11:00] Ty Wells: I built a replacement for Zendesk [tool:Zendesk] — typical tickets/reports UI. What I've built is a "terrain" system that puts a skin over the UI so you can change the interface without touching the code — strictly front-end.
[00:13:36] Ty Wells: ▶ All the ACLs still apply — this is just a different lens on the same data, like scanning a playground to instantly see what's going on.
[00:16:12] Ty Wells: <Q>Anybody want to guess how long it took me to build this new skin?</Q>
[00:16:26] Paul Miller: Four days?
[00:16:27] mdcatc: This morning. Four hours.
[00:16:29] Ty Wells: <A>I built that this morning in under an hour, probably about 30 minutes.</A>
[00:16:36] Paul Miller: <Q>How did you work out the hierarchical relationships in that?</Q>
[00:16:47] Ty Wells: <A>I don't have to — that's already built into the app. I'm just changing the terrain that operates on the same data; I didn't change any endpoints or backend.</A>
[00:17:37] Ty Wells: This is my ERP system [tool:custom ERP system] — receivables, payables, everything — now with a different skin, started just before this meeting.
[00:19:00] Ty Wells: ▶ The thing about it is I can do that for any project, any code base — I don't even need the code base, just an understanding of its layout, and I put a skin on top to make it more user-friendly.
[00:19:28] Paul Miller: <Q>So you're interacting at the HTML presentation level? Not going down to the API?</Q>
[00:19:36] Ty Wells: <A>No, that has to already be there — I take an existing app and reskin it.</A>

<!--SEGMENT
topic: Uptime Kuma reskin and multi-tenant application launch
speakers: Ty Wells, Patrick Chouinard, Juan Torres, mdcatc
keywords: Uptime Kuma, terrain, multi-tenant, Island Flow, NPX, open repo, work orders, dispatcher, field service
summary: Ty demonstrates reskinning the open-source monitoring tool Uptime Kuma using his "terrain" tool, showing a public repo/NPX install anyone can run against their own instance. He explains this reskinning approach is central to his upcoming September 15 launch of "Island Flow" in the Bahamas, letting each client see a custom UI without changing core code — useful for multi-tenant setups.
-->

[00:19:57] Ty Wells: Anybody familiar with Kuma [tool:Uptime Kuma]? It's a monitoring platform.
[00:20:51] Ty Wells: I applied my skin to it without touching anything — Uptime Kuma still works normally, I just wanted to see it differently.
[00:23:12] Juan Torres: <Q>What were the different colors?</Q>
[00:23:15] Ty Wells: <A>They represent different things — the state of a particular job and routes assigned.</A>
[00:23:42] Ty Wells: ▶ I've given you the ability to describe a scenario, point a repo to it, and it will generate a review terrain for you to look at [link:terrain demo tool].
[00:24:20] Ty Wells: Everybody could technically have their own interface, because you're not changing the core — this is just the UI skin, the terrain.
[00:25:00] mdcatc: <Q>Your interface is sitting on its own server, hitting the original interface — is that how you're doing that?</Q>
[00:25:10] Ty Wells: <A>Yes. Two ways: subdomain it, or reverse-proxy the main one. It uses the existing API endpoints.</A>
[00:26:53] mdcatc: ▶ I see it also as a good way to deal with multi-tenant customers who want a custom skin.
[00:27:04] Ty Wells: ▶ That's originally why I did it — on September 15th I'm launching Island Flow [tool:Island Flow] down in the Bahamas to clients, and some wanted a different skin, especially new users who don't need the contact-heavy UI.
[00:27:30] Patrick Chouinard: <Q>You mentioned your reskin was an open repo — for the Uptime Kuma thing I'd be interested in taking a peek.</Q>
[00:27:40] Ty Wells: <A>Yeah — at the bottom of that page there's an NPX install command; it'll run right against the repo.</A>

<!--SEGMENT
topic: Legacy printer driver rewrite via AI
speakers: mdcatc, Paul Miller, Ty Wells
keywords: Lake Tahoe, e-waste, Dymo printer, CUPS, Python, USB protocol, AI reverse engineering, CLI, UDP
summary: Morgan describes a weekend project rewriting drivers for an obsolete Dymo label printer whose Windows drivers no longer work and which had been dropped by modern CUPS support on Linux. Using AI-assisted protocol research, he rebuilt the driver in Python from scratch in about two hours, producing a working CLI that prints text and images directly, framed as a broader opportunity to revive e-waste hardware.
-->

[00:28:47] mdcatc: I was up in Lake Tahoe for a few days on vacation — parasailing, ziplining, spent time with the (adult) kids.
[00:29:42] mdcatc: ▶ Software is so cheap now that a lot of e-waste is wasted simply because the manufacturer stopped supporting it — no drivers. I had a Dymo printer [tool:Dymo printer] whose drivers no longer work with Windows, and CUPS on Linux has dropped support for a lot of printers.
[00:30:26] mdcatc: I spent about two hours rebuilding the whole thing and now have fully functional printing without CUPS — writing directly through Python.
[00:31:19] Paul Miller: <Q>Is that communicating through USB or Bluetooth?</Q>
[00:31:24] mdcatc: <A>USB. I lucked out having AI do the research — it found documents describing the entire protocol, so I was able to rebuild it entirely in Python.</A>
[00:31:42] mdcatc: I have a CLI that can dump anything to the printer, both text and image.
[00:33:12] mdcatc: ▶ It's fun because you don't need deep internal knowledge of how chips communicate — the AI can figure that out. I even fed it photos of the printed label so it could measure boundaries and recalculate resolution.

<!--SEGMENT
topic: Other hardware/software side projects
speakers: mdcatc, Ty Wells, Paul Miller
keywords: Classic Curve, heritage plot, SVG mapping, carpool line marketing, signature pad, Android device, digital frame firmware, inventory scanning, multi-tenant
summary: Morgan updates on two dormant client-ready projects — "Classic Curve" and a heritage plot mapping tool with vector-graph overlays on satellite imagery — plus a marketing idea targeting school carpool-line frustration via memes. Ty separately describes repurposing a cheap Android device as a multi-function signature pad, check-in kiosk, and inventory scanner for his ERP system by rewriting its digital-frame firmware.
-->

[00:28:00] mdcatc: Classic Curve [tool:Classic Curve] is underway — a new version is being built with group feedback and is ready to go if you want to look at it from your side.
[00:34:08] mdcatc: The heritage plot [tool:heritage plot tool] mapping was updated to support scalar vector graphs so individuals can plot their own sections/rows over an overlay of the actual satellite image. I'm done with both until I get clients to give direction.
[00:34:39] mdcatc: ▶ I did a search for "waiting in carpool lines for schools" — lots of good content and memes out there; plenty of frustrated parents to market to, letting them push their schools toward the product.
[00:35:13] Ty Wells: One of the things for the ERP system was needing a signature pad — I built a system using a cheap Android device that works as a signature pad, check-in pad, and inventory scanner (it has a camera). ▶ I rewrote the digital frame firmware (Android-based) to strip out unused features and add exactly what I needed.
[00:36:16] mdcatc: ▶ That's the advantage — writing software specific to your own use instead of carrying 70% bloat that's rarely used, which just slows things down.
[00:36:46] mdcatc: My printer setup is CLI-driven and on the network — any device can hit the UDP address and print straight to the printer.
[00:37:06] mdcatc: ▶ If you have old hardware you liked, take half a day to rewrite the driver or a custom interface for it to do more specifically what you want.

<!--SEGMENT
topic: Team-level agentic knowledge management architecture
speakers: Patrick Chouinard, Juan Torres, Paul Miller, mdcatc
keywords: Hermes, Fable, ChatGPT, Claude Code, Copilot, Azure DevOps, Git, CI pipeline, agentic memory, knowledge merge, SharePoint for Agents, object-oriented knowledge
summary: Patrick describes a new enterprise initiative building team-level (not individual "second brain") knowledge management, using per-person Git repos that publish via CI pipeline into a team repo on Azure DevOps, with Git complexity hidden behind natural-language skills and Claude used for "fastlane" conflict merging. He frames the result as agentic behavioral memory rather than a queryable RAG system — effectively "Git as SharePoint for Agents."
-->

[00:37:16] Patrick Chouinard: This week I ran multiple Claude sessions to restabilize my home lab — Hermes [tool:Hermes] manages it in the background, and I used Fable [tool:Fable] to reanalyze the entire lab and build a 33-step stabilization plan.
[00:39:16] Patrick Chouinard: ▶ We're starting team-level knowledge management at work — not individual second brains, but a team-level brain that can merge into a corporate brain. It must work with Copilot [tool:Copilot] and Claude Code [tool:Claude Code].
[00:40:45] Patrick Chouinard: I took the whole conversation with my manager, sent it to ChatGPT [tool:ChatGPT], explored it at length, then had it crystallize a non-technical vision document — the only tech constraint being Copilot/Claude Code.
[00:41:24] Patrick Chouinard: I gave that to Claude Code with Fable to attack every angle and find the best architecture: ▶ managing knowledge artifacts through Git using Azure DevOps [tool:Azure DevOps] (would work equally with GitHub [tool:GitHub]).
[00:41:55] Patrick Chouinard: Each individual has their own repo; within the project's security boundary sits the team knowledge repo. Each individual repo has a CI pipeline that publishes to the team repo — all Git terminology hidden behind a skill ("publish that" = commit + push).
[00:42:46] Patrick Chouinard: ▶ We use Claude in "endless mode" for what we call fastlane merging — summarizing genuine conflicts for a human to pick one option, rather than dumping the whole knowledge piece for review.
[00:43:41] Patrick Chouinard: ▶ We're basically transforming Git into "the SharePoint for Agents."
[00:44:12] Juan Torres: <Q>Does this also account for meetings that are recorded, the discussions in team meetings?</Q>
[00:44:24] Patrick Chouinard: <A>Not currently — the focus is on the Copilot-as-UI workflow itself, since 69,000 companies are already working on meeting aggregation. We're focusing on the one nobody's working on.</A>
[00:46:00] Paul Miller: <Q>What's your thinking on how you'll share and serve this back to people wanting to query it?</Q>
[00:46:35] Patrick Chouinard: <A>It's not meant to be queried — it's used transparently as context for Copilot/Claude Code. It's agentic memory, more behavioral than a data dump.</A>
[00:47:25] Paul Miller: So it's not a RAG, basically.
[00:47:45] Patrick Chouinard: Right now we're focused at team level (up to ~20-30 people) to build the foundation properly before merging into higher layers. ▶ I'm treating knowledge like a programming language — objects with assumptions and interfaces, almost object-oriented thinking.
[00:48:41] mdcatc: This reminds me of enterprise wikis — now they're becoming active and interactive with AI; instead of querying, you're living within the information and talking to it directly.
[00:50:10] Patrick Chouinard: ▶ We're deliberately avoiding top-down system ontology projects that drag on for months without results — building bottom-up from individual knowledge instead.

<!--SEGMENT
topic: AI photo booth event success
speakers: Juan Torres, Paul Miller
keywords: AI photo booth, Estetica Flux, event marketing, country club, promo video, LinkedIn, San Diego, high-end venues
summary: Juan reports a successful high-end AI photo booth deployment in San Diego where an event coordinator became an unofficial advocate, teaching guests to use the app herself and generating strong word-of-mouth interest, including a lead with a country club operations manager. He notes the market appears underserved regionally, positioning him as an early mover.
-->

[00:51:45] Juan Torres: I had another event Saturday — went better than the last one, a more app-scale event. People really liked it. I got contact info from an operations manager of a country club in Indio (near LA) whose mind was blown.
[00:52:34] Juan Torres: I offered this event essentially for free to get a coordinator to look at the AI Booth application [tool:AI Booth]. ▶ She really liked it, became my salesperson — teaching guests how to use it, building a crowd around it.
[00:54:08] Juan Torres: I finalized the promo video, currently under audio review for a possible music IP issue. Published on the Estetica Flux [tool:Estetica Flux] Instagram and on LinkedIn.
[00:55:28] Paul Miller: <Q>Do you think this will be driven by event management people using/owning the tech, or where will your pipeline come from?</Q>
[00:56:15] Juan Torres: <A>I think event coordinators will be the main pipeline since they have a vested interest in selling cool stuff to clients — and venue/country club managers could also be recurring providers of the service.</A>
[00:57:00] Juan Torres: ▶ The coordinator works with high-end clients (the venue was a premium San Diego Bay-view space) and had never heard of another service in San Diego offering this — indicating the market is young and I may be one of the most competent providers in the region.

<!--SEGMENT
topic: Scaling and fundraising strategy for photo booth business
speakers: Juan Torres, Paul Miller
keywords: Y Combinator, seed funding, VC, scalability, transportation logistics, Notebook LM, casinos, convention centers, partnerships, LED floor
summary: Paul advises Juan on preparing a funding pitch, recommending he study Y Combinator's best pitch videos via Notebook LM before approaching investors, and to think carefully about what a partner should contribute beyond money. The pair also discuss transportation/space constraints (an LED floor doesn't fit his Honda Pilot) and untapped venue partnership channels such as casinos and convention centers.
-->

[00:58:25] Paul Miller: <Q>How do you lock and load and scale really quickly? You've got this opportunity now, you need to run with it.</Q>
[00:58:37] Juan Torres: <A>Brandon recommended I apply for seed funding. I also have transportation issues — my Honda Pilot has space constraints, especially with a new LED floor prop for a second video.</A>
[00:59:48] Paul Miller: ▶ When looking for VC money, ask what they're really contributing beyond money — you don't want people along for the ride while you do all the work.
[01:00:26] Paul Miller: ▶ Recommendation: seed all of Y Combinator's [tool:Y Combinator] pitch videos into Notebook LM [tool:Notebook LM] for guidance — their credibility and pitch material are excellent starting points, and Y Combinator backing itself could make investors more receptive to an unconventional concept.
[01:02:00] Juan Torres: I know people connected to Y Combinator here in San Diego who occasionally run showcases — I'll check if that's viable this year.
[01:02:47] Paul Miller: ▶ Think about industry partners as advocates, but consider whether partnering with one would shut off selling to their competitors. Larger convention facilities or casinos could be a channel to bring people in.
[01:03:19] Juan Torres: I haven't even thought about casinos — there are a lot of venue opportunities I'm not tracking that could systematize and stream a lot of my work.

<!--SEGMENT
topic: Legacy cash register hardware and penny-elimination opportunity
speakers: Adam, mdcatc, Patrick Chouinard, Paul Miller
keywords: cash register software, penny elimination, nickel rounding, US Mint, legacy hardware, vendor lock-in, supermarket chains, Canada
summary: Adam raises a hardware/software opportunity: US cash register vendors have stopped updating machines to handle the discontinuation of the penny and rounding to the nickel, leaving automated change machines disabled at his wife's grocery store employer. The group discusses vendor lock-in, the "human/expensive" barriers to modernization, and notes Canada solved this problem years earlier.
-->

[01:05:00] Adam: My wife works at a grocery store; the vendor making the cash register machines isn't sending updates — the US isn't making pennies anymore, so cash register software needs to round to the nickel. The automated change machines are all turned off.
[01:05:48] mdcatc: <Q>That's probably a bad assumption though — is the system locked out?</Q> The barrier is usually that people just don't have the knowledge, not that it's actually locked.
[01:06:09] mdcatc: ▶ That's a huge service area — old registers are still "penny bound" instead of "nickel bound," and businesses are reluctant to upgrade because of change-aversion and cost; vendors may push a subscription model they don't want either.
[01:07:06] Paul Miller: <Q>Is it a franchise-based supermarket where you could talk to an owner?</Q>
[01:07:12] Adam: <A>I've met the owner a couple of times — but he owns the entire chain, so it'd be beyond my skill set to approach directly.</A>
[01:07:41] Paul Miller: ▶ Bring it to the group — throw the problem to Claude/AI to test on an old register; nothing promised, but it could save money and make you look good within the chain.
[01:08:14] Patrick Chouinard: ▶ Or ask us Canadians — we got rid of the penny a couple of decades ago; it's not a new problem.
[01:08:23] Paul Miller: New Zealand went through the same massive tills-replacement projects years ago, with a lot of waste.

<!--SEGMENT
topic: Claude Opus 4.5 prompting behavior
speakers: mdcatc, Patrick Chouinard, Paul Miller
keywords: Opus 4.5, Claude, prompting technique, problem vs solution, Fable, commitment bias, GPT-5.6
summary: Morgan critiques Opus 4.5's [tool:Claude Opus 4.5] responses as strangely narrow and hard to parse; Patrick explains this stems from over-specifying the desired solution rather than the problem, and that Opus performs far better when given a terse problem statement and left to figure out implementation itself — mirroring a classic consulting principle to avoid "commitment bias."
-->

[01:09:34] mdcatc: <Q>I don't necessarily like Opus 4.5's responses — sometimes strange, I have to read them several times to understand the answer.</Q>
[01:10:00] Patrick Chouinard: <A>Trim your prompt/skills context — Opus 4.5 requires much less instruction to behave well. If you treat it like Opus 4.1 with heavy specification, you get weird answers; if you just say "here's what I want, figure it out," it works ten times better. You have to be descriptive about *what* you want, not *how* to build it.</A>
[01:10:41] Patrick Chouinard: ▶ Basically, describe the problem, stop describing the solution — as we've told users for decades.
[01:10:50] Paul Miller: <Q>Do you find Opus getting distracted, going off on tangents, compared to GPT-5.6 [tool:GPT-5.6]?</Q>
[01:11:09] mdcatc: <A>Not so much distracted as narrowly focused on one specific problem, which is sometimes not the main problem you're trying to solve — so describe the real problem broadly, but don't over-specify the solution.</A>
[01:11:42] Patrick Chouinard: Fable behaves the same way — if you over-specify what you want, it reacts weirdly. Giving it a bare problem statement with minimal technical direction let it hit exactly what I wanted, because it had liberty to think, ▶ the same way an expert consultant does when not told the exact solution to build.
[01:12:39] mdcatc: ▶ Otherwise you end up with commitment bias instead of an actual solution.

<!--SEGMENT
topic: Cloud code consulting for corporate clients and Codex review plugin
speakers: Alex Roca, Patrick Chouinard
keywords: Claude Code, corporate consulting, AI champions, workshops, Mexico, pricing, Codex plugin, adversarial code review, OpenAI, ShipKit
summary: Alex reports a profitable consulting model teaching department-level "AI champions" to use Claude Code, shifting from horizontal (one champion per department) to vertical (deep automation within one department) engagement, charging roughly $2,000 per session in the Mexico market. Patrick then explains OpenAI's official Codex plugin, which hooks into Claude Code completions to trigger an automated adversarial code review.
-->

[01:14:00] Alex Roca: I'm focusing now on Claude Code [tool:Claude Code] in corporate clients. I started with several AI tools, but follow-ups converged on "let's just focus on Claude Code." I work with "champions of AI" from each department.
[01:14:44] Alex Roca: I started horizontally (one champion per department: HR, logistics, etc.) but now I'm focusing vertically — e.g., the logistics champion and I automate products directly using Claude Code.
[01:15:21] Paul Miller: <Q>Are these good, profitable engagements?</Q>
[01:15:26] Alex Roca: <A>Yeah — for Mexico standards, pretty good, as long as I do two a month. I charge around $2,000 a session, plus follow-ups specializing in Claude Code.</A>
[01:16:16] Alex Roca: I'm also trying to close a backend build (Next.js) for the same customers — bigger contracts, but slow, as you'd expect.
[01:18:09] Alex Roca: <Q>You shared that Codex [tool:Codex] can be used as a code reviewer — is there a plugin from Anthropic? How does that work — install it and it revises everything, or point it at a GitHub repo?</Q>
[01:18:48] Patrick Chouinard: <A>Actually it's OpenAI who created the plugin for Codex specifically — a legitimate plugin, not something built on the side. Once set up, it creates a hook so that every time Claude Code finishes a coding activity, it sends the output to Codex via an endless call. Codex has a system prompt for adversarial code review, receives the code, verifies it, sends back a report, and Claude reads and acts on it.</A>

<!--SEGMENT
topic: Building credibility through event photography
speakers: Juan Torres, Alex Roca
keywords: LinkedIn, Instagram, media reel, presentation credibility, personal branding, social proof
summary: Juan recommends Alex hire a photographer/videographer to accompany his client presentations, sharing his own practice of using a companion to shoot photos/video during talks (in Istanbul and San Diego) that he posts to LinkedIn and Instagram to build credibility and generate inbound leads.
-->

[01:19:42] Juan Torres: ▶ Have you thought of bringing a media person to your presentations to take photos/video and create a small reel to post on LinkedIn?
[01:20:00] Alex Roca: That's a great idea.
[01:20:04] Juan Torres: That's what I do — a person comes with me and shoots photos/film during presentations; it makes me look more impressive than I actually am. ▶ It's a strong credibility-builder because people are very impressed seeing someone in front of an engaged audience — a signal of high value in engineering or any skill.
[01:20:38] Juan Torres: I share it on both LinkedIn and Instagram [link:examples from Istanbul and San Diego presentations].
[01:21:19] Juan Torres: ▶ Since you're already systematizing presentations, systematize the demonstration of high value too, by having someone follow you and document it.
[01:21:43] Alex Roca: I'll do it — I think it gives credibility and increases customer reach.

<!--SEGMENT
topic: Deal-closing strategy for real estate client
speakers: Alex Roca, Paul Miller, Juan Torres
keywords: proof of concept, contract, phased engagement, signing authority, real estate client, Next.js, ShipKit, sensitive data, Mexico decision-makers
summary: Alex asks how much progress to show a real estate prospect who has already shared sensitive financial data across five calls but has not yet signed or paid. Paul recommends formalizing a small paid proof-of-concept phase with a draft contract sent directly to the key stakeholder, addressing signing authority and stakeholder buy-in before committing to the full build.
-->

[01:22:04] Alex Roca: <Q>I'm in conversations with a real estate client, five calls in, they've shared very sensitive financial information for the canonical model — I've already started building, but nothing's signed. Should I show them an advance, or wait?</Q>
[01:24:00] Paul Miller: <A>▶ Show them something tangible, but first frame the engagement as: you'll build a proof of concept together before the main project — not the full application, so it's clear what they're and aren't getting, with an initial cost for that phase. Consider signing authority — can the customer's initial commitment be small enough to sign off easily, then use excitement from that phase to commit to the bigger project?</A>
[01:26:00] Alex Roca: That's actually how we've divided it — Phase 1 is the concluded project (a Next.js [tool:Next.js] dashboard for existing results), with other projects charged separately at independent cost.
[01:26:49] Alex Roca: I think it's the summer season and the decision-maker being on vacation slowing things down.
[01:27:05] Paul Miller: ▶ Get your contract ready and send the draft to your key stakeholder now so they can review it and come back when comfortable to schedule a demo and get sign-off.
[01:28:12] Paul Miller: ▶ Also assess their team's capability — do they have the skills to consume the data and support the app post-launch? I'm seeing capability gaps in a similar Australian engagement despite it looking good on paper — worth surfacing those questions early.
[01:29:43] Alex Roca: Using ShipKit [tool:ShipKit] — already got paid back a couple of times on the phase-one work.

<!--SEGMENT
topic: Closing remarks
speakers: mdcatc, Patrick Chouinard, Paul Miller
keywords: scanner driver rewrite, Mac software, network printer, wrap-up
summary: Brief closing exchange in which Morgan wishes Patrick luck on a planned weekend project rewriting scanner software for an all-in-one network printer, ending the session on a lighthearted note before sign-off.
-->

[01:30:33] mdcatc: Good luck on your scanner rewrite.
[01:30:38] Patrick Chouinard: Yeah, when I saw that I thought, okay, here's my weekend. Scanner software for Mac is horrible, so I'm going to write my own.
[01:30:55] mdcatc: <Q>Is that a USB scanner or a SCSI scanner?</Q>
[01:31:00] Patrick Chouinard: <A>No, no — it's an all-in-one network printer.</A>
[01:31:10] Paul Miller: Okay guys, have a great week. Patrick, have an exciting weekend. We'll talk to you next week.
[01:31:22] Patrick Chouinard: Absolutely. Good day, guys.

=== UNRESOLVED SPEAKERS ===
- mdcatc (raw identifier used throughout transcript; strongly implied by context to be "Morgan," e.g., addressed as "Mr. Morgan" and "Morgan" by other speakers, but no alias mapping was available to confirm a canonical form, and no SPEAKER_ALIASES data was supplied in this session)