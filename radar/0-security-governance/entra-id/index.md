---
name: Entra ID (SSO / Conditional Access)
layer: 0-security-governance
ring: adopt
tags: [identity, sso, mfa, rbac]
champions: []
since: 2026-06
ring_history:
  - { ring: adopt, date: 2026-06, reason: "Initial radar import — identity default per stack documentation" }
certifications:
  - { name: "SC-300 — Identity and Access Administrator Associate", issuer: "Microsoft", holders: [] }
references:
  - { client: "Liebherr", title: "Open-Source-KI-Chatbot mit persönlichem Datenzugriff (SSO/RBAC via Entra)", url: "https://pexon-consulting.de/casestudie/open-source-ki-chatbot-mit-persoenlichem-datenzugriff-bei-liebherr/", public: true }
---

## What is it?

Microsoft's identity platform — SSO, MFA, Conditional Access. The identity backbone in nearly every German enterprise we work with.

## Why this ring?

Our default identity layer across all stack layers: RBAC on data, models and tools is enforced against Entra identities; audit trails reference them.

## When to use it — and when not?

- **Use** as the identity source for every AI platform component we deploy at Entra-running clients (which is most of them).
- **Don't** build parallel user stores in AI applications — integrate, don't duplicate.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

- Non-negotiable on client projects: RBAC on data/models/tools, DSGVO/EU-AI-Act risk classification, audit logging on model calls and MCP tools, DE/EU data residency by default.

## Resources

- https://learn.microsoft.com/entra/
