---
name: Apache Kafka
layer: 4-data-knowledge
ring: trial
tags: [streaming, event-driven, data-pipelines]
champions: []
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Added on team confirmation — event streaming backbone in data engagements" }
---

## What is it?

The de-facto standard for event streaming — durable, replayable logs as the backbone for event-driven architectures and real-time data pipelines (self-hosted, or managed via Confluent/MSK/Event Hubs-Kafka-API).

## Why this ring?

Confirmed by the team as part of our data-engineering toolkit. Trial pending a documented production reference here — whoever ran it last, add the project and take the champion slot.

## When to use it — and when not?

- **Use** for event-driven integration and streaming ingestion into the knowledge layer (e.g. keeping vector indexes fresh from operational systems).
- **Don't** deploy it for batch workloads a scheduler covers (→ Airflow) — Kafka's operational weight needs a streaming-shaped problem.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://kafka.apache.org/
