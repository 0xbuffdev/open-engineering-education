#!/usr/bin/env python3
"""Validate the active SEF program using only the OEE v0.2.0 course contract.

All eleven SEF courses use v0.2.0. This validator rejects absent, old,
unknown and partially migrated formats instead of interpreting historical
quiz/lab authoring conventions. Educational readiness is evaluated separately.
"""

from pathlib import Path
import re
import sys

from course_format_versions import is_outcome_course, validate_outcome_course


ROOT = Path(__file__).resolve().parents[1]
SEF = ROOT / "curriculum" / "SEF"
ORDERED = []  # read from the authoritative program catalog, never numeric IDs
EXPECTED = {f"SEF{i}" for i in range(1, 12)}
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
    """Parse comma-separated codes and inclusive ranges, with optional links.

    A capstone can require '[SEF1](SEF1.md)–[SEF9](SEF9.md), [SEF11](SEF11.md)'.
    Course codes are stable identifiers rather than ordering directives.
    """
    raw = value.strip()
    if raw in ("none", "—"):
        return []
    if not raw:
        ERRORS.append(f"{owner}: missing prerequisite")
        return []

    def unmark(match: re.Match) -> str:
        name, filename = match.group(1), match.group(2)
        if filename != f"{name}.md":
            ERRORS.append(f"{owner}: prerequisite link/label mismatch: {match.group(0)}")
        return name

    normalized = re.sub(r"\[(SEF\d+)\]\(([^)]+)\)", unmark, raw)
    dependencies = []
    for item in normalized.split(","):
        token = item.strip()
        range_match = re.fullmatch(r"SEF(\d+)\s*[–—-]\s*SEF(\d+)", token)
        if range_match:
            start, end = map(int, range_match.groups())
            if start < 1 or end > 11 or end < start:
                ERRORS.append(f"{owner}: invalid prerequisite range: {token}")
                continue
            dependencies.extend(f"SEF{i}" for i in range(start, end + 1))
        elif re.fullmatch(r"SEF[1-9]\d*", token):
            dependencies.append(token)
        else:
            ERRORS.append(f"{owner}: invalid prerequisite syntax: {token}")
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
    if set(order) != EXPECTED or len(order) != len(EXPECTED):
        ERRORS.append(f"SEF catalog: expected exactly eleven adopted courses, got {order}")
    if order and order[-1] != "SEF10":
        ERRORS.append("SEF catalog: SEF10 project must be last")
    ORDERED[:] = order
    return rows


def validate() -> int:
    ERRORS.clear()
    DEPS.clear()
    courses = sorted(SEF.glob("SEF[0-9]*.md"))
    if {path.stem for path in courses} != EXPECTED or len(courses) != len(EXPECTED):
        ERRORS.append("Expected exactly SEF1.md through SEF11.md, including capstone SEF10")

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

    # Ordered catalog must be a valid topological ordering. Numbered IDs
    # are stable public identities, not course sequence numbers.
    position = {code: index for index, code in enumerate(ORDERED)}
    for code, dependencies in DEPS.items():
        for dependency in dependencies:
            if dependency in position and code in position and position[dependency] >= position[code]:
                ERRORS.append(f"SEF catalog: prerequisite {dependency} must precede {code}")

    for code, required in {
        "SEF11": {"SEF2"},
        "SEF4": {"SEF11"},
        "SEF8": {"SEF11"},
        "SEF10": EXPECTED - {"SEF10"},
    }.items():
        missing = required - set(DEPS.get(code, []))
        if missing:
            ERRORS.append(f"{code}: missing required immediate prerequisites {sorted(missing)}")

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
