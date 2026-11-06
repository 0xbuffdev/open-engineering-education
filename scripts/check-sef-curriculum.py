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
            if code in {"SEF2", "SEF3", "SEF6", "SEF9"}:
                # These courses require a purposeful checkpoint preceding
                # each hands-on lab in the current authored curriculum.
                kinds = [entry[2] for entry in entries]
                if kinds.count("test") < 1 or kinds.count("lab") != 1:
                    ERRORS.append(f"{code} module {i+1}: checkpoint and one required lab expected")
                elif kinds.index("test") > kinds.index("lab"):
                    ERRORS.append(f"{code} module {i+1}: checkpoint must precede lab")
            lesson_kinds = [e[2] for e in entries]
        if not lesson_kinds or lesson_kinds[-1] != "lab":
            ERRORS.append(f"{code}: final lesson must be an integration lab")

        completion = text.split("## Completion requirements", 1)[-1]
        if code == "SEF8":
            # No external algebra qualification; verify the beginner bridge,
            # while keeping the module and lesson counts flexible.
            if "plus basic algebra" in text.lower() or "basic high-school algebra" in text.lower():
                ERRORS.append("SEF8: algebra cannot be an external prerequisite")
            if not sections or sections[0].group(2) != "Mathematical Literacy & Pre-Algebra":
                ERRORS.append("SEF8: beginner bridge must be the first module")
            if "Ungraded starting-point numeracy check" not in text:
                ERRORS.append("SEF8: ungraded diagnostic missing")
            if "Pre-algebra readiness checkpoint" not in text or "Mathematics-to-Python workbook" not in text:
                ERRORS.append("SEF8: readiness checkpoint and practical workbook missing")
            if len(re.findall(r"^- \*\*Q\d+ — [^\n]+:", completion, re.M)) < 8:
                ERRORS.append("SEF8: beginner bridge needs assessable numeracy examples")
            if "No prior algebra" not in text:
                ERRORS.append("SEF8: accessible mathematics entry requirement missing")

            # Every post-bridge module requires an inspectable checkpoint and
            # laboratory brief; newly authored modules are automatically checked.
            for match in sections[1:]:
                number = int(match.group(1))
                checkpoint_pattern = (
                    r"^\*\*Module " + str(number) +
                    r" — [^\n]+: checkpoint\*\* — Required assessment details$"
                )
                lab_pattern = (
                    r"^\*\*Module " + str(number) +
                    r" — [^\n]+: required lab\*\* — Required assessment details$"
                )
                checkpoint_matches = list(re.finditer(checkpoint_pattern, completion, re.M))
                lab_matches = list(re.finditer(lab_pattern, completion, re.M))
                if len(checkpoint_matches) != 1 or len(lab_matches) != 1:
                    ERRORS.append(f"SEF8 module {number}: checkpoint and required lab briefs missing or duplicated")
                    continue
                checkpoint_start = checkpoint_matches[0].end()
                lab_start = lab_matches[0].start()
                lab_end = next(
                    (m.start() for m in re.finditer(r"^\*\*Module \d+ — ", completion, re.M)
                     if m.start() > lab_matches[0].start()),
                    len(completion),
                )
                if lab_start <= checkpoint_start:
                    ERRORS.append(f"SEF8 module {number}: assessment must precede practical lab")
                    continue
                checkpoint_text = completion[checkpoint_start:lab_start]
                lab_text = completion[lab_matches[0].end():lab_end]
                if len(re.findall(r"^- \*\*Q\d+ \(free\):\*\*", checkpoint_text, re.M)) < 2:
                    ERRORS.append(f"SEF8 module {number}: at least two explained checkpoint questions required")
                if "Expected answer and scoring:" not in checkpoint_text:
                    ERRORS.append(f"SEF8 module {number}: expected-answer guidance missing")
                for field in ("Objective", "Prerequisites", "Environment", "Procedure",
                              "Expected result", "Verification", "Evidence",
                              "Failure analysis", "Acceptance"):
                    if f"- **{field}:**" not in lab_text:
                        ERRORS.append(f"SEF8 module {number}: missing lab {field.lower()}")


        if code in {"SEF1", "SEF2", "SEF3", "SEF4", "SEF5", "SEF6", "SEF7", "SEF9"}:
            # Detailed assessments are embedded in the canonical course, not REVIEW.md.
            # Check the actual module count without imposing a fixed lesson cap.
            module_count = len(sections)
            for number in range(1, module_count + 1):
                if f"**Module {number} — " not in completion:
                    ERRORS.append(f"{code}: missing detailed assessment for module {number}")
            if len(re.findall(r"^- \*\*Q[12] \(free\):\*\*", completion, re.M)) != 2 * module_count:
                ERRORS.append(f"{code}: expected two checkpoint questions per module")
            for label in ("Objective", "Acceptance"):
                matches = re.findall(r"^- \*\*" + label + r":\*\*", completion, re.M)
                if len(matches) != module_count:
                    ERRORS.append(f"{code}: expected one lab {label.lower()} for each module")
            for kind in ("checkpoint", "required lab"):
                labels = re.findall(
                    r"^\*\*Module \d+ — [^\n]+: " + kind + r"\*\* — Required assessment details$",
                    completion, re.M,
                )
                if len(labels) != module_count:
                    ERRORS.append(f"{code}: missing or duplicated {kind} briefs")
        if code == "SEF9":
            # Check each module's evaluable engineering-workflow contract
            # without limiting future module or lesson counts.
            labs = list(re.finditer(
                r"^\*\*Module (\d+) — [^\n]+: required lab\*\* — Required assessment details$",
                completion, re.M,
            ))
            if [int(h.group(1)) for h in labs] != list(range(1, len(sections) + 1)):
                ERRORS.append("SEF9: required labs must align with ordered modules")
            for i, heading in enumerate(labs):
                stop = labs[i + 1].start() if i + 1 < len(labs) else len(completion)
                lab = completion[heading.end():stop]
                for field in ("Objective", "Prerequisites", "Environment", "Procedure",
                              "Expected result", "Verification", "Evidence",
                              "Failure analysis", "Acceptance"):
                    if f"- **{field}:**" not in lab:
                        ERRORS.append(f"SEF9 module {heading.group(1)}: missing {field.lower()}")
            # Verify that public requirements preserve meaningful model
            # skepticism and do not make paid access a completion condition.
            for required in ("No paid AI service", "synthetic", "untrusted",
                             "independent reviewer", "unassisted", "permissions"):
                if required not in completion:
                    ERRORS.append(f"SEF9: missing AI-assisted engineering safeguard: {required}")
        if code == "SEF6":
            # C memory-safety contracts are inline with the canonical course,
            # checked against current modules rather than a module count cap.
            lab_headers = list(re.finditer(
                r"^\*\*Module (\d+) — [^\n]+: required lab\*\* — Required assessment details$",
                completion, re.M,
            ))
            if [int(h.group(1)) for h in lab_headers] != list(range(1, len(sections) + 1)):
                ERRORS.append("SEF6: required lab contracts must follow module order")
            for i, heading in enumerate(lab_headers):
                end = lab_headers[i + 1].start() if i + 1 < len(lab_headers) else len(completion)
                lab = completion[heading.end():end]
                for field in ("Objective", "Prerequisites", "Environment", "Procedure",
                              "Expected result", "Verification", "Evidence",
                              "Failure analysis", "Acceptance"):
                    if f"- **{field}:**" not in lab:
                        ERRORS.append(f"SEF6 module {heading.group(1)}: missing lab {field.lower()}")
            for required in ("C11", "CHAR_BIT", "signed overflow", "realloc",
                             "AddressSanitizer", "ownership", "collision"):
                if required not in completion:
                    ERRORS.append(f"SEF6: missing C semantics/failure case: {required}")
        if code == "SEF3":
            # Check each required shell lab without fixing the course size.
            headers = list(re.finditer(
                r"^\*\*Module (\d+) — [^\n]+: required lab\*\* — Required assessment details$",
                completion, re.M,
            ))
            if [int(h.group(1)) for h in headers] != list(range(1, len(sections) + 1)):
                ERRORS.append("SEF3: lab contracts must follow the actual module order")
            for i, header in enumerate(headers):
                end = headers[i + 1].start() if i + 1 < len(headers) else len(completion)
                lab = completion[header.end():end]
                for field in ("Objective", "Prerequisites", "Environment", "Procedure",
                              "Expected result", "Verification", "Evidence",
                              "Failure analysis", "Acceptance"):
                    if f"- **{field}:**" not in lab:
                        ERRORS.append(f"SEF3 module {header.group(1)}: missing lab {field.lower()}")
            for required in ("disposable Linux", "unprivileged", "NUL",
                             "pipefail", "POSIX", "SIGTERM", "restricted"):
                if required not in completion:
                    ERRORS.append(f"SEF3: missing shell safety/environment topic: {required}")
        if code == "SEF2":
            # Check the per-module public lab contract without hard-coding
            # the number of modules or lessons in the course.
            lab_headers = list(re.finditer(
                r"^\*\*Module (\d+) — [^\n]+: required lab\*\* — Required assessment details$",
                completion, re.M,
            ))
            if [int(h.group(1)) for h in lab_headers] != list(range(1, len(sections) + 1)):
                ERRORS.append("SEF2: required lab descriptions must match ordered modules")
            for i, heading in enumerate(lab_headers):
                end = lab_headers[i + 1].start() if i + 1 < len(lab_headers) else len(completion)
                lab = completion[heading.end():end]
                for field in ("Objective", "Prerequisites", "Environment", "Procedure",
                              "Expected result", "Verification", "Evidence",
                              "Failure analysis", "Acceptance"):
                    if f"- **{field}:**" not in lab:
                        ERRORS.append(f"SEF2 module {heading.group(1)}: missing lab {field.lower()}")
            for requirement in ("Python 3.11", "standard library", "disposable",
                                "File I/O and data formats", "CLI behavior and persistence contracts"):
                if requirement not in text:
                    ERRORS.append(f"SEF2: missing beginner/reproducibility requirement: {requirement}")
        if code == "SEF1":
            # Foundation-level assessment is self-contained: no programming
            # prerequisite, simulator gate work and consistent toy ISA.
            lab_headers = list(re.finditer(
                r"^\*\*Module (\d+) — [^\n]+: required lab\*\* — Required assessment details$",
                completion, re.M,
            ))
            if [int(x.group(1)) for x in lab_headers] != list(range(1, len(sections) + 1)):
                ERRORS.append("SEF1: required lab descriptions must follow module order")
            for i, heading in enumerate(lab_headers):
                stop = lab_headers[i + 1].start() if i + 1 < len(lab_headers) else len(completion)
                lab = completion[heading.end():stop]
                for field in ("Objective", "Prerequisites", "Environment", "Procedure",
                              "Expected result", "Verification", "Evidence",
                              "Failure analysis", "Acceptance"):
                    if f"- **{field}:**" not in lab:
                        ERRORS.append(f"SEF1 module {heading.group(1)}: missing lab {field.lower()}")
            for requirement in ("**Shared educational machine model", "0xF0", "0xF1",
                                "LDI", "ADDI", "STORE", "JZ", "HALT", "modulo 256",
                                "No programming experience"):
                if requirement not in text:
                    ERRORS.append(f"SEF1: missing beginner/reference machine requirement: {requirement}")
        if code == "SEF7":
            # Detailed field checks for Unix safety and reproducibility.
            # Every module has one checkpoint and one lab, without a fixed module cap.
            lab_headers = list(re.finditer(
                r"^\*\*Module (\d+) — [^\n]+: required lab\*\* — Required assessment details$",
                completion, re.M,
            ))
            if [int(x.group(1)) for x in lab_headers] != list(range(1, len(sections) + 1)):
                ERRORS.append("SEF7: required lab descriptions must follow module order")
            for i, heading in enumerate(lab_headers):
                end = lab_headers[i + 1].start() if i + 1 < len(lab_headers) else len(completion)
                lab = completion[heading.end():end]
                for label in ("Objective", "Prerequisites", "Environment", "Procedure",
                              "Expected result", "Verification", "Evidence",
                              "Failure analysis", "Acceptance"):
                    if f"- **{label}:**" not in lab:
                        ERRORS.append(f"SEF7 module {heading.group(1)}: missing lab {label.lower()}")
            for safety in ("127.0.0.1", "disposable", "waitpid", "EINTR"):
                if safety not in completion:
                    ERRORS.append(f"SEF7: documented Unix safety/failure case missing: {safety}")
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
