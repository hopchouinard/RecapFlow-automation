=== SESSION ===
date: unknown (estimated recent, 2025)
duration_estimate: ~2 hours 20 minutes
main_themes: OpenClaw/open-source AI agent security, multi-tenancy in web apps, AI agent architectures for business automation, local vs. cloud LLM deployment, documentation-as-code workflows, AI adoption in enterprise/financial settings, software-on-demand philosophy

---

<!--SEGMENT
topic: Pre-Meeting Logistics and Introductions
speakers: Patrick Chouinard, Ty Wells, Morgan Cook, Juan Torres, Paul Miller, Hemal Shah
keywords: OpenClaw, meeting link, documentation, EC2, reverse proxy, memory module, security framework, Brandon, Markdown, Claude
summary: Participants join the call and exchange brief updates. Ty Wells mentions running OpenClaw on an EC2 instance behind a reverse proxy with some tools removed, primarily using its memory and organizational features. Patrick previews his plan to walk through his OpenClaw security documentation, which he built using Markdown files and Claude.
-->

00:01:03 - Patrick Chouinard
Hey, Ty.

00:01:09 - Patrick Chouinard
I was just going to check and see because I saw you posted and then to mark this link.

00:01:14 - Ty Wells
And I was like, I think I might be in the wrong link.

00:01:26 - Ty Wells
No, it's just because the original link was tied to his profile, so I could not be hosting. It was his personal room.

00:01:37 - Ty Wells
I see your document you put out there. That was really good. I was like, oh, my God. I just happened to see that because you sent the message about the question I read. I think, oh, God, I don't have to do it. Patrick did all the work and I know it's done properly and I don't have to worry about anything.

00:01:52 - Patrick Chouinard
Can just use it right out the box.

00:01:59 - Ty Wells
I'd locked mine down in an EC2 instance [tool:AWS EC2], and basically I'm using a reverse proxy, so it's not out in the wild. I removed some tools and did some other things to it. I'm actually not using it at all — I'm using the memory of it, the memory and some organizational pieces that I like. The memory for sure.

00:02:35 - Patrick Chouinard
▶ The memory is golden.

00:02:39 - Patrick Chouinard
I'm going to go through pretty much how I built that documentation and why I did it tonight, if people are interested.

00:03:04 - Ty Wells
I know it was the most popular question we received.

00:03:12 - Ty Wells
Hi, Morgan.

00:03:19 - Morgan Cook
And I'm glad that we're continuing with this meeting. It's been very helpful as nothing more than motivation for some of the time, but that's sometimes what you need.

00:03:34 - Patrick Chouinard
And it's not just me. Paul will also take the reins for some of the calls.

00:03:59 - Juan Torres
I'm really excited to read it.

00:04:06 - Patrick Chouinard
I understood that it's a method of publication that was interesting that I should continue.

00:04:14 - Juan Torres
Humanity needs your publications.

00:04:20 - Patrick Chouinard
Yeah, actually, it was a lot more simple to do than it looks like.

00:04:31 - Juan Torres
You're using MD files in order to create one of the sections, right?

00:04:39 - Patrick Chouinard
It's just a bunch of MD files, and then I simply asked Claude [tool:Claude] to create a website around them. That's it.

---

<!--SEGMENT
topic: Multi-Tenancy Architecture with Supabase and Clerk
speakers: Patrick Chouinard, Paul Gallovich, Morgan Cook, Shah Martinez
keywords: multi-tenancy, Clerk, Supabase, RLS, row-level security, ShipKit, tenant ID, foreign keys, server-side data access, invitation flow, PostgreSQL views
summary: Paul Gallovich asks about implementing multi-tenancy using Clerk authentication and Supabase. Morgan Cook shares his approach of bypassing Supabase RLS in favor of a server-side data access layer with a dedicated role, using tenant IDs in tables and views for public search. The discussion covers invitation flows, users belonging to multiple tenants, and offers to share research notes.
-->

00:09:08 - Patrick Chouinard
So I think the first question is Paul Gallovich. Do you want to expose the detailed question you've posted in the school thread?

00:09:31 - Paul Gallovich
<Q>I was looking, trying to implement multi-tenancy in any of the apps, so I was hoping to explore the best use case — for example, Clerk [tool:Clerk] has a multi-tenant option where you can create organizations and implement those React components in the application. I know it's possible to do with Supabase [tool:Supabase]. I know Supabase does support it. I've seen an example of Supabase with Clerk, but just wanted to ask about the best way to do that.</Q>

00:10:19 - Patrick Chouinard
I think you're referencing from the ShipKit [tool:ShipKit] application template. Correct?

00:10:36 - Morgan Cook
<A>I don't necessarily have the complete experience yet, but I'm working on the same problem. What I've done is quite a bit of research in authentication with Supabase and how to set up Supabase structure to not require the RLS mechanism. The RLS is enabled, but I'm not using it. I'm going around it because all my data access is through a server-side data access layer with a dedicated role. So the problem is really just about foreign keys and table structure, making sure that you have your tenant ID in each of the appropriate tables.

In my instance, the public can view a certain set of all data for searching to find multiple tenants, but the tenants only have access to administer the individual data set that belongs to them. My plan right now is to do that through views and a trigger job or some kind of cron job in the background to populate that table so that the public can always do their search and find the data.

▶ Your question then becomes exactly how do you get logged in to a specific tenant? And I'm exploring that myself right now — some of my users actually belong to multiple tenants, which is another complexity. Most of the time, you're just going to have one login belonging to a very specific tenant. And then you're going to have to look at maybe doing an invitation process where the admin of a tenant can invite via an email link to somebody who needs to have access so that they can create a login.</A>

00:14:05 - Morgan Cook
I saved my conversation and it has a lot of detail about actually setting up tenant. It's very specific to my project, but that may be useful. Send me your email and I'll forward it to you, and maybe if I clean it up decent enough, I'll have it for the next meeting for everybody else to have access to.

00:14:49 - Shah Martinez
Yeah, if you want to put it in the chat — I'm working on a multi-tenancy project now too, so I'd be super interested in seeing what you have.

00:15:18 - Shah Martinez
<Q>Also, Patrick, is your documentation thing posted in the school or in Discord?</Q>

00:15:23 - Patrick Chouinard
<A>The documentation I've created is posted in school, and Juan was kind enough to post it in the chat.</A>

---

<!--SEGMENT
topic: Google ADK Production Readiness
speakers: Patrick Chouinard, Hemal Shah, anapreciado
keywords: Google ADK, Agent Development Kit, Cloud Run, agent engine, LangGraph, LangChain, API calls, production deployment, Vertex AI, Brandon
summary: Hemal Shah asks whether anyone has taken Google's Agent Development Kit (ADK) to production. Ana Preciado shares that Brandon previously flagged ADK's API call structure as non-optimal and that Google later migrated users from the agent engine to Cloud Run. The group concludes ADK has significant gaps despite polished documentation, and identifies LangGraph and LangChain as alternatives.
-->

00:15:37 - Patrick Chouinard
Next, Hemal, you had a question you wanted to talk about?

00:15:46 - Hemal Shah
<Q>Yeah, Google ADK [tool:Google ADK]. Just wondering if anybody has actually taken it to production. It's been out there for quite some time, but I'm still wondering about its production adoption. If anybody had any experience with that.</Q>

00:16:28 - Hemal Shah
I know zero about it, so there's my answer.

00:16:40 - anapreciado
<A>I haven't shipped to production, but I remember that was my starting point as well. When I first joined here, my main question was on ADK, and I remember that Brandon told me that the way Google configured the API calls to ADK was not optimal. I had issues with the API calls to it. I wouldn't have known by the Google documentation that they had a mess — they were not as organized as I thought they were.</A>

00:17:34 - Hemal Shah
Yeah. They have a lot of information on their website, but there's a lot of missing pieces. It looks good and fancy on the front, but when you really use it, there are a lot of gaps. So that's what we're trying to figure out — how mature it is. I know LangGraph [tool:LangGraph], LangChain [tool:LangChain] — those are the other ecosystems out there. Probably those are the alternatives we'll explore.

00:18:04 - anapreciado
▶ What Brandon also said is that a lot of the problems they had was with the agent engine, and they were later trying to migrate everyone to use Cloud Run [tool:Google Cloud Run]. It's like they deployed something and then said the official way was to do it with Cloud Run.

---

<!--SEGMENT
topic: Frank Labs — AI Employee Platform Demo
speakers: Ty Wells, Patrick Chouinard, Juan Torres, anapreciado, Paul Miller, Shah Martinez
keywords: Frank Labs, AI agents, voice AI, LiveKit, DeepGram, NVIDIA PersonaPlex, Mistral 7B, GPT-4o, LightRAG, prompt injection, guardrails, multi-agent, lead generation, Apollo, Hunter, Perplexity, Clay
summary: Ty Wells demos Frank Labs (franklabs.io), a platform providing AI-powered business employees (SDR, customer support, finance) with real phone numbers, email addresses, and tool access. The discussion covers voice AI guardrails using NVIDIA PersonaPlex, a council-based security model, hybrid local/cloud LLM architecture using Mistral 7B and GPT-4o, and lead generation tooling via Apollo, Hunter, Perplexity, and Clay.
-->

00:19:20 - Ty Wells
So I'm working on a project called Frank Labs [tool:Frank Labs]. It's basically a team of AI experts that augment and help you with your work. I was working on this before OpenClaw [tool:OpenClaw], but I actually implemented the memory that Peter used in OpenClaw because it was better than what I had.

You can basically go through and see your team — you've got an SDR and what he does and what he has access to, and a customer support person. These are actual entities. They have emails, they have phone numbers. They can talk to each other. They can actually go out and do things for that specific business function.

▶ Try it out — if you go on the site and call Sam, it's a web call. It's franklabs.io [link:franklabs.io].

00:22:14 - Juan Torres
<Q>Are you using NVIDIA's voice-to-voice model? Is that the reason it's working really well?</Q>

00:22:20 - Ty Wells
<A>I am using a variation of their PersonaPlex [tool:NVIDIA PersonaPlex]. I evaluated it, pulled out the good things, and implemented those for its natural speaking ability. There's still some tweaking — there's some variance in there that pauses maybe a little bit longer than I want.</A>

00:23:01 - Juan Torres
<Q>How does the rail guarding for a model like that look? Is it through prompting?</Q>

00:23:10 - Ty Wells
<A>It's a couple of things. I've got a few guardrails in place — some prompting firewalls, and then some on the front end and back end that are helping to keep it under wraps. Its response is always guardrailed, and even the incoming response, because of prompt injection. With DeepGram [tool:DeepGram] and LiveKit [tool:LiveKit] integrated.</A>

00:23:56 - anapreciado
<Q>This is a team of experts — how are you validating their expertise?</Q>

00:24:04 - Ty Wells
<A>They're experts in the business function that they do. They're trained in sales, finance, etc., and evaluated based on the user's response. The function of an accounts payable clerk is pretty straightforward — you don't need big models to determine their business function. You just need the context of the business itself.

I'm using Mistral 7B [tool:Mistral 7B] as a local model, and GPT-4o [tool:GPT-4o] for the business function. On top of that, I'm using LightRAG [tool:LightRAG] to bring context to the business itself. I've got sales playbooks for different functions — those are ingested with data from their business to build out the result of how the interaction goes.</A>

00:27:16 - Paul Miller
<Q>At a high level, without giving too much away — what's been your high-level strategy for building a guardrail approach that gives you the right validation and protection?</Q>

00:28:40 - Ty Wells
<A>Basically, you need a council. I have several councils. You're familiar with the five-thinking method? The optimistic, the pessimistic, and the neutral. They make up a council that is contextually aware. I have a security council that manages cybersecurity against all of these agents and what they're doing. And I have a different council — a prompt injection council — that does the same thing with the data that the agents are producing. So it's sort of self-checking.

▶ There's a tradeoff though — overkill leads to latency issues and token issues. But it puts you in a way better position.</A>

00:38:01 - Shah Martinez
<Q>The bot that can go and reach out and get leads — at a high level, what does that implementation look like?</Q>

00:38:01 - Ty Wells
<A>I'm using services — a combination of Perplexity [tool:Perplexity], Hunter [tool:Hunter.io], Apollo [tool:Apollo], and some Clay [tool:Clay] because it's got to meet its requirement. I don't want it hallucinating. Clay is for grounding the ICP. That's a tool available to that expert. Different experts have different tools available to them — that's in a package of lead enrichments.</A>

---

<!--SEGMENT
topic: Workflow Automation — Markdown to PDF Pipeline
speakers: Morgan Cook, Patrick Chouinard
keywords: Claude skills, Playwright, HTML, PDF generation, JavaScript, Markdown, deterministic workflow, token optimization, compliance checking, image generation, ChatGPT image generator, cron job
summary: Morgan Cook describes building a client worksheet automation pipeline: iterating through Claude skills to convert Markdown to structured HTML, then to PDF via Playwright, with a human-in-the-loop layout review step. Once the process became deterministic, he converted the Claude skill to a JavaScript script, reducing processing time from 30–90 seconds to ~3 seconds and eliminating token waste. He also added a compliance-checking skill for regulatory requirements.
-->

00:40:09 - Morgan Cook
I've been working on some worksheet automations for a client. I started off with some skills in Claude [tool:Claude], maybe five or six of them, to flesh out the process — converting from an MD document into a structured HTML with a stylesheet behind it, and then using Playwright [tool:Playwright] and a few other things to generate a PDF from that HTML. In the middle was a human-in-the-loop cycle of making sure the page layout was correct.

Once I had the skill down in Claude, I had Claude modify that skill and convert it into a JavaScript. Once it was well-structured and not changing — I didn't need it to think anymore — it was easy to convert to a skill, or rather to a JavaScript that could then be run. The skill just makes a single call to the JavaScript at that point.

▶ The end goal will probably be to throw it into a trigger behind the website so she could just upload the MD and then it would go through the whole process, calling each of the individual pieces as it goes.

Part of it actually uses the content she provides to generate a banner graphic or a quarter-page graphic. So it generates a prompt and then I feed that prompt off to different generators — the last one I was using was the ChatGPT [tool:ChatGPT] image generator, which seems fairly straightforward and consistent.

▶ It takes 30 seconds to a minute and a half to process the Markdown into HTML using the skill, and about three seconds using the JavaScript. As well, you're not wasting any tokens at that point — your skill is not spending tokens to do the work. You can just call a local script.

00:43:37 - Patrick Chouinard
▶ Anything you can make deterministic, always a good idea. The AI is there maybe to organize, maybe to manage when to run which skill depending on context. But the actual job, if you can make it deterministic, awesome.

00:44:00 - Morgan Cook
When I started, I didn't really have a deterministic plan of how this was going to work. So it was useful to have the skills available to iterate through the process until I got to a deterministic state, and then at that point I converted to a script.

00:44:19 - Patrick Chouinard
That's how I build scripts as well. I build a script in Markdown, then I use Claude to review the script and see how it could convert part of it into either Bash, JavaScript, whatever you want.

00:44:51 - Morgan Cook
One of the skills I built was a compliance check — to make sure there are no specific verbiage violations in any of the workbook, that it has the required elements, the required font size and text for the licensor number and all that. So that was part of the piece as well — making sure that when somebody presents content for a worksheet, it's not violating any of the compliance rules they have to follow.

---

<!--SEGMENT
topic: AI-Assisted Development Team Dynamics and Adoption
speakers: Juan Torres, Patrick Chouinard, Elijah, Paul Miller, anapreciado
keywords: agentic IDE, vibe coding, AI-assisted developer, team collaboration, proprietary workflows, shell scripts, EC2, Tailscale, development modes of production, consultant entry point, bureaucratic resistance
summary: Juan Torres raises the friction of working with engineers who haven't adopted agentic AI workflows, observing that solo developers move much faster than traditional teams. The group discusses the resistance to "vibe coding" terminology, the proprietary nature of enterprise AI workflows, and how consultants can bypass organizational inertia. Elijah shares an example of a well-funded startup using agents for competitive research and PRD generation, but facing CTO resistance.
-->

00:45:41 - Juan Torres
I feel like there is going to be a new modus operandi of how coders are going to generally produce code. I am encountering that when I'm working on myself or in my own environment with my own database, I move really fast. But then I have to work with other engineers and their mode of operation is — you could even say it's outdated now. I'm working with a backend engineer who has a lot of years of experience but still hasn't fully implemented a feasible agentic IDE mode of operating. And a front-end engineer who's not very flexible with creating shell scripts or SSH-ing into the EC2 instance.

So there's a lot of friction points that come about with the lack of dynamism and the gifts that AI provides. I do believe there will be pockets of development teams that are just creating new modes of production as a result of fully embracing all the tools available to them.

<Q>I would love to see if anyone has resources on how development teams — a data engineer, an AI engineer, a front-end engineer, a product manager — interact with these new tools. How do they delegate tasks? How do they create virtual environments? Do they deploy locally or work out of an EC2 instance using Tailscale [tool:Tailscale] to secure? How do they do migrations? How do they use AWS CLI [tool:AWS CLI] with new agentic capacities?</Q>

00:49:00 - Patrick Chouinard
<A>The challenge you're going to have is a lot of that information might be proprietary. You get a lot of individual developers sharing because they have the liberty to talk about what they're doing, but for a large-scale team, it's often a lot of their secret sauce. So it's a little bit harder to get open sharing about those scenarios.</A>

00:50:01 - Elijah
So my one friend, he's at a company, and he shared with me what they're doing internally. He has a series of agents that does research on competitors throughout the week, and also has some roles around what it's allowed to ask, and how often it can ask the developers certain questions, so that it's not all the time, but it keeps all the projects up to date — "Is this still your deadline? Are you doing this?" And then it uses all that information throughout the week to send to a council, and then the council will determine what the best feature functionality is for the team to work on the next week, and then develop the PRD for them to execute against.

He showed it to me probably two or three months ago, and he said the CTO is not on board with AI. And he goes, "We're not going to have a company." So I think you're right — I'd be curious to see these internal and external resistance as well. I went to a coding thing like a week or two ago with a bunch of coders, and I mentioned vibe coding. Man, I got eye rolls.

00:52:06 - Patrick Chouinard
▶ Replace "vibe coder" with "AI-assisted developer." You're going to get a lot less eye roll from a lot of higher-ups. Vibe coder has become a little bit pejorative.

00:52:53 - Juan Torres
▶ A good bypassing of the momentum of their historical deficiencies is coming in as a consultant, because internally it's going to be really hard. But if you come in as an outside consultant with experience in the industry and now have grasped the tools of AI, and say "I can actually optimize your workflow because I already know how to solve this issue, but I know how to optimize it with AI" — I think that's going to be the entrance towards basically destroying a lot of the parameters they have.

---

<!--SEGMENT
topic: OpenClaw Security Framework and Architecture
speakers: Patrick Chouinard, Hemal Shah, Juan Torres, Elijah, Jake Maymar, Paul Miller, anapreciado, Ty Wells
keywords: OpenClaw, security framework, Proxmox, SSH tunnel, Telegram, GitHub PR, Obsidian Vault, Claude Code, Gemini, identity isolation, API budgeting, Privacy.com, Notebook LM, Markdown documentation, Cloudflare Pages
summary: Patrick Chouinard walks through his OpenClaw security documentation site, explaining how he isolated the agent with its own Gmail, calendar, and GitHub account, uses GitHub PRs as an authorization pipeline for all agent-produced artifacts, externalizes memory to an Obsidian Vault, and restricts web panel access to SSH tunnels only. He also describes his publication workflow using Markdown, Claude, and Cloudflare Pages, and introduces Notebook LM as a zero-cost chatbot layer over the documentation.
-->

00:58:55 - Patrick Chouinard
Let me share this. So as you can see, it's just a very simple website that I've published because I realized I had so much content accumulated, it just didn't make sense to post a blog post with that — it was just too dense, too much content. Every one of the cards is just representing a Markdown document that defines part of the security framework I worked on.

Everything here was created by AI with just my intention. I started with a chat with ChatGPT [tool:ChatGPT]. I spoke with it for about an hour, an hour and a half. At the end, I simply asked it to create a roadmap of everything we'd been working on and split it into very specific subject elements — a list of files to be created. Then I went through one more time and had it create the files.

The files were everything we'd been discussing about how to isolate the instance, how to make sure it had its own identity. A lot of the problem with independent agents is we basically give them the key to the castle — they work in our email, our calendar, our files. It becomes extremely dangerous, extremely fast.

▶ So basically what I did with mine is I created it with its own Gmail, its own calendar, even its own GitHub account. And I created for myself an organization where we're both part of it. If the agent needs to work on my code, it creates a fork, brings it to the organization, works on it, and pushes a PR. So I approve everything that changes in my code base. It even uses the PR and GitHub to push documentation. So anything, any artifact it works on, it pushes through the PR mechanism. I'm using GitHub [tool:GitHub] as a publishing and authorization pipeline for any work created by the agent.

▶ I do not use the web control panel for the agent except when I have absolutely mandatory maintenance. Otherwise, it's not accessible. If I need to reach it, I instantiate an SSH tunnel to the machine. Otherwise, Telegram [tool:Telegram] only.

▶ I've also externalized its memory. There is the memory.md file, but I also have it document every decision, every step, everything it does into an Obsidian Vault [tool:Obsidian] that is shared through GitHub. So I can inspect whatever is in its brain at any time. There's nothing it does that I don't see.

01:08:50 - Patrick Chouinard
There's an Interactive Notebook button — don't hesitate to follow it. That will bring you to a Notebook LM [tool:Google Notebook LM] of all of the Markdown files that constitute this. I've created a couple of artifacts — you can listen to the audio or have a slide deck of the entire architecture.

01:09:39 - Hemal Shah
<Q>Do you have captured anywhere your best practices in terms of which model you use, what type of machines, memory, CPU?</Q>

01:09:56 - Patrick Chouinard
<A>Memory and CPU — it's not demanding. It's just a Linux VM running on a Proxmox [tool:Proxmox] machine. If you can give it four gigs of RAM, maybe 50 gig of disk, and two cores, it's more than enough. For models, I run mine on my Codex account because Claude — they don't want us to run it with OAuth, but with Codex it seems to work fine. I actually deployed Claude Code [tool:Claude Code] onto the machine. So it's using Claude Code as a tool. OpenClaw gives instruction to Claude Code to create something. So OpenClaw, I can move it from Gemini [tool:Gemini] to ChatGPT — no issue. The coding actually happens in a coding model.</A>

01:16:30 - Jake Maymar
<Q>I have to be logged into a whole bunch of different accounts. I don't think I can give credentials to the agent. How would you handle that?</Q>

01:17:00 - Patrick Chouinard
<A>I treat it like a coworker — you set up all those different things, but then it's secure.</A>

01:15:36 - Jake Maymar
On that note — Privacy.com [tool:Privacy.com]. This allows you to set up a whole bunch of different cards, and if you're doing some unusual API calls to models you don't totally trust, you can actually pause and freeze the card, and you can do very small amounts.

01:16:23 - Patrick Chouinard
▶ That would fall into one of the documents I created about API budgeting and access to money. Basically, put caps everywhere. Anything that the model or the agent can spend, cap it.

01:20:19 - Patrick Chouinard
▶ What I wanted to build with this is an out-of-the-box, no API keys, no token cost — you have a chatbot basically built in through Notebook LM with the entire content of the site. If you want to read the site, you have it. If you want to talk to the site, you have the Notebook LM notebook.

01:21:01 - Patrick Chouinard
I created something that's really easy to consume, and it took all of 45 minutes to create — I took the documents, asked Claude to rewrite them in an academic paper tone, then gave it to Claude Code and said, "Create me a website out of that documentation."

01:23:19 - Patrick Chouinard
I'm a what I call a new generation of developer. I refer to myself more as a Markdown developer than anything else. Most of the code is done by Claude. What I do is I create the Markdown that ends up generating the code.

---

<!--SEGMENT
topic: Software-on-Demand Philosophy and AI Agent Business Tools
speakers: Ty Wells, Patrick Chouinard, Paul Miller, Elijah, Jake Maymar, Juan Torres
keywords: software on demand, FreshBooks, Zendesk, WhatsApp Business, ticketing system, OpenClaw, token consumption, Anthropic, heartbeat, MaltBook, subscription replacement, Ashley AI engineer, Telegram, Claude Code
summary: Ty Wells announces he is replacing FreshBooks and Zendesk with custom-built tools, exemplifying the "software on demand" philosophy. The group discusses how OpenClaw's heartbeat mechanism drives massive token consumption, speculates on inference provider incentives behind the tool's release, and reflects on the broader shift toward building bespoke software instead of paying for SaaS subscriptions. Ty also describes using an AI coding agent named Ashley via Telegram to build his projects.
-->

01:24:15 - Ty Wells
Where software is going, it's software on demand. That's basically what it is. Zendesk came up, and that's why I wanted to chime in — I'm literally moving my WhatsApp Business account off of that, because I built my own ticketing system for my customer support team. And then I was on FreshBooks [tool:FreshBooks] — I just use that to send invoices out. So I was just having the code build so it can pull the data out of FreshBooks to go ahead and send out these invoices. And then I just caught myself — I'm just going to replace FreshBooks with my own.

▶ If it's software, just build it. That's one less subscription.

01:25:53 - Patrick Chouinard
▶ Software on demand, guys. If you don't have it, build it.

01:25:58 - Ty Wells
Even if somebody has it, still build it.

01:26:01 - Patrick Chouinard
▶ The most valuable software is going to be software with a single user.

01:34:06 - Ty Wells
I've got Ashley. Ashley creates and builds on the code. I don't actually do anything — I talk to Ashley over Telegram [tool:Telegram]. I'm like, "Hey, I need you to do this." Ashley has the same memory as OpenClaw. So it's my engineer. I'm not doing really anything in Claude code — I'm using Ashley through burning up some tokens.

▶ Let's just put that out there — you can't use your subscription with OpenClaw. You have to use your API key, because otherwise you could get banned.

01:52:12 - Jake Maymar
I am very curious to see where OpenClaw evolves to. It's changed its name three times already in like a couple of days. But I do think it's a fascinating sort of infrastructure. It feels a little bit like a GPT-3.5 moment — like it was kind of cool and everyone was playing with it, and I had no idea what was around the corner. I feel like OpenClaw, since it's open source, there's going to be a tremendous amount of forks of it.

01:53:06 - Patrick Chouinard
▶ This is one of those moments — not because of the tool itself, because I don't think OpenClaw is the best-coded tool ever, but for the idea that it opens and the capability that it provides. I wouldn't be surprised to see Anthropic [tool:Anthropic], Gemini, and OpenAI [tool:OpenAI] start to create their own.

01:53:29 - Ty Wells
Claude actually went down today because of too many API calls coming from it. It's a token-churning machine. It has a heartbeat. Without that heartbeat, it's just sitting there passively waiting for you to input. I wouldn't be surprised if one of these guys are behind it — Anthropic in particular. Without the heartbeat, it's not burning any tokens. Why do you think there is MaltBook? There is MaltTask. There is the agent version of LinkedIn that popped up in the last couple of days. This is keeping them alive.

01:57:39 - Ty Wells
▶ There's already like six or seven copies of what OpenClaw used to be popping up everywhere. There's a NanoClaw out there — I would definitely take a look at that. That's just an entry level, and if you're a developer, you can build on it.

---

<!--SEGMENT
topic: AI Specialist Role at a Bank — Governance and Strategy Advice
speakers: anapreciado, Patrick Chouinard, Paul Miller, Juan Torres, Tom Welsh, Jake Maymar
keywords: AI specialist, bank, SOC 2, governance, compliance, financial services, Claude for Financial Services, Anthropic, Azure, AWS, hyperscaler, approved platform, one-person team, proof of concept, security team, non-technical stakeholders
summary: Ana Preciado shares that she has received a job offer as an AI specialist at a bank, where she will be a one-person team reporting to a non-technical manager. The group advises her to prioritize governance and SOC 2 compliance, identify the bank's approved cloud hyperscaler, define success metrics aligned with her boss's KPIs, and win over security and IT teams early by providing them services. Patrick notes that Claude for Financial Services costs ~$250K to enter.
-->

01:39:27 - anapreciado
<Q>I got a confirmation last week that I was going to receive an offer for working as an AI specialist at a bank. That means I would be a one-person team. I don't know what advice you have on identifying what would be the most important things to look for, especially because I'm going to be the one AI person. My boss is non-technical. Any advice from the many years of experience that you have?</Q>

01:41:17 - Patrick Chouinard
<A>First, they're going to have to define what AI specialist means to them because it can mean pretty much anything right now. And the one thing you're going to want to look at is governance, governance, governance, governance. In a bank, this is absolutely critical. You're going to face some very specific restrictions in the financial industry. SOC 2 [tool:SOC 2] is probably one of the most important ones to look at. It has its own restrictions — like the medical field has HIPAA. This one is SOC 2.

▶ In terms of working in the financial industry with AI, there are tools that are extremely powerful. But if you are a one-person team in a bank, I'm guessing that means it's a branch, not a head office, and it means you can't necessarily implement new tools — you have to use whatever is provided by the head office.</A>

01:42:56 - Paul Miller
<A>Claude for Financial Services [tool:Claude for Financial Services] is built for the financial industry, but the ticket of entry is a quarter million. So for a branch of a bank, it might be a hard pill to swallow.

▶ Where I would start: get from the organization as much of the documentation about your governance as you could load into your own little Claude project [tool:Claude], or into Notebook LM. Set up a Claude project, and say, "I'm new to this industry — understand the governance of the organization I'm going to be working in. What documents can I grab? What about the standard industry body?" Just give me background context, and then go into that library and say, "This is me. This is where I'm starting. What are some base documents I can publish and say to my boss, this is me positioning myself as to where I'm going to start?"

▶ Always the biggest thing for me is: what's the metric for success for this role? What's the metric for success for your boss's role? As long as you're aligned to the metric of success that bonuses are delivered on, you're grounded not only from a governance perspective, but from a commercial perspective.</A>

01:46:23 - Juan Torres
It sounds like she's being given kind of a project manager position, and she might have to hire technical specialists. Her main role is going to be understanding the standard operating procedure of the company and then finding the technical specialists that are going to be able to fulfill the automation processes.

01:48:55 - Patrick Chouinard
▶ Basically what you want to look at is: is there an AI platform already approved? If not, do they have a hyperscaler they're working with — Google, AWS [tool:AWS], or something like that? Once you've identified it, run everything through that one specifically. The rule of thumb I give everyone who works with me is: you have XYZ platform that is approved — with that one, work with internal files, with internal documentation, no problem.

▶ The way you tell non-technical users what they can and cannot do with other AI systems: ask them, "Is the material you're giving the AI right now — the document or the question you're asking — are you comfortable if that was on the front page of the newspaper tomorrow morning?" If the answer is no, revert back to the approved platform.

01:50:20 - Tom Welsh
▶ Having worked in financial services in the City of London: do not be dismayed when you get knocked back left, right, and centre from security, from compliance, from risk. These are all going to be smackdowns every day and you'll be in an uphill struggle. But you've got to stick to your guns, get the appropriate frameworks, and work from a position of strength.

01:51:01 - Jake Maymar
▶ If you provide a service for the cybersecurity team, it makes your life a lot easier to negotiate with them afterward, because it's really hard for them to say no to a service that they are using themselves. Any team that might stop you — provide them a service for free as soon as possible, then you're good.

---

<!--SEGMENT
topic: Local LLM Deployment, Gemma 3, and Cloud Deployment Guidance
speakers: Patrick Chouinard, Juan Torres, Tom Welsh, Ty Wells, Raghav, Morgan Cook, Hemal Shah
keywords: Gemma 3, LM Studio, GPT-4o OSS, Mac Mini, Proxmox, Vercel, Render, Railway, GCP, Vertex AI, Claude Code, CLI, hallucination, deterministic scripts, cron job, local model, VRAM, quantization
summary: The group discusses local LLM options including Gemma 3 14B on Mac Mini and GPT-4o OSS 20B via LM Studio, with Juan Torres noting VRAM constraints when combining a 24GB GPU with optimization libraries. Raghav asks for guidance on deploying to GCP/Vercel using Claude Code, and the group recommends Vercel for simplicity, using Claude Code to set up the CLI step-by-step. The session closes with a discussion on hallucination as a signal of insufficient context, and Ty Wells' reverse hallucination training approach.
-->

01:32:45 - Patrick Chouinard
▶ If you're looking for a good local multi-modal model, one I really like is Gemma 3 [tool:Gemma 3]. I'm able to run the 14B locally without too many issues. It's not going to power something like OpenClaw in any significant fashion, but for simple interaction questions — expose it to a search API like Brave [tool:Brave Search], something like that — it handles like 75% of the questions I would ask an AI. And it has decent conversation skills.

01:33:48 - Patrick Chouinard
Mac Mini 24 gig works flawlessly. I used to run it on a Windows machine running two 1080 TIs that are now retired after 10 years.

01:28:47 - Patrick Chouinard
▶ For private data, just use LM Studio [tool:LM Studio]. There is LM Studio with GPT-4o OSS 20B — it will run on most reasonably recent machines. You don't even need a RAG. You can just point it to a directory and ask questions like that.

01:36:08 - Juan Torres
I had the same predicament — I deployed an 8B Mistral parameter model on an A10 GPU, which is only 24 gigabytes. The problem is that you cannot use optimizer libraries like vLLM [tool:vLLM] because if you have 24 gigabytes, the LLM is essentially taking almost all of them — about 22–23 gigabytes — and vLLM takes about five gigabytes. So you have no space to use the GPU for optimization. ▶ You have to go from a 24GB GPU to an A100 GPU, which is 40 gigabytes, in order to compensate for the lack of VRAM.

02:12:23 - Raghav
<Q>Do we need to have knowledge of deployment to the cloud? My app is running locally. Now I want to deploy it on the cloud, maybe in two different environments — dev and production. Do I need to have some kind of knowledge about how to deploy, where to deploy?</Q>

02:12:47 - Patrick Chouinard
<A>It's not a matter of if Claude can do it or not — you have to have at least an app knowledge to know where you're deploying and how, because Claude will automate the job, but you have to know what job you want it to automate.</A>

02:14:03 - Tom Welsh
<Q>What language are you developing in? Because that's a precursor. Looking at things like Vercel [tool:Vercel], Railway [tool:Railway] for Python — are you using Docker containers?</Q>

02:14:15 - Ty Wells
▶ Depending on who you're deploying to, it depends how easy it is. Google Cloud Platform [tool:Google Cloud Platform] is a nightmare to deploy to. Vercel — GitHub, set your projects up, press go, it's there and done. It's a simple setup and easy to run.

02:15:50 - Ty Wells
<A>You can tell Claude what you want done and let it figure out exactly what needs to happen. You just have to read and follow the instructions. The first time, ask Claude Code to guide you step-by-step on what you need to do to set up the Vercel environment. It will tell you, "Oh, this step, do you want me to take care of it?" And for steps that require generating a token or something like that, it's going to guide you on how to get the token created.

▶ One thing I would add: tell it to check every so often if the CLI version is updated before a critical release. If it's not up to date, you'd be in a bad spot trying to deploy.</A>

02:18:45 - Ty Wells
<Q>Is hallucination bad or good?</Q>

02:19:00 - Ty Wells
<A>Hallucination is basically a lack of information in the request. It's a good thing if you can see it, because that means you can understand that you didn't provide enough context.</A>

02:19:22 - Patrick Chouinard
▶ That's why all of my prompts always include: "If you don't know, say so." Always provide the model a way to achieve its goal without having to hallucinate to get there.

02:19:40 - Ty Wells
I've been running a reverse hallucination process. If the model hallucinates, I use that hallucination to teach it to not hallucinate — which means ask more questions. Rather than giving it a way out, my way out is for it to basically fix itself and be better about it. I'm tracking those hallucinations.

02:20:17 - Tom Welsh
▶ The danger is there are so many ways it could hallucinate that you're going to teach it forever, and you're not affecting the weight of the model.

---

=== UNRESOLVED SPEAKERS ===

- **anapreciado** — raw name passed through unchanged; no canonical form found in alias map
- **Elijah** — raw name passed through unchanged; no canonical form found in alias map
- **Mitch** — raw name passed through unchanged; no canonical form found in alias map
- **Raghav** — raw name passed through unchanged; no canonical form found in alias map
- **Shah Martinez** — raw name passed through unchanged; no canonical form found in alias map
- **Jake Maymar** — raw name passed through unchanged; no canonical form found in alias map
- **Paul Gallovich** — raw name passed through unchanged; no canonical form found in alias map
- **Tom Welsh** — raw name passed through unchanged; no canonical form found in alias map