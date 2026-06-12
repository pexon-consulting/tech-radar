---
name: Langfuse
layer: 3-platform-engineering
ring: trial
tags: [llm-observability, tracing, evals, self-hosted]
champions: []
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Radar expansion — LLM tracing/evals, self-hostable for sovereign setups" }
articles:
  - { title: "LLM-Kosten kontrollieren mit LangFuse: Token-Tracking für Enterprise", url: "https://pexon-consulting.de/blog/llm-kosten-langfuse-token-tracking-finops/", date: 2026-05 }
  - { title: "LangFuse vs LangSmith vs Helicone: LLM Observability Vergleich 2026", url: "https://pexon-consulting.de/blog/langfuse-vs-langsmith-helicone-observability-vergleich/", date: 2026-05 }
  - { title: "LangFuse Self-Hosted auf Azure: DSGVO-konformes LLM-Monitoring", url: "https://pexon-consulting.de/blog/langfuse-self-hosted-azure-dsgvo/", date: 2026-05 }
  - { title: "LLM Observability mit Langfuse: Tracing für AI-Act-ready Systeme", url: "https://pexon-consulting.de/blog/llm-observability-langfuse-tracing-guardrails/", date: 2026-04 }
---

## What is it?

Open-source LLM engineering platform: tracing of agent/RAG calls, prompt management, evals and cost tracking. Self-hostable — relevant for sovereign setups.

## Why this ring?

LLM apps without tracing are undebuggable; Langfuse is our current pick because it self-hosts cleanly on the platforms we build.

## When to use it — and when not?

- **Use** on every non-trivial LLM application — wire tracing in from the first sprint.
- **Don't** duplicate it where the client already standardizes on another LLM-observability stack.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://langfuse.com/
