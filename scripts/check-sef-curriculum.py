#!/usr/bin/env python3
"""Validate the active SEF program using only the OEE v0.2.0 course contract.

All ten SEF courses have been migrated. This validator rejects absent, old,
unknown and partially migrated formats instead of interpreting historical
quiz/lab authoring conventions. Educational readiness is evaluated separately.
"""

from pathlib import Path
import re
import sys

from course_format_versions import is_outcome_course, validate_outcome_course


ROOT = Path(__file__).resolve().parents[1]
SEF = ROOT / "curriculum" / "SEF"
ORDERED = [f"SEF{i}" for i in range(1, 11)]
EXPECTED = set(ORDERED)
SECTIONS = ["Overview", "Learning outcomes", "Modules", "Completion requirements"]
ERRORS = []
DEPS = {}


def check_links(path: Path, content: str) -> None:
    """Ensure local Markdown targets referenced by a source file exist."""
    for href in re.findall(r"\]\(([^)]+)\)", content):
        target = href.split("#", 1)[0].strip()
        if not target.endswith(".md") or "://" in target:
            continue
        if not (path.parent / target).resolve().is_file():
            ERRORS.append(f"{path.relative_to(ROOT)}: missing target {href}")


def prerequisites(value: str, *, owner: str) -> list[str]:
    """Normalize the public catalog's and course metadata's SEF references.

    Expand an inclusive range *before* checking the dependency graph: linked
    SEF10's '[SEF1](...)–[SEF9](...)' means nine prerequisites, not two.
    """
    raw = value.strip()
    if raw in ("none", "—"):
        return []

    def unmark(match: re.Match) -> str:
        name, filename = match.group(1), match.group(2)
        if filename != f"{name}.md":
            ERRORS.append(f"{owner}: prerequisite link/label mismatch: {match.group(0)}")
        return name

    normalized = re.sub(r"\[([A-Z]+\d+)\]\(([^)]+)\)", unmark, raw)
    range_match = re.fullmatch(r"SEF(\d+)–SEF(\d+)", normalized)
    if range_match:
        start, stop = map(int, range_match.groups())
        if start > stop or stop > 10 or start < 1:
            ERRORS.append(f"{owner}: invalid prerequisite range: {raw}")
            return []
        return [f"SEF{i}" for i in range(start, stop + 1)]
    if not re.fullmatch(r"SEF\d+(?:,\s*SEF\d+)*", normalized):
        ERRORS.append(f"{owner}: invalid prerequisite syntax: {raw}")
        return []
    dependencies = re.findall(r"SEF\d+", normalized)
    if len(dependencies) != len(set(dependencies)):
        ERRORS.append(f"{owner}: duplicate prerequisites: {raw}")
    return dependencies


def catalog_entries(catalog: str) -> dict[str, dict[str, str]]:
    """Read the SEF catalog table without creating a second curriculum registry."""
    rows = {}
    order = []
    for line in catalog.splitlines():
        match = re.match(r"^\|\s*\[(SEF\d+)\]\((SEF\d+\.md)\)\s*\|", line)
        if not match:
            continue
        code, target = match.groups()
        cells = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(cells) != 5 or target != f"{code}.md":
            ERRORS.append(f"SEF catalog: malformed row {code}")
            continue
        if code in rows:
            ERRORS.append(f"SEF catalog: duplicate course {code}")
            continue
        rows[code] = dict(title=cells[1], duration=cells[2],
                          prerequisites=cells[3], kind=cells[4])
        order.append(code)
    if order != ORDERED:
        ERRORS.append(f"SEF catalog: expected order {ORDERED}; got {order}")
    return rows


def validate() -> int:
    ERRORS.clear()
    DEPS.clear()
    courses = sorted(SEF.glob("SEF[0-9]*.md"))
    if {path.stem for path in courses} != EXPECTED or len(courses) != len(ORDERED):
        ERRORS.append("Expected SEF1.md through SEF10.md, exactly")

    catalog_path = SEF / "README.md"
    catalog = catalog_path.read_text(encoding="utf-8")
    rows = catalog_entries(catalog)
    check_links(catalog_path, catalog)

    for path in courses:
        code = path.stem
        content = path.read_text(encoding="utf-8")
        match = re.search(rf"^# {re.escape(code)} — (.+)$", content, re.MULTILINE)
        if not content.startswith(f"# {code} — ") or not match:
            ERRORS.append(f"{code}: missing or misplaced heading")
        metadata = {}
        for key in ("Program", "Type", "Prerequisites", "Duration", "Status", "Specification"):
            found = re.search(rf"^\*\*{key}:\*\* ([^\n]+)$", content, re.MULTILINE)
            if not found:
                ERRORS.append(f"{code}: missing {key} metadata")
            else:
                metadata[key] = found.group(1)

        # All active SEF input uses one strict parser. No historical fallback.
        if metadata.get("Specification") != "`v0.2.0`":
            ERRORS.append(f"{code}: active course must explicitly declare v0.2.0")
            continue
        try:
            if not is_outcome_course(content):
                ERRORS.append(f"{code}: unsupported legacy course format")
                continue
        except ValueError as exc:
            ERRORS.append(f"{code}: {exc}")
            continue

        if metadata.get("Program") != "SEF — Software Engineering Foundations":
            ERRORS.append(f"{code}: incorrect program identity")
        required_kind = "`project`" if code == "SEF10" else "`course`"
        if metadata.get("Type") != required_kind:
            ERRORS.append(f"{code}: incorrect course/project type")
        if metadata.get("Status") not in ("`draft`", "`tested`", "`verified`"):
            ERRORS.append(f"{code}: invalid readiness status")

        headings = re.findall(r"^## (.+)$", content, re.MULTILINE)
        if headings != SECTIONS:
            ERRORS.append(f"{code}: expected exactly {SECTIONS}, got {headings}")
        if re.search(r"\b[BR][0-9]{1,3}\b|^#### Module brief|^## Course brief|^\s*- kind: ",
                     content, re.MULTILINE):
            ERRORS.append(f"{code}: obsolete brief or resource authoring format")
        if "requirements/" in content or "authoring-notes/" in content:
            ERRORS.append(f"{code}: obsolete companion-file reference")

        row = rows.get(code)
        if row is None:
            ERRORS.append(f"{code}: missing catalog row")
        else:
            if match and row["title"] != match.group(1):
                ERRORS.append(f"{code}: title differs from catalog")
            if row["duration"] != metadata.get("Duration"):
                ERRORS.append(f"{code}: duration differs from catalog")
            if row["kind"] != required_kind:
                ERRORS.append(f"{code}: course kind differs from catalog")

        actual_dependencies = prerequisites(
            metadata.get("Prerequisites", ""), owner=f"{code} metadata"
        )
        DEPS[code] = actual_dependencies
        if row is not None:
            listed_dependencies = prerequisites(
                row["prerequisites"], owner=f"{code} catalog"
            )
            if actual_dependencies != listed_dependencies:
                ERRORS.append(f"{code}: prerequisites differ from catalog "
                              f"({actual_dependencies} != {listed_dependencies})")

        for dependency in actual_dependencies:
            if dependency not in EXPECTED or dependency == code:
                ERRORS.append(f"{code}: invalid prerequisite {dependency}")

        ERRORS.extend(f"{code}: {issue}" for issue in validate_outcome_course(path))
        check_links(path, content)

    visiting = set()
    visited = set()

    def visit(code: str) -> None:
        if code in visiting:
            ERRORS.append(f"Prerequisite cycle at {code}")
            return
        if code in visited:
            return
        visiting.add(code)
        for dependency in DEPS.get(code, []):
            if dependency in EXPECTED:
                visit(dependency)
        visiting.remove(code)
        visited.add(code)

    for code in ORDERED:
        visit(code)

    if ERRORS:
        print("\n".join("ERROR: " + issue for issue in ERRORS), file=sys.stderr)
        return 1

    module_count = sum(
        len(re.findall(r"^### Module \d+ — ", path.read_text(encoding="utf-8"),
                       re.MULTILINE))
        for path in courses
    )
    print(
        f"SEF structural validation passed: {len(courses)} courses across "
        f"{module_count} modules ({len(courses)} v0.2.0, 0 legacy), "
        "without fixed module/lesson caps"
    )
    return 0


if __name__ == "__main__":
    sys.exit(validate())
