---
name: Jenkins
layer: 3-platform-engineering
ring: hold
tags: [ci, legacy]
champions: []
since: 2026-06
ring_history:
  - { ring: hold, date: 2026-06, reason: "Radar expansion — no new Jenkins setups; GitHub Actions/GitLab CI instead" }
---

## What is it?

The classic self-hosted CI server.

## Why this ring?

**Hold — use GitHub Actions or GitLab CI instead.** Plugin sprawl, upgrade pain and groovy pipelines make every Jenkins estate a maintenance project. We migrate clients away from it; we don't build new ones.

## When to use it — and when not?

- **Use** only while maintaining or migrating an existing client installation.
- **Don't** set up new Jenkins instances.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://www.jenkins.io/
