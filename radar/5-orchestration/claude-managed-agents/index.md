---
name: Claude Managed Agents
layer: 5-orchestration
ring: assess
tags: [anthropic, agents, managed, sandbox, permissions]
champions: []
since: 2026-06
ring_history:
  - { ring: assess, date: 2026-06, reason: "Added from blog coverage — two posts, evaluating against self-hosted agent runtimes" }
articles:
  - { title: "Claude Managed Agents: KI-Agenten sicher steuern [2026]", url: "https://pexon-consulting.de/blog/claude-managed-agents-enterprise-guide/", date: 2026-04 }
  - { title: "Claude Managed Agents: Autonome KI-Agents ohne eigene Infrastruktur", url: "https://pexon-consulting.de/blog/claude-managed-agents-unternehmen/", date: 2026-04 }
---

## What is it?

Anthropic's server-side agent platform: agents run in a managed sandbox with controlled tool access (filesystem, shell, MCP servers), session-based instead of request-based, with declarative permission policies (`always_allow` / `always_ask`) in the agent definition.

## Why this ring?

Attractive where clients want autonomous agents without operating agent infrastructure, and the built-in permission model fits compliance-heavy contexts (NIS2, DORA). Assess: we are weighing it against self-hosted runtimes (LangGraph platform, own sandboxing) on data-residency and cost.

## When to use it — and when not?

- **Use** in evaluations for human-in-the-loop agent use cases where managed infrastructure is acceptable.
- **Don't** propose it where strict data residency rules out managed execution (→ self-hosted Layer-5 stack).

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://docs.claude.com/
