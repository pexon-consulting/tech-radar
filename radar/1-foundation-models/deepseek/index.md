---
name: DeepSeek (Self-Hosted)
layer: 1-foundation-models
ring: assess
tags: [open-weights, reasoning, self-hosted, dsgvo]
champions: []
since: 2026-06
ring_history:
  - { ring: assess, date: 2026-06, reason: "Added from blog coverage — four posts on local/Azure deployment, no project reference" }
articles:
  - { title: "DeepSeek lokal installieren: Kostenanalyse 2026", url: "https://pexon-consulting.de/blog/kostenanalyse-lokale-deep-seek-installation/", date: 2025-09 }
  - { title: "DeepSeek Offline nutzen: R1-Modelle sicher & DSGVO-konform", url: "https://pexon-consulting.de/blog/deepseek-offline-nutzen-anleitung/", date: 2025-03 }
  - { title: "Deepseek R1 auf Azure Machine Learning datenschutzkonform und privat deployen", url: "https://pexon-consulting.de/blog/deepseek-r1-azure-deployment-anleitung/", date: 2025-01 }
  - { title: "Lokale GPT-Modelle in Deutschland aufbauen: DeepSeek offline installieren und nutzen", url: "https://pexon-consulting.de/blog/deepseek-offline-installieren-und-nutzen/", date: 2025-01 }
---

## What is it?

Open-weight reasoning models (R1 family) that run fully self-hosted — on our GPU infrastructure or privately on Azure ML — making strong reasoning available in DSGVO-strict environments.

## Why this ring?

Four posts deep on installation, cost and private Azure deployment, but no client project referenced. Assess: a model option inside our sovereign stack (served via vLLM/SGLang), evaluated per use case against Llama/Mistral alternatives.

## When to use it — and when not?

- **Use** in sovereign/offline evaluations where reasoning quality per GPU-Euro matters.
- **Don't** select it without the client's risk assessment on model provenance — for some sectors that conversation decides it.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://github.com/deepseek-ai
