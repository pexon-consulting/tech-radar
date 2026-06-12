---
name: OpenAI Agents SDK
layer: 5-orchestration
ring: assess
tags: [agents, openai, sdk]
champions: []
since: 2026-06
ring_history:
  - { ring: assess, date: 2026-06, reason: "Added from leadership stack proposal — agentic option for Azure-OpenAI-committed clients" }
---

## What is it?

OpenAI's lightweight agent framework — agents, handoffs and guardrails as first-class primitives, usable against Azure OpenAI endpoints.

## Why this ring?

Proposed as the agentic option where the client is committed to OpenAI/Azure-OpenAI models anyway. Assess: it competes directly with LangGraph (our Adopt) and PydanticAI in the same slot — needs a comparison on a real use case before earning a lane.

## When to use it — and when not?

- **Use** in evaluations on OpenAI-committed stacks where its built-in handoff/guardrail model fits the use case.
- **Don't** pick it for model-agnostic builds — its strength is coupling to the OpenAI ecosystem, which is also its limitation.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://github.com/openai/openai-agents-python
