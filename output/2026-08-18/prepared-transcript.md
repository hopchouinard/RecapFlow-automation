=== SESSION ===
date: not explicitly stated (recurring Tuesday/Thursday AI builders community call)
duration_estimate: ~1 hour 55 minutes (timestamps span 00:00:00–01:54:46)
main_themes: Claude/Anthropic enterprise deployment and governance, coding-agent harness patterns (Claude Code, Opus, Codex), agentic framework selection and RAG tooling, personal AI side-projects (photo booth, digital signage, cemetery management, video generation), corporate memory architecture, AI consulting business models and defensibility ("moats")

---

<!--SEGMENT
topic: Opening Banter & Meeting Kickoff
speakers: Paul Miller, Tom Welsh, Patrick Chouinard
keywords: three-day week, UK economy, meeting recording, small talk
summary: Informal opening chatter about UK economic history before the call turns to business, with Paul asking Patrick to run the session. Establishes tone and hands off facilitation to Patrick for the roll call that follows.
-->
[00:00:00] Paul Miller: This meeting is being recorded.
[00:00:02] Paul Miller: The UK needs to go back to the 1970s. That's when the economy was going really well.
[00:00:09] Tom Welsh: Three-day week and everything.
[00:00:11] Paul Miller: Yep, yep, yep. Hyperinflation.
[00:00:15] Tom Welsh: I'd love a bit of three-day week, you know, if we could afford it.
[00:00:22] Patrick Chouinard: It's really easy to get a three-day week. It's a lot harder to have one that pays for everything.
[00:00:31] Paul Miller: You can have three days, but we'll pay you for two.
[00:00:42] Paul Miller: ▶ I'll get you to run stuff today, Patrick, if that's okay.
[00:00:47] Patrick Chouinard: Sure, no problem.
[00:00:49] Tom Welsh: How are you, Patrick? Keeping busy, trust.
[00:01:01] Paul Miller: Busy is never a question for Patrick.

---

<!--SEGMENT
topic: Claude Enterprise Rollout & Copilot Security Concerns
speakers: Patrick Chouinard, Tom Welsh, Paul Miller
keywords: Claude deployment, Copilot, Anthropic, security, data sovereignty, Fable, enterprise rollout, 2000 users
summary: Patrick shares that his organization is weeks away from deploying Claude [tool:Claude] to roughly 2,000 employees. Tom recounts an end-user request to bolt Anthropic/Claude onto Microsoft Copilot without any security or data-sovereignty review, illustrating a recurring theme of ungoverned AI tool adoption inside enterprises.
-->
[01:05:05] Patrick Chouinard: We're still working on our deployment. We're just a couple of weeks away to deploying Claude [tool:Claude] to around 2,000 people.
[01:17:00] Paul Miller: Impressive.
[01:18:00] Tom Welsh: We had a great one at work today. So one of the end users was like, "we got Copilot [tool:Microsoft Copilot], can we add Anthropic to it, please? Won't Claude it, Claude Fable, whoever it is." <Q>You do realize that's then just Copilot front end with a Claude back end and a ridiculous costing?</Q> And have you checked security? Have you checked data sovereignty? No, of course not. They're users, they just want to use it.
[01:51:00] Patrick Chouinard: Yeah, specifically Fable — that one is completely barred at work for security reasons.
[02:01:00] Tom Welsh: ▶ Security and data-sovereignty review should precede any ad-hoc tool integration requests from end users, even when the underlying request seems trivial.

---

<!--SEGMENT
topic: Fable Video Generation & Claude Architecture Workflow
speakers: Tom Welsh, Patrick Chouinard
keywords: Mythos Fables, deployable app generation, Claude Opus, Sonnet, architecture design, prompt-to-app
summary: Tom describes an expensive but powerful experience generating a full deployable app from a single prompt using a "Mythos Fables" tool. Patrick contrasts this with his own preference for using Claude Opus and Sonnet [tool:Claude Opus][tool:Claude Sonnet] specifically for architecture design work rather than one-shot app generation.
-->
[02:02:00] Tom Welsh: I played with Mythos Fables that came out. I burnt 300 pounds in an evening, but boy, did it work hard. It's pretty powerful. We fed a prompt and it just went, but it came out with a deployable app at the end.
[02:27:00] Patrick Chouinard: I still prefer to use it to do my architecture, though.
[02:34:00] Patrick Chouinard: Building a whole bunch of architecture and then work for weeks on creating them with Opus and Sonnet.
[03:02:00] Patrick Chouinard: I don't know if you saw, there's a new video from IndieDevDan where he talked about something he called fixing Smartass Opus 5 — basically a supplemental part of a system prompt specifically built to correct the verbosity of Opus.
[03:28:00] Paul Miller: Nice. Yes, I saw. <Q>Have you got the link there? Where was that one?</Q>

---

<!--SEGMENT
topic: Daniel Zivkovic Joins: System-Prompt Append Technique
speakers: Daniel Zivkovic, Patrick Chouinard, Tom Welsh
keywords: IndieDevDan, append system prompt file, Claude Code, verbosity, YouTuber, pi.dev, system prompt hierarchy
summary: First-time attendee Daniel Zivkovic joins mid-discussion. Patrick explains that IndieDevDan built a supplemental system-prompt addition (using Claude Code's "append system prompt file" option) to rein in Opus's verbosity, and clarifies that this is not the same as editing the base system prompt.
-->
[03:32:00] Daniel Zivkovic: Hi. First time here. Sounds like a good topic.
[03:37:00] Patrick Chouinard: <A>A YouTuber called IndieDevDan built a supplemental system-prompt part appended to the end of the [tool:Claude Code] system prompt, to rein in the verbosity of Opus.</A>
[03:53:00] Daniel Zivkovic: Oh, I'll share what I built, but it works for me.
[04:00:00] Patrick Chouinard: No, it's not that it doesn't work — it just talks too much and consumes tokens.
[04:05:00] Daniel Zivkovic: Yeah, it's a needle in the haystack — you have to read everything and then you miss important parts.
[05:14:00] Daniel Zivkovic: <Q>I heard somewhere that changing the system prompt doesn't help because it has to be reminded all the time.</Q>
[05:20:00] Patrick Chouinard: <A>It's not changing it — he's appending this part to the base system prompt. There's an option in Claude Code called "append system prompt file," and you just point to where the file contains the additional part of the system prompt.</A>
[05:44:00] Daniel Zivkovic: I was following IndieDevDan religiously for a year, and then he started talking about pi.dev, and I checked out.

---

<!--SEGMENT
topic: Roll Call Begins: New Members Join
speakers: Patrick Chouinard, Juan Torres, mdcatc
keywords: roll call, community check-in, no comments this week
summary: Additional attendees Juan Torres and mdcatc (referred to as "Morgan" by others) join the call. Patrick confirms there were no community forum comments this week and begins the weekly round-robin update format, starting with Tom.
-->
[06:02:00] Juan Torres: Hey, guys. Can you hear me?
[06:05:00] Tom Welsh: Hey, Morgan.
[06:19:00] mdcatc: Hello, everybody.
[06:32:00] Patrick Chouinard: I've looked at the community — there was no comment this week, so we're just basically going to go through the list of people.
[06:54:00] Patrick Chouinard: So then, the great return of Mr. Tom. What's the deal from you this week?

---

<!--SEGMENT
topic: Tom Welsh: MiniMax Video Generation & Cat Merchandising
speakers: Tom Welsh, Patrick Chouinard
keywords: MiniMax H3, ComfyUI, video generation, custom workflow, merchandising, children's content, AI automation
summary: Tom shares his experiments with MiniMax H3 and ComfyUI for AI video generation, creating a fantasy-cat character for a children's story that he's now considering merchandising as plush toys. He confirms he used a custom ComfyUI workflow rather than defaults and notes his existing AI automation client work remains stable.
-->
[06:57:00] Tom Welsh: I've been playing recently with MiniMax H3 [tool:MiniMax H3], with ComfyUI [tool:ComfyUI], just playing with videos and stuff, making cool content for my kid, and she's loving it. I cannot get over how powerful it is for video creation — ridiculously easy.
[07:34:00] Tom Welsh: I created an image of a fantasy cat lion, then made a cartoon with it, and I'm already thinking about merchandising the cat. So I've got a kid's story coming, a video coming, and friends in the plush/amusement trade I can talk to.
[08:16:00] Tom Welsh: My AI automation stuff's still out there working quite happily, clients are happy.
[08:32:00] Patrick Chouinard: <Q>Did you use any custom workflow in ComfyUI, or just the basic out-of-the-box workflows?</Q>
[08:40:00] Tom Welsh: <A>Oh, no, I found a custom workflow. I'll dig it out and post it.</A> I'm still trying to work out chaining end-frame into the next clip's beginning frame so you can cut sequences together.
[09:02:00] Tom Welsh: But yeah, I'm quite enjoying film photography — I think my Tolkien movie sequence is right in my brain.

---

<!--SEGMENT
topic: Hemal Shah: Agentic Framework Choice for a Commerce Agent
speakers: Hemal Shah, Patrick Chouinard
keywords: agentic frameworks, LangChain, LangGraph, Claude SDK, conversational agent, e-commerce, intent routing, knowledge corpus, order status
summary: Returning member Hemal Shah asks the group which agentic framework is currently recommended for building a conversational e-commerce agent that must answer FAQs, fetch real-time order status, and trigger actions like appointment scheduling. Patrick responds that he's moved away from LangChain/LangGraph toward using the Claude harness pattern directly.
-->
[09:38:00] Hemal Shah: Hello, everyone. I had a long summer break. I have two questions. <Q>From the agentic framework perspective, what agentic frameworks are the recommendation now? LangChain, LangGraph?</Q>
[10:05:00] Patrick Chouinard: <A>It's been a while since I've done any LangChain or LangGraph. I'm mostly working in the Claude environment with the Claude SDK at the moment. There's tons of them coming out, but honestly, I'm starting to use the harness as my workflow more than anything else.</A>
[10:45:00] Hemal Shah: For one of the e-commerce sites, I'm creating a conversational agent, an "AI mode," that needs to do three things: answer from a knowledge corpus (FAQs, static content), fetch real-time data (order status, shipping), and take actions (schedule an appointment). So it's a ChatGPT-like plane interface but more interactive — get the user's intent first, then route to the right knowledge area.
[11:54:00] Hemal Shah: Right now it is text only through the website; eventually we want a voice agent for the same static knowledge base and appointment scheduling.

---

<!--SEGMENT
topic: Daniel's Algolia & Thrillet Recommendations for Grounded AI Search
speakers: Daniel Zivkovic, Hemal Shah, Patrick Chouinard
keywords: Algolia, Algolia Agent Studio, Thrillet, grounded answers, RAG, lead generation, voice AI, CRM integration
summary: Daniel recommends Algolia Agent Studio as a low-code way to build grounded, hallucination-resistant AI search widgets, describing his real-world test on his wife's real-estate site. For voice, he points to Thrillet, noting its founder gives strong consulting advice, though integrating the two remains unsolved for him.
-->
[12:21:00] Patrick Chouinard: Daniel, do you have an answer you want to provide?
[12:30:00] Daniel Zivkovic: <A>I fell in love with Algolia [tool:Algolia]. This is the old enterprise search from before .com, and it really worked well. They did Algolia Agent Studio [tool:Algolia Agent Studio]. I tested it on my wife's real-estate mini-website — I wanted grounded answers to only come from the corpus, and it comes with widgets.</A> ▶ It's free for small sites; specialty is e-commerce (CRM connectivity for discounts/returns), not voice.
[13:20:00] Daniel Zivkovic: For voice channel, there are companies like Thrillet [tool:Thrillet] — I like them because the founder/CPO is really smart and gives consulting-level advice. I don't know how to integrate the two yet. [link: Daniel shared a link to his Algolia experiment in chat]
[14:59:00] Hemal Shah: <Q>Besides Algolia, any other recommendation? If there are limitations, any other recommendation from this group?</Q>
[15:35:00] Patrick Chouinard: <A>Honestly, I'm doing less and less live agents anymore.</A> We'll keep an eye out and let you know if we stumble into anything.
[15:42:00] Daniel Zivkovic: ▶ With a low-code tool like Algolia you get instantly into the head of the business, instead of spending six months tuning prompts before discovering the answers aren't good.

---

<!--SEGMENT
topic: Paul Miller: Mac Mini Setup for 24-Hour Coding Agents
speakers: Paul Miller, Patrick Chouinard, Shakur Abdullah
keywords: Mac Mini, M4 chip, Claude Code, Opus, Codex, Sonnet, Pocock skills, plugin, 24-hour agents, subscription plans
summary: Paul describes wrapping up a large, profitable Australian logistics project and setting up a dedicated Mac Mini (24GB RAM, M4, half-terabyte disk) to run coding agents around the clock, replacing his laptop setup. His workflow chains Claude Sonnet for high-level planning, Opus for delivery, and Codex for validation, using only two $200 plans.
-->
[16:22:00] Paul Miller: Getting to the end of this very large project in Australia — very profitable, but a hell of a lot of work. Got me efficient with an extra monitor managing multiple sessions simultaneously.
[16:55:00] Paul Miller: ▶ I bought a Mac Mini [tool:Mac Mini] so I could run agents the 24-hour way — still surviving with just two $200 plans, Claude Code and one Codex [tool:Codex], but managing to churn through the work.
[17:20:00] Paul Miller: It's Claude Sonnet [tool:Claude Sonnet] that sets the high level and Opus [tool:Claude Opus] that delivers it, then Codex that validates everything.
[17:41:00] Paul Miller: You're using the plugin? I've also been using the Pocock skills [tool:Pocock skills], keeping it nice and lean, focused and aligned.
[18:23:00] Paul Miller: I got a 24 gig Mac Mini with half a terabyte of disk with the M4 processor — just set it all up and it's humming.
[20:16:00] Patrick Chouinard: Shakur asked what the 24-hour setup means — running your agent for 24 hours?
[20:25:00] Paul Miller: <A>Yeah, you're running coding agents 24 hours a day. I was running everything on my laptop and it's not really optimized for that; now it's all running nicely in the Mac Mini remote.</A>

---

<!--SEGMENT
topic: Philippines Support Team & Offshore Staffing Strategy
speakers: Paul Miller
keywords: offshore staffing, Philippines, DevOps support, Asia Pacific time zone, business culture, logistics app
summary: Paul explains plans to fly to the Philippines to recruit an ongoing support and DevOps team for his newly delivered logistics application, preferring Philippines-based staff for time-zone alignment with Australia/New Zealand and better support-side business culture compared to some Indian offshore providers he's used previously.
-->
[19:00:00] Paul Miller: I'm being very cautious in terms of accepting new work — I just want to get stuff done.
[19:00:00] Paul Miller: ▶ Having delivered this whole logistics thing, I'm going to be flying up to the Philippines next month to recruit an ongoing support team, because as I roll things out commercially, I don't want to be doing the ongoing support myself.
[19:21:00] Paul Miller: I don't mind being involved in taking the app to the next level, but I want other people focused on user support and DevOps. The Philippines makes sense in the Asia Pacific region — similar time zone to Australia and New Zealand, and the business culture works well.
[20:00:00] Paul Miller: Some of the Indian offshore teams I've used in the past were highly technical and capable, but not brilliant on the support side — that's been one of the challenges with other organizations.

---

<!--SEGMENT
topic: Chief-of-Staff Harness Pattern for Autonomous Agents
speakers: Paul Miller, Shakur Abdullah
keywords: AIOS, harness, chief of staff agent, master project agent, autonomous coding agents, agent alignment
summary: Paul and Shakur compare notes on keeping long-running coding agents on task without constant supervision. Paul describes a harness/AIOS environment with a "chief of staff" master project-organizing agent that keeps subordinate agents aligned and reports back, which doubled his efficiency in the last week.
-->
[20:36:00] Shakur Abdullah: <Q>Every time I've tried to do that, it always just gets to a certain point — it's like, "no, you're done," and it just stops and doesn't keep going, finish the goal.</Q> I don't know if I'm not persuasive enough.
[21:00:00] Paul Miller: <A>I've set up a bit of a harness, AIOS [tool:AIOS] environment where it's always got things that trigger and keep it going and checking things, and then it reports to kind of a master project-organizing agent. I'm combining the co-work with Claude Code to keep it all aligned and prompted.</A>
[21:25:00] Shakur Abdullah: I still haven't set up my agent OS — it ended up just bothering me, so I never use it. Maybe I'll go back and fix it. It's on my to-do list.
[21:43:00] Paul Miller: ▶ When I first got started with it, it was asking me so many questions simultaneously — having the "chief of staff" managing your agents was a great fix. My efficiency's doubled in the last week because of it.

---

<!--SEGMENT
topic: Daniel Zivkovic: Background & Serverless Toronto Community
speakers: Daniel Zivkovic, Patrick Chouinard
keywords: Serverless Toronto, community meetups, Toronto, real estate, AI chatbots
summary: Daniel introduces himself further, explaining he runs the Serverless Toronto community (around 6,000 members) which shifted from in-person meetups to online after COVID, and that his current AI experimentation stems from boredom and helping his wife's real-estate business.
-->
[22:41:00] Daniel Zivkovic: I just shared that I'm experimenting with AI chatbots and figured that one out. I run Serverless Toronto [tool:Serverless Toronto] community in Toronto, Ontario — real meetups until COVID, then it was easier to do it online. Around 6,000 members, once-a-month meetup.
[23:04:00] Daniel Zivkovic: I was just bored — emptiness, nothing to do, just be on the computer and ride the AI.
[23:14:00] Patrick Chouinard: If Ryan ever joins in — I saw that you're in real estate.
[23:20:00] Daniel Zivkovic: My wife is; I'm just kind of an analyst.
[23:25:00] Patrick Chouinard: Ryan has built a bunch of real estate AI applications before.

---

<!--SEGMENT
topic: Juan Torres: AI Photo Booth Business & Scaling Beyond Personal Presence
speakers: Juan Torres, Patrick Chouinard, Tom Welsh
keywords: AI photo booth, diffusion models, image-to-image pipeline, Instagram marketing, hiring technician, field feedback, San Diego events
summary: Juan updates on his AI photo booth service, which transforms event photos using diffusion-model image-to-image pipelines and 30 selectable styles; he's growing an Instagram presence for it. Patrick and Tom advise him not to fully leave the field when hiring help, since being present yields feedback a technician wouldn't surface.
-->
[24:22:00] Juan Torres: I developed kind of like a photo booth — pictures are taken, then transformed according to prompted styles using diffusion models [tool:diffusion models] in an image-to-image pipeline. So far people in San Diego really like it.
[25:00:00] Juan Torres: I'm developing more transformations (interface allows for 30 styles) and building out an Instagram [link: newly created Instagram, ~10 posts so far] to showcase transformations.
[26:39:00] Patrick Chouinard: <Q>How do you see the expansion of the solution beyond what you're going to be able to be present for, since it's dependent on hardware and you being with the hardware?</Q>
[27:00:00] Juan Torres: <A>That's the question of hiring an AI booth technician to help me install and deploy — I haven't systematized that yet. There's a benefit to staying in the field for immediate feedback and reactions.</A>
[28:07:00] Patrick Chouinard: ▶ I wouldn't recommend getting out of the field entirely, but adding another team member without your baggage of platform knowledge might surface feedback you can't get because you resolve issues in your head automatically.
[29:20:00] Tom Welsh: ▶ It's important not to get out of the field too early — you'll pick up valid user feedback an employee won't surface, but the employee will show you stuff you gloss over because you know which buttons to press. As the product matures, you can take yourself out more.

---

<!--SEGMENT
topic: Morgan (mdcatc): SignPy Digital Signage Deployments
speakers: mdcatc, Juan Torres, Patrick Chouinard
keywords: SignPy, Convex, Raspberry Pi, digital signage, transitional homes, county parks, self-contained HTML slides, QR codes, iCal
summary: mdcatc (addressed as "Morgan") describes SignPy, a rule-driven digital signage system currently deployed at three sites (including transitional homes and a county parks/cemetery client), where content auto-expires and self-contained HTML slides can embed QR codes and iCal barcodes. He's also rewriting an earlier "Class to Curve" project in Convex.
-->
[31:10:00] mdcatc: I spent some time rewriting the Class to Curve project in Convex [tool:Convex] — not a direct translation, since Convex's model simplified things and made some MVP features possible that I'd previously pushed out.
[32:43:00] mdcatc: SignPy [tool:SignPy] is still going well — deployed at three different sites; working on the front end so site administrators can upload content themselves. It's basically a lobby sign with digital content that has automatic expiration rules tied to events.
[33:22:00] Juan Torres: <Q>So like a slideshow?</Q>
[34:00:00] mdcatc: <A>Kind of like a slideshow — as new images are processed they automatically pop up and randomly change, making the photo experience communal and real-time, similar to what Juan is doing with his photo booth.</A>
[34:22:00] mdcatc: Two deployments are in a transitional home, where residents lack proper information access, so it's used for benefits/informational messages. The other client is a county parks department managing a cemetery, wanting a lobby screen with upcoming events and project photos.
[36:00:00] mdcatc: ▶ Field staff can take pictures and upload rough content; AI cleans it up and presents it for the slideshow, matching a skin, adding iCal barcodes for dates and QR codes for addresses — all automated from rough input like scribbled notes.

---

<!--SEGMENT
topic: Morgan: Raspberry Pi vs Fire Stick Hardware Tradeoffs
speakers: mdcatc, Tom Welsh, Patrick Chouinard
keywords: Raspberry Pi 5, Raspberry Pi 4, Fire Stick, self-contained HTML, offline resilience, hardware cost fluctuation
summary: mdcatc explains the SignPy hardware runs standalone on a Raspberry Pi requiring only Wi-Fi, with each slide as self-contained HTML/JS so no external network calls can crash it. He compares Pi 5 vs Pi 4 graphics performance and explains why he abandoned Fire Stick due to its new app-publishing restrictions.
-->
[37:28:00] mdcatc: The Raspberry Pi [tool:Raspberry Pi] is standalone — you just need Wi-Fi configured; if network is lost it keeps recycling its last content forever.
[39:21:00] Patrick Chouinard: So basically you figured out how to do garbage in, nice thing out?
[39:38:00] mdcatc: I built it on Raspberry Pi 5 and quantified it on Raspberry Pi 4 to see it on a cheaper model. Pi 4 is workable, but for crisp graphic animation you should use a Pi 5. Each slide is a self-contained HTML page with its own JavaScript — no outside network calls, so it can't crash from an unavailable server.
[41:29:00] mdcatc: ▶ I looked at a Fire Stick, but they changed their interface to require publishing through their server like the Apple model — before you could install straight to the device. Otherwise it would've been nice since it's only $40–50 and has the needed video driver.
[42:34:00] Tom Welsh: <Q>Is that an eight-gig Raspberry Pi 5?</Q> There are 165-pound options in the UK, pretty close in price.
[42:59:00] mdcatc: <A>Yeah, prices fluctuate — they were well below $200 before chip manufacturers started refocusing.</A>

---

<!--SEGMENT
topic: AI-Assisted Printer Driver Rewrite
speakers: mdcatc, Patrick Chouinard
keywords: label printer driver, Claude, closed-loop testing, USB printer, driver rewrite
summary: mdcatc shares a side experiment where he used Claude to rewrite a legacy label printer's driver for modern operating systems in about half a day, using a closed feedback loop of photographing printed labels and feeding them back to the model for corrections.
-->
[43:17:00] mdcatc: A couple weeks ago I mentioned an old printer I couldn't get drivers for on new OSs, so I had AI rewrite the driver format for the modern OS. Took about half a day — just a USB printer.
[44:46:00] mdcatc: ▶ It's not something I had prior knowledge on writing a driver for — it's now possible to teach yourself quickly how to do something like this with AI doing the heavy lifting.
[45:07:00] Patrick Chouinard: ▶ That sounds like a good use case for a slash-goal with Fable [tool:Fable], because it's easily testable — you can figure out pretty quickly if it works.
[45:26:00] mdcatc: <A>The process found the API, the API was pretty complete, so it wrote tests and printed a label. I took a picture of the label and sent it back to Claude, and it made adjustments from there — a closed loop where I didn't have to describe the problems, I just let it look at the picture.</A>

---

<!--SEGMENT
topic: Heritage Plot Cemetery System & the FOIA Compliance Moat
speakers: mdcatc, Juan Torres, Daniel Zivkovic
keywords: Heritage Plot, cemetery management software, Freedom of Information Act, government compliance, moat, advocacy pressure campaigns
summary: mdcatc describes Heritage Plot, a cemetery management system on hold pending county buy-in, whose defensibility ("moat") is that it's the only system supporting a state-specific FOIA-style legal disclosure requirement no competing cemetery software meets. Juan draws a parallel to labor-union advocacy tactics for pressuring bureaucracies to adopt needed technology.
-->
[46:00:00] mdcatc: Heritage Plot [tool:Heritage Plot] is a cemetery management system, on hold pending the county getting off their "lazy laurels." I don't want to spend more time until I get buy-in and feedback on what they need changed.
[47:20:00] mdcatc: I got into that because an individual at the county has a government requirement — a Freedom of Information Act-style disclosure request — and none of the current cemetery software supports what the state requires by law. ▶ That's the moat around the whole thing: private cemeteries don't fall under the rule, but government-operated ones do, across many counties in that state.
[49:03:00] Juan Torres: From experience working for labor unions, advocacy groups run political campaigns pressuring boards of supervisors or city councils — bringing workers to give testimonies, going to the bosses/directors of departments to create pressure for adopting needed technology.
[51:20:00] mdcatc: <A>Good points, but I have a bandwidth issue right now, and this is a state I'm not in, so it's difficult for me to drive personally; the person I have there has a conflict of interest since he's a county member. Something will happen here soon, I guarantee it.</A>
[52:26:00] Daniel Zivkovic: (asked in text about the cemetery project's origin, addressed above by mdcatc)

---

<!--SEGMENT
topic: The Infinite Game: Rethinking "Finished" in Client Work
speakers: mdcatc, Paul Miller
keywords: The Infinite Game, finite vs infinite games, project completion, scope management, cricket analogy, client perception
summary: Prompted by Paul's comment about wanting to finish projects, mdcatc references the book "The Infinite Game" to reframe business work as cyclical rather than having true completion. Paul agrees but stresses the real challenge is aligning on what "finished" means to the client, drawing an analogy to test cricket innings and crediting a "head of staff" role for enforcing clear deliverables.
-->
[51:59:00] mdcatc: ▶ There's a great book called The Infinite Game [link: book reference, no URL given]. We think of many things as finite games with a clear beginning/end, but life and business are cyclical — there's no true completion, just the next cycle, the next contract. Changing that mindset helps past the anxiety of "wanting something finished."
[53:31:00] Paul Miller: <Q>What's the metric that you're working to? What's the metric in the mindset of the client you're working to?</Q> The biggest pain is the client's perception of what they believe they wanted finished.
[54:23:00] Paul Miller: ▶ You need clear lines to say "this week we're going to complete this," then move to the next phase. In cricket, test matches run five days and can still end in a draw — you focus on what you can achieve in an innings, eating the elephant one bite at a time.
[55:17:00] Paul Miller: Once I had a "head of staff" enforcing clear deliverables aligned to project scope and shutting down scope changes, life became so much better.

---

<!--SEGMENT
topic: IndieDevDan's Append-System-Prompt Technique Explained in Depth
speakers: Patrick Chouinard, mdcatc, Daniel Zivkovic
keywords: append system prompt file, Claude Code, system prompt hierarchy, CLAUDE.md, aliases, ELI, reference numbering, token efficiency
summary: Patrick gives a detailed technical walkthrough of IndieDevDan's system-prompt append technique in Claude Code: content appended this way sits at the same priority level as the base system prompt (reposted every turn, unlike CLAUDE.md which decays in context). He highlights two standout features — command aliases (e.g., "ELI" expands to "explain it to me like I'm 12") and reference numbering (R1, R2, F1, F2) for risks/findings so users can refer back concisely.
-->
[55:45:00] mdcatc: <Q>Patrick, you had mentioned last week about your sarcastic client rules to help Opus not be so verbose.</Q>
[55:55:00] Patrick Chouinard: <A>Last week was just my traditional system prompt copied everywhere. What IndieDevDan published this week takes that to a whole new level.</A>
[56:26:00] Patrick Chouinard: With Claude Code, there's an option called "append system prompt file" — whatever markdown content you put there gets appended to the end of Claude's own system prompt. It's not part of the user prompt or ingested context, so in terms of importance it sits at the same level as the system prompt — even higher than CLAUDE.md [tool:CLAUDE.md], since CLAUDE.md content decays far into context after 20 turns, while the system prompt gets reposted every single turn, so it's always fresh.
[57:24:00] Patrick Chouinard: He puts a set of instructions to make it concise first, then a list of do's and don'ts — like never using em-dashes — plus examples.
[57:49:00] Patrick Chouinard: ▶ One amazing feature is a table of aliases: e.g., the three-letter term "ELI" is defined as an alias for "explain it to me like I'm a 12-year-old," and the model expands it automatically every time it appears — essentially a basic skill embedded directly in the system prompt.
[58:42:00] mdcatc: That's like [Matt] Pocock's context vocabulary [tool:Pocock skills].
[58:52:00] Patrick Chouinard: On top of that, he adds reference numbering — every risk is R1, R2, R3... every finding is F1, F2... so you can refer to "R1" or "F3" later instead of restating the full context.
[59:29:00] Patrick Chouinard: ▶ I've been using it for a couple of days and saw token consumption drop dramatically while producing just as much output; the shorthands became muscle memory within a day.

---

<!--SEGMENT
topic: Over-Engineering Debate & Compound Engineering "Dark Factory"
speakers: Daniel Zivkovic, mdcatc, Patrick Chouinard
keywords: IndieDevDan, over-engineering, compound engineering, Codex, dark factory, max plan, parallel agents, token cost
summary: Daniel and mdcatc debate whether IndieDevDan's techniques are over-engineered, agreeing it's a matter of taking what fits your own problem. Daniel describes his own "compound engineering" workflow — a nightly, unattended setup where Claude and Codex cross-check each other and escalate disagreements to him in the morning — while Patrick notes enterprise per-token billing requires more restraint than subscription-based personal use.
-->
[59:29:00] Daniel Zivkovic: <Q>Loved his work before, but he complicates things — is this the guy who over-engineers sometimes?</Q>
[59:59:00] mdcatc: <A>It looks like over-engineering from your point of view, but when he's gone through a week of processing his own problem, it comes out looking like too much — but it's too much for maybe your problem, not his.</A>
[1:00:11:00] Daniel Zivkovic: I paid for his course when he started; you take what fits from him and go your own way.
[1:00:18:00] Patrick Chouinard: I'm not building a C-suite of agents just yet — I'm more than happy with my chief of staff, but I pick pieces from him, Matt Pocock, and "Superpower," and lately lean more toward "grill me with ducks."
[1:01:41:00] Daniel Zivkovic: ▶ I use compound engineering [tool:compound engineering] — it resonates with older software engineers, it's expensive on tokens but I run it on my max plan at night: parallel agents checking and validating each other, and a small wrapper on top I call "dark factory" — if Claude and Codex [tool:Codex] can't agree, they ask me in the morning.
[1:02:26:00] Patrick Chouinard: ▶ That works well with a subscription, but at my day job there's no subscription — we pay per token, so I always have to think about maximizing value per token spent.

---

<!--SEGMENT
topic: Shakur Abdullah: Shopping List App & Grandparent Call Device
speakers: Shakur Abdullah, mdcatc
keywords: design-to-code tool, shared shopping list, dietary restrictions, boycott list, low-screen device, grandparent calling device, Raspberry Pi cost
summary: Shakur shares a design-link-to-code tool he tested successfully, plus a custom shopping-list app he built for his wife that merges several existing app features (ingredient flags, boycott lists, dietary restrictions, synced lists). He also revisits an idea for a screenless button-based device letting his son call grandparents, but hits cost concerns with Raspberry Pi-based designs.
-->
[1:03:06:00] Shakur Abdullah: Started working on a few projects — finally got a tool where you drop a link in and within a reasonable time frame it gives back usable designs. Sent that to a couple people, they were pleasantly pleased.
[1:03:26:00] Shakur Abdullah: My wife asked for a better system than Apple Notes for our shared shopping list, since it kept dropping and not linking. I smashed together all the different shopping apps we use into one streamlined app — she's using it now. ▶ It scans items in-store, flags ingredients we don't like, checks boycott lists, checks dietary restrictions, and syncs the list between both of us.
[1:04:29:00] Shakur Abdullah: Morgan got me thinking about a project I'd put on the back burner: I saw on X a device someone built for their kid to push a button and talk to a grandparent with no screen. We're trying to go low-screen at home. <Q>My son needs to talk to more than one grandparent — can I put a dial on it?</Q>
[1:05:10:00] Shakur Abdullah: I went back and forth with Claude to make it cheaper and let us choose who to send the message to, but the design relied on a Raspberry Pi, and now that Pi prices are up, that's a sad time.

---

<!--SEGMENT
topic: Hardware Choices for Embedded AI Devices
speakers: mdcatc, Shakur Abdullah, Patrick Chouinard, Juan Torres
keywords: Arduino, Raspberry Pi Zero, Gumstix, embedded hardware, stackable hats, discontinued products, Facebook Marketplace
summary: mdcatc and Patrick discuss embedded hardware alternatives for Shakur's low-power, screenless communication device — Arduino for dedicated single-process use versus Raspberry Pi for full OS support, plus a note that the once-suggested Gumstix product line went out of business in 2025. Juan suggests sourcing used devices via Facebook Marketplace or OfferUp.
-->
[1:05:37:00] mdcatc: You might be able to use Arduino [tool:Arduino] or Gumstix [tool:Gumstix] for your no-screen build — a small USB pad or physical key connected to the device.
[1:06:34:00] mdcatc: ▶ Wi-Fi/Pi has a lot of support and handles a full OS install, but Arduino is a basic language that compiles and flashes directly to the device — smaller, dedicated to one process, not trying to run a whole OS. Arduino also has stackable "hats" that each add a function set.
[1:08:11:00] Patrick Chouinard: Just one note, Morgan — I think Gumstix went out of business at the end of 2025.
[1:08:26:00] Shakur Abdullah: As of August 13th, 2025 — a year ago.
[1:08:39:00] Juan Torres: <Q>Have you tried to get those devices from Facebook Marketplace or OfferUp? I'm pretty sure you can find something cheaper than buying new.</Q>
[1:08:59:00] Patrick Chouinard: <A>If you don't need a lot of power, the Pi Zero is still a possibility, or the Arduino R4 is only about $25.</A>

---

<!--SEGMENT
topic: Ty Wells Brief Check-in
speakers: Ty Wells, Paul Miller, Patrick Chouinard
keywords: late arrival, golf analogy
summary: Late-arriving member Ty Wells briefly checks in, explains he missed the start of the call, and says he'll watch the recording later — a short transitional moment before Patrick's enterprise update.
-->
[1:10:04:00] Ty Wells: Hi, guys. I was going to join at 5, and then I saw it was 5:48, so it was a little late — I'm unprepared, to say the least.
[1:10:17:00] Paul Miller: You're in the rough, Ty.
[1:10:21:00] Ty Wells: I'll watch the video later.
[1:10:28:00] Patrick Chouinard: No problem.

---

<!--SEGMENT
topic: Enterprise TechStack Recommendation Skill for Non-Technical Users
speakers: Patrick Chouinard
keywords: enterprise instructions, Claude Code, tech stack governance, Vercel, Supabase, Anthropic API key, skills, non-technical users
summary: Patrick describes building enterprise-wide Claude Code instructions and a skill designed to stop Claude from recommending unauthorized tools (e.g., a Vercel account, a Supabase account, an Anthropic API key) to non-technical staff who ask how to share interactive dashboards, since such recommendations, while technically valid, aren't feasible inside the corporate environment.
-->
[1:10:35:00] Patrick Chouinard: I've been looking at what IndieDevDan created, since it was part of some enterprise work — we're working on enterprise instructions, the Claude Code setup that affects everyone.
[1:11:01:00] Patrick Chouinard: One situation: we have non-technical people talking with Claude all day building dashboards and HTML reports who now want to integrate interaction into them. <Q>How do I share that with my colleague, how do I make that interaction live in whatever I send?</Q> Claude starts recommending things like an Anthropic API key, a Vercel account [tool:Vercel], a Supabase account [tool:Supabase] — all fun, but not usable in the enterprise.
[1:11:57:00] Patrick Chouinard: ▶ So we need a way to recommend the proper tech stack to non-technical users — I'm building a skill that reads our approved technology stack, understands what's homologated by the business, and what those technologies actually do, so it can recommend the right one at the right point in conversation without making the skill huge.

---

<!--SEGMENT
topic: Level-Zero Support Skill Built from Claude Cowork Pilot
speakers: Patrick Chouinard
keywords: Claude Cowork, pilot program, level-zero support, knowledge base generation, 200 users, 2000 users
summary: Patrick explains a second project: converting three months of manually-answered support questions from a 200-user Claude Cowork pilot into a packaged "level-zero support" skill, so that when the full 2,000-user rollout activates, Claude itself will filter Anthropic's generic answers through the company's own internal processes and known solutions.
-->
[1:12:49:00] Patrick Chouinard: The other project is building what we call a level-zero support skill. We've done a pilot with Claude Cowork [tool:Claude Cowork] for the past three months with about 200 users, and during the pilot I answered pretty much every support question myself using Cowork.
[1:13:09:00] Patrick Chouinard: ▶ That built an incredible amount of knowledge about the type of questions and answers we provide. I used that knowledge base to generate a support skill, so once we activate the 2,000 users, level-zero support will be done by Claude itself — you'll get an Anthropic-quality answer filtered through how we do things, who to contact, and solutions we've already found, all within the Claude Desktop and Claude Code installation.

---

<!--SEGMENT
topic: Enterprise Claude Deployment: AWS Bedrock, Copilot Comparison & M365 Integration
speakers: Daniel Zivkovic, Patrick Chouinard
keywords: AWS Bedrock, Vertex AI, Azure Foundry, Microsoft Copilot, M365 connectors, SharePoint, Teams, Outlook, plugin marketplace, model release lag
summary: Daniel asks how Patrick's company deploys Claude at enterprise scale (AWS, Vertex AI, Azure Foundry, or direct Anthropic license) and how skill-sharing works across teams. Patrick explains they use AWS Bedrock, that Anthropic just released a plugin marketplace and sub-team connector sharing, that M365 connectors give read-only SharePoint/Teams/Outlook/Calendar access, and that Claude is a better agent/system-prompt writer than Copilot despite Copilot "catching up." He also flags that model releases and Claude Code's stable branch lag behind the latest branch by a few weeks.
-->
[1:14:02:00] Daniel Zivkovic: <Q>There are so many ways to install Claude at the enterprise — are you using AWS [tool:AWS Bedrock], Vertex AI, Azure Foundry, or paying Anthropic directly for an enterprise license?</Q>
[1:14:14:00] Patrick Chouinard: <A>We're using AWS, we're using Bedrock.</A>
[1:14:22:00] Daniel Zivkovic: Do they have problems with sharing, like organizing teams, sharing skills between teams?
[1:14:34:00] Patrick Chouinard: <A>They just released the functionality this week — a marketplace. Now Claude AI desktop can leverage the plugins marketplace from the same one used for Cowork, and connectors can now be released to individual sub-teams, not just enterprise-wide.</A>
[1:15:01:00] Daniel Zivkovic: We decided to wait for Microsoft's Copilot license — it's still in beta/frontier for full sharing.
[1:15:18:00] Patrick Chouinard: We've tried both — Copilot's cowork feature isn't bad, but it's certainly not at the level of Anthropic's Cowork. Microsoft has improved a lot lately though; they're catching up, third player, but not as far behind as they used to be.
[1:15:52:00] Daniel Zivkovic: <Q>How do you integrate skills from Anthropic run in AWS with SharePoint/Copilot, since everybody uses Microsoft Office?</Q>
[1:16:10:00] Patrick Chouinard: <A>The M365 connectors [tool:M365 connectors] in the Claude environment are pretty insane — built into the platform, no download needed. It's a read-only access to SharePoint, Teams, Outlook, email, and Calendar.</A>
[1:16:46:00] Daniel Zivkovic: But how about Anthropic Skills feeding into agents other people use in Microsoft Copilot?
[1:17:07:00] Patrick Chouinard: <A>No, those are completely separate — no integration, because they don't use the same principle. Copilot uses "agents," which are really skills and sub-agents in the Claude world. But Claude is actually a better agent writer than Copilot — if you tell Claude to create a system prompt for a Copilot agent, it writes a better one than Copilot would for itself.</A>
[1:18:08:00] Patrick Chouinard: ▶ Be careful — model release and Claude Code version aren't in sync. When Opus 5 [tool:Claude Opus 5] launched, it worked on Claude Code's latest branch, but the stable branch caught up about three weeks later, so people wondering "where is Opus 5?" just weren't on the stable branch yet.

---

<!--SEGMENT
topic: Governance Strategy: Skills vs Global Instructions for Guardrails
speakers: Patrick Chouinard, mdcatc
keywords: global instructions, skills, hooks, citizen developers, vibe coding, sequential discovery, guardrails
summary: Patrick explains why he chose a "skill" architecture rather than a global instruction to stop Claude from recommending disallowed tools to non-technical staff: global instructions can't reference external files via sequential discovery and would become too large. mdcatc suggests using hooks instead, but Patrick clarifies hooks work well in Claude Code but not in Claude Desktop, which is where the ungoverned "citizen developer" recommendations actually occur.
-->
[1:19:40:00] Patrick Chouinard: The big idea is making sure Claude stops recommending stuff not allowed in our environment. I debated making it a global instruction but realized it would be far too big, and global instructions don't support sequential discovery — you can't put links to external files in them. So the only way to make it work is through skills.
[1:20:00:00] Patrick Chouinard: ▶ People working in Claude Code will be able to use that skill or deviate with good reason, but people who "vibe code" only within the desktop app won't be able to deactivate it — citizen developers get more hand-holding, developers get more leniency, but everyone reaches the same production bar.
[1:21:01:00] mdcatc: <Q>Could you solve that problem by using a hook?</Q>
[1:21:07:00] Patrick Chouinard: <A>The hook would work extremely well in Claude Code but extremely badly in Claude Desktop — remember, it's an executive assistant who's asking for Vercel accounts, not a Claude Code user.</A>
[1:22:03:00] Patrick Chouinard: ▶ Any time a request could result in a recommendation of an API key or app platform, it should call the skill — I want to test having the skill referenced directly in the global instruction.

---

<!--SEGMENT
topic: Elijah Stambaugh: Claude Desktop Enterprise Implementation Q&A
speakers: Elijah Stambaugh, Patrick Chouinard
keywords: Claude Desktop, enterprise license, per-token pricing, AWS reseller, Anthropic sales response, support contract, Claude Cowork
summary: New/returning participant Elijah Stambaugh questions Patrick about the mechanics of the enterprise Claude Desktop implementation — licensing cost structure, AWS's role as reseller, and why the organization chose Claude tooling over building a custom front-end harness. Patrick reveals Anthropic never returned their sales calls, so they went through AWS instead, and stresses that only Anthropic's own products come with a corporate-level support contract.
-->
[1:22:37:00] Elijah Stambaugh: <Q>Are you implementing Claude Desktop, and behind that are the connections to Microsoft and everything else in the organization? Are the skills you're developing going to be available to anyone, or proprietary to this client?</Q>
[1:23:11:00] Patrick Chouinard: <A>This is built on client time, so I can share the general idea for you to spawn your own instances of it, but not the source code.</A>
[1:23:41:00] Elijah Stambaugh: <Q>Is it a $20 plan or a corporate deal, and how much does Claude Desktop cost for an enterprise implementation?</Q>
[1:23:49:00] Patrick Chouinard: <A>It's an enterprise license, a corporate deal made through their supplier — I have no idea about the actual cost. We pay per token; there's no subscription concept in the enterprise world, which is why we have to be careful about tokens.</A>
[1:24:30:00] Elijah Stambaugh: <Q>How does AWS fit in if it's Claude Desktop?</Q>
[1:24:40:00] Patrick Chouinard: <A>All the Claude models' base supplier is AWS — they're the vendor of the tenancy and also a reseller of Claude licenses. You could talk to Anthropic directly, but AWS is a reseller.</A>
[1:25:14:00] Patrick Chouinard: ▶ Anthropic never returned our calls, and we're a pension fund with a $600 million investment value, not a mom-and-pop shop. We called AWS and had someone in our office 20 minutes later.
[1:26:38:00] Patrick Chouinard: We're not using Slack, we're using Teams — Cowork is Slack-only for now; we'll see when it's available in Teams. Cowork lives only in Claude Desktop, not yet in the Claude.ai web interface, and isn't available through any other harness.
[1:28:34:00] Elijah Stambaugh: <Q>Why not consider your own front-end harness instead, for more context control?</Q>
[1:28:34:00] Patrick Chouinard: <A>Support. There's no support contract with a Pi harness or an Omnigen — those are nice, but don't come with a support contract. Claude Code, Claude Desktop, and Claude Cowork come with an enterprise/corporation-level support contract. If your tool can't be supported by the supplier, it doesn't get into the enterprise.</A>

---

<!--SEGMENT
topic: Corporate Memory Architecture: Git-Backed Hierarchical Knowledge
speakers: Patrick Chouinard, Elijah Stambaugh, Daniel Zivkovic
keywords: corporate memory, Git, Markdown frontmatter, hierarchical memory, knowledge graphs, second brain, Azure DevOps, context loading
summary: Patrick outlines his next major challenge — building layered corporate memory (personal → team → corporate) using Git as the underlying version-control and reconciliation mechanism, with a Markdown-plus-frontmatter file structure where large topic files become tables of contents linking to detailed sub-files. Elijah and Daniel relate this to knowledge graphs and "second brain" concepts.
-->
[1:29:34:00] Patrick Chouinard: That's going to eventually link with corporate intelligence and corporate memory — how do we manage memory at a corporation level? Everybody has a personal wiki, but we need to bring that knowledge to team level, then eventually assemble it at corporate level. ▶ Memory layering is my next challenge for the next couple of months — anyone who's worked with hierarchical AI memory, comments welcome.
[1:30:14:00] Elijah Stambaugh: <Q>Are you thinking of storing that information in a database, or in GitHub repos, and what's the path for the agent to read and understand it?</Q>
[1:30:32:00] Patrick Chouinard: <A>We're looking at using Git — not necessarily GitHub or Azure DevOps specifically, but the concept of Git itself, so memory can be versioned and rolled back using source-management capability. We're transforming Azure DevOps from a development-support platform to a data-publishing platform — the actual production system is the Git repo, because we're managing data that doesn't live well in a database, and it'll be affected by many people concurrently, so you want Git's reconciliation capability with the model managing the Git complexity out of the user's way.</A>
[1:33:16:00] Patrick Chouinard: We're working with Markdown with frontmatter headers, and developed a context file structure — categories like contacts, ideas, projects, info, decisions each have their own Markdown files. When they get too large at team level, the initial file becomes a table of contents linking to more detailed articles — e.g., projects.md links to individual project memory files, decomposed further if needed. ▶ The model walks the relationship until it reaches the needed information, loading as little context as possible to answer the user's question.
[1:34:37:00] Daniel Zivkovic: So it sounds like knowledge graphs or these "second brains."
[1:34:45:00] Patrick Chouinard: It's inspired by knowledge graphs, LLM wikis, and other approaches — I'm picking and choosing functionality rather than waiting on one solution to fit everything.

---

<!--SEGMENT
topic: Patrick's Training Generator for Scaling Enterprise Onboarding
speakers: Elijah Stambaugh, Patrick Chouinard
keywords: training generator, self-sustaining training, curriculum, web search fallback, progress tracking, three trainers, 2000 users
summary: Elijah asks how Patrick trains the 2,000-user rollout. Patrick describes a plugin he built, the "training generator," which inspects any curriculum or document corpus and generates a self-sustaining training session that answers from the repo, falls back to web search for tangents, and tracks a progress file so users can resume where they left off.
-->
[1:36:16:00] Elijah Stambaugh: <Q>Do you have a stock curriculum, group training, or one-on-ones? How does the VP's secretary get up to speed on Claude?</Q> She gets Claude AI, not Claude Code, thank God.
[1:36:51:00] Patrick Chouinard: <A>For training, I built something I call the training generator — a set of skills that inspect any curriculum or data source (a repo or document corpus) and generate a self-sustaining training out of it. You just ask whatever question; because it's Claude behind the scenes, if the answer's in the repo it answers that way, and if you go on a tangent it can web-search and answer sideways. I built in keywords to ask the training skill to get back on track, since it has a progress file tracking where you are.</A> ▶ That's the only way I can manage to train 2,000 people with three trainers.

---

<!--SEGMENT
topic: Elijah Stambaugh's AI Consulting Business Model
speakers: Elijah Stambaugh, Daniel Zivkovic
keywords: AI implementation consulting, second brain for companies, six-month contract, agent replacement, business analyst, lead agents
summary: Elijah describes his consulting practice: building the "context layer"/second brain and agent-management tooling for small companies, currently acting as the agent himself while building the automation that will eventually replace his manual work, structured around a lower-cost six-month contract that transitions to a repriced ongoing engagement.
-->
[1:38:22:00] Daniel Zivkovic: <Q>Elijah, what do you do? You ask good questions.</Q>
[1:38:24:00] Elijah Stambaugh: <A>I work with companies to help them implement AI. Right now I'm working with a handful of companies building the kind of context layer for the organization — a second brain for the company — and the agent side, a way for people to manage what the agents are doing on their behalf, similar to Grok Bot and Buzz-type tools.</A>
[1:39:22:00] Elijah Stambaugh: Right now I'm in the consulting/implementation phase — I am the agent. I do all the work in Claude Code, build the apps and tools, sit in meetings, analyze transcripts — I'm basically a business analyst — then turn around and tell my team what to build, mostly lead-generation processes.
[1:41:14:00] Elijah Stambaugh: ▶ I've got a six-month contract at a lower dollar amount; my goal within that time is to build what the company needs and show them the value, then reprice at the end — not necessarily for more money, but for less of my time since agents will already be doing the work, plus an option to keep paying for my time separately.
[1:47:00:00] Elijah Stambaugh: ▶ I'm looking for an ICP of companies that are growing, have money and a need, but aren't going to build this internally themselves — construction companies, chicken farmers, luxury hotel management, indoor farming — not software development companies.

---

<!--SEGMENT
topic: Selling AI Services When Everyone Can "Vibe Code"
speakers: Daniel Zivkovic, Elijah Stambaugh, mdcatc
keywords: vibe coding, sales difficulty, ICP, code is cheap, differentiation, education contracts
summary: Daniel raises the hard problem that "everyone feels like they can code it themselves now" (especially in Canada), making sales the real bottleneck, not building. Elijah agrees code is no longer the value; the group discusses how some clients (a chicken/microgreens indoor farming operation using an "anti-gravity" tool) run wild with self-built systems, while others need low-cost, low-touch educational engagements just to stay engaged.
-->
[1:44:41:00] Daniel Zivkovic: <Q>Nobody's buying anything because they can do everything — how do you sell the service?</Q> For me coding is like running away from reality — I have three products, find something at a client, write it, repackage it, nobody buys it, move on to the next thing. The code is not the value anymore.
[1:44:11:00] Elijah Stambaugh: I don't go near [pure dev work] because if they can vibe code, they think they'll figure it out. Part of what I'm doing is just helping the team think — "did you guys do this, have you thought about this" — real low-dollar contracts, an hour meeting a week just to keep them educated and abreast of the space, not building for them.
[1:47:00:00] Daniel Zivkovic: One of my clients d