## general

This was an informal one-on-one coaching/peer check-in call between Juan Torres and Jake Maymar. The session covered Juan's ongoing data science and AI projects, including a banking concentration research project he is preparing to present at an event in San Diego, and a video/GitHub repo he has been working on but not yet published. Juan mentioned incorporating feedback from a third party named Brandon before republishing the video.

Jake walked Juan through his own assessment tool project, which tracks relational communication skills over time using periodic self-assessments, historical scoring, forecasting, and a RAG-based recommendation system. The conversation pivoted into a fairly detailed technical discussion about RAG systems, vector databases, hallucination mitigation, model drift, and the costs of re-encoding vector databases. Web scraping methods for data collection were also discussed.

The latter part of the call touched on Juan's career goals — seeking contract work in data engineering, data science, and AI development — and the broader market context for those skills. Juan's banking concentration project was noted as having received recognition from the Plotly/Dash community, appearing in their curated showcase. Jake shared a YouTube resource from a data science creator known as "Underfitted" (Santiago) covering MCP.

## insights

- Early critical feedback (like Brandon's annotations on Juan's video) is far more valuable than discovering flaws after significant time investment or during funding/client pitches.
- RAG alone (vanilla RAG) does not reliably prevent hallucinations; a re-ranker, a judge layer, and extensive prompting are needed alongside both a vector database and a traditional database to verify content.
- Hallucinations in LLM systems stem from three compounding sources: prompt drift, model drift, and system drift — all of which can change independently and make systems brittle over time.
- Re-encoding a vector database is necessary when substantial new data is added, because appended chunks lack relational context to the existing index — making dynamic data sources expensive and fragile for RAG.
- Garbage in, garbage out applies directly to RAG: noisy scraped data (ads, formatting artifacts) gets encoded and causes retrieval confusion; clean data preparation is essential before vectorization.
- Data engineering remains a critical and underappreciated foundation for AI systems — agent systems and models cannot produce high-quality analysis without well-engineered data pipelines feeding them.
- Using cheaper, faster models like GPT-4o mini introduces model drift risk because the model is updated by the provider and behavior changes without the developer's control.
- Synthetic data generation paired with hallucination-inducing test cases is the standard method for evaluating and tuning RAG systems.

## qa

**Q (Juan):** Are you using NLP in order to assess the communication style of people?
**A (Jake):** Not exactly — the assessment is score-based, using a series of questions answered by participants. That data feeds historical tracking, forecasting, and a RAG database that generates personalized activities to help users improve their scores.

**Q (Juan):** What is the difference between a RAG database and a vector database?
**A (Jake):** A vector database alone will produce hallucinations via cosine similarity matches that are close but not exact. RAG adds retrieval-augmented generation on top, and when you layer in a re-ranker, a judge, and verification against a traditional database alongside the vector store, you significantly reduce hallucinations. RAG is really a term that has evolved to encompass all these mitigation layers.

**Q (Juan):** How do you verify the answers your RAG system produces?
**A (Jake):** The best method is evaluations using synthetic data — you generate expected responses and also deliberately craft hallucination-inducing questions, then tune the system to minimize those hallucinations. It's very difficult to eliminate them entirely due to prompt drift, model drift, and system drift.

**Q (Juan):** Are you using AI to automate the web scraping process?
**A (Jake):** Yes — tools like Crawl4AI are used. Once content is converted to Markdown, you identify CSS selectors to extract the relevant data. Brandon had a tutorial on this approach as well.

## tools

- **RAG (Retrieval Augmented Generation)** — Core architecture Jake uses for his pharmaceutical drug interaction and assessment recommendation systems.
- **GPT-4o mini** — Jake's preferred LLM for cost and speed; noted as subject to model drift from provider updates.
- **Claude 3.7** — Mentioned as an expensive alternative model Jake considered for evals.
- **Neo4j** — Mentioned as a graph database approach for handling relational context between vector embeddings.
- **Crawl4AI** — Web scraping tool Jake uses to collect pharmaceutical data and convert pages to Markdown.
- **Plotly Dash** — Python web framework Juan uses for his banking concentration data application; project featured in Plotly's showcase.
- **MCP (Model Context Protocol)** — Referenced in context of a YouTube video by Santiago/Underfitted showing how to spin up and use models with MCP.

## links

- **Plotly/Dash Awesome showcase** — Juan's banking concentration project was featured here; URL not explicitly shared but referenced as visible on the Plotly community site.
- **Underfitted YouTube channel (Santiago)** — Jake shared a YouTube link demonstrating MCP usage for data science; channel formerly known as "Santiago," now "Underfitted."

## decisions

- Juan Torres will revise and re-record his data science video incorporating Brandon's feedback before publishing it.
- Juan Torres will make a live stream link available for his San Diego banking concentration presentation so remote attendees can join.
- Jake Maymar and Juan Torres agreed to continue the conversation on Thursday.