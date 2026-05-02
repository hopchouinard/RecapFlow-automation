## general

This was a weekly group coaching call for members of the ShipKit AI Developer Accelerator community, hosted by Brandon Hancock. The session followed a round-robin format where each participant shared project updates, asked questions, and received feedback from the group.

Topics ranged widely: Alex Rojas shared two client proposals (a contractor lead management SMS app and a legal contract generator) built using an HTML pitch deck format deployed on Vercel. Marc Juretus discussed building a custom web scraper/shopper using Antigravity IDE. Ty Wells previewed a digital photo frame project using Fire Sticks and teased a ShipKit-related project. Paul Miller asked about documentation tooling for a 10-year-old SaaS codebase and discussed Docploy for self-hosting. Patrick Chouinard demonstrated several contributions to the new ShipKit community GitHub repo, including setup automation scripts and a custom GPT file, and showed a Gemini CLI deep-research workflow and an AI-powered HTML prompt builder. Scott (HP) discussed the new Claude Opus 4.5 limits release. Juan Torres shared progress on a vendor name extraction agent with 95–98% confidence. Mitch discussed his AI-generated Facebook video monetization channel. Brandon shared updates on an AI video generation system (Pokemon-themed) using Kling 2.5 and the Sora API, and discussed the upcoming GitHub repo release.

A recurring theme throughout the call was the power of structured AI workflows, using Claude Code as a primary development environment, and the emerging pattern of building "AI employees" via markdown SOPs. The group also discussed tool comparisons between Claude Code, Antigravity, Cursor, Codex, and Gemini CLI.

## insights

- **Patrick Chouinard:** Running the ShipKit "generate diagram" prompt against an entire repo with Claude Code produced ~18,000 lines of documentation in a single two-hour session — a powerful way to bootstrap documentation for legacy codebases.
- **Brandon Hancock:** Automating documentation in CI/CD pipelines (e.g., via GitHub Copilot CLI headless mode) means every PR can trigger a corresponding doc-update PR, keeping docs and code in sync without manual effort.
- **Brandon Hancock:** Building one new markdown SOP ("AI employee") per week compounds quickly — after a month or two you effectively have a small AI workforce handling email, reports, and automations.
- **Patrick Chouinard:** Using Gemini CLI with a single prompt, he scraped the entire ShipKit community site, surfaced the top 10 genuine AI dev questions, and generated a fully cited answer — all in ~3 minutes and one session.
- **Brandon Hancock:** When teaching an agent a browser-based workflow (e.g., in Antigravity or Playwright), do the task manually once with the AI watching, then instruct it to save the process as a reusable SOP — you only have to do it once.
- **Andrew Nanton:** Claude tends to understand intent even with unstructured prompts; ChatGPT/Codex requires more explicit instructions but can outperform Claude on messy, vibe-coded codebases when given that structure.
- **Brandon Hancock:** For AI model selection: Claude handles ambiguous/unstructured input well; ChatGPT/Codex excels when given precise instructions; Gemini sits in the middle for broader problem-solving.
- **Patrick Chouinard:** Replacing PowerPoint with self-contained HTML files (generated via AI) is more interactive, more consistent, platform-independent, has no security exfiltration risk, and can be hosted for free on GitHub Pages.
- **Patrick Chouinard:** Using small, cheap models (GPT-4.1 Mini for content restructuring, Gemini Flash for HTML generation) keeps the presentation pipeline dirt cheap while reserving large models only where design creativity is needed.
- **Mitch:** Facebook monetization is driven more by bounce rate (keeping users on platform) than completion rate — videos should create insatiable demand rather than satisfying resolution.
- **Brandon Hancock:** Buying annual SaaS subscriptions at year-end (e.g., Black Friday) is a tax write-off strategy worth doing intentionally for business owners.
- **Paul Miller (re: legal clients):** Even when a partner says "it's just me deciding," legal partnerships often require co-signers — always identify the full decision-making committee before finalizing a proposal.
- **Brandon Hancock:** For proposals, drop database schema diagrams — they speak a foreign language to clients, and they'll change during build anyway. Keep technical sections high-level.

## qa

**Q (Paul Miller):** What documentation tools tie nicely into GitHub? We tried Confluence and hated it. We need to document an entire existing SaaS codebase.
**A (Patrick Chouinard + Brandon Hancock):** Patrick recommended GitHub Copilot CLI in headless mode within a CI/CD pipeline for automated documentation updates, paired with the ShipKit "generate diagram" prompt to create an initial draft. Brandon added that they use Mintlify for a docs folder in the repo, and set up a workflow where every merged PR triggers a new PR to update the corresponding documentation section. Brandon also recommended doing the documentation task manually once, having the AI observe, then scaling that process across all verticals using Claude Code background jobs.

**Q (Marc Juretus):** For a web scraper/shopper, should I have the AI read all images on a page individually, or use a description-based approach?
**A (Brandon Hancock):** Use page-level screenshots rather than individual image calls — 12 images would mean 12 separate calls. Instead, give the agent instructions to take a screenshot of the full page, scroll if needed, and look for the item by description. Define the available browser tool commands (scroll, screenshot, navigate, click) as constraints and build a multi-step SOP around them.

**Q (AbdulShakur Abdullah):** Is the new Gemini 3.0 model inconsistent? Should I switch from Claude Code and Cursor to Antigravity?
**A (Brandon Hancock):** Brandon hasn't experienced consistency issues personally, attributing it to always providing maximum context via task templates. He uses Antigravity for ~10–20% of tasks as an experiment but Claude Code remains his primary tool at 80–90% usage. He advised against switching — Antigravity's 50-request/5-hour cap makes it impractical for heavy daily development.

**Q (Paul Miller):** Where does Antigravity sit right now — is it still early days?
**A (Brandon Hancock):** Yes, it's early. Claude Code is still the primary workhorse. Antigravity is worth experimenting with, especially for browser-based tasks where it has the best native browser experience, but the 50-request cap per 5 hours is a real limitation for serious development work.

**Q (Andrew Nanton):** Codex doesn't have a plan mode like Claude Code — how do you work around it?
**A (Andrew Nanton):** He manually simulates plan mode by prompting "don't change any code yet, show me exactly what you plan to do first." It works but isn't as elegant as Claude Code's native plan mode.

**Q (Tom Welsh / AbdulShakur Abdullah):** For setting up a simple month-to-month client payment, what's the best tool?
**A (Brandon Hancock):** Use Stripe directly — set up a recurring invoice/subscription inside the Stripe dashboard and send the client a checkout link. Stripe auto-charges the card monthly. Recommend ACH over credit card to avoid the ~3.5% fee; Stripe offers generous free ACH for the first ~200 payments.

**Q (Biggi, via chat):** Can the Pokemon AI video system be published, or is it only for demo purposes given the brand?
**A (Brandon Hancock):** There are existing YouTube channels doing exactly this at scale (one example shown brings in $4,000–$12,000/month in ad revenue). The content exists in a gray area; Brandon used Kling 2.5 because it was the only model that didn't block Pokemon content.

**Q (Juan Torres):** When you automate tasks, do you just put the SOPs into Cursor rules/commands as markdown files?
**A (Brandon Hancock):** Yes — every week he creates one new markdown file defining a new automated task (inputs, steps, human-in-the-loop checkpoints, outputs). Over time this builds an "AI workforce." These aren't Cursor rules per se but standalone SOP documents used with Claude Code.

## tools

- **Claude Code** — Primary development environment used by Brandon and Scott; $100/month plan; used for coding, email, reports, automations, and long-running agentic tasks
- **Antigravity (IDE)** — Google-made Cursor competitor with native browser window; used by Marc and Adam for web scraping and general coding; 50-request/5-hour free tier limit
- **Cursor** — IDE used alongside Claude Code; mentioned as alternative for Playwright-based browser automation
- **Playwright** — Used by Marc for web scraping/image reading within his custom shopper project
- **Gemini CLI** — Used by Patrick for wide/deep web research; Patrick got early access to Gemini 3 Pro version; used to scrape and analyze the ShipKit community site
- **GitHub Copilot CLI (headless)** — Recommended by Patrick for automated documentation generation in CI/CD pipelines
- **Mintlify** — Documentation viewer/editor used in Brandon's Cray repo for the Docs folder
- **Trigger.dev** — Alex's preferred ShipKit template; used for both the contractor lead management and legal contract projects
- **Vercel** — Used by Alex to host HTML pitch deck proposals as shareable links
- **Stripe** — Recommended for month-to-month client billing; ACH payments preferred to avoid credit card fees
- **Docploy** — Self-hosting platform discussed by Paul and Tom; can replace Vercel/Supabase; available pre-configured via Hostinger VPS
- **Hostinger** — VPS provider with pre-configured Docploy setup; mentioned as cheap static file hosting option
- **Sora API** — Used by Brandon and Mitch for AI video clip generation (Pokemon video project)
- **Kling 2.5** — AI video generation model used by Brandon; chosen because it allowed Pokemon content; ~$0.42 per 10-second clip
- **Kia/Ki (kie.ai)** — AI video generation platform mentioned by Brandon as a tool Mitch pointed him toward
- **Crawl4AI** — Python web scraping package used by Tom in Dung Beetle project; has its own CSS that caused specificity conflicts
- **ChatGPT / OpenAI Codex** — Andrew used Codex successfully on a messy PySide GUI codebase where Claude struggled; requires more explicit instructions
- **Google AI Studio** — Brandon uses it with a Google Cloud API key for image generation at ~$0.14/image, bypassing subscription limits
- **Gamma** — Design tool mentioned by Patrick as useful for creating branded presentation templates to feed into his HTML pipeline
- **Fern** — API-first design platform briefly mentioned by Brandon in context of Adam's friend's dissertation topic
- **GitHub Pages** — Suggested as free hosting for Patrick's static HTML presentation files
- **ShipKit** — The community's core boilerplate/template platform; community GitHub repo newly created this week

## links

- **status.claude.com** — Anthropic's Claude API status page; Scott (HP) shared it for monitoring API outages and signing up for email alerts
- **YouTube video by Nate B. Jones** — Dropped by Brandon in chat; deep-dive engineering comparison of OpenAI vs. Anthropic vs. Google models
- **Git Worktrees tutorial video** — Brandon shared a YouTube link about Git worktrees (not subtrees) for running parallel feature branches; described as the clearest breakdown he found
- **Jake Tran YouTube channel/interview** — Brandon shared a link about how Jake Tran cracked the code for faceless YouTube content; recommended to Mitch for content strategy inspiration
- **Juan Torres's AWS SOC 2 architecture video** — Juan shared a video he created showing AWS VPC architecture (database, inference engine, EC2, Elastic Beanstalk) for SOC 2 compliance

## decisions

- **Patrick Chouinard** will submit two pull requests to the ShipKit community GitHub repo: (1) cross-platform setup scripts (Mac/Linux/Windows) automating fork/clone/branch, and (2) the custom GPT agent files he has discussed previously.
- **Brandon Hancock** merged both of Patrick's pull requests live during the call.
- **Brandon Hancock** will publish the AI video generation source code and GitHub repo the following morning (Wednesday).
- **Brandon Hancock** will record and publish a Black Friday course recommendations video.
- **Ty Wells** will demo his ShipKit-related project (described as "10x-ing Patrick's idea") at the next Tuesday call.
- **Ty Wells** will give family members the Fire Stick digital photo frame gift by Thanksgiving so they can build up photos before Christmas.
- **Alex Rojas** will remove the database schema section from his client proposals based on Brandon's and Paul's feedback.
- **Alex Rojas** will keep the group posted on outcomes of his Thursday and Friday client calls.
- **Brandon Hancock** will send Mitch the Jake Tran interview video link for content strategy inspiration.
- **Brandon Hancock** will look up and share the Git worktrees tutorial video with Scott (HP).
- **Brandon Hancock** will investigate and share clarity on the new Claude Opus 4.5 usage limit structure when he finds it.
- **AbdulShakur Abdullah** will use Thanksgiving break to go through ShipKit on his personal computer (work laptop has blocking firewall).
- **Juan Torres** will reach out to Tom Welsh if he needs help with web scraping for vendor name validation.
- **Patrick Chouinard** will aim to have a demo of the Deck AI Forge (HTML presentation pipeline) ready for a future call.
- **Brandon Hancock** will buy annual subscriptions to his tools (including Claude Code) before year-end for tax write-off purposes.