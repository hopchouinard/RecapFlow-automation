📝 SUMMARY

This coaching call covered advanced AI-assisted development workflows, business strategy for high-value software products, and technical implementation details across multiple projects. Members discussed optimizing API usage costs through strategic plan management, building software that directly impacts revenue streams, automating complex business processes from content creation to customer acquisition, and technical architectures for local and deployed applications. The session emphasized practical tactics for shipping production-ready code using branching strategies, environment management, and model selection based on cost-performance ratios.

💡 KEY INSIGHTS

Scott Rippey recommended stacking AI coding plans to avoid work stoppage, suggesting a $100 Max plan paired with a $20 backup plan to hammer through heavy coding sessions without hitting rate limits. He also emphasized the importance of GitHub branching with separate dev and production instances using Supabase, Netlify, and Stripe test modes to safely iterate on live projects.

Brandon Hancock argued that the highest-value software opportunities exist closest to monetary transactions, citing his fire department SOAP report automation that directly impacts reimbursement amounts. He noted that if turning off your service causes customers to lose money, you have found product-market fit, and advised against working for equity promises without upfront payment.

Ty Wells described building an operational OS for his Firephoto project that automates customer acquisition through autonomous agents handling prospecting, drafting, sending, and follow-up until conversion. He also discussed building a serious cloning tool that replicates existing software like Calendly for personal integration, producing production-ready repositories with full testing and database connections.

Patrick Chouinard showcased Prompt Weaver, an enhanced prompt library featuring assisted prompt creation through intention-based extraction or structured mode with AI improvement loops. He detailed his ShipKit implementation skills that include dependency analysis, impact assessment, confidence checking at 95% thresholds, and automatic roadmap backfilling to create resilient project memory.

Andrew Nanton reported better results with Codex CLI than Claude for certain tasks, particularly regarding environment management with tools like MISON PLOS. He introduced Wails as a solution for building local desktop applications with Go, offering cleaner file system access and easier cross-platform distribution compared to Python or Electron alternatives.

Brandon Hancock shared that he is swapping from GPT 4.1 to Gemini 3 Flash for application workloads, citing comparable quality at lower cost despite slight latency increases, while maintaining Claude for coding tasks.

Morgan Cook recommended Doppler for API key management across multiple projects, enabling secure sharing with developers and easy environment variable access without checking secrets into GitHub.

Mitch detailed his automated video content pipeline using Replicate for face detection and lip-sync analysis combined with 11labs transcription, processing clips for under three cents each to generate content that has reached ten million views.

Ryan described completing a social media automation platform featuring facial recognition, content generation via Nano Banana, automated publishing, and brand voice induction quizzes to manage multiple client accounts with minimal manual intervention.

❓ KEY Q&A

Elijah asked how to deliver ShipKit-built software to clients and whether to accept equity or payment. Brandon Hancock advised removing AI documents from the gitignore before delivery, positioning oneself as delivering outcomes rather than vibe coding, and insisted on upfront payment rather than equity promises to avoid unpaid work.

Marc Juretus asked whether developers use Hugging Face models during development. Andrew Nanton explained he uses narrow-purpose models from Hugging Face for specific tasks like OCR, layout analysis, and PII detection, while Brandon Hancock noted using DeepGram's custom medical model for transcription of specialized terminology.

Scott Rippey asked about costs for the video analysis workflow. Mitch clarified that processing runs approximately three cents per clip on Replicate, with his monthly usage reaching around fifty dollars for substantial volume.

🛠️ TOOLS AND CONCEPTS MENTIONED

Claude Code and Claude Desktop: Primary coding environment for several members, with discussion of Max plans and Opus vs Sonnet model selection.

Cursor: Alternative IDE used alongside Claude, with discussion of $20-22 monthly plans.

Codex CLI: OpenAI's coding agent that Andrew found superior to Claude for certain environment-aware tasks.

Wails: Go framework for building lightweight desktop applications with WebView frontends, recommended over Electron for local file system access.

ShipKit: Development framework with task templates and skills for AI-assisted implementation, discussed extensively by Patrick and Brandon.

Prompt Weaver: Patrick's tool for structured prompt creation, documentation, and lifecycle management with model-specific execution.

Trigger: Background job processing service recommended for workflows exceeding one minute or requiring retry logic.

Doppler: API key and secret management platform for multi-project environments.

Replicate: Cloud platform for running custom ML models like face detection and lip-sync analysis.

11labs: Transcription service used for low-error-rate speech-to-text processing.

DeepGram: Speech-to-text API with specialized medical models for acronym-heavy terminology.

Supabase: Database and backend platform used with branching strategies for dev/prod environments.

PostHog: Analytics platform suggested for tracking user journeys and location-based events in apps.

LLM Guard: Local PII/PHI detection and redaction tool discussed for privacy-sensitive applications.

Gemini 3 Flash: Google's model recommended by Brandon for cost-effective application workloads.

Phi 4: Microsoft's local model tested by Tom for real-world reasoning tasks.

Ponder: AI video editing tool mentioned by Ryan for automated clip assembly.

Nano Banana: Image generation service noted for handling text rendering well in graphics.

🔄 FOLLOW-UPS WORTH EXPLORING

Scott Rippey and Brandon Hancock scheduled a follow-up discussion on implementing PostHog analytics for the Baja tourism pass application to track QR code scans and user lifecycle events without requiring immediate user identification.

Andrew Nanton committed to sharing a repository link demonstrating local LLM Guard implementation for PII detection to replace regex-based solutions.

Tom Welsh offered to locate and share his Medium article detailing real-world testing of the Phi 4 local model against other options using AI judges for comprehension, coding, and logic questions.

Patrick Chouinard planned to attend the next ShipKit call to discuss wrapping his implementation skills into a unified autonomous agent.

Mitch intended to share a link to his viral AI-generated video content with Brandon for review.