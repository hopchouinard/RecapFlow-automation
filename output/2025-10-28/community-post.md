📝 SUMMARY

This coaching call covered the latest developments in AI-assisted development, with particular focus on Google's enhanced AI Studio for rapid prototyping, strategies for handling complex document formatting with AI, and tool comparisons between Claude Code, Cursor, and emerging AI browsers. The group shared practical workarounds for common AI limitations including nested list formatting and deterministic output control, while Ty announced an upcoming security scanning tool for community use.

💡 KEY INSIGHTS

Paul highlighted Google AI Studio's recent updates, particularly the build mode that preloads APIs like Google Maps and Places directly into vibe coding projects, enabling sophisticated proof-of-concepts in minutes rather than hours. He noted this is particularly valuable for client demonstrations before committing to full ShipKit builds.

Ty explained his approach to using Claude Skills to achieve deterministic results from non-deterministic models, treating them as pre-programmed steps to ensure consistency in outputs. He contrasted this with MCPs, noting Skills cannot access external data or perform tool calling, making them suitable for different use cases.

Jake identified a persistent limitation across AI models: difficulty maintaining proper nested list formatting (beyond two levels) in legal contracts and documents. Paul proposed solving this by staging content in JSON or XML first, then converting to markdown or docx, leveraging the strict structural rules of data formats to preserve hierarchy.

Rod cautioned that Gemini tends to spiral on complex tasks, even with Pro models, and noted that Google Cloud offers significant startup credits (up to a couple thousand dollars) through their startup school program, making it cost-effective for AI development despite the learning curve.

Ty advocated for a five-minute rule when stuck on technical problems, encouraging immediate community outreach rather than prolonged solo debugging, noting that Discord and other channels often contain solutions that prevent wasted hours.

❓ KEY Q&A

Q: How can AI handle complex legal contracts with nested bullet points and specific formatting requirements?
A: Jake described struggles with models changing wording, breaking indentation beyond two levels, and confusing numbering sequences (switching between uppercase, lowercase, and Roman numerals). Paul suggested using JSON or XML as the intermediate format to enforce structural integrity, then converting to the final document format. Ty offered to collaborate on building a solution using this approach.

Q: What are the practical differences between Claude Skills and MCPs?
A: Ty clarified that Skills work internally without external data access or tool calling, making them deterministic but isolated. MCPs act as black boxes that can process data externally but offer less transparency and control over what happens to the data once it leaves the local environment.

Q: How does Google AI Studio compare to Lovable for vibe coding?
A: Paul explained that AI Studio now offers pre-integrated Google services (Maps, Places, video analysis) through selectable capability cards, then allows direct deployment to Google's platform. While Lovable excels at UI/UX polish, AI Studio provides deeper API integration for data-heavy applications. Paul also mentioned Stitch, Google's UI/UX tool, can now feed designs into AI Studio for the best of both approaches.

🛠️ TOOLS AND CONCEPTS MENTIONED

Alpha Arena: A platform where AI models compete in trading competitions with real money, currently showing DeepSeek outperforming Gemini and ChatGPT.

Claude Memory: New feature in Claude Desktop that maintains context across projects, though participants noted it appears to work per-project rather than globally.

Claude Skills: Anthropic's feature for creating deterministic, step-based workflows within Claude, distinct from MCPs in that they cannot access external APIs or tools.

Claude Code: Terminal-based coding assistant that Ty prefers over Cursor, particularly after building a Telegram bridge for mobile access.

Google AI Studio: Recently updated with build mode that preloads specific Google APIs (Maps, Places, video analysis) into vibe coding projects, enabling rapid proof-of-concepts with real data integration.

Stitch: Google's UI/UX AI design tool that now integrates with AI Studio to provide polished interfaces for technically functional prototypes.

Strawberry Browser: An AI browser Ty tested that completes tasks through extended pondering, suitable for background tasks but slow for interactive use.

ShipKit: Brandon's framework for production-ready applications, contrasted with vibe coding tools used for initial client demos.

JSON/XML Staging: Technique proposed for maintaining document structure when AI struggles with markdown formatting, using data formats' strict hierarchies as an intermediate step.

📎 SHARED RESOURCES

Alpha Arena: Jake shared a link to the AI trading competition platform (specific URL not captured in transcript).

Python Code for Nested Lists: Rod shared Python code in the chat that successfully generates five-level-deep nested lists, offering a programmatic solution to the formatting problem.

Security App: Ty announced an upcoming repository scanning tool for detecting vulnerabilities in AI-generated code, planned for community release within the week.

🔄 FOLLOW-UPS WORTH EXPLORING

Validation of the JSON-to-Markdown approach for legal contract generation, specifically testing whether five-level nesting maintains integrity through the conversion process.

Results from Ty's Claude Skills implementation for deterministic outputs, particularly his adapted approach that modifies the concept for specific use cases.

Comparison of Google AI Studio's deployment pipeline versus ShipKit for production migrations, specifically regarding how easily prototypes transition to scalable applications.

Community testing of Ty's security scanning tool once released, particularly its effectiveness at identifying "AI slop" vulnerabilities in repositories.

Investigation of whether Claude Memory functions differently in Claude Code versus Claude Desktop, as participants observed varying behavior across interfaces.

Review of Gemini 3 capabilities when released (expected within weeks) and whether it resolves the "spiraling" issues Rod experienced with current models.