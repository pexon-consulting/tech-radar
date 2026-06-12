---
name: Docling
layer: 4-data-knowledge
ring: trial
tags: [document-parsing, pdf, rag-ingestion]
champions: []
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Radar expansion — document parsing for RAG ingestion pipelines" }
---

## What is it?

Open-source document conversion (IBM Research): PDFs, Office files and scans into structured Markdown/JSON — layout, tables and reading order preserved. The quality of RAG starts here.

## Why this ring?

Ingestion quality is the most underrated lever in RAG projects; Docling is our current pick for the parsing stage and feeds clean structure into chunking.

## When to use it — and when not?

- **Use** at the start of every document-heavy RAG/document-intelligence pipeline.
- **Don't** rely on it alone for handwriting or exotic scans — combine with a VLM pass.

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://github.com/docling-project/docling
