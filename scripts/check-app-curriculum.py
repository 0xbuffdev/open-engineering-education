#!/usr/bin/env python3
"""Validate the nine draft APP core courses and listed proposed electives."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "curriculum" / "APP"
CODES = {f"APP{i}" for i in range(1, 10)}
REQUIRED = ["Overview", "Learning outcomes", "Modules", "Completion requirements"]
ELECTIVES = [
    "Advanced Frontend Performance", "Advanced Backend Architecture",
    "Realtime Systems", "Mobile Application Engineering",
    "API Gateways & Edge Delivery",
    "Advanced TypeScript/Rust Application Development",
    "Platform Engineering",
]
TICK = chr(96)

def validate():
    errors = []
    files = sorted(APP.glob("APP[0-9]*.md"))
    if {p.stem for p in files} != CODES:
        errors.append("APP: expected APP1.md through APP9.md")
    dependencies = {}
    for file in files:
        code = file.stem
        data = file.read_text(encoding="utf-8")
        if not data.startswith(f"# {code} — "):
            errors.append(f"{code}: heading mismatch")
        if "**Program:** APP — Application Engineering" not in data:
            errors.append(f"{code}: incorrect program")
        kind = "project" if code == "APP9" else "course"
        if f"**Type:** {TICK}{kind}{TICK}" not in data:
            errors.append(f"{code}: incorrect type")
        if f"**Status:** {TICK}draft{TICK}" not in data:
            errors.append(f"{code}: expected draft status")
        if re.findall(r"^## (.+)$", data, re.M) != REQUIRED:
            errors.append(f"{code}: required sections must be ordered")
        if re.search(r"\b[BR][0-9]{1,3}\b|^## Course brief|^### Resource map", data, re.M):
            errors.append(f"{code}: private resource references or obsolete headings")
        sections = list(re.finditer(r"^### Module (\d+) — (.+)$", data, re.M))
        if len(sections) != 5:
            errors.append(f"{code}: expected five imported modules")
        for i, m in enumerate(sections):
            if int(m.group(1)) != i + 1:
                errors.append(f"{code}: module numbering")
            end = sections[i+1].start() if i+1 < len(sections) else data.index("## Completion requirements")
            section = data[m.start():end]
            if section.count("#### Outcomes") != 1 or section.count("#### Lessons") != 1:
                errors.append(f"{code} module {i+1}: missing Outcomes/Lessons headings")
            entries = re.findall(
                r"^(\d+)\. \*\*([^\n]+?)\*\* — " + TICK + r"(lesson|test|lab)" + TICK + r"[ \t]*$",
                section, re.M,
            )
            candidates = re.findall(
                r"^\d+\. \*\*[^\n]+?\*\* — " + TICK + r"(lesson|test|lab)" + TICK + r"[^\n]*$",
                section, re.M,
            )
            if not entries or len(candidates) != len(entries):
                errors.append(f"{code} module {i+1}: missing entries or trailing comments")
            if [int(e[0]) for e in entries] != list(range(1, len(entries)+1)):
                errors.append(f"{code} module {i+1}: nonsequential lessons")
            if i == 0 and entries and not entries[0][1].startswith("Course introduction:"):
                errors.append(f"{code}: first lesson must orient the learner")
            if i == len(sections)-1 and entries and entries[-1][2] != "lab":
                errors.append(f"{code}: final integration lab missing")
        completion = data.split("## Completion requirements", 1)[-1]
        if "**Final integration lab — required work:**" not in completion:
            errors.append(f"{code}: final lab brief missing")
        if code == "APP9":
            if "**Project defense:**" not in completion or "graduation requirement" not in completion:
                errors.append("APP9: project defense or graduation requirement missing")
        elif "**Exit demonstration:**" not in completion:
            errors.append(f"{code}: exit demonstration missing")
        match = re.search(r"^\*\*Prerequisites:\*\* (.+)$", data, re.M)
        source = match.group(1) if match else ""
        deps = re.findall(r"\bAPP[0-9]+\b", source)
        dependencies[code] = deps
        if any(dep not in CODES or dep == code for dep in deps):
            errors.append(f"{code}: invalid APP prerequisite")
        if code == "APP1" and "SEF10" not in source:
            errors.append("APP1: expected SEF10 entry prerequisite")
        for href in re.findall(r"\]\(([^)]+\.md)\)", data):
            if "://" not in href and not (file.parent / href).resolve().is_file():
                errors.append(f"{code}: broken internal link {href}")

    catalog_path = APP / "README.md"
    catalog = catalog_path.read_text(encoding="utf-8") if catalog_path.exists() else ""
    for code in CODES:
        if f"[{code}]({code}.md)" not in catalog:
            errors.append(f"APP catalog: missing core course {code}")
    for title in ELECTIVES:
        line = next((x for x in catalog.splitlines() if x.startswith("|") and title in x), "")
        if "**Elective · planned**" not in line:
            errors.append(f"APP catalog: missing planned elective {title}")
    if catalog.count("**Elective · planned**") != len(ELECTIVES):
        errors.append("APP catalog: seven electives expected")
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
            check(dep)
        active.remove(code)
        visited.add(code)
    for code in sorted(CODES):
        check(code)
    if errors:
        print("\n".join("ERROR: " + x for x in errors), file=sys.stderr)
        return 1
    print(f"APP structural validation passed: {len(files)} core drafts and {len(ELECTIVES)} planned electives")
    return 0

if __name__ == "__main__":
    sys.exit(validate())
