"""Single-parser, source-pinned structural inspection and derived export.

Normative course requirements remain OEE Markdown. This module reuses the
source-located checker; it does not implement a second course grammar.
"""

from __future__ import annotations

import json
import re

from . import _outcome_parser
from . import __version__ as TOOL_VERSION
from .source import GitSource, SourceError, VIRTUAL_ROOT

REPOSITORY = "0xbuffdev/open-engineering-education"
RULE_SET_VERSION = "v0.2.0-ot-i04"
SPECIFICATION = "v0.2.0"
CODE_RE = re.compile(r"([A-Z]{2,6})([1-9]\d*)\Z")
PREREQUISITE_TOKEN_RE = re.compile(
    r"\b([A-Z]{2,6})([1-9]\d*)(?:\s*[–—-]\s*([A-Z]{2,6})([1-9]\d*))?\b"
)
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")


def course_path(code: str) -> str:
    match = CODE_RE.fullmatch(code)
    if match is None:
        raise SourceError("unsupported_format", "course must be a canonical OEE code")
    return f"curriculum/{match.group(1)}/{code}.md"


def prerequisites(text: str) -> list[str]:
    """Extract identities only; preserve catalog authority over sequencing."""
    if not text or text.strip().casefold() in ("none", "—", "-"):
        return []
    # Ignore Markdown link destinations, which can repeat the same course ID.
    literal = MARKDOWN_LINK_RE.sub(lambda match: match.group(1), text)
    codes: list[str] = []
    for match in PREREQUISITE_TOKEN_RE.finditer(literal):
        area, start_text, last_area, end_text = match.groups()
        if last_area is None:
            codes.append(f"{area}{start_text}")
            continue
        start, end = int(start_text), int(end_text)
        if area != last_area or end < start or end - start > 99:
            raise SourceError("invalid_reference", "invalid prerequisite course range")
        codes.extend(f"{area}{value}" for value in range(start, end + 1))
    if not codes:
        raise SourceError("invalid_reference", "no resolvable prerequisite course code")
    return list(dict.fromkeys(codes))


def finding(rule: str, category: str, message: str, path: str, line: int = 1) -> dict:
    return {
        "code": rule, "category": category, "severity": "error",
        "message": message, "location": {"path": path, "line": line},
    }


def outcome(findings: list[dict]) -> str:
    categories = {item["category"] for item in findings}
    if categories.intersection({"structural_violation", "invalid_reference",
                                "unsafe_reference", "tool_error"}):
        return "failed"
    if categories:
        return "incomplete"
    return "passed"


def inspect(source: GitSource, code: str) -> tuple[dict, dict | None]:
    path = course_path(code)
    address = {
        "repository": REPOSITORY,
        "revision": source.revision,
        "specification": SPECIFICATION,
        "coursePath": path,
    }
    diagnostics = []
    extracted: dict = {}
    performed = []
    skipped = []
    try:
        content = source.read_file(path)
        parser = _outcome_parser
        try:
            supported = parser.is_outcome_course(content)
        except ValueError as exc:
            supported = False
            diagnostics.append(finding("OEE034", "unsupported_format", str(exc), path))
        if supported:
            performed.append("v0.2.0-structure")
            virtual = source.virtual_path(path)
            findings = parser.parse_structure(
                virtual, content, VIRTUAL_ROOT, capture=extracted,
                read_link=source.brief, format_path=source.label,
            )
            diagnostics.extend(item.to_dict() for item in findings)
            if extracted.get("code") and extracted["code"] != code:
                diagnostics.append(finding("OET001", "invalid_reference",
                                           "course heading identity disagrees with course path", path))
            try:
                related = prerequisites(extracted.get("prerequisitesText", ""))
                extracted["prerequisites"] = related
                for requirement in related:
                    if requirement == code:
                        diagnostics.append(finding("OET002", "invalid_reference",
                                                   "a course cannot require itself", path))
                    else:
                        # The prerequisite is a source identity, not a
                        # declaration that the legacy course conforms.
                        source.read_file(course_path(requirement))
            except SourceError as exc:
                diagnostics.append(finding("OET003", exc.category,
                                           f"prerequisite reference unresolved: {exc}", path))
        else:
            skipped.append({"check": "v0.2.0-structure", "reason": "unsupported_format"})
            if not diagnostics:
                diagnostics.append(finding("OEE034", "unsupported_format",
                                           "unsupported old course format (v0.2.0 required)", path))
    except SourceError as exc:
        diagnostics.append(finding("OET004", exc.category, str(exc), exc.path or path))
        skipped.append({"check": "v0.2.0-structure", "reason": exc.category})
    report = {
        "toolVersion": TOOL_VERSION,
        "ruleSetVersion": RULE_SET_VERSION,
        "source": address,
        "scope": "course",
        "checksPerformed": performed,
        "checksSkipped": skipped,
        "findings": diagnostics,
        "structuralOutcome": outcome(diagnostics),
        "manualReviewRequired": True,
    }
    return report, extracted if report["structuralOutcome"] == "passed" else None


def course_payload(data: dict) -> dict:
    """Build once from canonical parser capture; version-specific envelopes
    must never reinterpret academic outcomes, assessments or criteria.
    """
    coverage = {
        item["id"]: sorted(set(data["coverage"].get(item["id"], [])))
        for item in data["outcomes"]
    }
    return {
        "course": {
            "code": data["code"],
            "program": CODE_RE.fullmatch(data["code"]).group(1),
            "type": data["type"],
            "status": data["status"],
            "prerequisites": data["prerequisites"],
        },
        "outcomes": data["outcomes"],
        "assessments": data["assessments"],
        "modules": data["modules"],
        "coverage": coverage,
        "validation": {"structural": "passed", "manualReviewRequired": True},
    }


def export_course(source: GitSource, code: str) -> dict:
    """Internal pinned-Git golden source exporter, not the consumer CLI."""
    report, data = inspect(source, code)
    if data is None:
        raise ExportBlocked(report)
    return {
        "exportVersion": 1,
        "source": report["source"],
        **course_payload(data),
    }


def canonical_json(value: dict) -> bytes:
    return (json.dumps(value, sort_keys=True, ensure_ascii=False,
                       separators=(",", ":")) + "\n").encode("utf-8")


class ExportBlocked(Exception):
    def __init__(self, report: dict):
        self.report = report
        super().__init__("source inspection not structurally passed")
