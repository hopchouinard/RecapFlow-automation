## general

This was a weekly coaching/community call for a group of developers and builders using AI tools, organized by Brandon Hancock. The session ran round-robin style, with each participant sharing project updates, demos, and questions. Topics ranged from new tool discoveries (Gemini CLI, Cursor 2.0, Claude Code) to live project demos including a web scraper with visual element selection, a cybersecurity code-scanning platform, an in-person presentation tool, a wholesale plumbing supply quoting agent, and a real estate coaching agent. Brandon also shared updates on upcoming ShipKit content and Trigger.dev integration work.

Patrick Chouinard opened with a demo of a novel chat UI featuring a split-pane prompt editor with AI-powered tab autocomplete, and shared insights on using Gemini CLI as a parallel research agent. Tom Welsh demonstrated significant overnight progress on his web scraper, adding an augmented overlay UI for visual element selection backed by a Celery-based Python worker queue. Ty Wells showed two projects: a completed in-person presentation tool and a GitHub repository security scanner that checks against NIST/OWASP CVEs and runs in AWS Lambda. Alex presented a plumbing fixture schedule parsing agent built on Google ADK that uses Chunker for complex PDF table extraction.

The group also had an extended discussion about hiring practices in the AI era — whether to hire junior developers, seniors, or domain experts upskilled in AI — and debated how to measure developer productivity and AI impact. Brandon previewed upcoming content including a Playwright MCP server video, a Trigger.dev template, and a new LangChain/LangGraph masterclass video.

## insights

- **Patrick Chouinard:** Gemini CLI can run multiple simultaneous research queries in parallel (unlike deep research tools that go deep on one question), saving results to local files, then correlating them — effectively a parallel research swarm. Using a personal Gmail account gives 1,000 requests/day vs. ~100 on a Google Cloud enterprise account.
- **Patrick Chouinard:** Senior developers are more valuable in the AI era not because they code better, but because they have a larger "context window" — they can manage more agents simultaneously without losing track of the process. Junior developers can only safely manage one agent at a time.
- **Brandon:** Using Claude Code with Cursor's split-pane terminal layout (terminal on one side, file explorer on the other) replicates the Cursor IDE experience while using Claude Code's cheaper token pricing — a practical cost-saving workflow.
- **Brandon:** Claude Haiku 4.5 is twice as fast and roughly one-third the price of Sonnet/Opus for small-to-medium tasks, with no meaningful quality loss on those tasks.
- **Brandon:** When building agentic chart generation, save chart data to agent state rather than trying to parse it from message output. Display state diffs on the front end to trigger chart rendering — avoids messy markdown parsing.
- **Brandon:** For ADK deployments, Cloud Run is significantly more scalable and supports streaming better than Agent Engine; recommended path for anyone with production deadlines.
- **Brandon:** The Claude Code VS Code extension and the terminal-based Claude Code do not share conversation history — if you start in one, you must stay in that context. They are fully isolated.
- **Alex (AlexH):** Chunker (CHUNKR) outperformed Landing AI, Azure Document Intelligence, Reducto, and Xtend for maintaining table architecture (merged cells, column relationships) in complex PDF documents — critical for the plumbing fixture schedule use case.
- **Brandon:** Lines of code is a poor proxy for developer productivity. True impact is closer to: does the feature generate revenue, does it help customers achieve their goal faster, and how much are you consulted by others (Patrick's framing).
- **Garron:** Building a "canonical library" of ADK examples, video transcripts, and documentation — then feeding it into Cursor as context — dramatically reduced AI drift and allowed him to make more progress in three days than in three prior months.
- **Brandon:** Flexibility on tools is the name of the game right now; don't feel compelled to swap frameworks constantly, but be ready to adapt as the landscape shifts weekly.
- **Jake:** Cross-checking contracts across OpenAI, Gemini, and Claude simultaneously provides better coverage than relying on a single model for legal review.

## qa

**Q (Jake Maymar):** How does Gemini CLI's search capability relate to Claude Deep Research or OpenAI Deep Research?
**A (Patrick Chouinard):** Deep research goes hundreds of sources deep on a single question. Gemini CLI lets you run 20 different questions from 20 different points of view simultaneously, saving each result to a local file, then correlating them afterward. It's breadth across perspectives rather than depth on one topic.

**Q (Jake Maymar):** Can you hook Gemini CLI up to NotebookLM?
**A (Patrick Chouinard):** Yes, you can feed results back into NotebookLM. You can also ask it to look at videos directly since it's connected to Google's infrastructure.

**Q (Paul Miller):** With the current version of ShipKit, if I update and load it in, does it already have the hooks for Claude Code?
**A (Brandon):** Yes, it has the hooks, the commands, and everything. There's also a demo walkthrough video (the fifth one in the series) that shows how to use planning and call the commands properly.

**Q (Hemal Shah):** Is Google ADK still your favorite agent development framework?
**A (Brandon):** It's still great for local development and proof of concepts — the ADK editor makes it the easiest to learn. The two main pain points are: (1) no quick one-click deploy like AgentKit had, and (2) it's hard to integrate cleanly into a Next.js application. If they fix those two things it goes back to number one. For now, LangChain/LangGraph may become the new winner, especially if ADK doesn't improve deployment.

**Q (Hemal Shah):** Any recommendations for automated PR review tools?
**A (Brandon):** CodeRabbit is his personal favorite — it provides walkthrough summaries, sequence diagrams, and code snippets to fix identified issues. Alex also recommended Factory AI's Droids package from their GitHub, which has a free trial up to 20 million tokens and has received strong word-of-mouth. Patrick noted that Gemini also has a built-in PR review setup.

**Q (Hemal Shah):** How do you generate charts in an agentic UI?
**A (Brandon):** Have a specialist chart agent save its output to agent state (not to the message stream). On the front end, watch for state diffs — when the chart state updates, render it using a library like Chart.js. Avoid routing chart output through message markdown, as parsing it back out is messy and error-prone.

**Q (Adam):** Is the OpenAI Agent Builder GUI just a UI on top of the OpenAI Agent SDK? Can you export the Python and swap in a non-OpenAI model?
**A (Brandon):** Yes, it is a UI on top of OpenAI's agent framework, and there is an export button to see the underlying generated code. Alex confirmed in chat that the framework is model-agnostic, so swapping in a local or alternative model should be possible.

**Q (Jake Maymar):** Is Trigger.dev a fair replacement for Convex for real-time functionality?
**A (Brandon):** They solve somewhat different problems. Trigger.dev handles background job orchestration and has a subscribe/stream system for real-time updates that works from both the client and server side, without requiring you to expose Supabase credentials client-side (which creates RLS policy headaches). It has significantly more AI-oriented capabilities than competing platforms like Inngest. For real-time needs in a Next.js + Supabase stack, Trigger.dev is the recommended path.

**Q (Patrick Chouinard):** How does Chunker handle merged columns and rows in complex PDFs?
**A (Alex):** Chunker maintains table architecture — column relationships, merged cells, and text fidelity — better than any other tool Alex tested (Landing AI, Azure Document Intelligence, Reducto, Xtend). Landing AI preserved columnar structure but distorted the actual OCR text (manufacturer model numbers came out garbled), which broke the downstream quoting process. Chunker solved both problems.

## tools

- **Gemini CLI** — Used as a parallel web research agent; runs simultaneous queries, saves results to local files; 1,000 req/day on personal Gmail accounts
- **Claude Code** — Primary coding agent used by Brandon and others; discussed cost advantages over Cursor, terminal vs. VS Code extension isolation issue
- **Cursor** — IDE used by Tom Welsh and others; Cursor 2.0 released with a proprietary model and built-in browser for agentic self-checking
- **Cursor 2.0 (new release)** — New version with built-in browser for real-time app testing and a new proprietary code model
- **ShipKit** — Brandon's Next.js starter template; multiple members building products on top of it; has Claude Code hooks and commands built in
- **Playwright (MCP server)** — Brandon working on a YouTube video showing Playwright as an MCP server with Claude Code and Cursor for browser automation
- **Trigger.dev** — Background job and workflow orchestration platform; discussed for long-running tasks, video processing, and real-time subscribe/stream functionality
- **Celery** — Python task queue used in Tom Welsh's web scraper backend for scalable concurrent workers
- **Chunker (CHUNKR)** — PDF/document parsing SaaS; best-in-class for maintaining complex table architecture; used by Alex for plumbing fixture schedule extraction
- **Google ADK (Agent Development Kit)** — Agent framework used by Alex and Garron; recommended for local dev/POC; Cloud Run preferred over Agent Engine for deployment
- **CodeRabbit** — Automated PR review tool; provides summaries, sequence diagrams, and fix suggestions with code snippets
- **Factory AI / Droids** — Automated PR review package available on GitHub; free trial up to 20M tokens
- **Supabase** — Database platform; discussed in context of RLS policies and real-time subscriptions
- **AWS Lambda** — Used by Ty Wells to run his security scanning workloads
- **NotebookLM** — Mentioned as a downstream destination for Gemini CLI research output
- **LangChain / LangGraph** — Brandon previewing a new masterclass video; may become preferred agent framework if ADK deployment doesn't improve
- **Monaco Editor** — Patrick considering it for his prompt editor UI (open-source VS Code editor component)
- **TipTap** — Mentioned as an alternative rich text editor Patrick evaluated for his prompt editor
- **Chart.js** — Recommended for chart rendering in Next.js agentic UIs
- **Vercel** — Used by Tom Welsh for preview and production deployments of his scraper app
- **Claude Haiku 4.5** — Discussed as a cost-effective model for small/medium tasks; 2x faster, ~1/3 the price
- **Azure AI / Azure Agent SDK** — Sam evaluating Azure's agent SDK for work; found it feels like a high-level wrapper, less granular than LangGraph
- **GitHub Copilot** — Mentioned by Sam as the only AI tool some developers at his company have access to
- **OpenAI Agent Builder (AgentKit)** — GUI drag-and-drop agent builder; UI on top of OpenAI agent SDK; model-agnostic with Python export
- **Convex** — Real-time database platform a client requested; discussed as potentially replaceable with Trigger.dev + Supabase
- **Inngest** — Competing background job platform to Trigger.dev; fewer AI-specific capabilities
- **Moshe** — New event-driven background job framework; very young, limited framework support, not recommended yet
- **Landing AI** — Tested by Alex for PDF table extraction; good columnar structure but poor OCR fidelity on model numbers
- **Memory Bank** — Cursor/agent memory system; Garron got it working as part of his ADK canonical library setup
- **Linear** — Mentioned by Brandon for managing junior developer task queues

## links

- **Network Chuck video on Gemini CLI as a search agent** — Referenced by Patrick and Morgan; covers using Gemini CLI for browser-based research and stopping reliance on the browser UI
- **Anthropic published Claude Code system prompt** — Patrick shared a link in chat; noted the published version appears less detailed than what Ty extracted from a live session
- **Theo (T3) video on junior dev vs. senior dev in the AI era** — Brandon shared in chat; discusses why a "bad manager in AI" outperforms hiring four junior devs
- **ShipKit Claude Code demo walkthrough video (5th video in series)** — Brandon referenced and screen-shared; shows planning workflow and how to use Claude Code commands
- **Fathom recording from July 22nd** — Brandon pulled up to find Maxim's LiveKit discussion; shared link in chat for Morgan's reference on LiveKit latency workarounds
- **Factory AI / Droids GitHub repo** — Alex mentioned as source for the automated PR review package

## decisions

- **Brandon** will release the Trigger.dev ShipKit template before the accompanying video so members don't have to wait an extra week.
- **Brandon** will include Trigger.dev streaming/subscribe functionality in the upcoming Scribble-style audio processing project demo.
- **Brandon** will record a new LangChain/LangGraph masterclass video covering both frameworks (version 1 recently released).
- **Brandon** will publish a YouTube video on using Playwright as an MCP server with Claude Code and Cursor for browser automation.
- **Brandon** will try Cursor 2.0 the same evening as the call.
- **Patrick** will research Monaco vs. TipTap using Gemini CLI before committing to an editor for his prompt designer UI.
- **Alex** will deploy his ADK plumbing quoting agent to Cloud Run (rather than Agent Engine) per Brandon's recommendation.
- **Alex** will post in the ShipKit community about his project and co-founder search; Brandon offered to pin/amplify the post.
- **Brandon** offered to do a separate call with Alex to strategize on co-founder search and fundraising approach.
- **Garron** will demo a working prototype of his real estate coaching agent next week; Brandon committed to giving honest feedback and helping choose a path forward.
- **Ty** will follow up with a contact in another group who has used LiveKit to get advice on the latency issue Morgan is experiencing.
- **Morgan** will test Next.js 16 on his playground project and report back to the group.
- **Sam** will keep Brandon updated on his Azure Agent SDK evaluation.
- **Paul** will watch the ShipKit Claude Code demo walkthrough video (video 5) before switching from Cursor to Claude Code.