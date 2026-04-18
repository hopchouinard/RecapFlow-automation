# Session notes — 2026-03-10

The main thread this week was a deep comparison of agent orchestration frameworks, led by Alex Rojas sharing his three months of production experience with LangGraph. Alex made a strong case for state-machine models over role-based approaches like CrewAI, specifically around debuggability — when things go wrong in production, being able to trace state transitions is worth more than the demo-friendly ergonomics.

Sam pushed on the predictability claim and got a concrete answer: explicit state transitions mean you can replay the history. This felt like a genuine insight the group landed on together rather than just Alex's opinion.

The second thread picked up on embedding models, with Sam and Shakur weighing local (nomic-embed-text via Ollama) against cloud (text-embedding-3-large). Sam's position: the quality gap doesn't justify the per-token cost for conversational recall. Shakur's counter: it depends on query precision needs. Both positions had merit and the group didn't force a resolution, which felt right.
