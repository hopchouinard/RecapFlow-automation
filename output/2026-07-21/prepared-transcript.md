=== SESSION ===
date: unknown (transcript references "last week" and "next week" relative to recording)
duration_estimate: ~2 hours
main_themes: AgentTask app demo and feedback, community member project updates (meal prep app, AI photo booth, book publishing pipeline, website redesign automation, training generator), tool discussions (Robinhood agentic account, Omni-agent, Claude Code, Codex, Stream Deck), AI consulting and forward deployment

---

<!--SEGMENT
topic: Session Open and Introductions
speakers: Paul Miller, Patrick Chouinard, Alireza Mounesisohi, Marc Juretus, Ty Wells, mdcatc
keywords: community call, California timezone, New Zealand, Quebec, international community, golf, homeq.ai, appliance monitoring, meeting cadence
summary: The call opens with participants joining from New Zealand, Quebec, Canada, California, and other locations. Participants exchange pleasantries, discuss the challenge of scheduling calls across international time zones, and briefly reference prior meeting topics including Ty's home appliance monitoring project. The session host Paul Miller hands the floor to Alireza (Ali) for his application demo.
-->

[00:00:00] Paul Miller: Get to the level of detail.
[00:00:01] Paul Miller: This meeting is being recorded.
[00:00:06] Paul Miller: Hey, Patrick.
[00:00:09] Patrick Chouinard: Hey, Paul. How's it going?
[00:00:11] Paul Miller: Good. Glad to be in New Zealand, not Australia, but back in Australia next week, so backwards and forwards.
[00:00:22] Patrick Chouinard: I understand the, well, not necessarily the travel, but the administrative responsibility, let's say. My own meeting with the notary today, so.
[00:00:41] Alireza Mounesisohi: Patrick. Patrick. Hi, everyone.
[00:00:45] Marc Juretus: Hello.
[00:01:01] Patrick Chouinard: Thank you. Ali was asking to get some feedback on his application on the forum this week, so we're just waiting for everyone to join in and you'll definitely have the time to do your demo.
[00:01:18] Marc Juretus: <Q>Application does what?</Q>
[00:01:22] Alireza Mounesisohi: Should I go now?
[00:01:24] Patrick Chouinard: No, no.
[00:01:25] Paul Miller: We'll wait for people to join.
[00:01:56] Patrick Chouinard: Ali, this is the first time you joined a call?
[00:01:59] Alireza Mounesisohi: No, I haven't. I've been before, but the only thing is I live in California, so the timing is like right at the time that I'm almost like packing to go home, you know, it's like 3 p.m. of our time. It's like, oh my gosh, like have it on Sunday, Saturday, I don't know, 5, 6 p.m. or early in the morning, 7 a.m. This is a time that really is hard to join typically, but yeah, it's done by an East Coaster.
[00:02:40] Paul Miller: So unfortunately that's, yeah, it kind of works for most.
[00:02:47] Patrick Chouinard: Yeah. That's a challenge with an international community. No matter what hour or time we choose, there's going to be somebody who's not going to be happy.
[00:03:00] Patrick Chouinard: I'm in Quebec, but I'm not the owner of the community. Me and Paul are just there to help while the owner of the community is on a larger contract.
[00:03:21] Paul Miller: New Zealand for me.
[00:03:24] mdcatc: And California too. But this is only a problem for me because it's my normal nap time.
[00:03:36] Marc Juretus: Yeah, no, I'm trying to — like I was on the call two weeks ago. The gentleman was just talking, had something to do with cemeteries, and then Ty was doing something with controlling electronic components and turning off refrigerators. What was Ty's one that he was doing? He was turning off an appliance on a specific day, at a month, at a specific time?
[00:03:57] Ty Wells: Want Ty to respond?
[00:03:58] Marc Juretus: Oh, I didn't see he was on. I figured you were at some golf course somewhere.
[00:04:02] Ty Wells: I just got done actually. Just got done.
[00:04:04] Marc Juretus: I was explaining that to somebody at work and they kept asking me questions about it. I don't remember everything you said, man.
[00:04:16] Ty Wells: Well, I can answer now or later. It's up to you. Who's running the call? Paul or Patrick?
[00:04:18] Paul Miller: Yeah. No, I'm running. We'll come back to you, Ty.
[00:04:24] Paul Miller: How was the round? How was your handicap?
[00:04:28] Ty Wells: My handicap's a 10. So the round yesterday was one over.
[00:04:33] Paul Miller: So I shot a 73 yesterday.
[00:04:35] Ty Wells: Today I shot an 85. So there you go.
[00:04:38] Paul Miller: That explains the difference. Yeah. Golf.
[00:04:41] Ty Wells: Golf, right. The flogging. Love it.
[00:04:48] Paul Miller: Right. Well, we have a new chap. He has been on the call before, but he wanted to introduce his application, get some feedback. So, Ali, the floor is yours. Tell us about your app. Give us a bit of background as to what it's for so we've got some context.

---

<!--SEGMENT
topic: AgentTask App Demo Overview
speakers: Alireza Mounesisohi, Patrick Chouinard, Paul Miller
keywords: AgentTask, task management, MCP, Claude, Cursor, Notion, Linear, Jira, ClickUp, AI agents, spaces, projects, notes, crews, claim ID, agent tracking
summary: Alireza (Ali) introduces AgentTask, an AI-native task management platform he built. He describes its core structure — spaces, tasks, projects, notes, and crews — and how it integrates with AI coding tools via MCP. A key differentiator is agent claim tracking, which records which AI agent completed which task on which session. He positions the product between Notion and Linear in the market.
-->

[00:05:09] Alireza Mounesisohi: Sure. Thank you. My name is Alireza. A bit about myself, I have a PhD in AI task management system for robotics in unstructured environments. I got it while building some robots for a space station for NASA at the time. And then I joined a few enterprise companies, and now I'm working for a healthcare company. I'm an AI agent lead of the whole company. And beside that, my family is growing. I was like having an application which I truly believe is going to help the community and myself. So I started building an application. I have experience building a task management system, and with that experience I started building this application.

[00:06:42] Alireza Mounesisohi: Basically it's called AgentTask [tool:AgentTask]. I didn't buy the domain AgentTask as it is — it was really expensive. I didn't want to invest that much money, but basically AgentTask.com is going to be if it lands. So the application is basically helping you get going on your tasks. You can communicate with it, you can connect it to Cursor [tool:Cursor], connect it to Claude [tool:Claude] or any application, and also in itself it has an AI layer that you can communicate with. I'll show you in detail how it works.

[00:07:30] Alireza Mounesisohi: It has something called agent work and agent task, and it has different tiers. So it's like other task management systems, but more simplified, seamless. It's built for users who are really busy, who are having many, many tasks. And basically it has all these structures for different spaces and different task groups, projects — like Jira [tool:Jira], like ClickUp [tool:ClickUp], like all these other task management systems.

[00:08:17] Alireza Mounesisohi: So there are two companies started using this. One of them is Loreo, which basically does detection of sound when you are working in a meeting. And there is .med, which is building agents for other companies, but they got it and they are starting using this application.

[00:08:59] Alireza Mounesisohi: Once you are connecting this application with your AI agents, when they are making progress and working, not only do they update the ticket as they go, they also provide a claim ID and claim information that will be stuck to the tickets they are working on. So at any time you can basically go back and see which task that you have done is done by which agent, on which computer, on which session, on which session name. So you'd never lose the whole idea of where did I do this, when did I do this, which agent made this change to this task. So it records everything and more.

[00:09:45] Alireza Mounesisohi: So, as I said, it connects to Codex [tool:Codex], Cursor, Copilot [tool:Copilot], Gemini [tool:Gemini], Windsurf [tool:Windsurf], Cline [tool:Cline], ChatGPT [tool:ChatGPT], Claude, Claude Desktop — you name it. And also I have basically created the application for desktop Windows, connected to MCP [tool:MCP], and also I have done something for remote MCP, where you just give an MCP remote code and it does all that, connects it without you having to worry about where to configure this MCP. And the mobile application is in process — for both iOS and Android.

[00:11:09] Alireza Mounesisohi: There's a free tier, pro tier, and team tier, and enterprise. Free is like you get three seats, one space, five projects, a thousand tasks. It's four times what ClickUp or Monday.com offer. I have set this bar on free more than anyone — so Notion [tool:Notion], you can go and check them — none of them give you this much on their free tier service.

[00:12:40] Alireza Mounesisohi: And there's an enterprise where basically enterprise customers get the in-house version — I build the whole application in their ecosystem, so if they are sensitive — like if it's related to the Army or healthcare or some sensitive information that cannot leave the infra — this is what I'm offering.

[00:13:21] Paul Miller: <Q>Ali, who do you see as your biggest competitor for what you do?</Q>
[00:13:29] Alireza Mounesisohi: <A>I would say what I have done is in the middle between Notion and Linear [tool:Linear]. So that's how I categorize it.</A>

[00:13:47] Patrick Chouinard: <Q>So something in the middle ground of Notion and Linear. And if you come from Notion or Linear, what are the features that are unique to your platform that I'm not going to get anywhere else? How do you differentiate yourself from Notion and Linear, basically?</Q>

[00:14:06] Alireza Mounesisohi: <A>So I had friends who use Linear, Jira, Notion. They were sick of it. They were like, hey, we are tired. These applications are too much. We need something simple and doing the most. So what I would say, first, on the free tier and all these tiers, my pricing is — none of them can compete. My price is cheaper than all of them. Plus, the interface and usability is non-comparable.</A>

---

<!--SEGMENT
topic: AgentTask Feature Walkthrough
speakers: Alireza Mounesisohi, Patrick Chouinard
keywords: AgentTask, tasks, projects, notes, crews, skills, instructions, kanban, list view, timeline, versioning, Claude, MCP, agent modes, advice mode, execute mode, sub-tasks
summary: Ali walks through the live AgentTask interface, demonstrating task views (list, kanban, timeline, suspended particle view), project management, notes with skill/instruction/note types, and the crews concept — blueprints of AI agents that can be synced to Claude or Cursor. He shows how crews can operate in advice or execute mode and how they can autonomously generate leads, tasks, and project updates.
-->

[00:14:48] Alireza Mounesisohi: So after you log in, there are two tabs on the web. When you have a local install, there is one more tab, which is agent work — connects to your computer, brings the tasks, and you can say, create this document and stuff. But on the web, which is the basic, if you interact — so for example, this is a real one. This is what I'm using day to day right now.

[00:15:23] Alireza Mounesisohi: For example, I have hired the person who's working on my mobile, right? And the easiest way — I always had a problem hiring people and never knowing what they do. So this is just one simple example. I'm using this application and just tell Claude, hey, this is my person I have hired. I want X, Y, Z — go ahead and create the task, the sub-task information, what should be delivered, and what should be done. And it's like — the guy was telling me, I had arguments with every client before, but with you I have never had any problem because you always give me this instruction and I have it.

[00:16:28] Alireza Mounesisohi: From a higher perspective, you have spaces, and in each space, if you are in the team or free tier, you have basically the option to bring more people in. So for example, you can have a personal staff space, your application, your mobile — it depends on how many projects you are working on and how many people should be in those. Of course, for personal and home, my wife is in there. For website and mobile, it's the guy that I have hired. For work, it's nobody other than maybe a colleague. And in some spaces it's just me because I don't want to share information with anyone else.

[00:17:32] Alireza Mounesisohi: In each of them, you get tasks. I have created like 1,700 tasks myself. You get basically the list of the tasks, who are assigned to it. You can create groups. This is what my friend likes a lot, because when you are working with Claude, you can say, create this task and it auto-groups it for you. Other than that, you get all kinds of features on the tables. You get different views like card view, list view, kanban view, where you have like you want to move things from in-progress to done. I have created this intuitive view which is more friendly — doesn't come with the code, but it's more friendly that you can see and update it.

[00:18:28] Alireza Mounesisohi: This is the suspended view, which I created — I wanted to have something where every task is like a suspended particle in this space, and then you can kind of see which part of your application, especially if your application grows a lot. Sometimes I get a headache with it, so it's kind of easy for me to come and look at the task in this view. And there's a timeline view, which is for tasks that have a timeline attached to them. But the easiest one is the list view, which I typically use in my day-to-day life, or table.

[00:19:40] Alireza Mounesisohi: Then there is a concept of projects where basically you define a project. Like I'm thinking about building a knowledge base — customer-facing. And there is a desktop release pipeline hardening. These are the real projects I'm thinking about to add. And basically each project has a type, health, priority, target date, updates, and when you go in there, you can add tasks to it, either create new tasks or add existing tasks, or add attachments and comments to it, as well as linking any existing tasks, projects, or notes to it, and add a crew.

[00:20:40] Alireza Mounesisohi: Then there is a concept called notes, where basically — and this is super strong, one of the strongest things I have baked into this — for example, when I talk with Claude, there are many times that you are doing something and you want to retrieve information. One of the ways you can automate this, instead of having instructions scattered here and there, you can just have a skill where you can say, hey, based on the web note N1, define this work for this person. And in N1, I have defined, okay, these are the tasks, these are the style that I like, and every time this instruction is provoked, you should do this, this, this. And I told Claude. So it knows that every time I'm referencing this document, how to go ahead and create all those tasks and sub-tasks and projects for the people I have hired.

[00:22:11] Alireza Mounesisohi: There are three types: skill type, instruction, and note. Skills are mostly used by the agents. Instructions are something in your application you repetitively try to do — for example, every time you want to run your application, or every time you want to do a certain test. Notes are basically anything you would like to interact with as your reference when you are working in Claude. And you can have Claude update it, and you can also turn on versioning so every time you know how to version it.

[00:23:16] Alireza Mounesisohi: And finally, the crews. So crews are the concept that basically they are blueprints of agents that you would be able to sync with your Claude, Cursor, Cline, every other harness that you are comfortable using. So for example, I have created one for selling my own company. I have a crew that does the feature strategy, ICP strategy, prospect scout. And the way it works is that when you are in Claude and you are saying, hey, I want to do this strategy for my company — I can show you what the result was. The other day I did it and it found like 50 leads for my company.

[00:24:26] Alireza Mounesisohi: And then you can say, hey, out of these, create notes, create tasks, update the projects, update the attachments, etc. And they just work together. And each of them, like a member, like a teammate, will work. And eventually, based on what they are supposed to deliver, they deliver.

[00:25:13] Alireza Mounesisohi: So for example, a prospect scout — it has an instruction and it has options for different modes. Is it advice mode or execute mode? Depends. You want this kind of crew to execute on something or advise — advice is just comments. You can say, do this. And it does a search for you and comes back with advice, like comments that say, hey, I have searched this code base, that's this. Execute does it and updates it for you. That's the difference.

[00:25:43] Alireza Mounesisohi: So you can give different runtimes for it. You can give skills of what tools from the application and from your main application they can access to. And all these are controllable by Claude. So in Claude, you say, hey, I want two crews tomorrow, do this for me. So Claude will generate these crews for you with the proper instruction and also deliverables — what they are supposed to deliver.

[00:26:32] Alireza Mounesisohi: So you can think of it as these four items that initially I have on the launch — tasks, projects, notes, and crews — basically everything that your Claude Code or Cline or any application you are using requires for getting a task done without you being worried about any part. So I'll pause here. Do you have any questions? And then I can show you a bit more.

---

<!--SEGMENT
topic: AgentTask Feedback and Pitch Coaching
speakers: Patrick Chouinard, Paul Miller, Ty Wells, mdcatc, Alireza Mounesisohi
keywords: value proposition, ICP, onboarding flow, demo structure, pitch, target audience, AI slop, workflow story, user journey, task management, competitive differentiation, Jira, Linear
summary: Community members provide structured feedback to Ali on his demo. The core critique is that the product's value proposition and onboarding flow are unclear to a first-time user. Members advise him to use his own agent system to define his ICP, build a communication methodology, and create short workflow-focused demo clips rather than a feature tour. Patrick emphasizes not competing on price and focusing on unique differentiators.
-->

[00:27:06] Patrick Chouinard: If I had something to ask — I see all the pieces, I see the value in each piece, but from the demo, it's really hard for me to say from day one, what's the path that I use to create my first project, create my first task, info, skills, notes, and then hand them over to my agent or my harness to execute? Or do I use the harness to create them? And then where do I set it? Who's going to run them? Because there's a lot of pieces. I just don't know how they fit together in which order.

[00:27:52] Alireza Mounesisohi: Yeah. So there are many flows, right? But honestly, me and everyone else who are using this — one flow is that you come to the board agent and say, hi, what is my high priority?

[00:28:12] Patrick Chouinard: Yeah, but wait a minute, this actually entails that you've already created tasks. I'm day one, I'm getting in. The universe is empty. I don't know how to use your project.

[00:29:05] Alireza Mounesisohi: That's exactly what I was trying to show you. That's exactly what it is. So the second part is that you can come here and click on new and say, like, hey, you can select the project and say, I don't know, cleaning the code base and finding the issues, and then generate title and then assigning and then create a task.

[00:31:00] Paul Miller: I think, Ali, you need to probably focus on using your AI with clarifying the pitch and the comms to your target audience, because I'm hearing lots of really cool stuff in there, but I think half the challenge — for what all of us have got, little projects and different things that we're doing — is how are you clearly showing the value proposition with what you do, not the technical part of it, with your customer base, because it's critical for the success of the product. I can see lots of cool things embedded in there, but working through that, getting us across the line — because look, we're all doing some really cool stuff on the technical side. I think one of the things that has tied the group nicely together is how we have the conversations with the people that we're selling it to.

▶ [00:32:00] Paul Miller: Maybe if you have a think about that and use the AI to look at the market and put a comms wrapper around where your value proposition is — it's hard with some things where you're going into a new space and there isn't really something that does all of the things that you do, but you have to build that to be able to get the application across the line, at least for those initial users.

[00:33:25] Patrick Chouinard: Ali, if I could recommend — use your system to help your system. You have a task manager, so create yourself a task to ask your agent to build a communication methodology to target whoever is your target audience. So if you want to target a single developer, if you want to target enterprise, and address what's different, what are you selling they don't have.

▶ [00:33:54] Patrick Chouinard: Don't compete on price. Price is fine, it's a good argument, but you're not going to be able to compete with the Jiras of the world purely on price because they could come back tomorrow and say, oh, we're going to include our new agent for free for next month. So price is a good entry point, but it can't be the selling point of the application.

▶ [00:34:19] Patrick Chouinard: Focus on what you're bringing that nobody else is. Focus on the workflow that they're going to use from day one. Like, I come in. There's nothing in. I want to know how I fill that. Create that process. And give the task to your agent to help you build them. Because right now you're seeing it from your point of view and you're the creator. So you already have tons of context that in your explanation, we feel that you already know how the application works. So you're skipping over some of the explanations simply because they're obvious to you. But from somebody who hasn't seen the project, sometimes the stuff that you feel is the most obvious is the stuff that would make the most of a wow factor on your audience, so it's just a matter of delivery.

[00:35:07] Patrick Chouinard: I think your platform has a lot of potential. Just have the AI help you wrap the presentation for your target audience, and you might have a very interesting platform to sell.

[00:40:13] Ty Wells: Ali, I'll just add to that, what those guys said — but I mean, this is a group of technical guys. So we build for us, you know, we're building Claude Code or Codex or whatever, but we just build it if we need it. That's sort of what you're doing, but from our perspective now for a layman, right, an actual customer — that's, I think, what you need to do is use your agent to go find out who would be your ICP, right? Your ideal customer profile, and then use that to then target who those customers would be, go through the iterative process, and then create a pitch, a two-minute elevator pitch for your product based on the features of it, and that's what you would create a Loom or whatever, and send out to help you.

▶ [00:41:21] Ty Wells: I think everybody's saying that — Patrick, more so — use your agents to prepare for your audience relative to what. So I'll give you an example. If I was demonstrating your product, I would come on this call and do a quick, hey, you know, what do you guys think about this, blah, blah, blah, right? Try to sort of set and understand where your audience is, and then pitch relative to that.

[00:42:03] mdcatc: I'm kind of in the same boat there with some of my products and the one thing that has helped me was that you need to really identify what the user workflow story is. What is their problem, the user's problem, and then show a small example of how to solve that problem using your system, right? So what is the workflow of creating a project and creating a couple of onboarding tasks to that project and then actually running through a task to completion or whatever? Those are the little snippets that we need to see.

▶ [00:42:52] mdcatc: I'm not using the task program as my main focus of the day, right? I'm using a skill saw. I've got some task lists that I've got to do. Those are the tools of the day. This is just an audit tool that helps me keep it in order. So how do I keep it in order as I'm using the other tools of my day, whatever that happens to be? And that'll help you put a demo together that will ring with somebody.

▶ [00:43:20] mdcatc: That's where I think we're having a disconnect right now — we see all the pieces, but we don't see the workflow of: this is how you create a project, and after we have that project, this is how you add tasks to it, this is how you work through a task, this is how you complete a task. Those kind of things in an actual example. So just pick one or two really small examples that relate to a lot of people and you'll be able to identify some real quick little workflow demos that can be used in demonstrating your product.

[00:44:20] Alireza Mounesisohi: Thank you so much for giving me the chance and also providing all this feedback. All of it resonated. I will make sure that I will add it to the website, this kind of workflow day to day, and also add it to the channel. And if you guys would like to try the application, please feel free to reach out.

---

<!--SEGMENT
topic: Robinhood Agentic Account and Stock Trading MCP
speakers: Marc Juretus, mdcatc, Paul Miller
keywords: Robinhood, agentic account, MCP, Claude, stock trading, market sentiment, semiconductors, RSI, 200-day moving average, investment automation, ServiceNow, Copilot agents
summary: Marc shares his experience with Robinhood's new agentic account feature, which provides an MCP integration allowing Claude to read portfolio data and execute trades in a sandboxed account separate from the main investment account. He rates it 9/10 and explains the setup process, safety isolation, and trading pattern configuration. He also mentions ongoing work with Copilot agents for ServiceNow.
-->

[00:45:13] Marc Juretus: I'm still doing a lot of Copilot [tool:Copilot] agents with ServiceNow [tool:ServiceNow] for work at night and stuff, so I still have my stock traders going and everything. I will say this, though — I'm very impressed if anyone's used it up here with the agentic piece that Robinhood [tool:Robinhood] has added there. If anyone's done that with investing, it's pretty slick how they do it. You create an agentic account, bring down the MCP, and Claude can actually talk to your investments, tell you what your high and your low end is. Anyone gets a chance, I would give that a nine out of ten. I was very impressed with that product.

[00:45:53] Marc Juretus: But outside of that, I'm probably going to be spinning up some more of my fantasy apps for the season right now. I'm probably going to start on some individual projects next week because the season starts in September. It's very interesting how the space has migrated in a year with the code that's generated — when I was writing a lot of it last year, or at least writing it in conjunction. Now I'm not really writing anything anymore. It's just funny where we've evolved in 12 months.

[00:46:19] Marc Juretus: Even at work, we did our first app. We just rewrote our first app from scratch for basically reserving space for the days that you have to come into the office. And it was done completely without any code written. So that was our first delve into that. Using Claude. It was impressive. From everything from the pipelines to Azure and everything, I was impressed. So it's a different world we'll be living in.

[00:46:54] mdcatc: <Q>Hey, Marc, what was that product you mentioned? The one for the MCP for the stock.</Q>
[00:47:09] Marc Juretus: <A>Oh, yeah, that was Robinhood. So Robinhood basically has an agentic piece to it. So if you go up there, they'll give you the information to set it up. It'll give you the MCP code. You put it in either your terminal or inside of the Claude client. And the good part about it is it will not touch your individual account. It can read that information, but it can't do any trading, so it won't take your money. You can throw $500 up there. You can tell it to follow specific trading patterns, and it'll buy and trade for you when things hit on its own.</A>

[00:47:47] Marc Juretus: What I like about it the most — I'll ask a question like, what am I heavy in? What is the market sentiment on some of the stuff of my semiconductors that I own? So that's definitely a different age, right? I'm very impressed with that. I plan on putting a couple hundred dollars up there and letting it run with my trading patterns and see what it does.

[00:48:04] Paul Miller: <Q>Marc, is it the app that I've just stuck in the chat? Is it that one?</Q>
[00:48:07] Marc Juretus: <A>It's just robinhood.com. Yeah, you've heard of Robinhood, haven't you?</A>
[00:48:14] Paul Miller: Robinhood's the trading app if people don't want to start a Schwab account.
[00:48:17] Marc Juretus: That's the one I've used for years. But they have an agentic piece in there, like I stated. I will say I would give that a 9 out of 10 if I was going to give it a rating. It was a lot better than I expected. I was like, this is going to be a nightmare, and it's pretty flawless, man.

[00:48:41] Marc Juretus: <A>No, no, no. You're going to go in there, you'll have a completely separate — it's called the agentic account — and they'll show you how to do it when you go there. You just have to do a couple of clicks and then it sets up, and that account's completely separate. Now, it will have access to your individual account, but you can talk to that. You can't have it trade. It'll just say, okay, you only see three semiconductors, here's the market sentiment on it, here's what they have, this is how much you've won or lost. That's very impressive. But yeah, it can't touch your individual account.</A>

▶ [00:49:18] Marc Juretus: You can basically go up there and give it $500 and say, hey, if it hits above the 200-day moving average, the RSI, whatever your measurables are, you can tell it, and it'll trade for you on its own. So it's pretty slick.

---

<!--SEGMENT
topic: Ty's Meal Prep App and homeq.ai Update
speakers: Ty Wells, Marc Juretus, Patrick Chouinard, Paul Miller
keywords: meal prep app, USDA API, homeq.ai, power monitoring, refrigerator, PRD, spec, requirements, sub-domain, macro tracking, Dashlane AI, phishing warning, fresh domain
summary: Ty shares two updates: a brief mention of his homeq.ai home energy monitoring project (tracking refrigerator power usage), and a new meal prep app he built in a single session for his daughter. He describes his rapid development workflow — capturing requirements via voice, generating a PRD and spec, then executing with no manual coding. Patrick flags a Dashlane AI phishing warning on the fresh domain, which Ty notes is likely due to the domain being newly registered.
-->

[00:49:57] Ty Wells: The monitoring tool you started with is called homeq.ai [tool:homeq.ai]. [link:homeq.ai] You can read about it there.
[00:50:11] Paul Miller: Oh, that was the power thing?
[00:50:14] Ty Wells: Yes. The power — yeah, it monitors the usage on different devices and so forth. So I've got it connected to my two refrigerators if you go to that URL. I'm testing different things to try to make sure that it's doing what it's supposed to do.

[00:51:13] Ty Wells: My daughter yesterday — she meal preps. She wants a meal prep app. And I'm like, I'm sure they exist already. She says, yeah, but you have to pay for them. Like, okay. So I built a meal prep app this morning, gave it to her. So she's all set to go.

[00:51:47] Marc Juretus: I think I got it. It's funny you said that. I have that fitness app that I created. I was going to do a nutrition aspect, but I kind of put that on pause. That's interesting. That's a good idea, though. It was more of, though, when I would put training schedules up for people, I would provide — this is what I want you to eat — as opposed to her, probably what, she's tracking her macros with it?
[00:52:05] Ty Wells: Yeah, she's tracking her macros.

[00:52:25] Ty Wells: She wanted a USDA hookup. She specifically told me to pull it, so I got an API key and threw that in there.

[00:52:40] Ty Wells: So that's — I think that, is that the right, does that work? Yeah, you can sign in, it'll send you a code through email and check it out. So I said, she came home from work, I said, hey, did you check out the app? Nope, I haven't had time to do that.

▶ [00:52:40] Ty Wells: But that's crazy how, you know, you take an idea — because I was, I told her to tell me everything, and I used my limit list to capture everything she was saying, I didn't have to worry about it. And I pull that down, and then I use that to generate PRD, generate spec, generate plan. Execute. I didn't do anything. After I pulled the requirements and confirmed, that was the end of that. Built it out, set up the sub-domain, everything. I didn't have to touch it once I released it.

[00:53:57] Patrick Chouinard: Just so you know, Dashlane AI [tool:Dashlane AI] is reporting it as a phishing risk — this website might be trying to steal your data. So you might want to check something on the back end.
[00:54:13] Ty Wells: Well, the only thing would be it's a fresh domain. I mean, literally the domain spun up this morning.
[00:54:22] Patrick Chouinard: No, I'm sure that it's safe. I'm just saying Dashlane AI seems to think that it's not. So maybe you want to check.
[00:54:31] Ty Wells: Yeah, no, I will.

---

<!--SEGMENT
topic: Ryan's Security Review, Hermes AI Assistant, and Business Migration
speakers: Ryan C, Paul Miller, Marc Juretus, Ty Wells, Patrick Chouinard
keywords: security review, Claude Code, Codex, adversarial review, Code Rabbit, social app, CRM, email ingest, Google Workspace, SiteGround, Hermes, personal assistant, Google account, Dropbox migration, false positives, hooks, Scott
summary: Ryan describes a week of security hardening on his social app using a multi-tool review process (Claude Code, Anthropic security check, Codex adversarial review) that surfaced ~60 issues. He also reports migrating his business from SiteGround to Google Workspace and setting up a dedicated email and Google account for his AI personal assistant "Hermes." He teases a custom hook-based security review system built by a community member named Scott, which he has adopted across his codebases.
-->

[00:55:06] Ryan C: Yeah, too many things going on. Still slightly hungover from my birthday at the weekend, so I've just been slowly plodding through the social app and just plugging a load of holes around the security review thing that Scott showed off a few weeks ago, and it came up with about 60 different things between Claude Code [tool:Claude Code], Anthropic security check, and our agent security check and Codex's adversarial review. So I'm just working through each of those, marking false positives down. So I'm about 40 things into a list of 60, but it's found some stuff that's pretty good, and it's the first application I ever made in anger that's actually in production. So there's always going to be bits in it that weren't great from tightening processes and stuff.

[00:56:00] Ryan C: So I've found a load of stuff that's quite good, and the documentation wasn't amazing, so I've cleaned that all up and made that a lot nicer. So I've just been tweaking really. It's not been a week of anything majorly new. I know I'm supposed to hook in an email ingest system into the CRM, but I didn't quite get around to that. So that'll have to be reported on next week, once we actually got it working and tested.

[00:56:27] Ryan C: So yeah, nothing major. I've moved my entire business over to Google [tool:Google Workspace] this week, with a lot of help from Scott, from SiteGround where it was. So I'm just getting everything integrated into that, setting up all sorts of bits, and Patrick will be proud — we've now got my personal assistant's email set up, ready for Hermes [tool:Hermes] to be started. So we're taking an entire day next week, me and Scott, to go through and just build the thing out. I'm going to let it make phone calls, all sorts of cool stuff. It'll book appointments for me and things, slot it into my diary, so it has its own email, its own Google account, all of that fun stuff.

[00:57:20] Ryan C: Yeah, nothing major. The only question I have for you, Paul, was how the pitch went, if that had happened.
[00:57:28] Paul Miller: I'm meeting with the client in two hours.
[00:57:31] Ryan C: Oh! I will let you know — so I'm meeting with their CEO and their head of sales. Was what I sent over to you adequate for what you needed?
[00:57:41] Paul Miller: Yes, yeah, yeah.
[00:57:45] Ryan C: Shout out if you need anything else, obviously. I might not be awake in two hours' time, but pay me an email and I can always come back with any answers to questions or jump onto organizing a face-to-face, whatever, so.
[00:57:56] Paul Miller: I will update you overnight.

[00:58:08] Ryan C: I think Shakur's come up with a question in the chat. <Q>Have you tried Code Rabbit?</Q>
[00:58:10] Ryan C: <A>Yeah, I think Scott tried Code Rabbit [tool:Code Rabbit] and then he's essentially built his own hook-based local check system. And again, I think I said it last week, I don't want to steal his thunder because he was quite drunk when he came on and showed it last time and then he showed like one-eighth of actually what it did. So he has sworn that next time he's on he will run through it properly. So I don't want to steal his thunder and show everybody his security review thing because it's kind of his. I've just nabbed it because it's incredible. So hopefully we'll save me some lawsuits of someone finding a hole in something and breaking it. So I'm running it over all my code bases and it's great. It's finding bits that Fable didn't find. So it's quite good.</A>

▶ Ryan C: Jump on next time Scott's on, because he'll run you through exactly how it works and all the shiny bits in it.

---

<!--SEGMENT
topic: Patrick's Training Generator Plugin
speakers: Patrick Chouinard, Ty Wells, Paul Miller, Shakur Abdullah
keywords: Training Generator, Claude Code, open source, GitHub, skill, plugin, onboarding, interactive training, repo analysis, differential update, Notebook LM, developer training, Russian doll, exercises, demos
summary: Patrick presents his open-source Training Generator plugin, which analyzes any code repository and generates a self-serving, interactive training course delivered by Claude Code. The system adapts to the learner's role (developer vs. user), tracks progress, supports resumption, and updates differentially when the repo changes. He demonstrates it on the community's Recap Flow project and explains how he uses it professionally for Claude Code onboarding at work.
-->

[00:01:01] Patrick Chouinard: Well, I decided to not industrialize it, but open source it for once and make it into a deployable package. So let me share this here.

[00:01:23] Patrick Chouinard: So Training Generator [tool:Training Generator] — it's a plugin that you can install globally on your machine. And from the root of any project that you've built using Superpower, it works best with projects from Superpower just because they have more documentation, but any other project it will work. I can't guarantee the level of detail, but it will generate a self-serving training agent for Claude Code [tool:Claude Code]. So basically, it will generate a training that Claude Code will give for you, and you just start the training, and you answer the questions. You can ask questions to the trainer — Claude Code itself. It has a way to track your progress, and if you state that you want to resume where you were, it will go back to where it was in the training and continue the course, if you go on a tangent, for example, and ask it a bunch of questions.

[00:01:02] Patrick Chouinard: So, pretty happy with the actual result, and let me show you one training. I actually tried it on the Recap Flow project — you know, the project that gives us the recap of these meetings every single week?

[00:01:52] Ty Wells: The UI is just Claude Code.
[00:01:54] Patrick Chouinard: Yep, and for this I use the desktop application, not because I'm necessarily a fan of the desktop application, it's just when you run a training in Claude Code, I find the interface is a little bit more interesting. I just told it to start training and it taught me — all right, you've been at the very start, activity one of 65, clean state, welcome to running the community brain corpus, the tier B operator course, blah, blah, blah. It asks you what type of student you are, so let's say I'm going to say developer new to this repo, for example, and based on my answer, it will go into the training itself.

[00:01:45] Patrick Chouinard: I'm not going to go through the whole thing — this is an eight-hour course that it created, but it created it basically in one go, based on the content of the repo itself. So I didn't do anything to the repo. I simply asked the trainer generator skill or plugin to generate training off of the content of the repo. And as you can see, it talks about the corpus, the retrieval server. It described the architecture — because this is a project that required you to present the architecture, especially because I said I'm a dev that wanted to use that repo. But if I were to say that I was a user, it would have shown it in a different way.

▶ [00:01:04] Patrick Chouinard: So it creates a training that adapts to the audience. And you can also influence during the generation if you want to focus on one specific aspect of your repo. So if it's just to onboard new developers, to present to customers, to use your application in your repo — you control the direction. But the idea is that all the training you create is self-serving, and Claude Code is the one giving you the training itself.

[00:01:18] Patrick Chouinard: <Q>How have you used that in work?</Q>
[00:01:18] Ty Wells: <Q>How have you used that in work?</Q>
[00:01:27] Patrick Chouinard: <A>Oh, actually, this is how I give the Claude Code advanced training at work now. So Claude Code is maintaining the content of the training off of the GitHub repo of Claude Code itself. So anytime there's an update, it updates the training material, and the training material generates a course that is fed from that information. So it will do the differential every week whenever there's new content.</A>

▶ [00:01:06] Patrick Chouinard: But if your repo is different, remember that you take a lot of time and a lot of tokens to create the original training, but afterward, you just do a differential of what changed.

[00:01:34] Ty Wells: Patrick, I've got a thought. I love that stuff. I definitely want to use it tonight or tomorrow to update some training, but I would say what I'm going to do with your repo — I'm just putting this out there — is what if you create a Notebook LM [tool:Notebook LM] video because they have videos you can create?

[00:01:12] Patrick Chouinard: The only reason I didn't go that way was because I wanted the course to be — I didn't want it to be a presentation. I don't want Claude Code to just run through it like it was running through a PowerPoint presentation. I want it to be highly interactive. It's basically, there's a demo behind it.

[00:01:08] Patrick Chouinard: So you see this training repo — this is what the skill, the training generator, generated. So it's a full application basically that has a bunch of those skills, like answering questions, conducting training — all of that was created on the fly. The training generator decided what skills the training would need in order to conduct the training. You have the information for the instructor itself. You have all the exercises. So those are live exercises that you can do with the training harness. So as you can see, it even has demonstrations that you can go through. And Claude Code will go through itself — so it's a bit, yeah, you have to think a bit about it in terms of the time — it's basically the Russian doll: I have a skill that creates a skill, that teaches a skill.

[00:01:24] Ty Wells: Yeah, no, no, it's good stuff. But from the developer's perspective, for sure, I'm already thinking how I'm going to train my employees on any — in terms of giving them the training.
[00:01:37] Patrick Chouinard: Onboarding — it's been a lifesaver for now. And this is actually more advanced than the version I've created at work, because at work I created the prototype. And then I spent some time thinking about it, and I've created that version for myself on my own GitHub repo.

▶ [00:01:00] Patrick Chouinard: Feel free to steal the Training Generator and use it, modify it, fork it. I'll be interested in seeing your variations.

---

<!--SEGMENT
topic: Patrick's Stream Deck and Codex Micro Inspiration
speakers: Patrick Chouinard, Paul Miller
keywords: Stream Deck, Codex Micro, OpenAI, keyboard, automation, Claude Code, Codex, Hermes, Stream Deck Classic, Stream Deck Plus, profile, harness management, macro keys
summary: Patrick describes being inspired by OpenAI's Codex Micro keyboard announcement to repurpose his existing Stream Deck hardware as a more flexible alternative. He has created profiles for a Stream Deck Classic (15-key) and Stream Deck Plus (8-key + 4 knobs) to manage Claude, Codex, and Hermes from a single physical interface, with the advantage of not being locked to a single harness like the Codex Micro device.
-->

[00:01:23] Patrick Chouinard: That one is not completed at all, but I've rediscovered my Stream Deck [tool:Stream Deck] this week because I saw the announcement about Codex Micro [tool:Codex Micro], the little keyboard that OpenAI is selling with a bunch of micro keys. And I had a session with Codex, basically told it, do the research on what that thing does and help me figure out how I can do the same thing with a Stream Deck.

[00:01:00] Patrick Chouinard: And basically, we came up with a framework that will be a little bit more functional than what they're outputting, simply because theirs is hard-coded to the Codex harness. So all the keys cannot do anything else than automating the functionality of the Codex harness. We just got inspired from it, and now I've created a profile for my two Stream Decks, actually. There's a Stream Deck Classic 15-key and a Stream Deck Plus 8-key plus 4 knobs. And those two together will be able to manage either Claude, Codex, or Hermes. But I'm still playing with it. I'm still developing. It's not done yet. But yeah, that's my next toy.

[00:01:56] Paul Miller: Brilliant. Cool. Thanks, Patrick.

---

<!--SEGMENT
topic: Shakur's AI Website Redesign Tool
speakers: Shakur Abdullah, Paul Miller, mdcatc, Ty Wells, Patrick Chouinard
keywords: website redesign, Firecrawl, AI slop, design quality, Impeccable, UX Pro, Skill Arena, design competition, verifier skill, observer skill, Fable, Kimi, Gemini 5.6, iterative training, skill update, visual review, front-end design
summary: Shakur presents a multi-step automated website redesign pipeline: it takes a URL, uses Firecrawl to extract assets and copy, passes them to an AI for redesign, then runs a QC check. The core problem is that outputs consistently look generic ("AI slop") regardless of which design skills are applied. The group advises using before/after examples to teach the skill, iterating with a verifier/observer agent, and accepting that the definition of "AI slop" will shift over time as models retrain on AI-generated content.
-->

[00:01:08] Paul Miller: So you are extracting the content of a website, the assets of a website. And what were you wanting to do with those assets?

[00:01:13] Shakur Abdullah: So I take a URL. It's basically a skill — several skills that I've weaved together. So I take a URL, I give it to the AI. The AI then goes and kicks off Firecrawl [tool:Firecrawl], which pulls out all the assets of the website and puts it into a folder. It then pulls all the writing, everything, the copy as well. It then hands that and tells another AI to make a design. It will make the design. It then takes that design and does a QC check on it, puts all the original stuff back in, and then it's supposed to have a new redesigned website that still has everything from the original. But the issue is that they all just keep looking exactly the same. And the design quality — it's better than what they originally had, but it's still very AI-ish.

[00:01:05] Shakur Abdullah: I've tried a couple of the design skills to add those in. So I've tried Impeccable [tool:Impeccable], the Claude front-end design skill, some of the other ones, but unless I come in and tell it, hey, do X, Y, and Z, do this, do that, the design never really passes a certain threshold. That's what I'm trying to figure out. Has anyone figured out how to push it past that slop threshold?

[00:01:34] Ty Wells: I've used Impeccable. If you looked at UX Pro [tool:UX Pro], I think that's the name of it. Let me give you — I have this skill called Skill Arena [tool:Skill Arena], and that skill runs the design. So they compete, basically, at design. But it's front-end design, Impeccable — let me see what else. I'll get it to you, I'll put it in the chat.

[00:01:29] mdcatc: So my method to get to that point would be to use these as examples, right? You have examples already — what you liked and what you didn't like. So you'll use these examples in your next prompt to say, okay, this is what you did with this one. It was insufficient. And this is how you made it sufficient, right? So the AI has an idea. It can see what not to do and then what to do. And once you do a few of them manually — I mean, that's usually for any automation process, you want to make sure you can do the entire flow from beginning to end in a manual process so you can see exactly what the problems are along the way.

▶ [00:01:00] mdcatc: And then at the end of each of those cycles you tell your AI to make a learning on that, update your skill so that it doesn't do this, make it do the positive result that you can, and over time you'll see that it starts to change what it originally produces to the point that you can have it hit the first time 90 percent of the time instead of only 20 percent of the time. So you've got to go through some cycles to actually teach your skills how to make your skills smarter and update this as you go.

[00:01:38] mdcatc: One of the things you should look at too is — even just other sites — the AI slop has a very specific thing that you're seeing. We see it, but to be able to describe it with words is sometimes difficult, right? It's like this looks like AI, but how do I describe what I'm seeing that tells me it looks like AI. And that's how you've got to kind of look at that as a learning thing to your skills — to update your skill each cycle as you go through them.

[00:01:51] mdcatc: One of them has a skill that makes the UI compete. So it'll generate the same website page say like five different times using five different models. And that's a pretty good way to do it as well, and then have it rank them, but you've got to have something that can — you have a verifier or an observer skill that looks at it and says, okay, this meets the criteria or this doesn't meet the criteria.

▶ [00:01:39] Patrick Chouinard: And the other thing you need to keep in mind, Shakur, is that no matter how good you make it today, you will have to retrain it occasionally because as we get more and more good quality AI-generated material, it's going to become the AI slop of tomorrow because models are going to be retrained on it and every site will look like that at some point. So it's a continuous loop that you're going to have to go through if you want your system to always output top-quality material.

---

<!--SEGMENT
topic: Juan's AI Photo Booth Event Deployment
speakers: Juan Torres, Patrick Chouinard, Paul Miller, Marc Juretus, mdcatc, Ty Wells
keywords: AI photo booth, quinceanera, image generation, Firecrawl, Osmo Pocket 3, QR code, multi-model, GPT, Grok, image-to-video, Higgsfield, cost tracking, PIDFIRE, UX observation, mirror booth, style transfer, event photography
summary: Juan reports a successful first live deployment of his AI photo booth at a quinceanera event in San Diego. The system used a mirror booth for photo capture, a touchscreen display for AI-generated style-transfer images (Catholic Guilt, GTA 6, oil painting, etc.), and QR codes for guests to retrieve images. Total cost was $52 for 859 AI image generation jobs across multiple models. He discusses UX observations (children navigated it most intuitively), plans for image-to-video pipeline integration, and Patrick suggests adding a looping animation demo to guide users between sessions.
-->

[00:01:07] Paul Miller: I come back victorious from the deployment of the AI Booth application.
[00:01:07] Juan Torres: Yes, yes, I did deploy it into an event on Saturday. And it worked better than I thought it was going to work. So let me actually share my screen.

[00:01:49] Juan Torres: So these are some of the event-generated pictures, right? So for example, you have the original picture of these two ladies. Gets transformed — Funny Roast style, Mandarin Gala. This is the Funny Roast style Mandarin Gala.

[00:01:08] Juan Torres: And this is the Catholic Guilt one, the style, so it actually converts these gals into, you know, Catholic women. This is the oil painting one, GTA 6, again Catholic Guilt, oil painting. So there's plenty of them. There's plenty of pictures, several people taking pictures, right?

[00:01:21] Juan Torres: So, yeah, and I have several people as well. I don't know if you guys know Dr. Simi. Do any of you guys know this costume? So in Mexico, there's a brand called Dr. Simi. And so he has become a very popularized character. And so at the party, there was this character. And so it actually transformed the character itself. Which is really interesting.

[00:01:10] Paul Miller: <Q>So did they get emailed copies of these?</Q>
[00:01:13] Juan Torres: <A>Well, it's a QR code generated thing, right? So I remember if — you know, I was talking about how I set it up — basically there was the mirror booth for the taking of the pictures. And then there was the touch screen that actually I have on my side for displaying the generated images. So this is what was created during the event. And it actually — I was impressed at how well it worked. I was afraid that internet was going to be an issue. That the pipeline itself was not going to turn in the outcomes of the AI-generated images. It definitely did. I didn't see — I mean, there's the friction of having to wait up to two minutes for the AI images to be generated, but the thing is, I set it up so that people can take the QR code, get the original pictures, go back to their table or whatever, and in the meantime, while it's rendering, you can see in the tiles that are rendering, and then when it's ready, it comes back to whatever screen there is, right?</A>

[00:01:09] mdcatc: <Q>How much did your event cost you in AI tokens?</Q>
[00:01:12] Juan Torres: You'll see, you'll see. I know that was going to be a question.

[00:01:31] Juan Torres: So this is the sessions tab, right? And then my sessions tab, I see all the sessions that you just saw, all those pictures. I can see them and all the metadata around it. All the pictures generated, the job ID, the model that was used, the specs of the generation, and the prompts on the side. And I have a couple of action spots right here — to be able to send the images. So there was one occasion in which — and this is why I set up email capabilities, because I knew that the QR code was not going to be enough and there was going to be people that for some reason didn't bring their phone or don't have a phone — so I can actually send them all the images through their email, through my iPad, through this web application.

[00:01:32] Juan Torres: And you can see the styles that were essentially generated per the event, and the total amount that it cost me, you see, in terms of cents.
[00:01:38] mdcatc: Yeah, that's not bad.
[00:01:38] Juan Torres: Well, you got to consider that these are three generated, nine AI-generated images, you see? So this is what I spent. And you got to consider that I'm not using just one model. I'm using a multi-model system. Sometimes it's GPT [tool:GPT], sometimes it's Grok [tool:Grok], sometimes it's another model. So it quantifies, it sums up the total quantity of the cost per usage of the model. And the total cost that I had for this event was $52.
[00:01:18] mdcatc: Ooh, that's awesome.

[00:01:37] Juan Torres: So for 859 jobs, I spent $52.

[00:01:19] Patrick Chouinard: Ali, if I could recommend — maybe I'm going to give you homework for a couple of weeks here, but I'm looking at your demo and it's awesome, but can you think about how you could integrate that with what Scott showed us a couple of weeks ago — the video pipeline that generates a complete video using Higgsfield [tool:Higgsfield], plus all of his harness? Yeah, actually, at the end of the night, you take all of the pictures, have the AI put a little scenario on top of it and generate a video of the event as a bonus afterward.
[00:01:55] Juan Torres: Yeah, yeah, no, that's definitely the next step. After I further stabilize the image-to-image pipeline, that's the next project.

[00:01:24] Juan Torres: I was trying to be a behavioral scientist and observe the behavior of my subjects, right — which are the guests, the attendees of the quinceanera. I thought that I was making it obvious, easy, attractive, and satisfying to interact. Especially the easy component, right? Like you see a huge button that says, you know, take a picture, right? I was surprised at points that people didn't know what they were supposed to do, right.

[00:01:26] Juan Torres: And surprisingly, what I saw is that kids were actually the ones that just knew what to do. It was not even the teens — the 15-year-olds were still somewhat struggling — but the kids. They just knew what to do. It was really surprising because the adults — of course I expected the 40-year-olds to not know what to do. Some 30-year-olds, maybe they knew what to do. Some 15-year-olds knew what to do. But the kids, they just understood how it worked. It was just amazing.

▶ [00:01:21] Patrick Chouinard: In between clients, just have your screen running a small 10-second video loop that is an animation of, like, a persona in front of the thing, pushing on the button, making a picture. You can make a very, very basic animation of 10 seconds that's going to show the usage. People are going to come in, they're going to try it.

[00:01:14] Juan Torres: So yes, I actually think of doing the image-to-video pipeline on the phone and then have the capacity to, I don't know, maybe get a projector to display the gallery and to display videos generated through the process. So basically it's not isolated and people can enjoy the generation and it attracts more people to the booth itself.

[00:01:00] Juan Torres: So I replaced — there was a Canon camera. I replaced it with the Osmo Pocket 3 [tool:Osmo Pocket 3] because it's better for the dynamical. And then they choose the styles that they want to use. I allow for three styles to run the mock instead of one. I can arrange whether there's one style generation or three.

---

<!--SEGMENT
topic: Morgan's Book Publishing Pipeline and ClusterCurb Update
speakers: mdcatc, Paul Miller, Patrick Chouinard
keywords: Heritage Plot, ClusterCurb, cemetery management, book publishing, manuscript, markdown, YAML, ODT, PDF, KDP, Amazon, LibreOffice, Inkscape, SVG, Python scripts, EIN, business setup, G2, Capterra, competitor analysis, Google Deep Research
summary: Morgan (mdcatc) updates on two SaaS products (Heritage Plot cemetery management and ClusterCurb) and a book publishing automation pipeline. The publishing workflow converts a canonical markdown manuscript into hardback, paperback, ebook, and audiobook formats using deterministic Python scripts, reducing a 2-3 hour process to 15 minutes. The group recommends using G2 and Capterra competitor review sites with Google Deep Research to extract user sentiment for product positioning.
-->

[00:01:42] mdcatc: I've got the ClusterCurb [tool:ClusterCurb] out there. You had talked about maybe having an interest in that, Paul. It's out there right now. My task this week for both of those — for the Heritage Plot [tool:Heritage Plot], the Cemetery Management System, and ClusterCurb — is to get the EINs set up and the bank account and county record for the business. Both of those are going to be probably primarily PO invoice type of customer contracts. I don't see a lot of people putting up a credit card to do a monthly SaaS or anything like that. So those are both kind of an annual kind of — we've got an annual budget and this is what we'll spend this year.

[00:01:32] Paul Miller: ClusterCurb — I put a little GSAP SVG animation in the front of it there to demonstrate how it works. And a quick little — I'm going to put a little calculator so that they could enter in their counts, like how many teachers, how many vehicles, and see the cost difference and time difference. And over the year, just a quick little marketing campaign thing to let them play around with the numbers and see how beneficial it could be for them.

[00:01:14] Paul Miller: And everybody I talk to really likes it. Everybody sees what the problem is. There's a couple of other competitors out there that I've found over the past couple of months. So I've been seeing what they're doing. The price range would probably be around $15,000 to $20,000 a year per school.

[00:01:45] Paul Miller: <Q>Have you looked up in G2 [tool:G2], you know, the G2 Crowd and those comparison sites about the competitor products and then get AI to extract all the things people like about them and dislike about them?</Q>
[00:01:51] mdcatc: <A>I haven't. What's the G2 one?</A>
[00:01:55] Paul Miller: You know how there's comparison websites where users score the pros and cons of the products.
[00:01:05] Patrick Chouinard: Yeah. So there's companies like G2. Capterra [tool:Capterra]. Is that the one? Yeah, Capterra. Yeah, Capterra.

▶ [00:01:17] Patrick Chouinard: So get something like Google Deep Research [tool:Google Deep Research]. Tell it to look through all of the sites like Capterra, G2. Give the definition of the app that you use and some of the examples of the sites. Get it to comprehensively understand what user positives are of the competing products and the negatives to build a comparison with what you're doing and build a potential requirements list.

[00:01:30] mdcatc: So I'm going to take for both of those, I'm going to use Capterra. Patrick's a trainer and we'll see how it spits out what it spits out for those.

[00:01:30] mdcatc: The other stuff I've been using AI for is I've been working with a publishing company, and they have a few books that I've been publishing for them — like five of them — but there's no workflow for: we have a single manuscript, and I have to output it in four different formats, each book. So there's a hardback, a paperback, the ebook, an audiobook, and they're all based on the same manuscript, but every cover then has a different layout, and every book has a different ISBN, obviously, but then the insides of it were a problem with editing, right? So the author would edit in Word and then send me just text, basically, and it was just a mess.

▶ [00:01:32] mdcatc: So I created an entire workflow where I have the canonical of the book as the manuscript in markdown format with some YAML frontmatter and backmatter, and then a couple of other files and a couple of deterministic Python scripts that dissect it and rebuild the entire ODT for the manuscript — because that's just an XML or a zip file, basically, of XML structures — so it knows how to actually create and build an entire book, export it out to PDF, and export all the components so that it can be uploaded to Amazon and KDP [tool:KDP] (Kindle Digital Print). And it was taking like two or three hours to get through the whole process, and now I've got that down to like 15 minutes.

[00:01:40] mdcatc: There's a quick — here's the update — it'll go through and it'll give me a diff of all of the things that were changed, that I could send back to the client so that this is what was changed, is that correct? And is there anything in here that's modified that shouldn't be modified? So that's been pretty good. We just finished up all five of the books that they had yesterday, so that was pretty quick.

[00:01:54] Paul Miller: And I did all of it in LibreOffice [tool:LibreOffice] and Inkscape [tool:Inkscape] or SVG. So the script can modify everything directly.

[00:01:08] Paul Miller: So she generated this cover using AI for herself as a mock-up, and I just took the mock-up, dumped it into Inkscape, and re-layered it so that I could control the sizing and dimensions of the book and the spine.

▶ [00:01:40] Patrick Chouinard: So it calculates how thick the spine needs to be based on the number of pages and the thickness of paper that she wants to print on.

---

<!--SEGMENT
topic: Fable, Codex 5.6, Omni-agent, and AI Consulting Discussion
speakers: Paul Miller, Patrick Chouinard, Ty Wells, Juan Torres, mdcatc, Elijah Stambaugh
keywords: Fable, Claude Code, Codex 5.1, Omni-agent, meta-harness, token efficiency, Qwen K3, open router, context window, notary, succession planning, legalese, document analysis, AI consulting, forward deployment, standard operating procedure, Claude Co-Work, ChatGPT Work
summary: The group discusses recent AI tooling news: Fable being added to Claude Code subscriptions at 50% discount, Codex 5.6 as the new commercial benchmark, and the Omni-agent meta-harness that orchestrates multiple harnesses. Patrick shares a practical use case where Claude Co-Work analyzed dense legal documents for succession planning, found contradictions across six documents, and corrected tax calculations — leading to a new consulting engagement with his notary. The group debates the best AI interface for non-technical professional users.
-->

[00:01:07] Paul Miller: Just one thing — everybody saw that Fable [tool:Fable] is now permanently set into our Claude Code subscription at 50% of the subscription, but still, at least it's there.
[00:01:23] Patrick Chouinard: Thank goodness.
[00:01:25] Patrick Chouinard: Yeah, I think that what Codex did with 5.6 pretty much was their end. Yeah, they couldn't not respond to that. That's the new commercial bar.
[00:01:40] Patrick Chouinard: Exactly, exactly. So at least now we know we need to be careful with it, but we have it for the long run.

[00:01:48] Patrick Chouinard: <Q>Has anybody tried anything with Qwen K3?</Q>
[00:01:52] Patrick Chouinard: Not yet.
[00:01:55] Patrick Chouinard: I think that the feedback is that it uses up more — so while it is cheaper per token, Codex 5.6 is better overall value because of how it uses the tokens.
[00:01:15] Ty Wells: I'm pretty happy with Codex 5.6 [tool:Codex 5.6] at the moment, with its top one.

[00:01:23] Patrick Chouinard: And I don't know if you saw, but the other thing I want to try is what they call the Omni-agent [tool:Omni-agent], which is basically a new harness that can — it's basically a meta-harness. It's a harness that operates harnesses.
[00:01:40] Paul Miller: <Q>To reduce the tokens?</Q>
[00:01:47] Ty Wells: It's not only to reduce the tokens.
[00:01:49] Patrick Chouinard: It will split the job between literally Claude Code — not between the model, but between harnesses like Claude Code, Codex 5.6.

[00:01:03] Ty Wells: We ran that a couple of weeks back. It was good, but it was a little buggy. And I got thrown off of it, but it did start off strong, I'm not going to lie.
[00:01:14] Patrick Chouinard: Something happened, it crashed on me a couple of times, so I gave up on it. I haven't tried it yet, but I definitely want to give it a try.

▶ [00:01:36] Patrick Chouinard: Omni-agent. [link:omni-agent — dropped in chat] There you go. Omni-gent. Yeah, I don't know, that name gets you because you know it's omni, it's agent, but I keep saying omni-agent, it's omni-gent.

[00:01:55] Patrick Chouinard: You know my love for recursive stuff, so an agent that manages agents — yeah, it worked, like I said, pretty good initially, but I think it ran into a context window issue at some point.

[00:01:20] Patrick Chouinard: Oh, and one little tidbit. You know that I've been using Claude Co-Work [tool:Claude Co-Work] to help me with all of the succession planning that I need to do. And this week it digested a bunch of emails from the notary that were pretty dense legalese — stuff I don't like to read through. And Co-Work managed to find issues or stuff to be corrected by comparing six or seven different documents that were sent to me — finding like, oh, well, you have to talk to the notary to tell him, like, this sentence here actually contradicts this other sentence in this other document that you received, and you also need to send them this document that you had in archive for a couple of years that actually overrides this document.

[00:01:19] Patrick Chouinard: It was pretty insane. Stuff I would have never seen. I mean, it recalculated taxes on some of his invoices — like, hey, this is not calculated with the right tax code. What? And it was right, actually. So now I just got a contract with my notary. He wants me to give him training on how to leverage AI in his practice.

[00:01:47] Patrick Chouinard: You did something right if he wants to be trained by you.
[00:01:51] Patrick Chouinard: No, but it's just like — I know he's going to get a whole lot of money from me because there's a lot of stuff that he needs to take care of. If I can offset some of it by providing training, how much the better.

[00:01:09] Juan Torres: <Q>Do you have a playbook that you'll follow with them? I'm curious what kind of your step-by-step is when you have a training like that.</Q>
[00:01:19] Patrick Chouinard: <A>I try to avoid having a step-by-step training because step-by-step training you can find for a dime a dozen. What I try to do is just sit with my client and say, tell me what your daily job is. Tell me what your pain point is and let me observe what you do. Because for example, what I found in his documents are things that from a clerical perspective you would not have found because it's not a comparison you do normally. So those are the things where I can say, here's how you look at documentation, look at a dossier for a client, and have the AI look to make sure that from a clerical perspective everything aligns well. I don't need to know his business. I just need to see him work, and actually then I just feed everything back into Claude and have Claude build a plan to address the pain points that we observe.</A>

▶ [00:01:23] Patrick Chouinard: But it's really — that's where you bring value. If I could have a step-by-step scenario that I could just run through every time, I could automate it and I could have AI do it for me. If I still bring value, it's because I observe and I find stuff that wouldn't make sense to automate.

[00:01:44] Patrick Chouinard: Back to that whole thing that AI keeps changing, so what works yesterday probably doesn't work again in two to three weeks, a month, whatever.

[00:01:07] Juan Torres: <Q>Do you look at Claude Co-Work or something like that as your lead — like, that you plan to get them to subscribe to their own?</Q>
[00:01:21] Juan Torres: <A>Either Co-Work or I actually want to really evaluate ChatGPT Work [tool:ChatGPT Work], simply because I know their limits are more generous. From a subscription perspective, if it can do the work — but honestly, Co-Work is a little bit more easy for the user that is non-technical, because Codex, although it's really, really powerful, it's more of a tech tool, I find, right now, at least.</A>

▶ [00:01:56] Patrick Chouinard: So yeah, I would tend to go Co-Work for now, simply because it's easier for a non-technical user than Codex, but could change next week.

[00:01:00] Paul Miller: There's a story about lawyers that are trying to use AI and they invent a bunch of stuff and they get screwed. I mean, it's such a strictly defined field. I mean, it should be ideal for AI to work in.
[00:01:17] Paul Miller: The problem is they're not providing any resources for the RAG part of it, right? They're just going off of —
[00:01:25] mdcatc: Yeah, but that's the thing. As a service provider, that's where we should take a look at because if the harness is well-built —
▶ [00:01:32] Paul Miller: It's the easiest field to automate because everything is a written procedure somewhere.

---

=== UNRESOLVED SPEAKERS ===

- **Elijah Stambaugh** — appears at [01:56:00] and [01:58:18] with lines that appear to be continuations of Patrick Chouinard's speech (the content is contextually consistent with Patrick's thread about the notary and AI consulting). This may be a transcription attribution error, but the name was not in the alias map and is listed here unresolved.

- **mdcatc** — used throughout as both a speaker tag and as a participant name ("That's Morgan" at [01:42:38]). The alias "Morgan" is referenced but the canonical full name is not confirmed in the alias map. Passed through as-is.

- **Ryan C** — abbreviated speaker name, passed through unchanged as it does not appear in the alias map.

- **Shakur Abdullah** — passed through unchanged; not confirmed in alias map.

- **Juan Torres** — passed through unchanged; not confirmed in alias map.

- **Ty Wells** — passed through unchanged; not confirmed in alias map.

- **Marc Juretus** — passed through unchanged; not confirmed in alias map.