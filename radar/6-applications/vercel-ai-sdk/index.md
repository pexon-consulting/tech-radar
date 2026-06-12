---
name: Vercel AI SDK
layer: 6-applications
ring: trial
tags: [typescript, streaming, chat-ui]
champions: []
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Radar expansion — TS layer between Next.js frontends and model APIs" }
---

## What is it?

TypeScript toolkit for AI apps: unified provider API, token streaming, structured output and chat-UI hooks — the glue between our Next.js frontends and the model layer.

## Why this ring?

Massively reduces boilerplate in chat/streaming UIs; Trial until it has carried a few more production frontends for us.

## When to use it — and when not?

- **Use** in every Next.js AI frontend instead of hand-rolling streaming and tool-call plumbing.
- **Don't** use it as a backend orchestration layer — agent logic lives in Layer 5.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://ai-sdk.dev/
