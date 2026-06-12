---
name: Ollama
layer: 1-foundation-models
ring: assess
tags: [local-llm, prototyping, dev-tooling]
champions: []
since: 2026-06
ring_history:
  - { ring: assess, date: 2026-06, reason: "Radar expansion — local dev inference, not production serving" }
articles:
  - { title: "Ollama vs. vLLM vs. TGI: Inference Engines im Vergleich [2026]", url: "https://pexon-consulting.de/blog/ollama-vllm-tgi-vergleich-inference-engines/", date: 2026-03 }
  - { title: "Private KI mit Ubuntu & Ollama: Fünf Open-Source-Bausteine für Unternehmen", url: "https://pexon-consulting.de/blog/private-ki-mit-ubuntu-ollama/", date: 2025-06 }
---

## What is it?

Local LLM runner for laptops and workstations — pull and run open-weight models with one command.

## Why this ring?

Great for offline prototyping and demos; not a production serving stack (→ vLLM/SGLang).

## When to use it — and when not?

- **Use** for local development, quick demos, air-gapped experiments.
- **Don't** serve client workloads with it.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://ollama.com/
