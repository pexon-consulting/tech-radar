---
name: Kubernetes (EKS / AKS / GKE / OpenShift)
layer: 3-platform-engineering
ring: adopt
tags: [container, orchestration, gpu, managed-k8s]
champions: []
since: 2026-06
ring_history:
  - { ring: adopt, date: 2026-06, reason: "Initial radar import — Pexon default per stack documentation" }
certifications:
  - { name: "CKA — Certified Kubernetes Administrator", issuer: "CNCF", holders: [] }
  - { name: "CKAD — Certified Kubernetes Application Developer", issuer: "CNCF", holders: [] }
  - { name: "CKS — Certified Kubernetes Security Specialist", issuer: "CNCF", holders: [] }
references:
  - { client: "Spezialversicherer", title: "Von Monolith zu Microservices — Versicherungsplattform auf AKS", url: "https://pexon-consulting.de/casestudie/von-monolith-zu-microservices-spezialversicherungsplattform-auf-aks/", public: true }
  - { client: "Industrieversicherer", title: "Migration zu Azure Kubernetes Service", url: "https://pexon-consulting.de/casestudie/migration-zu-azure-kubernetes/", public: true }
  - { client: "Energieversorger", title: ".NET-Modernisierung und Migration auf AWS EKS", url: "https://pexon-consulting.de/casestudie/energiebranche-net-modernisierung/", public: true }
  - { client: "AOK", title: "DevOps-Automatisierung in AWS und OpenShift", url: "https://pexon-consulting.de/casestudie/aok/", public: true }
articles:
  - { title: "Kubernetes Security Hardening: 32-Punkte-Checkliste für Production", url: "https://pexon-consulting.de/blog/kubernetes-security-hardening-checkliste/", date: 2026-06 }
---

## What is it?

Container orchestration — the runtime layer for everything we deploy, including GPU node pools for model serving.

## Why this ring?

The unquestioned default. Managed flavors (EKS, AKS, GKE) preferred; OpenShift where the client mandates it.

## When to use it — and when not?

- **Use** for any workload beyond a single service — including AI inference with GPU node pools.
- **Don't** force it on tiny pilots where a managed container service or serverless does the job with less overhead.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://kubernetes.io/docs/
