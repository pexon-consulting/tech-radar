---
name: HashiCorp Vault
layer: 0-security-governance
ring: trial
tags: [secrets-management, encryption, pki]
champions: []
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Gap fix — secrets management was missing from the security layer entirely" }
---

## What is it?

Secrets management, encryption-as-a-service and PKI — the self-hosted standard; on cloud-committed clients the managed equivalents (Azure Key Vault, AWS Secrets Manager) fill the same slot.

## Why this ring?

Every platform we build handles model API keys, DB credentials and signing material — secrets management is non-optional. Vault is the answer where multi-cloud or on-prem rules out the hyperscaler-native vaults.

## When to use it — and when not?

- **Use** Vault for multi-cloud/on-prem estates; use the cloud-native vault on single-cloud clients — but never secrets in env files or pipelines.
- **Don't** self-host Vault for a single-cloud client without a reason — operational weight without benefit.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://developer.hashicorp.com/vault
