---
name: Azure AI Document Intelligence
layer: 4-data-knowledge
ring: trial
tags: [ocr, document-parsing, azure, idp]
champions: []
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Added from case-study coverage — contract data extraction delivered with it" }
references:
  - { client: "Enterprise-Kunde", title: "KI-gestützte Vertragsdatenextraktion mit Azure Document Intelligence", url: "https://pexon-consulting.de/casestudie/ki-gestuetzte-vertragsdatenextraktion/", public: true }
---

## What is it?

Azure's managed OCR/document-extraction service — prebuilt and custom models for contracts, invoices and forms, with layout and table understanding.

## Why this ring?

Delivered in a public contract-data-extraction project; the managed counterpart to our open-source parsing stack (→ Docling) when the client is Azure-committed and wants SLAs over self-hosting.

## When to use it — and when not?

- **Use** for document-intelligence pipelines on Azure-committed clients, especially forms/invoices with custom-model training.
- **Don't** use it where data must not touch a managed service (→ Docling + VLM self-hosted).

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://learn.microsoft.com/azure/ai-services/document-intelligence/
