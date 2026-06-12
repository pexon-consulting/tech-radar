---
name: vLLM / SGLang
layer: 1-foundation-models
ring: adopt
tags: [inference, self-hosted, gpu, sovereign, on-prem]
champions: []
since: 2026-06
ring_history:
  - { ring: adopt, date: 2026-06, reason: "Initial radar import — Pexon default for sovereign/on-prem inference" }
references:
  - { client: "Rku IT", title: "Open-Source-LLM (LLaMA) mit RAG für First-Level-Support-Automation", url: "https://pexon-consulting.de/casestudie/rku-genai-und-llm/", public: true }
articles:
  - { title: "SGLang vs vLLM: Welche Inference Engine spart GPU-Kosten?", url: "https://pexon-consulting.de/blog/sglang-vs-vllm/", date: 2026-04 }
  - { title: "Open Source KI für Unternehmen: Llama, Mistral, DeepSeek im Enterprise-Einsatz", url: "https://pexon-consulting.de/blog/open-source-ki-fuer-unternehmen/", date: 2026-01 }
---

## What is it?

Open-source high-throughput inference engines for serving open-weight LLMs on our own GPU infrastructure. vLLM is the general-purpose default; SGLang shines for structured generation and high-concurrency agentic workloads.

## Why this ring?

Our default for sovereign and on-prem deployments where hyperscaler model APIs are off the table (KRITIS, banking, strict data-residency requirements).

## When to use it — and when not?

- **Use** when the client requires on-prem or sovereign hosting of open-weight models on GPU clusters (H100/A100, MI300X).
- **Don't use** when a managed API (Bedrock, AI Foundry) is acceptable — self-hosting only pays off when it's mandatory.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://github.com/vllm-project/vllm
- https://github.com/sgl-project/sglang
