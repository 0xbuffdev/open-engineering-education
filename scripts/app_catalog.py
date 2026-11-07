"""Parse the authoritative APP Markdown catalog without treating numeric IDs as order.

The public program README remains the sole source of classification,
readiness label, prerequisite display, and learner sequence.
This module is an internal validation adapter, not an OEE specification
or a second course manifest.
"""

from dataclasses import dataclass
from pathlib import Path
import re


COURSE_CODE_RE = re.compile(r"APP[1-9]\d*")
COURSE_LINK_RE = re.compile(r"\[(APP[1-9]\d*)\]\(\1\.md\)")
ENTRY_RE = re.compile(r"(Core|Elective) · (draft|tested|verified)")
RANGE_RE = re.compile(r"\bAPP([1-9]\d*)\s*[–—-]\s*APP([1-9]\d*)\b")
MAX_RANGE = 100


@dataclass(frozen=True)
class APPEntry:
    code: str
    title: str
    duration: str
    prerequisites: str
    kind: str
    classification: str
    status: str


def prerequisite_codes(source: str) -> list[str]:
    """Resolve APP number ranges and de-duplicate linked/plain references.

    For example, the catalog uses APP1–APP8, while course metadata
    often links APP1.md through APP8.md separately.
    """
    def expand(match: re.Match[str]) -> str:
        low, high = map(int, match.groups())
        if high < low or high - low > MAX_RANGE:
            raise ValueError(f"invalid APP prerequisite range {match.group(0)}")
        return ", ".join(f"APP{i}" for i in range(low, high + 1))

    expanded = RANGE_RE.sub(expand, source)
    return list(dict.fromkeys(COURSE_CODE_RE.findall(expanded)))


def read_app_catalog(path: Path) -> tuple[list[APPEntry], list[str]]:
    """Read the APP course table, rejecting unparseable/duplicate course rows."""
    errors: list[str] = []
    entries: list[APPEntry] = []
    if not path.exists():
        return entries, ["APP catalog: missing README.md"]
    text = path.read_text(encoding="utf-8")
    marker = "\n## Courses\n"
    if marker not in text:
        return entries, ["APP catalog: missing Courses section"]
    section = text.split(marker, 1)[1].split("\n## ", 1)[0]
    seen: set[str] = set()
    for line in section.splitlines():
        if not line.lstrip().startswith("| [APP"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 6:
            errors.append(f"APP catalog: malformed course row: {line}")
            continue
        link = COURSE_LINK_RE.fullmatch(cells[0])
        if not link:
            errors.append(f"APP catalog: invalid course link: {cells[0]}")
            continue
        code = link.group(1)
        if code in seen:
            errors.append(f"APP catalog: duplicate course row {code}")
            continue
        seen.add(code)
        kind = re.fullmatch(r"\x60(course|project)\x60", cells[4])
        label = cells[5].removeprefix("**").removesuffix("**")
        status = ENTRY_RE.fullmatch(label)
        if not kind or not status or not all(cells[i] for i in (1, 2, 3)):
            errors.append(f"APP catalog: incomplete metadata for {code}")
            continue
        try:
            prerequisite_codes(cells[3])
        except ValueError as exc:
            errors.append(f"APP catalog: {code}: {exc}")
            continue
        entries.append(APPEntry(
            code=code,
            title=cells[1],
            duration=cells[2],
            prerequisites=cells[3],
            kind=kind.group(1),
            classification=status.group(1).lower(),
            status=status.group(2),
        ))
    if not entries:
        errors.append("APP catalog: no course rows found")
    codes = {entry.code for entry in entries}
    core = [entry for entry in entries if entry.classification == "core"]
    if not core:
        errors.append("APP catalog: at least one core course required")
    if entries and entries[0].code != "APP1":
        errors.append("APP catalog: APP1 must remain the entry course")
    if "APP9" not in codes:
        errors.append("APP catalog: missing APP9 graduation capstone")
    else:
        cap = next(entry for entry in entries if entry.code == "APP9")
        if cap.kind != "project" or cap.classification != "core":
            errors.append("APP catalog: APP9 must be a core project")
        if core and core[-1].code != "APP9":
            errors.append("APP catalog: APP9 must be last among core courses")
    if any(entry.classification == "elective" for entry in entries[:len(core)]):
        errors.append("APP catalog: core courses must precede elective rows")
    return entries, errors
