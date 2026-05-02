=== SESSION ===
date: Unknown (Tuesday, estimated late 2025)
duration_estimate: ~2 hours 15 minutes
main_themes: ShipKit platform usage and automation workflows, OpenAI Agent Kit announcement, Google ADK deployment on Cloud Run, AI-assisted documentation pipelines, Supabase/RLS migration, Cursor vs. GitHub Copilot vs. Claude Code tooling, Gamma presentation tool, N8N workflow validation, RAG application deployment, ShipKit costs and Windows compatibility, community member project updates

---

<!--SEGMENT
topic: ShipKit Documentation Automation Pipeline
speakers: Patrick Chouinard, Marc Juretus, Hemal Shah
keywords: ShipKit, GitHub Copilot, Jira, GitHub MCP, Azure DevOps, branch naming, pull request, documentation automation, Cursor, Claude, prompt engineering
summary: Patrick Chouinard describes how he has spent two weeks building an automated documentation pipeline using ShipKit templates. The pipeline creates Jira tickets, generates Git branches with standardized naming conventions, produces ~20,000 lines of documentation per project using AI, and automatically submits pull requests — all orchestrated through MCP servers. Hemal Shah asks about developer training programs Patrick is running for GitHub Copilot.
-->

00:04:08 - Patrick Chouinard
Hey, hello, Marc.

00:04:13 - Marc Juretus
Hey, Patrick, how you doing, brother?

00:04:15 - Patrick Chouinard
Good, good.

00:04:18 - Marc Juretus
What's the latest and greatest?

00:04:20 - Patrick Chouinard
I've been living in ShipKit [tool:ShipKit] for the last two weeks, honestly.

00:04:33 - Patrick Chouinard
Actually, I'm more interested in evolving the templates themselves than using them to create the three-sample project.

00:04:45 - Patrick Chouinard
▶ This is an insane Swiss Army knife of tools that I can leverage on my day-to-day.

00:04:57 - Marc Juretus
<Q>Any specific type of project you've built lately? What task were you trying to accomplish?</Q>

00:05:03 - Patrick Chouinard
<A>Well, for example, just the generate diagram, I've used it in a pipeline I've put in place at my work — obviously restricting the template itself to only myself — to document all of our projects for the past year or so in three days.</A>

00:05:28 - Patrick Chouinard
I've basically burned through my entire allocation of API tokens just to document our projects with that one prompt. But yeah, I've created about 20,000 lines of documentation per project, and I've run it through about 12 subprojects right now.

00:06:00 - Marc Juretus
That's like one of the worst things with doing projects — documentation.

00:06:15 - Patrick Chouinard
And I created also a workflow to give to the agent where it actually starts by creating an issue in Jira [tool:Jira] for creating the documentation and adding the Copilot instructions. So it creates the issue, then it creates a branch automatically using the GitHub MCP [tool:GitHub MCP]. Then it starts working on it, creating all the documentation. And then once it's done, it creates the PR and submits it.

00:07:00 - Patrick Chouinard
▶ I imported the standard commit documentation naming convention for commit messages and reused it for our branch naming. So we have either a feature, a breaking change, or in this case, a `docs/` prefix plus the name of the ticket that was created originally, as well as reusing the main ticket name as the branch name.

00:07:37 - Patrick Chouinard
▶ So the entire process is now automated just around that one template.

00:08:03 - Marc Juretus
I have the approach of learning all the different tools — CrewAI [tool:CrewAI], LangGraph [tool:LangGraph], the GDK — but I really haven't been building as many polished projects as you. I got some things like the fantasy league app, and it gave me a good foundation of Next.js [tool:Next.js] and more use of Docker [tool:Docker].

00:08:47 - Patrick Chouinard
I extracted the value I needed from ShipKit. To me, it was not as much about building the application as it was leveraging all of the templates, prompts, and information to help me automate my day-to-day work.

00:09:37 - Patrick Chouinard
▶ I don't spend as much time learning about the nitty-gritty details of specific coding anymore, because honestly, AI is doing most of it. I want to understand what it does, I want to be able to read it and understand it deeply, but not necessarily be able to write it manually myself anymore.

00:10:00 - Marc Juretus
That's where I'm at with Cursor [tool:Cursor] too — it's pretty much writing my stuff. But I will say this: when it navigates down a bad road, it's good to know, "Nah, don't do it that way."

00:10:24 - Marc Juretus
One thing I don't like is that it always says, "You're absolutely right." Like, hold on, you can push back once in a while.

00:10:35 - Patrick Chouinard
All of the system prompts I developed in Clara Forge [tool:Clara Forge] are always like, "I want you to challenge me. I want you to not accept what I tell you as fact." I force the AI to be contradictory — not just for the fun of it, but if it doesn't make sense, you will be rewarded for standing up. It's basically to break the training that in order to be rewarded, it has to be agreeable.

00:12:27 - Hemal Shah
Patrick, a quick question for your developers that you are creating trainings for — do you also go to a level where you teach them how to use Cursor or vibe coding?

00:12:47 - Patrick Chouinard
I would love to give them Cursor training, but sadly it's not an approved tool yet where I work. So I'm teaching them how to use GitHub Copilot [tool:GitHub Copilot] right now.

00:13:02 - Hemal Shah
Oh, yeah, I'm training a class of 100 next week.

00:13:11 - Patrick Chouinard
▶ Basically, what I'm going to teach next week is going into an existing project, starting with a very well-defined prompt to do a specific task with no instruction file whatsoever, then generating the instruction file — which is basically the equivalent of Cursor rules — and then running the same prompt again and showing them the difference in accuracy and quality of code generated with and without the instruction file.

00:14:03 - Patrick Chouinard
▶ I created a pipeline of prompts to ingest all of the release notes from different providers — Cursor or GitHub Copilot — and then transform all of that into training material. Changes so frequently you have to create it yourself.

---

<!--SEGMENT
topic: OpenAI Agent Kit Announcement
speakers: Brandon Hancock, Marc Juretus, Hemal Shah, Mitch
keywords: OpenAI Agent Kit, OpenAI Dev Day, RAG, guardrails, N8N, vector store, ChatGPT apps, Canva, Zillow, Sam Altman, workflow orchestration, multi-agent
summary: Brandon Hancock shares his excitement about OpenAI's Agent Kit announced at Dev Day, describing it as an easy-to-use agent-building platform with built-in RAG, guardrails, and one-click deployment. He compares it favorably to N8N for simplicity but notes it lacks true multi-agent orchestration. He also previews the new ChatGPT apps ecosystem featuring Canva and Zillow integrations.
-->

00:16:02 - Brandon Hancock
OpenAI Dev Day [tool:OpenAI Dev Day]. If you guys have not had a chance to watch this yet, it is unreal. Basically, all the changes that were made for Dev Day — so many cool announcements, like apps in ChatGPT [tool:ChatGPT], and just all sorts of crazy updates.

00:16:22 - Brandon Hancock
But the coolest one, the one I did a video on for you guys, it's called Agent Kit [tool:OpenAI Agent Kit]. It's very similar to Agent Development Kit — just take out the word "development." And it's crazy how easy they made it to build agents and then add agents to your websites.

00:16:59 - Brandon Hancock
Like, I literally spun up a RAG application in seconds using it. I made a RAG query agent. I was able to add in guardrails. I was able to hook up a vector store, do queries. It is insane how easy it is. And as soon as I was done, I just had to click publish.

00:17:25 - Brandon Hancock
▶ It kind of feels like N8N [tool:N8N] meets OpenAI [tool:OpenAI] is the best way I would describe it.

00:17:33 - Brandon Hancock
It is very workflow-oriented. It is not so much multi-agent orchestration. It's very much Agent 1 calls Agent 2. You can't have agents call other agents. But just for straight-up left-to-right workflow sequences, yeah, they've absolutely crushed it.

00:18:01 - Brandon Hancock
I have a video coming out on that tomorrow. So I'm excited for you guys to try it out.

---

<!--SEGMENT
topic: ShipKit Template Usage and Token Optimization
speakers: Brandon Hancock, Patrick Chouinard, Hemal Shah
keywords: ShipKit, ChatGPT custom GPT, Cursor rules, Windsurf, Claude Code, token costs, system prompt, markdown, GitHub Copilot, template variants
summary: The group discusses how to use ShipKit templates outside of Cursor to save on token costs, including Patrick's idea of embedding a ShipKit template as a ChatGPT custom GPT system prompt for the planning phase. Brandon confirms this is acceptable and announces upcoming Windsurf and Claude Code rule variants to help users rotate between $20/month plans.
-->

00:11:35 - Patrick Chouinard
<Q>Am I allowed to use this template in other systems as long as they're not being made public? For example, the first one where you actually generate your idea — instead of burning through Cursor tokens, why not put it as the system prompt of a ChatGPT project that I can talk to?</Q>

00:21:38 - Patrick Chouinard
<A>Yeah, I would like to create for myself a custom GPT [tool:ChatGPT custom GPT] out of one of the templates, in order to — instead of going through Cursor tokens, especially in the planning phase — do it verbally with a custom GPT powered by one of the templates.</A>

00:22:03 - Brandon Hancock
<A>I mean, yeah, if it's a custom GPT, the stuff's hidden. I think that's awesome. You'll have to let me know how that goes, because I'd love to see chatting with one of these docs.</A>

00:22:19 - Patrick Chouinard
▶ I just want to make sure that everything we can do without needing Cursor in the background, we do — so we save on tokens, basically.

00:22:22 - Brandon Hancock
▶ What we're working on right now for ShipKit is making it so we have a Windsurf [tool:Windsurf] variant of rules, Cursor, and Claude Code [tool:Claude Code], because I know a lot of people like to hop between them to stay below that $20 a month plan. This way, you guys will be able to hop through all the different plans and get, instead of racking up one huge Cursor bill, a very tiny Cursor one and a very tiny Claude Code one.

00:22:53 - Hemal Shah
<Q>When you hop through — to your point, hopping through Claude Code, your Cursor — if you are using the same model, Claude, whatever that version is, the output will be pretty much similar, right? Like if you change the IDE, it won't change the output?</Q>

00:23:11 - Brandon Hancock
<A>Yeah, there's going to be a few tweaks. In Cursor, you just chat and it's awesome — you have Cursor rules. Claude Code does not have Cursor rules. So you have to use sub-agents that have all the rules. So it's like every platform has its own unique way of producing high-quality results.</A>

---

<!--SEGMENT
topic: Google ADK Deployment on Cloud Run
speakers: Hemal Shah, Brandon Hancock
keywords: Google ADK, Agent Engine, Cloud Run, Next.js, Vercel, GCP, SSE endpoint, REST API, parts blobs, Vertex AI, deployment, back-office reconciliation
summary: Hemal Shah reports successfully deploying a Google ADK-based back-office reconciliation agent to Cloud Run after hitting limitations with Agent Engine's API (which doesn't support parts/blobs). He also deployed the Next.js frontend to Cloud Run using GitHub repository integration, mirroring Vercel's workflow. Brandon asks about instance scaling configuration and offers to incorporate Cloud Run deployment into ShipKit.
-->

00:23:41 - Hemal Shah
Continuing working on Google ADK [tool:Google ADK] for a back-office reconciliation project where we can compare different orders uploaded through files. The challenge we discussed last time about two different APIs for Agent Engine [tool:Agent Engine] versus the local ADK — so finally, I really wanted to use the ADK web version where we have `run` and `run_sse` endpoints because we can pass parts and blobs and everything, because Agent Engine couldn't allow it.

00:24:18 - Hemal Shah
So I went down the path to deploy the whole ADK web or ADK API server to Cloud Run [tool:Cloud Run] using `gcloud`. ADK provides a Cloud Run deploy shortcut as well. So I went through that, deployed it — it works like a charm.

00:24:44 - Hemal Shah
And then for the front end, for Next.js, I tried Vercel [tool:Vercel], which works. But then I thought to just keep everything together on GCP [tool:GCP]. So I deployed that Next.js application on Cloud Run. Cloud Run is now providing ways to connect a repository — just like Vercel — so it was a very similar flow. They're both secure, and things are working.

00:25:17 - Hemal Shah
▶ So I'm happy that I'm able to use the parts version of the REST API instead of Agent Engine's stream query, where we cannot use that and there's no documentation.

00:25:39 - Brandon Hancock
<Q>For Cloud Run, are you doing container instances that are on all the time, or are you having it scale to zero — min instance zero or one?</Q>

00:25:39 - Hemal Shah
<A>Because I'm still in the development phase, I'm doing request-based instead of instance-based, so minimum is zero — I let it cool down completely for now. But yeah, there are multiple flavors to it: fast cold start, things like that, so I need to dig into it a little bit deeper.</A>

00:26:15 - Hemal Shah
Brandon, if we want to add Cloud Run as another deployment option in ShipKit, I know the deployment is already there, but I'm more than happy to contribute or help out in any way I can.

00:26:34 - Brandon Hancock
No, seriously, thank you. I'm just fingers crossed any day they turn on Agent Engine and it works, and then there's no additional work needed. Because knowing our luck, we'd spend a week going to Cloud Run, and then literally the following day they're like, "Oh, it all works now."

---

<!--SEGMENT
topic: Legacy Application AI-Assisted Development
speakers: Hemal Shah, Brandon Hancock, Morgan Cook, Patrick Chouinard
keywords: legacy application, Supabase, RLS, row-level security, AI docs, ShipKit templates, bug fixing, monolith, Cursor rules, GitHub branch, staging environment
summary: Hemal Shah asks for best practices on using AI coding tools with legacy monolithic applications. Brandon recommends adapting ShipKit's AI docs to the specific legacy tech stack and iteratively updating them when mistakes occur. Morgan Cook shares his own legacy Supabase project migration, moving away from row-level security and restructuring admin policy storage from auth metadata to a user profile table.
-->

00:28:12 - Hemal Shah
<Q>When we are working with vibe coding with a legacy application where it's a huge monolith or tentacles are all around the place — are there any best practices on how to do bug fixing? It's not greenfield development. Any experience, tips, tricks, direction around that?</Q>

00:28:26 - Brandon Hancock
<A>The main thing I would do is adapt the AI docs to the project. The AI docs are designed to help you go from a blank boilerplate application designed around Next.js, TypeScript, Tailwind, Supabase [tool:Supabase], Drizzle — it's designed for that tech stack. So what you could do is, as the senior engineer, go: "In my legacy application, I'm using this type of database, this tech stack," and just tell it exactly what's going on and what it can expect. Then you'll come up with your own task template.</A>

00:29:06 - Brandon Hancock
▶ Same for bug fix — "You're no longer in this ecosystem, you're now in this ecosystem." It might take a few iterations, it might make a mistake, but it's a continual process to continually update your AI docs. If they make a mistake, tell your AI doc, "Don't do that again." After 20 iterations, you're like, "Oh my God, this thing is amazing."

00:30:35 - Morgan Cook
My problem is I'm working with a legacy project also. It is in Supabase, but it was using row-level security [tool:Supabase RLS]. I wanted to get away from that. Also, my admin policy was actually saved in the metadata of the authentication user instead of a user profile. So just moving that stuff around is taking a little bit of work.

00:31:14 - Brandon Hancock
<Q>Are you excited to get away from RLS?</Q>

00:31:19 - Morgan Cook
<A>I am.</A>

00:31:25 - Brandon Hancock
▶ The thing I dislike about RLS is you are one mistake away from allowing people to just wipe away everything. The stakes are so high with RLS that literally one weird edge case you didn't even think about, and your whole project is destroyed if you have a malicious user.

00:33:35 - Morgan Cook
I'm probably going to drop my local Supabase area and just go to staging and deployment on the server itself.

00:33:46 - Brandon Hancock
▶ You end up basically with two environments — production safe, and then that staging/development — to where it's the same thing running in the cloud that's on your local computer. And for $9 a month, it's such a peace of mind to know you're not accidentally wiping out all your users' data.

00:34:05 - Morgan Cook
▶ When you associate the GitHub repo now, it also looks for and creates those branches automatically if you have them tied. If it sees any changes to the schema, it'll create a branch for you.

---

<!--SEGMENT
topic: Patrick's ShipKit-Powered Documentation Workflow Deep Dive
speakers: Patrick Chouinard, Brandon Hancock
keywords: ShipKit, Claude 4.5, GitHub MCP, Jira MCP, Azure DevOps MCP, GitHub Copilot, prompt templates, GPT-5, model card, documentation automation, pull request, Cursor markdown
summary: Patrick gives a detailed walkthrough of his fully automated documentation workflow built using ShipKit templates as a reference. Using Claude 4.5 and MCP servers for GitHub, Jira, and Azure DevOps, the pipeline creates tickets, branches, documentation (~20,000 lines per project), commits, and pull requests autonomously. Brandon highlights how well-written prompts enable AI to replicate the same quality at scale.
-->

00:34:30 - Brandon Hancock
Patrick, what's going on, buddy?

00:34:35 - Patrick Chouinard
So this week, I've basically did what I was talking about — the ShipKit development kit — because I've used the generate diagram, but I pushed one step further. I have about 20 projects done so far, but another 30 to go through where they need to be documented. And there's a lot of administration around it. So I needed to create my Jira ticket, create my branch, create my commit, my pull request, on top of creating the documentation with that prompt.

00:35:14 - Patrick Chouinard
So basically now I use your list of prompts as reference. I brought in prompts that I already used and just told Claude 4.5 [tool:Claude 4.5], "Look at this list of prompts and templates and adapt this template of mine into the same fashion." So it ShipKitified my own prompt, basically.

00:35:39 - Patrick Chouinard
And now I created a workflow where, using all the MCP servers from specifically GitHub [tool:GitHub MCP] and Azure DevOps [tool:Azure DevOps MCP] and the one from Jira [tool:Jira MCP], it actually creates the ticket automatically. It creates the ticket, uses the ticket as a key to create the branch, does the work, creates the commit, and then generates the pull request and posts it for review. So the workflow does the whole thing around the documentation in and of itself, and it can run for about two hours on a project.

00:36:26 - Brandon Hancock
▶ If you have stuff codified, you can just say "go." It's just getting everything out of your head into a systematized process. How long would that have taken you as a regular developer without AI?

00:36:43 - Patrick Chouinard
Per project, we're talking about 20,000 lines of documentation, and I'm running about four or five iterations of GitHub Copilot [tool:GitHub Copilot] using that mechanic side-by-side, updating those projects simultaneously. It's insane the amount of work getting created. But all of that using ShipKit — not for ShipKit, but as a reference tool for how to create prompts to be effective and how to create templates to be effective.

00:37:23 - Brandon Hancock
▶ The second you have well-written prompts, AI goes, "That's what you want." The second the bar is met, AI can achieve the same bar.

00:37:49 - Patrick Chouinard
▶ Good prompt and the model documentation — because in that project where I create those artifacts, I always have the GPT-5 [tool:GPT-5] model card or the coding guidelines. So if I'm doing something that's going to be executed by a specific model, I always tell it, "Inspire yourself from this structure, but optimize it for this model based on that documentation."

00:38:27 - Brandon Hancock
▶ Any time I'm doing stuff now, I'm in Cursor. For example, working on pitches, client stuff, anything — I'm always in Cursor making markdown files. Every time I have a conversation, it's going into a markdown file. And the next time I work on the next thing for that client, boom, it's automatically back inside of Cursor. I don't really use Google Docs. I don't really talk with ChatGPT as much anymore. I am living in Cursor to generate the artifacts, store the artifacts, and then use them to help generate even more artifacts.

---

<!--SEGMENT
topic: Cursor as Second Brain and Non-Coding Workflows
speakers: Brandon Hancock, elijahstambaugh, Patrick Chouinard
keywords: Cursor, markdown files, second brain, project management, Google Drive MCP, Notion MCP, student newsletter, education, personalization, GitHub Copilot autocomplete, prompt iteration
summary: Elijah asks about using Cursor as a general-purpose knowledge management and project management tool beyond software development. Brandon explains his workflow of storing all work as markdown files in Cursor projects, enabling AI agents to reference and generate new artifacts. Patrick adds that GitHub Copilot has an edge over Cursor for markdown autocomplete within files. The group discusses building a personalized student newsletter generator using this approach.
-->

00:39:10 - elijahstambaugh
<Q>So what you're saying — and what Patrick's saying — is that's what I've been thinking as well for projects that are not software related. When you're doing that, you're just writing it all to a markdown file. Are you storing your notes and your transcripts as well? And are you using a unique project per folder, or are you saying "here's Brandon's life" and storing everything inside of that like a second brain?</Q>

00:39:56 - Brandon Hancock
<A>I'm definitely going per project right now. But there's nothing wrong with doing the master plan — like a "Brandon's second brain" with work, personal, fun. You really could do that. I probably should go to that. As long as it's out of your head and in your computer, it doesn't matter if it's two folders away. The main thing is it's out of your head and something the agent can read.</A>

00:40:49 - Brandon Hancock
I'm using it for creating everything — customer research, figuring out how big things could get, turning that into video scripts, turning that into landing pages, turning that into small pitch decks. Everything is happening in Cursor. And I'm able to do what used to be a week's worth of work in an afternoon.

00:41:27 - elijahstambaugh
So I'm working with my son on a project — I'm in the education space and he's in high school. We're working on a newsletter generator where the content from the classroom gets specialized or made unique to the students' learning style or preferences. We're working through it with Make [tool:Make] or n8n [tool:N8N]. But that Google Drive [tool:Google Drive MCP] / Notion [tool:Notion MCP] MCP — could I potentially do that workflow, maybe even without n8n, just using MCPs?

00:13:09 - Brandon Hancock
<A>▶ Yeah, if you wanted to do it locally, here's what that would look like: each student could have their own markdown file — "Bob is a very visual learner, his favorite sport is soccer" — a short bio on Bob with learning style. And you literally could tell Cursor, "Your whole goal is to take in student information, look at what was taught this week, and generate Bob's custom newsletter." You're not going to do this just for Bob — you're going to do it for every single person in this folder. And there could be 200 people in that folder. AI will literally go through every single file and create it.</A>

00:15:04 - Brandon Hancock
▶ Most people go wrong by just creating the lesson plan once. What you actually want to do is create the lesson plan template, then create the lesson plan — where the lesson plan template understands best practices for ingesting information from the prompt and from the transcript to generate the lesson plan. You basically create the instructions to generate the output.

00:15:47 - Brandon Hancock
▶ The first time you do this, the lesson plan is going to suck. So you say, "This was awful for A, B, C, D — you did all this wrong. Please update the instructions." You update your lesson plan template and do it again. Six to eight iterations later, it's a beast at creating lessons. The second it's good for one student, you say, "Fantastic, go do that 200 more times."

00:16:18 - Brandon Hancock
▶ Let AI train AI, where you're just the critiquer — that's the game plan.

00:18:25 - Patrick Chouinard
▶ For specifically markdown work, GitHub Copilot [tool:GitHub Copilot] has an edge over Cursor. Cursor doesn't autocomplete when you write into a markdown file — it will generate markdown very well, but if you're writing in a markdown file, it's not going to autocomplete for you, where GitHub Copilot does. Once you have a project with a lot of knowledge in it, it's absolutely insane — you're going to start a sentence and it's going to give you the whole paragraph. Now I can't work in Word anymore because I don't have that autocomplete intellisense.

---

<!--SEGMENT
topic: Gamma Presentation Tool and N8N Workflow Validator
speakers: Ty Wells, Brandon Hancock, elijahstambaugh
keywords: Gamma, N8N, JSON validation, workflow security, badge, webhook, static analysis, Gamma API, Gamma 3.0, presentation generation, GenSpark, Beautiful.ai, MCP
summary: Ty Wells demonstrates a tool he built for a hackathon that validates N8N JSON workflows, runs static security analysis, generates a Gamma AI presentation from the workflow, and mints a cryptographic badge to certify the workflow's validity. The group discusses Gamma's recent 3.0 API release and its position as the leading AI presentation tool, as well as the potential to use Gamma's MCP to generate slides directly from Cursor.
-->

00:43:21 - Ty Wells
Not much going on. Back in the Bahamas, doing some additional training and stuff for the two projects I launched down here. I've got another one I'm launching next week — it's an internet hackathon, so we'll see how that goes.

00:43:51 - Ty Wells
<Q>Any project in particular you're thinking about cranking out during the hackathon?</Q>

00:44:18 - Ty Wells
<A>So this is a tool that basically checks your N8N [tool:N8N] JSON and gives you a rating, and then you can generate a badge for it indicating that it's valid or not.</A>

00:45:47 - Ty Wells
Basically, you upload the JSON. This would be your static analysis of any issues with that JSON. Then you can make a web call to test it to see if it's good, and then you can create a client deck — a Gamma [tool:Gamma] slideshow for the client — and then you can create a badge for it, basically saying that it's valid, because it's all about security. Are you securing the workflow you're building for somebody? And you create this badge that's hashed, and then the owner of that can verify that it's a valid certificate for that JSON they got. So basically no Trojan horses in your JSON.

00:51:13 - Ty Wells
And then you can say if it's technical or if it's an executive summary and so forth.

00:51:39 - Ty Wells
And then you can mint the badge — that's your verification. This is your score. And then once you're here, you can come in and verify the badge to say that's a valid JSON that you imported.

00:52:06 - Brandon Hancock
I had not got to use Gamma yet. I've heard about it, but I have just not used it or seen it in action — that was insane. I'm definitely going to have to see if I like Gamma or Canva [tool:Canva] better. I'd love to do a side-by-side.

00:52:29 - elijahstambaugh
▶ Gamma just released a big release last month with their API — it was Gamma 3.0 [tool:Gamma 3.0] — so they just added in a lot of that functionality. As far as I can tell, they just kind of went to the top of the food chain. I was looking at GenSpark [tool:GenSpark] and Beautiful.ai [tool:Beautiful.ai], but...

00:52:54 - Ty Wells
▶ No one's really close to it. They're like the ElevenLabs [tool:ElevenLabs] of presentations. Especially today.

00:53:07 - Brandon Hancock
▶ What's really cool is the fact that you could generate the JSON in Cursor, then say, "Hey, Gamma MCP [tool:Gamma MCP], go update that slide or generate the entire slide deck." You're just talking to slides at that point.

---

<!--SEGMENT
topic: Video Clipping Tools and Riverside Magic Clips
speakers: Paul Miller, Brandon Hancock
keywords: Riverside, magic clips, video editing, Gemini, multimodal, Facebook, social media, AI video tools, podcast clips, interview segmentation
summary: Paul Miller asks for AI tools that can automatically break a long interview video into short shareable clips for social media without manual editing. Brandon recommends Riverside's Magic Clips feature, which automatically identifies highlight moments from a full video. Paul had already tried Gemini for identifying clip segments but needed a tool that would actually create the clips.
-->

00:18:43 - Paul Miller
<Q>I've got, in one of the many volunteer things I do, people send me some videos with a whole lot of Q&A-type questions in a single long video. I just wanted to know, is there a good little AI tool out there that will break the video down? Because my end objective is to look at it and say, "Ah, that would be a good little Facebook mini video of that question and that answer," without me having to sit around and be a video editor for several hours.</Q>

00:19:26 - Paul Miller
I tried chucking it up into Gemini [tool:Gemini], because of course Gemini takes it as a multimodal model, and said, "What do you see in there?" It said, "Oh, I can see five little mini videos," but I kind of then want to chuck it to something that would create that for me.

00:19:43 - Brandon Hancock
<A>▶ The only recommendation I have that could work is potentially Riverside [tool:Riverside]. I think they have what they call Magic Clips, and what it'll do is listen to a whole podcast and come up with clips. I literally just did this while you guys were on the call — I just clicked the button.</A>

00:20:55 - Brandon Hancock
If anyone else has other suggestions, I'd be curious, because that would be pretty cool.

---

<!--SEGMENT
topic: Paul Miller's Traveling Salesman SaaS Project
speakers: Paul Miller, Brandon Hancock
keywords: traveling salesman problem, ShipKit, route optimization, SaaS, Python, Matplotlib, consulting, AI development cost, background jobs, ADHD, enterprise sales
summary: Paul Miller shares that he has been building a route optimization SaaS app (based on the traveling salesman problem) using ShipKit for about a week and a half, has already pre-sold it to a top-10 global consumer goods company, and has spent ~$300 in AI development costs. Brandon uses this as a case study for the economics of AI-assisted development versus traditional engineering costs.
-->

00:53:59 - Paul Miller
So, yeah, no, I'm having a good play. I'm very focused on a project I wanted to do for quite some time — around something that Tom had actually played with, the traveling salesman problem on computing, where you have a whole bunch of people, a sales team, and you need to allocate all the places they need to visit over a schedule.

00:54:30 - Paul Miller
So I'm using ShipKit to help me with it. Just having the MCP and the rules stuff working, and the focus on requirements that ShipKit helps — which I didn't have before — is allowing me to do some really amazing stuff. I'm about a week and a half in.

00:55:05 - Paul Miller
▶ I've already sold the app to one of the largest consumer goods businesses in the world — in the top 10, out of Australia, their regional head office. So I know I've got a budget to get the app done, which is completely funded by the vendor.

00:55:53 - Paul Miller
I've already gone through $300 US worth of credits just for this project alone. But I'm determined to finish it. I know a client's going to pay the bill.

00:56:51 - Brandon Hancock
▶ Real quick on the tokens — I know you said you spent $300. What's crazy is just thinking back to 2020: if you hire any engineer, you're going to pay $80 to $100 an hour to do the level of programming. And the fact that for $300 — obviously plus your own time, and you can't ignore that — but still, for $300 you have an app in a week. It's crazy.

00:58:40 - Paul Miller
One of the purposes of me jumping into this — I'm the CEO and the main sales guy for a SaaS business, and I have a team of developers and a CTO that's supposed to be on top of it, but I haven't been able to get him down the path of doing this stuff. I kind of just want to do it to show him up and say, "Hey, you can do this. You're much more savvy at this."

00:59:34 - Paul Miller
▶ As the primary shareholder of a SaaS business, this stuff scares the bejesus out of me because I've got 10 years of IP building up recurring revenue. And I'm thinking, how do we build a better moat for our existing customers? I want us to be really productive — let's imagine the perfect world, throw AI at it, jump so far ahead of our competitors, go for as much market share as possible, then look to sell the business next year.

---

<!--SEGMENT
topic: ShipKit Trigger.dev Background Jobs Template Roadmap
speakers: Brandon Hancock, elijahstambaugh, Patrick Chouinard
keywords: Trigger.dev, background jobs, Next.js, Vercel, Python, ShipKit roadmap, student newsletter, queue management, AI workflows, marketing platform, context window
summary: Elijah asks whether he should rebuild the ShipKit marketing platform using the current templates or wait for the upcoming Trigger.dev-based background jobs template. Brandon explains the architectural improvement Trigger.dev brings over the current Python background worker approach and gives a realistic timeline of late October to early November. He also explains how iterative prompt refinement enables AI to scale personalized content generation.
-->

00:19:28 - elijahstambaugh
<Q>I know you have the full-stack marketing AI platform that you built out. Is there a way to use ShipKit to build that? Is that something you're looking to redo, or should I just wait, or should I try to be aggressive and try to make that happen?</Q>

00:19:58 - Brandon Hancock
<A>I would wait, and I'll explain why. Inside of that application, the whole concept was how to build and deploy a real-world Next.js application that also can run Python background jobs — because that is such a core archetype of a real-world project. However, the kicker is our background worker had to manage a queue in addition to doing the work. So we were doing a lot inside of our deployed Python application.</A>

00:21:00 - Brandon Hancock
▶ The next template we're working on is going to use Trigger.dev [tool:Trigger.dev] to help perform background jobs. It's a Next.js application that uses Trigger. Trigger can do workflows — do A, B, C, D, E — and this literally could run for one minute or 20 hours. It doesn't matter. And that's the beauty of using a background worker, because Vercel allows you to run stuff up to five minutes if you're on the paid plan, but a lot of real-world complex jobs take more than five minutes.

00:21:50 - Brandon Hancock
▶ In your case for the email newsletter for the students, Trigger would be perfect — you could literally just add 200 tasks to the Trigger queue, and it would start: "I'm going to fetch student information, fetch lesson plan, generate a custom email, then send it." It could easily handle all sorts of jobs like that.

00:22:30 - Brandon Hancock
I think realistically, late October, early November. Key thing is it's Trigger.dev. So I would not — you have Context 7 [tool:Context 7], you already have the chat SaaS template. Just take out all the AI and start working with Trigger tasks.

00:23:32 - elijahstambaugh
<Q>This is my last question — I was thinking RAG, but you're saying the chat SaaS template is probably the easiest one to build to start just to get the full stack going?</Q>

00:23:46 - Brandon Hancock
<A>▶ I mean, you just need a Next.js application for people to click around, and then you need something to do background work. I think the chat SaaS template is the simplest one for you to get started with.</A>

---

<!--SEGMENT
topic: OpenAI Agent Kit Deep Dive and ADK Comparison
speakers: Brandon Hancock, Mitch, Hemal Shah
keywords: OpenAI Agent Kit, Google ADK, guardrails, PII, jailbreak, moderation, RAG, vector store, TypeScript, multi-agent, workflow orchestration, CrewAI, deployment, Claude Code sub-agents
summary: Brandon gives a detailed comparison of OpenAI's Agent Kit versus Google's ADK, rating ADK 9-10/10 for local agent development but 4/10 for deployment, while Agent Kit scores 7/10 for agent capability but 10/10 for deployment ease. He demonstrates the built-in Guardrails feature for PII, moderation, and jailbreak checks. Mitch discusses using OpenCode with GPT-5 Codex for task implementation and the upcoming Claude Code sub-agent support in ShipKit.
-->

01:59:35 - Brandon Hancock
▶ I'll give my ADK versus Agent Kit comparison. ADK on true agent capability is like 9 out of 10 — the fact that your agents can work with other agents, do work sequences or parallel tasks. ADK for local development, for pure agent work, 10 out of 10. Deployment, I still stand by it right now — 4 out of 10, given all the workarounds you have to do.

02:00:07 - Brandon Hancock
▶ Today, just playing with Agent Kit — it is wild. And then you get the code too, right when you build it. It's like N8N, and all this nicety is nothing more than under the hood — it's their Agent SDK already all built out.

02:00:51 - Brandon Hancock
▶ I'm going to give Agent Kit a 7 out of 10 because right now it's purely left-to-right workflows. There's no Agent 1 delegating work to Agent 2 and getting back a result. It's not pure agentic — it's agentic workflows. So it's like a third of what Agent Development Kit is. However, 10 out of 10 on deployment — I click this button and it's deployed.

02:01:26 - Brandon Hancock
▶ They have a chat starter kit application, and it just works. All I did was update two fields and it's working in a Next.js application. That's insane.

02:02:03 - Brandon Hancock
▶ For just pure text-based RAG, this is insane — I uploaded four markdown files and boom, my vector store was good to go. But if you want to do anything outside of a markdown or PDF file, their vector store is not the best. Multimodal — good luck. Even if it is a PDF, you have no control over chunking. But for V1, like a RAG chat support for a website, you can't beat it.

02:04:15 - Brandon Hancock
<Q>What was the most you spent in a day for your API costs on Cursor?</Q>

02:06:17 - Brandon Hancock
<A>2,600 was the final bill. So break that over 30 days — I was averaging $90 a day, and on peak days probably around $180.</A>

02:05:03 - Mitch
I largely use Cursor to document the task and use Sonnet [tool:Claude Sonnet] to actually create the task document because Claude is very verbose. And then I have a little bit of a different tech flow — I use OpenCode [tool:OpenCode] and GPT-5 Codex [tool:GPT-5 Codex] to actually implement the task document.

02:05:31 - Mitch
▶ The core caveat is that Brandon worked really hard on all these rules for Cursor. So I need to implement the rules to also input into this. Cursor rules or whatever — I hate it anyway. But yeah, it's really good.

02:06:43 - Brandon Hancock
▶ Cursor rules easily apply to Windsurf — actively working on that as we speak. Then part two: Cursor rules turn into sub-agents. Claude Code does not support rules, so you have to make sub-agents. So you end up with a Next.js agent, a Python agent — all the rules get smashed into agents that have those rules.

---

<!--SEGMENT
topic: Al Cole's New Role at Kong and AI Gateway Technology
speakers: Al Cole, Brandon Hancock
keywords: Kong, API gateway, rate limiting, caching, PII masking, guardrails, LangSmith, observability, enterprise AI, OpenAI Agent Kit, Google ADK security manager, independent consulting
summary: Al Cole announces he is leaving independent consulting to join Kong as head of their global services team (~60 people). Kong provides API gateway technology that handles rate limiting, caching, PII masking, and AI model traffic inspection for enterprise clients. Brandon demonstrates OpenAI Agent Kit's new Guardrails feature as a relevant parallel to Kong's plugin capabilities.
-->

01:25:58 - Al Cole
On my side, I have had a status change. I had to reach out to a company that knew me from my days at Redis [tool:Redis], and I've accepted a new job. So I'm going back working for the man.

01:26:22 - Al Cole
I'll be working for Kong [tool:Kong]. I don't know if you guys have worked with API gateways before, but it is a big piece of technology for larger enterprise companies. So I'll be running their services team.

01:26:54 - Al Cole
And the way the tech works — it fits the AI story that we're talking about. So many of us will highlight when we're working with LangSmith [tool:LangSmith] and the fact that it's got that observability built in. That's what a gateway can do for you — it can do the rate limiting, do the caching. It can inspect what you're trying to send to a model and then intervene if you are sending things you shouldn't be. Or you can even have plugins where if you are sending up data that might have PII, it automatically will mask it so that it doesn't reveal the individual.

01:28:30 - Al Cole
▶ Right now it is growing gangbusters and they're just looking for some leadership to help them get to the next level.

01:31:35 - Al Cole
▶ My biggest concern in considering anything full-time was: is AI in the middle of your story as a company, or is it adjacent? If it's adjacent, I don't know how that plays out over the long term. But the fact that they're in the middle — and all models are APIs, really, in terms of access — you get a piece of that action.

01:32:22 - Brandon Hancock
I just want to show what OpenAI literally dropped yesterday because I think this at a larger scale would be awesome. It's called Guardrails [tool:OpenAI Guardrails] — you click it, and it allows you to quickly check: I want to do PII checks, moderation checks, jailbreak checks — like all the most common types of things you'd want to check for in working with real-world agents. And you just get to quickly say, "Yeah, I don't want this type of PII."

01:32:42 - Al Cole
▶ This is exactly what Kong's plugins do. And you don't feel like you're paying commercial the same way you would be for the enterprise stuff. So that's actually really powerful.

---

<!--SEGMENT
topic: ShipKit Costs, Windows Compatibility, and New Member Q&A
speakers: Brandon Hancock, Joel Wilson, alexrojas, Mario Polanco, Mitch
keywords: ShipKit, Vercel, Supabase, Cursor, Claude Code, Windsurf, Windows setup, Google Cloud billing, Vertex AI, RAG, text embeddings, consulting, N8N, HeyGen, Mexico market
summary: New members Joel Wilson and Mario Polanco ask candid questions about ShipKit's hidden costs, known issues, and Windows compatibility. Brandon gives transparent answers about subscription costs (Supabase ~$20/month, Vercel ~$20/month, Cursor variable), current Windows setup bugs being fixed, and the strategy of rotating between $20/month AI coding plans. Alex Rojas reports a $700 Google Cloud bill from repeated Vertex AI vector store operations and gets advice to use Supabase for embeddings instead.
-->

01:43:33 - Joel Wilson
First time visitor, long time lurker.

01:44:38 - Joel Wilson
<Q>What are some of the criticisms that you've heard? What are the things you don't brag about?</Q>

01:44:46 - Brandon Hancock
<A>Main hiccups you're going to hit right now: one, with the RAG SaaS, there was an issue where Docker completely changed the way they handle offline models right before launch, so that was not working for about six days — we fixed that, everyone got an update. Two, Windows right now — some of the setup instructions are beautiful on Mac; on Windows, there have been some issues. So we're fixing that. Those have been a few of the main hiccups.</A>

01:47:29 - Joel Wilson
<Q>Hidden fees — like database and server fees, paying for Vercel and Cursor and all the things. You get a ticket and then to use this you've got to pay another $100 in subscriptions. Talk to me about that.</Q>

01:47:39 - Brandon Hancock
<A>▶ Main services: for the chat SaaS, you're using Supabase and Vercel and Cursor. Those are the three core subscriptions. Supabase is on the free tier for your first four or five projects; if you want additional things, Supabase turns into $20 a month. Vercel, very similar — very generous free tier, but if you want analytics and custom things, Vercel is $20. Your biggest cost will come from the actual AI development. What people are doing to minimize cost is getting a Cursor subscription for $20, a Claude Code subscription for $20, a Windsurf subscription for $20 — and the second you hit a quota on one, you hop to the next. If you care about speed, you could spend a few hundred in Cursor development. Paul did $300 to build a full new app in a week and a half — that's going speed mode.</A>

01:38:05 - alexrojas
I just found out that a previous application I was working on racked up like $700 of embeddings.

01:38:24 - Brandon Hancock
<Q>Were you using the Vertex AI [tool:Vertex AI] specifically their Vector Store?</Q>

01:39:01 - alexrojas
<A>I was using the Gecko, but the application is using the 004. It's just a previous application that Cursor deleted and it redid the job so many times on the Vector Store. And it was very heavy — 20,000 pages — so it racked up a lot.</A>

01:39:25 - Brandon Hancock
▶ I think the issue was actually using Google Cloud as the Vector Store, specifically the RAG engine and Vertex AI engine. A lot of the Google services are actually very pricey for RAG. That's why we don't use Google Cloud as our Vector Store — we use Supabase, because if you look at the pricing for text embeddings, it's like a penny of a penny. Even a 10,000-page document might cost you a dollar. The kicker is the actual Google services — cancel anything related to those.

01:43:08 - Joel Wilson
One suggestion: for those bills — $700 — we can always reach out to Google support and they can take it off. I had that problem once. They removed the charge if it was by mistake.

01:51:06 - Joel Wilson
<Q>When did you say the Windows version is going to be out?</Q>

01:51:11 - Brandon Hancock
<A>Actively working on it as we speak. There were about four to six files that have to be tweaked — mostly just relating to: on Mac, this command works with Python; when working with PowerShell, that command doesn't work. So there's just some tweaks that have to be made. I will be sending out an update as soon as it works.</A>

02:08:01 - Mario Polanco
Hey, it's my first time here. I was in your group for quite a long time. I had a long talk with a buddy I work with and said, "Dude, if there were just templates that would just be made or something." We had a really weird conversation, and the next morning I had a notification. I saw it, called him, and said, "You won't believe what just came out." So I bought it, and that's been great.

02:09:02 - Mario Polanco
I'm a big Claude guy — I'm on the Max plan. I ran out even my $20 limit in the last web app I built, and I just kind of stopped using it. I wanted to know if I could just use Claude Code [tool:Claude Code] for this instead.

02:09:49 - Brandon Hancock
<A>▶ I think you will absolutely love the sub-agents that come out for Claude Code. The cursor rules are forcing these agents to become specialists. So now that we're having to support not only Cursor but Claude Code, we need to make specialists that understand how to not do the 20 common mistakes that AI does when writing code for these types of projects. That's what we're actively fixing right now.</A>

02:11:35 - Mario Polanco
I actually live in Mexico. I'm trying to tap into the market here, doing more like system integrations with different hotels and tourism businesses, trying to get them caught up with things. I've been focusing a lot on brand bots and implementing RAG to create knowledge bases for real estate brokers, property managers, things like that. And even going into the coaching space — I do work with HeyGen [tool:HeyGen], doing cloning right now and making avatars for people.

02:14:00 - Brandon Hancock
▶ The biggest problem, which has always been the biggest problem, is leads. You cannot express enough how much to talk about your work on YouTube from a customer standpoint — "Here's the problem, here's how we solved it." Think of it like a lawn care business: you just showcase the cool work you've done. The second someone sees you doing months of work in a day in Cursor, you're like, "I will never go back."

=== UNRESOLVED SPEAKERS ===
- elijahstambaugh (raw name passed through unchanged; no canonical form in alias map)
- alexrojas (raw name passed through unchanged; no canonical form in alias map)
- Adam (single name only; no canonical form in alias map)
- Mitch (single name only; no canonical form in alias map)
- Mario Polanco (not in alias map)
- Joel Wilson (not in alias map)
- Ty Wells (not in alias map)
- Morgan Cook (not in alias map)
- Paul Miller (not in alias map)
- Tom Welsh (not in alias map)
- Al Cole (not in alias map)