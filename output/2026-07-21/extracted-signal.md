## general

This was a recurring community coaching call hosted by Paul Miller (New Zealand) and Patrick Chouinard (Quebec, Canada), standing in for the community owner who is on a larger contract. The session featured project demos and updates from several members of an international AI-builder community.

The first and longest segment featured Alireza Mounesisohi (California) demoing AgentTask, a new AI-integrated task management platform he built and launched the previous week. The group provided extensive feedback on his pitch, value proposition, and demo structure. Subsequent updates covered Marc Juretus's work with Robinhood's agentic trading feature and ServiceNow Copilot agents; Ty Wells's meal prep app built for his daughter; Ryan C's security review work on his social app and plans to build out an AI personal assistant ("Hermes"); Patrick Chouinard's Training Generator plugin for Claude Code; Shakur Abdullah's automated website redesign pipeline; Juan Torres's successful first live deployment of an AI photo booth at a quinceañera; and Morgan (mdcatc) presenting two products — Heritage Plot (cemetery management) and Class2Curb — plus a book publishing workflow automation. The session closed with brief discussion of Fable's new pricing within Claude Code subscriptions, the OmniGent meta-harness, and Patrick's use of Claude to assist with notary/succession planning documents.

The call had a consistent throughline of members helping each other sharpen product pitches, identify ideal customer profiles, and structure demos around user workflows rather than feature lists. Several members noted the rapid pace of change in AI tooling over the past 12 months, with code now being generated almost entirely without manual writing.

## insights

- **Don't compete on price alone**: Patrick warned Ali that pricing can be undercut overnight by incumbents (e.g., Jira offering a free agent tier), so the differentiator must be a unique workflow or capability.
- **Founders skip obvious explanations**: Patrick noted that creators unconsciously omit context that would be the "wow factor" for new users, because it feels obvious to them. The most skipped-over detail is often the most marketable.
- **Use your own product to market your product**: Patrick advised Ali to use AgentTask itself to assign an agent the task of building a communication methodology and ICP strategy.
- **Demo workflow, not features**: Multiple members (mdcatc, Ty, Patrick) converged on the same advice — show a complete 2–3 step user workflow from empty state to completed task, not a tour of individual features.
- **Identify your ICP before pitching**: Ty emphasized using agents to research the ideal customer profile first, then tailor the pitch to that audience's specific pain points.
- **Record short single-feature clips for feedback**: Patrick suggested posting one focused feature demo at a time to X.com or the forum to gather targeted reactions.
- **AI "slop" is a moving target**: Patrick warned Shakur that what counts as high-quality AI output today will become the new slop as models retrain on it — continuous retraining of design skills is required.
- **Teach skills by example**: mdcatc advised Shakur to feed the AI examples of what it did wrong vs. right, then have it update the skill each cycle — iterating toward 90% first-pass quality.
- **Use a verifier/observer skill**: For design automation, having a separate skill that evaluates output against criteria is more reliable than hoping the generative step self-corrects.
- **Observe before training clients**: Patrick's approach to AI consulting is to watch the client work, identify pain points, then have Claude build a plan — not to deliver a generic step-by-step course.
- **Highly regulated fields are ideal for AI document analysis**: Legal/notarial work is text-based and procedurally defined, making it one of the easier domains to augment with AI — but only if the RAG resources are properly provided.
- **Robinhood's agentic account is sandboxed**: Marc noted the agentic account is completely separate from the personal account and cannot execute trades on it — only read data — which resolved his main trust concern. (Marc Juretus)
- **The pace of change is striking**: Marc observed that a year ago he was writing code alongside AI; now he writes nothing manually. A full internal app was rebuilt at his workplace without any hand-written code.
- **Use an idle-screen animation to reduce UX friction**: Patrick suggested Juan run a looping 10-second animation showing a persona using the booth, to guide attendees who don't know what to do.

## qa

**Q (Patrick Chouinard):** From day one, with an empty universe, what's the path a new user takes to create their first project, add tasks, notes, and skills, and hand them to an agent to execute?
**A (Alireza Mounesisohi):** There are multiple flows — you can talk directly to the board agent and say "create a task for me about X," or click New, select a project, describe the task, and generate it. The most common flow users adopt is using Claude or Cursor with the MCP connection to create tasks, sub-tasks, and projects conversationally, then letting the agent update them as work progresses.

**Q (Patrick Chouinard):** Why would I use AgentTask instead of just telling Claude — which is already connected to Jira, Linear, or GitHub — to create a task there?
**A (Alireza Mounesisohi):** That's exactly what AgentTask is — it's that layer. The difference is the claim ID/session tracking (knowing which agent on which computer made which change), the integrated notes/skills/crews system, and the simplified interface designed for busy users who find Jira/Linear overwhelming.

**Q (mdcatc):** How much did the quinceañera event cost in AI tokens?
**A (Juan Torres):** $52 total for 859 jobs across a multi-model system (GPT, Grok, and others), generating nine AI images per session. Cheaper than expected.

**Q (Shakur Abdullah):** Have you tried CodeRabbit for security reviews?
**A (Ryan C):** Scott (a community member) tried CodeRabbit and then built his own hook-based local check system that outperforms it. Scott will demo it properly on a future call — Ryan didn't want to steal his thunder.

**Q (Ty Wells):** How are you using the Training Generator at work?
**A (Patrick Chouinard):** Claude Code maintains the training content off the GitHub repo for Claude Code itself. Whenever there's an update, it updates the training material and generates a differential course. The initial generation is token-heavy, but subsequent runs only process what changed.

**Q (Juan Torres):** Do you use Claude Co-Work or Codex as the tool you'd recommend to a non-technical client like a notary?
**A (Patrick Chouinard):** Co-Work for now, because it's more accessible to non-technical users. Codex is very powerful but feels more like a developer tool at this stage — though that could change next week.

**Q (mdcatc):** Have you looked at G2 or Capterra to research competitor products for Class2Curb?
**A (Morgan/mdcatc):** Not yet from G2 specifically. The suggestion was to use Google Deep Research pointed at Capterra and G2, give it the app definition and competitor examples, and have it extract user positives and negatives to build a requirements comparison.

## tools

- **AgentTask (agent-task.com)** — New AI-integrated task management platform demoed by Alireza; connects to Claude, Cursor, Codex, Copilot, Gemini, Winsurf, ChatGPT via MCP.
- **Claude / Claude Code** — Primary AI harness used across nearly all member projects for coding, document analysis, training, and task management.
- **Cursor** — AI coding environment; used by Ali and others as an MCP-connected harness for AgentTask.
- **Robinhood (agentic account)** — Trading platform with a sandboxed agentic account; MCP integration lets Claude read portfolio data and execute trades in the agentic account only.
- **Codex / OpenAI Codex** — Used by multiple members; Codex 5.6 discussed as better overall token value than Kimi K3.
- **Firecrawl** — Used by Shakur to extract all assets and copy from a target website URL as part of his redesign pipeline.
- **Impeccable / UX Pro** — Front-end design skills used by Ty and Shakur to push past generic AI design output.
- **Skill Arena** — Ty's skill that runs multiple design agents in competition to produce better front-end output.
- **NotebookLM** — Suggested by Ty as a way to generate video/audio training content from Patrick's Training Generator output.
- **Training Generator (Patrick's plugin)** — Open-source Claude Code plugin that generates a self-serving interactive training course from any repo's content.
- **OmniGent (omnigent.ai)** — Meta-harness that orchestrates multiple AI harnesses (Claude Code, Codex, etc.); discussed as promising but buggy.
- **Fable** — Now permanently included in Claude Code subscription at 50% of subscription price; discussed as a security/code review tool.
- **Dashlane AI** — Patrick's password manager flagged Ty's fresh domain as a phishing risk due to its age.
- **Homecue.ai** — Ty's home energy monitoring tool connected to his refrigerators to track device power usage.
- **USDA API** — Integrated by Ty into his meal prep app for nutritional data lookup.
- **Firecrawl** — Web scraping tool used in Shakur's website redesign automation pipeline.
- **LibreOffice / Inkscape** — Used by Morgan in his book publishing pipeline to generate ODT manuscripts and SVG book covers.
- **KDP (Kindle Direct Print)** — Target output platform for Morgan's book publishing workflow.
- **G2 / Capterra** — Product review/comparison sites suggested for competitive research on Class2Curb and Heritage Plot.
- **Google Deep Research** — Suggested for scraping G2/Capterra competitor reviews to build requirements comparisons.
- **Stream Deck (Classic 15-key and Plus 8-key)** — Patrick repurposing hardware to replicate OpenAI's Codex Micro keyboard functionality for managing Claude, Codex, and Hermes.
- **Codex Micro** — OpenAI's physical keyboard product that inspired Patrick's Stream Deck project.
- **Claude Co-Work** — Discussed as more accessible than Codex for non-technical users; Patrick used it for notary document analysis.
- **Osmo Pocket 3** — Camera Juan replaced the Canon with in his AI photo booth for better dynamic range.
- **DeepSeek** — Mentioned by mdcatc as an alternative model used in Claude Code.

## links

- **https://agent-task.com** — Alireza's AgentTask platform (shared in chat)
- **https://x.com/theo/status/2072482460122964067** — Link shared by Patrick (context unclear from transcript)
- **https://gist.github.com/hopchouinard/333cc020bbdc4ccede8ea023c3b6d62c** — Patrick's GitHub Gist (likely related to Claude Code configuration)
- **https://github.com/trayders/trayd-mcp** — Robinhood/trading MCP repo shared by Paul in chat
- **https://robinhood.com/us/en/newsroom/robinhood-presents-yes-no-event/** — Robinhood newsroom link shared by Paul
- **https://homecue.ai** — Ty's home energy monitoring application
- **https://shef.rocksteady.ai** — Ty's meal prep app built for his daughter
- **https://github.com/hopchouinard/Training-Generator** — Patrick's open-source Training Generator plugin for Claude Code
- **https://www.youtube.com/watch?v=s5T5oQJcJ6U** — Matt Pocock's 15-minute video about his "Teach" skill (shared by Biggi Fraley)
- **https://www.aihero.dev/skills** — AI Hero skills directory (shared by Biggi Fraley as lead to Pocock's repo)
- **https://github.com/mattpocock/skills/tree/main/skills/productivity/teach** — Matt Pocock's "Teach" skill GitHub repo (shared by Biggi Fraley)
- **https://class2curb.com/** — Morgan's Class2Curb product website
- **https://omnigent.ai/** — OmniGent meta-harness platform shared by Patrick

## decisions

- **Alireza** will refine his pitch and demo by using AgentTask itself to have an agent build a communication methodology and ICP strategy targeting a specific audience.
- **Alireza** will record short individual feature clips and post them to X.com and the community forum for targeted feedback.
- **Alireza** will add a day-in-the-life workflow walkthrough to the AgentTask website and learning page.
- **Ty Wells** will investigate the security/phishing flag on his shef.rocksteady.ai domain using a dedicated tool.
- **Ty Wells** will use Patrick's Training Generator to update some of his training materials.
- **Patrick Chouinard** will continue developing his Stream Deck profile to manage Claude, Codex, and Hermes.
- **Patrick Chouinard** will try OmniGent again and report back to the group.
- **Patrick Chouinard** will deliver AI training to his notary, focusing on document analysis and dossier review workflows rather than a generic step-by-step course.
- **Ryan C** will build out the "Hermes" AI personal assistant (with its own email and Google account) in a full-day session with Scott next week.
- **Ryan C** will implement the email ingest system into his CRM and report back next week.
- **Ryan C** will migrate business files from Dropbox to Google Drive.
- **Juan Torres** will stabilize the image-to-image pipeline and then build an image-to-video pipeline as the next feature.
- **Juan Torres** will create a looping idle-screen animation showing how to use the photo booth to reduce UX friction at events.
- **Juan Torres** will consider routing the video generation experience through the attendee's phone rather than an additional screen.
- **Morgan (mdcatc)** will set up EINs and bank accounts for both Heritage Plot and Class2Curb this week.
- **Morgan (mdcatc)** will use Capterra/G2 via Google Deep Research to research competitor products for Class2Curb and Heritage Plot.
- **Morgan (mdcatc)** will use Patrick's Training Generator to build a Claude Code course for his projects and report back.
- **Paul Miller** will update Ryan C overnight on the outcome of his client pitch meeting.
- **Scott** (not present) is committed to properly demoing his hook-based security review system on a future call.