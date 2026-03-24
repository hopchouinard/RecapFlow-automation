📎 SHARED RESOURCES

RecapFlow Documentation Site (Patrick's automated meeting recap project)
https://recapflow.patchoutech.com/

Assay AI (Ty's hallucination-reduction project)
https://tryassay.ai

OpenArt Suite (multi-model image and video generation)
https://openart.ai/suite/home

AI Engineer YouTube Channel (agentic systems, described as up-to-date YC-equivalent content)
https://www.youtube.com/@aiDotEngineer

Nate Jones YouTube: Choosing Coding Models (highly recommended by community members)
https://www.youtube.com/watch?v=09sFAO7pklo

Lenny's Podcast YouTube (how companies are reorganizing in the AI era)
https://www.youtube.com/@LennysPodcast

Karpathy AutoResearcher Post
https://x.com/karpathy/status/2031135152349524125

Fine-Tuning Modalities Video from AI Engineer channel (rated 10/10, presented by OpenAI employee)
https://youtu.be/JfaLQqfXqPA?si=7-dSakV1q98LNsvf

Kimi Code (potential Claude Code supplement or review alternative)
https://www.kimi.com/code/en

CMUX Terminal (gives Claude Code genuine CLI-level terminal and browser control)
https://www.cmux.dev/

Symphony by OpenAI (multi-agent coordination using Linear as task board)
https://github.com/openai/symphony

Claude Facial Expression Analysis via Claude Code (Matt Berman YouTube)
https://www.youtube.com/watch?v=cHgCbDWejIs

Fieldy AI (wearable ambient audio capture with webhook and N8N integration)
https://www.fieldy.ai/

NVIDIA Startup Cloud Credits Program (up to $250K in Google Cloud credits for qualifying startups) — Paul offered to post the application form in the School community forum. Watch for that post.


❓ KEY Q&A

Q: How do you reduce hallucination and drift in AI agents?

Patrick: Maintain rich, up-to-date context through specs and roadmaps. Update specs after every completed feature. Good context is not the same as more context.

David: Treat it as an architecture problem. Use a Golden Master agent with ephemeral spawns for most interactions. Use sentiment analysis to flag only the interactions that reveal knowledge gaps, then train only the Golden Master on those.

Both approaches converge on selective, high-quality memory management rather than feeding everything into context.


Q: What is the best approach to UX when a platform has too many features?

Ty: Use wizard-style onboarding that shows only a few actions at a time. Let users graduate to advanced views.

Tom: Do not gray out unused features — hide them entirely. Only show what is enabled.

Morgan: Implement context switching at the user level. A single login holds multiple roles, and switching context changes the entire menu to reflect only what is relevant to that role.

Paul: Use AI to define user personas and map which features each persona needs at each stage of their journey. Build progressive disclosure into the navigation.

Feature visibility should be role- and context-driven, not just toggled on or off.


Q: How do you make a SaaS app production-ready with minimal bugs, especially when financial transactions are involved?

Paul: Start with ground-truth unit tests that validate core calculations. Be very prescriptive in prompting the AI to define what those test areas must be. Also build browser-based UI testing, not just API testing.

Juan: Define an acceptable margin of error upfront. Agentic AI coding can catch bugs that experienced engineers miss.

Patrick: Claude Code Review is Anthropic's own internal review process. It examines the entire codebase holistically when a branch is merged, not just the PR diff. Estimated cost is around $15 per review. Currently requires Teams or Enterprise plan.

Bastian: Using the same model to write and review code introduces shared bias. Code Rabbit is a viable alternative for independent review.


Q: What is the best approach to seed funding for an AI startup?

Paul: Build a POC first. Get at least one paying or discounted early customer to validate demand. Investors want to see that you have tested with real people, know your total addressable market, and have put your own money in first. YC videos are valuable for the questions they ask, but their assumption that you need a large team upfront is outdated. Use NotebookLM to ingest YC content and get it to coach you on first steps.

David: Local entrepreneur networking groups are a good place to find early testers. Offer a discount rather than free access to ensure real engagement.


Q: Should you file a provisional patent to protect your idea?

Paul: Real protection comes from agility and deep industry vertical credibility, not patents.

Tom: Patents must be filed per country for full protection, which is expensive. A comprehensive software agreement is more practical. Accept that some copying from certain regions is unavoidable.

For most AI software startups, speed to market and domain expertise are more defensible than patents.


Q: Is Claude noticeably slower recently?

Ty and David both confirmed the pattern. Anthropic introduced a fast mode that costs more, and standard mode appears to have been throttled to create a paid tier differential.


Q: What are the tradeoffs of using Claude Code with a non-Anthropic model?

Patrick: Anthropic provides scaffolding and agentic tooling on top of the Claude model that is not available when substituting another model. You get good code generation but lose many of the built-in agentic capabilities. Speed is better with alternatives, but nothing currently matches Codex Spark for raw speed, at significantly higher cost.


💡 KEY INSIGHTS

Good context beats more context. Feeding an AI agent large amounts of loosely relevant information increases hallucination risk. Curated, structured, up-to-date specs outperform volume.

Treat hallucination as an architecture problem, not just a prompting problem. Ephemeral agent spawns with a controlled Golden Master and sentiment-based selective training is more robust than trying to prompt your way out of drift.

Feature gating has a real cost argument beyond UX. If you offer all features to all users at all times, you pay infrastructure costs for features they never use. This is a pricing and margin problem, not just a design problem.

Context switching in UI is more powerful than role-based access alone. A single user with multiple roles who can switch their view context gets a cleaner, more focused experience than one who sees everything grayed out or hidden behind settings.

Claude Code Review is Anthropic's own internal process. It is not a third-party tool — it is what Anthropic uses to review Claude Code itself. The roughly $15 per review cost means it should be used selectively on significant merges.

Using the same model to write and review code introduces shared bias. A different model or tool for review provides more independent signal.

CMUX gives Claude Code genuine terminal control. By scraping the CMUX docs and giving Claude Code access to the terminal, it can open multiple windows, type commands, manage processes, and control a browser without custom scripting.

The Contributor Model as a business transformation framework. Ty Wells is implementing a three-bucket model (Digital, Judgment, Contributor) to restructure employee roles. AI handles digital work; humans focus on judgment calls and contributing new ideas. Being rolled out bottom-up with transparent contribution dashboards and monetization incentives.

For receipt and expense apps, the highest-friction point is requiring users to open the app. The most valued workflow is: take photo, share to app, done. Reducing steps to one action dramatically increases adoption.

Patrick's automated meeting recap workflow merges Zoom chat logs and Fathom transcripts via N8N, extracts links, Q&A, and insights, generates a structured recap, and drafts the next week's community invite — all triggered automatically after each call.


🛠️ TOOLS AND CONCEPTS MENTIONED

Claude Code — Primary AI coding agent used by multiple members. Recently introduced fast mode at higher cost.

Claude Code Review — New Anthropic feature (~$15 per review) that performs holistic codebase review on PR merge. Currently Teams and Enterprise only.

Fathom — Meeting recorder with API and webhook support. Used to pull raw transcripts for automated processing.

N8N — Workflow automation platform. Used by Patrick to build the meeting recap pipeline.

Hedra — AI video generation platform with custom character creation from green screen footage.

OpenArt — Multi-model image and video generation platform with storyboard mode. Suggested as a Hedra alternative.

CMUX — Terminal multiplexer that gives Claude Code CLI-level control of terminal windows and browser.

Kimi Code — Chinese AI coding tool raised as a potential supplement to Claude Code for review diversity.

Code Rabbit — Independent AI code review tool. Recommended to avoid model bias when reviewing code written by the same model.

Symphony by OpenAI — Multi-agent framework using Linear as task board. Agents provide proof of work including walkthrough videos.

Cloudflare D1, R2, and Pages — Backend-as-a-service for static and hybrid sites. Free tier covers significant functionality.

Fieldy AI — Wearable ambient audio capture device with chatbot query interface and webhook and N8N integration.

QDrant — Vector database. Patrick is planning to add it to the recap pipeline to accumulate and query knowledge across weeks.

Codex Spark — OpenAI's fastest coding model. Included in the $200 per month plan but consumes credits twice as fast.

Qwen (9GB local model) — Open-source model being explored as a local alternative to reduce Claude API costs.

Golden Master plus Ephemeral Spawns — Architecture pattern for multi-agent systems. One persistent trained agent; all other interactions are stateless and discarded unless flagged for training.

Contributor Model — Ty Wells' business transformation framework with three buckets: Digital, Judgment, and Contributor.

User Context Switching — UX pattern where a single login holds multiple roles and the entire menu and view changes based on selected context.

NotebookLM — Suggested as a way to ingest Y Combinator video content and use it as a coaching resource for fundraising preparation.

NVIDIA Startup Credits — Up to $250K in Google Cloud credits for qualifying startups.


🔄 FOLLOW-UPS WORTH EXPLORING

RecapFlow live output — This was its first real run on an actual meeting. Check the School community forum post-call to evaluate quality. Future enhancement: adding QDrant for cross-week knowledge accumulation.

Claude Code Review practical evaluation — Multiple members agreed to wait a week for community members and YouTubers to test it before committing to the cost. Worth revisiting next call.

Mitch and David collaboration on AI video generation — David is looking for a better and cheaper alternative to Hedra. Mitch was identified as the community's resident expert. Worth confirming if they connected and what was learned.

NVIDIA startup credits form — Paul offered to post it in the School community forum. Worth confirming it was posted and sharing the direct link.

Ty's Contributor Model rollout — Ty is mid-implementation across two businesses. A follow-up on staff response and whether the contribution dashboard is driving behavior change would be valuable.

Kimi Code as a Claude Code supplement — No one has done a direct comparison yet. Worth a structured test and report-back.

Karpathy AutoResearcher — Patrick is actively experimenting with it on a local Qwen model. An update on whether it produces meaningful fine-tuning improvements would be worth sharing.

Morgan's Heritage Plot cemetery platform demo — Morgan committed to having enough ready for a demo next week. Directly relevant to the UX and context switching discussion from this call.

David's salesvelocity.ai — David is bootstrapping and looking for collaborators and funding. Worth a check-in on progress and whether any community members followed up on his collaboration offer.


📝 SUMMARY

This was a high-signal call covering a wide range of practical topics including AI agent architecture, production code quality, UX design for complex platforms, startup funding strategy, and the evolving AI tooling landscape. The strongest themes were the importance of curated context over raw volume in agentic systems, the value of independent code review to avoid model bias, and the business case for progressive feature disclosure tied to user roles and context. Patrick's automated meeting recap pipeline — which produced the very documentation site linked above — was a standout demonstration of community-built tooling. Several follow-ups are worth tracking next week, including Morgan's platform demo, community feedback on Claude Code Review, and updates on Ty's Contributor Model rollout.