---
name: Apache Airflow
layer: 4-data-knowledge
ring: trial
tags: [etl, orchestration, data-pipelines, pyspark]
champions: []
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Gap fix — production use in the BaFin-regulated data-mesh case study" }
references:
  - { client: "Genossenschafts-IT-Dienstleister", title: "On-Premise Data Mesh für eine BaFin-regulierte Banking-Plattform (Python, PySpark, Airflow)", url: "https://pexon-consulting.de/casestudie/genossenschafts-it-dienstleister-on-premise-data-mesh-fuer-eine-bafin-regulierte-banking-plattform-mit-python-pyspark-und-airflow/", public: true }
---

## What is it?

The standard open-source workflow orchestrator for data pipelines — DAGs as Python code, battle-tested scheduling and backfills; in our projects typically paired with PySpark for the heavy lifting.

## Why this ring?

Ran in production in a BaFin-regulated on-premise data mesh (public case study). Trial rather than Adopt because managed alternatives (Fabric pipelines, Databricks workflows) win on cloud-committed clients — Airflow is our answer where self-hosted/regulated rules them out.

## When to use it — and when not?

- **Use** for self-hosted/regulated data platforms and as the neutral orchestrator across heterogeneous stacks.
- **Don't** introduce it next to a client's existing managed pipeline tooling.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://airflow.apache.org/
