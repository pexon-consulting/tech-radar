# Layer 4 — Data Platform & Knowledge Layer

> Connects enterprise data sources to AI workloads. Covers vector databases for
> semantic search, ETL pipelines for data ingestion and preparation, MCP integration
> for tool-based LLM access, and the broader data platform (Fabric, Snowflake, Lakehouse).
> This is the layer that determines what an AI system knows and how it accesses it.

---

## Cluster lead

| Scope | Lead | Contact |
|---|---|---|
| All Layer 4 components | Patricia Berger | `@patricia-berger` |

PRs are reviewed and merged by Patricia Berger,
as defined in [`CODEOWNERS`](../../.github/CODEOWNERS).

---

## Components

| Component | Path | Description |
|---|---|---|
| Vector DB | `vector-db/` | Semantic search and RAG knowledge stores |
| Enterprise Data | `enterprise-data/` | SAP, CRM, ERP, and filesystem connectors |
| ETL & Pipelines | `etl-pipelines/` | Ingestion, transformation, and scheduling |
| MCP Integration | `mcp-integration/` | Model Context Protocol tool-interface layer |
| Data Platform | `data-platform/` | Microsoft Fabric, Snowflake, Lakehouse templates |

---

## When to use this layer

| Use case | Component |
|---|---|
| Building a RAG application with semantic search | Vector DB |
| Connecting an LLM to SAP, CRM, or internal filesystems | Enterprise Data + MCP Integration |
| Ingesting and cleaning documents at scale | ETL & Pipelines |
| Centralising enterprise data for AI consumption | Data Platform |
| Giving agents real-time access to structured data | MCP Integration |

---

## General knowledge

### Vector databases

A vector database stores high-dimensional embeddings and supports approximate
nearest-neighbour (ANN) search — the core operation behind RAG retrieval.

**Provider comparison:**

| Provider | Deployment | Strengths | Best for |
|---|---|---|---|
| Qdrant | Self-hosted / Cloud | Fast, Rust-based, rich filtering, RBAC | Enterprise RAG, on-prem sovereignty |
| Pinecone | Managed SaaS | Zero ops overhead, serverless tier | Prototypes, low-ops teams |
| Weaviate | Self-hosted / Cloud | Built-in vectorisation, GraphQL API | Multi-modal, hybrid search |
| pgvector | PostgreSQL extension | No new infra, ACID transactions | Low scale, existing Postgres stack |

**Chunking strategies by document type:**

| Document type | Recommended strategy | Chunk size |
|---|---|---|
| Long-form prose (reports, articles) | Recursive character split with overlap | 512–1024 tokens, 10–15% overlap |
| Structured documents (contracts, forms) | Semantic / heading-aware split | Section-level |
| Code | Language-aware split (function / class boundaries) | Function-level |
| Tables and structured data | Row-level or cell-level with metadata | Row + schema context |
| Emails / short messages | Full document (no chunking) | — |

**Embedding model selection:**

| Model | Dimensions | Languages | Notes |
|---|---|---|---|
| `text-embedding-3-large` (OpenAI) | 3072 | Multilingual | High quality, per-token cost |
| `text-embedding-3-small` (OpenAI) | 1536 | Multilingual | Good quality/cost trade-off |
| `multilingual-e5-large` | 1024 | 100+ languages | Strong DE/EN, self-hostable |
| `bge-m3` | 1024 | 100+ languages | Dense + sparse hybrid, free |
| `jina-embeddings-v3` | 1024 | Multilingual | Long context (8192 tokens) |

### MCP (Model Context Protocol)

MCP is an open protocol (Anthropic, 2024) that standardises how LLMs connect to
external tools and data sources. It replaces ad-hoc function calling implementations
with a structured, discoverable interface.

Key concepts:
- **MCP Server** — exposes tools, resources, and prompts via a standardised schema
- **MCP Client** — the LLM-side consumer (Agent Hub in Layer 5)
- **Tool** — a callable function with typed inputs/outputs (e.g. `query_sap_material`)
- **Resource** — a readable data source (e.g. a SharePoint folder, a database table)

When to use MCP vs direct API integration:
- Use **MCP** when the tool will be consumed by multiple agents or reused across projects
- Use **direct API** for one-off integrations or when latency of the MCP layer is a concern

Reference: [MCP specification](https://modelcontextprotocol.io/)

### ETL pipeline design for AI

AI data pipelines differ from traditional ETL in a few important ways:

- **Idempotency is critical** — re-running an ingestion job must not create duplicate embeddings
- **Metadata is as important as content** — document source, date, author, and access tier
  must be stored alongside embeddings for filtering and attribution
- **Incremental updates** — full re-ingestion of large corpora (1M+ documents) is expensive;
  pipelines should detect changes and update only affected chunks
- **Quality gates** — low-quality content (boilerplate, duplicates, corrupted OCR) should
  be filtered before embedding to avoid polluting the knowledge store

---

## Internal / company-specific

> **Access:** Content described here lives in `_internal/layer-4/` and is restricted
> to `@pexon-consulting/internal`. Request access via `#stack-repo-access`.

### What is stored internally

**Vector DB (`_internal/layer-4/vector-db/`)**  
Maintained by Patricia Berger

- Pexon multi-tenant Qdrant RBAC schema used in DAX RAG deployments
  (1.2M-document corpus, Banking sector, anonymised)
- Tested embedding model performance benchmarks per language and domain
  (German legal, German technical, English financial)
- Qdrant collection config templates optimised for different document volumes

**Enterprise Data (`_internal/layer-4/enterprise-data/`)**  
Maintained by Patricia Berger

- SAP RFC connector templates (SAP ECC and S/4HANA)
- CRM connector templates (Salesforce, Dynamics 365)
- SharePoint and Confluence ingestion templates (used in 1.2M-document project)
- Filesystem crawler configs with DSGVO-compliant metadata handling

**ETL Pipelines (`_internal/layer-4/etl-pipelines/`)**  
Maintained by Patricia Berger

- Reusable Airflow DAGs for SAP/CRM/ERP data extraction with incremental load logic
- Pexon dbt macros for LLM data preparation (deduplication, quality scoring, PII detection)
- Databricks job templates for large-scale document processing
- Quality gate thresholds validated in production engagements

**MCP Integration (`_internal/layer-4/mcp-integration/`)**  
Maintained by Patricia Berger

- Pexon MCP tool schemas for SAP, CRM, ERP, and filesystem connectors
- Tested MCP server implementations (Python, TypeScript)
- Client-approved tool registries per compliance tier (KRITIS vs standard)
- Tool response caching patterns for high-latency enterprise systems

### Maintenance schedule

| Artefact | Review frequency | Owner |
|---|---|---|
| Embedding benchmark results | Per major model release | Patricia Berger |
| SAP/CRM connector templates | Per SAP release cycle | Patricia Berger |
| MCP tool schemas | Per MCP spec update | Patricia Berger |
| Airflow DAG library | Quarterly | Patricia Berger |

---

## Prerequisites

### Vector DB (Qdrant)

- Kubernetes cluster (from Layer 3) or Docker for local development
- Helm >= 3.14
- Persistent volume support in the cluster (min 50Gi for production)
- Embedding model endpoint available (from Layer 1 or a dedicated embedding service)

### ETL Pipelines (Airflow)

- Python >= 3.11
- Apache Airflow >= 2.9 (Helm chart provided)
- Access to source systems (SAP, SharePoint, filesystem)
- Object storage for intermediate data (Azure Blob / S3)

### MCP Integration

- Node.js >= 20 or Python >= 3.11 (depending on MCP server implementation)
- Access credentials for the target enterprise system
- MCP Registry entry created in Layer 5 before deploying a new tool

---

## Quick start

### Deploy Qdrant (Kubernetes)

```bash
cd layer-4-data-platform/vector-db

helm repo add qdrant https://qdrant.github.io/qdrant-helm
helm upgrade --install qdrant qdrant/qdrant \
  -f helm/qdrant-values.yaml \
  --namespace vector-db \
  --create-namespace
```

### Run a document ingestion pipeline (Airflow)

```bash
cd layer-4-data-platform/etl-pipelines

# Copy DAG to your Airflow DAGs folder
cp dags/document_ingestion_dag.py $AIRFLOW_HOME/dags/

# Set required Airflow variables
airflow variables set VECTOR_DB_URL "http://qdrant.vector-db.svc.cluster.local:6333"
airflow variables set EMBEDDING_ENDPOINT "http://litellm.ai-platform.svc.cluster.local/v1"

# Trigger the DAG
airflow dags trigger document_ingestion --conf '{"source": "sharepoint", "site_url": "..."}'
```

### Register an MCP tool

```bash
cd layer-4-data-platform/mcp-integration

# Install dependencies
pip install -r requirements.txt

# Start a local MCP server (example: SAP material query tool)
python servers/sap_material_server.py --config config/sap.yaml

# Register the tool in the MCP Registry (Layer 5)
curl -X POST http://mcp-registry.ai-platform.svc.cluster.local/tools \
  -H "Content-Type: application/json" \
  -d @tool-manifests/sap_material_query.json
```

---

## Related layers

- **Layer 1** (`layer-1-foundation-models/`) — embedding model endpoints used
  by ingestion pipelines originate here
- **Layer 3** (`layer-3-platform-engineering/`) — Kubernetes clusters and
  the AI platform gateway that data services run on
- **Layer 5** (`layer-5-orchestration/`) — MCP Registry and Agent Hub consume
  the tools and knowledge stores built in this layer
- **Layer 6** (`layer-6-applications/`) — RAG applications and document
  intelligence pipelines are the primary consumers of this layer

---

*Layer owner: Patricia Berger · Last reviewed: 2026-05*
