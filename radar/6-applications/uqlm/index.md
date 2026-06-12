---
name: UQLM
layer: 6-applications
ring: assess
tags: [uncertainty, evaluation, regulated-industries]
champions: [christoph.gotschlich]
since: 2026-06
ring_history:
  - { ring: assess, date: 2026-06, reason: "Initial radar import — evaluating for regulated-industry RAG outputs" }
---

## What is it?

Python package for uncertainty quantification on LLM outputs. Flags low-confidence responses — useful in regulated contexts (banking, insurance, healthcare) where hallucinations have high cost.

## Why this ring?

Promising addition to the output layer of RAG apps in regulated industries; we are evaluating it combined with RAGAS to get both retrieval quality and generation confidence signals.

## When to use it — and when not?

- **Use** in PoCs for regulated-industry RAG apps where low-confidence answers must be flagged or routed to humans.
- **Don't** add the latency/complexity for low-stakes internal tools.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://github.com/cvs-health/uqlm
