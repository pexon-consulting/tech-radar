# Layer 1 — Foundation Models & AI Backbone

> Provides access to foundation models across all deployment modes: cloud-managed
> (Azure AI Foundry, AWS Bedrock) and fully on-premises (vLLM, SGLang on GPU cluster).
> This is the lowest layer of the stack — everything above depends on it.

---

## Cluster leads

| Scope | Lead | Contact |
|---|---|---|
| Azure AI Foundry | Robin Werner | `@robin-werner` |
| AWS Bedrock | Alexander Laaser | `@alexander-laaser` |
| Local AI / On-Prem | Fabian Mirz | `@fabian-mirz` |

PRs to this folder are reviewed and merged by the responsible lead per subfolder,
as defined in [`CODEOWNERS`](../../.github/CODEOWNERS).

---

## Components

| Component | Path | Owner | Deployment target |
|---|---|---|---|
| Azure AI Foundry | `azure-ai-foundry/` | Robin Werner | Azure (Germany West Central, West Europe) |
| AWS Bedrock | `aws-bedrock/` | Alexander Laaser | AWS (Frankfurt) |
| Local AI | `local-ai/` | Fabian Mirz | On-prem GPU cluster / Sovereign Cloud |

---

## When to use this layer

Every AI use case in the stack routes through Layer 1. The decision between
providers is driven by three factors:

| Factor | Azure AI Foundry | AWS Bedrock | Local AI |
|---|---|---|---|
| Data residency | DE/EU (configurable) | EU (Frankfurt) | On-prem — no cloud egress |
| Model selection | GPT-4o, Claude, Mistral, Phi | Claude, Llama, Titan, Mistral | Any open-weight model |
| Compliance tier | Standard + DSGVO | Standard + DSGVO | KRITIS, BaFin, full sovereignty |
| Typical latency | Low | Low | Variable (hardware-dependent) |
| Cost model | Per token | Per token | CapEx (GPU hardware) + OpEx |

For use cases where data must never leave a client's own infrastructure
(KRITIS, Banking Tier 1, Defence), always use `local-ai/`.

---

## General knowledge

This section contains open reference material suitable for onboarding,
client discussions, and internal training.

### Model provider comparison

| Model family | Provider | Strengths | Limitations |
|---|---|---|---|
| GPT-4o / GPT-4o-mini | Azure AI Foundry | Strong reasoning, tool use, vision | US-origin model; data residency via Azure contract |
| Claude 3.x / 4.x | Azure Foundry, AWS Bedrock | Long context, instruction following, safety | Same residency considerations |
| Mistral Large / Small | Azure Foundry | Efficient, multilingual, EU-origin | Smaller ecosystem than OpenAI |
| Llama 3.x | AWS Bedrock, Local AI | Open weights, customisable, no per-token cost | Requires fine-tuning effort for domain tasks |
| Phi-3 / Phi-4 | Azure Foundry, Local AI | Lightweight, fast inference on smaller GPUs | Limited context window |

### GPU memory sizing (inference)

| Model size | Quantisation | Min VRAM | Recommended GPU |
|---|---|---|---|
| 7B | fp16 | 14 GB | A10G, RTX 4090 |
| 7B | int4 (AWQ) | 4 GB | L4, A10G |
| 13B | fp16 | 26 GB | A100 40GB |
| 70B | fp16 | 140 GB | 2× A100 80GB |
| 70B | int4 (AWQ) | 40 GB | A100 80GB |
| 405B | fp8 | 8× H100 | H100 NVL cluster |

### Quantisation options

- `fp16` — full precision, best quality, highest VRAM requirement
- `int8` (bitsandbytes) — moderate compression, minimal quality loss, easy to apply
- `AWQ` (Activation-aware Weight Quantisation) — good quality/speed trade-off, recommended default for 7B–70B
- `GPTQ` — slightly lower quality than AWQ at same compression, broader model support
- `fp8` — hardware-accelerated on H100; best option for large models on modern GPU clusters

### Useful external references

- [Azure AI Foundry documentation](https://learn.microsoft.com/en-us/azure/ai-studio/)
- [AWS Bedrock documentation](https://docs.aws.amazon.com/bedrock/)
- [vLLM documentation](https://docs.vllm.ai/)
- [SGLang documentation](https://sglang.readthedocs.io/)
- [Model cards — Hugging Face](https://huggingface.co/models)

---

## Internal / company-specific

> **Access:** This section describes content that lives in `_internal/layer-1/`
> and is restricted to `@pexon-consulting/internal`.
> If you need access, contact your cluster lead or request via `#stack-repo-access`.

### What is stored internally

**Azure AI Foundry (`_internal/layer-1/azure-ai-foundry/`)**  
Maintained by Robin Werner

- Pexon Terraform module for Azure AI Foundry with internal naming conventions,
  tag policies, and compliance guardrails pre-configured for Banking and Energy clients
- Approved model version list (updated quarterly) — specific versions validated
  in production and cleared for client use
- Known issues log per Azure region and model version, with workarounds

**AWS Bedrock (`_internal/layer-1/aws-bedrock/`)**  
Maintained by Alexander Laaser

- CDK stacks with Pexon account structure and tagging conventions
- Bedrock model access approval status per client AWS organisation
- Tested guardrail configurations for regulated industries

**Local AI (`_internal/layer-1/local-ai/`)**  
Maintained by Fabian Mirz

- Helm chart values tested on Pexon GPU cluster configurations
  (H100 SXM5, A100 PCIe, MI300X) — includes node affinity rules and resource limits
- NVIDIA driver and CUDA version matrix validated in production
- vLLM serving configs from Deutz and Yokogawa deployments (anonymised)
- Edge AI manufacturing configs for low-latency inference on factory hardware

### Maintenance schedule

| Artefact | Review frequency | Owner |
|---|---|---|
| Approved model version list | Quarterly | Robin Werner, Alexander Laaser, Fabian Mirz |
| GPU driver/CUDA matrix | Per new driver release | Fabian Mirz |
| Known issues log | Ongoing (update on discovery) | All three leads |
| Terraform module | Per major Azure provider update | Robin Werner |

---

## Prerequisites

### Azure AI Foundry

- Azure subscription with AI Foundry quota approved
- Terraform >= 1.7 and `azurerm` provider >= 3.100
- Azure CLI authenticated (`az login`)
- Contributor role on the target resource group

### AWS Bedrock

- AWS account with Bedrock model access approved (per-model opt-in required)
- Node.js >= 20 (for CDK)
- AWS CLI authenticated with appropriate IAM role
- `cdk bootstrap` run in target account/region

### Local AI (vLLM / SGLang)

- Kubernetes cluster with GPU node pool (see `layer-2-cloud-foundation/on-prem-gpu/`)
- NVIDIA device plugin deployed on the cluster
- Helm >= 3.14
- Container registry accessible from the cluster (for model image pulls)
- Sufficient persistent storage for model weights (see GPU memory table above)

---

## Quick start

### Azure AI Foundry

```bash
cd layer-1-foundation-models/azure-ai-foundry

cp terraform.tfvars.example terraform.tfvars
# Fill in: subscription_id, resource_group, location, model_deployments

terraform init
terraform plan -out=tfplan
terraform apply tfplan
```

### AWS Bedrock

```bash
cd layer-1-foundation-models/aws-bedrock

npm install
cp cdk.context.json.example cdk.context.json
# Fill in: account, region, enabled_models

npx cdk diff
npx cdk deploy
```

### Local AI (vLLM on Kubernetes)

```bash
cd layer-1-foundation-models/local-ai

# Copy and edit values for your model and GPU type
cp helm/values.yaml helm/values.local.yaml
# Set: model.name, resources.gpu, nodeSelector

helm upgrade --install vllm ./helm \
  -f helm/values.local.yaml \
  --namespace ai-inference \
  --create-namespace
```

---

## Related layers

- **Layer 2** (`layer-2-cloud-foundation/`) — provisions the cloud accounts and GPU
  infrastructure this layer deploys into
- **Layer 3** (`layer-3-platform-engineering/ai-platform/`) — wraps model endpoints
  behind the LiteLLM gateway and MLOps tooling
- **Layer 5** (`layer-5-orchestration/`) — routes agent requests to the appropriate
  model endpoint via the Agent Hub

---

*Layer owner: Robin Werner · Fabian Mirz · Alexander Laaser · Last reviewed: 2026-05*
