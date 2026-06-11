# Pexon AI Engineering Stack

> End-to-end reference architecture and infrastructure codebase for the Pexon Technology Stack —
> 6 architecture layers, 7 clusters, 20 components. Microsoft Partner · ISO 27001 · Hosting DE/EU.

---

## Table of contents

- [Overview](#overview)
- [Repository structure](#repository-structure)
- [Architecture layers](#architecture-layers)
  - [Layer 1 — Foundation Models & AI Backbone](#layer-1--foundation-models--ai-backbone)
  - [Layer 2 — Cloud & Compute Foundation](#layer-2--cloud--compute-foundation)
  - [Layer 3 — Platform Engineering](#layer-3--platform-engineering)
  - [Layer 4 — Data Platform & Knowledge Layer](#layer-4--data-platform--knowledge-layer)
  - [Layer 5 — AI Agent Hub & MCP Registry](#layer-5--ai-agent-hub--mcp-registry)
  - [Layer 6 — Custom AI Engineering & Applications](#layer-6--custom-ai-engineering--applications)
- [Cross-cutting: Security & Governance](#cross-cutting-security--governance)
- [Shared infrastructure](#shared-infrastructure)
- [Cluster leads & ownership](#cluster-leads--ownership)
- [Getting started](#getting-started)
- [Contributing](#contributing)
- [Internal documentation](#internal-documentation)
- [Compliance & certifications](#compliance--certifications)

---

## Overview

The **Pexon AI Engineering Stack** is a production-proven reference architecture for enterprise AI deployments.
This repository contains the infrastructure code, Helm charts, pipeline templates, and documentation
that implement all six architecture layers — from Foundation Model hosting to customer-facing AI applications.

```
Layer 6  │  Custom AI Engineering & Applications
Layer 5  │  AI Agent Hub & MCP Registry
Layer 4  │  Data Platform & Knowledge Layer
Layer 3  │  Platform Engineering
Layer 2  │  Cloud & Compute Foundation
Layer 1  │  Foundation Models & AI Backbone
─────────┼───────────────────────────────────────
         │  Security & Governance  (cross-cutting)
```

Public stack overview: <https://pexon-consulting.de/ki-beratung/ai-engineering-stack/>

---

## Repository structure

```
pexon-ai-engineering-stack/
│
├── layer-1-foundation-models/      # GPT, Claude, Mistral, vLLM, SGLang
├── layer-2-cloud-foundation/       # Azure, AWS, Sovereign Cloud, On-Prem GPU
├── layer-3-platform-engineering/   # IDP, Kubernetes, AI Platform / MLOps
├── layer-4-data-platform/          # Vector DB, ETL, MCP integration, Lakehouse
├── layer-5-orchestration/          # Agent Hub, MCP Registry
├── layer-6-applications/           # RAG apps, workflows, Document Intelligence
│
├── security-governance/            # RBAC, Entra ID, compliance (cross-cutting)
├── infrastructure/                 # Shared Terraform modules, Helm charts, CI/CD
│
├── _internal/                      # 🔒 Internal only — see access policy below
│   ├── cluster-leads/
│   ├── pricing/
│   ├── client-cases/
│   ├── runbooks/
│   ├── adr/
│   └── roadmap/
│
├── .github/                        # PR templates, issue forms, Actions workflows
│   └── CODEOWNERS                  # Folder → cluster lead mapping
├── ARCHITECTURE.md                 # Full 6-layer diagram + ADR index
├── CONTRIBUTING.md
└── README.md                       # This file
```

---

## Architecture layers

### Layer 1 — Foundation Models & AI Backbone

**Folder:** `layer-1-foundation-models/`  
**Cluster leads:** Fabian Mirz (Local AI) · Robin Werner (Azure AI Foundry) · Alexander Laaser (AWS Bedrock)

| Component | Path | Owner |
|---|---|---|
| Azure AI Foundry | `azure-ai-foundry/` | Robin Werner |
| AWS Bedrock | `aws-bedrock/` | Alexander Laaser |
| Local AI | `local-ai/` | Fabian Mirz |

**When to use this layer:** Any use case requiring model hosting — cloud-managed (Azure, AWS) or fully on-premises (NVIDIA H100/A100, AMD MI300X) for data-sovereignty-critical deployments.

**General knowledge** — maintained openly, suitable for onboarding and client discussions:

- Model provider comparison: GPT vs Claude vs Mistral vs Llama — capability, latency, cost trade-offs
- When to use cloud-managed hosting vs local inference (data sovereignty, cost at scale, latency requirements)
- GPU memory sizing guide for common model sizes (7B, 13B, 70B) and quantisation options (GPTQ, AWQ, fp8)
- Links to official Azure AI Foundry, AWS Bedrock, and vLLM/SGLang documentation

**Internal / company-specific** — restricted to `@pexon-consulting/internal`, owned by the respective cluster lead:

- Pexon-preferred model defaults per use-case type (RAG, summarisation, extraction, code) and approved version list
- Tested Terraform / Bicep modules for Azure AI Foundry with Pexon naming conventions and compliance guardrails
- vLLM and SGLang Helm charts validated in production (Deutz, Yokogawa GPU cluster configs)
- H100/A100/MI300X node affinity rules, tested NVIDIA driver and CUDA version matrix
- Known issues and workarounds per client environment type

---

### Layer 2 — Cloud & Compute Foundation

**Folder:** `layer-2-cloud-foundation/`  
**Cluster leads:** Robin Werner (Azure) · Alexander Laaser (AWS) · Patricia Berger (Sovereign Cloud) · Fabian Mirz (On-Prem GPU)

| Component | Path | Owner |
|---|---|---|
| Azure Landing Zone | `azure-landing-zone/` | Robin Werner |
| AWS Landing Zone | `aws-landing-zone/` | Alexander Laaser |
| Sovereign Cloud | `sovereign-cloud/` | Patricia Berger |
| On-Prem GPU Infrastructure | `on-prem-gpu/` | Fabian Mirz |

**General knowledge** — maintained openly:

- Azure Cloud Adoption Framework landing zone concepts; hub-spoke networking patterns; Azure Policy best practices
- AWS Control Tower multi-account strategy; GPU quota request process; compliance guardrail design
- US Cloud Act explainer; when to choose Sovereign Cloud (STACKIT, OTC) over hyperscaler for KRITIS and banking
- H100 vs A100 vs MI300X specification comparison; InfiniBand vs Ethernet for GPU clusters

**Internal / company-specific** — restricted to `@pexon-consulting/internal`, owned by the respective cluster lead:

- Pexon baseline Policy-as-Code set; approved VM/instance SKUs for AI workloads; Bicep modules with Pexon naming conventions
- STACKIT org IDs and project templates; OTC configs validated for KRITIS clients; AVV (data processing agreement) templates for sovereign setups
- Pexon GPU cluster bill of materials (BOM); client network topology templates (anonymised); IPAM allocation strategy

---

### Layer 3 — Platform Engineering

**Folder:** `layer-3-platform-engineering/`  
**Cluster leads:** Alexander Laaser (IDP, AI Platform) · Felix Notka (Kubernetes)

| Component | Path | Owner |
|---|---|---|
| Internal Developer Platform | `idp/` | Alexander Laaser |
| Kubernetes & Managed K8s | `kubernetes/` | Felix Notka |
| AI Platform Engineering | `ai-platform/` | Alexander Laaser |

**General knowledge** — maintained openly:

- IDP concepts; Backstage vs Port comparison; Crossplane provider patterns and golden path template design
- EKS vs AKS vs GKE decision matrix; ArgoCD GitOps patterns; GPU node pool sizing guide
- MLOps maturity model; LiteLLM gateway concepts; model serving trade-offs (batch vs streaming vs serverless)

**Internal / company-specific** — restricted to `@pexon-consulting/internal`, owned by the respective cluster lead:

- Pexon Backstage plugin list and Port catalog schema; Crossplane compositions used in IDP rollouts (E.ON, EnBW patterns, anonymised)
- Pexon base Helm chart values; cluster hardening checklist; validated K8s versions per cloud provider; NIS-2 / BSI C5 node configs
- Pexon LiteLLM gateway config with RBAC and cost tracking; tested inference benchmarks per model/GPU combination; production MLOps pipeline templates

---

### Layer 4 — Data Platform & Knowledge Layer

**Folder:** `layer-4-data-platform/`  
**Cluster lead:** Patricia Berger

| Component | Path | Owner |
|---|---|---|
| Vector DB | `vector-db/` | Patricia Berger |
| Enterprise Data | `enterprise-data/` | Patricia Berger |
| ETL & Pipelines | `etl-pipelines/` | Patricia Berger |
| MCP Integration | `mcp-integration/` | Patricia Berger |
| Data Platform | `data-platform/` | Patricia Berger |

**General knowledge** — maintained openly:

- Vector DB comparison: Qdrant vs Pinecone vs Weaviate vs pgvector — trade-offs for enterprise RAG
- Embedding model selection guide; chunking strategies by document type; hybrid search patterns
- Airflow DAG design for AI pipelines; dbt for LLM data preparation; Databricks job templates
- MCP protocol spec overview; tool-interface design patterns; when MCP vs direct API integration
- Microsoft Fabric vs Snowflake vs Lakehouse architecture decision criteria

**Internal / company-specific** — restricted to `@pexon-consulting/internal`, owned by Patricia Berger:

- Pexon multi-tenant Vector DB RBAC schema (used in DAX 1.2M-document RAG project); tested embedding models per language and domain
- Reusable Airflow DAGs for SAP/CRM/ERP extraction; Pexon dbt macros; Confluence + SharePoint ingestion templates
- Pexon MCP tool schemas for SAP, CRM, and ERP connectors; tested MCP server implementations; client-approved tool registries per compliance tier

---

### Layer 5 — AI Agent Hub & MCP Registry

**Folder:** `layer-5-orchestration/`  
**Cluster lead:** Patricia Berger

| Component | Path | Owner |
|---|---|---|
| AI Agent Hub | `agent-hub/` | Patricia Berger |
| MCP Registry | `mcp-registry/` | Patricia Berger |

**General knowledge** — maintained openly:

- Agent routing patterns; lifecycle management concepts; multi-agent orchestration frameworks compared (LangGraph, AutoGen, CrewAI)
- MCP tool discovery concepts; registry governance patterns; tool versioning and deprecation strategies
- Audit logging design for EU AI Act traceability requirements

**Internal / company-specific** — restricted to `@pexon-consulting/internal`, owned by Patricia Berger:

- Pexon Agent Hub routing engine configuration; audit log schema used for EU AI Act traceability; tested agent topologies per use-case type
- Pexon tool catalog schema; approved tool list per compliance tier (KRITIS vs standard); governance checklist before tool onboarding

---

### Layer 6 — Custom AI Engineering & Applications

**Folder:** `layer-6-applications/`  
**Cluster leads:** Constantin Budin (Custom AI, Workflows, Departmental Apps) · Max Hennig (Document Intelligence)

| Component | Path | Owner |
|---|---|---|
| Custom AI Engineering | `custom-ai-engineering/` | Constantin Budin |
| AI Workflows & Automation | `ai-workflows/` | Constantin Budin |
| Departmental Apps | `departmental-apps/` | Constantin Budin |
| Document Intelligence | `document-intelligence/` | Max Hennig |

**General knowledge** — maintained openly:

- RAG architecture patterns; evaluation metrics (RAGAS, BLEU, LLM-as-judge); retrieval pipeline design
- Chatbot and voice bot UX best practices; enterprise-grade conversation management
- VLM model selection guide; OCR pipeline architecture; document classification patterns
- Agent workflow design; human-in-the-loop concepts; process automation evaluation criteria

**Internal / company-specific** — restricted to `@pexon-consulting/internal`, owned by the respective cluster lead:

- Pexon RAG scaffold: multi-tenant, RBAC-aware, DSGVO-compliant; tested prompt templates per domain (banking, insurance, energy)
- Pexon invoice processing pipeline achieving 98% OCR accuracy, BaFin/MaRisk-compliant (Atruvia / banking anonymised config)
- Reusable workflow templates for HR, procurement, and service desk use cases; tested orchestration configs per tool combination
- App scaffolds for departmental use cases with role-based data access baked in

---

## Cross-cutting: Security & Governance

**Folder:** `security-governance/`

Security and compliance are built into every layer — not bolted on afterwards.
This folder contains the shared policies and schemas that all layers consume.

```
security-governance/
├── rbac/           # Role definitions for data, models, and tools across all layers
├── identity/       # Entra ID / SSO, MFA, Conditional Access policies
├── compliance/     # EU AI Act risk classification templates, DSGVO, NIS2, BSI C5
└── audit/          # Log schemas, SIEM integration configs
```

**Compliance standards covered:**

| Standard | Scope |
|---|---|
| EU AI Act (2024/1689) | Risk classification per use case (prohibited / high / limited / minimal) |
| DSGVO / GDPR | Data processing agreements, deletion concepts, data residency |
| ISO 27001 | Pexon-certified; controls mapped to stack components |
| NIS2 | For KRITIS customers (energy, finance, healthcare) |
| BSI C5 | Cloud architecture attestation |
| IEC 62443 | Industrial & manufacturing use cases |
| BaFin / MaRisk / DORA | Banking and financial services deployments |

---

## Shared infrastructure

**Folder:** `infrastructure/`

```
infrastructure/
├── terraform/
│   └── modules/    # Reusable IaC modules shared across Layers 1–3
├── helm-charts/    # Shared Kubernetes chart library
└── ci-cd/          # GitHub Actions reusable workflows (lint, test, deploy)
```

All Terraform modules follow the [standard module structure](https://developer.hashicorp.com/terraform/language/modules/develop/structure).
Helm charts target Kubernetes 1.28+.

---

## Cluster leads & ownership

Seven dedicated tech leads with pre-sales, delivery, and hiring responsibility.
See `CODEOWNERS` for the full folder-to-person mapping.

| Cluster | Lead | Primary folders |
|---|---|---|
| Private AI & Local AI | Fabian Mirz | `layer-1/local-ai`, `layer-2/on-prem-gpu` |
| Enterprise AI & Chatbots | Constantin Budin | `layer-6/custom-ai-engineering`, `layer-6/ai-workflows` |
| MCP, Data Engineering & KI Integration | Patricia Berger | `layer-4`, `layer-5`, `layer-2/sovereign-cloud` |
| Document Intelligence | Max Hennig | `layer-6/document-intelligence` |
| Platform Engineering & IDP | Alexander Laaser | `layer-3/idp`, `layer-3/ai-platform`, `layer-2/aws-landing-zone` |
| Kubernetes & Managed Kubernetes | Felix Notka | `layer-3/kubernetes` |
| Azure | Robin Werner | `layer-2/azure-landing-zone`, `layer-1/azure-ai-foundry` |

---

## Getting started

### Prerequisites

- Terraform >= 1.7
- Helm >= 3.14
- kubectl >= 1.28
- Python >= 3.11 (for MLOps pipeline tooling)
- Access to at least one cloud account (Azure, AWS, or on-prem GPU cluster)

### Quick start (Layer 1 — Azure AI Foundry)

```bash
git clone https://github.com/pexon-consulting/pexon-ai-engineering-stack.git
cd pexon-ai-engineering-stack/layer-1-foundation-models/azure-ai-foundry

cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your subscription ID, resource group, and model selections

terraform init
terraform plan
terraform apply
```

Each layer folder contains its own `README.md` with layer-specific prerequisites and deployment steps.

---

## Contributing

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) before opening a pull request.

Key points:

- Every PR must be reviewed by the responsible cluster lead (enforced via `CODEOWNERS`).
- Infrastructure changes to Layers 1–3 require a passing `terraform plan` output attached to the PR.
- All new components need an entry in `ARCHITECTURE.md` and, if architectural, a new ADR in `_internal/adr/`.
- Security-relevant changes (anything touching `security-governance/`) require a second review from the compliance owner.

**General vs. internal content rule:** When adding documentation, ask yourself: could this appear in a client workshop or a public blog post without concern? If yes, it belongs in the layer folder's `README.md` or a `docs/` subfolder. If it contains client-specific configs, pricing signals, internal tooling details, or anything under NDA — it belongs in `_internal/` instead. When in doubt, ask your cluster lead.

---

## Internal documentation

The `_internal/` folder is restricted to Pexon team members.

```
_internal/
├── cluster-leads/    # Contact details, responsibilities, escalation paths
├── pricing/          # Rate cards (1,100–1,600 EUR/day), TCO models, engagement templates
├── client-cases/     # Anonymised case notes, NDA references, outcome metrics
├── runbooks/         # Ops playbooks per layer (incident response, scaling, rollback)
├── adr/              # Full Architecture Decision Records with context and trade-offs
└── roadmap/          # Quarterly stack evolution plans, upcoming cluster priorities
```

Access is controlled via the `@pexon-consulting/internal` GitHub team.
If you need access, contact your cluster lead or open a request in the internal Slack channel `#stack-repo-access`.

> **Note:** Client-specific repositories and NDA-protected artefacts are never stored here.
> They live in dedicated client workspaces. `_internal/client-cases/` contains only sanitised summaries.

---

## Compliance & certifications

| | |
|---|---|
| **ISO 27001** | Pexon Consulting GmbH certified |
| **Data residency** | Default: DE/EU (Azure Germany West Central, AWS Frankfurt) |
| **Sovereign option** | STACKIT, Open Telekom Cloud — US Cloud Act-free |
| **On-prem option** | Full data sovereignty; no hyperscaler dependency |
| **Model training** | Inputs/outputs contractually excluded from model training on Azure OpenAI, AWS Bedrock, GCP Vertex |

---

*Stack version: 2026-05 · Maintained by the Pexon Engineering team · [pexon-consulting.de](https://pexon-consulting.de)*
