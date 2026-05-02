=== SESSION ===
date: Unknown (Tuesday evening, exact date not specified)
duration_estimate: ~97 minutes
main_themes: Vehicle routing optimization, AI agent memory architecture, conflict-resolution AI app, LLM evaluation strategies, deep research tool comparison, LinkedIn thought leadership, data visualization, audiobook voice synthesis, graph RAG with Neo4j, app-building platform comparison

---

<!--SEGMENT
topic: Session Opening and Vehicle Routing Problem Introduction
speakers: Tom Welsh, Paul Miller, Brandon Hancock
keywords: vehicle routing problem, distance matrix, OR-Tools, Google Distance API, train stations, time windows, rail network, coordinate mapping, backtracking, combinatorial optimization
summary: Tom Welsh introduces his real-world vehicle routing problem involving 49 train stations across three UK regions, with constraints including transport mode (car vs. train), time windows, and site opening hours. Paul Miller shares prior experience optimizing delivery routes for Coca-Cola bottlers. Brandon Hancock and Bastian Venegas briefly discuss the computational complexity of the problem.
-->

**00:01:00 - Tom Welsh**
Hey, Paul.

**00:01:44 - Paul Miller**
Hey, Tom. How's it going?

**00:01:49 - Tom Welsh**
Oh, you know, I'm with distance matrices, and this, that, and the other. Just going around in circles and blowing my brain.

**00:02:00 - Paul Miller**
Yeah, no, I've done a lot of work in this space because I did it to work out the optimised delivery programme for Coca-Cola bottlers, because when you've got trucks doing lots of deliveries, there's some interesting — you've got the practical science of how do you do all the points, but then you have to put a value on each of the business. It's like, well, there's the cost to do it, there's the beneficial outcome with prioritising certain ones, like if you're delivering to a store, you want to deliver at the time they need the products and they're able to fulfil it. You factor all of that in potentially. I don't know what you're trying to get out of it — would be interesting to understand.

**00:02:54 - Tom Welsh**
Yeah, it's mad. So I'm basically — I'm not quite the road warrior, but I've got 49 places to visit, and I've got like three rail networks. Let's just say northern is the top one, so anything northern I'd rather do by car, and anything southern I'll do by train, because you have to get down to London and south. So there's two different costings for that — which one do I go do by train, do I go car — and then I only want to do three or four stations a day, because I don't want to push it too much, so that's my time window. And then of course a lot of these things only open at certain times — certain times being like the one I missed this morning, it closed at 10am, I got there at 11am. Yeah, it's an interesting problem anyway, but I'm currently doing it all longhand by basically just going.

**00:03:51 - Paul Miller**
<Q>What are you doing at each of these stations? What's the objective of when you're there, what do you do?</Q>

**00:03:59 - Tom Welsh**
<A>They've got a whole bunch of ancient IT kit, and I'm just replacing it.</A>

**00:04:03 - Paul Miller**
Oh, is this some kind of rail track or whatever?

**00:04:08 - Tom Welsh**
Yeah, it's for a rail company. So yeah, basically we've got a whole bunch of ancient, vulnerable PCs that need swapped.

**00:04:17 - Paul Miller**
Yeah, no, I just stopped working for London Underground years ago — was ancient as well.

**00:04:52 - Brandon Hancock**
<Q>What are you working on, Tom? The vehicle routing problem?</Q>

**00:05:03 - Brandon Hancock**
That was fun. That made me think. Did you see the thing Bastian wrote up for you?

**00:05:13 - Tom Welsh**
That was like, yeah, he full geeked on it.

**00:05:21 - Brandon Hancock**
He did. Because yeah, I was like, oh, high level — do backtracking and some recursion. And then we talked about it afterwards for a second, Bastian and I did. And he was like, no, like it blows up. He's like, look at the AI report I generated on it. And I was like, you're right. It does blow up. So yeah, that's very interesting. But how much — where would we say we're at on it? Close to 50% done?

**00:05:49 - Tom Welsh**
No, I'd say we're 10 to 15% in. I've mapped it on the coordinate. Now I'm lost in math. I'm just about to do this — I'm just going to do a distance matrix. So I've just knocked that out previously, just a couple of examples from the OR-Tools [tool:Google OR-Tools] and see how we get on.

**00:06:07 - Brandon Hancock**
Please, once you get that working, I'd love to see that.

**00:06:14 - Brandon Hancock**
Yeah, this is very interesting. I'm just curious to see how you implement the solution. I understand all the core things that Bastian said, but actually seeing it fully built up now is about to be wild.

---

<!--SEGMENT
topic: Member Updates and New Job Announcement
speakers: Brandon Hancock, Michal Simko
keywords: Oracle, Gen AI division, ecosystem developer, pre-sales, Brazil, LinkedIn, Neo4j, graph databases, job search, authority accelerator
summary: Brandon Hancock gives brief housekeeping updates about the Authority Accelerator program and upcoming content. Michal Simko announces he is joining Oracle's Gen AI division in a technical pre-sales role focused on bringing AI-first companies in Brazil to Oracle's cloud platform, and discusses how networking and luck played a role in landing the position.
-->

**00:06:29 - Brandon Hancock**
Speaking of the devil, he just joined. So, hey guys, quick updates on my side. I apologize — still slow on video making. Week one of the Authority Accelerator went well. Now we're going to week two. So once people get up creating their own videos and everything, I will be back to production mode. I'll actually get to make my first video in a while this week, and then we'll get back to regular content. So pumped to dive in. And yeah, that's the big thing on my side. We'll just start going around the room.

**00:07:12 - Brandon Hancock**
And the only change that I'd like to do differently is if you actually want to go first, because I know we've been pinging a little bit, and I apologize for not being able to fully respond to your message yet. But yeah, I would love for you to go first, and I've thought about the problem and how to do it. I just haven't had time to record it for you. So if you want to hop on first, briefly explain it, and then I'll pull up a whiteboard, and we'll take it from there.

**00:07:40 - Michal Simko**
Awesome. Thank you, Brandon. Hey, guys. Good evening. I missed the last two weeks — I went to two work events, and they both fell on Tuesday night. So it was a bit unfortunate. And I'm also in the middle of a job change. I'm basically leaving the SaaS company that I'm working at and joining a big tech company in their Gen AI division.

**00:08:12 - Brandon Hancock**
That's exciting.

**00:08:15 - Michal Simko**
Thank you. Yes, it is very much. And it is official — I got the offer from the hiring manager, from HR, but the whole process from within their system is taking a bit longer than I want. And so I haven't yet updated my LinkedIn and whatnot.

**00:08:37 - Brandon Hancock**
<Q>Out of curiosity, did they tell you what you would get to do? Have they broken that down?</Q>

**00:08:43 - Michal Simko**
<A>Yeah, it is kind of like a pre-sales role. The role is really called Ecosystem Developer, which is a mix of technical pre-sales and sales. So basically — well, it's for Oracle [tool:Oracle Cloud], and basically to get, you know, they compete against Amazon and Google, and really to bring tech companies and AI-first companies in Brazil towards their cloud. And yeah, they seem to be recognizing — they've done like 15 years ago when Amazon and Google landed in Brazil, they made a bit of a positioning mistake and now have to catch up. And so they're investing quite heavily in this space. They're doing events, and I'll probably speak to companies like Eleven Labs [tool:ElevenLabs] if they want to land in Brazil. And so I'm going to help them with go-to-market here and organize some meetings with big telco companies. So leveraging Oracle's network as well, you know, as an exchange.</A>

**00:10:17 - Brandon Hancock**
<Q>When it came to the job, did you already have an AI presence? Did you get to know somebody? Was it like an apply?</Q>

**00:10:37 - Michal Simko**
<A>So I started applying — basically I was in a process with a few different companies because I realized the company I'm working for is not going to go anywhere. They're not going to raise a Series B, and it's just literally going to go through their cash they raised in Series A — in a year and a half or so it'll be dead. And so I started looking for other companies. I spoke to two AI strategy consulting houses here in Brazil, started to connect to the system. I posted a bit on LinkedIn, and so when I posted a post on graph databases and went to the Neo4j [tool:Neo4j] event, LinkedIn works. And so suddenly one guy reached out to me from Uruguay who has a consulting company trying to land in Brazil. So I started getting these, in a bit random way, these interviews. And specifically the Oracle one — I knew someone in the team, went for lunch, went into the office, met his boss, and I spoke to the pre-sales team, to the tech people. They were asking me some technical questions. And yeah, so it went very organically.</A>

**00:11:43 - Michal Simko**
I really recommend reading this book — it's called *The Drunkard's Walk* or something. It's really about how these highly improbable situations in our lives kind of guide our life and the role of luck. So in the case of Oracle, it was literally that. And I think that brings a bit of humbleness — it's easy for us to recognize that, you know, if you ask someone like Elon Musk, maybe he doesn't even have the empathy to realize how many people probably helped him along the way, or how many random things happened in his life to put him where he is.

▶ **00:13:21 - Michal Simko**
LinkedIn is a baseline, right? And then you kind of have a CV and a cover letter and whatnot where you can tell a more specific story. And I'm happy to share whatever I used if anyone wants to take this offline.

---

<!--SEGMENT
topic: AI Agent Memory Architecture for Conflict Resolution App
speakers: Michal Simko, Brandon Hancock, Maksym Liamin, Bastian Venegas, Richard
keywords: agent memory, WhatsApp, persistent memory, Neo4j, graph RAG, Supabase, Cloudflare Durable Objects, key-value storage, conflict resolution, LangGraph, CrewAI, Gemini, context window
summary: Michal Simko presents his project: a WhatsApp-based AI mediator for conflict resolution (initially targeting divorcing parents) that requires persistent long-term memory of both users. The group discusses memory architecture options ranging from simple message tables with large context windows to Cloudflare Durable Objects and Supabase, ultimately recommending a simple V1 approach using a messages table and prompt engineering with Gemini or similar large-context models.
-->

**00:13:59 - Michal Simko**
So the question that I posed you was really about mid-term and long-term agent memory, right? And so I'm trying to figure out — I've been looking at Neo4j [tool:Neo4j] and graphs and how you can store more ontological, semantic information in a graph when you need specific retrieval. But basically what I'm trying to build is this WhatsApp-driven text or voice interface where both users can interact. Maybe in the beginning it would be like you put them into the same group — both people and the agent as well. But basically the system maintains a long-term memory, which is memory about both of them — like who they are, age, where they live, the whole context of this person. And then obviously there is this conversation, and the conversation is asynchronous, right? And so you cannot really use the context. So yeah, it's persistent memory. That's kind of what I'm trying to tackle. And also like CrewAI [tool:CrewAI] — I mean, we're in the context of CrewAI. And then all the stuff I saw was on LangGraph [tool:LangGraph].

**00:15:37 - Maksym Liamin**
So what we use for our bot for memory is mostly Cloudflare Durable Objects [tool:Cloudflare Durable Objects]. It's basically like a cache layer that is very fast and can really filter what you want to save there. For example, if you're talking short-term memory, it's absolutely fantastic to work with it. And then we first store the short-term memory there — so it's very fast — and then in the actual Supabase [tool:Supabase] database. Then once you identify that there is something important that we would like to save long-term, we just save it already to Supabase, to a separate table. But you can also just insert it directly in the Durable Object so that it's always there. Right now how we do it is that we have a maximum of, I don't know, 15 messages that we want to keep in the Durable Object. But you can also say, okay, I want to leave these two messages that are kind of long-term important, so they are always there. And then the other 13 will be varied every time the user is in this batch.

**00:16:41 - Michal Simko**
<Q>And you have some kind of format for the Durable Objects — you just like add a new line in there? Did you control the length of these messages, like cut it off, or how do you control the size of that?</Q>

**00:17:00 - Maksym Liamin**
<A>Yes. So it works as a key-value storage — like a cookie storage or local storage in the browser database, pretty much the same. And you can obviously control the size as you want. You can save either as a full message, if it's all relevant — that's what we do, because we just try to keep the memory of the previous 15 messages of the conversation. But for sure you could also add a layer of processing and say, okay, I want to actually split it into only valuable keywords, where you extract only maybe two or three words out of the sentence and save it there. So it really depends on the use case.</A>

**00:17:39 - Michal Simko**
<Q>And do you then take that and — because once you've cut off, let's say, 15 messages — do you then put it into an LLM to create a summary and put that into a vector just to save it there as a summary of that? Or do you do any of that?</Q>

**00:17:58 - Maksym Liamin**
<A>No, right now we just save it all as it is. We keep the full track of conversations in a separate table, and we just have it indexed. It's not even a vector database — it's just a relational database, an SQL database. And we keep track of it, but with very good indexes, so we can easily find it. Yeah, so we still haven't moved to vectors, but maybe that should be the next move. But as for right now, it's been good like this.</A>

**00:18:26 - Brandon Hancock**
So I wanted to do like a dumb answer first, and then explain why I think keeping it as dumb as possible might also be a cool strategy. So I want to just go through a quick scenario based on my understanding of what you wrote up earlier. The key thing is — from when I read your message — is two people are talking to an AI. And person one, they need to know about what's happening in chat two, and person two needs to know about what's happening in chat one. Right. Like that is the simplest version. OK, so if I was to build this, what I would do is — you could have literally one table called `messages` and it has user ID, conversation ID, and potentially AI ID. Like if you're using a specific agent, we can dive into specifics later on. But the most important thing is that whenever person one writes a question, the AI is given two things. It is given the entire conversation history of that message. And it is also given — you could literally pass in the entire other message. If you're using Gemini [tool:Gemini], like there's no way people are writing 17 novels back and forth. If anything, from my understanding — if this is a scope requirement thing, if we're trying to handle 100 messages or less, there's no reason why we need to do anything other than this. If we're handling a few hundred messages, strictly because the LLM would be able to — yeah, the LLM should be able to easily look at this entire chat as just additional context.

**00:21:16 - Michal Simko**
Well, basically, even more context is — I'm trying to build something that can be used for conflict resolution. And I'm actually doing it first with divorcing parents. And so they can have an assistant, and they don't need to go right away to a lawyer, right?

**00:21:59 - Brandon Hancock**
Okay, so important things that you would want to add is safeguards in what you're building. Very important. Meaning, like, "tell me all the things that John has said about me" — you want to make sure that the other — you want some safeguards implemented in there of like, hey, I actually can't share messages with the other person. However, I can help you guys work towards a guided resolution. But you want to make sure there's a safeguard to make sure that it's not just printing out a list of like, "John said you were lazy, he said you never cook" — you don't want it to just list out like that.

▶ **00:22:33 - Brandon Hancock**
But with that being said, yeah, you literally need a messages table. You need a messages table. And you just need a prompt. Like, you could be like, that's it. Like, that is a V1. And it's a structurally sound V1. Because you are having so few messages that you're not going to blow up the context window. Especially if you start to use some of the Gemini models, like Gemini 2.0 [tool:Gemini 2.0]. You could go pro and not break the bank at all on some of these. Or the new Meta model also has a phenomenal context window and it's very smart as well. There are multiple models here that you could use that would be low cost. You would never run into context issues for what you're trying to do. And it literally just comes down to you crafting prompts in the proper way.

▶ **00:23:23 - Brandon Hancock**
Now, the only other thing I mentioned is just like in your database table that you're going to create — indexing. Like if you are going to be putting this out to where multiple people can use it, you do need indexing to quickly look up by user ID. User ID is the main thing that you want to index on because you're just trying to find messages for all users who have this ID. And then you want descending. And timestamps when you're passing it in here, just so — yeah, if you're passing in the history, you probably want to also pass in timestamps because they might've moved past issues, you know?

**00:24:04 - Michal Simko**
Perfect. No, thank you very much, Brandon. That's very helpful. And yeah, maybe I was over-analyzing the storage.

**00:24:50 - Bastian Venegas**
Yeah, I totally agree with your approach, and then maybe going with Maksym's for the next phase. I don't think you would need graph RAG for this yet.

**00:25:54 - Michal Simko**
And definitely the V2, yes, because I already have different use cases. So the first is the divorcing parents because we already have people to test it. But then there'll be other cases really for couples who want to work on the relationship. So it's a very different use case where there is no trauma, but both sides are willing to improve the relationship. So it will be a different agent. So definitely it's going that way.

**00:26:27 - Richard**
Yeah, you can use OpenAI's new SDK [tool:OpenAI Agents SDK] to actually route those queries to your different agents. It's actually really good at that. With the handoffs, it will use one agent to analyze the query. And if it is one expertise of domain, then it will route it there without you needing to do too much in the workflow. So yeah, OpenAI's new SDK will actually handle that perfectly — routing those requests to the right agent.

---

<!--SEGMENT
topic: Vehicle Routing Problem Deep Dive and Strong Node Clustering
speakers: Tom Welsh, Brandon Hancock, Paul Miller
keywords: vehicle routing problem, time windows, OR-Tools, Google Distance API, strong nodes, backtracking, factorial complexity, clustering, Excalidraw, train stations, combinatorial optimization
summary: Tom Welsh shares a visual map of his 49-station routing problem with time constraints and regional splits. Brandon Hancock introduces the concept of "strong nodes" (geographic clustering) to reduce the problem from 49 individual nodes to roughly 10 clusters, dramatically cutting computational complexity. He references a YouTube video by Clement where a high schooler solves a similar problem in 57 minutes.
-->

**00:27:11 - Brandon Hancock**
Next up is Tom solving the world's hardest traveling problems known to man.

**00:27:23 - Tom Welsh**
I'm making pretty pictures. Yeah, so I'm working on a thing called the eco-routing problem with a time window. So basically, I've got 49 train stations to visit, split across three different regions. As I said to Paul earlier, my northern region — it's better to do it by car. The southern regions are more closely together with train stations. I'm just trying to work out how to get the routing of that done. I'm currently playing with — yeah, that's the one. So basically, the reds are one set of systems. The yellows are another set of systems. I've got a base, which is blue, kind of hidden in the back there. And I've got time constraints — I want to be out at nine o'clock in the morning, back by four o'clock in the afternoon. And certain sites have certain opening hours that aren't conducive to that kind of work. So yeah, I'm just spitballing, moving stuff around. Bastian, thank you very much for the stuff you gave me. That was amazing. I've got some Excalidraw [tool:Excalidraw] stuff going on, but I'm just jotting ideas down. I'm currently playing with the OR-Tools [tool:Google OR-Tools] and Distance API [tool:Google Distance API] from Google, just getting some better ideas of how to get stuff together.

**00:28:34 - Brandon Hancock**
<Q>Can I give you another idea really fast I just thought about?</Q>

**00:28:39 - Tom Welsh**
Yes, you can.

**00:28:39 - Brandon Hancock**
<A>Okay. So you and I — whenever I was first talking and suggesting options, the main thing I said was backtracking. Basically, guys, it's like when you go to solve a Sudoku programmatically — you use a technique called backtracking, where it attempts to, like, can I put a 5 here in this specific grid, and it tries based on a few constraints and rules to keep — does a 5 work? Yes, yes, yes, yes, yes. And then eventually goes, oh, no, it doesn't work? Cool. Backtrack. I'm going to try 6, and then we'll keep going. So that's how it works. Bastian brought up a great point of like, the time complexity of this was factorial. So that just hit me. Something I think you could do that would be very helpful is there's a concept in programming when you're solving complex problems like this called strong nodes. And basically what you do is you would just cluster things together as strong — basically, all these are almost the same thing. You know, so what you end up doing is like picking an entry and exit point. So the entry point to this strong node would be your entry and exit point for this one would be right here, because obviously that's where people need to leave. Your exit point would be here. Your entry is here. And what's cool about this is you actually reduce the scope from 49 individual nodes down to like 10. And 10, you can so easily do that.</A>

▶ **00:30:31 - Brandon Hancock**
So yeah, there's a great YouTube video — I will find it and send it over to you. A high schooler actually solved this problem. So if a high schooler can do it, why can't we do it, guys? He solved it in 57 minutes, Tom. So if it's taking you any longer than that, I mean, what the heck, man?

**00:30:58 - Tom Welsh**
Thanks for that, because yeah, the strong node thing's quite good, because one of the constraints I've got is hitting three or four stations at a time. So I don't want to do much more on that, so cluster it. So I was actually looking for some way of clustering, so that strong node — that's a good tip.

▶ **00:32:21 - Brandon Hancock**
Yeah, this is literally the exact problem you're trying to solve. Software engineering comes down to like there's a bunch of small patterns that exist and they just work. And you have to know when to throw in the right ingredients to actually solve complex problems.

---

<!--SEGMENT
topic: LLM Evaluation Strategies for Document Processing
speakers: Andrew Nanton, Brandon Hancock, Maksym Liamin
keywords: LLM evals, evaluation framework, document summarization, prompt iteration, human-in-the-loop, JSON output, binary classification, LightRAG, foundation models, Supabase, likes/dislikes feedback
summary: Andrew Nanton discusses the challenge of designing evaluations for a document-processing project he and Maksym Liamin are building together, particularly for long-document summarization where correct answers are not binary. Brandon Hancock notes that current eval tooling works best for clear binary classification tasks. Maksym describes their current approach of capturing human-in-the-loop feedback through UI buttons to gather training signal.
-->

**00:32:43 - Brandon Hancock**
Next up is Andrew. What's been going on?

**00:32:51 - Andrew Nanton**
Not a whole lot of new stuff on my end to report. Doing some testing on the project that Maksym and I are working on together. Been doing a lot of thinking about the right kind of evals for something — for projects that don't necessarily lend themselves as easily to evals as others. In terms of what kind of output are we looking for — longer, processing longer documents and making sure that as we continue to iterate on the prompts that we're getting improvements rather than backslide. Looking ahead to using newer foundation models or being able to switch them and just having an easy way to make sure that everything is where it needs to be. But doing that in a way that it doesn't necessarily only need to send JSON back. And so that's a little bit trickier, but interesting problems to think about. Also, I saw the stuff on the school page that I think, Bastian, you posted about LightRAG [tool:LightRAG], and so I was taking a look at that just to make sure I'm staying on top of that stuff, because it sure is interesting.

**00:34:22 - Brandon Hancock**
<Q>Real quick, out of curiosity, Drew, what are you using for evals, and how are you adding it into what you're thinking about doing? Are you doing it on the document search to make sure it got the right thing, it generated the right response? Where are you adding them in? Tools? Any suggestions? Ideas?</Q>

**00:34:42 - Andrew Nanton**
<A>Right now, I'm not doing it systematically. Maksym has some ways that he's doing that more systematically, and that's where we need to put our heads together. But mostly I've just been thinking about what should these evals look like. What would be sort of best practice? For example, summarizing a document that is 100 pages long — what kind of output should the summary include and how do you structure an eval around that? I mean, you could just go with a bunch of regex or something like that, but what's the best approach?</A>

**00:35:30 - Brandon Hancock**
So if you're asking me — OpenAI, they have their setup, but their setup is more for classifiers, because evaluations are best for, like, did you give the right answer? Because the classic example that's always used is, like, if you're angry on a customer support line and you're upset, elevate to the proper thing and not accidentally send them to the customer success manager, which would be like, oh, heard things are going great. And they're like, what the hell? No, I'm upset. You know, like, make sure things get routed properly. That's been the classic example. So like where it's a clear binary, yes or no. So I personally have yet to see a really good example of evals working in vague terms, because it's like, yeah, it's very weird to do it for non-concrete instances of a correct binary yes or no. If anyone has any suggestions, happy to hear it though.

**00:36:50 - Maksym Liamin**
Thanks, Brandon for sharing this. We definitely need to figure out how we exactly do it. Right now we have just put in the code and in the program itself a lot of places for human-in-the-loop. So for example, we extract different facts from a document, and we have like buttons to verify or reject them. So we kind of gather the data if it was useful or not. Also we have likes, dislikes, and comments for chat answers. So there is a search and chat functionality, and there you can all kind of grade it. So now we are just capturing the data, and the more users come, the better it will be, the more data we will have. And then we really need to think exactly how we utilize it.

▶ **00:37:43 - Brandon Hancock**
Yeah, Andrew and Maksym, if you ever just want a second pair of eyes on anything, feel free to schedule — I'd be happy to hop on a call and look at it. This is doing very cool work, and pushing the edge of — like some of this stuff, like there's not even really tools built properly right now. So it's like you having to make your own stuff, which is much harder than if there was pre-built stuff. So y'all are doing the hard work. Y'all are solving hard problems.

---

<!--SEGMENT
topic: Deep Research Tool Comparison and LinkedIn Thought Leadership Strategy
speakers: Paul Miller, Brandon Hancock, Richard, Dr. Mohamed Samy
keywords: deep research, Perplexity, Google Gemini, OpenAI o3-mini, NotebookLM, LinkedIn strategy, thought leadership, consumer goods, CRM, Insightful.mobi, newsletter, ghostwriter, prompt engineering, virality
summary: Paul Miller presents findings from a comparative analysis of three deep research tools (Perplexity, Google Gemini, OpenAI o3-mini), including using NotebookLM to aggregate outputs. He discusses using this research as the basis for LinkedIn thought leadership content targeting consumer goods companies. Brandon Hancock and others advise on content strategy, recommending LinkedIn-native video demos, prompt giveaways, and email capture over Medium articles.
-->

**00:38:16 - Brandon Hancock**
Paul, you are up next.

**00:38:19 - Paul Miller**
Hey, guys. So this week I've been focused — well, it's tax time in New Zealand. So I've focused on revenue to pay our taxes for the business side and my personal side. But what I'm doing — so look, I've talked about this deep learning comparison that I've done, and I'm going to share with you what my findings were on that. And probably the question for everybody as I take you through this is, what's the best way — what do you think of my idea with getting value out of this? So I'm thinking of doing a LinkedIn post, maybe that LinkedIn post links to a Medium article or a post on my core company's website so I can get customers into the funnel. I want to be a thought leader — from a company hat, not an individual hat. I want to show that we're giving away some practical ideas to customers, to our customers in the market, that for $20 US dollars a month, they can get some really capable, deep research tools to help their business.

**00:40:11 - Paul Miller**
So if I can share — so just a bit of context. We're a CRM Salesforce automation business. This is my Insightful.mobi [tool:Insightful.mobi] company. So the website is insightful.mobi if you want to see any more. And we've got competitors — Salesforce.com [tool:Salesforce], StayInFront [tool:StayInFront] is another one. And I wanted to do a little analysis against StayInFront. So I'm wanting to introduce a new frozen dessert that goes into the ice cream aisle — tell me about the markets. But this is just showing what my early research was. And I wanted to go through the steps of if I've got this prompt and I want to put it through three of the main tools of deep research, what's the quality of the output of each of those tools?

**00:42:00 - Paul Miller**
So they all have a kind of similar approach of the steps and saying, what are the questions back from that prompt that we should ask? They all kind of have the model. Perplexity [tool:Perplexity] led the curve with this, even though they actually differentiate the deep research product against the base research product for quick questions. And they all cost roughly the same. Interestingly, so I used — at the end, in terms of my testing — I used Google Gemini [tool:Google Gemini] to rate each of the three research output documents. And I used OpenAI o3-mini [tool:OpenAI o3-mini] to do the same research. And so Google said that the OpenAI deep research was better, while OpenAI said the Google research was better. So it's quite interesting to compare what makes each report better in terms of usefulness.

**00:43:09 - Paul Miller**
In terms of how I personally use them, I took all three reports, stuck them in NotebookLM [tool:NotebookLM], and then aggregated the three deep research documents to give me a single kind of view that I could ask questions on about our software competitor. But it's pretty comprehensive, and I was thinking, well, maybe put this into an article, compare those tools, and talk about the value of deep research to start with. You know, are you wanting to research about products, your competitors, your customers? Because if we go back to the prompt, it's not just talking about features, because everyone's going to talk positively about their product on their own website. What you want to be able to do is look at those public review sites.

**00:44:37 - Paul Miller**
The question is really much about the audience — inspiring the audience that copy-pastes this prompt for their use case. How useful could this be for me? Because it's a huge cost to do research and development in the food industry. So while it's not technically complex, there's a high opportunity cost because you divert your production facility and your internal development resources for maybe six to nine months. There's a lot of risk to it, and one of the ways to mitigate risks is to look at other global markets that are similar to yours, or look at how your competitor did with a similar product in that category.

**00:45:20 - Brandon Hancock**
<Q>So real quick — goal is more leads, correct? Like that is the goal?</Q>

**00:45:38 - Paul Miller**
<A>We're thought leaders. Have a look at the cool stuff that we're doing.</A>

**00:46:27 - Paul Miller**
Look, most of my customers — if you do a good post on LinkedIn, it really raises our profile. And I kind of want to keep some LinkedIn content going. But LinkedIn itself for an article — maybe put it back to Medium, push it back to our website with a call to action at the bottom. Like, click on there, make a time. We can talk about AI, have a coffee, blah, blah, blah.

**00:50:42 - Brandon Hancock**
Cool things that you could do — basically, what these guys have done — if you wanted to do it and steal their idea — they're focused on helping writers write with AI, and they have a weekly newsletter that has a free and a paid component. In your case, I don't think you would care about the paid component because you're actually just trying to bring in new customers. You don't really care about a $20 subscription. You're trying to help grow the business. So you could literally just target customers with AI and just focus on, like, hey guys, here's how you can use AI in your business. I'm just going to give away prompts. And then all you're doing is you write the article on LinkedIn, and you show — literally copy their format. And then all you do is just swap out the customer you're serving to help your customers. And you're going to say, hey, use this prompt, and here's the awesome results you can get. And then you go, comment the name of the topic below, and I'll DM it to you.

▶ **00:51:55 - Brandon Hancock**
It explodes. Like, it genuinely will explode your LinkedIn profile every time I do it. I love it and hate it at the same time because I'm like, damn it, I have to now reply to 200 comments. This is a pain in the butt, but it's a good problem to have. And it just opens up conversations because like, oh, thank you — how else can we help? It just, it's a natural conversation starter for the next step. So I wouldn't kick them over to Medium — just talk to them in LinkedIn would be my thing.

▶ **00:52:30 - Brandon Hancock**
And then if there's an extra tool — like if you want to get really fancy with it — you could be like, oh, if you give me your email too, I already have this other tool that goes even deeper. And it can actually go off and do a full report for you, where you're just continually offering value. And it's all free, but you got their email for it. That's literally exactly what I did for the AI Authority Accelerator.

**00:53:56 - Dr. Mohamed Samy**
Regarding this, I think, Paul, you're mentioning that you need to be a thought leader on LinkedIn for a specific industry, right? In my opinion, I think that thought leadership requires engagement and many reactions through your posts. And I think that each platform has its own algorithm that they work to elevate your viewership. So LinkedIn has a different approach and algorithm than YouTube or Facebook. And the nice thing is that through AI, all the machine learning algorithms, you can get like an API that will access all these algorithms and it will give you feedback on what will work for your posts. Like, for example, you can make an automation tool — you put in your first thought about the post, and then this automation tool will take this and call an API that will be linked to LinkedIn algorithms, and it will give feedback whether this will go viral or not, and then it will modify it again through Gemini [tool:Gemini] or any LLM, and then it will modify the post until the API tells it that it works fine and it will go viral.

▶ **00:58:41 - Brandon Hancock**
It's so hard to use AI to do something well if you haven't done it yourself first. So like, I think in your case, Paul, I'd start manual and try to emulate someone that's absolutely crushing it. And say like, I like these six posts, help me write mine — is what I would start with. But yeah, emulating someone first, and then next level is to get fancy, but let's just get going first, and we can get fancy.

**00:55:00 - Richard**
Yeah, if you can make it into a demo, you'll probably, like Brandon said, have a lot more success with getting those email addresses and kind of getting people signed up. The Product Launch Funnel was a really popular funnel at one point where they would give you like four videos from a topic — day one we do this, day two do this, day three we do this, and day four is pretty much like a little sales video that says, hey, if you've gotten value out of this, you don't have to do this alone, because we can do this and da-da-da-da.

▶ **00:55:09 - Brandon Hancock**
You are a LinkedIn master. I would just publish videos on LinkedIn. Let's just focus on where your customers are at, which is LinkedIn. Publishing videos to LinkedIn does really well right now because LinkedIn's pushing it right now — they just want more organic content on their network. So if you're going to record a video, use Screen Studio [tool:Screen Studio], record it, publish it on LinkedIn. By the way, here's a demo of it working. Comment this, and I'll send it to you for free. And then I think you do that for a month straight, and then together I'd be happy to look at results with you, and we can figure out some next steps.

---

<!--SEGMENT
topic: NYC Open Data Web Application and Manus AI Tool Exploration
speakers: Juan Torres, Brandon Hancock
keywords: AWS RDS, PostgreSQL, New York open data, data visualization, scatter map, sample size, trend analysis, Manus AI, MCP, GitHub, data pipeline, rodent complaints, data science
summary: Juan Torres demonstrates a data web application built on AWS RDS PostgreSQL that visualizes 600,000 New York City public complaint records with filters, scatter maps, and trend analysis. Brandon Hancock suggests experimenting with Manus AI to automate data analysis tasks, and encourages Juan to frame content around helping data scientists use new AI tools more efficiently.
-->

**00:59:14 - Brandon Hancock**
Next up is Juan. What is going on, man?

**00:59:22 - Juan Torres**
Nothing much. I've just been working on a project to develop a data web application regarding public data from New York through an API. So I had to set up the database through AWS RDS [tool:AWS RDS], and then I have to retrieve that information and put it into my application.

**01:00:01 - Juan Torres**
So this is the data web application that I'm retrieving through an API based on the public data from New York, and it's been stored in my AWS RDS environment database based on PostgreSQL [tool:PostgreSQL], and it's about 600,000 data points that I have to work with. So I had to try to break down the data in order to be able to display information based on certain filters, like we want to only look at animal abuse, specific year or range. Then we have the scatter map with the data points right here. Also, we can also filter this information based on ranges and dates. And then since there's so much data, what I had to do is just create a sample size of the data — a random sample size — in order to visualize the data based on a sample size of 1,000, 3,000, 5,000. And if I were to go more than 5,000, then the application starts working really slowly. So it's better for me to just create a random sample. And also we can parameterize based on the variables, as you can see right here. And then this is a trend analysis of the highest complaints on animals back from 2010, which is our latest range, all the way to 2024. And as you can see in New York, rodents are the biggest problems, particularly during summer.

**01:02:03 - Brandon Hancock**
<Q>Dude, so right — this is very, very cool. How are we going to leverage this to win? What are we going to do with this?</Q>

**01:02:15 - Juan Torres**
<A>Well, I was thinking that we could do a how-to video. Then I'm thinking of creating, together with someone else, creating a GenAI system to automate the process of analysis. And then also present this information like I did for the data pipeline for the concentration of banking data application.</A>

**01:02:47 - Brandon Hancock**
Out of curiosity, is it possible to go all in on just passing raw data sets into, like, Manus [tool:Manus]? Or some of these other more powerful tools to do this for you. That would be like a very cool experiment that I would like — I have that question. Like, could I give this data set to Manus and say, please make me a map, do trend analysis? And I would be curious if that could be — I think that's a very good tool. Like, that would be a very cool experiment to try out. At the end of the day, you type — M-A-N-U-S — like Manus. And then the AI — I would definitely sign up for it. I think you can use it for free, I think they have free credits, but like, I would be very curious to see if you can start to use some of these more powerful AI tools that go off.

**01:06:03 - Juan Torres**
I've been trying to also write some articles on the addition of MCP [tool:MCP] in order to increase my workflow. And I mean, they haven't gone viral at all. It's just me trying to share what I did in order to, you know, attach GitHub through my Cursor ID, and maybe that's something that other people may find useful.

▶ **01:06:38 - Brandon Hancock**
I think it's very cool. I think it's just framing it to the viewer of, like, here's how you can do this. Because that's what — focusing on how do we help them — is the main question people ask. So that would be the one thing. But dude, I love it. You were cranking out content. You're getting after it. This is very cool.

---

<!--SEGMENT
topic: Automotive AI Chatbot Progress and RAG Architecture
speakers: Maksym Liamin, Brandon Hancock
keywords: Nissan, automotive chatbot, PDF parsing, JSON, vector database, SQL, Azure Document Intelligence, Supabase, key-value storage, image metadata, multi-tool RAG, Cloudflare, evals
summary: Maksym Liamin provides an update on his automotive AI chatbot project (currently deployed for Nissan), reporting 500 new users onboarding and testimonial collection underway. He details the hybrid RAG architecture: PDFs parsed to JSON with LLM assistance and manual correction, a vector database for car specs, a relational SQL database for financing information, and a manually labeled key-value store for car images.
-->

**01:07:07 - Brandon Hancock**
Next up, we got Maksym. Dude, that's a sick hoodie. What's it say?

**01:07:22 - Maksym Liamin**
No, no, it's not the company. The company is called Icon. But this is the previous company of one of our partners. It's like a big marketplace — it was especially big actually in Ukraine and the former Soviet Union.

**01:07:51 - Maksym Liamin**
No, not that much. I mean, we are just moving forward. Everything is going great. Tomorrow we can onboard another 500 people to the tool. Everybody likes it. We've already started gathering some testimonials. So we have it for the next meetings because I think from May we start prospecting already other automotive brands — not only Nissan [tool:Nissan] that we work with directly, but others too. And yeah, everything is moving great. Also a lot of progress on the tool with Andrew. I hope really that we can start heavy testing it with users and yeah, we'll see how it goes. So both projects are going good.

**01:08:30 - Brandon Hancock**
<Q>I had a quick question back to you going back on the — for the car salesman. What was your end-up tool that you used for all RAG things? Did you go Docling at the end? Is that what you ended up using for everything or no?</Q>

**01:08:44 - Maksym Liamin**
<A>No, no, no. We just parse our PDFs as JSON and most of the time we do it just with an LLM and then with manual correction. So we do as much as we can with tools. I'm mostly using Anthropic's PDF processing [tool:Anthropic Claude]. And then we also change it manually because still not a single model that I have tried can do it properly. But I actually am about to try Azure Document Intelligence [tool:Azure Document Intelligence] layout model because we only tried the normal one. The normal one didn't do it good enough. But most of the time it's just manual. But again, it's very limited. And they don't update that fast — it may be like a new model every three months. So it's not that much of an overhead for us to do it manually for now at least. So we just put it all into the database and then we already have it all.</A>

**01:09:36 - Brandon Hancock**
<Q>And then so out of curiosity — so your approach was actually more pre-processing, meaning raw documents to JSON, JSON to database, database to LLM SQL query. Is that the next step? Or is it — that was the question I had with like, cool, I now know I want to talk about this car this year. Is it a SQL query? Is it something else?</Q>

**01:10:01 - Maksym Liamin**
<A>We have a mix of vector and SQL, so it depends on which kind of information is asked. We have different tools. Some of the information — for example, financing, how I can finance the car — then it goes into a separate database. Then we have a database that has just normal questions with car specs, and this is a vector database. And we have another one, which is just kind of a key-value storage for all the images. That was a really popular image asking. And we have it labeled — again, manually labeled — with all the metadata, for example, "rear view of Nissan March in blue in 2024." And then we have all the indexing, and we have different tools that query, and there can be that one answer consists of financing and some information about car specs and the photo. So it really depends on what the query and which information is asked.</A>

▶ **01:11:04 - Brandon Hancock**
That's very cool. I love the multi-search approach. And they consolidated it onto an awesome result. That's amazing.

---

<!--SEGMENT
topic: Audiobook Voice Synthesis with Multi-Character Support
speakers: Richard, Brandon Hancock, Bastian Venegas, sherif abushadi
keywords: ElevenLabs, OpenAI TTS, voice ID, structured output, Pydantic, audiobook, character voices, sentiment analysis, streaming, voice cloning, OpenAI FM, regex, JSON config
summary: Richard presents a completed audiobook reader that assigns different AI voices to different characters and narrators. He discusses limitations of OpenAI's TTS API voice selection and asks about adding emotional sentiment to voice delivery. Brandon Hancock recommends using OpenAI structured outputs with Pydantic to extract character, text, and emotion fields. Bastian Venegas clarifies ElevenLabs voice ID usage and streaming. Sherif Abushadi highlights OpenAI FM's voice annotation capabilities as a potential solution.
-->

**01:12:13 - Brandon Hancock**
Next up, we got Richard. What's going on, man?

**01:12:19 - Richard**
Tough month for me. My grandmother died the other day, but I had to go down to Florida and clean out her place and stuff. But I have worked on the last project that I talked about. I did get it done. And so the last project I was working on was an audiobook reader that would do different character voices and stuff like that for audiobooks. I tried to make it as automated as possible as far as like, hey, just give it any script in any kind of way. And then it would go in there and regex it up and stuff like that. But it was kind of not working. So I had to kind of give it a format and say, hey, like, I'm going to give you a script like this, and with a script like this, then separate the characters from here. And when I did that, I used OpenAI's new voice thing [tool:OpenAI TTS], but the voices are limited. So the voices are limited through the API. And then, like, how do you — for sentiment and all of that stuff — all of that stuff is kind of limited. Everything is kind of limited. So with that being said, it works great, though. I mean, it was very surprising to see the different voices come in on time. And your suggestion was right on point because I forgot — you add the delay that you told me to add, and so when the new character would come in, it would like pick up right where the other guy left off, and it was so unnatural, but with that tip, it was like, okay, boom, Brandon did tell me to put a delay there, so I did that.

**01:14:21 - Richard**
<Q>My question is, would I be better off using something like Eleven Labs [tool:ElevenLabs]? Because right now, I do have to find the voices in a JSON config file, so I have a config file where I give it all of the voices that will be in the script, and I assign a voice to a voice in the API, and then it knows that the narrator — if there's no name here — then the narrator reads all that. If there is a name, like "John said," and it will look in that config file, get John's voice, and then it will just start reading John's part whenever it pops up. But the problem that I am having is, is there any way to get it to just parse through any script without it needing to be in a certain format? And is there something — will I be able to use something like Eleven Labs if I want to add sentiment to the — I mean, it does a good job at reading it, and it's not too planned, but I would like to be able to raise the voice and it kind of analyzes that and says, well, this is a high-emotion scene, they need to be kind of yelling at each other?</Q>

**01:15:33 - Brandon Hancock**
<A>So I want to answer a technical question first really fast, and then we can go into the sentiment side. Okay, so whenever — it sounded like what you were currently doing is, like, if — to find which character you would see if the character's name was mentioned, like "John said" or something like that. What I really think we could be doing is setting up your initial script — like however you're creating the script — I think you could be using some Pydantic [tool:Pydantic] objects, like expected output format is the main thing I would be looking at, to where all it is is your script is a series of characters and text. So it always says the character that's speaking, and then it shows what they should be saying. You could add a third element, which would also just be like, for example, it could be like sentiment or like tone. You could add like, hey, you have four options of like different ways to say this — like normal, excited, sad, angry — like basically the emotion or tone. That would be the third object that I would potentially return. Character, text, emotion. And OpenAI does support that, because I think you said you're using OpenAI to produce it — basically it's in the structured response is what you're looking for. You want an array of those objects is basically what you're looking for.</A>

▶ **01:17:18 - Brandon Hancock**
Yeah, structured output [tool:OpenAI Structured Outputs] is the term that we're looking at. And it's actually, like, once you see this, you're like, damn, this was so easy. But they don't advertise all the proper things. But in the example I just sent you, what you're doing is you'll do the normal call to OpenAI, where you're doing a completion message. And then what you pass in the messages — and then finally, you say `response_format`. And that's where you pass in a Pydantic model of, like, character — you would have a `script` would be your overall object. And within a script, you would have like blurbs or soundbites or whatever phrase you want to call it, where you have speech, emotion, and character. And then once you have that array, cool. Now that you have the array with all the proper things, you might have to eventually afterwards do some sort of mapping to where like John's voice — whenever you see the word John as the character — in Eleven Labs play this character. So you'll have some sort of dictionary in your script to get it to work.

**01:19:51 - Bastian Venegas**
<A>Yeah, each voice that you can see in your dashboard when you're logging into Eleven Labs [tool:ElevenLabs], they have a voice ID. And you just need to pass that voice ID to the API call, and that's all. And remember to use streaming so it doesn't need to create the complete voice thing, and it instead just starts whenever it's ready to output the tokens. But even if you create your custom voice or clone something, that will have its own voice ID that you will pass to the API, so it's really flexible.</A>

**01:20:30 - Richard**
Okay, okay, got it. So instead of using a name, I can use the voice ID.

**01:20:33 - Brandon Hancock**
So the only other thing I would add to that, Richard, is like — from my understanding, each voice is like static. Like, it's one style. It's not like, it's not a voice and then an upset voice. Like, I thought you — don't you have to create a separate voice per style? Or is it one voice that you can then change inflections and everything? Because if not — what I was going to suggest is, Richard, is per character, create five different types — angry, happy, sad, the five different emotions, or whatever you want to list. And then whenever in your dictionary, when you get back "John angry," you have a map to say, "John angry" equals voice ID two. So you'll come up with five voice types per character.

**01:22:29 - Brandon Hancock**
Sharif, you dropped a good suggestion in the chat. If you don't mind elaborating a little bit for Richard.

**01:22:43 - sherif abushadi**
<A>All I know is that this was an innovation that OpenAI — you're talking about the OpenAI FM [tool:OpenAI FM], right? Yeah. There was a lot of fans around it specifically because you could give voice annotations and kind of modulate the tone the way you're describing. So I just did a quick scan of Eleven Labs, and it seems like per voice you can tune a handful of sliders around like exaggeration or speed or whatever. And so you can kind of enhance some of the qualities, but there's nothing as sophisticated as this kind of sort of the hints — text-to-speech hints — that you can do in OpenAI's FM Labs demo, basically, of something they have by API. I'm pretty sure this is available by API. This kind of keyboard-looking thing is just a demo that they made using that. And I remember it kind of hit the waves about a month ago. But everybody's really excited about it, because it was particularly capable at these intonations and stuff like that.</A>

**01:24:01 - Bastian Venegas**
Yeah, you can play around in the playground. OpenAI's playground [tool:OpenAI Playground] has the version of that dashboard. It's not the same, but you can do it directly, and then you see how the API behaves, actually.

▶ **01:25:48 - Brandon Hancock**
After looking at the example that Sharif sent, it is 100% possible to pass in and update with just some added tags to be angry or something like that. So yeah, I think OpenAI is the move for what you're trying to do, based on what they're saying.

**01:25:55 - Richard**
The only problem, though, Brandon, is that OpenAI has very limited voices. I think there's only like — that's the other issue I was kind of running into — is that I'm doubling up on some of the voices, just because there's not a whole lot of options there as well.

---

<!--SEGMENT
topic: Graph RAG with Neo4j and Query Rewriting Strategies
speakers: Bastian Venegas, Brandon Hancock
keywords: Neo4j, graph RAG, LightRAG, semantic chunking, HyDE, query decomposition, vector similarity, FastAPI, Cypher queries, knowledge graph, Pride and Prejudice, Shakespeare, retrieval strategies, cosine similarity threshold
summary: Bastian Venegas demonstrates a graph RAG implementation combining semantic chunking, Neo4j graph traversal, and multiple query rewriting strategies (HyDE, decompose, step-back, paraphrase). He shows examples using Shakespeare and Pride and Prejudice as test corpora, as well as coaching call transcripts. Brandon Hancock suggests this work could be broken into multiple focused YouTube videos explaining each retrieval strategy individually.
-->

**01:27:40 - Bastian Venegas**
Yeah, two different things I've been working here, like in the brand kit, with the tagline that we shared yesterday. But I wanted to show this graph RAG [tool:Graph RAG] implementation. And this is basically — it combines big search. It does the pipeline — starts with a bunch of markdown documents that are sanitized first, so you don't have problems with special characters. Then it does semantic chunking that basically uses a statistic thing that will try to have each chunk end in a logical place instead of just chunking based on characters. And then it just goes to this whole building — the graph and everything — and it mixes the similarity search and the graph and the document indexing.

**01:29:00 - Bastian Venegas**
Right now, the test corpus that I'm using has some Shakespeare and some other classical English literature. And the main thing here compared to a knowledge graph is that this uses more global entities and relationships — like, this entity mentions this one, it's next to this entity and stuff like that — while if you use the knowledge graph, this is the CAG thing that I posted in the school community that we use — the LLM will make the entities and relationships and all of that, but it will be specific to the domain knowledge that you use. So here's an example of something that has to do with the transcript of the coaching calls from the last couple of weeks, and this is just an example of asking what have Andrew and Maksym been working on.

**01:30:00 - Bastian Venegas**
And also this rewrite strategy, which is a way to rewrite your query. And you can use paraphrase, so it will just ask a similar question. You can create a hypothetical answer, and that will improve the similarity of the chunks you're comparing. You can decompose the question into several others. And you can step back — like, go one level more general than the question you're asking. So for example, here is the hypothetical document — and this is basically a general hallucination from the LLM, because this isn't accurate, but it's what the LLM thinks it could find in the corpus. So this is the answer synthesized by the final LLM after retrieving these chunks — that you can see are pretty good, they make sense, they don't stop abruptly at the end. And you can see which is exactly the source — which is the actual document — in case you want to review it manually.

**01:31:08 - Bastian Venegas**
You can also get these scores that you can use as the threshold. This is for the vector similarity. So right now those are 0.7. I put the threshold at 0.65, and the usual parameters go around there, like 0.7, 0.775, and all that. So for example, if I didn't rewrite the question, it's like this. And it did get a good answer, but here you can see that it didn't rewrite anything. So the chunks were pretty similar in this case. And you can also see, since I'm using Neo4j [tool:Neo4j], these are the Cypher queries that were executed down the road in case you want to debug something specifically.

**01:31:54 - Bastian Venegas**
And here's another example — this is something for Pride and Prejudice, and I'm showing this because when I just tested this and I didn't rewrite it, yeah, it returns null. But if you run the HyDE approach, since the LLM hallucinates — yeah, so here's what the LLM thinks, but this doesn't ensure that it's actually in the text. So this is a good test because you can see if this was answered by the general knowledge or if it really went and read the chunks. And here is something that it found with a score of 0.8, which — I didn't move the threshold at all. And then it found that it actually was set in this Pride and Prejudice. So yeah, that's in a nutshell. And it also has a FastAPI [tool:FastAPI] in the backend, and it runs really fast. That's something I really like.

**01:33:19 - Brandon Hancock**
<Q>So, in as simple as possible, why do you want to use HyDE? Is it because it is a fallback when RAG fails, so you can still give an informed answer?</Q>

**01:33:40 - Bastian Venegas**
<A>Why HyDE? Yeah, actually it goes more basically than that. It has to do with the fact that the query — if you create this as you would query a chat — the corpus is not really structured in a way that it will find this exact phrase. So you should really try to decompose or rewrite it. For example, this is decompose: "Who is the author of the quote?" "In what context is this set?" Or you could also use something like this, which uses more like the graph features. And basically the HyDE question is that it's trying to match the query to the format that the LLM expects the answer to actually be in the corpus.</A>

▶ **01:34:40 - Brandon Hancock**
Dude, for your channel, starting off — I think a video on breaking down the different retrieval modes, like that's a video in and of itself. A video on the strategies — I think that's a video in and of itself. Like each one of those is a really good listicle. Just to say, okay, so like, why this one's good, here's how it works, let me show you the results. Here's why this one's good, here's how it works, here's the results. Like, I would focus — that's a really good, quick video to make. This is just the main thing of just telling someone, like, why this applies, like, why they should even care. Like, that's the main thing. It's just, like, why do I care about MapReduce? Why do I care about Decompose?

**01:35:45 - Bastian Venegas**
I think that's a great idea, and I should just find representative queries that will just — oh yeah, I know this, like this rings a bell, and this makes sense — and then I can query with the rewrite strategy, and oh, this is the section in the corpus that actually says that.

▶ **01:36:00 - Brandon Hancock**
Yeah, just because these are so technical, so it's like — why do I care about this? And it's like, oh, you need Decompose because most of the time questions are not going to match exactly what's stored in your vector store. So you need to break it apart. Just breaking it down would be the only — that would be my feedback because this is all very cool. I really like this. Ping me for next week because I think it's going to be a cool first video for you.

---

<!--SEGMENT
topic: Session Wrap-Up and Upcoming Content Plans
speakers: Brandon Hancock, Paul Miller
keywords: Lovable, Bolt, V0, Replit, app building, content creation, LinkedIn, Adam Silverman, agent ops, YouTube, Screen Studio, platform comparison
summary: Brandon Hancock closes the session by previewing upcoming content: a comparison video of Lovable, Bolt, V0, and Replit for rapid app development, followed by a deep-dive Lovable and Postgres masterclass. He also recommends Adam Silverman on LinkedIn as a thought leadership example in the AI agent space, relevant to Paul Miller's content strategy discussion.
-->

**01:36:25 - Brandon Hancock**
All right, guys. Perfect. Well, we'll go ahead and wrap up this week's call. Yeah, updates from me. I'll have a video dropping soon on comparing different platforms to help you guys go from idea to app as quick as possible. So I'll have a video coming out on that pretty quickly. Deep dive into Lovable [tool:Lovable] the week after. And then starting hopefully late next week is when I'll become content machine Brandon.

**01:36:53 - Brandon Hancock**
And I got to hop on a quick call today with a guy that runs Agent Ops [tool:AgentOps]. Dude's a genius. And it was insanely cool because he was like, oh, if I was you — then he just like value-bombed for 30 minutes of like, you need to do this, you need to do this, you need to do this. So yeah, same to Adam. He is — if y'all get a chance — he is doing some amazing things on LinkedIn. So Paul, if you're looking for thought leadership, I would check out Adam Silverman on LinkedIn. He's doing it in the agent space. He was very, very helpful. So I just wanted to say good things behind his back — he's awesome.

**01:27:15 - Brandon Hancock**
Someone in the group chat recently was asking which tool to use briefly — Bolt [tool:Bolt], V0 [tool:V0], or Lovable [tool:Lovable]. So I was going to answer that question, so I'll have a YouTube video coming out of that soon. If y'all haven't tried Lovable yet to spin up your projects, your full-site project, it is unreal. So I'll be doing a video on that, and then a masterclass on Lovable and Postgres next week. So overview this week, deep dive next week. We were excited for that to come out.

**01:27:43 - Bastian Venegas**
Yeah, I probably need to add Replit [tool:Replit] to there, don't I?

**01:27:46 - Brandon Hancock**
Yeah, good idea.

▶ **01:37:44 - Brandon Hancock**
That's a wrap, guys. I hope y'all have a great rest of your Tuesday. Excited to make some more content for you guys soon. And yeah, please ping me if anything. Y'all are awesome. Can't wait to talk to you next week, guys.

---

=== UNRESOLVED SPEAKERS ===

- **Richard** — Last name not provided in transcript or alias map; passed through as "Richard"
- **sherif abushadi** — Raw name passed through unchanged (not confirmed in alias map)
- **Dr. Mohamed Samy** — Raw name passed through unchanged (not confirmed in alias map)