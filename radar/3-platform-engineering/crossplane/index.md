---
name: Crossplane
layer: 3-platform-engineering
ring: trial
tags: [idp, provisioning, kubernetes, self-service]
champions: []
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Gap fix — named in our public stack (IDP: Backstage, Port, Crossplane), no own entry yet" }
---

## What is it?

Kubernetes-native control plane for infrastructure: cloud resources become K8s custom resources, enabling self-service provisioning behind an IDP portal.

## Why this ring?

The provisioning engine in our IDP reference setup (Backstage/Port + Crossplane, as published on our stack page). Trial: powerful in platform engagements, but compositions carry real complexity — needs a champion per engagement.

## When to use it — and when not?

- **Use** when an IDP needs governed self-service infrastructure beyond what pipelines + Terraform modules give you.
- **Don't** replace plain Terraform for estates without a platform team — Crossplane is a platform-team tool.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://www.crossplane.io/
