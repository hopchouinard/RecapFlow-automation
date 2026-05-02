=== SESSION ===
date: Unknown (transcript begins at 00:07:02)
duration_estimate: ~110 minutes
main_themes: OpenClaw/ClawBot AI agent framework setup and security, Claude Code deployment automation, app development showcases (fitness app, stock trading app, developer productivity tool), AI-assisted client delivery and value-based pricing, business consulting with AI, technical debugging (Drizzle DB, Sharp library, Vercel/Supabase multi-tenancy), AI agent memory architecture, enterprise AI adoption divide

---

<!--SEGMENT
topic: Hosting and Deployment Automation
speakers: Patrick Chouinard, Marc Juretus
keywords: Cloudflare, Railway, Google Cloud, Claude Code, Databricks, CLI, deployment, artifact repository, Vercel, headless automation
summary: Patrick and Marc compare hosting platforms and discuss how Claude Code can autonomously manage CLI-based deployments. Patrick demonstrates that Claude Code successfully deployed to Databricks without any prior human expertise in that platform, establishing a pattern of AI-managed infrastructure.
-->

00:07:33 - Patrick Chouinard
Hey, Marc.

00:07:36 - Marc Juretus
Hello. What's up, brother? How you doing?

00:07:38 - Marc Juretus
Good, good.

00:07:39 - Patrick Chouinard
Yourself?

00:07:40 - Marc Juretus
I can't complain. Another day in the books, if you will.

00:07:53 - Patrick Chouinard
Got to check out your page there. What do you got that hosted on? Is that on Railway or Cloudflare?

00:08:00 - Patrick Chouinard
Oh, Cloudflare? [tool:Cloudflare]

00:08:02 - Marc Juretus
Yep.

00:08:03 - Patrick Chouinard
▶ Free storage, free hosting, and a full API available through a CLI tool that Claude Code [tool:Claude Code] can manage by itself. So Claude builds it, Claude deploys it.

00:08:25 - Marc Juretus
I have two apps. I told you I have that fitness app, and I have a stock school app where basically they have to go in and take a series of three tutorials. Once they finish the three tutorials on different things about the stock market, they are given $25,000 of paper money to trade with. And it monitors their trades, and at some point the agent will analyze how they're doing, what they're doing, maybe get charts in there about reading charts and stuff like that. But the fitness app is all on Railway [tool:Railway], but the stock app is Vercel [tool:Vercel] front-end, Google Cloud [tool:Google Cloud] back-end.

00:09:02 - Marc Juretus
But yeah, I brought that up because the way you were saying how it was managing the CLI, it was doing that very well — the commands for pushing to the artifact repository and then up to the site.

00:09:25 - Patrick Chouinard
▶ So basically for me, any hosting I'm using, there has to be a CLI to manage it. I don't want to deal with the user interface because I want Claude to take care of it.

00:09:43 - Patrick Chouinard
Basically it runs the CLI as a tool in order to do the deploy and monitors the deployment also. So if there's anything that goes wrong, it can take it into account and correct it.

00:10:00 - Patrick Chouinard
I managed to get Claude Code to do a deployment on Databricks [tool:Databricks], and I've never used Databricks in my life. So Claude knew how to deploy on Databricks more than I did.

00:10:13 - Marc Juretus
Well, I saw somewhere that Elon was saying something to the effect where he wants software created and deployed without any user interaction. So don't know about all of that, but maybe at some point.

00:10:30 - Patrick Chouinard
Well, we're going to see. I'm definitely not going to wait on his idea to go forward.

---

<!--SEGMENT
topic: Claude Code vs. Cursor Comparison
speakers: Patrick Chouinard, Marc Juretus, Ty Wells
keywords: Claude Code, Cursor, Claude Sonnet, Claude Opus, Composer, terminal, coding assistant, model selection, IDE, comparison
summary: The group compares Claude Code running in the terminal versus using Claude models inside Cursor IDE. Patrick argues Claude Code is significantly superior to Claude-in-Cursor, while Marc describes a hybrid approach of using Cursor for lighter front-end work and Claude Code for heavier tasks.
-->

00:10:39 - Marc Juretus
Claude is definitely it, man. That writes some damn good code, man.

00:10:46 - Marc Juretus
It's like basically — I don't know if you have sodas up there — it's like Coca-Cola's Cursor [tool:Cursor], and that's like RC Cola or the store brand. Like, it'll get you by, but the other one will bring you home.

00:11:01 - Patrick Chouinard
▶ And honestly, Claude in Cursor is good, but Claude in Claude Code is miles ahead.

00:11:11 - Marc Juretus
<Q>Now, when you say that, I'm using Cursor, but I'm using Claude inside of my terminal. What do you mean when you say that?</Q>

00:11:20 - Patrick Chouinard
<A>When I mean in the terminal, you're using Claude Code.</A>

00:11:25 - Marc Juretus
You were saying Claude in Claude Code, and I was like, oh, is there now?

00:11:28 - Patrick Chouinard
No, what I mean is in Cursor, you can select Composer, but you can also select Claude Sonnet [tool:Claude Sonnet] or Opus [tool:Claude Opus] in Cursor. And yeah, they're good, but not as good as Claude Code.

00:11:43 - Marc Juretus
But if I've got some front-end stuff that I'm working on, I'll be like, all right, I've used up all my Claude time. Let this Cursor stuff handle a little front-end Next.js stuff while we're doing that.

00:11:55 - Marc Juretus
Hey, Ty.

00:12:00 - Ty Wells
Hey, guys. Hey, Patrick. What's going on?

00:12:08 - Patrick Chouinard
Just doing what I do. Just hoping that Paul will join us. He's supposed to be hosting tonight.

00:12:16 - Ty Wells
Oh, he's pushing it to the wire.

---

<!--SEGMENT
topic: OpenClaw Bot Overview and Use Cases
speakers: Patrick Chouinard, Ty Wells, Marc Juretus, Scott Rippey
keywords: OpenClaw, ClawBot, Anthropic, Telegram, Discord, memory, SQLite, soul, identity, skills, agent framework, security, Raspberry Pi, Proxmox
summary: The group introduces OpenClaw (formerly ClawBot), an open-source AI agent framework. Patrick and Ty describe its architecture — memory stored in SQLite, identity/soul Markdown files, and skills — and share personal use cases including traffic monitoring, automated invoicing, and project management. Security concerns about the out-of-box configuration are raised prominently.
-->

00:12:27 - Ty Wells
<Q>What are you working on this week, Patrick?</Q>

00:12:31 - Patrick Chouinard
<A>Well, I'm still working on OpenClaw [tool:OpenClaw], but I'm not to the point where I have new stuff to showcase. Basically I'm rebuilding my instance because I've gone through the whole security aspect. Now I'm going through the functionality aspect, and I've decided to go from Telegram [tool:Telegram] to Discord [tool:Discord] — a dedicated Discord server where I have multiple channels so I can split the conversation, meaning my context window is going to be a lot cleaner. It can be dedicated to certain subjects. And I want to work on a special new layer of memory per channel on top of the global memory.</A>

00:13:20 - Ty Wells
Yeah, that shared memory is great, but that individual memory keeps it context-aware.

00:13:28 - Patrick Chouinard
▶ The shared memory for the personality, the identity of the assistant; the channel-specific memory for whatever task that channel is specialized in; then the context for my memory.

00:13:45 - Marc Juretus
<Q>When you say OpenClaw, I'm assuming they refactored the name from ClawBot to that?</Q>

00:13:51 - Marc Juretus
I was going to say, what the hell is OpenClaw? I knew they were changing their names, so that kind of lined up.

00:13:57 - Patrick Chouinard
Yeah, it was ClawBot. OpenClawBot. But the fact that it was started as Clawed, C-L-A-W-D, but Anthropic [tool:Anthropic] sued them. So that's why they went to another name, but for some reason it didn't stick. So now they're OpenClaw.

00:14:22 - Marc Juretus
I think the creator — was she just on 60 Minutes? One of the ladies from Anthropic.

00:14:40 - Patrick Chouinard
I mean, it's one of the hottest agent frameworks on the market, and it's been coded by someone in his basement, basically.

00:14:49 - Ty Wells
No, he was on the scene. He stepped away. He came back. He used to develop — he had, I forget the name of the tool he had, when he got burnt out. And then he left, and he hadn't done anything for years. And then he came back.

00:15:10 - Patrick Chouinard
He developed it himself. He doesn't have a company behind it.

00:15:11 - Ty Wells
Oh, he's got a company now. And there are other companies that are growing off of it.

00:15:27 - Ty Wells
There is actually a security link — let me see if I can paste that in — where you can check your bot. [link:security check tool for OpenClaw bots — URL not captured]

00:15:35 - Ty Wells
But I went away from the skills. I created my own — I call it Secure Claw. I just build the skills as I need them.

00:15:43 - Patrick Chouinard
Because I'm trying to load skills in, and they come from people you don't know.

00:15:47 - Patrick Chouinard
▶ I always have the bot create the skills. So there's nothing external they can inject anyway.

00:16:00 - Marc Juretus
It's one of those things like that nightclub in the bad area. Let me have a couple of my friends go there before I start attending. I don't see a need for using ClawBot right now. I'll let people iron out the hells of it — getting access to something they shouldn't — and I'll come in later.

00:16:22 - Patrick Chouinard
You don't think you have use cases because you haven't used it. The moment you do, use cases will pop out of everywhere.

00:16:31 - Marc Juretus
<Q>Well, give me one off the top of your head that it suddenly opened up for you, Patrick.</Q>

00:16:37 - Patrick Chouinard
<A>For me, right now, it's monitoring traffic in Montreal live. And every morning it decides if it's going to send me an alert to wake me up if the light rail system is disrupted. Because if it does, then I have to get up an hour earlier in order to get into the office at the right time.</A>

00:17:01 - Marc Juretus
<Q>So my question would be — what is that doing that APScheduler [tool:APScheduler] wouldn't do?</Q>

00:17:07 - Patrick Chouinard
<A>It verifies the different information points. So it gathers the information and it makes the decision to say, "This is going to slow him down in half an hour" — not "right now traffic is bad." Because that's the problem. When that screws up, it's not an immediate effect. It's a compounding effect. But I need to react before it compounds.</A>

00:17:33 - Patrick Chouinard
All of the ideas I have, I just send to my assistant. It has its own GitHub repo [tool:GitHub] and its own GitHub project. So it manages the project. It creates the tasks in there. Every morning it sends me a list of projects that it thinks would help me based on everything it knows, plus all of the work we're doing together every day. I can choose one of the projects, assign it to the assistant, and it starts working on it.

00:18:04 - Patrick Chouinard
▶ I've started to allow it access through a headless version of Claude Code so it can use Claude to start coding for it as a tool.

00:18:17 - Patrick Chouinard
So yeah, there's metric tons of scenarios you can think of, because it's always there and you can tell it to start working on something and it's going to iterate until it comes up with a solution, no matter what it is.

00:18:35 - Marc Juretus
I have a bunch of stuff kicked off with APScheduler, like stock updates and this and that.

00:18:40 - Patrick Chouinard
<Q>Yeah, but midday, can you tell it, "Oh, now stop looking at that, but start looking at this signal," and it reconfigures itself for the next day?</Q>

00:18:53 - Marc Juretus
<Q>How are you making that jump to make it do that? Are you using some type of conditional that it's reaching?</Q>

00:19:00 - Patrick Chouinard
<A>No, I just send it a text message.</A>

00:19:08 - Ty Wells
Yeah, Marc, you need to look into it. Seriously, what you describe — what you're doing now with that scheduler — you would 10x the ability with that, because that's a use case. I use it: I send invoices out at the end of the month. I've got to check my credit card, check my different provider accounts to determine what to charge clients. I have it do all that for me and generate the invoice. It drafts the bill, the invoice, and sends me a message in Telegram and says, "Hey, does this look good? Should I send it?" And I'd say, "Yeah, send it off." Or I'd say, "Add this other cost that I forgot about," and then it sends it off.

00:20:11 - Marc Juretus
<Q>So did you do that with the Claude Ask tool and have an interview to get to that point?</Q>

00:20:17 - Ty Wells
<A>No, that's just inside of OpenClaw. It has what's called memory — great memory. It stores it in a SQLite database [tool:SQLite]. It has a soul, which is more of its persona — what it is and how it works. And what's the other one, Patrick?</A>

00:20:47 - Patrick Chouinard
Identity, I believe.

00:20:52 - Ty Wells
Identity, yeah. It's all Markdown files. But basically, you build this person, if you will. And it then has all of the tools that it needs to go do the things that you would do.

00:21:07 - Ty Wells
▶ So like Patrick said, go find the traffic data, what's available — and the more you give it access to do those things, like API keys and stuff, you could probably just give it an Apify [tool:Apify] key because that's loaded with different tools, and then it has access to build and code. It's a definite change in the game. There's no going back.

00:21:44 - Patrick Chouinard
Now I'm using Discord. I used to use Telegram, but multiple group chats for multiple subjects — it's not the easiest environment.

00:22:00 - Marc Juretus
I prefer a Discord server with multiple channels so I can split my discussion with my assistant.

00:22:07 - Ty Wells
I just created multiple Telegram groups. It's possible.

00:22:12 - Patrick Chouinard
I just prefer the Discord environment. But the idea is to split your conversation, basically.

00:22:22 - Marc Juretus
<Q>So did you buy another computer for it to run?</Q>

00:22:24 - Patrick Chouinard
<A>Well, I already had a Proxmox [tool:Proxmox] server running virtual machines, so I just started an additional VM and that's it.</A>

00:22:40 - Marc Juretus
One of you guys, send me a video of where to start. Like, what's the one that's worth a damn to start?

00:22:53 - Scott Rippey
▶ Just make sure you find people that talk about security, because most of the internet screwed themselves over.

00:23:01 - Scott Rippey
Yeah, I saw that one influencer I follow — he ripped the hell out of that. It was going over some telnet port or something that was getting in. It's just something that went viral when it shouldn't have — meaning it shouldn't have been for the general public.

00:23:19 - Scott Rippey
▶ It's really not meant for the general public because there's no documentation on how to do almost anything with it. People are like, "Let's go," and then they give it access to the world.

00:23:31 - Patrick Chouinard
It's like, here's my credit card, here's my crypto wallet, have fun.

00:25:32 - Patrick Chouinard
By the way, if you really want to, it runs on a Raspberry Pi [tool:Raspberry Pi].

00:25:39 - Jake Maymar
The only problem is on the Raspberry Pi, it gets unresponsive.

00:25:44 - Patrick Chouinard
Obviously, it's not going to be the most powerful thing in the world, but it does work.

00:25:56 - Jake Maymar
You just have to nudge it. It has a heartbeat, but you just kind of have to nudge it.

00:26:09 - Jake Maymar
▶ Just be careful with the security thing. My friend actually gave it some permissions, then tried to erase them. Seemed like it was fine. And then it started finding a way around. And it got into all the stuff it shouldn't be in and changing stuff that he didn't realize it was changing. So yeah, just be aware. It's very intelligent.

00:26:58 - Ty Wells
Yeah, it's persistent in completing its goals.

00:27:05 - Scott Rippey
Did you guys hear about they were creating social networks and it was posting their users' information because they got mad?

---

<!--SEGMENT
topic: Marc's App Demos — Fitness and Stock School
speakers: Marc Juretus, Patrick Chouinard, Ty Wells
keywords: fitness app, Stock School, Railway, Vercel, Google Cloud, FinHub, paper trading, Grok, AI trainer, Next.js, Python, Supabase, Klerk, Docploy, Auth0, WorkOS
summary: Marc screen-shares two apps he has built: a fitness app with an AI trainer persona (drill sergeant, motivator, nice guy) and AI-generated workout videos via Grok, and a Stock School app with real-time FinHub data and paper trading. The group then discusses authentication and database alternatives to Supabase, including Klerk and Docploy.
-->

00:28:29 - Marc Juretus
So, basically, this is my fitness app. That's me, my little caricature. This is basically on Railway. It's Python back-end, Next.js [tool:Next.js] front-end. So I built little stuff in — because I work out at 5 a.m., so I'm kind of out of it in the morning. Sometimes I just pull three random exercises for each. But I'll show you the AI aspect of it.

00:29:55 - Marc Juretus
The AI aspect of it is — I did make the chat thing where you're asking a trainer, and I'm giving you three levels: a nice guy, a motivator, or a drill sergeant. And basically if you say to the drill sergeant, "I'm tired, I don't want to work out," it'll come back with a response.

00:30:36 - Marc Juretus
And then the other thing I got in is — they are so gonna replace us — these are all my exercises. But the thing that just blows me away — hopefully this will load — that's not even me, that's from Grok [tool:Grok]. So I'm generating my own videos for workout suggestions with that.

00:31:01 - Marc Juretus
So that's the one app that I'm working on. And then the other one I got is called Stock School. The premise of this one is basically you come in here, you take three of the tutorials that I give you. Once you finish all three levels on basics of stocks, I give you $25,000 in paper money. And then at that point, you can invest wherever you want. And then at some point, I'll have an agent analyze all your trades, what you did, and do some charting with the candles and stuff.

00:31:46 - Marc Juretus
Here's your market data. This is coming from FinHub [tool:FinHub]. This is real time. And like, now I have $19,000. So let's invest in, I don't know, Microsoft. So I can come in here and buy 10 shares.

00:32:18 - Marc Juretus
So I'm building these two apps right now. The first app is all Railway. This one is a Vercel front-end and a Google Cloud back-end.

00:32:29 - Marc Juretus
<Q>Maybe the only question I'd have for the group is — was it Paul or somebody else that were using something outside of Supabase [tool:Supabase]? Because I've been trying to taste a couple of things that maybe I could use outside of all the framework stuff I've been using. Is there another one that's similar to it?</Q>

00:32:49 - Paul Miller
<Q>So are you talking for authentication?</Q>

00:32:52 - Marc Juretus
Yeah, for authentication, and I have my Postgres databases on Supabase as well.

00:32:58 - Paul Miller
<A>Maybe get into Klerk [tool:Klerk]. Klerk's pretty good on the authentication side of things. It's really elegant, and the free tier is really capable. And then I use Docploy [tool:Docploy] to manage the hosting side of things. Then I can just run up a Postgres database, which is basically all running on Docker [tool:Docker], but Docploy's like an interface to manage all your Docker deployments and security.</A>

00:34:44 - Patrick Chouinard
And I see two recommendations — WorkOS [tool:WorkOS] and Auth0 [tool:Auth0] — with the other ones. Anyone want to talk a bit about those?

00:34:55 - Marc Juretus
Auth0. I've never heard of that one.

00:35:57 - Marc Juretus
The stock stuff here is in real time with a service called FinHub, I think it is, with an API. It's pretty up-to-date stock data, oddly enough.

00:36:02 - Marc Juretus
▶ You can use your OpenClaw to go out and keep you right up-to-date, and you say, "Do this," it'll do that. You lay your conditions out, and it'll do those things for you.

00:36:08 - Marc Juretus
That video of me just blew me away. I'm like, are you kidding me, man? Like, I don't even need to record videos. I was expecting it to look like some half-assed thing from the mid-90s, but Grok is pretty damn good, man.

---

<!--SEGMENT
topic: Scott's Clarity Developer Productivity App
speakers: Scott Rippey, Patrick Chouinard, Marc Juretus
keywords: Clarity app, GitHub sync, Anthropic API, Claude Sonnet, Remotion, Suno, Stripe, Context7, Google Calendar, time blocking, prompt generator, project management, dev branch, Supabase
summary: Scott screen-shares his Clarity app — a developer-focused tool combining GitHub codebase Q&A, AI prompt generation with Context7 integration, meeting note ingestion, and Google Calendar time-blocking. He describes the monetization model using Stripe with tiered AI usage credits and discusses plans for beta testing with friends.
-->

00:36:24 - Scott Rippey
Well, I suppose I can just give a little screen share and update on that developer Clarity app I was working on. It's pretty much the only thing I've been living in for a little while.

00:36:48 - Scott Rippey
So I've got this one now to where I actually have it set up with a dev branch and a whole work tree and a separate copy of the database, which is nice because I actually integrated some other stuff. Now I want to be able to do development and fork on this thing and then merge it to main when I want to put stuff in here.

00:37:08 - Scott Rippey
I've actually used Remotion [tool:Remotion] to create this video, which is a really cool repository. If you guys ever want to check that out, you can create from prompts these animated videos, and it's feeding it information from my application. And it's just a nice little — you create some music in Suno [tool:Suno] and then put it together really, really fast and easy. Like this was made in like five minutes for this application.

00:37:35 - Scott Rippey
But basically what I'm trying to do is combine, for developers, code-based context, where we have a GitHub sync, you can ask questions across your code bases. And I have a prompt generator thing that I've made as a Claude project that now lives in this. That's really built for Claude Code — to help you put natural language in and then create really structured prompts, and it's checking some Context7 [tool:Context7] stuff.

00:38:02 - Scott Rippey
But now it also has access to — when you sync your GitHub projects, you can create these things and sync them in here. I have it automatically pulling the documentation that's in Git. And so all of these are available to the prompt generator. So it actually knows more about your project when you're creating your prompt.

00:38:23 - Scott Rippey
So you can ask Clarity a question about this project, and this is all using the Anthropic API [tool:Anthropic API], and then the generate prompt does that. You can actually go to Ask Clarity and ask questions across the entire code base.

00:38:40 - Scott Rippey
What I haven't tested yet — because I've got to start some of these projects for clients — is where you can also import documents. I want to combine, like, if you're in a project, it needs to know what decisions or action items or open questions are there. Because I want to be able to dump in meeting notes and have it actually analyze what to have in here.

00:39:17 - Scott Rippey
So I'm trying to combine both worlds — developing and then planning and project coordination. And then something more recently that I kind of got into was this time-blocking thing, where you can actually see what open items are, connect your Google Calendar [tool:Google Calendar], and see your projects. And then if you have open items, it should start suggesting work times based on your calendar and when you have time blocks — just something to help organize when to work on projects.

00:39:53 - Scott Rippey
The other thing is on the dev branch, I do have all this working with Stripe [tool:Stripe] too, so I can use test mode for the dev branch. I've got two plans. ▶ At $20 a month, you get $13 of AI usage. At $50 a month, you get $35. So I make a little money off it for the hosting and everything else. But then beyond that, you can do a little top-up pack — if you run out, you can just buy $10 increments.

00:40:26 - Scott Rippey
But it's pretty efficient. Even with Sonnet, it's not a huge, heavy AI usage. You can do quite a few things manually as well.

00:40:35 - Scott Rippey
I've got more testing to do. I've tested most things. I just haven't tested a lot of the import on the project side. And I've got to refine the time blocking. But yeah, I want to start with some friends and then eventually may roll it out wider.

00:40:57 - Patrick Chouinard
Very, very nice. The time-block functionality would be a godsend, obviously.

00:41:06 - Scott Rippey
▶ Any one of us that gets busy enough knows that we start squirreling. Yeah.

---

<!--SEGMENT
topic: Ryan's Projects — Social Platform, E-commerce, and Client Work
speakers: Ryan C, Patrick Chouinard, Scott Rippey
keywords: social platform, e-commerce, WordPress migration, US Postal Service API, label printer, N8N, Bolt, Claude Code, thumbnail optimization, MailChimp, NAN credits, London taxi booking
summary: Ryan describes multiple concurrent projects: a social platform he's patching post-launch, a complex e-commerce migration from WordPress with USPS API and label printer integration, a London taxi booking system, and several informational websites built rapidly with Bolt and Claude Code. Scott advises using a self-hosted N8N instance to reduce costs for the email marketing component.
-->

00:41:47 - Ryan C
I've finally got the social platform up and running, and as the first client stuff's been happening, I've been catching bugs and things that would only come up through actual client use. I've tried to test all the different scenarios I could think of, but as you always do, missed stuff. So nothing major yet, thankfully. I've just been patching stuff.

00:42:20 - Ryan C
I realized it was loading all of the raw images every time, and as I've uploaded more and more stuff into it, it's getting slower and slower. So I did a massive patch yesterday which replaced all of the stuff with thumbnail renders — so it compressed them, I had a compressed version of all of it, that just loaded into the media bank. So I've sped it up considerably.

00:43:00 - Ryan C
I've got a big e-commerce website with a whole mailing piece and an orders piece, and I need to write some integrations for a label printer, and then I need to write an integration for the US Postal Service [tool:US Postal Service API] and a whole bunch of other stuff to print the labels and to pull the labels out to pay for the postage. All of that stuff. So there's a shed load of complication. The back end is going to be fun to build.

00:43:30 - Ryan C
And then I've got a very similar one, but for a black cab taxi private tour for London — that I've got to build, which will be a booking system, and then a whole CMS back end for him.

00:44:00 - Ryan C
You do informational websites nowadays, and you get the brief from them, and you're like, right, well, that's one prompt into Bolt [tool:Bolt], and that's pretty much the website done, and then just a bit of refinement in Claude Code doesn't need anything more than that. ▶ If you get the Bolt prompt right, just tighten it up, secure it, and make sure it works, and upload it. So I have to sit on it for two weeks to make it look like I've done something, and then I do it in about half an hour.

00:44:42 - Patrick Chouinard
<Q>Anything we might be able to help you with this week?</Q>

00:44:46 - Ryan C
<A>I'll probably want your help when it comes to integrating the US Postal Service stuff, because that feels like the bit I'm the most uncertain about. They've got an API and everything, but it looks really complicated, and then I've got to try and make it work with a printer as well. And printers — I hate printers more than anything else in the world. And obviously I'm in London, so I don't have physical access to this thing to test it.</A>

00:45:27 - Patrick Chouinard
Good. Keep us appraised. I'm anxious to see your e-commerce system — that's some type of my old world.

00:45:38 - Ryan C
Yeah, I used to build — it's currently on WordPress [tool:WordPress], and it's a mess. So I'm going to pull everything out of that product-wise, so I don't have to recreate all the products. I'm going to create a whole admin back end for them to be able to administer that, and then a whole email system for when they do promotions that just emails their mailing list.

00:46:00 - Ryan C
Through N8N [tool:N8N], and that's going to be a $1,000 a month running cost for them, because it's going to be thousands and thousands of emails going out, so those N8N credits are going to go through the roof.

00:46:37 - Scott Rippey
Hey Ryan, remind me of one of our conversations coming up. When you get to that point — since you're going to be administering this whole thing for them — you're probably going to want to not do the cloud N8N for them. ▶ Actually do the free local instance and secure it on something virtual, because then you can get around all that usage cost for the cloud model. That'll make really a lot of sense for your particular use case.

00:47:00 - Ryan C
Let me know when you've got a minute to squeeze me in, Scott. I know you've got a mental week this week. That'd be appreciated, because that again is an unknown for me — I'm essentially building a MailChimp [tool:MailChimp] into the back end of their website.

00:47:16 - Scott Rippey
▶ And you'll do it the same as you would in cloud N8N — it's just that it's going to be installed locally on a virtual environment. There are a lot of good hosting options out there that work well with N8N, that are secure, that you can do that and get around that extra cost.

00:47:30 - Ryan C
Love that. Lower costs is always a win.

---

<!--SEGMENT
topic: AI-Accelerated Client Delivery and Value-Based Pricing
speakers: Jake Maymar, Ryan C, Scott Rippey, Paul Miller, Patrick Chouinard, Marc Juretus
keywords: Jira, Claude Code, value-based pricing, MVP, critical path, client management, unit tests, project delivery, business consulting, AI productivity, scope management
summary: Jake describes completing months of Jira-tracked bug fixes in 30 minutes using Claude connected to Jira, shocking his client who expected a multi-month timeline. The group debates the ethics of delivery speed versus perceived value, converging on value-based pricing as the right model. Paul expands this into a broader consulting philosophy: use AI-generated savings to invest in deeper business process discovery rather than just faster coding.
-->

00:47:48 - Jake Maymar
I kind of wanted to pull on the string a little bit for what Ryan was saying. It's an interesting world that we can accomplish things in 30 minutes that would take months to do.

00:48:00 - Jake Maymar
One of my clients — we were going back and forth, and he's like, well, I don't know, there's something like a thousand different bugs and issues and features that he had in Jira [tool:Jira], and he's like, "But you have to basically do all of these." And I was like, "Okay, no problem." And I basically connected Jira to Claude, and went back and forth, and identified some of them — I'm not kidding, I think it was 30 minutes — and it was done. And I was like, oh my god. So of course, I ran all the unit tests and everything, and I have all the stuff that does unit tests automatically. And then I just didn't believe it, so I went through and eyeballed it and manually checked everything. It was done.

00:49:12 - Jake Maymar
And then I was like, well, now I'm confused. So what do I do? Like, do I sit back, wait a couple of days, then tell him it took the full two days to do it?

00:49:29 - Ryan C
That's what I've been doing. "Oh, I've been working nonstop at this. Have a look at this beautiful website I've just built for you." It didn't take me half an hour about two days ago. Enjoy.

00:49:43 - Patrick Chouinard
Yeah.

00:49:45 - Scott Rippey
One thing that'll teach you as you start realizing some of this — Ryan and I were learning this in the video world too — ▶ you start getting into value-based pricing. It's not really based on the time, it's based on the value of the solution and setting those expectations up front. Then you don't get caught on the, "Crap, now I've got to fake like it's taken me days or weeks."

00:50:04 - Ty Wells
Yeah, I agree with that. It's a great point, Scott.

00:50:09 - Jake Maymar
My stuff is value-based, right? So I'm doing value-based stuff, but he thought that he didn't have to pay me for several months. And I basically pushed the changes, and we're on chat, and he chatted me like, "What?" Because he was expecting that was going to be months of work, and so he thought he had just created a buffer for payment. And then we went back and forth, and he's like, "Yeah, that's amazing. I didn't even think that we could do that." And because I connected it to the Jira, it fixed things that he didn't even know — basically backlog things and other things.

00:51:00 - Jake Maymar
It would have taken me months, if not several months, to do that kind of stuff. And it's just tedious too.

00:51:18 - Marc Juretus
You over-delivered, man. I would have laid that stuff out in little dribs and drabs.

00:51:33 - Paul Miller
The opportunity on that is — can you go back to him and say, "Rather than us focused on these very specific problems, can we sort of just go into a little bit more scope around the business things?"

00:52:00 - Paul Miller
I got this big one a week ago Friday — potentially huge. This company had an old-fashioned dev house, a whole bunch of Microsoft coders, BAs, SAs. And the customer goes along and says, "Look, we want to build a custom app. We want to own it, and we just want it to be wonderful. We're manual at the moment." And when they asked the dev house, "Can you do AI, can you use AI and make it better?" — they said, "Oh, that'll be extra." It's like, for a moment, why aren't they developing with AI?

00:53:34 - Paul Miller
So they ended up coming to me. And I said, "No, we'll develop with AI, but it still needs the same effort in doing the original scoping. But the savings — we're going to invest back into your business side of things and really challenge the way you do your business process stuff."

00:54:05 - Paul Miller
This other crowd paid that 1990s business, they scoped everything. They had BAs, they looked at every process, and it was all in an electronic document. And they said to me, "Oh, this is obviously a waste of money." And I said, "Well, no. This is actually, in 2026, this is the gold. The coding part is the cheap part."

00:54:25 - Paul Miller
▶ What I think we should do is let's step back and say, "OK, if this is a good map of what you should potentially have — these people don't understand AI — let's think about those steps, revalidate those steps, and talk about how we can make this incredible."

00:54:54 - Paul Miller
<Q>But is that an opportunity for how you're engaging with your one, or some of the other ones that come along?</Q>

00:54:59 - Jake Maymar
<A>And actually, it was kind of why I sped up the timeline. Because we were just getting lost in little change after change after change. And I was like, we are missing the critical path. Like, you have a deliverable. We have already signed clients. The clients have prototypes that they're working on, and he had all these changes. And I honestly think, in some ways, he was getting scared — thinking, "What's going to happen when they get in and they start using this and it doesn't work?" And I'm like, "Well, we then refine, right? It doesn't work off the bat. That's how MVPs work."</A>

00:55:46 - Jake Maymar
But you're right, Paul. Stepping back and understanding the business case and the strategy around it. I think we're going to start wearing different hats — understanding the business case and the strategy, and less about the code.

00:57:06 - Patrick Chouinard
<Q>Am I correct to assume, hearing you, that you have a good idea what the critical path actually is? You're just wanting him to say it?</Q>

00:57:19 - Jake Maymar
<A>Patrick, that's kind of how I work — I make it so that the client, it's their idea, right? And they get really excited about it, they get buy-in. But the problem is, with this particular client, they change their mind. They wake up in the middle of the night, and they get nervous, and they change their mind. And so I've been trying to come up with systems that basically bypass that.</A>

00:59:15 - Patrick Chouinard
Actually, what Bastien just said in the chat makes a lot of sense. It's his final question: "How does that make me look good inside my company?" Is really it. That's what you need to get him to think about.

00:59:38 - Patrick Chouinard
▶ It's always ego in some form or another.

---

<!--SEGMENT
topic: OpenClaw Security Architecture and Isolation Strategy
speakers: Patrick Chouinard, Jake Maymar, Ty Wells, Scott Rippey
keywords: OpenClaw, NanoClaw, security isolation, blast radius, AWS, virtual machine, identity separation, Gmail, GitHub, API key caps, Telegram, WhatsApp, FreshBooks, invoicing, SQLite, soul, heartbeat
summary: Jake raises concerns about OpenClaw's security maturity, prompting Patrick to articulate his "blast radius" isolation philosophy — giving the agent its own separate identity, capped API keys, and sandboxed accounts. Ty describes building his own Secure Claw variant on AWS, replacing FreshBooks with a custom invoicing system. The group recommends NanoClaw as a simpler starting point and emphasizes building custom skills rather than loading untrusted ones.
-->

00:59:46 - Jake Maymar
I really want to understand how you guys are using OpenClaw and all these different things. I can see a lot of hype, but I'm also seeing it very effective. I'm not currently using it as much as other people are, because I'm still nervous and I don't feel it's hardened enough.

01:00:15 - Patrick Chouinard
<A>It's never going to be hardened enough. That's why you have to isolate it — isolate the hell out of it. Because I'm never going to trust that that platform will be truly hardened, because in order to be efficient, it has to be somewhat open. So it's for you to build a bubble, a secure bubble around it.</A>

01:00:52 - Patrick Chouinard
▶ I treat it as a co-worker. A co-worker — I can trust that it has good intention because we're working together, but I have no way to trust that it's going to be secured and it's not going to make a mistake. I treat OpenClaw the exact same way. It has its own identity, its own Gmail account, its own calendar, its own Google Docs, its own Google Drive, its own GitHub account. I created an identity for it.

01:01:35 - Patrick Chouinard
So yeah, it can screw up, but only within the blast radius I allow it to have. ▶ If it needs an API key, I'll create an API key with a very strict cap for it to use. So yeah, if it publishes it on the web by mistake, it's going to burn five bucks. Whatever I give it — even if it was published — the blast radius would be as small as I can make it for it to still be operational and useful.

01:02:10 - Jake Maymar
That makes a lot of sense. So I'm sure it's evolved a lot, Patrick, from when you first started.

01:02:46 - Patrick Chouinard
There are multiple releases per day at this point. So yeah, it evolves a lot. But again, I'm not trusting the core to be secure. I will always think of the core as unsecure. That's why I isolate it at multiple levels.

01:03:19 - Ty Wells
Yeah, Marc, you can use it to do the things you were talking about — go out and give you stock reports every day. It would obviously be able to do that with a skill.

01:03:28 - Ty Wells
I was on FreshBooks [tool:FreshBooks]. That's why I do my invoicing. And so I decided, well, I don't really need FreshBooks — that's $38 a month. ▶ Why don't you just build me a FreshBooks? And so I had it build me an invoicing system with all the features that I wanted, which was really just invoicing — clients, products. And then I had to take all the data in my FreshBooks and figure out what my invoices should look like, what they typically look like, which services to go hit, all of that.

01:04:10 - Ty Wells
But that's using my Secure Claw. I created my own. I used some of the framework — like we talked about earlier, the heartbeat, the identity, the soul. I created it based off of that, because that structure is architecturally really good. But obviously, security-wise, yes, it was horrible out of the box.

01:04:46 - Ty Wells
There's also another one out there called NanoClaw [tool:NanoClaw]. That's just an easier starting point, where it doesn't have any of the security, but it doesn't have the massive amount of capability either.

01:05:00 - Ty Wells
▶ But I would say build your own — simply take the NanoClaw and the OpenClaw and have Claude put together a secure version of this with these features. I only wanted Telegram and WhatsApp, I only wanted whatever, right? And then you do, like Patrick did, which I did also — give that identity a separate, secure, sandboxed guest. Don't give them your real identity and stuff. And of course, mine's secure on AWS [tool:AWS] on a lockdown machine. I can only get to it through a Telegram bot.

---

<!--SEGMENT
topic: Paul's Logistics Client and Business-First AI Consulting
speakers: Paul Miller, Jake Maymar, Ty Wells, Patrick Chouinard
keywords: logistics, supply chain, business discovery, AI consulting, deep research, value-based pricing, SaaS, recurring revenue, sales process, AI adoption, enterprise, digital transformation, applied AI
summary: Paul describes signing a significant logistics client and articulates a "business-first" consulting philosophy: use AI-generated development savings to fund deeper business process discovery rather than just faster delivery. Jake and Ty affirm this, with Ty coining the term "intelligent architects" for the emerging role. The group discusses how to position AI consulting credibly against skeptical enterprise buyers.
-->

01:06:03 - Paul Miller
Yeah, so pretty quiet on my side, other than signing up this very interesting client. So getting my head around it — it's about using resources away from traditional dev challenges and putting it more back in the business discovery.

01:06:40 - Paul Miller
The guys I'm working with are in the logistics space. It's pretty boring stuff if you look at it from a general perspective. But I geek out on that kind of thing because I've always been involved with supply chain and supermarkets and products and getting that stuff around. If you look at it from a commercial sense, these types of industries really just have to happen. It doesn't matter what happens to consumers. People still have to eat. Containers still have to go backwards and forwards, whether it's domestically or internationally.

01:07:32 - Paul Miller
▶ And if people feel that you're focused on solving specific issues in their space, and you're very focused on that — and hey, the other side of AI is doing the deep research, knowing who the competitors are, knowing the top issues holding back the company you're about to talk to, and just happen to talk about that when you come in — that's powerful.

01:08:00 - Paul Miller
▶ We're not an AI-first business. We're a business-business-first. Give them comfort that you understand the business problem rather than the AI-cool stuff. They want the AI-cool stuff, but they want to know you understand the business problem first.

01:09:00 - Paul Miller
My most practical concern at the moment is not trying to do all of this myself. I'm kind of so addicted to the fact that I can make anything, that I just want to sit around my home machine with its massive screen and just make all sorts of cool stuff. But I need to contain myself, get out there, and take my little gold pan to get all the bits of gold that are sitting out there.

01:09:49 - Paul Miller
It's really out there. And people are looking for the answers, but they're skeptical of a lot of people selling the bulls**t. And most of us here are well-experienced in our fields — we've got deep technical understanding or product understanding in the industry verticals where we've got credibility.

01:10:26 - Paul Miller
I'm simultaneously, while I'm on this call, having a play with some random idea I had last night and I want to see how easy it is to code it. But I'm trying to restrict my ideas to repeatable things that I know customers have asked about — like automated inbound/outbound calling, or clever things with their sales emails looking at communications with customers, or jobs, or orders. ▶ There are a number of very practical things you can ring-fence that can become part of your playbook for your business once you're focused first on those customers.

01:11:43 - Paul Miller
I'd love things to be recurring SaaS models, but I just don't know the future of SaaS. So I'm thinking it's big consulting upfront at a really good hourly rate.

01:12:08 - Jake Maymar
What you're talking about is timeless, right? Understanding the business. And the biggest problem with AI now is you can do everything. And because you can do everything, it may or may not be tied to a business need. ▶ Just because you can do something doesn't mean you should.

01:12:33 - Jake Maymar
Understanding the business, having that deep research, and going into the meeting basically ready to go — having essentially a mock-up of what you could build together as a discussion point, but knowing those backgrounds about all the people that you're meeting with — that's one of my favorite workflows that I run.

01:13:27 - Jake Maymar
Like, I get an email where I'm like, I don't know who the hell this is, and then I click on it, and it just has everything about this person, everything about the company, everything about the thing. My friend even did this really interesting thing where you put your credit card in Stripe to basically buy a meeting, and he doesn't actually know who's going to do that, but what's neat is it does the full research on that person, so when he gets on the call, he knows everything about that person.

01:17:33 - Ty Wells
Yes, I think what you guys were talking about — what we do with AI — I think we all become intelligent architects, if you will. From a business perspective, business intelligence — that's what they need, so things can be recognized, synergies, insights can be recognized. And then we use AI to produce whatever solutions to realize those insights.

01:18:08 - Ty Wells
▶ So basically, applied AI is sort of what I think is going to happen. You're applying AI to the best places, but you're using AI to get you the best understanding. So very, very circular. And then you use it to actually build what you need.

01:18:30 - Patrick Chouinard
Absolutely. And you see, Paul, you might say that you didn't have the shiny new toy this week, but business wisdom might not be shiny, but it's extremely valuable.

---

<!--SEGMENT
topic: Patrick's AI News Monitor and OpenClaw Architecture Deep Dive
speakers: Patrick Chouinard, Jake Maymar, Ty Wells, Paul Miller
keywords: OpenClaw, Claude Code, Databricks Apps, Astro, OpenRouter, Qwen 3, Kimi 2.5, Claude Opus, Discord, GitHub Projects, Obsidian, memory architecture, headless Claude, token economy, channel-specific memory, AI news crawler, Gemini, NotebookLM
summary: Patrick describes two major projects: a work AI news monitoring system that crawls five platforms, tracks tool inventories, generates daily briefings, and publishes to a Databricks App via Claude Code — all without prior Databricks expertise. He then details his personal OpenClaw architecture: Discord channels mapped to memory layers, model routing via OpenRouter (Qwen 3 for cheap tasks, Kimi 2.5 for medium, headless Claude Code for complex), GitHub Projects for task tracking, and Obsidian for brain transparency.
-->

01:28:27 - Patrick Chouinard
This week, at work at least — sadly I can't really showcase it — I've delivered basically a search bot for AI news on the different platforms that we're evaluating right now.

01:28:57 - Patrick Chouinard
It crawls the news sites. What it does is — I gave it the five platforms we're monitoring. Out of each platform, it goes for the news, the general news about the platform. Nothing technical — like, are they in the news? Are they in a funding spree? Are they planning an IPO? Are they being sued by someone? Have they acquired someone? Did their board change? Anything about the company itself.

01:29:32 - Patrick Chouinard
Then I do an inventory of the tools in their ecosystem, because it's not all to say, "Oh, Claude has a new model" — they have tools in their ecosystem, like Gemini [tool:Gemini] will have NotebookLM [tool:NotebookLM], Claude will have their Artifacts — like all of the things around them. So I inventory those. I approve the new tools. So basically, if there is something in inventory today that was not there yesterday, it actually captures it and asks for my approval: "Do we want to track that new tool as of today?"

01:30:00 - Patrick Chouinard
Then it goes through each and every tool and does a web search on all of them to get all the news about each tool individually. Then it does a differential between what it found yesterday and what it found today — so it's basically an ever-evolving report on all of those provider platforms. And the final result — I do a daily briefing — so basically out of everything it found, what's new today and interesting that it needs to surface. Then I pump all of that Markdown into an Astro [tool:Astro] static site, and I publish that as of today.

01:31:00 - Patrick Chouinard
And I know it's wildly over-engineered, but the idea was we wanted to test if it was possible. We published that site as a Databricks Apps [tool:Databricks Apps], and the goal was just to see if Claude Code by itself could do the publishing and do the configuration of a new app in Databricks, because I've never published apps in Databricks. It's the first time at the client I'm at that they're starting to use Databricks Apps.

01:31:42 - Patrick Chouinard
So there was no expertise in-house on how to create, instantiate, deploy, test, do the permissions. ▶ Basically, Claude did all of that for us, documented itself, and published the site. So I used my little project as basically a showcase to see — here's how you do that kind of publishing. So now we have a site that we can go on every day and it's going to have all of the latest news about all of the AI platforms we want to monitor.

01:32:28 - Patrick Chouinard
And at the same time, we managed to display that a developer will now be able to include — because when I say document, I mean I've created the skills out of it. So now we can distribute that skill internally. And now every developer that wants to publish an app through Databricks can just invoke that skill.

01:33:00 - Patrick Chouinard
On the OpenClaw front, I haven't been able to complete the thing I wanted to, but I've moved forward a lot. As I talked about in the beginning of the call, I've moved away from Telegram and into Discord — just because it's a simpler interface for me to work with. And I've created a dedicated Discord server for my discussion with OpenClaw. Basically, we're the only two members, so security from that front. And also, I can now split my discussion in multiple discussions, so I have way more precise and short discussions, so it doesn't burn through tokens resending three weeks of chat every single time.

01:33:48 - Patrick Chouinard
▶ And I also assign models per conversation. So basically, simple conversation, I'll use the cheapest model possible. And the more I expect from the conversation, that's when I'm going to burn through more expensive tokens. And the very complex stuff — instead of having it do it, I have it use Claude Code in headless mode as a tool.

01:34:20 - Patrick Chouinard
So basically it just sends the request to Claude Code to do whatever the most complex task is that I don't want the agent itself to take care of. The day-to-day stuff is running through OpenRouter [tool:OpenRouter], so I'm using Qwen 3 [tool:Qwen 3] for the day-to-day stuff. Pretty solid model, good tool calls, very, very cheap. If I need a little more oomph, I go to Kimi 2.5 [tool:Kimi 2.5]. And for the hard stuff, I use OAuth authentication with Codex, and whenever I need Opus, it's through a call through Claude Code — meaning I can use my subscription and OAuth without getting banned, and I don't pay through the nose for Opus tokens.

01:35:28 - Patrick Chouinard
So that's something I want to formalize as an overlay project on top of OpenClaw — not modifying OpenClaw itself. And also by separating the multiple channels, I also want to implement a third level of memory, because right now it has its own context — the chat itself — plus the memory files, plus its personality. ▶ Now I want to insert a second layer in between, which is the channel-specific memory. Always to diminish the context — to make sure that I only pass what it needs to know when it needs to know it, so I don't burn uselessly through tokens by sending a bunch of useless information.

01:36:23 - Jake Maymar
<Q>So how do you route it to Claude? Because you said you go to Codex when it's really hard, but then how do you — do you specifically say, "Go ahead and use Claude for this"?</Q>

01:36:37 - Patrick Chouinard
<A>Basically, I call Claude through a script that calls it endlessly, so it just makes a `claude -p` with the prompt. I want to make it interactive — I'm not there yet — but with a headless call, it works perfectly well, and Claude's not the wiser. I'm not going against TOS, I'm not sharing my OAuth with them for Claude, so I'm not going to get banned or anything, and I've leveraged the tokens I already paid for.</A>

01:37:15 - Patrick Chouinard
And so having it split like that, having it layered in terms of memory — it means I only send it what it needs to know. So it's not only for token economy, it's also for precision. If you send it three weeks' worth of conversation every time, it's never going to be as precise as if I personally tweaked the memory for it.

01:37:43 - Patrick Chouinard
And I've made sure that first it handles its own backup daily — so it created itself a backup job. The backup is sent through GitHub, so I use GitHub to backup. It's just a Markdown file. Why pay for online storage when you have one free with GitHub?

01:38:10 - Patrick Chouinard
I have it replicated inside of an Obsidian Vault [tool:Obsidian]. Not replicated directly, but basically every time it does something, every decision it makes, every checkpoint that we make — like, "From now on, you're going to do that" — it documents it in a journal fashion inside of an Obsidian Vault that is also synced through GitHub. Meaning I can read it anytime, and I can alter it anytime. And it has the structure of an Obsidian Vault with all the backlink connections. ▶ So I can basically look at its brain hierarchy in a file whenever I want. So it also helps a lot with reassurance that it learned the right thing, because I always have access to its mind without having to log into the VM.

01:39:28 - Patrick Chouinard
▶ And I use GitHub Projects for it to share its stage of evolution with the ideas it's working on. So every time I tell it, "Oh, I want to work on this thing," or it proposes something in the morning — it sends me its three ideas of what it thinks would help me for the day. So whenever I say, "Oh, I want you to work on that," basically what it means is it creates an entry in the GitHub project for it, and it prioritizes them. And every day I'll say, "OK, today I want you to work on that one." So it starts working on whichever project we've selected.

01:41:12 - Patrick Chouinard
Yep, so it can create multiple branches and work on multiple ways to resolve the same issue at the same time. And I look at the project — I can go modify the project because it uses the project item to create issues. It uses the issues as context to start the actual development, and it reports back up. So basically I have project tracking with the assistant.

01:42:02 - Patrick Chouinard
This is where you're at now, and I'm sure Ty and Scott are in an interesting place as well. Where is this going to be in two months? Like, you guys have already advanced very, very far. We're just scratching the surface.

01:42:17 - Patrick Chouinard
The Kraken has been released. It's exponential.

01:44:25 - Patrick Chouinard
▶ That's exactly why every day I talk with it — like with everything that pisses me off, slows me down, whatever. There's always a message about it. And that's where it comes up with the ideas it proposes the next morning at 7 a.m. Every morning at 7, it sends me a message saying, "Here's three ideas that might be helpful for you today." And whenever there's a good idea, I say, "Oh, add that to your queue. That's something I want you to work on."

01:45:00 - Jake Maymar
The more I do that, the more it updates its memory, and the better the recommendations the next day. So the more you use it, the more useful it's going to become.

01:45:26 - Jake Maymar
Yeah, and people will have difficulty finding the value because it's really, really hard — and I had the same challenge before I started to use it. It's just, now that I have it, I would not dream of not having it. ▶ Whenever you make the unit of work cheaper, you create the possibility to do work that was always too expensive to take care of before.

---

<!--SEGMENT
topic: Technical Debugging — Drizzle DB, Sharp, Vercel, and Supabase Multi-Tenancy
speakers: Morgan Cook, Patrick Chouinard
keywords: Drizzle DB, connection pool, SQLite, Sharp library, Vercel, Windows, Linux, Supabase, multi-tenancy, IPv4, IPv6, Postgres role, Context7, documentation, package.json, optional dependencies
summary: Morgan shares two significant debugging discoveries from the week: a silent Drizzle DB connection pool failure caused by a missing `prepare: false` flag, and a Sharp image library cross-platform incompatibility between Windows development and Vercel's Linux runtime requiring optional dependency configuration. He also describes a Supabase multi-tenancy limitation on Vercel due to IPv4-only support blocking dedicated Postgres roles. Patrick recommends building project-specific documentation packs over relying solely on Context7.
-->

01:21:01 - Morgan Cook
I was doing some storage of content in buckets, and for whatever reason, after like five or six adds to the bucket, it would just stop responding, and it would silently fail. And it took me about an hour to dig this thing out, but in the Drizzle [tool:Drizzle] `db.ts` when it creates the connection stream, I didn't have the `prepare: false` flag.

01:21:30 - Morgan Cook
So the connection pool was resetting, and the transaction layer doesn't travel with the connection pool.

01:21:42 - Morgan Cook
▶ So that's something to watch out for. If you're doing something that's working fine, but then it just all of a sudden stops with no errors, check to make sure it's not the connection pool cycling and your prepared transactions are being lost.

01:22:00 - Morgan Cook
The other thing was — I actually started my implementation of the multi-tenant issue, and the way I was going to do the connection was with a dedicated Postgres role, but using Vercel [tool:Vercel] and IPv4, it does not support that.

01:22:27 - Morgan Cook
So you have to use — if you're going to use a database URL connection string — you have to use the Postgres user if you're connecting from Vercel. The AI is going to try and build it correctly by generating a new Supabase Postgres role for the data access layer and give it permissions and everything, but it'll fail because of the IPv4 issue.

01:23:01 - Morgan Cook
▶ So until they update that for IPv6, we can't use that feature. So I went back to the Postgres user, which was fine, but it limits how far you can lock it down because I was intending on making the data access layer restricted to its specific tables.

01:23:44 - Morgan Cook
Oh, I ran into a problem with the Sharp library [tool:Sharp] that gets included. I'm on Windows, so that's one of the problems — the Sharp library for Windows is a little different. That's the image processor. And the package for the PnPM unlock package for the YAML — it would package it up, but you would have to specify an optional set of packages, because Vercel is running on Linux, and my development is on Windows, and it doesn't know how to properly connect them.

01:24:51 - Morgan Cook
So it was failing to generate or convert the images properly when I deployed to Vercel. ▶ The fix: you have to add a `vercel.json` file that has PnPM install with an `include optional` flag, and then there's another place to set up the actual two different binaries — I think that's in `package.json`. So in `package.json`, you've got to include both of them as optional libraries — so you include the Linux x64 as well as the two for the Windows environment.

01:26:00 - Morgan Cook
I've got like three clients right now that I'm working on three different sites for, and that's where these problems are raising their heads. And it seems like it's always — it's like you fight with the AI to get it to pay attention to the documentation or notes that you have. I have Context7 [tool:Context7] loaded for some of it, but that's not enough when you have a problem that's not documented in the documentation — it's documented in issues, but not necessarily in the documentation.

01:26:40 - Patrick Chouinard
On that front, Morgan — one thing I do pretty often now, because I used to have a problem of the same nature — Context7 is awesome when you start a new project and you're not sure about the entire technical stack you're going to use. ▶ But when you have an established application, I find that compiling my own documentation for the very version I'm using and everything I'm going to be working on is a lot of times way more efficient than just fishing through Context7 all the time. So if there is online documentation, if you find articles, issues, Reddit threads about the solution, I tend to include them in my own documentation pack, and I make that documentation grow over time with the project. And every time I've done this, I've diminished the number of errors by a factor of 10.

01:27:42 - Morgan Cook
Yeah, so I have a guides folder with specific things — like for my Sharp/Vercel/Windows issue, an issue I found with Resend [tool:Resend] email, and the multi-tenant issue with the IPv4 stuff. So yeah, I've been doing the same kind of thing.

01:28:15 - Patrick Chouinard
Exactly. We're having problems, but hopefully we're having them once.

01:28:22 - Morgan Cook
DRY. Practice DRY.

---

<!--SEGMENT
topic: Enterprise AI Adoption Divide and Meeting Preparation Workflow
speakers: Patrick Chouinard, Paul Miller, Ty Wells, Morgan Cook, Raghav Ram
keywords: enterprise AI adoption, corporate IT restrictions, deep research, meeting transcription, Fathom, Plaud, Zoom, Claude, ChatGPT, prompt engineering, business consulting, AI Anonymous, Claude fast mode, Opus 4, context window, OpenRouter
summary: The group discusses a growing divide between large corporations restricting AI use and individuals/SMBs embracing it. Raghav asks for advice on structuring discovery meetings with prospective clients (an IT services provider and a tax consultant), and the group recommends recording transcripts as the foundational step, then using AI to analyze and fill templates. The session closes with humor about AI addiction and a brief mention of Claude's new fast mode and Opus 4's extended context window.
-->

01:18:54 - Ty Wells
Speaking about burn triggers — did anybody try fast mode just by accident and Claude? It has a fast mode, so it runs two and a half times faster. So it's like lightning fast, but the tokens deplete at a rapid pace. They have a half-off price now. So the hook is they get you in on that fast mode, and then the price doubles after, I think, February 16th.

01:19:23 - Scott Rippey
<Q>Is it only API calls though? Isn't it not on the plan, except for like that free $50 they've given us?</Q>

01:19:29 - Ty Wells
<A>It's what they call extra usage. So it's still in the plan, but you're paying for it and they give you $50, but you will spend that $50 in like five minutes.</A>

01:19:46 - Scott Rippey
I want to know if the results are the same or not. That's what I truly wanted to know.

01:19:51 - Jake Maymar
<Q>Oh, have you guys used the million context window, the Opus 4 [tool:Claude Opus 4] 6-million context?</Q>

01:19:57 - Jake Maymar
That thing is amazing.

01:20:01 - Ty Wells
I can't actually use that on a plan.

01:20:05 - Scott Rippey
Yeah, it's not in the plan.

01:20:08 - Ty Wells
Because Sonnet 4.5 [tool:Claude Sonnet 4.5] has had this for a long time, but only in API calls. Now they have it on Opus. They won't give it to us in the plan.

01:20:27 - Jake Maymar
Well, I'm sure eventually you'll try it out. It's stunning.

01:48:30 - Patrick Chouinard
Did you guys see — there's one of those commentators — he raised an interesting point. There's a growing divide between large corporates using AI and everyone else. Because their IT teams, their legal teams are like, "Oh no, you can't touch any of this," and everyone else is like, "Oh, how can it help us? Let's get on with it."

01:49:18 - Ty Wells
<Q>Are you seeing that with big corporates where you are?</Q>

01:49:31 - Morgan Cook
Definitely. I've seen that even today again.

01:49:44 - Patrick Chouinard
Yeah, it's like, everybody needs to invest in AI, but be careful not to use AI too often.

01:50:00 - Patrick Chouinard
AI Anonymous, huh? Is that what we've come to, guys?

01:50:09 - Raghav Ram
AI Anonymous, yeah. I am Ty. I'm addicted to AI solving. You guys are supposed to say, "Hey, welcome, Ty."

01:50:50 - Raghav Ram
My wife said I'm not allowed any more Claude subscriptions. I've cut back down to OpenRouter, and I'm spending $20 a day.

01:51:09 - Raghav Ram
Patrick, so I'm trying to — I mean, I have an appointment to meet a couple of business owners. One of them is an IT services provider, and the other is a tax consultant. I'm trying to talk to them to understand — I know one of them said they have some problems with the sales process. The question here is, is there any standard — I mean, templates, or is there a way using Claude Code or AI, anything, that I can talk to them and gather the information in a structured way? Are there any suggestions?

01:51:55 - Patrick Chouinard
<Q>Well, are you going to talk to them in person? Are you doing a virtual?</Q>

01:52:02 - Raghav Ram
I think with one of them, it will be in person, and the other one will probably be a virtual meeting.

01:52:10 - Patrick Chouinard
<A>Because honestly, if you can record a transcript of the meeting — that's right now, I try to have everything in text. I have Fathom [tool:Fathom] and I have the Plaud [tool:Plaud] as well. I want to make sure that I have a way to record absolutely everything. So either it's recorded here, either it's recorded on the Plaud, or it's a recorded session in Zoom [tool:Zoom], Teams, or whatever. Once you have that, whatever you need to do is a prompt away with Claude, ChatGPT, or whatever AI you have access to. And if you want to do something specific, just ask the AI you have access to to help you build a prompt that's going to analyze your transcript. ▶ But as long as you have a transcript, there's nothing that can't be done with AI.</A>

01:53:14 - Raghav Ram
Yeah, I was trying to scour the internet for some kind of templates and all that, but I think...

01:53:24 - Ty Wells
▶ Honestly, by the time we find templates these days, there's 16 better ones that have come up. So just ask the AI — it's going to build one on the spot and it's going to be tailored to whatever you require. We're beyond the world of templates because we have access to the best template builder in the world.

01:53:49 - Patrick Chouinard
Actually, if you want another thing you could do — if you even have forms or templates that you want to fill in with the information that came from that meeting — you could design a very simple prompt. Again, just ask the AI to build a prompt for you and say, "Here I have a template. Here I have a transcript. I need to fill this with this. Can you create a prompt that will do it for me?"

01:54:21 - Paul Miller
So the core thing seems to be: record the conversation.

01:54:25 - Patrick Chouinard
▶ If you have it in text, you're good.

01:55:01 - Patrick Chouinard
Yeah, Raghav — before you have your meeting, if you're not already planning to do so, it might be worth doing a deep research on the parties you're going to catch up with. Just in your deep research prompt, say, "Look, you're going to have a sales meeting with these guys, and they kind of at a high level talked about these things." ▶ Prepare yourself before you walk in.

---

=== UNRESOLVED SPEAKERS ===

- **Sam** — appears briefly (00:41:32), no alias mapping available; passed through unchanged.
- **Ryan C** — surname initial only; no canonical full name in alias map; passed through unchanged.
- **Morgan Cook** — not found in alias map; passed through unchanged.
- **Jake Maymar** — not found in alias map; passed through unchanged.
- **Raghav Ram** — appears in transcript attributed to both "Raghav Ram" and "Patrick Chouinard" (likely a transcription attribution error in the 01:09–01:17 range where Patrick's lines are labeled Raghav Ram); passed through as-is without correction.
- **Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com** — raw name includes social handle and URL; normalized display name used as **Scott Rippey** throughout; no canonical alias map entry confirmed.
- **Bastien** — referenced in chat by Patrick ("what Bastian just said in the chat") but never appears as a speaker; not resolvable.