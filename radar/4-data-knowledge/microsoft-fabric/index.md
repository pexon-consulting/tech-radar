---
name: Microsoft Fabric / Snowflake / Databricks
layer: 4-data-knowledge
ring: trial
tags: [data-platform, lakehouse, etl, dbt]
champions: []
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Initial radar import — data platform defaults, depth varies by engagement" }
certifications:
  - { name: "DP-600 — Fabric Analytics Engineer Associate", issuer: "Microsoft", holders: [] }
  - { name: "SnowPro Core", issuer: "Snowflake", holders: [] }
  - { name: "Databricks Certified Data Engineer Associate", issuer: "Databricks", holders: [] }
references:
  - { client: "AXXCON", title: "Datenplattform mit Microsoft Fabric", url: "https://pexon-consulting.de/casestudie/datenplatforn-mit-microsoft-fabric/", public: true }
articles:
  - { title: "Pilotprojekt Datenplattform mit Microsoft Fabric: Risikoarm starten", url: "https://pexon-consulting.de/blog/pilotprojekt-datenplattform-microsoft-fabric/", date: 2026-06 }
  - { title: "Databricks vs Fabric: Welches Tool passt 2026?", url: "https://pexon-consulting.de/blog/databricks-vs-microsoft-fabric-analytics-tool/", date: 2026-06 }
  - { title: "Data Quality Agent: KI-gestützte Datenqualität in Fabric", url: "https://pexon-consulting.de/blog/data-quality-agent-microsoft-fabric/", date: 2026-05 }
---

## What is it?

The managed data platform triad we encounter and build on at clients: Microsoft Fabric (Azure-native, Power-BI-integrated), Snowflake (cloud-agnostic warehouse), Databricks (lakehouse, with dbt and Airflow for pipelines).

## Why this ring?

We integrate AI workloads with all three regularly; Trial because we usually extend a client's existing platform rather than green-fielding one — depth of experience varies per platform. As individual production references accumulate, split this entry per platform and promote.

## When to use it — and when not?

- **Use** the platform the client already has — the knowledge layer for RAG should build on the governed data platform, not bypass it.
- **Don't** introduce a new data platform as a side effect of an AI project.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://www.microsoft.com/microsoft-fabric
- https://www.snowflake.com/
- https://www.databricks.com/
