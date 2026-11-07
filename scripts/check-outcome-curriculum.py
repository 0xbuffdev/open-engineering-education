#!/usr/bin/env python3
"""Structural checks for OEE v0.2.0 outcome-driven course definitions.

This validator checks documented IDs, references, and assessment fields.
It does NOT establish whether a task truly measures an outcome, whether
evidence is sufficient, or whether a course is conforming/tested/verified.

Usage:
    python3 scripts/check-outcome-curriculum.py --all
    python3 scripts/check-outcome-curriculum.py --course curriculum/SEF/SEF1.md
    python3 scripts/check-outcome-curriculum.py --course FILE --course FILE

The --all mode only validates explicitly v0.2.0-marked courses and
courses containing v0.2.0-style outcome/assessment IDs. It reports legacy
courses as skipped. This keeps historical definitions unchanged while
courses are migrated in separate pull requests.

For an explicit version marker, use this OPTIONAL course metadata line:
    **Specification:** \`v0.2.0\`

Do not use --all's legacy skip as proof of new-format conformance.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SECTIONS = (
    "Overview",
    "Learning outcomes",
    "Modules",
    "Completion requirements",
)
SECTION_RE = re.compile(r"^## ([^\n]+)$", re.MULTILINE)
COURSE_RE = re.compile(r"^# ([A-Z]{2,6}[1-9]\d*) — (.+)$", re.MULTILINE)
MODULE_RE = re.compile(r"^### Module (\d+) — (.+)$", re.MULTILINE)
OUTCOME_RE = re.compile(r"^\s*-\s+\*\*([A-Z]{2,6}[1-9]\d*-O[1-9]\d*):\*\*\s*(.*?)\s*$")
ASSESSMENT_RE = re.compile(r"^\s*-\s+\*\*([A-Z]{2,6}[1-9]\d*-AS[1-9]\d*)\*\*(.*)$")
FIELD_RE = re.compile(
    r"^\s*-\s+(?:\*\*)?(Outcomes|Work|Criteria|Evidence):(?:\*\*)?\s*(.*?)\s*$",
    re.IGNORECASE,
)
VERSION_RE = re.compile(
    r"^\*\*(?:Specification|OEE specification):\*\*\s*\`?v0\.2\.0\`?\s*$",
    re.IGNORECASE | re.MULTILINE,
)
ID_HINT_RE = re.compile(r"^\s*-\s+\*\*[A-Z]{2,6}[1-9]\d*-(?:O|AS)[1-9]\d*", re.MULTILINE)


def block_after_heading(text: str, heading: str) -> str:
    sections = list(SECTION_RE.finditer(text))
    for index, match in enumerate(sections):
        if match.group(1).strip() == heading:
            stop = sections[index + 1].start() if index + 1 < len(sections) else len(text)
            return text[match.end():stop]
    return ""


def validate_course(path: Path) -> list[str]:
    """Return inspectable structural errors; empty does not certify pedagogy."""
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    title = COURSE_RE.search(text)
    if not title or title.start() != 0:
        return ["expected a first-line course heading, e.g. '# APP1 — Course title'"]

    code = title.group(1)
    metadata = text[:text.find("\n## ")] if "\n## " in text else text
    for field in ("Type", "Prerequisites", "Duration", "Status"):
        if not re.search(rf"^\*\*{field}:\*\*\s*\S", metadata, re.MULTILINE):
            errors.append(f"missing {field} metadata")
    kind_match = re.search(r"^\*\*Type:\*\*\s*\`?(course|project)\`?\s*$", metadata, re.MULTILINE)
    if not kind_match:
        errors.append("Type must be 'course' or 'project'")
    kind = kind_match.group(1) if kind_match else ""

    found_headings = [m.group(1).strip() for m in SECTION_RE.finditer(text)]
    indices = [found_headings.index(h) for h in REQUIRED_SECTIONS if h in found_headings]
    if len(indices) != len(REQUIRED_SECTIONS) or indices != sorted(indices):
        errors.append("four required top-level sections are missing or out of order")

    learning = block_after_heading(text, "Learning outcomes")
    defined_outcomes: set[str] = set()
    for line in learning.splitlines():
        if not re.match(r"^\s*-\s+", line):
            continue
        match = OUTCOME_RE.match(line)
        if not match:
            errors.append("every course outcome bullet must have a stable 'CODE-O#' ID")
            continue
        identifier, description = match.groups()
        if not identifier.startswith(code + "-"):
            errors.append(f"outcome ID {identifier} does not match course {code}")
        if identifier in defined_outcomes:
            errors.append(f"duplicate outcome ID {identifier}")
        if not description.strip():
            errors.append(f"outcome {identifier} lacks an observable description")
        defined_outcomes.add(identifier)
    if not defined_outcomes:
        errors.append("no stable course outcome IDs defined")

    modules = block_after_heading(text, "Modules")
    matches = list(MODULE_RE.finditer(modules))
    if not matches:
        errors.append("at least one numbered module is required")
    if [int(m.group(1)) for m in matches] != list(range(1, len(matches) + 1)):
        errors.append("module numbering must begin at 1 and be sequential")
    for i, match in enumerate(matches):
        stop = matches[i + 1].start() if i + 1 < len(matches) else len(modules)
        module = modules[match.end():stop]
        number = match.group(1)
        outcomes_pos = module.find("#### Outcomes")
        lessons_pos = module.find("#### Lessons")
        if outcomes_pos < 0 or lessons_pos < 0 or outcomes_pos >= lessons_pos:
            errors.append(f"module {number}: requires Outcomes followed by Lessons")
            continue
        outcome_block = module[outcomes_pos + len("#### Outcomes"):lessons_pos]
        lesson_block = module[lessons_pos + len("#### Lessons"):]
        if not re.search(r"^\s*-\s+\S", outcome_block, re.MULTILINE):
            errors.append(f"module {number}: outcomes are empty")
        for ref in re.findall(rf"\b{re.escape(code)}-O[1-9]\d*\b", outcome_block):
            if ref not in defined_outcomes:
                errors.append(f"module {number}: unknown course outcome {ref}")
        lesson_numbers = [int(n) for n in re.findall(r"^(\d+)\.\s+\S", lesson_block, re.MULTILINE)]
        if not lesson_numbers:
            errors.append(f"module {number}: ordered learning sequence is empty")
        elif lesson_numbers != list(range(1, len(lesson_numbers) + 1)):
            errors.append(f"module {number}: lesson numbering is not sequential")

    completion = block_after_heading(text, "Completion requirements")
    headers = list(re.finditer(
        r"^\s*-\s+\*\*([A-Z]{2,6}[1-9]\d*-AS[1-9]\d*)\*\*(.*)$",
        completion, re.MULTILINE,
    ))
    covered: set[str] = set()
    seen_assessments: set[str] = set()
    required_count = 0
    for i, header in enumerate(headers):
        identifier, title_text = header.groups()
        stop = headers[i + 1].start() if i + 1 < len(headers) else len(completion)
        block = completion[header.end():stop]
        if not identifier.startswith(code + "-"):
            errors.append(f"assessment ID {identifier} does not match course {code}")
        if identifier in seen_assessments:
            errors.append(f"duplicate assessment ID {identifier}")
        seen_assessments.add(identifier)
        fields = {}
        for line in block.splitlines():
            field = FIELD_RE.match(line)
            if field:
                fields[field.group(1).lower()] = field.group(2).strip()
        optional = bool(re.search(r"\boptional\b", title_text, re.IGNORECASE))
        if optional:
            continue
        required_count += 1
        for field_name in ("outcomes", "work", "criteria", "evidence"):
            if not fields.get(field_name):
                errors.append(f"{identifier}: missing or empty {field_name} field")
        refs = re.findall(rf"\b{re.escape(code)}-O[1-9]\d*\b", fields.get("outcomes", ""))
        if not refs:
            errors.append(f"{identifier}: no valid course outcomes referenced")
        for ref in refs:
            if ref not in defined_outcomes:
                errors.append(f"{identifier}: unknown course outcome {ref}")
            else:
                covered.add(ref)
        # Cross-course outcome references in the same field are invalid.
        for ref in re.findall(r"\b[A-Z]{2,6}[1-9]\d*-O[1-9]\d*\b", fields.get("outcomes", "")):
            if not ref.startswith(code + "-"):
                errors.append(f"{identifier}: foreign outcome reference {ref}")

    if not required_count:
        errors.append("no required summative assessments found")
    if len(headers) == 0:
        errors.append("assessment definitions must use stable 'CODE-AS#' IDs")
    for outcome in sorted(defined_outcomes - covered):
        errors.append(f"required course outcome {outcome} has no required summative assessment")

    if kind == "project":
        if "deliverable" not in completion.lower():
            errors.append("project course requires public deliverables")
        if "defense" not in completion.lower():
            errors.append("project course requires a reviewable technical defense")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all", action="store_true", help="check migrated or explicitly version-marked course files")
    group.add_argument("--course", action="append", type=Path, help="check a specific file; repeat for multiple files")
    args = parser.parse_args()

    if args.all:
        files = sorted(
            path for path in (ROOT / "curriculum").rglob("*.md")
            if re.fullmatch(r"[A-Z]{2,6}[1-9]\d*\.md", path.name)
        )
    else:
        files = [path.resolve() for path in args.course]

    checked = skipped = 0
    errors = []
    for path in files:
        if not path.is_file():
            errors.append(f"{path}: file does not exist")
            continue
        content = path.read_text(encoding="utf-8")
        if args.all and not (VERSION_RE.search(content) or ID_HINT_RE.search(content)):
            skipped += 1
            continue
        checked += 1
        for failure in validate_course(path):
            try:
                label = str(path.relative_to(ROOT))
            except ValueError:
                label = str(path)
            errors.append(f"{label}: {failure}")

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print(
        f"OEE v0.2.0 structural check: {checked} checked, {skipped} legacy skipped, "
        f"{len(errors)} errors; substantive pedagogical review still required."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
