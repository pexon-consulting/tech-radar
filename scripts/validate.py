#!/usr/bin/env python3
"""Validate all radar entries (radar/**/index.md) against the frontmatter schema.

Exit code 0 = all entries valid, 1 = at least one error.
Warnings (e.g. missing champions) do not fail the build.

Usage: python3 scripts/validate.py
"""
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
RADAR_DIR = REPO_ROOT / "radar"

LAYERS = {
    "0-security-governance",
    "1-foundation-models",
    "2-cloud-compute",
    "3-platform-engineering",
    "4-data-knowledge",
    "5-orchestration",
    "6-applications",
}
RINGS = {"adopt", "trial", "assess", "hold"}
DATE_RE = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

REQUIRED_KEYS = ["name", "layer", "ring", "tags", "champions", "since", "ring_history"]


def parse_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None, "missing frontmatter block (file must start with '---')"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, "unterminated frontmatter block"
    try:
        data = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        return None, f"invalid YAML in frontmatter: {e}"
    if not isinstance(data, dict):
        return None, "frontmatter is not a mapping"
    return data, None


def normalize_date(value) -> str:
    # YAML may parse "2026-06" as a string; keep whatever str() gives us
    return str(value)


def validate_entry(path: Path, errors: list, warnings: list):
    rel = path.relative_to(REPO_ROOT)
    fm, err = parse_frontmatter(path)
    if err:
        errors.append(f"{rel}: {err}")
        return

    for key in REQUIRED_KEYS:
        if key not in fm:
            errors.append(f"{rel}: missing required key '{key}'")
    if any(key not in fm for key in REQUIRED_KEYS):
        return

    folder_layer = path.parent.parent.name
    slug = path.parent.name

    if not isinstance(fm["name"], str) or not fm["name"].strip():
        errors.append(f"{rel}: 'name' must be a non-empty string")
    if fm["layer"] not in LAYERS:
        errors.append(f"{rel}: unknown layer '{fm['layer']}'")
    elif fm["layer"] != folder_layer:
        errors.append(f"{rel}: layer '{fm['layer']}' does not match folder '{folder_layer}'")
    if fm["ring"] not in RINGS:
        errors.append(f"{rel}: ring must be one of {sorted(RINGS)}, got '{fm['ring']}'")
    if not SLUG_RE.match(slug):
        errors.append(f"{rel}: folder name '{slug}' must be lowercase kebab-case")

    if not isinstance(fm["tags"], list) or not all(isinstance(t, str) for t in fm["tags"]):
        errors.append(f"{rel}: 'tags' must be a list of strings")
    else:
        for t in fm["tags"]:
            if not SLUG_RE.match(t):
                errors.append(f"{rel}: tag '{t}' must be lowercase kebab-case")

    if not isinstance(fm["champions"], list) or not all(isinstance(c, str) for c in fm["champions"]):
        errors.append(f"{rel}: 'champions' must be a list of strings")
    elif not fm["champions"]:
        warnings.append(f"{rel}: no champions set — every entry needs an internal contact")

    if not DATE_RE.match(normalize_date(fm["since"])):
        errors.append(f"{rel}: 'since' must be YYYY-MM, got '{fm['since']}'")

    history = fm["ring_history"]
    if not isinstance(history, list) or not history:
        errors.append(f"{rel}: 'ring_history' must be a non-empty list")
    else:
        for i, item in enumerate(history):
            if not isinstance(item, dict):
                errors.append(f"{rel}: ring_history[{i}] must be a mapping")
                continue
            if item.get("ring") not in RINGS:
                errors.append(f"{rel}: ring_history[{i}].ring invalid: '{item.get('ring')}'")
            if not DATE_RE.match(normalize_date(item.get("date", ""))):
                errors.append(f"{rel}: ring_history[{i}].date must be YYYY-MM")
            if not str(item.get("reason", "")).strip():
                errors.append(f"{rel}: ring_history[{i}] needs a non-empty 'reason'")
        last = history[-1]
        if isinstance(last, dict) and last.get("ring") != fm["ring"] and fm["ring"] in RINGS:
            errors.append(
                f"{rel}: ring is '{fm['ring']}' but last ring_history item is "
                f"'{last.get('ring')}' — append the change to ring_history"
            )

    # optional: certifications — list of { name, issuer?, holders?: [people] }
    certs = fm.get("certifications", [])
    if not isinstance(certs, list):
        errors.append(f"{rel}: 'certifications' must be a list")
    else:
        for i, cert in enumerate(certs):
            if not isinstance(cert, dict) or not str(cert.get("name", "")).strip():
                errors.append(f"{rel}: certifications[{i}] needs a non-empty 'name'")
                continue
            if "holders" in cert and (
                not isinstance(cert["holders"], list)
                or not all(isinstance(h, str) for h in cert["holders"])
            ):
                errors.append(f"{rel}: certifications[{i}].holders must be a list of strings")

    # optional: articles — list of { title, url, date? } pointing at our blog posts
    articles = fm.get("articles", [])
    if not isinstance(articles, list):
        errors.append(f"{rel}: 'articles' must be a list")
    else:
        for i, art in enumerate(articles):
            if not isinstance(art, dict):
                errors.append(f"{rel}: articles[{i}] must be a mapping")
                continue
            if not str(art.get("title", "")).strip():
                errors.append(f"{rel}: articles[{i}] needs a non-empty 'title'")
            if not str(art.get("url", "")).startswith("https://"):
                errors.append(f"{rel}: articles[{i}].url must start with https://")

    # optional: references — list of { client, title, url?, public? }
    refs = fm.get("references", [])
    if not isinstance(refs, list):
        errors.append(f"{rel}: 'references' must be a list")
    else:
        for i, ref in enumerate(refs):
            if not isinstance(ref, dict):
                errors.append(f"{rel}: references[{i}] must be a mapping")
                continue
            for key in ("client", "title"):
                if not str(ref.get(key, "")).strip():
                    errors.append(f"{rel}: references[{i}] needs a non-empty '{key}'")
            url = ref.get("url", "")
            if url and not str(url).startswith("https://"):
                errors.append(f"{rel}: references[{i}].url must start with https://")


def main() -> int:
    if not RADAR_DIR.is_dir():
        print(f"error: {RADAR_DIR} not found", file=sys.stderr)
        return 1

    errors: list = []
    warnings: list = []
    entries = sorted(p for p in RADAR_DIR.glob("*/*/index.md") if p.parts[-3] != "_archive")
    for entry in entries:
        validate_entry(entry, errors, warnings)

    # technologies must live at radar/<layer>/<slug>/index.md — catch strays
    for stray in sorted(RADAR_DIR.glob("*/*.md")):
        if stray.name != "README.md":
            errors.append(f"{stray.relative_to(REPO_ROOT)}: entries must be folders with an index.md")
    expected = set(entries)
    for stray in sorted(RADAR_DIR.rglob("index.md")):
        rel_parts = stray.relative_to(RADAR_DIR).parts
        if "_archive" in rel_parts or "experiences" in rel_parts:
            continue
        if stray not in expected:
            errors.append(
                f"{stray.relative_to(REPO_ROOT)}: wrong location — "
                "entries must sit exactly at radar/<layer>/<slug>/index.md"
            )
    for top in sorted(p.name for p in RADAR_DIR.iterdir() if p.is_dir()):
        if top not in LAYERS and top != "_archive":
            errors.append(f"radar/{top}: not a known layer folder")

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"\n{len(entries)} entries checked, {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
