# Pexon AI Engineering Stack — Knowledge Repository

Internal knowledge base for AI engineering at Pexon, structured around our 6-layer reference architecture. This repo is the starting point for shared know-how across projects — add what you learn, link what you use.

> **Contribute:** Open a PR against the relevant layer folder. Short, opinionated, and practical beats comprehensive and theoretical.

---

## Architecture Overview

```
Layer 6 │ Custom AI Engineering & Applications
Layer 5 │ AI Agent Hub & MCP Registry
Layer 4 │ Data Platform & Knowledge Layer
Layer 3 │ Platform Engineering
Layer 2 │ Cloud & Compute Foundation
Layer 1 │ Foundation Models & AI Backbone
─────────────────────────────────────────────
          Security & Governance  (cross-cutting)
```

Full stack description: [pexon-consulting.de/ki-beratung/ai-engineering-stack](https://pexon-consulting.de/ki-beratung/ai-engineering-stack/)

---

## Layer 1 — Foundation Models & AI Backbone

**What lives here:** Model hosting, inference endpoints, model selection, local AI setup.

**Pexon defaults:**
- Azure AI Foundry (GPT, Claude, Mistral) — primary for Azure-based clients
- AWS Bedrock (Anthropic, Meta, Titan) — for AWS-native setups
- vLLM / SGLang on GPU cluster — for sovereign/on-prem requirements

**Key decisions to document per project:** model choice rationale, context window requirements, hosting region, zero-data-retention config.

---

## Layer 2 — Cloud & Compute Foundation

**What lives here:** Landing zones, GPU infrastructure, sovereign cloud, networking and security baselines.

**Pexon defaults:**
- Azure Landing Zone with Policy-as-Code for AI workloads
- AWS multi-account with Control Tower and GPU quotas
- Sovereign alternatives: STACKIT, Open Telekom Cloud (US-Cloud-Act-free)
- On-prem GPU: NVIDIA H100/A100, AMD MI300X

---

## Layer 3 — Platform Engineering

**What lives here:** MLOps, model serving, internal developer platforms, Kubernetes.

**Pexon defaults:**
- IDP: Backstage / Port + Crossplane
- K8s: EKS, AKS, GKE, OpenShift with GPU node pools
- MLOps: MLflow for experiment tracking, model registry, artifact storage
- AI Platform: LiteLLM gateway, GPU scheduling, inference optimization

**Tools:**

### MLflow
[github.com/mlflow/mlflow](https://github.com/mlflow/mlflow)
Open source platform for the full ML lifecycle: experiment tracking, model registry, serving. Use as the central MLOps backbone across projects. Pairs well with Azure ML and SageMaker as managed alternatives.

**At Pexon:** Deploy on Kubernetes. Use the model registry as source of truth for promoted models. Track evals and fine-tuning runs as experiments.

### gstack
[github.com/garrytan/gstack](https://github.com/garrytan/gstack)
Opinionated Claude Code setup with 23 tools configured for AI engineering workflows. Useful reference for standardizing local AI dev environments across the team.

**At Pexon:** Use as a starting point for onboarding engineers into Claude Code-based workflows. Adapt the tool selection to project context.

---

## Layer 4 — Data Platform & Knowledge Layer

**What lives here:** Vector DBs, ETL pipelines, enterprise data connectors, knowledge retrieval, MCP data integrations.

**Pexon defaults:**
- Vector DB: Qdrant (preferred for sovereign setups), Weaviate, Postgres pgvector
- Data platforms: Microsoft Fabric, Snowflake, Databricks/dbt
- Enterprise connectors: SAP, CRM, ERP, Confluence, SharePoint

**Tools:**

### qmd
[github.com/tobi/qmd](https://github.com/tobi/qmd)
Lightweight CLI search engine for local docs, knowledge bases, and meeting notes using embeddings. Good for quickly adding semantic search to a project's internal documentation or during a pilot before a full Vector DB setup is warranted.

**At Pexon:** Useful for prototyping retrieval on small corpora. Not a production replacement for Qdrant/pgvector.

---

## Layer 5 — AI Agent Hub & MCP Registry

**What lives here:** Agent lifecycle management, MCP server registry, tool discovery, routing, governance for multi-agent setups.

**Pexon defaults:**
- Central MCP Registry with RBAC and audit logging
- Agent Hub for routing and lifecycle management of enterprise agents
- Tool governance: every MCP tool registered, versioned, access-controlled

**Tools:**

### SonarQube MCP Server
[github.com/SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)
Official MCP server exposing SonarQube's code quality and security analysis to LLM agents. Register in the MCP Registry to give agents access to code quality signals without custom integration work.

**At Pexon:** Register as a standard tool in client MCP registries where SonarQube is already in use. Useful for AI-assisted code review agents and DevSecOps workflows.

---

## Layer 6 — Custom AI Engineering & Applications

**What lives here:** RAG chatbots, document intelligence, voice bots, workflow automation, AI apps for business units.

**Pexon defaults:**
- RAG: LangChain / LlamaIndex on Vector DB (Layer 4) via Agent Hub (Layer 5)
- Evaluation: RAGAS for RAG quality, custom evals per use case
- Output quality: uncertainty quantification before going to production
- Document Intelligence: VLM-based pipelines for OCR, contract analysis, invoice processing

**Tools:**

### RAGAS
[github.com/vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas)
Evaluation framework for RAG pipelines. Measures faithfulness, answer relevance, context precision, and recall without requiring ground-truth labels for every run.

**At Pexon:** Integrate RAGAS evals as part of the pilot acceptance criteria. Run before and after retrieval tuning to show measurable improvement. Results go into MLflow as experiment metrics.

### UQLM
[github.com/cvs-health/uqlm](https://github.com/cvs-health/uqlm)
Python package for uncertainty quantification on LLM outputs. Flags low-confidence responses — useful in regulated contexts (banking, insurance, healthcare) where hallucinations have high cost.

**At Pexon:** Add to the output layer of RAG apps in regulated industries. Combine with RAGAS evals to get both retrieval quality and generation confidence signals.

### Understand-Anything
[github.com/Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)
Converts codebases into graph-based representations for AI-assisted understanding. Useful when onboarding into large legacy codebases as part of a modernization or AI integration project.

**At Pexon:** Use during discovery/analysis phases of projects with large existing codebases. Not a production runtime dependency.

### autoresearch
[github.com/karpathy/autoresearch](https://github.com/karpathy/autoresearch)
Automated research workflow using LLM agents for literature and topic research. Reference implementation for multi-step reasoning agent patterns.

**At Pexon:** Use as a pattern reference for building research-oriented agents. Adapt the agentic loop pattern for document analysis or competitive intelligence use cases.

---

## Security & Governance (Cross-Cutting)

Applies to every layer. Non-negotiable on client projects.

- **RBAC** on data, models, and tools — enforced at Layer 4 (Vector DB) and Layer 5 (MCP)
- **DSGVO / EU AI Act** — risk classification per use case, AVV in place, DE/EU hosting default
- **Audit logging** — full trace on Layer 5 (MCP), model call logs on Layer 1
- **Identity** — Entra ID / SSO with MFA and Conditional Access
- **Data residency** — DE/EU default; sovereign (STACKIT, OTC) or on-prem for KRITIS / banking

---

## Contributing

- Each layer folder has its own `README.md` with layer-specific patterns and decisions
- Add tools as short entries: what it is, when to use it, how we use it at Pexon

