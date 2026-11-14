#!/usr/bin/env python3
"""Derived OEE migration and assessment inventory; never a course parser or grade.

The public Markdown curriculum remains authoritative. This report is an audit
of format and references, not a conformance, reviewer or learner decision.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

PROGRAMS = ("SEF", "APP", "SYS", "AI", "SEC")
COURSE = re.compile(r"^(SEF|APP|SYS|AI|SEC)[1-9]\d*$")
COURSE_LINK = re.compile(r"\[([A-Z]+[1-9]\d*)\]\(\1\.md\)")
CODE = re.compile(r"\b(?:SEF|APP|SYS|AI|SEC)[1-9]\d*\b")
RANGE = re.compile(r"\b((?:SEF|APP|SYS|AI|SEC)[1-9]\d*)\s*[–—-]\s*((?:SEF|APP|SYS|AI|SEC)[1-9]\d*)\b")
META = re.compile(r"^\*\*(\w+(?: \w+)?):\*\*\s*(.*?)\s*$", re.MULTILINE)
REPO = "0xbuffdev/open-engineering-education"


def load_checkers(root: Path):
    """Use the existing format classifier and outcome validator, not a fork."""
    scripts = root / "scripts"
    if str(scripts) not in sys.path:
        sys.path.insert(0, str(scripts))
    from course_format_versions import is_outcome_course  # noqa: PLC0415
    spec = importlib.util.spec_from_file_location("oee_outcome_validator", scripts / "check-outcome-curriculum.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load the existing OEE outcome validator")
    validator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(validator)
    return is_outcome_course, validator


def metadata(text: str) -> dict[str, str]:
    return dict(META.findall(text.split("\n## ", 1)[0]))


def prerequisites(raw: str) -> tuple[list[str], list[str]]:
    """Normalize explicit course-code references and bounded same-program ranges."""
    errors = []
    source = re.sub(r"\[([A-Z]+[1-9]\d*)\]\([^)]*\)", r"\1", raw)

    def expand(match: re.Match[str]) -> str:
        first, last = match.groups()
        prefix_a, number_a = re.fullmatch(r"([A-Z]+)(\d+)", first).groups()
        prefix_b, number_b = re.fullmatch(r"([A-Z]+)(\d+)", last).groups()
        low, high = int(number_a), int(number_b)
        if prefix_a != prefix_b or high < low or high - low > 100:
            errors.append(f"unsupported prerequisite range: {match.group(0)}")
            return match.group(0)
        return ", ".join(f"{prefix_a}{n}" for n in range(low, high + 1))

    source = RANGE.sub(expand, source)
    return list(dict.fromkeys(CODE.findall(source))), errors


def declared_counts(root: Path) -> dict[str, int | None]:
    index = root / "curriculum" / "README.md"
    text = index.read_text(encoding="utf-8") if index.exists() else ""
    counts: dict[str, int | None] = {}
    for program in PROGRAMS:
        match = re.search(rf"^\|\s*`?{program}`?\s*\|[^\n]*\|\s*([^|]+)\|\s*\[{program}/\]", text, re.MULTILINE)
        counts[program] = sum(map(int, re.findall(r"\d+", match.group(1)))) if match else None
    return counts


def catalog_rows(program: str, index: Path) -> tuple[dict[str, dict], list[str]]:
    if not index.is_file():
        return {}, [f"{program}: program catalog README missing"]
    text = index.read_text(encoding="utf-8")
    section = text.split("\n## Courses\n", 1)
    if len(section) != 2:
        return {}, [f"{program}: no per-course Courses table"]
    rows, errors = {}, []
    for line in section[1].split("\n## ", 1)[0].splitlines():
        if not line.lstrip().startswith(f"| [{program}"):
            continue
        cells = [s.strip() for s in line.strip().strip("|").split("|")]
        match = COURSE_LINK.fullmatch(cells[0]) if cells else None
        if not match or not COURSE.fullmatch(match.group(1)) or not match.group(1).startswith(program):
            errors.append(f"{program}: invalid catalog course link: {line}")
            continue
        name = match.group(1)
        if name in rows:
            errors.append(f"{program}: duplicate catalog entry {name}")
            continue
        if len(cells) < 5:
            errors.append(f"{name}: incomplete catalog row")
            continue
        kind = cells[4].strip("`")
        status = re.search(r"\b(draft|tested|verified)\b", cells[5], re.I) if len(cells) > 5 else None
        classification = re.search(r"\b(core|elective)\b", cells[5], re.I) if len(cells) > 5 else None
        codes, parse_errors = prerequisites(cells[3])
        rows[name] = {"title": cells[1], "kind": kind, "prerequisites": codes,
                      "classification": classification.group(1).lower() if classification else "core",
                      "status": status.group(1).lower() if status else None}
        errors.extend(f"{name}: {err}" for err in parse_errors)
    if not rows:
        errors.append(f"{program}: no per-course catalog entries")
    return rows, errors


def request_json(url: str, token: str | None):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "oee-curriculum-inventory"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urlopen(Request(url, headers=headers), timeout=15) as response:
        return json.load(response)


def open_pr_files(repository: str, token: str | None = None) -> list[dict]:
    """Annotate review work only; do not treat PR heads as accepted courses."""
    base = f"https://api.github.com/repos/{repository}"
    prs = []
    for page in range(1, 21):
        batch = request_json(f"{base}/pulls?state=open&per_page=100&page={page}", token)
        for pr in batch:
            files = []
            for file_page in range(1, 21):
                changed = request_json(f"{base}/pulls/{pr['number']}/files?per_page=100&page={file_page}", token)
                files.extend(f["filename"] for f in changed if f["filename"].startswith("curriculum/"))
                if len(changed) < 100:
                    break
            prs.append({"number": pr["number"], "url": pr["html_url"],
                        "head_sha": pr["head"]["sha"], "files": sorted(set(files))})
        if len(batch) < 100:
            break
    return sorted(prs, key=lambda pr: pr["number"])


def source_sha(root: Path, override: str | None):
    if override:
        if not re.fullmatch(r"[0-9a-f]{40}", override):
            raise ValueError("--source-sha must be a full lowercase 40-digit Git SHA")
        return override
    result = subprocess.run(["git", "rev-parse", "--verify", "HEAD"], cwd=root,
                            text=True, capture_output=True, check=False)
    if result.returncode or not re.fullmatch(r"[0-9a-f]{40}", result.stdout.strip()):
        raise ValueError("run inside the source checkout or supply --source-sha")
    return result.stdout.strip()


def build_inventory(root: Path, commit: str, pull_requests: list[dict] | None = None) -> dict:
    classify, validator = load_checkers(root)
    declared = declared_counts(root)
    pending: dict[str, list[dict]] = {}
    for pr in pull_requests or []:
        for path in pr["files"]:
            if re.fullmatch(r"curriculum/(?:SEF|APP|SYS|AI|SEC)/[A-Z]+[1-9]\d*\.md", path):
                pending.setdefault(path, []).append(pr)
    records, programs = [], []
    for program in PROGRAMS:
        folder = root / "curriculum" / program
        rows, errors = catalog_rows(program, folder / "README.md")
        files = {p.stem: p for p in folder.glob("*.md") if COURSE.fullmatch(p.stem) and p.stem.startswith(program)}
        paths = dict.fromkeys([*rows, *sorted(files), *sorted(
            Path(path).stem for path in pending if path.startswith(f"curriculum/{program}/"))])
        for course_code in paths:
            relative_path = f"curriculum/{program}/{course_code}.md"
            path = files.get(course_code)
            prs = pending.get(relative_path, [])
            catalog = rows.get(course_code)
            entry = {"code": course_code, "program": program, "path": relative_path,
                     "catalog": "listed" if catalog else "unlisted",
                     "classification": catalog["classification"] if catalog else None,
                     "source_sha": commit if path else None,
                     "source_prs": [{"number": pr["number"], "url": pr["url"], "head_sha": pr["head_sha"]} for pr in prs],
                     "status": None, "format": "missing" if not path else "unsupported",
                     "structural_validation": "not_applicable",
                     "structural_errors": [], "prerequisites": [], "prerequisite_issues": [],
                     "outcome_count": None, "assessment_count": None,
                     "covered_outcome_count": None, "uncovered_outcomes": None,
                     "project_defense": "not_assessed",
                     "editorial_review": "not_established", "learner_validation": "not_established"}
            if not path:
                if prs:
                    entry["format"] = "pending_pr_unreviewed"
                records.append(entry)
                continue
            content = path.read_text(encoding="utf-8")
            meta = metadata(content)
            entry["status"] = meta.get("Status", "").strip("` ") or (catalog["status"] if catalog else None)
            entry["classification"] = entry["classification"] or meta.get("Classification", "").strip("` ") or None
            raw_prereqs = meta.get("Prerequisites", meta.get("Prerequisite", ""))
            codes, parse_errors = prerequisites(raw_prereqs)
            entry["prerequisites"] = codes
            entry["prerequisite_issues"].extend(parse_errors)
            if not raw_prereqs:
                entry["prerequisite_issues"].append("missing course prerequisite metadata")
            if catalog:
                if set(codes) != set(catalog["prerequisites"]):
                    entry["prerequisite_issues"].append("course prerequisites differ from catalog")
                if catalog["status"] and entry["status"] != catalog["status"]:
                    entry["structural_errors"].append("course status differs from catalog")
                if meta.get("Type", "").strip("` ") != catalog["kind"]:
                    entry["structural_errors"].append("course kind differs from catalog")
            try:
                outcome = classify(content)
                entry["format"] = "v0.2.0" if outcome else "legacy_unsupported"
            except ValueError as exc:
                entry["format"] = "unsupported"
                entry["structural_errors"].append(str(exc))
                outcome = False
            if outcome:
                failures = validator.validate_course(path)
                entry["structural_errors"].extend(failures)
                learning = validator.block_after_heading(content, "Learning outcomes")
                outcomes = {m.group(1) for line in learning.splitlines()
                            if (m := validator.OUTCOME_RE.match(line))}
                completion = validator.block_after_heading(content, "Completion requirements")
                headers = list(re.finditer(
                    r"^\s*-\s+\*\*([A-Z]{2,6}[1-9]\d*-AS[1-9]\d*)\*\*(.*)$",
                    completion, re.MULTILINE))
                covered, required = set(), []
                for index, header in enumerate(headers):
                    if re.search(r"\boptional\b", header.group(2), re.IGNORECASE):
                        continue
                    stop = headers[index + 1].start() if index + 1 < len(headers) else len(completion)
                    block = completion[header.end():stop]
                    refs = next((m.group(2) for line in block.splitlines()
                                 if (m := validator.FIELD_RE.match(line)) and m.group(1).lower() == "outcomes"), "")
                    covered.update(set(re.findall(rf"\b{course_code}-O[1-9]\d*\b", refs)) & outcomes)
                    required.append(header.group(1))
                entry["outcome_count"] = len(outcomes)
                entry["assessment_count"] = len(set(required))
                entry["covered_outcome_count"] = len(covered)
                entry["uncovered_outcomes"] = sorted(outcomes - covered)
                if meta.get("Type", "").strip("` ") == "project":
                    entry["project_defense"] = "mentioned" if "defense" in completion.lower() else "missing"
                entry["structural_validation"] = "failed" if entry["structural_errors"] else "passed"
            records.append(entry)
        programs.append({"program": program, "catalog_present": (folder / "README.md").is_file(),
                         "catalog_entries": len(rows), "declared_course_count": declared[program],
                         "missing_catalog_entries": max(0, declared[program] - len(rows)) if declared[program] is not None else None,
                         "issues": errors + ([f"{program}: overview declares {declared[program]} courses but catalog lists {len(rows)}"]
                                             if declared[program] is not None and declared[program] != len(rows) else [])})
    known = {c["code"] for c in records if c["source_sha"]}
    for entry in records:
        for prereq in entry["prerequisites"]:
            if prereq == entry["code"]:
                entry["prerequisite_issues"].append("self prerequisite")
            elif prereq not in known:
                entry["prerequisite_issues"].append(f"missing prerequisite course: {prereq}")
    graph = {r["code"]: r["prerequisites"] for r in records if r["source_sha"]}

    def visit(code: str, stack: set[str]):
        if code in stack:
            return True
        return any(visit(pr, stack | {code}) for pr in graph[code] if pr in graph)

    for row in records:
        if row["source_sha"] and visit(row["code"], set()):
            row["prerequisite_issues"].append("prerequisite cycle detected")
    return {"schema_version": 1, "source_repository": REPO, "source_commit": commit,
            "note": "Structural/metadata inventory only. No course is certified, learner-tested or verified by this scan.",
            "pr_scan": "completed" if pull_requests is not None else "not_requested",
            "programs": programs, "courses": records}


def markdown(report: dict) -> str:
    lines = ["# OEE curriculum migration inventory (generated)", "",
             f"Source: `{report['source_repository']}@{report['source_commit']}` (exact commit)",
             f"Open PR scan: `{report['pr_scan']}`", "",
             "> This is a derived structural inventory, not educational conformance, editorial approval, or learner evidence.",
             "> `legacy_unsupported` courses are **not** v0.2.0 and were **not** validated against v0.2.0.", "",
             "## Program coverage", "",
             "| Program | Listed courses | Declared courses | Catalog gap | Notes |",
             "| --- | ---: | ---: | ---: | --- |"]
    for p in report["programs"]:
        lines.append(f"| {p['program']} | {p['catalog_entries']} | {p['declared_course_count'] if p['declared_course_count'] is not None else '?'} | {p['missing_catalog_entries'] if p['missing_catalog_entries'] is not None else '?'} | {'; '.join(p['issues']) or '—'} |")
    lines += ["", "## Courses and pending source PRs", "",
              "| Course | Catalog | Format | Status | Outcomes covered | Assessments | Prerequisites | PRs | Issues |",
              "| --- | --- | --- | --- | --- | ---: | --- | --- | --- |"]
    for c in report["courses"]:
        coverage = (f"{c['covered_outcome_count']}/{c['outcome_count']}" if c["outcome_count"] is not None else "not measurable")
        prs = ", ".join(f"[#{pr['number']}]({pr['url']})" for pr in c["source_prs"]) or "—"
        issues = [*c["prerequisite_issues"], *c["structural_errors"]]
        if c["catalog"] == "unlisted":
            issues.insert(0, "not in course catalog")
        if c["format"] in ("missing", "pending_pr_unreviewed"):
            issues.append("not in current source")
        if c["format"] == "legacy_unsupported":
            issues.append("v0.2.0 checks not applicable")
        course_link = (f"[{c['code']}](https://github.com/{report['source_repository']}/blob/{report['source_commit']}/{c['path']})" if c["source_sha"] else c["code"])
        lines.append(f"| {course_link} | {c['catalog']} | {c['format']} / {c['structural_validation']} | {c['status'] or 'unknown'} | {coverage} | {c['assessment_count'] if c['assessment_count'] is not None else '—'} | {', '.join(c['prerequisites']) or 'none/unknown'} | {prs} | {'; '.join(issues) or '—'} |")
    lines += ["", "Every existing course row uses the exact `source_commit` and relative `path` in the JSON report.",
              "A pending PR row is not an adopted course and is not interpreted using the PR head.",
              "All editorial review and learner validation fields are `not_established`; source status labels are descriptive, not generated promotions.", ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--source-sha", help="exact source commit when testing outside Git")
    parser.add_argument("--include-open-prs", action="store_true", help="fetch GitHub PR/file metadata; requires network")
    parser.add_argument("--repo", default=REPO, help="public repository to query for pending PRs")
    parser.add_argument("--format", choices=("json", "markdown"), default="markdown")
    parser.add_argument("--output-dir", type=Path, help="write both inventory.md and inventory.json to this directory")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        commit = source_sha(root, args.source_sha)
        prs = open_pr_files(args.repo, os.getenv("GITHUB_TOKEN")) if args.include_open_prs else None
        report = build_inventory(root, commit, prs)
    except (ValueError, HTTPError, URLError, OSError, KeyError) as exc:
        parser.exit(2, f"inventory unavailable: {exc}\n")
    report["source_repository"] = args.repo
    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        (args.output_dir / "inventory.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        (args.output_dir / "inventory.md").write_text(markdown(report), encoding="utf-8")
    else:
        print(json.dumps(report, indent=2) if args.format == "json" else markdown(report), end="\n" if args.format == "json" else "")
    return 0


if __name__ == "__main__":
    sys.exit(main())
