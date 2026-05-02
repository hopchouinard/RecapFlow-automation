📝 SUMMARY

This coaching call covered advanced AI-assisted development workflows, sales strategy for high-ticket contracts, and emerging monetization opportunities through AI-generated video content. Members shared practical implementations ranging from automated Git workflows and HTML-based client proposals to sophisticated Facebook monetization strategies and documentation automation for legacy SaaS platforms. The discussion heavily featured tooling comparisons between Claude Code, Anti-Gravity, and Codex, with consensus building around using Claude Code as a primary driver while experimenting with newer agentic IDEs for specific use cases.

💡 KEY INSIGHTS

Alex detailed his approach to sending HTML-based proposals hosted on Vercel for contractor lead management and legal contract automation projects, pricing them at $800 and nearly double for legal work respectively. He built these using Cloud Code to create interactive pitch decks with technical architecture sections.

Patrick contributed automation scripts to the new ShipKit community repository, creating cross-platform bash and PowerShell scripts that handle forking, cloning, and branching to reduce friction for vibe coders unfamiliar with Git workflows. He also shared his custom GPT agent files for community use.

Brandon outlined his AI video generation system costing approximately seven to ten dollars per two-minute video using Kling 2.5, contrasting this with traditional video production costs and timelines. He emphasized this creates leverage for content creators willing to master the workflow.

Mitch revealed his Facebook monetization strategy focusing on pattern interrupts and bounce rate optimization rather than just completion rates. He noted that creating "limitless demand" keeps viewers on the platform longer, generating higher CPMs, with his channel recently hitting days exceeding one thousand dollars in revenue.

Patrick demonstrated using Gemini 3 Pro CLI for deep research across the Skool community, automating the analysis of posts to surface genuine AI development questions and generate detailed, cited answers suitable for community publication.

For documentation automation, Patrick recommended GitHub Copilot CLI integrated into CI/CD pipelines, while Brandon suggested using Mintlify with automated PR analysis to update docs when code changes occur, treating documentation as living code.

Brandon advised Marc that Anti-Gravity works best for experimental tasks while maintaining Claude Code as the primary production tool due to rate limits, suggesting an eighty-twenty split between the two.

Tom discussed architecting queue systems for his Dung Beetle scraping project, moving from full-stack to backend-focused infrastructure with individual user scrape queues to handle detached processing.

❓ KEY Q&A

Marc asked whether to use image analysis or page description when building a custom shopper with Anti-Gravity. Brandon recommended treating the agent as a web driver using page views rather than individual image calls to minimize API requests, suggesting a four-phase prompt structure: input, navigation/search, extraction, and output.

Paul asked for documentation tool recommendations for a ten-year-old SaaS with poor technical documentation. Patrick suggested GitHub Copilot CLI for automated documentation generation, particularly using the ShipKit generate diagram prompt for initial drafts. Brandon recommended Mintlify for documentation hosting combined with CI/CD automation that analyzes PRs and creates documentation update PRs automatically.

Abdul asked about consistency issues with the new Opus 3.0 model. Brandon noted he had not experienced consistency problems but attributed this to using maximum context through structured task templates, suggesting workflow structure matters more than model choice for reliability.

Juan asked how to automate specific procedures within his codebase. Brandon explained his method of creating weekly markdown files containing standard operating procedures that define inputs, seven-step processes, and human-in-the-loop checkpoints, effectively building an AI workforce through accumulated automation documents.

Biggi asked whether DocTloy can replace Vercel and Supabase subscriptions. Paul and Tom confirmed DocTloy functions as a self-hosted alternative where you manage your own VPS infrastructure, with Hostinger offering pre-configured instances, though it requires more manual setup than managed platforms.

🛠️ TOOLS AND CONCEPTS MENTIONED

Anti-Gravity: Google's agentic IDE with built-in browser tools, discussed for web scraping and automation tasks but noted for its fifty-request-per-hour limitation.

Claude Code: Anthropic's terminal-based coding agent, positioned as the primary production tool for most members due to higher rate limits and planning mode features.

Codex: OpenAI's coding agent mentioned by Andrew as effective for messy, vibe-coded repositories where explicit instruction works better than Anthropic's approach.

Gemini CLI / Gemini 3 Pro: Google's command-line interface for AI research, highlighted by Patrick for deep community research and by Brandon for multi-city data gathering workflows.

Cloud Code: Mentioned by Alex for generating HTML proposals and by Brandon for background job orchestration.

Cursor: Referenced as an alternative IDE with Playwright integration for browser automation tasks.

ShipKit: Community repository and template system, with Patrick contributing automation scripts and Git workflow helpers.

Trigger.dev: Alex's preferred ShipKit template for background job processing in his lead management and legal contract applications.

Playwright: Browser automation tool used by Marc for web scraping and recommended by Brandon as an alternative to Anti-Gravity for high-volume scraping.

Mintlify: Documentation platform used by Brandon's team for hosting docs with automated update workflows.

GitHub Copilot CLI: Patrick's recommendation for headless documentation generation in CI/CD pipelines.

DocTloy: Self-hosting platform discussed as a Vercel alternative requiring VPS management.

Hostinger: VPS provider offering pre-configured DocTloy instances.

Crawl4AI: Tom's scraping library causing CSS specificity issues in his Dung Beetle project.

Kling 2.5: AI video generation model used by Brandon for Pokemon content creation at approximately forty-two cents per ten-second clip.

Git Worktrees: Concept discussed by Brandon and Scott for managing multiple branches simultaneously without switching.

📎 SHARED RESOURCES

https://www.youtube.com/@NateBJones (Nate B. Jones YouTube channel covering deep dive engineering model comparisons and AI analysis)

https://status.cloud.com (Cloud service status monitoring site recommended by Scott for tracking API outages across AI providers)

Git worktrees tutorial video (YouTube resource shared by Brandon for managing multiple code branches simultaneously, specific URL not captured in transcript)

Jake Tran interview video (YouTube content strategy interview recommended by Brandon for Mitch regarding faceless video channel growth tactics)

🔄 FOLLOW-UPS WORTH EXPLORING

Patrick's Deck AI Forge project demonstration showing automated HTML presentation generation from raw text inputs, potentially scheduled for next week's call.

Ty's ShipKit project tease involving a ten-times improvement on Patrick's community repository concept, promised for demonstration next Tuesday.

Results from Alex's HTML proposal experiments with contractor and legal clients, particularly pricing validation for the higher-tier legal automation project.

Integration of web scraping validation into Juan's GenTech vendor extraction system, potentially leveraging Tom's recent expertise with Crawl4AI and Playwright.

Mitch's critique of Brandon's AI video generation workflow, specifically regarding story arc optimization and automation potential for Facebook content creation.

Evaluation of DocTloy as a complete Vercel/Supabase replacement for community members considering self-hosting migrations during Black Friday subscription reviews.

Assessment of Claude 3 Opus 4.5 rate limit changes following Anthropic's removal of caps, with Scott and Brandon monitoring usage patterns for production viability.

Review of API-first design methodologies versus MVP approaches for academic versus practical software development contexts, sparked by Adam's dissertation review.