# Contributing to the Pexon AI Engineering Stack

Thank you for contributing. This document covers everything you need to know before
opening a pull request — from branching conventions to the general vs. internal
content rule that keeps sensitive information in the right place.

---

## Table of contents

- [Who can contribute](#who-can-contribute)
- [Branching strategy](#branching-strategy)
- [What belongs where: general vs. internal content](#what-belongs-where-general-vs-internal-content)
- [Pull request process](#pull-request-process)
- [Commit message conventions](#commit-message-conventions)
- [Documentation standards](#documentation-standards)
- [Infrastructure changes](#infrastructure-changes)
- [Adding a new component](#adding-a-new-component)
- [Security & compliance changes](#security--compliance-changes)
- [Internal-only changes](#internal-only-changes)
- [Review expectations](#review-expectations)
- [Getting help](#getting-help)

---

## Who can contribute

| Contributor type | Access level | What they can do |
|---|---|---|
| Pexon engineers | Full repo access | Contribute to all folders including `_internal/` |
| Cluster leads | Write + merge rights on their folders | Approve and merge PRs in their scope (enforced via `CODEOWNERS`) |
| External contributors | Public layer folders only | Contribute to layer READMEs and general knowledge docs via fork |
| Clients / partners | Read-only on public folders | No direct contributions; raise issues instead |

Folder-to-owner mapping is defined in [`.github/CODEOWNERS`](./.github/CODEOWNERS).

---

## Branching strategy

```
main                  ← production-ready, protected
  └── develop         ← integration branch for ongoing work
        └── feat/     ← new components or capabilities
        └── fix/      ← bug fixes in existing configs or docs
        └── docs/     ← documentation-only changes
        └── chore/    ← dependency updates, refactors, CI tweaks
        └── sec/      ← security or compliance changes (fast-tracked review)
```

Branch naming: `<type>/<layer>-<short-description>`

Examples:
- `feat/layer-1-vllm-helm-chart`
- `docs/layer-4-vector-db-chunking-guide`
- `fix/layer-3-kubernetes-gpu-nodepool`
- `sec/compliance-eu-ai-act-checklist`

Never commit directly to `main` or `develop`. All changes go through a PR.

---

## What belongs where: general vs. internal content

This is the single most important rule in this repo.

**General knowledge** — goes in the layer folder directly (e.g. `layer-1-foundation-models/README.md`
or a `docs/` subfolder within the layer):

- Architecture concepts, patterns, and decision criteria
- Technology comparisons and trade-off analyses
- Links to official documentation
- Anonymised examples that could appear in a client workshop or public blog post
- Setup guides based on public tooling with no Pexon-specific identifiers

**Internal / company-specific** — goes in `_internal/` or the layer's `_internal/` subfolder:

- Pexon-specific Terraform modules, Helm values, or config files with internal naming conventions
- Client project configs, even when anonymised, if they contain environment-specific details
- Pricing, rate cards, engagement templates
- Runbooks referencing internal tooling, Slack channels, or escalation paths
- Architecture Decision Records (ADRs) with full commercial or strategic context
- Anything covered by an NDA or client confidentiality agreement

**When in doubt:** Ask yourself — could this appear in a public GitHub repo or a client-facing slide deck without any concern? If yes, it's general. If no, it's internal. If still unsure, ask your cluster lead before merging.

---

## Pull request process

1. **Create a branch** from `develop` following the naming convention above.
2. **Make your changes.** Keep PRs focused — one component or one concern per PR.
3. **Update documentation.** Every code change needs a corresponding doc update in the same PR.
   - New Terraform module → update the layer `README.md` component table
   - New internal template → update `_internal/` index and add an ADR if architectural
4. **Open the PR against `develop`** with the provided PR template filled in completely.
5. **Automated checks must pass** before review is requested:
   - `terraform fmt` and `terraform validate` for any `.tf` files
   - `helm lint` for any Helm chart changes
   - Markdown linting (`markdownlint`) for documentation changes
6. **Request review** from your cluster lead. GitHub will auto-assign via `CODEOWNERS`.
7. **Address feedback** — resolve all comments before re-requesting review.
8. **Merge** is performed by the cluster lead after approval. Squash merge is preferred for feature branches; merge commit for releases.

### PR size guidelines

| Change type | Max files | Notes |
|---|---|---|
| Documentation only | No limit | Keep to one layer or topic per PR |
| Single Terraform module | ~20 files | Include tests and docs |
| Helm chart addition | ~15 files | Include values.yaml and README |
| Cross-layer refactor | Discuss first | Open an issue before starting |

---

## Commit message conventions

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <short summary>

[optional body]

[optional footer: refs #issue, breaking changes]
```

Types: `feat`, `fix`, `docs`, `chore`, `sec`, `refactor`, `test`  
Scope: layer folder short name, e.g. `layer-1`, `layer-4`, `security`, `infra`, `internal`

Examples:
```
feat(layer-1): add vLLM Helm chart for H100 GPU nodes
docs(layer-4): add chunking strategy guide for long-form documents
fix(layer-3): correct GPU node affinity rule in AKS base config
sec(security): update EU AI Act risk classification checklist to 2026-05
chore(infra): bump Terraform AWS provider to 5.50
```

---

## Documentation standards

All documentation in this repo is written in Markdown.

- **Language:** English throughout. German is acceptable in `_internal/` docs where the audience is exclusively German-speaking team members.
- **Headings:** Use sentence case (`## Getting started`, not `## Getting Started`).
- **Code blocks:** Always specify the language for syntax highlighting (` ```bash`, ` ```hcl`, ` ```yaml`).
- **Links:** Use relative links within the repo (`[CODEOWNERS](./.github/CODEOWNERS)`), not absolute GitHub URLs.
- **Tables:** Use for comparisons and component lists. Keep columns to four or fewer for readability.
- **Callout blocks:** Use `> **Note:**` for important information and `> **Warning:**` for things that can cause data loss or compliance issues.

Each layer folder must contain a `README.md` that includes at minimum:

- Folder purpose and scope
- Component table with path and owner
- General knowledge section
- Internal / company-specific section (with access note)
- Local prerequisites and quick-start command

---

## Infrastructure changes

### Terraform

- All modules must follow the [standard module structure](https://developer.hashicorp.com/terraform/language/modules/develop/structure): `main.tf`, `variables.tf`, `outputs.tf`, `README.md`.
- Run `terraform fmt -recursive` before committing.
- Attach a `terraform plan` output as a PR comment for any change that modifies existing resources.
- New modules must include a `terraform.tfvars.example` with all required variables documented.
- Do not hardcode credentials, subscription IDs, or account numbers. Use variables with descriptions.

### Helm charts

- Target Kubernetes 1.28+ unless the component has a specific version requirement (document it).
- Run `helm lint` before committing.
- Every chart must have a `values.yaml` with all defaults and inline comments explaining non-obvious settings.
- GPU node pool configs must include resource limits and node affinity rules.

### CI/CD workflows

- Reusable workflows live in `infrastructure/ci-cd/`. Refer to them from layer-specific workflows — don't duplicate logic.
- Secrets are never stored in the repo. Use GitHub Actions secrets or Vault references.

---

## Adding a new component

1. Create the folder under the appropriate layer.
2. Add a `README.md` following the layer README template (see `layer-1-foundation-models/` as reference).
3. Add the component to the parent layer's `README.md` component table.
4. Update `ARCHITECTURE.md` with the new component and its position in the stack.
5. If the addition represents an architectural decision, create an ADR in `_internal/adr/` using the ADR template.
6. Update `.github/CODEOWNERS` if ownership differs from the parent layer default.

---

## Security & compliance changes

Changes to `security-governance/` require two approvals:

1. The responsible cluster lead
2. A member of `@pexon-consulting/compliance-owners`

For changes that affect compliance posture (EU AI Act classification, DSGVO templates, RBAC schemas):

- Reference the relevant regulation and article in the PR description.
- If the change is triggered by a regulatory update, note the effective date.
- Tag the PR with the `compliance` label.

---

## Internal-only changes

Changes to `_internal/` require approval from `@pexon-consulting/engineering-leads`.

Additional rules for internal content:

- **Client case notes:** Always anonymise before committing. No client names, contract values, or identifiable system names. Use sector + anonymised descriptor (e.g. "DAX energy utility", "Tier-1 private bank").
- **Pricing:** Rate cards and TCO models live in `_internal/pricing/`. Never reference pricing in public layer folders or PR descriptions.
- **Runbooks:** Must include a "last validated" date at the top. Runbooks older than 6 months should be reviewed and re-dated or archived.
- **ADRs:** Use the ADR template in `_internal/adr/TEMPLATE.md`. ADRs are append-only — mark superseded decisions as deprecated rather than deleting them.

---

## Review expectations

**For contributors:**

- PRs should be ready for review when opened, not drafts sent for early feedback (use Draft PRs for work in progress).
- Respond to review comments within 2 business days.
- If a review comment is unclear, ask for clarification — don't guess.

**For cluster leads (reviewers):**

- First review within 2 business days of PR assignment.
- Approve only when all CI checks pass and all comments are resolved.
- If a PR is out of scope for a layer, redirect it to the correct owner rather than rejecting without guidance.

---

## Getting help

| Channel | Purpose |
|---|---|
| `#stack-repo` (Slack) | General questions about the repo structure or contribution process |
| `#stack-repo-access` (Slack) | Request access to `_internal/` or specific folders |
| GitHub Issues | Bug reports, documentation gaps, component requests |
| Your cluster lead | Architecture questions, ADR guidance, internal content decisions |

For urgent security issues, do not open a public GitHub issue. Contact `@pexon-consulting/compliance-owners` directly via Slack.
