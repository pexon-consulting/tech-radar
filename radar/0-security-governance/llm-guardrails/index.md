---
name: LLM Guardrails & Prompt-Injection Defense
layer: 0-security-governance
ring: assess
tags: [llm-security, owasp, prompt-injection, guardrails]
champions: []
since: 2026-06
ring_history:
  - { ring: assess, date: 2026-06, reason: "Added from blog coverage — recurring LLM-security topic with no radar home" }
articles:
  - { title: "OWASP LLM Top 10: Prompt Injection Defense für deutsche Unternehmen", url: "https://pexon-consulting.de/blog/owasp-llm-top-10-prompt-injection-defense-dach/", date: 2026-05 }
  - { title: "Indirect Prompt Injection in RAG-Systemen: Wenn Dokumente den Agent übernehmen", url: "https://pexon-consulting.de/blog/indirect-prompt-injection-rag-systeme/", date: 2026-05 }
  - { title: "Azure AI Content Safety: Kurzüberblick — Features für eigene KI-Anwendungen", url: "https://pexon-consulting.de/blog/azure-ai-content-safety/", date: 2025-03 }
---

## What is it?

The defense layer for LLM applications: input/output filtering, prompt-injection detection (direct and indirect via retrieved documents), tool-permission scoping — anchored on the OWASP LLM Top 10. Tooling in this space includes content-safety services (e.g. Azure AI Content Safety) and open-source guardrail frameworks.

## Why this ring?

Every RAG/agent system we ship needs this, and we publish about it — but we haven't standardized on a specific guardrail stack yet. Assess until we converge on a default toolset; the practices themselves are non-negotiable on client projects.

## When to use it — and when not?

- **Use** threat-modeling against the OWASP LLM Top 10 on every agent/RAG build; treat retrieved documents as untrusted input.
- **Don't** treat a content filter as sufficient defense — tool permissions and sandboxing (→ MCP entry) carry most of the weight.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://owasp.org/www-project-top-10-for-large-language-model-applications/
