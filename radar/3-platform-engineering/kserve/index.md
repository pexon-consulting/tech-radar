---
name: KServe
layer: 3-platform-engineering
ring: trial
tags: [model-serving, kubernetes, mlops]
champions: []
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Radar expansion — standardized model serving on K8s, building references" }
---

## What is it?

Kubernetes-native model serving: standardized inference CRDs, autoscaling (including scale-to-zero), canary rollouts for models.

## Why this ring?

Our candidate for standardized model serving on client platforms — promising, but we want more production miles before making it the default over plain Deployments + vLLM.

## When to use it — and when not?

- **Use** when a platform serves many models with differing scaling profiles.
- **Don't** add the complexity for a single-model deployment.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://kserve.github.io/website/
