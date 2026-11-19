#!/usr/bin/env python3
"""Structural inspection for outcome-driven OEE v0.2.0 courses.

This is a repository maintenance checker, not an official Toolkit release.
Its parser is the single source of structural findings for the text CLI,
JSON diagnostics, and existing program/inventory validation callers.

Only current OEE v0.2.0 sources can pass. Structural success does not
establish pedagogy, graded learner achievement, or course conformance.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from course_format_versions import is_outcome_course

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
OUTCOME_RE = re.compile(r"^[ \t]*-[ \t]+\*\*([A-Z]{2,6}[1-9]\d*-O[1-9]\d*):\*\*[ \t]*(.*?)\s*$")
ASSESSMENT_RE = re.compile(r"^[ \t]*-[ \t]+\*\*([A-Z]{2,6}[1-9]\d*-AS[1-9]\d*)\*\*(.*)$", re.MULTILINE)
FIELD_RE = re.compile(
    r"^[ \t]*-[ \t]+(?:\*\*)?(Outcomes|Work|Criteria|Evidence):(?:\*\*)?[ \t]*(.*?)\s*$",
    re.IGNORECASE,
)
LINK_RE = re.compile(r"\[[^\]\n]+\]\(([^)\n]+)\)")
ID_REF_RE = re.compile(r"\b[A-Z]{2,6}[1-9]\d*-O[1-9]\d*\b")
LESSON_RE = re.compile(r"^(\d+)\.[ \t]+\S", re.MULTILINE)


def line_at(text: str, offset: int) -> int:
    """Return an actual one-based source line, not a guessed module index."""
    return text.count("\n", 0, offset) + 1


def display_path(path: Path) -> str:
    """Avoid machine-dependent absolute paths in JSON inspection output."""
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return path.name


class Finding:
    """Immutable-in-practice diagnostic; safe for existing direct module loaders."""

    __slots__ = ("code", "category", "message", "path", "line", "severity")

    def __init__(self, code: str, category: str, message: str,
                 path: str, line: int, severity: str = "error") -> None:
        self.code = code
        self.category = category
        self.message = message
        self.path = path
        self.line = line
        self.severity = severity

    def to_dict(self) -> dict:
        return {
            "code": self.code,
            "category": self.category,
            "severity": self.severity,
            "message": self.message,
            "location": {"path": self.path, "line": self.line},
        }


def outcome_of(findings: list[Finding]) -> str:
    if any(f.category in ("structural_violation", "unsafe_reference", "invalid_reference", "tool_error")
           for f in findings):
        return "failed"
    if any(f.category in ("unsupported_format", "missing_input", "parser_limitation")
           for f in findings):
        return "incomplete"
    return "passed"


def section_range(text: str, heading: str) -> tuple[int, int] | None:
    sections = list(SECTION_RE.finditer(text))
    for i, match in enumerate(sections):
        if match.group(1).strip() == heading:
            return match.end(), (sections[i + 1].start() if i + 1 < len(sections) else len(text))
    return None


def block_after_heading(text: str, heading: str) -> str:
    """Shared selector retained for the inventory's derived coverage report."""
    section = section_range(text, heading)
    return text[section[0]:section[1]] if section else ""


def brief_reference(title: str, body: str) -> tuple[str | None, bool]:
    """Identify the supported explicit local assessment-brief link presentation.

    A link on the assessment heading or a line named 'Brief' is recognized.
    We do not infer assessment authority from unrelated resource links.
    """
    items = LINK_RE.findall(title)
    for line in body.splitlines():
        if re.match(r"^[ \t]*-[ \t]+(?:\*\*)?(?:Assessment[ \t]+)?Brief(?:\*\*)?:", line, re.I):
            items.extend(LINK_RE.findall(line))
    return (items[0] if len(items) == 1 else None), len(items) > 1


def read_brief(raw: str, owner: Path, root: Path) -> tuple[str | None, Path | None, str | None]:
    """Resolve relative public Markdown inside the authorized source tree.

    An external URL is an unsupported parser input, not an OEE violation.
    Symlink escapes and absolute filesystem paths are unsafe references.
    """
    if raw.startswith(("/", "\\")) or "\\" in raw:
        return None, None, "unsafe_reference"
    parts = urlsplit(raw)
    if parts.scheme or parts.netloc:
        return None, None, "parser_limitation"
    if parts.query:
        return None, None, "parser_limitation"
    relative = unquote(parts.path)
    if not relative or not relative.endswith(".md") or "\x00" in relative:
        return None, None, "parser_limitation"
    if relative.startswith("/") or "\\" in relative:
        return None, None, "unsafe_reference"
    candidate = (owner.parent / relative).resolve()
    if not candidate.is_relative_to(root.resolve()):
        return None, candidate, "unsafe_reference"
    if not candidate.is_file():
        return None, candidate, "missing_input"
    try:
        return candidate.read_text(encoding="utf-8"), candidate, None
    except (OSError, UnicodeError):
        return None, candidate, "missing_input"


def fields_in(text: str, base_line: int, source: Path,
              format_path=display_path) -> dict[str, tuple[str, str, int]]:
    found = {}
    for number, row in enumerate(text.splitlines(), start=base_line):
        match = FIELD_RE.match(row)
        if match:
            found[match.group(1).lower()] = (match.group(2).strip(), format_path(source), number)
    return found


def parse_structure(path: Path, text: str, root: Path, *,
                    capture: dict | None = None, read_link=None,
                    format_path=None) -> list[Finding]:
    """Single structural interpretation for inspection and derived export.

    Optional capture and read_link hooks are for Git-pinned Toolkit consumers;
    the repository's existing maintenance callers retain worktree behavior.
    """
    found: list[Finding] = []
    format_path = format_path or display_path
    read_link = read_link or read_brief
    label = format_path(path)

    def add(code: str, message: str, offset: int = 0,
            category: str = "structural_violation", source: Path | None = None,
            source_line: int | None = None) -> None:
        found.append(Finding(
            code, category, message,
            format_path(source) if source else label,
            source_line if source_line is not None else line_at(text, offset),
        ))

    title = COURSE_RE.match(text)
    if title is None:
        add("OEE001", "expected a first-line course heading, e.g. '# APP1 — Course title'")
        return found
    code = title.group(1)
    first_section = SECTION_RE.search(text)
    metadata = text[:first_section.start()] if first_section else text
    for key in ("Type", "Prerequisites", "Duration", "Status"):
        if not re.search(rf"^\*\*{key}:\*\*\s*\S", metadata, re.MULTILINE):
            add("OEE002", f"missing {key} metadata")
    kind_match = re.search(r"^\*\*Type:\*\*\s*`?(course|project)`?\s*$",
                           metadata, re.MULTILINE)
    if not kind_match:
        add("OEE003", "Type must be 'course' or 'project'")
    kind = kind_match.group(1) if kind_match else ""
    if not re.search(r"(?m)^\*\*Status:\*\*\s*`?(draft|tested|verified)`?\s*$",
                     metadata):
        add("OEE036", "Status must be 'draft', 'tested', or 'verified'")
    metadata_value = lambda key: (
        match.group(1).strip()
        if (match := re.search(rf"(?m)^\*\*{key}:\*\*\s*(.+)$", metadata))
        else ""
    )
    if capture is not None:
        capture.update({
            "code": code,
            "program": metadata_value("Program").split(" — ", 1)[0].strip(),
            "type": kind,
            "status": metadata_value("Status").strip("`"),
            "prerequisitesText": metadata_value("Prerequisites"),
            "outcomes": [],
            "assessments": [],
            "modules": [],
            "coverage": {},
        })

    headings = list(SECTION_RE.finditer(text))
    heading_names = [m.group(1).strip() for m in headings]
    indices = [heading_names.index(h) for h in REQUIRED_SECTIONS if h in heading_names]
    if len(indices) != len(REQUIRED_SECTIONS) or indices != sorted(indices):
        add("OEE004", "four required top-level sections are missing or out of order",
            first_section.start() if first_section else 0)
    for heading in REQUIRED_SECTIONS:
        if heading_names.count(heading) > 1:
            add("OEE004", f"duplicate required top-level section {heading}")

    learning = section_range(text, "Learning outcomes")
    outcomes: dict[str, int] = {}
    if learning:
        start, end = learning
        cursor = start
        for row in text[start:end].splitlines(keepends=True):
            if re.match(r"^[ \t]*-[ \t]+", row):
                match = OUTCOME_RE.match(row.rstrip("\r\n"))
                if not match:
                    add("OEE005", "every course outcome bullet must have a stable 'CODE-O#' ID",
                        cursor)
                else:
                    identifier, desc = match.groups()
                    if not identifier.startswith(code + "-"):
                        add("OEE006", f"outcome ID {identifier} does not match course {code}",
                            cursor)
                    if identifier in outcomes:
                        add("OEE007", f"duplicate outcome ID {identifier}", cursor)
                    if not desc.strip():
                        add("OEE008", f"outcome {identifier} lacks an observable description",
                            cursor)
                    outcomes[identifier] = cursor
                    if capture is not None:
                        capture["outcomes"].append({
                            "id": identifier,
                            "description": desc.strip(),
                            "location": {"path": label, "line": line_at(text, cursor)},
                        })
            cursor += len(row)
    if not outcomes:
        add("OEE009", "no stable course outcome IDs defined",
            learning[0] if learning else 0)

    modules = section_range(text, "Modules")
    if modules:
        start, end = modules
        matches = list(MODULE_RE.finditer(text, start, end))
        if not matches:
            add("OEE010", "at least one numbered module is required", start)
        if [int(m.group(1)) for m in matches] != list(range(1, len(matches) + 1)):
            add("OEE011", "module numbering must begin at 1 and be sequential", start)
        for i, match in enumerate(matches):
            module_end = matches[i + 1].start() if i + 1 < len(matches) else end
            chunk_start = match.end()
            chunk = text[chunk_start:module_end]
            outcomes_heading = re.search(r"(?m)^#### Outcomes[ \t]*$", chunk)
            lessons_heading = re.search(r"(?m)^#### Lessons[ \t]*$", chunk)
            module_number = match.group(1)
            if not outcomes_heading or not lessons_heading or outcomes_heading.start() >= lessons_heading.start():
                add("OEE012", f"module {module_number}: requires Outcomes followed by Lessons",
                    match.start())
                continue
            o_start = chunk_start + outcomes_heading.end()
            o_end = chunk_start + lessons_heading.start()
            o_text = text[o_start:o_end]
            if not re.search(r"(?m)^[ \t]*-[ \t]+\S", o_text):
                add("OEE013", f"module {module_number}: outcomes are empty", o_start)
            for ref in ID_REF_RE.finditer(o_text):
                ident = ref.group()
                if ident not in outcomes:
                    add("OEE014", f"module {module_number}: unknown course outcome {ident}",
                        o_start + ref.start())
            l_start = chunk_start + lessons_heading.end()
            lessons = text[l_start:module_end]
            lesson_matches = list(LESSON_RE.finditer(lessons))
            numbers = [int(m.group(1)) for m in lesson_matches]
            if capture is not None:
                capture["modules"].append({
                    "number": int(module_number),
                    "title": match.group(2).strip(),
                    "outcomeIds": list(dict.fromkeys(ID_REF_RE.findall(o_text))),
                    "lessons": [
                        {
                            "ordinal": int(item.group(1)),
                            "title": re.sub(r"^\d+\.\s+", "", lessons[item.start():].splitlines()[0]).strip(),
                        }
                        for item in lesson_matches
                    ],
                })
            if not numbers:
                add("OEE015", f"module {module_number}: ordered learning sequence is empty",
                    l_start)
            elif numbers != list(range(1, len(numbers) + 1)):
                add("OEE016", f"module {module_number}: lesson numbering is not sequential",
                    l_start)

    completion = section_range(text, "Completion requirements")
    covered: set[str] = set()
    required_count = 0
    linked_project_details: list[str] = []
    if completion:
        start, end = completion
        headers = list(ASSESSMENT_RE.finditer(text, start, end))
        # Other valid v0.2.0 Markdown representations may have their
        # authoritative assessment requirements in modules or linked briefs.
        # Report a parser limitation rather than a fabricated violation.
        alternate_assessments = not headers and bool(re.search(
            rf"\b{re.escape(code)}-AS[1-9]\d*\b", text
        ))
        if alternate_assessments:
            add("OEE035", "assessment uses an unsupported Markdown presentation",
                start, "parser_limitation")
        seen_assessments = set()
        for i, header in enumerate(headers):
            ident, label_text = header.groups()
            block_end = headers[i + 1].start() if i + 1 < len(headers) else end
            body = text[header.end():block_end]
            if not ident.startswith(code + "-"):
                add("OEE017", f"assessment ID {ident} does not match course {code}",
                    header.start())
            if ident in seen_assessments:
                add("OEE018", f"duplicate assessment ID {ident}", header.start())
            seen_assessments.add(ident)
            link, multiple = brief_reference(label_text, body)
            if multiple:
                add("OEE019", f"{ident}: multiple candidate assessment briefs require review",
                    header.start(), "parser_limitation")
            inline = fields_in(body, line_at(text, header.end()), path,
                               format_path=format_path)
            if link:
                linked, linked_path, reason = read_link(link, path, root)
                if reason:
                    add("OEE020", f"{ident}: {reason} for assessment brief {link}",
                        header.start(), reason)
                elif linked is not None and linked_path is not None:
                    linked_project_details.append(linked)
                    brief_fields = fields_in(linked, 1, linked_path,
                                             format_path=format_path)
                    if not brief_fields:
                        add("OEE021", f"{ident}: linked brief uses an unsupported field presentation",
                            header.start(), "parser_limitation")
                    else:
                        for key, value in brief_fields.items():
                            if key in inline and inline[key][0] != value[0]:
                                add("OEE022", f"{ident}: conflicting inline and linked {key} fields",
                                    header.start(), "invalid_reference")
                            else:
                                inline.setdefault(key, value)
            optional = bool(re.search(r"\boptional\b", label_text, re.I))
            if optional:
                continue
            required_count += 1
            # An unsupported/missing brief means its assessment coverage is unknown,
            # not proof of a false structural requirement or a successful export.
            if link and any(f.code in ("OEE020", "OEE021", "OEE022")
                            and f.message.startswith(ident + ":") for f in found):
                continue
            if multiple:
                continue
            for key in ("outcomes", "work", "criteria", "evidence"):
                if not inline.get(key) or not inline[key][0]:
                    if key in inline and inline[key][1] != label:
                        # Empty fields in a linked brief belong to that source.
                        found.append(Finding(
                            "OEE023", "structural_violation",
                            f"{ident}: missing or empty {key} field",
                            inline[key][1], inline[key][2],
                        ))
                    else:
                        add("OEE023", f"{ident}: missing or empty {key} field", header.start())
            refs = ID_REF_RE.findall(inline.get("outcomes", ("", "", 0))[0])
            if capture is not None:
                assessment_location = (
                    {"path": inline["work"][1], "line": inline["work"][2]}
                    if link and inline.get("work") else
                    {"path": label, "line": line_at(text, header.start())}
                )
                capture["assessments"].append({
                    "id": ident,
                    "required": True,
                    "outcomeIds": list(dict.fromkeys(refs)),
                    "work": inline.get("work", ("", "", 0))[0],
                    "criteria": inline.get("criteria", ("", "", 0))[0],
                    "evidence": inline.get("evidence", ("", "", 0))[0],
                    "location": assessment_location,
                })
            valid_refs = [ref for ref in refs if ref.startswith(code + "-")]
            if not valid_refs:
                add("OEE024", f"{ident}: no valid course outcomes referenced",
                    header.start())
            for ref in refs:
                if not ref.startswith(code + "-"):
                    add("OEE025", f"{ident}: foreign outcome reference {ref}",
                        header.start())
                elif ref not in outcomes:
                    add("OEE026", f"{ident}: unknown course outcome {ref}",
                        header.start())
                else:
                    covered.add(ref)
                    if capture is not None:
                        capture["coverage"].setdefault(ref, []).append(ident)
        if not required_count and not alternate_assessments:
            add("OEE027", "no required summative assessments found", start)
        if not headers and not alternate_assessments:
            add("OEE028", "assessment definitions must use stable 'CODE-AS#' IDs", start)
        for ident in sorted(set(outcomes) - covered):
            # Incomplete brief inspection must not assert an outcome is definitely
            # unassessed; only produce an incomplete outcome for that course.
            ambiguous = any(f.category in ("missing_input", "parser_limitation")
                            for f in found)
            if not ambiguous:
                add("OEE029", f"required course outcome {ident} has no required summative assessment",
                    outcomes[ident])
        if kind == "project":
            # Authoritative linked assessment briefs may provide project details.
            project_details = (text[start:end] + "\n" +
                               "\n".join(linked_project_details)).lower()
            if "deliverable" not in project_details:
                add("OEE030", "project course requires public deliverables", start)
            if "defense" not in project_details:
                add("OEE031", "project course requires a reviewable technical defense", start)
    return found


def inspect_course(path: Path, root: Path | None = None) -> dict:
    """Inspect exactly one source file and expose stable source-located findings."""
    path = path.resolve()
    root = (root or ROOT if path.is_relative_to(ROOT) else path.parent).resolve()
    label = display_path(path)
    findings: list[Finding] = []
    checked = []
    skipped = []
    if not path.is_file():
        findings.append(Finding("OEE032", "missing_input", "course source file does not exist",
                                label, 1))
    else:
        try:
            data = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            findings.append(Finding("OEE033", "missing_input",
                                    f"course source cannot be read: {type(exc).__name__}", label, 1))
        else:
            try:
                supported = is_outcome_course(data)
            except ValueError as exc:
                findings.append(Finding("OEE034", "unsupported_format", str(exc), label, 1))
                supported = False
            if supported:
                checked.append("v0.2.0-structure")
                findings.extend(parse_structure(path, data, root))
            else:
                skipped.append({"check": "v0.2.0-structure", "reason": "unsupported_format"})
                if not findings:
                    findings.append(Finding("OEE034", "unsupported_format",
                                            "unsupported course source; OEE v0.2.0 outcome/assessment format required",
                                            label, 1))
    return {
        "toolVersion": "maintenance-ot-i03",
        "source": {"path": label},
        "scope": "course",
        "checksPerformed": checked,
        "checksSkipped": skipped,
        "findings": [f.to_dict() for f in findings],
        "structuralOutcome": outcome_of(findings),
        "manualReviewRequired": True,
    }


def validate_course(path: Path) -> list[str]:
    """Return current-course inspection findings for repository maintenance."""
    report = inspect_course(path)
    return [finding["message"] for finding in report["findings"]]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all", action="store_true",
                       help="inspect all active courses; unsupported formats yield incomplete")
    group.add_argument("--course", action="append", type=Path,
                       help="inspect one course file; repeat to inspect several")
    parser.add_argument("--format", choices=("text", "json"), default="text",
                        help="human or machine-readable inspection results")
    args = parser.parse_args()
    files = (sorted(path for path in (ROOT / "curriculum").rglob("*.md")
                    if re.fullmatch(r"[A-Z]{2,6}[1-9]\d*\.md", path.name))
             if args.all else [path.resolve() for path in args.course])
    reports = [inspect_course(path) for path in files]
    findings = [f for report in reports for f in report["findings"]]
    outcomes = [report["structuralOutcome"] for report in reports]
    result = ("failed" if "failed" in outcomes else
              "incomplete" if "incomplete" in outcomes else "passed")
    summary = {
        "formatVersion": 1,
        "toolVersion": "maintenance-ot-i03",
        "ruleSetVersion": "maintenance-ot-i03-1",
        "scope": "repository" if args.all else "course",
        "structuralOutcome": result,
        "manualReviewRequired": True,
        "inspectedCourses": len(files),
        "passedCourses": outcomes.count("passed"),
        "failedCourses": outcomes.count("failed"),
        "incompleteCourses": outcomes.count("incomplete"),
        "findings": findings,
        "courses": reports,
    }
    if args.format == "json":
        print(json.dumps(summary, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    else:
        for finding in findings:
            where = finding["location"]
            print(f"ERROR: {where['path']}:{where['line']}: "
                  f"[{finding['code']}/{finding['category']}] {finding['message']}",
                  file=sys.stderr)
        print(f"OEE v0.2.0 structural check: {len(files)} inspected, "
              f"{outcomes.count('passed')} passed, {outcomes.count('incomplete')} incomplete, "
              f"{outcomes.count('failed')} failed; manual pedagogical review required.")
    return {"passed": 0, "failed": 1, "incomplete": 3}[result]


if __name__ == "__main__":
    sys.exit(main())
