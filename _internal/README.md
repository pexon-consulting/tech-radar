# Internal Documentation

> **Access restricted to `@pexon-consulting/internal`.**
> If you need access, contact your cluster lead or request via `#stack-repo-access` on Slack.

This folder contains company-specific documentation that is not suitable for
public repositories, client handovers, or external sharing.

---

## Folder structure

```
_internal/
├── adr/              # Architecture Decision Records (full detail with context and trade-offs)
├── cluster-leads/    # Lead contacts, responsibilities, escalation paths, capacity overview
├── pricing/          # Rate cards, TCO models, engagement scope templates
├── client-cases/     # Anonymised case notes, outcome metrics, NDA references
├── runbooks/         # Operational playbooks per layer (incident response, scaling, rollback)
└── roadmap/          # Quarterly stack evolution plans, upcoming cluster priorities
```

---

## Content rules

**What belongs here:**
- Pexon-specific configs with internal naming conventions or account identifiers
- Pricing, rate cards, and engagement templates
- Client case notes (anonymised — see rules below)
- Runbooks referencing internal tooling, Slack channels, or escalation contacts
- Full ADRs with commercial or strategic context not suitable for public view

**What does NOT belong here:**
- NDA-protected client artefacts or client-specific source code → use dedicated client workspace
- Personal employee data → use HR systems
- Security credentials or secrets → use Azure Key Vault / AWS Secrets Manager / GitHub Secrets

**Client case note rules:**
- No client names, contract values, or identifiable system names
- Use sector + anonymised descriptor: "DAX energy utility", "Tier-1 private bank", "mid-size manufacturer"
- If uncertain whether content is safe to store, ask your cluster lead before committing

---

## Runbook freshness policy

Every runbook must include a `Last validated:` date in its header.
Runbooks older than 6 months without a re-validation date are considered stale
and should be reviewed, updated, and re-dated — or moved to `runbooks/archive/`.

---

## ADR process

Full ADR content lives in `_internal/adr/`. The ADR index (titles and status only)
is maintained in the public `ARCHITECTURE.md` so the decision history is visible
to all contributors without exposing internal context.

To create a new ADR:
1. Copy `_internal/adr/TEMPLATE.md`
2. Name it `ADR-XXX-short-title.md` (increment from the last ID)
3. Fill in all sections
4. Add a row to the index table in `ARCHITECTURE.md`
5. Open a PR — requires approval from `@pexon-consulting/engineering-leads`
