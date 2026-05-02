=== SESSION ===
date: 2025-04-15
duration_estimate: 1h 21m
main_themes: Enterprise AI agent deployment, local LLM infrastructure, agentic coding workflows, AI-assisted business automation, knowledge management systems, AI model comparison and selection

<!--SEGMENT
topic: Opening and Previous Week Recap
speakers: Patrick Chouinard, Marc Juretus, Ty Wells
keywords: Obsidian, Cloud Code, Codex, text-to-SQL, SEO, recap flow, school community, golf, Quebec weather
summary: Patrick and Marc exchange greetings and discuss weather conditions in Quebec versus Marc's location. Patrick references the community's automated recap system for previous meeting content. They review last week's demonstrations including a text-to-SQL Slack integration, SEO-optimized agency site rebuilds, Claude plus Codex development workflows, and Andrej Karpathy's lightweight RAG implementation using Claude Code within Obsidian for Markdown-based knowledge management.
-->

[00:00:30] Patrick Chouinard: Hey Marc!
[00:00:30] Marc Juretus: Good to see you there, Patrick.
[00:00:34] Patrick Chouinard: How's it going?
[00:00:36] Marc Juretus: It's going okay, you?
[00:00:39] Patrick Chouinard: Good, good. The sky is falling around here. It's raining like mad, but April in Quebec.
[00:00:50] Marc Juretus: Oh, that's where you're in. That's where you're in Quebec. It's about 80. Kind of humid, but it's at least warm.
[00:00:58] Patrick Chouinard: Yeah, I thought it was not too bad. It was like 60, 65, getting warmer.
[00:01:23] Marc Juretus: Anything I had to miss last week, talk about anything, I was going to say something interesting, everything we talked about is interesting, anything particular, let's put it that way.
[00:01:32] Patrick Chouinard: To be really honest, I now rely so much on recap flow that I don't remember it by heart. If you look at the school community, there's now a full detail recap with everything.
[00:01:47] Marc Juretus: Cool.
[00:02:00] Patrick Chouinard: Let me take a look. Oh yeah, we had a couple of demo that were interesting last week. Someone showed us a text-to-SQL platform that integrated with Slack that was kind of interesting. How to rebuild the SEO-optimized agency site. Claude plus Codex [tool:Codex], so developing with both systems together.
[00:02:26] Marc Juretus: We tried that, yeah, let's check that out.
[00:02:29] Patrick Chouinard: Yeah, so there was a, oh, obviously the lightweight rag from Andrej Karpathy in using Cloud Code [tool:Claude Code] in Obsidian [tool:Obsidian].
[00:02:41] Marc Juretus: <Q>What's Obsidian?</Q>
[00:02:43] Patrick Chouinard: <A>Note-taking application. It's a free note-taker that just takes note in Markdown [tool:Markdown], so it allows Cloud Code [tool:Claude Code], Codex [tool:Codex], all of those to basically write all the notes themselves directly.</A> Andrej Karpathy created a very, very, very optimized prompt where you could digest or ingest pretty much any type of content and store it and document it inside of an Obsidian [tool:Obsidian] Vault. So pretty interesting.
[00:04:49] Ty Wells: Hey, guys. I'm presenting the golf course today, so that is my presentation. So my presentation is done. I'll be listening in. That's about it.
[00:05:04] Patrick Chouinard: Okay.
[00:05:05] Marc Juretus: This guy, hackathons and golf courses.
[00:05:08] Ty Wells: Man, you lived a lifetime.
[00:05:09] Marc Juretus: Is that what it is?
[00:05:11] Ty Wells: Oh, wait a minute. We're taking shots.
[00:05:13] Marc Juretus: Hang on a second, guys. I can share that moment, too.
[00:05:17] Ty Wells: This is our tradition, though. We have certain holes we have to take shots on. The guys are getting it together. Still haven't washed it. All right, you guys. And remember, I got to fill mine up just in case we need it. Cheers, guys.
[00:05:40] Ty Wells: That was my presentation. I'm going to go off video now.

<!--SEGMENT
topic: AI Model Preferences and Voice Interfaces
speakers: Marc Juretus, Patrick Chouinard
keywords: Gemini, Claude, ChatGPT, voice interface, system prompts, conversational AI, Google certification, gems
summary: Marc and Patrick debate the relative strengths of leading LLM platforms. Marc advocates for Gemini's superior conversational continuity and daily workflow integration, particularly for stock analysis using custom gems, while acknowledging Claude's coding superiority. Patrick counters that ChatGPT dominates for voice-based interaction. They discuss how system prompt customization significantly impacts output quality across platforms.
-->

[00:03:17] Marc Juretus: I'll say this, as far as conversational flow that you're going to maintain a conversation over days, I've used ChatGPT [tool:ChatGPT] to a point, and I think Claude [tool:Claude] excels way above everybody when it comes to code, but Gemini [tool:Gemini], because since I had that Google cert, I was starting to use it a little more because I knew a little bit more about it, and just conversation from day to day and leaving off where you left off and just some of the stuff it does. Plus, it's pretty seamless to YouTube [tool:YouTube] because it's a part of their product, but I've been using their gems where, you know, I see it's basically a prompt, I'll pass it a stock symbol, and it'll give me detailed analysis. I'm sure you could do it in Claude [tool:Claude]. I don't know. I kind of like the conversation day-to-day with that.
[00:04:06] Patrick Chouinard: The way I converse is always vocally, and for that right now, nothing comes close to ChatGPT [tool:ChatGPT], sadly.
[00:04:13] Marc Juretus: I don't know if I agree with that, but we can beg to differ. I use it all the time, dude. I talk all day to it. I mean, my open-claw agent is actually pretty good, too, but I don't know, man. For my 20 hours a month, I never run out, and it's just slick. I'm a fan. Let's just put it that way.
[00:04:35] Patrick Chouinard: Mind you, there might be the thing that I've tweaked their system prompt to hell, and that makes all the difference in the world.

<!--SEGMENT
topic: Enterprise AI Agent Architecture
speakers: Marc Juretus, Patrick Chouinard, Andrew Nanton, Paul Miller
keywords: Copilot Studio, Azure Foundry, Microsoft, Anthropic, Claude, Service Manager, SharePoint, authentication, Power Automate, enterprise deployment
summary: Marc seeks advice on deploying employee assistant agents within his hospital's Microsoft ecosystem, specifically integrating with Service Manager and SharePoint. Patrick cautions against investing in Copilot Studio's current drag-and-drop paradigm, suggesting the recent Microsoft-Anthropic partnership will fundamentally improve agent capabilities. Andrew highlights the potential of unified Microsoft data access, while Patrick details severe functionality gaps between Google Pro and Enterprise tiers, warning against premature enterprise commitments.
-->

[00:06:01] Paul Miller: Hey, Patrick. Hey, Andrew.
[00:06:05] Marc Juretus: What's up, Paul?
[00:06:06] Andrew Nanton: Hello, hello.
[00:06:08] Paul Miller: I'm over in our Western Isle of New Zealand, the landmass that they call Australia.
[00:06:17] Marc Juretus: Man, I feel like I stepped into the late 90s and we're gaming with those big headphones on you two guys tonight. Where's the big mic that looks like an ash?
[00:06:27] Andrew Nanton: Right? No. Yeah, yeah.
[00:06:32] Paul Miller: And now it's a podcast.
[00:06:36] Paul Miller: This meeting is being recorded.
[00:06:42] Patrick Chouinard: Good.
[00:07:58] Patrick Chouinard: Oh, that's a good one, Andrew. And I do see the need for Codex [tool:Codex] price per token, they are massively in front of Anthropic [tool:Anthropic] right now. And not every task requires Claude-level intelligence. There's a lot of cleanup work that is perfectly able to run in Codex [tool:Codex] at way cheaper prices. Honestly, I think that's where we're going. We're going to have a layered tier of model working together to get something done without costing an arm and leg.
[00:11:41] Patrick Chouinard: Marc, did you have anything you wanted to share or any question you wanted to ask?
[00:11:47] Marc Juretus: Yeah, what I probably would want to ask is, seems like my place of business hospital, they are starting to try to get some chat agents that are going to connect to like a Service Manager [tool:Service Manager], SharePoint [tool:SharePoint], you know, maybe submitting tickets and stuff like that. <Q>Has anybody did a deployment at work where they had an agent of that nature that's like an employee assistant agent, where they actually either leverage Copilot [tool:Copilot], like a Copilot [tool:Copilot], Copilot Studio [tool:Copilot Studio], or even deployed something from Foundry [tool:Azure Foundry] because we're an Azure shop and we're looking in that direction?</Q> The one problem is we have like a proprietary CMS [tool:CMS] and maintaining your login credentials into the actual chat bot is becoming the rub, but outside of that, is anybody you use that at work and have any thoughts on that?
[00:12:48] Patrick Chouinard: <A>We haven't implemented anything yet, but we are in the same case where we're a Microsoft shop as well. And I agree. It was like that until a couple of weeks ago, but now that Microsoft has actually made a partnership with Anthropic [tool:Anthropic], and now Claude [tool:Claude] is pervasive inside of Copilot [tool:Copilot], it got a massive intelligence update.</A> I'm anxious to see what happens in the agent world, because that's going to change a whole lot of things here, because the way they were doing agents in Copilot Studio [tool:Copilot Studio], was the Power Automate [tool:Power Automate] way. It's the drag and drop shape, and try to build things. Now that they have that partnership with Anthropic [tool:Anthropic], I am hoping that they're going to take on some of the managed agent stuff that Anthropic is pushing. Because they decided to implement Claude [tool:Claude] pretty much as is, so I'm guessing there's a chance that they're going to take more than just the model from Anthropic [tool:Anthropic]. We're going to have to see, but right now, ▶I would not recommend investing any kind of build agent with Copilot Studio [tool:Copilot Studio] as it stands. Will it change in the near future? I think it will, but be careful right now, because every time we try to build agents in there, it's not really the best of experience.</A>
[00:14:16] Marc Juretus: We have something up running now, and I'll be perfectly frank, it was a lot better than I thought it would be, because when they first said that, I was like, look, we're going to do something in Microsoft Foundry [tool:Azure Foundry]. That's my recommendation, but at this point, we actually have it connecting to Service Manager [tool:Service Manager] for the knowledge base, as well as SharePoint [tool:SharePoint] sites, and you're able to have sub-agents in route. So it's actually better than I thought it would be. But where I believe my boss wants to go, you're going to need to go to Foundry [tool:Azure Foundry], because there's more models. They have that Red Hat agents that'll go in there and scan for vulnerabilities. There's just so much to offer up there.
[00:15:21] Patrick Chouinard: The one thing I will raise though, in the enterprise, Andrew, I recognize that if you can move everything, it's easy. In the enterprise, it's not that easy to move to a completely different framework. So for us, for example, moving anything to Google [tool:Google] would be like a year worth of vetting of a new hyperscaler, and it would be pure hell. Sometimes you have to live with the infrastructure you have.
[00:15:42] Andrew Nanton: Totally. And I guess I would throw out there that Microsoft [tool:Microsoft] has all the pieces. It's just putting them together. So what I've been struggling with is I would like to have a single project have a tag across Google Drive [tool:Google Drive], Google Calendar [tool:Google Calendar], email, just everything. And even in Google [tool:Google], where it's a little more uniform than Microsoft [tool:Microsoft], it is still heterogeneous. If Microsoft [tool:Microsoft] could get that act together and allow a single SQL-like query to reference a single patient or topic, they would be way ahead of the game. I mean, these, and that's where I think Anthropic [tool:Anthropic] is behind the eight ball, is that they don't have email, documents, calendar.
[00:16:46] Patrick Chouinard: Yeah, but be careful there, because now they just changed their SharePoint [tool:SharePoint] connector to an M365 [tool:Microsoft 365] connector. It is now connected to email, calendar, Teams [tool:Microsoft Teams], SharePoint [tool:SharePoint], everything.
[00:17:24] Patrick Chouinard: <Q>Are you using Google Pro or Google Enterprise?</Q> Because if you tried Gemini Enterprise [tool:Gemini Enterprise], you're going to see why I would not go there right now. Google Pro [tool:Gemini Pro], awesome. Like the Gemini Pro [tool:Gemini Pro] model, incredible. Notebook LM [tool:Notebook LM] in the wild, incredible. Move to Google Enterprise [tool:Gemini Enterprise], pure hell. Absolutely unusable. They do not have parity in terms of feature, a bunch of limitation. Notebook LM [tool:Notebook LM] Enterprise is kneecapped completely. We can't create a Word document with Gemini [tool:Gemini]. It gives it to us in Markdown and gives us the script to create the Google Doc. The disparity of functionality between Pro and Enterprise right now is insane.

<!--SEGMENT
topic: Local LLM Infrastructure and Multi-Agent Isolation
speakers: Ty Wells, Patrick Chouinard, alexrojas
keywords: Local LLM, Proxmox, Docker, OpenClaw, gaming PC, Discord, context isolation, VPN, security
summary: Ty discusses plans to deploy local LLMs on a gaming PC using Proxmox, seeking guidance from Patrick who has triggered multiple installations recently. Alex inquires about running multiple OpenClaw instances for client work, exploring Docker and VPS options. Patrick recommends against hosting on third-party hardware for sensitive applications, suggesting Discord channels for context separation within single agent instances, and Docker only when true hardware isolation is required for separate client environments.
-->

[00:08:46] Ty Wells: I'm working on my local LLM that I'm going to push a lot of data to that same gaming PC I have. I haven't started yet, but Patrick, I'm probably going to reach out to you now that I'm back to set that up.
[00:09:03] Patrick Chouinard: No problem. Yeah, I seem to have triggered a bunch of Proxmox [tool:Proxmox] installations or something.
[00:09:11] Ty Wells: Do you have a guide or best practices? If you have something you can send to me, otherwise I'll just use Claude [tool:Claude].
[00:09:22] Patrick Chouinard: I don't have anything per se, I've just learned by myself. Honestly, Claude [tool:Claude] is doing most of my configuration these days.
[00:09:44] Patrick Chouinard: Right now, what he's talking about is setting up a full infrastructure for Proxmox [tool:Proxmox] to have local AI intelligence. It could be OpenClaw [tool:OpenClaw], but it's not just for that. It's local models and basically.
[00:10:33] Andrew Nanton: Well, I'll just say, I appreciated your security-minded approaches to some of the boundaries that in your notebook.lm.
[00:10:43] Patrick Chouinard: Yeah, absolutely. That's still there. That, I'm not taking that down, but yeah, that was, and actually it would be worth revisiting now with ARMYs and all of the new system that came out.
[00:33:29] alexrojas: Paul, are you using the Cloud Agents or OpenClaw [tool:OpenClaw]?
[00:33:36] Paul Miller: Cloud Agents [tool:Cloud Agents] was the path I was going to go down. I kind of wanted it quite controlled. OpenClaw [tool:OpenClaw], I just feel a bit uncomfortable on the security side.
[00:33:57] alexrojas: Okay. Because I have one OpenClaw [tool:OpenClaw] agent running in my computer, but <Q>I wonder if I want to run more than one instance of OpenClaw [tool:OpenClaw], I do need Docker [tool:Docker], right?</Q> I don't know if you guys know, because I have a VPN, that's where I do other agents, but I have not had two agents running in my machine, exactly for that reason.
[00:34:22] Patrick Chouinard: <A>Why do you have two agents?</A>
[00:34:24] alexrojas: Yeah, I was just thinking out, you know? It was for a client, so they needed individualized agents, not to get across each other. There was agendas and stuff, and that's why I just saw this Docker [tool:Docker] container idea.
[00:35:37] Patrick Chouinard: <A>If you do that, then I would say, yes, go Docker [tool:Docker] on Linux VMs. You can do the VPS, but I'm not a fan of hosting all of those things on someone else's hardware, especially that it doesn't take that much to host it yourself. If you have an old laptop running somewhere, you can drop Proxmox [tool:Proxmox] on there and run your Linux.</A> But if you want to split their processing or their context, instead of using Telegram [tool:Telegram], which it's doable but complex, ▶go to Discord [tool:Discord], and then you just split by channels, so you have a context memory specific to that channel. It's the same agent engine behind it, but you have completely different contexts that you can address.

<!--SEGMENT
topic: Next-Generation AI Models and Existential Risk
speakers: Marc Juretus, Paul Miller, Patrick Chouinard, Bastian
keywords: Mythos, Spud, OpenAI, Anthropic, quantum computing, Bitcoin, cybersecurity, model release timeline, AGI safety
summary: The group discusses upcoming frontier models including Anthropic's Mythos and OpenAI's Spud (potato), debating release timelines and corporate access. Marc expresses concern about quantum computing threats to Bitcoin encryption within 3-5 years, while Patrick remains skeptical of apocalyptic AI predictions, noting similar warnings since GPT-2. They analyze the irony of model naming conventions contrasting Mythos's ominous tone with Spud's mundane vegetable reference.
-->

[00:22:58] Ty Wells: Open source. I think that's where you need to grow because that's not going to stop setting up your own model. You're going to need that and it's going to actually help you and save money because, yes, you'll get like Mythos [tool:Mythos] or something better. The problem with that is you're going to pay the price, and I think now is the time to prepare your environment for handing off even what Opus is doing right now, handing it off to your LLM, your open source, your local model.
[00:23:43] Marc Juretus: <Q>Is Mythos [tool:Mythos] anywhere near being released to the general public?</Q> I haven't looked and I saw all the stuff that was finding and like, we got to get, are we going to get in that zone where we're going to wish we uninvented something for the havoc that was created? I follow a bunch of financial influencers investing in data centers. They always say, I hope we don't blow ourselves up with all this technology. Like, you got a guy in his bedroom that has nothing about code, but he writes this impressive virus that takes things out. Very powerful.
[00:24:20] Paul Miller: <A>What they've said on Mythos [tool:Mythos] at the moment is that they're going to start unlocking just sub-parts of it in the next two to three months. Not the full model, but it sounds like they're giving the full model to certain corporates.</A>
[00:24:54] Patrick Chouinard: But yeah, honestly, I take some, I give some in there. Because we've heard that those models would revolutionize the world and destroy cyber security since GPT-2 [tool:GPT-2], so... We're moving way faster than we've expected, but the big, scary, this model will destroy civilization, we've heard that since GPT-2, GPT-3. It is a massive improvement, but the human race has a way to absorb those things and dampen their ability very quickly.
[00:25:48] Marc Juretus: The thing I'm keeping an eye on now is quantum computing [tool:Quantum Computing] get to the point in three to five years that it can hack Bitcoin [tool:Bitcoin]? Now, there's a bunch of companies that are starting to try to build stuff to protect that, but that is something I will actually be keeping an eye on.
[00:26:17] Marc Juretus: There is irony in that, though, where the name is Mythos [tool:Mythos], where it's the one, no sonnet, no haiku, no opus, don't sound like no villain. Mythos [tool:Mythos] does.
[00:26:39] Patrick Chouinard: This one is a myth. Its opponent is a potato [tool:Spud]. I don't know who chooses names at OpenAI [tool:OpenAI], but Spud [tool:Spud] was not their best pick.
[00:27:22] Bastian: We'll see if that vegetable has its own constitution as well.
[00:27:53] Patrick Chouinard: Well, the other one has a soul, so might as well.

<!--SEGMENT
topic: Agentic Coding Implementation and User Feedback Systems
speakers: Paul Miller, Ty Wells, Patrick Chouinard
keywords: Claude Code, Agent SDK, voice recording, user-driven development, Telegram, PRD automation, CTO onboarding
summary: Paul describes onboarding his CTO to agentic coding using Claude Code and automated PRD generation after a Peruvian holiday. Ty demonstrates his enhanced user-driven development framework featuring voice-recorded feedback widgets that capture console logs and generate implementation plans, enabling full development loops from mobile devices via Telegram integration. Patrick discusses using Claude Code to build training materials recursively.
-->

[00:28:08] Paul Miller: Bastian, you'll be interested to know this. We had our CTO return back from a big holiday in South America. I told him that when he got back, I needed him to move to agentic coding straightaway, that we have to defend our moat. So he agreed, and we had a big Claude Code [tool:Claude Code] Getting Started session, and we're talking about building PRDs [tool:PRD] in an automated way, mapping our existing environment. He's right into it. Apparently, there's some kind of drink you drink in Peru that kind of gets you high in the mountains. He tried it and said it was very bitter, but now he seems very compliant around agentic coding.
[00:30:03] Patrick Chouinard: Honestly, if agentic coding was hiding in some kind of a drink, Quebec would be the central of agentic coding for the world.
[00:31:21] Ty Wells: I think I shared with you guys my user-driven development framework today. So I enhanced that. The way that workflow works is you have a feedback widget on my application. Right now, it just has record. They narrate the issue they're having. It then gives them a list of choices, like an ask user format. It gives them buttons they can click. It keeps going until they're up 85%, like a mini chat window. Once that's done, it sends it off to my feedback hub. I look at it, get an email. I can decide to initiate that. It builds out the plan. I look at the plan. If it looks good, I can initiate that right from my phone, Telegram [tool:Telegram], accept that, sends that off, creates the PR [tool:Pull Request]. Then I review the PR right from my phone again and merge that in. So it's a full loop now, but the recording was the key. It has a button there to capture the console logs.
[00:45:35] Patrick Chouinard: Today I had Claude Code [tool:Claude Code] use Claude [tool:Claude] to create a Claude Code [tool:Claude Code] training material based on a project that we did in order to monitor the usage of Claude Code [tool:Claude Code]. So I have to have my little top on my desk.

<!--SEGMENT
topic: Government Contract Intelligence and Legal Risk Management
speakers: alexrojas, Paul Miller, Patrick Chouinard
keywords: RFP, tender scraping, government contracts, Claude Managed Agents, OpenClaw, legal implications, council minutes, Mexico
summary: Alex explores automating government RFP (tender) discovery in Mexico using AI agents. Paul suggests analyzing council meeting minutes to identify opportunities before public posting. Patrick strongly cautions against using self-hosted OpenClaw for legally sensitive government work, recommending Anthropic's Claude Managed Agents for enterprise compliance. They discuss the limitations of technology in relationship-based procurement environments versus early intelligence gathering.
-->

[00:36:15] alexrojas: I'm exploring this agent that scrapes government requirements that they publish, and they say like, hey, we need these X amount of shoes, X amount of these for different projects, and trying to get as fast as possible who leads to get quotes.
[00:37:01] Paul Miller: Tenders, or RFPs [tool:RFP], is what they call them. A request for proposal, or a tender.
[00:37:24] alexrojas: Yeah, the only problem is in Mexico, a lot of these things work a lot through connections, getting to know the right people. I think this could take you 20%, 30% the road, and then exploring a personal side.
[00:37:51] Paul Miller: Alex, I had a similar customer requirement in New Zealand. One of the sources of data is council meeting minutes. If you can get notes that there was a discussion around doing something, and process those notes and say, hey, they were talking about a new water treatment plant, or they were talking about a new highway eroding project, and then you're constantly looking out for those opportunities. That's kind of the line that I was taking, because a lot of the insights are hidden within meeting notes.
[00:39:15] Patrick Chouinard: But for those, when you start to touch RFPs [tool:RFP] and things that have legal consequences, I should say, ▶I would be very careful with the OpenClaw [tool:OpenClaw] and Hermes of the world. Anthropic [tool:Anthropic] has posted something called Claude Managed Agents [tool:Claude Managed Agents]. Basically, their answer to OpenClaw [tool:OpenClaw] for corporate entities, I would probably look far more through that type of system than self-hosted OpenClaw [tool:OpenClaw] installation for stuff that has legalese attached to it. They're fun to explore, to try things. I have many running myself, but ▶I would not recommend installing them at a client site in production, dealing with something that has legal implication today.</A>

<!--SEGMENT
topic: Enterprise Adoption Realities and Recursive AI Debugging
speakers: Patrick Chouinard, Paul Miller, alexrojas
keywords: C-suite, enterprise training, token costs, recursive debugging, Claude Code, context transfer, SDLC, markdown developers
summary: Patrick shares a case study of C-suite adoption of Claude Code resulting in $3,000 monthly token consumption and ongoing training commitments. He describes a novel debugging method where two developers transferred context between separate Claude Code instances via copy-paste to resolve bugs, effectively using human intermediaries as "sneaker net" for AI context. The discussion highlights how enterprise AI adoption requires reinventing traditional SDLC processes and creates new categories of technical debt.
-->

[00:42:51] Patrick Chouinard: I've been working a lot to integrate Claude [tool:Claude] in the enterprise in the last week. I had fun teaching some higher upper management about Claude Code [tool:Claude Code], even to a C-suite level manager. I did not expect that. Now we have somebody in the C-suite of a multi-billion dollar company that requested a local installation of Python [tool:Python] and NPMs [tool:NPM] and Node [tool:Node.js]. We've looked at his consumption, he already topped off three grand last month. Next week I'm actually showing him how to instantiate Claude [tool:Claude] as a full agent with personality, with memories, with contacts, with projects. When you can have somebody at that level, every other door gets opened really easily.
[00:46:16] Patrick Chouinard: Last week, we had a bug in the software we're developing with Claude Code [tool:Claude Code], and we each have our own context. Patrick the guy had issues trying to figure out what the bug was. So he sent me a message that Claude Code [tool:Claude Code] told him. I copied it, pasted it into my instance of Claude Code [tool:Claude Code] in the same project. My Claude Code [tool:Claude Code] actually found that I had the context required to solve the issue, and then he actually responded, saying, like, tell that to the other Claude Code [tool:Claude Code]. So basically, you have now a middleware between different Claude [tool:Claude] instances. We were just copy and pasting Claude [tool:Claude] message through Teams [tool:Microsoft Teams] in order to solve and debug the issue. We're back to doing sneaker net.
[00:47:38] Patrick Chouinard: Doing AI-assisted coding in the enterprise is completely different from the vibe coding I do at home. We're looking at almost reinventing the SDLC [tool:SDLC] because the steps are completely different. We are becoming markdown developers.

<!--SEGMENT
topic: Strategic Transformation of Software Development Value
speakers: Paul Miller, Patrick Chouinard, alexrojas
keywords: Death of SaaS, arbitrage, value add, consulting, Nate Jones, strategic direction, trust, AI replacement
summary: Paul queries whether software professionals are transitioning from code writers to strategic directors managing AI output, referencing Nate Jones's commentary on SaaS business mortality. Alex notes AI reduces arbitrage opportunities by closing market inefficiencies rapidly. Patrick agrees that finding valuable use cases is now the primary challenge, recommending focus on eliminating time-wasting pain points rather than technically interesting problems.
-->

[00:48:08] Paul Miller: Do you think, Patrick, that we're no longer about writing the code, we're about managing where we should be going from a direction, purpose, where our value add is, how we coordinate our strategy? There's been quite a lot of interesting discussion. I'll post it on the Nate Jones channel. He's giving commentary as to the death of SaaS [tool:SaaS] businesses and how you reinvent yourself in terms of people get trust with having other people they can go to or strangle if everything goes wrong. If all the code's being done by AI, you still need to be able to rely on some people to save you when you go down the wrong path.
[00:50:23] alexrojas: Patrick, I watched one of him where he says that the AI is reducing the arbitrage space. So it's like the added value of AI now is that you can do things, find those inefficiencies in the market, and close the gap like this.
[00:50:54] Patrick Chouinard: Definitely. But honestly, finding the right use case or the right business is probably the hardest part of the work. Once you have the context of whatever use case you need to resolve, you can pretty much resolve anything. ▶Often I will go and poke at them and say, no, tell me where you lose the most amount of time every week. Like, tell me what is painful, what tasks that you have to do that you cannot avoid, but you would love to avoid because you consider it a waste of your time. Removing the worst pain point of their week, after that, everything's going to flow.

<!--SEGMENT
topic: Event Management Automation Platform
speakers: David’s iPhone, Patrick Chouinard
keywords: Event planning, RFQ automation, vendor selection, FileMaker Pro, no-code, AI transition, Gusto, SMS
summary: David presents his event management platform designed for event rental companies and planners, featuring AI-driven vendor matching, automated RFQ generation and negotiation, and staff management via SMS integration with Gusto payroll. He describes transitioning from FileMaker Pro background to modern AI-enabled development, expressing liberation at being able to build enterprise-worthy applications without traditional JavaScript or Python expertise.
-->

[00:51:31] David’s iPhone: Basically, what it is, it serves event planners and event rental companies. I'm building this web-based system focused on streamlining event planning. From a user perspective, you can use AI and chat with AI, but one of the first steps is going to show you this beautiful cloud of different types of vendors in your area based on your event details, and then you click each vendor card to select those vendors, and then you basically just click go, and it just starts sending out RFQs [tool:RFQ], negotiating with it. It manages your guests over SMS [tool:SMS] and your staff. They don't need to log in anywhere, it's all done over SMS [tool:SMS], they can swap shifts, say they're late. It all goes to payroll, syncs with Gusto [tool:Gusto].
[00:55:42] David’s iPhone: I'm actually a pretty low-level coder. I've done a lot of deep work with FileMaker Pro [tool:FileMaker Pro] and integrating it with SQL [tool:SQL] databases. I never was able to learn JavaScript [tool:JavaScript] or Python [tool:Python]. And now with AI, I'm finally able to start to craft things that I feel are more enterprise-worthy. I went from one repo in the last 10 years in GitHub [tool:GitHub], I'm up to 77.

<!--SEGMENT
topic: Knowledge Management and Vector Database Strategies
speakers: Patrick Chouinard, David’s iPhone, Morgan Cook, alexrojas
keywords: Andrej Karpathy, LLM Wiki, Obsidian, Ghost, Postgres, Memory Palace, LanceDB, RAG, vector database, chunking
summary: Patrick recommends Andrej Karpathy's LLM Wiki approach for managing idea overflow using Obsidian vaults and optimized prompts. Morgan introduces Ghost, a CLI-based Postgres database designed specifically for agent use. The group discusses various knowledge persistence strategies including Memory Palace's visual organization versus Karpathy's method, and LanceDB for portable vector storage. Patrick describes using Karpathy's prompt architecture as a preprocessor for RAG pipelines.
-->

[00:57:47] Patrick Chouinard: If you are overwhelmed with ideas, Andrej Karpathy's LLM Wiki [tool:LLM Wiki] will help you. Just talk with whichever AI you prefer, take all of the conversation, drop them into an Obsidian [tool:Obsidian] vault. This will dissect all of the material you give it and restructure it in the form of a navigable wiki. Then you can just ask, based on everything you have, find me an idea that is doable, that I can actually create, that has market value.
[01:04:09] Morgan Cook: There's a tool called Ghost [tool:Ghost]. It's a free Postgres [tool:Postgres] database for your agents. It's completely CLI [tool:CLI] based. You know, like you were talking about building your RAG [tool:RAG] database, but this is a Postgres [tool:Postgres] database which has no GUI. It's completely CLI [tool:CLI] built for the agent so that your agent can fire up the database, create the schema, load it and do stuff with it and destroy it however many times it needs to.
[01:05:43] Patrick Chouinard: For my RAG [tool:RAG] database, I'm looking at something that's more portable that could be vectorized and package within a single application and travel with the application. I started playing with LanceDB [tool:LanceDB] right now, and so far it's serving me well. It doesn't need to be installed or deployed, it's just packaged in.
[01:07:18] Morgan Cook: Memory Palace [tool:Memory Palace] is more of a visual organizational thing of putting things in specific rooms of the palace, relational-wise, so that was more of a mental concept that they applied to the database directly.
[01:08:36] Patrick Chouinard: It's an interesting idea, but honestly, it overlaps a lot with what Andrej Karpathy [tool:Andrej Karpathy] does.

<!--SEGMENT
topic: Hardware Integration for Business Systems
speakers: Ty Wells, Patrick Chouinard
keywords: ERP, signature pad, KDS, Fire tablet, customer-facing display, inventory counter, peripheral hardware
summary: Ty demonstrates using Amazon Fire tablets as flexible peripheral interfaces for his ERP system, eliminating dedicated hardware dependencies. The system passes sessions to tablets functioning as signature pads, kitchen display systems (KDS), check-in terminals, and inventory counters. This approach avoids vendor lock-in while providing richer customer-facing displays showing full invoices and enabling SMS/email receipt delivery for locksmithing operations.
-->

[01:09:01] Ty Wells: One thing I would share with you guys, this ERP [tool:ERP] system that I know I've demoed before. One of the problems I ran into was we needed a signature pad, and I didn't want to do that hardware connected to a physical PC. I built this system using tablets to pass off the session during checkout process. You can do the same thing for a kitchen display [tool:KDS], so you can use it as a signature pad. I'm using like a Fire tablet [tool:Fire tablet], 10-inch tablet, that takes over the session. This is a front display, as an inventory counter. I don't need any additional hardware, I'm not tied in to anybody. We do locksmithing, so I use it also as a check-in terminal. When they go into the store, they put in their phone number, and if they're on the account, it'll pull it up. We do only SMS [tool:SMS] or email receipts now.

<!--SEGMENT
topic: AI Education Initiatives and Business Consulting Challenges
speakers: Elijah Stambaugh, Patrick Chouinard
keywords: Presidential AI Challenge, N8N, Gemini 2.5 Flash, education technology, business process documentation, use case identification
summary: Elijah announces winning the Ohio state level of the Presidential AI Challenge with his son, presenting an N8N automation using Gemini 2.5 Flash that generates personalized learning recordings from lesson plans and student interest inventories. He describes pitching to judges including OpenAI leadership. He then discusses challenges in productizing AI consulting services, struggling to help businesses identify valuable use cases beyond their immediate technical pain points.
-->

[01:11:38] Elijah Stambaugh: My son and I won the presidential AI challenge. President Trump signed an executive order to put AI in education last year in May. We won the state of Ohio, and then yesterday we pitched for the national level. We built an automation, an N8N [tool:N8N] automation with Google Gemini 2.5 Flash [tool:Gemini 2.5 Flash] that takes a lesson plan and an interest inventory from the student, and we combined that to create a personalized recording. The kids explained RAG [tool:RAG], embedding, semantic search. One of the guys was a high up at OpenAI [tool:OpenAI].
[01:14:02] Elijah Stambaugh: I've been working with several different prospects trying to figure out how to build more of a business in a box. Trying to get certain processes documented so that we can implement AI into their business. I've been struggling. I'm trying to productize what we're doing, but as we engage with these businesses, and they start to learn about what AI can do, it's like they just don't have any ideas. They wanted to do everything, but then they really just get to something that it's like, well, can it just do this one thing?
[01:20:40] Patrick Chouinard: Well, we had a short one this week, so we'll let everybody go back to finishing their taxes. And hopefully next week, we're going to be everyone in a better mood after tax season.
[01:21:23] Patrick Chouinard: Thank you very much, everyone.

=== UNRESOLVED SPEAKERS ===
- Patrick Chouinard
- Marc Juretus
- Ty Wells
- Paul Miller
- Andrew Nanton
- alexrojas
- Bastian
- David’s iPhone
- Morgan Cook
- Elijah Stambaugh
