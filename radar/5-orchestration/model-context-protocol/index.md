---
name: Model Context Protocol (MCP)
layer: 5-orchestration
ring: adopt
tags: [mcp, tool-integration, standards]
champions: []
since: 2026-06
ring_history:
  - { ring: adopt, date: 2026-06, reason: "Initial radar import — our standard for agent-tool integration" }
articles:
  - { title: "MCP Tool Poisoning: Wie deutsche Unternehmen Agent-Pipelines absichern", url: "https://pexon-consulting.de/blog/mcp-tool-poisoning-agent-pipelines-absichern/", date: 2026-06 }
  - { title: "LLM Agent Sandboxing: Wie MCP, Tool Permissions und DSGVO zusammenpassen", url: "https://pexon-consulting.de/blog/llm-agent-sandboxing-mcp-dsgvo/", date: 2026-05 }
  - { title: "MCP Registry: Eigene Subregistry für Enterprise IT?", url: "https://pexon-consulting.de/blog/mcp-registry-enterprise-subregistry/", date: 2026-04 }
  - { title: "MCP vs API vs iPaaS: Welcher Ansatz passt 2026?", url: "https://pexon-consulting.de/blog/mcp-vs-api-vs-ipaas/", date: 2026-03 }
  - { title: "KI-Integration zu Datenquellen: Das USB-C für KI — warum der Mittelstand es 2026 braucht", url: "https://pexon-consulting.de/blog/ki-integration-zu-datenquellen/", date: 2026-02 }
  - { title: "MCP Server für Google Drive: KI-gesteuerte Dokumentenautomatisierung 2026", url: "https://pexon-consulting.de/blog/mcp-server-fuer-googledrive/", date: 2026-01 }
---

## What is it?

Open protocol (Anthropic-initiated, broadly adopted) for connecting LLM agents to tools and data sources via standardized servers — instead of bespoke per-tool integration code.

## Why this ring?

Our standard for agent-tool integration. Governance principle: every MCP tool in a client setup is registered, versioned and access-controlled in a central MCP registry with RBAC and audit logging.

## When to use it — and when not?

- **Use** whenever an agent needs tools or enterprise data — build or reuse an MCP server rather than hardcoding integrations.
- **Don't** wrap trivial single-purpose functions that only one agent will ever call.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://modelcontextprotocol.io/
