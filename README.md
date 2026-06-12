# Pexon Tech Radar

The Pexon technology radar: a shared, versioned map of every technology we **use, trial, assess, or retire** across the [Pexon AI Engineering Stack](https://pexon-consulting.de/ki-beratung/ai-engineering-stack/) — plus the knowledge that goes with it: why we picked it, where we used it, who to ask.

**One folder per technology. One PR to contribute. The radar visualization is generated — never edited by hand.**

---

## The 6-layer stack

The radar mirrors our public AI Engineering Stack one-to-one:

```
Layer 6 │ Customer-Facing Applications        radar/6-applications/
Layer 5 │ AI Agent Hub & MCP Registry         radar/5-orchestration/
Layer 4 │ Data Platform & Knowledge Layer     radar/4-data-knowledge/
Layer 3 │ Platform Engineering                radar/3-platform-engineering/
Layer 2 │ Cloud & Compute Foundation          radar/2-cloud-compute/
Layer 1 │ Foundation Models & AI Backbone     radar/1-foundation-models/
─────────────────────────────────────────────────────────────────────
          Security & Governance (cross-cutting)  radar/0-security-governance/
```

## The 4 rings

| Ring | Meaning |
|---|---|
| **Adopt** | Our default. Use it on client projects without further justification. |
| **Trial** | Ready for real client projects, with a champion involved. We are building production experience. |
| **Assess** | Worth understanding. PoCs and internal experiments only — not on client projects yet. |
| **Hold** | Do not start anything new with this. The entry explains why and what to use instead. |

Ring changes happen via PR — see [GOVERNANCE.md](GOVERNANCE.md).

## Browse

- **Radar visualization:** built from this repo on every merge to `main` and published via GitHub Pages (see repo settings → Pages once enabled).
- **In the repo:** every technology lives at `radar/<layer>/<technology>/index.md` — metadata in the frontmatter, knowledge in the body: what it is, why this ring, when (not) to use it, client references, lessons learned, and who to ask (`champions`).
- **Reference architectures:** cross-layer blueprints (RAG platform, document intelligence, …) live in [`docs/blueprints/`](docs/blueprints/).

## Contribute

Three ways, lowest friction first:

1. **Add experience or a client reference** to an existing technology → edit its `index.md` or drop a file into its `experiences/` folder. Any approval merges.
2. **Propose a new technology** → open a [New technology](../../issues/new/choose) issue or directly PR a new folder based on [`templates/entry-template.md`](templates/entry-template.md). New entries start in `assess`.
3. **Request a ring change** → PR that updates `ring` + appends to `ring_history` with a reason. Reviewed by the layer owners.

Details in [CONTRIBUTING.md](CONTRIBUTING.md). Every PR is schema-validated by CI (`scripts/validate.py`) — if it merges, the radar builds.

> Short, opinionated, and practical beats comprehensive and theoretical.
