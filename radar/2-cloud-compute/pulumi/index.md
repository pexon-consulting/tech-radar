---
name: Pulumi
layer: 2-cloud-compute
ring: hold
tags: [iac, provisioning]
champions: []
since: 2026-06
ring_history:
  - { ring: hold, date: 2026-06, reason: "Radar expansion — we standardize IaC on Terraform; no new Pulumi estates" }
---

## What is it?

Infrastructure-as-code using general-purpose languages (TypeScript, Python, Go) instead of HCL.

## Why this ring?

**Hold — use Terraform/OpenTofu instead.** Technically fine, but running two IaC stacks splits module reuse, review experience and hiring. We maintain existing Pulumi estates at clients; we don't start new ones.

## When to use it — and when not?

- **Use** only to maintain a client's existing Pulumi codebase.
- **Don't** start new projects with it.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://www.pulumi.com/
