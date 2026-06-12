# Governance

The radar only stays trustworthy if ring assignments mean something. This is the minimal process that keeps them honest.

## Roles

- **Contributor** — anyone at Pexon. Can add experiences, propose technologies, request ring changes.
- **Layer owner** — accountable for the entries in one layer. Reviews new entries and ring changes there. Defined in [`.github/CODEOWNERS`](.github/CODEOWNERS).
- **Radar board** — the layer owners together. Meets quarterly (30 min), decides contested ring changes, prunes stale entries.

## Ring change rules

| Change | Requirement | Decided by |
|---|---|---|
| (new) → Assess | A filled-in entry | Any layer owner |
| Assess → Trial | A concrete project/PoC where we will use it, plus a named champion | Layer owner |
| Trial → Adopt | At least one production use on a client project | Layer owner; board if contested |
| Any → Hold | Written reason and a recommended alternative in the entry | Layer owner; board if contested |
| Hold → anything | Board decision | Radar board |

Every change is a PR that appends to the entry's `ring_history` — the radar's audit trail lives in git.

## Quarterly radar board

Agenda, strictly 30 minutes:

1. Decide all open ring-change PRs that layer owners did not merge themselves.
2. Review entries untouched for 12+ months: still accurate? Champion still at Pexon? Move to Hold or archive.
3. Scan `assess` for entries older than 2 quarters with no activity — archive or recommit.

## Archiving

Technologies we no longer want on the radar at all (vs. Hold, which is a visible warning) are moved to `radar/_archive/<layer>/` by the board. History stays in git.
