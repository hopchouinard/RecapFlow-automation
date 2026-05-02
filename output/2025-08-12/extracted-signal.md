## general

This was a weekly group coaching/community call hosted by Paul Miller (standing in for the regular host Brandon, who was travelling back from the Caribbean). The session opened with a roundtable discussion on recent model releases — primarily GPT-5 and Claude's updates — covering practical experiences with coding, context management, and temperature settings. Participants then went around sharing individual project updates, questions, and tool recommendations.

Topics ranged from technical deep-dives (MCP server construction, vector databases, local model inference with llama.cpp, context engineering with Repo Prompt) to business and community topics (meetup strategies, government consulting, prompt engineering for clients, publishing content via Notebook LM). The group included developers, consultants, an enterprise architect, a digital marketer, and a music/game creator, reflecting a broad mix of backgrounds and geographies.

A recurring theme was the challenge of maintaining consistency and reliability when using AI coding assistants at scale — particularly around thinking models deviating from plans, context window bloat, and rolling back commits. A secondary theme was how to find and create professional opportunities through local meetups, government contracts, and AI-assisted content publishing.

## insights

- **GPT-5 behaves like a blank canvas**: Patrick noted its base personality is highly malleable and responds well to personality-shaping prompts, rather than being "heartless" — it just requires a different interaction style than previous models.
- **GPT-5 defaults to its weakest sub-model**: Jake observed that GPT-5 is a composite of three models and almost always defaults to the worst one; you have to deliberately prompt it toward the better model.
- **Avoid thinking/reasoning models for coding when the answer should already be in training**: Bastian argued that if a model likely has the answer baked in, a non-thinking model at temperature zero is more reliable and predictable than a reasoning model, which can send a chain of thought off-track and corrupt subsequent tool calls.
- **Thinking model chains are not retained between messages**: Bastian explained that reasoning chains are not fed back into context by default, so a wrong thought in one step can silently corrupt the next without the model being aware.
- **Temperature zero + same seed still doesn't guarantee deterministic output from LLMs**: Jake and Bastian confirmed that while temperature zero gets you closer to repeatability, true determinism is not achievable in practice with current LLMs.
- **Context engineering is more important than prompt engineering**: Andrew surfaced this framing — the real skill is deciding what goes into context, how much, and in what form.
- **Build MCP servers starting with a trivial tool**: Bastian recommended getting a single calculator-style tool working first before adding complexity, to isolate the learning from the implementation.
- **CLI-first approach for MCP**: Andrew shared an article suggesting that building a shell/CLI tool first and shelling out to it may be a more deterministic and predictable path to building an MCP server.
- **Use Repo Prompt's codemap to compress context**: Bastian demonstrated that Repo Prompt's codemap (extracting imports, functions, classes) can reduce token usage dramatically (e.g., 40k → 17k) while preserving enough structure for the AI to reason about the codebase.
- **Deep research agents work better with targeted code context**: Bastian noted that feeding a codemap alongside a specific question to a deep research agent produces much more actionable results than open-ended queries.
- **Layered, validated development beats one-shot generation**: Al described always building and validating one layer at a time rather than one-shotting, which he found consistently more reliable.
- **Claude Code can spiral in troubleshooting mode**: Al observed that Claude Code sometimes generates enormous token streams when stuck in a test-debug loop and requires human intervention.
- **Government and non-tech audiences are extremely receptive to basic AI demos**: Alex found that showing 120 government auditors a simple Claude session produced amazement — the knowledge gap is large and the opportunity is real.
- **Submitting a working POC prototype alongside an RFP increases win rates**: Al shared that teams using AI to build quick prototypes as part of government RFP submissions have seen higher selection rates.
- **Metaprompting compounds over time**: Patrick described writing only the *intent* of a prompt and letting the model generate the actual prompt, with accumulated examples making the process increasingly efficient — now requiring only half a line of intent.

## qa

**Q (Andrew):** Can you say a few words about how you use Repo Prompt and how it fits into your workflow?
**A (Bastian):** Repo Prompt is a native Mac app where you select files from a tree, and it packages their full contents (not tool-call reads) into a structured context block. Its codemap feature extracts imports, functions, and classes to create a compressed summary. You can copy this to any chat interface or expose it via MCP so an agent can dynamically adjust the file selection. It reduced one context from 40k to 17k tokens while retaining enough structure for the AI to understand the codebase.

**Q (Andrew):** If I pointed Repo Prompt at a set of Markdown files with Obsidian-style backlinks, would the codemap trace through those?
**A (Bastian):** The codemap itself won't (it's likely regex-based, looking for imports/functions/classes), but the AI-assisted context-building feature can filter and select relevant Markdown files based on your prompt, so you can still get value from Markdown/Obsidian files through that path.

**Q (Al):** How did you start with the digital marketing agency client — was there a pre-sales process?
**A (Al):** The owner approached him because he sees generative AI as an existential threat to his business. They were already using ChatGPT but in a fragmented, unautomated way. Al is mapping their job descriptions, inputs, and outputs, then building structured prompts. He also discovered the agency is a HubSpot partner, and Anthropic just released an MCP server for HubSpot, which opens significant automation possibilities.

**Q (Paul):** How do you help people learn about prompting — any resources you'd recommend?
**A (Al):** He researched the client's domain (digital marketing) via YouTube, including a video from HubSpot's CMO, to learn the terminology and typical workflow phases. From that he extracted the vocabulary needed to build effective prompts. He offered to share example prompts via Google Drive.

**Q (Patrick):** Does your company have an already-approved cloud provider that could be a route to getting AI dev tools in?
**A (Hemal):** Yes, Google Cloud Platform / Vertex AI is their approved provider. Patrick suggested that getting a tool approved through an already-vetted inference provider is much easier than introducing a net-new vendor, and once security teams get a taste of the tools, they often become advocates for opening further access.

**Q (Jake):** How close are we to deterministic models?
**A (Bastian/Jake):** Not close in practice. Temperature zero gets you closer but doesn't guarantee identical outputs. True repeatability would require temperature zero plus the same seed, but even then variation occurs. Thinking/reasoning models explicitly don't support temperature control in a meaningful way.

**Q (Ammar):** What is the best vector database for a conversational AI / LiveKit project?
**A (Bastian):** The provider matters less than proximity to your LiveKit server. Weaviate has a strong user base; Pinecone is well-known; Supabase with pgvector is what most people are defaulting to now and is very fast. He also suggested decomposing the problem — get the text chatbot working first, then layer in voice/LiveKit.

**Q (Nate):** Are there open-source tools for animating AI-generated images into talking-head style videos?
**A (Jake):** ComfyUI is the main open-source hub for this (requires a GPU). "Ruined" (spelled with three O's — "Ruuined") is another option that's easier to use and open source. For production quality, Midjourney + Runway are the go-to paid options.

## tools

- **GPT-5** — Discussed extensively; coding performance, model-switching behaviour, and personality malleability.
- **Claude / Claude Code** — Used for coding; noted for context issues in long sessions and token spiralling during debugging.
- **Claude Sonnet (1M token context)** — Andrew noted this was enabled during the call, potentially helping with large documentation ingestion.
- **Cursor** — Primary IDE for several participants; noted to slow down significantly with large codebases and long context windows.
- **GitHub Copilot** — Patrick's enterprise-mandated tool; noted major improvements in auto-completion and agent mode with recent updates.
- **Kiro** — New IDE mentioned by Asako; has structured spec/task approach and a "steering" rules feature, but rules are sometimes ignored.
- **Repo Prompt** — Mac app for context engineering; demonstrated by Bastian for codemap generation and selective file context packaging.
- **Context7** — MCP-based tool for pulling in relevant documentation; Bastian recommended it over raw LLMs.txt for more granular, semantically relevant doc retrieval.
- **Fast MCP** — Python library for building MCP servers; Andrew found it convoluted to work with.
- **Notebook LM** — Used by Patrick and Al for generating podcast audio and video previews from written content; praised as a new publishing workflow.
- **Gamma** — AI presentation builder; Al demonstrated generating a full slide deck from a Notebook LM outline in ~10 minutes.
- **Lovable** — Al used it with GPT-5; noticed speed improvement in page rendering.
- **Replit** — Bastian noted it has improved significantly with its agent for building React/Supabase websites with built-in auth and hosting.
- **Google Gemini Deep Research** — Paul recommended it as a top tool for deep research, especially combined with Google Search integration.
- **Genie 3 (Google)** — Jake mentioned it; converts any image into a playable video game environment.
- **LM Studio** — Al mentioned wanting to run the new OpenAI open-weights model locally via LM Studio.
- **llama.cpp** — Andrew described using it to offload layers of the 120B OpenAI open-weights model from GPU to CPU for local inference.
- **Ollama** — Mentioned as built on top of llama.cpp.
- **Alarma (LM cloud hybrid)** — Paul mentioned an update enabling hybrid local/private model hosting with GPU offload to Alarma cloud.
- **Warp** — Terminal with AI agent integration; mentioned by Bastian as included in Lenny's newsletter bundle.
- **WhisperFlow** — Voice-to-text tool; mentioned by Bastian as useful for reducing typing strain.
- **Linear** — Issue tracking integrated with GitHub; mentioned by Bastian.
- **Suno AI** — Music generation tool; used by Aleksandr to generate music lines fed into FL Studio.
- **FL Studio** — DAW used by Aleksandr to remix and style AI-generated music.
- **ComfyUI** — Open-source image/video generation UI; used by Nate for Stable Diffusion workflows.
- **Midjourney** — Mentioned as production-quality image generation for animating AI images.
- **Runway** — Mentioned for production-quality video animation of AI images.
- **Ruuined (focus tool)** — Open-source, fast image generation tool shared by Jake as an alternative to Midjourney.
- **HubSpot MCP server** — Anthropic released an MCP integration with HubSpot; relevant to Al's digital marketing agency client.
- **Supabase / pgvector** — Recommended by Bastian as the default vector database choice for most current projects.
- **Pinecone** — Mentioned as a well-known vector database option.
- **Weaviate** — Mentioned as having a strong user community for vector search.
- **Lenny's Newsletter** — $200/year subscription that bundles pro subscriptions to multiple tools (including Warp, Whisperflow, Linear, Gamma, etc.) plus access to a Slack community of Silicon Valley PMs.
- **Meetup** — Platform used by Al to organise and find local AI community events.
- **Luma** — Event platform preferred by Jake and Asako over Meetup for finding quality AI events.
- **NVIDIA Startup Program** — Paul mentioned it gives generous cloud credits across Google, AWS, and NVIDIA's own infrastructure with a simple application form.
- **LangChain / CrewAI** — Mentioned by Ammar as frameworks he is learning for agentic AI development.
- **LiveKit** — Voice/conversational AI infrastructure; Ammar is building a call-centre bot with it.
- **Cloudflare Pages** — Patrick is using it to auto-publish his ClaraForge content site from a GitHub repo.
- **VS Code** — Patrick uses it with his entire MyDocuments folder as a project for context-rich metaprompting.

## links

- No explicit URLs were shared in the transcript text (Jake mentioned putting a link to "Ruuined" in the chat, but the URL was not captured in the transcript).

## decisions

- **Al Cole** will upload example prompts built for the digital marketing agency client to Google Drive and share the link with the group during the call.
- **Al Cole** will post the Lenny's Newsletter link in the community chat for others to review.
- **Patrick Chouinard** will continue publishing all new ClaraForge content through Notebook LM video pipeline and push updates automatically from the main repo to the Cloudflare Pages site.
- **Aleksandr** will post links to his YouTube channel and SoundCloud in the community chat.
- **Al Cole** offered to share his meetup playbook with Alex Wilson if she decides to start a local group.
- **Hemal Shah** will explore using Gemini CLI / Google Vertex AI as a route to getting AI tooling approved internally, following Patrick's suggestion.
- **Adam** will investigate FFmpeg-based voice-activity detection (VAD) to fix the CPU usage issue with his voice-to-text setup on his virtual machine.
- **Alex (Mexico)** committed to requiring 50% upfront payment for future consulting engagements, and will pursue law firm clients for short Zoom AI training sessions.
- **Paul Miller** will post information about the NVIDIA Startup Program credits in the community forum.