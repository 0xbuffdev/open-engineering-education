#!/usr/bin/env python3
"""Validate current APP catalog entries and OEE v0.2.0 course requirements."""
from pathlib import Path
import re
import sys

from course_format_versions import is_outcome_course, validate_outcome_course
from app_catalog import prerequisite_codes, read_app_catalog

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "curriculum" / "APP"
REQUIRED = ["Overview", "Learning outcomes", "Modules", "Completion requirements"]
TICK = chr(96)

def markdown_table_errors(data: str) -> list[str]:
    """Catch broken APP Markdown table rows; not a normative OEE rule."""
    issues: list[str] = []
    expected_pipes: int | None = None
    in_fence = False
    for line_number, line in enumerate(data.splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            expected_pipes = None
            continue
        if in_fence or not line.startswith("|"):
            expected_pipes = None
            continue
        # Authoring convention: pipes are table separators unless escaped.
        pipes = len(re.findall(r"(?<!\\)\|", line))
        if expected_pipes is None:
            expected_pipes = pipes
        elif pipes != expected_pipes:
            issues.append(
                f"table line {line_number}: expected {expected_pipes} "
                f"pipe separators but found {pipes}"
            )
        if line.count("`") % 2:
            issues.append(f"table line {line_number}: unclosed inline-code delimiter")
    return issues


def validate():
    catalog_path = APP / "README.md"
    entries, errors = read_app_catalog(catalog_path)
    course_map = {entry.code: entry for entry in entries}
    codes = set(course_map)
    core_codes = {entry.code for entry in entries if entry.classification == "core"}
    elective_codes = codes - core_codes
    files = sorted(APP.glob("APP[0-9]*.md"), key=lambda p: int(p.stem[3:]))
    actual_codes = {p.stem for p in files}
    for code in sorted(codes - actual_codes):
        errors.append(f"APP catalog: missing course file {code}.md")
    for code in sorted(actual_codes - codes):
        errors.append(f"APP catalog: unlisted course file {code}.md")
    dependencies = {}
    for file in files:
        code = file.stem
        entry = course_map.get(code)
        if entry is None:
            continue
        data = file.read_text(encoding="utf-8")
        try:
            if not is_outcome_course(data):
                errors.append(f"{code}: unsupported course source; OEE v0.2.0 required")
                continue
        except ValueError as exc:
            errors.append(f"{code}: {exc}")
            continue
        if not data.startswith(f"# {code} — "):
            errors.append(f"{code}: heading mismatch")
        if "**Program:** APP — Application Engineering" not in data:
            errors.append(f"{code}: incorrect program")
        if f"**Type:** {TICK}{entry.kind}{TICK}" not in data:
            errors.append(f"{code}: type differs from catalog")
        status_match = re.search(r"^\*\*Status:\*\* `([^\n]+)`$", data, re.M)
        if not status_match or status_match.group(1) != entry.status:
            errors.append(f"{code}: readiness status differs from catalog")
        title_match = re.search(r"^# (APP\d+) — ([^\n]+)$", data, re.M)
        duration_match = re.search(r"^\*\*Duration:\*\* ([^\n]+)$", data, re.M)
        if not title_match or not duration_match:
            errors.append(f"{code}: title and duration required")
        elif title_match.group(2) != entry.title or duration_match.group(1) != entry.duration:
            errors.append(f"{code}: title/duration differ from catalog")
        classification = re.search(r"^\*\*Classification:\*\* (.+)$", data, re.M)
        metadata_class = (f"{TICK}{entry.classification}{TICK}")
        if entry.classification == "elective" and (
            not classification or classification.group(1) != metadata_class
        ):
            errors.append(f"{code}: elective course classification missing or invalid")
        if classification and classification.group(1) != metadata_class:
            errors.append(f"{code}: classification differs from catalog")
        if re.findall(r"^## (.+)$", data, re.M) != REQUIRED:
            errors.append(f"{code}: required sections must be ordered")
        if re.search(r"\b[BR][0-9]{1,3}\b|^## Course brief|^### Resource map", data, re.M):
            errors.append(f"{code}: private resource references or obsolete headings")
        match = re.search(r"^\*\*Prerequisites:\*\* (.+)$", data, re.M)
        source = match.group(1) if match else ""
        if not match:
            errors.append(f"{code}: missing prerequisite metadata")
        try:
            deps = prerequisite_codes(source)
            catalog_deps = prerequisite_codes(entry.prerequisites)
        except ValueError as exc:
            errors.append(f"{code}: {exc}")
            deps, catalog_deps = [], []
        dependencies[code] = deps
        if set(deps) != set(catalog_deps):
            errors.append(f"{code}: prerequisites differ from catalog")
        if any(dep not in codes or dep == code for dep in deps):
            errors.append(f"{code}: invalid APP prerequisite")
        if code in core_codes and any(dep in elective_codes for dep in deps):
            errors.append(f"{code}: a core course cannot require an elective")
        if code == "APP1" and (
            "SEF10" not in source or "SEF10" not in entry.prerequisites
        ):
            errors.append("APP1: expected SEF10 entry prerequisite")
        for href in re.findall(r"\]\(([^)]+\.md)\)", data):
            if "://" not in href and not (file.parent / href).resolve().is_file():
                errors.append(f"{code}: broken internal link {href}")

        errors.extend(f"{code}: {issue}" for issue in markdown_table_errors(data))
        errors.extend(f"{code}: {issue}" for issue in validate_outcome_course(file))

    catalog = catalog_path.read_text(encoding="utf-8") if catalog_path.exists() else ""
    if "Electives provide optional specialization" not in catalog:
        errors.append("APP catalog: electives must not be graduation requirements")

    visited, active = set(), set()
    def check(code):
        if code in active:
            errors.append(f"APP: prerequisite cycle at {code}")
            return
        if code in visited:
            return
        active.add(code)
        for dep in dependencies.get(code, []):
            if dep in codes:
                check(dep)
        active.remove(code)
        visited.add(code)
    for code in codes:
        check(code)

    # The capstone must actually cover the complete core, even when
    # the catalog assigns newly added core courses nonconsecutive IDs.
    def closure(start):
        reached, pending = set(), list(dependencies.get(start, []))
        while pending:
            dep = pending.pop()
            if dep not in reached and dep in codes:
                reached.add(dep)
                pending.extend(dependencies.get(dep, []))
        return reached
    if "APP9" in codes and "APP9" in dependencies:
        missing_capabilities = core_codes - {"APP9"} - closure("APP9")
        if missing_capabilities:
            errors.append(
                "APP9: graduation capstone is missing core prerequisites: "
                + ", ".join(sorted(missing_capabilities))
            )
    if errors:
        print("\n".join("ERROR: " + x for x in errors), file=sys.stderr)
        return 1
    modules = sum(len(re.findall(r"^### Module \d+ — ", file.read_text(encoding="utf-8"), re.M)) for file in files)
    print(f"APP v0.2.0 structural validation passed: {len(core_codes)} core, {len(elective_codes)} electives, {modules} modules; outcome and catalog checks applied")
    return 0

if __name__ == "__main__":
    sys.exit(validate())
