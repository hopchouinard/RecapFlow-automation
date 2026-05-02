📝 SUMMARY

This coaching call covered a wide spectrum of technical and strategic challenges, from complex optimization problems to career transitions and content marketing. Tom Welsh opened with a vehicle routing dilemma involving 49 rail stations with time windows and multimodal transport constraints, while Michal Simko shared news of his new role at Oracle's Gen AI division and sought architectural advice for persistent agent memory. The group dove deep into implementation strategies, with Brandon Hancock advocating for simplicity in V1 architectures and Maksym Liamin sharing production patterns using Cloudflare Durable Objects. Paul Miller explored thought leadership strategies using AI deep research tools, and Richard discussed technical approaches for multi-character audiobook generation. Bastian Venegas demonstrated an advanced GraphRAG implementation with query rewriting strategies, highlighting the group's focus on practical, production-ready AI systems.

💡 KEY INSIGHTS

Tom Welsh is tackling a complex eco-routing problem with time windows, needing to visit 49 train stations across three regions with constraints including opening hours, transport mode preferences (car for northern regions, train for southern), and a limit of three to four stations per day. Paul Miller shared relevant experience from optimizing Coca-Cola delivery routes, emphasizing the need to balance practical routing with business value prioritization.

Michal Simko announced his transition to Oracle as an Ecosystem Developer in their Gen AI division in Brazil, a role blending technical pre-sales and commercial strategy to help AI-first companies migrate to Oracle Cloud. He attributed the opportunity to a combination of LinkedIn presence, networking, and what he termed "random luck," referencing the book "The Drunkard's Walk."

For agent memory architecture, Maksym explained his production approach using Cloudflare Durable Objects as a fast cache layer for short-term memory (keeping last 15 messages) with overflow to Supabase for long-term storage, using key-value storage rather than vectors for now. Brandon argued for starting "dumb" with a simple messages table containing user ID, conversation ID, timestamps, and full message history, noting that modern LLMs like Gemini 2.0 can handle hundreds of messages without context window issues, making complex vector or graph solutions unnecessary for V1.

Brandon introduced the "strong nodes" concept to Tom for solving the vehicle routing problem, suggesting clustering stations into entry/exit points to reduce 49 individual nodes down to approximately 10, making the computational problem tractable without exponential backtracking.

Paul detailed his methodology for comparing deep research tools (OpenAI, Google Gemini, Perplexity), using competing models to rate each other's outputs and aggregating results in Notebook LM for comprehensive competitive analysis of consumer goods markets.

Bastian showcased a GraphRAG implementation combining semantic chunking, Neo4j graph databases, and query rewriting strategies including HyDE (Hypothetical Document Embedding), decomposition, and step-back prompting to improve retrieval accuracy beyond standard vector similarity.

Richard discussed his audiobook generation project, using OpenAI's structured outputs to create arrays of character-text-emotion objects, with Brandon suggesting mapping multiple voice variants (angry, happy, sad) per character using different voice IDs to simulate emotional range.

❓ KEY Q&A

Michal asked about architecture for midterm and longterm memory in a WhatsApp-based conflict resolution bot for divorcing parents, where conversations are asynchronous and require persistent context about both parties. Brandon recommended a simple relational approach: one messages table with user ID, conversation ID, AI ID, timestamps, and full conversation history passed as context, with proper indexing on user ID for performance. Maksym alternatively suggested Cloudflare Durable Objects for speed with Supabase backup for persistence.

Tom asked how to solve the vehicle routing problem with 49 stations and complex constraints. Brandon suggested using "strong nodes" to cluster geographically close stations into single entry/exit points, reducing the problem space from 49 to roughly 10 nodes, and referenced a YouTube video by Clement featuring a high schooler solving a similar airport routing problem in 57 minutes.

Richard asked about controlling voice sentiment and tone for different characters in an audiobook reader via API. Brandon explained using OpenAI's structured outputs to define character, text, and emotion fields, then mapping emotion variants to specific voice IDs. Bastian clarified that 11 Labs allows passing specific voice IDs via API for any custom or cloned voice, though granular sentiment control may require creating multiple voice variants per character.

Paul asked about strategy for establishing thought leadership on LinkedIn to generate leads for his CRM business. Brandon recommended short demo videos published directly to LinkedIn using Screen Studio, with calls to action like "comment below and I'll DM you the prompt," rather than pushing traffic off-platform to Medium. Richard suggested a product launch funnel format with sequential educational videos leading to a soft pitch.

🛠️ TOOLS AND CONCEPTS MENTIONED

OR Tools - Google's operations research library for solving vehicle routing and scheduling problems
Google Distance API - for calculating travel times and distances between waypoints
Cloudflare Durable Objects - edge-based key-value storage used as fast cache for short-term agent memory
Supabase - PostgreSQL database used for persistent long-term conversation storage
Neo4j - graph database used for knowledge graph and entity relationship storage
OpenAI SDK (new) - mentioned by Richard for agent routing and handoffs between specialized agents
11 Labs - voice synthesis platform for character voices and audiobook generation
Notebook LM - Google's AI research assistant used by Paul to aggregate and query multiple deep research reports
Manus - autonomous AI agent suggested by Brandon for analyzing raw datasets without manual coding
Lovable, Bolt, V0, Replit - AI-powered app development platforms compared for rapid prototyping
Screen Studio - screen recording software recommended for creating LinkedIn demo videos
Azure Document Intelligence - mentioned by Maksym for PDF parsing and layout analysis
GraphRAG - retrieval architecture combining vector similarity with graph-based relationships
Semantic chunking - document processing technique ensuring chunks end at logical boundaries rather than fixed character counts
Query rewriting strategies - including HyDE (Hypothetical Document Embedding), decomposition, paraphrase, and step-back prompting for improving RAG retrieval
Strong nodes - clustering technique for reducing complex routing problems by grouping proximal points into single entry/exit nodes

📎 SHARED RESOURCES

Clement's YouTube video featuring a high schooler solving an airport routing problem using strong nodes - Brandon offered to find and share the specific link with Tom
Category newsletter creator course - Brandon mentioned he would attempt to locate access for Paul regarding LinkedIn content strategy
OpenAI structured outputs documentation - Brandon shared with Richard for implementing character voice mapping
Adam Silverman's LinkedIn profile - Brandon recommended Paul follow for examples of agent space thought leadership

🔄 FOLLOW-UPS WORTH EXPLORING

Developing evaluation frameworks for non-binary outputs such as document summarization quality, where Andrew and Maksym are currently using human-in-the-loop feedback rather than automated evals
Testing Manus or similar autonomous agents on Juan's 600,000-point NYC dataset to compare automated analysis against traditional data science workflows
Architecting multi-agent conflict resolution systems for Michal's V2, potentially using specialized agents for different relationship counseling scenarios with the OpenAI SDK handoff features
Investigating granular sentiment control in voice APIs, specifically whether 11 Labs or OpenAI supports dynamic tone modulation within a single voice ID or requires distinct voice models per emotion
Comparative analysis of Bolt, V0, Lovable, and Replit for full-stack application development, which Brandon plans to address in upcoming content