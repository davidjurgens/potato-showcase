#!/usr/bin/env python3
"""
Build `showcase.manifest.json` — one machine-readable index of every design.

    python3 scripts/generate_manifest.py
    python3 scripts/generate_manifest.py --check     # exit 1 if stale

`CATALOG.md` and `ANNOTATION-TYPES.md` are for people. Nothing here was readable
by a tool, so an agent looking for "a span task on dialogue with written
instructions" had to open 440 `metadata.json` files and parse 440 configs.

The manifest merges both halves of each design: what `metadata.json` claims
(title, paper, tags, complexity) and what `config.yaml` actually contains
(annotation types, display types, scheme names, whether instructions were
written and how long they are). Those two disagree often enough to be worth
recording separately -- `metadata.annotationTypes` is hand-maintained and the
config is the thing that runs.

No timestamps in the output, so `--check` means something.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT = os.path.join(ROOT, "showcase.manifest.json")

SKIP_DIRS = {"node_modules", ".git", ".claude", "scripts"}

#: Repo-root directories that hold designs.
CATEGORIES = ("text", "semeval", "video", "image", "audio", "evaluation",
              "preference-learning", "agentic", "multimodal", "templates")


def _load_yaml(path: str):
    try:
        import yaml
    except ImportError:
        sys.exit("This script needs PyYAML: pip install pyyaml")
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _words(value) -> int:
    if not value:
        return 0
    text = re.sub(r"<[^>]+>", " ", str(value))
    return len(text.split())


def _describe_config(path: str) -> dict:
    """What the config actually declares, as opposed to what metadata claims."""
    try:
        config = _load_yaml(path)
    except Exception as exc:
        return {"config_error": str(exc)[:200]}

    schemes = config.get("annotation_schemes") or []
    display = (config.get("instance_display") or {}).get("fields") or []

    instructions = config.get("annotation_instructions")

    return {
        "annotation_types_in_config": sorted(
            {s.get("annotation_type") for s in schemes if s.get("annotation_type")}),
        "display_types": sorted(
            {f.get("type") for f in display if isinstance(f, dict) and f.get("type")}),
        "scheme_names": [s.get("name") for s in schemes if s.get("name")],
        "scheme_count": len(schemes),
        "has_instructions": bool(instructions),
        "instruction_words": _words(instructions),
        "has_codebook_url": bool(config.get("annotation_codebook_url")),
        "has_phases": bool(config.get("phases")),
        "has_training": bool((config.get("training") or {}).get("enabled")),
        "annotators_per_item": config.get("num_annotators_per_item"),
        "task_name": config.get("annotation_task_name"),
    }


def _count_items(directory: str) -> int:
    for name in ("sample-data.json", "sample-data.jsonl"):
        path = os.path.join(directory, name)
        if not os.path.isfile(path):
            continue
        try:
            with open(path, encoding="utf-8") as f:
                text = f.read().strip()
            if text.startswith("["):
                return len(json.loads(text))
            return len([line for line in text.splitlines() if line.strip()])
        except Exception:
            return 0
    return 0


def _designs() -> list:
    designs = []
    for category in CATEGORIES:
        base = os.path.join(ROOT, category)
        if not os.path.isdir(base):
            continue
        for current, dirs, files in os.walk(base):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            if "metadata.json" not in files:
                continue
            relative = os.path.relpath(current, ROOT)
            parts = relative.split(os.sep)

            with open(os.path.join(current, "metadata.json"), encoding="utf-8") as f:
                metadata = json.load(f)

            entry = {
                "id": relative.replace(os.sep, "/"),
                "path": relative.replace(os.sep, "/"),
                "category": parts[0],
                "subcategory": parts[1] if len(parts) > 2 else None,
                "name": parts[-1],
                "title": metadata.get("title"),
                "description": metadata.get("description"),
                "complexity": metadata.get("complexity"),
                "tags": metadata.get("tags") or [],
                "domain": metadata.get("domain") or [],
                "use_case": metadata.get("useCase") or [],
                "annotation_types": metadata.get("annotationTypes") or [],
                "paper_reference": metadata.get("paperReference"),
                "paper_url": metadata.get("paperUrl"),
                "dataset_url": metadata.get("datasetUrl"),
                "featured": bool(metadata.get("featured")),
                "sample_items": _count_items(current),
            }

            config_path = os.path.join(current, "config.yaml")
            if os.path.isfile(config_path):
                entry.update(_describe_config(config_path))
                entry["config"] = os.path.join(relative, "config.yaml").replace(os.sep, "/")

            designs.append(entry)

    return sorted(designs, key=lambda d: d["id"])


def build() -> dict:
    designs = _designs()

    by_type = {}
    for design in designs:
        for name in set(design.get("annotation_types_in_config") or
                        design.get("annotation_types") or []):
            by_type.setdefault(name, []).append(design["id"])

    by_category = {}
    for design in designs:
        by_category[design["category"]] = by_category.get(design["category"], 0) + 1

    with_instructions = [d for d in designs if d.get("has_instructions")]

    return {
        "schema": "potato-showcase-manifest/1",
        "count": len(designs),
        "categories": dict(sorted(by_category.items())),
        "annotation_types": {k: sorted(v) for k, v in sorted(by_type.items())},
        "with_instructions": len(with_instructions),
        "designs": designs,
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true",
                        help="Verify the committed manifest matches the designs")
    args = parser.parse_args(argv)

    manifest = build()
    rendered = json.dumps(manifest, indent=1, sort_keys=False) + "\n"

    if args.check:
        if not os.path.isfile(OUTPUT):
            print(f"{OUTPUT} does not exist. Run this script without --check.",
                  file=sys.stderr)
            return 1
        with open(OUTPUT, encoding="utf-8") as f:
            current = f.read()
        if current != rendered:
            print("showcase.manifest.json is stale. Regenerate with:\n"
                  "  python3 scripts/generate_manifest.py", file=sys.stderr)
            return 1
        print(f"Manifest is current ({manifest['count']} designs).")
        return 0

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(rendered)
    print(f"Wrote {OUTPUT}")
    print(f"  {manifest['count']} designs across {len(manifest['categories'])} categories")
    print(f"  {len(manifest['annotation_types'])} annotation types")
    print(f"  {manifest['with_instructions']} carry written instructions")

    drift = [d["id"] for d in manifest["designs"]
             if d.get("annotation_types_in_config") is not None
             and sorted(d["annotation_types"]) != sorted(d["annotation_types_in_config"])]
    if drift:
        print(f"\n  {len(drift)} design(s) where metadata.annotationTypes disagrees "
              f"with config.yaml — the config is the one that runs:")
        for design_id in drift:
            print(f"    {design_id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
