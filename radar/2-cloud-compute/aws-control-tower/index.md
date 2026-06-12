---
name: AWS Control Tower (Multi-Account)
layer: 2-cloud-compute
ring: adopt
tags: [aws, landing-zone, multi-account, governance]
champions: []
since: 2026-06
ring_history:
  - { ring: adopt, date: 2026-06, reason: "Initial radar import — Pexon default per stack documentation" }
certifications:
  - { name: "AWS Certified Solutions Architect — Associate", issuer: "AWS", holders: [] }
  - { name: "AWS Certified Solutions Architect — Professional", issuer: "AWS", holders: [] }
references:
  - { client: "MyToys", title: "AWS-Landing-Zone-Professionalisierung", url: "https://pexon-consulting.de/casestudie/case-study-mytoys-aws-landing-zone/", public: true }
  - { client: "Atos", title: "AWS-Multi-Account-Architektur für sicherheitskritische Energie-Applikation", url: "https://pexon-consulting.de/casestudie/atos-2/", public: true }
---

## What is it?

AWS's managed service for setting up and governing a multi-account environment: account vending, guardrails, centralized logging.

## Why this ring?

Our default AWS foundation. For AI workloads we add GPU quota management and account separation for model-serving workloads.

## When to use it — and when not?

- **Use** for AWS-native clients without an existing multi-account strategy.
- **Don't use** for clients with a mature, customized organizations setup — work within it.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://docs.aws.amazon.com/controltower/
