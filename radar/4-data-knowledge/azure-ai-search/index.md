---
name: Azure AI Search
layer: 4-data-knowledge
ring: trial
tags: [vector-db, hybrid-search, azure, managed]
champions: []
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Added from leadership stack proposal — positioned as default vector store for Azure-committed clients" }
---

## What is it?

Azure's managed search service — vector, keyword and hybrid retrieval with semantic ranking, natively integrated with Azure AI Foundry, Document Intelligence and Blob Storage.

## Why this ring?

Positioned internally as the fastest route to RAG retrieval on Azure-committed clients: "1 Woche, 80 % Use-Case-Coverage" — no cluster to operate, IAM and networking come from the landing zone. Trial until a documented production reference lands here.

## When to use it — and when not?

- **Use** as the default retrieval layer in Azure-native RAG stacks (Foundry + Document Intelligence + Blob), especially when time-to-value beats tuning depth.
- **Don't** use it for sovereign/on-prem requirements (→ Qdrant, Vespa) or when retrieval needs exceed what its tuning surface offers — and watch the per-index pricing on many small tenants.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://learn.microsoft.com/azure/search/
