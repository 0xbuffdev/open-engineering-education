#!/usr/bin/env python3
"""Validate the nine draft APP core courses and seven elective drafts."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "curriculum" / "APP"
CORE_CODES = {f"APP{i}" for i in range(1, 10)}
ELECTIVE_CODES = {f"APP{i}" for i in range(10, 17)}
CODES = CORE_CODES | ELECTIVE_CODES
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
        errors.append("APP: expected APP1.md through APP16.md")
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
        title_match = re.search(r"^# (APP\d+) — ([^\n]+)$", data, re.M)
        duration_match = re.search(r"^\*\*Duration:\*\* ([^\n]+)$", data, re.M)
        if not title_match or not duration_match:
            errors.append(f"{code}: title and duration required")
        else:
            catalog = (APP / "README.md").read_text(encoding="utf-8")
            row = next((line for line in catalog.splitlines() if line.startswith(f"| [{code}]({code}.md) |")), "")
            if not row or f"| {title_match.group(2)} | {duration_match.group(1)} |" not in row:
                errors.append(f"{code}: title/duration differ from catalog")
        if code in ELECTIVE_CODES and f"**Classification:** {TICK}elective{TICK}" not in data:
            errors.append(f"{code}: expected elective classification")
        if code in CORE_CODES and "**Classification:** `elective`" in data:
            errors.append(f"{code}: core course cannot be an elective")
        if re.findall(r"^## (.+)$", data, re.M) != REQUIRED:
            errors.append(f"{code}: required sections must be ordered")
        if re.search(r"\b[BR][0-9]{1,3}\b|^## Course brief|^### Resource map", data, re.M):
            errors.append(f"{code}: private resource references or obsolete headings")
        sections = list(re.finditer(r"^### Module (\d+) — (.+)$", data, re.M))
        if not sections:
            errors.append(f"{code}: at least one module required; no fixed module cap")
        for i, m in enumerate(sections):
            if int(m.group(1)) != i + 1:
                errors.append(f"{code}: module numbering")
            end = sections[i+1].start() if i+1 < len(sections) else data.index("## Completion requirements")
            section = data[m.start():end]
            if section.count("#### Outcomes") != 1 or section.count("#### Lessons") != 1:
                errors.append(f"{code} module {i+1}: missing Outcomes/Lessons headings")
            if "#### Outcomes" in section and "#### Lessons" in section:
                outcomes = section.split("#### Outcomes", 1)[1].split("#### Lessons", 1)[0]
                if not re.search(r"^- .+", outcomes, re.M):
                    errors.append(f"{code} module {i+1}: measurable module outcomes missing")
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
            if code == "APP1":
                # Every APP1 module has one purposeful checkpoint preceding
                # its lab. No assumption about future module/lesson counts.
                kinds = [e[2] for e in entries]
                if kinds.count("test") != 1 or kinds.count("lab") != 1:
                    errors.append(f"APP1 module {i+1}: one test and lab required")
                elif kinds.index("test") > kinds.index("lab"):
                    errors.append(f"APP1 module {i+1}: test must precede lab")
            if i == len(sections)-1 and entries and entries[-1][2] != "lab":
                errors.append(f"{code}: final integration lab missing")
        completion = data.split("## Completion requirements", 1)[-1]
        if not re.search(r"\*\*Final integration lab — [^\n]+:\*\*", completion):
            errors.append(f"{code}: final lab brief missing")
        if code == "APP1":
            # These checks assert the published assessment contract, not
            # executed network behavior or readiness beyond 'draft'.
            checkpoint_headers = list(re.finditer(
                r"^\*\*Module (\d+) — [^\n]+: checkpoint\*\* — Required assessment details$",
                completion, re.M,
            ))
            lab_headers = list(re.finditer(
                r"^\*\*Module (\d+) — [^\n]+: required lab\*\* — Required assessment details$",
                completion, re.M,
            ))
            expected = list(range(1, len(sections) + 1))
            if [int(h.group(1)) for h in checkpoint_headers] != expected:
                errors.append("APP1: checkpoints must match the actual modules in order")
            if [int(h.group(1)) for h in lab_headers] != expected:
                errors.append("APP1: lab contracts must match the actual modules in order")
            for index, heading in enumerate(checkpoint_headers):
                if index >= len(lab_headers):
                    break
                lab_heading = lab_headers[index]
                if int(heading.group(1)) != int(lab_heading.group(1)):
                    continue
                if heading.start() >= lab_heading.start():
                    errors.append(f"APP1 module {heading.group(1)}: checkpoint must precede lab")
                    continue
                questions = completion[heading.end():lab_heading.start()]
                if len(re.findall(r"^- \*\*Q[12] \(free\):\*\*", questions, re.M)) != 2:
                    errors.append(f"APP1 module {heading.group(1)}: expected two explained questions")
                if questions.count("Expected answer and scoring:") != 2:
                    errors.append(f"APP1 module {heading.group(1)}: answer guidance missing")
            for i, heading in enumerate(lab_headers):
                end = lab_headers[i+1].start() if i+1 < len(lab_headers) else len(completion)
                lab = completion[heading.end():end]
                for field in ("Objective", "Prerequisites", "Environment", "Procedure",
                              "Expected result", "Verification", "Evidence",
                              "Failure analysis", "Acceptance"):
                    if f"- **{field}:**" not in lab:
                        errors.append(f"APP1 module {heading.group(1)}: missing lab {field.lower()}")
            # APP1 now teaches the browser-loading journey without requiring
            # a learner-written backend or JavaScript. These are smoke checks,
            # not proof that the educational scope is complete or tested.
            for required in ("127.0.0.1", "DNS", "TLS", "304", "CORS",
                             "hosting", "browser", "layout", "paint",
                             "compositing", "no paid service"):
                if required.lower() not in data.lower():
                    errors.append(f"APP1: missing web-foundations scope or safety term: {required}")
            prohibited = (
                "Build and defend an HTTP service without and with a framework",
                "Build and test a small HTTP service",
            )
            for obsolete in prohibited:
                if obsolete in data:
                    errors.append(f"APP1: obsolete backend implementation requirement: {obsolete}")
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
    for index, title in enumerate(ELECTIVES, 10):
        code = f"APP{index}"
        line = next((x for x in catalog.splitlines() if x.startswith("|") and title in x), "")
        if f"[{code}]({code}.md)" not in line or "**Elective · draft**" not in line:
            errors.append(f"APP catalog: missing linked draft elective {code}: {title}")
    if catalog.count("**Elective · draft**") != len(ELECTIVES):
        errors.append("APP catalog: exactly seven elective drafts expected")
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
    modules = sum(len(re.findall(r"^### Module \d+ — ", file.read_text(encoding="utf-8"), re.M)) for file in files)
    print(f"APP structural validation passed: {len(CORE_CODES)} core, {len(ELECTIVE_CODES)} electives, {modules} modules; no fixed module cap")
    return 0

if __name__ == "__main__":
    sys.exit(validate())
