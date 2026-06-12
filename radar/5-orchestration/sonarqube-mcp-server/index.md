---
name: SonarQube MCP Server
layer: 5-orchestration
ring: assess
tags: [mcp, code-quality, devsecops]
champions: []
since: 2026-06
ring_history:
  - { ring: assess, date: 2026-06, reason: "Initial radar import — promising registry candidate, limited usage so far" }
---

## What is it?

Official MCP server exposing SonarQube's code quality and security analysis to LLM agents — code quality signals without custom integration work.

## Why this ring?

A natural candidate for client MCP registries where SonarQube is already in use; we still need real usage in AI-assisted code review or DevSecOps workflows before promoting.

## When to use it — and when not?

- **Use** in PoCs for AI-assisted code review agents at SonarQube-running clients.
- **Don't** introduce SonarQube itself just to get this tool.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://github.com/SonarSource/sonarqube-mcp-server
