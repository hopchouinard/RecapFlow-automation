=== SESSION ===
date: 2026-03-10
duration_estimate: ~90 min
main_themes: [agent frameworks, production deployment, model selection]
===

<!--SEGMENT
topic: agent orchestration tools
speakers: Alex Rojas, Sam
keywords: LangChain, LangGraph, CrewAI, agent orchestration, tool calling, state machines
summary: Alex and Sam compare LangChain, LangGraph, and CrewAI for production agent deployments. Alex argues for LangGraph's state-machine model over CrewAI's role-based approach.
-->

[00:02:15] Alex Rojas: So I've been running [tool:LangGraph] in production for about three months now, and the state-machine model is way more predictable than [tool:CrewAI].
<Q>[00:02:45] Sam: Can you say more about the predictability angle?</Q>
<A>[00:03:01] Alex Rojas: ▶ With LangGraph you explicitly define the state transitions, so when something breaks you can trace back through the state history. CrewAI's role-based thing is nice for demos but painful to debug.</A>
[00:03:40] Alex Rojas: [link:https://langchain.com/docs/langgraph] is the best reference I've found.

<!--SEGMENT
topic: embedding model tradeoffs
speakers: Sam, Shakur
keywords: nomic-embed-text, text-embedding-3-large, embedding, local inference, cost
summary: Sam and Shakur discuss choosing between local nomic-embed-text and OpenAI's text-embedding-3-large. They agree local is right for BYO-AI but cloud quality is still better.
-->

[00:15:20] Sam: For our use case, [tool:nomic-embed-text] via Ollama is plenty. The quality gap with [tool:text-embedding-3-large] isn't worth $0.13 per million tokens.
[00:15:55] Shakur: Depends on the retrieval pattern. For conversational recall, nomic is fine. For precise technical queries, the OpenAI model catches nuances we lose locally.
