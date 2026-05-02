=== SESSION ===
date: Unknown (DST transition week)
duration_estimate: ~2 hours
main_themes: AI-assisted app development, Lovable/Cursor for rapid prototyping, LLM model selection in Windsurf, lead qualification with Perplexity API, AI sales training tools, go-to-market strategy for AI agencies, N8N automation, OpenAI Agents SDK launch, technical interview preparation

---

<!--SEGMENT
topic: Pre-Meeting Small Talk
speakers: Andrew Nanton, Patrick Hutchinson, Brandon Hancock, Jake Maymar, Nate G
keywords: standing desk, treadmill desk, time change, DST, sweater, hoodie, chiropractor, schedule confusion, warm-up
summary: Participants exchange casual conversation about shared clothing tastes, standing and treadmill desks, and a scheduling confusion caused by daylight saving time. No technical content; serves as session warm-up and attendance check.
-->

**00:02:03 - Andrew Nanton**
How are you?

**00:02:04 - Andrew Nanton**
I have that same sweater.

**00:02:06 - Patrick Hutchinson**
Yeah, I think we've determined that in the past.

**00:02:10 - Patrick Hutchinson**
We shop at the same stores.

**00:02:12 - Andrew Nanton**
Yeah, I guess so.

**00:02:19 - Brandon Hancock**
I was saying, it looks super comfy.

**00:02:21 - Patrick Hutchinson**
How do I get one?

**00:02:25 - Brandon Hancock**
I'm going to have to look this up.

**00:02:28 - Brandon Hancock**
I mean, I talk hoodies all the time. There's just nothing. It's my favorite shirt. I love a good, like, mid-60s, low 70s, a nice shirt like this. And I'm a happy man. I'll look it up real fast.

**00:02:54 - Brandon Hancock**
I'm sitting all day, so I might as well be comfy while I'm doing it.

**00:03:05 - Brandon Hancock**
<Q>Did school mess up the time for you guys at all with the time change? Did it say anything different for y'all?</Q>

**00:03:12 - Brandon Hancock**
<A>When I first logged into the site it said the call was an hour and a half away, and then I refreshed the page and it said 30 minutes. I was just curious if it messed up for anyone else.</A>

**00:03:36 - Brandon Hancock**
Jake, are you a sweater man or a hoodie man?

**00:03:44 - Jake Maymar**
Oh, definitely. Yeah, definitely. That's the best. It's actually starting to warm up though, which is nice finally. Much needed.

**00:03:57 - Jake Maymar**
<Q>Brandon, are you going to get a standing desk — one of those ones where you stand — or a treadmill desk?</Q>

**00:04:05 - Brandon Hancock**
<A>I actually have one right there, but I'm bad and I don't use it as much as I should. My monitor broke so it became my monitor stand. Ten out of ten loved the standing desk but definitely should use it more.</A>

**00:04:29 - Patrick Hutchinson**
The treadmill desk — a coworker always had one and in meetings he was doing this and it would make me seasick just watching him on video.

**00:04:40 - Nate G**
Hey, this is Nate. I'm driving so I can't video, but the chiropractor is telling you to get on your standing desk to get it fixed.

**00:04:53 - Brandon Hancock**
All right, all right — doctor's orders. I can't argue. New monitor, new standing desk. Alright, it's decided.

---

<!--SEGMENT
topic: Authority Accelerator Launch & Lovable for Landing Pages
speakers: Brandon Hancock, Jake Maymar
keywords: Authority Accelerator, Lovable, Cursor, landing page, UI/UX design, AI tools, graphic designers, Mighty Networks, course platform, no-code
summary: Brandon announces the launch of his AI Authority Accelerator program and demonstrates how he built the landing page using Lovable in a fraction of the time traditional design workflows would require. He argues Lovable represents a major threat to UX/UI designers and shares early enrollment numbers.
-->

**00:05:05 - Brandon Hancock**
Alright guys, we'll go ahead and start kicking things off this week. Big updates on my side. I apologize for blowing up your email inboxes on all things Authority Accelerator, but that's been my project that I've been preparing for the past few months. So I've just been kicking it off. Super excited, definitely making progress. I want to share a few technical things and a few things about the program, and then also something that I think you guys will find pretty cool.

**00:05:39 - Brandon Hancock**
Here's the website and everything for the program — I'll drop a link in the chat. But the part that I think you guys will find super cool is I built it all with Lovable [tool:Lovable], Lovable and Cursor [tool:Cursor], and it took me no time at all. I've already know everything I wanted to talk about for the landing page, and then I just went over to Lovable. I'll just show you guys real fast because it's so easy.

**00:06:10 - Brandon Hancock**
Yeah, so you just log in and then you have access to your project right here, and I mean it was so easy to actually build a really nice-looking landing page. I spent three hours trying to use a pre-existing template and I was like, what the hell am I doing? I know how to make websites — I'm just going to go over and use AI. That was the first time going deep in Lovable and I understand all the hype now.

**00:07:00 - Brandon Hancock**
▶ Key takeaway for Lovable: I think it's honestly the biggest threat to UX/UI designers, because in the past you'd have a UX/UI person mock up option A or B, and that would take all week. I just said show me A — don't like that — give me B — don't like that — C — oh my god I love C. And I did it in three minutes. That was one of the biggest eye-openers. Ten out of ten — I would be very scared.

**00:07:57 - Jake Maymar**
Yeah, I come from that background and it's terrifying. I'm still talking to my friends that are still designers and they're doing text-to-video as well — just kind of all the broadcast motion graphics work — I mean it's all going away. And Lovable and really DIY tools — it's amazing what you can do. Actually, when it's my turn, I'll show you kind of what I did with Lovable.

**00:08:10 - Brandon Hancock**
It's amazing. I'm excited to see that.

**00:08:20 - Brandon Hancock**
Only other two things I was going to mention real fast: so far we've got about six people in the program out of the 20 slots, so excited to see that keep going. And yeah, I've tried to make it very easy to hop on a one-on-one call — there are links on the page. Happy to answer questions you guys have.

**00:08:51 - Brandon Hancock**
And final thing — I will stop blowing up everyone's emails on Sunday, and then I'll go back to our normal schedule of like one email every other week.

---

<!--SEGMENT
topic: Jake's Assessment Tool App Demo
speakers: Jake Maymar, Brandon Hancock, Sagar Passi
keywords: Lovable, Supabase, Google OAuth, Next.js, GPT-4o Mini, assessment tool, streaks, dashboard, POC, white-label, Figma, client project
summary: Jake demos a client-built assessment and progress-tracking app featuring Google OAuth, streak tracking, score visualization, and AI-generated improvement suggestions. The group discusses the POC-first development approach, replacing Figma mockups with live prototypes, and the white-label resale model.
-->

**00:09:00 - Brandon Hancock**
Jake, the show is yours, buddy.

**00:09:22 - Jake Maymar**
OK, so I'm just going to share this. My mantra last year was learn. And my mantra this year is build and publish. My goal is every single time I show something, I'm going to show something you haven't seen.

**00:09:41 - Jake Maymar**
So this is an app I built — it's an assessment tool. I got the OAuth working, which was the interesting work — Google OAuth [tool:Google OAuth] and actually a little bit of Next.js OAuth [tool:Next.js] as well. And this is built in Supabase [tool:Supabase]. Basically, it tracks your streak, overall score, shows your strongest area, improvement areas, recent growth, recent assessments. And then what it also does is it takes all this information and generates suggestions on how to improve your score. So here it basically says, oh hey, you can attend this networking event, or you can leverage LinkedIn connections, or you can do these things to increase your visibility — meaningful conversations. It's supposed to be focused on networking ability.

**00:11:43 - Brandon Hancock**
<Q>Very cool — so was it Lovable to generate all of it, or what was Lovable's role?</Q>

**00:11:52 - Jake Maymar**
<A>It's a combination. I still love using Lovable. I also messed a little bit with other tools and Claude [tool:Claude], so I'd copy and paste things into Claude and try different things. Lovable was pretty cool for little animations and stuff. Certain pages it did a good job, other pages not so much.</A>

**00:13:00 - Brandon Hancock**
<Q>I can see you obviously have a generate response — is that Next.js AI SDK, or was that something else?</Q>

**00:13:04 - Jake Maymar**
<A>Yes, that's Next.js AI SDK [tool:Next.js AI SDK], and I'm just using GPT-4o Mini [tool:GPT-4o Mini].</A>

**00:13:17 - Brandon Hancock**
No, very cool. I love that you've connected all the dots. It looks very clean. What's next for it — is it a passion project or turning into something?

**00:13:28 - Jake Maymar**
Well, no, actually this was a client. They wanted an assessment tool. I was like, yeah, I can definitely do that. And now we're adding features to it. The goal is to take this and refine it more into something. Right now it's very generic, and it's going to be really focused into an executive tool.

**00:13:56 - Sagar Passi**
<Q>I have a question — you mentioned it was for a client. How does using the AI tools and wrapping it together work on the production side?</Q>

**00:14:07 - Jake Maymar**
<A>▶ I like to build POCs. We get an idea of what we're building, and that way it saves a lot of time. Once we're pretty happy with the direction and have a solid foundation — these are the core features — then we start talking about actually scaling the correct way and building it out. But right now it's mostly POC.</A>

**00:14:57 - Sagar Passi**
That means you're getting rid of the whole Figma [tool:Figma] design level and just building an actual thing they can play with.

**00:15:02 - Jake Maymar**
▶ Yes, absolutely. The idea is they want to be able to kick the tires as soon as possible, because it's not a product until you have customers. The amazing thing is you hand it to someone and they're like, oh, I really wanted to do this.

**00:15:30 - Jake Maymar**
▶ I think it just saves so much time. And it really creates a great connection with the client because the client's asking for features, you're implementing those features, you're working together, and they start getting skin in the game because they're using the app. They're getting really excited, showing it to friends — you can often get really positive results very quickly.

**00:16:14 - Brandon Hancock**
<Q>Quick contract question — did you flat fee, milestone, or hourly?</Q>

**00:16:24 - Jake Maymar**
<A>With this one it started out as a flat fee. We hit the milestone really fast. The flat fee for a POC was really low — my idea was to get my foot in the door. It's a customer that has a friend relationship, so it's not someone I'm going to charge a high value. But the idea is it was fixed cost, and from there we're adding features and talking about a roadmap, and it's starting to roll into more of a budget, which is exciting. They're going to resell it — it's a white label.</A>

**00:17:30 - Brandon Hancock**
Dude, that is awesome. And hopefully as people join, that also means more changes, more money, all around. That's just a great spot to be in.

---

<!--SEGMENT
topic: LLM Report Generation Pattern & Windsurf Model Selection
speakers: Andrew Nanton, Brandon Hancock, Jake Maymar, Bastian Venegas
keywords: LLM, report generation, markdown, prompt chunking, divide and conquer, Claude 3.7, Claude 3.5, Windsurf, Cascade, LangChain, CrewAI, context window, psychiatric interview, model credits
summary: Andrew describes a recurring pattern of chunking structured report outlines into isolated LLM prompts to maximize output quality per section, then consolidating results. The group discusses model selection in Windsurf — Claude 3.5 vs. 3.7 vs. Cascade Base — and when to use cheaper models for simple tasks.
-->

**00:17:44 - Brandon Hancock**
Andrew, you're up next, man. What's been going on?

**00:17:46 - Andrew Nanton**
Not a whole lot. I had another talk on AI this weekend with the Massachusetts Psychiatric Society. Lots of good questions. It's really interesting — having my entire head in this AI world and then surfacing every now and then to see where people are, at least in my professional circles, with their understanding of AI — it's sometimes a little jarring.

**00:18:23 - Andrew Nanton**
I've also been working on a pattern that I'm finding a lot, and I'm curious if other people are finding this pattern. And then I had a couple of Windsurf [tool:Windsurf] questions for Jake or anyone else who's using Windsurf.

**00:18:44 - Andrew Nanton**
One pattern that I keep finding myself coming back to and writing over and over again: I tend to do more report generation than chat-style stuff with LLMs [tool:LLM]. I have the structure of the report that I'm looking for in markdown format, I'm chunking that up into sections because I want to get the best possible results for each section. In my case, it might be a transcript of an interview that I have with somebody, and then it's running each section of the report against the transcript. I'm trying to cache the transcript — because usually these are multi-hour interviews — and then it'll run a prompt against each section, and then produce a document based on that. After I have each section generated, I'm going through and refining — check accuracy against the transcript, remove repetitive sections, reorganize if needed — things that require the output of these multiple runs.

**00:20:16 - Brandon Hancock**
<Q>So when you say you're generating a section — tell me where I'm wrong — you already have an outline of the document, and then per section you come back and do it again. How is that set up right now?</Q>

**00:20:42 - Andrew Nanton**
<A>Right now the way it's set up is that there is no enduring chat session for each of these. Each prompt is running to generate one section of the report in isolation from all the others, by design, because the output context isn't very long. Each section for all 15 sections is going to end up being a lot longer than I'd want if I tried to do it all at once. So: generate a section, generate a section, generate a section. And then I end up with this document, and from there I use it to proceed to the next phases.</A>

**00:21:49 - Brandon Hancock**
▶ My thoughts on this: I'm generally thinking Cursor [tool:Cursor] is going to become like the new word processor for markdown, because what you'll eventually be able to do is literally highlight a section, run your thing, and hopefully eventually they'll allow you to run multiple at the same time — because that's basically what you're doing with your document. Instead of writing code, you're writing a full-blown document. I'd be very curious if you could start to do a lot of what you're trying to do inside Cursor with some custom workarounds.

**00:22:40 - Andrew Nanton**
Well, I am, but the outline for the report is the thing that is being broken into multiple prompts. It's like: introduction — this section gives an overview of X, Y; medical history — this section focuses on general medical conditions, medications, dose iterations, hospitalizations, et cetera. I am finding that over and over — maybe because I'm just doing the same task over and over — but it seems like this should be a fairly repeatable thing.

**00:23:47 - Brandon Hancock**
▶ Yeah, okay — so to go deeper, the underlying pattern is like divide and conquer and then rejoin. The best example I have of that is doing the flow inside of CrewAI [tool:CrewAI] — basically generate a book outline, there are 10 chapters, here's your focus, generate the chapter, and then at the end rejoin all chapters in order. So it's: divide, split, do work, put all work together. That could probably be a pretty good way to automate what you're trying to do. I'll share that link in the chat.

**00:25:00 - Andrew Nanton**
And LangChain [tool:LangChain] text splitters has a markdown header splitter where you can split by header, which is pretty slick. [link:LangChain markdown header text splitter]

**00:25:06 - Andrew Nanton**
And my Windsurf question is: <Q>what models are people using? I saw some chatter on Reddit that Cascade Base is pretty good, but I've been sticking mostly to Claude 3.7 [tool:Claude 3.7] — not the thinking one, just the standard one. I'm wondering where and when and why people are reaching for different models, because it would be nice to use one that doesn't eat into my credits. I just trust Claude, so that's what I'm sticking with.</Q>

**00:25:48 - Jake Maymar**
<A>Yeah, I'm using Claude. I'm actually using 3.5 [tool:Claude 3.5]. I was using 3.7 and it had some issues — 3.5 is pretty rock solid. But yeah, it definitely burns the credits. For fixing type errors and simple stuff, sometimes you can try the cheaper o1 models — o3, o3 Mini [tool:o3 Mini] — on things. But I find myself using Claude most of the time.</A>

**00:26:42 - Bastian Venegas**
<Q>What's the issue with your current workflow — is the output not what you expected?</Q>

**00:27:00 - Andrew Nanton**
<A>Oh, that part is going okay. I'm just wondering if I'm missing out by not choosing other models, because I've just been sticking to what works, which has been Claude. I actually jumped to 3.7 and haven't had any issues.</A>

**00:27:29 - Bastian Venegas**
▶ I found that Claude 3.7 is really good — it has a pretty good taste when it comes to words and being like a co-writer. I've used it for formal documents and communications with clients, and it's really better than the other models. It's more stable — different from the thinking models, which are really hard to steer. I can talk to you more about draft-writing or pre-processing with a specific tool — I'll send you that at the end.

---

<!--SEGMENT
topic: Patrick's Survey Analytics Tool — Lens
speakers: Patrick Hutchinson, Brandon Hancock, Sagar Passi
keywords: Lens, survey analytics, Stripe, dynamic follow-up questions, sentiment analysis, School, Mighty Networks, webhooks, Tavus, AI avatar, course creators, testimonials, pulse surveys, Mom Test
summary: Patrick demos Lens, a post-learning survey and analytics tool near launch, featuring dynamic follow-up questions, sentiment analysis, and AI-generated recommendations. Brandon provides targeted feedback on positioning for course creators — emphasizing testimonial capture and mid-course pulse checks — and recommends the Mom Test approach for customer discovery.
-->

**00:28:16 - Brandon Hancock**
Patrick, you're up next, man.

**00:28:24 - Patrick Hutchinson**
Hey, so yeah, just a couple quick things to share. After you recommended I look at kind of casting services almost, I actually put together this — it took me six minutes, not three minutes, using just Cursor. So I did put together a kind of services overview.

**00:28:49 - Brandon Hancock**
Dude, that's beautiful. It worked out okay.

**00:28:52 - Patrick Hutchinson**
So this was really — as a reminder — I was thinking about casting a wider net instead of focusing just on medium businesses or enterprises with my survey analytics tool. It was really, hey, are there creators publishing courses where this could help them boost their revenue as well? So that's what this is aimed at.

**00:29:26 - Patrick Hutchinson**
But as far as the actual tool itself — this is it, Lens [tool:Lens] — I'm really close to launching now. I'm going through Stripe [tool:Stripe] and looking at my different features and linking things out at the different tiers. This is kind of how it's working: it starts off with you creating a survey, it has dynamic follow-up questions based on what people enter, you can generate surveys, and this is based on the point of view I've built into the model as far as how to build a good survey. It also reviews them to help people build better post-learning surveys to improve their course design, improve engagement, and give some recommended actions. Then on the analytics side, it's all about rolling things up into what I call lenses that help people categorize where things are good — whether that's application impact, environment, etc. And it also does sentiment analysis on open text questions.

**00:30:33 - Patrick Hutchinson**
One ask from this group: those that have a School [tool:School] community or maybe a Kajabi [tool:Kajabi] or one of those — I'm interested in what kind of data can come out of those because I don't have that. School has webhooks. I'd love an opportunity to test some of that so I can plug in and test launching a survey after a course.

**00:31:07 - Brandon Hancock**
So I want to drop quite a few different pieces of feedback on this because I definitely love what you're doing, but I could share some pain points because I think I'm slightly in the target audience.

**00:31:24 - Brandon Hancock**
Here's what would be most valuable to me, based on doing the last course I did: a course creator wants to sell more courses — that's what it comes down to.

**00:31:48 - Brandon Hancock**
▶ So how do I sell more courses? I build better courses. And testimonials — that's what I need help with. If I was to wave a magic wand, it would be a software platform that upon course completion asks a post-completion survey — kind of like you're doing — where people say did you like it, what did you not like, what would you change. It puts that all into a platform for me to see what I should change, do better, tweak. It would be cool if there were checkpoints as well — instead of waiting for somebody to go through 15 hours of course, it'd be nice to have touch points at hour two, five, ten.

**00:33:00 - Brandon Hancock**
▶ Outside of that — pre and post — asking somebody where they're at before they start and then comparing to after, and you can even show them where they've made progress. Honestly, it sounds like you shouldn't tie a form to only post-course — you should be able to create any form that anyone could plug in at any time.

**00:33:17 - Brandon Hancock**
And another area I've been talking to some folks about is employee pulse. Because of the sentiment analysis stuff you have built in, it's really good at deciphering pulse data — like, what's your experience like working at this company?

**00:33:36 - Patrick Hutchinson**
Yeah, I have that built in as well. And I've been experimenting with Tavus [tool:Tavus] a bit — turning these surveys into actual conversations with AI avatars, which is actually looking pretty cool.

**00:33:46 - Brandon Hancock**
<Q>Is it expensive?</Q>

**00:33:47 - Patrick Hutchinson**
<A>It's pretty cool. The model is like you join a Zoom call almost. I was able to just create a prompt for it out of my survey, and it basically lays out the questions and turns it into an interview. It'll do follow-up questions on its own. And through the webhooks, it'll send me back a call when it's converted into a transcript. So I just grab the transcript and line it up with my survey and fill it out.</A>

**00:37:42 - Sagar Passi**
<Q>Can it mimic yourself, or is it pre-trained?</Q>

**00:37:45 - Patrick Hutchinson**
<A>I believe they have that, but I haven't really dug into that part of it yet.</A>

**00:38:00 - Brandon Hancock**
I'm not 100% sure. Yeah, full face renderings potentially. If you make a Sagar AI, please send it over to me.

**00:38:27 - Brandon Hancock**
▶ Final advice, Patrick: focus. This is like the Mom Test book [link:The Mom Test by Rob Fitzpatrick] — the more course creators you can talk to and the more common problems they all say, like, one of the most important lessons from that book is abandon all assumptions going into the test. Write down your assumptions and you will quickly find out, as you have more conversations, okay, seven people said this and they'd actively pay for a solution. So you kind of get to follow the problems and the money for building stuff.

**00:39:38 - Brandon Hancock**
▶ Two main things: testimonials and pulse checks — those are the main things I think would be very cool, at least for course creators.

---

<!--SEGMENT
topic: Asako & Aaron's AI Business Companion App
speakers: asako, The Dharma House, Brandon Hancock
keywords: AI companion, RAG, knowledge graph, small business, solopreneur, Slack, Notion, Gmail, HubSpot, LangChain, LangGraph, Agent Inbox, Superhuman, go-to-market, ICP, executive email assistant
summary: Asako and Aaron (The Dharma House) present a collaborative AI companion product for small business owners and solopreneurs, featuring RAG retrieval and graph-based correlation. Brandon provides detailed go-to-market advice: target funded tech startups, integrate with Slack/Notion/Gmail/HubSpot, lead with an executive email assistant use case, and implement a human-in-the-loop approval inbox.
-->

**00:39:40 - Brandon Hancock**
Alright, Asako, you're next. What cool project are we working on?

**00:39:46 - asako**
So I just started working with Aaron. I think he's here. I was building an AI companion for a small team with mid-size owners who have a lot of operational tasks and cannot focus on key strategies. So I just made a UI for the product.

**00:40:18 - asako**
This is the UI top page that I made, and you can chat with each agent. Right now I only have a mockup and I'm trying to connect with the backend to do some simple drag operation. I wonder if Aaron can talk a little bit more about the backend he's working on.

**00:40:50 - The Dharma House**
Hey team. Yeah, Sam and I have kind of connected powers and we're working on this on the backend. So far, RAG [tool:RAG] retrieval is working well. I did reincorporate the graph and I'm able to show some solid correlation. I just got one bug that popped up yesterday — I'm working on it, but I think I'll have it done by the end of the day and we should be able to demo a functional front and back end.

**00:41:43 - Brandon Hancock**
So excited. You're flying. I love it. Thoughts on positioning and who you're going to target — like who are your first ten customers?

**00:42:35 - The Dharma House**
The idea is the small business, the new business, the budding business that needs a tech stack that covers general business operations. And maybe balance that with a solopreneur that has two or three ventures — several operations and several businesses — that they want to be able to manage or see a dashboard around and interact with the data from those businesses at the same time.

**00:43:45 - Brandon Hancock**
All right, I'm going to go real fast and just brainstorm with you because I think this is in such a cool spot.

**00:44:00 - Brandon Hancock**
▶ We want to build things for people who have money, because we want to get paid money ourselves. So if I was to pick any CEO, I would strictly want to focus on tech-enabled executives — startups that have funding. They have money to burn and they have to move fast. Speed is everything to them — they're literally fighting for survival.

**00:44:36 - Brandon Hancock**
▶ Set up an ideal customer profile: they are a startup with less than 100 people, they are cash flush, speed is the number one most important thing. What tools are they using? Slack [tool:Slack], Notion [tool:Notion]. And they're most likely using Gmail [tool:Gmail]. Boom — you have your three major integrations right there, focused on that customer.

**00:45:18 - Brandon Hancock**
▶ What do they want to do? They probably want some sort of knowledge base — great, Notion, you're leaning on that. And then you could probably pick one to two tasks to automatically automate. Executive email assistant is the first thing that comes to my mind. Make that insanely easy to train and set up some sort of relationships — I am boss, here are my three team leaders, here's my CTO, CFO, COO. Set up that org chart so it understands context in all communications.

**00:46:00 - Brandon Hancock**
▶ They're probably using HubSpot [tool:HubSpot] if they're a startup. So those are the core integrations: manage my team, manage my customers, have an internal doc, and communicate via Slack and Gmail. If you told any tech-enabled startup, I can help you — here's what onboarding looks like and by the end of onboarding here's what you're going to be able to do — let's make that desired output as shiny as possible. I'll be able to cut your email time from ten hours a week to one hour. You just gave them back nine hours of their life.

**00:47:03 - Brandon Hancock**
▶ They're probably using some sort of internal task management tool — Linear [tool:Linear] if they're software developers, Monday [tool:Monday] or Asana [tool:Asana] if they're not. Integrate those tools and you're golden. You can start with email and branch from there. You just got to get your foot in the door.

**00:47:48 - The Dharma House**
No, yeah, that's great. I love every bit of that. We were talking earlier today — is anybody emailing Cursor? I got an incredibly fast response and it was about my issue — faster than I think a human could do, the speed at which it returned my email and with the accuracy. It was kind of up the alley of what I want as one of our first communication tools.

**00:48:23 - Bastian Venegas**
I think they may be using Superhuman [tool:Superhuman] — I'll link it in the chat.

**00:48:36 - Brandon Hancock**
▶ One of the most important problems agents are going to face is they're going to do the job 100% of the time sometimes, and 90% other times. So what actually needs to happen is you need to create a human-and-agent inbox — your agent is going to do as much work as it possibly can, and then it's going to ask for human approval before sending it off. LangChain [tool:LangChain] built a tool called Agent Inbox [tool:Agent Inbox] — it's similar to what you're building. They made a full-blown executive email assistant, but it was just to showcase LangChain and LangGraph [tool:LangGraph]. It was not meant to be a commercial tool, so I would steal as much inspiration from them as possible and take integrations to the next level.

---

<!--SEGMENT
topic: Sagar's Agency Marketing & Niche Strategy
speakers: Sagar Passi, Brandon Hancock, Andrew Nanton, Bastian Venegas
keywords: MCP, CrewAI, AI agency, LinkedIn, TikTok, niche marketing, ICP, content strategy, pain points, export button framework, AI wrappers, recommendation engine, consultant
summary: Sagar shares updates from AI networking events including discussions about MCP and RAG knowledge management, then asks for advice on content marketing for his AI software agency. Brandon and Andrew advise picking a specific niche, leading with outcome-driven messaging rather than tool names, and positioning as a consultant-implementer hybrid.
-->

**00:50:11 - Brandon Hancock**
Sagar, you're up next, man. What fun products have you been working on?

**00:50:15 - Sagar Passi**
So this week I went to a few AI events. One of them was from Pedantic, and one of the founders was doing a talk on what they built, and another startup was using them and instead of writing in Python, wrote it in Go. So it's quite interesting about what was happening in the space.

**00:50:36 - Sagar Passi**
I met this gentleman who was building a lot of RAG [tool:RAG] kind of applications, and we had an interesting conversation in the pub talking about what happens with RAG over time — if knowledge gets updated, how does the agent or the information get archived and sentiment and all this stuff. That went way over my head, but it made me think about how we should be thinking about stuff.

**00:51:04 - Sagar Passi**
Apart from that, I don't know if it's been on many people's feeds, but on LinkedIn I'm seeing a lot of things about MCP [tool:MCP], and I guess that goes with CrewAI [tool:CrewAI] and agent framework tools. If anyone has any hints on that, I would like to connect on that bit.

**00:51:23 - Sagar Passi**
And the last thing I'm trying to work on is a bit more social proof of AI and how all this noise can be cut to help business value. So I'm trying to build a new LinkedIn post and TikTok post. If anyone can give me ideas of what people might find interesting, that'd be appreciated.

**00:51:43 - Jake Maymar**
About MCP — I believe you can build them now in Cursor [tool:Cursor]. They're fairly straightforward.

**00:52:00 - Brandon Hancock**
It's a really, really nice framework. I think it's going to be a standard — actually it probably already is a standard. And Manus [tool:Manus] — I wish I had gotten access to that. I applied, I'm waiting for it. If you want to get it before me, please let me know.

**00:52:23 - Brandon Hancock**
<Q>Sagar, quick question — diving deeper into the post — would you elaborate a little more on what you're trying to do when you say create the post?</Q>

**00:52:43 - Sagar Passi**
<A>So it's to promote our software agency. We build AI wrappers and applications. Our marketing guy mentions that you should post about becoming an expert in AI and kind of into the course you're providing. The block I always have is that I am so deep in the trenches of AI and I struggle to come back to the surface of what people are actually asking. People talk about these high-level concepts and you know all the answers, but it's just engaging the audience of people coming into AI and this tech stack. What burning questions do they have that you've found with your conversations?</A>

**00:53:33 - Brandon Hancock**
<A>▶ The simplest one is: what can AI do for me? That is the main question they have on the top of their head. And every type of customer is coming in with a different type of question or different needs. So what I'm doing — and I'd definitely recommend you do the same — is pick a general niche. For example, I picked wedding venues because my buddy owns one. They're cash heavy, event driven, operationally simple — check, check, check. Very easy to go off and incorporate solutions for them. Now, AI is something very different to them than it is to someone in a completely different market. To them, AI is strictly operations, management, sales.</A>

**00:54:44 - Brandon Hancock**
▶ If you're everything to everyone, you're almost nothing. If you're too generic, anytime you shout, it's going to be meaningless. The flywheel I advocate for — and talk a lot about in the AI Authority Accelerator — is: just pick someone, pick a niche that you serve. Identify the problems and start generating valuable solutions. The second you build a solution and showcase it to the world, other people resonate because they see, oh my god, that is valuable — I'd like that too. But just shouting random things like "we do MCP" — that's meaningless to most people. MCP is something you as a developer should know about to implement a solution, but the average person could care less. They're just learning what ChatGPT [tool:ChatGPT] is.

**00:56:00 - Brandon Hancock**
▶ So the flywheel: pick a niche — someone who has money — and then as aggressively as you possibly can, solve their problems. And as you're doing it, document what you've done and showcase it to the world, because you're going to be like a magnet — people are going to come and ask you to do the exact same thing.

**00:57:02 - Andrew Nanton**
▶ A lot of the people I'm talking to are not tech savvy. When you start saying anything about AI, if they know anything at all, it's that they've heard of or maybe poked at ChatGPT, and often they're trying to use it like Google. So I think jumping immediately to: what are the most tedious parts of your day? — those are quick answers for most people. And often these really mundane, thoughtless tasks are a great fit for AI anyway. You're immediately solving a pain point for them. And then you can backfill that with information about AI. Jarring them out of the ChatGPT frame as soon as possible is the right way to go.

**01:00:00 - Brandon Hancock**
▶ Final thing — this is what I did recently and feel free to steal it. When going into one-on-one sales, you are part consultant, part AI implementation. No one's going to walk up to you and say, "have you heard about the new MCP thing, I'd love to set that up in my new business." What they're going to say is: I have problems, you seem like a guy who knows about AI, what can I do, can you help me? The name of the game is education. You're going to educate them on what's possible, and then from there you can segue into, oh by the way, if you're interested in any of these, I can build all these solutions — which one is most appealing to you?

**01:01:00 - Brandon Hancock**
▶ Going into one of these businesses, I would break it down into three areas: leads and sales, marketing, and operations. The closer you are to making leads and sales, you'll make more money. Operations is just cost cutting and saving. If you could help someone bring in another $10,000, they're going to pay you more than if you could make their weekends a little less hectic. Rule of thumb for that.

**01:04:00 - Bastian Venegas**
▶ Paul suggested a great framework: try to spot anywhere you see an export button on any software that people use, because that means usually the worker will need to carry their work to another software or another person to complete a workflow. Those are sections that break the flow and could take hours. That's a great way to make something the user will notice because it changes how they work.

---

<!--SEGMENT
topic: Paul's LinkedIn Lead Qualification with Perplexity API
speakers: Paul Miller, Brandon Hancock, Jake Maymar
keywords: Perplexity Sonar, Perplexity Sonar Pro, LinkedIn Sales Navigator, Pipedrive, MongoDB, lead qualification, web scraping, Apify, Firecrawl, Apollo, cold outreach, Instantly, ABoot, CRM
summary: Paul describes a lean lead generation pipeline: using LinkedIn Sales Navigator and the ABoot scraping tool to pull company lists, storing them in MongoDB, then enriching and pre-qualifying leads using the Perplexity Sonar Pro API — all for approximately $10 in API costs. Brandon highlights this as a replicable agency pattern and recommends Instantly for cold outreach follow-up.
-->

**01:07:31 - Paul Miller**
Hey guys. In the last week I've been in the day job, which is a little boring but it pays the bills, pays the mortgage, keeps the wife happy. So that's kind of the focus. But I came across something very interesting that touches on some of the stuff you've been focused on, Brandon — managing your customer funnel.

**01:08:14 - Paul Miller**
As many of you might know, I've got a base business that pays most of my costs. It's a SaaS startup I started with a couple of other guys about 19 years ago — a CRM [tool:CRM] product we sell to consumer goods companies to manage merchandisers and salespeople going into retail outlets. I had my board members say, look, you've been a bit distracted in the last month — we need to see the sales funnel boosted a little bit.

**01:08:52 - Paul Miller**
So of course I put my AI hat on and think, how can I do this with the least amount of effort in the coolest possible way. To cut a long story short: I've got a base CRM tool — we use Pipedrive [tool:Pipedrive] because it's simple and easy. I've got a good basic set of people I know in the industry, and I thought, well, I want to replenish this — grab as many from LinkedIn Pro as possible — but then qualify leads using AI.

**01:09:48 - Paul Miller**
▶ So rather than writing a whole app with CrewAI [tool:CrewAI] and doing agents and doing something complex, I just pay for the Perplexity Sonar Pro API [tool:Perplexity Sonar Pro], and I have a set of questions that pre-qualify leads. For the cost of a premium LLM model, it's doing everything for me.

**01:10:25 - Paul Miller**
▶ It's taught me a lesson that while you can get to the basics and make agents that do everything, you can save a lot of time and use things like the Perplexity API. There's the cheaper Sonar model [tool:Perplexity Sonar] for the tokens, or you can go up to Sonar Pro and not only get context back but also get it to create the links that feed that data — so you've got insights you could look at later.

**01:11:14 - Paul Miller**
The context I used was: I want to come up with a list of companies I should talk to. I'm looking for certain types of companies that have certain types of roles, of a certain size. As many of you know, you can't directly search LinkedIn for this, but somehow with Sonar Pro they do it. If you're wanting to understand a community or understand companies and the insights and leads and opportunities for those companies, this is a wonderful way to do it.

**01:12:00 - Brandon Hancock**
<Q>I have a few questions — from my understanding, I did not know Perplexity could go on LinkedIn. I thought that was not allowed. Is it working in your case, or is it just straight Perplexity to LinkedIn?</Q>

**01:12:17 - Paul Miller**
<A>I don't know how it does it — it seems like a black box. I'm not saying to go to LinkedIn. My questions are like: does this company employ people doing this kind of role? How many do they employ? And in the results set that comes back, it's looked at LinkedIn, it's looked at job hiring sites, and it's pulled all this data together. Which is like, wow.</A>

**01:13:00 - Brandon Hancock**
That's the reason I was going to ask — I was curious if you were using Apify [tool:Apify] or something else. Like, there's a lot of tools that you can just speed-run scraping. And I don't think enough people realize — just raw scraping, something people have needed since the internet has existed, is still super powerful. The amount of times I get asked, can you help us scrape — and now scraping is even more powerful because you get to go to the next step, which is qualify or filter and provide meaningful insights instead of just here are 10,000 leads, good luck.

**01:14:00 - Paul Miller**
But it's simple — keep it simple, stupid. I'm going through an extra level of qualification. So it came up with a list of companies I should talk to, and then I started looking at those with an extra level of filtering using the typical qualification questions I ask. I went and got it to go a higher level in Perplexity on the API to get deeper knowledge. I started with Sonar, then went to Sonar Pro. You can do 150 calls per minute, so if you've got quite a big list of companies to trawl through, it's pretty good.

**01:15:02 - Jake Maymar**
<Q>Curious if you can share a price range — how is your cost?</Q>

**01:15:12 - Paul Miller**
<A>I'm dealing with a pool of about 2,000 companies. I think I've spent about $10 US on the API queries. It's not expensive at all.</A>

**01:15:49 - Jake Maymar**
That's amazing. That's going to wipe out some serious companies very quickly.

**01:16:00 - Paul Miller**
What about Firecrawl [tool:Firecrawl]? They've got this new API type where you do an LLM-type search — you say, okay, I've got this company site, I'm looking for this data across it, and it'll crawl the whole site and pull it all out for you. But I can't be bothered engineering for that, and it's a bit experimental. Perplexity does all this really well, and I just couldn't believe how reasonably priced their model was.

**01:17:15 - Paul Miller**
So I've looked at Apollo [tool:Apollo] and a few other things, but basically I'm using LinkedIn Sales Navigator [tool:LinkedIn Sales Navigator], which gives me access to all the power of LinkedIn search on steroids. It gets the pool of potential individuals and the companies those individuals are connected to. I use the tool ABoot [tool:ABoot], which pulls using my key — because LinkedIn is so blocked — it's a very cheap way to pull all that list off LinkedIn. Then I put that into a MongoDB [tool:MongoDB] database, and then I go through the MongoDB database using the Perplexity API and enrich that data to pre-qualify what leads make sense. It took me a couple of hours yesterday and it's done.

**01:18:09 - Brandon Hancock**
▶ Quick note for all people wanting to do more agency work: Paul just gave you an idea that you could go off and apply to any business.

**01:18:09 - Brandon Hancock**
I'm sending three or four videos on Instantly [tool:Instantly] in the chat because they're crushing it on YouTube right now. [link:Instantly cold outreach YouTube videos] If anyone's planning on doing any cold outreach whatsoever anytime soon, these four videos broke my brain. I would 100% recommend watching them. Their tool has a ton of AI integrations and they just make it so easy now.

---

<!--SEGMENT
topic: Maksym's Car Dealership AI Sales Training Launch
speakers: Maksym Liamin, Brandon Hancock
keywords: Flutter, AI sales training, car dealership, Latin America, voice notes, white-label SaaS, manufacturing sales, look-alike markets, forensic psychiatry, Andrew Nanton, launch
summary: Maksym announces the successful launch of an AI sales training companion for the largest car dealership group in Latin America, built in Flutter, with 500 users onboarded on day one. Brandon advises on expanding to look-alike markets — particularly high-ticket manufacturing sales — and discusses the white-label SaaS opportunity.
-->

**01:20:37 - Brandon Hancock**
Maxim, you're up next, buddy. Where are we calling from?

**01:20:41 - Maksym Liamin**
Hello everybody. Calling from Mexico City, so I'm back from the resort. First of all, congrats, Brandon, on the launch. I've seen it. It looks amazing.

**01:20:58 - Maksym Liamin**
OK, and from myself — same as you, we had the launch actually basically yesterday. So it was like a call to the director so that they accept all the work, and today already the first batch of 500 people joined it.

**01:21:13 - Brandon Hancock**
So it's going really good. And Flutter [tool:Flutter] is doing all the job and it doesn't break. So I'm very, very happy that it runs smooth.

**01:21:26 - Maksym Liamin**
I mean, I was excited, but not nervous. Even if it crashed, I know that we're always online so we can fix it in minutes. So it shouldn't be a problem.

**01:21:46 - Brandon Hancock**
Yeah, and then it's also growing — 500, like every day.

**01:21:51 - Maksym Liamin**
Yeah, up until around three to four thousand, maybe a little more. And then we'll see how it goes.

**01:22:00 - Brandon Hancock**
<Q>Any initial feedback so far — any positive, any anything?</Q>

**01:22:04 - Maksym Liamin**
<A>We already gathered a lot of feedback from the testing phase because we had about 150 people testing for basically the whole month before the launch to make sure we have all the features and everything is right. Right now I hear only positive stuff and everybody is enjoying it. Everybody likes the voice feature — you can send a voice note instead of typing. I think this is the most used feature right now. Everybody prefers to just quickly record their question and get the answer instantly.</A>

**01:23:00 - Brandon Hancock**
▶ I think the fact that you could easily go off and just say, I could help your sales team level up — I could help make every one of your sales agents a world-class sales agent — that's an easy yes for so many businesses. And every time you do it you get to charge more because you have more social proof or demand. And after doing it for a few people, you can just turn it into a white-labeled SaaS. I think really hard about what's the best way to maneuver on this one to maximize your upside potential.

**01:23:33 - Maksym Liamin**
Yes, that's very true. And it's very good that we started with the first customer being basically the biggest dealership group in Latin America. So it would be easier to go to other countries down the way, and also expand both horizontally and vertically. And there's also the opportunity with the actual car manufacturer — it's directly correlated with this one because they're kind of working together. So if we get that one, then we can distribute it even more across basically the same groups and the same manufacturing companies, but in the whole continent.

**01:24:17 - Brandon Hancock**
▶ Yeah, I mean, also — just to think beyond cars — if you look at a lot of my friends, they're in engineering sales and they're selling machines that are millions of dollars. I would honestly look up the chain as well. Selling a $100,000 car is awesome, but helping sell a machine that's a million, $10 million — that sales job is very stressful, has to be very knowledgeable. So I would also just look — you've struck gold. Now we can maneuver to different areas. I would really think about how do you go up-level — in this case, sales engineering with higher-ticket items. And there are so many manufacturing companies. I would throw this into ChatGPT [tool:ChatGPT] and say, hey, what look-alike markets are there out there? Do it for yachts, dude.

**01:25:56 - Maksym Liamin**
That's really good advice. Let us just take a little with this one, because it hasn't even been two or three months with this project. And for the other project I'm also doing — the one with Andrew — the deployment is pretty soon, I hope this weekend. I'm actually super excited about this project because it's an actual complex product that makes me think super hard for every single feature of the pipeline. It's starting to look more and more like Cursor [tool:Cursor] but for forensic psychiatrists, with a lot of human-in-the-loop and all the verifications.

**01:27:02 - Brandon Hancock**
Dude, absolutely love it. Crushing it on all fronts, man. Please just keep us posted.

---

<!--SEGMENT
topic: Cyril's Job Interview Success & Technical Interview Prep
speakers: Cyril I, Brandon Hancock, Bastian Venegas
keywords: Self-Made Millennial, technical interview, LeetCode, AlgoExpert, object-oriented programming, whiteboard interview, Python, junior developer, interview prep, CV, London
summary: Cyril reports a highly successful behavioral interview for a junior developer role in London, crediting the Self-Made Millennial YouTube channel for interview structure. The group advises on technical interview preparation — emphasizing OOP vocabulary, whiteboard problem-solving communication, and AlgoExpert for algorithm practice.
-->

**01:27:18 - Brandon Hancock**
Alright, Cyril, how was the interview?

**01:27:23 - Cyril I**
Oh my god, I can't even express how grateful I am for Self-Made Millennial [tool:Self-Made Millennial]. This was really good for the whole interview, because I watched like five, six, seven videos, pre-made all the answers. I went to the interview, first minute was the lady telling me about the company. Then she asked me one question: tell me about yourself. And just because Self-Made Millennial gave such a good structure and such a good answer, by one answer I'd answered like six or seven of her questions. After I finished my tell-me-about-yourself answer, her jaw dropped and she was like, I'm not even sure that you'll be interested in our role because it might be too simple for you. Like, we just don't feel like we need to waste your potential.

**01:28:20 - Cyril I**
After that, she asked me about my projects. I dived deep into them once again due to Self-Made Millennial guides — with proper structure, problem-situation-result — it literally just carried me. First, it's a very good experience because now I know how an interview goes and what examples I need to include. Secondly, the way I introduced myself — my first interview — and the outcome is that the interviewer is telling me I'm too good for the role.

**01:29:00 - Cyril I**
So yeah, I've passed the initial interview. The next stage would be a technical interview, which would be either a coding challenge or a technical interview on Zoom.

**01:29:20 - Cyril I**
<Q>So that was actually my question. On the last call you told me about the car park problem and to revise some things. Are there any other pieces of advice for the technical interview that you can give?</Q>

**01:29:36 - Brandon Hancock**
<A>Because what's the role again? I'll put it — it's for junior, so I'll find — okay, yeah. In a junior role, the main thing that will most likely be asked is just to see you solve a problem. And probably object-oriented programming. That's what I would ask about. I would deeply understand — I think I sent you over another guy as well — Arsh, yeah, NeetCode [tool:NeetCode]. I'll find it and send it over to you. I would just watch some of his Python stuff because he goes pretty deep. The biggest thing when interviewing a junior candidate — the way they're able to communicate ideas — if they can only say "class" and "function" and can't say any other words, I'm like, ooh, I don't really know if you know how to code or if you just kind of hacked together some stuff in the past. I don't know if you could build a project that works with other developers.</A>

**01:31:12 - Brandon Hancock**
▶ The more you can communicate like: when building out this class, I would like to set up an interface or an abstract class where I know each concrete instance of this class is going to do this — I'm instantly seeing green flags because I know you can speak my same language. If you only say "function" and "class," everyone that goes through Code 101 at college can say those two words.

**01:31:49 - Brandon Hancock**
▶ And Bastian brought up a good course — AlgoExpert [tool:AlgoExpert]. I've bought that thing like four times since 2020. Cannot recommend it enough. I do think it would be very good to practice whiteboarding — easy up to medium challenges. If you have a budget, I'd recommend it. If not, you could just look up NeetCode problems — just simple LeetCode [tool:LeetCode] problems — just so you have a framework for tackling problems.

**01:32:21 - Brandon Hancock**
▶ One other tip: whenever you get asked a question, talk. Sometimes people get asked a whiteboard question and they just go mute. In a developer interview, we're not asking just to see if you got it right or wrong — I just want to see how you're thinking. So just talk. That's one of the biggest things.

**01:33:44 - Cyril I**
Thank you very much. And another thing — I received another interview for another role.

**01:33:50 - Brandon Hancock**
Oh my gosh, you're making it rain, dude. Slow down for the rest of us.

**01:33:56 - Cyril I**
Yeah, I don't know what I did. Maybe I adjusted my answers in the applications — Self-Made Millennial made suggestions to my CV — but yeah, surprisingly, without any kind of professional experience, I started landing London interviews. I did it for like two, three months with no responses, made some adjustments, changed the style that I applied to messages, and it just started working.

**01:34:28 - Brandon Hancock**
▶ If I was you, I would just bite the bullet and pay a hundred bucks for AlgoExpert. You're going to learn so much in that course. Clement from AlgoExpert taught me all things data structures and algorithms. It's well worth a hundred bucks because you could study it literally for the rest of this year, and that'll pay dividends for the rest of your software development career. I cannot tell you how many times in my current day job I'm referencing, oh yeah, this is the blank problem from AlgoExpert. So I still use that course years later.

---

<!--SEGMENT
topic: Steve's N8N Telegram-Jira Automation & Go-to-Market Advice
speakers: Steve, Brandon Hancock
keywords: N8N, Telegram, Jira, automation, project manager, RAG, classifier, LinkedIn, Screen Studio, lead magnet, warm network, portfolio building, in-house automation
summary: Steve demos an N8N workflow that connects Telegram to Jira — allowing natural language task creation, assignment, and querying via a chatbot interface — built after interviewing a project manager about her pain points. Brandon praises the approach of building for real users and advises Steve to post on LinkedIn with the N8N template as a lead magnet to start building authority.
-->

**01:42:12 - Brandon Hancock**
Alright, Steve, you're next.

**01:42:19 - Steve**
Yes, thanks. What I'm going to try to do is automate many of the tasks that a project manager does. What I did is I had a call with a friend who is a project manager, and I asked what are the main points, and she said she doesn't have any idea how to use AI. So I just had some questions, I had some ideas. Later, I plugged myself in to do something with those ideas, and I automated many of those ideas that she gave me. So I'm going to share my screen.

**01:46:23 - Steve**
So it's Telegram [tool:Telegram] connected to N8N [tool:N8N]. What you can do is you can create and manage issues in Jira [tool:Jira] — it's connected to Jira. Here you can send emails, provide contacts, meeting minutes, check and display tasks, and so on.

**01:47:00 - Steve**
For example, here — it will connect to the database and it will tell you. So in your N8N setup, are you doing some sort of classifier or router — like, this is a RAG [tool:RAG] request or this is a Jira request?

**01:47:44 - Steve**
And he will try to do it. And it will create a task in Jira. And what it does is this flow: I start here to analyze the input from Telegram. This will get it from text and also from audio converted to text, and then we send it to an agent. Here we have the contacts, the issues in Jira, email agents, and we can add more but now I think it's good enough.

**01:48:27 - Brandon Hancock**
Dude, this is very cool, very cool, man.

**01:48:31 - Steve**
And maybe — so this one: make budget and for tomorrow. And later we should see it here — make the budget — and here it tries to assign, but since the contact is not really a user from this Jira table, it didn't find it and didn't assign it. But if it finds it, it will assign. And you can also ask it: what tasks are due tomorrow? It will also give you that.

**01:49:36 - Brandon Hancock**
I just want to say a few kudos on this, because I love that you built a solution for someone else — so you're already identifying other people's problems. You're building, obviously we can see it in our own eyes, this actually works, you're providing value. And this makes it so much easier if you want to start building in-house automations for companies. This is a very easy way to say, hey, I've already built this for one person, I could do something for you as well. You could easily start to say this could save the company time, and your nice chat interface makes it very easy to set up — all you're doing is connecting N8N and more and more tools so now you can just chat and they can do anything.

**01:51:37 - Steve**
<Q>I don't know — since this is my very first automation, I don't know really how to start. Should I post this on LinkedIn directly, or maybe a YouTube channel, or something like that?</Q>

**01:52:00 - Brandon Hancock**
<A>▶ If your goal is to start implementing this type of solution for other people, I mean you could post this on LinkedIn and give it away — because what that will do is two things will happen: you'll attract an audience of people who want to learn how you did what you did, and you'll also attract an audience of people who want that solution. That's the give-it-away-for-free-but-build-authority approach, which honestly could be a really great play.</A>

**01:52:56 - Brandon Hancock**
▶ There's a cool tool called Screen Studio [tool:Screen Studio] that makes it very easy to record a quick demo — you don't even have to talk, you can just click and it auto-zooms in and out on your screen. So you could make a nice video demo with some examples like you just showed, and say: hey, I just built this cool automation, watch it in action. Here's the template — respond with "Telegram executive automator" and I'll send you the entire N8N thing. That would be a really good way to start getting some eyeballs on you.

**01:53:36 - Brandon Hancock**
▶ For right now for this one, I would go LinkedIn because you could write this up in 20 minutes, package the automation as the lead magnet, and then you'll just engage with everyone that responds to you.

**01:56:23 - Brandon Hancock**
▶ If I was you, Steve, what I would do is directly reach out using your immediate network and just say, I will build you anything. Because what we're trying to do is just get together a portfolio of working automations. We want to build it up so that without a doubt, people know when they hear Steve, they know — oh yeah, he can build automations. So I think you're in the learn-and-prove stage. I would just use your warm network at first. If there's anyone in your family or relatives who owns a business — hey, I will be your number one AI employee, I can help automate literally anything. And after you do it once and you have the confidence, it's just easier now that you have almost like a testimonial to go up and do it for the next one. And each time you're just going to charge more and more and more.

---

<!--SEGMENT
topic: OpenAI Agents SDK Launch & Session Wrap-Up
speakers: Brandon Hancock
keywords: OpenAI Agents SDK, web search, RAG, production agents, AI Authority Accelerator, Responses API, computer use, tool calling, startup opportunity
summary: Brandon briefly showcases the newly released OpenAI Agents SDK, highlighting its simplified approach to building production-ready agents with built-in web search, document retrieval, and computer use capabilities. He closes the session with updates on the AI Authority Accelerator enrollment and encourages members to review the new SDK.
-->

**01:43:28 - Brandon Hancock**
While Steve's gone real fast — any of you guys see OpenAI's agent stuff that just released today?

**01:43:40 - Brandon Hancock**
They released a new feature to where you can basically do production agents. I think this is going to be very game-breaking for the amount of startups that are going to get built on top of this — it's going to be insane. Simply put, this just unlocked so much new value for creators.

**01:44:24 - Brandon Hancock**
▶ Here's what it comes down to: it's a simple agent — OpenAI Responses API [tool:OpenAI Responses API], create — and boom, you're now using a web search ReAct agent. And it's all happening on the OpenAI [tool:OpenAI] side of things. From my understanding, it's like Assistants from back in the day, but even easier. They basically want you to be able to easily search online data with a web searcher, and then also provide your own documents and search them internally. And it can also do computer use [tool:computer use] — which is like, my god, they just keep cooking out new stuff. They never stop. So hard to keep up with.

**01:45:23 - Brandon Hancock**
I'll send you guys the video where they release it and start showcasing it. I didn't fully watch it all because I didn't see it until like two minutes before the call, but I'll send it.

**01:58:03 - Brandon Hancock**
Alright guys, I do have to hop off — I have so many things I have to get done tonight. But with that being said, quick updates: yeah, definitely if you don't get a chance, I dropped a link to the new OpenAI agents that just dropped. It looks very cool, dropped a video to it. Like I said, I've been going hard on the AI Authority Accelerator — almost done, guys. There are a few other things I'll be sending out for the rest of the week. But yeah, if you have anyone that's interested or has questions, please let me know. Always happy to help. We're slowly cruising — we have six so far in the program. Definitely want to keep it small just so we can focus attention and make sure I win in the results that they're shooting for. So super excited, and I'll keep posting as well. If y'all need anything, always a DM away, and I can't wait to see you guys next week.

---

=== UNRESOLVED SPEAKERS ===

- **asako** — First name only; no canonical full name available in alias map. Passed through unchanged.
- **The Dharma House** — Referred to as "Aaron" during the session but raw speaker label is "The Dharma House"; no alias map entry found. Passed through unchanged.
- **Steve** — First name only; no canonical full name available in alias map. Passed through unchanged.
- **Nate G** — Partial name; no canonical full name available in alias map. Passed through unchanged.
- **Cyril I** — Partial name; no canonical full name available in alias map. Passed through unchanged.
- **Paul Miller** — Not confirmed in alias map; passed through as given.
- **Maksym Liamin** — Not confirmed in alias map; passed through as given.
- **Sagar Passi** — Not confirmed in alias map; passed through as given.
- **Bastian Venegas** — Not confirmed in alias map; passed through as given.