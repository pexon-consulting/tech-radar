---
name: GitHub Actions
layer: 3-platform-engineering
ring: adopt
tags: [ci-cd, github, automation]
champions: []
since: 2026-06
ring_history:
  - { ring: adopt, date: 2026-06, reason: "Gap fix — named as the recommended Jenkins alternative, our CI default on GitHub" }
---

## What is it?

GitHub's integrated CI/CD — workflows as YAML next to the code, with a huge marketplace of reusable actions and managed runners.

## Why this ring?

Our CI default wherever the code lives on GitHub (including this radar's own validate-and-deploy pipeline). Named as the recommended migration target in the Jenkins Hold entry.

## When to use it — and when not?

- **Use** as the default for build/test/deploy pipelines on GitHub-hosted repos; pair with Argo CD for GitOps-style K8s delivery (CI builds, Argo deploys).
- **Don't** run heavy, long-lived deployment logic in it on K8s platforms — that belongs to Argo CD.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://docs.github.com/actions
