## general

This coaching call brought together roughly a dozen participants working on diverse technical and business projects, facilitated by Brandon Hancock. The session followed a round-robin format where each member gave updates and received feedback from the group. Topics ranged from algorithmic routing problems and AI agent memory architectures to LinkedIn content strategy, data visualization, audiobook voice synthesis, and RAG (Retrieval-Augmented Generation) implementations.

Key presenters included Tom Welsh (vehicle routing problem for a rail IT project), Michal Simko (WhatsApp-based conflict resolution AI with persistent memory), Paul Miller (deep research tool comparison and LinkedIn thought leadership strategy), Juan Torres (NYC public data web application), Richard (multi-voice audiobook reader), Maksym Liamin (automotive chatbot for Nissan), Andrew Nanton (document processing evals), and Bastian Venegas (advanced RAG pipeline with graph search and query rewriting).

Brandon also shared his own updates, noting that the Authority Accelerator program's first week had concluded and that he planned to resume content production, including a comparison video on app-building platforms (Bolt, V0, Lovable, Replit) and a deep-dive Lovable + Postgres masterclass.

The call had a collaborative, peer-learning tone, with participants frequently building on each other's suggestions and Bastian in particular providing detailed technical depth on several topics.

---

## insights

- **Start with the simplest architecture that works**: For Michal's conflict-resolution AI, Brandon argued that a single messages table with user ID, conversation ID, and timestamps — passed directly into a large-context LLM — is a structurally sound V1 before reaching for vector databases or graph stores.
- **Large context windows reduce early architectural complexity**: Models like Gemini 2.0 or the new Meta model have context windows large enough that hundreds of conversational messages can be passed directly, eliminating the need for sophisticated retrieval at the prototype stage.
- **Index on user ID for multi-user message tables**: When scaling a messages table to multiple users, indexing on user ID with descending timestamp ordering is the critical performance step.
- **Timestamps in conversation history matter for AI context**: Passing timestamps alongside message history helps the LLM understand that parties may have moved past earlier issues, improving response relevance.
- **Safeguards are essential in sensitive AI applications**: For a divorce/conflict-resolution bot, explicit prompt-level guardrails must prevent the AI from revealing one party's private messages to the other.
- **Strong nodes (clustering) can reduce routing problem complexity**: For Tom's 49-station routing problem, grouping geographically close stations into clusters with defined entry/exit points reduces the effective node count from 49 to ~10, making the problem tractable.
- **Backtracking alone doesn't scale for large routing problems**: Bastian noted that naive backtracking has factorial time complexity, making it impractical for large node counts without additional heuristics.
- **Pre-processing documents to structured JSON before vectorizing is a valid RAG strategy**: Maksym's team manually parses PDFs to JSON, then splits data across a vector database (car specs), a relational SQL database (financing), and a key-value store (images with metadata labels) — each queried by different tools.
- **Multi-database RAG with specialized stores per data type outperforms a single vector store**: Routing queries to the right store (vector, SQL, or key-value) based on query type improves both accuracy and speed.
- **Query rewriting strategies (HyDE, decompose, step-back, paraphrase) significantly improve RAG retrieval**: Bastian demonstrated that rewriting a query before similarity search helps match the format of stored chunks, especially when user queries don't naturally resemble the corpus language.
- **For LinkedIn growth, the "comment [keyword] and I'll DM it" format reliably drives engagement**: Brandon noted this consistently generates large comment volumes and natural follow-up conversations.
- **Start content manually before automating**: Brandon advised Paul to manually emulate successful LinkedIn posts before building AI automation around them, since AI quality depends on the quality of instructions given.
- **Eleven Labs voice IDs are accessible via API**: Every voice in the Eleven Labs dashboard — including custom/cloned voices — has a unique voice ID that can be passed directly to the API, enabling full programmatic control.
- **OpenAI's structured output (Pydantic models) can enforce character/text/emotion arrays for TTS pipelines**: Returning a structured array of `{character, text, emotion}` objects from the LLM simplifies downstream voice assignment logic.
- **Luck and network effects play an underappreciated role in career outcomes** (Michal, referencing *The Drunkard's Walk*): Michal's Oracle job came through an organic lunch meeting, not a formal application, reinforcing the value of in-person networking and LinkedIn visibility.

---

## qa

**Q (Brandon):** For Michal's conflict-resolution WhatsApp bot, do you really need graph databases or vector stores at V1?
**A (Brandon):** No. A single messages table with user ID, conversation ID, and timestamps, passed entirely into a large-context LLM like Gemini 2.0, is sufficient for V1. The context window is large enough that you won't hit limits for a realistic number of messages between two people.

**Q (Michal):** How do you handle short-term vs. long-term memory in your bot, Maksym?
**A (Maksym):** We use Cloudflare Durable Objects as a fast cache layer for short-term memory (last 15 messages). When something important needs to be retained long-term, we write it to a separate Supabase table. We keep the full conversation history in a relational SQL table with good indexes rather than a vector database.

**Q (Michal):** Do you summarize old messages into vectors once they're cut off from the short-term window?
**A (Maksym):** No, not yet. We store full messages in the relational database. Moving to vectors is a potential next step but hasn't been necessary so far.

**Q (Brandon):** For the audiobook reader, how do you currently identify which character is speaking?
**A (Richard):** I use a JSON config file that maps character names to voice IDs. If no name is present, the narrator reads it. If a name like "John said" appears, it looks up John's assigned voice in the config.

**Q (Richard):** Is there a way to add emotional sentiment/inflection to voices via the Eleven Labs API?
**A (Bastian):** Yes — every voice in your Eleven Labs dashboard has a voice ID, including custom or cloned voices. Pass that voice ID to the API call and use streaming so output starts immediately. The API is fully flexible for any voice you've created.

**Q (Brandon):** For the audiobook project, could you create separate voice profiles per emotion per character (e.g., "John angry," "John happy") and map them in a dictionary?
**A (Richard/Brandon):** That's a viable approach — create five emotional variants per character voice in Eleven Labs, each with its own voice ID, and map `{character + emotion}` to the correct voice ID in your code.

**Q (Brandon):** What did Maksym's team ultimately use for parsing car spec PDFs?
**A (Maksym):** Primarily LLM-based parsing with manual correction. They also tried Azure Document Intelligence (standard model) but found it insufficient; they're about to test the Azure Document Intelligence layout model. Manual correction remains the baseline because document updates are infrequent (roughly every three months).

**Q (Brandon):** Why use HyDE (Hypothetical Document Embeddings) in a RAG pipeline?
**A (Bastian):** User queries are phrased conversationally and often don't match the language structure of stored corpus chunks. HyDE generates a hypothetical answer the LLM thinks would exist in the corpus, then uses that to find better-matching chunks via similarity search — improving retrieval even when the original query would return nothing.

---

## tools

- **Google OR Tools** — Tom is using it to prototype distance matrix calculations for the 49-station routing problem.
- **Google Distance Matrix API** — Referenced by Tom for getting real-world travel distances between rail stations.
- **Cloudflare Durable Objects** — Maksym's team uses it as a fast key-value cache for short-term bot conversation memory.
- **Supabase** — Used by Maksym as the persistent relational database for long-term conversation storage.
- **Neo4j** — Used by Bastian for the graph component of his advanced RAG pipeline; also mentioned by Michal as something he was researching for memory storage.
- **CrewAI** — Mentioned by Michal as the multi-agent framework context he was working within.
- **LangGraph** — Mentioned by Michal as something he had been reading about for agent memory.
- **OpenAI Agents SDK** — Richard suggested it for routing queries to specialized agents via handoffs in Michal's conflict-resolution system.
- **Gemini 2.0** — Recommended by Brandon as a large-context, cost-effective model for Michal's use case; also used by Paul to rate deep research outputs.
- **OpenAI o3 Mini** — Used by Paul in his deep research tool comparison.
- **Perplexity** — One of three deep research tools Paul compared; noted as the earliest to differentiate deep vs. quick research modes.
- **NotebookLM** — Paul aggregated all three deep research outputs into NotebookLM to create a unified queryable view.
- **Eleven Labs** — Discussed extensively for Richard's audiobook voice synthesis project; noted for voice ID-based API access and streaming support.
- **OpenAI TTS / OpenAI FM** — Used by Richard for multi-voice audiobook generation; Sharif highlighted its voice annotation/intonation capabilities.
- **OpenAI Structured Outputs (Pydantic)** — Brandon recommended it for enforcing `{character, text, emotion}` array responses in Richard's audiobook pipeline.
- **AWS RDS (PostgreSQL)** — Juan is using it to store ~600,000 NYC public data points for his web application.
- **Manus** — Brandon suggested Juan experiment with it for AI-assisted data analysis and visualization of his dataset.
- **Azure Document Intelligence** — Maksym's team tested the standard model for PDF parsing; planning to test the layout model next.
- **FastAPI** — Used by Bastian as the backend for his RAG pipeline demo.
- **Lovable** — Brandon announced an upcoming comparison video and deep-dive masterclass on using Lovable for full-stack app generation.
- **Bolt** — Mentioned alongside V0 and Lovable as an app-building platform to be compared in Brandon's upcoming video.
- **V0** — Mentioned alongside Bolt and Lovable in the upcoming platform comparison video.
- **Replit** — Bastian suggested adding it to Brandon's platform comparison video.
- **Screen Studio** — Brandon recommended it to Paul for recording LinkedIn demo videos.
- **AgentOps** — Brandon mentioned meeting with someone who runs AgentOps; described as doing impressive work in the agent monitoring space.
- **Excalidraw** — Tom mentioned using it for diagramming/brainstorming the routing problem.

---

## links

- **OpenAI Structured Outputs documentation** — Brandon shared this in chat to help Richard enforce typed response formats for his audiobook script parser.
- **OpenAI FM / voice playground demo** — Sharif referenced this as the demo showcasing advanced intonation/sentiment control for TTS; noted as likely available via API.
- **Manus (manus.im)** — Brandon pulled up the site during the call and shared it with Juan as a tool for AI-powered data analysis.
- **Adam Silverman on LinkedIn** — Brandon recommended his profile to Paul as an example of strong thought leadership content in the AI agent space.
- **"The Drunkard's Walk" (book by Leonard Mlodinow)** — Mentioned by Michal as a book about randomness and luck's role in life outcomes; he recommended it to the group.
- **Clement's YouTube video on airport/routing problem** — Brandon referenced a video by a channel called "Clement" featuring a high schooler solving a routing/graph problem in 57 minutes using strong node clustering; promised to find and send the link to Tom.
- **LightRAG** — Andrew mentioned Bastian had posted about it in the school community page; Andrew was reviewing it to stay current.

---

## decisions

- **Tom Welsh** will implement a distance matrix using Google OR Tools and share results with the group once working.
- **Brandon Hancock** will find and send Tom the Clement YouTube video on solving routing problems with strong node clustering.
- **Michal Simko** will start with a simple messages table (V1) rather than graph or vector databases for his conflict-resolution bot.
- **Michal Simko** will explore multi-agent routing using the OpenAI Agents SDK (as suggested by Richard) for a future version of the conflict-resolution system.
- **Brandon Hancock** will send Paul screenshots/examples of the newsletter format he referenced (category newsletter creator) tomorrow.
- **Paul Miller** will publish LinkedIn videos using Screen Studio, targeting four videos over the next month, with Brandon offering to review results.
- **Paul Miller** will explore the "comment [keyword] and I'll DM it" LinkedIn engagement strategy rather than routing followers to Medium.
- **Brandon Hancock** will send Paul examples of the newsletter format he referenced for thought leadership content.
- **Juan Torres** will sign up for and experiment with Manus to test AI-assisted data analysis on his NYC dataset.
- **Juan Torres** will write articles/content framed around how viewers can replicate his workflow, rather than just documenting what he built.
- **Richard** will investigate Eleven Labs voice IDs via API and explore creating multiple emotional voice variants per character for his audiobook reader.
- **Richard** will review the OpenAI Structured Outputs documentation Brandon shared to enforce typed script parsing responses.
- **Maksym Liamin** will test the Azure Document Intelligence layout model for PDF parsing as a potential improvement over manual correction.
- **Maksym Liamin and Andrew Nanton** will schedule a separate call with Brandon to discuss eval strategies for their document processing project.
- **Bastian Venegas** will create a video breaking down the different RAG query rewriting strategies (HyDE, decompose, step-back, paraphrase) with representative examples, targeting it as a first video for his channel.
- **Brandon Hancock** will publish a platform comparison video (Bolt vs. V0 vs. Lovable vs. Replit) and follow it with a deep-dive Lovable + Postgres masterclass the following week.