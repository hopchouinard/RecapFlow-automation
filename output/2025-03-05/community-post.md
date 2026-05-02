📝 SUMMARY

This coaching call covered practical AI engineering workflows, career strategy for breaking into AI, and monetization approaches for technical creators. Brandon Hancock shared updates on an upcoming comprehensive video about building an AI personal brand, while community members discussed the tradeoffs between Cursor's agent and ask modes, strategies for reducing LLM costs in production, and whether traditional machine learning degrees are worth pursuing versus applied AI skills. The group also provided detailed feedback on landing page optimization, interview preparation for junior developer roles, and technical architecture decisions for voice agents and document ingestion systems.

💡 KEY INSIGHTS

Paul and Brandon discussed Cursor's agent mode, with both expressing skepticism despite its theoretical promise. Paul noted he is moving back to "ask" mode for better control and to update his rules, while Brandon observed that agent mode sometimes "loses control and does not what I want it to do" compared to guided ask mode.

For local embedding generation, Paul uses BGE base EN-V1.5 with 700 dimensions for his recipe database project. Brandon suggested exploring Supabase's recommended GTE small model, noting that smaller models can sometimes outperform larger ones on specific test sets while running faster locally.

Regarding job interviews for junior Python roles, Brandon emphasized the "bucket of stories" method—preparing specific projects that showcase abilities and can be adapted to answer most behavioral questions. For technical portions, he stressed demonstrating object-oriented programming knowledge (abstract classes, interfaces) and asking clarifying questions before coding rather than jumping straight into solutions.

Jake described building a "second brain" RAG system to aggregate Slack, Discord, and other channels into a searchable, personalized knowledge base with prioritized results based on his interests. Brandon recommended keeping it simple with Notion for brain dumps and project tracking.

On the no-code versus traditional development debate, Jake noted his consultancy clients are splitting into specialized groups and increasingly using no-code for proof-of-concepts before rebuilding in traditional tools for production. Brandon agreed no-code excels at rapid iteration but becomes expensive at scale.

Sherif challenged Naveen's plan to pursue a Georgia Tech master's in Machine Learning, arguing that the signal of being accepted is often as strong as completing the program, that universities are 6-12 months behind the current AI landscape, and that frontier models can generate equivalent curricula in minutes. Brandon and Bastian agreed that applied AI skills and building in public create more job opportunities than theoretical ML knowledge.

For reducing Crew AI costs, Brandon recommended switching to cheaper models like o3-mini for appropriate tasks, using output_pydantic for structured data to reduce prompt size, and implementing AgentOps for traceability to identify where agents are looping unnecessarily.

Maksym shared that his car dealership AI launch was postponed due to data dependencies, but they secured a paid trial with a major manufacturer for a voice-based marketing solution using 11 Labs for text-to-speech, building custom rather than using frameworks to maintain integration flexibility with proprietary dealer systems.

❓ KEY Q&A

Q: Paul asked how others handle high-processing development tasks—running locally versus SSH to a remote GPU box?

A: Brandon stated he strictly uses online models to leverage external GPUs rather than local processing. Bastian mentioned using Cohere for local embeddings but prefers OpenAI's text-embedding-3-small for non-proprietary data. Paul explained he moved to local GPU processing for embedding generation to avoid API latency with his 2.5 million recipe database.

Q: Cyril asked for advice on his first technical interview for a junior Python developer role?

A: Brandon recommended the Self-Made Millennial YouTube channel for behavioral interview prep using prepared story buckets. For technical portions, he advised mastering OOP principles, asking clarifying questions before coding (such as scope requirements for a parking lot design question), and being able to discuss abstract versus concrete classes. Jake warned that interviewers sometimes provide prep materials then ask completely different questions, or restrict tool usage to notepad-like environments.

Q: Alex asked about local vision models to extract text from images of old code without using public APIs due to banking security concerns?

A: Paul suggested looking at Microsoft's Phi-4 models (3.5GB parameter versions) runnable locally via LM Studio or similar hosts, noting some require upgraded Ollama versions not yet released. Brandon asked Alex to report back on performance since some vision models struggle with text extraction.

Q: Sagar asked how to reduce costs for his Crew AI financial services agent that was costing £3 per run?

A: Brandon recommended switching to o3-mini which should provide drastic price drops, using output_pydantic for structured outputs to reduce prompt engineering overhead, and implementing AgentOps for traceability to identify and eliminate unnecessary agent loops. He also suggested putting simpler tasks on cheaper models like 4.0-mini.

Q: Naveen asked whether to pursue Georgia Tech's Interactive Intelligence (applied AI) or Machine Learning (theoretical) specialization?

A: Brandon, Jake, and Bastian unanimously advised against the theoretical ML track, arguing it requires deep calculus and theoretical knowledge that does not translate to market value compared to applied AI skills. Sherif suggested Naveen could list the acceptance on his resume as "in progress" to send the signal without completing the program, noting that universities are behind the current AI curve and frontier models can generate equivalent curricula instantly.

🛠️ TOOLS AND CONCEPTS MENTIONED

Cursor Agent vs Ask Mode: Cursor's agent mode allows high-level delegation but can lose control; ask mode provides guided precision preferred by Paul and Brandon for complex codebases.

Plaud and Limitless: AI voice recorders for meeting notes and brainstorming. Plaud costs $160 upfront with $9-20/month plans; Limitless is $40/month with longer wait times.

Crew AI: Framework for multi-agent systems. Discussed strategies for cost reduction including model selection and structured outputs.

Embedding Models: BGE base EN-V1.5 (Paul), GTE small (Supabase recommendation), Cohere, and OpenAI text-embedding-3-small discussed for local versus API-based vector generation.

Second Brain / RAG: Jake's project using retrieval-augmented generation to create a personalized search engine across Slack, Discord, and personal notes.

Vibe Coding: Emerging practice of giving vague prompts like "make a grocery app" and iteratively saying "improve it" to let AI handle implementation details.

AgentOps: Tool for tracing agent execution to identify costly loops and optimize performance.

11 Labs: Speech-to-speech and text-to-speech service used by Maksym for voice agents, with custom enterprise pricing for credits.

LM Studio and Ollama: Local model hosting solutions for running vision and language models privately.

📎 SHARED RESOURCES

Brandon's upcoming AI Authority Accelerator video (hour 20 minutes) covering how to build an AI personal brand, select niches, create content, network, and monetize—releasing tomorrow with waitlist link for additional coaching support.

Self-Made Millennial YouTube channel recommended by Brandon for interview preparation and behavioral question strategies.

Thomas Frank's Notion templates and tutorials recommended by Bastian and Brandon for second brain implementation.

Supabase documentation on GTE small embedding model recommended by Brandon for Paul's local embedding optimization.

🔄 FOLLOW-UPS WORTH EXPLORING

Brandon to send Cyril specific resources on Python OOP interview questions and the Self-Made Millennial interview prep videos.

Brandon to locate and share the Supabase article recommending GTE small embeddings for Paul to test against his current BGE model.

Jake to share specific vibe coding examples and videos with Brandon for potential tutorial content.

Brandon to review Bastian's updated landing page with larger CTA, mobile optimization, and revised thumbnail design for his Crew AI Docker deployment video.

Naveen to watch Brandon's personal brand video and report back on whether it changes his perspective on the master's program necessity.

Alex to test Microsoft's Phi-4 vision models via LM Studio and report back on text extraction accuracy from code images.

Sagar to record a Loom video of his Crew AI financial agent for Brandon to review specific optimization opportunities.

Hackysterio to record a Loom demonstrating his security vulnerability detection agent for technical troubleshooting.