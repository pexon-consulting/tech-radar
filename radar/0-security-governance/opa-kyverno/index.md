---
name: OPA / Kyverno (Policy as Code)
layer: 0-security-governance
ring: trial
tags: [policy-as-code, kubernetes, compliance, admission-control]
champions: []
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Gap fix — our landing-zone entries promise policy-as-code, the tooling had no entry" }
---

## What is it?

Policy engines for Kubernetes and beyond: Open Policy Agent (Rego, general-purpose) and Kyverno (K8s-native YAML policies) enforce rules at admission time — image provenance, resource limits, network policies, labels.

## Why this ring?

Our landing-zone and governance story explicitly promises policy-as-code; on the K8s layer these two are how it's enforced. Trial: pick per engagement (Kyverno for K8s-only platform teams, OPA where policies span beyond K8s) until we declare one the default.

## When to use it — and when not?

- **Use** admission policies on every multi-team K8s platform — compliance requirements (KRITIS, ISO 27001) make them mandatory anyway.
- **Don't** run both engines on one cluster.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://www.openpolicyagent.org/ · https://kyverno.io/
