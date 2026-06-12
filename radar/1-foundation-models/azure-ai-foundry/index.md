---
name: Azure AI Foundry
layer: 1-foundation-models
ring: adopt
tags: [azure, model-hosting, inference, gpt, claude, mistral]
champions: []
since: 2026-06
ring_history:
  - { ring: adopt, date: 2026-06, reason: "Initial radar import — Pexon default per stack documentation" }
certifications:
  - { name: "AI-102 — Azure AI Engineer Associate", issuer: "Microsoft", holders: [] }
references:
  - { client: "Currenta", title: "AI Agents für Chemie & Pharma — Azure OpenAI RAG, Roadmap bis MVP", url: "https://pexon-consulting.de/casestudie/ai-agents-bei-currenta-vom-workshop-zur-umsetzungs-roadmap/", public: true }
articles:
  - { title: "Azure OpenAI Datenschutz: FAQ für Unternehmen 2026", url: "https://pexon-consulting.de/blog/azure-openai-datenschutz-faq/", date: 2026-06 }
  - { title: "Azure AI Foundry Tutorial: Erste KI-App in 60 Minuten", url: "https://pexon-consulting.de/blog/azure-ai-foundry-tutorial-deutsch/", date: 2026-04 }
  - { title: "Azure AI Foundry: Der komplette Leitfaden für 2026", url: "https://pexon-consulting.de/blog/azure-ai-foundry-leitfaden/", date: 2026-03 }
  - { title: "Azure OpenAI in EU Data Zones: Garantierte Datensouveränität für Unternehmen", url: "https://pexon-consulting.de/blog/azure-openai-eu-data-zones-garantierte-datensouveraenitaet/", date: 2025-03 }
  - { title: "Azure AI PTU im Azure OpenAI Service: Ein umfassender Leitfaden", url: "https://pexon-consulting.de/blog/azure-ai-ptu/", date: 2024-12 }
---

## What is it?

Microsoft's managed platform for hosting and consuming foundation models (GPT, Claude, Mistral and others) with enterprise controls: private networking, content filtering, regional deployment.

## Why this ring?

Our primary model platform for Azure-based clients — most German enterprise clients already have Azure agreements and Entra ID in place, which makes Foundry the path of least resistance.

## When to use it — and when not?

- **Use** when the client is Azure-native or needs EU data residency with a hyperscaler.
- **Don't use** for sovereign/on-prem requirements (→ vLLM/SGLang) or AWS-native setups (→ Bedrock).

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

- Document per project: model choice rationale, context window requirements, hosting region, zero-data-retention config.

## Resources

- Official docs: https://learn.microsoft.com/azure/ai-foundry/
