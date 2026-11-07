# Curriculum validation tools

OEE currently has two course-format generations. The scripts serve different
purposes, and **none** replaces a substantive conformance review.

## Legacy courses

- `python3 scripts/check-sef-curriculum.py` validates the published SEF
  courses against their legacy structure and assessment briefs.
- `python3 scripts/check-app-curriculum.py` validates the published APP
  courses against their legacy structure and assessment briefs.

These scripts currently enforce historical per-module test/lab and final-lab
rules. They must be adapted during course migration before a migrated course
can pass all applicable CI checks. Legacy success is not v0.2.0 conformance.

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
python3 -m unittest discover -s tests -p 'test_outcome_curriculum.py' -v
```

The `--all` mode checks courses that either contain v0.2.0-style outcome or
assessment IDs, or declare this optional metadata:

```markdown
**Specification:** `v0.2.0`
```

The metadata prevents partially migrated courses from being silently
classified as legacy, but is a **validator opt-in convention** rather than
a new mandatory field in the public specification.

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

1. Adapt legacy validators to recognize explicitly migrated courses while
   retaining their historical checks for untouched files.
2. Pilot SEF1, APP1, and a project course such as SEF10.
3. Verify the two generations coexist in CI without regressions.
4. Migrate additional courses in reviewable batches.
5. Add a versioned export for OEE Workspace, 0xNAND, and other consumers
   after the public evaluation contract has been proven.
