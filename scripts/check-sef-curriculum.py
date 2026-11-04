#!/usr/bin/env python3
"""Validate SEF import integrity; this is not a conformance assessment."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SEF = ROOT / "curriculum" / "SEF"
EXPECTED = {f"SEF{i}" for i in range(1, 11)}
issues = []
dependencies = {}

def check_links(path, text):
    for href in re.findall(r"\]\(([^)]+)\)", text):
        target = href.split("#", 1)[0]
        if not target.endswith(".md") or "://" in target:
            continue
        if not (path.parent / target).resolve().is_file():
            issues.append(f"{path.name}: unresolved link {href}")

def main():
    files = sorted(SEF.glob("SEF[0-9]*.md"))
    if {p.stem for p in files} != EXPECTED:
        issues.append("SEF course inventory is not SEF1 through SEF10")
    for path in files:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("> [Software Engineering Foundations]"):
            issues.append(f"{path.name}: missing navigation")
        if not re.search(r"^# " + path.stem + r" — ", text, re.M):
            issues.append(f"{path.name}: heading/code mismatch")
        for field in ("Program", "Type", "Prerequisites", "Duration", "Status"):
            if not re.search(r"^\*\*" + field + r":\*\* \S+", text, re.M):
                issues.append(f"{path.name}: missing {field}")
        if "**Status:** " + chr(96) + "draft" + chr(96) not in text:
            issues.append(f"{path.name}: course not marked draft")
        if not re.search(r"^### Module [0-9]+", text, re.M):
            issues.append(f"{path.name}: no modules")
        if re.search(r"\b[BR][0-9]{1,3}\b", text) or "## Resource map" in text or re.search(r"^\*\*Reading:\*\*", text, re.M):
            issues.append(f"{path.name}: external resource mapping found")
        for heading in ("## Prerequisites", "## Learning outcomes", "## Modules"):
            if heading not in text:
                issues.append(f"{path.name}: missing {heading}")
        if path.stem != "SEF10" and "## Course lab" not in text:
            issues.append(f"{path.name}: missing course lab")
        if path.stem == "SEF10" and "## Project defense" not in text:
            issues.append(f"{path.name}: missing project defense")
        found = re.search(r"\*\*Prerequisites:\*\* ([^\n]+)", text)
        prereqs = found.group(1) if found else ""
        deps = [f"SEF{i}" for i in range(1, 10)] if "SEF1–SEF9" in prereqs else re.findall(r"\bSEF[0-9]+\b", prereqs)
        dependencies[path.stem] = deps
        for dep in deps:
            if dep not in EXPECTED or dep == path.stem:
                issues.append(f"{path.name}: invalid prerequisite {dep}")
        check_links(path, text)
    for name in ("README.md", "MIGRATION.md"):
        p = SEF / name
        check_links(p, p.read_text(encoding="utf-8"))
    visited, active = set(), set()
    def visit(code):
        if code in active:
            issues.append(f"Prerequisite cycle: {code}")
            return
        if code in visited:
            return
        active.add(code)
        for dep in dependencies.get(code, []):
            visit(dep)
        active.remove(code)
        visited.add(code)
    for code in sorted(EXPECTED):
        visit(code)
    if issues:
        print("\n".join("ERROR: " + issue for issue in issues), file=sys.stderr)
        return 1
    print(f"SEF import integrity passed: {len(files)} draft courses")
    return 0

if __name__ == "__main__":
    sys.exit(main())
