---
name: Grafana / Prometheus
layer: 3-platform-engineering
ring: adopt
tags: [observability, monitoring, metrics]
champions: []
since: 2026-06
ring_history:
  - { ring: adopt, date: 2026-06, reason: "Radar expansion — observability default on our platforms" }
certifications:
  - { name: "PCA — Prometheus Certified Associate", issuer: "CNCF", holders: [] }
---

## What is it?

The open-source observability pair: Prometheus for metrics collection and alerting, Grafana for dashboards — extended with Loki/Tempo where logs and traces are needed.

## Why this ring?

Our observability default on every platform we operate, including GPU and inference metrics (DCGM exporter, vLLM metrics).

## When to use it — and when not?

- **Use** as the baseline on every K8s platform; dashboard GPU utilization and model latency from day one.
- **Don't** replace a client's established Datadog/Dynatrace estate without a reason.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://grafana.com/ · https://prometheus.io/
