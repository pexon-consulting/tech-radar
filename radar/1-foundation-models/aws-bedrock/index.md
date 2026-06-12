---
name: AWS Bedrock
layer: 1-foundation-models
ring: adopt
tags: [aws, model-hosting, inference, anthropic]
champions: []
since: 2026-06
ring_history:
  - { ring: adopt, date: 2026-06, reason: "Initial radar import — Pexon default per stack documentation" }
certifications:
  - { name: "AWS Certified AI Practitioner", issuer: "AWS", holders: [] }
  - { name: "AWS Certified Machine Learning — Specialty", issuer: "AWS", holders: [] }
---

## What is it?

AWS's managed service for foundation models (Anthropic Claude, Meta Llama, Amazon Titan and others) behind a single API, with IAM-based access control and VPC integration.

## Why this ring?

Our default model platform for AWS-native client setups.

## When to use it — and when not?

- **Use** for AWS-native clients, especially when Claude models are required inside the client's AWS perimeter.
- **Don't use** for sovereign/on-prem requirements (→ vLLM/SGLang) or Azure-first clients (→ Azure AI Foundry).

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

- Document per project: model choice rationale, context window requirements, hosting region, zero-data-retention config.

## Resources

- Official docs: https://docs.aws.amazon.com/bedrock/
