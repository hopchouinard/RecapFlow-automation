## general

This was a group coaching call hosted by Brandon Hancock, bringing together a mix of developers, entrepreneurs, and career-changers working on AI-related projects. The session opened with Brandon sharing two personal updates: his experience with the PLAUD AI voice recorder and the imminent release of a comprehensive "AI Authority Accelerator" masterclass video on building an AI personal brand. The call then moved through individual participant check-ins, each person sharing their current project status and receiving feedback from the group.

Topics ranged widely across technical and strategic domains: embedding models and vector databases for a recipe-matching app (Paul), preparing for a junior Python developer interview (Cyril), building a RAG-based "second brain" system (Jake), creating a lead-magnet landing page and YouTube content strategy (Bastian), career path advice for breaking into AI (Naveen), recovering a broken codebase for an AI assistant called Eleanor (AK), extracting code from images using local vision models (Alex), reducing CrewAI agent costs and enforcing structured outputs (Sagar), building a voice-activated medical intake tool (Nate), launching a voice agent trial with a car manufacturer (Maksym), and developing a survey-based corporate learning evaluation SaaS (Patrick).

The call also touched on broader strategic themes including when to use no-code vs. full-stack development, the value of building a public personal brand over pursuing advanced degrees, and multiple monetization paths beyond just building software products. Sherif offered a particularly pointed perspective on the value of graduate programs in the current AI landscape.

A new participant (hackysterio) building security-focused CrewAI agents was redirected to record a Loom walkthrough for async review, and Andrew shared updates on a speaking engagement with the Massachusetts Psychiatric Society and a Google/Wellcome Trust mental health AI funding opportunity.

## insights

- Brandon: Cursor's agent mode produces inconsistent results; switching back to "ask" mode with tighter control and updated rules often yields better outcomes.
- For large-scale embedding generation, running a local model (e.g., BGE-base-EN-V1.5) on a GPU is faster than waiting on API calls, but smaller models like GTE-small may match performance at higher speed.
- Bastian: Cohere and Ollama are options for local embeddings, but OpenAI's text-embedding-3-small is nearly as good as the large version and is a practical default for non-proprietary data.
- Brandon: On landing pages for lead magnets, the CTA button text should mirror the promise made in the video (e.g., "Get Free Source Code") rather than a generic "Subscribe" to reduce friction.
- Jake: Design landing pages and UIs for "drunk babies" — assume the user is 10 feet away or on a phone; minimize text, maximize clarity, and make the primary action unmissable.
- Brandon: For YouTube thumbnails, lead with the outcome (e.g., "Run CrewAI Enterprise for Free"), not the method (e.g., Docker). Use existing templates rather than starting from scratch.
- Brandon: In a technical interview, asking clarifying questions before writing any code signals good communication and team-readiness; jumping straight to building is a red flag.
- Brandon: Object-oriented programming fluency (abstract classes, interfaces, concrete classes) differentiates junior candidates from those who only write scripts and functions.
- Jake: When a codebase is working, immediately create a named "demo" branch; never overwrite it — create "demo2" for the next stable state.
- Brandon: Build end-to-end shallowly first, then add fallbacks and complexity; adding fallbacks before the happy path works creates compounding debugging difficulty.
- Brandon: The closer your product or service is to where money actually changes hands, the more you will earn — downstream value (e.g., ensuring learning retention) is harder to monetize than upstream value.
- Sherif: Graduate programs in AI are typically 6–12 months behind the current state of the field; frontier models can replicate a syllabus in minutes, and being enrolled (not finished) already sends the credential signal.
- Brandon: For CrewAI cost reduction, assign simpler tasks to cheaper models (e.g., GPT-4o Mini) and use AgentOps tracing to identify where agents loop or over-process.
- Jake: Breaking a large script into smaller, independently tested pieces dramatically reduces context-window regressions when using AI coding assistants.
- Patrick: Adopting test-driven development with AI-generated tests prevents silent regressions as codebases grow beyond ~1,000 lines.

## qa

**Q (Paul Miller):** When doing high-volume embedding generation locally, is SSH-ing to a separate GPU box the standard approach, or do people run it on their dev machine?
**A (Brandon Hancock / Bastian Venegas):** Brandon relies on online models and their GPUs for any heavy processing, so he hasn't faced this locally. Bastian has used Cohere and Ollama locally but defaults to OpenAI's text-embedding-3-small for non-proprietary data. Brandon also flagged that Supabase recommends GTE-small for most vector use cases and offered to send the relevant article.

**Q (Cyril I):** I have a junior Python developer interview on March 10th — any advice?
**A (Brandon Hancock / Jake Maymar):** Brandon recommended preparing a "bucket of stories" (projects that showcase abilities, reusable across many interview questions), referencing the Self-Made Millennial YouTube channel for soft-skills prep. For the technical side, he emphasized OOP fluency (abstract classes, interfaces) and practicing whiteboard-style design questions (e.g., "design a parking lot app") — the key being to ask clarifying questions before writing any code. Jake added that interviewers sometimes ask completely different questions than the prep material suggests, and that in-person interviews may still include a whiteboarding component even without live coding.

**Q (Jake Maymar):** Is "vibe coding" — giving very vague prompts and iterating with "make it better" — something people are seeing gain traction?
**A (Brandon Hancock):** Brandon hadn't tried it yet but was interested; he asked Jake to share specific video examples for review.

**Q (Naveen Selvaraju):** Should I pursue the Interactive Intelligence or Machine Learning specialization at Georgia Tech's online master's program to break into AI in Canada?
**A (Brandon Hancock / Sherif Abushadi / Bastian Venegas):** Brandon advised against the ML specialization — the math depth doesn't translate quickly to employable AI engineering skills, which today is mostly applied AI (using LLMs, agents, RAG). Sherif pointed out that programs are 6–12 months behind the field, that being enrolled already sends the credential signal without completing the degree, and that frontier models can generate equivalent curriculum instantly. Bastian agreed that riding the LLM wave with practical projects is more market-relevant than deep ML theory.

**Q (Alex Wilson):** I have images of old proprietary code and need to extract it locally without sending it to public cloud APIs — any local vision models that can handle this?
**A (Paul Miller):** Microsoft's Phi-4 models (around 3.5 GB) can run locally and support vision tasks. They work with LM Studio if the current Ollama version doesn't yet support them.

**Q (Sagar Passi):** My CrewAI travel-agent-style build costs ~£3 per run with GPT-4o — how do I reduce cost and enforce consistent JSON output?
**A (Brandon Hancock):** Switch simpler tasks to GPT-4o Mini (or the newly released o3-mini) for significant cost reduction. Use AgentOps to trace each run and identify where agents loop unnecessarily. For structured output, use CrewAI's Pydantic output field on each task to enforce a schema rather than relying on prompt instructions alone.

**Q (Patrick Hutchinson):** I'm building a survey-based corporate learning evaluation SaaS — any strategic feedback?
**A (Brandon Hancock / Paul Miller):** Brandon suggested doing the service manually 10 times before productizing it, and positioning as an "expert implementer" of established methodologies rather than claiming to be the originating expert. He also proposed affiliate or referral arrangements with existing specialists as a faster path to revenue. Paul described a recurring subscription model used in sales consulting: standardized video content plus an AI-powered monthly check-in tool that reports progress back to the organizational buyer — embedding the product deeply and justifying ongoing subscription fees.

## tools

- **Cursor** — AI coding assistant; discussed agent mode vs. ask mode reliability and context management
- **PLAUD (P-L-A-U-D)** — AI voice recorder hardware; Brandon demoed it for meeting notes and brainstorming walks
- **Limitless** — AI wearable/recorder; compared to PLAUD on price (~$40/month) and data export ease
- **BGE-base-EN-V1.5** — local embedding model Paul is using for 2.5M recipe vector database
- **GTE-small** — embedding model recommended by Supabase; Brandon suggested it as a potentially faster alternative
- **Qdrant** — vector database Paul is using to store recipe embeddings on a Linux server
- **OpenAI text-embedding-3-small** — Bastian's default embedding model for non-proprietary data
- **Ollama** — local model host; mentioned for running embeddings and vision models locally
- **LM Studio** — local model host; recommended for running Microsoft Phi-4 vision models where Ollama support is pending
- **Microsoft Phi-4** — local multimodal model (~3.5 GB); suggested for extracting code from images locally
- **CrewAI** — multi-agent framework; used by Sagar (financial agent), hackysterio (security agent), and referenced throughout
- **AgentOps** — tracing/observability tool for CrewAI; recommended for identifying cost-inefficient agent loops
- **Pydantic output (CrewAI task field)** — enforces structured JSON output from CrewAI tasks without relying on prompt instructions
- **Notion** — second brain / knowledge management; Brandon uses it with Notion AI for journaling and project tracking
- **Obsidian** — note-taking app Jake previously used before switching to Notion for its export capability
- **Faster Whisper** — local speech-to-text library Nate's medical intake tool uses
- **ElevenLabs** — text-to-speech API; Maksym's team uses it for voice notes in their dealership app and plans to use it for the new voice agent trial
- **Bland AI** — voice agent platform; briefly mentioned as a potential option for Maksym's voice agent
- **Windsurf** — AI coding assistant; Jake mentioned preferring it but cautioned against automation mode
- **Loom** — async screen recording tool; Brandon directed hackysterio to record a walkthrough for async review
- **Canva** — design tool; recommended for YouTube thumbnail templates rather than starting from scratch
- **Perplexity** — search/AI tool; Nate used it to draft his medical review-of-systems template
- **GPT-4o / o3-mini** — OpenAI models; Sagar switched from 4o to o3-mini to reduce per-run costs
- **Langchain / Pydantic / small agents** — agent frameworks mentioned as core AI engineering competencies
- **Hugging Face** — model hub; Bastian mentioned using available vision and other models from it for applied ML use cases
- **Cohere** — embedding model provider Bastian has used locally
- **Supabase** — vector + relational database; AK uses it as a fallback in Eleanor's retrieval stack
- **Chroma** — local vector store; AK's second fallback for document retrieval in Eleanor

## links

- Supabase GTE-small embedding recommendation article — Brandon referenced and offered to send to Paul; specific URL not shared verbally but dropped in chat
- CrewAI Pydantic output documentation — Brandon shared a link in chat showing how to specify structured task output schemas
- Self-Made Millennial YouTube channel — recommended by Brandon for interview soft-skills prep (Thomas Frank also mentioned by Bastian for Notion templates)
- "Building a Second Brain" book by Tiago Forte — Brandon held it up on screen and recommended it for knowledge management
- Google / Wellcome Trust Mental Health and AI Accelerator — Andrew mentioned dropping this in the school forum; up to £3M per approved group, focused on mental health and AI
- Georgia Tech OMSCS program page — Brandon pulled it up on screen while discussing Naveen's master's program options

## decisions

- Brandon will send Paul the Supabase article recommending GTE-small as an embedding model to test for speed improvements.
- Brandon will send Cyril links to the Self-Made Millennial YouTube interview prep videos and a junior Python interview question example video before March 10th.
- Cyril will prepare a "bucket of stories" from past projects and practice OOP whiteboard questions ahead of the March 10th interview.
- Bastian will update his landing page: make the locked-content section more prominent, change the CTA button text to "Get Free Source Code," reduce body copy to 2–3 sentences, and add a PS-style section for consulting/collaboration links.
- Bastian will revise his YouTube thumbnail to lead with "Run CrewAI Enterprise for Free" as the primary text, use an existing Canva template, and add relevant logos (Docker, cloud provider).
- Bastian will revise his video title to "How to Run CrewAI Enterprise for Free with Docker" and restructure the hook to show the end result and enumerate the steps.
- Brandon will review updated versions of Bastian's landing page and thumbnail if sent by late that night or early the next morning.
- Sagar will send Brandon a Loom recording of his CrewAI financial agent for async review and feedback.
- Sagar will switch from GPT-4o to o3-mini and implement Pydantic output schemas on his CrewAI tasks.
- hackysterio will record a Loom of his security-focused CrewAI agent and DM it to Brandon for review.
- Nate will share his voice-activated medical intake tool with his chiropractor friend for beta testing before any broader rollout.
- Brandon will send Nate two links — one for a local speech-to-text model and one for a local text-to-speech model — to improve the voice pipeline.
- AK will target having a live demo ready for the following week's call and will create a dedicated "demo" Git branch to protect working states going forward.
- Brandon will post call notes/resources in the School community group chat after the call.
- Brandon's "AI Authority Accelerator" masterclass video will be published the following morning; participants encouraged to watch and report back.
- Naveen will watch the AI personal brand masterclass video when it drops and report back with feedback.
- Andrew will explore whether his forensic psychiatric evaluation AI project qualifies for the Google/Wellcome Trust Mental Health and AI Accelerator grant (up to £3M).