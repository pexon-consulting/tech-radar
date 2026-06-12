---
name: Azure Logic Apps
layer: 5-orchestration
ring: assess
tags: [workflow-automation, azure, low-code, integration]
champions: []
since: 2026-06
ring_history:
  - { ring: assess, date: 2026-06, reason: "Added from leadership stack proposal — Azure-native workflow option next to n8n and Power Automate" }
---

## What is it?

Azure's managed integration and workflow service — connector-based automation that lives inside the client's Azure governance (networking, IAM, policy) rather than in a separate tool.

## Why this ring?

The Azure-native answer in our workflow lineup (n8n self-hosted, Power Automate for M365 land, Logic Apps for Azure-platform integration). Assess: we need clearer internal guidance on when it beats the other two.

## When to use it — and when not?

- **Use** for integration workflows that must live under Azure governance and connect Azure services.
- **Don't** use it for department-level automation M365 users own themselves (→ Power Automate) or where self-hosting is required (→ n8n).

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://learn.microsoft.com/azure/logic-apps/
