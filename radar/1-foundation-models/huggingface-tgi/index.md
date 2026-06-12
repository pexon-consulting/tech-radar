---
name: Hugging Face TGI
layer: 1-foundation-models
ring: trial
tags: [inference, self-hosted, huggingface]
champions: []
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Radar expansion — alternative serving stack to vLLM" }
---

## What is it?

Text Generation Inference — Hugging Face's production inference server for open-weight models, with tight Hub integration.

## Why this ring?

Solid alternative to vLLM, especially when the client is already deep in the Hugging Face ecosystem; we still prefer vLLM as the default.

## When to use it — and when not?

- **Use** when the client standardizes on Hugging Face tooling and Hub-based model governance.
- **Don't** introduce it alongside vLLM in the same platform — pick one serving stack.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://github.com/huggingface/text-generation-inference
