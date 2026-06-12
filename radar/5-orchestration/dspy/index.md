---
name: DSPy
layer: 5-orchestration
ring: assess
tags: [prompt-optimization, llm-pipelines, python]
champions: []
since: 2026-06
ring_history:
  - { ring: assess, date: 2026-06, reason: "Added from blog coverage — May 2026 post, no radar entry yet" }
articles:
  - { title: "RAG Pipelines mit DSPy statt LangChain: Messbar bessere Antworten", url: "https://pexon-consulting.de/blog/rag-pipelines-dspy-langchain-vergleich/", date: 2026-05 }
---

## What is it?

Framework (Stanford) that treats prompts as optimizable programs: declare the pipeline, let DSPy compile and optimize prompts/few-shots against a metric instead of hand-tuning them.

## Why this ring?

The "measure instead of guess" approach fits our eval-driven delivery style (RAGAS, Langfuse); we are assessing whether the optimization gains survive contact with messy client data.

## When to use it — and when not?

- **Use** in PoCs where answer quality is measurable and prompt hand-tuning has plateaued.
- **Don't** introduce it where there's no eval metric yet — optimize against nothing and you get nothing.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://dspy.ai/
