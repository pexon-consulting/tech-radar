---
name: LangGraph
layer: 5-orchestration
ring: adopt
tags: [agents, orchestration, langchain]
champions: []
since: 2026-06
ring_history:
  - { ring: adopt, date: 2026-06, reason: "Initial radar import — agentic framework default per stack documentation" }
articles:
  - { title: "Agentic RAG mit LangGraph: Warum naives RAG 2026 ausgedient hat", url: "https://pexon-consulting.de/blog/agentic-rag-langgraph-live-code-python/", date: 2026-06 }
---

## What is it?

Graph-based agent orchestration framework from the LangChain family: explicit state machines for multi-step agent workflows, with checkpointing and human-in-the-loop support.

## Why this ring?

Our default for production agent workflows where control flow must be explicit and debuggable rather than a free-running loop.

## When to use it — and when not?

- **Use** for multi-step agent pipelines with branching, retries and human approval gates.
- **Don't** use it for simple single-tool chains — plain SDK calls are easier to maintain.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://github.com/langchain-ai/langgraph
