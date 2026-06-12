# Architecture Blueprints

Cross-layer reference architectures — how the technologies on the radar combine into the solutions we sell (RAG platforms, document intelligence, agent platforms, voice bots, …).

The marketing offerings on [pexon-consulting.de](https://pexon-consulting.de/ki-beratung/ai-engineering-stack/) live here in their technical form: one blueprint per offering, wiring concrete radar entries across all 6 layers.

## Format

One Markdown file per blueprint:

```markdown
# <Blueprint name>

## Problem it solves
## Architecture (diagram + walkthrough, bottom-up through the layers)
## Radar entries used
Links to radar/<layer>/<technology>/ per layer.
## Known variants
e.g. sovereign/on-prem variant, Azure vs. AWS variant.
## Reference implementations
Client projects (where allowed) or internal repos.
```

Blueprints reference radar entries — never the other way around inventing new technology descriptions. If a blueprint needs a technology that has no radar entry, add the entry first.
