---
name: Vespa
layer: 4-data-knowledge
ring: trial
tags: [search, vector-db, hybrid-search, on-prem]
champions: []
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Added from blog coverage — production knowledge base in the Rku IT project" }
references:
  - { client: "Rku IT", title: "Wissensdatenbank für die First-Level-Support-Automation (LLaMA + RAG)", url: "https://pexon-consulting.de/casestudie/rku-genai-und-llm/", public: true }
articles:
  - { title: "Vespa On-Premise: Installation und Performance für RAG", url: "https://pexon-consulting.de/blog/vespa-on-premise-installation-performance/", date: 2026-05 }
---

## What is it?

Open-source search and ranking engine (ex-Yahoo) — combines BM25, vectors and ML-ranking in one engine, built for large-scale, low-latency retrieval and fully self-hostable.

## Why this ring?

Ran as the knowledge base in the Rku IT support-automation project and we've documented the on-premise setup; heavier to operate than Qdrant, but stronger when ranking quality and scale dominate.

## When to use it — and when not?

- **Use** for demanding on-prem retrieval with hybrid search and custom ranking at scale.
- **Don't** pick it for standard RAG corpora where Qdrant/pgvector do the job with far less operational weight.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://vespa.ai/
