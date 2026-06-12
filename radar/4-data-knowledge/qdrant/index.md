---
name: Qdrant
layer: 4-data-knowledge
ring: adopt
tags: [vector-db, embeddings, semantic-search, sovereign]
champions: []
since: 2026-06
ring_history:
  - { ring: adopt, date: 2026-06, reason: "Initial radar import — preferred vector DB for sovereign setups" }
articles:
  - { title: "Vektordatenbanken Vergleich: 8 Lösungen für Unternehmen [2026]", url: "https://pexon-consulting.de/blog/vektordatenbanken-vergleich-unternehmen/", date: 2026-04 }
---

## What is it?

Open-source vector database for embeddings and semantic search, self-hostable on Kubernetes with strong filtering and hybrid search support.

## Why this ring?

Our preferred vector DB, especially for sovereign setups where managed services are excluded.

## When to use it — and when not?

- **Use** as the default for production RAG retrieval, particularly self-hosted/sovereign.
- **Don't** spin it up when the client already runs Postgres and the corpus is small (→ pgvector) or for quick prototypes (→ qmd).

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://qdrant.tech/
