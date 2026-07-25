📝 SUMMARY

This week's coaching call featured project demos and strategic feedback from an international group of AI builders. Hosted by Paul Miller and Patrick Chouinard, the session centered on helping members sharpen their product pitches and demo strategies, with a particular focus on Alireza's launch of AgentTask. The conversation reinforced a recurring theme: show workflows, not features, and identify your ideal customer before building your marketing narrative. Members also noted the dramatic shift in development practices over the past year, with code now being generated almost entirely through AI harnesses rather than manual writing.

💡 KEY INSIGHTS

Don't compete on price alone. Patrick warned that incumbents can undercut pricing overnight, so differentiate through unique workflows or capabilities.

Founders unconsciously skip the "wow factor." The details that feel obvious to creators are often the most marketable to new users.

Use your own product to market your product. Ali was advised to use AgentTask itself to assign an agent the task of building his communication methodology and ICP strategy.

Demo workflow, not features. Multiple members converged on showing a complete 2-3 step user journey from empty state to completed task rather than touring individual features.

Identify your ICP before pitching. Research the ideal customer profile first, then tailor the pitch to their specific pain points.

Record short single-feature clips. Post focused demos to X or the forum to gather targeted feedback rather than lengthy walkthroughs.

AI "slop" is a moving target. What counts as high-quality AI output today becomes tomorrow's slop as models retrain on it, requiring continuous skill updates.

Teach skills by example. Feed the AI examples of wrong versus right output, then have it update the skill each cycle to iterate toward 90% first-pass quality.

Use a verifier skill. For design automation, a separate skill that evaluates output against criteria is more reliable than hoping the generative step self-corrects.

Observe before training. Watch clients work to identify pain points, then have Claude build a plan rather than delivering generic step-by-step courses.

Highly regulated fields are ideal for AI document analysis. Legal and notarial work is text-based and procedurally defined, making it easier to augment if RAG resources are properly provided.

Robinhood's agentic account is sandboxed. The agentic account is completely separate from personal accounts and cannot execute trades on them, only read data.

The pace of change is striking. One member observed that a year ago he was writing code alongside AI; now he writes nothing manually.

Idle-screen animations reduce UX friction. A looping 10-second animation showing a persona using the product can guide users who don't know what to do.

❓ KEY Q&A

Patrick Chouinard asked Alireza Mounesisohi: From day one with an empty universe, what is the path a new user takes to create their first project, add tasks, notes, and skills, and hand them to an agent?
Alireza replied that users can talk directly to the board agent, click New to select a project, or use Claude or Cursor with the MCP connection to create tasks and projects conversationally, then let the agent update them as work progresses.

Patrick asked Alireza: Why use AgentTask instead of just telling Claude to create a task in Jira, Linear, or GitHub?
Alireza explained that AgentTask is that layer, but adds claim ID and session tracking to know which agent on which computer made which change, plus an integrated notes, skills, and crews system with a simplified interface for users who find Jira overwhelming.

mdcatc asked Juan Torres: How much did the quinceañera event cost in AI tokens?
Juan answered $52 total for 859 jobs across a multi-model system generating nine AI images per session.

Shakur Abdullah asked Ryan C: Have you tried CodeRabbit for security reviews?
Ryan replied that Scott, a community member, tried CodeRabbit and then built his own hook-based local check system that outperforms it, which Scott will demo properly on a future call.

Ty Wells asked Patrick Chouinard: How are you using the Training Generator at work?
Patrick explained that Claude Code maintains the training content off the GitHub repo for Claude Code itself, updating the material and generating a differential course whenever there is an update.

Juan Torres asked Patrick Chouinard: Do you recommend Claude Co-Work or Codex for a non-technical client like a notary?
Patrick recommended Co-Work for now because it is more accessible to non-technical users, while Codex feels more like a developer tool at this stage.

mdcatc asked Morgan: Have you looked at G2 or Capterra to research competitor products for Class2Curb?
Morgan had not yet looked at G2 specifically. The suggestion was to use Google Deep Research pointed at Capterra and G2 to extract user positives and negatives for a requirements comparison.

🛠️ TOOLS AND CONCEPTS MENTIONED

AgentTask (agent-task.com): AI-integrated task management platform connecting to Claude, Cursor, Codex, and others via MCP.

Claude / Claude Code: Primary AI harness used across projects for coding, document analysis, and training.

Cursor: AI coding environment used as an MCP-connected harness.

Robinhood agentic account: Sandboxed trading account with MCP integration allowing Claude to read portfolio data and execute trades only within the agentic account.

Codex / OpenAI Codex: Coding model discussed as better token value than alternatives.

Firecrawl: Web scraping tool used to extract assets and copy from websites.

Training Generator: Patrick's open-source Claude Code plugin that generates interactive training courses from repo content.

OmniGent: Meta-harness that orchestrates multiple AI harnesses.

Fable: Security and code review tool now permanently included in Claude Code subscriptions.

Skill Arena: Ty's skill running multiple design agents in competition for better front-end output.

Verifier/Observer skill: A separate skill that evaluates design output against criteria rather than relying on self-correction.

NotebookLM: Tool suggested for generating video and audio training content.

Claude Co-Work: Interface considered more accessible than Codex for non-technical users.

Stream Deck: Hardware being repurposed to replicate OpenAI's Codex Micro keyboard functionality for managing AI tools.

Google Deep Research: Suggested for scraping G2 and Capterra reviews for competitive analysis.

LibreOffice / Inkscape: Used in book publishing pipelines for manuscript and cover generation.

📎 SHARED RESOURCES

https://agent-task.com — Alireza's AgentTask platform

https://github.com/hopchouinard/Training-Generator — Patrick's open-source Training Generator plugin for Claude Code

https://shef.rocksteady.ai — Ty's meal prep app built for his daughter

https://homecue.ai — Ty's home energy monitoring application

https://class2curb.com — Morgan's Class2Curb product website

https://omnigent.ai — OmniGent meta-harness platform

https://github.com/trayders/trayd-mcp — Robinhood trading MCP repository

https://robinhood.com/us/en/newsroom/robinhood-presents-yes-no-event/ — Robinhood newsroom article on agentic features

https://www.youtube.com/watch?v=s5T5oQJcJ6U — Matt Pocock's video on his Teach skill

https://github.com/mattpocock/skills/tree/main/skills/productivity/teach — Matt Pocock's Teach skill repository

https://www.aihero.dev/skills — AI Hero skills directory

https://gist.github.com/hopchouinard/333cc020bbdc4ccede8ea023c3b6d62c — Patrick's GitHub Gist

🔄 FOLLOW-UPS WORTH EXPLORING

Scott will demo his hook-based local security review system that outperforms CodeRabbit on a future call.

Patrick will report back on testing OmniGent again after finding it promising but buggy.

Alireza will use AgentTask itself to build an ICP strategy and communication methodology, then record short single-feature clips for feedback.

Juan will create a looping idle-screen animation for his photo booth to reduce UX friction and explore routing video generation through attendees' phones.

Morgan will set up EINs and bank accounts for Heritage Plot and Class2Curb, plus use Google Deep Research on G2 and Capterra for competitive analysis.

Ryan will build out the Hermes AI personal assistant in a full-day session and implement the email ingest system into his CRM.

Patrick will deliver AI training to his notary focused on document analysis workflows rather than generic courses.

Juan will stabilize the image-to-image pipeline and build an image-to-video pipeline as the next feature.

Ty will investigate the security flag on his shef.rocksteady.ai domain and use Patrick's Training Generator to update materials.