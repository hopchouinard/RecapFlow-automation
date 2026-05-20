=== SESSION ===
date: Unknown (weekly coaching call)
duration_estimate: ~2 hours
main_themes: AI-assisted development workflows, adversarial code review, career transition into AI engineering, payment integration, infrastructure-as-code with AI tools, project showcases (SwingTrack, ConkPass, ShipSafe/MCP marketplace, AI photo booth, YouTube content pipeline), portable HTML/markdown artifact format, natural language security and prompt injection

---

<!--SEGMENT
topic: Session Open and Small Talk
speakers: Marc Juretus, Tom Welsh, pchouinard, Bastian Venegas, Ty Wells
keywords: Community Brain Project, Claude Code, Codex, Brendan, LinkedIn, gardening automation, ChatGPT, webcam monitoring, weather sensors
summary: Participants join the call with informal greetings and weather chat across Chile, Canada, and the UK. Patrick gives a brief update on the Community Brain Project, noting it is nearly packaged for cross-platform deployment (Windows, Linux, Mac) and that a demo video with Brendan was posted on LinkedIn and the school community.
-->

[00:00:00] Marc Juretus: Yeah, I basically use Cursor [tool:Cursor], but I have the Claude CLI [tool:Claude CLI] that I use for the most. Hey, Patrick.

[00:00:15] Marc Juretus: No sound, brother.

[00:00:18] Tom Welsh: You're muted.

[00:00:20] pchouinard: Sorry, I said you can continue talking. It's not because I arrived that you have to stop.

[00:00:24] Tom Welsh: I was just looking at that magnificent beard of yours.

[00:00:35] pchouinard: Let's just say I have a good barber.

[00:00:41] Marc Juretus: Is that something religious or is that just the look you like?

[00:00:45] pchouinard: No, just my look. Give a lumberjack.

[00:01:09] Tom Welsh: We should have a couple of interesting questions tonight, if the people who posted actually come in.

[00:01:24] Tom Welsh: Yeah, invited one of the new guys — he's been asking the starting question — to come along. He's from India. So it's about 4am in the morning for him if he turns up.

[00:01:36] pchouinard: The question I got was more of a statistician with 20 years experience, wants to transition into AI engineering.

[00:01:45] pchouinard: Hey, Bastian.

[00:01:50] Bastian Venegas: Hey, Tom. Hey, Patrick.

[00:01:56] Marc Juretus: Hey, Bastian.

[00:01:57] Tom Welsh: How goes it down in Chile?

[00:02:00] Bastian Venegas: It's very cold, man.

[00:02:18] pchouinard: We were closing on 85 today.

[00:02:35] pchouinard: We're in the land of extreme. We experience minus 30 as well as plus 35.

[00:02:59] pchouinard: Hey, Ty.

[00:03:07] Ty Wells: I'm on the deck today. I've got a hoodie on. It's a little nippy over here.

[00:03:23] Ty Wells: Do we have any Germans on the call, typically?

[00:03:37] Ty Wells: I'm headed to Berlin tomorrow.

[00:04:09] Ty Wells: Actually, Claude [tool:Claude] should know. I can just ask it.

[00:04:41] Ty Wells: It's at the Betahaus Arena. Kreuzberg.

[00:04:56] Tom Welsh: Turkish sector.

[00:05:31] pchouinard: Let's slowly get started, and I'm going to monitor to see if the person who asked the question in the comments this week actually shows up and we can address this question.

[00:05:49] pchouinard: First, just a little update on the Community Brain Project. I did not have a whole lot of time to go further. It's almost packaged. I just need to finalize some things to make sure it can be deployable in any environment because I need to make sure it deploys on Windows, Linux, and Mac.

[00:06:16] pchouinard: I need to do another pass. Sadly, my garden needed my attention this weekend. So for once I was outside and not having fun with Claude Code [tool:Claude Code] during the weekend.

[00:06:34] pchouinard: And as you might have seen, Brendan was nice enough to do a little video with me that got posted on both LinkedIn and in the school community.

[00:06:47] Tom Welsh: That was a good video.

[00:06:48] Ty Wells: I saw that. That was a great video.

[00:06:53] pchouinard: Thank you. Hopefully the first one of many, but we'll see.

[00:07:14] pchouinard: So I don't see the person who asked the question, so let me grab a screenshot, and we're going to start with the people that are actually on the call.

---

<!--SEGMENT
topic: Payment Integration for Nonprofit Site
speakers: Marc Juretus, Tom Welsh, pchouinard, Bastian Venegas, Ty Wells, Adam
keywords: Stripe, PayPal, Next.js, Sanity.io, Clerk, open banking, MCP, Codex, Alpaca, stock trader, donation integration
summary: Marc describes building a website for a historic foundation using Next.js and Sanity.io, and asks for recommendations on payment/donation providers. The group discusses Stripe (recommended for Next.js compatibility), PayPal (negative experience shared by Bastian), Clerk (uses Stripe under the hood), and open banking as a lower-fee alternative. Patrick notes there is both a Stripe CLI and an MCP for Claude Code. Marc also briefly mentions his AI stock trader running on Alpaca paper trading, currently up $5,200 of a $100K virtual portfolio.
-->

[00:07:41] pchouinard: So based on this, I would start with Marc.

[00:07:44] Marc Juretus: Hey, not too much to report on my end. I'm working on a personal site for a historic foundation. They have a donation section and I've been looking at PayPal [tool:PayPal] and Stripe [tool:Stripe]. <Q>Are there any other better options or something you recommend, or any drawbacks for anyone who's done that?</Q>

[00:08:17] Bastian Venegas: I hate PayPal. My experience was terrible. I tried to wire money to pay a course and the money was kind of lost in the way. They blocked money that I was supposed to receive — it was like two grand — and I was never able to recover it. PayPal said to check with my credit card provider, and my credit card provider told me to check with them, so at the end, I lost the 2K.

[00:09:08] Tom Welsh: <Q>What front end are you using, Marc?</Q>

[00:09:16] Marc Juretus: <A>So it's basically Next.js [tool:Next.js] and I'm using this interface called Sanity [tool:Sanity.io] that lets you update the pages for them to add. They just update blocks of the page. They did have an existing site, but they had a real falling out with the developer. So they did have donations before. I've got a meeting with the guy tomorrow night. So we may use what he has already or we may change to something else.</A>

[00:09:43] Tom Welsh: ▶ Yeah, Stripe interfaces quite well with Next.js. They've got good tooling in there.

[00:10:01] Marc Juretus: There's real news of note — I still have my stock trader running on its own. I keep tweaking that every day, every couple of days from its lessons list that it learns lessons and it teaches itself stuff. So we'll see where I'm at in a month. I'm up like $5,200 out of the 100 grand that Alpaca [tool:Alpaca] gives you by default for trading. So it's doing okay.

[00:10:19] Adam: So, Marc, I was trying to think about helping one of my friends with his charity. And when I looked into it, there's a couple of providers that do open banking. And if they want to use their bank account instead of credit cards, the fees are just way lower.

[00:10:51] Bastian Venegas: ▶ Yeah, Clerk [tool:Clerk] does provide the service too, but they use Stripe under the hood. They just try to make it easier for you. So in case you run into issues, you may look into that.

[00:11:14] pchouinard: ▶ I believe there is a CLI for Stripe as well as an MCP [tool:Stripe MCP] for Claude Code, so it might make it easier.

[00:11:22] Ty Wells: Yeah, that's all I use too for Stripe, and the CLI is a wonderful way it works. The issues are usually on the callback. For some reason, those fail sometimes when you set up your callback to indicate receipt, payment, or whatever it is. ▶ So just make sure that that's tested thoroughly.

[00:12:06] pchouinard: Oh, there's a Codex [tool:Codex] plugin as well.

[00:12:19] pchouinard: I've been a big fan of dual-harness development — basically Claude Code and Codex simultaneously.

[00:12:53] pchouinard: Good. Anything else for you, Marc?

[00:12:56] Marc Juretus: No, that's pretty much it for me. I haven't done anything new. I just kind of wanted to sit back and watch and see what Patrick's up to this week.

[00:13:18] pchouinard: Right now, my life is between my office and my garden — which is actually monitored by a webcam and fed back into ChatGPT [tool:ChatGPT] for evaluation to tell me what I need to do to the garden. I might eventually present that little project.

[00:13:42] pchouinard: Yeah, actually, I want to tie in with an automated irrigation system. So ChatGPT monitors the garden, has all the feedback from the agrometer and all of the sensors in the garden, and whenever it needs it, ChatGPT triggers irrigation.

[00:14:01] Adam: I see a lot of people use weather prediction, right, and then they can minimize their watering.

[00:14:08] pchouinard: Yeah, to me it's not much to minimize because in Quebec we don't pay for water, so it's not a matter of reducing, but it's a matter more of making sure that I don't kill the thing by overwatering it.

[00:14:21] Ty Wells: Yeah, I know pH is very important. That's very, very — just a decimal point is very important between good and bad.

[00:14:35] pchouinard: ▶ Yeah, basically anything is data now. So if you have a source of data, you can have AI help you navigate it.

---

<!--SEGMENT
topic: Career Transition — Statistician to AI Engineer
speakers: pchouinard, Eric Tsai, Ty Wells, Bastian Venegas, Adam
keywords: AI engineering, statistics, applied mathematics, LLM, OpenAI API, Anthropic API, full-stack development, Claude Code, Codex, Lovable, machine learning, TurboQuant, convolutional nets, image recognition
summary: Eric Tsai, a PhD statistician with 20+ years of experience, asks how to transition into AI engineering. He observes that job postings emphasize software engineering and API usage over mathematical depth. The group advises him to leverage his domain expertise as an evaluator of AI outputs, build projects in his own field of knowledge, and use tools like Claude Code and Codex rather than no-code tools like Lovable. Adam and Bastian suggest that classical ML and specialized domains (audio, video, quantization) may be a stronger niche for someone with his math background.
-->

[00:14:43] pchouinard: I just saw that Eric has joined us. So Eric, if you want — you were the one with a question posted. Just a quick recap: basically you're a statistician with 20 years of background and you want to transition into AI engineering, so feel free to tell us a little bit more about that and what questions you want to answer specifically.

[00:15:11] Eric Tsai: Yeah, thank you so much, Patrick. So my background — I got a PhD in Applied Math 20-plus years ago. So after that, I started working when AI was still in the winter. Started out as a statistician, used traditional statistical models. Up to five or six years ago when the data scientist job title became a trend, I switched to data scientist — even though I still pretty much did similar things, traditional statistical models. And then the AI hit — large language models. And I'm trying to pivot into an AI engineer job position. I just saw within the company I work for, they just created an AI engineer job, and I look at the job description, and also look outside of the company — there are so many AI engineer job postings. And basically, to be honest with you, from all the jobs, the laundry list of things you need to know, it's shouting "software engineer, software engineer" to my face. Basically, a software engineer who knows how to use the OpenAI [tool:OpenAI] API, Anthropic [tool:Anthropic] API, and send a request and get a response back.

[00:17:00] Eric Tsai: So basically what I'm saying is I see more and more mathematics and statistics going out the window. Nobody really cares. Even the company I work for, there are data scientists who are building AI agents to handle documents or answer customer call requests. They build models day in, day out, and when I ask them, "Do you really understand a little bit underneath what's going on?" they say, "No, why do I need to know? I just know how to call the API." So this reinforces my conviction that I need to pick up the full stack — the front end, the back end, the database, the authentication — in order to build a full-stack AI application or AI product.

[00:18:28] Eric Tsai: So my question for you: can you guys help me? My goal for this year is by end of this year, I want to feel confident enough to apply to AI engineer positions, which clearly require three-plus years of software engineering experience and knowing how to use APIs. So I cannot wait to hear from you guys — experts — on how to pick up those software engineering skills.

[00:19:05] pchouinard: <A>Actually, Eric, I'm a trainer in a company, and I train classic developers into becoming AI-assisted developers, and what I always tell them is: you think your skills are no longer valuable, but they are extremely valuable. Because you know how to evaluate the work the AI would create around your field of expertise, and that's the skill that's most needed. ▶ So if you want to train on AI engineering, don't try to go and grab a course that will show you how to do a SaaS website. If you want to understand what it is to be an AI engineer, do a project where you build something that you understand. Build an A/B testing system. Whatever you do normally in your work, your expertise — build a system that does that. That will teach you how to use AI to do something, and you have the ability to evaluate what the AI has created, because that ability to evaluate is the most important thing that you need to add to your skill set.</A>

[00:20:48] pchouinard: ▶ After that, you can go and learn how to do front-end, learn how to do back-end — not learning how to code those things. You never will write a line of code in that realm. But once you know how to guide AI, how to do the architecture to get to a solid structure, the rest is just the same method applied again and again.

[00:20:57] Ty Wells: I'm in 100% agreement with that. The only thing I would add is that it's about asking the right questions, being really curious, and yes, in your space, with your background. ▶ For me, it's more of: I envision what the end result is, and then I reverse engineer back to code. Claude Code [tool:Claude Code] is doing the work, but I want to get to the product or the end result first.

[00:22:37] Eric Tsai: So, for example, there's a lot of things like no-code tools — like Lovable [tool:Lovable], right? You guys know Lovable. So I tried it and it just generates. I type it, prompt it, and it creates a front end for me. And after several iterations, it finally gets to work, and I know nothing of those JavaScript or TypeScript codes. And later I heard the term "technical debt" — like, you may have it generate thousands of lines of code for you and it runs okay, and just call it your own. I feel not confident whatsoever.

[00:23:58] pchouinard: <A>Actually, I'm surprised — Claude Code [tool:Claude Code], Codex [tool:Codex], all of those coding harnesses are very good at debugging if you guide them properly. What you need to learn to do is guide those systems. Actually, Codex and Claude Code are now probably better than 90% of true software engineers at debugging code.</A>

[00:24:26] pchouinard: ▶ You become someone that will guide, operate, and manage a team of virtual agents way more than you're going to be a software developer per se. So you have to understand what a front-end is, what a back-end is, how they talk to each other, what's the need for each one. But you don't need to know specifically how to code any of the nitty-gritty detail functions in there, as long as you understand the structure.

[00:24:53] pchouinard: And Lovable might be a little — it's good to start, but for my taste it's a little bit too hands-off. I like something in between, so that's why Claude Code, Codex, Cursor [tool:Cursor], Windsurf [tool:Windsurf] — a little bit more where I like to get in — simply because you see the background, you see the code getting generated, and as you're reading it, you're going to understand it more and more.

[00:25:45] Eric Tsai: Yeah, exactly. But in order to know the overall structure — what is right, what's wrong, how to guide it — exactly what you said: when I ask Claude Code to generate some traditional statistical model, I have to know in my mind what works and what does not work, and I have to tell it the direction to take. Exactly that. When it comes to software, you guys know high-level how to design the infrastructure. But to get to know that, you need to at least be experienced enough to know how to guide those directions, right?

[00:26:05] pchouinard: I would agree, yes. But you have to practice. ▶ I'm not saying go tomorrow and get hired to do a multi-million dollar project with Claude Code, but I'm sure you have thousands of ideas of little applications you can build from start to finish based on knowledge you already have — stuff that you will know how to validate if it was done properly.

[00:26:30] pchouinard: ▶ And another tool I might suggest, no matter the harness you choose, is a plugin called Superpower [tool:Superpower]. I absolutely love that thing, because it will guide you through the software development life cycle. In the beginning, it will hold your hand as you go through a brainstorming phase, it will present you the architecture that it recommends — 90% of the time it's decent — and whatever it produces will be correct enough to create an application that will at least work. And you will go through the whole process of brainstorming, design review, implementation, code review. It will guide you through the whole Git process to create the proper branch, do a PR, it will tell you: now we need to do this.

[00:28:00] Adam: <Q>Have you considered doing something more mathematical than software development, given your background? The software development market is pretty saturated right now because a bunch of people got flooded — new grads couldn't get jobs. For example, Google just changed the way they do quantization to basically a strategy of keeping the vectors the same between some of the values. And it's like an old technique in math that none of the young kids knew, and it just made the model much more powerful with the same amount of data.</Q>

[00:28:45] pchouinard: <Q>Are you talking about TurboQuant [tool:TurboQuant]?</Q>

[00:28:46] Adam: <A>Yes, yeah.</A>

[00:28:56] Bastian Venegas: <A>You have a heavy math background — you're in a much better position to leverage that in more classical machine learning, meaning not generative AI, such as convolutional nets and recurrent neural networks within domains like audio and video, where generative AI really struggles. There's a lot of space there to actually innovate when you have the knowledge for that — to actually fine-tune models and leverage stuff to get even proprietary things that you could sell to other businesses. For example, I'm from Chile and we have miners here, and there are safety concerns always. Someone invented a model that does one thing: it sees if you have your safety equipment on. And the companies pay a lot of money because it has to do with compliance. That's not a problem for a software engineer — it has to do with understanding the problem, being able to measure the impact, understanding the baseline, and actually iterating on that solution.</A>

[00:30:33] Eric Tsai: Yeah, thank you. You're talking about image recognition or something.

[00:30:39] Bastian Venegas: Yeah.

[00:30:43] pchouinard: Good. Well, hopefully it answered your question, and if you come up with others, we're here every week, so don't hesitate to join back.

---

<!--SEGMENT
topic: Adversarial Code Review Workflow
speakers: pchouinard, Tom Welsh, Juan Torres, Bastian Venegas
keywords: adversarial review, Claude Code, Codex, ChatGPT, GPT-4, Cursor, context pollution, Git diff, Superpower plugin, model bias, sub-agent, claude -p, codex exec
summary: Tom asks how Patrick conducts adversarial code review across different AI tools. Patrick explains his workflow: using Claude for brainstorming and implementation, then using Codex/GPT models to review Git commit diffs without sharing conversation context, to avoid model bias and context pollution. Juan describes a complementary approach of having Codex create a plan and Claude review it before implementation. Bastian introduces the claude -p and codex exec sub-agent commands as a way to spawn context-isolated reviewers programmatically.
-->

[00:31:03] pchouinard: Next would be Tom.

[00:31:09] Tom Welsh: Not done too much, really. I had my eye cut up yesterday with a cataract. So I'm just recovering. I'm still working on my membership application. I've been using Claude [tool:Claude] and Perplexity [tool:Perplexity] just to create privacy agreements — using your adversarial thing: chuck it into Perplexity, then chuck Perplexity's output into Claude and take Claude's output and put it back into Perplexity and go, okay, I'm happy with that now.

[00:32:27] pchouinard: By the way, when I do that, I love to tell the AI that what it reads comes from another AI. For some reason — I don't know if there's an adversarial thinking built into their training data — but they love to get more intelligent than the next guy.

[00:32:48] Tom Welsh: <Q>Oh, quick question — I missed last week's call. You're talking about adversarial on the code. Do you use different coding models or different IDEs?</Q>

[00:33:00] pchouinard: <A>To do the adversarial — actually, I tried to use different models. The idea is: first, you don't want to do it in the same conversation to avoid context pollution. And I always take a different model of the same level of intelligence in order to avoid model bias. So if I code something using Claude, I will do the adversarial with ChatGPT [tool:ChatGPT] or GPT-4 [tool:GPT-4] or something like that. And vice versa, if I code with ChatGPT, I'm going to do the adversarial with Claude. But somehow I find that GPT is more specific — it's better basically at doing adversarial than Claude, in my experience.</A>

*[RECORDING BREAK — same coaching call, second recording starts here. Timestamps restart from 00:00:00 but represent a continuous conversation.]*

[00:01:12] Patrick Chouinard: Basically Codex [tool:Codex] and ChatGPT are very good for the adversarial stuff.

[00:01:18] Juan Torres: <Q>Patrick, how do you get them to read each other's conversations? Do you create an empty file for one conversation and then tell the other one to read that empty file and see the problems with that, or how do you do that?</Q>

[00:01:31] Patrick Chouinard: <A>I actually open them both. The thing is I don't use the same harness. So basically I do that with Claude Code and Codex. I just open them both in the same repo. I don't want them to see the context because that's context pollution. I will ask Codex, for example, to do an adversarial review based on the Git output. So I'm going to have a list of Git commits to be reviewed. That's what I'm going to give Codex and say, go have at it and be as savage as you can be, basically, to find problems. Then it's going to give me a report. That's what I'm going to save as a file. So this is the analysis report. That's what I'm going to give to Claude and say, Codex found these things.</A>

[00:02:36] Juan Torres: Gotcha. What I've done is allow Codex to create a plan and then Claude to review that plan before the implementation. And sometimes I find that it's really good to do that even before the implementation process.

[00:02:54] Patrick Chouinard: ▶ Well, I do that, but since I'm a big fan of Superpower [tool:Superpower], I do the brainstorming with Claude, and then I'll review this with Codex. Codex is my reviewer. So basically, I love the GPT model for review of plan, specs, or code, and the implementation I leave to Claude.

[00:03:21] Patrick Chouinard: Actually, I don't know if you saw, but the latest version of Codex actually has a terminal where you can run Claude Code inside of the Codex desktop application.

[00:03:47] Patrick Chouinard: ▶ To me, the brainstorming part is more of the architecture part, and I find that Claude is a better architect most of the time. The GPT model, once you have a plan, will follow it to the comma compared to Claude. But for ideas and to go maybe a little bit outside the box, I find that Claude does a better job.

[00:04:16] Patrick Chouinard: But again, my Claude and my Codex also have a personality block inside of their agent.md and claude.md at my profile level. So it also helps because it removes a lot of the sycophancy.

[00:08:21] Bastian Venegas: One quick comment for what Juan was commenting about the adversarial review. ▶ The other thing you can do is if you want to spawn a sub-agent from the chat that you're working on, you can use `claude -p` [tool:claude -p] for Claude Code, and there's `codex exec` [tool:codex exec] that will launch a sub-agent that won't inherit the context of your conversation. So you can ask Codex, for example, to use `claude -p` to review its work or present a different view for the plan that you were just elaborating. When it says "fork," it means it will pollute its context, just as Patrick was saying he wouldn't want to. But if you tell it "don't fork," it will set it up as a regular sub-agent, and it will just get the prompt that the model will give.

[00:09:21] Patrick Chouinard: Yeah, the only thing you have to be careful of is that Anthropic has announced that now `claude -p` is not considered as part of the subscription. You will pay API calls.

[00:09:43] Bastian Venegas: They will give you an equivalent amount of dollars that you pay in your plan as subsidized API calls. But once you're out of that, you're done.

[00:09:46] Patrick Chouinard: ▶ That's why I love to do that with Codex, because the limit on the Codex side, even the $20 a month, are extremely high.

---

<!--SEGMENT
topic: Bastian's Music Production AI Project
speakers: Bastian Venegas, Juan Torres, Patrick Chouinard
keywords: Ableton Live, MIDI, music theory, chord progression, songwriter co-pilot, dbt real-time, Suno, EDM, model benchmarking, Stripe refund, chargeback
summary: Bastian shares a side project building an AI-powered songwriter co-pilot integrated with Ableton Live, using real-time music theory and MIDI to help compose melodies and chord progressions. The tool is designed to teach music theory interactively rather than generate finished songs like Suno. He plans to benchmark different AI model families on the same musical prompt. Bastian also briefly raises a question about Stripe refund recourse, which the group confirms is limited to contacting the vendor directly.
-->

[00:05:04] Bastian Venegas: So I don't have anything to share right now because I'm not on my main computer, but I'm working on some fun stuff. Side project: I'm a music producer as well, so I'm working on something with Ableton Live [tool:Ableton Live], which is like FL Studio — a digital audio workstation to make music. And I built a program that uses dbt real-time [tool:dbt] and some music knowledge — which is basically math — to help you write a song with an actual scale, chords, and a melody that fits in that chord progression. And it's like a songwriter co-pilot, not like Suno [tool:Suno] that will create your song with all the instruments and all that. The idea is that the model can help you program MIDI and adjust to that tempo and tell you — you can select a note, for example, or a couple of notes and say, "This section feels soft, can you help me understand why I don't like this, why my ears don't like this?" — and it can fill in the blanks for you in terms of music theory, so you can actually learn things as you go.

[00:06:18] Bastian Venegas: I have achieved some good melodies to start with, so I want to, when it's more advanced, benchmark how each model family makes music for a similar prompt. I think that will be a good thing to share later on.

[00:06:49] Bastian Venegas: And other than that, I wanted to ask you guys something that's kind of a legal question. <Q>Have you guys ever had to deal with a refund that wasn't fulfilled by an online company? An online partnership via Stripe [tool:Stripe].</Q>

[00:07:22] Ty Wells: <A>No, I mean, I have chargebacks with that. It's like a chargeback, right? They're canceling the order. But there's nothing... your recourse is minimal. You don't have many options except try to work it out.</A>

[00:10:18] Juan Torres: <Q>Bastian, what kind of music are you trying to produce?</Q>

[00:10:24] Bastian Venegas: <A>Right now it was kind of like an EDM thing, but it was just basic. The identity comes mainly from the instruments. Since it's MIDI in the first stage, I've kept it very simple — like a couple of synths, some pads, basic drum kits that come included with the software — because I don't want the model to have too many options. If I pass all of the virtual instruments I have, it would be like trying to choose from a final instrument. So I've just kept it very simple for now.</A>

[00:11:04] Juan Torres: Do you know Seven Lions?

[00:11:07] Bastian Venegas: Is that a group? A band?

[00:11:09] Juan Torres: It's an EDM artist. Actually, you kind of look like him. I'll send him to you.

---

<!--SEGMENT
topic: IDE Costs, Subscription Plans, and Tool Choices
speakers: Tom Welsh, Ryan C, Patrick Chouinard, Bastian Venegas, Juan Torres, Fitz
keywords: Cursor, Claude subscription, Codex, Gemini, OpenAI, Anthropic, API costs, $20 plan, $100 plan, $200 plan, Sam Altman, rate limits, Claude Code
summary: Tom reveals he has been using the $20/month Cursor plan for months without hitting limits, puzzling the group. Ryan explains he alternates between $100 and $200 Cursor plans depending on coding intensity, uses Gemini as a Claude backup, and avoids OpenAI on principle. Patrick shares an anecdote about a colleague whose Claude subscription was never properly canceled yet remains active. The group discusses the rapid cost escalation of API calls, especially with claude -p sub-agents, and why Codex's $20 plan offers comparatively generous limits.
-->

[00:11:36] Tom Welsh: <Q>Ryan, what IDE are you using and what models?</Q>

[00:11:42] Tom Welsh: So I'm using Cursor [tool:Cursor] and paying the $20 a month. And you guys are all talking about $200 bills. My biggest bill has been $48 and I've been on here for eight hours. I'm just wondering if it's a European thing.

[00:12:01] Ryan C: <A>I'm not sure how much coding you're doing — I don't know how you're managing to use the $20 plan for eight hours, that's quite impressive. I'm on the $100, and then if I know I want to have a particularly deep coding month, I'll upgrade to the $200 for the month, and then come back down when I know I'm going to have a slightly slower coding month. I'm using it in Cursor. I essentially mirror exactly how Scott does his stuff, because he taught me how to do all of this with the AI things. We're currently using Cursor, obviously we've got 12 to 13 agents set up within there — we don't use too many of them outside of using them to do security audits, checks, SEO, that kind of thing. And the SEO agent we've built is sensational. I use a smattering of Gemini [tool:Gemini] as kind of a backup when Claude decides to have one of his days where it's just not going to work for half the day. I vehemently try not to give Sam Altman any money because he is essentially the devil, so I attempt not to give OpenAI [tool:OpenAI] any money as far as I possibly can. Otherwise Codex [tool:Codex] is my backup really from a quality perspective.</A>

[00:14:24] Patrick Chouinard: Actually, just doing the debugging with the $20 a month on Cursor, I used to go through my limit within not even a week.

[00:14:30] Patrick Chouinard: I have a colleague of mine who actually bought the $20 a month Claude subscription, canceled it, called them multiple times because it wasn't stopping. Actually, they stopped charging her. She called them and said, "You're not billing me and my account is still active." She did everything she could and has all the proof that she tried. It's been years and she still has her subscription.

[00:15:05] Ryan C: You've just fallen between some gaps in Anthropic and they've forgotten about you, so don't tell them whatever you do.

[00:15:12] Tom Welsh: Oh, I'm definitely not telling anybody. I'm just sitting here smiling.

---

<!--SEGMENT
topic: Career Transition — Infrastructure/DevOps to AI Engineering
speakers: Patrick Chouinard, Fitz, Tom Welsh, Ty Wells, Juan Torres
keywords: AWS, DevOps, CI/CD, Terraform, Ansible, Docker, Claude Code, Codex, infrastructure as code, IAM, GCP, agentic DevOps, CLI, MCP, platform engineering
summary: Fitz, with a background in AWS DevOps and systems infrastructure, asks about transitioning into AI engineering. Patrick and Tom both emphasize that infrastructure knowledge is highly valuable precisely because AI tools like Claude Code and Codex can now generate Terraform, Ansible, and AWS CLI commands — but only someone with infrastructure expertise can validate whether those outputs are correct, secure, and compliant. Juan demonstrates how he uses Claude Code with IAM roles to provision EC2 instances via Terraform. The group identifies "agentic DevOps" as an underserved and high-value niche.
-->

[00:15:29] Patrick Chouinard: Good. Before I go too far, I know I got another question before the call from Fitz. Did you want to ask your question in the call now, or do you want to do it later?

[00:15:46] Fitz: Yeah, it's similar to the chat that came earlier on. I wanted to just ask about the career path to maybe an AI engineer. I've come mainly from the background of systems and infrastructure, and I want to pivot into AI engineering because if you don't have any AI these days, I think you might be toasting in the next two to three years. So that's my idea, but a roadmap towards that would be great.

[00:16:33] Patrick Chouinard: <A>Again, I'm going to tell you the exact same thing. ▶ Use AI to amplify what you know, and what you know is actually extremely useful right now. There's a lot of need for that. Claude Code or Codex or any of those harnesses are really good operators as well, because the infrastructure world is basically the world of CLIs. Guiding Claude Code or Codex to take the action — but having the ability to validate the action it does — way better than most devs will be, because you know the infrastructure. That would be incredibly useful.</A>

[00:18:21] Tom Welsh: Going back to your point about where you're coming from — my background is infrastructure and servers and stuff. And I've transitioned across to — I'm a "promptgrammer." I don't even attempt to say I'm a programmer because I just prompt my way to wherever I'm going. I use TypeScript, but I don't know TypeScript. I've used Claude and Cursor for things like Docker [tool:Docker], for setting up Terraform [tool:Terraform], for setting up config scripts for Ansible [tool:Ansible]. ▶ AI is not just for coding Python — there's a whole bunch of other config stuff you can do in your AI, and your transition, as Patrick says, you can go from where you are now to being a full-on platform engineer or site reliability engineer, just by prompting.

[00:19:43] Tom Welsh: ▶ You need to go away and get your vocabulary right. Ask the right questions with the right vocabulary and you'll get the results you want. If you don't know what a modal window is, how are you going to ask for a modal window in an application?

[00:19:58] Fitz: So it does Terraform and Ansible and everything?

[00:20:04] Patrick Chouinard: ▶ Yeah. To do infrastructure as code, Claude Code or Codex are incredibly good. There's a CLI and MCP for everything in AWS — you can have Claude Code or Codex do pretty much everything. And the advantage you have is you know if what they do is correct or not.

[00:20:57] Juan Torres: I've been giving Claude Code a user with the right IAM [tool:AWS IAM] policies in order to construct EC2 instances, platforms, data links with S3 [tool:Amazon S3], right? So I just give either a user the right policies or the IAM role. And then you can do a lot of things. You can use AWS CLI [tool:AWS CLI] with Claude Code and do a lot of resource generation and review. And it has just facilitated everything.

[00:21:45] Fitz: But my inclination is that you've got to check it though, don't you? You can't just blindly give it trust and say, okay, you've generated the code, go on.

[00:22:13] Patrick Chouinard: ▶ But that's the thing — it works, but your value, Fitz, comes into the fact that, especially in the enterprise, you have the ability to validate if what the system did was secure, was according to best practice, was according to its own internal rules. That's where your value comes in that the generic AI developer off the street will not be able to do the same thing you do, even with the power of Claude Code or Codex.

[00:22:45] Ty Wells: Yeah, so that knowledge that Patrick's talking about — those tools you were concerned about, the code that it's generating — the CLI is written by AWS. They know how it should work. It's going to function. The question is: you can write the wrong tools, you can use it in the wrong way, so you actually need that knowledge that you have so it can be used properly. ▶ Anybody can connect the AWS CLI and start going away, but do they do the right things, do they set it up properly, do they set up standards? So that's where you come in. The job doesn't go away — it actually becomes harder, because now you've got 10X people doing that, and it's breaking, and you need people that can solve those issues.

[00:24:17] Juan Torres: I feel like there's a huge need to teach people how to do agentic DevOps. I feel like that's something so, so underrated. Everybody's doing agentic coding. But nobody's talking about agentic DevOps. ▶ And I think that can be a really powerful niche.

[00:24:37] Fitz: And you should do that on GCP first.

[00:24:44] Fitz: GCP is all over the place. I try and avoid it as much as I can. I stay in Azure and AWS.

[00:25:13] Tom Welsh: ▶ There's probably more pay for GCP because there's less people out there that know it. And if you can agentify a GCP setup, because that's one of the biggest problems with GCP is trying to get something to automatically deploy.

[00:25:34] Patrick Chouinard: Actually, I think there's a Google Cloud Platform CLI [tool:Google Cloud CLI] that just got out recently that can help in that domain. Again, if you have the knowledge of what it means or what it creates and how it works. Because I also come from the infrastructure and virtualization side of things before I did what I do today.

---

<!--SEGMENT
topic: Ty's Project Showcases — SwingTrack and ConkPass
speakers: Ty Wells, Patrick Chouinard, Juan Torres, Ryan C, Brandon Hancock, Bastian Venegas
keywords: SwingTrack, golf wearable, gyro sensors, BLE, Wi-Fi, MIDI, hardware design, ConkPass, Bahamas, cruise ship, vendor vetting, AR product preview, GPT Image 2, mystery shopper, Stripe, image diffusion
summary: Ty presents two projects. SwingTrack is a golf analytics wearable system combining a wristband with gyro sensors, a cap-mounted camera, and club shaft reflectors to capture swing data, visualize shots, and provide statistics — with hardware design meetings underway. ConkPass is a platform for cruise ship passengers in the Bahamas to find vetted local merchants, featuring a ConkPass badge for approved vendors, receipt-based proof of purchase, an AI agent monitoring vendor reputation, a mystery shopper program, and an AR feature using GPT Image 2 to visualize purchasable items in the buyer's home before buying.
-->

[00:26:03] Patrick Chouinard: Next one would be Ty. What have you created this week?

[00:26:10] Ty Wells: Oh, you guys are in for a treat.

[00:27:08] Ty Wells: Okay, so you guys can see SwingTrack [tool:SwingTrack]. Well, this is a device that I'm building, a system for, because I play a lot of golf, and this device, this system allows me to visualize my game, replay it, and also get statistics and measurements. So that wristband has some gyro sensors in it, the cap will have a camera in it, and on the shaft of the club, there will be some reflectors that will help in determining where the club face is open for golfers and so forth. In combination with that, you will be able to look at all your shots and see how you were set up or how well you did and look at all the analytics. I'm combining some wearables with AI.

[00:28:20] Brandon Hancock: <Q>Wait, do you have the hardware too?</Q>

[00:28:22] Ty Wells: <A>I'm building the hardware, yes. I actually have another meeting with the guys tomorrow that are helping me with the design of the hardware.</A>

[00:28:52] Bastian Venegas: <Q>Could you also do a version that uses Meta Smart Glasses if people already have glasses for the camera?</Q>

[00:28:57] Ty Wells: <A>The problem with that is not everybody wears glasses, and as a golfer, I'm looking at this strictly from — like Patrick talked about — stuff you know and do. I know what will work, what won't work. This would be a bundle, but that's a good point.</A>

[00:30:00] Ty Wells: These will talk to each other over BLE [tool:Bluetooth Low Energy], and then it'll send the data on Wi-Fi, because I prefer to send it live. You'll still have an app, so you could still do it through Bluetooth, but you can also send it live as well, because there is a network play part to this.

[00:31:50] Ty Wells: Okay, so that is share number one. Let's go to share number two.

[00:32:11] Ty Wells: Okay. So who's been on a cruise ship before? One of the things I know when you go on a cruise — you get off and you explore that destination. And really, when you get off that ship, you are caught between vendors, people trying to sell you stuff, all kinds of stuff going on. And you want to be safe. There's no safety security layer between you when you get off that ship and when you're walking amongst cruise destinations. You don't know which restaurant's good, who's selling fake goods, who's selling real goods.

[00:33:00] Ty Wells: ConkPass [tool:ConkPass] is what comes into play. What it does is: local people — such as myself, I'm originally from the Bahamas — local people are vetting the vendors. There's a pass, this ConkPass, that's displayed at their business outside if they're fully vetted. They submit all the necessary documentation, you want to make sure they're legal, and then one local person goes and onboards these vendors, these merchants. So now you're able to see that symbol outside the store that this is a vetted merchant.

[00:33:41] Ty Wells: When you go inside and if you purchase something, you can upload a picture of what you purchased, and that'll show you — so you scan and save when you go out. And then you can share if you want to. But sending this receipt back is proof because the merchant pays 5% for the platform. So they're sending basically proof that somebody did make a purchase in the store through the platform.

[00:34:35] Ty Wells: These are actual places there in Nassau and the Bahamas. This is a second-tier release, which is more of bringing together a post that somebody may have put up of this carved turtle. And you can go ahead and try to see the turtle as it would exist in your living room or on your shelf or your mantle or whatever. This is before you even get on the cruise, right? If you're scrolling on ConkPass and you're seeing all of these postings, you can take a picture and it'll overlay the turtle in the picture. So that you can sort of visualize and make a connection to that item. And then you'll have the ability to pre-order that, because something like this is custom made.

[00:36:19] Juan Torres: <Q>Which diffusion model are you using for the overlaying of objects into specific areas of your living room?</Q>

[00:36:34] Ty Wells: <A>Oh, GPT Image 2 [tool:GPT Image 2]. It's amazing.</A>

[00:36:38] Juan Torres: Yeah. It is incredible what it can do.

[00:36:47] Patrick Chouinard: <Q>Extremely interesting. But I would just be worried a little bit — not about you, obviously — but about someone doing the same idea. Because you're promoting the validity of a vendor, but what promotes the validity of your platform? What tells me that the platform itself is not just a bunch of people paying for good publicity?</Q>

[00:37:17] Ty Wells: <A>Well, the vendors don't pay anything. They pay when the guest purchases something. They don't pay to be on the platform. They can't enhance their level on the platform. It's either you are approved or you're not. We're not saying this vendor is better than that vendor. They're just vetted, trustworthy. They're not going to take your card and scam it. It's that trust comfort layer. It's going to be an agent running that vendor and the reports on Yelp and wherever they send — it's going to be pulling all that data, keeping that vendor honest. And also, I have a mystery shopper program — we'll offer a random vendor at different ports some incentive to go ahead and see: does this person actually give you a receipt, and do they try to oversell you?</A>

---

<!--SEGMENT
topic: Ty's ShipSafe MCP Security Tool and MCP Marketplace
speakers: Ty Wells, Patrick Chouinard, Ryan C, Juan Torres
keywords: ShipSafe, MCP server, cybersecurity, code generation, pre-generation hooks, post-generation hooks, zero-day vulnerabilities, Claude Code, Codex, MCP marketplace, indie developers, pay-as-you-use, neuroscience UI design, Appify
summary: Ty presents ShipSafe, an MCP server that sits on the developer's local machine and checks code for security vulnerabilities against a rule set during both pre- and post-generation phases, keeping code off external servers. It stays current with zero-day vulnerabilities and is available free to members of Ty's cybersecurity coaching community. He also previews an MCP marketplace platform allowing indie developers to monetize their MCP tools on a pay-per-use basis. Ty explains his UI design process uses three competing design agents evaluated through a neuroscience archetype framework.
-->

[00:40:44] Ty Wells: Okay. So I've been talking about ShipSafe [tool:ShipSafe] for a while. What I added on to ShipSafe is the ability to — I added an MCP [tool:MCP] that's tied into your code on your pre-generation of code and the post-generation. Through one MCP server that's sitting on your own machine, so the code never leaves your machine, but it's checking it for security. This is for cybersecurity. It's checking to make sure that you're generating good, solid code against a rule set, and then you can do other things in terms of getting recommendations for fixes. And yes, you could do that in Claude Code or any of these harnesses — this has additional information. Having the skills, knowing what to run the code — this MCP service puts things in context and keeps up to date with zero-day vulnerabilities.

[00:42:37] Ryan C: <Q>Are you going to SaaS this?</Q>

[00:42:39] Ty Wells: <A>This is for another school community that people come in — it's free in that school community for them to use, because I'm a coach in that community for cybersecurity. And certainly you guys are invited. Just send me an email, I'll get you in. But you have access to some of these tools that you can then use, especially this MCP tool, to check your code as you build it. ▶ Not after the fact, because that's the thing about security — you want to build security from day one, not after.</A>

[00:43:42] Ty Wells: And then the bonus I said was: if I go and take this further, other people have MCP tools that they want to use, and it's valuable for them, but they could potentially monetize their MCP tool. And this was a platform I was working on — I built it actually — to basically enroll your MCP tool. I know there are some platforms out there now, but it's straightforward to get your tool there wrapped up. You pay very little to use it, you can bring your own key. It's sort of like an Appify [tool:Appify]. It's more of a payments platform for indie developers that have something good that they want to throw out there — really an MCP tool that has some value. Pay as you use, not as you go.

[00:44:57] Ryan C: <Q>Left field question for you, Ty. What are you using for your UI design?</Q>

[00:45:03] Ty Wells: <A>I have a skill that I have three UI design agents that compete against each other to present three options. And then I run a neuroscience archetype against that. I always look at things from a neuroscience perspective because that's the best way to look at it from a person's perspective, not just my perspective — from accumulated data. So that's how I always look at the data to present a UI that would appeal to the masses as opposed to what I might personally like.</A>

[00:46:01] Patrick Chouinard: Extremely nice product, and I'll take a look even deeper if I have a chance, because bizarrely that's the part I'm working on for the training I'm building right now.

---

<!--SEGMENT
topic: Clean Code, SDLC for Natural Language Artifacts, and Portable HTML/Markdown Format
speakers: Patrick Chouinard, Adam, Juan Torres, Morgan Cook, Mitch McCauley, Tom Welsh, Ty Wells
keywords: clean code, LLM-generated code, SDLC, natural language artifacts, agent.md, claude.md, HTML artifact, markdown payload, prompt injection, Base64 encoding, ePUB, Astro, HTMX, Claude Code, Codex, Cursor, skill creation, adversarial review training
summary: Adam raises the question of whether clean code principles (small methods, DRY) still apply in LLM-generated codebases. Patrick frames this as part of a broader problem: there is no SDLC for natural language artifacts (agent.md, claude.md files), and these need linting, validation, and security scanning for prompt injection and Base64-encoded malicious instructions. Patrick then describes a project to create a portable file format — a self-contained HTML file with an embedded markdown payload — that is human-readable in a browser and machine-readable by AI agents, enabling bilingual artifact sharing. Morgan connects this to the ePUB format. The segment closes with Patrick describing his plan to use adversarial review as the teaching example for a one-hour Claude Code skills training, using a "cake method" to show completed results without waiting for live generation.
-->

[00:46:25] Adam: Well, I had an extra monitor and laptop sitting around, so I decided to hook them all together with a virtual KVM switch, so now I've got three monitors and two laptop screens. I just thought — so I used to be really into clean code, so things like make your methods small, don't repeat yourself at all. And there doesn't seem to be any real AI tools to do that kind of thing, and it seems like the LLM-generated code doesn't adhere to those kinds of policies. So I just basically told ChatGPT, "Learn everything you know about clean code, and then write up a prompt I can put in." I didn't know what other people were doing, or if in modern agent-generated development, that stuff's just all not necessary anymore.

[00:47:40] Patrick Chouinard: <A>I wouldn't say it's not necessary — it's just another layer of tooling. And honestly, it goes back to another thing I'm working on business-wise, which is the entire SDLC of natural language artifacts inside of an AI coding assistant workflow. What you're mentioning sounds like pieces of an agent file, or a claude.md [tool:claude.md], agent.md [tool:agent.md], whatever your assistant is using. This is a building block of one of those files. Because right now, there is no SDLC that addresses natural language artifacts, and at some point we'll need one — an SDLC that does all the linting, all the validation, the actual security validation, to make sure that whatever natural language artifact doesn't have buried code, or buried statements, or even a Base64-encrypted statement in there that would be executed to do exfiltration. All of those will be the building blocks that will create the next type of SDLC.</A>

[00:49:09] Juan Torres: Yeah. And I feel that in itself, it's like a new skill that is coming up now that we're free from having to actually code. I feel like the whole cycle itself is going to be a skill in itself.

[00:49:25] Patrick Chouinard: Absolutely.

[00:49:40] Patrick Chouinard: Next one would be Juan. [*Juan's AI photo booth update and AWS/CloudFront architecture discussion follows — see next segment.*]

[01:31:43] Patrick Chouinard: This week at work, I've been working a lot into thinking about a portable file type for the agentic world. Basically, I realized that a lot of people are leveraging those tools to output HTML, but I realized that we ended up in a dichotomy where the HTML is really nice for human consumption, horrible for token consumption for AI, and the markdown is really efficient for AI, but horrible to look at for humans. So basically what I've been trying to create is a type of HTML that has a markdown payload — that gets created out of a skill — that also embeds a brand kit. So basically, it would give people inside of the company a skill that they can call to generate output that is bilingual: one version for the human to consume, one version for the agent to consume, but all self-contained into one HTML file. So you'd have the HTML file and it had a payload tag in there using a custom type of script tag where you can put the entire markdown.

[01:33:41] Patrick Chouinard: So basically, as your answer gets created in your chat interface, it outputs markdown by default. And then you simply call that skill to generate the self-contained HTML artifact, but that also gets the markdown as a payload. So that way, if you share the artifact, it will be openable by everyone in their browser. They're going to have the full detail layer and they're going to be able to give it back to their agentic system with a consumer that will know where to look for the payload and just consume the markdown — so to have the full capability in both directions, to be used as much for a human as for AI systems.

[01:34:22] Patrick Chouinard: So as soon as I figure all of that out, I'm probably going to create an open source version of that. I'm not saying I'm creating a new standard for the world, but I'm creating a standard that's going to work for me, and if it's useful for others, I'm going to be happy to share it.

[01:37:45] Morgan Cook: <Q>I recently did an electronic book, and the format for an ebook is an ePUB [tool:ePUB], which is basically just a zip file, and that zip file has exactly what you're talking about — it's got an HTML version for the table of contents, and it has an XSD version of the table of contents for the exact same kind of reason. I think the idea is sound and used in other places. And I can see this would be a useful thing to have that original markdown actually embedded with that for future use so it stays versioned together.</Q>

[01:45:37] Patrick Chouinard: I'm building an advanced training internally for a Claude Code user — beyond introduction. And I was trying to find a good example for introducing the concept of skills and how you build them. The one I fell into is what I was telling you, Ty, earlier — the concept of adversarial review. Because there's tons of examples of code review skills that exist, but a shockingly small amount of adversarial review. So I wanted to use that as the background for the demo, not to do an in-depth one, but at least to introduce the process.

[01:46:45] Ty Wells: ▶ So to give my developer the mindset of: don't just do a code review that's going to compile — do an adversarial code review that's actually going to try to break your code to make sure it finds actual bugs. And everything I've talked about earlier: do it as a sub-agent to make sure you're in a fresh context window, you don't get polluted by the context history that generated the code. Make sure as much as possible to use a different model, but at the very least, use a different context window to separate the generation from the validation.

[01:47:26] Patrick Chouinard: And I wanted to know, based on your experience, do you think I'm aiming too high, or too complex, or do you think that's something that's bringing value — if it's just actually bringing people to think about the fact that they need to do adversarial code review for stuff to be viable?

[01:47:43] Ty Wells: I think you're on the right track. You start with the climax — broken code and the result of that — and you work your way back.

[01:48:20] Patrick Chouinard: Because what I thought about using is what I call the cake method. Basically, I save a Claude Code session that's already completed with the skill already built and used. And I start a new session with broken code, show them how to create the skill and use it. But basically, when we get to the creation or the implementation of the skill, I then cut over to the second session that's already completed — because I have an hour to give that training. So I cannot wait 10 minutes for Claude Code to build.

[01:49:04] Ty Wells: ▶ Why don't you table-walk the process? Because you're teaching engineers. So you do a table walkthrough where you don't use any code at all. But what you do is, going through that table walkthrough, you identify all the steps that are in that skill. And then you simply go to Claude Code at the end and you say, "Use the skill creator." And you've documented your walkthrough — those are the steps. And then you're just initiating that in Claude Code.

[01:58:25] Fitz: Patrick, if you don't mind — I think last time you did touch on something about: do not go and copy skills from anywhere else and use them, because there's a lot of stuff going around. People hacking stuff and all that?

[01:58:32] Patrick Chouinard: <A>Well, it's natural language execution code, basically. You're executing natural language. It's really easy to hide malevolent intention — what's called prompt injection [tool:prompt injection]. It's not necessarily invisible — it's just written in a way that when you read it as a human, it doesn't seem like it's a problem. But it can be targeted at an AI to do something. And there's an even more invisible way where they add Base64 encoding — basically a little string that's Base64 encoded, innocuous to a human reading, but it contains very specific instructions. ▶ The Quebec government has actually implemented some kind of regulation for the usage of natural language artifacts in the financial industry that we will have to comply with. And there's no company right now that I know of that offers the equivalent of an antivirus for natural language — so it's techniques that exist, but no product yet.</A>

---

<!--SEGMENT
topic: Juan's AI Photo Booth App — QR Download Architecture
speakers: Juan Torres, Patrick Chouinard, Mitch McCauley, Ty Wells
keywords: AI photo booth, QR code, CloudFront, Amazon S3, EC2, iOS Safari, iOS Chrome, image download, browser detection, diffusion model, image-to-image, Whimsical, CloudFront signed cookies, OAC, Terraform, FastAPI, Flask
summary: Juan presents his progress on an AI photo booth application, focusing on solving a complex cross-browser image download problem. He built a decision tree (diagrammed in Whimsical) to handle Safari iOS, Chrome iOS, and Android Chrome differently — Safari allows parallel batch downloads to the Photos app, while Chrome iOS requires individual saves. He also explains his AWS architecture: images stored in S3, served via CloudFront with OAC and signed cookies, decoupled from the EC2 instance to reduce egress costs. Mitch asks about the egress setup, and Juan explains the CloudFront-to-S3 connection and cost advantages.
-->

[00:49:44] Juan Torres: Hey, folks. Oh, I haven't — I had to resolve a lot of — spent a lot of time resolving the QR problem with the AI Photo Booth [tool:AI Photo Booth] application. The main reason it became a problem is I'm reaching a point in which I think I've systematized a really good methodology to assess non-deterministic outputs by the agentic systems from LLMs and now with diffusion models. The problem with the QR code was mainly the result of: when you have a phone, you have two main browsers — Safari [tool:Safari] and Chrome [tool:Chrome]. There are different modes in which you can download several files from the application. Chrome in iOS doesn't download several files in a normative way, so I had to find a methodology for my system to be able to read which browser the user is using — whether Safari in iOS, Chrome in iOS, Chrome in Android — so I had to create quite a complex system for the person to be able to download the images as soon as possible.

[00:51:50] Juan Torres: So I was able to get a sweet spot because the main thing I'm trying to do is make it obvious, make it attractive, make it easy, and make it satisfying. ▶ The responsibility as an engineer is to pre-suppose possible permutations and deal with the complexity of the system so that the end user doesn't have to.

[00:52:24] Juan Torres: I have a diagram. Whimsical [tool:Whimsical] is my whiteboard now. So this is the decision tree on dealing with this. The main transition — IO egress data comes from CloudFront [tool:Amazon CloudFront], right? This was a conversation I was having with you guys two weeks ago — I decouple IO egress internet traffic away from the EC2 instance [tool:Amazon EC2]. In the future, it's going to be out of a load balancer. But for now, in beta mode, a T3 x-large EC2 instance is enough to carry out an event. But I decouple the IO egress data transfer processing away from the EC2 instance into CloudFront because it's better, more cost-effective at handling data transfer.

[00:54:00] Juan Torres: Are any photos ready? No, still rendering. We poll every four seconds so the photos appear. If they are ready, you wait 15 milliseconds so that thumbnails get bandwidth into the QR code page. Pre-pack one photo — at least one photo is going to be already pre-packed when you load the page. The reason why is because when I was pre-loading all the pictures, there were issues with too much information being loaded into the page.

[00:55:26] Juan Torres: If you're using iPhone Chrome, then you have to download the images individually. There's no mechanism for Chrome in iOS to download several images at the same time. If you have Safari, then you can run a save-all parallel fetch of three images concurrently, show progress cards, and photos are already preparing in memory — the share menu opens immediately. One of the issues was that instead of downloading into the Photos app, it was downloading into the Files app of the iPhone. So I didn't want that because most people actually want their photos saved into their photo apps instead of their files apps.

[01:00:49] Mitch McCauley: <Q>I was curious about the egress situation and hosting media. Is it actually that simple — you just give a media link and they just pay for egress every time they request it or download it?</Q>

[01:00:49] Juan Torres: <A>Yeah. Well, the egress from CloudFront is relatively cheap. What happens is you have your media in a data lake, right? There is a particular link — it's through an OAC connection — that the data in your data lake, being images or videos, goes into your CloudFront. And then CloudFront issues signed cookies and authorization only — flow back into the EC2 instance in order to pick up on processes, on metadata. But the application itself picks the thumbnails and picks the images directly from Amazon CloudFront. And I found that Amazon CloudFront is cheaper, and especially since you want the EC2 instance or the auto-scale group to handle the specialized computational necessities solely. CloudFront is specifically for this.</A>

[01:03:37] Juan Torres: And guys, this is made again with Terraform [tool:Terraform]. I don't have to do any Terraform coding. I just tell Claude Code to create a plan for the development — hosted in an EC2 instance, Ubuntu, 40 gigabytes of memory. All those specs, the security mechanism — created in a private subnet within a specific VPC with specific VPC endpoints in order for it to connect to the S3 bucket. All those things you can specify to your Claude Code or even your Cursor IDE in order for your agents to develop the CloudFront code. And if you have the right permissions — which is something I do manually — the only manual thing I've done really is to give my IAM role and my user the right permissions in order to create resources, read resources, and edit resources.

[01:05:00] Patrick Chouinard: And as I said a couple of weeks ago — as soon as that application goes online, let me know. My boss would love that for our next Christmas party.

---

<!--SEGMENT
topic: Morgan's Google Workspace Automation and Looker Studio
speakers: Morgan Cook, Patrick Chouinard, Mitch McCauley, Juan Torres
keywords: Google Apps Script, Google Workspace, Google Sheets, Firebase, Looker Studio, data synchronization, spreadsheet automation, queue processing, Flask, FastAPI, Docker, data dashboard, stakeholder access, agentic access
summary: Morgan describes building a Google Apps Script automation for a foundation that uses Google Workspace — moving data between multiple spreadsheets, managing folder attachments, and running a queue-based background process triggered from a menu. He notes the system is hitting the limits of what Apps Script can do and may need a proper database. Mitch demonstrates Looker Studio as a way to create dashboards from Google Sheets data. Juan suggests Flask as a lightweight data web application alternative for displaying and filtering data, and describes using Docker Compose to run FastAPI and Flask together.
-->

[00:05:41] Patrick Chouinard: Next one I would say would be Morgan.

[00:05:49] Morgan Cook: Hey guys. I've been working this last week on Apps Script [tool:Google Apps Script], basically a bunch of automations. This foundation uses Google Workspace [tool:Google Workspace], and they manage a lot of their stuff in spreadsheets and documents and emails. So I've been trudging my way through Apps Scripts. And so that's really what I've been working on. They're pushing the limits of what they can do with Apps Scripts in a spreadsheet. It's like, okay, you're at the point where you really ought to just stick this in a database. And if you want to stay with Google products, I guess we'll use Firebase [tool:Firebase].

[01:07:00] Morgan Cook: It's just their workflow itself — they have multiple spreadsheets and the data needs to move from one spreadsheet to another through the process and then back to the original and into a historical archive, and there's an attached folder of files that are moving along with all this stuff into different shared drives. It's functional and it's working. There's a trigger process — they can request a specific thing from a menu in their main spreadsheet, it'll add it to a queue, and then a background process picks that up to run the actual process against the data. So they set states in the spreadsheet, fire off a request, and then it goes through and does the work eventually. And the queue updates itself from queued to running and completed.

[01:08:06] Morgan Cook: Any more requests, then we've got to redo something into a database. And I think we might end up there when they want to build a dashboard for the people that need to see some of the content but not actually operate on the content. And the problem right now is Google's authorization layer to the resources is not convenient to that.

[01:08:44] Mitch McCauley: <Q>Have you looked at Looker at all?</Q>

[01:08:47] Morgan Cook: <Q>No, I haven't. What is Looker?</Q>

[01:09:04] Mitch McCauley: <A>Give me a more description about it — it's really cool because you can basically have Looker [tool:Looker Studio] use the data source as the Google Sheet, and then you can do augmentation right on the preview level to the data level on the Google Sheet as the data source. You can connect multiple spreadsheets and do queries, just like SQL queries.</A>

[01:09:30] Morgan Cook: So the spreadsheet becomes more like a data view into the database?

[01:09:30] Mitch McCauley: Yeah. It is like a basically simple front end to any website. And then you can share it just like a Google Doc kind of thing. And then you can have tabular views, you can have graph views. I would say with what your use case is, I think Looker is definitely the spot that I would unironically look into. I 100% recommend that.

[01:12:54] Juan Torres: <Q>Morgan, are you trying to be able to display all your data to stakeholders? Is that why Mitch is showing you this?</Q>

[01:12:58] Morgan Cook: <A>Yeah, there's a group of stakeholders that are outside the foundation that need to see into the data, and then there are different levels within the foundation — like there's the administration of the foundation, and then the foundation runs a bunch of houses, and the houses are managed, and so the house manager only has access to their own content, not to see all of the other houses.</A>

[01:13:24] Juan Torres: ▶ Another suggestion is creating a Flask [tool:Flask] web application. Flask is really good for displaying data, and it has really good table formats. That's what I always use in order to display my data and filter it accordingly to my needs. And also to be able to see the outputs of each iteration in my agentic system. So I would say have your front-end application and then have a folder in which you have your data web application — Flask application. For this app that I just showed you, I have a Docker Compose [tool:Docker Compose], which has two images — mainly the data web application and then the front-end application. So I can trigger the starting of FastAPI [tool:FastAPI] and Flask with one terminal command.

---

<!--SEGMENT
topic: Mitch's YouTube Content Pipeline and Team Version Control
speakers: Mitch McCauley, Juan Torres, Patrick Chouinard, Adam
keywords: YouTube monetization, image-to-video, text-to-image, GPT Image 2, Kling, Wavespeed, OpenRouter, GitHub, CI/CD, GitHub Actions, NGROK, version control, feature branches, Codex, static HTML, video generation, diffusion model leaderboard
summary: Mitch shares that his YouTube channel is now monetized and demonstrates a static HTML prototype for a content pipeline application that manages AI-generated video thumbnails and first frames — handling prompt editing, retake requests, queue management, and output review. He asks the group for advice on managing version control for a non-technical team. Patrick recommends creating a GitHub org with forks so team members work in isolated environments. Adam suggests using Codex's web interface to handle branching and pull requests automatically. Juan recommends feature branches, GitHub Actions for CI/CD, and NGROK for sharing staging environments. The group also discusses image generation model selection, with Juan sharing a text-to-image leaderboard and recommending Wavespeed as a unified API gateway for multiple diffusion models.
-->

[01:15:36] Patrick Chouinard: Next would be Mitch, the revival of the Mitch. What have you done lately and what can you share with us?

[01:15:41] Mitch McCauley: Yeah, I mean, I've just been — I got my YouTube channel monetized, so that's been good.

[01:16:00] Mitch McCauley: So basically making static HTML previews of the application that I'm wanting to build. Basically, before this whole part, you put in the contents — you're not having AI really make the idea itself or the text that is then used to make the queries to make the request to the AI. This is just like a nice front end of all the different requests. Instead of having to put all of my clip contents in TXT files, I can just copy and paste it in a specific format and then it will generate the requests so I can basically choose a winning first frame for my vertical or horizontal thumbnails. I have a series of images that are the starting frames for each of my videos. And so there's 25 different starting frames throughout the whole video. I can click here and I can edit the prompt if I want to, or I could request a retake — and it really just gets added to the queue. And the dialogue is to see what the actual words are being exchanged that I can edit and audit if needed.

[01:17:48] Mitch McCauley: And then for outputs, this is the final output — where all those different videos live. That's what I was asking you about, egress and some other media hosting stuff. And then basically they can request a simple retake or download all the different videos, and they can choose all 30 videos, only the newest retake, the landscape and the portrait version.

[01:19:27] Juan Torres: <Q>For image-to-image or text-to-image — what is the model that you're using right now?</Q>

[01:19:57] Mitch McCauley: <A>I was looking at mostly Nano Banana, like the lightest one. Cost isn't that big of a factor because these videos aren't meant with the idea of making money. I actually thought GPT Image 2 [tool:GPT Image 2] made some really good realistic images.</A>

[01:21:00] Juan Torres: ▶ This leaderboard of text-to-image generation is pretty decent in accuracy, and I think people who are interested in diffusion model engineering should look into this just because it gives really accurate information as to really good models. Right now GPT Image 2 is really good. [link:text-to-image generation leaderboard]

[01:22:27] Juan Torres: <Q>Have you tried Wavespeed [tool:Wavespeed] as your general API recall tool?</Q>

[01:22:35] Mitch McCauley: <A>No, I've never heard of it.</A>

[01:22:36] Juan Torres: <A>Wavespeed has basically all the main models. So if you were to use Wavespeed, create an account, put a couple of credits — I don't think it's that expensive — you can use GPT Image 2, you can use Gemini [tool:Gemini], you can use CogVideoX for image generation, for video generation. And they actually have a CLI so you can use it to basically ask questions about documentation and creating workflows. ▶ So I recommend you check them out. If you wanted to systematize it into your whole data web application, it would be a good fit.</A>

[01:23:19] Mitch McCauley: Yeah, I was thinking about just using OpenRouter [tool:OpenRouter]. I know they take a classic 5%.

[01:23:38] Mitch McCauley: And then for my question for the class: so basically we have a data provider that hosts all of the Amazon data in very unique ways for the accounts that we manage. Now I have a fixed IP at a Digital Ocean droplet [tool:DigitalOcean], and we make requests through there. I'm introducing this to the team and we're going to have to bring everyone on as far as doing a request through this actual company IP address. This is the first time that AI is going to make requests for them and take insights from that data so they can basically talk to the data. So I'm presenting this tomorrow. And I've already had all the queries and all this other stuff kind of mapped out so they don't need to do all the complex stuff. But I'm probably going to have to create a GitHub project. And I've done this before, but they don't use GitHub. So it's like all this stuff is great — CI/CD is great — but people have to use it and they don't even know how to use it. So they just use Google Drive, and they download it, and that's what they've actually used instead of GitHub.

[01:27:37] Patrick Chouinard: <A>▶ Listening to what you're saying, what I would try to do is probably create an org in GitHub that you share with them, and basically you get them to fork your code in there. And then at the root of your project, you can put a little instruction file for the AI that they can reference in order to update their fork. But that way they work in their own environment, so whatever they screw up, they can't screw up your main project, and they still have a tie-in that the GitHub mechanic will allow them to get updates from you.</A>

[01:27:46] Adam: ▶ Yeah, the Codex [tool:Codex] web interface handles that all for you. If they just have a ChatGPT account, you could just tell it, "Hey, change the color to background," it'll create a fork, a branch, it'll push that branch back up to GitHub, create a pull request, and as the code owner, you'd have to approve the pull request.

[01:29:20] Juan Torres: ▶ If you practice good CI/CD discipline — ideally have your data engineer work on a migrations folder, have your front-end person working on the front-end folder, and then have GitHub Actions [tool:GitHub Actions] in order to automate the process from local development environment to pushing it to the staging environment. And just create a CLI command for someone to just push — for them to be able to generate the NGROK [tool:NGROK] tunnel URL for them to see your web app.

---

=== UNRESOLVED SPEAKERS ===

- **Ryan C** — Last name not provided; appears in alias map only as "Ryan C." Passed through unchanged.
- **Adam** — No last name provided in transcript or alias map. Passed through unchanged.
- **Fitz** — No last name provided. Passed through unchanged.
- **Eric Tsai** — Passed through as given; not confirmed in alias map.
- **Morgan Cook** — Passed through as given; not confirmed in alias map.
- **Mitch McCauley** — Passed through as given; not confirmed in alias map.
- **Juan Torres** — Passed through as given; not confirmed in alias map.
- **Brandon Hancock** — Passed through as given; not confirmed in alias map.

*(Note: The `SPEAKER_ALIASES` context block resolved `pchouinard` → **Patrick Chouinard** for the second recording segment. All other speakers were passed through as transcribed.)*