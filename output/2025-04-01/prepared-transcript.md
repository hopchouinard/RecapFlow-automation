=== SESSION ===
date: Not explicitly stated (Tuesday, recent)
duration_estimate: ~78 minutes
main_themes: AI image generation disrupting creative workflows, multi-agent frameworks for enterprise, agentic tooling landscape (CrewAI/LangGraph/Azure Foundry/OpenAI Agents SDK), knowledge graphs and GraphRAG for personal knowledge bases, cold outreach automation, Limitless AI pendant for ambient recording, community member project updates

---

<!--SEGMENT
topic: Introductions and Host Announcements
speakers: Brandon Hancock, Maksym Liamin
keywords: AI Authority Accelerator, OpenAI image generation, entrepreneurship, branding kit, YouTube content, Mexico City, Cancun, DALL-E, deflationary AI, content creation
summary: Brandon announces his transition from employment to full-time entrepreneurship and shares a real-time example of AI image generation replacing $1,000+ worth of branding work for his AI Authority Accelerator program. Maksym recaps a recent trip to Cancun. This segment establishes the session's theme of AI-driven cost disruption.
-->

00:00:22 - Brandon Hancock
So, guys, Maxim, you're not at the beach with the gang. You're not at the resort.

00:00:27 - Maksym Liamin
No, no, I'm already back. I'm back in Mexico City now.

00:00:33 - Brandon Hancock
Do you miss Paradise?

00:00:36 - Maksym Liamin
Yeah, actually, yes. I really liked Cancun. We went to two beach spots with a distance of two weeks. So one was Huatulco in Oaxaca, and another one was Cancun. They are basically two most famous resort places. But the second I liked more. Cancun is just too good. The ocean is better on the east side than on the west.

00:01:00 - Brandon Hancock
It's so funny. I saw Nate last night, and I was telling him about you. And I was like, you just broke my brain that you and Andrew were hanging out, just drinking a Corona, living up life. And I was like, man, I should be there with him.

00:01:20 - Maksym Liamin
You're always welcome here, man. You can come. We give you a flat anytime.

00:01:24 - Brandon Hancock
Dude, might have to take you up on that. Carly is always looking for an excuse to go on vacation.

00:01:40 - Brandon Hancock
All right, guys. Well, we'll go ahead and get things started off. So a few quick updates before we go around. A big announcement — I am officially unemployed or an entrepreneur, whichever label you want to use. So it's been awesome. Weirdest transition. It's so weird, like, waking up — a normal job, it's just like, I know where my next dollar is coming from. And now it's like, huh, well, I have an idea of where my next dollars are coming from, but not 100% guaranteed, because it's not like a normal paycheck or anything. So weirdest transition, but liking it so far.

00:02:23 - Brandon Hancock
This is the last week of — I apologize for the delay on content and YouTube — getting everything spun up for the AI Authority Accelerator [tool:AI Authority Accelerator]. There's literally so many things I've had to make this week. But after this week, everything will be on a regular cadence, and I'll get back to some videos. So I have some on OpenAI Assistants planned, some Lovable content coming up, and then after that, MCP. So there's just literally so many things to do.

00:02:52 - Brandon Hancock
Also, I just wanted to — final AI nerding out this week — give you guys an update. Let me share my screen.

Quick background for the AI Authority Accelerator: I'm helping people create a branding kit so they can go off and run their YouTube channels. And I was on track to hire multiple brand kit developers to create everything. And then the OpenAI new image generation feature [tool:OpenAI Image Generation] came out. And it has actually replaced 80% of the work I was about to hire a branding team for. In the past, I was going to have to pay them all like $100 each to create screenshots like this. And now there's no need to do it anymore, because this was created by AI, which is insane. I'll still hire some guys to help with headshots and stuff, but —

00:04:01 - Brandon Hancock
▶ In real time, AI is insanely deflationary. I was going to pay over a grand to make 10 of these. And now it's like, well, with my $20 a month subscription, it's done. So what was almost $1,000 is now $20. So it is wild to see this happen in real time.

00:04:33 - Brandon Hancock
But enough about me, guys. I want to hear all the awesome things y'all have been working on this week.

---

<!--SEGMENT
topic: Juan's Data Engineering Presentation
speakers: Brandon Hancock, Juan Torres
keywords: Federal Reserve data scraping, ETL pipeline, GitHub, API keys, Colab notebook, San Diego Data Engineering Group, LinkedIn networking, agentic system, regression model, client acquisition
summary: Juan Torres recaps a successful 15–20 person workshop where attendees scraped Federal Reserve data, built regression models, and generated scatterplots using a Colab notebook. The discussion pivots to strategies for converting presentation attendees into consulting clients or coaching students.
-->

00:04:51 - Brandon Hancock
Juan, you're up first. I would love to hear all about your presentation recently, hear how it went.

00:05:02 - Juan Torres
Yeah, it went great. 15 to 20 people came. We went through the presentation of the two data applications, and then I went through the Colab notebook [tool:Google Colab] workshop, and everybody seemed happy with it.

00:05:17 - Brandon Hancock
Dude, I know you said live demo. How did it go?

00:05:35 - Juan Torres
Yeah, the workshop went well. The notebook was successful in scraping the Federal Reserve, and then the people were able to have their own HTML, CSV code, and then their data sets that allowed them to create a regression model, a scatterplot. The only things that they weren't able to do was the uploading of the data sets to a GitHub repository [tool:GitHub], which is the loading aspect of the ETL data pipeline. And the other aspect was I didn't do the process of creating API keys for everyone, but there were some people that actually created their own API key before coming to the meeting in order for them to be able to use the agentic system. So, yeah, it actually went smoothly. It's more smoother than I thought it was going to be.

00:06:30 - Brandon Hancock
I was rooting for you. I was stressed because I was like, he's got it. He sounds confident. He sounds like he's ready for it. So I saw a LinkedIn post. I liked it. The room looked crowded. So it looked like it went well, but I've been waiting to hear your feedback on it. So, yeah, congrats, man. So what's up next?

00:06:53 - Juan Torres
In terms of presentations, I may actually have another presentation with the San Diego Data Engineering Group. They were supposed to do it this week. For some reason, they had to move it into another day, so we'll see how that goes.

00:07:14 - Brandon Hancock
Dude, you're going to be presentation famous. I'm very excited. You're networking. Just out of curiosity, any cool leads? Because that's one of the — you know, fingers crossed — I was curious.

00:07:32 - Juan Torres
Yeah, well, there was a lot of people that I was talking to after the meeting, and we exchanged LinkedIn, so they're following me. I still have issues with how to create the bridge between presenting my information and trying to acquire clients from presentations.

<Q>00:07:59 - Juan Torres
For you and for everybody else, how will you channelize the high value that you portray that you are able to bring to the table in a meeting in order to get leads as clients?</Q>

<A>00:08:16 - Brandon Hancock
Yeah, I'll go real quick. Every person in that room came with their own problems. So, if one of them was like a founder at a startup or at a big company that needed data science needs, they see you, they probably go, I'd love to have him a part of my company — so he's thinking, hire you. There's probably someone who's also like, man, I'm just learning all this stuff. I wish he would teach me — so he's thinking, coach me. And then there's probably some people that are like, man, it would be cool if he could do this for just a quick project that I need. So, there's three main ways that you could have gotten leads from that.

▶ The last thing I'd say is just follow up with every single one of them. Just because, you know, sometimes they just need a little suggestion — like, hey, what do you think? How can I help?</A>

00:10:09 - Juan Torres
A soft proposition of working together could come in great value in the future. As of right now, if there's no particular needs, they'll definitely remember me when they do have an issue similar to what they're facing. And especially because you're in presenter mode and everything that you're supposed to do works, and they actually are impressed by your applications — they can see them sooner or later coming to, or at least contacting to follow you or network or lead you to someone else that may need that.

---

<!--SEGMENT
topic: Agentic Frameworks for Enterprise and Digital Twins
speakers: Brandon Hancock, Sagar Passi
keywords: CrewAI, LangGraph, LangChain, Amazon Bedrock, Azure Foundry, multi-agent orchestration, digital twin, financial services, MCP, Dagger, tooling integration, agentic teams
summary: Sagar Passi shares a successful CrewAI demo to financial services executives and asks the group to evaluate agentic team frameworks for building employee digital twins. Brandon recommends CrewAI and LangGraph as current best options while flagging Azure Foundry as an imminent enterprise-grade solution, particularly for its tooling integration capabilities.
-->

00:11:28 - Sagar Passi
I've actually done quite a bit. I also had a presentation with the CEO. We kind of presented CrewAI [tool:CrewAI] and agentic teams to financial services. So I used a demo that I created and it went down really well. And we've got a few leads from there that we're chasing up. So it's really exciting.

00:11:57 - Sagar Passi
I also just came back from an event by a company called Dagger [tool:Dagger]. They do a lot of MCP kind of things. It's a new framework. I wasn't aware of it, but it was interesting to see what they're doing. So if anyone heard about them or know about them, it'd be cool to connect.

00:12:16 - Sagar Passi
And one thing I'm blocked on and I want to ask this group about — I'm looking for something like CrewAI. <Q>What else is there available for constructing agentic teams? One of the propositions we found in financial services is a digital twin and how we can actually co-create an employee to help them. Is CrewAI the right stack to build this? How can we go to production on it?</Q>

<A>00:13:00 - Brandon Hancock
Right now, it is like everything is on the cusp of making production-level agents easy — meaning Bedrock [tool:Amazon Bedrock] from Amazon. They're in the middle of creating everything on their side. Microsoft Azure's new — Microsoft Foundry [tool:Microsoft Azure AI Foundry] — their new agent suite is amazing.

00:14:01 - Brandon Hancock
So just to be clear, Bedrock already has features for multi-agent. So you could already set that up. The next one, obviously, CrewAI. Outside of that, LangGraph [tool:LangGraph] specifically — I wouldn't use LangChain as much. LangGraph itself does have capabilities for exactly what you're describing. Deployment is pretty straightforward on LangGraph. So that would be another alternative. It would really just depend on the workflow that you're trying to do.

▶ On the digital twin side, it sounds like you need context of everything that employee knows. So you're going to have to set up some sort of RAG. Part two is I don't know if the digital twin is taking actions or just feeding information back — that's the hard part.</A>

00:15:26 - Brandon Hancock
Microsoft Foundry — they're literally this close to unlocking the tooling part, because that's actually the biggest blocker for most of these frameworks. Without tooling, these agents are just really smart, talking back and forth, and they can't get out of the box very easily. But the second these enterprise versions allow for tooling, it becomes so much easier.

<Q>00:15:42 - Sagar Passi
Do you think it's worth going down the rabbit hole of CrewAI still? Or is it now time to do a bake-off between all the software you said?</Q>

<A>00:15:51 - Brandon Hancock
▶ If I had to tell a client tomorrow what to recommend — I couldn't tell them Amazon yet, and I couldn't tell them Microsoft yet because their stuff is just not there. I would definitely say, either right now today, CrewAI or LangGraph. Those would be the two immediate solutions I'd pick. But I would keep an eye out specifically for Azure Foundry — when they launch their new foundry thing, they're going to be the most popular one. I think they're going to win, hands down.</A>

00:16:56 - Brandon Hancock
Your digital twin obviously needs access to your email. It probably needs access to a few other folders. And they're making that tooling part insanely easy on Azure. So I am super pumped for Azure when they bring this out.

---

<!--SEGMENT
topic: OpenAI Agents SDK and Agentic Architecture
speakers: Brandon Hancock, Parker Rex, Sam
keywords: OpenAI Agents SDK, Swarm, browser agents, SEO automation, SaaS architecture, mono repo, RAG, context window, Stripe analogy, deterministic agents, resource consent documents
summary: Parker Rex shares his experience building and managing swarms of agents before the OpenAI Agents SDK existed, and explains how the SDK has simplified orchestration and observability. Sam describes a New Zealand resource consent document automation project. The group discusses the maturity of browser agents versus API-based approaches and the value of deterministic, reusable agent workflows.
-->

00:17:32 - Sam
<Q>Do you have any secrets to make more hours in the day, Brandon? Have you hacked that yet?</Q>

00:17:39 - Brandon Hancock
I mean, I'm on like coffee number five right now. So that's how I make the most of the hours I am awake.

00:18:13 - Sam
Yeah, I mentioned about doing a mock-up for someone. And, yeah, it just came down to a scoping issue. I think they're not entirely sure what they want, so I have to go back to drawing board with them. One of my colleagues complained that people are asking for magic, and my response is, well, we can probably do magic, but they just need to tell us what trick they want us to do.

00:18:58 - Sam
In New Zealand, when you want to do developments or do anything to a property, you have to file a resource consent request, and that can be a 40-page document. And I'm looking at essentially doing a first draft for those people who submit those applications. And I just wanted to understand how much — because you can go down the road of having knowledge graphs and really getting into the details about filling it accurately, or if they just want a template with something vibe-coded right — the effort and cost changes dramatically. So trying to figure out what they actually want.

00:20:36 - Brandon Hancock
All right, we're going to hop over to Parker. Parker, which is one of the first guys that I got to talk to when kicking off the program.

00:20:53 - Parker Rex
Yeah, I was just on YouTube. So a little background — I've been in the startup world for a little over 10 years and had one success. And then when AI dropped I was like, whoa, I should go all in on this. And basically just started building a bunch of different agents and realized when you're managing like a swarm of them — like over 20 — it gets very challenging. This is before the Agents SDK [tool:OpenAI Agents SDK], which should clean things up a little bit. It's before Swarm [tool:OpenAI Swarm] came out. And so now I feel a lot more confident in it.

00:21:57 - Parker Rex
But then I realized businesses really want these things if you make them deterministic. So that's kind of like the hack — how can you make it reusable? I've done client work: okay, how do I get a quick $25K in the door? What are the business goals? How do I align that to a stack? And qualifying is not always as important as disqualifying. So you can come into a new stack and it's like a total mess, and you just know — oh, there's no way this is going to be quick and easy.

00:23:00 - Parker Rex
I've basically been leveraging my own internal agent server that I rolled that has all the things that I like, to help me with client work so that I don't have to play the VC game. And then coincidentally, the Agents SDK came out and that's opened up a lot of doors for the SaaS app that I'm building.

00:23:23 - Parker Rex
And I owe you a big thank you because we did brainstorm and I just start unloading on all the different things. And you're like, whoa, whoa, whoa. Let's go to domain-based architecture. Like, what would this look like from a data perspective?

<Q>00:23:42 - Brandon Hancock
Quick questions for you — thoughts, experience, you liking it, loving it, hating it? Any advice to the group on the OpenAI Agents SDK?</Q>

<A>00:23:57 - Parker Rex
You know how Stripe packaged up a lot of stuff that existed before that you'd have to cobble together yourself? It's kind of like what OpenAI is doing — they're Stripe-ifying AI. You go in, now you have logs. Those are fantastic. So you can see what decision is it making, when is it making it — it's just in a nice little GUI. And then they just bundled up all the tools. You could do a lot of this stuff before, but now it's just packaged. You have all the tools in there and there's a bunch of examples.

▶ A lot of RAG isn't even necessary for a lot of use cases, where it's like — okay, 2 million context window, that's pretty dope.</A>

00:25:50 - Parker Rex
Everything was on hard mode before.

<Q>00:25:55 - Brandon Hancock
Out of all the agents, which ones have you used the most? Browser agents?</Q>

<A>00:26:00 - Parker Rex
Yeah, I think those are bar tricks to me. It's like this cool thing and it's good for development, but there's a lot — anytime you have these big movements, like when we went to mobile and everyone was running the cloud, you have these intermediary kludgy solutions to things and they won't last long, but they're necessary now. They're like the stepping stones.

▶ Some of the browser agent ones — why wouldn't I do something behind the scenes if there's an API that I can tap? The only thing I've built with the browser one that was worth its salt that you could make money on is for clients doing automated multi-step SEO audits: on-page, off-page performance, doing an internal link check to scrape every single page and find where we could link stuff in, finding relevant sites for outbound automation to do link sharing.</A>

---

<!--SEGMENT
topic: OpenAI Image Generation for Branding and Thumbnails
speakers: Brandon Hancock, Bastian Venegas
keywords: OpenAI image generation, DALL-E, Runway Gen 4, Sora, YouTube thumbnails, CrewAI, Docker, branding kit, infographics, Midjourney, digital marketing disruption
summary: Bastian Venegas demonstrates OpenAI's new image generation model applied to YouTube thumbnails and infographics, including a technically complex thumbnail showing CrewAI deployed via Docker across multiple platforms. Brandon and Bastian discuss how this capability is replacing expensive freelance branding work, echoing Brandon's earlier cost-disruption example.
-->

00:29:09 - Bastian Venegas
Hey, guys. I have been playing a lot with the image generation from OpenAI [tool:OpenAI Image Generation], and I also tried again Sora [tool:Sora], which wasn't really amazing. I think Runway Gen 4 [tool:Runway Gen 4] looks much better, but the image generation is really impressive. And in fact, I was trying to explore how it works internally with some prompting. And it's very interesting. I probably will make a post about it in school at some point.

00:29:54 - Bastian Venegas
And I wanted to maybe show you guys a few of the image generations that I have been doing. Because I totally agree with Brandon in the sense that this is a total game changer for YouTube thumbnails and branding stuff and all of that.

00:30:36 - Bastian Venegas
Yeah, so this was the idea that I showed you guys a few weeks ago. And I think the idea was cool, but the execution was really poor. So this section — I don't know if you can see my mouse — but this was the old DALL-E [tool:DALL-E]. And this was just like, I'm trying to stitch things up. But when I gave this idea to the new model, and I kind of explained what I was aiming for, it came up with this — which is like, deploy CrewAI anywhere through Docker [tool:Docker] in this kind of platforms as example.

00:31:26 - Bastian Venegas
And after some iterations — oh, well, this is unrelated, but it's just to showcase how it's very powerful for infographics. They say it can render up to 15 or 20 elements with their own characteristics in a decent way, like best of three or four generations maybe. This is like for a YouTube banner. Just put a picture and describe the theme and ask it to do it in anime style and describe the background colors. And that was pretty much it.

00:31:56 - Bastian Venegas
And this is my favorite — which represents the thumbnail without the text, but this image has the CrewAI icon on top of these containers that are local, Railway, and Azure, and that's all on top of the whale that's Docker.

00:32:24 - Brandon Hancock
What's wild, guys, is getting — I mean, was going to tell you — like getting a thumbnail designer to do this: technically in the past, what they would have had to do is literally make an AI image of the Docker, of the local computer, and the CrewAI. So boom, that's three digital assets that they would have had to make with AI. That's going to take time. Then from there, they would have to make little standing pods — use Illustrator, or once again use Midjourney [tool:Midjourney] to make all these different elements, put it all together, and set the background. Like this could have been realistically probably $80-ish. And then now the fact that you get to do this in minutes and it's perfect is insane.

00:33:15 - Brandon Hancock
▶ Right now, my heart goes out to all digital marketing thumbnail designers and everyone because that is crushing. I hope we have a few more years of goodness for developers because like I just said — I was about to spend a grand to help with this stuff. And there was just no reason to do it now because it's better and it took me minutes.

---

<!--SEGMENT
topic: GraphRAG and Knowledge Graph for Personal Knowledge Base
speakers: Brandon Hancock, Bastian Venegas, Parker Rex, Nate Ginn
keywords: GraphRAG, Neo4j, Leiden algorithm, Notion, knowledge graph, embeddings, Microsoft GraphRAG, graph database, EHR, medical records, agentic proposals, vector database
summary: Bastian Venegas demonstrates his implementation of Microsoft's two-phase GraphRAG system combining traditional graph algorithms with LLM-generated entity relationships, applied to over 1 GB of Notion documents. The discussion covers the Leiden community detection algorithm, Neo4j as the graph store, and potential healthcare applications for connecting patient records and clinical documents.
-->

00:33:50 - Bastian Venegas
And the other thing I have been playing with is the Microsoft implementation of this two-phase RAG that combines a graph with GraphRAG [tool:Microsoft GraphRAG], and I'm trying to run that. I tested it with a small corpus of text of Markdown documents. So there's a bit of preprocessing there. And then that goes to an algorithm — it goes to actually embeddings and also to the Leiden algorithm [tool:Leiden Algorithm]. That is the one that Microsoft recommends for building the communities that represent the relationship between the different entities.

00:34:40 - Bastian Venegas
I found it can be very powerful. I've experimented with other systems. And this is the one that initially seems best suited, at least for my use case, which is basically — I have a really huge Notion [tool:Notion] database, mostly Markdown documents with different thoughts and projects and some code as well. And I want to make that available to the agents, so I can draft, for example, proposals for client work and have it mention related projects or something that can be similar to what the client is looking for.

00:35:18 - Bastian Venegas
And I also built a graph. Yeah, so this is not the GraphRAG implementation, but you can see — this needs screening because it has these UUIDs and there are some untitled documents — but it's just to show what it can represent. And this is the full representation for the over one gigabyte of Notion documents.

00:36:02 - Bastian Venegas
And this was like a mistake when I was first exploring it, because the relationships should really be done not through the hierarchical position of each document and its titles, but instead you should have a way to reference each document — but all of the building of the relationships are actually done by the GPT model.

<Q>00:36:29 - Parker Rex
How did you make this? This is an HTML output of a knowledge graph relation? Is that like vector space represented as a knowledge tree?</Q>

<A>00:36:39 - Bastian Venegas
It's not embedded, but this is like some older machine learning algorithms to represent the relationships between each document. But this is more hierarchical, because each document is contained within a page, and that is a sub-page of something else. That's basically the relationship I'm showing here. The definitive representation is much cooler, and it's done through Neo4j [tool:Neo4j], and that has its own interface. You can run the queries here, and it will surface what you kind of need — it contains the graphical representation as well as the output of the query.</A>

00:38:00 - Brandon Hancock
Very cool, man. This is next level. I'm very excited because I knew you said it was like the hierarchical setup right now, but when it's actually like full thought-to-thought representation — I'm very excited to see what that looks like, how many edges you end up getting, and then also what the new updated responses are going to be.

00:38:24 - Bastian Venegas
I will have it ready for next week, for sure.

<Q>00:38:29 - Nate Ginn
I know you're in the medical field too. Is this something that you could see implemented as, like, the database side of an EHR, where you have patient information, and then all of the other — whether they're uploaded documents or chart notes or scripts — all connected together?</Q>

<A>00:39:00 - Bastian Venegas
▶ I can totally see that because if you dive into how data is represented, it's very suitable for graphs, especially because they also have this hierarchical internal structure where each patient has different resources and procedures have resources, and there's all this built-in hierarchy which you can actually embed into the system.</A>

---

<!--SEGMENT
topic: SaaS Business Strategy and AI-Powered Lead Generation
speakers: Brandon Hancock, Paul Miller, Parker Rex
keywords: Salesforce, SaaS moat, Notebook LM, deep research, cold outreach, Instantly, lead scraping, consumer goods, agentic research, Google Gemini 2.5 Pro, AI Studio, competitive differentiation
summary: Paul Miller discusses the competitive pressures facing his 10-year-old SaaS business from both enterprise players like Salesforce and AI-empowered individual competitors. The conversation pivots to AI-powered lead generation and cold outreach automation, with Brandon recommending Instantly's YouTube channel as a case study in AI-driven sales. Paul also highlights Google Gemini 2.5 Pro in AI Studio for large-context code generation.
-->

00:39:46 - Paul Miller
Congratulations again, Brandon, on being disconnected from the rest of the world.

00:41:25 - Paul Miller
In the last week, I've been mainly focused on getting sales closed for my primary business that provides primary income. For those who don't know me that well, my primary business is a traditional SaaS business that was set up 10 years ago. Our customers are corporates in the consumer goods space, and they've got lots of money to spend on stuff, and we charge them a decent enough amount each month. So I need to be able to expand the recurring revenue for that business, but I'm getting contention now from the big players. Salesforce.com [tool:Salesforce] is one of my competitors, and they spend more on tech marketing than any other tech business in the world.

00:42:37 - Paul Miller
And then with the medium to larger businesses, we're getting smart individuals that are using AI to challenge some of the stuff that we're doing. And the reality is — using the deep research that I've talked about in the last few weeks, Notebook LM [tool:NotebookLM], to build — well, why are we good? Why should companies work with us? The fact that we've already built the tool, it's not just one person sitting in the company that goes on holiday and then suddenly all the knowledge has gone out the door.

00:44:17 - Paul Miller
How do you build a moat around that and continue to add value? I've been trying to build strong business cases, get those customers across the line. I think the simplest way to solve it is just win as many customers as possible and sell the business as quickly as possible and secure the bag.

00:44:51 - Paul Miller
I've played a lot further with the Google Gemini 2.5 Pro [tool:Google Gemini 2.5 Pro] model on programming. And for those that haven't had a play with it, it's utterly fabulous. ▶ Rather than going down the path of using it in Cursor, go into AI Studio [tool:Google AI Studio] and take blocks of your code and have a play with it, because it's quite good at looking at that — using that million to two million context and grabbing it all together. I've been getting some really great code at first prompt.

00:45:42 - Brandon Hancock
That's awesome. Yeah, the 2.0 — just not Pro — was like not good at programming, but obviously its context was insane. So it makes me so happy to hear that 2.5 Pro is at the point now where it's actually cranking out great code. In my opinion, long term, I think they're going to win. If I had to bet on a horse right now, I think it's going to be them.

00:46:08 - Brandon Hancock
I would be very curious if that end of itself is a business ready for just a service offering — lead scraping. Because how many other businesses need leads? Anytime your business needs a lead, whatever you just did, that means there's hundreds of other people who need the same thing. Just might not have the same technical know-how.

00:47:00 - Paul Miller
It's a good one because when you talk to other people out there in the market, everyone wants to expand their customer base, especially in challenging commercial times. But I don't know about your inbox — I get so filled with people trying to sell me that service. It's how do you differentiate yourself against all of those people that are selling that service? You kind of want to add a lot more pre-qualification and insights about those leads. Because a lot of those companies are very generalist in the way that they do searching.

00:49:09 - Paul Miller
One of the things I've thought about is — it's not just identifying potential customers, but it's identifying the sales opportunity. So say if a friend of mine advises a large business that sells tires — what makes a good tire seller? Who are the leading tire sellers in the market? Why do the customers like them? And why do the customers complain about them? Looping all of that information together with who are the people that you need to get across the line — if you came to someone and said, we can help you with your business, not only can we get you customers, but we can talk about where you sit in your market against your competitors.

00:50:52 - Brandon Hancock
▶ Cold outreach with agents is about to be insane. Like it's already getting much better than it used to be — just autofill name, industry, something, random fact. But now pretty much everything going forward will have some sort of agentic research value-provided portion to it to help stand out. Instantly [tool:Instantly] is starting to do very well in this. If y'all haven't watched Instantly's YouTube channel [link:Instantly YouTube channel] on one of their founders going off and actually creating a cold email campaign with AI — he actually just makes a fake business in a week and a day, sends out a thousand leads, and he actually gets a customer. It isn't even a real business. He just wanted to show you that it works. Watch me start and sell a service in ten hours — it's their most popular video.

---

<!--SEGMENT
topic: Limitless AI Pendant and Life-Logging API
speakers: Brandon Hancock, Maksym Liamin, Juan Torres, Paul Miller, Bastian Venegas
keywords: Limitless pendant, life log, ambient recording, transcription, API, WhatsApp bot, Azure CLI, agentic task automation, wearable AI, voice input, dealership chatbot
summary: Maksym asks about Brandon's Limitless AI pendant, prompting a live demo of the device's real-time transcription and life-log API. The group discusses potential applications including integrating ambient audio capture into Maksym's WhatsApp-based car dealership bot, and building an agent that automatically converts life-log entries into actionable tasks. Paul Miller reveals he has one on order.
-->

00:54:51 - Brandon Hancock
Hit us. What awesome projects are you working on? And did you hear your buddy Cyril — he got an offer?

00:54:57 - Maksym Liamin
Yes, yes. I know. I know that he got an offer. That's really great. He still needs to discuss it more with these guys because he's using my strategy — applies as if you have a degree and then tells them whenever you already impress them. So now the problem is that he doesn't have a degree and they normally don't hire undergrads. And now he needs to just see how it goes — he already talks with the manager, and they're now kind of investigating if they can do it. But if he doesn't, he will be kind of the first employee that doesn't have a degree in this whole company.

00:55:52 - Maksym Liamin
And on my side, this week was more chill. Because now everything is launched, and we're cruising, and also I was on vacation, basically, so life is great.

00:56:09 - Brandon Hancock
Any feedback so far from the launch group, just out of curiosity?

00:56:16 - Maksym Liamin
They all really like it. The majority of the use cases are for just images to actually show the cars right in the dealership. Because, for example, you want to see one model but in a different color, and before they used to just pull out stuff from the website that has fancy brand pictures, but people don't like it. And our database has all of the models and all of the pictures in different angles, but shot just on the phone, so it looks really very real, and that's what people like. And still, the majority of the input messages are not coming from text, but from audio.

00:57:41 - Maksym Liamin
I saw in school that you bought this pendant, the Limitless [tool:Limitless Pendant]. Are you actually using it? What do you think about it?

00:58:56 - Brandon Hancock
So it lasts almost two days — pretty wild, two full days. Obviously you turn it off when you go to bed, but it lasts the entire time. It records all conversations. So what was nice was — I call it going on a thought walk — where I literally will go walk and just say what I need to do for the rest of the day. And it does it in real time. Like in real time, you can see — oh, you're saying hey to this person, if you say your name, it'll understand what you've said and what you've done.

00:59:38 - Brandon Hancock
▶ It's almost like I have an assistant walking around with me, creating my schedule at all times. If I say "action items," it'll say — hey, these are action items you did today. You said you were going to do them, did you do them? So that's great, because I'm always hopping between calls and I can't always write it down on paper.

01:00:06 - Brandon Hancock
One of my friends — Nate — he went to a convention recently and he just wore it the entire convention. And the amount of people that gave him advice on what they need to do for their business — literally thousands of dollars worth of advice. Instead of scribbling down left and right, he was just there in the conversation. And then when they got home, they were like, all right, give me to play it back. And it's there forever. ▶ It literally paid for itself in like 10 minutes at that conference.

01:00:47 - Brandon Hancock
The only kicker is you can only ask about a specific day. It is day-by-day question asking. I can't say like, hey, the other week I was on a walk and I met a guy — what did we say? It doesn't do that yet. So that's the main kicker I dislike.

<Q>00:58:46 - Maksym Liamin
I saw in school that you bought this pendant, the Limitless. Are you actually using it? What do you think about it?</Q>

00:01:02 - Juan Torres
I just wanted to ask — is there no modulation in order to save all the conversations in a vectorized database, and then you can use all of that and conceptualize the AI in order to give you advice on that database?

<A>00:01:24 - Brandon Hancock
So here's what's really cool — they do have an API [tool:Limitless API]. I haven't played with it yet. But yeah, in real time, what you can do is access what they call the life log. So life log basically just gives you a list of entries on a specific date.

▶ What I would love to do is make an agent that all it does is listen to my life log, and from there it takes tentative actions on my behalf. So like — oh, you said you were going to respond to so-and-so? Cool. Either make a task, write the email, just go ahead and do it. So whenever I sit down and look at my active task list, it's right there. That would be the next step. I'm surprised they haven't done it — like, life log actions or something like that.</A>

01:04:43 - Juan Torres
I use mostly AWS. I just wanted to ask you, why do you opt in for Azure?

01:04:53 - Maksym Liamin
We just had $5,000 free credits in Azure. That's why. I like that Azure has OpenAI models because it's also what we use, but again, mostly because of the credits.

01:05:36 - Maksym Liamin
Mostly to just test how it would work in comparison to what we have right now with this bot. As I said, just to give it to, let's say, one salesman out of a group and say, okay, you have this on your jacket, and to see how it improves the user experience. That's the only kind of way I was thinking about it.

01:06:25 - Brandon Hancock
▶ Never use the Azure graphical interface. Like don't even open it — it's not worth it. Their approach for just doing anything just takes so long. Make a project, make a resource, make a hub — there's 10 things to just press go. It breaks your brain.

---

<!--SEGMENT
topic: Healthcare Tech, Document Automation, and Closing Updates
speakers: Brandon Hancock, Nate Ginn, Andrew Nanton
keywords: LangChain Markdown splitter, document chunking, resource consent, EHR integration, Dropbox, medical records, agentic document generation, minimum viable document, OpenAI Assistants, MCP, Lovable, content roadmap
summary: Nate Ginn shares plans for a multi-provider medical practice and envisions automated document sharing between providers and attorneys. Andrew Nanton offers practical advice on AI-assisted document drafting — emphasizing the value of a minimum viable first draft — and recommends LangChain's Markdown header splitter for structured document chunking. Brandon closes with his upcoming content roadmap including OpenAI Agents, Lovable, and MCP deep-dives.
-->

01:07:37 - Nate Ginn
I don't have a lot. I've been busy expanding my business and man, it's been strange. I might actually be getting a divorce from my current partner already after one month.

01:07:55 - Nate Ginn
What the good news is, is that I'm being courted by another group who really wants to blow up my business big time. But the thing is — the reason I asked Bastian about the database thing — is because it's funny, because now when I go into these business deals, all I think is, how could I create software to make this better? What can they do to automate these processes?

01:08:30 - Nate Ginn
One of the things that this new project is doing is it's going to be a bunch of different providers — medical specialists that are coming together to basically treat injured patients from auto accidents and stuff like that. And so you have a lot of these relationships with both other providers and attorneys, and of course they're all using different software to manage their cases. And so I thought, man, wouldn't it be cool, just from a marketing perspective, to be able to go in and create something you can just download on their thing that says — look, attorney, if you want access to everything we've done, which right now you have to fax and request records and bills and all that stuff — wouldn't it be great if as soon as we did it, it just dropped right into like a Dropbox [tool:Dropbox] kind of thing or a database that they access on their stuff?

01:09:31 - Nate Ginn
Anyways, that's where my mind's been going lately, but I haven't had time to hardly write any code, which is driving me nuts. I'm literally going through withdrawals.

01:09:38 - Brandon Hancock
You're wearing all the hats right now. Business owner, healthcare — you're wearing every hat right now.

01:09:45 - Nate Ginn
The only time we get to code is like from 10 to 2 in the morning when everybody's asleep.

01:10:17 - Brandon Hancock
All right, Andrew, you are last up. What's been going on? Anything fun?

01:10:24 - Andrew Nanton
So, well, lots of fun stuff. Not a lot to report. As you saw last week, I was hanging around in Mexico.

01:10:55 - Andrew Nanton
Another idea here — I'm just spitballing — maybe you just get everyone together. We're going to need satellite internet, but we'll have a hackathon on the sea.

01:11:15 - Andrew Nanton
So, yeah, I'm sorry that I missed Sam because his idea of putting something together for remodeling homes and the paperwork that needs to go with that — I mean, for what it's worth for people who are still here on the call, I would say that for these big, complicated documents, having a first draft where you're, one, not just staring at a blank screen, and two, if it went in, it may not be great, but it wouldn't necessarily be a ridiculous failure — there's really something to be said for that. Like just a minimum viable document.

▶ It's easy to revise and improve a document when you know what it needs to look like. Just having something to get you started — even if you had just an intern who had no idea what they were talking about, you're like, just fill out the parts that seem obvious. They can get through even the most tedious parts, which are often the parts that make you want to pull your hair out. It's not because they're hard. It's just like you just have to go through the motions of it.

01:12:42 - Andrew Nanton
▶ If you can get 40 percent of the way to a completed document — it's like in physics class, it's the static versus sliding friction, right? Once the ball is rolling, it's just so much easier to keep going.

01:13:00 - Andrew Nanton
And if anyone else is doing longer-form report generation kind of stuff — some of the stuff that I was telling you about last time — taking chunks out of things using the LangChain library [tool:LangChain] for Markdown is a great way to go. I'll find it and put it in the chat.

▶ You can chunk a document by header. So like, one pound sign — everything that's under one pound sign, all the subheadings — just pull all of that. In terms of breaking something up — what I'm using for my template is basically a template that says something like, at the top-level heading, this is describing the current state of the property, and the reason why it needs to be revamped, or whatever. But it's very descriptive and it's very effective.

01:14:44 - Brandon Hancock
Yeah, that'd be awesome. I just remember seeing it last time and I was just like, that's very powerful — the custom parser — because it's how humans think. Humans organize their documents that way: header, body. That was probably one of the most efficient chunkers that I've seen and heard about.

01:15:06 - Brandon Hancock
All right, guys. Well, if you haven't had a chance to go yet, feel free. If not, guys, yeah, just a quick recap of what's coming up. This is the last week of spinning everything up. So I'll be back to — I cannot tell you guys how pumped I am for next week to be content machine Brandon. I'm going to wake up, chug a coffee and record and just do that every day.

01:15:44 - Brandon Hancock
The main things that are going to come out — the order will vary — but it's going to be OpenAI Agents [tool:OpenAI Agents SDK] as one of the first ones. A Lovable [tool:Lovable] collaboration. And then after that, diving into as many MCP [tool:MCP] ways as I possibly can. And then after that, there's a thousand things. I'll be sending out a poll next week of are there any specific topics you guys want me to look at.

01:16:24 - Brandon Hancock
I do want to go a little bit deeper into some of the enterprise agents that are coming out — just to show what's possible because they're coming. They're there. They're just a little hard to use right now. I definitely want to have the Azure one — the Azure agent framework right now is winning. It will at least give it two more weeks, three more weeks when they launch their new Foundry thing. And they're going to be the most popular one.

01:17:14 - Brandon Hancock
If you want to get a brain teaser in for the day, go look at Tom's post for the traveling salesman problem that he just dropped — 49 cities. That is a perfect job interview question right there. So if you want a brain teaser for the day, that's your homework. Leave it to Tom.

01:17:37 - Brandon Hancock
All right. Well, that's a wrap, guys. I hope y'all have an awesome rest of your Tuesday. I will be dropping the recording immediately after this, whenever Fathom [tool:Fathom] finishes processing it all. But yeah, seriously, great seeing all of you guys. Can't wait to see you next week. Thank you. See you guys. Have a great one. Bye.

---

=== UNRESOLVED SPEAKERS ===
- Sam (last name not provided in transcript or alias map)