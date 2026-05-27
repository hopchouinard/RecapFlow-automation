📝 SUMMARY

This week's call covered agentic AI workflows, production PDF extraction, and client monetization. Patrick unveiled his pre-release Community Brain distribution and detailed migration from OpenClaw to Hermes. Brandon shared his overnight parallel Codex workflow. Scott broke down shipping projects including a parking app that generated $5K in its first weekend and a video generation pipeline. Morgan, Juan, Alex, and Bastian presented updates on lobby displays, AI photo booths, multi-tenant architecture decisions, and healthcare partnership negotiations.

💡 KEY INSIGHTS

Spec-driven development only works after clarifying infrastructure, framework, and database choices or it loops endlessly. For high-frequency simple tasks like single-word lookups, use smaller models like Gemini Flash or GPT-4o Mini instead of frontier models to dramatically drop latency and cost without quality loss. When extracting content from complex PDFs, convert each page to an image and feed it to a cheap multimodal model like Gemini Flash with a markdown output prompt, handling tables and flowcharts better than text-only extractors. Hermes offers significant advantages over OpenClaw including cleaner API key management, built-in identity isolation, a Kanban dashboard, recursive self-updating skills, and native Codex integration. AI engagements often serve as a foot in the door for larger consulting relationships where surface-level problems reveal deeper systemic work; focus on high-margin problems for businesses with clear ROI. When building multi-tenant applications, start a brand-new project with organizations as a first-class concept rather than retrofitting existing single-tenant apps to avoid breaking live customers. Adversarial code review using the Codex plugin for Claude Code consistently finds issues that Claude alone misses. Queue up multiple parallel Codex work-tree sessions overnight running self-critiquing iterations on specific goals to effectively double productive hours. Hermes recursively builds and prunes its own skills based on usage to keep system prompts within character limits.

❓ KEY Q&A

Question: Should I use Recap Flow to scan large PDFs and retrieve data?
Answer: No. Recap Flow is built not to digest documents. Use Ollama for embeddings and handle PDF extraction separately beforehand.

Question: I built a vocabulary app prototype but lost momentum when shifting to spec-driven development. When is it worth it?
Answer: Spec-driven development requires a clear infrastructure foundation first. Since you already have mocks and specs, go back through ShipKit's master plan phases, point to your existing work, and let it fill gaps to create a roadmap, then execute phase by phase.

Question: The vocabulary app is slow. How do I fix latency?
Answer: Use a smaller, faster model like Gemini Flash or GPT-4o Mini for single-word lookups. Large frontier models cost more and add unnecessary latency for simple tasks.

Question: Is Hermes productive outside of coding?
Answer: Yes. Every morning it emails asking for your daily goal, then follows up with research, prepped materials, and scheduled jobs, interacting via Discord channels to keep context separated by topic.

Question: Any cons to Hermes?
Answer: Like any independent agent, you must isolate it properly for security. However, it organizes API keys better than OpenClaw with single-place management and clear safety warnings.

Question: For OCRing scanned PDFs, should I use Tesseract?
Answer: No. Convert each page to an image and pass it to Gemini with a prompt to produce markdown. This works far better for complex layouts, tables, and graphics than Tesseract.

Question: Do you use specific prompting to convert flowchart images into Mermaid diagrams?
Answer: For medical protocols, convert decision trees into nested markdown bullet lists rather than Mermaid diagrams as the output needs to be readable plain text for end users.

Question: Do you spawn parallel agents to process each PDF page?
Answer: It is simpler than that. Convert the page to image, base64 encode it, make one LLM call per page, and get markdown back. The complexity lies in handling edge cases like tables split across pages.

Question: I want to make my studio booking app multi-tenant. Any recommendations?
Answer: Build a brand-new project with organizations as a first-class concept from the start. Once it works with dummy orgs, port the existing customer over. Retrofitting risks breaking your current live customer.

Question: Have you found it necessary to add an additional memory layer to Hermes?
Answer: Yes. Honcho was added as an additional memory layer.

🛠️ TOOLS AND CONCEPTS MENTIONED

Hermes — Agentic AI framework replacing OpenClaw with cleaner API management, identity isolation, and recursive skill building, connected to Codex, Discord, Tavily, Firecrawl, and Honcho.
Codex (OpenAI) — Used as a sub-agent tool within Hermes for coding tasks and overnight deep-work sessions with adversarial code review.
Claude Code — Primary coding environment used by multiple members.
Gemini Flash — Cheap multimodal model recommended for converting PDF page images to markdown and high-frequency simple tasks.
Honcho — Memory layer service added to Hermes for enhanced context retention.
ShipKit — Course/framework including master plan phases and prep templates for structured development.
Ollama — Local model runner recommended for embeddings in PDF and RAG pipelines.
Firecrawl and Tavily — Web scraping and search APIs integrated with agentic workflows.
Remotion, ElevenLabs, and Higgs Field — Video generation stack using React-based framework, voice synthesis, and AI scene generation.
ORGO.ai — Cloud full-computer-use machines with API recommended for running Hermes agents in the cloud.
Fieldy — AI meeting note-taker with API supporting wake-word and termination-word patterns for agent commands.

📎 SHARED RESOURCES

Patrick's Community Brain distribution repository
https://github.com/hopchouinard/community-brain-distribution

Hermes autonomous GitHub profile
https://github.com/clara-patchou-ai

OpenAI Codex plugin for Claude Code
https://github.com/openai/codex-plugin-cc

Scott's video generation repository using Remotion and ElevenLabs
https://github.com/scott-rippey/video-generator

Honcho memory layer service
https://honcho.dev/

Wavespeed AI inference dashboard
https://wavespeed.ai/dashboard

Anthropic Claude Code in Action course
https://anthropic.skilljar.com/claude-code-in-action

🔄 FOLLOW-UPS WORTH EXPLORING

Hiral will restart her vocabulary app using ShipKit's prep phases with sequential and parallel LLM calls, switching to Gemini Flash or GPT-4o Mini for latency reduction.

Patrick will test the Community Brain distribution repo before wider release and extract his ChatGPT chat logs for integration into Hermes memory.

Brandon will add Codex adversarial code review to his overnight deep-work sessions and test Scott's video-generator for personalized cold-outreach clips.

Morgan will complete setting up Hermes on a VPS and evaluate ORGO.ai as a cloud alternative.

Scott will share his developer guide documents and n8n Claude Code skill via email to interested members, and will research newsletter monetization playbooks from Milk Road and The Hustle.

Alex will build a brand-new multi-tenant version of his studio booking app with organizations as a first-class concept rather than retrofitting the existing codebase.

Bastian will report back on the healthcare center partnership negotiation outcome.

Tom will investigate the Association of Old Crows as a potential customer for his military membership database application.

Juan will implement Vercel and AWS log drain with alerting for his photo booth application.