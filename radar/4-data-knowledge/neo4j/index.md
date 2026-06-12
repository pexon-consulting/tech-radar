---
name: Neo4j (GraphRAG)
layer: 4-data-knowledge
ring: assess
tags: [graph-db, graphrag, knowledge-graph]
champions: []
since: 2026-06
ring_history:
  - { ring: assess, date: 2026-06, reason: "Radar expansion — evaluating GraphRAG for relationship-heavy corpora" }
certifications:
  - { name: "Neo4j Certified Professional", issuer: "Neo4j", holders: [] }
---

## What is it?

Graph database — in our context the backbone for GraphRAG: retrieval over entities and their relationships instead of flat chunks.

## Why this ring?

GraphRAG promises better answers on relationship-heavy corpora (org structures, contracts, supply chains); we are validating whether the extraction cost is worth it in practice.

## When to use it — and when not?

- **Use** in PoCs where multi-hop questions ("who supplies whom via what contract?") fail with vector RAG.
- **Don't** default to it — plain vector RAG is cheaper to build and operate.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://neo4j.com/
