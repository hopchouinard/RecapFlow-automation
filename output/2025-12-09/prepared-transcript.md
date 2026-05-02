=== SESSION ===
date: unknown (transcript timestamps span 00:08:00–02:10:24)
duration_estimate: ~2 hours
main_themes: ShipKit community project updates, AI agent development, enterprise AI evaluation, parallel agent workflows, voice AI for automotive CRM, compliance/certification, local models, developer tooling

---

<!--SEGMENT
topic: Session Opening & ShipKit Onboarding Problem
speakers: Patrick Chouinard, Brandon Hancock
keywords: ShipKit, custom GPT, template selection, onboarding, Claude Code, Discord, RAG template, TinySeed, prompt engineering, chicken-and-egg problem
summary: Brandon Hancock opens the call with a personal update about being accepted into TinySeed and a passport emergency that delayed travel. Patrick Chouinard describes a solution he is building to help users identify which ShipKit template to use from within a custom GPT, addressing a community-raised onboarding friction point. Brandon confirms this is a priority improvement for the platform.
-->

00:08:38 - Patrick Chouinard
Hey, Brandon.

00:08:40 - Patrick Chouinard
Yo, yo, what's going on, Patrick?

00:08:43 - Patrick Chouinard
Good, good.

00:08:45 - Patrick Chouinard
Still, I'm actually working on something that popped up in Discord today.

00:08:51 - Brandon Hancock
Oh, what was it?

00:08:54 - Patrick Chouinard
The request to have a way to, out of the first prompt, identify which template it should be used with.

00:09:03 - Patrick Chouinard
So I've cloned all of your repo, and right now I'm analyzing it to create a file that will contain that, that I will add to my custom GPT [tool:custom GPT].

00:09:14 - Brandon Hancock
Oh, that's sick. Which — interesting, no, that makes sense. <Q>Because that was one of the issues I ran into, was like, it's a chicken-and-the-egg issue of like, oh, download the prompt, or download the project to get the prompts.</Q>

00:09:31 - Brandon Hancock
But, no, I see where you're going. I like that. I really like that.

00:09:37 - Brandon Hancock
<Q>Are you thinking a community thing, or what were you thinking, or put it in your GPT?</Q>

00:09:40 - Patrick Chouinard
<A>Yeah, I'm going to put it in my GPT, but I'm also going to publish the updated code in the community as well.</A>

00:09:49 - Brandon Hancock
Oh, you're the man.

00:09:54 - Brandon Hancock
It's funny. I've been so swamped. Just a quick update before we dive in. So I think I mentioned to you guys a little while ago, I got accepted into TinySeed [tool:TinySeed] for a startup, which was kind of based off the RAG template [tool:RAG template], and so we literally all week have been traveling to do a kickoff, and I was supposed to be gone today, except my wife's passport expired — we realized that yesterday at 10am, and we were supposed to fly out today at 10am. So we had to sprint to the passport embassy, but we got it, so we get to fly out tomorrow.

00:10:52 - Brandon Hancock
Thank you guys for being flexible on adjusting for a Monday call. Patrick, you're up first anyway, buddy, so if you want to kick us off, we'd love to hear what you've been up to.

00:11:15 - Patrick Chouinard
Well, basically, you've heard what I've been up to in the last couple of hours. It's something that popped up in the Discord today, like mid-afternoon.

00:11:28 - Brandon Hancock
No, 100% needs to exist. The second we get back, I really want to redo the onboarding experience to answer that question. ▶ Like, literally probably have some training on, like, what template should I use? Just so you could ask the chat right then and there. Like, you could ask ShipKit [tool:ShipKit] itself, which one should I use for this project, and have it tell you. So I just need to redo the onboarding as soon as I get back.

00:11:46 - Patrick Chouinard
Yeah, well, you're probably going to be able to steal a couple of lines of what I put in the custom GPT to do that.

00:11:56 - Brandon Hancock
100%. All the files I'm extracting — basically I'm analyzing each codebase, and extracting the information, and that's specifically what I asked Claude Code [tool:Claude Code], like: extract all the information and put it in a file, the information that's going to be needed for another agent to be able to read and define which template to use to implement a project.

00:12:20 - Brandon Hancock
That's going to be awesome. No, I'm pumped to see it. Thank you so much for diving in, Patrick.

---

<!--SEGMENT
topic: Enterprise AI Platform Evaluation
speakers: Patrick Chouinard, Brandon Hancock
keywords: enterprise license, OpenAI, Anthropic, Gemini, Perplexity, token pool, multi-provider strategy, model evaluation, enterprise agreement, Claude Code
summary: Patrick shares that his company is pursuing enterprise licenses across all major AI platforms — OpenAI, Anthropic, Gemini, and Perplexity — to conduct a comprehensive evaluation. He explains that enterprise agreements differ significantly from public plans, including unlimited token pools shared across users, and argues against locking into a single provider given the pace of market change.
-->

00:12:28 - Brandon Hancock
Anything we can help with on Ayura?

00:12:30 - Patrick Chouinard
There's one part that's job-related. I have to be careful about how much I share, but basically, I'm going to end up with an enterprise license for all of the major platforms in order to do an evaluation. So that's OpenAI [tool:OpenAI], Anthropic [tool:Anthropic], Gemini [tool:Gemini], Perplexity [tool:Perplexity], all of them.

00:12:56 - Brandon Hancock
That's awesome. So, is this more of a — your company has a set of tasks that you want to evaluate each one amongst to figure out which one's the right one for the right task?

00:13:08 - Patrick Chouinard
That's the part I have to be careful about not going into too much detail, but let's just say that I'm going to have to evaluate every single aspect of every single platform in their enterprise version. And I've already realized that there's a bunch of stuff in the enterprise version that is not present in the public version.

00:13:32 - Brandon Hancock
Hey, after you go through that, dude, I'm sure there's going to be a ton of golden nuggets. So if there's anything, if you're like, hey, this is the model for enterprise, don't ask questions, just use this — that would be very helpful.

00:13:44 - Patrick Chouinard
I don't think that's going to be the answer. ▶ It's just enterprise agreements are different because they come with a bunch of tools, a bunch of assets on top, and I don't think — with the speed at which the market is changing right now — that it makes sense to bind yourself to a single provider for any length of time. So have an agreement with most of them, just decide where you send your tokens at any point in time.

00:14:19 - Patrick Chouinard
So basically what I'm building — and I've been at it for only two days — basically, you remember the Gemini search agent [tool:Gemini CLI] that you've been working on? I've actually tried it with Claude Code. Incredibly, it's far more powerful than Gemini CLI to do that.

00:14:51 - Brandon Hancock
Really? Claude Code? You learn something every day. Real fast, guys, what Patrick's talking about — what you can use, what Patrick was using Gemini CLI for a lot of times, is you could basically create your own custom research where you would basically come up with a ton of search terms and kick off dozens of agents at the same time to go off and search a bunch of different terms in parallel and basically put together findings. It was like a really cool custom way of doing deep research, and Patrick was using Gemini CLI because you get access to Google search.

00:15:28 - Brandon Hancock
But I tried it too, and I loved it. We used it to help find some customers for us. So I'm pumped to try it now with Claude Code to see if it works even better.

00:15:41 - Patrick Chouinard
It works better because Claude Code has a way to mix web search and fetch — web scraping. And the way we structured the prompt, it's basically analyzing every provider every day and gathering the information so we can have an evolution curve to see which provider becomes interesting. It tracks everything — the news about Code Red, something that Sam Altman said, the release of a new model. Actually, I learned doing that today that ChatGPT 5.2 is going to be released tomorrow.

00:16:22 - Brandon Hancock
Oh, seriously. You heard it here first.

00:16:27 - Patrick Chouinard
Yeah, and it's running that pipeline that I got that information, because it goes into news sites — it's basically the inverse of deep search. Deep research is a drill: one subject, very, very in-depth and in detail. This one is horizontal.

00:16:46 - Brandon Hancock
Oh, okay. Go wide.

00:16:49 - Patrick Chouinard
Exactly. So it's really, really interesting. And basically, when you have no limit on tokens that you pay for yourself, it's incredible what you can do with the tool.

00:17:04 - Brandon Hancock
Patrick, are you on the $100 plan or the $200 plan? I can't remember where you're at.

00:17:08 - Patrick Chouinard
Personally, I'm on the $100 plan, but the enterprise ones are unlimited.

00:17:14 - Brandon Hancock
Oh, sick. That's awesome.

00:17:24 - Patrick Chouinard
You basically buy a token pool that is used by all the users of the agreement.

00:17:34 - Brandon Hancock
No, I have never used one of the enterprise plans, so you learn something every day.

00:17:39 - Patrick Chouinard
So as I go through it — right now I just wrote the prompt to do that — but I also want to write a lot of internal analysis. We're going to dump all of our business requirements into that project, and I want to leverage cross-analysis between the result of the search and — basically, we decided to start with the conclusion with a degree of confidence, and every day we run all the searches, we will update the confidence level either up or down. If we go below a threshold, we're going to scrap the solution and change our approach. If we go above a certain threshold, we're going to state that this is the adopted one and go with it.

00:18:21 - Brandon Hancock
Hmm, okay. Dude, I love that you are leading the enterprise adoption at your company. It's very cool to kind of hear what's going on in the real world at scale, versus most of us are just kind of on our own stuff. So it's very cool to see both sides. Please keep us in the loop, Patrick. I'm eager to hear what happens next.

---

<!--SEGMENT
topic: Parallel Agent Workflows & Morning Summary App
speakers: scottrippey, Brandon Hancock
keywords: parallel agents, aggregator pattern, Anthropic SDK, Google APIs, Claude, Trigger.dev, Vercel AI SDK, context window, Haiku, Sonnet, system prompts
summary: Scott demonstrates a personal productivity application that runs multiple AI agents in parallel — a course summary, follow-up check, and relationship check — using the Anthropic TypeScript SDK and Google APIs, then aggregates results. The segment covers the generator-evaluator loop pattern, context window management strategies, and the decision to build natively rather than use Trigger.dev.
-->

00:18:54 - Brandon Hancock
All right, next up — Scott, you're next, buddy.

00:19:18 - scottrippey
Hey guys. So yeah, nothing much here other than — let me share and show you what we were talking about online. One of the ShipKit calls was the parallelization and the aggregator and that whole thing in my app. Just for context, so everyone else knows what's going on —

00:19:39 - Brandon Hancock
Scott's building a really cool agent tool to help automate a lot of what he's pulling up right now. He has built out a bunch of different agents to automate parts of his day. What you can see right now is a very cool morning summary. Basically, each one of those different agents does a different thing. And we were brainstorming together how we can speed things up. We talked about using a tool called Trigger.dev [tool:Trigger.dev], and they make it super easy to do a bunch of agentic workflows. So, dude, how did it go? Were you able to dive deeper into it?

00:20:14 - scottrippey
Yeah. So basically what I did was — I was thinking about doing something in parallel and I just basically took a screenshot of a workflow from Trigger.dev to give it extra context when I was building this. So we're not using Trigger.dev at all. This is still internal. But the cool thing now is this is all in one. Because I remember before I had like, this was its own thing and relationship check was its own thing. And I kind of realized when I was getting a morning summary that there was some weird overlap. So what we were talking about was: why don't we make this where the course summary, the follow-up check, and the relationship check all run in parallel at the same time with our own API calls.

00:20:52 - Brandon Hancock
We'll save — so it's a lot less tokens at once, too.

00:20:55 - scottrippey
I mean, yes and no, because it also helps if I grow them right. I have some room if I need to. But the cool thing is — I can see the hard-coded system prompts because I wanted to see them — and then what I did was, just like my chat down there, I've got Google APIs [tool:Google APIs] plugged into this, so I can get emails, meeting notes, tasks, all kinds of stuff. I've got Claude APIs [tool:Anthropic SDK] hooked into this where I have a big system prompt in here, and I can suggest improvements. This is like my system prompt for chatting in this side window against everything, where I can go, hey, what are my tasks for the week?

00:21:50 - scottrippey
So this was the first thing I had done, and then we were like, well, let's be more agentic. I think you might have actually given me the bump to do this.

00:21:56 - Brandon Hancock
Dude, it's coming along. Look at that.

00:22:00 - scottrippey
I mean, this thing works flawlessly, and you can have your four favorite prompts just sitting here, and name them whatever you want. That's Haiku [tool:Claude Haiku], that's Sonnet 4.5 [tool:Claude Sonnet], you can upload more context here if you want to do more than your system prompt, and I actually have two different email signatures, I can make one or the other active even within the same chat. I can have this actually send email, I can have it do anything — it'll send out meeting invites, it'll do it all from the chat.

00:22:28 - scottrippey
<Q>Quick question for you real fast — on the emails, are you using an SMTP tool, coded yourself, API calls, what's going on?</Q>

00:22:35 - scottrippey
<A>So all of this is built on the Anthropic SDK [tool:Anthropic TypeScript SDK], the TypeScript one — it's like the agent tool call on this — and the Google APIs. So I'm basically using those two together to code this, and then yeah, call everything. So I'm hooked right into my Google APIs, I'm not using any MCP in this.</A>

00:23:06 - scottrippey
And then the agent notification — the cool thing what I did, Brandon, was: well, okay, if we're in here doing this, I can still put on some custom behavioral instructions that adds it to the aggregator at the end after it all comes in.

00:23:28 - Brandon Hancock
Oh, that's cool.

00:23:29 - scottrippey
Actually be like, hey, prioritize this or do that — just some extra little behavioral guidelines. But still, if I'm just going to type this in, if I want to be lazy and I'm not going to be in Claude Desktop and actually build my prompt or whatever, I can do it in here and then it'll just keep suggesting improvements. And when you suggest improvements, it's really cool — it'll actually give you different options and you can click them and it'll do it. And it'll start giving you a score.

00:23:54 - Brandon Hancock
That's cool, dude. Seriously.

00:23:56 - scottrippey
It'll do it on both of those interfaces. So the next step at some point — what you and I were talking about — is combining this one with the other thing we saw on Trigger.dev of doing a loop for quality, a pass-fail, and then some sort of loop when it gets to the aggregator. I have a note in the future in Claude Code on that. Some of these ideas are sitting in my planning doc, but that'll be like — it might be overkill on that, but I kind of want to do it.

00:24:22 - Brandon Hancock
Let me show everyone what we were talking about — AI agents. So long story short, what Scott is talking about doing next — one of the easiest patterns to do is this one, where you have one agent do work — this is the generator, think of it as like the worker bee — then you have an evaluator who's basically saying like, hey, that worked, or no, it didn't. And if it doesn't work, what we're also going to do is provide feedback, so that then, whenever it comes back to the other agent after we go through the full loop, it's going to say, hey, try again, but here's the additional feedback on what you need to do differently this time. ▶ So it's a really good way — it takes a little bit longer, but it produces really high-quality results. So if you're working on kind of nebulous tasks and you just want to make sure that you get high-quality results, this is a really cool way to have the agents work and critique, work and critique until they get the desired output.

00:26:02 - scottrippey
Yeah, that one. So that's kind of what that does now.

00:26:06 - Brandon Hancock
So yeah, what Scott's doing is basically — you can do this in Trigger.dev, or you could technically do this with Vercel AI SDK [tool:Vercel AI SDK]. But the act of doing multiple parallel calls that get streamed is really hard. But if you're just doing straight-up generate-text calls with Vercel AI SDK, you could do that. And then whenever you're done, you bring in all the results into an aggregator.

00:26:32 - Brandon Hancock
<Q>Scott, quick question for you — what happens, what have you done if the output from all of your parallel tasks exceeds the context window?</Q>

00:26:39 - scottrippey
<A>Oh, yeah. So I have it — it won't, it shouldn't ever do that, only because I have hard-coded a few things. And there are certain things I put as settings. What I did also was — I was running into that problem. It was actually timing out because of that. Before I started doing this parallel thing, I was already having a problem. It was trying to do like a hundred emails, or a hundred days. I was like, no, like I only need like the last seven days. So I have all these parameters where it's never going to be so much data that it'll fill up the context window. It only tries to analyze meeting notes if it applies to something. And those are summaries too, because I'm using just the summaries, not the full transcripts. And it only hits my knowledge base to search for titles. So by splitting them into the separate calls, each of them has their own context window now.</A>

00:28:36 - Brandon Hancock
And I think it's very cool too that you have not Trigger.dev, but you still have it working on your own system through the Claude APIs. Like that's cool that you — I think you said you took a screenshot and you said, hey, do this.

00:28:50 - scottrippey
Cause I was explaining it and I'm like, but here's the screenshot. Cause that's so visual. I love that screenshot. I said, you know, I want to run them in parallel, but I probably could have said — if I could take those three things and do that, I probably would have done it because I mean it's already set up to use the SDK and I did so much with the system already. Like at this point it's getting easier and easier to start building these things in because it's kind of all been worked out and it's working and I just — it's tweaks now or like, oh, add this feature to it.

00:29:32 - Brandon Hancock
<Q>And final thing — just to make sure I understand — are you using the Vercel AI SDK and then using Claude Code, or are you specifically using Claude's SDK?</Q>

00:29:32 - scottrippey
<A>Yeah, so basically it's just a standard TypeScript, Next.js application — no Vercel SDKs or anything. It's just the Claude Anthropic TypeScript SDK. It's not the agent SDK — I got confused about that. The agent SDKs I think are for more things like Claude Code.</A>

00:30:11 - Brandon Hancock
I'll drop a link in the chat for everybody. [link:Anthropic TypeScript SDK]

00:30:16 - scottrippey
Yeah, and that thing was awesome. I mean, Claude Code just installed everything it needed to, and then we started building, because I wanted to build the API calls and the chat agent using the SDK, and that was perfect.

00:30:32 - Brandon Hancock
Well, Scott, you're crushing it. Literally, every time we call every other day, you have built something. You're consistently grinding on this, so you're becoming the agent expert. I love it.

---

<!--SEGMENT
topic: Social Media Automation SaaS with Image Editing
speakers: Ryan C, Brandon Hancock, scottrippey
keywords: social media automation, Nano Banana, image generation, Cloudflare R2, Supabase, Netlify, Claude, brand voice, client approval workflow, git commits, Claude Code
summary: Ryan demonstrates a social media management application that generates a month of posts using Claude, allows in-platform AI image retouching via Nano Banana 3 Pro, and manages client approval workflows. The segment also covers practical development tips including task-based development, git commit automation via Claude commands, and the importance of committing frequently to avoid losing context.
-->

00:30:46 - Brandon Hancock
Glenn, you're up next, buddy.

00:30:49 - Glenn Marcus
Hey, y'all. Just lurking today. Most of this week I've been actually in a lot of these types of rooms, spending a lot of time with fellow geeks, learning about new tools. Yeah, it's a good week. We're all trying to figure it out, right?

00:31:14 - Brandon Hancock
Speaking of that, just a quick update. So like I said at the beginning of the call, we got accepted to TinySeed and we all got to go to a kickoff this week. So it was cool because you had people that were just starting out their company and people who've been doing it for five years. And guys, it is unreal when some of these big businesses take off — the guy's like, oh yeah, we're probably making like two, three hundred thousand a month right now. And it's just like, you could buy a house every month with your software business. ▶ They solved a very valuable problem at scale. And it's not like they're smarter or more hardworking — they picked a very valuable problem and usually partnered up with someone who had very intimate knowledge in the field.

00:32:26 - Brandon Hancock
▶ Guys, if you can basically automate workflows for businesses using AI at scale, and it's a big business, and they normally pay an employee $8,000 a month, and you give them a $3,000 a month subscription that replaces five guys — you just print cash. Like, it's as simple as that.

00:32:51 - Brandon Hancock
So that was a very cool, just like eye-opening experience. I can confirm not making hundreds of thousands of dollars a month. If I do, I will let you guys know when it happens.

00:33:11 - Brandon Hancock
Next up, Ryan, what's up, man?

00:33:15 - Ryan C
How's everybody? I am currently doing extra lots of battle with Netlify [tool:Netlify] and Claude Code because it keeps failing to build something that it was building perfectly fine earlier today. And it's changed something I didn't ask it to. And now I can't figure out what has changed. So I'm currently smashing my head against the brick wall. It's really annoying. But I've made quite a lot of progress on my social app. I think last time I talked about it, I was working on building an application to automate social media posts. And Scott has already told me off today for this, but I'm reaching and singeing my fingers and my hair. I'm one of those people that has lots of ideas, and I go, oh, that's cool, sod it, I'll just add it. So I've now integrated Google and Nano Banana 3 Pro [tool:Nano Banana 3 Pro] to do retouching and complete image generation all within the application with a full preview shown and then accepting and overriding of the original image if I want to keep that, if it's better.

00:34:25 - Ryan C
So yeah, it was working and now isn't working because of whatever it's changed in the background, which is really annoying because I wanted to show it on this call because I can literally just tell it to change a really minute part of an image and it will just change that. But it's brilliant because it saves me having to bother to pull it out and edit it in Photoshop and then put it back in. I can just edit it in the platform.

00:34:44 - Brandon Hancock
So you're saying Nano Banana changed? Like something changed with a model?

00:34:49 - Ryan C
No, as in Claude Code has changed something in the back end of how I was API-ing into it and it's broken it, which is annoying. So it's now just going around in the doom loop trying to figure out what it is. I can't remember what it's done, because I may have been back to the conversation about 15 times today, and it's now hallucinating. So I need to clear that down and get it to start thinking about it again from scratch.

00:35:11 - Brandon Hancock
Right, so super, super fast — like two tips just on the development, like software development life cycle approach. ▶ So the way I'm building out all startups is I do everything task-based, where I end up creating an artifact of, like, here's the task, here's the plan, here's the code changes, here's the test. And basically just, that way for each change, there's an artifact that's associated with it. So if I ever have to go back — ideally you're committing along the way — but if not...

00:35:43 - Ryan C
I tried that, but it's forgetting.

00:35:45 - Brandon Hancock
Yeah, that's the hard part, because you get so good, and you're like, man, I'm on a streak, I'll just keep going forever. And then finally when you do need it, you're like, oh, I wish previously you'd done this.

00:36:06 - Ryan C
I can show you guys what it looks like up to the point where it doesn't die.

00:36:25 - Ryan C
So this is the dashboard and this is the demo company. So I've got it working now — so when I press "generate first month," that all links in with Claude. Generates a month's worth of posts from the stuff that's uploaded in the content bank. And you can upload galleries in here and stuff to post to Instagram. All that fun stuff. You can download it. And that's all linked up with Cloudflare [tool:Cloudflare R2] as the bucket to hold all of this. And then if you go into something like this, press edit, you've then got "enhance with AI" in here. And I've got a whole system — I can custom edit, and then get it to — I've had it change her uniform to blue multiple times — and then the preview will pop up there, and the idea being I could save the preview and just overwrite the other one in the database.

00:37:15 - Brandon Hancock
That's cool. That's very cool, man. And under the hood, just to make sure — the only image tool is Nano Banana. Are there any other moving parts?

00:37:28 - Ryan C
<A>Well, Nano Banana is literally it on the image side. Claude, for any social media writing, because I've got a big prompt system where I'm doing system prompt, and then Scott very kindly taught me through putting a framework in, so it goes system prompt, framework, and then client stuff — I've got a whole load of client information in the background that it pulls in as part of the client prompt — brand voice, brand context, all that sort of stuff — and then feeds through the images and all the descriptions and stuff, so Claude knows what it's looking at to write the prompts. I think I probably will start feeding through the image as well, just so Claude can look at the image also when it's writing the social media posts. And it pushes it through to the client side — the client can then approve or request an amendment, which then sends it back to Claude to amend with some notes that they put in.</A>

00:38:19 - Brandon Hancock
<Q>Are you a Supabase man? I think you said Netlify, so what are you using for your blob store?</Q>

00:38:27 - Ryan C
<A>I'm just a Scott Acolyte here, so I use everything he uses — GitHub to Netlify, Supabase [tool:Supabase] for database, Netlify to build it, and Cloudflare R2 [tool:Cloudflare R2] to store media. I don't want to smash my Supabase, so I've set up a Cloudflare R2 bucket for all the media, which works perfectly.</A>

00:38:55 - Brandon Hancock
Yeah, that's awesome. I mean, you're absolutely crushing it. Is there anything we can help with?

00:39:06 - Ryan C
Yeah, that's the only thing I'm stuck on right now, to be honest. The rest of it was just sort of flowing quite nicely. I just need to add a few more bits in here, but it's working quite nicely.

00:39:23 - Brandon Hancock
One thing, Ryan — just like super quick recommendation. ▶ So you can make your own version of this, but one thing that I always like to do is make a Claude command — a one-time thing — to where anytime I'm coding, I can just do "git workflow commit" and it just instantly looks at all the changes and does it all. So it's super easy — I'm working on something and then I just make a command, like a Claude command, to kick off the workflow to commit the changes, and then I just go back to working. So I'm just like, boom, save history, save history. So it just quickly always makes the changes and commits them all. So you can always go back in case something goes wrong.

00:40:20 - Brandon Hancock
And it just triggers in the background. So there's no reason to watch the process — just fire and forget it to at least commit.

00:40:46 - scottrippey
So even though we could do it with the command, I literally just — it knows from the Claude.md file to commit, but only commits when we tell it to. We just say, hey, commit this to GitHub. Like that's literally all we do when it does it. And it always picks good messages.

00:41:00 - scottrippey
But I love that because I know if people write them out — either tell it or do what you're doing — but I did want to ask you, though, if you do that, does that actually do it in the background where — well, you can just open up another terminal window if you had to, I guess, because it still takes up the terminal window to do it that you're in when you run the command, right? Or is it in background?

00:41:18 - Brandon Hancock
I spin up new ones. I'm spinning up new windows religiously, so I spin up a new window — yeah, because I treat them as background tasks, like, just go do stuff, go do stuff. And because I'm just cycling through them, like, it's basically like I'm working in a Slack with like a dozen employees, and I'm just like, how are you, how are you, how are you, you need help, give you stuff, review you, kick off a new guy. So I'm just rotating constantly. That's the fast way. And I'm talking 90% of the time. So it is honestly exhausting the way I do it, but damn, you can fly.

00:42:00 - Brandon Hancock
You entered the matrix.

00:42:02 - scottrippey
Ryan, I wanted to say — I use Whisperflow [tool:Whisperflow], I got him to use Whisperflow — we do the talking thing all the time, we're not typing.

00:42:15 - Ryan C
Yeah. I think my typing has slowed down now. I struggle with typing, I'm like, oh god, this is so slow, I want to talk to him in a public place and I can't, or whatever, it's frustrating.

00:42:27 - Brandon Hancock
Dude, I double down — I'm the guy in public space, I'm just like, I'll never see any of you again. Who cares if I'm rambling to my computer by myself.

00:42:37 - Brandon Hancock
The weird one, though — final thing — a random side note: I have the Limitless [tool:Limitless] pendant. That's — I feel awkward when I'm walking around, I have no headphones in, and I literally am just talking to myself. Because I'm trying to take notes, but I'm talking to myself so my note taker can do it. You get weird looks on that one.

00:43:04 - scottrippey
I tried that out, Brandon, and I had to return mine. I could not get anything to work. I got a bunk one, so I ended up returning it.

00:43:09 - Brandon Hancock
It's a cool product, though.

00:43:13 - Brandon Hancock
Ryan, any other things we can help with?

00:43:16 - Ryan C
I don't think so at the moment. I'm trying to get this thing to work. Because once I can get this to work, I've got a couple of social media clients I need to get into it. And then, in theory, I can scale that. I can probably 10x, maybe 20x the income on the social media arm, which then pays for everything and everything else is a bonus. That's the plan.

00:43:37 - Brandon Hancock
I gotcha. Now, very, very pumped. I love just a quick update — the way Ryan's tackling it, he has basically — from my understanding from the other week — you have a service that you're already offering right now. And now you're using — because that's generating money, like, boom, that's all the proof you need. So now it's just like, man, instead of me doing all the work, why don't I build systems to do it for me? ▶ I love that — that is my favorite way to build. A lot of times it's very easy to forget it's software as a service, meaning does the service actually provide value? And obviously Ryan's done that, so now it's like, cool, now I'm going to throw in the software. A lot of times it's easy to go backwards. But yeah, Ryan, you're absolutely crushing it. You've done it textbook. This is textbook SaaS land.

---

<!--SEGMENT
topic: Automotive AI CRM & Voice Agents
speakers: Maksym Liamin, Brandon Hancock, Ryan C, Carlos Aguilar
keywords: WhatsApp chatbot, voice agent, Nissan, Mazda, Infinity, CRM, Kimi K2, GPT-4o mini, LiveKit, latency, tool calls, RAG, automotive, Salesforce, lead tracking
summary: Maksym Liamin shares progress on automotive AI deployments for Nissan, Mazda, and Infinity — including a WhatsApp-based RAG chatbot for field sales (8,000 users) and a client-facing voice agent. He also describes a lightweight CRM built into WhatsApp that captures leads in real time, replacing end-of-month data dumps. The group discusses voice model trade-offs between latency and tool-call capability, with mentions of Kimi K2, GPT-4o mini, and a new OpenAI real-time model.
-->

00:44:24 - Brandon Hancock
I think next up, Maxim, what is up, you stud? Where are we at? Mexico? Europe? What's going on?

00:44:32 - Maksym Liamin
Yeah. Hi, how are you doing? I'm in Mexico.

00:44:35 - Brandon Hancock
I'm in Mexico right now, finally set up, finally did all my papers, rented the flat, everything, so now I can come back to the coast.

00:44:45 - Brandon Hancock
So are you founded — because I know for a while there, it was like an immigration thing — is everything good, you're saying?

00:44:52 - Maksym Liamin
Yes, yes, everything is great. I have my temporary residence now for one year, and then can extend it up until like four.

00:45:00 - Brandon Hancock
Oh, perfect, dude. That's awesome. So, dude, Maxim, last time we talked, you were doing a ton of cool RAG stuff. You were also starting to get into voice. Very last call I think we had was you were just starting to use a combination of, like, LiveKit [tool:LiveKit], Kimi K2 [tool:Kimi K2], with some self-hosted stuff. There were a few other things that were going on. So, dude, what's been going on?

00:45:25 - Maksym Liamin
Yeah, so we keep working with Automotive. Onboarded two more clients, which is Mazda and Infinity, so...

00:45:33 - Brandon Hancock
RAG or voice?

00:45:34 - Maksym Liamin
It's both. We have one solution that was already working. If you remember, we were doing it with Nissan. It has, I think, right now, cumulative, like, around 8,000 users or something like this. And it's for salespeople. It's for basically field sales. It's a chatbot in WhatsApp [tool:WhatsApp] that you can ask any questions on pricing, give you the credit data, give you photos, videos of the cars, whatever it is — all different colors — and it answers you. And the other application is client-facing, so it's basically the same, but now without a salesperson. So you just talk to a WhatsApp contact and it gives you all the information on pricing, crediting, photos, videos, technical sheets, and all the other stuff. And you can also call it, so it also works as a voice agent and it can give you the same info, but via voice.

00:46:23 - Brandon Hancock
But that's awesome. Okay, so a few questions. So for the voice side, that is to help the customer — do they still have sales agents at all or are they trying to get rid of them?

00:46:38 - Maksym Liamin
No, it's still in — it's very big companies. So they — like this kind of product is still in, let's say, early testing. Like they send us leads, which is, I don't know, maybe like 300 to 500 people per week. But obviously it's nothing in comparison to the full capacity. So we still need to do a lot of checks and tests and maybe in the next year we can already have it fully working, but still it's kind of in the middle of the beta.

00:47:08 - Brandon Hancock
Okay, so I recently got to talk to a few guys that were doing some cool stuff, so I just want to drop some business ideas for you. If you make millions, please don't forget us little guys. Okay, so cool idea one — either add to your current one or just like you're slowly building out a portfolio of SaaS companies. ▶ Basically a tool to train the sales guys. So basically what you could do — a lot of the times guys aren't following the scripts, they're not handling objections, or they do great when the customer is very easy going, but the second people hit them with constant objections, they just struggle. So you want to practice against an LLM [tool:LLM] that costs a few dollars for a call rather than losing a customer that could have been worth thousands. You're already in the market, you already have great connections with these customers — you really could start to make a sales voice training place where you could ask them hard questions.

00:48:14 - Brandon Hancock
And it kind of ties in with your other services — you already have these sales guys with the phones to where they can answer questions. So you're basically building a portfolio of products around a very profitable customer.

00:48:31 - Brandon Hancock
So I just wanted to throw that your way just because, you know, me trying to do this — I have no connections with those guys. But you, on the other hand — you already have those connections, which is the biggest unfair advantage and the social proof of already delivering value.

00:49:07 - Maksym Liamin
Yeah, that's a great idea. Actually, talking about business ideas — we recently also introduced a kind of CRM [tool:CRM] to our tools, to all the tools that are salesperson-facing. The point is that all these companies have CRMs, like they use Salesforce [tool:Salesforce] or in-house built CRMs, but nobody really uses them, actually. They use it only at the end of the month, in the last day of the month, because they get paid based on what they put in these systems. But it's very uncomfortable for them and they don't want to lose time during the day. So we started incorporating this kind of leads tracking to have it very easy, very simple for them — they just send a name and phone number and car of interest and it's already registered in the system. And they can query those and check the follow-ups and all this kind of stuff.

00:49:57 - Maksym Liamin
And yeah, the biggest advantage is that now these companies actually see what their salespeople are doing, not at the very last moment of the month, but actually throughout the whole month — there's a full progression.

00:50:14 - Brandon Hancock
<Q>Can you say the last part? So what analytics do you get to track?</Q>

00:50:18 - Maksym Liamin
<A>So before they would put all their leads — just dump them at the last day of the month to get paid. Now they put it throughout the day actually, as it goes, and we can see the actual real-time progression and kind of what is happening.</A>

00:50:33 - Brandon Hancock
Oh, okay. That's cool. I mean, that's awesome. Do they have to manually do it? Do you automatically do it for them now?

00:50:40 - Maksym Liamin
They just send the text with a name and the phone number and we already register the lead for them. And then they can question: which leads do I have this week? Whom do I need to call up? We have direct reminders in WhatsApp that come to their phone and tell them when to do what they put. So yeah, this is all hooked up.

00:51:00 - Brandon Hancock
That's very cool. Maxim, I always like to see all the cool things you're building because these are insanely big and valuable projects. Dude, is there anything we can help with on any of this?

00:51:12 - Maksym Liamin
No, I think everything is good. Yeah, I just wanted to join and see you guys.

00:51:52 - Maksym Liamin
Actually, the last week — literally — do you know a company called Poke?

00:52:07 - Brandon Hancock
I do not. What is that?

00:52:11 - Maksym Liamin
It's like also a WhatsApp companion. Well, not a WhatsApp — it's like an iMessage companion. It's a company from San Francisco. And they do kind of all the things with your emails and calendars and kind of automate it. So it's like a personal assistant. Still, they are like in the very early stage, but I see that they got big investments there in SF. So we took their idea literally like last Thursday, built it so that it's ready on Friday, and went to some schools because we've been recently invited to some universities to give talks.

00:52:46 - Maksym Liamin
And yeah, I mean — so it connects to your calendars, to Booking.com, to whatever you connect with, and can do a lot of stuff, and this is all via iMessage [tool:iMessage].

00:53:07 - Brandon Hancock
Oh, that's so cool. Yeah, because everything else has been WhatsApp throughout everywhere else in the world. So it's like, I've been very jealous for the WhatsApp people, because you could do so much more cool stuff than us. Now it's also in iMessage.

00:53:24 - Maksym Liamin
Well, we basically decided to try something like this here in Mexico. It's like a first attempt at B2C, because we've been always working B2B with these big industrial companies, but now went first time B2C to some schools where we've been giving talks to entrepreneurship students, and then we got our first batch of beta testers. So this is like a cool side project that I'm also working on. It also connects to your Gmail, you can connect it to multiple accounts, you can send emails, forward, reply, schedule events, get notifications for your reminders, connected to documents — ask questions about documents in Google Drive, whatever it is.

00:54:08 - Brandon Hancock
That's awesome, Maxim. That, once again, freaking cool, man.

**Voice model discussion:**

01:27:50 - Brandon Hancock
<Q>Maxim, any suggestions for voice? I mean, I've only really gone deep in ElevenLabs [tool:ElevenLabs].</Q>

01:28:06 - Maksym Liamin
<A>Yeah, it's a model that can do tool calls, right? And that has around 40 milliseconds of latency, not more. When you pick smarter LLMs, then suddenly they are too latent. When you pick ones that are very fast, then they cannot do tool calls properly. So it's always like a trade-off that you are taking.</A>

01:28:32 - Ty Wells
▶ Yeah, GPT-4o mini [tool:GPT-4o mini] seems to work well for me as the balance on ElevenLabs for tool calls and low latency. I think it's around 45 milliseconds, if I remember.

01:28:55 - Maksym Liamin
Okay. Yeah, you've got to get the model right though. The right model makes a difference to make both happen. Because you go with the cheaper model, then one of the two are going to fail — it's going to become agentic, non-deterministic. I haven't tried GPT models in a long time. Like last time was, I think, in June, but they were very slow for the use case. So I went on to try more open-source LLMs that are hosted and quantized properly and went with Kimi K2 [tool:Kimi K2], which seemed to work very well. And still until this time we use it in production. But definitely if you say that it's actually 40 milliseconds of latency, I will give GPT-4o mini a try.

01:29:33 - Carlos Aguilar
I think that would be even better than that. There is a new model for OpenAI. It's GPT real-time [tool:GPT real-time]. It's recommended for voice.

01:29:47 - Maksym Liamin
<Q>Have you tried it?</Q>

01:29:48 - Carlos Aguilar
<A>I have not tried it. I was just reading about voice agents two days ago and they recommend — I don't remember, it's GPT-5 real-time or just GPT real-time. But they recommend that if your use case is voice.</A>

01:30:04 - Maksym Liamin
I see. Thank you. I may have to try that too.

01:30:08 - Brandon Hancock
▶ If you guys do get to try that, please let me know because I'm always just like, I just want to have in the back of my head like, this is good, this is not good. So please share with the group too so everyone collectively gets smarter.

---

<!--SEGMENT
topic: Compliance Certification & Google CASA Tier 2
speakers: Maksym Liamin, Brandon Hancock, Ryan C
keywords: CASA Tier 2, SOC 2, Vanta, Google OAuth, cybersecurity certification, compliance, audit, Google APIs, beta testers, Accommodation
summary: Maksym asks for guidance on obtaining Google's CASA Tier 2 cybersecurity certification, required when using restricted Google OAuth scopes (Gmail, Calendar, Drive) in production beyond 100 beta testers. Brandon shares knowledge of SOC 2 certification platforms like Vanta, explains the difference between SOC 1 and SOC 2 Type II, and estimates costs. Ryan adds that some compliance gaps can be formally accepted rather than remediated.
-->

01:30:23 - Maksym Liamin
Another quick question that I had — because I know that you work a lot with the guys from Google. We are currently looking to get a CASA 2 certification [tool:CASA Tier 2], like a cybersecurity certification from Google. Do you know anybody who could help with it or have you heard anything about it or any tips, advice, contacts?

01:30:42 - Brandon Hancock
<Q>How do you spell it? CASA 2?</Q>

01:30:44 - Maksym Liamin
<A>Yeah, it's like this — CASA and Tier 2. It's basically when you use OAuth to give access to Gmails, calendars, drives, and everything, and you have this consent screen where you select scopes. If you have restricted permissions, then they ask you for this certification so that you can use it in production, because right now we're limited to 100 beta testers, and we're already close to getting that number, so we need to find a way to get this certification fast enough.</A>

01:31:29 - Brandon Hancock
So the main ones that we've looked at recently — there's Accommodation, there's Vanta [tool:Vanta], and there's a few other ones. I was just trying to look it up for you, but those are the ones for SOC 2 [tool:SOC 2], like things like SOC 2, which sounds very similar to what you're describing. They basically give you the checklist, and then they have partners that do the audit. They actually help on both sides — here's exactly what you need to do to implement, they give you a checklist, they run all the tests, and then part two, they actually help with connecting you with the auditor who gives you the stamp and seal of approval. ▶ So you do pay for it — you're roughly going to pay $7k for Vanta, or maybe a little bit more depending on the complexity, and another $7k for the audit itself. So just to share numbers, that's what you can expect.

01:32:28 - Brandon Hancock
V-A-N-T-A. But you would probably just want something similar to Vanta. I don't think they do it, but you would want something similar to it. And, you know, it just costs money. That's the part that sucks.

01:32:52 - Maksym Liamin
<Q>And have you gotten SOC 2 for some app? Like, how long did it take you in terms of time, not the money?</Q>

01:32:59 - Brandon Hancock
<A>I have. We are starting the process — literally January 1, 2026, we are going to be kicking things off. But no, I just know a lot of people, I've talked to a lot of people who have done it, because I wanted to make sure we were picking the right company. Vanta is the one we are going to use. SOC 2 is different — you can get SOC 1, SOC 2. SOC 1 is your compliant today, like at the time of the test. And then there's SOC 2, which is continuous monitoring — that takes, I think, six months, because they basically look at your logs for six months to verify that you have been doing things properly for a long time. But it just depends on your test, because if it's a one-time test, I've heard people get it done very quickly, like a month or two.</A>

01:34:00 - Ryan C
Sorry, Max — I was speaking to a guy who runs a big software company over here, and he's just done software compliance. And he said there's a lot of it that you can sort of indemnify away. So some of it, they come to you and say, you know, this is an issue, right? And you can literally just go, yes, we are aware, and we're happy to take the risk that that is a potential flaw. ▶ So there is that element of it as well — you don't have to be completely watertight and tick every single box. There can be bits where you say, yeah, we're aware it's a potential problem, and we're comfortable with it being a potential problem. That could save you some time and pain.

01:35:04 - Maksym Liamin
I see. Thank you guys.

---

<!--SEGMENT
topic: Kiosk Application, Windows Desktop Dev & Remote Coding Agent
speakers: Ty Wells, Brandon Hancock, Tiran Dagan, Glenn Marcus
keywords: kiosk, Windows application, Rust, Claude Code, Docker, VPS, ElevenLabs, voice, GitHub Actions, Electron, PyInstaller, Whisperflow, parallel agents, token usage
summary: Ty Wells describes rebuilding a Windows kiosk application using Rust compiled via Claude Code and GitHub Actions, and demonstrates a remote coding agent running Claude Code on a VPS accessible from his phone. He also shows a machine-learning prediction platform for SMBs (PECAN AI-inspired). Glenn Marcus shares relevant experience managing 9,000 kiosks at Target via NetKey. The segment covers practical tips for kiosk OS lockdown, fleet management, and the cost of running parallel Claude agents.
-->

01:03:19 - Brandon Hancock
I think it is Ty, then Tiran.

01:03:21 - Ty Wells
Oh, not too much. How's it going?

01:03:24 - Brandon Hancock
Doing good, man. What about you?

01:03:27 - Ty Wells
Good, good. I've got more questions than I have show-and-tell, you know. I do have a little show-and-tell. I finally got a MacBook. So, if you have any guidance on setting that up, the environment, that'd be great. I'm not a Mac person at all, so I'm Windows.

01:03:50 - Brandon Hancock
▶ The main things I would recommend buying instantly: Presentify [tool:Presentify], eight bucks; Amphetamine [tool:Amphetamine], six dollars — it keeps your computer on so it doesn't always close out, so whenever I start my workday, I just turn it on, just leave my computer on. Then, outside of that, it's called Magnet [tool:Magnet]. So what I can do is I hit Control-Option and I can just move stuff around on my screen or different screens. The second you get used to those Magnet shortcuts, oh, my God, it's so beautiful. So those are the main ones I'd recommend.

01:04:44 - Ty Wells
And then, let's see — I'm working on a couple of projects. I haven't gotten back to ShipKit Studio, because I'm in a hackathon.

01:04:51 - Brandon Hancock
Oh, that's awesome.

01:04:56 - Ty Wells
And then — so I'm building this kiosk application for my business. We have like 50 kiosks and I'm adding voice to it, but I'm rewriting the entire application. They run on Windows machines, so I would say I need a Windows application, and I'm building this in Next.js for the event space. <Q>Is there a way to build a Windows application through Claude Code?</Q>

01:05:34 - Brandon Hancock
<A>I mean, Electron [tool:Electron] is like the first thing that comes to my mind for making just desktop applications that work for Windows or Mac. That's the main thing that comes to my mind. And compiled Python.</A>

01:05:49 - Tiran Dagan
In the chat, I sent you the link of the package. It's called PyInstaller [tool:PyInstaller]. [link:PyInstaller]

01:05:58 - Ty Wells
What I did was I built a Rust application through Claude Code, deployed it over GitHub Actions [tool:GitHub Actions], and so I just downloaded from there. So I never touched any other environment outside of Claude Code to build that, because it needs a launching application that launches the kiosk software that then obviously is a web view of the kiosk that's running. So that seems to be working. I was just wondering if that was the best approach to build that.

01:06:37 - Brandon Hancock
The way I've done it in the past — you are on a Windows machine, you said? But the way you're running the final application — is that Windows or Linux, the kiosk itself?

01:06:53 - Ty Wells
That'll be Windows.

01:06:56 - Brandon Hancock
What you can do — I'll tell you what I did in Linux, and maybe a lot of it's transferable. ▶ But what you usually do is you can update your systemd records so that whenever the system boots on, it can actually auto-start certain applications. You can turn off other background processes. You basically have full control of what happens when you boot. So ideally what happens is whenever the computer boots up, you can turn off the bottom Windows bar. You can make the background of the actual Windows desktop the company logo so it just looks like a loading screen while your application is booting up. Then your application launches. Not only does the systemd records say auto-launch, but it also says like, hey, if this crashes under any circumstances, always force reboot. Always. So that's how I've done it in the past, and it's been strictly systemd records.

01:07:53 - Tiran Dagan
Just setting up a virtual machine that's configured and, you know, you have an image that you can reload in case something happens.

01:08:08 - Ty Wells
Yeah, I mean, keep in mind, this is an existing platform that another team built for us. I'm just rewriting it because we don't like the way they support it or whatever. But again, thanks for that, both of you guys.

01:08:47 - Ty Wells
Okay, so this is what we're building. I don't know if you guys are familiar with PECAN AI [tool:PECAN AI]. They're data modeling, machine learning, for predictions, right? So we're doing this — and so what it does is it allows small businesses to go ahead and do predictions on their data for different use cases. So like customer — you know, typical stuff that Amazon and stuff — presenting options to buy this or that, or those types of things. So that's what the platform is about.

01:09:31 - Brandon Hancock
Beautiful UI, by the way.

01:09:37 - Ty Wells
Thank you. And so let's log in here. So basically, you would come in and you can integrate your data. And obviously, we're going to link up a few of these, but you can take a raw file — you can do it if you have access to the Postgres that's where your data is — you can upload a file here, and basically it will — so I've got some data actually from that kiosk that I'm trying to — since I'm rebuilding it, I'm trying to present the next possible thing that they should purchase. So I'm using that historical data. Machine learning obviously does regressions and classifications, so it would take that data and try to regress it to come up with patterns for it. So I want to pull in that data, and then I can choose a use case for that. In this case, it would be like product recommendation, so then with product recommendations, you've got to tie your data — you'd need certain fields — and so that's the process that we're going through. And then it will learn that data through regression models, probably XGBoost [tool:XGBoost] for the most part — it's a combination of models, it depends on what the use case is. And then I can make predictions off of — will this customer churn, or that sort of thing.

01:11:07 - Brandon Hancock
<Q>So where are you getting these models from?</Q>

01:11:15 - Ty Wells
<A>Well, I'm creating these models. So I'm using — are you familiar with the way machine learning works? There are known models out there to do regression testing. That's what machine learning does — it takes your historical data and runs regression tests on it to figure out, you know, whatever your use case is. Like, for example, if you're doing customer churn — will this customer churn? So you'd need things like when was their last purchase, any issues they had, these types of things. Then you can learn off of that data to determine when you anticipate that they will churn based on their historical data. So that's what it's basically doing. And this is an expensive effort for enterprise. So we're building this for SMBs. Small businesses don't really do anything with their data — their customers come in, they buy what they buy, but they don't really take advantage of that data and use it to predict, to reach out to that customer and say, hey, we saw you purchase X amount ago, we have this new product.</A>

01:12:37 - Ty Wells
Mm. Yeah. So that is the project.

01:12:43 - Tiran Dagan
I was just going to suggest, if you haven't done it, you should build a bridge to SAP [tool:SAP]. Because that's — I see SAP entering into the SMB market. The $1,000-sized companies — that might be the sweet spot for you.

01:13:04 - Ty Wells
Yeah, that's exactly what we're thinking. That's going to be the sweet spot.

01:13:09 - Ty Wells
I'll share one other quick thing that I'm working on. I don't know if you guys are familiar with Daniel Messer's personal AI thing? Personal AI infrastructure?

01:13:21 - Brandon Hancock
Okay.

01:13:23 - Ty Wells
So basically, this is what I have here — it's a remote coding agent, if you will, because I work on multiple projects. But every time I leave my computer, for the most part, it's over, right? You can't do anything with my phone. So this is connected to a VPS [tool:VPS] that has Claude Code on it, that has Docker [tool:Docker] on it. And basically, I can pull down my repos to that instance on the VPS, and then I can communicate with that. So it's similar to what I think Chris was showing — something similar to this for his own personal thing. And this is sort of similar — so I can have all my windows, and you were talking about having all your terminals open, working on different things. In essence, it's the same thing, except I can do this from my phone.

01:14:17 - Brandon Hancock
That's cool. So which parts of — I guess, what are the most important parts of the VPS for you? Like, I know you said, so it's Claude Code running on Docker. So is it just like, is it your files that are the most important thing? Is it files plus tools?

01:14:35 - Ty Wells
Files plus tools, plus agents, plus skills, plus — I mean, all kinds of stuff. I've got all these agents here I can call on to do whatever. So Claude's streaming back over, tracking that stuff there. I got to add as many skills as I want. Obviously, there's a lot of repos out there. He uses something called Fabric [tool:Fabric], which is similar to a skill.

01:15:01 - Ty Wells
And then I've built in a voice too. So I can take my — I've got an ElevenLabs [tool:ElevenLabs] voice that I can have it play back. Like if I'm driving and it says, hey, this is what I need — the intent is to say, or it comes back and says, this is an issue — and then I can respond via voice and say, okay, we'll do this or do that or whatever the case may be.

01:15:21 - Ty Wells
I love this. It's all in the cloud because like I said, once I leave, I'm stuck. I can't work on multiple projects like that.

01:15:34 - Brandon Hancock
Cause like for me, like I have an email responder, but everything's in my Claude Code, like everything's on my local computer. So like, for example, I was traveling. So like, I genuinely don't like responding to emails unless I have my Claude Code with me, because I'm like, I could either do it and knock it all out in 20 minutes with Claude Code. Or if I do it manually, I'm going to be doing it for an hour and a half. So I love this because this would be — just on my phone — to go through the exact same email responder skill that he has trained for Claude Code. If I can do that manually, oh, that would be beautiful for my phone, just like a quick web app. So I love this problem.

01:16:13 - Ty Wells
I'm not sure what that is, but yeah, it pulls down that repo to the VPS and then you communicate. So I'll get another project window here. I can have all my projects open. I can move in between them. And this is my personal assistant here that can communicate with all of those windows and pulls in the context of the window that I'm on.

01:16:39 - Brandon Hancock
It is awesome. This is awesome. Ty, always coming through with sick demos. Always. I absolutely love it. So quick — I love software, I also love the business side. So quick question for both — for the personal assistant — I mean, that's huge. What are you — are you thinking just like, hey, this is my unfair advantage? Or are you thinking like, oh, I could maybe turn this into something else?

01:17:03 - Ty Wells
I know there are privacy concerns. Yeah, I mean, really, it's for me because it helps me continue to be effective while I'm working. So no matter where I'm at, right? So I can maybe check in just like I check my email, I can check in and see, that particular project is here and it needs a response on this or whatever the case — there's an issue. I can send that off and have that continue doing what it needs to do.

01:18:36 - Ty Wells
Thank you, Ty. Yeah, it's — no, I totally agree. Context — it's funny you're bringing that up, because I was talking with some developers in person, and the amount of times that they would just dive in and start coding — I was like, guys, you really got to plan, because you get the whole context window, and then you fly from that point forward. ▶ So even though it feels like you're making more progress for the first 10% of the project, the second you hit that mid-50%, you're not going as fast as you could if you just stopped to plan.

01:18:36 - Ty Wells
Well, can tell you, Anthropic is doing something right, too, because yesterday I burned through $300 — I was over my limits, just last evening.

01:18:51 - Brandon Hancock
Seriously? How did you do that, just out of curiosity?

01:18:55 - Ty Wells
Parallel agents. I had four projects going, and I had parallel agents — probably about, I saw some of them had like three different agents with sub-agents. I mean, I was just watching — all I was doing was refreshing my usage page, and it was just turning through the tokens.

01:19:24 - Brandon Hancock
You don't want that.

01:19:25 - Ty Wells
I think that's a badge of honor, man. I mean, the amount of work that got done — I got it all done last night, as opposed to, you know, why stretch it out?

01:19:36 - Brandon Hancock
Yeah, that's awesome.

**Kiosk history from Glenn Marcus:**

01:19:42 - Brandon Hancock
I know, okay, so I want to hop over to chat real fast. Glenn, you mentioned you used to work at NetKey [tool:NetKey], a kiosk management company.

01:19:49 - Glenn Marcus
Yes.

01:19:50 - Brandon Hancock
That's awesome. I actually tried to do a startup in that space. I started when COVID started, and companies were like, I just don't care about a kiosk.

01:20:08 - Brandon Hancock
Any advice for Ty on any kiosk-related things?

01:20:16 - Glenn Marcus
Oh, no. I mean, it sounds like he's already got the platform. My knowledge is, like I said, about 20 years old now. But yeah, back when we were doing it, you know, it was all Windows-based, like Ty was saying. ▶ Poor tenants of the platform were: being able to lock down a computer, because basically a Windows machine sitting out on a store floor somewhere — even though you can physically secure it, people are going to try to hack in. So we were doing kernel modifications and software, OS modifications to lock down the device. Fleet management was a big deal. We had Target with 9,000 kiosks nationwide. So being able to remotely control, reboot, update, check status of all those — before we had any Google Analytics, et cetera — so that was always a big challenge on just the runtime, the app development, and peripheral integrations.

01:21:09 - Glenn Marcus
We also bought a digital signage company. All the signs in Times Square were actually being run by my software, which was really cool.

01:21:17 - Brandon Hancock
That's so cool, man. That's so cool.

01:21:21 - Glenn Marcus
And then they were called WebPavement. We brought them in, then we revamped their software, then sold with NCR [tool:NCR] for a nice little exit.

01:21:29 - Brandon Hancock
Dude, well, that's awesome, Glenn. That's also just so cool. The fact that any time you do something with software — it's obviously very cool to see it on your laptop and other people using it, but the physical software, when you see it in the real world, it hits different. And in Times Square. That's the coolest place ever to actually do it.

01:21:49 - Glenn Marcus
80% of all Times Square screens are running on our software. It's really cool.

---

<!--SEGMENT
topic: Tiran Dagan's Project Portfolio
speakers: Tiran Dagan, Brandon Hancock, Patrick Chouinard
keywords: CV Refinery, resume tool, ATS, consulting disruption, Prepper tool, SherpaCow, trip planner, photo gallery, Dropbox, Supabase, face recognition, AWS Rekognition, ShipKit, markdown to HTML
summary: Tiran Dagan presents four projects: RefundMyCV (resume-job matching with iterative Q&A to build a personal fact repository), a Prepper emergency planning tool, SherpaCow (a trip planner with sequential and parallel itinerary workflows), and a family photo gallery app using Dropbox and AWS face recognition. He also discusses how AI is disrupting consulting deliverables, and Patrick suggests targeting consulting firms as a B2B market for the CV tool.
-->

01:41:34 - Tiran Dagan
All right. So I'm throwing in a little intro about myself. So I've been in all of these big companies — I work for Cognizant [tool:Cognizant], for IBM [tool:IBM], for Ernst & Young. And this is not going to be shocking to anyone — I had 400 engineers working for me at Cognizant. It will take them a month or two to build a tiny prototype that I can do myself in a matter of minutes today. It's just amazing.

01:42:02 - Tiran Dagan
So I'll do a little show-and-tell, because since I left Cognizant, I've been doing my consulting, opened up my own shop, and having a lot of fun. Here are a couple of projects, some of these you're familiar with. So one of them is this resume tool that I've built, RefundMyCV [tool:RefundMyCV]. It goes to address the fact that people find it hard to bubble up above the ATS [tool:ATS] filter. So it analyzes a resume against a job. So you upload the job, and then you analyze your specific resume to that specific job, and you get very detailed analysis — why are you a good fit, where are the gaps, what are the things you should do to your resume?

01:42:56 - Tiran Dagan
What I didn't share yesterday was that it also collects facts about you from your resume and from Q&As that the tool starts to ask you. So if I want to apply to this job, then it'll say — well, you have to address some gaps, answer these questions, and then I'll build you a better resume. And then it creates a new resume, and it changes the bullets and the wording and incorporates the information that you provided. If you do this 10, 15 times, you're building a repository that I'm collecting in the background so you can see all of the facts it knows about you — your domain expertise in mergers and acquisitions, here are some other questions, the Q&A answers, et cetera.

01:43:35 - Tiran Dagan
So that part is really fun, and I've been building a tool that allows you to scrape directly from LinkedIn [tool:LinkedIn], so if you see a job, you click onto the CV Refinery tool and it brings the job — click "Send to CV Refinery," it starts a job to ingest the job.

01:43:52 - Tiran Dagan
Another one is — I think I shared this yesterday — is this Prepper tool, and I have to — kudos to you. ▶ ShipKit [tool:ShipKit] is a game changer. It's un-freaking-believable. I spent the entire day today with my partner on this project, and it completely changed our thinking, the ideas that it threw out, and we're going to change. Also, we have a beautiful logo, thanks to your prompts, and a completely new UI. It correctly told me that this color scheme that I have is a little too dark and warning and scary. Need to use some different colors. It was really cool what it did.

01:44:38 - Tiran Dagan
This tool — you put in a couple of parameters or things that you're worried about that you want to plan. And, you know, where do you live? So I'm in London. And it's me and my wife and our child. And we want to plan for one month of bugging in, and I have a budget of $2,000. And it initiates a plan. And after then — so this is the part where the AI goes and builds an entire report — and it tells you, here are the supplies that you need to have, here is a map of escape routes and the benefits and the challenges with each of those choices, here are some resources for you to learn, skills you should build on to be prepared for this.

01:45:30 - Tiran Dagan
So it's early in development, so thanks for the tips yesterday, Brandon, and other guys that are here on the call. It's going to be much faster, and the architecture is completely changing, again, thanks to your prompts.

01:45:48 - Tiran Dagan
Another one — this is really cool, because I come from consulting. I used to be running a consulting practice starting at EY and through IBM and Cognizant. And consulting is about to be the biggest disrupted industry — and I'm not talking about IT consulting, but actual consulting: strategy, ops, et cetera.

01:46:13 - Brandon Hancock
This is an example of something I did. I obviously used AI to help me build a sample analysis. This is for Thumbcast. So I used AI — generated the beautiful report. We used all of the current data about the markets. This was a pitch for why you need to have a chief AI officer. But what we ended up doing is building a tool that converts a markdown report to a clickable interactive application. So you have that text, and now, in five minutes, you spin out an entire site that lets the executives drill into your analysis.

01:46:56 - Tiran Dagan
I think this is a perfect example of how AI is going to disrupt consulting as an industry, as a whole.

01:47:05 - Brandon Hancock
<Q>Real fast, going back to the consulting — so here, my question on this is, so are you thinking it's more going to disrupt it on the thinking and planning, more on the output deliverables, the whole process?</Q>

01:47:19 - Tiran Dagan
<A>In this case, there's two phases. One is the report generation — once I generated the report, have crafted the prompts that I want, and I have a report that I'm happy with — and it's usually what we'll do is that's going to be something that enhances and supports a report that we're actually doing, because the consultancy that I have is a loose-knit collection of C-suite folks, so they bring in their expertise. This brings in the data overlay market research. And then, now you have a report — what do you do? You spend days to create a beautiful PowerPoint or, you know — the report that we generate is essentially — this is a markdown converter, markdown to HTML, but it's taking that and turning that into drill-down graphics. That's the fun part — each one of these has some kind of interactivity and I let the AI choose what to do with it. I just instruct it to create beautiful visuals and drill-downs — the detail prompt on the outcome and not on the format. This is all self-selected.</A>

01:48:35 - Patrick Chouinard
That's beautiful. I love how interactive — my wife, she's a consultant, and the amount of time she has to spend right now on the deliverables is unreal.

01:48:44 - Tiran Dagan
So I'm always trying to say like, hey, use Gemma and like all these other ones, but it's a lot of — a lot of times their tools are kind of locked down on what they can bring in and adopt some AI stuff, which is like, man, like I — it's like you need to go faster.

01:49:06 - Patrick Chouinard
Yeah, actually — about your CV Refinery — <Q>have you ever thought about proposing that to consulting firms? Because they spend an insane amount of time reformatting CVs to be submitted as part of RFPs or client requests or things of that nature.</Q>

01:49:27 - Tiran Dagan
<A>That would solve an incredibly big problem they have, because they spend their days reworking Word files. Patrick, I'm going to give you a big hug. I love that idea. Coming from consulting, I know exactly what you're talking about, because as a partner — you've already picked the team that you are going to have, and usually you don't have any control over it, right? That's whoever is available, whoever is on the bench. But you have to convince the client that this is the reason why this is the team.</A>

01:50:00 - Patrick Chouinard
Because you need to pretend that they have the ability to turn down people.

01:50:05 - Tiran Dagan
Yes. The thing is, it's not even a matter of modifying the CV. It's just presenting it in a way that matches with whatever they request. So I see your system being used as consuming the request from the client and just selecting whatever's in the CV of the user and matching and then presenting it in a form that matches the request.

01:50:25 - Tiran Dagan
A hundred percent. That is a great idea and it's a different league.

01:50:35 - Tiran Dagan
Another one is more for fun — SherpaCow [tool:SherpaCow]. My wife helped me come up with this name. Right now I've parked it a little on the side, but it was a fun project that I'll come back to. It's the concept of — how do you create a trip? I couldn't find any real good trip organizers. There's a lot of apps on the iPhone and you end up paying for — when it's very closed. What I wanted to do is: how do you plan for it — you know, you're going to Japan, Brandon, right — you want to plan essentially mini trips. What does my day look like? Or here's a three-day trip in Tokyo, here's a two-day hike around. And your trips have to have some flexibility — here are some things that I'm going to do in sequence, I'm going to go to this museum and I'm going to go to that place, but when we have lunch, I want to know what are my five options for lunch so I can choose on the spot. And I didn't find a planner that really does that.

01:51:30 - Tiran Dagan
So here I have the concept of mini trips. So like waterfalls — and here I borrowed from the world of IT — it's essentially you build a workflow, so a workflow can have fixed sequences, things that I drag and drop. I want to add this — in between, it calculates the driving directions — or I want to have flexible options. I want to choose between going to this thing and that thing or that thing, the museum. So when you're looking at the itinerary, then you can see what is sequential and what is parallel options.

01:52:24 - Brandon Hancock
I'm upset you didn't have this built for me months ago.

01:52:31 - Brandon Hancock
I'm going to need you to go ahead and give me a login to that, and I'll pay you whatever you need.

01:52:37 - Tiran Dagan
Yeah. We'll be in Chile in a couple of days. This is going to — I'm going to use it. Is it live?

01:52:43 - Tiran Dagan
Yeah, it is. It's SherpaCow. Yeah, it's a little buggy in terms of when you're searching for places. I still have to do kind of the locality — well, you know you're going to London, then you shouldn't have to type that you want restaurants in London, which you do right now. But it's completely tied into Google Map Services [tool:Google Maps API]. So if you want to add Chinese food in London — so it's got everything that you want.

01:53:24 - Tiran Dagan
<Q>Yeah, what does — so here's the hardest part for when we were going through — I'd be curious if SherpaCow has it — we were just like, we don't even know what's there, if that makes sense. Like, that was our problem.</Q>

01:53:34 - Tiran Dagan
<A>I didn't build that yet. So here, let's say I know I'm going to Asheville — so I pull up matches from Google Maps, but this needs a lot more refinement. It needs to have more kind of packages and maybe community-based recommendations. You know, you went on the call yesterday, and you had two folks who know Japan really, really well and immediately gave you some lists — so that's the future iteration: creating lists, sharing lists, et cetera. But it's a fun concept because — I'm finding that there are some other concepts that have more immediate monetization opportunities, so I'm focusing on them.</A>

01:54:24 - Tiran Dagan
And the last fun thing I'll show is — do you guys remember Picasa [tool:Picasa]? Does anyone use that? It was an amazing product. It was a client app, and it sat on top of any folder you wanted, and indexed your photos, and then Google killed it once they had Google Photos. So my brother — he's a surgeon — his daughter had her bat mitzvah, and he, unfortunately — you know, doctors think that they know technology — so he used ChatGPT [tool:ChatGPT] to try to build a website. And I was like, I don't understand what this is telling me to do and how to do it.

01:55:00 - Tiran Dagan
So it dawned on me — we're missing something like a Picasa. He had all of his photos in Dropbox [tool:Dropbox], so I went and did a one-day project — a photo gallery. Essentially, it erects a website for you from a folder that you have in Dropbox. So you just set up the Dropbox folder. It goes through all the photos and the folders and gives you everything in a folder. Dropbox API is extremely slow. So I tried doing this live on Dropbox — every photo took a second or two to load. So it goes through a process of caching in Supabase [tool:Supabase]. And then I'm using AI to do face recognition and automatic identification of faces using AWS Rekognition [tool:AWS Rekognition].

01:55:44 - Brandon Hancock
And then all he has to do is assign a name. So people that don't have a name come up as unknown. And then folks who are visiting the photo gallery can come in and say, I want to see all the photos that have Brandon in them, and boom, you're done.

01:56:04 - Brandon Hancock
That's wild. I love this. Dude, you are prolific — all of you guys — with the amount of cool things you guys are creating constantly. Like, this is my favorite part. It's just like, y'all bringing your ideas to life.

01:56:22 - Tiran Dagan
My favorite part is — I'm a woodworker and welder, so just last night, this 15-foot sculpture that I worked together with two artists came up. It's made from fishing nets. It's in Cape Cod, so it's got a whole nautical theme. And it's all made from fishing nets and parts. They just set it up yesterday.

01:56:45 - Tiran Dagan
But no, seriously — every part of that, awesome. So a few things just to say back to you. The travel planner — please — that is awesome. As soon as you get some of the recommendation stuff, because that's the biggest thing that we ran into. And then also the only thing I didn't mention is collaboration, because we have a group going — so it's just like, it will be so cool if we could share it. Because hey, that was a thing — like half the group knew what we're doing, the other half didn't, and it was hard to keep everything in sync. We had to do it in Notion, it was a mess. Those are like my only two customer feature requests.

01:57:33 - Tiran Dagan
To be radical — the features that came out through the ShipKit prompts blew us away. It was so — I'll talk about it once it's up and running — so groundbreaking, and it doesn't exist in the market. My partner — he's a serious prepper. I told you people hire him for big bucks to build their shelter. He's been doing this for 10 years, he's an ex-FBI special response agent response team, and it really blew him away how much brainstorming you can do with this.

01:58:13 - Brandon Hancock
<Q>Was this after the master idea? Just out of curiosity, which one?</Q>

01:58:16 - Tiran Dagan
<A>Yes, the master idea. And especially when it came — I'll share with you a little tip that worked really well. You know, you're expecting that someone's going to put into the prompts, dump their brain into it. What I did, since I already built a lot of features and I already had a PRD, I took the PRD into a new prompt, and then I took the questions that you're asking in ShipKit — one of the questions is: define who are you talking to and what problem are you solving for? So I asked the AI to answer that for my existing documents and then — so enriched it. Now I had these massive responses to plug in and I got some really fascinating results.</A>

01:59:08 - Brandon Hancock
What's really funny — so I love that. What you did, that meta-skill, absolutely crushed it. If you were to extrapolate — what's funny is how earlier we had that generate-critique pattern where the AI agents are doing it. Dude, you were just a critiquer. That's the cool part. You were forcing it to think and generate and you were saying, nope, again, again. Like, that is awesome.

---

<!--SEGMENT
topic: LinkedIn Outreach, Local Models & Developer Tooling
speakers: Brandon Hancock, Elijah, Patrick Chouinard, Tiran Dagan, Bastian Venegas Arevalo
keywords: LinkedIn Helper, Gemini CLI, Claude Code, Appify, local models, Qwen3, OpenCoder, Windsurf, Cursor, anti-gravity, Claude Code usage extension, B2B enterprise outreach, Whisperflow
summary: The group discusses LinkedIn automation tools (Linked Helper) for B2B enterprise outreach, Brandon's Gemini CLI-based parallel web scraping workflow for lead generation, and the upcoming plan to use Appify for LinkedIn data. Patrick recommends OpenCoder as an open-source Claude Code alternative for running local models like Qwen3. The session closes with discussion of IDE choices — Cursor vs. Windsurf (anti-gravity) vs. VS Code — and a Claude Code usage-tracking extension.
-->

01:35:17 - Brandon Hancock
And then, PH, just to go back to your question real fast on the CLI scraper you made. So once again, shout out to Patrick for opening my eyes to this. But basically, he was asking: can you explain the CLI scraper you made when I was a guest on the Google Channel? I saw the structure, but I didn't get what results would look like.

01:35:38 - Brandon Hancock
So what we were doing is we were basically trying to find all medical chiefs throughout America. That's what we were trying to do. So the workflow that I was doing is I created a seed file with the 500 biggest cities in America. And per city, I would kick off — so I would do Gemini CLI [tool:Gemini CLI] and pass in a prompt, and the prompt was basically like a long file of like: phase one, you find this; phase two, find this; phase three, verify this; phase four, analyze. And I would just pass that into Gemini CLI, which is at the end of the day an agent that has Google search. So I could end up kicking off 10, 15, or 20 deep searches per city, per time. So that's what I was doing.

01:36:34 - Brandon Hancock
Now I will say, even though it is Google search, it does not do things such as LinkedIn, which was the biggest obstacle where we ran into. So I'm going to be trying to do it again, using Appify [tool:Appify]. That's what I want to dive into next. It costs money to actually pull people's LinkedIn stuff, but I think it's going to be worth it. ▶ So I think what we're going to do is: step one, Appify, to get the list — probably pay between the amount of information we need, I think it's like $30 to do like an insane amount of scrapes — and then I'm going to, once I have the initial seed data with names, emails, profiles, I'm going to kick off Gemini CLI again to per person, go off and do a deeper search. So that's kind of what I'm going to be doing. And it costs like — it's very affordable.

01:37:31 - Brandon Hancock
And Patrick did say — I don't know if you were here at the beginning of the call — he did say actually using Claude Code was performing better, giving better results than Gemini CLI. So just — I haven't got to try it myself, but Patrick is the thought leader on this, and I was following what he was doing, and it worked great, and I'm excited to try it out with Claude Code to see if it does even better.

01:37:51 - Patrick Chouinard
Well, Claude Code works better. Costs more, but works better.

01:37:55 - Brandon Hancock
Yeah, hey, I got to put my max plan to the test, man. I got to have it work for me.

01:38:02 - Elijah
One thing there too, Brandon — I don't know if you've used Linked Helper [tool:Linked Helper].

01:38:07 - Brandon Hancock
Linked Helper?

01:38:13 - Elijah
Yeah, so Dawn, who's a part of the ShipKit Community — Dawn Davis, who's been working on the podcast. Yeah. So I've been working close with him. I brought him in here. He is the one that showed me that, so if you needed a tutorial on it, he uses it. He's got the number one life science podcast right now, and it does all the LinkedIn search help for him. He's got a whole automation that brings people into his podcast, does the research on them, tees it up for his podcast, and he just shows up. It's pretty cool.

01:38:41 - Brandon Hancock
I am literally sending this to my partner right now, because that is a very cool tool. Because my partner — he's kind of the face of the company, and he is the one doing those 20 LinkedIn outreaches.

01:39:13 - Brandon Hancock
Okay, yeah, thank you. And just quick heads up, guys — like, seriously, if you are going into enterprise land, where there are bigger deals, ▶ the best way is — it's a long play, but it's almost like a guarantee — the play is just over the course of a year, connect consistently with your desired target customers. Just throughout the year, connect with as many as you can, talk about the subject on LinkedIn, so whenever they do connect with you, like, oh, yeah, you are a thought leader. Don't ask instantly for, like, can I sell you this? Like, just — it's a long play, but, you know, if you're doing 20 invites a day over the course of a year, the amount of connections you're going to have with every single customer you want, it is unreal.

01:41:00 - Tiran Dagan
▶ Don't sleep on LinkedIn connections if you're going to go into a B2B kind of — yeah, B2B, but more specifically business enterprise or business to government — like just these connections are super invaluable. So it's just one playbook to have in your head to try all of them, but it's working out really well for us right now.

**Local models discussion:**

01:24:36 - Brandon Hancock
Real fast, I was curious, Patrick — you were dropping some model suggestions. I do think I want to try out a local model. Which one were you saying?

01:24:48 - Patrick Chouinard
Qwen3 Coder [tool:Qwen3 Coder], the second one you have on the screen there. But if they have maybe a 14B, because 32B will be a little bit big.

01:26:03 - Patrick Chouinard
For the one you were selecting, just check for maybe a smaller quantization. ▶ As long as it fits within your 24 gigs of RAM, you should be OK. It's not going to be fast, but it's going to work.

01:26:21 - Brandon Hancock
If y'all have any local models — Qwen or any other ones — I got space on my machine, so I want to put it to the test. So if y'all have any model recommendations or links you want to pass along, I'd love to see them.

01:26:39 - Patrick Chouinard
And actually install it through using OpenCoder [tool:OpenCoder]. It's basically Claude Code open source.

01:26:46 - Brandon Hancock
OpenCoder. Okay. Dude, all the recommendations. I haven't tried this one either. OpenCoder. I just want to make sure I'm grabbing the right one.

01:27:01 - Patrick Chouinard
Okay. It's basically, like I said, OpenCoder is basically Claude Code, but for open models.

01:27:08 - Tiran Dagan
Damn.

**IDE and tooling discussion:**

02:05:22 - Brandon Hancock
So just a teaching moment. So all that `cursor .` command is doing is just opening up Cursor [tool:Cursor]. Like, it doesn't do anything important. The command itself is basically saying, hey, Cursor, please open up this folder. That's all that's saying. Like, it's not doing any magic. So you could literally just open up Windsurf [tool:Windsurf] manually and say, open this folder. Like, there's nothing special about `cursor .`.

02:05:34 - Brandon Hancock
▶ What I do, and I would recommend everyone to do at this point — I'm using Windsurf as my editor. I use it for 10% of the time when I'm doing something visual. The other 90%, it's all Claude Code. That is my current work paradigm. And in the new video, the new workflow — the new worker SaaS walkthrough — you'll see me doing that, hopping between Windsurf specifically to use Gemini 2.5 Pro [tool:Gemini 2.5 Pro] with all the new cool tools they have, but 90% of the time, I'm just doing Claude Code.

02:07:10 - Brandon Hancock
Yeah, there's a really cool plugin for Visual Studio Code called Claude Code Chat [tool:Claude Code Chat]. So that gives you — if you're used to having that chat experience, it looks like a chat and it converts all the responses into structured boxes and buttons for you to click on.

02:07:34 - Tiran Dagan
Yeah, and Carlos Rojas — to answer your question — so I do not use Gemini CLI that much for actual development. I'm not a big Gemini CLI guy for coding. I'm just using Windsurf and that's how I'm getting access to Gemini 2.5 Pro.

02:08:00 - Brandon Hancock
And then the way — because I'm using Windsurf — Windsurf does their own memory management, so as you're working with the project, it's learning lessons about your coding style. So it's a little bit more agentic learning, so it's like a curve — to start off, you're not going to get the best results, but as time goes on, Windsurf gets smarter.

02:09:29 - Bastian Venegas Arevalo
Hey, I just wanted to mention that since you're using Claude Code in the IDE, I sent in WhatsApp a screenshot of an extension that's called like "Claude Code usage" or something like that. It should do exactly what you wanted to know — how much session time you have left and all of that.

02:10:01 - Brandon Hancock
Just to give people context real fast — so the issue I was wanting to look at is I wanted to know how much tokens I was using, because normally right now I'm typing in "usage" all the time to see where I'm at. But what I would love to do instead is just what you can use with status line. Everyone in Claude Code has status line. You can potentially set it up to where it will actually change stuff down here.

=== UNRESOLVED SPEAKERS ===

The following speaker names appeared in the transcript but were not present in the `SPEAKER_ALIASES` context block (which was not supplied in this session):

- **scottrippey** — passed through unchanged; likely "Scott Rippey" or similar
- **Glenn Marcus** — passed through unchanged
- **Ryan C** — passed through unchanged
- **Maksym Liamin** — passed through unchanged
- **George Kurian** — passed through unchanged
- **Ty Wells** — passed through unchanged
- **Tiran Dagan** — passed through unchanged
- **Elijah** — passed through unchanged (appears late in transcript, no last name given)
- **Carlos Aguilar** — passed through unchanged
- **Bastian Venegas Arevalo** — passed through unchanged
- **Juvenal A. Silva Jr.** — appeared once at 01:58:00 timestamp, no spoken content attributed; passed through unchanged