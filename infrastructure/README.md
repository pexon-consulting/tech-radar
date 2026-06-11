# Infrastructure — Shared Tooling

> Shared Terraform modules, Helm chart library, and CI/CD workflows used across
> all six stack layers. Nothing in this folder is layer-specific — if a module
> or workflow is only relevant to one layer, it lives in that layer's folder.

---

## Owners

| Scope | Owner | Contact |
|---|---|---|
| Terraform modules | Alexander Laaser · Robin Werner | `@alexander-laaser` `@robin-werner` |
| Helm chart library | Felix Notka · Alexander Laaser | `@felix-notka` `@alexander-laaser` |
| CI/CD workflows | `@pexon-consulting/engineering-leads` | Via `#stack-repo` on Slack |

---

## Structure

```
infrastructure/
├── terraform/
│   └── modules/      # Reusable IaC modules (network, identity, storage, GPU node pool, ...)
├── helm-charts/      # Shared Kubernetes chart library
└── ci-cd/            # GitHub Actions reusable workflows
```

---

## Terraform modules

All modules follow the [standard Terraform module structure](https://developer.hashicorp.com/terraform/language/modules/develop/structure):

```
modules/<module-name>/
├── main.tf
├── variables.tf
├── outputs.tf
├── versions.tf
└── README.md
```

### Module catalogue

| Module | Path | Description | Owner |
|---|---|---|---|
| `azure-resource-group` | `modules/azure-resource-group/` | Resource group with standard tags | Robin Werner |
| `azure-vnet-ai` | `modules/azure-vnet-ai/` | VNet with private endpoints for AI services | Robin Werner |
| `azure-aks-gpu` | `modules/azure-aks-gpu/` | AKS cluster with GPU node pool | Felix Notka |
| `aws-vpc-ai` | `modules/aws-vpc-ai/` | VPC with VPC endpoints for Bedrock and ECR | Alexander Laaser |
| `aws-eks-gpu` | `modules/aws-eks-gpu/` | EKS cluster with GPU-enabled managed node group | Alexander Laaser |
| `gpu-node-pool` | `modules/gpu-node-pool/` | Cloud-agnostic GPU node pool abstraction | Fabian Mirz |
| `qdrant-storage` | `modules/qdrant-storage/` | Persistent storage provisioning for Qdrant | Patricia Berger |

**Adding a new module:** Follow the structure above, include a `terraform.tfvars.example`,
and add a row to the catalogue. PR requires approval from the module owner and one
`@pexon-consulting/engineering-leads` member.

### Standards

- Terraform >= 1.7 required for all modules
- All variables must have `description` set; sensitive variables must have `sensitive = true`
- No hardcoded regions, account IDs, or subscription IDs — use variables
- Run `terraform fmt -recursive` and `terraform validate` before opening a PR
- Tag all cloud resources using the standard tag module (`modules/standard-tags/`)

---

## Helm chart library

Shared charts used by multiple layers. Layer-specific charts stay in the layer folder.

| Chart | Path | Description | Owner |
|---|---|---|---|
| `base-workload` | `helm-charts/base-workload/` | Base chart with standard labels, probes, resource limits | Felix Notka |
| `gpu-workload` | `helm-charts/gpu-workload/` | Extends base-workload with GPU resource requests and node affinity | Fabian Mirz |
| `internal-service` | `helm-charts/internal-service/` | ClusterIP service with standard network policies | Felix Notka |
| `cronjob` | `helm-charts/cronjob/` | Standard CronJob template for pipeline/batch tasks | Alexander Laaser |
| `postgres-client` | `helm-charts/postgres-client/` | Init container pattern for DB migration jobs | Alexander Laaser |

**Chart standards:**
- Target Kubernetes >= 1.28
- All charts must pass `helm lint` with no warnings
- `values.yaml` must have inline comments for non-obvious settings
- Breaking changes increment the chart major version and require a 30-day deprecation notice

---

## CI/CD reusable workflows

GitHub Actions reusable workflows in `ci-cd/`. Reference these from layer-specific
workflows rather than duplicating logic.

| Workflow | File | Trigger | Description |
|---|---|---|---|
| Terraform validate | `ci-cd/terraform-validate.yml` | PR (`.tf` files changed) | `fmt`, `validate`, `tflint` |
| Terraform plan | `ci-cd/terraform-plan.yml` | PR (`.tf` files changed) | `plan` with output as PR comment |
| Helm lint | `ci-cd/helm-lint.yml` | PR (chart files changed) | `helm lint` + `helm template` dry-run |
| Markdown lint | `ci-cd/markdown-lint.yml` | PR (`.md` files changed) | `markdownlint-cli2` |
| Security scan | `ci-cd/security-scan.yml` | PR (all) | `trivy` for IaC misconfigs + secrets |
| Release tag | `ci-cd/release-tag.yml` | Push to `main` | Creates a semantic version tag |

**Using a reusable workflow in your layer:**

```yaml
# .github/workflows/layer-1-ci.yml
name: Layer 1 CI

on:
  pull_request:
    paths:
      - 'layer-1-foundation-models/**'

jobs:
  terraform:
    uses: ./.github/workflows/../infrastructure/ci-cd/terraform-validate.yml
    with:
      working_directory: layer-1-foundation-models/azure-ai-foundry
```

---

## Secrets management

Secrets are never stored in this repository. Use:

- **Azure:** Azure Key Vault, referenced via managed identity
- **AWS:** AWS Secrets Manager, referenced via IRSA
- **Kubernetes:** External Secrets Operator (ESO) syncing from Key Vault / Secrets Manager
- **GitHub Actions:** GitHub Actions secrets (org-level for shared secrets, repo-level for specific)

---

*Owners: Alexander Laaser · Robin Werner · Felix Notka · Last reviewed: 2026-05*
