#!/usr/bin/env python3
"""Advisory OEE source/export drift detection for Workspace consumers.

Compare a trusted pinned export to another *explicit* immutable Git revision.
Never update a resource map, change learner evidence, imply equivalence, read
moving HEAD implicitly, or interpret an old v1 Workspace mapping.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tooling.oee_toolkit.core import ExportBlocked, canonical_json, export_course
from tooling.oee_toolkit.source import GitSource, SourceError

SHA = re.compile(r"[0-9a-f]{40}\Z")
REPO = "0xbuffdev/open-engineering-education"


def by_id(data: list[dict], key: str) -> dict:
    return {item[key]: item for item in data}


def compare_sets(before: dict, after: dict, fields: tuple[str, ...]) -> dict:
    left, right = set(before), set(after)
    return {
        "added": sorted(right - left),
        "removed": sorted(left - right),
        "changed": sorted(
            ident for ident in left & right
            if any(before[ident].get(field) != after[ident].get(field)
                   for field in fields)
        ),
    }


def affected(delta: dict) -> set:
    return set().union(*(set(delta[field]) for field in ("added", "removed", "changed")))


def load_verified_base(export: dict, expected_revision: str) -> None:
    source = export.get("source", {})
    if (export.get("exportVersion") != 1
            or source.get("repository") != REPO
            or source.get("revision") != expected_revision
            or source.get("specification") != "v0.2.0"
            or export.get("validation") != {
                "structural": "passed", "manualReviewRequired": True
            }):
        raise ValueError("baseline is not the selected, structurally passed export v1")


def map_advisory(path: Path | None, source: dict, deltas: dict) -> dict:
    if path is None:
        return {"status": "no_map_supplied", "affectedResourceIds": [],
                "note": "No reviewed v2 Workspace map was available to compare."}
    try:
        map_data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError):
        return {"status": "source_missing", "affectedResourceIds": [],
                "note": "Workspace resource map missing or unreadable; no comparison made."}
    if not isinstance(map_data, dict) or map_data.get("schemaVersion") != 2:
        return {"status": "unsupported_map_schema", "affectedResourceIds": [],
                "note": "Only Workspace resource-map v2 is supported. The v1 map was not reinterpreted."}
    ref = map_data.get("curriculum")
    expected_course = Path(source["coursePath"]).stem
    if (not isinstance(ref, dict) or
            any(ref.get(k) != v for k, v in (
                ("repository", source["repository"]),
                ("revision", source["revision"]),
                ("specification", source["specification"]),
                ("path", source["coursePath"]),
                ("course", expected_course),
            ))):
        return {"status": "source_mismatch", "affectedResourceIds": [],
                "note": "Map does not pin the exact baseline course; no remapping attempted."}
    if map_data.get("status") != "reviewed":
        return {"status": "unreviewed_map", "affectedResourceIds": [],
                "note": "Draft/unreviewed v2 map cannot be treated as an approved mapping."}
    affected_outcomes = affected(deltas["outcomes"]) | set(deltas["coverageChanged"])
    affected_assessments = affected(deltas["assessments"])
    affected_modules = affected(deltas["modules"])
    impacted = set()
    for module in map_data.get("modules", []):
        if not isinstance(module, dict):
            continue
        number = module.get("number")
        for resource in module.get("resources", []):
            if not isinstance(resource, dict):
                continue
            if (number in affected_modules
                    or affected_outcomes.intersection(resource.get("outcomeIds", []))
                    or affected_assessments.intersection(resource.get("assessmentIds", []))):
                rid = resource.get("resource")
                if isinstance(rid, str) and rid:
                    impacted.add(rid)
    changed = (
        any(affected(deltas[key]) for key in ("outcomes", "assessments", "modules"))
        or bool(deltas["coverageChanged"])
        or deltas["prerequisitesChanged"]
    )
    return {
        "status": "needs_mapping_review" if changed else "needs_source_pin_review",
        "affectedResourceIds": sorted(impacted),
        "note": "Review source requirement meaning and all mapped locators before any repin.",
    }


def compare(repo: Path, base: dict, base_revision: str, target_revision: str,
            map_path: Path | None = None) -> dict:
    if not SHA.fullmatch(base_revision) or not SHA.fullmatch(target_revision):
        raise ValueError("both source revisions must be full lowercase Git commit SHAs")
    load_verified_base(base, base_revision)
    code = base["course"]["code"]
    baseline_source = base["source"]
    result = {
        "course": code,
        "sourceRevision": base_revision,
        "targetRevision": target_revision,
        "specification": "v0.2.0",
        "manualReviewRequired": True,
    }
    try:
        new = export_course(GitSource(repo, target_revision), code)
    except ExportBlocked as exc:
        findings = exc.report["findings"]
        classes = sorted({finding["category"] for finding in findings})
        result.update({
            "status": "unsupported_version" if "unsupported_format" in classes else "source_missing",
            "findings": findings,
            "mapping": {"status": "not_compared", "affectedResourceIds": []},
        })
        return result
    except SourceError as exc:
        result.update({
            "status": "source_missing" if exc.category == "missing_input" else "unsupported_version",
            "findings": [{"category": exc.category, "message": str(exc)}],
            "mapping": {"status": "not_compared", "affectedResourceIds": []},
        })
        return result

    outcomes = compare_sets(
        by_id(base["outcomes"], "id"), by_id(new["outcomes"], "id"),
        ("description",)
    )
    assessments = compare_sets(
        by_id(base["assessments"], "id"), by_id(new["assessments"], "id"),
        ("required", "outcomeIds", "work", "criteria", "evidence")
    )
    modules = compare_sets(
        by_id(base["modules"], "number"), by_id(new["modules"], "number"),
        ("title", "outcomeIds", "lessons")
    )
    coverage = sorted(
        key for key in set(base["coverage"]) | set(new["coverage"])
        if base["coverage"].get(key) != new["coverage"].get(key)
    )
    prerequisites = base["course"]["prerequisites"] != new["course"]["prerequisites"]
    deltas = {
        "outcomes": outcomes, "assessments": assessments, "modules": modules,
        "coverageChanged": coverage,
        "prerequisitesChanged": prerequisites,
    }
    changed = (any(affected(deltas[key])
                   for key in ("outcomes", "assessments", "modules"))
               or bool(coverage) or prerequisites)
    mapping = map_advisory(map_path, baseline_source, deltas)
    result.update({
        "status": "needs_mapping_review" if changed else "compatible",
        "deltas": deltas, "mapping": mapping,
        "note": ("Compatible is structural comparison only; the Workspace map "
                 "remains pinned to its old revision until explicitly reviewed. "
                 "This advisory never creates or updates a map."),
    })
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--base-export", type=Path, required=True)
    parser.add_argument("--base-revision", required=True)
    parser.add_argument("--target-revision", required=True)
    parser.add_argument("--workspace-map", type=Path)
    args = parser.parse_args()
    try:
        base = json.loads(args.base_export.read_text(encoding="utf-8"))
        report = compare(args.repo, base, args.base_revision,
                         args.target_revision, args.workspace_map)
        sys.stdout.buffer.write(canonical_json(report))
        return 0  # Drift is advisory, never an automatic repin or status promotion.
    except (OSError, UnicodeError, ValueError, KeyError, TypeError) as exc:
        print(f"source drift advisory cannot run: {type(exc).__name__}: {exc}",
              file=sys.stderr)
        return 3


if __name__ == "__main__":
    sys.exit(main())
