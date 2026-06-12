---
name: OpenSearch / Elasticsearch
layer: 4-data-knowledge
ring: trial
tags: [search, bm25, hybrid-search, aws]
champions: []
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Radar expansion — keyword/hybrid retrieval, often already present at clients" }
---

## What is it?

Distributed search engines — BM25 keyword search, aggregations, and increasingly vector/hybrid retrieval. OpenSearch is the AWS-managed open-source fork.

## Why this ring?

Many clients already run one of them — extending an existing cluster for RAG retrieval often beats introducing a new vector DB.

## When to use it — and when not?

- **Use** when the client has an existing cluster, or when keyword+filter search dominates over pure semantic search.
- **Don't** pick it green-field purely for vector search (→ Qdrant).

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://opensearch.org/
