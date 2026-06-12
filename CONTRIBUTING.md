# Contributing

Everything in this repo is Markdown + frontmatter. If `scripts/validate.py` passes, your PR is mergeable.

## 1. Add experience to an existing technology

The most common and most valuable contribution. Two options:

- **Small:** edit `radar/<layer>/<technology>/index.md` — add a row to *Client projects & references*, a bullet to *Lessons learned*, or a link to *Resources*.
- **Larger write-up:** add a file to the technology's `experiences/` folder, named `YYYY-MM-<topic>.md` (e.g. `2026-06-clientx-landing-zone.md`). Free-form content; link it from `index.md`.

One approving review from anyone merges this. No governance involved.

## 2. Propose a new technology

1. Copy [`templates/entry-template.md`](templates/entry-template.md) to `radar/<layer>/<technology-slug>/index.md` (slug: lowercase, kebab-case).
2. Fill the frontmatter. New entries start with `ring: assess` unless you bring production evidence.
3. Fill at least *What is it?* and *Why this ring?* — the rest may stay as stubs.
4. Open a PR. A layer owner reviews.

Not sure about the layer? Pick the technology's **home layer** (where its primary job is) and add `tags` for everything else. One entry per technology — no duplicates across layers.

## 3. Request a ring change

1. Edit the entry's frontmatter: update `ring`, append an item to `ring_history` with `ring`, `date` (`YYYY-MM`), and a one-line `reason`.
2. Update the *Why this ring?* section to match.
3. Open a PR. Layer owners review; contested changes go to the quarterly radar board (see [GOVERNANCE.md](GOVERNANCE.md)).

Moves **to Adopt** need at least one production use on a client project. Moves **to Hold** need a stated alternative.

## Frontmatter schema

```yaml
---
name: MLflow                      # display name (required)
layer: 3-platform-engineering     # must match the parent folder (required)
ring: adopt                       # adopt | trial | assess | hold (required)
tags: [mlops, model-registry]     # lowercase kebab-case (required, may be empty)
champions: [jane.doe]             # internal contacts; firstname.lastname (required, fill ASAP)
since: 2026-06                    # YYYY-MM the entry first appeared (required)
ring_history:                     # required, newest last
  - { ring: assess, date: 2026-06, reason: "Initial import" }

# optional fields — add when you have them:
certifications:                   # certs we hold or aim for on this technology
  - { name: "CKAD — Certified Kubernetes Application Developer", issuer: "CNCF", holders: [jane.doe] }
references:                       # PUBLIC case studies (pexon-consulting.de/casestudies)
  - { client: "Liebherr", title: "Open Source KI-Chatbot", url: "https://pexon-consulting.de/casestudie/...", public: true }
articles:                         # our blog posts about this technology
  - { title: "Agentic RAG mit LangGraph", url: "https://pexon-consulting.de/blog/...", date: 2026-06 }
---
```

**Public vs. internal references:** the frontmatter `references:` list is for *public* case studies only — it is rendered on the radar website. Internal or NDA-covered project experience goes into the *Client projects & references* table in the entry body (repo is internal) or into `experiences/`.

## Validate locally

```bash
pip install pyyaml
python3 scripts/validate.py          # schema check, same as CI
python3 scripts/build_radar_json.py  # writes site/radar.json for the visualization
```

## Style

- English, short sentences, opinions welcome — "we tried X, it broke at Y" is exactly what we want.
- Name names: client (where allowed), project, internal contact. That is what makes an entry useful.
- Don't paste vendor marketing. Two honest sentences beat a feature list.
