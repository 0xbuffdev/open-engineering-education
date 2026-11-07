# Curriculum validation tools

OEE currently has two course-format generations. The scripts serve different
purposes, and **none** replaces a substantive conformance review.

## Legacy courses

- `python3 scripts/check-sef-curriculum.py` validates the published SEF
  courses against their legacy structure and assessment briefs.
- `python3 scripts/check-app-curriculum.py` validates the published APP
  courses against their legacy structure and assessment briefs.

Both program validators now classify courses using the shared
`course_format_versions.py` helper. **Untouched legacy courses** retain
their original per-module test/lab, final-lab, and public brief checks.
**Migrated v0.2.0 courses** are routed to the outcome-based validator
instead of being required to preserve legacy assessment patterns.

Both program validators continue checking shared metadata, catalog
consistency, course prerequisites, and local links. A failed outcome check
also fails the applicable APP or SEF validator. Neither type of successful
structural check proves educational conformance or learner mastery.

### APP catalog order and classification

The `APP/README.md` course table is the **authoritative ordered program
catalog**. `app_catalog.py` reads its explicit Core/Elective label, type,
readiness status, title, duration, prerequisites, and row order. Course IDs
are identifiers, **not sequence numbers**: a future APP17 core course may
appear between APP1 and APP2 without repurposing historical identifiers.

The APP validator compares every linked catalog row with exactly one
course file and rejects missing, duplicate, extra, or malformed rows,
missing files, contradictory metadata, prerequisite cycles, and new
core prerequisites omitted from the APP9 graduation capstone.
A core course cannot require an elective. Elective course files must declare the `elective` classification
in metadata. The catalog explicitly classifies every course, and a core
course may optionally declare the `core` classification as well.

A catalog entry's displayed prerequisite codes must agree with
the course's own prerequisite metadata, including expanded ranges
such as `APP1–APP8`. Proposed new APP17–APP21 course identities in
`APP/ARCHITECTURE.md` are **not** part of the active catalog yet.
The current nine-core/seven-elective catalog remains authoritative
until later course-migration PRs update it. This adapter changes no
normative specification, course outcome, or existing learner record.

## Outcome-based v0.2.0 courses

Validate a specific file, including a course still under development:

```sh
python3 scripts/check-outcome-curriculum.py --course curriculum/APP/APP1.md
```

Scan the curriculum, explicitly skipping legacy files:

```sh
python3 scripts/check-outcome-curriculum.py --all
```

Run regression tests:

```sh
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

All three validators use the same course-revision classification rules.
The `--all` mode checks courses that either contain v0.2.0-style outcome or
assessment IDs, or declare this optional metadata:

```markdown
**Specification:** `v0.2.0`
```

The metadata prevents partially migrated courses from being silently
classified as legacy, but is a **validator opt-in convention** rather than
a new mandatory field in the public specification. An unmarked course
that has begun defining stable outcome or assessment IDs is also routed
to v0.2.0 checks; malformed new requirements cannot escape review by
omitting the marker. An explicitly declared unknown version, or a
legacy version declaration mixed with new IDs, fails closed.

### Inline assessment example

```markdown
## Learning outcomes

- **APP1-O1:** Diagnose a browser request failure with evidence.
- **APP1-O2:** Distinguish DNS and HTTP errors.

## Modules

### Module 1 — Request Lifecycle

#### Outcomes
- APP1-O1
- APP1-O2

#### Lessons
1. Requests and responses
2. Browser network diagnostics
3. Optional investigation of a reference trace

## Completion requirements

- **APP1-AS1** (required practical investigation)
  - Outcomes: APP1-O1, APP1-O2
  - Work: diagnose an unfamiliar request trace.
  - Criteria: classify the failure and support the conclusion.
  - Evidence: annotated observations and technical explanation.
```

A required assessment must map to existing outcome IDs and provide nonempty
`Outcomes`, `Work`, `Criteria`, and `Evidence` fields. One assessment may
cover several outcomes. A course need not have per-module knowledge tests or
labs when the evidence genuinely supports the required outcomes. Project
courses must also define deliverables and a reviewable defense.

**Scope limitation:** The validator currently handles this simple inline
Markdown pattern. The specification also permits authoritative linked public
assessment briefs and other formats. Such cases need a manual review or an
extended parser. Rejection by this narrow parser does not necessarily imply
a specification violation.

The checker cannot establish pedagogical validity, reproducibility in
practice, learner mastery, `tested` or `verified` status, or course
conformance. Every course migration also requires a documented substantive
review of assessment quality, evidence, and independence from paid tools.

## Migration order

1. **Completed by validator routing:** retain historical checks for legacy
   courses and dispatch migrated v0.2.0 courses to the new checker. The
   mixed-format regression suite exercises APP and SEF together.
2. Pilot SEF1, APP1, and a project course such as SEF10; maintain the
   original program catalog and prerequisite invariants as each migrates.
3. Review the outcome-to-assessment mapping and run manual pedagogical
   assessment in addition to the structural tests.
4. Migrate additional courses in reviewable batches without rewriting
   historical learner evidence.
5. Add a versioned export for OEE Workspace, 0xNAND, and other consumers
   after the public evaluation contract has been proven.
