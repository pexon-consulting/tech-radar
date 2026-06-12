---
name: Argo CD
layer: 3-platform-engineering
ring: adopt
tags: [gitops, cd, kubernetes]
champions: []
since: 2026-06
ring_history:
  - { ring: adopt, date: 2026-06, reason: "Radar expansion — GitOps default for K8s deployments" }
certifications:
  - { name: "CAPA — Certified Argo Project Associate", issuer: "CNCF", holders: [] }
articles:
  - { title: "ArgoCD auf AKS: GitOps für Azure Kubernetes in der Praxis", url: "https://pexon-consulting.de/blog/argocd-aks-gitops-kubernetes/", date: 2026-05 }
---

## What is it?

GitOps continuous delivery for Kubernetes — the cluster state is whatever Git says it is.

## Why this ring?

Our default deployment mechanism on every Kubernetes platform we build, including model-serving workloads.

## When to use it — and when not?

- **Use** on any K8s platform with more than a handful of apps.
- **Don't** bolt it onto non-K8s deployment targets.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://argo-cd.readthedocs.io/
