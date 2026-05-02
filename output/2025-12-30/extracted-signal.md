## general

The session was a casual coaching/community call with Patrick Chouinard, Tom Welsh, Marc Juretus, Ty Wells, and Scott Rippey (scottrippey). The call opened with weather small talk among participants in various cold-weather locations (Canada, UK, Omaha, and Colorado). The group was also anticipating the return of a regular participant named Brendan, who had been absent the previous week.

The main technical throughline was a discussion of Patrick's newly published development workflow — specifically an "implementation loop" built within Shipkit, published as Claude skills in the community GitHub repository. Patrick shared that he had been testing it and it was working well, and he floated the idea of adding a PR skill to automate branching per roadmap subsection. Ty Wells mentioned he had been working on a hackathon project that had its deadline extended, giving him time to expand features. Marc Juretus shared that he had recently built a Next.js/FastAPI project using Claude Code for the first time.

A secondary thread involved billing and usage issues with Claude's API and subscription tiers. Tom Welsh noted he wasn't being billed despite having multiple active subscriptions, and Marc described being locked out of Claude API access after running out of credits before his Pro subscription activated. The group offered troubleshooting suggestions including using incognito windows and checking usage resets in the Claude UI.

## insights

- Patrick's implementation loop workflow, published as Claude skills in the Shipkit community repo, reduces the amount of manual interaction needed and enables more simultaneous work.
- Using Claude skills instead of raw API calls is more efficient for developers; one participant noted "anybody who's coding should not be using API calls."
- Claude has had known invoicing/billing issues — one anecdote described a user retaining Pro access six months after cancelling their subscription.
- Adding a PR skill to the development loop (auto-branching per roadmap subsection) could help keep Git history clean and structured.
- Baking `.gitignore` logic into the automation helps keep repositories cleaner within automated workflows.
- Claude's usage reset date and remaining credits can be checked directly in the Claude UI under Settings > Usage, or via Claude Desktop.

## qa

**Q (Marc Juretus):** I'm in a state where Claude says I can't do anything because I need to insert credits, and I can't log out to log back in with the correct API for the new Pro version. Will I be able to do that in a day?
**A (Patrick Chouinard / Ty Wells):** It should normally resolve, but try an incognito window to log in. Also, you can check your usage reset date in the Claude UI under Settings > Usage.

**Q (Tom Welsh):** I pay $20/month for Claude, $20 for something else, and barely get any bills. What's going on?
**A (Patrick Chouinard):** Claude has had known invoicing issues. A colleague of his cancelled her subscription six months ago and still has full Pro access, so Tom may be in a similar situation.

**Q (Ty Wells):** Is the workflow published in Discord?
**A (Patrick Chouinard):** Yes — posted in the Discord show-and-tell channel, and also in the GitHub Shipkit AI community repo, with the link shared in Discord.

## tools

- **Claude (Anthropic)** — Primary AI used for coding workflows, skills, and API calls; billing issues discussed.
- **Claude Code** — Used by Marc Juretus to build a Next.js/FastAPI project; noted as different but effective.
- **Claude Desktop** — Mentioned as a way to check usage and credit reset dates.
- **Shipkit** — Framework within which Patrick built and published his implementation loop as Claude skills.
- **GitHub (Shipkit AI community repo)** — Repository where Patrick published his development workflow/skills.
- **Discord** — Used to share links and post in show-and-tell; community communication hub.
- **VS Code (with terminal)** — Marc's environment for running Claude Code and API interactions.
- **Next.js** — Framework Marc used in his recent project built with Claude Code.
- **FastAPI** — Backend framework paired with Next.js in Marc's project.
- **Supabase** — Tom mentioned paying ~$45/month for 10 databases; only service actively billing him.

## links

- Shipkit AI community GitHub repo — Location where Patrick published his Claude skills/implementation loop workflow (exact URL not stated, but linked in Discord).
- Discord show-and-tell channel — Where Patrick posted the announcement and link to the published workflow.

## decisions

- Patrick Chouinard will explore adding a PR skill to the implementation loop so each roadmap subsection implementation auto-creates a branch that can be pull-requested.
- Patrick Chouinard will consider baking `.gitignore` logic into the automation to keep repositories cleaner.
- Ty Wells will review Patrick's published Claude skills workflow from the community repo/Discord link.