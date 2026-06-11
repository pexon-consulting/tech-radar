# Layer 6 — Custom AI Engineering & Applications

> The user-facing layer. Contains the scaffolds, pipelines, and app templates that
> deliver value to end users and client departments. Everything in Layers 1–5 exists
> to support what is built and deployed here.

---

## Cluster leads

| Scope | Lead | Contact |
|---|---|---|
| Custom AI Engineering | Constantin Budin | `@constantin-budin` |
| AI Workflows & Automation | Constantin Budin | `@constantin-budin` |
| Departmental Apps | Constantin Budin | `@constantin-budin` |
| Document Intelligence | Max Hennig | `@max-hennig` |

PRs are reviewed and merged by the responsible lead per subfolder,
as defined in [`CODEOWNERS`](../../.github/CODEOWNERS).

---

## Components

| Component | Path | Owner |
|---|---|---|
| Custom AI Engineering | `custom-ai-engineering/` | Constantin Budin |
| AI Workflows & Automation | `ai-workflows/` | Constantin Budin |
| Departmental Apps | `departmental-apps/` | Constantin Budin |
| Document Intelligence | `document-intelligence/` | Max Hennig |

---

## When to use this layer

| Client need | Component |
|---|---|
| "We want a chatbot that knows our internal documents" | Custom AI Engineering — RAG scaffold |
| "We want a voice assistant for our service desk" | Custom AI Engineering — voice bot template |
| "We want to automate our invoice approval process" | AI Workflows — process automation |
| "Our HR team needs an AI assistant" | Departmental Apps — HR scaffold |
| "We need to extract data from 10,000 contracts" | Document Intelligence — extraction pipeline |
| "We want to classify and route incoming documents" | Document Intelligence — classification pipeline |

---

## General knowledge

### RAG application architecture

A production RAG application has more moving parts than a prototype:

```
User query
  → Query rewriting / expansion          (improves retrieval recall)
  → Hybrid retrieval (dense + sparse)    (vector search + keyword search)
  → Re-ranking                           (cross-encoder to sort results)
  → Context assembly                     (chunk selection, metadata, citations)
  → Generation                           (LLM with assembled context)
  → Response with source attribution     (trust and verifiability)
```

**Evaluation framework (RAGAS metrics):**

| Metric | What it measures |
|---|---|
| Faithfulness | Does the answer stick to the retrieved context? |
| Answer relevancy | Is the answer relevant to the question? |
| Context precision | Are the retrieved chunks actually useful? |
| Context recall | Were all relevant chunks retrieved? |
| Answer correctness | Is the answer factually correct? (requires ground truth) |

Reference: [RAGAS documentation](https://docs.ragas.io/)

### Voice bot architecture

A production voice bot pipeline:

```
Audio input
  → Speech-to-text (STT)         (Azure Speech, Whisper, Deepgram)
  → Intent / entity extraction   (LLM or classifier)
  → Agent Hub invocation         (Layer 5)
  → Response generation          (LLM)
  → Text-to-speech (TTS)         (Azure Speech, ElevenLabs, Kokoro)
  → Audio output
```

Key latency budget: end-to-end < 2s for acceptable UX. STT and TTS each take ~300–500ms;
the remaining budget goes to model inference and retrieval.

### AI workflow / process automation

AI workflows differ from RPA in that they handle unstructured inputs and exceptions
rather than executing deterministic steps. Key design decisions:

- **Human-in-the-loop triggers** — define when the agent escalates vs. acts autonomously
  (cost threshold, confidence score, document type, regulatory sensitivity)
- **Idempotency** — workflows that write to external systems must handle retries safely
- **Observability** — every workflow invocation should produce a trace linkable to the
  business process record (invoice ID, ticket number, etc.)
- **Rollback** — for write actions, define compensating transactions

### Document Intelligence

Document Intelligence handles the full lifecycle from raw document to structured data:

```
Raw document (PDF, image, scan, email)
  → Pre-processing (deskew, denoise, format normalisation)
  → Layout analysis (VLM or layout model: tables, headers, fields)
  → OCR / text extraction
  → Entity extraction (LLM-based: amounts, dates, names, codes)
  → Validation (business rules, cross-field consistency)
  → Output to target system
```

**VLM model selection for document tasks:**

| Model | Strengths | Notes |
|---|---|---|
| GPT-4o (vision) | Strong table understanding, multilingual | Per-token cost; cloud only |
| Claude 3.x (vision) | Long document context, careful extraction | Per-token cost; cloud only |
| Qwen2-VL | Strong OCR, multilingual, open weights | Self-hostable; good for DE docs |
| PaddleOCR | Lightweight, high-accuracy traditional OCR | Best for text-heavy, low-layout docs |
| Docling (IBM) | PDF layout parsing, open source | Good pre-processor before LLM extraction |

---

## Internal / company-specific

> **Access:** Content described here lives in `_internal/layer-6/` and is restricted
> to `@pexon-consulting/internal`. Request access via `#stack-repo-access`.

### What is stored internally

**Custom AI Engineering (`_internal/layer-6/custom-ai-engineering/`)**  
Maintained by Constantin Budin

- Pexon RAG scaffold: multi-tenant, RBAC-aware, DSGVO-compliant, with citation rendering
- Tested prompt templates per domain (German legal, Banking compliance, Technical documentation)
- Evaluation suite with domain-specific test sets (RAGAS + custom metrics)
- Voice bot integration configs: Azure Speech + LiteLLM gateway patterns
- Reusable frontend components for chat interfaces (React, white-label ready)

**AI Workflows (`_internal/layer-6/ai-workflows/`)**  
Maintained by Constantin Budin

- Workflow templates: invoice processing, procurement approval, HR onboarding automation
- Human-in-the-loop trigger thresholds validated in production (Banking, Manufacturing)
- Tested orchestration configs per tool combination (LangGraph + MCP + SAP connector)
- SLA baseline data: processing times per document type and workflow complexity

**Departmental Apps (`_internal/layer-6/departmental-apps/`)**  
Maintained by Constantin Budin

- HR assistant scaffold with role-based data access (HR vs employee vs manager view)
- Sales enablement assistant scaffold (CRM-integrated, DSGVO-aware)
- Service desk assistant scaffold with ticket system integration
- Approval workflow templates per department type

**Document Intelligence (`_internal/layer-6/document-intelligence/`)**  
Maintained by Max Hennig

- Pexon invoice processing pipeline: 98% OCR accuracy, BaFin / MaRisk compliant
  (developed for Atruvia ecosystem, fully anonymised)
- Contract analysis pipeline: clause extraction, obligation tracking, risk flagging
- VLM config benchmarks per document type (invoices, contracts, technical drawings)
- Validation rule templates per document type and sector (Banking, Energy, Insurance)
- Anonymised accuracy benchmarks from production deployments

### Maintenance schedule

| Artefact | Review frequency | Owner |
|---|---|---|
| RAG scaffold | Per major LangChain / LlamaIndex release | Constantin Budin |
| Prompt template library | Quarterly + post-engagement learnings | Constantin Budin |
| Document Intelligence benchmarks | Per new VLM release | Max Hennig |
| Invoice pipeline compliance config | Per BaFin / MaRisk guidance update | Max Hennig |
| Workflow SLA baselines | Post each new production deployment | Constantin Budin |

---

## Prerequisites

### Custom AI Engineering (RAG)

- LiteLLM gateway running (Layer 3)
- Vector DB deployed and populated (Layer 4)
- Agent Hub available for multi-step queries (Layer 5)
- Python >= 3.11 or Node.js >= 20 depending on scaffold variant
- Frontend: Node.js >= 20, React >= 18

### Document Intelligence

- Python >= 3.11
- Model endpoint with vision capability (GPT-4o or Claude 3+ via Layer 1)
- Object storage for input documents and pipeline state (Azure Blob / S3)
- Target system API credentials (ERP, DMS, or database)

### AI Workflows

- Agent Hub deployed (Layer 5)
- MCP tools for target systems registered in MCP Registry (Layer 5)
- Workflow orchestration framework installed (LangGraph recommended; see `ai-workflows/`)

---

## Quick start

### RAG chatbot scaffold

```bash
cd layer-6-applications/custom-ai-engineering/rag-scaffold

cp .env.example .env
# Configure: LITELLM_URL, QDRANT_URL, EMBEDDING_MODEL, LLM_MODEL

pip install -r requirements.txt

# Index your documents
python scripts/ingest.py --source ./docs --collection my-knowledge-base

# Start the API
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Start the frontend (optional)
cd frontend && npm install && npm run dev
```

### Document extraction pipeline

```bash
cd layer-6-applications/document-intelligence

cp config/pipeline.yaml.example config/pipeline.yaml
# Configure: input_storage, output_target, model_endpoint, document_type

pip install -r requirements.txt

# Run on a single document (test)
python run_pipeline.py --doc sample/invoice_sample.pdf --dry-run

# Deploy as a Kubernetes Job
kubectl apply -f k8s/pipeline-job.yaml
```

### Departmental app (HR assistant)

```bash
cd layer-6-applications/departmental-apps/hr-assistant

cp .env.example .env
# Configure: AGENT_HUB_URL, HR_SYSTEM_MCP_TOOL, AUTH_PROVIDER

docker compose up
# App available at http://localhost:3000
```

---

## Related layers

- **Layer 1** (`layer-1-foundation-models/`) — model endpoints that power
  all AI generation in this layer
- **Layer 3** (`layer-3-platform-engineering/ai-platform/`) — LiteLLM gateway
  that all model calls in this layer route through
- **Layer 4** (`layer-4-data-platform/`) — vector stores and enterprise data
  connectors that ground AI responses in company knowledge
- **Layer 5** (`layer-5-orchestration/`) — Agent Hub and MCP Registry that
  orchestrate multi-step workflows and provide governed tool access

---

*Layer owners: Constantin Budin · Max Hennig · Last reviewed: 2026-05*
