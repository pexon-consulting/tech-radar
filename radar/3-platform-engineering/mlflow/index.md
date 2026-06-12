---
name: MLflow
layer: 3-platform-engineering
ring: adopt
tags: [mlops, experiment-tracking, model-registry]
champions: [christoph.gotschlich]
since: 2026-06
ring_history:
  - { ring: adopt, date: 2026-06, reason: "Initial radar import — central MLOps backbone across projects" }
---

## What is it?

Open-source platform for the full ML lifecycle: experiment tracking, model registry, serving. Pairs well with Azure ML and SageMaker as managed alternatives.

## Why this ring?

Our central MLOps backbone across projects.

## When to use it — and when not?

- **Use** as the default for experiment tracking and as the model registry — the source of truth for promoted models. Track evals and fine-tuning runs as experiments.
- **Don't** add it to pure API-consumer projects with no models or evals of their own.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

- Deploy on Kubernetes; RAGAS eval results go into MLflow as experiment metrics.

## Resources

- https://github.com/mlflow/mlflow
