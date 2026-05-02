## general

This was a group coaching/community call hosted by Brandon Hancock, who announced it was his final week at his full-time job before transitioning to full-time content creation focused on AI and developer tools. The session followed a round-robin format where each participant gave updates on their projects and asked questions of the group.

Topics ranged widely: Andrew Nanton and his collaborators (Maxim and Emilio, joining from Mexico) discussed scaling an AI app for LATAM car dealership salespeople to ~30,000 users; Bastian Venegas demoed a browser-based tool he built for a law firm to generate JSON schemas for insurance document search; Asako shared her podcast project using Microsoft Autogen for agent-to-agent conversation with ElevenLabs voice synthesis; Richard discussed building an SEO agent for Shopify and a multi-voice audiobook concept; Juan Torres prepared for an upcoming live presentation on AI agents and Federal Reserve data; and Cyril I. reported on being in final-round interviews at multiple companies simultaneously. Paul Miller shared excitement about Google's newly released Gemini 2.5 Pro model and his ongoing exploration of graph databases via Neo4j.

Brandon also sparked a broader discussion about AWS Bedrock Flows (which he had just discovered as an N8N-style visual workflow builder), SageMaker versus Bedrock, and the competitive AI landscape between Google and Amazon. The call closed with a discussion about NVIDIA's Project Digits personal supercomputer, which Richard had already reserved.

## insights

- Brandon: N8N-style automations are great for personal use, but building apps for other people requires leaning back on full developer tools (AWS Bedrock, GCP Gemini stack, etc.).
- Paul: Google's search advantage over other LLM-augmented search tools stems from its underlying graph database that links knowledge entities across the internet — combining that graph with an LLM produces superior results.
- Brandon and Paul: The long-term AI infrastructure race is likely Google vs. Amazon (via Anthropic partnership), with Microsoft/OpenAI potentially losing ground due to cost and model quality concerns.
- Mitch: For live presentations where you want the audience to feel empowered to run code, hard-coding a demo API response as a fallback is a practical safety net — avoids live failures without sacrificing the sense of agency.
- Richard: Lawyers on contingency/settlement models are more incentivized to adopt AI efficiency tools than hourly-billed lawyers, who can always add minimum billing increments regardless of actual time spent.
- Bastian: SageMaker is best suited for large enterprises needing fine-tuned model management; for most current client needs, Bedrock is sufficient and far simpler to work with.
- Brandon: Deploying AI agents securely is still very hard — AWS Bedrock's private network architecture is one of the first platforms enabling agents to communicate within a secure, contained environment.
- Tom: Cursor's context window has improved dramatically — he ran a continuous prompting session for 4–5 hours writing Jest tests without hitting context limits.
- Brandon: Mastering the native agent/workflow tools being released by Google and AWS now could be a major differentiator, as enterprises want to build on trusted, established platforms.
- Paul: AWS billing on certain agent services can be unexpectedly expensive — always check pricing before using higher-level Bedrock agent features.

## qa

**Q (Richard):** Does FFMPEG work with audio — like to mute it, make it louder, stitch it together?
**A (Brandon):** Yes, 100%. FFMPEG handles audio files (e.g., MP3) the same way it handles video. For a multi-voice audiobook, generate a sound byte per speaker per line, number them in order, and use FFMPEG to concatenate them sequentially.

**Q (Richard):** If you link two NVIDIA Digits units together, can you run a 400 billion parameter model?
**A (Bastian):** You can fit a larger model across both units, but the interconnect is faster than Ethernet yet slower than on-chip communication, so there will be a speed bottleneck. You gain capacity but lose some inference speed compared to a single unified system.

**Q (Sam):** What low-code tools do people use to quickly spin up a proof-of-concept to demo to a non-technical audience?
**A (Brandon):** For simple in-and-out document operations (e.g., pull from Google Docs, check criteria, write back), Make is very straightforward. If you need an actual agent with multiple iterations, N8N gives you more flexibility. The right choice depends on whether you need persistent memory or multi-step agentic behavior.

**Q (Mitch):** What is GitHub Pages and how does it work for hosting?
**A (Brandon):** GitHub Pages lets you publish a static HTML/CSS/JavaScript site directly from a repository. Your site deploys to `[username].github.io`. It's ideal for simple static sites like support pages or portfolios, not for dynamic applications.

**Q (Juan Torres):** Should I require attendees to create their own API keys during the live workshop, or use a shared key?
**A (Brandon/Mitch/Richard):** Brandon recommended giving attendees their own keys so they have something to use afterward and to avoid rate limits from many simultaneous requests. Mitch suggested hard-coding a demo API response as a fallback so the demo still works if the live API call fails. Richard agreed a backup is essential since demos frequently break live.

**Q (Asako):** Does ElevenLabs support agent-to-agent conversation for podcast generation?
**A (Asako, self-answered):** ElevenLabs' conversational AI does not support agent-to-agent conversation. She switched to Microsoft Autogen, which supports group chat with preserved conversation history between agents, then passed the generated text to ElevenLabs for voice synthesis.

**Q (Asako):** Are there voice/TTS models with better multilingual (specifically Japanese) capability than ElevenLabs?
**A (Bastian):** OpenAI's newly released text-to-speech models show dramatically reduced error rates across all languages compared to previous generations and outperform Whisper on speech-to-text. They are likely the current state-of-the-art attempt for multilingual voice generation.

## tools

- **AWS Bedrock Flows** — Brandon discovered it as an N8N-style visual workflow builder for AI agents inside AWS; discussed pricing concerns
- **AWS Bedrock** — Paul uses it for client projects; praised for security architecture and Nova models; Anthropic models available via Amazon's investment
- **AWS SageMaker** — Bastian explained it's best for large-scale fine-tuning and model management, not typical client agentic workflows
- **Google Gemini 2.5 Pro** — Paul highlighted as newly released, 1M context (expanding to 2M), API accessible, strong for document analysis
- **Google Gemini Advanced (gemini.google.com)** — Paul demonstrated uploading large documents for analysis; free with sign-up
- **Notebook LM** — Mentioned as comparison point for document analysis and audio summary generation; Paul found Gemini Advanced comparable
- **N8N** — Referenced repeatedly as the dominant low-code automation tool; Paul transitioning to it for faster prototyping
- **Microsoft Autogen** — Asako used it for agent-to-agent podcast script generation with group chat and agenda-based conversation flow
- **ElevenLabs** — Used by Asako for voice synthesis from Autogen-generated scripts; Richard planned to use for multi-voice audiobook; noted weak Japanese support
- **OpenAI text-to-speech (new models)** — Bastian and Richard discussed using for audiobook project; supports emotion/pace customization; better multilingual than prior generation
- **FFMPEG** — Richard asked about using it to stitch together per-character audio clips for a multi-voice audiobook
- **Sesame** — Scott and Bastian recommended it as an alternative voice tool; described as "uncanny" quality
- **Cursor** — Tom used it extensively for writing Jest tests; noted dramatically improved context window (4–5 hours of continuous prompting)
- **Jest** — Tom spent 8 hours learning it to write functional tests for his web app before a CVE-related upgrade
- **Neo4j** — Paul is taking a course on it to understand graph databases before building a graph RAG system
- **Cloudflare Workers** — Emilio/Maxim's team used it for authentication in their car dealership WhatsApp app
- **Open Web UI** — Scott is deploying it alongside a full-stack marketing app on a VPS for script writing and AI filmmaking workflows
- **Windsurf** — Bastian built his insurance JSON schema tool in it; completed in ~two iterations
- **Plotly** — Juan mentioned using it for data visualization in his Federal Reserve data presentation notebook
- **Google Colab** — Juan's workshop participants will run code in Colab notebooks; discussed API key distribution challenges
- **Shopify** — Richard's SEO agent posts blog drafts directly to Shopify, pulling internal links and product images
- **NVIDIA Project Digits** — Richard reserved one; discussed running 200B parameter models locally for ~$3,000; two units can be linked

## links

- `gemini.google.com` — Paul's recommended entry point for trying Gemini 2.5 Pro Advanced for free
- GitHub Pages documentation — Mitch asked about it; Brandon referenced it for deploying static sites via `[username].github.io`

## decisions

- Brandon Hancock will transition to full-time content creation starting next week, targeting 2–3 YouTube videos per week on real-world AI agentic applications (AWS Bedrock, GCP Gemini, etc.)
- Brandon will run weekly polls asking the community what content they want to see next
- Paul Miller will connect with Aaron for a follow-up call on graph RAG / Neo4j once both are ready
- Juan Torres will provide post-presentation instructions (slide or post) on how attendees can create their own API keys to run the agentic system independently
- Juan Torres will prepare a hard-coded demo response as a backup in case the live API call fails during the presentation
- Richard will build a multi-voice audiobook pipeline using OpenAI's new TTS models and FFMPEG to stitch character audio clips together
- Richard will move forward with his NVIDIA Project Digits reservation and purchase when it becomes available
- Bastian Venegas will keep Brandon posted on the law firm deal and potential onboarding
- Tom Welsh will share his M&A presentation with Brandon for review/feedback before delivering it in ~1.5 weeks
- Asako will try OpenAI's new multilingual TTS models as an alternative to ElevenLabs for Japanese-language podcast generation
- Brandon will dedicate focused time to exploring AWS Bedrock and GCP tools and share findings with the group