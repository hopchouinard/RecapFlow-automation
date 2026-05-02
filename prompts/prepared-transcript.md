=== SESSION ===
date: Unknown (April, tax season context suggests mid-April)
duration_estimate: ~81 minutes
main_themes: AI model comparisons (Claude/Gemini/ChatGPT), enterprise agent deployment (Microsoft Copilot/Foundry/Anthropic), local LLM infrastructure (Proxmox/OpenClaw), agentic coding and SDLC transformation, user-driven development workflows, RAG database construction, government RFP automation, event management platform demo, Presidential AI Challenge win

---

<!--SEGMENT
topic: Session Open and Recap
speakers: Patrick Chouinard, Marc Juretus, Ty Wells, Paul Miller, Andrew Nanton
keywords: RecapFlow, text-to-SQL, Slack integration, Claude Code, Obsidian, Andrej Karpathy, lightweight RAG, SEO agency site, Codex, Markdown
summary: The session opens with casual weather chat and a review of the previous week's demos using the community's RecapFlow tool. Topics covered last week included a text-to-SQL Slack integration, SEO-optimized agency site rebuilding, Claude Code with Codex, and Andrej Karpathy's lightweight RAG system using Obsidian. Ty Wells joins briefly from a golf course for a comedic "presentation."
-->

[00:00:30] Patrick Chouinard: Hey Marc!
[00:00:30] Marc Juretus: Good to see you there, Patrick.
[00:00:34] Patrick Chouinard: How's it going?
[00:00:36] Marc Juretus: It's going okay, you?
[00:00:39] Patrick Chouinard: Good, good.
[00:00:42] Patrick Chouinard: The sky is falling around here. It's raining like mad, but April in Quebec.
[00:00:50] Marc Juretus: Oh, that's where you're in Quebec. It's about 80. Kind of humid, but it's at least warm.
[00:01:23] Marc Juretus: Anything I had to miss last week — anything particular, let's put it that way.
[00:01:32] Patrick Chouinard: To be really honest, I now rely so much on RecapFlow [tool:RecapFlow] that I don't remember it by heart. If you look at the school community, there's now a full detail recap with everything.
[00:02:00] Patrick Chouinard: Oh yeah, we had a couple of demos that were interesting last week. Someone showed us a text-to-SQL [tool:text-to-SQL] platform that integrated with Slack [tool:Slack] that was kind of interesting.
[00:02:14] Patrick Chouinard: How to rebuild the SEO-optimized agency site.
[00:02:20] Patrick Chouinard: Claude plus Codex [tool:Codex], so developing with both systems together.
[00:02:29] Patrick Chouinard: Yeah, so there was — oh, obviously the lightweight RAG from Andrej Karpathy [tool:lightweight RAG] using Claude Code [tool:Claude Code] in Obsidian [tool:Obsidian].
[00:02:41] Marc Juretus: <Q>What's Obsidian? Why am I drawing a blank on that?</Q>
[00:02:44] Patrick Chouinard: <A>Note-taking application. It's a free note-taker. It just takes notes in Markdown, so it allows Claude Code, Codex, all of those to basically write all the notes themselves directly.</A>
[00:03:00] Patrick Chouinard: Andrej Karpathy created a very, very optimized prompt where you could digest or ingest pretty much any type of content and store it and document it inside of an Obsidian Vault. So pretty interesting.
[00:04:49] Ty Wells: Hey, guys. I'm presenting the golf course today, so that is my presentation. So my presentation is done. I'll be listening in. That's about it.
[00:05:05] Marc Juretus: This guy, hackathons and golf courses.
[00:05:39] Ty Wells: Cheers, guys.
[00:05:44] Ty Wells: That was my presentation. I'm going to go off video now.

---

<!--SEGMENT
topic: AI Model Preferences for Voice and Daily Use
speakers: Patrick Chouinard, Marc Juretus, Paul Miller, Andrew Nanton
keywords: ChatGPT, Claude, Gemini, voice interface, conversational memory, Gemini Gems, system prompt, OpenClaw, Google certification, stock analysis
summary: Participants compare their daily AI model preferences across voice interaction, conversational continuity, and specialized tasks. Marc favors Gemini for day-to-day conversation and its YouTube integration, while Patrick argues ChatGPT leads for voice interaction but acknowledges system prompt tuning makes a significant difference. The group also discusses Gemini's "Gems" feature for stock analysis.
-->

[00:03:17] Marc Juretus: I'll say this — as far as conversational flow that you're going to maintain over days, I've used ChatGPT [tool:ChatGPT] to a point, and I think Claude [tool:Claude] excels way above everybody when it comes to code, but Gemini [tool:Gemini], because since I had that Google cert, I was starting to use it a little more. Just conversation from day to day and leaving off where you left off — plus it's pretty seamless to YouTube because it's part of their product. I've been using their Gems [tool:Gemini Gems] where I pass it a stock symbol and it'll give me detailed analysis.
[00:04:06] Patrick Chouinard: The way I converse is always vocally, and for that right now, nothing comes close to ChatGPT, sadly.
[00:04:13] Marc Juretus: I don't know if I agree with that, but we can beg to differ. I use it all the time, dude. I talk all day to it. I mean, my OpenClaw [tool:OpenClaw] agent is actually pretty good too, but I don't know, man. Just for my 20 hours a month, I never run out. It's pretty slick.
[00:04:39] Patrick Chouinard: Mind you, there might be the thing that I've tweaked their system prompt to hell, and that makes all the difference in the world.

---

<!--SEGMENT
topic: Enterprise Agent Deployment on Microsoft Stack
speakers: Marc Juretus, Patrick Chouinard, Andrew Nanton, Paul Miller
keywords: Copilot Studio, Microsoft Foundry, Azure, SharePoint, M365 connector, Anthropic partnership, Claude, Power Automate, Service Manager, authentication
summary: Marc raises a real-world enterprise challenge: deploying an employee assistant agent at a hospital connecting to SharePoint, Service Manager, and a proprietary CMS. The group discusses the Microsoft Copilot Studio vs. Azure Foundry tradeoff, the recent Anthropic–Microsoft partnership bringing Claude into Copilot, and the limitations of low-code Power Automate for agentic workflows. Patrick recommends watching Anthropic's managed agent developments before committing to Copilot Studio.
-->

[00:11:47] Marc Juretus: <Q>Yeah, what I probably would want to ask is — my place of business, a hospital, they are starting to try to get some chat agents that are going to connect to Service Manager, SharePoint, maybe submitting tickets and stuff like that. Has anybody done a deployment at work where they had an agent of that nature — an employee assistant agent — where they actually either leveraged Copilot Studio [tool:Copilot Studio] or even deployed something from Foundry [tool:Azure Foundry] because we're an Azure shop?</Q>
[00:12:48] Patrick Chouinard: <A>We haven't implemented anything yet, but we are in the same case — we're a Microsoft shop as well. Until a couple of weeks ago, but now that Microsoft has actually made a partnership with Anthropic [tool:Anthropic], and now Claude is pervasive inside of Copilot, it got a massive intelligence update. The way they were doing agents in Copilot Studio was the Power Automate [tool:Power Automate] way — drag and drop shapes. Now that they have that partnership with Anthropic, I am hoping they're going to take on some of the managed agent stuff that Anthropic is pushing. Right now, I would not recommend investing in building agents with Copilot Studio as it stands.</A>
[00:14:16] Marc Juretus: We have something up and running now, and I'll be perfectly frank — it was a lot better than I thought it would be. We actually have it connecting to Service Manager for the knowledge base, as well as SharePoint sites, and you're able to have sub-agents in route. It's actually better than I thought it would be. But where I believe my boss wants to go, you're going to need to go to Foundry, because there's more models. They have the Red Hat agents that'll go in there and scan for vulnerabilities.
[00:15:12] Patrick Chouinard: The one thing I will raise though — in the enterprise, it's not that easy to move to a completely different framework. For us, moving anything to Google would be like a year's worth of vetting of a new hyperscaler, and it would be pure hell. Sometimes you have to live with the infrastructure you have.
[00:15:42] Andrew Nanton: Totally. And I guess I would throw out there that Microsoft has all the pieces, right? It's just putting them together. What I've been struggling with is I would like to have a single project have a tag across Google Drive, Google Calendar, email, just everything. If Microsoft could get that act together and allow a single SQL-like query to reference a single patient or topic or thing, they would be way ahead of the game.
[00:16:44] Marc Juretus: That's very powerful.
[00:16:46] Patrick Chouinard: Yeah, but be careful there — now they just changed their SharePoint connector to an M365 connector [tool:M365 connector]. It is now connected to email, calendar, Teams, SharePoint, everything.
[00:20:17] Patrick Chouinard: If you stay in Foundry, yeah, you have some power there. But Copilot Studio and Power Automate are low-code variants that worked well five years ago. I don't think it's the paradigm that's going to move forward. ▶ If you stay in Foundry and build on top of Foundry, you might have stuff that has some kind of a future, but I don't see Microsoft investing a whole lot in Power Automate, because right now you have models where you can just tell them to build those things. So why do you need low-code when you have no-code solutions?
[00:21:19] Patrick Chouinard: ▶ Watch what Anthropic is doing, because if they bring their managed agent into the Microsoft ecosystem — which they seem to be doing right now — that's going to be your big unlock.
[00:21:36] Marc Juretus: Well, that is what — the model we're using for the LLM is Claude. So the model is Claude, but I know you're saying more. I was surprised that was even offered, to be honest with you. But now it's pretty much everywhere.
[00:22:00] Patrick Chouinard: You have Claude in Copilot, the desktop application, you have Claude in Copilot in Excel, PowerPoint, Word, and now they're launching CoWork [tool:CoWork] — basically the same functionality that's in Claude desktop, but inside of Copilot desktop as well. So yeah, they've basically integrated the entire Claude ecosystem inside of Copilot.

---

<!--SEGMENT
topic: Gemini Enterprise Limitations and Google Workspace
speakers: Patrick Chouinard, Andrew Nanton, Paul Miller, Marc Juretus
keywords: Gemini Enterprise, Gemini Pro, NotebookLM Enterprise, Google Workspace, GWS CLI, feature parity, Markdown output, enterprise restrictions
summary: Patrick shares a cautionary firsthand account of evaluating Google's enterprise AI tier, finding severe feature gaps compared to the consumer Gemini Pro experience. NotebookLM Enterprise is described as "kneecapped," and even basic document creation fails. Andrew counters that the GWS CLI has been a powerful unlock for his workflows, prompting a discussion about the gap between consumer and enterprise AI product maturity.
-->

[00:17:24] Patrick Chouinard: But are you using Google Pro or Google Enterprise? Because if you tried Gemini Enterprise [tool:Gemini Enterprise], you're going to see why I would not go there right now. Google Pro, awesome. The Gemini Pro [tool:Gemini Pro] model, incredible. NotebookLM [tool:NotebookLM] in the wild, incredible. Move to Google Enterprise — pure hell. Absolutely unusable. They have no parity in terms of features, a bunch of limitations. NotebookLM Enterprise is kneecapped completely in terms of functionality.
[00:18:01] Patrick Chouinard: We couldn't even evaluate. We can't create a Word document with Gemini. And I'm not talking about a Microsoft Word document — I'm talking just even a Google Doc document. It gives it to us in Markdown and gives us the script to create the Google Doc. It's insane. The disparity of functionality between Pro and Enterprise right now.
[00:17:13] Andrew Nanton: Well, the GWS CLI [tool:GWS CLI] is super powerful. And yeah, that's been a big unlock for the stuff I'm doing.
[00:22:26] Marc Juretus: I do like what Google offers.
[00:22:30] Paul Miller: Yeah, Microsoft have invested a whole lot of money into Claude as well, a lot more recent money than anyone else. So I think it's a sign of things to come — which is great for us, but then you can just pick and choose between ChatGPT and Claude for running stuff. Maybe use Claude for the agentic stuff.

---

<!--SEGMENT
topic: Local LLM Infrastructure and Proxmox Setup
speakers: Patrick Chouinard, Ty Wells, Andrew Nanton, Marc Juretus
keywords: Proxmox, local LLM, OpenClaw, Docker, Linux VM, NotebookLM, security, self-hosted, gaming PC, ARM
summary: Ty Wells plans to set up a local LLM on a gaming PC and asks Patrick for guidance on Proxmox configuration. Patrick explains he has no formal guide but uses Claude for most configuration work. Andrew references Patrick's existing NotebookLM on OpenClaw setup and its security-minded approach. The group briefly discusses updating that resource to reflect newer systems like ARMs.
-->

[00:08:46] Ty Wells: I'm working on my local LLM [tool:local LLM] that I'm going to push a lot of data to — that same gaming PC I have. I haven't started yet, but Patrick, I'm probably going to reach out to you to set that up.
[00:09:04] Patrick Chouinard: Yeah, I seem to have triggered a bunch of Proxmox [tool:Proxmox] installations or something.
[00:09:11] Ty Wells: <Q>Do you have a guide or best practices? If you have something you can send to me, otherwise I'll just ask Claude.</Q>
[00:09:22] Patrick Chouinard: <A>I don't have anything per se, I've just learned by myself. Honestly, Claude is doing most of my configuration these days.</A>
[00:09:33] Ty Wells: Yeah. No, that's what I was going to do. I just need to actually get to that box, check the memory on it, wipe it, and then start fresh.
[00:10:07] Andrew Nanton: I thought you had one that you prepared about OpenClaw.
[00:10:15] Patrick Chouinard: Right now, what he's talking about is setting up a full infrastructure for Proxmox to have local AI intelligence. Yes, it could be OpenClaw, but it's not just for that. It's local models and, yeah, basically.
[00:10:33] Andrew Nanton: Well, I'll just say, I appreciated your security-minded approaches to some of the boundaries in your NotebookLM.
[00:10:45] Patrick Chouinard: Yeah, absolutely. That's still there. I'm not taking that down. And actually it would be worth revisiting now with ARMs and all of the new systems that came out.

---

<!--SEGMENT
topic: Anthropic Mythos Model and AI Safety Concerns
speakers: Patrick Chouinard, Marc Juretus, Paul Miller, Ty Wells, Bastian
keywords: Mythos, Anthropic, OpenAI, Spud, GPT-2, GPT-3, quantum computing, Bitcoin, cybersecurity, open source, parameter size
summary: The group discusses Anthropic's upcoming Mythos model and OpenAI's competing model (internally nicknamed "Spud"), with humorous commentary on naming conventions. Marc raises concerns about AI-enabled cybersecurity threats and quantum computing's potential to break Bitcoin encryption. Patrick contextualizes the hype, noting that civilization-ending AI predictions have been made since GPT-2 without materializing, while acknowledging the pace of progress has exceeded expectations.
-->

[00:23:41] Ty Wells: Open source — I think that's where you need to grow because that's not going to stop. Setting up your own model — you're going to need that and it's going to actually help you and save money. Because yes, you'll get like a Mythos [tool:Mythos] or something better. The problem is you're going to pay the price. I think now is the time to prepare your environment for that kind of handing off — even what Opus is doing right now, handing it off to your LLM, your open source, your local model. And then you use Mythos or something else for truly complex tasks.
[00:23:43] Marc Juretus: <Q>Is Mythos anywhere near being released to the general public?</Q>
[00:24:20] Paul Miller: <A>What they've said on Mythos at the moment is that they're going to start unlocking just sub-parts of it in the next two to three months. Not the full model, but it sounds like they're giving the full model to certain corporates.</A>
[00:24:54] Patrick Chouinard: We've heard that those models would revolutionize the world and destroy cybersecurity since GPT-2 [tool:GPT-2], so...
[00:25:17] Marc Juretus: Yeah, but would you admit — did you think if you went out to where we are now, we'd be as far as we are? I didn't. Absolutely did not.
[00:25:21] Patrick Chouinard: We're moving way faster than we've expected, but the big scary "this model will destroy civilization" — we've heard that since GPT-2, GPT-3 [tool:GPT-3]. ▶ The human race has a way to absorb those things and dampen their ability very, very quickly.
[00:25:48] Marc Juretus: The thing I'm keeping an eye on now is — will quantum computing get to the point in three to five years that it can hack Bitcoin? There are a bunch of companies starting to try to build stuff to protect that, but that is something I will actually be keeping an eye on.
[00:26:17] Patrick Chouinard: Seeing that OpenAI is ramping up their equivalent — the potato model called Spud [tool:Spud] — I'm not too terrified either.
[00:26:28] Marc Juretus: There is irony in that, though, where the name is Mythos — no Sonnet, no Haiku, no Opus — those don't sound like a villain. Mythos does.
[00:27:48] Bastian: We'll see if that vegetable has its own constitution as well.
[00:27:53] Patrick Chouinard: Well, the other one has a soul, so might as well.

---

<!--SEGMENT
topic: Agentic Coding in Enterprise and SDLC Transformation
speakers: Patrick Chouinard, Paul Miller, Marc Juretus, alexrojas
keywords: Claude Code, CoWork, agentic coding, SDLC, Markdown developers, PRD automation, C-suite adoption, enterprise deployment, context sharing, sneaker net
summary: Patrick shares his experience introducing Claude Code to enterprise users, including a C-suite executive who quickly became a heavy user spending $3,000/month on tokens. The group discusses how agentic coding is fundamentally changing the software development lifecycle, with developers becoming "Markdown developers" who manage direction rather than write code. A humorous anecdote about manually copy-pasting Claude messages between instances to share context illustrates current multi-agent coordination limitations.
-->

[00:28:08] Paul Miller: No, just some news from my side. We had our CTO return back from a big holiday in South America. I told him that when he got back, I needed him to move to agentic coding [tool:agentic coding] straightaway — that we have to defend our moat, we have to leverage all the cool stuff I'd been doing. So he agreed, and we had a big Claude Code Getting Started session, and we're talking about building PRDs [tool:PRD automation] in an automated way, mapping our existing environment.
[00:30:33] Patrick Chouinard: Okay, good. Anything you're working on besides that?
[00:30:45] Paul Miller: I'm working on my second brain, trying to link. I've got lots of individual little Claude Code projects that are running on Markdown together, but I'm trying to link them all together — have a master one that understands there are all these separate ones and merge in what the Karpathy approach offers. Use some of the skills from that, tie into Agent SDK [tool:Agent SDK], and link it all together.
[00:41:36] Patrick Chouinard: On my side, this week I don't have a demo, but there's a reason why. I've been working on a little project — it's going to be for the community. I stumbled onto a pattern that I want to build, and if it works, I think it will — basically I'm going to be more than happy to show all of you guys in the upcoming weeks. It's already starting to pay off. Basically building the intelligence of the community — not the individual human intelligence, I'm talking about the digital intelligence we've been creating. ▶ If I can pull it off, it's obviously going to be an open source GitHub repo for everyone.
[00:43:01] Patrick Chouinard: I've been working a lot to integrate Claude in the enterprise in the last week. I had fun teaching some higher upper management about Claude Code, even to a C-suite level manager. I did not expect that. Now we have somebody in the C-suite of a multi-billion dollar company that requested a local installation of Python and NPM and Node.
[00:43:50] Patrick Chouinard: We've looked at his consumption — he already topped off three grand last month. So yeah, it's going to be fun. It's just a single training that escalated into, "oh, now I need you every week for the next six months." Next week I'm actually showing him how to instantiate CoWork as a full agent with personality, with memories, with contacts, with projects. ▶ When you can have somebody at that level, every other door gets opened really, really easily.
[00:46:16] Patrick Chouinard: Last week, we had a bug in the software we're developing with Claude Code, and we each have our own context. Patrick — the other guy — had issues trying to figure out what the bug was. So he sent me a message that Claude Code told him, through Teams. I copied it, pasted it into my instance of Claude Code in the same project. My Claude Code actually found that I had the context required to solve the issue, and then actually responded saying, "tell that to the other Claude Code." So basically, you have now a middleware between different Claude instances. We were just copy-pasting Claude messages through Teams in order to solve and debug the issue.
[00:47:21] Paul Miller: Like they used to call it sneaker net, where you'd go around the office with USBs and stuff.
[00:47:28] Patrick Chouinard: We're back to doing the same thing. It's humbling when you step on those scenarios for the first time. And it's completely different — doing AI-assisted coding in the enterprise is completely different from the vibe coding I do at home. ▶ We are becoming Markdown developers.
[00:48:11] Paul Miller: Do you think, Patrick — the repurposing of what we do in the software space where we're no longer about writing the code, we're about managing where we should be going from a direction, purpose — where our value add is, how we coordinate our strategy to leverage best practice?
[00:50:23] alexrojas: Patrick, I watched one of him where he says that AI is reducing the arbitrage space. So it's like the added value of AI now is that you can do things, find those inefficiencies in the market, and close the gap like this.
[00:50:50] Patrick Chouinard: Yep, definitely. We're discovering on a daily basis. So if ever I stumble upon the new way to do SDLC in the AI world, I'm going to be more than happy to share.

---

<!--SEGMENT
topic: OpenClaw Multi-Instance and Government RFP Agent
speakers: alexrojas, Patrick Chouinard, Paul Miller
keywords: OpenClaw, Docker, Proxmox, Linux VM, Claude Managed Agents, RFP, government tenders, Mexico, Anthropic, security, self-hosted
summary: Alex asks about running multiple OpenClaw instances for a client and whether Docker is required. Patrick recommends using Discord channels to split context within a single agent rather than running multiple instances, and suggests Proxmox/Linux VMs with Docker for true isolation. Alex then describes an agent he's building to scrape government procurement opportunities in Mexico, and Paul shares a complementary strategy of mining council meeting minutes to get ahead of formal tender announcements. Patrick cautions against using self-hosted open-source agents for legally consequential tasks.
-->

[00:33:26] alexrojas: <Q>Paul, are you using the Claude Agents or OpenClaw?</Q>
[00:33:36] Paul Miller: <A>Claude Agents was the path I was going to go down. I kind of wanted it quite controlled. OpenClaw, I just feel a bit uncomfortable on the security side. So, Claude Agent SDK [tool:Claude Agent SDK].</A>
[00:33:58] alexrojas: Because I have one OpenClaw agent running in my computer, but I wonder — if I want to run more than one instance of OpenClaw, do I need Docker [tool:Docker]?
[00:34:22] Patrick Chouinard: <A>Why do you have two agents? Because if you want to split their processing or their context, go to Discord [tool:Discord], and then you just split by channels, so you have context memory specific to that channel. So it's the same agent engine behind it, but you have completely different contexts that you can address. They share an agent.md file, but they have context memory within the individual conversation, so they act as many agents, basically.</A>
[00:35:12] alexrojas: The thing was that it was for a client — they had a Mac Mini, and they needed individualized agents, not to get across each other. There were agendas and stuff, and that's why I saw this Docker container idea.
[00:35:37] Patrick Chouinard: ▶ If you do that, then I would say yes, go Docker on Linux VMs. You can do the VPS, but I'm not a fan of hosting all of those things on someone else's hardware, especially since it doesn't take that much to host it yourself. If you have an old laptop running somewhere, you can drop Proxmox on there and run your Linux.
[00:36:15] alexrojas: Other than that, I'm exploring a lot of agents. I've been doing a lot of workshops for other companies, and now these last weeks I am landing a bit of all these uses into one specific case. Currently I'm exploring this agent that scrapes government requirements — it's like government procurement notices where they say, "we need X amount of shoes, X amount of these for different projects" — and trying to get as fast as possible who leads to get quotes.
[00:37:01] Paul Miller: Tenders, or RFPs [tool:RFP automation] — a request for proposal, or a tender, is what they tend to call them in Australia, New Zealand, or the UK.
[00:37:24] alexrojas: The only problem is — okay, I would have the tech part, but the reality in Mexico, a lot of these things work a lot through connections, knowing the right people. So I think this could take you like 20–30% of the road.
[00:37:51] Paul Miller: Alex, I had a similar customer requirement for that in New Zealand. One of the sources of data for these types of opportunities — while they might not be publicly offering the contract and you kind of have to talk to the person — if you can get notes of the council meetings, a lot of the council or regional government meetings are minuted. ▶ If you can get notes that there was a discussion around doing something, and then process those notes — "hey, they were talking about a new water treatment plant" — and then you're constantly looking out for those opportunities. A lot of the insights around those tender projects are hidden within meeting notes.
[00:39:15] Patrick Chouinard: ▶ But for those — when you start to touch RFPs and things that have legal consequences — I would be very careful with OpenClaw and Hermes of the world. Anthropic has posted something called Claude Managed Agents [tool:Claude Managed Agents]. So basically their answer to OpenClaw for corporate entities — I would probably look far more through that type of system than a self-hosted OpenClaw installation. For stuff that has legalese attached to it, I'd be very careful in the corporate environment.

---

<!--SEGMENT
topic: Karpathy LLM Wiki, RAG Preprocessing, and LanceDB
speakers: Patrick Chouinard, David's iPhone, Morgan Cook, alexrojas
keywords: Andrej Karpathy, LLM Wiki, Obsidian Vault, RAG database, LanceDB, chunking, metadata enrichment, vector database, Ghost Postgres, Memory Palace, idea management
summary: Patrick recommends Andrej Karpathy's LLM Wiki gist as a tool for organizing overwhelming idea backlogs by ingesting AI conversations into an Obsidian Vault and generating a navigable wiki. He then describes experimenting with a modified version of Karpathy's prompt as a RAG preprocessor for metadata enrichment before chunking. Morgan Cook introduces "Ghost," a CLI-only Postgres database designed for agent use. The group also briefly compares Ghost to the Memory Palace concept.
-->

[00:57:19] Patrick Chouinard: Let me try to get you the link — or if someone can find the link to Andrej Karpathy's gist about LLM Wiki [tool:LLM Wiki]. If you are overwhelmed with ideas, this thing will help you. Basically, just talk with whichever AI you prefer — be it Gemini, ChatGPT, Claude, whatever — take all of the conversation, drop them into an Obsidian Vault [tool:Obsidian Vault]. This will dissect all of the material you give it and restructure it in the form of a navigable wiki. ▶ So then you can just ask Claude Code: find me an idea that is doable, that I can actually create, that has market value. This is going to be the game changer for selecting among a sea of ideas. [link:Andrej Karpathy LLM Wiki gist on GitHub]
[00:59:24] Patrick Chouinard: That's the other thing I've been playing with — that very gist. He's doing it without using vectors or a vector database, but I'm trying to play with the idea of using it as a preprocessor before chunking, before I put it in a RAG database. ▶ Basically, I'm thinking about using a modified version of Karpathy's prompt in order to do my preprocessing and metadata enrichment of whatever I want to put in my RAG database, and so far it's yielding pretty nice results.
[00:59:46] Patrick Chouinard: I'm anxious to see where I can push that thing, especially since I've never built a RAG database in my life, so let's learn from the best.
[01:04:09] Morgan Cook: One thing I saw — it's called Ghost [tool:Ghost Postgres]. It's a free Postgres database for your agents. It's completely CLI-based. And you were just talking about building your RAG database — this is a Postgres database which has no GUI. It's completely CLI, built for the agent so that your agent can fire up the database, create the schema, load it, do stuff with it, and destroy it however many times it needs to.
[01:05:17] Patrick Chouinard: The website is pretty straightforward, but perfect to be used by an engine.
[01:05:43] Patrick Chouinard: For my RAG database, I'm looking at something that's more portable — something that could be vectorized and packaged within a single application and travel with the application. Right — not something you need to install a back-end server for.
[01:06:13] Patrick Chouinard: ▶ I started playing with LanceDB [tool:LanceDB] right now, and so far it's serving me well. It doesn't need to be installed or deployed — it's just packaged in.
[01:07:48] Morgan Cook: Memory Palace [tool:Memory Palace] is more of a visual organizational thing — putting things in specific rooms of the palace, relational-wise, so that was more of a mental concept they applied to the database directly. A way of automatically remembering where things are.
[01:08:25] Patrick Chouinard: It's an interesting idea, but honestly it overlaps a lot with what Andrej Karpathy does. ▶