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
  - { title: "Service Mesh in bestehende Landschaften einführen, ohne den laufenden Betrieb zu gefährden", url: "https://pexon-consulting.de/blog/service-mesh-in-bestehende-landschaften-einfuehren-ohne-den-laufenden-betrieb-zu-gefaehrden/", date: 2025-12 }
  - { title: "Sicherheit mit Service Mesh: mTLS leicht erklärt", url: "https://pexon-consulting.de/blog/sicherheit-mit-service-mesh-mtls-leicht-erklaert/", date: 2025-12 }
  - { title: "Fünf Gründe, warum du ein Service Mesh verwenden solltest", url: "https://pexon-consulting.de/blog/fuenf-gruende-warum-du-ein-service-mesh-verwenden-solltest/", date: 2025-12 }
  - { title: "Service Mesh erklärt: Control Plane vs. Data Plane in Kubernetes", url: "https://pexon-consulting.de/blog/control-plane-vs-data-plane-das-service-mesh-in-zwei-schichten-erklaert/", date: 2025-12 }
  - { title: "Warum Microservices ohne Service Mesh schnell unübersichtlich werden", url: "https://pexon-consulting.de/blog/warum-microservices-ohne-service-mesh-schnell-unuebersichtlich-werden/", date: 2025-12 }
---

## What is it?

Service mesh for Kubernetes — mTLS between services, traffic management (canary, splitting, rollbacks) and centrally enforced policies. Our complete nine-part series is linked below.

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
