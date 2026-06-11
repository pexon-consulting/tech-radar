# Layer 3 — Platform Engineering

> Installs and operates the developer platform, Kubernetes clusters, and AI platform
> tooling that sit between raw cloud infrastructure (Layer 2) and data/application
> workloads (Layers 4–6). This layer is where self-service, GitOps, and MLOps live.

---

## Cluster leads

| Scope | Lead | Contact |
|---|---|---|
| Internal Developer Platform (IDP) | Alexander Laaser | `@alexander-laaser` |
| Kubernetes & Managed K8s | Felix Notka | `@felix-notka` |
| AI Platform Engineering | Alexander Laaser | `@alexander-laaser` |

PRs are reviewed and merged by the responsible lead per subfolder,
as defined in [`CODEOWNERS`](../../.github/CODEOWNERS).

---

## Components

| Component | Path | Owner |
|---|---|---|
| Internal Developer Platform | `idp/` | Alexander Laaser |
| Kubernetes & Managed K8s | `kubernetes/` | Felix Notka |
| AI Platform Engineering | `ai-platform/` | Alexander Laaser |

---

## When to use this layer

| Need | Component |
|---|---|
| Teams need self-service infrastructure provisioning | IDP (Backstage / Port) |
| Deploying containerised AI workloads at scale | Kubernetes |
| Routing LLM requests across multiple model providers | AI Platform — LiteLLM gateway |
| Tracking model versions, experiments, and deployments | AI Platform — MLOps pipelines |
| Standardising developer workflows across a client org | IDP golden paths |

---

## General knowledge

### Internal Developer Platform (IDP)

An IDP abstracts cloud complexity behind self-service workflows. Engineers provision
infrastructure, deploy services, and manage dependencies without deep cloud expertise.

Key tools and their roles:

- **Backstage** (CNCF) — software catalogue, golden path templates, plugin ecosystem
- **Port** — developer portal with a flexible data model; lower config overhead than Backstage
- **Crossplane** — Kubernetes-native infrastructure provisioning via CRDs; bridges IDP actions to Terraform/cloud APIs

When to choose Backstage vs Port: Backstage suits larger engineering orgs with capacity
to maintain plugins; Port is faster to deploy and operationally lighter for mid-size teams.

Reference: [Backstage docs](https://backstage.io/docs) · [Port docs](https://docs.getport.io/) · [Crossplane docs](https://docs.crossplane.io/)

### Kubernetes for AI workloads

Standard K8s requires additions for AI:

- **GPU node pools** with NVIDIA device plugin and time-slicing or MIG partitioning
- **Karpenter / Cluster Autoscaler** for cost-efficient GPU node scaling
- **ArgoCD** for GitOps — all workload state is declared in Git, never applied manually
- **Kyverno or OPA Gatekeeper** for policy enforcement (required namespaces, resource limits, image registries)

Managed K8s comparison:

| Dimension | AKS (Azure) | EKS (AWS) | GKE (Google) | OpenShift |
|---|---|---|---|---|
| GPU support | Strong (NV + AMD) | Strong (NV) | Strong (NV + TPU) | Strong (NV) |
| Managed control plane | Yes | Yes | Yes (Autopilot) | Yes |
| GitOps integration | ArgoCD, Flux | ArgoCD, Flux | Config Sync | ArgoCD (built-in) |
| Compliance posture | Azure Policy | SCPs + OPA | Org Policy | Built-in SCC |
| Sovereign option | Azure DE | None native | None native | On-prem |

### AI Platform Engineering

The AI platform sits between the model layer (Layer 1) and applications (Layer 6).
Its job is to make model access uniform, observable, and cost-controlled.

Key components:

- **LiteLLM gateway** — unified OpenAI-compatible API across Azure, AWS, local models;
  adds RBAC, rate limiting, cost tracking, and fallback routing
- **MLflow / MLOps pipeline** — experiment tracking, model registry, deployment pipelines
- **Model serving** — vLLM or Triton Inference Server for throughput-optimised inference;
  KServe for K8s-native model serving

Serving pattern selection:

| Pattern | When to use |
|---|---|
| Streaming (SSE) | Chat interfaces, real-time user-facing apps |
| Batch inference | Document processing, overnight jobs, cost-sensitive workloads |
| Serverless (scale-to-zero) | Low-traffic apps, dev/staging environments |
| Dedicated GPU pod | High-throughput production workloads with SLA requirements |

---

## Internal / company-specific

> **Access:** Content described here lives in `_internal/layer-3/` and is restricted
> to `@pexon-consulting/internal`. Request access via `#stack-repo-access`.

### What is stored internally

**IDP (`_internal/layer-3/idp/`)**  
Maintained by Alexander Laaser

- Pexon Backstage instance config including approved plugin list and theme
- Port catalog schema used in IDP rollouts (E.ON, EnBW patterns, anonymised)
- Crossplane compositions for common Pexon infrastructure patterns
- Golden path templates validated in production engagements

**Kubernetes (`_internal/layer-3/kubernetes/`)**  
Maintained by Felix Notka

- Pexon base Helm chart values for AKS, EKS, and GKE
- Cluster hardening checklist mapped to NIS-2 and BSI C5 controls
- Validated Kubernetes versions per cloud provider (updated quarterly)
- GPU node pool configs with tested time-slicing ratios per workload type
- Karpenter provisioner templates for cost-optimised GPU scaling

**AI Platform (`_internal/layer-3/ai-platform/`)**  
Maintained by Alexander Laaser

- Pexon LiteLLM gateway config with RBAC, cost tracking, and model fallback logic
- Tested inference throughput benchmarks: tokens/sec per model/GPU combination
- MLOps pipeline templates used in production (anonymised per engagement)
- Model serving SLA baselines for common use cases (RAG, summarisation, extraction)

### Maintenance schedule

| Artefact | Review frequency | Owner |
|---|---|---|
| K8s validated version matrix | Quarterly | Felix Notka |
| LiteLLM gateway config | Per LiteLLM major release | Alexander Laaser |
| Inference benchmarks | Per new GPU or model generation | Alexander Laaser |
| Cluster hardening checklist | Per NIS-2 / BSI C5 guidance update | Felix Notka |

---

## Prerequisites

### IDP (Backstage)

- Kubernetes cluster (from `layer-2-cloud-foundation/`)
- Helm >= 3.14
- GitHub App credentials for Backstage GitHub integration
- PostgreSQL instance for Backstage catalog persistence (managed DB recommended)

### Kubernetes

- Cloud account with K8s service quota (AKS, EKS, or GKE) or bare-metal cluster
- `kubectl` >= 1.28, `helm` >= 3.14
- ArgoCD CLI for GitOps operations
- GPU quota approved in target cloud account (for AI node pools)

### AI Platform (LiteLLM gateway)

- Running Kubernetes cluster with ingress controller
- Model endpoints available from Layer 1
- Redis instance for rate limiting state (in-cluster or managed)
- PostgreSQL for LiteLLM spend tracking

---

## Quick start

### Deploy LiteLLM gateway

```bash
cd layer-3-platform-engineering/ai-platform

cp helm/litellm/values.yaml helm/litellm/values.local.yaml
# Configure: model_list, master_key, database_url, redis_url

helm upgrade --install litellm ./helm/litellm \
  -f helm/litellm/values.local.yaml \
  --namespace ai-platform \
  --create-namespace
```

### Bootstrap ArgoCD (GitOps)

```bash
cd layer-3-platform-engineering/kubernetes

helm repo add argo https://argoproj.github.io/argo-helm
helm upgrade --install argocd argo/argo-cd \
  -f helm/argocd/values.yaml \
  --namespace argocd \
  --create-namespace

# Apply the root app-of-apps
kubectl apply -f argocd/root-app.yaml
```

### Install Backstage

```bash
cd layer-3-platform-engineering/idp/backstage

cp app-config.local.yaml.example app-config.local.yaml
# Fill in: GitHub App credentials, database connection, base URL

helm upgrade --install backstage ./chart \
  -f app-config.local.yaml \
  --namespace idp \
  --create-namespace
```

---

## Related layers

- **Layer 2** (`layer-2-cloud-foundation/`) — provides the cloud accounts and
  Kubernetes-ready compute this layer installs onto
- **Layer 4** (`layer-4-data-platform/`) — data pipelines and vector stores
  run as workloads on the Kubernetes clusters managed here
- **Layer 5** (`layer-5-orchestration/`) — Agent Hub and MCP Registry are
  deployed via the AI platform tooling in this layer
- **Layer 6** (`layer-6-applications/`) — applications consume model endpoints
  through the LiteLLM gateway configured here

---

*Layer owners: Alexander Laaser · Felix Notka · Last reviewed: 2026-05*
