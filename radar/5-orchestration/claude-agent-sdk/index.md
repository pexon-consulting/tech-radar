---
name: Claude Agent SDK
layer: 5-orchestration
ring: trial
tags: [agents, anthropic, sdk]
champions: []
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Initial radar import — agentic framework per stack documentation, building production evidence" }
---

## What is it?

Anthropic's SDK for building autonomous agents on Claude — the agent loop, tool execution, context management and MCP support come built-in rather than hand-rolled.

## Why this ring?

Part of our agentic framework lineup alongside LangGraph. Trial: strong fit for Claude-centric agent builds, and we are accumulating production references before declaring it a default.

## When to use it — and when not?

- **Use** for agentic applications committed to Claude models, especially with MCP-based tooling.
- **Don't** use it when the client requires model-agnostic orchestration (→ LangGraph).

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://docs.claude.com/en/api/agent-sdk/overview
