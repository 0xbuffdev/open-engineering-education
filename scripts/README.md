# Curriculum validation tools

OEE currently has two course-format generations. The scripts serve different
purposes, and **none** replaces a substantive conformance review.

## Program validators

- `python3 scripts/check-sef-curriculum.py` validates **all eleven** published SEF v0.2.0 courses, catalog-defined prerequisite-valid study order, new SEF11 mathematical prerequisites and capstone closure. SEF course IDs are stable identities, not numeric study order.
- `python3 scripts/check-app-curriculum.py` validates the published APP catalog, including both migrated and still-legacy course contracts.

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
are identifiers, **not sequence numbers**: APP17 already appears between
APP1 and APP2 in the published catalog without changing existing IDs.

The APP validator compares every linked catalog row with exactly one
course file and rejects missing, duplicate, extra, or malformed rows,
missing files, contradictory metadata, prerequisite cycles, and new
core prerequisites omitted from the APP9 graduation capstone.
A core course cannot require an elective. Elective course files must declare the `elective` classification
in metadata. The catalog explicitly classifies every course, and a core
course may optionally declare the `core` classification as well.

A catalog entry's displayed prerequisite codes must agree with
the course's own prerequisite metadata, including expanded ranges
such as `APP1–APP8`. APP17–APP19 are published new core courses;
APP4 provides an independent SEF10-entry database foundation,
APP21 provides Node.js backend runtime foundations after APP18,
APP2 follows APP17 + APP19 as framework-neutral browser engineering,
APP20 follows APP2 as React Application Engineering, APP3
follows APP19 + APP21 + APP4 for typed framework API engineering,
APP5 combines APP20 + APP3 for full-stack integration (with
APP4 included transitively through APP3), APP6 follows APP5
for risk-based quality, CI, supply-chain evidence, observability,
performance and incident-driven improvement, and APP7 follows
APP5 + APP6 for deployable artifacts, verified HTTPS, applied
infrastructure, safe releases, data restoration and recovery,
and APP8 follows APP5 + APP6 + APP7 for measured architecture
capacity, overload fairness, cache/data consistency, failure
containment and reversible performance/cost evolution.
APP9 is the independently assessed `project` capstone with direct
prerequisite closure over all 13 preceding APP core courses and
eight outcome-mapped v0.2.0 summative graduation assessments.
Unmigrated elective scope/dependency changes remain in the
[APP migration decision](../curriculum/APP/ARCHITECTURE.md).
The [current APP catalog](../curriculum/APP/README.md) contains
**14 core courses and 7 electives** and is authoritative until reviewed
course-migration PRs change it. The validator does not change course
requirements or historical learner records.

## Outcome-based v0.2.0 courses

Validate a specific file, including a course still under development:

```sh
python3 scripts/check-outcome-curriculum.py --course curriculum/APP/APP1.md
```

Inspect the entire active curriculum, **including unsupported legacy files**:

```sh
python3 scripts/check-outcome-curriculum.py --all --format json
```

The full inspection returns `incomplete` (exit code `3`) until every
active course uses v0.2.0; legacy drafts cannot silently count as a pass.
Run `--course` on selected migrated courses to require structural success
(exit code `0`). Structural violations exit `1`; an incomplete or
unsupported course exits `3`. Machine-readable diagnostics have stable
rule IDs and actual source path/line. The current JSON report is an
**internal maintenance diagnostic**, not a published Toolkit export API.

Run regression tests:

```sh
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

All three validators use the same course-revision classification rules.
The `--all` mode checks recognizable v0.2.0 courses and reports older
active courses as unsupported/incomplete. Recognizable sources contain
outcome/assessment IDs or declare the optional metadata:

```markdown
**Specification:** `v0.2.0`
```

The metadata prevents partially migrated courses from being silently
classified as legacy, but is a **validator opt-in convention** rather than
a new mandatory field in the public specification. An unmarked course
that has begun defining recognizable stable outcome or assessment IDs is
also routed to v0.2.0 checks. Because detection uses the recognized ID
pattern, a malformed, unmarked partial migration could still be mistaken
for a legacy course; newly migrated files should therefore declare their
specification version explicitly. An explicitly declared unknown version,
or a legacy version declaration mixed with recognized new IDs, fails closed.

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

**Parser coverage:** In addition to inline assessment fields, the checker
resolves one explicit local public assessment-brief link on an assessment
heading or a `Brief:` line, using safe repository-contained relative Markdown
paths. It reads the required `Outcomes`, `Work`, `Criteria`, and
`Evidence` fields from that brief. It rejects missing or escaping files
without silently treating them as empty validated assessments. Unsupported
remote links, multiple competing brief links, and unrecognized valid Markdown
presentations are reported as `parser_limitation` / `incomplete`, not a
definitive violation of OEE's authoring rules. This maintenance checker reads supplied working files, not a pinned Git
source revision. The separate, repository-local
[OEE Toolkit](../tooling/README.md) provides source-pinned, immutable
course checks and exports; its package and public API are not released
or stabilized.

The checker cannot establish pedagogical validity, reproducibility in
practice, learner mastery, `tested` or `verified` status, or course
conformance. Every course migration also requires a documented substantive
review of assessment quality, evidence, and independence from paid tools.

## Current coverage and limitations

**All eleven SEF courses** use the outcome-driven v0.2.0 draft format and remain `draft`; neither a structural check nor the mathematics migration establishes learner-tested readiness. SEF11 appears before SEF4/SEF8 in the authoritative catalog, and SEF10 requires all other ten SEF courses. The [mathematics migration map](../curriculum/SEF/MATH-MIGRATION.md) preserves historical outcome and assessment identities.

APP1 and APP17 also use v0.2.0, while other APP courses may retain legacy format until migrated. Neither a legacy checker pass nor successful v0.2.0 structural validation alone establishes educational conformance.

The repository-local [Toolkit](../tooling/README.md) implements pinned
course checks and derived exports. Its
[interoperability tests](../tooling/interop/README.md) check a pinned
Workspace consumer, but they do not make Workspace resource mappings
current, release a supported Toolkit package, or validate educational
quality. A stabilized package/API and official release require separate
readiness review.

Migration of the remaining course definitions requires public outcome
and assessment criteria, substantive quality review, careful catalog
and prerequisite updates, and explicit treatment of changed course
revisions. Automated success is never proof of learner mastery.

## Public documentation checks

Run from the repository root:

```sh
python3 scripts/check-links
python3 scripts/check-public-docs.py
python3 -m unittest discover -s tests -p 'test_public_docs.py' -v
npx --yes markdownlint-cli2@0.24.0
```

The link checker validates local paths and anchors without network
access. The public-document check rejects links to 0xBUFF's internal
planning repositories in the main entry points, specifications, RFCs,
program catalogs, issue templates, and tooling guides. It does not
verify external links, assess educational claims, or replace editorial
review.
