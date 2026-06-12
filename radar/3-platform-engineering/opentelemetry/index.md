---
name: OpenTelemetry
layer: 3-platform-engineering
ring: trial
tags: [observability, tracing, metrics, standards]
champions: []
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Gap fix — the vendor-neutral glue between our observability and LLM-tracing stack" }
---

## What is it?

The vendor-neutral standard for traces, metrics and logs — one instrumentation layer that exports to Grafana/Tempo, Langfuse (OTel-compatible) or any commercial APM.

## Why this ring?

It connects our two observability worlds: platform telemetry (Grafana/Prometheus) and LLM tracing (Langfuse) can share OTel instrumentation instead of double-instrumenting services.

## When to use it — and when not?

- **Use** OTel SDKs as the default instrumentation in every service we build — the export target can change, the instrumentation shouldn't.
- **Don't** rip out a client's working proprietary APM agents mid-project for purity.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://opentelemetry.io/
