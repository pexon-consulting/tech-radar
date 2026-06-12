---
name: LiteLLM
layer: 3-platform-engineering
ring: trial
tags: [llm-gateway, routing, cost-tracking]
champions: []
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Initial radar import — gateway component of our AI platform setups" }
articles:
  - { title: "LLM Gateway 4er-Vergleich: LiteLLM, Portkey, Helicone und Kong", url: "https://pexon-consulting.de/blog/llm-gateway-4er-vergleich-kong-ai-gateway/", date: 2026-06 }
---

## What is it?

Open-source LLM gateway: one OpenAI-compatible API in front of many providers, with routing, budgets, rate limits and usage tracking per team/key.

## Why this ring?

The gateway component in our AI platform engineering setups — central model access with cost attribution instead of API keys scattered across teams.

## When to use it — and when not?

- **Use** when a client consumes models from multiple providers or needs per-team cost control and audit on model usage.
- **Don't** add it for a single app talking to a single provider — needless hop.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://github.com/BerriAI/litellm
