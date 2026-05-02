## general

This coaching call brought together Brandon Hancock (host/coach) and several participants — Tom Welsh, Christopher Marin, Delvis, and Richard Collier — for a weekly group session. The session opened with Brandon and Tom discussing AI coding tools, model selection in Cursor, and the upcoming AI Authority Accelerator course Brandon is preparing to launch. Brandon shared a LinkedIn lead-generation strategy (posting AI templates and asking people to comment for access) that had generated significant engagement and booked calls for a client named Alexandra.

The bulk of the session was spent going around the room. Christopher Marin demonstrated a multi-LLM "Content Fusion" app he built that sends prompts to multiple models simultaneously and synthesizes their outputs, as well as a "Content Remix" feature for generating content variations. Tom Welsh shared that he landed a potential AI presentation opportunity at a mergers and acquisitions company after a chance conversation on a train. Delvis discussed his transition from a digital marketing agency into AI automation consulting, targeting marketing agencies as his niche. Richard Collier showcased a B-roll video generation agent integrated into Slack that pulls content from his Shopify store (blog posts and products), generates scripts, voiceovers via ElevenLabs, and video clips via Luma Labs, then stitches them together with FFmpeg.

Brandon provided coaching feedback throughout: advising Tom and Christopher on content strategy and personal branding angles, encouraging Delvis to prioritize getting clients over building a website, and walking Richard through next deployment steps (Neon for database, blob storage, Docker, Railway). The session closed with Brandon previewing his AI Authority Accelerator email course launching March 4th and recommending Steven Pressfield's *The War of Art*.

## insights

- **LinkedIn "comment for access" posts create exponential engagement loops**: LinkedIn's algorithm rewards high-engagement posts, and giving away a free template in exchange for a comment drives comments rapidly — roughly 10% of follower count in comments is a rough benchmark. One post generated four booked calls within 24 hours for a user with ~2,500 connections.
- **The content flywheel compounds**: Making a YouTube video produces a template as a byproduct; that template becomes a LinkedIn lead magnet; the LinkedIn post drives inbound leads — all from one piece of work.
- **Authority statement is a prerequisite for raw/lecture-style content**: You can only get away with unpolished, high-information-density videos (à la Andrej Karpathy) if your name or credentials already carry weight. Newcomers need an explicit authority statement and a consistent niche.
- **Niche content strategy for Christopher**: AI + marketing + coding/automation is a differentiated angle — documenting how he automates marketing tasks at his company would attract both marketing CEOs looking to hire and junior marketers wanting to learn.
- **Tom's unfair advantage**: 30+ years of infrastructure/cybersecurity experience combined with AI coding is an underserved content niche; framing content around "how I land security clients and do the work faster with AI" would be distinctive.
- **Proof of concept before polish**: Brandon repeatedly advised against building websites, dashboards, or branding before getting paying customers. The goal is to reduce friction between the builder and their first clients.
- **Sell the outcome, not the technology**: Cold outreach and lead generation services are easier to sell because they are directly tied to clients making money — people pay more when the problem solved is revenue-related.
- **Use yourself as the case study**: If you automate your own content pipeline and it works, that becomes the most compelling sales argument — it eliminates the "if it works so well, why don't you do it?" objection.
- **Command+Enter in Cursor** grabs all relevant files across the codebase (not just the ones explicitly referenced), leveraging the model's large context window — useful for fixing bugs that span multiple files.
- **Slack as an agent orchestration layer**: Using Slack as the interface for a multi-agent system lets agents share a message history natively, reducing the need to handle inter-agent communication inside code.
- **Deployment order for Richard's app**: Move database to Neon → add blob storage (Dropbox or S3) for generated video files → containerize with Docker → deploy to Railway.

## qa

**Q (Tom Welsh):** I'm getting five to seven fix iterations in Cursor instead of one-shot fixes — is there a better approach or model?

**A (Brandon Hancock):** Use Command+Enter instead of just Enter — it searches your entire codebase for relevant files rather than only the ones you explicitly reference. Claude 3.5 with its 200,000-token context window handles this well. Also consider trying O3 Mini, which several people in the community have switched to exclusively.

**Q (Delvis):** Does follower count on LinkedIn matter for these posts to work, similar to YouTube?

**A (Brandon Hancock):** It matters to some degree, but the mechanism is engagement-driven — LinkedIn surfaces posts getting high engagement regardless of follower count. The rough ratio observed is about 10% of your follower count in comments. Christopher Marin added that at his previous company, a large existing follower base did accelerate newsletter sign-ups when LinkedIn newsletters launched.

**Q (Brandon Hancock):** Chris, did you use LiteLLM or LangChain to connect to all the different LLM providers in your app?

**A (Christopher Marin):** Started with OpenRouter (direct connection), then added direct Anthropic connection and an OpenAI Assistants integration. Crew AI uses LiteLLM under the hood. For the other providers, just straight API calls.

**Q (Christopher Marin):** Does Crew AI support OpenAI Assistants?

**A (Brandon Hancock):** Not as far as we know currently. LiteLLM is the recommended abstraction layer because it handles tool calling, structured responses, and provider-specific quirks — it also tells you which models support which capabilities, which prevents confusing errors when pushing models to their limits.

**Q (Christopher Marin):** What's the difference between AI Suite (Andrew Ng's library) and something like LiteLLM or small agents?

**A (Brandon Hancock):** AI Suite is newer and aims to simplify tool calling significantly — you can pass a plain function and it auto-generates the JSON schema, whereas LiteLLM requires you to build that schema manually. It's not fully there yet but is getting close. Haven't personally tested it deeply yet.

**Q (Richard Collier):** Does ngrok require the computer to stay on, and how does it work?

**A (Brandon Hancock):** Yes — ngrok is just port forwarding that lets internet servers (e.g., Slack sending webhooks) reach your local machine. The moment your computer turns off, nothing works. The solution is to deploy the application to a cloud host (e.g., Railway in a Docker container) so it runs 24/7 independently.

**Q (Richard Collier):** How do I prevent the image/video generation from producing inappropriate content (e.g., undressed figures)?

**A (Brandon Hancock):** Add a prompt review step before passing the prompt to Luma Labs or any image generator — have an LLM check the generated prompt for anything NSFW and sanitize it before it goes out. You don't need to review the image itself; reviewing the raw prompt is sufficient.

**Q (Delvis):** What's the difference between a regular personal brand and an AI personal brand?

**A (Brandon Hancock):** Two things: (1) the core subject you discuss must be AI plus two other topics (e.g., AI + marketing + software), and (2) you actively use AI in your own content creation and business operations, so you're both talking about AI and demonstrating it. This lets you ride the current demand wave, which makes growth significantly easier than a generic personal brand.

## tools

- **Cursor** — AI code editor; discussed for multi-file context handling and model selection (Claude 3.5, O3 Mini, DeepSeek)
- **Claude 3.5 (Sonnet)** — LLM used inside Cursor; noted for 200,000-token context window
- **O3 Mini** — OpenAI model; several community members switching to it exclusively for coding projects
- **DeepSeek** — LLM; mentioned as potentially better than Claude for some coding tasks in Cursor
- **LiteLLM** — LLM abstraction library; discussed for tool calling, structured responses, and multi-provider support
- **AI Suite (Andrew Ng)** — Open-source library; simplifies tool calling by auto-generating JSON schemas from plain functions
- **OpenRouter** — Multi-LLM API gateway; used by Christopher as the starting provider for his app
- **Crew AI** — Agent framework; uses LiteLLM under the hood; discussed re: OpenAI Assistants support
- **LangChain** — Agent/LLM framework; mentioned as an alternative to LiteLLM
- **ElevenLabs** — Text-to-speech; used by Richard for voiceover generation in his B-roll agent
- **Luma Labs** — AI video generation; used by Richard to generate B-roll clips from prompts
- **FFmpeg** — Video processing library; used by Richard to stitch video clips together
- **Slack** — Used by Richard as the interface and orchestration layer for his multi-agent content system
- **Shopify** — E-commerce platform; Richard's app pulls blog posts and products from his Shopify store via API
- **Make (formerly Integromat)** — Automation platform; mentioned by Brandon as part of a marketing automation stack
- **Go High Level** — CRM/marketing platform; mentioned alongside Make for marketing agency automation
- **Airtable** — Database/project management; mentioned as part of a marketing automation stack
- **Instantly** — Cold email platform; Brandon recommended their YouTube content for learning cold outreach strategy
- **Neon (neon.tech)** — Serverless Postgres database; recommended by Brandon for Richard to replace local SQLite
- **Railway** — Cloud deployment platform; recommended for deploying Richard's Slack bot
- **Docker** — Containerization; recommended as the next step for deploying Richard's application
- **Dropbox** — File storage; Richard already uses it for Flux-generated images; suggested as a simple blob store for generated videos
- **Amazon S3** — Object storage; suggested as a more developer-friendly alternative to Dropbox for video storage
- **Google VO2 (via fal.com)** — AI video generation; Christopher mentioned it as a high-quality alternative to Sora, available through fal.com
- **Devin** — AI coding agent; mentioned by Brandon as an example of Slack-native agent interaction
- **LinkedIn** — Social platform; central to the lead generation strategy Brandon demonstrated
- **Monday.com** — Work OS; Christopher mentioned his Content Remix app runs on their Monday instance

## links

- **fal.com** — Platform to access Google VO2 video generation model (mentioned by Christopher Marin)
- **neon.tech** — Free serverless Postgres database recommended for Richard's deployment
- **Instantly (YouTube channel)** — Brandon recommended their YouTube videos on cold email outreach strategy (no direct URL given)
- **AI Authority Accelerator landing page** — Brandon dropped a link in chat for participants to review his upcoming course (URL not captured in transcript)
- **Andrej Karpathy LLM explainer video** — Christopher referenced a recent video on how LLMs are built from the ground up (link to be shared by Christopher in chat)
- ***The War of Art* by Steven Pressfield** — Book recommended by Brandon to Delvis about overcoming resistance/procrastination in creative/business work

## decisions

- **Brandon** will send the AI Authority Accelerator email course outline to Tom Welsh and Delvis.
- **Brandon** will begin sending announcement emails for the AI Authority Accelerator starting March 4th.
- **Brandon** will send Richard a Dropbox link to the generated video from the session.
- **Richard Collier** will move his local SQLite database to Neon (neon.tech) as a first deployment step.
- **Richard Collier** will add blob storage (Dropbox or S3) for generated video files and surface a working URL in the Slack output.
- **Richard Collier** will containerize his application with Docker and deploy to Railway.
- **Richard Collier** will add a prompt review/NSFW filter step before sending prompts to Luma Labs.
- **Richard Collier** will investigate the content handler/adapter as the likely source of the script truncation bug.
- **Richard Collier** will prioritize getting 5–10 paying e-commerce clients using the Slack B-roll agent before building a full-stack application.
- **Christopher Marin** will share the Andrej Karpathy LLM video link in the group chat.
- **Christopher Marin** will investigate context window mitigation in his Content Fusion app.
- **Delvis** will target getting 2–3 free/low-cost pilot automation projects with existing clients to build social proof before formally launching.
- **Tom Welsh** will share more details with Brandon about his upcoming AI presentation to the mergers and acquisitions company once dates and scope are confirmed.
- **Brandon** will send Delvis the book *The War of Art* by Steven Pressfield.