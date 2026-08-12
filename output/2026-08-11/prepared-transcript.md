=== SESSION ===
date: not specified in transcript (weekly recurring community call)
duration_estimate: ~1 hour 36 minutes (00:00:01–01:36:21)
main_themes: AI agent orchestration ("chief of staff" / coworker models), enterprise Claude adoption and governance, Claude Opus verbosity management, Convex.dev real-time sync architecture, personal AI assistants (Hermes/Honcho), ROI measurement for AI-assisted development, and a range of personal side-projects (genealogy app, golf coaching AI, AI photo booth, biometric driver verification, AI video generation)

<!--SEGMENT
topic: Session opening and attendance
speakers: Patrick Chouinard, mdcatc, Ty Wells, Paul Miller
keywords: weekly meeting, attendance, recurring invite, community call
summary: Brief opening banter noting lower-than-usual attendance, attributed to Patrick forgetting to post the weekly meeting invite. Establishes that the group is a recurring weekly AI-focused meetup with a habitual attendance pattern.
-->
[00:00:01] Patrick Chouinard: This meeting is being recorded.
[00:00:08] Patrick Chouinard: Hey, how's it going?
[00:00:13] mdcatc: Good, how are you doing? I had my mute.
[00:00:16] Patrick Chouinard: I'm doing good, just I don't see a lot of people tonight. We'll see. I'm tired.
[00:00:40] mdcatc: It's my nap time.
[00:00:42] Patrick Chouinard: I think it's been my nap time since yesterday morning.
[00:00:50] mdcatc: One of those weeks?
[00:00:52] Patrick Chouinard: We're about three weeks away until the go-live with 2,000 users getting clogged.
[00:02:47] Patrick Chouinard: Hey, Paul.
[00:02:49] Paul Miller: Hey, guys. I have the feeling it's going to be an intimate session tonight.
[00:02:53] Paul Miller: Ah, something else going on up in the northern hemisphere there.
[00:03:01] Patrick Chouinard: I think it might be my fault. I forgot to post the weekly invite and thought that, oh, people are so used to it, they're going to be there anyway. <Q>It seems like it might not be the case.</Q>
[00:03:14] mdcatc: <A>I just always go to school and click in through that link. That's always right there.</A>
[00:03:25] Patrick Chouinard: I created dependency, it seems.
[00:03:45] Paul Miller: Oh, well, we've got the quorum here, so we're all good. So what's happening in everyone's world at the moment?

<!--SEGMENT
topic: Chief of staff agent architecture
speakers: Patrick Chouinard, mdcatc, Paul Miller, Ty Wells
keywords: Claude, Claude Code [tool:Claude Code], Cowork [tool:Cowork], chief of staff model, assistant model, human-in-the-loop, agent orchestration, Jira, local git repo, decision-making
summary: Patrick describes abandoning the "assistant" model for a "chief of staff" model, where Cowork coordinates work, tracks obligations in a local git repo/ledger, and hands off implementation to Claude Code, leaving him only to make rapid-fire decisions. Paul and Ty independently report converging on the same architecture, indicating this is an emerging pattern across the group for scaling agentic work beyond what a human can personally coordinate.
-->
[00:03:59] Patrick Chouinard: Yeah, can start if you want, actually this week I realized that there's just too many tasks to manage, and I keep on jumping on every one of them... using Claude as an assistant was no longer enough, because it's a bit like rocket fuel — the more fuel you put, the more fuel you need in order to lift the fuel that you just put in, so coordinating the agents at some point becomes the work. ▶ So I decided to skip completely the assistant model and go straight to the chief of staff model.
[00:05:03] Patrick Chouinard: Since we're in the Claude world at work... Cowork is my chief of staff. It coordinates with Claude Code through a single repo that is not in Azure DevOps or GitHub [tool:GitHub] — it's just a local Git repo that lives by user profile. In there, there's a ledger, a charter, a list of to-dos... it shares the actual writing with Claude Code. Whenever Claude Code is doing something, it reports to that repo.
[00:05:48] Patrick Chouinard: Whenever Cowork is looking at what I have to do, it looks at my Teams, my calendar, my emails, Jira [tool:Jira], and the local ledger. It does a briefing every morning... it always has, here's what you need to work on. ▶ If it has enough context, it's going to provide me the initializing prompt for the next Claude Code session I need to start.
[00:07:00] Patrick Chouinard: So basically, I'm just giving decisions all day long... it's basically the ecosystem of Claude that does all the work now.
[00:07:15] mdcatc: <Q>So you're the ultimate human in the loop.</Q>
[00:07:19] Patrick Chouinard: <A>Yeah, I'm the human.</A>
[00:07:25] Patrick Chouinard: Hopefully at some point Anthropic will be brilliant enough to realize that Cowork should be able to talk to Claude Code so I don't have to do the plumbing... they really, truly [are] talking to each other. So the executing and the coordinator.
[00:08:10] Paul Miller: It's funny you got to that conclusion in the last week because that's exactly what I've been doing as well... each of the Claude Code sessions write back to themselves with what they're looking at... that saves it to a message box that the main chief of staff is looking at. ▶ But it needs to come back to me for a certain type of decision because it can't do lots of noise... you can't do it as an assistant anymore. You've got to be sort of higher level than that.
[00:09:36] Ty Wells: I think we're on the same Kool-Aid because I'm literally doing the exact same thing... it has to make decisions... I'm giving it more and more decisions and actually having it show me only the [things] I need to make. I don't need to know about the things that are working smoothly.
[00:10:44] Patrick Chouinard: The coordinator in my team told me, wow, you've never had so clean of a Jira stack on your side. ▶ I told my chief of staff that it needed to document in Jira to a level where another instance of itself could take that ticket and implement it.
[00:11:13] mdcatc: You need to get your chief of staff on the payroll so you can collect that money that's saving the company.
[00:11:19] Patrick Chouinard: Oh, it knows which team member it can write email to directly in its own voice.

<!--SEGMENT
topic: Timing expectations and agent burnout
speakers: Paul Miller, Patrick Chouinard, Ty Wells
keywords: burnout, timing expectations, Bastian, logistics project, Opus 4.5 [tool:Claude Opus 4.5], task duration, decision fatigue
summary: Paul raises the practical challenge of processing a high volume of agent decisions, referencing a project with Bastian where setting clear timing expectations with Claude was crucial since tasks tend to expand ("concertina effect"). The group agrees this timeline drift is a real issue amplified by Opus 4.5's verbosity.
-->
[00:12:00] Paul Miller: I think one of the practical challenges is if you're not doing it this kind of way, you end up going through a kind of burnout with the volume of brain-numbing crap you have to process. ▶ Probably the biggest thing I want to see is progress.
[00:12:45] Paul Miller: I was talking to Bastian yesterday, we're doing this project with a logistics company in Australia... one of the things he discovered with Claude was to actually be quite decisive on your timing expectations with the work that you're asking it to do... it feels that there's like a moving timeline. A task that should really be completed within an hour might be taking three or four hours, and that's got a concertina effect on everything else. <Q>Do you guys experience that challenge where it just kind of keeps going and thinking it's got unlimited time?</Q>
[00:14:07] Patrick Chouinard: <A>Yeah, Opus [4.5] has been a little bad on this one. It's a lot more verbose and sometimes takes more time. So if you have infinite money, you can always switch to fast mode, but not necessarily a solution for everyone.</A>
[00:14:26] Paul Miller: Well, yeah, Opus [4.5] is definitely talkative.

<!--SEGMENT
topic: Managing Claude verbosity with skills and styles
speakers: Ty Wells, Patrick Chouinard, mdcatc, Paul Miller
keywords: Opus 4.5 verbosity, Matt Pocock, wait-what skill, style templates, natural language skill, hooks, tokens
summary: The group discusses the excessive verbosity of Claude Opus 4.5 and shares mitigation tactics: Ty's natural-language/verbosity-reduction skill, a hook that proved wasteful, and Matt Pocock's "wait, what" skill that re-simplifies confusing paragraph outputs. Patrick plans to build separate style templates for his chief-of-staff versus implementer agents.
-->
[00:14:31] Ty Wells: Oh my God. I literally almost put a hook in to say, hey, bring this down a notch. But then I realized it was first bringing me its results and then firing that hook and then redoing. I was like, that's a waste of time and tokens. So I changed the settings to reduce how verbose it is.
[00:14:53] Patrick Chouinard: ▶ That's my next step — because now they have style templates you can put to Claude, I want to work on style templates specifically... one for my chief of staff, one for Claude Code the implementer, really split the way they talk... and don't give me a report of 3,000 words about one coding session.
[00:15:19] mdcatc: So last week I had brought up the fact that Opus [4.5] was verbose, but also that sometimes it puts a whole paragraph in there and I don't even understand what it's trying to relay to me. And then Pocock came out with a skill called "wait, what?" [tool:wait-what skill] — so you get that paragraph, and it goes and redoes it in more simplified [form].
[00:16:02] Ty Wells: Yeah, I've got a natural language skill... but, oh my God, this thing just talks too much.
[00:16:19] Paul Miller: I've got to try that "wait, what" — that sounds right up my street at the moment.
[00:16:23] mdcatc: ▶ Yeah, look at Pocock's skill list. He's got it in there.

<!--SEGMENT
topic: Whisperflow meeting transcription tool
speakers: Ty Wells, mdcatc, Paul Miller, Patrick Chouinard
keywords: Whisperflow, note taker, transcription, speaker recognition, Otter, Fathom, real-time transcription
summary: Ty demonstrates running Whisperflow's note-taker live during the call to test its real-time transcription and speaker-recognition capability. Paul compares it to Otter and Fathom, which he currently uses, noting Otter's reliable transcripts but weaker video handling.
-->
[00:16:27] Ty Wells: By the way, guys, I'm running Whisperflow's [tool:Whisperflow] note taker just to test it out. I don't know if you guys have seen it or used it yet. It looks pretty good. I ran it in a meeting earlier. It was great. So I'm running it on this call, too.
[00:16:42] mdcatc: <Q>Does it run in the meeting or separate from the meeting?</Q>
[00:16:46] Ty Wells: <A>It's separate from the meeting, but it's hearing the voices... it's got my mic taken over, but it's working with the mic... it's also listening.</A> And it's transcribing real-time here.
[00:17:09] Paul Miller: <Q>How has it been in terms of learning, understanding the people, remembering the people that's coming in the transcription detail?</Q>
[00:17:22] Ty Wells: <A>I haven't really tested that yet, but this is Paul Miller speaking right now.</A>
[00:17:26] Paul Miller: Okay, so it's getting that from the stream.
[00:17:41] Paul Miller: Because I normally use Otter [tool:Otter], which is pretty good. Fathom's [tool:Fathom] been good, but Otter's quite reliable in terms of pure transcript, but then the video part's never as good.
[00:18:00] mdcatc: <Q>Can you [set it] up like if we were to do introductions at the beginning, then voice match and pick up the person's name?</Q>
[00:18:08] Ty Wells: <A>I don't know, I haven't — I've just clicked it on today.</A>

<!--SEGMENT
topic: Enterprise Claude license and access tracking
speakers: Patrick Chouinard, Paul Miller
keywords: Claude enterprise, license distribution, Entra ID groups, compliance API, admin API, Azure, Claude Cowork, Claude Code, governance dashboard
summary: Patrick describes building an enterprise dashboard to track Claude license and access distribution across ~2,000 users spanning Claude AI chat, Cowork, and Claude Code, each governed by separate Entra ID groups. He notes Anthropic's enterprise tier exposes an admin API (with heavily restricted compliance endpoints) that enables this kind of management automation, unlike the more limited Teams tier.
-->
[00:18:38] Patrick Chouinard: The only thing else is I'm working on something to track the access and the license distribution of Claude. It's going to be a nice enterprise project because we're distributing over 2,000 licenses in a month, so we need to track the request.
[00:19:00] Patrick Chouinard: Every subsystem in the Claude ecosystem is tracked separately — Claude AI (desktop/chat), Cowork, and Claude Code for developers. Some have chat plus Cowork, some chat plus code, some all three. Those are all Entra groups... plus we have security harnesses for Cowork and Claude Code users, also distributed by Entra ID group.
[00:19:45] Patrick Chouinard: For those of you who have worked in enterprise environments, requesting membership to a group and getting membership to a group are two completely different things. ▶ So it became an entire management dashboard of tracking — a user profile model of who has what, and what group memberships they must/must not have.
[00:20:31] Paul Miller: <Q>Does Claude play nice in terms of providing data back into that?</Q>
[00:20:36] Patrick Chouinard: <A>Yeah, actually, the enterprise layer provides you an API to see everything that's in the admin window.</A>
[00:20:52] Patrick Chouinard: The only thing you have to be careful about is the compliance API because this one has a metric ton of legal framework attached — with that API you could pump every single prompt of every single user, so there's tons of red tape around that one, but for management it works pretty well.
[00:21:26] Patrick Chouinard: ▶ There's a huge gap between Teams and Enterprise [tiers] — Teams is okay-ish but not even close to the control you have with enterprise licenses, and not anywhere close to the price either.
[00:21:56] Patrick Chouinard: You'll have to update often because there's a brand new screen and brand new API that appear on a weekly basis.

<!--SEGMENT
topic: WhatsApp-based family history project
speakers: Ty Wells, Paul Miller
keywords: family history, WhatsApp, genealogy, family tree visualization, terrain UI, globe view, birthday map, multilingual chat
summary: Ty demonstrates a personal project built for his daughter that ingests years of WhatsApp family group chat history and automatically constructs an interactive family tree, globe map of locations, and birthday visualization. He plans to extend it to his wife's Spanish-language family chat and add a timeline/journey map feature.
-->
[00:22:55] Ty Wells: I have a project that I will show you — it's a family history project. My youngest daughter was asking me for more information about my family... it's a WhatsApp login... it sent me a WhatsApp code that I grab and put in here to log in.
[00:23:46] Ty Wells: What this is, is the ability for me to see where I fit in the family, and it's associated all my [connections]... I took from my mother and my father's side, all the history from these WhatsApp family group chats, and had it build out the association of how people are linked together.
[00:24:38] Ty Wells: You can come in here and I can go find myself in the tree... then drill into something and see exactly where they're at.
[00:25:00] Ty Wells: I can pull up my brother — he gets a color based on his conversation... all of this is accurate, and if you're a family member you can go in and change and correct whatever you want.
[00:25:39] Ty Wells: Then, of course, I've got a globe — everybody's in the Bahamas there, some people in the US... Now I've got this birthday terrain — here's the birthday of everybody... like a street map, and I can click on somebody to see their details.
[00:26:36] Ty Wells: The next thing is a journey/timeline with locations... this is what I'm going to give my daughter so she can go research me and all the cousins. I'm extending this to my wife who's Chilean and speaks Spanish, so I've got to transcribe that group chat too and build the same thing. So when you connect spouses, your connections grow from here.
[00:27:15] Paul Miller: Well, have fun.
[00:27:20] Ty Wells: ▶ It didn't hallucinate this information — this is what you said... it's just a visual representation of [the WhatsApp chat], updating from live chat data two to four times a day.

<!--SEGMENT
topic: AI-assisted golf swing coaching
speakers: Ty Wells, Paul Miller
keywords: Garmin watch, GPS, golf swing analysis, pattern detection, coaching AI
summary: Ty describes reusing GPS-tracking code (originally built to find a lost pendant) with his Garmin watch to map his golf course play and correlate swing quality with behavioral factors. The AI identified a pattern that talking too much or waiting too long between swings correlates with bad shots, prompting Ty to adjust his on-course behavior.
-->
[00:28:51] Ty Wells: Oh, I'm on a new [golf] swing... I'm actually implementing a swing I paid for years ago.
[00:29:06] Paul Miller: <Q>Are you getting the AI to analyze your swing?</Q>
[00:29:13] Ty Wells: <A>Yeah, that's the other part. It's taking my Garmin watch, which has GPS position... I reused that same code to map the course I'm on, the hole I'm on. I'm constantly saying what happened, why it was a bad shot... it's analyzing that with the course itself and telling me... it's like a coaching [tool].</A>
[00:29:53] Ty Wells: <Q>Yesterday I said, is there a pattern to what I'm doing when I have these bad swings?</Q> <A>They said yeah, there is a pattern: one, you talk too much, and you wait too long between swings... whenever I'm making fun of somebody on the course, seems like I screw up... or if I'm waiting more than five minutes.</A>
[00:30:27] Ty Wells: ▶ So I'm going to be talking less on the golf course, just an FYI, and see if I can break that pattern.
[00:30:48] Ty Wells: This is the best time to be building stuff.

<!--SEGMENT
topic: Convex.dev migration for real-time carpool app
speakers: mdcatc, Paul Miller, Bastian Venegas Arevalo
keywords: Convex.dev, Supabase, real-time sync, multi-tenant, WorkOS, T3, indexing, database costs, stateless architecture
summary: Morgan (mdcatc) explains prototyping a migration of his multi-client "Carpool" app from Supabase's socket-based sync to Convex.dev's native real-time sync to better handle hundreds of concurrent school-tenant connections. Bastian, an experienced Convex user, endorses the move, highlighting WorkOS integration for multi-tenant auth, full-stack type safety for agent-driven development, and cost-safety via proper indexing.
-->
[00:31:17] mdcatc: One of the things I'm looking at right now is for the Carpool app, because it is so reactive and multi-client reactive, I'm looking at switching that back into Convex.dev [tool:Convex.dev], which has a built-in sync mechanism that is really slick. I did a prototype... to test out the infrastructure and make sure it could handle 300 clients or more at a time... a lot better than the Supabase [tool:Supabase] method I used with the previous version.
[00:32:36] Paul Miller: <Q>Why did you go down Convex? Did you talk with the system about architecture and the shortfall to get guidance?</Q>
[00:32:45] mdcatc: <A>I went down Convex because I was looking for something that had native built-in sync — if two clients are looking at the same data and I update it, the other client automatically sees my update. No refresh, no communication between clients. Your queries are all subscribed views into the data.</A> ▶ I needed it because any time the tenant updates information, it needs to pop up on the students'/classroom screens automatically without polling a socket.
[00:34:00] Paul Miller: Yeah, that would be a little bit complicated.
[00:34:15] mdcatc: That's what I have right now with Supabase — a socket you call that sends the update when the table updates... it works okay, but by the time I have a hundred schools, that's going to be 3-4,000 connections pounding the system.
[00:35:00] mdcatc: What brought me down that path was I saw it in a video — I think it was one of T3's [tool:T3] videos, and he had mentioned Convex.
[00:35:37] Paul Miller: Bastian's a big user of Convex. <Q>Any advice for Morgan before he makes this plunge?</Q>
[00:35:49] Bastian Venegas Arevalo: <A>It should all work pretty well. If you're going to do something multi-tenant, Convex integrates really nicely with WorkOS [tool:WorkOS], which you can use for social logins... having this full-stack type safety mechanism where your agent can find out about your schema and functions makes it very easy to steer the agent instead of going to the Supabase dashboard. I haven't run into any problems like exhausting your connection pool.</A>
[00:37:00] Bastian Venegas Arevalo: ▶ The worst that could happen is you may need to upgrade your plan, but the billing is very affordable. There are also plugins for Convex for Claude Code and Codex.
[00:38:04] Paul Miller: <Q>You hear some scary stories about people getting bill-shocked with Convex. What's the way for Morgan to safeguard any risks?</Q>
[00:38:21] Bastian Venegas Arevalo: <A>As long as you're not trying to do a bunch of transactions, indexing the queries makes the most of the work — instead of calling the database many times, you call an index and that saves a bunch of traffic.</A>
[00:39:40] Bastian Venegas Arevalo: The guy with the highest Convex billing is Theo, who uses it for T3Chat [tool:T3Chat] — like $6,000-$7,000, but that makes sense with hundreds of thousands of users, all transactional real-time chat. For a stateless application, everything runs serverless from Convex, which kind of replaces your Vercel [tool:Vercel] backend.
[00:40:32] mdcatc: Mind if I reach out to you if I have questions?
[00:40:36] Bastian Venegas Arevalo: Yeah, of course, please do.

<!--SEGMENT
topic: Automated book and podcast publishing pipeline
speakers: mdcatc, Paul Miller
keywords: agentic automation, deterministic scripts, publishing pipeline, audiobook, podcast automation, manuscript processing
summary: Morgan describes a client-facing automation he built that takes an unformatted manuscript and cover art and deterministically generates paperback, hardback, ebook, and audiobook outputs, with a new in-progress workflow for automatically generating a podcast from the client's recordings.
-->
[00:40:46] mdcatc: I had a client who does all these books, right? So I put a whole automated agent process together to take what she gives me — basically the manuscript with no formatting, and a badly formatted cover — and the script automatically processes all that data into four different outputs for each book: paperback, hardback, e-book, and an audiobook (done but not posted yet).
[00:41:28] mdcatc: ▶ Right now I'm working on a process for her podcast so that it automatically generates the podcast from her recordings. Fun little agent work, but nothing visible other than the end product — the workflow all happens inside Claude with a bunch of deterministic scripts.
[00:42:00] mdcatc: That's pretty much it for this last week of sitting on my laurels, doing nothing until Saturday — it took four days [to recover from vacation] this last week.

<!--SEGMENT
topic: Enterprise adoption skepticism and persuasion strategy
speakers: Rod Morrison, Paul Miller, Patrick Chouinard
keywords: data scientists, skepticism, adoption resistance, ROI, personality profiling, McKinsey, BCG, change management, project swap experiment
summary: Rod describes driving Claude adoption among a skeptical team of ten data scientists while facing pressure from his CRO to quantify ROI. Paul shares his strategy of building Claude-based personality profiles of team members to tailor persuasion, and Patrick describes a decisive experiment where swapping project assignments between resistant and adopting developers proved the productivity gap and broke resistance.
-->
[00:42:40] Rod Morrison: I'm running a team of data scientists... putting rigor around usage, standardization, code standards, how do we log issues, cradle to grave... I report directly to the CRO and he wants to understand the return on investment. Typically we have 2.5 data scientists assigned to a project — how can we compress that using Claude Code? Haven't quite figured out a way to do that yet.
[00:44:57] Rod Morrison: Being in that sort of administrivia wears you out sometimes.
[00:45:15] Paul Miller: <Q>I was listening to your comment about dealing with skeptics.</Q> I ended up, my strategy had been — while my CTO was away, I rewrote what the guys were supposed to be doing in a long weekend instead of six months, and that was the last straw for my CTO. ▶ I built a personality profile understanding in Claude — I have a project for each of my team members, looking back to previous emails and discussions, and it builds a strategy of what's engaging to deal with those people, where their hot buttons are.
[00:47:21] Rod Morrison: We have two sides of the business — technical (data engineers/scientists) and business (former McKinsey, BCG). The management consultants have fully adopted... but they don't understand that a static HTML file with fake data does not make an enterprise application. I'm wondering if there's some fear of being replaced on the data scientists' part.
[00:49:23] Patrick Chouinard: <A>I faced every single one of those issues. The most resisting members were more team members than management. We found one member of a team that was resisting a lot, and we simply swapped projects with another member — you say your method works, no problem, you're going to take on his project and he's going to take on yours. Both flat-out no context, starting from the same point.</A> ▶ Bizarrely, the agentic-aided developer tripled the delivery of the traditional guy. At that point it's a taste [issue] — it has nothing to do with ability. That eliminated a lot of resistance pretty fast.

<!--SEGMENT
topic: Governance through skills and plugins
speakers: Patrick Chouinard, Rod Morrison
keywords: enterprise instructions, Claude MD, skills, plugins, living specifications, SDLC, artifacts, Figma, Claude Code, GitHub Copilot, code freeze
summary: Patrick explains that enterprise-level Claude governance is now implemented through mandatory enterprise instructions, skills, and plugins rather than rules and process documents — covering tech-stack constraints, onboarding flows, and a full SDLC rework to treat outputs as "living specifications" rather than throwaway prototypes. Rod corroborates with a real incident of unmanaged production-data prototypes breaking before a client demo.
-->
[00:50:56] Patrick Chouinard: One of the worst things when you deploy Claude at the enterprise level is you get a bunch of people coming to you saying "I need an Anthropic API key, I need access to Supabase and Vercel — Claude told me that['s what I need] to publish the thing it created for me." ▶ [You need] enterprise instructions to say here's the tech stack, here's what you do, you never recommend any of those things.
[00:51:44] Patrick Chouinard: We just started a work group to rethink the entire SDLC for agentic work at the enterprise level. All the UX team are on board too — how we're going to supplement our Figma team using Claude [Cowork for] design, outputting to Claude Code and GitHub Copilot [tool:GitHub Copilot], since we have both populations internally. ▶ The governance is no longer implemented through rules and process — it's implemented through skills and plugins.
[00:53:00] Patrick Chouinard: The artifacts [tool:Claude Artifacts] are great, but you have to guide it — people will say "I want to share this and this person doesn't have a Claude license," and Claude says "create a web page and get an Anthropic API key." That's the part you have to be careful about — Claude presents it to users who have no idea what it's proposing.
[00:53:39] Rod Morrison: Standardizing on everything goes into GitHub, period, hard stop. I had a situation with 30 people in the audience at a client, and the night before they're making dramatic changes to the prototype, something broke. ▶ 72-hour code freeze before [a demo] — we're just fixing bugs. Production data was promised in this prototype, and I was like, we're not setting ourselves up for success there. He was using Cowork [for a customer-facing solution] — Claude hallucinated. He didn't know anything about the Claude MD [tool:Claude.md], just putting some guardrails around it.
[00:54:50] Patrick Chouinard: That's where you need to manage your user. For me, all Cowork deployments have an onboarding skill we built — we don't let them just go have fun with Cowork. The onboarding builds a Claude.md for them, builds a context file, structures their directory... they're confined to a single top-level directory.
[00:55:30] Patrick Chouinard: ▶ For prototypes, we no longer call them prototypes — we call them living specifications. Whenever it creates a static HTML, it's created with a skill that inserts comments that Claude can read to derive a functional spec to give to Claude Code to build a real application.

<!--SEGMENT
topic: Measuring ROI of AI-assisted development
speakers: Rod Morrison, Patrick Chouinard
keywords: ROI, token consumption, GitHub activity tracking, productivity metrics, quality of output, job displacement
summary: Rod raises the question of how to measure real productivity ROI from Claude adoption, initially considering GitHub-activity-based tracking. Patrick warns this is dangerous since raw output (tokens, lines of code, PRs) can be trivially inflated, and argues ROI must be based on end-deliverable quality/functionality per token, illustrated by a real example of two developers with vastly different token spend and output value.
-->
[00:57:43] Rod Morrison: What about the ROI piece? I was thinking okay, first get everybody into GitHub... I can parse that at a [team] layer just to see if people are working, because everybody's remote.
[00:59:06] Patrick Chouinard: That's very dangerous, because in the world of AI, if you start to count ROI based on the number of things created, Claude can generate a truckload of useless things in half an hour. ▶ The reality is you have to look at the end deliverable — solution per token, not just tokens consumed or lines of code or PRs completed. Those can be faked extremely easily.
[00:59:49] Patrick Chouinard: We've had a developer consume like $2,000 worth of tokens in a week but deliver three basic solutions, and another guy using $800 worth of tokens but delivering half a year's worth of deliverable.
[01:00:18] Patrick Chouinard: ▶ So ROI is not just ROI of the technology, it's ROI of the quality of operator you have. AI is not going to steal anyone's job — somebody who knows how to use it properly will. Learn to use it properly, you're going to keep your job. Don't, and you're going to lose it to another human.
[01:00:50] Rod Morrison: It's not a fad. It's not going anywhere.

<!--SEGMENT
topic: Juan's AI photo booth project update
speakers: Juan Torres, Paul Miller
keywords: diffusion AI, UX/UI design, AI transformations, mirror booth, event safety, cable covers
summary: Juan gives a routine project update covering UX/UI, data science/engineering work, and diffusion AI engineering to add new AI transformation styles for his event photo/mirror booth, plus physical safety improvements (trip-wire cable covers) after a prior event hazard.
-->
[01:01:03] Juan Torres: I haven't done other events. I do have two events scheduled, one for September, another for January. But other than that, I've been doing boring UX/UI design, data science work, some data engineering, and then I have to do some diffusion AI [tool:diffusion AI] engineering in order to add more styles of AI transformations.
[01:01:33] Juan Torres: ▶ I did some purchases in order to create a more safe setup — cable covers on the ground, because last time there weren't any and people could trip over them, so I had to tape them and they looked pretty ugly. So I made some cable and trip-wire cover purchases.
[01:02:07] Juan Torres: It hasn't been that exciting as last Saturday. I don't think there's a very specific question that I have right now.

<!--SEGMENT
topic: VC funding versus partnership strategy
speakers: Juan Torres, Paul Miller
keywords: venture capital, funding, partnership model, distribution, dilution, business strategy, event industry
summary: Juan and Paul discuss whether Juan should pursue venture capital funding for his AI photo/mirror booth venture, given how far solo AI-driven development can now go without upfront capital. Paul frames the modern alternative as smaller-equity partnerships focused on distribution/introductions rather than traditional large-dilution investment, referencing Bastian's suggestion of revenue-share partnerships with venue/event companies.
-->
[01:02:24] Paul Miller: <Q>You were thinking about potentially getting someone on board on the funding side or doing the pitch. How did you go with that?</Q>
[01:02:34] Juan Torres: <A>I haven't contacted anyone. The September application for the [funding] that Brandon recommended, I still have to prepare for it. I haven't asked myself the right questions about whether venture capital funding would be useful, particularly at this stage.</A>
[01:03:52] Paul Miller: ▶ In this world where you can do so much with AI, what is it exactly that an investor or partner could truly add? Is it just money that's the barrier? ...You don't need the money to build the code really quickly, but you do need the people, the introductions. ...That's a very different value proposition when you're going to an investor — dilution would be much lower, getting a smaller share but just focusing on distribution.
[01:06:39] Juan Torres: I don't really think I need other engineers or technicians at this point — it's the funding to get several moving parts that have nothing to do with the technical aspect, like the media. I do want to still get involved [in operations] because it's fun and I get a lot of feedback from the field.
[01:08:10] Paul Miller: Bastian's just made a comment there — maybe the real opportunity is around the partnership for distribution, with event/venue companies as partners or investors.
[01:08:41] Juan Torres: ▶ Maybe partnership as a contractual thing, like they get a cut for every contract that gets [signed] at the venue event... I agree with you, Bastian, that's a really good suggestion, and it goes along with Brandon's suggestion of giving away some of the hardware for them to have and offer as a business.

<!--SEGMENT
topic: Photo booth hardware costs and licensing potential
speakers: Ty Wells, Juan Torres
keywords: mini PCs, mirror booth, hardware cost, licensing, Facebook Marketplace, freestanding kiosk
summary: Ty asks Juan about the cost of his mirror-booth hardware setup, prompting a discussion of a possible licensing/distribution model for freestanding interactive kiosks versus Ty's own TV-based "crowd picks" fire-stick product.
-->
[01:10:27] Ty Wells: <Q>Juan, what's the cost of your equipment, your setup?</Q>
[01:10:32] Juan Torres: <A>I got two mini PCs through Facebook Marketplace, and I cleaned them for security... the Mirror Booth also got through Marketplace... configured to have fancy LED around and a very glossy display screen so it looks like a mirror, with hardware engineering to plug in my mini PC or GPU. Maybe I'm in the $1,500 [range] for the investment.</A>
[01:11:42] Ty Wells: ▶ I'm wondering, because I did something similar — the crowd picks, on a fire stick thing, but it's not freestanding. You actually touch and feel it rather than on a TV. I think that definitely adds value... that might be something you could license out as a package — if you took the venue to an event, I know they would use it. Ping me on the side if you want to talk further.

<!--SEGMENT
topic: Biometric verification for trucking compliance
speakers: Paul Miller
keywords: chain of responsibility, driver compliance, Veriff [tool:Veriff], biometric authentication, subcontractor fraud, government ID validation, live face check-in
summary: Paul describes a client problem where independent truck drivers were falsifying identity to work excessive hours across multiple companies, creating chain-of-responsibility legal risk for the business owner. He researched and adopted Veriff, a biometric/government-ID verification API, to authenticate drivers and validate live check-ins.
-->
[01:12:53] Paul Miller: One of my customers is having issues — they have a lot of independent truck drivers doing deliveries. In Australia, the chain of responsibility always flows to the directors of the business, so if drivers are taking on too much work, you need to verify how many hours they've done, whether they've had enough sleep, etc.
[01:13:46] Paul Miller: The problem the business owner was having is that subcontractors were lying about who they were — people were doing 17 days of work without a break for multiple companies, and they weren't able to verify the right driver was accepting the right job.
[01:14:21] Paul Miller: ▶ I started doing research into biometric validation and came across a company called Veriff, V-E-R-I-F-F, a really good API [link:Veriff — biometric/ID verification API]. You build a profile based on government ID, and that individual does live face check-ins, and you can verify situational context proving it's the same valid person.
[01:15:16] Paul Miller: My whole productivity has increased quite significantly [using] Patrick's chief-of-staff operation and the Pocock skills working as well.

<!--SEGMENT
topic: Claude personality and sarcasm customization
speakers: Patrick Chouinard, Ty Wells, Paul Miller, Ryan C
keywords: sarcasm, personality tuning, tone control, cultural humor, chief of staff persona, audience-aware writing
summary: Patrick shares a tactic for reducing Claude's verbosity by giving it a sarcastic personality, which naturally produces shorter, simpler sentences, and describes how his chief-of-staff agent adapts its tone (sarcastic, polite, or overtly AI-voiced) depending on which specific person it is writing to. The conversation pivots into a light discussion of sarcasm as a cultural/business norm across countries.
-->
[01:16:32] Patrick Chouinard: ▶ If you want a good way for Claude Code or Claude in general to talk less, I find that a very sarcastic personality tends to use a lot of smaller words — the more sarcastic it is, the simpler the words it uses, and the funnier the conversation ends up being.
[01:17:16] Patrick Chouinard: Honestly, on Teams these days, the most amount of stuff in my team is just snippets of Claude cranking me up like this.
[01:17:24] Paul Miller: <Q>Is sarcasm, the use of sarcasm/humour, popular in Canada?</Q> I certainly know in Australia, New Zealand, and the UK it's pretty much the normal in a business context.
[01:17:53] Patrick Chouinard: <A>Oh yeah, no, definitely — whenever it communicates with the outside world, it has instruction to lessen the sarcasm. It knows there's enough material in its memory that it will literally tell me, "this is an outside email, so I'm going to turn down the sarcasm."</A> ▶ It even knows depending on who it's writing for — this person, I can be very sarcastic; this person, very politely; this person, in my own voice, and it's going to know it's the AI writing.
[01:18:42] Paul Miller: Talking about sarcasm — certainly from living in the UK for many years, that's the capital of sarcasm. <Q>What's happening in your world, Ryan, and what's happening with sarcasm in terms of working with your clients?</Q>
[01:19:08] Ryan C: <A>It's essentially our only source of joy in the UK. Everything else has been drained from us. So that's all we've got left. Don't take the sarcasm from us as well.</A>

<!--SEGMENT
topic: Video production and AI animation projects
speakers: Ryan C, Paul Miller
keywords: NDA project, micro-sites, video generation, Higgsfield, ElevenLabs, animation, avatars, HeyGen, IDE replacement
summary: Ryan shares an NDA-bound private project generating micro-sites for wealthy clients, and details an in-progress ~1-minute animated video made with a modified video-generation repo shared by Scott, combining Higgsfield's CLI tool MCP'd into ElevenLabs for voice/sound. He also previews that Scott is building a Cursor/VS Code replacement tool with harness-related features, to be demoed by Scott directly in a future session.
-->
[01:19:22] Ryan C: I've done a private project that I can't share because I had to sign an NDA... should lead to a lot more micro-sites showing off assets... for some of the biggest and wealthiest people in the world... that came out of nowhere just from networking with estate agents.
[01:19:59] Ryan C: I'm making an animated video at the moment with a video generation repo that Scott shared with me, and I've modified it — it's essentially like an animation studio has made it. It's incredible.
[01:20:32] Paul Miller: <Q>How long is the video?</Q>
[01:20:36] Ryan C: <A>About a minute. There's 10, 12 scenes now... voice-over, music, sound effects, the whole lot. I've got a Higgsfield [tool:Higgsfield] CLI tool, MCP'd into 11 Labs [tool:ElevenLabs], and using Higgsfield with all the various video generation tools.</A>
[01:21:01] Ryan C: If this one does what I want it to do, I'm going to get all of their training material — I think I'm going to have avatars, bring in HeyGen [tool:HeyGen] for avatar stuff.
[01:21:10] Ryan C: ▶ Scott wanted me to share with you guys that he is currently working on a replacement for cursor or VS Code, adding a bunch of harness-related features. He's going to show it off next time he comes on — he's on holiday this week but has been texting me incredibly excited about it, making himself a macOS .dmg program.

<!--SEGMENT
topic: Hermes personal AI assistant setup
speakers: Ryan C, Patrick Chouinard, Paul Miller
keywords: Hermes, personal assistant, Scott, phone call automation, Google integration, digital PA, Honcho AI, memory layers, multiple profiles
summary: Ryan describes onboarding onto "Hermes," a phone-call-capable personal digital assistant (built by Scott) that he is branding as a named PA with her own email, planning to onboard 30 clients into it and integrate it with his calendar/client-portal data. Patrick contrasts this by explaining he runs separate Hermes profiles for his chief-of-staff versus personal-assistant roles, using Honcho AI as an external memory/reasoning layer.
-->
[01:22:26] Ryan C: Scott's 99% through setting me up with Hermes [tool:Hermes]. I've just got to onboard all of my clients — I listed them all out yesterday, I've got 30 clients to onboard.
[01:22:52] Ryan C: I'm calling it my digital personal assistant — they've given it a human name and a human email. The idea is I can say "put it over to my PA," she's got an email, she's going to be making phone calls. Scott's hooked it up with a phone call service in the US; I found an equivalent in the UK.
[01:23:22] Ryan C: I'm going to add bits that pull in from a couple of my apps to give it more context — dates and times from my client book, client portal... I've moved my entire business over to Google to enable this to work properly.
[01:24:27] Paul Miller: Biggi was asking, Ryan, are you using additional memory layers in your Hermes? If so, which ones?
[01:24:24] Ryan C: <A>The best person to ask would be Scott — I haven't asked very many questions, if I'm honest.</A> I think, Patrick, you've probably deviated from the way Scott set it up.
[01:24:52] Patrick Chouinard: ▶ Yeah, on my side, I use Honcho AI [tool:Honcho AI] — it's an LLM [tool:LLM] memory layer... it absorbs all of the memory content but reasons about them. There's a small cost, but since opening my account about four months ago they gave me $100 worth of credit and I still have $75 left, and I talk to that thing 12 hours a day. It analyzes the memory before storing it and after, to re-inject it as very specific context, so it doesn't overwhelm the agent's context — it just gives it whatever context is necessary to answer the question just asked.
[01:24:40] Patrick Chouinard: I actually use multiple profiles — my chief of staff is not the main profile of Hermes; my main profile is the personal assistant. The chief of staff is a secondary profile with another system prompt and another set of memory completely independent from the first, and it talks to the personal assistant.
[01:25:42] Ryan C: I'm personally not going to use Hermes to code — I'm using it more as business admin, because I have pretty severe ADHD and struggle with boring [tasks]... last year I put off ringing my dentist for six months. ▶ The theory is I can just say "Imi, call my dentist, make an appointment" — it knows my diary and has Google Maps integration.

<!--SEGMENT
topic: ADHD, productivity, and learning styles
speakers: Ryan C, Juan Torres
keywords: ADHD, Atomic Habits, Healthy Gamer GG, productivity bursts, dopamine, medication, creativity, self-awareness
summary: Following the Hermes discussion, Ryan and Juan discuss managing ADHD without medication — Ryan explains his non-linear productivity pattern (bursts of intense work offset by procrastination), his aversion to reading versus podcasts/video, and views medication as risking creativity. Juan references the book Atomic Habits and the Healthy Gamer GG channel as related resources.
-->
[01:27:58] Juan Torres: My brother also has ADHD, and I've recommended him to read Atomic Habits [link:Atomic Habits book], but he said this doesn't work for people with ADHD.
[01:28:20] Ryan C: I don't do a huge amount of reading on behalf of my ADHD — my brain just doesn't do reading anymore... I can listen to podcasts for hours and hours, I struggle with audiobooks conversely... I've figured out the best way for it to learn is I've got to be interested in it.
[01:29:00] Ryan C: I'm one of those people that'll have bursts of productivity, and then bursts sat scrolling through Instagram for two hours, but I need that because the bursts burn me out quicker. ▶ I don't medicate because I've seen people medicate and it changes them — it's a bit of a superpower really, because I've got a fair amount of creativity that comes with it.
[01:30:08] Juan Torres: I've seen Healthy Gamer GG [link:Healthy Gamer GG YouTube channel], it's really good.
[01:30:18] Ryan C: It's a blessing and a curse, that's for sure.

<!--SEGMENT
topic: Session wrap-up and closing remarks
speakers: Paul Miller, Bastian Venegas Arevalo
keywords: session close, weekly wrap-up
summary: Brief closing exchange where Bastian confirms he has nothing further to add beyond project work, and Paul begins wrapping the session before Alex joins with a late addition.
-->
[01:26:26] Paul Miller: Cool. Thanks, Ryan.
[01:26:30] Paul Miller: Bastian, did you have anything you want to add?
[01:26:34] Bastian Venegas Arevalo: No, nothing really — heads down on the project. I just found that they also have moved some items to the deleted folder, so that was a blessing.
[01:30:50] Paul Miller: Anyone else want to raise anything before we wrap for today? No?
[01:31:00] Paul Miller: Guys, have a wonderful week. Let the superpower agent that manages the chief of staff make your weeks better going forward. It's good we're getting to the same page on that.

<!--SEGMENT
topic: Moonshots podcast recommendation and funding update
speakers: Alex, Paul Miller, Juan Torres
keywords: Moonshots podcast, Peter Diamandis, AI longevity, X (Twitter), funding close, pitch success
summary: Alex, joining late, recommends the "Moonshots" podcast with Peter Diamandis and co-hosts as a positive, technically substantive source on AI and longevity news, and shares that he successfully closed a follow-on client deal from a pitch, marking a return to development work after the pitching process.
-->
[01:31:24] Alex: Just before leaving, guys, I don't know if you guys know of this podcast called Moonshots [link:Moonshots with Peter Diamandis, YouTube] with Peter Diamandis.
[01:32:00] Alex: For guys, there's Dr. Alex [Wissner-Gross?], Dave Blondin, Salim Ismail, and Peter Diamandis, and it has been like my go-to place for the last three weeks... it's a two-hour long pod, but they do really talk very interesting stuff on the edge of AI and longevity. Peter has many portfolio companies, Dave has been training [neural] nets for 40 years.
[01:33:42] Juan Torres: <Q>Alex, is this like the AI engineering YouTube channel in which they go through cases of the implementation of AI for a business?</Q>
[01:33:45] Alex: <A>Actually, it's Peter's personal channel... they talk about the newest news, what model, what was the most impactful news on AI and longevity. They do talk also a lot about X.</A>
[01:34:16] Alex: ▶ Their objective is to try to have a positive view on AI, so everything is like empowerment, not this drama type of thing.
[01:35:24] Alex: And just a little update, I did close my follow-on with the one client, so I'm just going back to the programming stash instead of the pitching table.
[01:35:39] Paul Miller: <Q>So the pitch that you did in terms of the closed pitch, that got them across the line?</Q>
[01:35:45] Alex: <A>Yeah, yeah, exactly — by that I mean the payment went through.</A> So it's for real, I'm just cranking tokens now.
[01:36:03] Paul Miller: Brilliant. Well done. Well done.
[01:36:14] Paul Miller: Thanks, everyone. Have a great week and we'll see you next week. Cheers. Have a good one, guys.

=== UNRESOLVED SPEAKERS ===
- mdcatc (raw handle/username, not resolvable to a canonical full name from the supplied alias data)
- Ryan C (partial name; last name not resolvable from the supplied alias data)
- Alex (single first name only; surname not resolvable from the supplied alias data)