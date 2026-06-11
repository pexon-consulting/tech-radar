# Layer 2 — Cloud & Compute Foundation

> Provisions the cloud accounts, networks, and compute infrastructure that all
> upper layers run on. Covers Azure, AWS, Sovereign Cloud (STACKIT, OTC), and
> on-premises GPU clusters. No AI workload runs without this layer being in place first.

---

## Cluster leads

| Scope | Lead | Contact |
|---|---|---|
| Azure Landing Zone | Robin Werner | `@robin-werner` |
| AWS Landing Zone | Alexander Laaser | `@alexander-laaser` |
| Sovereign Cloud | Patricia Berger | `@patricia-berger` |
| On-Prem GPU Infrastructure | Fabian Mirz | `@fabian-mirz` |

PRs are reviewed and merged by the responsible lead per subfolder,
as defined in [`CODEOWNERS`](../../.github/CODEOWNERS).

---

## Components

| Component | Path | Owner | Target |
|---|---|---|---|
| Azure Landing Zone | `azure-landing-zone/` | Robin Werner | Azure Germany West Central / West Europe |
| AWS Landing Zone | `aws-landing-zone/` | Alexander Laaser | AWS Frankfurt (eu-central-1) |
| Sovereign Cloud | `sovereign-cloud/` | Patricia Berger | STACKIT, Open Telekom Cloud |
| On-Prem GPU Infrastructure | `on-prem-gpu/` | Fabian Mirz | Client data centre / Pexon lab |

---

## When to use this layer

| Requirement | Recommended path |
|---|---|
| Standard enterprise AI workload | Azure Landing Zone or AWS Landing Zone |
| EU data residency, no US Cloud Act exposure | Sovereign Cloud (STACKIT / OTC) |
| KRITIS, BaFin Tier 1, no cloud dependency | On-Prem GPU Infrastructure |
| Hybrid: cloud orchestration + on-prem inference | Azure or AWS LZ + On-Prem GPU |

---

## General knowledge

### Azure Landing Zone (Cloud Adoption Framework)

The Azure CAF landing zone pattern separates platform concerns (networking, identity, policies)
from application workloads. For AI deployments, the key additions over a standard landing zone are:

- Dedicated AI subscription with GPU quota pre-approved
- Private endpoints for all Azure AI services (no public internet exposure)
- Azure Policy assignments blocking non-EU regions and enforcing tagging
- Managed identity baseline for workload identity federation (no stored credentials)

Reference: [Azure CAF Landing Zone documentation](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/)

### AWS Landing Zone (Control Tower)

AWS Control Tower establishes a multi-account structure with guardrails applied organisation-wide.
For AI workloads the relevant additions are:

- Dedicated AI workload account with Bedrock and EC2 GPU quota requests
- Service Control Policies (SCPs) restricting compute to eu-central-1
- VPC endpoints for Bedrock, S3, and ECR (no internet egress for model calls)
- IAM Identity Center (SSO) for human access; IRSA for workload access

Reference: [AWS Control Tower documentation](https://docs.aws.amazon.com/controltower/)

### Sovereign Cloud decision criteria

Choose STACKIT or OTC when any of the following apply:

- Client explicitly requires freedom from the US Cloud Act (CLOUD Act, 18 U.S.C. § 2713)
- Sector regulation mandates German/EU data centre operators (energy, public sector, some financial)
- Client's legal team has rejected Azure and AWS DPA terms

STACKIT is the BOSH Group (Schwarz/Lidl) cloud — strong enterprise track record in DE.
OTC (Open Telekom Cloud) is Deutsche Telekom's OpenStack-based platform with BSI C5 attestation.

### On-premises GPU infrastructure

On-prem is appropriate when:

- No data must leave the client's own network (absolute data sovereignty)
- Inference volume is high enough to justify CapEx over per-token costs
- Low-latency requirements that cloud round-trips cannot meet (e.g. manufacturing edge)

Key networking considerations:
- InfiniBand (HDR/NDR) for multi-GPU training workloads; 100GbE sufficient for inference-only
- RDMA over Converged Ethernet (RoCE v2) as an InfiniBand alternative on existing Ethernet fabric
- Out-of-band management network (BMC/IPMI) required for GPU server fleet

References:
- [STACKIT documentation](https://docs.stackit.cloud/)
- [Open Telekom Cloud documentation](https://docs.otc.t-systems.com/)
- [NVIDIA DGX infrastructure guide](https://docs.nvidia.com/dgx/)

---

## Internal / company-specific

> **Access:** Content described here lives in `_internal/layer-2/` and is restricted
> to `@pexon-consulting/internal`. Request access via `#stack-repo-access`.

### What is stored internally

**Azure Landing Zone (`_internal/layer-2/azure-landing-zone/`)**  
Maintained by Robin Werner

- Pexon Bicep module library with internal naming conventions and tag schema
- Approved VM SKU list for AI workloads (updated on Azure SKU availability changes)
- Policy-as-Code set validated for Banking, Energy, and Manufacturing sector requirements
- Network topology templates used in E.ON and EnBW-type deployments (anonymised)

**AWS Landing Zone (`_internal/layer-2/aws-landing-zone/`)**  
Maintained by Alexander Laaser

- CDK constructs for Pexon-standard multi-account structure
- SCP templates for DSGVO-compliant AWS organisations
- GPU quota request templates and escalation contacts at AWS

**Sovereign Cloud (`_internal/layer-2/sovereign-cloud/`)**  
Maintained by Patricia Berger

- STACKIT project templates with Pexon org structure and RBAC baseline
- OTC Terraform configs validated for NIS-2 and BSI C5 workloads
- AVV (Auftragsverarbeitungsvertrag) template for sovereign cloud engagements
- KRITIS client network isolation patterns

**On-Prem GPU (`_internal/layer-2/on-prem-gpu/`)**  
Maintained by Fabian Mirz

- Pexon GPU cluster bill of materials (H100 SXM5, A100 PCIe, MI300X configurations)
- IPAM allocation templates for GPU clusters
- Tested BIOS and firmware settings for H100 / A100 performance optimisation
- Deutz and Yokogawa infrastructure patterns (anonymised)

### Maintenance schedule

| Artefact | Review frequency | Owner |
|---|---|---|
| Azure approved SKU list | On Azure SKU changes | Robin Werner |
| SCP / Policy-as-Code set | Quarterly | Robin Werner, Alexander Laaser |
| Sovereign cloud configs | Per STACKIT / OTC release | Patricia Berger |
| GPU cluster BOM | Per new hardware procurement | Fabian Mirz |

---

## Prerequisites

### Azure Landing Zone

- Azure subscription with Owner role
- Terraform >= 1.7, `azurerm` provider >= 3.100, `azuread` provider >= 2.47
- Azure CLI authenticated (`az login`)
- Entra ID permissions to create service principals and assign roles

### AWS Landing Zone

- AWS management account with `OrganizationAccountAccessRole`
- Node.js >= 20 (CDK), AWS CLI authenticated
- `cdk bootstrap` completed in management account

### Sovereign Cloud (STACKIT)

- STACKIT organisation account with project-creator role
- Terraform >= 1.7, `stackit` provider >= 0.25
- STACKIT CLI authenticated (`stackit auth login`)

### On-Prem GPU

- Physical access or remote BMC access to GPU servers
- Ansible >= 9.0 for node provisioning playbooks
- Kubernetes cluster or pre-provisioned bare metal (see `layer-3-platform-engineering/kubernetes/`)

---

## Quick start

### Azure Landing Zone

```bash
cd layer-2-cloud-foundation/azure-landing-zone

cp terraform.tfvars.example terraform.tfvars
# Fill in: management_subscription_id, location, environment_tag

terraform init
terraform plan -out=tfplan
terraform apply tfplan
```

### AWS Landing Zone

```bash
cd layer-2-cloud-foundation/aws-landing-zone

npm install
cp cdk.context.json.example cdk.context.json
# Fill in: management_account_id, home_region, permitted_regions

npx cdk diff --all
npx cdk deploy --all
```

### STACKIT Sovereign Cloud

```bash
cd layer-2-cloud-foundation/sovereign-cloud/stackit

cp terraform.tfvars.example terraform.tfvars
# Fill in: project_id, region, network_cidr

terraform init
terraform plan -out=tfplan
terraform apply tfplan
```

### On-Prem GPU Cluster

```bash
cd layer-2-cloud-foundation/on-prem-gpu

# Edit inventory with your server IPs and BMC credentials
cp inventory.yml.example inventory.yml

# Provision base OS and NVIDIA drivers
ansible-playbook -i inventory.yml playbooks/01-base-setup.yml
ansible-playbook -i inventory.yml playbooks/02-nvidia-drivers.yml
ansible-playbook -i inventory.yml playbooks/03-kubernetes-join.yml
```

---

## Related layers

- **Layer 1** (`layer-1-foundation-models/`) — deploys model hosting into the
  infrastructure this layer provisions
- **Layer 3** (`layer-3-platform-engineering/`) — installs Kubernetes, the IDP,
  and the AI platform on top of this cloud/compute foundation
- **Security** (`security-governance/`) — RBAC, identity, and compliance policies
  that govern all resources created here

---

*Layer owners: Robin Werner · Alexander Laaser · Patricia Berger · Fabian Mirz · Last reviewed: 2026-05*
