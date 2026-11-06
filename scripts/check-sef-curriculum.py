#!/usr/bin/env python3
"""Check the draft SEF course structure and inlined practical requirements.

This structural gate does not assert OEE conformance or learner mastery.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SEF = ROOT / "curriculum" / "SEF"
EXPECTED = {f"SEF{i}" for i in range(1, 11)}
SECTIONS = ["Overview", "Learning outcomes", "Modules", "Completion requirements"]
ERRORS = []
DEPS = {}


def check_links(path, content):
    for href in re.findall(r"\]\(([^)]+)\)", content):
        target = href.split("#", 1)[0].strip()
        if not target.endswith(".md") or "://" in target:
            continue
        if not (path.parent / target).resolve().is_file():
            ERRORS.append(f"{path.relative_to(ROOT)}: missing target {href}")


def validate():
    courses = sorted(SEF.glob("SEF[0-9]*.md"))
    if {p.stem for p in courses} != EXPECTED:
        ERRORS.append("Expected SEF1.md through SEF10.md, exactly")

    for path in courses:
        code = path.stem
        text = path.read_text(encoding="utf-8")
        title_match = re.search(r"^# " + code + r" — (.+)$", text, re.M)
        if not title_match:
            ERRORS.append(f"{code}: heading or code missing")
        catalog = (SEF / "README.md").read_text(encoding="utf-8")
        duration = re.search(r"^\*\*Duration:\*\* (.+)$", text, re.M)
        row = next((line for line in catalog.splitlines() if line.strip().startswith(f"| [{code}]({code}.md)")), "")
        if title_match and duration and (not row or title_match.group(1) not in row or duration.group(1) not in row):
            ERRORS.append(f"{code}: catalog title/duration mismatch")
        if not text.startswith("# "):
            ERRORS.append(f"{code}: heading must be first")
        for key in ("Program", "Type", "Prerequisites", "Duration", "Status"):
            if not re.search(r"^\*\*" + key + r":\*\* \S+", text, re.M):
                ERRORS.append(f"{code}: missing {key} metadata")
        if "**Status:** " + chr(96) + "draft" + chr(96) not in text:
            ERRORS.append(f"{code}: expected draft status")
        if not re.search(r"^\*\*Type:\*\* " + chr(96) + ("project" if code == "SEF10" else "course") + chr(96) + "$", text, re.M):
            ERRORS.append(f"{code}: incorrect course type")

        headings = re.findall(r"^## (.+)$", text, re.M)
        if headings != SECTIONS:
            ERRORS.append(f"{code}: expected exactly {SECTIONS}; got {headings}")
        if re.search(r"\b[BR][0-9]{1,3}\b|^#### Module brief|^## Course brief|^\s*- kind: ", text, re.M):
            ERRORS.append(f"{code}: legacy brief or resource format found")

        sections = list(re.finditer(r"^### Module (\d+) — ([^\n]+)$", text, re.M))
        if not sections:
            ERRORS.append(f"{code}: no modules")
        if [int(m.group(1)) for m in sections] != list(range(1, len(sections) + 1)):
            ERRORS.append(f"{code}: nonsequential module numbering")
        lesson_kinds = []
        for i, match in enumerate(sections):
            end = sections[i + 1].start() if i + 1 < len(sections) else text.index("## Completion requirements")
            module = text[match.start():end]
            if module.count("#### Outcomes") != 1 or module.count("#### Lessons") != 1:
                ERRORS.append(f"{code} module {i+1}: expected Outcomes and Lessons only")
            # Typed lesson lines are a navigation index, without inline commentary.
            candidates = re.findall(
                r"^\d+\. \*\*[^\n]+?\*\* — " + chr(96) + r"(?:lesson|test|lab)" + chr(96) + r"[^\n]*$",
                module, re.M,
            )
            entries = re.findall(
                r"^(\d+)\. \*\*([^\n]+?)\*\* — " + chr(96) + r"(lesson|test|lab)" + chr(96) + r"[ \t]*$",
                module, re.M,
            )
            if len(candidates) != len(entries):
                ERRORS.append(f"{code} module {i+1}: lesson entries must end at the kind; no trailing comments")
            if not entries:
                ERRORS.append(f"{code} module {i+1}: missing typed lessons")
            if [int(x[0]) for x in entries] != list(range(1, len(entries) + 1)):
                ERRORS.append(f"{code} module {i+1}: lesson numbering is not sequential")
            if i == 0 and entries and not entries[0][1].startswith("Course introduction:"):
                ERRORS.append(f"{code}: first module must start with course orientation")
            lesson_kinds = [e[2] for e in entries]
        if not lesson_kinds or lesson_kinds[-1] != "lab":
            ERRORS.append(f"{code}: final lesson must be an integration lab")

        completion = text.split("## Completion requirements", 1)[-1]
        if code == "SEF4":
            # The assessment quality contract is embedded in the canonical course,
            # rather than maintained in a separate review document.
            for module_number in range(1, 9):
                if f"**Module {module_number} — " not in completion:
                    ERRORS.append(f"SEF4: missing detailed assessment for module {module_number}")
            if len(re.findall(r"^- \*\*Q[12] \(free\):\*\*", completion, re.M)) != 16:
                ERRORS.append("SEF4: expected two scored review prompts for each of eight modules")
            if len(re.findall(r"^- \*\*Objective:\*\*", completion, re.M)) != 8:
                ERRORS.append("SEF4: every module must specify its required lab objective")
            if len(re.findall(r"^- \*\*Acceptance:\*\*", completion, re.M)) != 8:
                ERRORS.append("SEF4: each lab must specify reproducible acceptance criteria")
        if "required exercises" not in completion.lower() and code != "SEF10":
            ERRORS.append(f"{code}: required exercises missing from completion requirements")
        if code == "SEF10":
            if "Project defense:" not in completion or "graduation requirement" not in completion:
                ERRORS.append(f"{code}: missing capstone defense or graduation criterion")
            if "The project must include:" not in text:
                ERRORS.append(f"{code}: missing capstone deliverable qualities")
        else:
            if "Final integration lab" not in text or "Exit demonstration:" not in completion:
                ERRORS.append(f"{code}: final lab or exit demonstration missing")
        if "requirements/" in text or "authoring-notes/" in text:
            ERRORS.append(f"{code}: obsolete companion file reference")
        
        prereq = re.search(r"^\*\*Prerequisites:\*\* ([^\n]+)", text, re.M)
        value = prereq.group(1) if prereq else ""
        DEPS[code] = [f"SEF{i}" for i in range(1, 10)] if "SEF1–SEF9" in value else re.findall(r"\bSEF[0-9]+\b", value)
        for dep in DEPS[code]:
            if dep not in EXPECTED or dep == code:
                ERRORS.append(f"{code}: invalid prerequisite {dep}")
        check_links(path, text)

    for name in ("README.md",):
        path = SEF / name
        check_links(path, path.read_text(encoding="utf-8"))

    visited, active = set(), set()

    def visit(code):
        if code in active:
            ERRORS.append(f"Prerequisite cycle at {code}")
            return
        if code in visited:
            return
        active.add(code)
        for dep in DEPS.get(code, []):
            visit(dep)
        active.remove(code)
        visited.add(code)

    for code in sorted(EXPECTED):
        visit(code)
    if ERRORS:
        print("\n".join("ERROR: " + issue for issue in ERRORS), file=sys.stderr)
        return 1
    modules = sum(len(re.findall(r"^### Module \d+ — ", course.read_text(encoding="utf-8"), re.M)) for course in courses)
    print(f"SEF structural validation passed: {len(courses)} draft courses across {modules} modules, without fixed module/lesson caps")
    return 0


if __name__ == "__main__":
    sys.exit(validate())
