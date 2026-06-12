# How an entry moves through the radar

```
 proposal (issue/PR)
        │
        ▼
   ┌─────────┐   concrete PoC/project    ┌─────────┐   production use     ┌─────────┐
   │ ASSESS  │ ───────── + champion ───▶ │  TRIAL  │ ──── on a client ──▶ │  ADOPT  │
   └─────────┘                           └─────────┘       project        └─────────┘
        │                                     │                                │
        └──────────── reason + ──────────────┴────────────────────────────────┘
                      alternative
                          ▼
                     ┌─────────┐        board decision
                     │  HOLD   │ ─────────────────────▶  _archive/
                     └─────────┘
```

- Every transition is a PR that updates `ring` and appends to `ring_history`. The diff *is* the decision record.
- Skipping rings is allowed with evidence (e.g. straight to Trial when a client project already commits to the technology).
- **Hold is not deletion.** Hold entries are warnings with an alternative — they stay visible on the radar. Archiving removes an entry from the radar entirely and is a board decision.
- Requirements per transition: see [GOVERNANCE.md](../GOVERNANCE.md).

## What counts as evidence

- **Trial:** a named project or funded PoC, a champion who commits to writing up the result.
- **Adopt:** it ran in production for a client and we would choose it again. Link the reference in the entry.
- **Hold:** a real failure mode, a dead upstream, a strategic conflict — written down, with the replacement named.
