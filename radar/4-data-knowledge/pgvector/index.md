---
name: Postgres pgvector
layer: 4-data-knowledge
ring: adopt
tags: [vector-db, postgres, embeddings]
champions: []
since: 2026-06
ring_history:
  - { ring: adopt, date: 2026-06, reason: "Initial radar import — Pexon default per stack documentation" }
---

## What is it?

Vector similarity search as a Postgres extension — embeddings live next to relational data, no extra database to operate.

## Why this ring?

The pragmatic default when the client already runs Postgres: one less system, transactional consistency between documents and embeddings.

## When to use it — and when not?

- **Use** for small-to-medium corpora in Postgres-centric stacks.
- **Don't** push it past its limits — very large corpora or heavy hybrid-search needs go to Qdrant/Weaviate.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://github.com/pgvector/pgvector
