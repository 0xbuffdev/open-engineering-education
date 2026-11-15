# RFC 0002: Public OEE Toolkit Stewardship, Scope and Licensing

- **Status:** `accepted`
- **Author:** Public Toolkit proposal; contributor attribution through the reviewed PR and DCO
- **Created:** 2026-11-14
- **Last updated:** 2026-11-15
- **Related issue:** [Public Toolkit decision #57](https://github.com/0xbuffdev/open-engineering-education/issues/57)
- **Affected specification version:** OEE v0.2.0 draft; **no course-format change proposed**

## 1. Summary

Approve an optional first-party **OEE Toolkit**, maintained publicly under
[OEE governance](../GOVERNANCE.md), with implementation at `tooling/` in
this repository. It would validate and optionally export the existing
normative OEE v0.2.0 Markdown curriculum with exact source provenance.

The public specification and course Markdown remain authoritative.
The Toolkit is an *optional implementation*, not a new mandatory authoring
format, learner grading service, conformance certification, or paid dependency.

**Decision status:** Accepted on 2026-11-15 through the steward-reviewed
and merged [PR #63](https://github.com/0xbuffdev/open-engineering-education/pull/63).
This decision authorizes the optional Toolkit source and its scoped
licensing boundaries; it does **not** publish or stabilize an official
release, override contributor rights, or claim normative OEE conformance.
See [Section 10](#10-decision).

## 2. Problem

The existing [OEE scripts](../scripts/README.md) provide version
classification, structural checks and catalog validation. They are useful
maintenance/migration utilities, and, before the implementation changes
reviewed in PRs #59–#62, did not provide an independent Toolkit with pinned-revision
source resolution, source-located diagnostics and deterministic export.
The source implementation is now merged, but release readiness and
stabilized packaging remain separate approvals.

Without a reviewed public implementation contract, Workspace and independent
adopters risk separately interpreting course Markdown, checking moving HEAD,
silently accepting older course formats, or treating parser success as
educational conformance. The existing parser also documents limited support
for alternative and linked assessment-brief syntax.

The Toolkit's authority, supported behavior, and implementation conditions
must be specified and reviewed here in the public OEE RFC. No separate
planning document can appoint a maintainer, determine software licensing,
or impose additional requirements on the standard.

This decision requires public RFC review because it affects the boundary
between the OEE standard and implementations, source layout, licensing scope
and OEE governance.

## 3. Approved design and implementation scope

### Stewardship, source home and authority

1. OEE's existing steward oversees an optional, publicly available, free,
   independently usable Toolkit, with decision and maintenance history
   recorded in the public OEE repository.
2. Prefer `tooling/` for the new public implementation, offline CLI,
   library interface, tests, software schemas and package-specific docs.
   Preserve the distinction between normative educational requirements,
   editable course Markdown, repository maintenance scripts, and derived
   Toolkit exports.
3. Reuse/refactor the proven v0.2.0 structural checker and its tests so the
   Toolkit has **one production parser and rule interpretation**.
   Existing legacy program validators may temporarily serve curriculum
   migration but are **not** supported Toolkit APIs.
4. No public package, official release or steward endorsement is implied
   until this RFC is explicitly accepted and a separate implementation and
   release review passes. A future normative change requires a separate
   public RFC, not a Toolkit-only patch.

### License and contribution scope

Adopt the repository's existing [MIT License](../LICENSE-MIT)
for **original Toolkit implementation code, software tests, maintenance
scripts and machine-readable software-interface schemas**, with explicit
file-level boundaries in [Toolkit licensing](../tooling/LICENSING.md).
[CC BY 4.0](../LICENSE) remains the license for normative specification
and educational curriculum text. Maintain the existing
[Developer Certificate of Origin](../DCO.md).

This is a **file-scope decision** with its exact implementation boundaries
recorded in [Toolkit licensing](../tooling/LICENSING.md). Generated golden
exports reproducing real OEE course outcomes, assessment criteria and
lesson text remain **CC BY 4.0 educational derivatives**, even though the
exporter and JSON Schema software interface are MIT. This decision
does not silently relicense existing contributions or educational
material; bundled third-party code requires rights verification and
preserved attribution. Toolkit examples that reproduce significant OEE
educational text must carry its applicable notices. OEE/0xBUFF marks
remain governed by their existing attribution and trademark policies.

### Implementation boundary and input contract

The first Toolkit implementation supports **only OEE v0.2.0 outcome-driven
course inputs**, and would:

- Resolve course Markdown, catalogs and authorized linked public assessment
  briefs from an **exact full Git commit SHA**, never moving HEAD, a dirty
  worktree, or a network fallback.
- Fail explicitly on unsupported v0.0.1/v0.1.0 courses, mixed/unknown
  formats, absent revisions and incomplete prerequisite/brief sources.
  It has **no** compatibility parser, converter, reader, alias or automatic
  revision migration.
- Produce deterministic source-located structural findings with stable
  rule IDs, performed/skipped checks and honest `passed`, `failed` or
  `incomplete` results, keeping `parser_limitation` distinct from actual
  specification violations.
- Optionally export versioned, derived UTF-8 JSON for outcomes,
  required assessments, criteria, public source locations and coverage.
  Export is a **read-only interface**; source Markdown remains the only
  authority for educational requirements.
- Distinguish Toolkit version, OEE specification revision, export format
  version and exact source Git SHA. Same inputs must produce byte-identical
  exports without timestamps, private network data or local path leakage.
- Offer a portable offline CLI and library interface, initially
  **Python standard-library only** unless reviewed implementation evidence
  establishes a need for more dependencies.
- Never execute student submissions, collect evidence remotely, issue a
  learner grade, promote status to `tested` or `verified`, or assert formal
  course/program/implementation conformance. Those need separate human
  review under the published OEE evidence and conformance requirements.

The implementation must publish its concrete schema, CLI, diagnostics and
negative fixtures in this public repository. This RFC and the published OEE
specification define the reviewable source requirements.

### Workspace and vendor independence

OEE Workspace and independent tools may consume derived pinned exports.
The first-party Workspace should not maintain another production
Markdown parser that can contradict the Toolkit. However, **using the
Toolkit is optional** for independent OEE implementations: public
specification requirements remain available without it.

No commercial platform, model API, 0xNAND login, private `content` data,
affiliate purchase or paid teaching material may be a prerequisite.
Workspace owns learner-authored projects, evidence and private records;
the Toolkit never edits them or silently maps completions across course
revisions.

### Approved architectural wording (not a release claim)

> OEE Toolkit is an optional first-party open-source implementation for
> checking supported OEE course structure and producing reproducible
> source-pinned exports. Public OEE specification and curriculum text remain
> authoritative. A structural Toolkit result is not an assessment, course
> status promotion, accreditation or independent conformance certification.

The wording is the accepted **architectural description**, not a statement
that a distributable Toolkit or official release has shipped. Publication
of official release and support claims remains conditional on a
separately reviewed release-readiness decision.

### Consolidated architecture decisions

The following architectural decisions, their rationale, trade-offs,
and implementation consequences are adopted by the public steward-reviewed
decision recorded below. The reviewed RFC is the public decision record;
the complete source and licensing decision is stated here without relying
on separate planning documents.

| Decision | Rationale | Consequence and trade-off |
| --- | --- | --- |
| A1 — Public OEE ownership at `tooling/` | Keep implementation open, close to normative source and existing tests | Repository grows; Toolkit releases still need their own scoped versioning |
| A2 — Markdown is the only editable course requirement source | Avoid dual-source JSON/Markdown drift | Export is generated and never manually maintained as authoritative |
| A3 — One v0.2.0 parser/checker for all supported tooling | Prevent conflicting interpretations across checker, exporter and Workspace | Requires refactoring proven checks instead of writing a competing parser |
| A4 — Pin every input to a full Git commit SHA and path | Prevent moving-HEAD identity errors | Missing objects fail explicitly; no automatic network resolution |
| A5 — Strict current-format input; no legacy runtime | No ambiguous historical assessment equivalence or compatibility maintenance | Earlier course definitions are unsupported until editorial migration |
| A6 — Offline derived export with public schema | Enable independent Workspace and third-party consumers | Export versioning is separate from normative OEE specification version |
| A7 — Structural evidence is not educational conformance | Preserve integrity of `draft`/`tested`/`verified` and reviewer judgment | Checks always disclose manual review requirements |
| A8 — Separate code and educational licensing notices | Preserve MIT software openness without silently changing CC BY text rights | Requires file-level license review before an official release |

### Technical contract

The supported technical contract is defined directly in this public RFC.
Implementations and tests follow the requirements stated here while
preserving the independent authority of OEE's published normative
educational requirements. No unreviewed implementation detail or
private planning text may add binding educational requirements.

#### Input and structural interpretation

- Input selects a local repository root, a **40-character lowercase Git
  commit SHA**, and an explicit course code/path or repository scan scope.
  Resolve all file/brief content from that exact commit's object tree,
  including permitted in-tree links. No substitution of HEAD, dirty
  filesystem content, HTTP response, or another revision.
- A supported course has `v0.2.0` outcome-driven structure: canonical
  course identity, required metadata, `Overview`, `Learning outcomes`,
  `Modules` and `Completion requirements`, unique outcome and
  assessment IDs, required assessment `Outcomes`, `Work`, `Criteria` and
  `Evidence`, module/lesson order and prerequisite references when source
  context is available. Projects also declare deliverables and a
  reviewable technical defense.
- The normative course format permits linked public assessment briefs.
  Resolve safe in-tree linked briefs at the **same commit** and preserve
  their original location. A valid expression the parser cannot handle
  yields `parser_limitation` and an incomplete result; a missing, unsafe or
  escaping link never becomes a fabricated empty valid assessment.
- Explicit legacy, unknown and mixed-format inputs must fail clearly;
  unmarked legacy drafts are **unsupported**, not skipped in a way that
  makes an entire repository scan look complete. No v0.1.0 reader or
  upgrade workflow is part of the Toolkit.
- Every outcome/assessment reference is checked against its course
  identity; only **required summative assessments** satisfy outcome
  coverage. Structural checks cannot establish pedagogical quality.

#### Inspection result and diagnostic contract

An inspection result records `toolVersion`, `ruleSetVersion`,
`source` (repository, full revision, course path and supported OEE
specification), `scope` (course/program/repository),
`checksPerformed`, `checksSkipped` with reasons, `findings` with stable
code/severity/message and best available source path and line, and
`structuralOutcome`: `passed`, `failed` or `incomplete`.
Structural success must still state `manualReviewRequired: true`.
A parser limitation is not a claim that valid source violated OEE.

At minimum, distinguish these failure classes:
`unsupported_format`, `missing_input`, `parser_limitation`,
`invalid_reference`, `structural_violation`, `unsafe_reference`
and `tool_error`. Skipped material checks are reported, not discarded.
An all-repository inspection containing unsupported active courses is
`incomplete` even if every supported course passes.

#### Derived course export format 1

The first export is UTF-8 JSON with exactly the following top-level
fields: `exportVersion`, `source`, `course`, `outcomes`,
`assessments`, `modules`, `coverage` and `validation`.
The implementation will publish a machine-readable JSON Schema and
negative fixtures in its own public source. The following is a **synthetic
schema-shape example**, not a published course:

~~~json
{
  "exportVersion": 1,
  "source": {
    "repository": "0xbuffdev/open-engineering-education",
    "revision": "0123456789abcdef0123456789abcdef01234567",
    "specification": "v0.2.0",
    "coursePath": "curriculum/SEF/SEF1.md"
  },
  "course": {
    "code": "SEF1",
    "program": "SEF",
    "type": "course",
    "status": "draft",
    "prerequisites": []
  },
  "outcomes": [
    {
      "id": "SEF1-O1",
      "description": "Example measurable outcome",
      "location": {"path": "curriculum/SEF/SEF1.md", "line": 1}
    }
  ],
  "assessments": [
    {
      "id": "SEF1-AS1",
      "required": true,
      "outcomeIds": ["SEF1-O1"],
      "work": "Example observable work",
      "criteria": "Example public acceptance criteria",
      "evidence": "Example reproducible evidence",
      "location": {"path": "curriculum/SEF/SEF1.md", "line": 1}
    }
  ],
  "modules": [
    {
      "number": 1,
      "title": "Example module",
      "outcomeIds": ["SEF1-O1"],
      "lessons": [{"ordinal": 1, "title": "Example lesson"}]
    }
  ],
  "coverage": {"SEF1-O1": ["SEF1-AS1"]},
  "validation": {"structural": "passed", "manualReviewRequired": true}
}
~~~

- Each outcome includes a unique course-scoped ID, nonempty published
  description and source location. Each assessment includes a unique ID,
  explicit `required` Boolean, outcome references, published work,
  criteria, evidence and source location. Optional evaluations never
  satisfy required coverage. Source fields are mandatory.
- Preserve published module order and titles. Lesson ordinals are
  **revision-scoped navigation**, not permanent learning identities.
  Do not derive stable identifiers from numeric course suffix or
  heading position.
- A course export does not invent catalog order if the program catalog
  was not supplied. A program export includes its authoritative catalog
  order, core/elective classification and prerequisite edges, and must
  report incomplete when the relevant catalog is absent.
- Unsupported, incomplete or unsafe input cannot produce a successful
  authoritative export. Export never contains learner submissions,
  grades, privately sourced book material or invented assessments.

#### Determinism, command surface and result codes

For identical source Git commit, Toolkit/rule-set version and arguments,
outputs must be **byte-identical**: fixed object key serialization, UTF-8,
LF and stable array order where semantically meaningful. Exclude current
timestamps, machine-specific absolute paths, locale and implicit network
lookups. An optional generated index/manifest remains a derived artifact.

**Actual source-checkout CLI, now implemented** (run from the OEE
repository root; Python 3.11+ and local Git required):

~~~text
python3 -m tooling.oee_toolkit check  --repo PATH --revision SHA --course SEF1
python3 -m tooling.oee_toolkit export --repo PATH --revision SHA --course SEF1 --output FILE
python3 -m tooling.oee_toolkit check  --repo PATH --revision SHA --all
~~~

This command surface is reviewed as the **source-repository implementation**
of the architectural contract, not a released installed command.
The internal importable `tooling.oee_toolkit` code provides a public
inspection/export implementation, but **no separately installed
`oee_toolkit` distribution, semantic Toolkit version, stable
third-party library API or promised compatibility window** has been
approved. `toolVersion: 0.0.0-dev` remains an implementation identifier;
A separate public release-readiness review must choose packaging,
API support, release numbering and distribution after independent smoke
tests. These are explicit release
boundaries, not a backwards-compatibility obligation.

| Exit | Meaning |
| --- | --- |
| 0 | All selected structural checks passed (manual review still required) |
| 1 | Structural violation |
| 2 | Invalid CLI arguments |
| 3 | Unsupported, missing or incomplete selected input |
| 4 | Internal Toolkit failure |

**Acceptance fixtures** must include fixed valid SEF1/SEF10/APP1
revisions, an actual supported public linked brief, a rejected old
version, contradictory metadata, duplicate/unknown assessment IDs,
missing criterion and evidence, bad prerequisites, escaping/missing
briefs, project defense, byte-identical repeated exports, deliberate
wrong-commit references and an offline Workspace consumer test.
A historical revision must never be silently reinterpreted as meeting
a changed required assessment.

## 4. Alternatives considered

| Alternative | Benefit | Risk | Decision |
| --- | --- | --- | --- |
| Continue standalone `scripts/` only | Minimal new code | Separate consumers interpret source inconsistently; no stable export | Reject as long-term interface |
| First-party `tooling/` inside public OEE | Transparent stewardship and shared tests | Explicit separation of spec and implementation needed | Preferred |
| Separate public Toolkit repository | Independent release lifecycle | More duplication and governance/version drift | Revisit when justified |
| Private 0xNAND service | One hosted implementation | Proprietary service dependency, opaque results | Reject |
| Runtime compatibility with v0.1.0 and older | Convenient for stale documents | Ambiguous learning semantics and complex fallback | Reject |

## 5. Impact assessment

### Existing courses and programs

No course, catalog, prerequisite, outcome, assessment, curriculum status or
learning requirement changes. Legacy drafts are **unsupported** as Toolkit
input until individually authored to v0.2.0 in later curriculum PRs. A
repository-wide check that includes such files reports **incomplete**,
never an all-courses-green result.

### Implementations

Existing `scripts/` remain public repository maintenance tools; their
old-format dispatch is not a new Toolkit compatibility commitment.
Future Workspace consumption must compare pinned source identities and
reject incomplete or wrong-revision exports. Shared parser extraction
requires separately reviewed source PRs and regression tests.

### Evidence, statuses and conformance

No changes. Automated structural checks cannot claim learner mastery,
status promotions or full conformance. The RFC does not change any normative course-format requirement or
course-status definition.

### Licensing and governance

The reviewed steward decision permits the first-party `tooling/`
implementation and clarifies the MIT code/CC BY educational derivative
boundaries in [Toolkit licensing](../tooling/LICENSING.md). Authentic DCO,
contributor rights, existing CC BY educational content and trademark
rights stay unchanged. A further notice/distribution audit is required
in a separately approved release-readiness review before any officially
supported package is released.

## 6. Compatibility and transition

The Toolkit will have **one active input contract: OEE v0.2.0**.
Historical tags/commits remain immutable citation records, not runtime
input obligations. There is no legacy reader, converter, dual-mode API or
automatic transfer of historic completion evidence.

### Implementation evidence and remaining gate

The public source implementation was reviewed and merged through
[PR #59](https://github.com/0xbuffdev/open-engineering-education/pull/59)
(strict current-format fixtures),
[PR #60](https://github.com/0xbuffdev/open-engineering-education/pull/60)
(source-located diagnostics and safe linked briefs),
[PR #61](https://github.com/0xbuffdev/open-engineering-education/pull/61)
(offline source-pinned CLI and deterministic exports), and
[PR #62](https://github.com/0xbuffdev/open-engineering-education/pull/62)
(pinned golden exports and independent consumer checks).

The implementation PRs were merged before governance acceptance. The
steward subsequently adopted the architecture and licensing boundaries
through [PR #63](https://github.com/0xbuffdev/open-engineering-education/pull/63),
following the public discussion in
[issue #57](https://github.com/0xbuffdev/open-engineering-education/issues/57).
That decision does **not** approve official distribution.
Official packaging, supported interfaces, copyright/attribution notices,
and a fresh-checkout portability review require a **separate public
release-readiness decision**. Workspace's reviewed source-pinned resource
mappings are independently maintained and must not be assumed approved
by the OEE source implementation.

No APP, SEF, SYS, AI or SEC course redesign is authorized by this RFC.

## 7. Risks and mitigations

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Toolkit and specification diverge | Misleading validation | Normative Markdown remains authority; shared rules and tests |
| Unsupported legacy file is green | False educational claim | Strict rejection/incomplete reporting |
| MIT/CC scope ambiguity | Misattribution of rights | Explicit file-scope decision and notice audit |
| Hidden moving-HEAD or network dependency | Nondeterminism and provenance error | Exact Git commit, offline fixtures |
| Official/released status claimed early | Governance confusion | Draft and approval gates, public decision record |
| Downstream maps use wrong course revision | Incorrect learning evidence mapping | Full SHA identity and cross-repository negative fixtures |

## 8. Validation plan

The steward accepted the RFC in
[PR #63](https://github.com/0xbuffdev/open-engineering-education/pull/63).
That adoption records the first-party source home and
[file-level license boundaries](../tooling/LICENSING.md) without changing
normative educational requirements or waiving third-party rights.

The already-merged implementation provides public evidence:

- [PR #59](https://github.com/0xbuffdev/open-engineering-education/pull/59):
  strict v0.2.0 fixtures, legacy and mixed-format rejection.
- [PR #60](https://github.com/0xbuffdev/open-engineering-education/pull/60):
  source-located diagnostics, linked briefs and incomplete findings.
- [PR #61](https://github.com/0xbuffdev/open-engineering-education/pull/61):
  offline SHA-pinned reader, single-parser CLI, export v1 JSON Schema,
  negative tests and Windows/macOS/Linux integration checks.
- [PR #62](https://github.com/0xbuffdev/open-engineering-education/pull/62):
  byte-identical pinned SEF1/SEF10/APP1/APP17 golden exports,
  wrong-SHA rejection, independent Workspace consumer contract and
  advisory source-drift reporting.

**Implementation checks are not official release checks.** A separate
public release-readiness review must verify legal notices and a fresh
independent installation/use flow,
supported public interfaces and status-disclosure wording. Workspace
schema-v2 map adoption remains an independent downstream dependency.

## 9. Resolved decisions and later release questions

1. **Public source home:** `tooling/` in this OEE repository, under the
   existing OEE steward. A separate Toolkit repository is **not**
   required for the first source implementation.
2. **File-level licenses:** MIT for original Toolkit software, interface
   schemas, tests and software-oriented docs; CC BY 4.0 for normative
   OEE educational text and the derived course-content golden exports.
   See [Toolkit licensing](../tooling/LICENSING.md). Existing rights and
   third-party attribution are preserved.
3. **Distribution and versioning:** This decision approves the existing
   `python3 -m tooling.oee_toolkit` **repository-local CLI** but **no
   official package, support policy, public semver or installed module
   name**. Independent package/release/API approval is deferred to
   a separate public release-readiness decision; internal
   `toolVersion: 0.0.0-dev` is not a release.
4. **Maintenance scripts:** `scripts/check-outcome-curriculum.py` is the
   shared v0.2.0 source parser called by the Toolkit; other historic
   program validation scripts remain repository maintenance/migration
   tooling, **not a Toolkit legacy API or supported old-format mode**.
5. **External integration:** Workspace's schema-v2 resources and reviewed
   source mapping remain separate work and cannot be assumed accepted
   merely because an interop consumer test passes.

## 10. Decision

- **Decision:** Accept first-party OEE Toolkit architecture, source home,
  and file-scoped licensing as specified in this RFC and
  [Toolkit licensing](../tooling/LICENSING.md).
- **Decision date:** 2026-11-15; adopted through merged public
  [PR #63](https://github.com/0xbuffdev/open-engineering-education/pull/63).
- **Decision-maker:** The existing OEE steward, 0xBUFF, represented by
  Christopher S. Aondona under [Governance](../GOVERNANCE.md).
  The merged decision PR records public approval.
- **Rationale:** Maintain one independent public source of truth, an
  optional reproducible implementation with a single parser, explicit
  source provenance, vendor-neutral access and correct separation
  between software and educational-content licenses.
- **Alternatives rejected:** Private service, second normative JSON
  authoring format, historical course compatibility, independent Toolkit
  repository before it is needed, and automatic release/conformance claims.
- **Affected normative requirements:** None. Published course requirements,
  curriculum text, grading, evidence and course status definitions do not change.
- **Implementation evidence:** Merged public PRs
  [#59](https://github.com/0xbuffdev/open-engineering-education/pull/59),
  [#60](https://github.com/0xbuffdev/open-engineering-education/pull/60),
  [#61](https://github.com/0xbuffdev/open-engineering-education/pull/61),
  and [#62](https://github.com/0xbuffdev/open-engineering-education/pull/62).
- **Conditions:** No official supported Toolkit package or API release
  until a separate, publicly reviewed decision validates packaging,
  notices, version boundaries, CLI/library documentation and fresh-checkout
  portability. No course conformance, learner evaluation, status
  promotion, automatic Workspace map migration, or backwards
  compatibility is authorized.
- **Public decision PR:** [#63](https://github.com/0xbuffdev/open-engineering-education/pull/63), merged 2026-11-15.
- **Public discussion:** [issue #57](https://github.com/0xbuffdev/open-engineering-education/issues/57).
