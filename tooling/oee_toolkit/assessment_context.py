"""Source-bound assessment review envelope; not a second academic parser.

The complete verified source remains the authority, including multiline
fields, shared prose and linked briefs. Reviewed ranges are navigation and
applicability metadata for one exact source revision, not new requirements.
"""
from __future__ import annotations

from .core import ExportBlocked, canonical_json
from .release_source import (
    ReleaseSource, inspect_release, release_course_payload, sha256,
)

# Review of the published SEF1 source, not a mutable course-code rule.
# All ranges use one-based inclusive LF-delimited source lines. If any byte
# changes, the index is NOT applied; a new academic source review is required.
_SEF1_SHA256 = "87f557cac53f6d3aebfe0c808858b620acae7b3a8d50ea5ea468a0e2c2b953bb"
_SEF1_ASSESSMENTS = ("SEF1-AS1", "SEF1-AS2", "SEF1-AS3")
_SEF1_RANGES = (
    ("completion-rules", 172, 192, _SEF1_ASSESSMENTS),
    ("shared-rules", 194, 212, _SEF1_ASSESSMENTS),
    ("shared-rules", 214, 273, ("SEF1-AS3",)),
    ("assessment-definition", 277, 297, ("SEF1-AS1",)),
    ("assessment-definition", 299, 327, ("SEF1-AS2",)),
    ("assessment-definition", 329, 362, ("SEF1-AS3",)),
    ("optional-practice", 364, 388, ()),
    ("completion-rules", 390, 398, _SEF1_ASSESSMENTS),
)


def _lines(text: str) -> list[str]:
    # Do not split on Unicode separators or normalize CRLF. These are the
    # actual LF-delimited source lines, including their original terminators.
    parts = text.split("\n")
    return [part + "\n" for part in parts[:-1]] + ([parts[-1]] if parts[-1] else [])


def _document(source: ReleaseSource, path: str) -> dict:
    text = source.read_file(path)
    return {
        "path": path,
        "sha256": source.course_sha256(path),
        "startLine": 1,
        "endLine": len(_lines(text)),
        "markdown": text,
    }


def export_assessment_context(source: ReleaseSource, code: str) -> dict:
    report, data = inspect_release(source, code)
    if data is None:
        raise ExportBlocked(report)
    course = release_course_payload(report, data)
    identity = course["source"]
    path = identity["coursePath"]
    # The parser resolves explicit required-assessment brief references using
    # the same verified release. Never scrape unrelated links or use Git.
    briefs = data["assessmentBriefs"]
    documents = [_document(source, path)]
    documents.extend(_document(source, p) for p in sorted(set(briefs.values()) - {path}))
    assessments = [
        {
            "assessmentId": item["id"],
            "sourcePaths": [path] + ([briefs[item["id"]]]
                                    if item["id"] in briefs and briefs[item["id"]] != path
                                    else []),
        }
        for item in course["assessments"] if item["required"]
    ]
    ranges = []
    indexed = (
        code == "SEF1" and identity["courseSha256"] == _SEF1_SHA256
        and tuple(a["assessmentId"] for a in assessments) == _SEF1_ASSESSMENTS
        and not briefs
    )
    if indexed:
        lines = _lines(documents[0]["markdown"])
        for kind, start, end, ids in _SEF1_RANGES:
            excerpt = "".join(lines[start - 1:end])
            ranges.append({
                "kind": kind,
                "location": {"path": path, "startLine": start, "endLine": end},
                "assessmentIds": list(ids),
                "sha256": sha256(excerpt.encode("utf-8")),
            })
    payload = {
        "contextVersion": 1,
        "source": identity,
        "toolkit": course["toolkit"],
        "courseExportSha256": sha256(canonical_json(course)),
        "documents": documents,
        "assessments": assessments,
        "reviewedRanges": ranges,
        "applicability": "source-indexed" if indexed else "manual-resolution-required",
        "manualReviewRequired": True,
    }
    return {**payload, "contextSha256": sha256(canonical_json(payload))}
