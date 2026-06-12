---
name: GitLab CI/CD
layer: 3-platform-engineering
ring: adopt
tags: [ci-cd, gitlab, self-hosted, automation]
champions: []
since: 2026-06
ring_history:
  - { ring: adopt, date: 2026-06, reason: "Gap fix — named as the recommended Jenkins alternative, CI default in GitLab estates" }
---

## What is it?

GitLab's integrated CI/CD — pipelines as code with self-hosted runners, available fully on-prem via self-managed GitLab.

## Why this ring?

Our CI default in GitLab-based client estates — common in enterprises and the public sector, where self-managed GitLab covers data-residency requirements that GitHub's cloud cannot. Named as the recommended migration target in the Jenkins Hold entry.

## When to use it — and when not?

- **Use** wherever the client runs GitLab, especially self-managed/on-prem; pair with Argo CD for K8s delivery.
- **Don't** introduce GitLab just for CI in a GitHub organization (→ GitHub Actions).

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://docs.gitlab.com/ee/ci/
