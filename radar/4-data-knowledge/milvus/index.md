---
name: Milvus
layer: 4-data-knowledge
ring: assess
tags: [vector-db, embeddings, self-hosted]
champions: []
since: 2026-06
ring_history:
  - { ring: assess, date: 2026-06, reason: "Gap fix — used in our open-source-stack write-up, no own entry yet" }
articles:
  - { title: "Open-Source KI-Stack für Unternehmen: OpenWebUI, LiteLLM, Milvus und n8n im Praxiseinsatz", url: "https://pexon-consulting.de/blog/open-source-ki-stack-unternehmen/", date: 2026-04 }
---

## What is it?

Open-source vector database built for very large-scale similarity search, with a distributed architecture (and Zilliz as managed offering).

## Why this ring?

Part of the open-source stack we wrote up in practice; Assess because Qdrant is our standing default and Milvus must show where its scale-out architecture beats it for our actual corpus sizes.

## When to use it — and when not?

- **Use** in evaluations for very large vector corpora where Qdrant's scaling becomes the question.
- **Don't** add a fourth vector DB to an estate that already runs one fine.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://milvus.io/
