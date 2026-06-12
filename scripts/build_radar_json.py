#!/usr/bin/env python3
"""Build site/radar.json from the frontmatter of all radar entries.

The visualization in site/ renders exclusively from this file —
the radar is generated, never edited by hand.

Usage: python3 scripts/build_radar_json.py
"""
import json
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
RADAR_DIR = REPO_ROOT / "radar"
OUT_FILE = REPO_ROOT / "site" / "radar.json"

LAYER_TITLES = {
    "6-applications": "Layer 6 — Customer-Facing Applications",
    "5-orchestration": "Layer 5 — AI Agent Hub & MCP Registry",
    "4-data-knowledge": "Layer 4 — Data Platform & Knowledge Layer",
    "3-platform-engineering": "Layer 3 — Platform Engineering",
    "2-cloud-compute": "Layer 2 — Cloud & Compute Foundation",
    "1-foundation-models": "Layer 1 — Foundation Models & AI Backbone",
    "0-security-governance": "Security & Governance (cross-cutting)",
}
# top-down stack order for the visualization
LAYER_ORDER = list(LAYER_TITLES.keys())


def parse_entry(path: Path) -> tuple[dict, str]:
    parts = path.read_text(encoding="utf-8").split("---", 2)
    fm = yaml.safe_load(parts[1])
    body = parts[2] if len(parts) > 2 else ""
    match = re.search(r"^## What is it\?\s*\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    description = re.sub(r"\s+", " ", match.group(1)).strip() if match else ""
    return fm, description


def main() -> int:
    entries = []
    for path in sorted(RADAR_DIR.glob("*/*/index.md")):
        if path.parts[-3] == "_archive":
            continue
        fm, description = parse_entry(path)
        rel = path.relative_to(REPO_ROOT).as_posix()
        entries.append(
            {
                "name": fm["name"],
                "slug": path.parent.name,
                "description": description,
                "layer": fm["layer"],
                "ring": fm["ring"],
                "tags": fm.get("tags", []),
                "champions": fm.get("champions", []),
                "since": str(fm["since"]),
                "ring_history": [
                    {"ring": h["ring"], "date": str(h["date"]), "reason": h.get("reason", "")}
                    for h in fm.get("ring_history", [])
                ],
                "certifications": fm.get("certifications", []) or [],
                "references": fm.get("references", []) or [],
                "articles": [
                    {"title": a.get("title", ""), "url": a.get("url", ""),
                     "date": str(a["date"]) if a.get("date") else ""}
                    for a in (fm.get("articles") or [])
                ],
                "path": rel,
            }
        )

    radar = {
        "title": "Pexon Tech Radar",
        "layers": [{"id": layer, "title": LAYER_TITLES[layer]} for layer in LAYER_ORDER],
        "rings": ["adopt", "trial", "assess", "hold"],
        "entries": entries,
    }

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps(radar, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT_FILE.relative_to(REPO_ROOT)} with {len(entries)} entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
