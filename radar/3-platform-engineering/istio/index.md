---
name: Istio (Service Mesh)
layer: 3-platform-engineering
ring: trial
tags: [service-mesh, mtls, zero-trust, kubernetes]
champions: []
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Added from blog coverage — nine-part service-mesh series (Dec 2025) signals deep practice" }
articles:
  - { title: "Was ist ein Service Mesh?", url: "https://pexon-consulting.de/blog/was-ist-ein-service-mesh/", date: 2025-12 }
  - { title: "Zero-Trust Beyond mTLS: Die Control Plane von Istio absichern", url: "https://pexon-consulting.de/blog/zero-trust-beyond-mtls-wie-wir-die-control-plane-von-istio-besser-absichern-koennen-und-sollten/", date: 2025-12 }
  - { title: "Service Mesh & Progressive Delivery: Canary-Releases, Traffic-Splitting & Safe Rollbacks", url: "https://pexon-consulting.de/blog/service-mesh-progressive-delivery-ein-deep-dive-in-canary-releases-traffic-splitting-safe-rollbacks/", date: 2025-12 }
  - { title: "Service Mesh Governance: Policies zentral durchsetzen", url: "https://pexon-consulting.de/blog/governance-im-service-mesh-einheitliche-regeln-fuer-sicherheit-compliance-durchsetzen/", date: 2025-12 }
---

## What is it?

Service mesh for Kubernetes — mTLS between services, traffic management (canary, splitting, rollbacks) and centrally enforced policies. We published a nine-part series on it; the four most substantial posts are linked here.

## Why this ring?

Deep written expertise and a clear fit for zero-trust requirements on our platforms; Trial because a mesh is significant operational weight and we recommend it case-by-case, not by default.

## When to use it — and when not?

- **Use** on multi-team K8s platforms with zero-trust/compliance requirements or progressive-delivery needs.
- **Don't** add a mesh to a handful of services — mTLS via simpler means first.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://istio.io/
