---
name: RAGAS
layer: 6-applications
ring: trial
tags: [evaluation, rag, quality]
champions: [christoph.gotschlich]
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Initial radar import — used in pilot acceptance criteria" }
---

## What is it?

Evaluation framework for RAG pipelines. Measures faithfulness, answer relevance, context precision, and recall without requiring ground-truth labels for every run.

## Why this ring?

We integrate RAGAS evals into pilot acceptance criteria — run before and after retrieval tuning to show measurable improvement. Promote to Adopt once it's standard across all RAG deliveries.

## When to use it — and when not?

- **Use** on every RAG pilot to make retrieval quality measurable; results go into MLflow as experiment metrics.
- **Don't** rely on RAGAS alone for regulated contexts — combine with uncertainty quantification (→ UQLM).

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://github.com/explodinggradients/ragas
