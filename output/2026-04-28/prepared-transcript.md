=== SESSION ===
date: [Not specified in transcript]
duration_estimate: 88 minutes
main_themes: AI coding assistant workflows, custom wearable hardware for personal intelligence, RAG architecture for community knowledge, multi-model strategies for development, enterprise vs. consumer AI tool limitations

<!--SEGMENT
topic: Custom Wearable AI Devices
speakers: Ty Wells, Patrick Chouinard
keywords: Limitless, Fieldy, wearable, 3D printing, camera, privacy, capture device, firmware, Supabase, golf training, Telegram
summary: Ty Wells presents a custom-built wearable device with camera capabilities intended to replace his expiring Limitless subscription. He discusses 3D printing the prototype, integrating with Supabase for data storage, and use cases ranging from golf swing analysis to restaurant staff training. Patrick Chouinard raises privacy concerns regarding continuous video recording in public spaces.
-->

[00:00:17] Patrick Chouinard: I have some news on the evolution of my community brain project processing the last two years of coaching calls.
[00:00:30] Ty Wells: You had a busy weekend then?
[00:00:33] Patrick Chouinard: Always.
[00:00:37] Ty Wells: My wife went out of town, so there were some late nights. I was switching between TOCA accounts constantly. These things are getting burnt. And then Claude [tool:Claude] was down today, so I went golfing early.
[00:00:54] Patrick Chouinard: I don't think it was down everywhere because I didn't have too many problems. I was giving training.
[00:00:59] Ty Wells: It was down for me and it could have been Opus [tool:Claude Opus]. Usually I keep forgetting to switch when it's down, switch to Sonnet [tool:Claude Sonnet]. I just was like, no, I think I'm just going to go play nine holes. That way I managed to get out.
[00:02:00] Ty Wells: I'm trying to, I have my Limitless [tool:Limitless]. I know you have your Fieldy. I'm going to send a request. I'm going to show you a picture.
[00:02:24] Ty Wells: I've been working with a guy that does 3D printing, but basically I'm creating my own.
[00:02:32] Patrick Chouinard: Okay.
[00:02:32] Ty Wells: This one has a camera built in and that's your light indicator and then your microphone. Are you sure you're not in the same realm as what OpenAI [tool:OpenAI] is working on?
[00:02:49] Patrick Chouinard: Don't care what they're doing.
[00:02:51] Ty Wells: Can't stop them. But I just need, I wanted to talk to the group about that because there's no real platform. My Limitless ends in September, so I've got to find a replacement. I think video, there's so many use cases for video, not just for what I do, but to be able to capture those screenshots and apply them for training. Actually, I'm doing it for my golf swing, too, because I want to make sure I'm getting through to the other side. If it's recording and see where my hands were, it's a whole thing. Of course, this is the one time my buddy's all interested because it's golf related. He doesn't want anything to do with this meeting being recorded. He wants the results of it. He says, yeah, I'll get one from you.
[00:34:00] Ty Wells: This is the image. My Limitless device, Meta bought them, they killed the project or whatever, that ends in September. So I'm trying to build my own. This is a prototype of what it looks like, with a camera, because this one just has microphone, but a camera here, that'll be indicated if it's recording or not, and that's your speaker, USB-C, so I'm trying to put this together. That would be that capture device. Especially when I'm doing my user-driven development, I'm able to capture the entire moment, not just a Zoom recording or anything, but actually what I'm doing, what I'm saying. More so this is my golf swing, so I can see better, take some analytics and apply that to golf, to training new people at a restaurant, all kinds of different things, right? Inspections, real-time feeds of that and looking at it and assessing that.
[00:35:51] Ty Wells: I've been working on these, all of those little parts are all coming together and pushing signals. I've been working on this probably last few months, at least, maybe even from last year, off and on, just building those different pieces. Like I said, this is one of six layers. That's just the bottom layer. I've got five other layers on top of that.
[00:36:33] Ty Wells: The repo, I'm going to put a public repo out there for Propria [tool:Propria] just because it's for me, it's my stuff, but everybody could use it. No matter what devices you have, you just plug in whatever devices. But I get accurate information to my phone. I try to kill the noise and get true information to Telegram [tool:Telegram] where I can reply, yes or no, to whatever. And then it reflects on that data every day, so it gives me a better, and it learns, captures memories and stuff that I can add that will add value to the next iteration that comes.
[00:37:43] Patrick Chouinard: You don't want to run the Limitless all day, and I have the same issue with Fieldy, because mine captures every single YouTube video I listen to while working. It screws up the signal a little bit, especially if you're context switching.
[00:38:09] Ty Wells: It'll mess up the context. I'm trying to get it to say, hey, this was wrong. Hopefully my new device, I'm able to do a lot more with it, because obviously, I've got the firmware and everything ready, I'm building it on my own. I want everybody to have one of those because again, it's personal thing that you can use to capture another capture device, you're not tied into any contract. This thing cost me $10 to print the 3D thing. The device is like $25 for that XIO board. Now you just take the firmware, you fork it and do whatever you want to do. Then you have it goes to your database, which mine is Supabase [tool:Supabase]. Then you can manipulate that information as best as you want or use it in whatever form you want.
[00:39:24] Patrick Chouinard: I'm going to be really curious to see also what you do with privacy concern when you're closer to release.
[00:39:32] Ty Wells: I'm not sure exactly how I'm going to tackle that in terms of the camera. The other thing I was going to do is put a GoPro [tool:GoPro] on my head and let it walk around with it all day with its red light flashing, indicating that it's recording. What's the difference? Does anybody know?
[00:39:55] Patrick Chouinard: It's more as to how you publicize the fact that you're recording so people around you are aware, because that's also a concern I have with the Fieldy just being an audio recording device that records all day. I can't imagine with a camera on top of that.
[00:40:14] Ty Wells: The camera is definitely a challenge for me. I'll have a version without the camera. As long as you can turn it off and there is some kind of visual confirmation on the device that the camera's off, maybe a different color LED or something.
[00:40:33] Ty Wells: I think the same thing that they use on the webcams, a little slider against the lens, that might work.

<!--SEGMENT
topic: Global Training Logistics and Prompt Engineering
speakers: Patrick Chouinard, Tom Welsh, Ty Wells
keywords: prompt engineering, training, Claude Code, Codex, global teams, timezone, LLM, AI models, Singapore, London
summary: Patrick Chouinard discusses scheduling challenges for global AI training sessions across London, Paris, Sao Paulo, and Singapore. The conversation shifts to whether prompt engineering will become obsolete as models improve, concluding that understanding how to communicate with AI will remain essential even if structured prompting evolves.
-->

[00:03:48] Patrick Chouinard: Hey, Tom.
[00:03:50] Tom Welsh: Hey. I was sorry, I didn't realize I was on mute earlier. I was saying, I'm awake just now. I'm not sure for how long. It's been crazy mad, another 13 hour day.
[00:04:07] Patrick Chouinard: Actually, I'm training a bunch of people from your neck of the wood tomorrow morning at seven, my time.
[00:04:14] Tom Welsh: Nice.
[00:04:17] Patrick Chouinard: I have the weirdest class tomorrow morning. We've scheduled some off hour training for people around the world in the other divisions, but this one is like 7 AM Eastern time. And I have people from London, makes sense. Paris, for a French, for an English training session. Not sure, but okay. Sao Paulo, basically 7 AM their time. You truly want to get trained. And then people from Singapore, like, what? It's like 10 or 11 at night for them.
[00:04:55] Tom Welsh: That is the thing with the UK. I used to run a data center here and I was the linchpin between East Coast, U.S. and Australia. So I'd take the hardware from Australia and pass it off to America in the evening. We always had the longest days. Everywhere else I had 8 hour days, we had 12.
[00:05:15] Patrick Chouinard: No, but the weird part is I gave that same training on Monday at 9 AM their time in Singapore. But somehow they decided to register for the one at 10 PM their time tomorrow morning. Like, okay, why not?
[00:05:30] Tom Welsh: That's because they're diligent. They want to work at 9 AM and they'll sit at home and do it properly in their own time.
[00:05:39] Ty Wells: What are you training on?
[00:05:41] Patrick Chouinard: Tomorrow is the advanced training on prompt engineering for business folks. Not the basic basic, but a little bit more advanced, let's say.
[00:05:58] Ty Wells: If you look at the technology over the last, just the new inventions of technologies and stuff, training is sort of tough. I'm wondering if prompt engineering is going to go away at some point with some new models, what's the guy need?
[00:06:17] Patrick Chouinard: To a degree, but you still have to understand how to talk to the AI. So not as structured as it is today, but you still need some kind of a prompt engineering structure.
[00:06:29] Ty Wells: I think I agree with that, the better, especially if you're developing something that's complex. Complex, you really need to know how those things, well, software engineering, but also then how to change, turn that software engineering into prompt engineering to deliver the same results. That's always going to be.
[00:06:49] Patrick Chouinard: And that's going to be my afternoon training where I do the introduction to Claude Code [tool:Claude Code] for another class in the afternoon. That's going to be fun. A training that actually was written by Claude Code based on our training curriculum, updated through the output of the changelog from the Claude Code repo. So every time there's a change in the changelog, I use that as signal to go search on the documentation to update the training material accordingly.

<!--SEGMENT
topic: Claude Code Performance and Multi-Model Workflows
speakers: Juan Torres, Patrick Chouinard, Ty Wells
keywords: Claude Code, Cursor, Codex, performance, latency, OpenRouter, Kimi K2, Sonnet, model bias, planning, offline processing
summary: Juan Torres raises concerns about Claude Code's significant slowdown over the past two months, prompting a discussion on multi-model strategies. Participants recommend using Claude Code for initial architecture and planning while switching to faster alternatives like Codex 5.5 or Kimi K2 for intensive editing, and mixing models to reduce individual bias.
-->

[00:08:31] Patrick Chouinard: I'm going to make sure to answer our good friend Juan. Basically, what you've posted is, I noticed Claude Code slowing down significantly over the last two months. It got to the point which I rely more and more on Cursor [tool:Cursor] instead of Claude Code. So do you want to elaborate on exactly what you're looking for from the group?
[00:08:56] Juan Torres: <Q>How are they using Claude Code? If they're balancing that with the utilization of other models within Cursor or CLI-based ones, like Kimi K2?</Q>
[00:09:15] Juan Torres: I know Vastgen was using GLM [tool:GLM], and the reason that I'm asking is because I don't know, I know people have noticed the slowing down of Claude Code, but it's getting to the point in which it's pretty slow for me in terms of trying to get things done.
[00:09:44] Patrick Chouinard: <A>Well, on my end, what I've been doing is I work with Claude Code a lot offline. So basically, it runs in the background. I do my planning with it off hours. Basically, the time that it's most performant. Once the plan is done, I launch it and then I go do something else, and I monitor it using remote control. Meaning that even though it's slower than usual, it's okay, I just look at it once in a while and just keep it working. But when I do intensive back and forth, I find that right now, Codex [tool:Codex] is extremely fast. 5.5, honestly, you can barely see any difference from Opus, actually, it might even be on top of it some of the time, depending on the task.</A>
[00:10:38] Ty Wells: I wouldn't touch Cursor in ages, but yeah, it's definitely slower, it is frustrating. I'm working, I got my Proxmox [tool:Proxmox] set up, I've got another 3090 I'm adding in, and then I'll be good for Kimi 2.6. To run on that, so that should be good, but I plan on offloading to my Proxmox after the planning. I agree with you, Patrick, on the planning. I did some planning with ChatGPT [tool:ChatGPT] yesterday, oh my God, it was really good. I was like, whoa, this is a transitional period here.
[00:11:30] Patrick Chouinard: Right now, I would have to say my daily work is not single model anymore. I do a little bit on one, a little bit on the other. I mean, ideation, Claude still pretty much the best overall architect brain, but creation Codex does very well, code review Codex does extremely well, research, it's always Gemini [tool:Gemini]. It's not an insane coding model, but if you send it on a retrieval job, it will chug along and do it perfectly well. I tried to use a little bit of token everywhere instead of putting everything under the Claude umbrella.
[00:12:19] Juan Torres: I guess just, because I do planning and architecture through Claude Code, but then when it's done, I tend to try to follow up on Claude Code to do some of the revisions, some of the changes. Perhaps what I can do is continue to use Claude Code as my architecture and planner and then switch to Gemini or Codex 5.5 in order to do a lot of the editing back and forth that's pretty quick. I think that's what I can do.
[00:12:58] Patrick Chouinard: Yep. Honestly, when I figured out that when you mix models in your daily work, it increased the quality as well because each model have different bias. So one will detect the bias of the other way more than a single model reviewing itself.
[00:13:24] Ty Wells: Absolutely. It's a game changer. It gives you a different perspective. The code builder reviewing its own code, that's never going to work.
[00:13:34] Ty Wells: But also in the planning stage, sometimes I give Claude back its own plan. It's like, wait a minute, who wrote this? There are some issues here.
[00:13:47] Patrick Chouinard: Yeah. And the last thing I've seen is, and I know a lot of people will look at this and like, what are you talking about? But give personality to your coding model. Especially in the ideation. I know it sounds stupid, but it will give you feedback. It will challenge your idea more. And when it does, sometimes it's going to make you laugh because of the way it makes the comment. And it's going to stick in your head way more. You can have the same exact perfect response given flat, you're going to have forgotten it five seconds later. If it put a little bit of personality in it, you're going to remember it for days.
[00:14:28] Patrick Chouinard: I mean, I just gave a training today and it was an expert level training. We gave them a bunch of prompts. We went through to the level of getting people to do an agentic process manually. So basically doing the loop themselves to understand what the AI would do. The one thing they all remembered is they wanted three lines of personality for Copilot [tool:GitHub Copilot]. That's the thing that everybody cheered on. Just the fact that Copilot was actually responding with a bit of sass, bit of personality, it made them laugh, and they remembered what the AI told them as a pushback.
[00:15:20] Juan Torres: Nice.
[00:15:21] Ty Wells: The bonding thing, right? When you get these responses, they make some emotional attachment to those responses. I find myself laughing at my personality stuff that I get back all the time.
[00:15:48] Patrick Chouinard: I've used it with the Excalibur MCP [tool:Excalibur MCP] this weekend, and it created a diagram, but there was a lot of crisscrossing arrows. So I told it, please take a look and remove all of those and clean it up. The moment you see your coding agent reply with, oh, crap, there's still some that are crisscrossing. Let me go fix it. You're going to remember it.
[00:16:18] Patrick Chouinard: So, yeah, it's weird. It's a psychological trick, but it works extremely well.
[00:16:34] Patrick Chouinard: Let me post the order. And before we start, I'm just going to update everyone because last week I've talked about the fact that I was working on a community brain project. Basically, I'm ingesting the transcript from the past two and a half years worth of coaching calls. Brendan was nice enough to actually supply me with all of the transcripts. For the past two months, I've been digesting every single week, the transcript plus the chat logs. I'm putting all of that into a... I've been improving the pre-processing way more than chunking and embedding. Actually, chunking and embedding in this project is doing the least amount of work. Like 99.9% of the work is all the pre-processing because I realized one thing, most RAG systems are designed to ingest documents that are sequential information. So you can chunk it in size and it still makes sense because it's a sequential document. But for conversation, absolute crap, because you have a discussion that a subject starts, then stops, then starts over again, 20 minutes later. And you have to re-aggregate all of that together. I've done a lot of work in the pre-digestion. I only have six transcripts for now too, because it's quite expensive to process. Once I've nailed the preprocessing, I'm going to do the entire two and a half years. Here it gives you an idea and it's GPT-OSS. So nothing, it works perfectly well locally. You see the question I gave is, what's the connection between content creation strategy and AI consultancy sales funnel? This is not find the information in the transcript, this is ask a question as if you were in the coaching call itself. You could see the thinking process and the actual answer. It really stated what content does, how it fills the funnel, and the evidence from the transcript. It talks about what Brendan mentioned, Adam, you see it referenced exactly when did that happen, where it happened, in which information, plus all the thinking. A very basic model, so GPT-OSS, nothing too fancy, but the way I pre-processed the information that's made it so I can ask an architectural question to it instead of simple, go find me this information.
[00:20:35] Ty Wells: What are you using to pre-process?
[00:20:38] Patrick Chouinard: It's actually a pipeline that I've created in N8N [tool:n8n], that have a series of prompts. The first one pre-processes the transcript, so it re-aggregates all of the transcript sections together in topics with a bunch of metadata. Then the second pass, it extracts signal, so it's going to extract all of the question and the answer. The question that don't have answer, it's going to extract a summary of the entire conversation. It's going to extract all of the insight that were surfaced. A lot of metadata processing, a lot of additional data inferred from the content. I even now ingest the actual community post that I post called Recap Flow every week. All of that together, inside of a fully detailed schema that shows the link between each information and the source transcript information, gave me so far the ability to go, and this is not even the final model. Now, I'm finalizing a version that merges in an hybrid model, both the vector search and keyword search as well. So I'm expecting the result to be even more interesting.
[00:22:20] Ty Wells: Did you consider the new DeepSeek [tool:DeepSeek] version? I tested that out the other day. It's not as fast, but it gets to the same result, and it costs way less.
[00:24:09] Patrick Chouinard: Way less than what?
[00:24:07] Ty Wells: Than Sonnet. But I've tried Kimi K2 [tool:Kimi K2], I've tried DeepSeek, I've tried MinMax [tool:MinMax], I've tried GLM. I've tried all of them, and none of them actually has the reasoning for the first two phases. After that, I can use smaller model, no problem. But those two steps, they would truncate, they would not understand the whole. To understand two hours' worth of transcript, it's a very big job.
[00:24:48] Ty Wells: What were the first two steps?
[00:24:49] Patrick Chouinard: The preprocessing. So basically taking every statement in the transcript and reorder them to group them into topics. So it has to understand the entire two and a half hours' worth of transcript to do that phase. The second is extracting signals. You're going to have access to all the prompts when I'm done. I'm working privately right now, but as soon as it's deployable, I'm going to open source the project in GitHub. The solution is made to be self-hosted. It uses a bit in the preprocessing phase, but I already provide you with the full preprocessed database anyway. Afterward, it's just a matter of running GPT-OSS on Ollama [tool:Ollama] from an OpenWebUI [tool:OpenWebUI] interface. Everything's local, everything costs zero to interrogate as much as you want. Once you have the VectorDB, you can build whatever you want on top of it.
[00:25:50] Patrick Chouinard: Ty, if you want to build on top of the knowledge, the aggregated knowledge of the community or anyone else, have at it.
[00:27:46] Patrick Chouinard: For the question about how I do the embedding in the VectorDB. The embedding, really easy. Since I've done all the preprocessing before, I rely a lot less on the quality of the embedding. So I was able to do it with Nomic [tool:Nomic], the free embedding model that runs with Ollama. So zero cost for the embeddings. And the VectorDB, I've used LanceDB [tool:LanceDB]. So a very minimal infrastructure that can run on anyone's machine that doesn't need any install, any configuration. I mean, you just tell Claude Code, please install LanceDB and you're done. I tried to make it as easy as possible for anyone to grab it and use it once I've done the heavy lifting. I'm also going to have in there all of the preprocessed material. So not only the data itself, the vector database, but also the preprocess prompts, the extracted insight textually. People will be able to take that project from any step in the pipeline I created and switch wherever they want to take the pipeline on their own.

<!--SEGMENT
topic: Tom's Legacy Membership System
speakers: Tom Welsh, Patrick Chouinard, Ty Wells
keywords: Supabase, Vercel, membership system, data cleaning, security, JWT, welfare gate, audit trail, Resend, invite-only
summary: Tom Welsh demonstrates a membership management system for a regimental association built with Supabase and Vercel. He addresses challenges with legacy Access database migration including deceased members and data corruption, and showcases a "welfare gate" security feature with double authentication and comprehensive audit logging for sensitive welfare data.
-->

[00:41:08] Tom Welsh: I've been writing a membership system for my regimental association. The background is it was an Access database. Everyone has right now. And they couldn't get the system working. So they stopped putting data into it in 2016. So you can imagine a lot of this data is completely buggered. I've got five and half thousand members, probably 30% are dead. I've got an age spread of 38 to 127. So I'm guessing everybody above 100 is probably gone. Because we know we've got four centenarians in our association. We haven't got 127 of them. That in itself has been challenging.
[00:42:00] Tom Welsh: I've sucked stuff into members, and we've got branches. A lot of the stuff came across, like 180 for a mobile number, stuff was duffed in left and centre. I started playing with some other stuff. I like this. We've got an email outreach, which is basically a markdown editor, set some stuff up, get some emails, and get a nicely formatted email that comes out to everybody. Currently we haven't got a piece of comms policy, so this is because one guy writes and just sends it. It's basically a crappy email, just looks like a dog's dinner.
[00:44:09] Tom Welsh: We do a lot of welfare through what we do, and this is obviously pretty sensitive, so I've got what I call a welfare gate. So you log into the system, Supabase Auth [tool:Supabase], you then go to welfare, you have to double log in again, which gets you here, then you can start looking at information. Everything we do gets logged, so I've got a good old audit trail going on. That's basically my little app. I've got a campaign thing here going on, where we can start building out campaigns. I call it the studio.
[00:45:13] Tom Welsh: The majority of this is all done prompt gramming through Cursor [tool:Cursor], because I'm not made to jump to Claude Code at all. This month was quite depressing because I got a $48 bill. It's the first bill I've had.
[00:45:40] Tom Welsh: I'm interested in any kind of security kind of stuff we can get around. This is my welfare gate. You confirm your password again before you go back in again. It times out after 15 minutes. That's using JWT [tool:JWT]. Using keep you in and out.
[00:48:00] Tom Welsh: If somebody does something untoward, we can see who did it when, to play the blame game that we never play.
[00:48:25] Patrick Chouinard: Do you know where it's going to be deployed?
[00:48:28] Tom Welsh: Yes, it's going to be on Vercel [tool:Vercel] with Supabase backend. Because I'm using Supabase and Supabase auth. So Vercel makes a logical choice.
[00:48:37] Patrick Chouinard: You're doing email auth or you're doing Gmail?
[00:48:46] Tom Welsh: No, I'm doing invite only. So you create the system with the admin and the admin then can add people and send email invites to them who then get authenticated.
[00:49:10] Patrick Chouinard: None of this super duper nice and click and log in with Gmail because it's a pretty much closed system. We're going to get five users for it in the association headquarters.
[00:49:19] Ty Wells: One thing I would add, Tom, is an OTP login, login with a code. Just because if you put passwords on there, I don't know what your password rotation policy is, but obviously it makes it a lot easier. You won't forget your email. You'll forget the password over and over.
[00:49:43] Ty Wells: Log in with the code. Their emails, because you're inviting them, you know that email is legit. If they log in with the code, they're sending it to an email, which you know is legit. It's not going to any other email.
[00:49:56] Tom Welsh: Yeah. I'll bear that in mind.
[00:50:00] Patrick Chouinard: Whatever you can give out to a piece of infrastructure. It's the same thing I told my gym manager. You don't want to manage password. You don't want to manage auth. Way more brilliant people than us manage to create it securely. Leave them the challenge of it.
[00:50:31] Ty Wells: One caveat, if you do that, you did mention Supabase. ▶ Make sure you use your own provider, email provider, like I use Resend [tool:Resend], because Supabase can do it, but they have throttles on there. They're only going to send so many. I have a 60 second window to get that code, it may not even get there in 60 seconds. That's why I have to use my own provider. You may send multiple, have a limit like so many an hour.
[00:51:21] Tom Welsh: Yeah, so I'm using Resend for my emails as well.

<!--SEGMENT
topic: AI Photo Booth and Behavioral Design
speakers: Juan Torres, Patrick Chouinard
keywords: AI booth, Docker, QR code, behavioral change, James Clear, frontend, Diffusion, containerization
summary: Juan Torres previews updates to his AI photo booth project, including a Docker-orchestrated architecture and a QR code delivery system for guests to retrieve images on their phones. He frames the user experience design around James Clear's four laws of behavioral change to maximize engagement.
-->

[00:51:31] Juan Torres: I was working on the front end component of the AI booth project that I was displaying yesterday. I have a function of prototype, but I'd rather get down the security levels. But first, before I share anything, by next week, you'll see a really cool frontend. What I was showing two weeks ago was the DataWeb [tool:DataWeb] application, which basically serves as the tool for the diffusion prompt engineer to actually create the prompts. And the AI booth technician to see all the processes happening. There was a lot of tables and each row had a sub row, which stipulated detail, all the AI generated images with the frontend.
[00:52:47] Juan Torres: I have the backend docker containerized in its own image, the frontend docker image containerized in its own image. So in case I need to separate them into different... I created a Docker [tool:Docker] orchestrator to activate it, activate one or the other, or both at the same time. For the front end, I also added a feature you're going to see next week that it's going to allow the guest to click a button and that QR code is going to be generated. And through the QR code, with the phone, they're going to be able to get all the images, and they're going to be able to see them in their phone.
[00:53:52] Juan Torres: Trying to follow the four laws of behavioral change, accordingly stipulated by James Clear, which is make it obvious, make it attractive, make it easy, and make it satisfactory. If I can achieve those four laws of behavioral change, I think this could be an attractive approach.
[00:54:15] Patrick Chouinard: We're going to all be looking forward for the demo next week.

<!--SEGMENT
topic: SaaS Prototyping and Customer Presentation Strategy
speakers: Adam, Patrick Chouinard, Tom Welsh, Ty Wells
keywords: SaaS, security guards, customer demo, staging, production, UI/UX, fridge paradox, prototype
summary: Adam seeks advice on prerequisites for demonstrating a security guard SaaS to customers, specifically whether to set up staging environments and polished UI before first contact. The group advises prioritizing visual polish for non-technical buyers to avoid the "fridge paradox" where customers fixate on superficial missing features rather than core value.
-->

[00:54:48] Adam: Working on this SaaS project. It's for like security guards. Trying to figure out what stuff needs to be done before putting this in front of customers. Do I have to do the staging and all that stuff before any customers, you know, setting up dev, staging, prod, before customers see it or hold off on that? And some of the button layouts, do I need to have those real super optimized before putting this in front of customers?
[00:55:24] Patrick Chouinard: <A>It depends on the customer you're showing it to. If you have a highly technical customer, they're going to see the value in the scaffolding, but if you get some other type of customer, you're going to have the fridge paradox, where you sell a fridge to someone and say, this is awesome, it's 22 cubic feet, it has a nice cooler at the bottom, it has a water dispenser, and the person asks, do you have it in black? So then you might want to put a little bit, maybe not the final touch, but make sure that it at least looks nice visually in order for them not to focus on the fact that it doesn't look finished and completely skip the rest of your presentation mentally.</A>
[00:56:23] Ty Wells: Adam, I have a security company in my ERP. I built that into the ERP when I redid it. I can certainly show it to you if you're interested in looking at seeing how it's set up.
[00:56:47] Adam: Like guards, like armored guards stuff.
[00:56:50] Ty Wells: Yeah. That's what we do as well.
[00:57:05] Tom Welsh: <A>I wouldn't be focusing too much on my dev and staging environment. I'd have a front end up to show to the client. When they then pay for it, I'd then get my backups going. If you're using things like Vercel, yeah, dev and previews there to start with. But I wouldn't be scaffolding too much on that back end. Get the front end sale done with your nice buttons and what looks nice in their face, and then backfill afterwards.</A>

<!--SEGMENT
topic: Google Cloud Platform Developer Experience
speakers: Andrew Nanton, Patrick Chouinard, Ty Wells, Juan Torres
keywords: Google Workspace, Azure, AWS, GCP, Gemini, Enterprise, ADK, Vertex AI, CLI, MCP, infrastructure
summary: Andrew Nanton discusses migrating from Azure to Google Workspace and GCP, finding the CLI-based approach more manageable for small-scale projects despite Google's complex UI. Patrick critiques Google Workspace Enterprise for stripping AI features available in Pro plans, while Juan suggests Terraform for infrastructure management.
-->

[00:59:17] Andrew Nanton: I have moved a lot of development over to Google Workspace [tool:Google Workspace]. Versus working with Office 365 [tool:Microsoft 365], what I've found is that being able to aggregate information, the value of a lot of these things like Claude Code [tool:Claude Code] and Claude is the being able to very quickly access all the stuff you need without a lot of fuss. I still am a little shocked that they don't have a single tagging system across all elements of Google Workspace. But I found that very pleasant. The new Gemini [tool:Gemini] models seem pretty good, the 3.1 previews. It has removed a lot of blocks for me to move from the Azure [tool:Microsoft Azure] stack to the Google stack.
[01:01:08] Patrick Chouinard: Have you done a lot of the admin work in the backend in GCS? How do you find it? Because I find it incredibly hard to understand. Compared to Azure, Google Cloud Platform [tool:Google Cloud Platform] seems like what it is. They bought a lot of product and just shoved them together.
[01:01:42] Andrew Nanton: No, I mean, fair enough. I will say, I don't think any of them, so having briefly tried AWS [tool:Amazon Web Services], Google, and Microsoft, I think they're all terrible. Right now, everything is pre-released, I'm not dealing with a number of users. Having the Google Cloud and GWS CLI clients and just like I do everything through Claude and tell it or Codex or whatever and say, use the CLI, use the MCP [tool:MCP], confirm with me before you do stuff. It's very effective at being able to navigate those crusty and baroque APIs.
[01:02:37] Patrick Chouinard: It's kind of telling that you need an agentic framework to navigate the administration platform of your hyperscaler.
[01:03:05] Ty Wells: One was coordinated and planned, and that's what you've got with Azure. With Google, it's like developers built the tools, and if I remember some context around that, they were using the tools, and then they became good tools. So they start to throw them in, but everybody's building different ways.
[01:04:37] Juan Torres: Have you tried using Terraform [tool:Terraform] in order to carry out all your infrastructure work, Andrew?
[01:04:47] Andrew Nanton: No, I mean, that's probably where I need to go. I've been under such heavy iteration that massive things are changing.
[01:05:10] Juan Torres: I thought it was genius because I was using Claude Code to carry out all the AWS CLI infrastructure work. Then Brandon comes in, it's like, hey, have you tried Terraform? I could just use code as infrastructure, and it will do it super fast.
[01:05:38] Andrew Nanton: Everything's built on ADK [tool:ADK] to the alpha, I guess beta now. The scaling that I mostly have is pretty much solved by Google Cloud Workers [tool:Google Cloud Workers]. Anything that I have that's kind of a longer running process, ADK hands it off to that.
[01:06:25] Patrick Chouinard: Did you try Gemini Enterprise or are you still on Pro using GCP to control it?
[01:06:42] Andrew Nanton: I'm using the Gemini models through Vertex AI [tool:Vertex AI]. I have yet to get to the point where I'm using A2A or something for the ADK agents.
[01:06:56] Patrick Chouinard: <A>It's not an enterprise subscription. The only reason I ask is because my experience on the enterprise side is the enterprise offering is horrible compared to the pro offering. Everything you have in pro is fine because they ship really quick. At the moment you switch to enterprise, Google mentality is, oh, we have to be hyper-secure, it's an enterprise, so basically we're going to strip every fun functionality we ever had. With Gemini Enterprise, I'm not able to have the model create a Google Sheet. In the Pro version, it can create an Excel document, a Word document, a PDF. In Google Enterprise, no document creation. Notebook LM Enterprise can't create video, can't create slide deck, it can only create the Bear podcast. It's really, really stripped down.</A>

<!--SEGMENT
topic: Advanced Coding Workflows and Tools
speakers: Patrick Chouinard, Ty Wells, Juan Torres
keywords: Superpower, Shipkit, Codex, Claude Code, adversarial review, skills, plugins, automation
summary: Patrick Chouinard details his workflow combining Shipkit templates with the Superpower plugin for Claude Code and Codex. He recommends using Codex's adversarial review capability to catch bugs missed by the primary model, emphasizing the value of distributing work across multiple AI tools to reduce model-specific bias.
-->

[01:11:21] Patrick Chouinard: Don asked if a lot of people are still using Shipkit [tool:Shipkit]. He primarily switched to Superpower [tool:Superpower]. I'm still using Shipkit for the templates because they're still awesome. So whenever I start a new project, but honestly, I've started using Superpower to work with the Shipkit template. I'm using Superpower pretty much every day with both Codex [tool:Codex], Claude Code [tool:Claude Code], and I'm probably going to start trying it in GitHub Copilot [tool:GitHub Copilot] as well.
[01:12:19] Ty Wells: I use strictly Superpower, and it has superpowers.
[01:12:48] Patrick Chouinard: One of the things I absolutely love, it's in their design phase. They use something very similar to the front-end design skill, but in order to present whatever design they're about to implement to you, they spawn a local web server and actually show you, here's the three design I'm proposing. Choose one.
[01:13:36] Ty Wells: It's a tool that you shouldn't be building without it. If you're building anything, you should have that tool.
[01:13:52] Patrick Chouinard: That's what I use when I said that I use Claude Code offline. I basically do the brainstorming with Superpower. Build a spec, build the implementation plan, and when I'm there, the implementation plan can run for one or two hours autonomously. I just start remote control, let it start the implementation with subagent, and I walk away.
[01:14:18] Patrick Chouinard: ▶ One trick, if you have the token, use the Codex plugin to do the adversarial review at the end of the superpower process. It will find bugs that the superpower code review will have skipped.
[01:14:40] Juan Torres: Adversarial review?
[01:14:43] Patrick Chouinard: It's a Codex skill that literally tried to break your code. It will report, here's everything that I found, give it to Claude Code so it can use it to start correcting everything. You can configure it to work in a loop where every time Claude Code corrects, it will re-evaluate until it finds nothing. You can distribute the charge, distribute the bias, and it's a very nice finishing touch to a superpower creation pipeline.

<!--SEGMENT
topic: AI-Generated Educational Content Creation
speakers: Ty Wells, Patrick Chouinard, Tom Welsh
keywords: ShipSafe, coaching, curriculum, GPT Image 2, educational graphics, visual aids, cybersecurity training, DALL-E
summary: Ty Wells showcases a 12-week cybersecurity coaching curriculum called ShipSafe, highlighting the use of GPT Image 2 to generate textbook-quality technical diagrams. The discussion touches on the rapid commoditization of high-quality visual assets and the implications for creative professionals.
-->

[01:23:13] Ty Wells: I know I told you guys that I will be doing something. I'm trying to find the page. For some reason, I have lost it. This is ShipSafe [tool:ShipSafe]. I start this coaching here next Wednesday. I'm doing a 12-week program with them, like a cohort. These were the 12 different areas that I'm going to be teaching on or coaching. I broke it down into some of the fundamentals, depending on the domain. I added this summary here, which breaks it down a little bit further for them. I use some graphics as I figure, let me teach them like a 10-year-old exactly where these things are and how this works.
[01:25:45] Ty Wells: You can click on it and see what it does. I did add a scan URL, so you can scan your URL, your public facing. If it's your own, you can check it.
[01:26:10] Adam: You told me you did stuff with physical security. Is this what you're talking about, this website?
[01:26:13] Ty Wells: No, this is something. I do cybersecurity stuff.
[01:26:28] Patrick Chouinard: What did you use to create the images? Is it a Nano Banana or you tried a GPT image?
[01:26:34] Ty Wells: GPT Image 2 [tool:GPT Image 2]. It was a game changer in terms of what I was trying to describe how I wanted. I wanted basically a textbook graphic and it did a wonderful job. It knocked out. It cost me like two bucks to run all 12. It was really, really worth it.
[01:26:57] Patrick Chouinard: Very nice. I've done a couple of tests, not in-depth. Modifying image, I thought Nano Banana was great, but GPT Image 2 is extremely impressive.
[01:27:18] Ty Wells: I think I did a Nano Banana. It wasn't there. It was like night and day.
[01:27:39] Tom Welsh: You look at those images now and you think, five, ten years ago, you could pay thousands of pounds to get those images. You spent $2 and you've got production quality images in your documentation.
[01:27:51] Ty Wells: It's just, I feel for the creative sometimes.

<!--SEGMENT
topic: Community Resources and Tool Discounts
speakers: Adam, Andrew Nanton, Ty Wells, Patrick Chouinard
keywords: Lenny's Newsletter, Linear, Whisperflow, Granola, discounts, tools, subscriptions, Mercury
summary: Adam asks about experiences with Lenny's Newsletter product discounts. Andrew Nanton confirms value in the lower subscription tier for discovering tools like Linear and Whisperflow, and shares a strategy of using burner credit cards from Mercury to prevent unwanted automatic renewals on trial offers.
-->

[01:20:06] Adam: Cool. I was wondering if anyone's used the discounts from Lenny's Newsletter [link:Lenny's Newsletter].
[01:20:17] Ty Wells: I've never tried it. I've heard people be successful with doing it.
[01:20:27] Andrew Nanton: Definitely do run out sometimes. A lot of them aren't especially useful for me doing what I'm doing, but I've definitely gotten my money's worth. I didn't do the super premium tier, but I've gotten a lot out of the lower tier. I don't think I'll renew it, but it's given me a chance to try a lot of different stuff.
[01:20:52] Adam: So basically, if you subscribe for a year, you can get discounts for a year. That's kind of how I understand it.
[01:20:58] Andrew Nanton: Most of the codes are, they have a few different ways that they work. Sometimes it's like a monthly code that applies 12 times. I created a burner credit card on my Mercury [tool:Mercury] account to lock it to say, if you try to rebuild that, it's not going to go through because I don't want these to automatically renew in the background for thousands of dollars. I found Linear [tool:Linear] to be really useful. I also got Whisperflow [tool:Whisperflow] and Granola [tool:Granola] and all kinds of other stuff. Some of them I used for 10 minutes, some of them I use every day.

=== UNRESOLVED SPEAKERS ===
- Ty Wells
- Patrick Chouinard
- Tom Welsh
- Juan Torres
- Andrew Nanton
- Adam
- Alex Wilson
- Rod Morrison (mentioned)
- Don (mentioned)
- Brendan (mentioned)
- Morgan (mentioned)
- Scott (mentioned)
- Fitz (mentioned)
- Biggie (mentioned)
- Vastgen (mentioned)