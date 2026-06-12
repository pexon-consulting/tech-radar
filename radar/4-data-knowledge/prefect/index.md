---
name: Prefect
layer: 4-data-knowledge
ring: assess
tags: [etl, orchestration, data-pipelines, python]
champions: []
since: 2026-06
ring_history:
  - { ring: assess, date: 2026-06, reason: "Added from leadership stack proposal — ingestion orchestrator candidate next to Airflow" }
---

## What is it?

Python-native workflow orchestrator — plain functions become flows with retries, caching and observability; lighter to adopt and operate than Airflow's scheduler/DAG model.

## Why this ring?

Proposed as the orchestrator for our RAG ingestion pipelines (documents → chunking → embeddings → vector DB), where Airflow's operational weight is overkill. Assess: needs a head-to-head against Airflow (which carries our production reference) on a real ingestion workload.

## When to use it — and when not?

- **Use** in PoCs for Python-heavy ingestion pipelines that a few developers own end-to-end.
- **Don't** replace an established Airflow estate for it — the migration cost outweighs ergonomics.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://www.prefect.io/
