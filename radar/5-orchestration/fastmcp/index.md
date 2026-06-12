---
name: FastMCP
layer: 5-orchestration
ring: assess
tags: [mcp, python, sdk, tooling]
champions: []
since: 2026-06
ring_history:
  - { ring: assess, date: 2026-06, reason: "Added from leadership stack proposal — framework for our custom-built MCP servers" }
---

## What is it?

The Pythonic framework for building MCP servers — decorators turn functions into MCP tools/resources, with auth, composition and deployment ergonomics on top of the protocol SDK.

## Why this ring?

Our MCP strategy is "custom build" where no official server exists — FastMCP is the proposed standard way to build them instead of hand-rolling protocol plumbing. Assess until the first client-facing servers built with it ship.

## When to use it — and when not?

- **Use** for every custom MCP server we build in Python.
- **Don't** wrap what an official, maintained MCP server already covers (→ MCP entry's governance rules apply).

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://github.com/jlowin/fastmcp
