=== SESSION ===
date: not stated in transcript
duration_estimate: ~88 minutes
main_themes: AI coding agent tooling (Cloud Code/Codex status lines, subscription management, model tracking), agentic harnesses and code-review automation (pi.dev, Copilot CLI plugin), enterprise agentic SDLC design (Superpower, Matt Pocock skills, compound engineering), just-in-time AI training ("teach" skill), mobile app deployment (Expo vs native iOS), biometric identity verification, career advice for AI/software engineers, resume optimization with AI, and an AI-driven CRM reporting product vs. Salesforce.

=== UNRESOLVED SPEAKERS ===
(No speaker alias data was supplied in the SPEAKER_ALIASES context block for this session, so all speaker names below are passed through unchanged from the raw transcript.)
- Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
- Ty Wells
- Daniel Zivkovic
- Patrick Chouinard
- Ryan C
- Paul Miller
- Morgan
- Elena
- Varun Sharma

---

<!--SEGMENT
topic: Power Your Process AI walkthrough
speakers: Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
keywords: Power Your Process AI, Vercel, GitHub, deployment monitoring, feedback loop, guided walkthrough, personal project, app onboarding
summary: Scott demos his personal app "Power Your Process AI," showing automated deployment-completion monitoring across GitHub and Vercel, an in-app feedback pipeline that opens GitHub issues, and a newly built guided walkthrough that explains every feature and setting for new users.
-->

[00:00:00] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: This is the one I set up as personal — it's called Power Your Process AI [tool:Power Your Process AI]. The nice thing is I can push multiple things and just monitor them. <Q>Let me know when it's done on Vercel [tool:Vercel] too</Q> — not just when it's pushed to GitHub [tool:GitHub], but when the deploy actually finishes. I'll just let this thing roll.

[00:00:17] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: This one already has an update pending — you get updates over the air, and you can submit feedback, which opens a GitHub issue automatically.

[00:00:31] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: I'm blogging this one. ▶ I built a really cool guided walkthrough for it, since it has so many features — it explains everything happening in each part of the app and walks through all the settings. If anyone's interested I'll drop the link in the chat afterward. [link:shared in chat after the call]

[00:01:00] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: That's it on that one — moved through it pretty fast, but it's a lot of functionality.

---

<!--SEGMENT
topic: Model Radar for tracking AI models
speakers: Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
keywords: Model Radar, Doppler, API key scanning, deprecated models, retired models, hybrid AI scan, confidence scoring, Claude Code, n8n, Electron
summary: Scott introduces "Model Radar," a locally-run tool that scans his entire development folder structure to detect which AI models are referenced across all client and personal projects, checks them against live provider APIs to flag deprecated or retired models, and shows confidence-scored evidence per project on a dashboard.
-->

[00:01:00] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: The last thing I built today — I have a lot of projects for customers and myself, and even though I use Doppler [tool:Doppler] to track API keys, I couldn't keep track of which models are used in which apps. Models get retired, and with enough apps you start forgetting.

[00:01:25] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: ▶ Since everything's local, I built "Model Radar," which scans my entire root app-development folder. It's a hybrid — partly AI, partly rule-based — and automatically excludes markdown, lock files, build output, and secret stores; you can also add custom directories to ignore.

[00:02:07] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: <Q>How does it know which models are still actually active?</Q> <A>If you add your API keys, it makes a free call to the provider's API to pull the currently active model list, on a schedule.</A> On the dashboard I can go customer by customer and it flags changes — I already caught a model that had been deprecated or retired and fixed it. There's also a confidence level, because the AI reviews the evidence — for example it correctly flagged one project as "docs-only evidence" since that's a Claude Code [tool:Claude Code] repository connected to n8n [tool:n8n] via CLI, where models are documented in JSON rather than called from a web app directly.

[00:03:08] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: ▶ It flags when code changes and can rescan automatically or on demand. I haven't tested it yet, but there's also an agentic chat mode where I can say "I just added another folder, go check it out." It's already public, easy to set up, and built on Electron [tool:Electron] for macOS.

---

<!--SEGMENT
topic: CC Black Box machine sync and CMUX browser control
speakers: Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com, Ty Wells
keywords: CC Black Box, Bonjour, machine sync, encrypted sync, CMUX, browser automation, Claude Code, agentic IDE, screenshots
summary: Scott describes a cross-Mac sync feature in his "CC Black Box" tool that keeps Claude Code session and reporting data synced between two machines via an encrypted Bonjour connection, while Ty Wells contrasts this with his CMUX-based setup, which lets him drive a browser directly for testing — a feature Scott says he'll add next.
-->

[00:03:50] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: I should mention — on "Black Box" [tool:CC Black Box], I develop from two Macs, so I built machine sync. ▶ It syncs your two databases so wherever you work, all your session and reporting information stays in sync. It uses Bonjour [tool:Bonjour] over a secure encrypted connection and pulls both ways — I already tested it, forgot to mention it earlier, but it's a pretty cool feature.

[00:04:25] Ty Wells: That's good stuff, Scott. I'm definitely interested in those two — I'm building something similar myself, using CMUX [tool:CMUX], a derivative, and I keep tweaking it since it's still not 100%. <Q>What I really like about CMUX is being able to drive the browser — have you integrated a browser?</Q>

[00:04:50] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: <A>Not yet, but I will — that's a good one.</A>

[00:04:53] Ty Wells: That's the key thing for me — controlling the browser for testing, seeing it myself, and grabbing screenshots.

[00:05:03] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: ▶ That'll probably be my next item on the list. I do some agentic stuff, but I like running things on demand or on a schedule rather than the more freeform CMUX style — it's just a different way of thinking. This is more of a classic IDE with a lot of small quality-of-life tweaks, simplified because a lot of IDEs cram in too much. The agentic harness piece is probably a bit limited right now, so I want people to test it and make suggestions.

---

<!--SEGMENT
topic: Subscription multiplexing and mobile intent capsules
speakers: Ty Wells, Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com, Daniel Zivkovic
keywords: Anthropic subscription, Codex subscription, CMUX, intent capsules, cold session, Proxmox, mobile access, usage threshold, session switching
summary: Ty Wells explains how his CMUX-based system automatically manages and switches between multiple Anthropic and Codex subscriptions based on remaining usage, packages work into self-contained "intent capsules" that can launch fresh cold sessions with full context, and remotely controls sessions from his phone via a Proxmox-hosted setup — built out of necessity for staying productive while traveling or on the golf course.
-->

[00:05:50] Ty Wells: The other thing I added to my CMUX setup is management of my Anthropic [tool:Anthropic] and Codex [tool:Codex] subscriptions. Certain projects run only on a dedicated subscription so they don't eat into others, and other projects share a subscription I bounce between — same idea with Codex. ▶ If usage drops below about 5% remaining for a session (weekly or daily), it automatically switches over to a fresh session so I don't lose work.

[00:06:27] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: If you've got one hooked in a lot, that's nice — you won't lose work, it just stops and you can switch anytime. Claude Code [tool:Claude Code] already handles that gracefully, but auto-switching on top is cool. This app can only be used with Claude Code directly, though you can reach Codex through Claude Code via CLI — not a full dedicated Codex client, but I like the auto-switch idea too.

[00:06:54] Ty Wells: I used to watch usage manually and got tired of it, so now it's automatic — I can see what's running under each account and move a session between accounts to avoid running out.

[00:07:13] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: <Q>It'd be nice to tap into usage and pin it permanently in a tab — do you know if that's possible?</Q> Ty Wells: <A>Yes, that's what I show now — percentage remaining per account, plus which sessions are running under each.</A> Manually logging into an account can create a duplicate entry, as shown in his demo — one account dedicated to a specific project, another to "Island Flow," and Codex currently unused.

[00:08:27] Ty Wells: ▶ I use "intent capsules" — self-contained context packages that can run in a cold session with zero prior context, so I can launch a batch and they run without issues; if capsules depend on each other, they wait their turn.

[00:09:06] Ty Wells: This whole system is accessible from my phone, so I can reply to a running session remotely — I built it because I needed to keep working from the golf course or while traveling. ▶ It runs on my Proxmox [tool:Proxmox] server, so when my laptop is closed, it clones state there and keeps going.

---

<!--SEGMENT
topic: Claude Code status line plugin
speakers: Patrick Chouinard, Ty Wells, Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com, Daniel Zivkovic
keywords: status line, Claude Code, Codex, open source plugin, session tracking, five-hour limit, seven-day limit, Git branch, usage tracking
summary: Patrick shares an open-source, minimalist Claude Code status-line plugin he built that shows reasoning effort, five-hour and seven-day usage limits with time remaining, separate usage tracking for Claude Code and Codex, and the current Git branch — designed to surface key session info at a glance.
-->

[00:10:24] Patrick Chouinard: I see you still have the old CC [tool:Claude Code] status line — you should update it, I've added session tracking now.

[00:10:49] Ty Wells: That's because I wiped my Claude Code rules and redid everything the other day, so it's still the old version — need to update the plugin.

[00:12:03] Patrick Chouinard: This is the status line I built — nothing too fancy, but I've added an "effort" indicator that wasn't there before, plus usage tracking.

[00:12:21] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: What's cool is my CC Black Box app also tracks all of that usage, so you can see actual cost across all sessions together and run reports per customer.

[00:13:39] Patrick Chouinard: ▶ Now it tracks my five-hour limit with time remaining and usage amount, plus the seven-day limit the same way — not a big change, but it's constant feedback. I've also added a button that tracks usage for Claude Code and another for Codex.

[00:14:11] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: I'll install that just to see it — I don't need it baked into my IDE since it's really just a Claude Code status line, I just want to glance at it.

[00:14:26] Daniel Zivkovic: <Q>Is it open source?</Q> Patrick Chouinard: <A>Yes, absolutely.</A> [link:GitHub repo shared in chat] It also tracks your Git [tool:Git] repo and which branch you're on. ▶ I tried to keep it minimalistic while still surfacing every piece of information you need at a glance.

[00:14:49] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com / Daniel Zivkovic: Very tight — less is more.

---

<!--SEGMENT
topic: Subscription spend, Fable, and Hermes agent
speakers: Paul Miller, Patrick Chouinard, Daniel Zivkovic
keywords: Claude subscription, Codex subscription, Fable, Hermes agent, thinking partner, design thinking, weekly planning, requirements gathering
summary: Paul, Patrick, and Daniel compare monthly spend on Claude and Codex, and Daniel and Patrick describe using "Fable" as a high-value AI thinking/design partner rather than a coder, with Patrick's custom "Hermes" agent condensing weekly context from every machine and project into a single high-value Fable prompt that then drives his week's work.
-->

[00:14:54] Paul Miller: <Q>What about the other three Claude accounts you have to run to keep the tokens up?</Q> Patrick Chouinard: <A>I'm actually just running one account, flipping between Claude [tool:Claude] and Codex [tool:Codex].</A>

[00:15:09] Paul Miller: So you mean I don't need to spend $800 a month? Patrick Chouinard: I'm spending $100 on Claude and $100 on Codex. Daniel Zivkovic: $100 isn't enough for me on Claude, because I do everything in Claude.

[00:15:32] Paul Miller: I keep working with Fable [tool:Fable]. Patrick Chouinard: <Q>Are you coding with Fable?</Q> Daniel Zivkovic: <A>No — just design thinking, gathering requirements, philosophical discussions with my thinking partner.</A>

[00:15:48] Patrick Chouinard: ▶ I have that too, but through "Hermes," an agent I built that manages my entire environment and runs on my Codex subscription — it knows every machine and project I have. A recurring job condenses everything into a single Fable prompt each week; whatever Fable's analysis produces becomes the week's work. The goal is to concentrate usage as much as possible and treat that Fable prompt as very high value — I want it to think as hard as it possibly can, since everything else processes off that output.

---

<!--SEGMENT
topic: Optometry theory and field-based requirements gathering
speakers: Daniel Zivkovic
keywords: optometry theory, requirements elicitation, business analyst, Fable, Kindle audiobook, Video Intel, conference research, field-based requirements
summary: Daniel Zivkovic describes his "optometry theory" of iterative requirements elicitation for stakeholders who can't articulate what they want but recognize it when shown, his practice of having Fable narrate drafts as audiobooks for review, and his open-source "Video Intel" project that scrapes conference talks and Q&A discussions to mine ideas that feed back into Fable.
-->

[00:17:06] Daniel Zivkovic: I feel small after listening to you guys. There's a constant conflict between business not being able to define requirements and IT asking for them. ▶ I call it "optometry theory" — like an optometrist asking "this better or this better, one or two, one or two," and after a few iterations you land on the right lens. I want that in IT, and now with AI I can prototype fast enough to make it work.

[00:17:37] Daniel Zivkovic: 17 years ago I worked for a pension plan as a business analyst and asked a VP of marketing for requirements. She said, "Daniel, show me what you have and I'll tell you what I want." That became my mantra with AI. ▶ I'm building a field-based requirements-gathering system — eliciting requirements from business users who don't know what they want but feel it.

[00:18:03] Daniel Zivkovic: Fable [tool:Fable] publishes my drafts as audiobooks on Kindle so I can lie down and listen and say "yes, that's good" — that keeps Fable grounded. I also have an open-source "Video Intel" project that scans the internet and transcribes videos with full context of what's discussed and shown on screen. I love conferences and the discussion afterward, because I believe two ideas combine into a new one — so I fish through Q&As and group chats for nuggets, then feed those into Fable to make sense of the noise. Just research.

---

<!--SEGMENT
topic: Codex-to-Copilot plugin port and pi.dev review harness
speakers: Patrick Chouinard, Daniel Zivkovic
keywords: Codex plugin, GitHub Copilot CLI, OpenAI restriction, ChatGPT, pi.dev, adversarial review, code review harness, OpenRouter, cybersecurity governance
summary: Patrick describes rebuilding an open-source adversarial-review Codex plugin so it runs on GitHub Copilot CLI instead (since OpenAI/Codex isn't permitted at his workplace), and his follow-on project building a minimal, model-agnostic pi.dev-based harness dedicated purely to code review, security, and adversarial analysis at the stop-hook, pre-commit, branch, and project level.
-->

[00:19:06] Patrick Chouinard: At work we don't have Codex — OpenAI [tool:OpenAI] isn't allowed, only Claude [tool:Claude] or Copilot [tool:GitHub Copilot]. Since Copilot has a CLI, ▶ I took the open-source Codex plugin for Claude Code, had Fable analyze it along with the Copilot CLI source code, and told it to build an equivalent plugin using Copilot CLI instead, adding model selection since that doesn't exist on the Copilot side. I brought it back to work; people like it, and now they have access to ChatGPT 5.6 [tool:ChatGPT] models through GitHub Copilot — security and governance are happy, and it's working.

[00:20:43] Patrick Chouinard: But going through that made me think it doesn't go far enough, so I started something bigger, working from the harness perspective rather than the UI. ▶ I'm building on pi.dev [tool:pi.dev], an open-source, minimal, fully modifiable harness, to create a version optimized strictly for review — not coding, not even fixing issues found, just receiving code and context and analyzing it (not to be confused with DeepSeek).

[00:22:00] Patrick Chouinard: Pi isn't bound to any model or supplier — you can feed it a Codex, Claude, or Copilot subscription, or bind it to OpenRouter [tool:OpenRouter]. The harness is very light but fully configurable. Whenever it's called by Claude Code or Codex, it returns an adversarial review — same mechanic as the Copilot CLI plugin, but extended with review hooks at the stop-hook, pre-commit, branch, and full-project level. ▶ The goal is a harness purely for code review, security, and adversarial analysis that hands the coding agent a report saying "here's what to fix, go fix it."

---

<!--SEGMENT
topic: Enterprise agentic SDLC design
speakers: Patrick Chouinard, Daniel Zivkovic, Paul Miller
keywords: agentic SDLC, Superpower, Matt Pocock skills, Grill with Docs, compound engineering, business analyst workflow, citizen developer, approved technology stack
summary: Patrick outlines his plan for an enterprise-grade agentic software development lifecycle merging the guided "Superpower" framework with Matt Pocock's "Grill with Docs" skill, customized for non-technical business analysts to surface the real underlying problem before jumping to a solution, layered with a technology-stack skill constrained to internally approved tools; Daniel counters that "compound engineering" already covers this as a full enterprise SDLC framework.
-->

[00:23:59] Patrick Chouinard: ▶ At work we've started thinking about agentic SDLC in the enterprise, because everything that exists today is geared toward individual developers. I'm considering merging Superpower [tool:Superpower] with Matt Pocock's skills [tool:Matt Pocock skills] — instead of Superpower's brainstorming (great for a solo dev, doesn't work in the enterprise), I want a customized "Grill with Docs" [tool:Grill with Docs] geared toward business analysts with no dev background, that keeps asking "what problem are you actually trying to solve" instead of accepting "I need a dashboard" at face value.

[00:24:56] Patrick Chouinard: The analyst's output would feed a second skill layer analyzing which technology stack should solve the problem — constrained to what's already approved and implemented internally, rather than recommending everything on the market. Then it hands off to a developer to finish implementation.

[00:25:37] Daniel Zivkovic: <Q>Patrick, have you looked at compound engineering?</Q> I've looked at five or six of these frameworks — compound engineering is basically full-blown, old-fashioned SDLC thinking; you don't need to hunt for other frameworks, just watch your token spend.

[00:26:05] Patrick Chouinard: <A>I'm not looking for a framework — I'm pulling bits and pieces from several to optimize for our specific business. Most frameworks out there target single developers or small teams.</A> Daniel Zivkovic: Compound engineering is different — it's truly enterprise SDLC, and the author refines his thinking every few months; I don't mind connecting you with him.

[00:26:38] Patrick Chouinard: I'll take a look, but we're accommodating users at very different technical levels — citizen developers get a short leash but full prototyping ability, professional developers follow the same path with more liberty to deviate, as long as they explain why.

---

<!--SEGMENT
topic: Theo's Pocock video and the "teach" skill
speakers: Paul Miller, Patrick Chouinard, Daniel Zivkovic
keywords: Theo video, Matt Pocock, teach skill, just-in-time training, quiz generation, Deep Wiki, NotebookLM, Mark Kashif
summary: Paul references a Theo video on customizing Matt Pocock's skills that inspired Patrick's approach; Patrick then describes implementing Pocock's "teach" skill at work — pointing it at a repo or doc set to generate a short, quiz-driven training module in about 15 minutes — as a replacement for building traditional courses that go obsolete quickly, contrasted with Daniel's older Deep Wiki + NotebookLM podcast workflow.
-->

[00:27:24] Paul Miller: <Q>Patrick, did you see Theo's video on this?</Q> Patrick Chouinard: <A>Yes — that's exactly where I got the inspiration.</A> Paul Miller: He basically said what you said — you're making it your own, not just copying and pasting, because you've got a unique environment and challenge. [link:video shared in chat]

[00:28:09] Patrick Chouinard: I follow Matt Pocock, Theo, and Nate mostly, daily. Daniel Zivkovic: Mark Kashif is good too — I believe Ty is his coach.

[00:28:39] Patrick Chouinard: ▶ I've implemented Pocock's "teach" skill [tool:teach skill] at work — point it at documentation, a technology, or a repo and it slash-teaches a specific gap in about 15 minutes via generated HTML training material, rather than a full course. We don't build training anymore — creating courses is increasingly useless because they're obsolete by the time you finish, so we generate them just in time.

[00:29:37] Daniel Zivkovic: I used to do it the long way — upload a repo into Deep Wiki [tool:Deep Wiki], extract the pages, feed them to NotebookLM [tool:NotebookLM] to generate a podcast, then spend 20 minutes listening to figure out if something's good or bad.

[00:30:00] Patrick Chouinard: ▶ The podcast is fine for passive learning, but slash-teach builds an actual web app with quizzes — it's not just reading, it gives homework and quiz feedback. It's pretty amazing.

---

<!--SEGMENT
topic: Migrating a project from Supabase to Convex
speakers: Morgan
keywords: Supabase, Convex, Wayfinder, code review, sync database, WebSockets, GitHub issues, Carpool App
summary: Morgan describes migrating an app's backend from Supabase to Convex, using Matt Pocock's "Wayfinder" skill to run a thorough code review that surfaced existing bugs before the migration even began, and explains why Convex's built-in WebSocket-based sync model fits a real-time "Carpool App" use case.
-->

[00:30:34] Morgan: I've been working on changing one of my apps' stack from Supabase [tool:Supabase] to Convex [tool:ConvexDev], which has been a bit of a trek. The biggest part was spending last week using Pocock's Wayfinder [tool:Wayfinder] to figure out all the unknowns. ▶ It found a lot of bugs in the existing code just running through it as a code review — broken pieces already present, let alone what needed to change going forward.

[00:31:23] Morgan: Wayfinder uses all the other skills — research, "Grill with Docs" — and it's a nice process; it ties into GitHub [tool:GitHub] issues so everything's logged, and you build specs and tickets off of that. That was a good process. I've finished the exploration of converting from Supabase to Convex.

[00:32:00] Morgan: ▶ ConvexDev is a sync database — it has all the WebSockets mapped out for you, so any client connected stays in sync with any change in the database, which is exactly what I needed for the Carpool App. I'm about halfway through coding it on the new platform.

---

<!--SEGMENT
topic: Restructuring Google Docs data into a relational system
speakers: Morgan
keywords: Google Docs, relational data, disconnected spreadsheets, client project, criminal justice data, domain knowledge migration
summary: Morgan describes a client project where all domain knowledge and application content currently lives in scattered Google Docs and disconnected spreadsheets, and is being rebuilt into a cohesive relational data structure — complicated by the fact that some of the underlying data is subject to criminal-justice data-handling restrictions.
-->

[00:32:37] Morgan: The other project — a client whose domain knowledge and application content all live inside Google Docs [tool:Google Docs] in several broken, disconnected spreadsheets. I'm redoing that so they have a cohesive relational data structure, because their copy-paste approach isn't workable, especially with multiple team members. That data is under criminal justice control, so I can't display any of it. ▶ Both of these projects are going pretty well and are kind of fun.

---

<!--SEGMENT
topic: iOS deployment strategy: Expo vs native Swift
speakers: Morgan, Ryan C, Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com, Paul Miller
keywords: iOS deployment, Expo, Swift, Xcode, Apple developer license, Android, offline-first, native vs cross-platform
summary: Morgan asks how to deploy an existing app to iOS with no prior iOS experience; Ryan and Paul recommend Expo over native Swift/Xcode development for apps that offload most logic to a server, describing it as a cross-platform (iOS + Android) approach that still supports GPS, camera, and other native features, while noting native development is preferable for deep, platform-specific integrations.
-->

[00:33:29] Morgan: A third project is an app I've written that now needs to be deployed to iOS — I haven't done any iOS development, though we did get the Apple developer license set up under the client.

[00:33:53] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: Ryan's the guy to talk to — I only got mine signed and downloaded the GitHub DMG onto the Mac.

[00:34:22] Ryan C: <Q>There are two ways you can go</Q> — <A>the "proper" way, developing natively with Swift and pushing into Xcode the way Apple wants, or the easier way, using something called Expo [tool:Expo], which lets you build one app that distributes to both Android and iOS. You pay a monthly fee, put your Apple credentials in, and it handles app-store submission for you.</A>

[00:35:00] Ryan C: If the app is "dumb" on the phone and offloads most of its logic to your actual web app behind it, Expo works great. You still have to sign up for the Apple developer program yourself — Claude will talk you through the steps. ▶ I'm using Expo and it works perfectly fine, and I've started testing on Android this last week too.

[00:36:00] Paul Miller: I'd second what Ryan's saying — I'm also using Expo, building both Android and iOS apps. ▶ On the Apple side, I've also set up remote-control emulation of both device types, and I get Claude Code [tool:Claude Code] to run full user-flow testing through that emulation, feeding results back into the loop to fix UI/UX issues. You really need an Apple dev machine for that, though — I wouldn't try it on a Windows stack.

[00:38:19] Morgan: <Q>What was your issue with having business logic in the app itself on the phone with Expo?</Q> Ryan C: <A>No specific issue — but if you need something deeply native to Apple, linking into their services, you're probably better off using native tooling for fewer headaches.</A> ▶ Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: That's the whole point of Expo — you're not relying on anything platform-specific unless you truly need something like device GPS. Paul Miller: You can still access GPS, camera, and most base device features through Expo — the only real friction is native AI functionality specific to one platform. My main reason for caring was wanting offline support so the app degrades gracefully if the server is unreachable.

---

<!--SEGMENT
topic: Apple developer account setup and Expo build costs
speakers: Ryan C, Morgan, Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com, Paul Miller, Ty Wells
keywords: Apple developer account, Mac requirement, Expo subscription, build credits, free trial, Mac Mini M5
summary: The group walks through practical friction points in setting up an Apple developer account (which requires a Mac or iPhone to activate) and Expo's paid build/subscription model, including the number of builds included per plan and advice to batch changes before triggering paid builds; Paul also flags the upcoming M5 Mac Mini as a low-cost dev machine option.
-->

[00:40:34] Ryan C: You need to sign up for your Apple developer account, which can take a minute to register and come through. Morgan: We got it signed up and authorized, but can't activate it because it requires a Mac.

[00:41:07] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: You can also do it from an iPhone — I activated mine off my phone. ▶ It was a little convoluted (Scott recounts struggling to photograph his ID close enough with his phone's camera to complete verification), but it's doable without a full Mac.

[00:44:04] Morgan: <Q>Tell me about the Expo subscription model — what's that?</Q> Ryan C: <A>I'm spending about $45/month, and it gives roughly 15 pushes, but you're charged per build, so you don't get many — batch your changes and build once you're done rather than after every small change, or you'll burn through it fast.</A>

[00:44:50] Paul Miller: On my side, I wait until local testing with the two emulators gets me to a solid version before pushing more updates to Apple — you can test extensively locally first, then push when you're closer to ready. ▶ Also worth noting: the latest Mac Mini with an M5 processor just became available with September availability — a good low-cost dev machine option if you're going this route, Morgan.

[00:45:47] Morgan: <Q>Can I get started with Expo without subscribing to the paid service?</Q> Ryan C: <A>Yes — they offer a free trial with about 10 builds, so use that first, then subscribe once you need more builds per month.</A> Paul Miller: It's well-built and lightweight; avoiding the subscription usually means using less-reliable third parties that bloat the app, whereas Expo is lean, well-supported, and has a strong community.

---

<!--SEGMENT
topic: Offline storage and biometric identity verification
speakers: Ryan C, Paul Miller, Daniel Zivkovic, Morgan
keywords: SQLite, offline storage, SumSub, biometric verification, driver license authentication, anti-money laundering, Clerk, facial verification
summary: Ryan describes using SQLite for offline-first storage in his Expo-based capture app; Paul then details "SumSub," a third-party biometric identity-verification service he uses to confirm delivery drivers match their driver's license via face-matching after an initial registration, which Ryan flags as directly useful for anti-money-laundering (AML) client onboarding in his estate-agency CRM project.
-->

[00:46:40] Ryan C: Yes, it does handle offline app storage — mine has an offline mode for a capture app; if it's offline it stores photos on the phone until it's back online, then sends them to storage.

[00:47:03] Daniel Zivkovic: <Q>What do you use for offline storage — Firebase? Is it part of Expo?</Q> Paul Miller: <A>It's SQLite [tool:SQLite] — you can use that or a third-party option, but SQLite is a good cross-platform starting point.</A>

[00:47:29] Paul Miller: ▶ On biometric authentication — I put the link in chat, it's called SumSub [tool:SumSub][link:SumSub shared in chat]. I'd recommend it; it costs about a dollar per full authentication, so you don't want to run it every sign-in. I trigger it only when a user's behavior looks suspicious relative to the base-level authentication on Clerk [tool:Clerk], requiring them to step up to verifying against a valid driver's license or passport.

[00:48:10] Ryan C: I could use this for anti-money-laundering (AML) legislation in the UK — I'm building an estate-agency CRM, and client onboarding requires AML checks that most agents currently outsource to third parties. If I can build this in directly, that's great — I'll definitely be using this.

[00:48:41] Paul Miller: It's well-ranked; I tried three or four tools and this was the best. ▶ Once you've done the initial ID registration, on reconnection you can request just a lightweight face-match instead of the driver's license again — it has you move your head so it can't be spoofed with a static photo.

---

<!--SEGMENT
topic: Follow-up on the "teach" skill
speakers: Morgan, Patrick Chouinard
keywords: teach skill, personalized training, active quizzing, grill me skill, skill design, recursive skills, non-sequential skills
summary: Morgan expands on Patrick's earlier mention of Pocock's "teach" skill, explaining that it tailors training specifically to what a user says they've forgotten rather than repeating known basics, includes active quizzing with scoring, and — like most of Pocock's skills — can be run standalone, out of order, and recursively (e.g., "teach" can teach you how to use "grill me").
-->

[00:50:01] Morgan: The teach skill Patrick mentioned is really nice because it's specific to your request — if you say you learned something before but forgot certain pieces, it redoes the material for that specific scenario rather than teaching all the base content you already know. ▶ It's what you forgot that it focuses on, and the active quizzing part is genuinely useful — it takes you through questions, gives you a score like nine out of ten, and gives you a chance to rework the piece you got wrong.

[00:51:08] Morgan: The skill itself isn't large, and Pocock's "grill me" skill is even smaller — about five lines. ▶ His skills are a great reference for how to write a concise, tight, effective skill.

[00:51:36] Patrick Chouinard: They can be used recursively — "teach" is a good skill for teaching you how to use "grill me."

[00:51:47] Morgan: ▶ Unlike a lot of skills that force strict sequential order (spec, then next spec, then next), most of Pocock's skills can run standalone from different entry points, out of order, depending on the task at hand. Teach is a great skill — that's all I have for now; it's been a busy week focused on migrating from Supabase to Convex and the Expo/iOS piece.

---

<!--SEGMENT
topic: Fully autonomous AI development lifecycle
speakers: Elena, Patrick Chouinard, Daniel Zivkovic
keywords: autonomous AI DLC, guardrails, observability, human-in-the-loop, Superpower, Matt Pocock skills, compound engineering, dark factory, requirement quality
summary: Elena asks for advice on building a fully autonomous AI development lifecycle with guardrails, security, and observability; Patrick argues true full autonomy is impossible without human-supplied intent, contrasts Matt Pocock's flexible-but-advanced skills with the more guided Superpower framework, and stresses that autonomous loops only work when requirements are precise enough to be tested against — a point Daniel reinforces via his "Dark Factory" compound-engineering wrapper that runs overnight but still depends on heavy up-front human planning.
-->

[00:54:00] Elena: <Q>Can I ask advice on fully autonomous AI development life cycle — if anyone has good experience with guardrails, security, observability, etc., any good framework or implementation blueprint?</Q>

[00:54:25] Patrick Chouinard: <A>Fully autonomous AI DLC is something I've seen discussed a lot but it's not well defined, because "fully autonomous" implies no human in the loop — and if that's the case, what are you developing, and for whom? You need at least someone supplying intent; otherwise you might build a very good application targeted at no one. It can't be more autonomous than that.</A>

[00:55:19] Elena: Of course there should be some human in the loop, but minimized — running coding agents on servers with harnesses and skills covering the whole cycle, from assisted requirements gathering and refinement through deployment. AWS has posted something showing a line from "AI system" to "AI autonomous," saying you need to refine your cycle and processes.

[00:57:00] Patrick Chouinard: ▶ From my experience, Matt Pocock's skills [tool:Matt Pocock skills] (grill with docs → spec → ticket → code) are a very good baseline, but they're aimed at more advanced developers — highly flexible and customizable, but you need to know what you're doing. Superpower [tool:Superpower] holds your hand a lot more and is more guided/autonomous, but you have to do it the Superpower way. It's always a trade-off: the more autonomous, the less freedom; the more custom freedom you want, the less autonomous it becomes.

[00:58:09] Patrick Chouinard: ▶ With goal-loops or agent loops, the quality of your initial requirement or intent has to go up tremendously for them to work, because they need something they can evaluate against — hard, testable facts, not opinions. Most people don't have that, which is why fully automated development loops don't work perfectly yet, at least in my experience.

[00:58:52] Daniel Zivkovic: I second that — if you don't know where you're going, you'll end up somewhere else. ▶ I spend a full day planning before kicking off an overnight run of what I call "Dark Factory" (a term from Nate B. Jones), a wrapper around compound engineering — it never works correctly if requirements aren't properly set. Requirements start with brainstorming, so work shifts left; fully automated is a utopia because a human still has to spend the planning time up front.

[00:59:38] Elena: I agree — you need to refine your system and processes, minimize where possible, but it's not easy.

[01:00:00] Daniel Zivkovic: But it's possible to a degree — I run compound engineering fully autonomously on three to five tickets in parallel, though they sometimes conflict, so I prefer running them in sequence overnight and reviewing the list in the morning. ▶ The more hours spent up front on planning, the better the result — there's still a human in the loop.

[00:59:25] Elena: Autonomous agents still need very small, well-defined tasks — give them too much and they drift.

[01:00:48] Daniel Zivkovic: Even specification itself is hard — I'm not a front-end developer, I know what "good" looks like but can't specify it, so I generate three to five different prototypes overnight, review them in the morning like the optometry approach (choose A, B, C, or D), and iterate with feedback each time.

---

<!--SEGMENT
topic: Breaking into AI/software engineering roles
speakers: Varun Sharma, Paul Miller, Daniel Zivkovic, Patrick Chouinard
keywords: AI engineer, junior developer, career transition, self-starter, portfolio, Google ADK, agentic workflows, systems thinking, hiring
summary: Varun Sharma, transitioning careers after seven months of self-taught Python and agent-building, asks what recruiters and companies look for beyond experience in junior AI/software roles; Paul and Daniel emphasize self-starter portfolios and curiosity over credentials, while Daniel highlights a company's "one junior, one senior, both use AI" hiring model and the enduring value of systems thinking.
-->

[01:01:36] Varun Sharma: I've followed Brandon's work for 8–12 months, took his full-stack course and Shipkit [tool:Shipkit], then spent seven months learning Python from first principles, building agents and AI workflows. <Q>I've realized an AI engineer isn't a separate field from software engineering — it's a good software engineer who also knows how to work with and build with AI. Beyond experience, what's a must-have that recruiters or startups usually look for in a junior role?</Q>

[01:03:44] Paul Miller: <A>Running a software business with a team, what we look for now is different from three to five years ago — we want self-starters. What have people built for themselves? What apps, what solutions from nothing? You need to get yourself from junior to intermediate level just to get started with a software house now.</A> ▶ Leverage great YouTube channels and communities for inspiration, and build applications that make you stand out — several people in this community started exactly where Varun is and got there by building and shipping.

[01:06:00] Paul Miller: ▶ Recalibrate how you apply and what you bring — walk in with intermediate-level experience already demonstrated, because no one has time to train juniors from scratch right now.

[01:06:46] Varun Sharma: I've built personal AI workflows on Google ADK [tool:Google ADK], deployed agents on Google Cloud [tool:Google Cloud] saving myself 10+ hours a week, plus some RAG workflows — but making a career switch in my mid-30s without enterprise software experience, I worry about unknown unknowns going into interviews.

[01:08:34] Daniel Zivkovic: "Mind is a dangerous place to be alone in" — talking to AI creates feedback loops that can convince people they're making progress when they're not. ▶ Avery.tv's compound-engineering-framework company hires one junior and one senior together, both using AI, precisely so someone can keep the other honest rather than just echoing AI back. Curiosity is the trait to hire for and to cultivate.

[01:09:51] Daniel Zivkovic: What stays constant is systems thinking — I follow Professor Ali Kessler's free calls (his post-university pricing model is "42 coffees" in your local currency) for exactly that reason; I'm trying to find my own unknown unknowns, aiming to be like "Tariq from Anthropic."

[01:11:03] Patrick Chouinard: Build a portfolio — put as much code as you have ideas for into GitHub and keep it open (commercial work aside); the more visible your public work, the more interesting it is to recruiters.

---

<!--SEGMENT
topic: AI-assisted resume optimization and prompt injection
speakers: Patrick Chouinard, Elena, Ryan C, Paul Miller, Daniel Zivkovic, Varun Sharma
keywords: resume optimization, CV humanizer, AI-written resume detection, cover letter, LinkedIn optimization, prompt injection, steganography, ethical hacking
summary: The group discusses tactics for AI-assisted resume writing — targeting each CV to the specific job rather than embellishing, keeping wording in the applicant's own voice, using paid models, and testing what the market is actually hiring for — before turning into a lighter tangent about "prompt-injecting" CVs (including hidden text and steganography in photos) to game AI-based applicant screeners, with a caution to only do this transparently as a security-skills demonstration.
-->

[01:11:16] Patrick Chouinard: Recruiter expectations change almost daily. ▶ Use AI to optimize how you present yourself for a specific job — restructure your CV to target and extract what's applicable to that role — but don't have AI embellish your profile, because embellishment is either caught by AI screening or exposed in the interview. My CV is never sent raw; it's always re-optimized per client request without inventing anything.

[01:13:16] Elena: I created a skill to shape my CV to each job description while keeping it honest, keeping my own language and style, and generating cover letters — that worked well. I also built a LinkedIn-optimization skill for more traction that my husband uses successfully.

[01:14:22] Patrick Chouinard: ▶ Anything you do repeatedly, turn into a skill — including job search. Also, find a good "humanizer" prompt, because AI-written text is easy to detect; whether that's desirable depends on your positioning, but a CV that reads like generic ChatGPT [tool:ChatGPT] output won't go over well since detection is getting easier.

[01:15:43] Ryan C: ▶ The best CV method: write it yourself, ask AI to analyze and suggest improvements, then rewrite the improved bits yourself too, so it stays in your voice — otherwise you look like every other AI-written CV in the stack.

[01:16:17] Paul Miller: Use a good paid model, not a free/cheap one. Daniel Zivkovic: Run multiple versions for different angles — some optimized for ATS filters, some for humans — and periodically pull job-posting data via API to see what's actually being hired for, then optimize around that rather than what you want to sell.

[01:16:50] Ryan C: If you want to be crafty, you could hide invisible white-on-white text in your CV as a prompt injection telling an AI reviewer to rank you at the top — someone in the UK news did exactly that and got multiple jobs this way.

[01:17:24] Patrick Chouinard: I'd actually do that if positioning myself for a cybersecurity/AI role — showcasing the qualification itself, e.g. hiding a prompt inside a photo via steganography so an AI reviewer picks it up when analyzing the image; it's been done and it works.

[01:18:35] Ryan C / Patrick Chouinard: ▶ The only acceptable way to do this is to be upfront about it in the interview — "I got this interview by demonstrating a security technique" — not to hide it, since getting caught covertly would end the opportunity immediately.

[01:19:26] Varun Sharma: I might actually test one of these tricks on resumes for enterprise roles I'm not that interested in, just to see how their ATS screeners handle it, since there's no real downside for me there.

---

<!--SEGMENT
topic: AI-powered CRM reporting vs. Salesforce
speakers: Paul Miller, Ryan C
keywords: CRM software, Salesforce automation, AI reporting, LanceDB, RAG, grounded data, consumer goods, retail distribution, Omnicom, field capture apps
summary: Paul describes finalizing an AI-powered analytics/reporting layer for his CRM/Salesforce-automation software company, aimed at surfacing grounded, non-hallucinated insights about salesperson and retailer performance for consumer-goods distributors, positioned as a better alternative to Salesforce's own AI push; Ryan connects this to his own experience fighting to get a large agency off Salesforce and offers UK business connections, including at Omnicom Group.
-->

[01:20:17] Paul Miller: I've been finalizing AI reporting for my software company, which does CRM [tool:CRM] and Salesforce [tool:Salesforce] automation for consumer-goods companies and broker-distributors. ▶ The core question in any CRM is how to add AI's benefits without slop that isn't grounded in truth. I built a comprehensive system that looks at all layers of ground truth and runs overnight research to surface deeper insights — gaps in salesperson effectiveness, gaps in what's happening at retailers — that no one has time to look at manually. A few customers are now piloting it.

[01:21:30] Paul Miller: Salesforce.com is our biggest competitor and is throwing money at AI features, but customers are increasingly turned off by how much they get overcharged for poor value; Salesforce still markets itself as the answer to everything and outspends everyone. ▶ I'm using LanceDB [tool:LanceDB] and a modern RAG approach to classify raw data so it stays practical, grounded, and useful — in line with some of what Patrick's discussed around grounding. I'll share examples next week without exposing customer data.

[01:23:47] Ryan C: <Q>Paul, are you making field-capture apps that then feed into the CRM as well?</Q> Paul Miller: <A>Yes — people go into the field to capture insights from conversations with retailers or merchandising audits.</A>

[01:24:16] Ryan C: If you ever bring this to the UK, let me know — I used to work for CPM, part of Omnicom Group [tool:Omnicom Group], and battled to get them off Salesforce because of the cost versus what a small in-house dev team could build; they have ~20 people just maintaining their Salesforce instance. I have connections into major field-marketing companies if you're open to a UK opportunity, though you'd need SOC 2 or ISO 27001 compliance given how security-conscious Omnicom is.

[01:25:22] Paul Miller: Always happy to jump on a plane for a commercial opportunity — I'm a UK citizen as well.

---

<!--SEGMENT
topic: Subscription multiplexing across providers
speakers: Daniel Zivkovic, Ty Wells
keywords: subscription multiplexing, Mark Kashif, intent capsules, Gemini, Anthropic, proxy usage, cold session
summary: Daniel asks Ty whether his subscription-switching setup is based on a tool from Mark Kashif that pools multiple subscriptions to reduce API costs (e.g., for scraping Gemini YouTube videos); Ty clarifies his own system is built around programmatic plan-switching plus "intent capsules" for cold-session starts, not Mark Kashif's proxy utility, which Daniel hasn't yet investigated.
-->

[01:26:37] Daniel Zivkovic: <Q>Ty, I heard Mark [Kashif] talking about combining three different subscriptions into a pool — could that help someone like Paul save on his bill? I haven't researched it myself.</Q>

[01:27:00] Ty Wells: <A>I'm just switching my plans around programmatically — monitoring usage and, when it drops to a certain point, gracefully ending that session and starting a new one.</A> ▶ I use intent capsules that encapsulate full context in short form, so a cold session can start from that and implement the plan completely — that's how I manage it; every session start is effectively a cold session because the capsule gives the agent everything it needs.

[01:27:45] Daniel Zivkovic: <Q>So you're not using Mark Kashif's code for that?</Q> Ty Wells: <A>No, not that.</A> Daniel Zivkovic: My own issue was scraping Gem