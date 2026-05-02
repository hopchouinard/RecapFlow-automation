📝 SUMMARY

This coaching call featured rapid-fire updates from community members building production applications with ShipKit, deep technical discussions on architecture patterns, and innovative workflows for AI-assisted development. Key highlights included Ty's interactive presentation SaaS built over a weekend, Paul's complex route optimization engine combining classical algorithms with agentic AI, and Patrick's voice-driven ideation system using Custom GPTs. The group also covered practical business topics including LLC formation, SOC 2 compliance, and multi-tenant database architecture.

💡 KEY INSIGHTS

Patrick demonstrated a breakthrough workflow moving ShipKit's master ideation process from Cursor into a Custom GPT, splitting the personality, workflow, and template into separate files. This allows voice-based brainstorming while driving to work, generating complete master idea documents without consuming expensive coding tokens, then importing the final output into Cursor for implementation.

Ty showcased "InPerson," an interactive presentation platform built with ShipKit featuring real-time polling, Q&A, and trivia games synchronized between a presenter dashboard and audience mobile devices. The system uses Gamma for slide generation and includes a voice agent for booking consultations, demonstrating ShipKit's flexibility beyond traditional SaaS templates.

Paul revealed a beta route optimization application solving the traveling salesperson problem for New Zealand's retail distribution networks. Recognizing that brute force approaches fail against the mathematical complexity (10^1134 combinations for 500 stores), he combined Dockerized classical algorithms with agentic workflows for pre-optimization logic and post-route analysis, securing purchase orders from major consumer goods companies before the product was fully built.

Brandon assessed OpenAI's new agent builder, rating deployment ease a 10/10 comparable to N8N, but agentic capabilities only a 6/10 due to lack of inter-agent communication and delegation compared to ADK or CrewAI. He noted approximately 20% error rates immediately post-launch but expects rapid improvement.

Mitch and Brandon discussed Vercel's new Fluid Compute tier for long-running LLM chains, offering up to 13-minute timeouts on Pro plans specifically optimized for AI workloads where compute waits for model responses rather than processing locally, potentially eliminating the need for Trigger.dev in some architectures.

Morgan shared a workaround for Windsurf users struggling with reference projects: moving the reference folder to be a sibling rather than child of the main project directory avoids gitignore and indexing conflicts while maintaining IDE visibility.

Prem discovered Cursor's commands feature (`.cursor/commands`) allowing templates to be accessed via slash commands rather than drag-and-drop, though Brandon noted that proper indexing via `.cursorignore` with negation patterns achieves similar accessibility.

❓ KEY Q&A

AlexH asked about OpenAI's new agent builder UI. Brandon explained it offers exceptional deployment simplicity (N8N-level) but lacks agent-to-agent communication and delegation features found in ADK or CrewAI. It functions as single agents passing work sequentially rather than collaborative crews. He observed a 20% error rate immediately after launch but expects rapid iteration.

Mitch asked about handling long-running LLM chains (series of inputs/outputs feeding between models) within the ShipKit stack. Brandon recommended investigating Vercel's Fluid Compute beta, which extends serverless function timeouts to 13 minutes specifically for AI workloads, potentially avoiding the complexity of Trigger.dev for simple LLM chaining.

Hemal asked about LLC formation and business banking for beginners. Jake advised against LegalZoom due to aggressive upselling, suggesting instead using Perplexity for research and direct state filing (approximately $100-500). Brandon recommended single-member LLC for starters but suggested evaluating S-Corp election once revenue stabilizes to avoid double taxation. For banking, Brandon suggested Chase Ink Business Preferred for the signup bonus and point accumulation.

Morgan asked about multi-tenant architecture where multiple clients share a frontend but require separate databases. Brandon clarified that Supabase doesn't natively support multiple production databases per project, suggesting Neon or AWS RDS Serverless v2 for per-tenant database isolation. Paul noted he uses AWS Redshift with separate database files per client for analytical workloads.

Morgan asked about voice AI solutions with lower latency than LiveKit. Ty recommended Retell AI and Bland AI, noting Retell wraps 11Labs and other providers with defensive prompt capabilities. Brandon mentioned Deepgram as a cost-effective alternative ($200 in credits, usage measured in cents per hour) for those building custom implementations.

🛠️ TOOLS AND CONCEPTS MENTIONED

ShipKit - The core development framework being used by multiple members for rapid SaaS deployment

OpenAI Agent Builder - New UI-based agent deployment tool reviewed by Brandon for ease of use but limited agentic features

Vercel Fluid Compute - New compute tier allowing up to 13-minute timeouts optimized for LLM workloads

Tmux - Terminal multiplexer recommended by Mitch for managing multiple cloud code sessions and projects simultaneously

Trigger.dev - Background job processing platform discussed as alternative to Vercel Fluid Compute for long-running tasks

Supabase - Database platform noted to have limitations for true multi-tenant architectures requiring separate databases per client

AWS RDS Serverless v2 - Recommended by Juan for multi-tenant setups allowing clusters of databases with individual connection URLs

Neon - Database platform suggested by Brandon for spinning up separate databases per tenant

Redshift - AWS data warehouse used by Paul for analytical databases with separate files per client

Fern - API specification tool recommended by Brandon for aligning frontend and backend teams through agreed-upon contracts

Vanta - SOC 2 compliance automation platform mentioned by Anthony with pricing around $15K annually for government contracting requirements

GitHub Copilot - Recommended by Patrick specifically for Markdown autocomplete and document editing at $10/month with unlimited GPT-4.1 and GPT-5 Mini usage

Cursor - Primary IDE used by most participants, with discussion of indexing and the new commands feature

Windsurf - Alternative IDE used by Morgan with Warp CLI on Windows

Retell AI - Voice AI platform used by Ty for conversational agents with calendar integration

Deepgram - Voice transcription service recommended by Brandon for cost-effective implementation

Bland AI - Alternative voice AI platform mentioned by Ty

LiveKit - Real-time communication platform mentioned as having latency challenges for voice AI

Ngrok - Tunneling service used by Juan for exposing local development servers to clients

Custom GPTs - OpenAI's feature used by Patrick to create voice-accessible ideation workflows

Cursor Commands - Feature discovered by Prem allowing slash-command access to templates stored in `.cursor/commands`

📎 SHARED RESOURCES

Udemy course "AWS Certified Cloud Practitioner" by Stefan Marek - Recommended by Brandon for cloud certification, approximately 4-6 weeks study time

"Software as a Science" by Dan Martell - Book recommended by Brandon for Paul regarding SaaS sales and growth strategies

"The E-Myth" by Michael Gerber - Book mentioned by Brandon regarding standardization and building scalable business systems

Vanta.com - SOC 2 compliance platform (note: expensive for enterprise/government use cases)

Chase Ink Business Preferred - Business credit card recommended by Brandon for points and travel rewards

Fern API - Tool for creating API specifications to align development teams

Patrick's Custom GPT - Shareable link mentioned for the voice-based ShipKit ideation workflow (check community for link)

🔄 FOLLOW-UPS WORTH EXPLORING

Windows Ragsass compatibility fixes were confirmed resolved during the call; Prem to test the updated release

Google's deprecation of text-embedding-004 model (sunsetting February/June 2025) requires migration path for existing Ragsass implementations; Brandon to provide utility script for reprocessing embeddings to text-embedding-005

Ty's Chamber of Commerce presentation recording to be shared with group for review of the interactive presentation platform

Juan's potential "Five Tip Friday" AWS newsletter or YouTube series for AI developers; community encouraged to support launch

Patrick's Custom GPT sharing link to be distributed for community testing of voice ideation workflow

Multi-tenant architecture patterns for charter school application; Morgan to evaluate soft tenant isolation via RLS versus hard separation via AWS RDS

Voice agent latency optimization strategies; Maxim to be consulted regarding LiveKit workarounds using custom inference endpoints

Cursor commands versus indexing strategies for template management; further testing needed on Windows environments with PowerShell compatibility