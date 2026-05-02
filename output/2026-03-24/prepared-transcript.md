=== SESSION ===
date: 2026-03-24
duration_estimate: ~155 min
main_themes: [eliminate-myself-from-systems philosophy + auto-eval feedback loops (Brandon Hancock), Anthropic Architects + Google Generative AI Leader exams + study-site builders, FaceGate web-native face-ID for shared-device authentication, Terraform + agentic DevOps for AWS resource provisioning, Databricks Lakehouse architecture + organic GitHub-discovery client wins, AI personality kit auto-deployed across CLAUDE.md / GEMINI.md / Copilot, Ironclaw secure-by-design AI-assistant white paper (governance-first + smart router), Stripe key hell + ShipKit pattern + Codex+Vercel reliability, consulting program design (embed + equipped + 30-40 skills per business)]
===

<!--SEGMENT
topic: pre-meeting + gym AI banter + Sanity CMS + RecapFlow auto-research
speakers: Patrick Chouinard, Marc Juretus, Ty Wells
keywords: gym AI app, member cap, Sanity CMS for non-profits, history society site, RecapFlow auto-research integration, Karpathy auto-research philosophy, two-loop pattern (mechanical + comments)
summary: Patrick joined a new gym whose owner is building a CloudCode app — caps members and bans tripods. Marc has a similar gym-app idea with leaderboards, currently building a history-society donations site using Sanity CMS. Patrick's been pairing RecapFlow with Karpathy's auto-research philosophy via Cowork: a fast inner mechanical loop (links extracted, compression bounds, no markdown leakage) plus a slow weekly outer loop where viewer comments become training data.
-->

[00:00:04] Patrick Chouinard: Hey, What's it, Patrick?
[00:00:11] Patrick Chouinard: I've talked about you this week at my gym.
[00:00:16] Marc Juretus: Oh, my gym.
[00:00:17] Marc Juretus: You like it?
[00:00:19] Patrick Chouinard: Yeah, yeah.
[00:00:21] Patrick Chouinard: I joined about a month ago.
[00:00:25] Patrick Chouinard: Pretty good.
[00:00:27] Patrick Chouinard: Just because the guy was developing an application using Claude Code for his gym, so you came to mind with your gym application.
[00:00:40] Marc Juretus: Yeah, it's pretty, it's fun how you can basically customize it to how you work out.
[00:00:45] Marc Juretus: Like, my particular problem is 530, Chess tries, I don't want to look at all my exercise in my database, it randomly pulls them off.
[00:00:54] Marc Juretus: Yeah, that sounds about right today.
[00:00:57] Marc Juretus: As long as it doesn't draw  I don't want, but yeah.
[00:00:59] Marc Juretus: It's pretty cool.
[00:01:02] Patrick Chouinard: Actually, I just talked to the guy at the reception, but I want to talk to the owner and invite him to the call if he wants to.
[00:01:09] Marc Juretus: Yeah, that's cool.
[00:01:11] Marc Juretus: Yeah, honestly, the coolest thing I can do with it is I can go into the admin profile and I can set you up like a workout and you just go in and your workout's there.
[00:01:23] Marc Juretus: So it's pretty slick.
[00:01:25] Patrick Chouinard: No, exactly.
[00:01:26] Patrick Chouinard: I remember when you showed it and I thought like, what, for a gym owner, it might be an interesting set of ideas.
[00:01:34] Marc Juretus: Yeah, yeah.
[00:01:35] Marc Juretus: You should have like a leaderboard, like everyone wants to one up.
[00:01:39] Marc Juretus: Once you induce competition in the end, people are just working out more.
[00:01:42] Marc Juretus: So it's good.
[00:01:43] Marc Juretus: Like I did 10,000 steps.
[00:01:45] Marc Juretus: Yeah, did 10,005, you know.
[00:01:49] Marc Juretus: So there you go.
[00:01:50] Patrick Chouinard: Yep.
[00:01:51] Patrick Chouinard: And I really like that, Jim, actually, because the guy did something I've never seen before [tool:CloudCode gym app].
[00:01:56] Patrick Chouinard: He has the cap on members.
[00:01:59] Marc Juretus: Nice.
[00:01:59] Marc Juretus: literally boogavoise, to
[00:02:00] Patrick Chouinard: So it's not like as many people who want to register as possible.
[00:02:04] Patrick Chouinard: No, I guarantee that many people top and not one more.
[00:02:10] Patrick Chouinard: So, no, really nice.
[00:02:12] Marc Juretus: Yeah, that's the beauty of doing that.
[00:02:15] Marc Juretus: Hey, what's up, Ty?
[00:02:16] Patrick Chouinard: Hi, Ty.
[00:02:17] Marc Juretus: That's the beauty of doing that where he probably had an experience for overcrowded gyms.
[00:02:22] Marc Juretus: There's a lot of people complaining about that because, as you know, you probably know, working out, Monday is generally National Chess Day.
[00:02:29] Marc Juretus: So, good luck getting a bench on that if you're overcrowded that day.
[00:02:33] Patrick Chouinard: Yep, exactly.
[00:02:35] Patrick Chouinard: So that's why I like the place.
[00:02:36] Patrick Chouinard: It's never overcrowded.
[00:02:38] Patrick Chouinard: And he also bans tripods.
[00:02:43] Ty Wells: That's a good thing.
[00:02:45] Patrick Chouinard: So, yeah, maximum number of members and no tripods.
[00:02:48] Ty Wells: Which gym is this?
[00:02:50] Patrick Chouinard: Oh, it's my local gym here.
[00:02:53] Marc Juretus: Yeah, man, proud of you.
[00:02:55] Marc Juretus: Good, man.
[00:02:55] Marc Juretus: I love people getting in the mix, man.
[00:02:57] Marc Juretus: Yeah, you saw some gold.
[00:02:59] Marc Juretus: Yeah.
[00:03:01] Marc Juretus: I tell people when I give them diets and stuff, the problem is the first five pounds is easy because generally most of it's water, five to seven.
[00:03:09] Marc Juretus: It's when you try, all right, now when you want to go, it's one to two, and you're like, how come I got five?
[00:03:14] Marc Juretus: Well, that's not how that works.
[00:03:15] Marc Juretus: It's water weight, and you got to go from there and work.
[00:03:18] Patrick Chouinard: Oh, don't worry.
[00:03:19] Patrick Chouinard: I'm three years in, three times a day, three times a week, so.
[00:03:23] Marc Juretus: Oh, okay.
[00:03:24] Marc Juretus: I'm sorry.
[00:03:24] Marc Juretus: I thought you just started out.
[00:03:25] Marc Juretus: You were talking about joining the No, I changed.
[00:03:27] Patrick Chouinard: I changed gym because my other one, uh, closed, so.
[00:03:32] Marc Juretus: Got you.
[00:03:33] Patrick Chouinard: And I had the other one using AI all the way, so now I'm doing it again with that one.
[00:03:42] Marc Juretus: Doing some site for, there's like a local history, uh, history society that takes donations.
[00:03:47] Marc Juretus: I guess the last web developer, like, kind of left them hanging.
[00:03:51] Marc Juretus: So, but they want to be able to modify, and I used to always, when I would do that, not regularly, I'd point them towards WordPress and set them up, but this uses this
[00:03:59] Marc Juretus: Some library I've never heard of before called Sanity CMS, so it's like some, it's some headless CMS, I'm like, all right, let's see what it does.
[00:04:09] Patrick Chouinard: Cool.
[00:04:12] Patrick Chouinard: And on your side, Ty, were you able to make everything work properly from the, I think it was the core backup you downloaded?
[00:04:23] Ty Wells: Yeah, yeah, no, I did.
[00:04:24] Ty Wells: I had fixed it and then just sent you that message.
[00:04:28] Ty Wells: So that's the only thing I'm using these days, I'm not even nowhere, and I've extended it beyond, just for my own use, as I basically find an issue, I would extend it a little further to, if I'm repeating the same thing over and over.
[00:04:46] Patrick Chouinard: Yeah, actually, I'm just working with it right now.
[00:04:49] Patrick Chouinard: I gave it the repo for RecapFlow, you know, the thing I build that builds the Recap every week?
[00:04:57] Ty Wells: Yeah.
[00:04:57] Patrick Chouinard: Yeah.
[00:04:58] Patrick Chouinard: And I fed it also under.
[00:05:00] Patrick Chouinard: Patrick Carp had he auto-research, and I told him, like, explore both and come up with a way that I can use auto-research to improve RecapFlow on a weekly basis [tool:Auto Researcher].
[00:05:11] Ty Wells: You know, the thing I used, I touched his auto-research initially, and for a project that I was working on, my SAI project, my LucidLoop project, and I couldn't break through the barrier from my perspective.
[00:05:28] Ty Wells: But I know it's good for other things.
[00:05:30] Ty Wells: I just haven't had a chance to circle back to it to do other things.
[00:05:35] Ty Wells: But I think there's something there.
[00:05:36] Ty Wells: I just haven't had an opportunity because, you know, a week's gone by, which is like, you know, that's like six months.
[00:05:45] Patrick Chouinard: ▶ Actually, it proposed two loops, an inner loop that validate mechanically that the output matches every single rule, like every link has been extracted.
[00:05:59] Patrick Chouinard: right back to
[00:06:00] Patrick Chouinard: The link count is perfect.
[00:06:01] Patrick Chouinard: There is no leakage of markdown in the message being posted.
[00:06:07] Patrick Chouinard: I'm doing compression because the original message is always way too long.
[00:06:11] Patrick Chouinard: So it calculates if the compression is all right.
[00:06:15] Patrick Chouinard: So this is purely mechanical.
[00:06:17] Patrick Chouinard: It can run very quickly within the pipeline itself.
[00:06:21] Ty Wells: Then what I'm going start...
[00:06:22] Ty Wells: Go ahead.
[00:06:23] Ty Wells: Go ahead.
[00:06:24] Patrick Chouinard: ▶ What I want to do this week is I want to start taking the comments we get on the recap itself and feed it back into the loop.
[00:06:34] Patrick Chouinard: So I'm probably going to encourage people if they want to comment because this will become training data forcing the loop to improve itself on the weekly basis once it's been mechanically improved.
[00:06:46] Ty Wells: So yeah, I had what I had tried.
[00:06:48] Ty Wells: That's that's a great idea.
[00:06:49] Ty Wells: Actually, what I had tried to do is to reduce that five minute.
[00:06:53] Ty Wells: So instead of wasting the five minutes trying to see if there was something successful, I was trying to minimize...
[00:07:00] Ty Wells: And then if I could minimize that amount of time that's actually needed, then, you know, sort of tweak the five minute and then I can know because I'm checking, you know, for hallucinated code and stuff that code that doesn't work and all kinds of other stuff that I'm doing.
[00:07:17] Ty Wells: So my application of it was probably I need to circle back to that.
[00:07:21] Ty Wells: I'm going to make a actually put a reminder to remind me to circle back to that I've added to my list of reminders for tomorrow.
[00:07:31] Patrick Chouinard: ▶ So that's why I've asked co-work like to think philosophically about auto-research, like not implement the code as is, but really think of the philosophy of the Auto Researcher when it does, how we can adapt it to other scenario to have nothing to do with ML.
[00:07:49] Ty Wells: Yeah, basically.
[00:07:50] Ty Wells: And that's what I was, I was, I started down that path, but I know I can use it.
[00:07:55] Ty Wells: I like that approach.
[00:07:56] Ty Wells: That's what I'm going to have to do.
[00:07:58] Ty Wells: Hopefully I get some, some time to.
<!--SEGMENT
topic: Anthropic Architects exam + Google Generative AI Leader exam + M365 Copilot + ServiceNow
speakers: Ty Wells, Marc Juretus, Patrick Chouinard, Hemal Shah
keywords: Anthropic Architects certification, Google Generative AI Leader exam (NotebookLM study), Microsoft M365 Copilot Cowork release, ServiceNow connectors for ticket-status RAG, Azure AI Foundry, CIO using $100 Claude plan to rewrite legacy code, Cursor private marketplace for enterprise plugins, shoes-off Cursor HQ culture
summary: Ty mentions the new Anthropic Architects certification (40 pages on agentic coding agents, invite-only, 10 employees per company must pass). Marc just took the Google Generative AI Leader exam — 70-75% product pushing, scenario-based with 'two right of five' scoring; NotebookLM was his prep tool. Marc's enterprise (hospital running Azure) is rolling out Copilot agents on ServiceNow connectors for ticket-status queries. Patrick notes Microsoft M365 Copilot is releasing its own Cowork-like product with Claude as the model. Hemal just got back from Cursor HQ — they're rolling out a private enterprise plugin marketplace, plus the famous shoes-off culture story.
-->

[00:08:00] Ty Wells: And some of the projects that I'm working on, any of you guys working on the, you're going to take that architect, the anthropic architect exam, did you see that? [tool:Anthropic Architects exam]
[00:08:14] Patrick Chouinard: Yeah, would love to, but time is of the essence right now.
[00:08:18] Marc Juretus: Well, I built you a tool to help you get through it real quick, real easy.
[00:08:24] Ty Wells: Of course I did.
[00:08:24] Marc Juretus: I just took the, why did I just take the Google Generative AI Leader exam? [tool:Google Generative AI Leader exam]
[00:08:30] Marc Juretus: I ain't taking the exam in about 10 years, man.
[00:08:33] Marc Juretus: It was weird sitting in there because the computers were kind of tight.
[00:08:36] Marc Juretus: And there were a bunch of nurses and stuff taking stuff too, but it was interesting.
[00:08:41] Marc Juretus: It's been a while.
[00:08:42] Ty Wells: Proctored?
[00:08:43] Marc Juretus: I mean, the curriculum basically was 70% of them presenting their products, so you become certified, you use their Google Cloud, Vertex, and all that.
[00:08:53] Marc Juretus: But the scenarios were interesting.
[00:08:56] Marc Juretus: When they would present you, here's the situation, what would the company use?
[00:08:59] Marc Juretus: awards....
[00:08:59] Marc Juretus: it
[00:09:00] Marc Juretus: That I kind of, in a way, enjoyed, but I'll tell you what, as far as, like, taking an exam, it's been a while.
[00:09:06] Marc Juretus: That damn notebook LLM, you find yourself about three or four good sources on, you know, taking the exam and just take quizzes out the butt, man [tool:NotebookLM].
[00:09:15] Marc Juretus: It helped a lot.
[00:09:16] Ty Wells: Oh, yeah.
[00:09:17] Ty Wells: Oh, yeah.
[00:09:19] Ty Wells: For sure.
[00:09:21] Marc Juretus: But, yeah, that actually would pretty cool to take.
[00:09:24] Marc Juretus: We use Azure, and they're trying to do AI now, which is Azure AI Foundry.
[00:09:27] Marc Juretus: They're basically leveraging Copilot, though.
[00:09:30] Marc Juretus: So you can deploy Copilot agents [tool:Microsoft Copilot].
[00:09:32] Marc Juretus: So they're looking into doing that to, I don't know if you guys have ever used ServiceNow.
[00:09:37] Marc Juretus: So ServiceNow has the connectors where you can pull in incidents and tickets [tool:ServiceNow connectors].
[00:09:41] Marc Juretus: So they want customers to able to go, hey, what is the status of my ticket?
[00:09:46] Marc Juretus: It goes back to the RAG, which connects to ServiceNow and pulls back their ticket status.
[00:09:52] Marc Juretus: So that's our infancy of starting in the AI at the hospital now.
[00:09:56] Patrick Chouinard: So have you seen that Copilot is coming up?
[00:09:59] Patrick Chouinard: Okay.
[00:10:00] Patrick Chouinard: with its own version of Cowork.
[00:10:02] Marc Juretus: Now, Copilot, now which one are you talking about, from GitHub or from Microsoft?
[00:10:06] Patrick Chouinard: ▶ Microsoft Copilot, the M365 Copilot will have its own version of Cowork with the Claude model backing it.
[00:10:17] Marc Juretus: Interesting.
[00:10:18] Patrick Chouinard: It's supposed to release by the end of the month, which is basically in a week.
[00:10:23] Marc Juretus: We got an interesting demographic.
[00:10:25] Marc Juretus: Our CIO pulled down Claude and bought the $100 model, and he did a version of the ServiceNow application at home.
[00:10:34] Marc Juretus: And I'm like, dude, like, how much time do have on your hands?
[00:10:38] Marc Juretus: ▶ But anyways, so he's all full bore and wants to try to leverage Claude for analyzing old code bases and rewriting them in something new.
[00:10:50] Marc Juretus: So that's his latest thing, what he wants to use Claude for.
[00:10:54] Marc Juretus: But I will say this, because I know Azure AI Foundry a little bit from Azure.
[00:10:58] Marc Juretus: Projektor.
[00:10:59] Marc Juretus: Mm-hmm.
[00:11:00] Marc Juretus: I will say this.
[00:11:01] Marc Juretus: I was like, man, why are you guys using Microsoft Copilot for like agents?
[00:11:06] Marc Juretus: And then I did a bunch of research on it.
[00:11:08] Marc Juretus: ▶ And at the end of the day, 80% of society or whatever you would word that, because of all the connectors to SharePoint, ServiceNow, this, that, and the other, is real easy for the task that they're trying to accomplish.
[00:11:20] Marc Juretus: You know, if you needed something more advanced, then you would create an agent and deploy it up in Azure AI Foundry.
[00:11:27] Ty Wells: I ran into some ServiceNow employees by accident, just some randos at my daughter's apartment in Tampa.
[00:11:33] Ty Wells: And I'm like, I just heard them.
[00:11:34] Ty Wells: They're on their computer.
[00:11:35] Ty Wells: I didn't even know they work for ServiceNow.
[00:11:36] Ty Wells: I'm like, hey, can you test this for me?
[00:11:38] Patrick Chouinard: Because, I mean, they just seemed like they would be a good test.
[00:11:41] Patrick Chouinard: And sure enough, they were.
[00:11:44] Ty Wells: They randomly just tested my app that I was building at the time.
[00:11:48] Ty Wells: I didn't even know what I was building at the time, but they tested it, gave me feedback as well.
[00:11:53] Marc Juretus: Yeah, we were, they were, I was on a demo of their, of their AI that they have in that.
[00:11:58] Marc Juretus: They were demoing that stuff, but.
[00:12:00] Marc Juretus: It's funny, the couple of companies I see that use it, you remember how everyone's IDE always looked like Eclipse?
[00:12:05] Marc Juretus: I think it was called?
[00:12:06] Marc Juretus: No, what is the other one that would job?
[00:12:08] Marc Juretus: This meeting is being recorded.
[00:12:10] Marc Juretus: It's IntelliJ, the other one.
[00:12:11] Marc Juretus: Is it Eclipse?
[00:12:13] Marc Juretus: And then everyone would have a version of it, but just skinned with their own version?
[00:12:18] Marc Juretus: That's what their interface looked like for ServiceNow to develop was just like Copilot, but all labeled out with ServiceNow.
[00:12:31] Patrick Chouinard: Hello, everyone!
[00:12:37] Patrick Chouinard: Long time no see?
[00:12:38] Marc Juretus: Yeah!
[00:12:39] Hemal Shah: Yeah, I was traveling.
[00:12:41] Hemal Shah: I visited Cursor's headquarter in California last week [tool:Cursor private marketplace].
[00:12:47] Hemal Shah: It's, you know, they keep their shoes outside.
[00:12:52] Hemal Shah: It was interesting culture to see.
[00:12:55] Marc Juretus: Really?
[00:12:56] Hemal Shah: Really?
[00:12:56] Hemal Shah: Yeah.
[00:12:57] Marc Juretus: would be interesting around here to try that.
[00:13:00] Hemal Shah: See, when people do that, I swear you're trying too hard to be interesting.
[00:13:07] Marc Juretus: Unless you've got some real expensive rugs or something going on.
[00:13:11] Marc Juretus: Yeah, like, whatever.
[00:13:14] Ty Wells: People just don't believe in bringing dirt inside that stuff.
[00:13:17] Ty Wells: You know, it's stuff you step on on your shoes, like you're tracking that all through your house.
[00:13:22] Ty Wells: And they walk their feet inside.
[00:13:24] Marc Juretus: So I bet you there's a mantra where you have your shoes off, you're more grounded as an employee.
[00:13:29] Marc Juretus: But it's probably something stupid like that, in my opinion.
[00:13:32] Marc Juretus: But that's just me.
[00:13:34] Ty Wells: You get closer to the ground.
[00:13:35] Marc Juretus: That's for sure.
[00:13:36] Marc Juretus: Yeah, you do.
[00:13:38] Hemal Shah: It's multiple theories.
[00:13:40] Hemal Shah: I mean, they started off in the apartment, which was Chef's house.
[00:13:44] Hemal Shah: So they did not want shoes inside.
[00:13:46] Hemal Shah: And then that's how the culture started.
[00:13:49] Hemal Shah: There are multiple theories.
[00:13:50] Hemal Shah: But we, I visited with, so me, my CTO, we all were there.
[00:13:55] Hemal Shah: And they offered us that you don't have to take off shoes, know, because we were just visiting.
[00:13:58] Hemal Shah: But But I was
[00:14:00] Hemal Shah: The CTO removed it, so then we all were forced to remove our shoes, and it was fine most of the time, but when it was time to visit the washroom, that's where it felt a little weird.
[00:14:13] Ty Wells: Yeah, that's like going on the plane, walking to the lavatory, and I do this in my socks, but then those socks get burnt in a bin like later on, because I don't feel like putting my shoes back on.
[00:14:26] Hemal Shah: Yeah, that's got to be tricky.
[00:14:28] Marc Juretus: How would you use the bathroom at Cursor?
[00:14:31] Marc Juretus: Oh, that's disgusting, man.
[00:14:33] Hemal Shah: You go to a urinal.
[00:14:35] Marc Juretus: Dudes used to do that at the gym.
[00:14:37] Marc Juretus: Like, I used to go to this franchise called LA Fitness.
[00:14:40] Marc Juretus: They'd walk up to the urinal with no shoes on, because they just got, you know, took stuff.
[00:14:44] Marc Juretus: I'm like, wow, this is repugnant, what you're doing right now.
[00:14:48] Marc Juretus: Like, oh, God.
[00:14:56] Marc Juretus: What made you go to Cursor?
[00:14:58] Hemal Shah: Cursor.
[00:14:59] Hemal Shah: There.
[00:14:59] Hemal Shah: I'm
[00:15:00] Hemal Shah: My company, they are heavily using Cursor, so we are one of their bigger clients, so I met with the leadership, some of the requirements we had.
[00:15:11] Hemal Shah: ▶ Cursor is coming up with a private marketplace for an enterprise organization to host their own internal plugins and everything.
[00:15:19] Hemal Shah: was going through last week's video, Patrick, you had some of your plugins and marketplace discussion you're talking about in Cloud.
[00:15:25] Hemal Shah: But yeah, talk to different features that Cursor is rolling out and things like that.
[00:15:34] Patrick Chouinard: ▶ Yeah, hopefully someone will unify all of those marketplaces so we don't have to publish to 16 different places for the same thing.
[00:15:42] Hemal Shah: Yeah.
[00:15:44] Ty Wells: That's no fun if it's all unified.
[00:15:46] Hemal Shah: Nobody wants that.
[00:15:49] Patrick Chouinard: Yeah, right.
[00:15:51] Marc Juretus: Yeah, know who I wonder would happen to?
[00:15:53] Marc Juretus: He's kind of like Ty, has his own company.
[00:15:55] Marc Juretus: Remember the older gentleman that came on for a while, Patrick and Ty?
[00:15:59] Marc Juretus: I've You're trying I don't
[00:16:00] Marc Juretus: He had, like, his own company, and now he was trying to branch out and push it out.
[00:16:03] Patrick Chouinard: I forgot what his name was.
[00:16:04] Patrick Chouinard: Was Tom or something like that?
[00:16:06] Ty Wells: Well, Tom is one of them, but I'm not sure.
[00:16:09] Ty Wells: I don't think he's talking about Tom.
[00:16:11] Ty Wells: I sort of remember.
[00:16:12] Ty Wells: Oh, yeah.
[00:16:13] Marc Juretus: It's not Tom, yeah.
[00:16:14] Ty Wells: Yeah.
[00:16:15] Ty Wells: We're like habits of creatures.
[00:16:16] Ty Wells: Like, some of the projects we talk about, I'm like, am I having deja vu?
[00:16:20] Ty Wells: I know we discussed this at some point.
[00:16:23] Ty Wells: Somebody showed me this project before somewhere.
[00:16:25] Ty Wells: What did I say?
[00:16:25] Ty Wells: And it's right here.
[00:16:26] Ty Wells: This is where I saw it.
[00:16:28] Ty Wells: I don't remember.
[00:16:29] Ty Wells: I sort of remember, but I do not remember the name.
[00:16:31] Ty Wells: I remember what you're talking about, but I don't remember the name.
[00:16:34] Marc Juretus: He was the one that was breaking down if you were going to charge people how to break down how to charge a company if you were doing work.
[00:16:41] Marc Juretus: I remember him getting into how he used to do it.
[00:16:43] Marc Juretus: That's the only thing that stands out.
[00:16:45] Marc Juretus: But I know, remember, he went to the Google conference in New York and gave us information.
[00:16:50] Marc Juretus: It was probably about three, four months ago.
[00:16:52] Marc Juretus: I was just wondering what happened to him because I know he was being aggressive with trying to go out and get business.
[00:16:59] Patrick Chouinard: Hey, Mr.
[00:17:00] Brandon Hancock: Yo, guys, I'm trying to get this working, and I have too many Fathom accounts, so I'm fixing as quickly as I can.
[00:17:11] Brandon Hancock: There we go.
[00:17:12] Brandon Hancock: Now we're cruising.
[00:17:15] Brandon Hancock: What were you saying, Marc?
[00:17:17] Brandon Hancock: Just to make sure I didn't miss.
[00:17:18] Marc Juretus: I was trying to, I was just saying we were reminiscing.
[00:17:21] Marc Juretus: I was trying to remember that the, remember the older gentleman that had his own company and he was kind of breaking down how, you know, would charge a client.
[00:17:28] Marc Juretus: Like, have you heard from him?
[00:17:30] Marc Juretus: Because I haven't seen him in months.
[00:17:32] Marc Juretus: You know what I'm talking about?
[00:17:34] Brandon Hancock: I know exactly who you're talking about.
[00:17:38] Brandon Hancock: He had a very, his name was short, white guy.
[00:17:42] Brandon Hancock: He joined a big company that was doing enterprise level stuff.
[00:17:46] Hemal Shah: Kong API?
[00:17:47] Hemal Shah: The one who joined Kong API?
[00:17:49] Hemal Shah: Maybe?
[00:17:50] Marc Juretus: No, no.
[00:17:50] Ty Wells: No, I know who you're talking about.
[00:17:52] Ty Wells: I hooked up with him on LinkedIn.
[00:17:54] Marc Juretus: Oh God, I'll find him.
[00:17:55] Marc Juretus: I don't think that's what I'm talking about, though.
[00:17:57] Marc Juretus: The guy owned his own, he had
[00:18:00] Marc Juretus: owned his own business where he was doing service for years with companies like coding and, you know, IT support.
[00:18:07] Ty Wells: Oh, no, it's a different guy.
[00:18:08] Marc Juretus: Yeah, then it's not that guy.
[00:18:10] Marc Juretus: You saw his face, don't know exactly.
[00:18:13] Marc Juretus: What is it?
[00:18:14] Prem: Al Cole?
[00:18:15] Marc Juretus: Al.
[00:18:16] Marc Juretus: It was Al.
[00:18:17] Brandon Hancock: Short name.
[00:18:17] Brandon Hancock: It was 100% Al.
[00:18:18] Prem: Yeah.
[00:18:20] Prem: He joined, he became a global VP in Kong Inc.
[00:18:25] Prem: I think he might be the one.
[00:18:26] Ty Wells: Let me.
[00:18:27] Ty Wells: Yeah, Al.
[00:18:28] Prem: That's his name.
[00:18:28] Prem: Let me share my screen.
[00:18:30] Prem: don't know.
[00:18:30] Prem: Like, I have his LinkedIn profile.
[00:18:32] Marc Juretus: You might.
[00:18:32] Marc Juretus: Okay.
[00:18:32] Marc Juretus: I cannot share.
[00:18:33] Marc Juretus: So.
[00:18:34] Marc Juretus: Wow.
[00:18:34] Marc Juretus: He did not seem like he was at a point in life where he was going to join a company like that.
[00:18:39] Marc Juretus: seemed like he was going to do his own thing.
[00:18:40] Marc Juretus: Okay.
[00:18:42] Brandon Hancock: Never mind.
[00:18:43] Ty Wells: Like Mike Tyson says, you'd want to do that until you get punched in the face.
[00:18:48] Marc Juretus: Everybody.
[00:18:49] Marc Juretus: Yeah.
[00:18:49] Marc Juretus: Yeah.
[00:18:50] Marc Juretus: Everybody's tough that they get punched in the face.
<!--SEGMENT
topic: Brandon — eliminate-myself-from-systems philosophy + auto-eval feedback loops
speakers: Brandon Hancock, Jake Maymar, Elijah Stambaugh, Juan Torres
keywords: SOAP narratives for ambulance reimbursement, work-tree development environment, hyper-clear scoring functions, evaluation suite of 60+ inputs, grading rubric pass/fail + point-based, Codex 45-minute long-running iteration, agentic data science, skill-as-multi-step-process vs system-as-iterating-pipeline, GPT-5.4 non-thinking favorite for consumer apps
summary: Brandon's North Star: eliminate himself from the systems he creates. At his EMS startup, the deliverable is SOAP narratives for ambulance reimbursement — they've built a multi-step pipeline (narrative → follow-up Qs → revised narrative → grader). Each stage gets its own self-evaluation feedback loop with hyper-clear pass/fail criteria. Codex runs the iteration for 45 minutes building its own experimentation lab. Brandon distinguishes a skill (multi-step process to achieve one objective) from this pattern — agentic data science. GPT-5.4 non-thinking is his current favorite consumer-app model.
-->

[00:18:53] Brandon Hancock: Well, perfect.
[00:18:53] Brandon Hancock: Well, hey, guys.
[00:18:54] Brandon Hancock: Hope you all are having a great Tuesday so far.
[00:18:57] Brandon Hancock: Long time no see.
[00:18:59] Brandon Hancock: And.
[00:19:00] Brandon Hancock: Hello, What I'd love to do today is, well, first off, always shout out to Patrick and Paul for holding down the fort.
[00:19:07] Brandon Hancock: Literally would not be possible without them.
[00:19:09] Brandon Hancock: So always huge round of applause to Patrick and Paul, the true goats.
[00:19:15] Brandon Hancock: But what I'd love to do is dive in a little bit, just real quick on kind of what I have been like capturing my attention recently, explain why, and then would love to hear everything that you guys are, have been up to.
[00:19:29] Brandon Hancock: So before, what I'd love to like, Patrick, I just said like a request.
[00:19:36] Brandon Hancock: The, there we go.
[00:19:38] Brandon Hancock: Cool.
[00:19:39] Brandon Hancock: Desktop.
[00:19:42] Brandon Hancock: Cool.
[00:19:43] Brandon Hancock: Let me move these things around.
[00:19:44] Brandon Hancock: ▶ So the main thing that I have been focusing on recently is how to eliminate myself from the systems I create.
[00:19:53] Brandon Hancock: That is my North Star right now.
[00:19:56] Brandon Hancock: So, so for example, what that means inside of.
[00:20:00] Brandon Hancock: So startup, we have to create SOAP narratives.
[00:20:05] Brandon Hancock: Like, that is the end result that we are trying to create.
[00:20:08] Brandon Hancock: And we're basically building out evaluations to say, like, did this SOAP narrative pass or fail?
[00:20:15] Brandon Hancock: And we have hard criteria that basically determine if it was like, you know, pass or fail.
[00:20:21] Brandon Hancock: ▶ And what you can do is using a tool like Codex, you can basically have Codex go in a loop infinite number of times running experiments [tool:Codex].
[00:20:32] Brandon Hancock: I don't know if you guys are familiar with Andrej Karpathy's or Andrej Karpathy's auto-research.
[00:20:37] Brandon Hancock: It's very similar to that.
[00:20:40] Brandon Hancock: It's funny, I literally, I had my thing, and then I saw his thing, and I've merged them together.
[00:20:44] Brandon Hancock: ▶ And I have fallen in love with this idea of building out systems to where the bottleneck is, you have to be hyper, hyper, hyper clear on what your, like, scoring function
[00:21:00] Brandon Hancock: is and meaning like what is good and what is bad and what the ultimate objective is.
[00:21:07] Brandon Hancock: If you can get hyper clear on defining what's good and what's bad and what you're ultimately shooting for, you could just let the AI run multiple, multiple, multiple iterations and experiment and continually self improve.
[00:21:21] Brandon Hancock: So I'm doing this and it is the coolest thing ever.
[00:21:25] Brandon Hancock: So in our case, we have like a multi-step system to where like we first make soap, narratives.
[00:21:31] Brandon Hancock: Then we, uh, after we make a soap narrative, we ask follow up questions.
[00:21:36] Brandon Hancock: After we ask follow up questions, we make new narratives.
[00:21:40] Brandon Hancock: Then we also grade.
[00:21:42] Brandon Hancock: So we're doing a bunch of stuff.
[00:21:44] Brandon Hancock: So we have to take this approach of, you know, uh, basically like building self evaluation, evaluating feedback loops.
[00:21:54] Brandon Hancock: We have to do that for each one individually to set up a good baseline.
[00:21:58] Brandon Hancock: And after
[00:22:00] Brandon Hancock: We set up an individual, like make sure each phase is working great, then you do an entire system-based evaluation, but it forces you to get hyper-clear on what's good and bad and what you're ultimately trying to do.
[00:22:15] Brandon Hancock: ▶ So you have to make a grading rubrics and then just let AI rip.
[00:22:17] Brandon Hancock: It's a little expensive, not going to lie, but this has caught my attention.
[00:22:22] Brandon Hancock: ▶ And we're taking this approach, final thing, we're taking this approach also to actually building out software.
[00:22:28] Brandon Hancock: So a cool other thing, because I'm trying to apply this principle everywhere in my life, so even for our actual software development lifecycle, so we're doing this exact same approach to where, you know, we start off with creating a work tree.
[00:22:44] Brandon Hancock: Our work tree is going to build a brand new development environment, so we have production, staging, and development.
[00:22:50] Brandon Hancock: And in development, it has its own database, so we could experiment as much as we possibly want, and it doesn't affect anything else.
[00:22:59] Brandon Hancock: So then...
[00:22:59] Brandon Hancock: then...
[00:23:00] Brandon Hancock: What we get to do is, you know, we end up working on like a new feature, but then we also are building out, we're actively trying to build out in a test suite.
[00:23:09] Brandon Hancock: ▶ So at any point, we're just trying to eliminate the human because like right now I as human have to say what I want in the work tree, I have to make a new task template, then the AI goes off, does the work, but then when it comes to evaluation at the end, I'm still back in the loop.
[00:23:25] Brandon Hancock: And I'm like, wait, how do I once again build myself out of the loop for the evaluations?
[00:23:30] Brandon Hancock: So it's like forcing me to describe like, well, I would say that this past, if this set of new evaluations of new features, old features, and new things work.
[00:23:39] Brandon Hancock: So I'm just continually trying to work myself out of the loop.
[00:23:43] Brandon Hancock: And it's forcing me to think differently about everything that I do.
[00:23:47] Brandon Hancock: So I'm loving the idea.
[00:23:49] Brandon Hancock: It's been a little bit expensive to build out some of these suites, but I mean, it is auto improving.
[00:23:55] Brandon Hancock: Like that's the coolest part.
[00:23:56] Brandon Hancock: Like I'm actually seeing it improve our narratives from a week ago.
[00:24:00] Brandon Hancock: If until today, I'm seeing all sorts of improvement.
[00:24:03] Brandon Hancock: So that's what my brain's been focused on.
[00:24:05] Brandon Hancock: I'll have more clarity as soon as I, like, finish building out some suites of, like, getting things to work.
[00:24:10] Brandon Hancock: But that's where I'm at.
[00:24:12] Brandon Hancock: Jake?
[00:24:13] Jake Maymar: That's fantastic.
[00:24:16] Jake Maymar: So you build a series of tests, and then you're essentially doing, like, a simulation, right?
[00:24:25] Jake Maymar: And so you're simulating all the possible—I'm just trying to get my head around it.
[00:24:33] Jake Maymar: So basically, you know that you're—so I guess are you using, like, OKRs?
[00:24:39] Jake Maymar: I'm trying to figure out the overarching thing.
[00:24:42] Jake Maymar: So you basically have, like, your Goldens, and then you know you're going to add a feature in, but it applies to an OKR.
[00:24:53] Brandon Hancock: So real fast, Jake, we are still working hard on the test suite.
[00:24:56] Brandon Hancock: Like, this is still, like—that is the hardest problem.
[00:24:59] Brandon Hancock: So we—
[00:25:00] Brandon Hancock: We know what we want to do.
[00:25:01] Brandon Hancock: We have designed playbooks, but we have no code yet.
[00:25:05] Brandon Hancock: Like this was as of the past three days, we decided to start investigating this.
[00:25:10] Brandon Hancock: So I just like, we're going there because we are thinking, how do I lean as hard as possible on the AI?
[00:25:18] Brandon Hancock: Like if I was to lean 100% on the AI, what would have to be true?
[00:25:21] Brandon Hancock: I would have to make a way to where AI could work in its own sandbox on my computer and just rip and not mess up any database.
[00:25:27] Brandon Hancock: It would also have to be able to create its own, I would have to be able to evaluate the results against something.
[00:25:33] Brandon Hancock: Because right now I'm the bottleneck of knowing every like, oh, this button should do this.
[00:25:38] Brandon Hancock: Oh, this, when you should do this.
[00:25:40] Brandon Hancock: Like that exists zero places except my brain.
[00:25:44] Brandon Hancock: So anytime there's something in my brain that I manually review, I have to put that into the system in one shape, form or fashion.
[00:25:49] Brandon Hancock: And it really comes down to making playbooks of like, here's the manage user playbook.
[00:25:54] Brandon Hancock: It's like user stories.
[00:25:55] Brandon Hancock: It literally just comes down to user stories.
[00:25:57] Brandon Hancock: Over and over and over and again.
[00:25:58] Brandon Hancock: So we're actively working.
[00:26:00] Brandon Hancock: I'll let you guys know, because we want to, we know what we want to do, but we also don't want to break the bank running a bunch of like, you know, agents to do a lot of this stuff.
[00:26:08] Brandon Hancock: So I'll keep you guys posted.
[00:26:09] Brandon Hancock: But that's where, that's where my head's going.
[00:26:12] Brandon Hancock: Just so eventually what's going to happen is like, it literally just becomes talk.
[00:26:16] Brandon Hancock: Like talk and then make a PR.
[00:26:19] Brandon Hancock: Like that's it.
[00:26:19] Brandon Hancock: It's talk.
[00:26:20] Brandon Hancock: And then I look at the final PR.
[00:26:21] Brandon Hancock: Everything else in between is just done.
[00:26:23] Brandon Hancock: Because there's, we're just trying to get humans out of the loop.
[00:26:26] Brandon Hancock: Obviously we're in a review, but just that's where we're headed.
[00:26:30] Brandon Hancock: So I'm excited.
[00:26:31] Brandon Hancock: It's a very, it's a fun, hard problem.
[00:26:33] Brandon Hancock: Um, it's going to keep us lean too.
[00:26:35] Brandon Hancock: That's the thing.
[00:26:35] Brandon Hancock: It's going to keep us very lean.
[00:26:37] Brandon Hancock: Uh, Elijah, I saw you had a question too, buddy.
[00:26:42] Elijah Stambaugh: I don't know if you had the opportunity to see, um, if you saw the skill evaluator from Anthropic, but that may have some interesting criteria for you as you consider how you're evaluating your,
[00:27:01] Elijah Stambaugh: The other thing is, I know Gemini or Google released a skill as well that allows you to use their database tools, and I think it's similar to the RAG stuff that we've built, that you've built now, that I've built on top of what you built, right?
[00:27:23] Elijah Stambaugh: So, you know, I saw something similar just yesterday, I'll send you the link, but what the guy did was he used the multimodal to record his process, and then from that, he worked his way backward to building out the skill that would redo that particular thing every single time the same way.
[00:27:44] Elijah Stambaugh: And he used the Google CLI skill that they just came out with.
[00:27:51] Elijah Stambaugh: I know they came out with the Google Google Workspace CLI last Monday, but this was a new one over the past couple of days.
[00:27:56] Elijah Stambaugh: So, just something, I'm not sure, like, again, how you're wrapping your...
[00:28:00] Elijah Stambaugh: How head around if it's more database centric, or if it's the files themselves, how you're building skills to do the work?
[00:28:09] Brandon Hancock: So real fast, a skill, the way I usually look at a skill is it's a multi-step process, maybe involving some code to achieve an objective, which is great for automating individual tasks.
[00:28:22] Brandon Hancock: But what we're talking, the thing I'm talking about is taking that on steroids, where it is, I mean, it's data science.
[00:28:34] Brandon Hancock: Like that's what I'm talking about, but it's like agentic data science.
[00:28:38] Brandon Hancock: So it's like a skill does a thing, but what we're talking about is, hey, we have a system.
[00:28:43] Brandon Hancock: This system has multiple steps in it.
[00:28:46] Brandon Hancock: Each step produces an output, and we are trying to maximize the quality of the output of each step.
[00:28:55] Brandon Hancock: ▶ And to do that, I have to define through a grading criteria.
[00:29:00] Brandon Hancock: What I'm looking for, a combination of like, these are mandatory things that are pass-fail, and then everything else is a point-based system of like, the styling, here's what good styling looks like, here's what bad styling looks like.
[00:29:14] Brandon Hancock: So you're forced to describe and articulate your optimization, like what you're shooting for and your grading, and then what happens is once you build out an evaluation suite of like, here's 60 different inputs to throw into this system, like, have to have that input, you then get to grade each output against your rubric and be like, oh, I'm failing, and then let the AI self-experiment.
[00:29:38] Brandon Hancock: ▶ But you're forced to build out an evaluation input suite, a grading function, so that you can then grade the outputs, so then the AI goes, oh, based on your grading rubric, objective one, I'm just dying on.
[00:29:51] Brandon Hancock: Like I'm completely, that's messing up over and over again.
[00:29:54] Brandon Hancock: I'm going to adjust the system prompt so when I run iteration two, I'll now do it again.
[00:29:59] Brandon Hancock: And I'm going to try
[00:30:00] Brandon Hancock: I'm a new hypothesis to see if that updating the system prompt will work.
[00:30:03] Brandon Hancock: So it's just a loop.
[00:30:05] Brandon Hancock: You're allowing AI to do the work and allowing AI to review itself.
[00:30:08] Brandon Hancock: It's like the grading critiquer functionality, but on steroids.
[00:30:11] Brandon Hancock: So I don't know.
[00:30:12] Brandon Hancock: That was probably very deep, but I just wanted to like, that is the exact problem that we're working on right now.
[00:30:16] Brandon Hancock: It's the funnest problem I've worked on in a very long time, but it's weird to get your brain around it.
[00:30:23] Brandon Hancock: And I'm letting Codex do all the work, by the way.
[00:30:25] Brandon Hancock: I let Codex run for like 45 minutes just iterating on itself over and over again.
[00:30:30] Brandon Hancock: ▶ I'm loving Codex for these long running jobs.
[00:30:32] Brandon Hancock: Because it built its own, it built its own lab, like experimentation suite inside my app.
[00:30:38] Brandon Hancock: And now I just let it rip.
[00:30:40] Brandon Hancock: It's the coolest experience.
[00:30:42] Brandon Hancock: I love Codex for that.
[00:30:43] Brandon Hancock: I tried it with Claude Code.
[00:30:44] Brandon Hancock: Claude Code was just a little, tried to make me in the loop a little too much.
[00:30:48] Brandon Hancock: But Codex just did as like, it was happy to work for a very long time without me.
[00:30:52] Brandon Hancock: And I like that.
[00:30:54] Brandon Hancock: Juan.
[00:31:00] Juan Torres: Novelas?
[00:31:00] Juan Torres: what were you saying?
[00:31:02] Juan Torres: was like stories?
[00:31:04] Brandon Hancock: Soap narratives.
[00:31:05] Brandon Hancock: It's what our customers have to write.
[00:31:07] Brandon Hancock: They have to do a narrative like when an ambulance rolls up because you broke your leg and they have to transport you to the hospital.
[00:31:19] Brandon Hancock: have to document, here was a situation, here's what we assessed, here was our objective, here's our plan going forward, here's why we didn't transport them, here's why we did transport them, here was the vitals.
[00:31:27] Brandon Hancock: Like they have to paint the picture of what actually happened to determine if they get reimbursed.
[00:31:33] Brandon Hancock: So we have a suite of inputs that we have, like we know these are potential narratives that someone would pass into our system and we have a grading functions and now we're letting AI improve its own system prompt over and over and over again to make sure that we're, it's doing what we want to do.
[00:31:49] Brandon Hancock: We're not just flying blind of like, oh yeah, I think it's working.
[00:31:52] Brandon Hancock: It's like, no, at this point we're forcing it to, now that we know what we want it to do, to improve itself, to get the desired result.
[00:31:59] Brandon Hancock: GPT.
[00:31:59] Brandon Hancock: GPT.
[00:32:00] Brandon Hancock: ▶ 5.4, real fast guys, favorite model, non-thinking for consumer apps, GPT-5.4, non-thinking for consumer apps, has beat everything else.
[00:32:08] Brandon Hancock: I've tested all of them, it's crushing it.
[00:32:12] Brandon Hancock: Gemini 3 Flash, or 3 Flash, whatever number they're on, no, 5.4, no thinking.
[00:32:17] Brandon Hancock: It's the fastest, it's fantastic.
[00:32:20] Brandon Hancock: But, Dan, over to you, buddy.
[00:32:23] Brandon Hancock: And then we'll start going, Patrick was super nice and put together some community questions.
[00:32:27] Brandon Hancock: Don, you're actually the first community question anyway, so.
<!--SEGMENT
topic: Don's question — Codex consistency + Stripe key hell + MCP/CLI strategies
speakers: Don Davis, Brandon Hancock, Marc Juretus
keywords: Codex first-run Vercel deploy success, Stripe key proliferation, monthly + annual + tier products, multiple subscription IDs, Stripe MCP, Stripe CLI, leave-everything-on-Stripe + only store customer ID, ShipKit pattern, Lemon Squeezy as donation alternative
summary: Don asks why Codex deploys to Vercel cleanly first-run while Claude Code stumbles, then pivots to Stripe key hell — every monthly, annual, product tier needs its own key plus the master one. Brandon's recommendation: leave everything in Stripe, only store the customer ID locally to avoid stale data — that's the ShipKit pattern. Use the Stripe CLI (or the MCP) to provision via natural language. Marc asks about donations specifically; Brandon suggests Lemon Squeezy as an alternative.
-->

[00:32:30] Patrick Chouinard: If you wanna.
[00:32:31] Don Davis: Well, I'll start with, I'll start with my comment on Codex first, and then I'll, and then I'll, I'll circle back to my question.
[00:32:38] Don Davis: So, my view of Codex is that when I've used it on coding products, projects that I'm passing back into Vercel, it goes straight into Vercel, no issues, passes on the first run every single time.
[00:32:53] Don Davis: Well, where with, with, constantly with, with, with Claude Codex, I put something into Vercel, and
[00:33:00] Don Davis: there's, you know, I don't know, a bunch of issues, and I've got to deal with the issues whenever I first put it in, you know, to do that initial release.
[00:33:07] Don Davis: So I've had a great, just a great experience with Codex, although I still am not using it with ShipKit.
[00:33:15] Don Davis: So that's my, my other side is, you know, I've been doing a lot of stuff with like lead magnets and other stuff for clients, but no, you know, no real other, you know, big projects yet with Codex.
[00:33:28] Don Davis: So, um, we'll see how it goes whenever, whenever I try that first time, my question, my question was on, um, what people are doing with regards to Stripe.
<Q>[00:33:39] Don Davis: mean, I just find myself like, I mean, anytime I've got to get to that step of like implementing Stripe, it's just like, I feel like I wind up in key hell, um, where I've got to get like the initial two keys you got to have.</Q>
[00:33:52] Don Davis: And then, um, you know, you got to go get all the product keys and then you got to put all those in and then you got to do all the testing.
[00:33:57] Don Davis: I'm just curious, like, um.
[00:34:00] Don Davis: I know everybody has to do this, but, I mean, does everybody go through, one, I've found myself in applications just in case the pricing changes or something else later, like building in the test mode right into the application itself, so that I can flip back and forth.
[00:34:17] Don Davis: I also don't know if there are, you know, just any other best practices.
[00:34:21] Don Davis: I saw somebody get responded back with try the Stripe MCP, but yeah, just curious what people do.
[00:34:29] Brandon Hancock: So real fast, Don, just a quick question to make sure I understand.
[00:34:31] Brandon Hancock: So what, in your app, are we having like multiple subscriptions?
[00:34:35] Brandon Hancock: Is this multiple one-time products?
[00:34:36] Brandon Hancock: What do we, what do we, what's the end goal real fast?
[00:34:39] Don Davis: Yeah, so normally, let's just say it'd be like maybe one product and possibly like a bigger version of that product, right?
[00:34:47] Don Davis: So like, you know, hey, look, maybe if you're a small, you know, small company that wants to use the software, then maybe it's a smaller thing.
[00:34:56] Don Davis: But if you're an agency, maybe there's a bigger price.
[00:34:59] Don Davis: And then also also have.
[00:35:00] Don Davis: Having monthly and annual as well, right?
[00:35:03] Don Davis: So you've got two keys, one for monthly, one for annual, the product, you know, key, and then you also have the, each of the subscriptions have a key, and then also Stripe has a key.
[00:35:17] Don Davis: I just feel like it's, I don't know, it's just a lot to manage, but every, every startup that I've worked at, that is, it is always a bottleneck.
[00:35:25] Brandon Hancock: It does not matter.
[00:35:27] Brandon Hancock: Yeah, it has always been a bottleneck.
[00:35:30] Brandon Hancock: Uh, for every company we've always worked on.
[00:35:33] Brandon Hancock: Um, there's just, Stripe is always a pain for, for managing all of that.
[00:35:37] Brandon Hancock: Um, I will say the more you just leave on the Stripe side, the better, like that's what we did with ShipKit is like, we don't put a lot of information on our app [tool:ShipKit].
[00:35:49] Brandon Hancock: ▶ We keep it always in Stripe.
[00:35:51] Brandon Hancock: So the set, just because you don't want to have, you end up with stale data, basically, if you don't.
[00:35:57] Brandon Hancock: Um, so that's why we always just like, you have the Stripe customer ID,
[00:36:00] Brandon Hancock: And if you want to ever find anything, we just go over to StripeLand to figure it out.
[00:36:03] Brandon Hancock: So that's just a helpful tip.
[00:36:05] Brandon Hancock: That's how I've seen multiple startups do it at this point, but I just want to pass that along.
[00:36:08] Brandon Hancock: But yeah, it is a pain getting it set up.
[00:36:10] Brandon Hancock: It's a pain managing it.
[00:36:11] Brandon Hancock: And it's a pain when you want to go actually change stuff, too.
[00:36:16] Brandon Hancock: Patrick, though, fantastic advice.
[00:36:18] Brandon Hancock: And everyone else who also said, looking at the MCP, like at this point, I mean, we know we can articulate.
[00:36:25] Brandon Hancock: ▶ I want a product with this, and maybe it's six CLI commands that would have been a pain in the past to deal with.
[00:36:31] Brandon Hancock: But now it's just like, who cares if it's six or a hundred?
[00:36:34] Brandon Hancock: Like, all I want is the product key and you save it to my environment variables and then hook it up to my app.
[00:36:38] Brandon Hancock: Like, you know, so Patrick, great advice on that.
[00:36:42] Brandon Hancock: But no, anything manual, it is a pain.
[00:36:44] Brandon Hancock: And if there is a CLI, use the CLI.
[00:36:47] Brandon Hancock: Don't bother with the MPP.
[00:36:49] Brandon Hancock: Always.
[00:36:51] Don Davis: Yeah, I mean, so I have the Stripe.
[00:36:53] Don Davis: I have the Stripe CLI.
[00:36:56] Don Davis: And I think I think these are good takeaways that I'm pulling.
[00:36:59] Don Davis: idea.
[00:36:59] Don Davis: really easy.
[00:37:02] Don Davis: I think I don't think I've approached it in the same way, and so I think if I use the Stripe CLI the way that it's intended to be used, and then also if I sort of, you know, force everything back to the Stripe user ID, that'll help too, because I saw it, I saw you mentioned it in your, in one of your videos, you know, even in the school community, you know, way back when, Brandon, you mentioned the fact that, you know, look, you should be using the Stripe Stripe user ID as well, back then, so, yeah.
[00:37:34] Brandon Hancock: Have a good luck, Brandon.
[00:37:35] Brandon Hancock: Stripe, it's not the easiest.
[00:37:36] Brandon Hancock: I, I appreciate them, they're a mandatory evil to get, to get paid, but, uh, but yeah, so on the, the good news is on the other side of getting it working is dollar signs, so that's always, that's always exciting.
[00:37:47] Don Davis: Right.
[00:37:49] Brandon Hancock: Perfect.
[00:37:50] Brandon Hancock: Um, and then I, okay, I don't think there was any other questions.
[00:37:57] Brandon Hancock: Um, so yeah.
[00:37:58] Brandon Hancock: Yeah.
[00:37:59] Brandon Hancock: Um, I guess.
[00:38:00] Brandon Hancock: We'll just start going round robin.
[00:38:02] Brandon Hancock: Um, I think, Marc, you're up first, buddy.
[00:38:06] Marc Juretus: Yeah, not too much going on since the last time we talked.
[00:38:09] Marc Juretus: still working on some, I'm actually, uh, I was telling Patrick and Ty, uh, just working on some local Fyro, uh, it's like a historical society site.
[00:38:18] Marc Juretus: So if I just do one site, maybe I'll start doing some AI sites.
[00:38:21] Marc Juretus: But, uh, it's actually a good question.
[00:38:24] Marc Juretus: What he said there was the, they want to do donations for their society.
[00:38:28] Marc Juretus: So you're saying stay away from Stripe, go PayPal, or do you have another recommendation for them to receive donations?
[00:38:35] Brandon Hancock: I've heard lemon squeezy is also really good [tool:Lemon Squeezy].
[00:38:36] Brandon Hancock: I'm curious if anyone else has any alternatives, but for donations, I don't know.
[00:38:44] Marc Juretus: Okay.
[00:38:45] Marc Juretus: And, uh, and I'm using something called, uh, some CMS library called Sanity CMS, uh, CMS.
[00:38:49] Marc Juretus: I've never heard before.
[00:38:51] Marc Juretus: So it's just kind of like me playing around with it.
[00:38:53] Marc Juretus: So, but, but outside of that, there's not like a lot to report.
[00:38:56] Marc Juretus: I did take that, that Google's in we had talked about.
[00:38:59] Marc Juretus: So.
[00:39:00] Marc Juretus: Degenerative AI, it's just something where you put a title next to your name so somebody thinks you know something more, sounds like more than it really is, so, but.
[00:39:08] Brandon Hancock: Was it helpful, out of curiosity?
[00:39:11] Marc Juretus: Well, the exam was, what was weird was I didn't think of the exam in about 10 years, how tight you sit next to people, like there were a couple nurses on both sides of me taking exams, so it was like an exam center.
[00:39:20] Marc Juretus: I would say 70-75% of it is them pushing their products, hopefully that when you leave and go to a company, that's what you have them use.
[00:39:27] Marc Juretus: Yeah.
[00:39:28] Marc Juretus: But the company scenarios were interesting, like so-and-so needs to do this, that, and the other, supervise learning, this, that, and the other, what, which would you do?
[00:39:37] Marc Juretus: And, uh, what they make it tricky is, you gotta get two right out of five, which is, you know, I'm not used to taking tests like that before, where you, they, there was two right answers out of the five that they provided you.
[00:39:48] Brandon Hancock: Oh, that's tricky.
[00:39:49] Marc Juretus: In some, in some, some cases, and some of them would be kind of close, but anyways, it is what it is, it's just something to put on my title.
[00:39:56] Marc Juretus: So, um, I would ask you is, are you.
[00:40:00] Marc Juretus: Do you do the remote coding with Claude right now, like the dispatch and stuff like that?
[00:40:05] Brandon Hancock: Do you use that?
[00:40:06] Brandon Hancock: Um, occasionally, yeah, especially when I'm out and about, I like to, if I have an idea, like if I'm, it's a weird thing, if I'm listening to a podcast, um, or if I'm just talking to someone and they give me a good idea, I instantly open up Claude on my phone, and I just say, I have a cool idea, go make a new task to work on this, and just to at least get that idea out of my head.
[00:40:28] Brandon Hancock: I'm not going to take it to the finish line, but at least I have the idea out of my head, the start of it working, so whenever I get back to a place to where I can like fully analyze what's going on, I have it ready, but yeah, the, actually using Claude Code on the go, or, you know, using Claude, but the code part on your phone, absolute cheat code, um, just, just to get some ideas out of your head, um, cool, so would recommend.
[00:40:53] Marc Juretus: Yeah, that's pretty much it for me, man, I don't have a whole lot to report this week, I'm gonna sit back and see what cool things you guys are talking about.
[00:40:58] Brandon Hancock: Okay.
[00:40:59] Brandon Hancock: Okay.
<!--SEGMENT
topic: Ty's Anthropic-exam study site + zero-token challenge + FaceGate face-ID SDK
speakers: Ty Wells, Brandon Hancock, Morgan Cook, Patrick Chouinard
keywords: Anthropic Architects study site (interactive video + assessment + key-terms reveal + Q&A chat + feedback hub), zero-token challenge, FaceGate web-native face ID SDK, shared-device auth (security guards, manufacturing kiosks, ambulance Toughbooks), 99.7% accuracy, password-rotation obsolescence, 4th-amendment passcode-vs-face warrant gap, biometric-data goldmine warning, Vanta intro
summary: Ty built an interactive study site for the Anthropic Architects exam content (assessment + study guide with reveal terms + per-domain quiz + chat Q&A + embedded feedback hub). Brandon issues the 'zero-token challenge': max out every subscription per week. Then Ty's bigger reveal — FaceGate, a drop-in web-native face-ID SDK targeting shared-device authentication (security guards, kiosks, EMS Toughbooks). 99.7% accuracy, vector store of mathematical face representation only (no images), every clock-in re-rotates the vector. Morgan flags US 4th-amendment angle (police can compel face but not passcode). Patrick warns biometric data is a hacking goldmine; Brandon offers a Vanta intro for compliance.
-->

[00:41:00] Brandon Hancock: Perfect.
[00:41:00] Brandon Hancock: No, I'm excited, too.
[00:41:02] Brandon Hancock: I think, Ty, you are up.
[00:41:04] Brandon Hancock: Thanks, man.
[00:41:06] Ty Wells: Brandon, welcome back.
[00:41:08] Brandon Hancock: Always good to see you guys.
[00:41:09] Brandon Hancock: I swear I blink and a month has flown by.
[00:41:13] Brandon Hancock: 2026 has been the fastest year of my life.
[00:41:16] Brandon Hancock: I literally cannot believe it's March.
[00:41:18] Brandon Hancock: Yeah, it is unreal.
[00:41:21] Brandon Hancock: So it happens when you live into the singularity, man.
[00:41:24] Ty Wells: It's absolutely true.
[00:41:26] Ty Wells: I think last week I mentioned that I used Claude Cowork to work on my taxes, but it didn't.
[00:41:35] Ty Wells: It did a pretty good job, too good a job.
[00:41:37] Ty Wells: So I'm leaving it to the accountants because it was finding too many things.
[00:41:46] Ty Wells: This week I've been using Patrick's CMUX.
[00:41:51] Ty Wells: He turned this on to CMUX last week and that's what I'm using for my interface and working on
[00:42:00] Ty Wells: taking the test for the Anthropic Architects exam, some certification they have that they pushed out.
[00:42:11] Ty Wells: So if anybody...
[00:42:12] Brandon Hancock: to point it up?
[00:42:13] Brandon Hancock: What's it called?
[00:42:13] Ty Wells: I'm trying to...
[00:42:14] Ty Wells: What's the link?
[00:42:15] Ty Wells: It's called...
[00:42:16] Ty Wells: Hang on, I'll show you.
[00:42:20] Ty Wells: Let's see.
[00:42:25] Ty Wells: As usual, there's a few windows open.
[00:42:27] Ty Wells: So, okay, so this is the course here.
[00:42:33] Ty Wells: Drop this in the group chat.
[00:42:37] Ty Wells: Okay, that's the link.
[00:42:39] Ty Wells: Oops, it might be cut off there.
[00:42:41] Ty Wells: That doesn't look right.
[00:42:43] Brandon Hancock: See if you can click on that.
[00:42:44] Brandon Hancock: Fog Certified Architect.
[00:42:48] Ty Wells: Yeah, just search for Anthropic Architect certification thing.
[00:42:54] Brandon Hancock: I don't know if...
[00:42:57] Brandon Hancock: No, I don't think I found it.
[00:42:59] Ty Wells: Okay, hang
[00:43:00] Ty Wells: I'll get you one.
[00:43:03] Ty Wells: Why is that cut off?
[00:43:09] Brandon Hancock: Guys, we're struggling to paste a link.
[00:43:11] Ty Wells: I'm telling you.
[00:43:12] Brandon Hancock: What is wrong with us?
[00:43:14] Ty Wells: The problem is the link's all over the place, and so here, I'll get another one.
[00:43:20] Brandon Hancock: Okay, I got the real one, I think.
[00:43:21] Ty Wells: You got the real one?
[00:43:22] Brandon Hancock: I think I got the real one.
[00:43:23] Brandon Hancock: Let me share it real fast.
[00:43:26] Ty Wells: Okay, well, it's still cutting off.
[00:43:29] Ty Wells: I don't know what's going on.
[00:43:30] Ty Wells: Did you get?
[00:43:31] Ty Wells: All right, there you go.
[00:43:32] Ty Wells: That is the guy.
[00:43:35] Ty Wells: So that's their 40 page, basically showing you about agentic coding agents, how to create them in their, you know, their approach for it.
[00:43:44] Ty Wells: And so you have to, they have to invite you to take it.
[00:43:50] Ty Wells: And it covers those five domains.
[00:43:53] Brandon Hancock: Anyone can't take this?
[00:43:54] Ty Wells: Like it's not public?
[00:43:55] Ty Wells: No.
[00:43:56] Ty Wells: And then there's, you have to geth 10 people in your company to take it.
[00:44:00] Ty Wells: And they have to pass in order for you to then apply, become a, a anthropic partner, network, something, blah, blah.
[00:44:08] Brandon Hancock: Yeah.
[00:44:08] Ty Wells: This sounds like a Ponzi scheme.
[00:44:09] Ty Wells: Well, it'll, it'll change next week.
[00:44:12] Ty Wells: There'll be something else, but, you know, I had to take it up a notch.
[00:44:16] Brandon Hancock: That just wasn't sufficient for me.
[00:44:19] Ty Wells: So what I did was I built a little bit of more interactive way to learn that material.
[00:44:26] Ty Wells: Just for those that are not even, you don't even have to take it, but it helps you get a better understanding of what, you know, the subject matter is and so forth.
[00:44:37] Ty Wells: So let me copy that link.
[00:44:42] Ty Wells: So I will share my screen if I can.
[00:44:49] Ty Wells: All right.
[00:44:55] Ty Wells: I got to be better prepared than this.
[00:44:57] Ty Wells: This is crazy.
[00:44:58] Brandon Hancock: I had too many tabs.
[00:44:59] Brandon Hancock: ▶ Well, Ty's pulling.
[00:45:00] Brandon Hancock: Get up real fast, guys.
[00:45:00] Brandon Hancock: My new challenge for the week, I recommend everyone to try this challenge.
[00:45:05] Brandon Hancock: I'm trying to max out every subscription I have.
[00:45:10] Brandon Hancock: Basically every week, my goal is to leave zero tokens on the table.
[00:45:14] Brandon Hancock: So that is my new challenge for myself, because it just forces you to be busy or build systems that can run for a long time without you.
[00:45:24] Brandon Hancock: Because you'll never hit it by yourself just doing it regularly.
[00:45:27] Brandon Hancock: ▶ You have to build systems to work on things for a long time.
[00:45:30] Brandon Hancock: Extend the time.
[00:45:31] Brandon Hancock: just, you know, new challenge.
[00:45:33] Brandon Hancock: Zero token challenge.
[00:45:34] Brandon Hancock: Want to throw that out.
[00:45:35] Brandon Hancock: Nothing left on the table.
[00:45:37] Ty Wells: Sorry, Ty.
[00:45:37] Brandon Hancock: Thank you, buddy.
[00:45:39] Ty Wells: That or you can do what I did and just get another 200 max subscription because I'm burning through those tokens like crazy.
[00:45:45] Ty Wells: So on this page, you'll see I did a little video representation that explains that 40 page content.
[00:45:56] Ty Wells: And then.
[00:45:56] Ty Wells: And you can come in and do an assessment of.
[00:46:00] Ty Wells: You know, the material, and then you've got a study guide here you can go through in each domain.
[00:46:07] Ty Wells: I've got it broken down.
[00:46:09] Ty Wells: You know, what it means, just as easy as possible.
[00:46:12] Ty Wells: I added some graphics.
[00:46:14] Ty Wells: It's easier to learn this way than it is, you know, trying to read through the pages.
[00:46:18] Ty Wells: It's key terms and you can click on them and you're in a reveal and then the common mistakes, you know, it's all in there.
[00:46:26] Ty Wells: You've got a quiz that you can take, right?
[00:46:29] Ty Wells: Your domain.
[00:46:30] Ty Wells: Name quiz.
[00:46:30] Ty Wells: Then I even dropped in a little Q&A so you can, you know, you can chat about the material.
[00:46:39] Ty Wells: This is only based on the material, so it'll give you the same stuff about that material just presented in a different way so that you can better manage, you know, your learning style.
[00:46:51] Ty Wells: I'm using my feedback loop on the back here so you can click that and this will send me feedback.
[00:46:58] Ty Wells: I I use this on all my
[00:47:00] Ty Wells: Applications when users are testing so they can go ahead and send me feedback directly and it's all into a feedback hub that I then determine if it's a bug or a feature or a new request or whatever [tool:feedback hub].
[00:47:11] Ty Wells: So that is that guy that I'm working on.
[00:47:17] Ty Wells: So I'll drop the link in here.
[00:47:21] Ty Wells: Let's see.
[00:47:23] Ty Wells: Stop sharing.
[00:47:26] Ty Wells: And, um, the other project that I'm Sorry, Ty, real fast.
[00:47:31] Brandon Hancock: I just have a question.
[00:47:32] Brandon Hancock: Have you tried any of these?
[00:47:34] Brandon Hancock: Because what you're doing, like, it's so funny, everything you're describing, me and my wife always talk about, like, I, for some reason, I want her to get into AI.
[00:47:42] Brandon Hancock: It's like, it's my favorite thing to talk about.
[00:47:45] Brandon Hancock: So I was curious, have you tried any of these?
[00:47:48] Brandon Hancock: Because what you built looks like a version of this on steroids, where they have obviously like the small cores, but it's very much just like, just watch it, you know?
[00:47:57] Brandon Hancock: it does not have everything.
[00:48:00] Brandon Hancock: Yeah.
[00:48:01] Brandon Hancock: Which I think is the important part.
[00:48:03] Brandon Hancock: Instead of just absorbing, it's absorb, then test, and apply.
[00:48:07] Brandon Hancock: So that's why I'm just curious.
[00:48:08] Brandon Hancock: Have you tried any of these or any recommendations?
[00:48:11] Ty Wells: I have tried those, but the way I built it is that I can take any content and throw it into it to produce that sort of layout.
[00:48:21] Ty Wells: The format that works for me, it's really, I'm just sharing it with the community, but I've tried those, but I want that same format every time.
[00:48:29] Ty Wells: I just need the source material, right?
[00:48:31] Ty Wells: Yeah.
[00:48:31] Ty Wells: then it'll build it out and create the tests and, you know, tie it to the Q&A so you can work that way.
[00:48:39] Ty Wells: So that's, and I have to take that test on, I think, or I have to take the courses.
[00:48:46] Ty Wells: There are lessons by Friday, I think.
[00:48:48] Ty Wells: And then you take the exam after that once people go through the, like, prerequisite courses.
[00:48:54] Ty Wells: But that's the material that the exam would be on.
[00:48:57] Ty Wells: It's nothing crazy.
[00:48:58] Ty Wells: It's just, you know, they're nomenclature.
[00:49:00] Ty Wells: Patrick Chouinard so forth, the way they do it at Anthropic, but the more exciting thing that I'm working on is a new authentication system.
[00:49:13] Ty Wells: Yes, so I am doing an SDK to drop into any web application for face ID [tool:FaceGate].
[00:49:24] Brandon Hancock: That's cool.
[00:49:25] Ty Wells: Yeah, so that project I'm working on because I needed that for a project.
[00:49:31] Ty Wells: We have a lot of security guards and they check in remotely.
[00:49:34] Ty Wells: They clock in and out.
[00:49:36] Ty Wells: And we were using something called exact time.
[00:49:39] Ty Wells: And so we wanted to replace that and they're going to forget passwords.
[00:49:43] Ty Wells: And I mean, we have a hell of a time right now.
[00:49:45] Ty Wells: ▶ So we're really using that to for them to clock in and clock out with their face.
[00:49:50] Ty Wells: And so they enroll, they go ahead and they after they enroll, then they, you know, they verify and then it does, you know, a liveness check.
[00:49:59] Ty Wells: same Right...
[00:49:59] Ty Wells: it
[00:50:00] Ty Wells: That sort of thing.
[00:50:00] Ty Wells: Same thing you have.
[00:50:01] Brandon Hancock: The problem is if you're with your phone, obviously you've got face ID, you've got biometrics there, but that's tied to your phone, a single device.
[00:50:10] Ty Wells: They share a device, they share a tablet, people clock in and out.
[00:50:14] Ty Wells: So you can't use that single device for multiple people, right?
[00:50:18] Ty Wells: Because that's built into the OS.
[00:50:20] Ty Wells: This will drop into any web application.
[00:50:22] Ty Wells: So when you're choosing, I want to, you know, email password or Google auth or whatever, you know, Microsoft, this would be another one.
[00:50:29] Ty Wells: It's FaceGate.
[00:50:31] Ty Wells: That's what you would use.
[00:50:33] Ty Wells: And basically you enroll the same way.
[00:50:35] Ty Wells: Instead of getting an email to verify, you set your face up, you do some verification, you do a little liveness check, and then you're onboarded.
[00:50:43] Ty Wells: And every time you go to your whatever web application, you just show your face, use your camera.
[00:50:48] Ty Wells: And then I have an offload.
[00:50:49] Ty Wells: So if you don't have, you have a desktop with no camera, you can scan the QR code with your phone and offload and use your phone to then finish that session to actually authenticate.
[00:51:00] Brandon Hancock: David Can I have one thing real fast?
[00:51:03] Brandon Hancock: I want Morgan to go.
[00:51:04] Brandon Hancock: So in my head, I love this because it does, like, this solves a very cool problem because this applies to so many different types of businesses with shared resources.
[00:51:15] Brandon Hancock: Like, I mean, specifically fire departments, ambulance companies, the ones I'm thinking, like, they're on the same truck and they're using the same Toughbook.
[00:51:21] Brandon Hancock: So I love that because there's so many times that it would just be nice for them to, like, make it frictionless to hop onto their own accounts that's made for them.
[00:51:28] Brandon Hancock: David out of curiosity, though, how accurate is face detection?
[00:51:35] Brandon Hancock: Because is it 99.9%, which is fine if it's tied to my device, but, like, if it's global, or is it org-ready?
[00:51:45] Brandon Hancock: I guess it's like, when does the math become, like, Bob accidentally signed in as Joe because they look similar?
[00:51:51] Ty Wells: ▶ That was just my question..D.: so it's 99.7%, right?
[00:51:57] Ty Wells: And for what, like I said, for time and attendance-
[00:52:00] Ty Wells: That's great.
[00:52:01] Ty Wells: ▶ If you have some critical, you know, pull the button, push the button type thing, obviously you don't want that, but it handles a lot of the things that passwords have been killing us with for years.
[00:52:12] Ty Wells: You know, you've got to rotate password, password digest.
[00:52:16] Ty Wells: None of that stuff matters because every time you authenticate, I get a new vector to store for your face.
[00:52:23] Ty Wells: So you don't have that 30 days.
[00:52:24] Ty Wells: You're really rotating every day because when you clock in, you've got a new photo.
[00:52:30] Ty Wells: So it's, you know, it's 99.7 is the accuracy that I'm, I'm with, and that's good.
[00:52:35] Ty Wells: I mean, password, I could brute force your password like in, you know, like no time, right?
[00:52:41] Ty Wells: I mean, that's, that's the space.
[00:52:42] Ty Wells: So, and that's always a challenge trying to manage, you know, resetting passwords and all the things that we've always suffered with passwords forever.
[00:52:50] Ty Wells: That's what I'm trying to solve really for my use case, but obviously I'm building it out as a block, a drop in SDK and off you go.
[00:53:00] Ty Wells: Choose that as an option to authenticate to your platform.
[00:53:04] Brandon Hancock: That's very cool.
[00:53:05] Brandon Hancock: I think Morgan had a quick question too.
[00:53:06] Morgan Cook: Yeah, I was just going to, not so much a question, just more a comment, but that's a very useful thing as well in a lot of manufacturing type shops where they have kiosks set up and the employees got to use, you got 20 employees in the manufacturing thing using the same exact kiosk.
[00:53:25] Ty Wells: Yeah.
[00:53:25] Morgan Cook: That's a great way to deal with that.
[00:53:27] Ty Wells: Yeah, any shared device, that's a thing.
[00:53:31] Ty Wells: But even your regular, you know, all these vibe coders that are here that are, you know, their email password is an option.
[00:53:37] Ty Wells: This is an alternative and it's actually more secure than your email password.
[00:53:42] Ty Wells: I mean, if go with Google Auth, that's good too, but, you know, you've got...
[00:53:46] Morgan Cook: There's one piece of that that is a legal issue, and that is that if you have a passcode that you have to ask and give the question to, or the answer to, that's secured...
[00:53:59] Morgan Cook: ...
[00:54:00] Morgan Cook: ▶ There's search and seizure, but if they can just show the device to your face and log in, that is not secure by search and passcode.
[00:54:06] Ty Wells: There's only a liveness check.
[00:54:09] Ty Wells: But if you introduce a passcode, then you're back to passwords.
[00:54:13] Morgan Cook: My point, though, was that if the cops are using that to gain information and access to information, they don't need to have a warrant to show the device and get your face to access.
[00:54:26] Morgan Cook: They do need to have a warrant if you have to give them a passcode.
[00:54:32] Ty Wells: Well, that's interesting.
[00:54:33] Ty Wells: Okay, I get your point.
[00:54:34] Morgan Cook: That's U.S.
[00:54:34] Ty Wells: thing, yeah.
[00:54:35] Ty Wells: Yeah, I get your point.
[00:54:36] Ty Wells: Yeah, and I'll definitely look into that.
[00:54:40] Ty Wells: But the same rules apply in terms of, you know, verifying, like, when you're not sure you're logging in from a different location, you know, your geofence, the same thing.
[00:54:50] Ty Wells: Then that's when the liveness check comes in.
[00:54:52] Ty Wells: And so hopefully next week I'll have something where you guys can test it in terms of just you just go on.
[00:54:59] Ty Wells: see Bye.
[00:55:00] Ty Wells: Put your face there and try to and then try to verify it and then try to break it, you know, in terms of photos or whatever you try to do, put somebody else's face there.
[00:55:10] Ty Wells: So that's where I'm at.
[00:55:14] Brandon Hancock: That's very cool.
[00:55:15] Brandon Hancock: That's always thinking outside the box.
[00:55:16] Brandon Hancock: I'm very excited because and I would also just we just I always like think about ideas from like not just the tech side, but the business side, the real.
[00:55:25] Brandon Hancock: The only thing that I could think of that's even remotely similar to what you're doing is I think it's called real ID for the government.
[00:55:35] Brandon Hancock: Like a lot of government websites have this.
[00:55:39] Brandon Hancock: So I would be very curious if there's like.
[00:55:43] Brandon Hancock: I'd be very curious if there's something else that they're not serving because like I would just think of like as your brainstorming ideas, if there's anything else that could be like if you could steal some inspiration from them, too, because they're actively doing real ID, but strictly for like I had to sign a legal.
[00:56:00] Brandon Hancock: The other day, and they were like forced me to go do my real ID account.
[00:56:04] Brandon Hancock: Like they basically became a trusted source for to authenticate stuff because it's a multi-step.
[00:56:11] Brandon Hancock: It's a video process of my face plus an ID.
[00:56:14] Brandon Hancock: They match.
[00:56:16] Brandon Hancock: Fantastic.
[00:56:16] Brandon Hancock: I can virtually confirm that Brandon is doing something real.
[00:56:20] Brandon Hancock: So I just want to throw like that's another example.
[00:56:22] Brandon Hancock: Just maybe get some other ideas juices flowing.
[00:56:25] Brandon Hancock: But I just want to share that because I always love the creative ideas.
[00:56:27] Ty Wells: Yeah, I appreciate that.
[00:56:28] Brandon Hancock: Yeah.
[00:56:29] Brandon Hancock: And then Patrick.
[00:56:31] Patrick Chouinard: Yep.
[00:56:31] Patrick Chouinard: ▶ The only thing I would say, Ty, be careful about the type of data that that represents because the accumulating biometric data about your user will be a goldmine of data for, let's say, interested third party.
[00:56:49] Patrick Chouinard: So that's the only thing I'd be careful about, the responsibility you would put on yourself hosting that type of data.
[00:56:57] Ty Wells: Yeah.
[00:56:57] Ty Wells: And it's, I mean, it's, it's, a vector store, right?
[00:57:00] Ty Wells: It's, that's what it is.
[00:57:02] Ty Wells: So, I mean, it's a mathematical representation that's seeded, keyed, you know, encrypted.
[00:57:08] Ty Wells: I mean, it's, it's just like your password, except it is not, and I'm not storing the face, the image or anything.
[00:57:16] Ty Wells: It's just the mathematical representation, but I get your, I get your point.
[00:57:20] Patrick Chouinard: It's just when more valuable is the information, more means will be put to trying to hack it.
[00:57:27] Ty Wells: Oh yeah.
[00:57:28] Ty Wells: Oh, absolutely.
[00:57:30] Patrick Chouinard: So that's why, and that is probably the top type of information.
[00:57:34] Patrick Chouinard: So a lot of mean would go to the words hacking it.
[00:57:38] Ty Wells: Yeah.
[00:57:39] Ty Wells: Yeah.
[00:57:39] Ty Wells: Oh, I'm sure they'll put some resources to it.
[00:57:42] Ty Wells: I'm to put Auto Researcher on it.
[00:57:47] Brandon Hancock: I mean, hey, you could just get HIPAA, HIPAA, go through the whole process, drop a cool 16, 16, 20,000, and then you're good to go, man.
[00:57:55] Ty Wells: Yeah.
[00:57:56] Ty Wells: Well, I'm going to, I'm going to, I'm thinking about Invanta, you know, let's say once we've got it full of
[00:58:00] Ty Wells: If it's out, I'm probably going to do a Vanta to see where we're at.
[00:58:04] Brandon Hancock: ▶ I'd be happy to make an introduction.
[00:58:07] Brandon Hancock: The guy talked to us.
[00:58:08] Ty Wells: He was very nice.
[00:58:11] Brandon Hancock: Okay, cool.
[00:58:12] Brandon Hancock: We'll keep on cruising, guys.
<!--SEGMENT
topic: Juan — agentic DevOps + Brandon recommends Terraform IaC
speakers: Juan Torres, Brandon Hancock, Hemal Shah, Naren
keywords: agentic DevOps, AWS CLI for VPC + EC2 + cluster provisioning, T3 x-large + Ubuntu spec docs, four laws of behavioral change for UX, image-to-image diffusion pipeline, Terraform infrastructure-as-code, Alembic SQL analogy, source-of-truth for infrastructure
summary: Juan demos his agentic DevOps workflow — AWS CLI driven by Claude Code provisions VPC, EC2 (T3 x-large + Ubuntu), database clusters, all captured as MD-spec SOPs that he reuses across projects. Frontend follows the four laws of behavioral change. Brandon recommends Terraform: representing infrastructure as code is a source of truth that beats Python-script drift. Juan can work backwards from his existing setup to extract Terraform files (Hemal/Naren agree on IaC = Alembic for SQL).
-->

[00:58:13] Brandon Hancock: I think, Juan, you're up next, man.
[00:58:15] Juan Torres: What awesome projects are we working on?
[00:58:17] Juan Torres: Hey, nice to see you, Brandon.
[00:58:20] Juan Torres: Hey, man.
[00:58:21] Juan Torres: Yeah, I've been actually, I've been trying to use some of the methodology that you deployed in ShipKit in order to get things faster.
[00:58:34] Juan Torres: I like it.
[00:58:36] Juan Torres: I'll go in, yeah.
[00:58:36] Juan Torres: So I've been working on this web application, and this is, you know, my own, I guess, business idea.
[00:58:45] Juan Torres: We, I haven't finalized the application.
[00:58:51] Juan Torres: I think I found feasible, a feasible AI pipeline.
[00:58:56] Juan Torres: It's basically a diffusion image to image [tool:AWS CLI] [tool:Kero CLI].
[00:58:59] Juan Torres: lot get the out it's…
[00:59:00] Juan Torres: You know, generation kind of application, I've finished the back-end data web application, haven't finished the front-end, but I want to, you know, show it to you guys when it's finished, because I think you guys are going to like it, I think you guys are going to appreciate some of the aspects of the engineering and the DevOps, so I'll keep myself uh, project-wise version for now.
[00:59:34] Brandon Hancock: So, so wait, you said next week, show it?
[00:59:37] Juan Torres: Uh, well, I don't know when I'm going to finish the first, um, and, and I don't uh, whether I want to, like, first, uh, what is it called, stress-tested on the field, because this is going to get, uh, stress-tested on the field, so it's going to be, and, uh, in a, in in a physical location, uh, to be actually, uh, you know, uh, stressed it through.
[00:59:59] Juan Torres: That's true.
[01:00:00] Juan Torres: all the parameters that I have set up.
[01:00:03] Juan Torres: So I don't know if to show it to you guys before or after, I stressed it on the field.
[01:00:09] Juan Torres: And also, having finished the front end, I've been very methodological on the data science aspect of it, because I've been trying to take quality control of the transformation, right?
[01:00:20] Juan Torres: So I've been very meticulous on the development of the back end data web application.
[01:00:26] Juan Torres: So my modus operandi is basically developed a data web application for the back end, right?
[01:00:32] Juan Torres: For me to be able to see the processes that happen.
[01:00:35] Juan Torres: And for a technician to be able to fix issues rather fast.
[01:00:39] Juan Torres: And then there's going to be the front end, which, you know, follows the four laws of behavioral change, which is make it easy, make it attractive, make it satisfying, make it, I don't remember the third one.
[01:00:52] Juan Torres: But basically, that's the one that it's like for dummies, right?
[01:00:54] Juan Torres: You just click a button and everything works smoothly.
[01:00:58] Juan Torres: So I haven't finished process thing.
[01:01:00] Juan Torres: I'm almost done with the data web application.
[01:01:02] Juan Torres: So I have the data engineering aspect of it.
[01:01:06] Juan Torres: It's going to have text messaging capabilities, right?
[01:01:09] Juan Torres: So you're going to put your text and your email, and it's going to use AWS resources for sending transform images to people, right?
[01:01:18] Juan Torres: So it has a relatively comprehensive cloud architecture in AWS.
[01:01:25] Juan Torres: ▶ And also, like I said before, I can emphasize, you guys need to use agentic DevOps by giving the right permissions to a user and then having AWS CLI in your whatever agentic ID you're using, right?
[01:01:43] Juan Torres: So you can just give it the resources for it to construct EC2 instances, clusters of databases, set up the rules of inbound rules, outbound rules, right?
[01:01:54] Juan Torres: And everything is much smoother, and I'm basically collecting...
[01:02:00] Juan Torres: Documentation on all the steps that I'm doing as standard operating procedures and specs for me to go back and be able to basically tell my clock code, hey, there's an issue with the EC2 instance, do you think this is an issue with two little gigabytes in CPU that it has, right?
[01:02:21] Juan Torres: ▶ So it, and then I can use the standard operating procedure, MDs, and then place them somewhere in another project and be like, hey, create something similar to this, right, create the same EC2 instance with the Ubuntu operating system with, you know, T3 x-large EC2 instance with 30 gigabytes of memory, solid memory, right?
[01:02:43] Juan Torres: So all those things I'm already systematizing, trying to systematize agentic DevOps for me to then be able to replicate similar projects in the future.
[01:02:52] Brandon Hancock: And so, hey, out of curiosity, because I love everything you're saying, totally makes sense.
[01:02:56] Brandon Hancock: Are you using Terraform at all to, like, define your.. [tool:Terraform].
[01:03:03] Juan Torres: You mean my AWS infrastructure?
[01:03:07] Brandon Hancock: Yeah, and the only reason I ask is because at one point when I was trying to spin up a document parser kind of service or whatever, Terraform was stupid helpful because Terraform, I applied it to Google Cloud in my case, and as a result, I had my Cloud Run functions, I had my S3 buckets, like I had everything stood up, and then when I ran into an issue, I could always point back to my Terraform as a source of truth.
[01:03:36] Brandon Hancock: So that's why I was going to say, I'd be very curious, making sure if, because it sounds like you're doing the full loop, it's just, what is, how are we representing the state of our infrastructure?
[01:03:48] Brandon Hancock: I was going say, I played with Terraform, and I was curious if you had another alternative or if you recommend something else.
[01:03:56] Brandon Hancock: So what is Terraform?
[01:03:58] Brandon Hancock: It is...
[01:03:59] Brandon Hancock: It is...
[01:04:00] Brandon Hancock: It's basically a way to document how you want to set up your cloud infrastructure.
[01:04:06] Naren: So, Terraform, if someone wants to add on to what I'm saying too, feel free.
[01:04:11] Brandon Hancock: But basically it's a, let me just show you really fast.
[01:04:15] Hemal Shah: ▶ Infrastructure as a code, so you define infrastructure as a code.
[01:04:19] Naren: Whatever you're doing with your agent, it can do almost easily.
[01:04:24] Juan Torres: Well, it's almost like if you were to, okay, I see.
[01:04:27] Juan Torres: It's like Alembic for SQL kind of deal.
[01:04:31] Brandon Hancock: Yeah, it basically just, it is a code representation of your infrastructure.
[01:04:37] Brandon Hancock: So IAC, infrastructure as code.
[01:04:40] Brandon Hancock: It is a source of truth for how your infrastructure should look like.
[01:04:44] Brandon Hancock: So I was gonna say, as a guy who's like, I mean, I've done the like, I've done cloud infrastructure.
[01:04:49] Brandon Hancock: I'm not gonna say I'm a pro by any means.
[01:04:50] Brandon Hancock: I'm definitely not.
[01:04:52] Brandon Hancock: This passed over to our agents was a game changer because we could argue about the same thing.
[01:04:58] Brandon Hancock: think.
[01:04:58] Brandon Hancock: think.
[01:04:58] Brandon Hancock: I think.
[01:04:59] Brandon Hancock: I
[01:05:00] Brandon Hancock: Versus I've done it in the past, where I've just done a bunch of Python scripts, and then it's like, wait, what is the state of my database?
[01:05:07] Brandon Hancock: Because my Python code does not represent the state, because I'm constantly making changes, you know, so Terraform, an absolute cheat code.
[01:05:15] Brandon Hancock: So what you're describing, I was gonna say, I think you would really like that.
[01:05:18] Brandon Hancock: And it knows it very well, Patrick called it out, yeah.
[01:05:21] Juan Torres: Okay, cool.
[01:05:23] Juan Torres: Yes, actually, I've heard of infrastructure as code, and it totally overpassed my mind.
[01:05:30] Juan Torres: I don't know why I didn't just, from the beginning, started to do that.
[01:05:34] Brandon Hancock: ▶ The cool part is, you already have the thing set up, so you can always work backwards at this point, to say, hey, Claude Code, inspect the hell out of everything I've done, and go make these Terraform files.
[01:05:44] Brandon Hancock: You've already done the work, you know.
[01:05:46] Brandon Hancock: Now it's just extract and codify, so.
[01:05:50] Juan Torres: For sure.
[01:05:51] Brandon Hancock: But yeah, I'm pumped at this point.
[01:05:53] Brandon Hancock: Patrick, if you want to hop in too.
[01:05:55] Patrick Chouinard: I was gonna say, Cloud is actually extraordinary as an operator.
[01:06:02] Patrick Chouinard: So, yeah, lean on it, because just to give you an example, right now, while the call is going, I have it deploying application in Databricks, so it works extremely well.
[01:06:14] Juan Torres: Nice.
[01:06:16] Brandon Hancock: Perfect.
[01:06:17] Brandon Hancock: Anything else we can help with, or any other exciting news?
[01:06:20] Juan Torres: No, no, I will hit you guys up if there's any questions regarding efficiency, because there's like definitely corners like this that, you know, you guys are like pointing to me too, that I, you know, I'm not thinking about, so this is really helpful.
[01:06:35] Brandon Hancock: Okay.
[01:06:36] Brandon Hancock: Hey, always happy to help.
[01:06:37] Brandon Hancock: Smarter as a group.
[01:06:38] Brandon Hancock: That's what we're here for.
[01:06:40] Brandon Hancock: All right.
[01:06:41] Brandon Hancock: Perfect.
[01:06:42] Brandon Hancock: We'll keep on cruising.
[01:06:45] Brandon Hancock: I think, let me just take a screenshot so you guys can see what I see, by the way, so it's not just not having to guess.
<!--SEGMENT
topic: Patrick — Databricks deployment + AI personality kit + organic GitHub-repo client win
speakers: Patrick Chouinard, Brandon Hancock, Hemal Shah
keywords: Intelligent Dashboard published to public GitHub, GitHub agent search-driven client discovery, Databricks deployment via Claude Code, AI personality kit, CLAUDE.md + GEMINI.md + copilot-instructions.md auto-deploy script, schema with behavior + output type + constraints, OpenClaude vs Cowork maturity
summary: Patrick's Intelligent Dashboard (published openly on GitHub) was discovered organically by an architect at his client via GitHub's agent-driven search — direct contract to deploy at the client. Currently deploying to Databricks live during the call via Claude Code. He also built an AI personality kit with deploy script that pushes a personality + output type + constraints schema into CLAUDE.md, GEMINI.md, and copilot-instructions.md across all CLI installations. Hemal asks about ChatGPT-to-Cowork integration; Patrick: the missing bridge — OpenAI has best voice, Claude has best dev model, no direct talk yet.
-->

[01:06:52] Brandon Hancock: Patrick, you are up, buddy.
[01:06:54] Brandon Hancock: So what's been going on in Patrick land?
[01:06:56] Brandon Hancock: What are we, what cool new projects we working on?
[01:07:00] Brandon Hancock: Always cooking up something, what are we doing?
[01:07:03] Patrick Chouinard: A little bit slower week this week, in terms of new project, because the business has been ramping up a lot.
[01:07:11] Patrick Chouinard: Basically, I don't know if you remember, Brendan, but the whole research pipeline using Claude Code or Gemini CLI.
[01:07:21] Brandon Hancock: Yeah.
[01:07:21] Patrick Chouinard: Well, basically, I've now been contracted to implement that in production form at my client, so.
[01:07:28] Brandon Hancock: That's awesome, man.
[01:07:31] Brandon Hancock: I love, real fast, I think this is going to be a trend from this point going forward.
[01:07:36] Brandon Hancock: It will be self-experimentation, step one, like Patrick was doing.
[01:07:41] Brandon Hancock: Step two is internal to an organization, your own organization, just so you can help experiment in the confines of a big business where there's more rules, maybe some more set up.
[01:07:51] Brandon Hancock: And then that becomes a case study to then go off and do client work.
[01:07:54] Brandon Hancock: But it all starts with the individual playing around with it themselves first.
[01:07:59] Brandon Hancock: And Patrick's doing that.
[01:08:00] Brandon Hancock: And on steroids, on a thousand different domains.
[01:08:02] Patrick Chouinard: ▶ The very funny part about this is that I published to my own GitHub repo on the Intelligent Dashboard, and basically one of the architects at the client where I work found it through searching using the GitHub agent on the GitHub site.
[01:08:23] Patrick Chouinard: And while he was searching for something to answer one of his use case.
[01:08:28] Patrick Chouinard: So I got a call.
[01:08:29] Patrick Chouinard: He's like, can we take that and implement it here?
[01:08:33] Brandon Hancock: That's very cool.
[01:08:34] Brandon Hancock: So literally it happened organically.
[01:08:36] Brandon Hancock: Like you never heard of this guy.
[01:08:37] Brandon Hancock: was just strictly a...
[01:08:38] Patrick Chouinard: Well, I've heard of him because he's an architect in the company, but I never interacted with him.
[01:08:43] Patrick Chouinard: He's the one who contacted me.
[01:08:44] Patrick Chouinard: He's like, hey, I found that on the repo that seems to be yours.
[01:08:48] Brandon Hancock: And we won one for this.
[01:08:50] Brandon Hancock: That's awesome, man.
[01:08:52] Brandon Hancock: Very cool, Patrick.
[01:08:53] Brandon Hancock: Always.
[01:08:53] Brandon Hancock: Yeah.
[01:08:54] Brandon Hancock: I mean, hey, that's cool things happen when you put your thoughts out there.
[01:08:58] Patrick Chouinard: That's actually what I'm deploying.
[01:09:00] Patrick Chouinard: I'm Databricks right now [tool:Databricks].
[01:09:02] Brandon Hancock: Really?
[01:09:03] Patrick Chouinard: I'm literally in the middle of deploying it, or having Claude Code deploy it for me.
[01:09:08] Brandon Hancock: So real fast, I am not an expert on Databricks.
[01:09:14] Brandon Hancock: Out of curiosity, let me just look real fast, I just want to show, I'd love to just like, in your words, when and why would someone use Databricks?
[01:09:26] Patrick Chouinard: For me, to be quite honest, I'm not an expert in Databricks, it's just the platform, the architecture as deemed as where we need to deploy our data application, so.
[01:09:37] Brandon Hancock: Okay.
[01:09:38] Brandon Hancock: I just heard, I've heard a bunch of people talk about it, I've only ever heard good things, it's just like, I've never actually seen it in action, if that makes sense.
[01:09:48] Patrick Chouinard: Yeah.
[01:09:49] Patrick Chouinard: Well, actually the models used are provided by Databricks itself, so it is a model provider, it has obviously the data layer internally.
[01:09:59] Patrick Chouinard: And.
[01:10:00] Patrick Chouinard: And the application is deployed as a Databricks apps because I basically created my little CMS version, if you want, behind the scene that manages the dashboard.
[01:10:13] Patrick Chouinard: And the dashboard is just the publishing surface to show the data that's been gathered through the research pipeline.
[01:10:23] Brandon Hancock: So what's being deployed?
[01:10:25] Brandon Hancock: I need to look at this more.
[01:10:27] Brandon Hancock: That's very cool.
[01:10:29] Patrick Chouinard: What I worked on personally during this week is I was tired because I've been talking with Claude Code and Gemini CLI for weeks now, pretty much 10 hours a day.
[01:10:44] Patrick Chouinard: So their boring personality was getting to me.
[01:10:49] Patrick Chouinard: So this weekend I created a personality kit that auto-deployed to all of my CLIs [tool:AI personality kit].
[01:10:55] Patrick Chouinard: So now they have a little bit more spunk and personality.
[01:10:58] Patrick Chouinard: So it makes my coding sense.
[01:11:00] Patrick Chouinard: So a lot livelier and more fun.
[01:11:02] Brandon Hancock: Who'd you go for?
[01:11:03] Brandon Hancock: What type of personality do go for?
[01:11:05] Brandon Hancock: Like an actor or just like a funny, like for a movie or something?
[01:11:09] Patrick Chouinard: No, I actually created a personality schema with behavior, with output type, and with also constraint to make sure that I had a good output, and actually I'm gonna put the repo in, because yeah, obviously I made it a repo.
[01:11:29] Patrick Chouinard: So I'm gonna put it in the chat.
[01:11:34] Brandon Hancock: Well, let me see this.
[01:11:37] Patrick Chouinard: And the other thing, I've worked with Cowork to actually integrate auto-research loop into RecapFlow.
[01:11:52] Patrick Chouinard: So I know you weren't there, Brendan, but for a couple of weeks, I've built something called RecapFlow that analyzes international Okay, that's
[01:12:00] Patrick Chouinard: The and the chat, and it outputs a new recap, including all the links that are in the chat and reconcile answers that are in the chat versus what's been asked in the transcript, all of that.
[01:12:13] Brandon Hancock: Okay.
[01:12:14] Patrick Chouinard: So to improve it, now I want to implement the auto-research loop, both at a mechanical level to improve the quality of the output, and also, and that's what I want to ask the people.
[01:12:30] Patrick Chouinard: here is now every week, I'm going to try to take all of the comments out of the recap and feed them back into the improvement loop.
[01:12:41] Brandon Hancock: Mmm.
[01:12:41] Patrick Chouinard: So please comment as much as possible on that post, and we'll see from week to week if we can improve the quality.
[01:12:50] Patrick Chouinard: One, if you remember, you had a comment last week about reordering the section, so that's been done already.
[01:12:57] Brandon Hancock: That's cool.
[01:12:57] Brandon Hancock: So we'll see.
[01:12:59] Patrick Chouinard: you at how later
[01:13:00] Patrick Chouinard: So we can improve it.
[01:13:01] Patrick Chouinard: Let's make it a little community experiment.
[01:13:05] Brandon Hancock: I love that, Patrick.
[01:13:07] Brandon Hancock: And I will say real fast, one of the hardest parts is doing loops on language, sorry, on language.
[01:13:15] Brandon Hancock: Because if you watch, like if you dig into auto-research, their key scoring function is like perf per bits or something along those lines where it's a mathematical number.
[01:13:27] Brandon Hancock: Like you 100% know if you're getting closer to your desired goal or if you're moving further away.
[01:13:33] Brandon Hancock: But with subjective stuff like narratives, documents, language, it is infinitely harder because it's like what is good, you know?
[01:13:45] Patrick Chouinard: Yeah, but that's exactly why I use Cowork to think about how to use the philosophy of the loop without using the loop itself.
[01:13:53] Patrick Chouinard: Because now the evaluation is going to be all of your comments, not an honest function.
[01:13:59] Patrick Chouinard: But...
[01:14:00] Patrick Chouinard: The actual application of the improvement will be within the loop.
[01:14:04] Patrick Chouinard: So I'm going to have a fast loop that's going to run on every pipeline to correct the mechanical problem.
[01:14:10] Patrick Chouinard: So have I captured all the URL?
[01:14:12] Patrick Chouinard: Have I compressed properly?
[01:14:14] Patrick Chouinard: Everything that has a yes or no answer.
[01:14:17] Patrick Chouinard: And then the evaluation will be the processing of the comment on a weekly basis.
[01:14:23] Patrick Chouinard: And I might actually even run a side loop to improve the question themselves in order to improve loop itself.
[01:14:32] Brandon Hancock: So we'll see what's crazy is this is literally what's happening at the AI labs, like the big boy AI labs.
[01:14:38] Brandon Hancock: And now it's just like what they do now gets applied to a thousand individual small projects, you know?
[01:14:45] Brandon Hancock: Um, so we, we are basically the big boys, uh, you know, we're doing what they're doing.
[01:14:50] Brandon Hancock: So that's awesome.
[01:14:51] Brandon Hancock: And I think Elijah had a quick question for you too.
[01:14:53] Brandon Hancock: Yeah.
[01:14:54] Naren: Brendan, I have, I'm coming from UK, so I need to go.
[01:14:57] Brandon Hancock: So can I ask you a question, please?
[01:14:59] Patrick Chouinard: Sure.
[01:15:00] Brandon Hancock: Can we, wait, do we want Elijah then?
[01:15:04] Brandon Hancock: Okay, sorry, Naren, if you want to go.
[01:15:06] Elijah Stambaugh: Yeah, whatever, it's fine with me.
[01:15:08] Naren: Sorry, sorry, very sorry for that.
[01:15:11] Brandon Hancock: Naren, yeah, if you want to go real fast.
[01:15:12] Naren: Yeah, Naren, when will you be back?
[01:15:15] Naren: You know, I'm planning to get the Shipkit, so I know you're not, you know, I have one more question.
[01:15:27] Naren: Are RAG and other stuff currently available on Shipkit still relevant, you know, given that the space is moving fast?
[01:15:34] Brandon Hancock: Yeah, so a few things.
[01:15:36] Brandon Hancock: When I'll be back full-time, still TBD, I was basically planning to do, like, a five-ish month just deep dive into our startup.
[01:15:46] Brandon Hancock: And just, like, it's going well.
[01:15:47] Brandon Hancock: Like, just heads up, like, we're slowly on the cusp of, like, going from, like, this to, like, landing a big strategic partnership.
[01:15:55] Brandon Hancock: So it's just, like, I'm working on this 24-7.
[01:15:58] Brandon Hancock: So, like, the goal...
[01:16:00] Brandon Hancock: The is eventually to get to where we're not having to fight for every dollar and customer to where it's more in a maintenance mode, so the second things are in a maintenance mode, that's when I wanted to start back up YouTube and community stuff, but it's just like, I would kick myself if I cave up on, I mean, literally potentially millions of dollars to do more YouTube videos, so that's, mean, just being honest, so the answer is I think it'll be five months, which should be late May at this, maybe late May, early June at this point, but I, I just truly don't know until, like, we start landing some big contracts, just, just truthfully.
[01:16:38] Brandon Hancock: Um, on the relevance of the Shipkit projects, so, I'll tell you a few things that would be helpful to know, so, like, chat, RAG, the core ideas in the same technologies, like, I mean, we're using a lot of Vercel AI SDK, that's still the exact same thing that you'll use today.
[01:16:55] Brandon Hancock: When it comes to RAG, that still exists, we've updated all the models.
[01:16:59] Brandon Hancock: So, all the,
[01:17:00] Brandon Hancock: The fundamentals of the projects have not changed, like chat and RAG have not changed fundamentally, the only thing that's have changed is we're now on bigger models, the thing that has changed a little bit is the workflows, so a lot of people use cursor, like when this came out, it was all cursor, then it kind of moved to Claude Code, so that's what I use now primarily, there's a whole extra modules on it, the thing that's even better now is I like to use, it's called CMux, which is great for managing multiple instances of Claude Code, so at this point I have, I mean on my screen, I probably have like 20 different Claude Code instances in different tabs and windows, but that's like getting advanced, so for like beginners, all the core concepts that you need to understand are in there, and then it's once you get to that advanced side, that's where it needs updating of like how things are as of March, because then it's kind of changed a little bit with some new tools that just didn't exist three months ago.
[01:17:59] Brandon Hancock: So, so hopefully
[01:18:00] Brandon Hancock: Hopefully, hopefully that helps, uh, that, hey, guys, I'll get a, I'll get a nice John boat, I'll take turns putting y'all on, uh, but I, I hope that helps, so, still things are very, very relevant, but other parts, like, they've just been new things that could be, could be nicer, and I'll shoot you the instance, I mean, CMUX is, uh, I'll shoot you a link to it right now, shout out to Mitch getting me onto it, I don't think he's on the call today, but he's the one who got me on, but I hope, I hope that, helps.
[01:18:30] Brandon Hancock: Um, yeah, thank you, and, uh, uh, and I sent a private message to you in this chat, would you please, uh, say, oh, okay, well, let me go, um, um, if you could email me on that one, I'd be, I mean, I mean, I'll just be honest, the short answer is, at this point, no, uh, I apologize, but, yeah, yeah, I, I just apologize, we just, uh, uh, uh, uh
[01:19:00] Brandon Hancock: have not done any of those, I, yeah, so I just apologize, okay, cool, all right, well, thank you, man, all right, Elijah, you're up next, man.
[01:19:14] Elijah Stambaugh: Yeah, so Patrick, you had mentioned about you, you insert that personality into all of your CLI, can you, could you, so my question is, if I could give it a little bit of context.
[01:19:28] Elijah Stambaugh: Sure.
[01:19:29] Elijah Stambaugh: What I'm wondering is, basically, I've got my executive assistant in AI, you know, my Claude Code executive assistant, and then I have these other repos where I have different skills for different jobs, and then repos that I'm sharing with people on my team as well, that we're working in.
[01:19:49] Elijah Stambaugh: Now, don't think just code per se, right?
[01:19:52] Elijah Stambaugh: Um, but when you said the, they're in your CLIs, what do you, what do you, what exactly do you mean by that?
[01:19:59] Patrick Chouinard: It's, it's big.
[01:20:00] Patrick Chouinard: ▶ It's basically just a small snippet of code that I put in the CLAUDE.md that gives the AI a personality, an output type, and a list of constraints.
[01:20:13] Patrick Chouinard: So basically, it replies the same way that my web-based AI chatbot are responding.
[01:20:21] Patrick Chouinard: It's just because I have highly modified personalities in ChatGPT and Claude and Gemini.
[01:20:28] Patrick Chouinard: And when you get used to that type of answer, going into the code part and having it respond like a dry cereal box, it's not fun, let's say.
[01:20:41] Patrick Chouinard: basically...
[01:20:42] Elijah Stambaugh: So when you use the term CLI, you're referencing specifically your CLAUDE.md file within a particular project.
[01:20:49] Patrick Chouinard: No, actually, I've modified the CLAUDE.md, the GEMINI.md, and the copilot-instructions.md at the profile level.
[01:20:57] Patrick Chouinard: So basically, it's all of that.
[01:20:59] Patrick Chouinard: And...
[01:21:00] Patrick Chouinard: Every time I open a Claude Code CLI, a Gemini CLI, or a Copilot CLI on my machine, or a Codex CLI for that matter, they all have the same personality now.
[01:21:09] Patrick Chouinard: And I made the deployment.
[01:21:11] Patrick Chouinard: ▶ If you look at the repo, there's a script that once you've tweaked the personality, you just run the script and it deploys it to all of the CLI you have installed.
[01:21:21] Elijah Stambaugh: Okay.
[01:21:22] Elijah Stambaugh: Can you repost the repo?
[01:21:24] Patrick Chouinard: I apologize in the channel.
[01:21:27] Elijah Stambaugh: Yeah, I've looked at it before.
[01:21:29] Elijah Stambaugh: I just...
[01:21:29] Elijah Stambaugh: Thank you.
[01:21:30] Elijah Stambaugh: Thanks, Brandon.
[01:21:31] Elijah Stambaugh: Good to see you.
[01:21:32] Patrick Chouinard: You did not see that one because I posted it literally this week, but...
[01:21:37] Elijah Stambaugh: Oh, okay.
[01:21:38] Patrick Chouinard: Perfect.
[01:21:39] Elijah Stambaugh: This one is brand, brand new.
[01:21:41] Patrick Chouinard: AI personality is something I have worked on this weekend.
[01:21:45] Elijah Stambaugh: All right.
[01:21:46] Elijah Stambaugh: Thank you.
[01:21:48] Patrick Chouinard: Yep.
[01:21:48] Patrick Chouinard: Okay.
[01:21:51] Brandon Hancock: is is a so.
[01:21:56] Brandon Hancock: is a good.
[01:22:00] Brandon Hancock: How, where are we at?
[01:22:02] Hemal Shah: Where are we at, buddy?
[01:22:04] Hemal Shah: I'll message you.
[01:22:05] Hemal Shah: Okay.
<!--SEGMENT
topic: Hemal — Databricks Lakehouse explainer + driving-mode Whisperflow workflow
speakers: Hemal Shah, Brandon Hancock, Patrick Chouinard
keywords: Databricks Delta Lake, Lakehouse architecture, BYO storage on GCP/AWS S3, ChatGPT mobile new-session voice flow, Whisperflow on iPhone, source-of-inspiration prompt context, two-way ChatGPT clarification while driving, ChatGPT-Cowork bridge gap
summary: Hemal explains Databricks: Lakehouse marries data warehouse analytical efficiency with data lake raw breadth, served at lightning speed via their proprietary Delta Lake. They store nothing in their own ecosystem — BYO GCP/AWS bucket. Then asks Brandon about driving-mode coding: Brandon uses ChatGPT mobile + Whisperflow to dump ideas as new task templates branched off main; the ShipKit task template clarifies follow-up steps before coding. Patrick wraps OpenAI's car-voice into a CowoRoOS environment that converts the discussion to PRD, splits into features, and hands off to Claude Code.
-->

[01:22:08] Hemal Shah: All right.
[01:22:10] Hemal Shah: So, yeah, I mean, nothing much actively going on, but quick comment on the data warehouse that you mentioned, Brendan.
[01:22:17] Hemal Shah: Sorry, Databricks.
[01:22:19] Hemal Shah: So, Databricks is where it shines and we use it heavily.
[01:22:25] Hemal Shah: It's kind of, we have data warehouse, which is very analytical, and we have Data Lake, all technologies, right?
[01:22:31] Hemal Shah: Which has been around, which provides you raw data, but it's very, very efficient.
[01:22:37] Hemal Shah: But, when you want to do both, efficiently, you want to look up data in a structured and analytical way.
[01:22:43] Hemal Shah: That's where Databricks shines.
[01:22:45] Hemal Shah: They came up with a Lakehouse [tool:Lakehouse].
[01:22:47] Hemal Shah: They run new terminology.
[01:22:49] Hemal Shah: So, you can do analytical stuff, but at a lightning speed, with very minimal latency.
[01:22:56] Hemal Shah: And they bring ML, AI, pipeline, dashboard, everything.
[01:23:00] Hemal Shah: ▶ And beauty is they don't store any of this in their ecosystem, they rely on GCP, AWS, Cloud Bucket Storage, so it's their own secret sauce, they call it Delta Lake, is what they're saying [tool:Delta Lake].
[01:23:16] Hemal Shah: Anyway, yeah, but it's good for all data-heavy processing.
[01:23:21] Hemal Shah: One question I have is, Claude Code, whenever you are, you know, driving or when you want to brainstorm some ideas, I think you also mentioned earlier in the poll, if you want to have it quickly capture ideas and continue the conversation, I tried a Cloud's mobile apps conversation mode.
[01:23:42] Brandon Hancock: Is that what you use or what's the recommendation?
[01:23:45] Brandon Hancock: It's not that...
[01:23:47] Brandon Hancock: Yeah, yeah, yeah.
[01:23:48] Brandon Hancock: So it's strictly, let me see if I can turn this on, uh, look at this, Cloud.
[01:23:56] Brandon Hancock: Um, yeah, so let me click a button.
[01:24:03] Brandon Hancock: Yeah, so I just, every time I, I hope you guys can see that, but every time I have a new idea, I just click Claude, and then I click Code, and then I have New Session [tool:Whisperflow].
[01:24:11] Brandon Hancock: When I click New Session, it's going to say, like, where do you want to build this, and off what branch?
[01:24:18] Brandon Hancock: And then at that point, two things you could do, I usually just hit the microphone button, and I just talk for a long time.
[01:24:24] Brandon Hancock: The other thing that I did recently is I put Whisperflow on my iPhone, and I love that.
[01:24:30] Brandon Hancock: Okay.
[01:24:31] Brandon Hancock: So I actually can hit, I can hit the little globe button, and then I can click Start Flow, and then I can just talk.
[01:24:38] Brandon Hancock: And I'll literally just sit there and say, like, here's where we're at, here's where we're trying to go, here's the gap, here's what success looks like, and I just blurt it out.
[01:24:46] Brandon Hancock: ▶ Here's the, and I usually will also tell it, if you're reading a book or a podcast or something, I'll tell it the source of inspiration, because the second you can give it the source of inspiration, it has more context automatically, you know?
[01:24:57] Brandon Hancock: So that's, that's usually how I go about So
[01:25:01] Hemal Shah: So that was one for whisper flow, by the way, always plus one for whisper flow.
[01:25:07] Hemal Shah: Yeah.
[01:25:08] Hemal Shah: Is it, is that two way communication though, where there is a follow up questions and then you continue just one way you, you speak it out and then broad will go off and that's it basically.
[01:25:21] Brandon Hancock: No, no, it's a hundred percent two way.
[01:25:22] Brandon Hancock: Yes.
[01:25:22] Brandon Hancock: I mean, you say like, here's what I want.
[01:25:24] Brandon Hancock: If you come up with a plan before you do it, like I always tell it to like, do the task template.
[01:25:29] Brandon Hancock: Part like, cause you're using, if you're using the ship kit templates, I'm like, look at the task template, create a new task template and follow the instructions.
[01:25:37] Brandon Hancock: You have to be a little bit more precise in knowing what's at your fingertips.
[01:25:41] Brandon Hancock: And then I'm like, oh, okay, I'll make the task template.
[01:25:44] Brandon Hancock: Oh, the task template says there's three follow up steps to where I can proceed with the build.
[01:25:49] Brandon Hancock: You can clarify what's going to happen or provide feedback.
[01:25:53] Brandon Hancock: It'll hit those off before, you know, before coding.
[01:25:57] Brandon Hancock: So it opens up to a conversation, but now.
[01:26:00] Brandon Hancock: 99% of the time, it's just a throwaway idea anyway, so I'm just like, da-da-da-da-da, and I just let it rip, and I'll come back to it when I want to work on it later, which is just, and then I have it on my desktop when I get home, I just open up Claude, and then I open up the code part, and then it has a branch ready, and I just pull that branch down to my local machine, I make sure it saved everything, like I made sure it fully saved that new task template, and then I'm ready to go on my actual computer.
[01:26:26] Hemal Shah: Prakrit, So the response that you get from Claude about some clarification, that is not in voice, right?
[01:26:33] Hemal Shah: If I'm driving or something, that is in text, right?
[01:26:37] Hemal Shah: That's the only thing I want to define.
[01:26:38] Hemal Shah: Prakrit, there's no two-way communication using Claude Code section within the app, right?
[01:26:45] Hemal Shah: That was one thing I wanted to confirm.
[01:26:48] Hemal Shah: Prakrit, I have not seen that.
[01:26:50] Brandon Hancock: Patrick, I know you do a lot of coding while driving.
[01:26:53] Brandon Hancock: Any tips or tricks?
[01:26:55] Patrick Chouinard: Prakrit, Not really coding while driving, ideating while driving.
[01:26:58] Patrick Chouinard: Basically, I-
[01:27:00] Patrick Chouinard: I have configured...
[01:27:02] Brandon Hancock: sure the officer will understand the difference whenever you get pulled over.
[01:27:06] Patrick Chouinard: Oh, no phone in hand.
[01:27:07] Brandon Hancock: Bluetooth only.
[01:27:10] Patrick Chouinard: Bluetooth only all the time.
[01:27:13] Patrick Chouinard: ▶ But the idea is I talk with ChatGPT at the length about something, and whenever it actually gets to the point where we've talked about everything, I just tell it, like, now compile that into a PRD.
[01:27:32] Patrick Chouinard: And I used to give it directly to Claude, but now I have an intermediate step.
[01:27:38] Patrick Chouinard: I give it to Claude Cowork, which is now my designer.
[01:27:43] Patrick Chouinard: And Cowork has skills and memory, because I created what I call CowoRoOS [tool:CoworkOS].
[01:27:50] Patrick Chouinard: So basically all of my discussions are within one big co-work environment with memory, with personality, with everything set up.
[01:27:59] Patrick Chouinard: So basically...
[01:28:00] Patrick Chouinard: Basically, I drop the PRD there, and it knows how to parse it, split it, make it in a bunch of feature size, and it knows that it will hand it off to Claude Code.
[01:28:13] Patrick Chouinard: So it is aware that it is a designer, it will not actually do the code, and it gives me a package that I can just drop into a folder, either brownfield or greenfield, and say, Claude, like, go, have fun.
[01:28:27] Hemal Shah: Have you connected your ChatGPT with Cowork, where you're just driving, you generate the PRD, and then you can send it over to Cowork?
[01:28:36] Patrick Chouinard: I haven't seen any way to do that, right?
[01:28:39] Patrick Chouinard: That's the big thing that's missing.
[01:28:42] Patrick Chouinard: ▶ It's that ChatGPT or OpenAI have the best voice model there is right now, and Claude has the absolute best development model, and they don't talk to each other.
[01:28:54] Patrick Chouinard: The first time I'm actually able to get Claude to talk the way ChatGPT does...
[01:29:02] Patrick Chouinard: Github's going to have an issue with them about the repo I'm going to send their way.
[01:29:07] Hemal Shah: Yeah.
[01:29:07] Hemal Shah: My last question is, I was going a little bit deeper into OpenClaude, but then all the advancement in Cloud Cowork and Claude Cowork Dispatch and channels and everything, I'm just wondering if I wait a little longer, mean, Cloud Cowork will be a great competitor to...
[01:29:24] Hemal Shah: Well, now has the ability to connect to a Discord channel or a Telegram.
[01:29:30] Hemal Shah: Yeah.
[01:29:31] Patrick Chouinard: I mean, you're basically at the level where it does everything OpenClaude does.
[01:29:36] Patrick Chouinard: The only thing it doesn't do yet are things that are so unsecure that it should not do it anyway.
[01:29:43] Hemal Shah: So, yeah, OpenClaude has more possibility, but it's like, it can't send a nuclear bomb yet.
[01:29:49] Patrick Chouinard: Yeah, I don't really want it to be able to do that.
[01:29:52] Hemal Shah: Sounds good.
[01:29:53] Hemal Shah: Okay.
[01:29:54] Hemal Shah: Thank you.
[01:29:56] Brandon Hancock: All right.
[01:29:57] Brandon Hancock: Cool, guys.
[01:29:57] Brandon Hancock: We'll keep on cruising.
[01:29:59] Brandon Hancock: I...
<!--SEGMENT
topic: Jake — pulled-the-wrong-branch lesson + ShipKit task template saves the day
speakers: Jake Maymar, Brandon Hancock
keywords: five-repos-into-one consolidation, live-coding-during-code-freeze, deterministic + probabilistic mixed output, subject-matter-expert review, branch-not-main pull mistake, exhausting exponential pace, ShipKit task template, Session Buddy tab manager
summary: Jake landed the major investor pitch — but only after a near-miss when subject matter experts said his consolidation was missing knowledge bases. Cause: he'd pulled main on five repos but one team was experimenting on a branch. Lesson: verify everything when moving at exponential pace. Brandon agrees the constant-success grind has eliminated the brain-decompress 'filler' phase that used to exist between hard-thinking 20-minute windows. Jake mentions Session Buddy — saves all your tabs with metadata when you have too many to track.
-->

[01:30:00] Brandon Hancock: I think it goes Jake, then Morgan, then Scott.
[01:30:05] Jake Maymar: Good seeing you, Brandon.
[01:30:08] Brandon Hancock: Likewise, man.
[01:30:09] Brandon Hancock: Always happy to see some familiar faces.
[01:30:12] Jake Maymar: Yeah, so I learned a powerful lesson.
[01:30:17] Jake Maymar: I've kind of been like almost, I don't know, submerged with so many different things.
[01:30:26] Jake Maymar: It's amazing.
[01:30:28] Jake Maymar: And I've kind of built a whole bunch of different teams.
[01:30:31] Jake Maymar: Like, if you use AI, then basically I'm going to build with you.
[01:30:36] Jake Maymar: Yeah, yeah.
[01:30:37] Jake Maymar: And, you know, because, you know, there's a whole bunch of teams where they're not using AI at all.
[01:30:41] Brandon Hancock: And there's a lot of sort of education and ramp up and all that other stuff.
[01:30:45] Brandon Hancock: Yeah.
[01:30:46] Jake Maymar: But this is a really powerful lesson I learned.
[01:30:48] Jake Maymar: So we had a major pitch and everyone's using AI and everyone's moving very, very, very fast, right?
[01:30:57] Jake Maymar: So we're all doing many,
[01:31:00] Jake Maymar: Many, um, terminals, all those different things, um, and several different Githubs, and it was my job to basically take all of the repos and combine them into one, uh, and basically, uh, put a scaffolding around everything, um, and the thing I learned, I was able to do that no problem, that worked no problem, but the thing I learned, which I thought was really powerful, was, um, Be able to understand if the agentic flows are producing the correct output, and what I mean by that is it was really, really, really, really complex output, and I thought I was nailing it.
[01:31:46] Jake Maymar: I just thought I was totally, totally nailing it.
[01:31:49] Jake Maymar: Um, and then when I got it in front of the subject matter experts, they're like, no, this is, this is like missing, because we had a combination of probabilistic and deterministic things.
[01:32:00] Jake Maymar: And it's like, oh, this is missing, like, this knowledge base, and this, and this, and this, and this, this, and I was kind of devastated, and I went back, and I, like, looked through everything, and I, like, checked everything, and went back, and then slept on it, then woke up, and was like, oh, wait a second, all I had to do, and this is a dumb thing, but all I had to do, I just hadn't pulled the right branch.
[01:32:28] Jake Maymar: ▶ They weren't working on main, so they were experimenting with all these different things, and we were moving so fast that one of the branches I hadn't pulled, and so there's, like, five different repos, almost all of them were in main, but this one wasn't main, it was actually a different.
[01:32:48] Jake Maymar: ▶ Yeah, and it affects everything, in effect, it affected the entire thing, so I learned a super powerful lesson when you're moving that fast, just kind of verify everything, but, yeah, so we
[01:33:00] Jake Maymar: We landed the deal.
[01:33:01] Jake Maymar: was pretty awesome.
[01:33:01] Brandon Hancock: awesome.
[01:33:03] Brandon Hancock: That's awesome.
[01:33:03] Brandon Hancock: Hey, I'm glad it all worked out.
[01:33:05] Brandon Hancock: But I mean, I understand exactly where you're coming from of like, there's so many more room.
[01:33:11] Brandon Hancock: There's so much more room now to like, wait, did I just like, I think I kept up with it all.
[01:33:17] Brandon Hancock: Like, like, because there's so much happening.
[01:33:20] Jake Maymar: Well, there was a thing and I was, I was, I was, you know, basically ship kit, right?
[01:33:24] Jake Maymar: My template, the task template has saved my butt so many times [tool:ShipKit task template].
[01:33:29] Brandon Hancock: mean, that ship kit is awesome.
[01:33:31] Jake Maymar: I heavily modified it, but man, that ship's awesome.
[01:33:35] Jake Maymar: And so, but that was the thing.
[01:33:38] Jake Maymar: They're live working on theirs.
[01:33:41] Jake Maymar: And so I'm built, I'm, I mean, I, and this shouldn't be like, you know, but obviously like they're, they're pulling in all their different things.
[01:33:48] Brandon Hancock: They're live working on all their different things.
[01:33:50] Brandon Hancock: Yeah.
[01:33:50] Jake Maymar: And I'm pulling in all those systems into one and then testing.
[01:33:53] Jake Maymar: And it has to be, you really don't know the output until everything is all assembled.
[01:33:59] Brandon Hancock: Yeah.
[01:34:00] Jake Maymar: And, and so, yeah, so that was, that was a really interesting thing.
[01:34:04] Jake Maymar: But yeah, anyway.
[01:34:06] Brandon Hancock: Now, I, it's crazy with, I was actually talking to this today with someone, but like, I'm working more and harder than I've ever done, because at every point, like in the past, I used to make one big idea, and I would work on it for like three to four hours to bring it to life.
[01:34:25] Brandon Hancock: But all the hard thinking happened in this 20 minute window.
[01:34:28] Brandon Hancock: ▶ And then the other part was just filler of bringing it to life.
[01:34:31] Brandon Hancock: But now, that, that hard part doesn't exist, or the filler doesn't exist anymore, where my brain got to decompress.
[01:34:39] Brandon Hancock: Yeah.
[01:34:39] Brandon Hancock: It's just, what's the hardest problem?
[01:34:41] Brandon Hancock: Because Claude's just going to throw the hard stuff at me over and over and over again.
[01:34:44] Brandon Hancock: And it's just hopping from thing to thing to thing to thing.
[01:34:46] Brandon Hancock: Like, it's, it's brutal.
[01:34:49] Jake Maymar: Yeah, it really isn't.
[01:34:51] Jake Maymar: And that's the thing is, I think, I think, it's important to know that we're doing exponential after exponential after exponential and solving like...
[01:35:00] Jake Maymar: really, really, really hard problems quickly.
[01:35:04] Brandon Hancock: And you're right, there's no downtime, right?
[01:35:07] Jake Maymar: And so, and it's even, you know, you know, just imagine working, like, I'm sure you're already working with, like, five Brandons or 10 Brandons, and if you're all moving at that speed, and that's the thing, that's kind of what I love about these groups of people, is everyone's moving at that speed already, but it's exhausting.
[01:35:28] Jake Maymar: Like, it's just crazy.
[01:35:29] Jake Maymar: I, um, I feel like we can accomplish, what we were able to accomplish in two weeks, I think would have taken us, like, five years.
[01:35:37] Brandon Hancock: Like, easily.
[01:35:38] Brandon Hancock: Easily.
[01:35:39] Jake Maymar: And again, that's like, that's just like Tuesday.
[01:35:43] Elijah Stambaugh: I just want to say amen.
[01:35:45] Jake Maymar: Sorry, I don't know.
[01:35:47] Brandon Hancock: Amen.
<!--SEGMENT
topic: Brandon — Accelerando book + agents-talking-to-agents future
speakers: Brandon Hancock, Jake Maymar, Scott Rippey
keywords: Accelerando audiobook, three-generation singularity narrative, deconstructing planets for compute, Elon Musk following Accelerando, audiobook required (terminology dense), Claude Million-context-window in Claude Code (Opus only), Codex 5.4 better than Bard for backend, Apple Vision Pro alternative
summary: Brandon evangelizes Accelerando — three-generation family across the singularity, deconstructing-planets-for-compute end state, Elon's actions track the manual. Audiobook required because the terminology blizzard breaks reading flow. Quick aside: Claude Million-context window is Opus-only in Claude Code; once you switch you can't get the old session back. Codex 5.4 has become Scott's preferred backend over Bard.
-->

[01:35:48] Brandon Hancock: No, but seriously, it is, it is, it is unreal.
[01:35:51] Brandon Hancock: If y'all, I talked about this book last time.
[01:35:54] Brandon Hancock: I, I please, please, please, it's the nerdiest book you're ever going to read.
[01:35:59] Brandon Hancock: In your life.
[01:36:00] Brandon Hancock: Nice.
[01:36:01] Brandon Hancock: Accelerando [tool:Accelerando].
[01:36:02] Brandon Hancock: But, wait, let me find it real fast.
[01:36:04] Scott Rippey: I still have it on my screen to buy.
[01:36:06] Jake Maymar: I know, me too.
[01:36:08] Jake Maymar: I have, oh, but I found this great tool if anyone wants it.
[01:36:14] Jake Maymar: I mean, you probably don't need it, but Session Buddy, I love Session Buddy [tool:Session Buddy].
[01:36:19] Brandon Hancock: What's that?
[01:36:20] Jake Maymar: Okay, you know how, Brandon, I have way too many tabs.
[01:36:23] Jake Maymar: I have like, I have so many tabs that it stopped working, right?
[01:36:28] Jake Maymar: So, Session Buddy, what it does, I'll just put the link in the chat.
[01:36:31] Jake Maymar: What this does is, if you're kind of lazy like me and you have tons and tons and tons of tabs running, you can just basically log into Session Buddy and it just grabs all the tabs and you can basically write any information you want to it, any sort of metadata, and then that's it, you're done.
[01:36:52] Jake Maymar: So, you can go back to that.
[01:36:54] Jake Maymar: can basically add notes to any of the things.
[01:36:58] Jake Maymar: It's just really, really nice.
[01:36:59] Jake Maymar: Don't
[01:37:00] Jake Maymar: If you have a lot of tabs, it's just a really nice tool.
[01:37:05] Brandon Hancock: Okay.
[01:37:06] Brandon Hancock: Okay.
[01:37:07] Brandon Hancock: No, please drop it.
[01:37:08] Brandon Hancock: I'd love to check that one out.
[01:37:11] Brandon Hancock: The last thing, just please, if you guys get a chance, just listen to the first two parts of the book.
[01:37:17] Brandon Hancock: So it's like three books merged into one where you follow one family, a dad, his daughter, and grandson going through the singularity.
[01:37:27] Brandon Hancock: And the thing that's crazy is the rate of change just, it never stops.
[01:37:33] Brandon Hancock: It only keeps getting faster because, like, eventually you end up to where the only thing that really matters is compute and power.
[01:37:40] Brandon Hancock: Like, that is what the universe turns into.
[01:37:42] Brandon Hancock: And, like, you're deconstructing planets.
[01:37:44] Brandon Hancock: Like, everything Elon Musk is doing, he's literally just following this as a manual.
[01:37:48] Brandon Hancock: ▶ Like, this is the manual for what happens over the next, like, 50, 60 years.
[01:37:53] Brandon Hancock: So if you get a chance, please, please, please read it.
[01:37:55] Brandon Hancock: It's the nerdiest book to start off.
[01:37:57] Brandon Hancock: Like, when it's like, it just makes up terms.
[01:37:59] Brandon Hancock: Yes.
[01:37:59] Brandon Hancock: ▶ I
[01:38:00] Brandon Hancock: Definitely recommend getting the audiobook, the actual read, it's too hard, you'll get caught up on like, wait, what the hell you said?
[01:38:05] Brandon Hancock: So at least the audiobook forces you to go fast.
[01:38:08] Brandon Hancock: But it is one of the coolest reads that I've ever done.
[01:38:11] Brandon Hancock: I'm in the last like hour and a half and I'm so sad.
[01:38:16] Brandon Hancock: I mean, like, they live, but like, it is, it's not the like happiest ending, but I'm not fully there yet.
[01:38:25] Brandon Hancock: But, uh, but it's, it is, um, yeah, that's what I'm saying.
[01:38:29] Brandon Hancock: Like, I would, I almost like want have a book club on this one, just to go through each chapter, because the ideas it introduces is unreal.
[01:38:37] Brandon Hancock: Um, yeah, I mean, I mean, by the end of it, like, once again, Neuralink, they talk about it in this book.
[01:38:43] Brandon Hancock: Obviously, it's a different thing, but like, it's all happening.
[01:38:46] Brandon Hancock: Um, yeah, if you get a chance, please, please read it.
[01:38:49] Brandon Hancock: We'd love to nerd out with you guys.
[01:38:52] Jake Maymar: That's really, um, okay, cool.
[01:38:55] Brandon Hancock: Jake, anybody, one, one last question.
[01:38:57] Jake Maymar: Um, this one's, I'm sure.
[01:38:59] Jake Maymar: I'm hurt.
[01:38:59] Jake Maymar: Bye.
[01:39:00] Jake Maymar: I'm just catching up.
[01:39:01] Jake Maymar: Like, I'm just kind of coming up from air.
[01:39:03] Jake Maymar: Are you using the Claude Million Context window, or it's a, yeah, no question.
[01:39:13] Brandon Hancock: Yeah, I'm always using it.
[01:39:14] Jake Maymar: Like in Claude Code, right?
[01:39:16] Jake Maymar: Yeah, in Claude Code.
[01:39:17] Scott Rippey: Well, the other one goes away.
[01:39:18] Scott Rippey: If you switch to it, it's gone.
[01:39:19] Scott Rippey: You have to, I think.
[01:39:21] Brandon Hancock: Mm-hmm.
[01:39:22] Jake Maymar: Oh, I see.
[01:39:23] Brandon Hancock: So it's either, are you using Opus or Sonnet?
[01:39:25] Brandon Hancock: ▶ And I'm using Opus is really the choice at this point.
[01:39:28] Jake Maymar: Yeah, I'm using Opus for this.
[01:39:31] Jake Maymar: So Opus is only Million Context window at this point.
[01:39:34] Brandon Hancock: Yes.
[01:39:35] Brandon Hancock: Mm-hmm.
[01:39:36] Jake Maymar: Okay.
[01:39:36] Brandon Hancock: Which is nice.
[01:39:37] Brandon Hancock: Which is very nice.
[01:39:38] Scott Rippey: Less compactions.
[01:39:39] Scott Rippey: It's funny.
[01:39:39] Scott Rippey: It keeps you on the old one, though.
[01:39:40] Scott Rippey: Like, until you actually go in there and look.
[01:39:42] Scott Rippey: At least it did for me for a while.
[01:39:43] Scott Rippey: And then, boop, switched to it.
[01:39:45] Scott Rippey: Gone.
[01:39:46] Scott Rippey: Can't get to the old one.
[01:39:48] Jake Maymar: Oh, interesting.
[01:39:49] Jake Maymar: Very, very interesting.
[01:39:50] Jake Maymar: Hmm.
[01:39:52] Jake Maymar: Nope.
[01:39:52] Jake Maymar: That's it.
[01:39:53] Brandon Hancock: That's all I got.
[01:39:54] Brandon Hancock: Okay.
[01:39:55] Brandon Hancock: Cool.
[01:39:55] Brandon Hancock: All right.
[01:39:56] Brandon Hancock: I think next up, going back to our picture, I think it was Morgan and Scott.
[01:39:59] Morgan Cook: Right.
[01:40:00] Morgan Cook: I'm just catching up.
[01:40:01] Morgan Cook: Like, I'm just kind of coming up from air.
[01:40:03] Morgan Cook: Are you using the Claude Million Context window, or it's a, yeah, no question.
[01:40:13] Morgan Cook: Yeah, I'm always using it.
[01:40:14] Brandon Hancock: Like in Claude Code, right?
[01:40:16] Brandon Hancock: Yeah, in Claude Code.
[01:40:17] Brandon Hancock: Well, the other one goes away.
[01:40:18] Brandon Hancock: If you switch to it, it's gone.
[01:40:19] Morgan Cook: You have to, I think.
[01:40:21] Morgan Cook: Mm-hmm.
[01:40:22] Morgan Cook: Oh, I see.
[01:40:23] Morgan Cook: So it's either, are you using Opus or Sonnet?
[01:40:25] Morgan Cook: And I'm using Opus is really the choice at this point.
[01:40:28] Brandon Hancock: Yeah, I'm using Opus for this.
[01:40:31] Morgan Cook: So Opus is only Million Context window at this point.
[01:40:34] Morgan Cook: Yes.
[01:40:35] Morgan Cook: Mm-hmm.
[01:40:36] Morgan Cook: Okay.
[01:40:36] Morgan Cook: Which is nice.
[01:40:37] Morgan Cook: Which is very nice.
[01:40:38] Morgan Cook: Less compactions.
[01:40:39] Morgan Cook: It's funny.
[01:40:39] Morgan Cook: It keeps you on the old one, though.
[01:40:40] Morgan Cook: Like, until you actually go in there and look.
[01:40:42] Morgan Cook: At least it did for me for a while.
[01:40:43] Morgan Cook: And then, boop, switched to it.
[01:40:45] Morgan Cook: Gone.
[01:40:46] Morgan Cook: Can't get to the old one.
[01:40:48] Morgan Cook: Oh, interesting.
[01:40:49] Morgan Cook: Very, very interesting.
[01:40:50] Morgan Cook: Hmm.
[01:40:52] Morgan Cook: Nope.
[01:40:52] Morgan Cook: That's it.
[01:40:53] Morgan Cook: That's all I got.
[01:40:54] Morgan Cook: Okay.
[01:40:55] Morgan Cook: Cool.
[01:40:55] Morgan Cook: All right.
<!--SEGMENT
topic: Morgan — Heritage Plot government data block + Brandon's free-license outreach tactic
speakers: Morgan Cook, Brandon Hancock, Jake Maymar
keywords: 687 Utah cemeteries database, GRAMA officer non-compliance, network-Nazi DOD-style request chain, lumpy-mail outreach for direct call to action, free-license-to-3 acquisition pattern, age-of-director scrape, $1500/month per cemetery price floor, three-for-almost-free + 3-at-50%-off + full-price progression
summary: Morgan's Heritage Plot project is blocked: county GRAMA officer won't respond despite calling the project urgent. Brandon's been there ('network Nazis' = DOD slow-roll). Tactical pivots: Morgan now has all 687 Utah cemeteries' contact info via a marketing hire. Brandon recommends free-license-to-3-customers + 3-at-50%-off + full-price progression to get past the trust gap. Add LinkedIn age-of-director scrape — under 40 is more likely to engage. Lumpy mail with the director's title gets past the gatekeeper. Morgan estimates $1500/month/cemetery floor.
-->

[01:40:56] Morgan Cook: I think next up, going back to our picture, I think it was Morgan and Scott.
[01:40:59] Morgan Cook: Right.
[01:41:01] Morgan Cook: Hey guys, how's everybody doing?
[01:41:03] Morgan Cook: Glad to be here.
[01:41:04] Morgan Cook: pretty good.
[01:41:05] Morgan Cook: And good to see you, Brandon.
[01:41:07] Morgan Cook: What fun things have we been up to?
[01:41:10] Morgan Cook: Well, have one of the projects I'm working on is I'm under a DNA, so I can't really discuss much of that, but it's going pretty good.
[01:41:19] Morgan Cook: Safe space, man.
[01:41:19] Morgan Cook: Secret safe with us.
[01:41:22] Brandon Hancock: Well, the thing is, it's like, okay, well, I have a DNA with you, but the tools I'm using are from these people who I need to discuss things with.
[01:41:33] Brandon Hancock: Anyway, so that project's going pretty good, and I'm probably about three-quarters of the way done with that one.
[01:41:40] Brandon Hancock: On the Heritage Cemetery project, my problem there right now is actually trying to get information out of a government-based employee structure.
[01:41:54] Brandon Hancock: It's like, these people are just so lazy and non-responsive, and it's like...
[01:41:59] Brandon Hancock: like...
[01:42:00] Brandon Hancock: They ask for stuff that they want, but then when you try to get information from them, it seems like it's a one-way street.
[01:42:08] Morgan Cook: So I'm just really fighting with trying to get them to communicate a little bit clearer about providing me the information I need.
[01:42:16] Morgan Cook: And part of it is their, I think their IT department is, I call them network Nazis.
[01:42:23] Morgan Cook: Network Nazis.
[01:42:24] Morgan Cook: It's so funny.
[01:42:25] Morgan Cook: ▶ So I literally used to work and we like half, the majority of the day, we're just trying to talk to the DOD, like the Air Force.
[01:42:31] Brandon Hancock: And like, my God, you want to talk about pulling teeth.
[01:42:35] Brandon Hancock: It was a request would go to a request, which would go like up six requests.
[01:42:40] Brandon Hancock: would end on someone's desk, manually printed out, have to go across to another building, sit on their desk, and then go all the way back down the chain.
[01:42:46] Brandon Hancock: was like, you couldn't design a more painful process if you tried.
[01:42:51] Brandon Hancock: So, I mean, half the time, it's literally not even a person's fault.
[01:42:54] Morgan Cook: It's just like the actual systems in place make things go slow.
[01:42:59] Brandon Hancock: So, I- So,
[01:43:00] Brandon Hancock: I feel your pain, dude.
[01:43:00] Brandon Hancock: It was like, I literally might as well not come to work for three weeks.
[01:43:04] Brandon Hancock: I'll wait for the response instead, you know?
[01:43:07] Morgan Cook: So, especially when you're trying to move fast.
[01:43:09] Morgan Cook: So, I feel you on that, So, since we last talked, or I've showed the product with the group last week and the week before a little bit.
[01:43:18] Morgan Cook: I do have a list now of all of the cemeteries in Utah, and I have a marketing guy that's going to start working on contacting all of them.
[01:43:28] Morgan Cook: So, I took your advice on that one to, you know, really start pushing the marketing.
[01:43:33] Morgan Cook: Oh, wait, what are we talking about?
[01:43:34] Morgan Cook: I was like, wait, I got confused.
[01:43:36] Morgan Cook: Yes, where are things at on that?
[01:43:39] Morgan Cook: From a software side, from a customer one side?
[01:43:42] Morgan Cook: Where, can you hit me with a recap?
[01:43:43] Brandon Hancock: Because I'm still excited.
[01:43:45] Brandon Hancock: one is the problem.
[01:43:47] Brandon Hancock: They're not responding.
[01:43:49] Brandon Hancock: But I thought they were not compliant.
[01:43:52] Brandon Hancock: They're not compliant.
[01:43:53] Brandon Hancock: That's the thing.
[01:43:54] Brandon Hancock: It's like, you guys are the ones who need this, and you're not helping me get it to you.
[01:43:59] Brandon Hancock: Do I need to make a call?
[01:44:00] Brandon Hancock: ▶ Call to the compliance officer to help light a fire under them.
[01:44:03] Brandon Hancock: You give me the number, man.
[01:44:04] Brandon Hancock: Anonymous tip.
[01:44:06] Brandon Hancock: Hey, these people are not in compliance and, yeah.
[01:44:11] Brandon Hancock: Anyways, so yeah, it's a, you know, the worst part of that is my, my...
[01:44:16] Brandon Hancock: I have a brother who works there.
[01:44:18] Brandon Hancock: It's like, he's the one who's supposed to...
[01:44:20] Brandon Hancock: That's awkward.
[01:44:21] Brandon Hancock: Come call me.
[01:44:25] Morgan Cook: So, it's just, it's just a, a difficult thing trying to get the information out of and when they came to me, it was like, they're the ones who came to me, right?
[01:44:34] Morgan Cook: And it was like, uh, at that point, it seemed like it was a very urgent thing.
[01:44:39] Morgan Cook: And it's like, okay, well, what happened to the urgency?
[01:44:41] Morgan Cook: You guys aren't, aren't, uh, providing...
[01:44:45] Morgan Cook: Morgan, out of curiosity, is there something, is there anything preventing you picking up three other clients and basically saying like, hey, you helped me build this.
[01:44:52] Morgan Cook: ▶ I'll literally let you use this for free for two years or something crazy.
[01:44:57] Morgan Cook: I know you're not compliant.
[01:44:58] Morgan Cook: You know, I know, we both...
[01:44:59] Morgan Cook: both...
[01:45:00] Morgan Cook: No, you're not compliant, and you're one anonymous tip, which I'm not afraid to do, away from getting sued for millions, you know, so it's like, you need this, I already have stuff built, would you mind being a part of my beta users, I want to give you the sweetheart deal, all I ask for is over the next three months, just a call once a week for 30 minutes, I need it for one month, just to get you on the same page, but just to, so you're not stuck by them.
[01:45:25] Brandon Hancock: Yeah, exactly.
[01:45:27] Brandon Hancock: I do have, that's what I was saying, so I did obtain a list of all 687 cemeteries that are in the state, and all of their contact info, their actual GIS, it's not the entire Plod info, it's just the cemetery location, right?
[01:45:46] Morgan Cook: So I do have all that info.
[01:45:49] Morgan Cook: I do not have the piece, which is not necessarily part of the cemeteries most of the time, it's usually part of the police force, and that's the...
[01:46:00] Morgan Cook: Uh, the grandma, uh, officer, the officer who's in charge of approving or disproving the, the GRAMA request that, that their, the compliance issue.
[01:46:12] Brandon Hancock: ▶ So real fast, Morgan, the one thing to always look at is the cost to acquire a customer.
[01:46:18] Brandon Hancock: Yeah.
[01:46:19] Brandon Hancock: So even if it costs you a hundred, a thousand, $3,000 to get one of these guys, like it's the, on the other side of that is, I don't know how the, how big the contract would be per year, almost indefinitely.
[01:46:35] Brandon Hancock: It's like, okay.
[01:46:37] Brandon Hancock: Like, even if I, I mean, the numbers are crazy.
[01:46:39] Brandon Hancock: I'm, assuming contracts probably what, like 5,000 to, I don't have no idea.
[01:46:42] Brandon Hancock: What would a contract be per year?
[01:46:43] Brandon Hancock: If you just had a ball market?
[01:46:45] Brandon Hancock: I'm not sure exactly what it is at this point yet either, because that was the other piece I needed to figure out.
[01:46:50] Brandon Hancock: So I have the list of all the cemeteries.
[01:46:53] Brandon Hancock: I don't know what their, uh, annual budgets are yet.
[01:46:56] Brandon Hancock: And that's one of the things the marketing guy is actually going to be working on is trying to identify identify.
[01:47:00] Brandon Hancock: I, what is the budget that they have for any of this stuff in the first place?
[01:47:03] Brandon Hancock: And then...
[01:47:04] Brandon Hancock: guarantee you it's more than a hundred dollars a month.
[01:47:07] Morgan Cook: Oh, absolutely.
[01:47:08] Morgan Cook: So that's what I'm thinking, a minimum is going to be like fifteen hundred or somewhere around there.
[01:47:12] Brandon Hancock: Yeah.
[01:47:13] Morgan Cook: So that's what I'm saying.
[01:47:14] Morgan Cook: It's like, man, I, even today, and it's like, I'm like, obviously this is, this is your money.
[01:47:20] Morgan Cook: So it's much easier for me to talk.
[01:47:22] Morgan Cook: Uh, but like, it is, it is so, I, I could see starting to send items to these people.
[01:47:29] Morgan Cook: Like, Hey, I'm just going to go ahead.
[01:47:31] Morgan Cook: Here's a thousand dollars that I'm going to go ahead and start figuring out what I can do.
[01:47:35] Brandon Hancock: Can I send lumpy mail?
[01:47:37] Brandon Hancock: Like, can I go ahead and actually send something that has like a direct call to action?
[01:47:42] Brandon Hancock: Like, Hey, I'm more, you know, there's so many things that you can do to just be different than anyone else that's reaching out to them.
[01:47:48] Brandon Hancock: ▶ And because it's the biggest problem is that you didn't know who was on the inside that was approving the decision.
[01:47:53] Brandon Hancock: So it's like, all you have to do is send in lumpy mail.
[01:47:56] Brandon Hancock: And I call out the title.
[01:47:59] Brandon Hancock: Sure.
[01:48:00] Brandon Hancock: And then it will literally go on their desk.
[01:48:02] Brandon Hancock: So it's worth paying the 20 bucks, 30 bucks, maybe sitting out.
[01:48:06] Brandon Hancock: I do have the director's name of each cemetery now.
[01:48:09] Brandon Hancock: Okay.
[01:48:10] Brandon Hancock: I do have all that info.
[01:48:12] Brandon Hancock: Okay.
[01:48:13] Brandon Hancock: So that's kind of where I'm at with that.
[01:48:15] Brandon Hancock: I kind of, I hit the brick wall.
[01:48:18] Brandon Hancock: I've been sitting on it for two weeks now, and I got to get past it with some other method of communication.
[01:48:26] Brandon Hancock: And maybe, like you said, give a couple of free licenses out to whoever wants to jump on board and help get it, you know, laid out.
[01:48:37] Brandon Hancock: ▶ And the cool part is like, just like, I mean, I've heard this rule literally back in like college, but it's like three for almost free, you know, like make it, have some skin in the game.
[01:48:48] Brandon Hancock: So they actually care, but almost free.
[01:48:51] Brandon Hancock: Then three at like a 50% discount, and then the next are pretty much full, but because the biggest thing is no one trusts you right now.
[01:48:58] Brandon Hancock: Because Because you...
[01:49:00] Brandon Hancock: And that's just what happens with every software product.
[01:49:02] Brandon Hancock: No one knows you.
[01:49:02] Brandon Hancock: No one can trust you.
[01:49:04] Brandon Hancock: That's literally what we're doing.
[01:49:05] Brandon Hancock: It basically was for almost free.
[01:49:08] Morgan Cook: Then we gave a stupid discount and now we're charging full price.
[01:49:11] Morgan Cook: That's, that's literally what we're, the exact playbook I'm telling you is what we're following too.
[01:49:16] Morgan Cook: And just because someone has to be the guinea pig to try it out.
[01:49:21] Morgan Cook: So it's finding that early adopter is the hardest one.
[01:49:24] Morgan Cook: That's the first one is going to be the hardest one.
[01:49:27] Brandon Hancock: Especially in that industry.
[01:49:28] Morgan Cook: I don't know how many like, young upcoming guys are like, oh, I'm happy to like, talk software.
[01:49:34] Morgan Cook: ▶ So if you could also have an age attached to each one of the directors, that might be worth the LinkedIn scrape.
[01:49:40] Morgan Cook: Just to like, if someone's above 65, like, I would not, they most likely are not going to be the one that are like interested in talking software and AI, you know?
[01:49:51] Morgan Cook: Right.
[01:49:51] Morgan Cook: Yeah.
[01:49:52] Morgan Cook: But the guy who inherited it from his dad, who's now 30, he probably is happy to talk with you.
[01:49:58] Morgan Cook: So I mean, just being a, a, a,
[01:50:00] Morgan Cook: A ageist on that, finding that first early adopter.
[01:50:03] Morgan Cook: If I was in your shoes, that's how I would be playing it, if possible.
[01:50:08] Morgan Cook: Cool.
[01:50:09] Morgan Cook: All right.
<!--SEGMENT
topic: Fieldly v3 + Limitless going away + Plod desktop + supersonic mic
speakers: Morgan Cook, Brandon Hancock, Patrick Chouinard, Ty Wells
keywords: Fieldly v3 onboarding pain (Apple-only billing, three tiers), Limitless Meta acquisition + September 25 deadline, Plod pin button-driven recording + desktop app for kicked-out note-takers, Fieldly supersonic mic transcribing whispers from another room, $180 + monthly subscription pricing
summary: Fieldly v3 onboarding is rough (Apple-only billing, three tiers, only the unlimited one worth it). Limitless is going away in September after Meta acquired them — Ty stops investing in the platform. Brandon switched to Plod for its button-driven recording and desktop app, which records desktop audio and bypasses kicked-out Fathom note-takers in client meetings. Patrick has both Fieldly and Plod — for live in-person meetings Plod wins, for ambient context-gathering Fieldly's mic catches conversations in the next room ('supersonic'). Fieldly hardware ~$180 + tiered subscription.
-->

[01:50:09] Morgan Cook: Well, that's all I really have.
[01:50:10] Brandon Hancock: I don't have any questions of technology that I need.
[01:50:13] Morgan Cook: I did have a, I did get, I get a, I got a Fieldly.
[01:50:21] Morgan Cook: What is it?
[01:50:21] Brandon Hancock: Is it a Limitless or what'd you get?
[01:50:23] Morgan Cook: No, the Fieldly, the little tiny.
[01:50:25] Morgan Cook: Oh, Fieldly.
[01:50:26] Morgan Cook: How do you like it?
[01:50:27] Morgan Cook: Out of curiosity.
[01:50:28] Morgan Cook: You know what?
[01:50:29] Brandon Hancock: ▶ Their onboarding really sucked.
[01:50:31] Brandon Hancock: Really?
[01:50:32] Morgan Cook: It was difficult.
[01:50:35] Brandon Hancock: Like, the app installed, I couldn't get it to sync.
[01:50:38] Brandon Hancock: I had to reset all of my freaking antennas to get the Bluetooth to sync and reset.
[01:50:44] Brandon Hancock: That was annoying.
[01:50:46] Brandon Hancock: To pay for their subscription, I could only do it through, if you wanted the, I can't remember the details of but if you wanted a specific one of their levels, you could only do it through the phone and through Apple.
[01:50:59] Brandon Hancock: hope.
[01:51:02] Brandon Hancock: I couldn't put it on a specific card, like I wanted to put it on a different card that wasn't associated with my Apple Pay, right?
[01:51:09] Brandon Hancock: That is wild.
[01:51:12] Brandon Hancock: I actually sent them an email and said, look, there's way too much friction for this onboarding.
[01:51:18] Brandon Hancock: Yeah, you're supposed to record.
[01:51:20] Brandon Hancock: It should be simple.
[01:51:22] Brandon Hancock: And that was the whole point of the devices, to make things simple, and you're making the onboarding so much friction.
[01:51:30] Brandon Hancock: I, real quick.
[01:51:32] Brandon Hancock: Besides that though, it's a great, it's a great device.
[01:51:35] Brandon Hancock: ▶ So I was gonna say, I was so torn, because I actually, like, now that the Limitless is going away, like, now that Meta has it, basically, they bought out Limitless.
[01:51:43] Brandon Hancock: It's like, I actually stopped using mine, because I was like, I don't want to invest more time into this platform if I know it's about to get yanked off in a year.
[01:51:50] Brandon Hancock: So I actually, I don't have it, it's upstairs.
[01:51:52] Brandon Hancock: I went with applaud.
[01:51:54] Brandon Hancock: I really liked it so far.
[01:51:57] Brandon Hancock: It's not listening 24-7.
[01:51:59] Morgan Cook: from You're again.
[01:51:59] Morgan Cook: I'm
[01:52:00] Morgan Cook: I have to press a button, like it attaches to the back of my phone, and I just press a button, it has been so helpful for just calls with a customer or a co-founder, and they also, like, have, well, I can't show it, but I have the desktop app too, so all the time when we keep going, I mean, I'm probably creepy, I don't know if I'm breaking any rules, but I'll tell you guys, all the time when I join meetings and they kick out my Fathom, I'm like, well, screw you guys, I'm gonna record anyway, because I need the context.
[01:52:27] Brandon Hancock: ▶ I need to feed my AI agents with context, so Plod has a record meeting, and it doesn't care, it's just listening to desktop audio, input and output, and that's been a game changer, I use that feature at least three times a week, so I was gonna say, if you're on a bunch of meetings, and you can't bring note takers, or you get a bunch of calls with clients, Plod, the one that goes on the back of your phone, I've loved it, so I just want to throw it out for everyone in the group, but I've also heard great things about Fieldy, so I just don't know if they have a desktop.
[01:52:57] Patrick Chouinard: But I've heard awesome things too.
[01:52:59] Patrick Chouinard: They do, I haven't.
[01:53:00] Patrick Chouinard: I it yet to see how it works, so I'm not sure, and it's for both Mac and Windows, but I haven't tested or played with it on my desktop yet.
[01:53:10] Patrick Chouinard: Patrick?
[01:53:11] Patrick Chouinard: It's pretty sensitive.
[01:53:12] Patrick Chouinard: I was surprised.
[01:53:13] Patrick Chouinard: ▶ I was at a job construction site, and I was standing in the kitchen, and there were two people in the room next to me whispering that I couldn't hear, but I was looking at my phone.
[01:53:24] Patrick Chouinard: It was transcribing it perfectly, everything they were saying.
[01:53:28] Patrick Chouinard: I was like, wow, that's some clarity.
[01:53:31] Patrick Chouinard: That's awesome.
[01:53:33] Patrick Chouinard: Yeah, seriously, it's a supersonic mic or whatever you want to call it.
[01:53:36] Patrick Chouinard: That's awesome.
[01:53:37] Patrick Chouinard: Patrick, I think you had a few things said too.
[01:53:40] Brandon Hancock: Yeah, actually, I have both fieldy, and I got the first fieldy, and the second one, the one that Morgan has, I finally received it.
[01:53:49] Brandon Hancock: And I also have the Plod pin, and the tripod ecosystem.
[01:53:56] Brandon Hancock: I like Plod.
[01:53:59] Brandon Hancock: I'll you time.
[01:53:59] Brandon Hancock: Bye.
[01:53:59] Brandon Hancock: Bye.
[01:54:00] Brandon Hancock: But it's really when I have a meeting that I want to listen to, a specific meeting that I know I'm going to start the recording, stop the recording, and there's multiple people, yes, but for day-to-day context-gathering, Fieldy is way above Loggamy, and the application is pretty nice, and it's getting nicer by the minute.
[01:54:25] Ty Wells: ▶ I think somebody is coding with Claude Code there, because they're pushing update very, very quickly, and it's catching up to the Plod desktop application, and they also offer a webhook if you want to take the output from it and feed it into n8n, for example, and use it for your own purposes.
[01:54:45] Ty Wells: Okay.
[01:54:46] Ty Wells: See, what's wild to me, that's super helpful, Patrick, by the way, thank you, and for everyone else.
[01:54:51] Brandon Hancock: The part that's wild to me is Limitless was so far ahead of everyone else, and now it's like I had to go buy back.
[01:54:59] Brandon Hancock: Like, I'm full
[01:55:00] Brandon Hancock: Four months, six months behind buying the Field of Your Plod compared to where Limitless was.
[01:55:06] Brandon Hancock: Like, that was the most beautiful UI towards the end.
[01:55:09] Brandon Hancock: I loved the UI.
[01:55:10] Brandon Hancock: I loved how I could ask questions for today or in past time.
[01:55:14] Brandon Hancock: It was auto-suggesting action items constantly.
[01:55:17] Morgan Cook: Like, I mean, he's rocking it as we speak.
[01:55:20] Brandon Hancock: He's lighting up right now.
[01:55:23] Brandon Hancock: Ty, if you want go, buddy.
[01:55:26] Scott Rippey: I've got till September 25th.
[01:55:28] Scott Rippey: So I'm sucking every minute out of this.
[01:55:31] Scott Rippey: Got to feed the beast, right?
[01:55:33] Scott Rippey: Yeah.
[01:55:34] Scott Rippey: Capturing that content.
[01:55:36] Scott Rippey: But what I do is I pull my stuff down daily.
[01:55:39] Scott Rippey: Yeah.
[01:55:40] Scott Rippey: I'm just stacking it up.
[01:55:41] Scott Rippey: So yeah, it'll come a point where I have to switch to one of these other guys.
[01:55:45] Scott Rippey: But who knows?
[01:55:45] Scott Rippey: September's far away.
[01:55:47] Scott Rippey: You never know what's going to change between.
[01:55:49] Scott Rippey: Next week's far away.
[01:55:51] Scott Rippey: Seriously.
[01:55:52] Scott Rippey: Prim, real fast to answer your question, every single one of them comes with a monthly subscription.
[01:55:58] Scott Rippey: The hardware is usually like 180.
[01:55:59] Scott Rippey: 80.
[01:56:00] Scott Rippey: And then I think there was three tiers.
[01:56:03] Scott Rippey: Basic, medium, and pro.
[01:56:06] Scott Rippey: I'm on the medium one right now, and it's crushing it for me.
[01:56:11] Brandon Hancock: So hopefully that helps.
[01:56:15] Scott Rippey: Okay, cool.
[01:56:16] Scott Rippey: Morgan, anything else?
[01:56:17] Scott Rippey: We all good?
[01:56:18] Scott Rippey: No, that's it.
[01:56:19] Scott Rippey: I'm good.
[01:56:19] Scott Rippey: Thank you, guys.
[01:56:21] Brandon Hancock: Perfect.
[01:56:22] Brandon Hancock: All right, cool.
[01:56:23] Scott Rippey: Scott, you're up next, man.
[01:56:25] Scott Rippey: Oh, man.
[01:56:27] Scott Rippey: What's going on?
[01:56:28] Scott Rippey: I'm to keep this short.
[01:56:29] Scott Rippey: There's way too much.
[01:56:30] Brandon Hancock: I have a laundry list.
<!--SEGMENT
topic: Scott — Meta Quest 3 + Immersed VR coding rig
speakers: Scott Rippey, Brandon Hancock
keywords: Meta Quest 3, Immersed VR coding, four-screen wraparound, BoboVR battery headset, prescription lens skip, $3K Apple Vision Pro skipped, music + AirPods + multiple Claude Code instances
summary: Scott bought a Meta Quest 3 + comfort headstrap and is doing 4-screen wraparound VR coding via Immersed (2K). Looks forward to no-call days because that's when he 'lives in the metaverse all day' with multiple Claude Code instances + Cloud Desktop. Skipped the $3K Apple Vision Pro — Immersed at 2K is good enough for his use case.
-->

[01:56:33] Brandon Hancock: So one thing that's fun is I did the VR coding thing.
[01:56:37] Scott Rippey: I got a Meta Quest 3 in it.
[01:56:39] Scott Rippey: Did the Immersed thing with the 2K [tool:Meta Quest 3] [tool:Immersed].
[01:56:42] Scott Rippey: I'm doing four screens.
[01:56:43] Scott Rippey: I'm literally sitting, like, with my keyboard, my mouse, and I'm like, dude, this is freaking awesome.
[01:56:48] Scott Rippey: Like, when you mentioned that, I was like, I gotta look into this.
[01:56:50] Scott Rippey: once I did, I was like, yup, I need to buy this.
[01:56:54] Scott Rippey: And I did.
[01:56:54] Scott Rippey: And I'm telling you guys, like, it's fun.
[01:56:57] Scott Rippey: And it's, it's like, like, it's just just, like,
[01:57:00] Scott Rippey: ▶ I have it wrapped around me and above me, and I'm just sitting here with multiple cloud codes and cloud desktop, and I'm just like, oh, this is great.
[01:57:08] Scott Rippey: It's freaky.
[01:57:09] Scott Rippey: It is freaky.
[01:57:10] Scott Rippey: So out of curiosity, did you get the secondary headset?
[01:57:15] Scott Rippey: What's the one everybody recommends?
[01:57:18] Scott Rippey: The comfortable one with the B?
[01:57:20] Brandon Hancock: What's it called?
[01:57:21] Brandon Hancock: I couldn't tell you, but yes.
[01:57:22] Brandon Hancock: Yeah, that one has the battery thing on the headset and everything.
[01:57:26] Brandon Hancock: Yeah, yeah.
[01:57:26] Scott Rippey: So I did that whole thing, swapped it out.
[01:57:28] Scott Rippey: Yep, yep.
[01:57:29] Scott Rippey: Okay, that makes me happy that you did it.
[01:57:32] Brandon Hancock: Okay, now final, final question.
[01:57:34] Brandon Hancock: Have you got prescription lenses in there?
[01:57:36] Scott Rippey: No, no.
[01:57:37] Scott Rippey: So, I mean, I probably am starting to go blind, but I didn't need to, because I technically, like, these are Bluetooth glasses.
[01:57:44] Scott Rippey: So I technically don't wear glasses, probably could, but I'm really good with, like, close stuff.
[01:57:51] Scott Rippey: I think it's more far away stuff for me anyway, at the moment, so I haven't really done glasses yet.
[01:57:55] Scott Rippey: But, yeah.
[01:57:56] Brandon Hancock: ▶ So, you know, I looked at, I was like, I'm not going to pay.
[01:58:00] Brandon Hancock: I know the Apple one would look really, really well, but I'm like, no, 3k for like, like with immersed and doing your, your, your, your right settings.
[01:58:13] Brandon Hancock: I think you're using immersed too, right?
[01:58:14] Brandon Hancock: Like, is that how you're using?
[01:58:15] Brandon Hancock: Yeah.
[01:58:15] Brandon Hancock: Yeah.
[01:58:16] Scott Rippey: It's like, it's 2k, right?
[01:58:18] Scott Rippey: It looks good.
[01:58:18] Scott Rippey: If you get it close, it looks good.
[01:58:20] Scott Rippey: Like, yeah, it is perfect for what I need.
[01:58:23] Scott Rippey: I can watch like, uh, no, I absolutely love it.
[01:58:27] Scott Rippey: I have laid in bed and watched a movie.
[01:58:31] Scott Rippey: Like, I was like, my wife's like, really?
[01:58:34] Scott Rippey: And I'm like, it's so good.
[01:58:37] Scott Rippey: It's so wild though.
[01:58:39] Scott Rippey: It's so wild.
[01:58:40] Scott Rippey: Cause I, I mean, I, so I had a, um, I'm not new to VR, but I hadn't used it in long time.
[01:58:44] Scott Rippey: I had the old, uh, uh, quest, the old one, like around COVID time, but I wasn't doing this kind of stuff then.
[01:58:52] Scott Rippey: And obviously it wouldn't look as good as like 40 P or something.
[01:58:54] Scott Rippey: So, you know, uh, I look forward to days when I have no calls.
[01:58:59] Scott Rippey: Because
[01:59:00] Scott Rippey: Because I literally just, I rock it the whole day, that's the, I get like, it messes up my hair and everything when I put it on, so I go, I look forward to no call days, because that's the first thing I do, I throw it on, and then I'm like, I'm in the metaverse today, and I just crank out code all day, and I love it.
[01:59:17] Scott Rippey: I will, I'll throw on my, my Apple AirPods and just play music, and I totally don't do the whole immerse thing, like I'll, I don't want their music, I'll just do my own stuff, and I'll just get going, you know, so anyway.
[01:59:29] Scott Rippey: So, I just want to tell you that, because.
[01:59:31] Scott Rippey: That's awesome.
[01:59:32] Scott Rippey: You mentioned that, I think the last time you were on, I think is when you mentioned it a month ago or so.
[01:59:36] Scott Rippey: Yeah.
[01:59:36] Scott Rippey: And I was like, but it didn't hit me right away, like, a few weeks ago I was like, oh, I need to do this, so.
<!--SEGMENT
topic: Scott + Patrick — Ironclaw secure-by-design AI assistant white paper
speakers: Scott Rippey, Brandon Hancock, Patrick Chouinard
keywords: Ironclaw architecture, governance-first vs features-first, smart router (Ollama local + Sonnet frontier), 14-hour Patrick collaboration, 40-page paper, Astro+Cloudflare in 15 minutes via Claude, human-in-the-loop, Telegram + Discord channel-split memory, NeuralSpark wizard onboarding + Slack integration, Claude Code mobile remote-coding compliance issues, Codex-5.4-as-OpenClaude-backend
summary: Scott shares his and Patrick's Ironclaw secure-AI-assistant white paper (40 pages, generated as Astro site to Cloudflare in 15 minutes after the 14-hour discussion). Architecture: governance first, features second; smart router blends local Ollama with frontier Sonnet/Codex; everything human-in-the-loop via Telegram/Discord. Patrick recommends Discord over Telegram because channels split memory cleanly. Adjacent: Scott's NeuralSpark added wizard onboarding + Slack RAG; his Code Anvil mobile remote-coding flow may not be in compliance with Anthropic's Agent SDK terms (Theo's recent video). Workaround: Codex-5.4-as-OpenClaude-backend works flawlessly and is fully allowed.
-->

[01:59:43] Scott Rippey: NeuralSpark updates, I was telling you I was going to sass that, I did, which is really cool.
[01:59:49] Scott Rippey: I'll show a couple screenshots real quick of that in a second, just as in like the onboarding, so I have it like wizarded, like, so a user logs in, because I want them to be able to add a user, they log in with Google, and it like.
[01:59:59] Scott Rippey: What?
[01:59:59] Scott Rippey: What?
[02:00:00] Scott Rippey: Unboards them for like the different things, because I also had to add in Slack, that was new, because I didn't, I do not use that myself, I mean, I have before, but not personally now, so, so for my clients, I took NeuralSpark, and they've got the whole Google AI assistant with the knowledge base rag, all that stuff, so we're in testing mode with two of them right now, it's going really well, so very little issues, which is nice.
[02:00:27] Scott Rippey: Um, the Code Anvil, I think you guys saw this before, it's funny, because then Claude Code came out with their mobile thing, which is a little different, um, and I knew they would eventually, like, I do like the fact that you can, from the, like, from your, like, continuous session, um, although it's still buggy, it still doesn't work, like, I can't get mine to work, like, and I know everybody's had a ton of problems with it, so.
[02:00:53] Brandon Hancock: With the Cloud, with the, which part, the, on the phone?
[02:00:56] Patrick Chouinard: like, if you're in your terminal, and then you're, like, go mobile for RC, and then, like, like.
[02:01:00] Patrick Chouinard: Like, I just can't even, like, I'm getting errors.
[02:01:02] Patrick Chouinard: Like, I can't even do it.
[02:01:03] Patrick Chouinard: It's a thing.
[02:01:04] Patrick Chouinard: It's a common thing.
[02:01:05] Scott Rippey: So, I still have that repo I share with you guys.
[02:01:09] Scott Rippey: I'm still going to use it once in a while, because I like the UI, because I build it with the Agent SDK.
[02:01:13] Scott Rippey: I actually don't think I'm within compliance, though.
[02:01:17] Scott Rippey: I thought I just read something, even though I'm calling it something different.
[02:01:20] Patrick Chouinard: I don't know if it's actually compliant.
[02:01:23] Patrick Chouinard: What's the name?
[02:01:25] Scott Rippey: So, like, I called it Code Anvil.
[02:01:27] Patrick Chouinard: So, I didn't call it anything, like, Claude now, but, like, Patrick's familiar with this, but, but I actually thought I saw something somewhere in a post once, recently, where it was like, you can't use the Agent SDK for something like that, and I wasn't sure, so.
[02:01:44] Patrick Chouinard: Oh, Theo, I thought it had a deep video on it, like, yesterday or today.
[02:01:49] Patrick Chouinard: I don't know if, I didn't fully watch it, but I just saw something.
[02:01:52] Scott Rippey: Yeah.
[02:01:52] Scott Rippey: Anyone watch it deeply that could elaborate?
[02:01:55] Scott Rippey: ▶ Yeah, basically, you can't use your subscription for entry.
[02:02:00] Scott Rippey: Tropic is horrendous with subscription, the only place they allow you to use it is Claude Code, that's it, that's all.
[02:02:06] Scott Rippey: In Claude Code, and that's exactly what I'm circumventing, because I'm technically doing a, it's a web app, using Claude Code's SDK, but it does a CloudFlare tunnel back to my Mac to use my subscription, now I'm not doing like a claw thing or anything.
[02:02:20] Brandon Hancock: be careful, because they don't allow you to use your subscription with the SDK either.
[02:02:24] Scott Rippey: No, I know, exactly, and then that's, that's what I'm saying, is like, I just saw this, and I'm like, oh , I'm like, not in compliance either.
[02:02:31] Scott Rippey: ▶ And honestly, Codex works way better now, with 5.4 as a brain for OpenClaude, than BOD does, so.
[02:02:43] Scott Rippey: I've switched to Codex as the backend, it works flawlessly, and it's fully allowed, there's no risk, I'm not going to lose my subscription or anything.
[02:02:54] Scott Rippey: Well, Patrick, this leads into a, what I want, I don't want to go into it on this call, but I wanted to bring it up, because I want to share.
[02:03:00] Scott Rippey: I think people need time to digest it.
[02:03:06] Scott Rippey: Patrick really sparked me with his whole, if you guys looked at his OpenClaude thing, brilliant [tool:Ironclaw].
[02:03:14] Scott Rippey: So, so good.
[02:03:15] Scott Rippey: Because everything we know about security, YouTubers just saying install it, we all know this is wrong, right?
[02:03:22] Scott Rippey: So, love his take on this.
[02:03:24] Scott Rippey: So I really started looking at stuff at some point.
[02:03:26] Scott Rippey: I'm like, I really do want to use something at some point.
[02:03:29] Scott Rippey: As an AI assistant with a claw architecture, and Patrick actually mentioned, turned me on to Ironclaw too [tool:Ollama].
[02:03:36] Scott Rippey: I think I found that through you.
[02:03:37] Scott Rippey: I didn't even know about it.
[02:03:39] Scott Rippey: And so, Ironclaw is really the one I've been looking at.
[02:03:41] Scott Rippey: I think it is probably the best one out there at the moment, I think, for like everything we're looking at.
[02:03:46] Scott Rippey: So I spent like 14 hours back and forth with Patrick too.
[02:03:50] Scott Rippey: He gave me great feedback.
[02:03:52] Brandon Hancock: And 14 hours in conversations with Opus and information I had and things I wanted to do.
[02:04:00] Scott Rippey: ▶ He to come up with this kind of setup guide white paper kind of a thing for doing iron claw and it was just fun though because you know the whole thing that that him and I were talking about was like you know governance you know over you know first you know over just functionality and and building a system and in a certain way so it was really really fun to get a lot of feedback from him and I think I came up with something that with his help that I think you guys would really love to look at even if you don't ever institute it uh on a mac mini or whatever like I just picked a mac mini everybody does but um I really think it would be something fun for you guys to read through uh and I'll share that I mean I'm sure we can add it to the post um yeah nano's one like so it actually talks about a lot of these like in my research I did about like why uh and and where their um shortcomings are but what did you end up on just out of curiosity because there's I I literally I I
[02:05:00] Scott Rippey: You did end up on Ironclaw?
[02:05:02] Scott Rippey: Yes.
[02:05:03] Brandon Hancock: And if you read the paper, like there's code stuff you guys can skip through because literally this paper, like I have a CloudMD file and a paper that it, I mean, what is it, Patrick?
[02:05:15] Patrick Chouinard: Their initial one was 33.
[02:05:16] Patrick Chouinard: It's gotta be at least 40 pages by now.
[02:05:17] Patrick Chouinard: So it literally can be, it handles all the edge cases, auditing, testing, like knowing exactly what you're doing, starting very, very small and then adding things later.
[02:05:28] Patrick Chouinard: Like I built this one to be like a researcher, a planner, kind of like, you know, it's its own teammate, it has its own accounts, you know, all the stuff Patrick talks about too.
[02:05:42] Scott Rippey: But like the, like reading through the first part of this document, I feel like is just, even if you're never going to install this, I feel like is a good read.
[02:05:50] Scott Rippey: Cause I think that's what were telling me Patrick too, was like, it's just like something good to think about, you know?
[02:05:56] Brandon Hancock: Exactly.
[02:05:56] Brandon Hancock: So I'll put it, I'll put it in the chat for you guys, but we'll, I'm sure we'll add it to the post too.
[02:05:59] Brandon Hancock: you.
[02:06:00] Brandon Hancock: So I want to give you guys a chance to, like, absorb it, and then I'd love for Patrick and I to, like, talk about how we were talking about it later on, you know, after you guys have had a chance, so.
[02:06:09] Brandon Hancock: Okay.
[02:06:10] Brandon Hancock: No, I'm pumped.
[02:06:11] Brandon Hancock: Patrick, how long did it take to write all this?
[02:06:14] Brandon Hancock: By hand.
[02:06:15] Brandon Hancock: That?
[02:06:15] Brandon Hancock: About 15 minutes.
[02:06:17] Brandon Hancock: It's Claude.
[02:06:19] Brandon Hancock: ▶ I basically chat with ChatGPT about it, extract the information, drop it into Claude, tell it to, uh, make it into the form of a academic paper and then transform it into an astral website and publish it to Cloudflare.
[02:06:35] Brandon Hancock: What's great is when Patrick and I email each other back and forth when we're talking about this stuff, we'll be like, hey, just, just, you know, like, obviously this was done with AI, but also I've manually reviewed it all.
[02:06:43] Scott Rippey: And it's like, we always do that.
[02:06:45] Scott Rippey: I stand by this, yeah.
[02:06:46] Scott Rippey: Because it's got to pull the information.
[02:06:47] Scott Rippey: It's like, I have to review it, but like, can't write this from scratch.
[02:06:52] Scott Rippey: Yeah, we had an exchange through co-work basically.
[02:06:55] Scott Rippey: Yeah.
[02:06:56] Scott Rippey: That's funny.
[02:06:57] Scott Rippey: mean, it, I mean, eventually it's going to be agents talk.
[02:07:00] Scott Rippey: You're to agents and then you just get the other end of it.
[02:07:02] Scott Rippey: Like, that is 100% how the future is about to work.
[02:07:06] Scott Rippey: ▶ Because it removes the friction of like, wait, I didn't understand what Patrick was trying to say here.
[02:07:10] Scott Rippey: Okay, like, you know, the agent knows what you know, and the agent knows what the person was trying to convey, and it just removes friction in the middle.
[02:07:16] Scott Rippey: So it's a fool's freaking time to be alive.
[02:07:18] Scott Rippey: Still, Accelerando.
[02:07:19] Scott Rippey: I'm telling you, your brain is not ready to hear what this book is about to tell you.
[02:07:25] Scott Rippey: I'm not shitting you guys.
[02:07:26] Scott Rippey: I sometimes have to put it down and just literally go, oh my God.
[02:07:29] Scott Rippey: I just bought it on Audible, by the way, so I'm going to listen to it.
[02:07:33] Patrick Chouinard: Okay, Scott, be in the metaverse and just fully just embrace it, man.
[02:07:39] Scott Rippey: No, but on the whole Ironclaw thing, like, I just want to give a shout out to Patrick because like, he inspired me to really like get into like my old IT roots of like security and like thinking about something in a different way.
[02:07:51] Scott Rippey: Like, you know, the whole governance thing first instead of features like, like he got me going and the whole back and forth.
[02:07:58] Scott Rippey: Like, I spent probably at least 14 to...
[02:08:00] Scott Rippey: 16 hours on this paper, and I'm like, I'm pretty proud of it, I think.
[02:08:05] Scott Rippey: And he said it wasn't bad, so...
[02:08:08] Scott Rippey: It was more than not bad, believe me.
[02:08:12] Scott Rippey: Because when he says something's good, I'm like, I respect it.
[02:08:14] Scott Rippey: I'm like, I know he knows what he's doing.
[02:08:16] Scott Rippey: So the last thing I want to share real quick, and I'll be done, is, let me screen share here.
[02:08:22] Scott Rippey: And actually, Patrick, you don't know about this.
[02:08:24] Scott Rippey: This was inspired by one of your earlier, like, AI news type...
[02:08:29] Scott Rippey: Well, you were doing...
[02:08:29] Scott Rippey: What was it you were sharing about, like, news, or, like, you were tracking, like, AI type...
[02:08:33] Scott Rippey: The intelligence dashboard.
[02:08:34] Scott Rippey: Yeah, the one that my client actually picked up.
[02:08:38] Scott Rippey: Yeah.
[02:08:39] Scott Rippey: So, you inspired me.
<!--SEGMENT
topic: Scott — daily AI News Brief with ElevenLabs Jarvis voice + Haiku RAG
speakers: Scott Rippey, Brandon Hancock
keywords: AI News Brief email + audio, RSS aggregation, Haiku for context-aware deduplication, 10-day RAG database, Paul Bettany Jarvis voice from ElevenLabs ($100/mo subscription), 10-20 min daily audio briefing
summary: Scott built (and runs) a daily AI News Brief: aggregates RSS feeds, runs through Haiku (story-thread context aware so it doesn't repeat the same news across days), keeps last 10 days in a RAG database, then sends both email and an ElevenLabs-generated audio briefing in a Paul-Bettany-Jarvis voice (his Iron Man hooks voice). Free to add new email recipients to the distribution. $100/mo ElevenLabs subscription pays for the volume.
-->

[02:08:41] Scott Rippey: I'm going to share this.
[02:08:42] Scott Rippey: Let's see.
[02:08:42] Scott Rippey: Okay.
[02:08:44] Scott Rippey: So you actually inspired me for this.
[02:08:46] Scott Rippey: So, and if anybody wants me to add them in, I will, because...
[02:08:50] Scott Rippey: I'm already paying for this, meaning, like, I have a dashboard, but it sends out an email.
[02:08:56] Scott Rippey: And what I did was, I did RSS feeds, because I was getting all these emails, like...
[02:09:00] Scott Rippey: It made me think, I was like, so I go in here and I can save stuff and it's fine, right, but I have all these feeds that I'm using, and what it does is I can add you guys as recipients, it doesn't cost me anything to do this, and I got a lot of friends on this already, where every day it sends out an email that looks like this, and I'm using Haiku to smartly pull in, and I'm doing a RAG database where I'm just, and I'm only keeping the last 10 days of information in the database, but it's, so I never repeat a story, but it will do the developing story, so it's giving some context too, not just the titles, so every time Haiku looks at these things, it goes, okay, if this same story comes out like a day or two later on a different feed, is it the same or is it not, so it gets the summary, so it kind of knows, and this is still super cheap for me to run, and Haiku is more than enough for this, don't need Sonnet, so like, it'll combine sources, so you get an email, but the benefit for you guys, the real benefit is this, Here's your AI News Brief [tool:ElevenLabs] [tool:RSS]
[02:10:01] Scott Rippey: I'm on the wrong.
[02:10:02] Scott Rippey: So what I did was I'm also sending this out to ElevenLabs with my Tony Stark, you know, Iron Man voice [tool:Jarvis voice].
[02:10:11] Scott Rippey: Jarvis.
[02:10:12] Scott Rippey: Jarvis, yes.
[02:10:12] Scott Rippey: Because I use Jarvis.
[02:10:13] Scott Rippey: I've made this Paul Bettany clone for my, like, Claude Code hooks and everything.
[02:10:17] Scott Rippey: I've been using this forever.
[02:10:19] Brandon Hancock: ▶ So now I have, I get my daily AI news, which, because I usually listen to it.
[02:10:23] Scott Rippey: It's like, I'm not going to, like, it's great to have this as a reference, but I'm usually driving or doing something.
[02:10:27] Jake Maymar: So every morning, 10 to 20 minutes max, you get your kind of developing news in the AI world.
[02:10:34] Jake Maymar: And I just need to change this to the right thing.
[02:10:37] Jake Maymar: So you guys can see, because this is going to be, I got too many speakers.
[02:10:42] Scott Rippey: All right.
[02:10:42] Scott Rippey: So I think you guys will hear this.
[02:10:44] Scott Rippey: Here's your AI news briefing for Tuesday, March 24th.
[02:10:48] Scott Rippey: Claude's computer control desktop automation goes mainstream.
[02:10:52] Scott Rippey: What happened?
[02:10:53] Scott Rippey: Anthropic has released a new feature allowing...
[02:10:55] Scott Rippey: You guys hear that?
[02:10:57] Scott Rippey: Yeah.
[02:10:58] Scott Rippey: Yeah.
[02:10:58] Scott Rippey: Yeah.
[02:10:58] Scott Rippey: That sounds awesome,
[02:11:00] Scott Rippey: The on this, I mean, I've been using it for a month now, or a little less, and I've got some friends on it.
[02:11:06] Scott Rippey: I'll gladly add anybody's email in.
[02:11:08] Scott Rippey: It costs me nothing to add extra emails.
[02:11:11] Scott Rippey: So, I had to up my 11 labs to my $100 a month subscription because I'm transcribing so much with it, but it's worth it.
[02:11:19] Scott Rippey: Hey, please send me, add me to that, please, Scott.
[02:11:23] Scott Rippey: Yeah, yeah.
[02:11:26] Scott Rippey: So that's all I got.
[02:11:29] Scott Rippey: Scott, are you doing anything local?
[02:11:33] Scott Rippey: Oh, I should put my hand up.
[02:11:35] Scott Rippey: You mean, well, so you mean like a local model?
[02:11:38] Scott Rippey: Yeah, yeah.
[02:11:39] Scott Rippey: Yeah, so the Ironclaw thing that I'll put in there when you guys look at that actually is like primarily going to be Ollama locally with using Sonnet.
[02:11:50] Scott Rippey: There's going be a smart router with like, you know, there's certain complex things that you've got to use the frontier model for, but you're trying to do as much as you can locally.
[02:11:57] Scott Rippey: So, this is all.
[02:11:59] Scott Rippey: This
[02:12:00] Scott Rippey: It's out in theory, it should work, I obviously have to wait for my Mac Mini before, and they're all back-order because of OpenClaude, which was dumb, it's like, they like, they hit that supply chain so hard, I know it was OpenClaude, like, it's like seven weeks at least.
[02:12:16] Scott Rippey: But so I haven't done a lot with, I've looked into a lot of stuff, but I planned with it for that, for this particular use case, because it makes sense, it's like, you want to kind of blend, but smartly.
[02:12:27] Juan Torres: And the whole point, too, though, I just can't wait for you guys to read this, because it's auditable, and it's, it's tweakable, to where, like, you're going to fine-tune how the router works, so that it gets better and better.
[02:12:41] Scott Rippey: The more information it gets, the smarter it gets, because the database is the brain, not the model.
[02:12:46] Scott Rippey: And the whole, you know, router is the thing that, like, starts to understand better and better, like, oh, when do I use local versus, you know, the frontier model.
[02:12:55] Scott Rippey: So, it's, it's a fun, fun project.
[02:12:59] Scott Rippey: Yeah, perfect.
[02:12:59] Scott Rippey: Get
[02:13:00] Patrick Chouinard: I feel like a lot of you guys would just want to try this as an assistant for your business because you can do it securely and just you're not going to get like just for research and planning even like it's only going to have read only to my calendar, you know, and it's going to know, you know, non-sensitive client stuff.
[02:13:15] Patrick Chouinard: It's not going to be able to do anything.
[02:13:16] Patrick Chouinard: And there's like Patrick and were talking about, everything is like human in the loop.
[02:13:20] Patrick Chouinard: We're like through Telegram, it's going to hit me for anything.
[02:13:23] Scott Rippey: It's like, it's not going to send anything without me knowing.
[02:13:25] Scott Rippey: It's not going to do anything without me knowing.
[02:13:26] Scott Rippey: It's like, it's just going to do the background stuff, you know.
[02:13:30] Scott Rippey: I was actually going to ask you this if you were planning to use Telegram or a texting service to send that audio.
[02:13:36] Juan Torres: Yeah.
[02:13:37] Juan Torres: I think that's going to be more accessible to people.
[02:13:40] Brandon Hancock: Yeah.
[02:13:41] Patrick Chouinard: Yeah.
[02:13:41] Patrick Chouinard: Telegram.
[02:13:42] Scott Rippey: Telegram is a good one.
[02:13:43] Scott Rippey: I mean, I could use WhatsApp or something else probably too, but Telegram is an easy one to do.
[02:13:46] Scott Rippey: They got the bot father thing that works.
[02:13:48] Scott Rippey: I mean, we all know that.
[02:13:49] Patrick Chouinard: So I think that that's an easy, easy in.
[02:13:52] Patrick Chouinard: Um, but yeah, I, I'm going to put it in the chat now, but obviously we'll try to.
[02:13:59] Patrick Chouinard: No.
[02:13:59] Patrick Chouinard: Thank
[02:14:00] Patrick Chouinard: Add it to the post or whatever, too, that goes out for anybody, so.
[02:14:04] Scott Rippey: Yeah, just one little thing.
[02:14:05] Scott Rippey: ▶ In the communication, after working with Telegram a lot on OpenClaude, I've moved now to Discord, and I find that Discord, if you dedicate a server and you have multiple channels where you split your conversation, it makes memory management...
[02:14:24] Brandon Hancock: I about that, and now you make me want to edit this thing before I share it, because I totally forgot about Discord, and I do love Discord.
[02:14:31] Brandon Hancock: And I'm like, dang it, now I'm going to have to, like, rework something before I share it.
[02:14:34] Brandon Hancock: So I may rework it, and then I'll share it.
[02:14:37] Brandon Hancock: Everything needs to be pre-approved by Patrick.
[02:14:39] Brandon Hancock: Yep.
[02:14:40] Brandon Hancock: No, I don't know.
[02:14:41] Brandon Hancock: It's so good.
[02:14:43] Brandon Hancock: No, I mean, I totally agree, because, like, I love Discord, and I'm like, I totally forgot about that when I was doing this, and I went to Telegram, and I'm like, oh yeah, that makes sense, and I totally forgot about Discord.
[02:14:52] Brandon Hancock: programs work very well.
[02:14:53] Brandon Hancock: It's just that Discord, since you have channels, you can split the memory, so you can have a whole lot more content.
[02:15:00] Brandon Hancock: Yeah.
[02:15:01] Brandon Hancock: Yeah.
[02:15:01] Brandon Hancock: Without polluting each other.
[02:15:02] Brandon Hancock: Yeah.
[02:15:03] Brandon Hancock: Well, yeah, exactly.
[02:15:03] Brandon Hancock: I think actually using Discord over Telegram would give more flexibility on how we design something as this grows.
[02:15:10] Brandon Hancock: Really.
[02:15:10] Brandon Hancock: So, yeah.
[02:15:11] Brandon Hancock: Yep.
[02:15:11] Brandon Hancock: Nope.
[02:15:12] Brandon Hancock: Sorry, guys.
[02:15:12] Brandon Hancock: I'm going to rework it a little bit and then I'll share it.
[02:15:16] Brandon Hancock: That's awesome.
[02:15:17] Brandon Hancock: Patrick got me.
[02:15:21] Brandon Hancock: The process is never done.
[02:15:24] Brandon Hancock: Patrick, I'm pumped for you to read what you put together just because literally I have to get it set up.
[02:15:31] Brandon Hancock: Like we've been just like so focused on like a few high priority things that we have to like, they're a bottleneck right now.
[02:15:36] Elijah Stambaugh: But the next thing is like we want to start working on like what we're calling like a customer success manager.
[02:15:42] Elijah Stambaugh: And it's like why we always ask ourselves first, like, can we build it instead of hire for it?
[02:15:49] Elijah Stambaugh: So that literally is what my box is going to start being is like we're going to try and create a customer success person to where it's like you manage, you are, you're constantly monitoring quality.
[02:16:05] Elijah Stambaugh: So I'm excited to dig deeper into this because I think pumped to get a bunch of cool ideas and feedback on on what we can do.
<!--SEGMENT
topic: Elijah — embed/equipped consulting program + 5 principles of AI engineering
speakers: Elijah Stambaugh, Brandon Hancock, Ty Wells
keywords: embed program (2 days/week × 6 months), equipped program point solutions, 30-40 Claude Code skills per business, output-driven thinking, work-on-the-machine-not-the-output, instructions are context, task-template feedback loop, The Phoenix Project bottlenecks, Three Buckets framework reference, Lubrizol 25-50× innovation cycle from data-store work
summary: Elijah is launching an embed program (2 days/week × 6 months in a client business documenting processes and storing data correctly) and an equipped program (point solutions). Brandon's framing: every business needs ~30-40 Claude Code skills to run 100× more efficient. Five principles: context problem first, frictionless work via more-context + more-steps + more-agentic, work on the machine (task template) not the output. Recommends The Phoenix Project — businesses are bottlenecks + SOPs. Ty cross-references threebuckets.ai (Contributor Model framework matches the same separation). Lubrizol cousin: 80% of project work is now data side, but innovation cycle 25-50× post-investment.
-->

[02:16:17] Elijah Stambaugh: So it might not be soon, but by the next time we have a call, it should be built.
[02:16:22] Elijah Stambaugh: So I'm excited to let you guys know how it goes.
[02:16:26] Brandon Hancock: So cool.
[02:16:27] Brandon Hancock: All right.
[02:16:28] Brandon Hancock: Well, any final questions?
[02:16:29] Elijah Stambaugh: Thanks, also, uh, oh, go ahead.
[02:16:34] Elijah Stambaugh: Sorry.
[02:16:35] Elijah Stambaugh: Um, no, Elijah, if want go ahead and go.
[02:16:39] Brandon Hancock: Well, was just going to say, I sent you a direct message.
[02:16:42] Elijah Stambaugh: I was literally about to announce it until I said, until I read the first sentence.
[02:16:47] Elijah Stambaugh: Yeah.
[02:16:48] Elijah Stambaugh: Sorry.
[02:16:48] Elijah Stambaugh: I, it's, uh, we, I would love to share with the group.
[02:16:52] Elijah Stambaugh: I'll be able to share it pretty soon, but my son and I won a competition.
[02:16:55] Elijah Stambaugh: Um, he's a, he's a junior in high school, but we're not allowed to share until like.
[02:17:00] Elijah Stambaugh: A week or two from now, but I want to share with you guys because you've all contributed to my ability to help him learn how to do things.
[02:17:11] Brandon Hancock: Well, I'm pumped.
[02:17:12] Elijah Stambaugh: I know what it is, and I'm very pumped, man.
[02:17:15] Elijah Stambaugh: Very, very excited.
[02:17:16] Elijah Stambaugh: and I think we can continue to move forward with it as well.
[02:17:22] Elijah Stambaugh: And so, yeah, it should be pretty good.
[02:17:25] Elijah Stambaugh: Awesome.
[02:17:26] Elijah Stambaugh: Awesome.
[02:17:28] Elijah Stambaugh: That's so freaking awesome.
[02:17:30] Elijah Stambaugh: I'm so excited for you guys.
[02:17:31] Elijah Stambaugh: So when you're on the call in a month, I should be able to give all the details.
[02:17:36] Elijah Stambaugh: But I did have one other question about business in general.
[02:17:40] Elijah Stambaugh: Yeah, of course.
[02:17:41] Elijah Stambaugh: And we maybe don't have time for it tonight.
[02:17:44] Elijah Stambaugh: That's fine.
[02:17:45] Elijah Stambaugh: But I've been, as I've been engaging with clients, I'm thinking of a program.
[02:17:52] Elijah Stambaugh: So I have two different programs that I'm thinking about building in my consulting business.
[02:17:58] Elijah Stambaugh: One is an embed program.
[02:17:59] Elijah Stambaugh: different, program.
[02:17:59] Elijah Stambaugh: So I've
[02:18:00] Elijah Stambaugh: And the other one's an equipped program, because what I'm finding is these, these businesses, they want to use AI, they want to change what they're doing, but they don't know how.
[02:18:11] Elijah Stambaugh: Yeah.
[02:18:12] Elijah Stambaugh: They don't even know what good looks like.
[02:18:13] Elijah Stambaugh: of like, they don't know what good looks like.
[02:18:15] Elijah Stambaugh: They don't know, you know, and so my real question and challenge was around that Databricks stuff.
[02:18:22] Elijah Stambaugh: So I had posted a couple links there as well.
[02:18:24] Elijah Stambaugh: Like, how do we have to store the data in a business to get it to run a certain way?
[02:18:30] Elijah Stambaugh: I can add in like, you know, social posting and some CRM stuff, like aging on, you know, bids or prospects, some things like that.
[02:18:43] Elijah Stambaugh: So I'm going to build those point solutions, but the embed program where, where is where I would put somebody in the business like two days a week for like six months.
[02:18:54] Brandon Hancock: Yeah.
[02:18:55] Brandon Hancock: And they would just document the processes and figure out how to store the data.
[02:19:00] Brandon Hancock: ▶ So it's just something I've been thinking about, and as I continue to move forward, I have a couple businesses that are interested, and these are legacy businesses, but the owners are, you know, most of them are in their late 50s, early 60s, they've made enough money to stop working if they wanted to, but they're not really wanting to retire, but they're innovative in their mindset, and so they're trying to use AI, not just ChatGPT.
[02:19:30] Brandon Hancock: So they're working with storing their data correctly, and how they get that piece of it right, so I don't know if it's a question right now, as much as it is, like, I'm gonna, I'm gonna land like five of them and try to create a cohort, and basically implement within their business, the repeatable processes that I can take to every other business too.
[02:19:53] Brandon Hancock: So, real quick, Elijah, I'm actually helping, like, a big company do this right now, and...
[02:19:59] Brandon Hancock: And...
[02:20:00] Brandon Hancock: ▶ The key thing is educating the actual people what we're doing and why and honestly just turning that into like a video series first to just share with them because like they need to know like at end of the day here's what we're trying to teach people.
[02:20:19] Brandon Hancock: I call it like the five the five principles of AI engineering like the most important problem is the context problem everything else derives from that at this point if you don't have context you can't have a valid answer.
[02:20:33] Brandon Hancock: I can't remember there's a few other ones I can't remember all of them but basically like strive for frictionless work mean and to get there it's honestly just comes down to more context more steps and more agentic work.
[02:20:45] Brandon Hancock: ▶ And there's a few other work on the machine not the output so in your case you were like oh like they're working on task.
[02:20:53] Brandon Hancock: No, they should be working on the machine that then produces the output.
[02:20:57] Brandon Hancock: So in our case the outputs code.
[02:20:59] Brandon Hancock: Well.
[02:21:00] Brandon Hancock: What's the machine?
[02:21:01] Brandon Hancock: The machine is the task template.
[02:21:03] Brandon Hancock: ▶ Any time the task template doesn't produce the desired result, we fix the task template.
[02:21:10] Scott Rippey: We don't fix the code.
[02:21:11] Brandon Hancock: You fix the task template so it understands what's going wrong and what it should have done differently, then it updates the code.
[02:21:17] Elijah Stambaugh: So as a result, you're always one layer of extraction away from the actual work.
[02:21:22] Elijah Stambaugh: You never just like, give me the answer.
[02:21:24] Elijah Stambaugh: You're always one layer away.
[02:21:27] Elijah Stambaugh: So teaching people things like this, like, you know, like you could, I mean, there's, there's multiple ways you could do this.
[02:21:36] Elijah Stambaugh: Cause it's funny.
[02:21:36] Elijah Stambaugh: I've actually talked to my wife about this.
[02:21:37] Elijah Stambaugh: I'd love for her to do it.
[02:21:38] Elijah Stambaugh: ▶ Like it really comes down to every business needs probably 30 to 40 Claude Code skills and they could run their business to a hundred times more efficient.
[02:21:45] Elijah Stambaugh: It's literally the difference from them.
[02:21:48] Elijah Stambaugh: It's, it's, it's, it's, 30 to 40 Claude Code skills.
[02:21:50] Elijah Stambaugh: That is, it's from them doing, uh, it's like high quality Claude Code skills, not just like, you know, summarize this.
[02:21:58] Elijah Stambaugh: Um, yeah.
[02:21:59] Elijah Stambaugh: okay.
[02:21:59] Elijah Stambaugh: Okay.
[02:22:00] Elijah Stambaugh: Stott, if you could do Brandon at BrandonHancock.io What was that?
[02:22:06] Elijah Stambaugh: Sorry.
[02:22:06] Elijah Stambaugh: Sorry.
[02:22:07] Elijah Stambaugh: Just Brandon at BrandonHancock.io.
[02:22:10] Brandon Hancock: would be huge.
[02:22:11] Elijah Stambaugh: Awesome.
[02:22:11] Elijah Stambaugh: Thanks.
[02:22:13] Elijah Stambaugh: Sorry, Elijah.
[02:22:14] Elijah Stambaugh: Obviously, you know, I'll say humbly because it would be an honor to work with you or your family, your wife.
[02:22:21] Elijah Stambaugh: But if she is interested, I mean, that's so I'm not on my computer, right?
[02:22:28] Elijah Stambaugh: I'm on my phone.
[02:22:29] Elijah Stambaugh: But I have my computer here.
[02:22:30] Elijah Stambaugh: But and we're getting late.
[02:22:32] Elijah Stambaugh: I could show you if you wanted.
[02:22:34] Elijah Stambaugh: But I have created.
[02:22:37] Elijah Stambaugh: So I've owned the domain name creator class.com for a while.
[02:22:41] Elijah Stambaugh: And, you know, I work in the education system.
[02:22:44] Elijah Stambaugh: Yeah.
[02:22:44] Elijah Stambaugh: So.
[02:22:46] Elijah Stambaugh: So what I've built is it's it's ship kit.
[02:22:51] Elijah Stambaugh: It's the rag as well.
[02:22:53] Elijah Stambaugh: So it's fully stacked on the rag, you know, infrastructure, cloud and everything.
[02:22:58] Elijah Stambaugh: But what
[02:23:00] Elijah Stambaugh: I've built is a parallel system to setting up exactly what you're talking about, I'll say Claude code, but it's basically like very raw, get dirty real fast, get your machine up and running, and then here's the concepts as well, and then what I'm envisioning is what is, you know, what I read was, it's called malleable software, so the guy that wrote his doctoral paper and did all the research on it, he got headhunted by Notion, so he's now hired at Notion, and he's the one running their, like, their new agent stuff they've been doing with their Notion AI, I don't know if you've seen it, it's getting really, really good, um, yeah, so Notion added agents, they have, I mean, they're releasing a lot of functionality fast, I mean, I've, I'm this is not a of
[02:24:00] Elijah Stambaugh: I've been wanting to go away from Notion, because I wanted to just be in Claude Code, but they have Opus 4.6 now, and I do have an MCP running with Notion, so I can update my pages and pull all my context back and forth, but long story short is, if your wife wants to work on some I'm trying to convince her, so it's not a...
[02:24:22] Elijah Stambaugh: I'm the one trying to convince her, so no.
[02:24:25] Elijah Stambaugh: I can bring the clients.
[02:24:27] Elijah Stambaugh: I've got a handful of businesses that are ready, willing, and eager, and I can give them pieces of it, which I am doing.
[02:24:38] Elijah Stambaugh: I'm trying to get them, like I said, into a cohort to commit to me and me to commit to them, because this context saving, like, I'm not sure exactly, when you use that term, are you talking about Supabase?
[02:24:52] Elijah Stambaugh: Are you talking about the .md memory files, and then you've probably seen Claude Code today released?
[02:24:59] Elijah Stambaugh: .
[02:24:59] Elijah Stambaugh: .
[02:24:59] Elijah Stambaugh: .
[02:24:59] Elijah Stambaugh: .
[02:24:59] Elijah Stambaugh: .
[02:25:00] Brandon Hancock: ▶ Their dream, they have their dream function they just released, which is a way to update your memory files, so, and then the, I posted in the link, and then the other gentleman on the call talked about like the Data Lake solutions, those solutions, I talked to my cousin who's a organic chemistry at Lubrizol, and he called me like six months ago and said, Elijah, I gotta change my career, he's, he's done really well, but, and he's, you a PhD in the scientist, but he said the data side of the project now is 80% of the work, once they have that done, they've increased their innovation cycle 25 to 50 times, and he said it's unreal, and we're talking about Lubrizol, right, I mean, this is like biggest in the world, right, chemicals, and so, it's just, we can do that with every business, I agree with you on the 40, and if we can store the data right,
[02:26:00] Brandon Hancock: Right?
[02:26:00] Brandon Hancock: And that's the piece where I need your guys' help.
[02:26:02] Brandon Hancock: Like, I would love to try to solve that problem.
[02:26:04] Brandon Hancock: What does that look like?
[02:26:07] Brandon Hancock: Okay.
[02:26:08] Brandon Hancock: So, one thing real fast, I love Ty to Go.
[02:26:10] Brandon Hancock: So, I mean, what I'm talking about when it solves the context problem, at the end of the day, we have to think in an output-driven fashion.
[02:26:20] Brandon Hancock: So, like, what is the actual output that we're trying to produce?
[02:26:24] Brandon Hancock: A business produces hundreds of them.
[02:26:25] Brandon Hancock: They produced annual reviews of their employees.
[02:26:28] Brandon Hancock: They write emails day to day.
[02:26:30] Brandon Hancock: Like, there's a dozen outputs that truly run the business, you know?
[02:26:35] Brandon Hancock: Like, oh, a customer wants to, like, I'm thinking a wedding venue, back to my friend's business.
[02:26:40] Brandon Hancock: A customer wants to do a wedding venue.
[02:26:42] Brandon Hancock: Okay, well, like, we take in a transcript of them talking to the client the whole time, and then we output a pitch with, like, a pricing proposal.
[02:26:51] Brandon Hancock: Like, there's a thousand, there's a dozen small things that have to happen for that business to run.
[02:26:57] Brandon Hancock: And right now, people do it.
[02:26:58] Brandon Hancock: Each employee.
[02:26:59] Brandon Hancock: employee.
[02:26:59] Brandon Hancock: A
[02:27:00] Brandon Hancock: ▶ Truthfully, probably does 12 SOPs.
[02:27:03] Brandon Hancock: They're not documented anywhere, they're just talked about.
[02:27:06] Brandon Hancock: And they know what to do because we're humans.
[02:27:08] Brandon Hancock: But if you actually look at doing that person's job, just like a software developer's jobs, we do the same software development lifecycle forever.
[02:27:17] Brandon Hancock: We just happen to work on bigger problems, you know, and different problems.
[02:27:21] Brandon Hancock: But as an employee making $20 an hour or so, you're doing the same task all day, every day.
[02:27:27] Brandon Hancock: And that's what agents can crush.
[02:27:29] Brandon Hancock: So what is solving the context problem for a $20 an hour employee?
[02:27:34] Brandon Hancock: It is a combination of, A, who is this person?
[02:27:38] Brandon Hancock: What is the identity of this person?
[02:27:40] Ty Wells: I'm a sales rep, I do this, here's context about the business, here's what we do, here's common things that you need to know about our business, just background information.
[02:27:48] Ty Wells: Part two is we are trying to produce an output.
[02:27:53] Ty Wells: To produce an output, a proposal, a pitch, something else, it just steps, broken down into very...
[02:28:00] Ty Wells: It's concise.
[02:28:01] Ty Wells: Instructions.
[02:28:03] Ty Wells: Instructions are context.
[02:28:04] Ty Wells: So that's what I'm saying.
[02:28:05] Ty Wells: It's like solve the context problem because the second you have enough information to produce that output, it's done going forward, you know?
[02:28:13] Ty Wells: So that's what I'm talking about.
[02:28:15] Ty Wells: So like, I really would recommend if this is the type of business you're about to get into, I would read the book, The Phoenix Project, because it just forces you to think in bottlenecks because every business is just a series of bottlenecks and it's a series of standard operating procedures [tool:The Phoenix Project].
[02:28:32] Ty Wells: ▶ And the second you get everything codified, the business just sinks.
[02:28:37] Ty Wells: And yeah, so I'll leave it at that.
[02:28:40] Ty Wells: I know you had your hand up too, buddy.
[02:28:42] Ty Wells: Yeah.
[02:28:42] Ty Wells: And just to really put a cap on what you're saying, I put a link in there for a three buckets.ai [tool:threebuckets.ai].
[02:28:50] Elijah Stambaugh: It is exactly what you're talking about.
[02:28:53] Elijah Stambaugh: This is a framework.
[02:28:54] Elijah Stambaugh: I think I presented it to you guys before.
[02:28:57] Elijah Stambaugh: It's evolved slightly.
[02:28:59] Elijah Stambaugh: So if you get a minute.
[02:29:00] Elijah Stambaugh: Take a look at it, it's right down the same path that you're talking about in terms of I separate things into three buckets, your digital bucket, your judgment bucket, and then their contributor bucket where employees have freed up their time from digital stuff so they can go into the contributor bucket and they actually can innovate and it's a grassroots sort of, that starts at the bottom.
[02:29:29] Elijah Stambaugh: And that's what I'm here implementing.
[02:29:33] Brandon Hancock: This is a framework that I came up with that's all out there in the public.
[02:29:37] Brandon Hancock: You can take a look at it.
[02:29:39] Brandon Hancock: Elijah, you should look at it, because I think that's where you're headed.
[02:29:42] Brandon Hancock: That's what you want to do, but I put a whole framework around it.
[02:29:46] Brandon Hancock: So take a peek at it, threebuckets.ai.
[02:29:51] Brandon Hancock: It automatically started the voice bucket.
[02:29:54] Brandon Hancock: I'm just smiling because, man, you always got something.
[02:29:56] Brandon Hancock: You crack me up.
[02:29:57] Brandon Hancock: I love it.
[02:29:58] Brandon Hancock: Thank you so much.
[02:30:00] Brandon Hancock: it's good stuff.
[02:30:01] Brandon Hancock: I'm going to dive into it.
[02:30:04] Brandon Hancock: So the only thing is, Brandon, when you're referencing this, you know, getting these skills in place to execute these operations or these tasks is, my only concern is like, what is the memory of the business need to be?
[02:30:28] Brandon Hancock: You know, how much information do you have to store?
[02:30:31] Brandon Hancock: By doing the task, you'll find out.
[02:30:33] Brandon Hancock: You won't know until you start to do the task and do the task at scale.
[02:30:38] Brandon Hancock: Because if you start to find out, man, to do this task, like, it keeps making mistakes on A, B, C, D, and E.
[02:30:44] Brandon Hancock: Oh, cool.
[02:30:45] Brandon Hancock: That's background knowledge that it just needs to know.
[02:30:48] Brandon Hancock: Like, you never know until you do it.
[02:30:49] Brandon Hancock: Like, that's why doing these types of businesses, you just have to get in and do the work yourself or a contractor or somebody and do the work, because by doing the work and knowing that you're...
[02:31:00] Brandon Hancock: It's allowed to produce the output.
[02:31:01] Brandon Hancock: The agent has to produce the output by looking at markdown files or doing tool calls.
[02:31:07] Brandon Hancock: That's the only way it can get that output.
[02:31:09] Brandon Hancock: If you're having to add anything else manually, you know there's something missing.
[02:31:13] Brandon Hancock: You know?
[02:31:14] Brandon Hancock: And that's the way to think about it.
[02:31:17] Brandon Hancock: Perfect.
[02:31:18] Brandon Hancock: Perfect.
[02:31:19] Brandon Hancock: Yep, that makes total sense.
[02:31:21] Brandon Hancock: Yes, thank you.

=== UNRESOLVED SPEAKERS ===
- Don Davis (appears 27 times, example: "Well, I'll start with, I'll start with my comment on Codex first, and then I'll,")
- Hemal Shah (appears 67 times, example: "Yeah, I was traveling.")
- Naren (appears 7 times, example: "So, Terraform, if someone wants to add on to what I'm saying too, feel free.")
- Prem (appears 8 times, example: "Al Cole?")
- Scott Rippey (appears 222 times, example: "I still have it on my screen to buy.")
===