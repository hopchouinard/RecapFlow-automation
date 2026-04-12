---
session_date: "2025-01-15"
session_title: "RAG Architectures Deep Dive"
content_tier: "historical"
speakers: ["Patrick Chouinard", "Alice Chen", "Bob Martinez", "Carol Singh"]
chunk_count: 3
---

## Session: RAG Architectures Deep Dive | Date: 2025-01-15

### Chunk 1 of 3

[00:05:12] Patrick Chouinard: Today we're diving into RAG architectures. I've been experimenting with three different approaches over the past month and want to share what I found. The first approach uses LangChain with FAISS as the vector store. It's the fastest to prototype but has some limitations at scale.

[00:06:45] Alice Chen: I've been using the same LangChain plus FAISS combo. One thing I noticed is that for collections under 100,000 documents, FAISS performs really well. The main bottleneck isn't retrieval speed — it's the chunking strategy. I switched from fixed-size chunks to semantic chunking and saw a 40% improvement in retrieval relevance.

[00:08:30] Bob Martinez: What embedding model are you using with that, Alice? I tried OpenAI's text-embedding-3-large and nomic-embed-text. The nomic model is surprisingly good for a local model, and it's free.

[00:09:15] Alice Chen: I'm using nomic-embed-text through Ollama. The quality is close enough to OpenAI's offering that the cost savings make it a no-brainer for development. I only switch to text-embedding-3-large for production deployments where clients need the absolute best retrieval quality.

---

### Chunk 2 of 3

[00:15:22] Carol Singh: I want to share something different. I've been building a RAG system for legal documents, and the standard chunking approaches don't work well. Legal text has very specific structural requirements — you can't split a clause across chunks or you lose the legal meaning.

[00:17:01] Patrick Chouinard: That's a great point about domain-specific chunking. What did you end up doing?

[00:17:45] Carol Singh: I built a custom chunker that respects section boundaries in the legal documents. It uses the heading hierarchy — chapters, sections, subsections — as natural chunk boundaries. Each chunk also includes a breadcrumb trail showing where it sits in the document structure. The retrieval quality improved dramatically, about 65% better relevance scores.

[00:19:30] Bob Martinez: That breadcrumb idea is clever. I wonder if we could apply something similar to our call transcripts — using speaker transitions as natural boundaries instead of arbitrary token counts.

[00:20:15] Patrick Chouinard: That's exactly what I've been thinking about. Speaker-aware chunking for conversational content. Never split mid-speaker-turn, prefer breaking at topic transitions. We should prototype this.

---

### Chunk 3 of 3

[00:35:00] Patrick Chouinard: Let me summarize the key tools and recommendations from today. For vector stores: FAISS for prototyping, Pinecone or Weaviate for production scale. For embedding models: nomic-embed-text via Ollama for local development, text-embedding-3-large for production. For frameworks: LangChain is the most mature, but LlamaIndex has better document parsing.

[00:36:45] Alice Chen: One more tool to mention — I've been using Ragas for evaluating RAG pipeline quality. It gives you metrics like faithfulness, relevance, and context precision. Really helpful for comparing different chunking strategies objectively.

[00:37:30] Carol Singh: And for anyone working with legal or structured documents, I recommend looking at Unstructured.io. Their document parser handles PDFs, DOCX, and HTML with layout awareness. It's open source and works well as a pre-processing step before chunking.

[00:38:15] Bob Martinez: Great session everyone. My action item is to test speaker-aware chunking on a few of our past transcripts. I'll share results next week.

[00:38:45] Patrick Chouinard: Perfect. Next week we'll review Bob's chunking experiments and also look at hybrid search — combining BM25 keyword search with vector similarity. See everyone Tuesday.
