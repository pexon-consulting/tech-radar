---
name: LangChain (Chains)
layer: 5-orchestration
ring: hold
tags: [llm-framework, legacy-pattern]
champions: []
since: 2026-06
ring_history:
  - { ring: hold, date: 2026-06, reason: "Classic chain abstractions superseded — LangGraph for graphs, PydanticAI for validation-first, DSPy for optimized pipelines" }
---

## What is it?

The original LLM application framework — chains, retrievers and integrations that defined the early RAG era.

## Why this ring?

**Hold — for new builds use LangGraph (same ecosystem), PydanticAI or DSPy instead.** The classic chain abstractions hide control flow exactly where production systems need it explicit; our own posts argue this repeatedly ("RAG Pipelines mit DSPy statt LangChain", "PydanticAI vs LangChain"). The integration ecosystem stays useful — accessed via LangGraph, not via chains. We maintain existing LangChain code at clients; we don't start new projects on it.

## When to use it — and when not?

- **Use** only to maintain or migrate existing client codebases.
- **Don't** start new agent or RAG builds on classic chains.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://www.langchain.com/
