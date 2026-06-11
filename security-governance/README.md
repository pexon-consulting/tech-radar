# Security & Governance

> Cross-cutting security layer — applies to all 6 stack layers.
> Changes here require approval from both the responsible cluster lead
> and `@pexon-consulting/compliance-owners`.

---

## Owner

| Scope | Owner | Contact |
|---|---|---|
| All security & governance | `@pexon-consulting/compliance-owners` | Via `#compliance` on Slack |

---

## Structure

```
security-governance/
├── rbac/         # Role definitions across all layers and tools
├── identity/     # Entra ID, SSO, MFA, and Conditional Access policies
├── compliance/   # Regulatory templates (EU AI Act, DSGVO, NIS-2, BSI C5)
└── audit/        # Log schemas and SIEM integration configs
```

---

## RBAC

Roles are defined at three levels and must be consistent across all levels:

| Level | Technology | Managed in |
|---|---|---|
| Cloud resources | Azure RBAC / AWS IAM | `rbac/cloud/` |
| Kubernetes | K8s RBAC + Kyverno policies | `rbac/kubernetes/` |
| Application | LiteLLM RBAC + Agent Hub compliance tiers | `rbac/application/` |

**Principle of least privilege applies everywhere.** No role should grant more
access than required for its specific function. Wildcard permissions (`*`) are
prohibited except in the management account landing zone bootstrap.

---

## Identity

All human and workload access follows these rules:

- **Human access:** Entra ID SSO with MFA enforced via Conditional Access policy.
  No local accounts. No shared credentials.
- **Workload access:** Managed identities (Azure) or IRSA (AWS) only.
  No static API keys or client secrets stored in code or config files.
- **Emergency access:** Break-glass accounts documented in `_internal/runbooks/`
  and subject to quarterly review.

Policies live in `identity/` and are applied via Terraform during landing zone setup.

---

## Compliance coverage

| Standard | Scope | Templates in |
|---|---|---|
| EU AI Act (2024/1689) | Risk classification, audit trail, human oversight | `compliance/eu-ai-act/` |
| DSGVO / GDPR | Data processing, deletion, residency, AVV | `compliance/dsgvo/` |
| ISO 27001 | Control mapping to stack components | `compliance/iso27001/` |
| NIS-2 | KRITIS and critical infrastructure deployments | `compliance/nis2/` |
| BSI C5 | Cloud architecture attestation | `compliance/bsi-c5/` |
| IEC 62443 | Industrial / OT environments | `compliance/iec62443/` |
| BaFin / MaRisk / DORA | Banking and financial services | `compliance/bafin/` |

### EU AI Act — quick reference

Every use case must be classified before deployment. Classification templates
are in `compliance/eu-ai-act/risk-classification-template.md`.

| Risk tier | Action required |
|---|---|
| Prohibited | Do not deploy. Escalate to `@pexon-consulting/compliance-owners`. |
| High risk | Full audit trail via Agent Hub, human oversight configured, register in EU database |
| Limited risk | Transparency notice to end users (chatbot disclosure, synthetic content labelling) |
| Minimal risk | No mandatory requirements; document classification decision |

---

## Audit logging

The audit log schema is defined in `audit/log-schema.json` and consumed by:

- **Agent Hub** (Layer 5) — logs every agent invocation and tool call
- **LiteLLM gateway** (Layer 3) — logs every model call with token counts and latency
- **Cloud audit logs** — Azure Monitor / AWS CloudTrail forwarded to central SIEM

SIEM integration configs are in `audit/siem/`. Currently supported:
Microsoft Sentinel and Splunk.

Retention policy: 12 months hot storage, 7 years cold storage (for high-risk AI use cases
as required by EU AI Act Article 12).

---

## Change policy

All changes to this folder require:

1. A PR with a description referencing the relevant regulation or control
2. Approval from a `@pexon-consulting/compliance-owners` member
3. For EU AI Act or DSGVO changes: legal team sign-off (reference in PR description)
4. The `compliance` label on the PR

---

*Owner: `@pexon-consulting/compliance-owners` · Last reviewed: 2026-05*
