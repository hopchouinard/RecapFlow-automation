## tools

- LangGraph — Alex Rojas uses it for production agent deployments
- CrewAI — mentioned as an alternative to LangGraph
- nomic-embed-text — local embedding via Ollama
- text-embedding-3-large — cloud embedding alternative

## qa

**Q (Sam):** Can you say more about the predictability angle?
**A (Alex Rojas):** With LangGraph you explicitly define state transitions, making debugging easier than CrewAI's role-based approach.

## insights

- State-machine agent frameworks are easier to debug than role-based ones
- Local embeddings are sufficient for conversational recall; cloud wins on technical precision

## links

- https://langchain.com/docs/langgraph — LangGraph documentation
