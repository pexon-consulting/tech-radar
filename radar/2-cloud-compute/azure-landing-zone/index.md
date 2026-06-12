---
name: Azure Landing Zone
layer: 2-cloud-compute
ring: adopt
tags: [azure, landing-zone, policy-as-code, networking]
champions: []
since: 2026-06
ring_history:
  - { ring: adopt, date: 2026-06, reason: "Initial radar import — Pexon default per stack documentation" }
certifications:
  - { name: "AZ-104 — Azure Administrator Associate", issuer: "Microsoft", holders: [] }
  - { name: "AZ-305 — Azure Solutions Architect Expert", issuer: "Microsoft", holders: [] }
references:
  - { client: "Enterprise-Kunde", title: "Landingzone-Initiative: strukturierte Azure-Governance", url: "https://pexon-consulting.de/casestudie/landingzone-initiative-strukturierte-azure-governance-und-automatisierte-infrastrukturprozesse/", public: true }
  - { client: "Lebensmitteleinzelhändler", title: "Azure-Architektur, Landing Zone und Applikationsmigration", url: "https://pexon-consulting.de/casestudie/case-study-azure-landing-zone-food-retail/", public: true }
  - { client: "Industrieversicherer", title: "Sicherheit & Compliance — zentrales Azure-Plattform-Team", url: "https://pexon-consulting.de/casestudie/insurance-sicherheit-und-compliance/", public: true }
articles:
  - { title: "Azure Governance: So behalten Mittelständler die Kontrolle über ihre Cloud", url: "https://pexon-consulting.de/blog/azure-governance/", date: 2025-12 }
  - { title: "Azure Zertifizierungen und Karrierewege: Der strategische Leitfaden für IT-Profis", url: "https://pexon-consulting.de/blog/azure-zertifizierungen-leitfaden/", date: 2025-02 }
---

## What is it?

Microsoft's reference architecture for enterprise-scale Azure environments: management group hierarchy, policy-as-code, networking and security baseline.

## Why this ring?

Our default foundation for AI workloads on Azure — we extend the standard landing zone with AI-specific policies (model endpoint governance, GPU quotas, private endpoints for AI services).

## When to use it — and when not?

- **Use** as the starting point for every Azure-based client engagement that lacks a governed foundation.
- **Don't** rebuild from scratch when the client already runs a CAF-aligned landing zone — extend it instead.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://learn.microsoft.com/azure/cloud-adoption-framework/ready/landing-zone/
