---
name: LlamaIndex
layer: 4-data-knowledge
ring: assess
tags: [rag, retrieval, ingestion, multimodal]
champions: []
since: 2026-06
ring_history:
  - { ring: assess, date: 2026-06, reason: "Added from blog coverage — two posts in May 2026, no radar entry yet" }
articles:
  - { title: "Private RAG mit LlamaIndex: On-Premise ohne Cloud-Lock-in", url: "https://pexon-consulting.de/blog/private-rag-llamaindex-on-premise/", date: 2026-05 }
  - { title: "Multimodale RAG mit LlamaIndex: ISO-Normen & CAD durchsuchbar", url: "https://pexon-consulting.de/blog/multimodale-rag-llamaindex-iso-normen-cad/", date: 2026-05 }
  - { title: "Standard RAG Grenzen: Warum PDF-Chat bei DIN-Normen scheitert", url: "https://pexon-consulting.de/blog/standard-rag-grenzen-technische-dokumente/", date: 2026-04 }
---

## What is it?

Data framework for LLM applications — ingestion, indexing and retrieval abstractions over documents and enterprise sources, including multimodal retrieval.

## Why this ring?

We've used it in content for private/on-premise RAG and multimodal retrieval (ISO norms, CAD); promising for retrieval-heavy builds, but our production RAG pipelines are currently hand-rolled on vector DBs — Assess until a project commits.

## When to use it — and when not?

- **Use** in PoCs with complex ingestion/retrieval needs (multimodal, many source types) where its abstractions save real time.
- **Don't** add the framework layer for a simple chunk-embed-search pipeline.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://www.llamaindex.ai/
