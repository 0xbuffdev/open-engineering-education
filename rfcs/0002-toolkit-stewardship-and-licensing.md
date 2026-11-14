# RFC 0002: Public OEE Toolkit Stewardship, Scope and Licensing

- **Status:** `draft`
- **Author:** Public Toolkit proposal; contributor attribution through the reviewed PR and DCO
- **Created:** 2026-11-14
- **Last updated:** 2026-11-14
- **Related issue:** [OT-I01 — Public Toolkit decision](https://github.com/0xbuffdev/open-engineering-education/issues/57)
- **Affected specification version:** OEE v0.2.0 draft; **no course-format change proposed**

## 1. Summary

Propose an optional first-party **OEE Toolkit**, maintained publicly under
[OEE governance](../GOVERNANCE.md), with implementation at `tooling/` in
this repository. It would validate and optionally export the existing
normative OEE v0.2.0 Markdown curriculum with exact source provenance.

The public specification and course Markdown remain authoritative.
The Toolkit is an *optional implementation*, not a new mandatory authoring
format, learner grading service, conformance certification, or paid dependency.

**This RFC is a draft.** An open or merged draft proposal is not a steward
decision, code license approval, or official Toolkit release.

## 2. Problem

The existing [OEE scripts](../scripts/README.md) provide version
classification, structural checks and catalog validation. They are useful
maintenance/migration utilities, but they do not yet supply an approved,
independent first-party Toolkit with a stable pinned-revision consumer
interface, source-located diagnostics and deterministic export.

Without a reviewed public implementation contract, Workspace and independent
adopters risk separately interpreting course Markdown, checking moving HEAD,
silently accepting older course formats, or treating parser success as
educational conformance. The existing parser also documents limited support
for alternative and linked assessment-brief syntax.

The Toolkit's authority, supported behavior, and implementation conditions
must be specified and reviewed here in the public OEE RFC. No separate
planning document can appoint a maintainer, determine software licensing,
or impose additional requirements on the standard.

This proposal requires public RFC review because it may affect the boundary
between the OEE standard and implementations, source layout, licensing scope
and OEE governance.

## 3. Proposed change

### Stewardship, source home and authority

1. OEE's existing steward oversees an optional, publicly available, free,
   independently usable Toolkit, with decision and maintenance history
   recorded in the public OEE repository.
2. Prefer `tooling/` for the new public implementation, offline CLI,
   library interface, tests, software schemas and package-specific docs.
   Preserve the distinction between normative `spec/`, editable source
   `curriculum/`, maintenance scripts `scripts/` and derived Toolkit export.
3. Reuse/refactor the proven v0.2.0 structural checker and its tests so the
   Toolkit has **one production parser and rule interpretation**.
   Existing legacy program validators may temporarily serve curriculum
   migration but are **not** supported Toolkit APIs.
4. No public package, official release or steward endorsement is implied
   until this RFC is explicitly accepted and a separate implementation and
   release review passes. A future normative change requires a separate
   public RFC, not a Toolkit-only patch.

### License and contribution scope

Propose applying the repository's current [MIT License](../LICENSE-MIT)
to **new Toolkit implementation code, tests, scripts and machine-readable
software schemas**, with clear file/package licensing notices.
[CC BY 4.0](../LICENSE) remains the license for normative specification
and educational curriculum text. Maintain the existing
[Developer Certificate of Origin](../DCO.md).

This must be a **reviewed, explicit file-scope decision**. A proposal
does not silently relicense existing contributions or educational
material; bundled third-party code requires compatible licenses and
preserved attribution. Toolkit examples that reproduce significant OEE
educational text must carry its applicable notices. OEE/0xBUFF marks
remain governed by their existing attribution and trademark policies.

### Implementation boundary and input contract

The proposed first Toolkit supports **only OEE v0.2.0 outcome-driven
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
  review under [Evidence Rules](../spec/evidence-rules.md) and
  [Conformance](../spec/conformance.md).

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

### Proposed wording following acceptance

> OEE Toolkit is an optional first-party open-source implementation for
> checking supported OEE course structure and producing reproducible
> source-pinned exports. Public OEE specification and curriculum text remain
> authoritative. A structural Toolkit result is not an assessment, course
> status promotion, accreditation or independent conformance certification.

This wording is **not yet adopted** and must not be used as an official
release claim until governance and separate release review approve it.

### Consolidated architecture decisions (proposed)

The following architectural decisions, their rationale, trade-offs,
and implementation consequences are proposed **in this RFC**.
On acceptance, the reviewed RFC is the public decision record; no separate
architecture document is needed to interpret these choices.

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

### Implementable specification (proposed)

This section defines the proposed **implementable technical contract**
directly in the public RFC. After acceptance, implementation PRs and tests
must follow the approved text here and the published normative `spec/`.
No separate proposal, design document, or unreviewed implementation detail
may add binding requirements.

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

Proposed initial commands (final names adopted through implementation
review, not implied by this draft RFC):

~~~text
python3 -m oee_toolkit check  --repo PATH --revision SHA --course SEF1
python3 -m oee_toolkit export --repo PATH --revision SHA --course SEF1 --output FILE
python3 -m oee_toolkit check  --repo PATH --revision SHA --all
~~~

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

| Alternative | Benefit | Risk | Proposed decision |
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
status promotions or full conformance. The RFC does not modify
[Course Format](../spec/course-format.md) or
[Status Labels](../spec/status-labels.md).

### Licensing and governance

New MIT code scope and official Toolkit stewardship require explicit
steward approval and contribution/license review. Existing CC BY
educational text, trademark rights and DCO obligations stay unchanged.

## 6. Compatibility and transition

The Toolkit will have **one active input contract: OEE v0.2.0**.
Historical tags/commits remain immutable citation records, not runtime
input obligations. There is no legacy reader, converter, dual-mode API or
automatic transfer of historic completion evidence.

### Implementation tickets and dependencies (proposed)

This is the RFC's proposed **implementation work breakdown, dependencies
and acceptance gates**. Public OEE issues and PRs record execution and
review, without replacing this RFC's approved requirements. A ticket is
completed **only after its required implementation PR merges with acceptance
evidence**, not because this RFC was merged.

| Ticket | Priority | Blocked by | Deliverable and acceptance gate |
| --- | --- | --- | --- |
| **OT-I01** | P0 | None | Public Toolkit steward/home/license decision in [issue #57](https://github.com/0xbuffdev/open-engineering-education/issues/57); explicit accepted RFC record before claiming official status |
| **OT-I02** | P0 | None | Pin valid/invalid v0.2.0 fixtures, rejected legacy/mixed formats, linked-brief limitation; regression tests without compatibility parser |
| **OT-I03** | P1 | OT-I02 | Source-located rule IDs and diagnostics; explicit incomplete/parser-limitation behavior, linked briefs, prerequisite/project defense cases |
| **OT-I04** | P1 | OT-I01 accepted, OT-I03 | Single-parser offline CLI and deterministic export format 1 with Git commit blob resolution, schema, and negative source-identity cases |
| **OT-I06** | P1 | OT-I04, Workspace WS-I03 / WS-I01 | Pinned golden SEF1/SEF10/APP1 export fixtures and public Workspace consumption/drift tests; wrong-revision rejection |
| **OT-I05** | P2 | OT-I01–OT-I04, OT-I06 | Independent portability, license/notice, coverage and release-readiness review; no implicit publication |

**Order:** OT-I01 and OT-I02 may progress independently. OT-I03 then
OT-I04 then OT-I06 feed Workspace pinned-source interoperability. OT-I05
is a later release decision. Implementation PRs should link this RFC
and the relevant ticket ID, identify their exact source revisions, and
record test results, reviewer findings and legitimate DCO sign-off.
Do not undertake unrelated curriculum rewriting as a side effect.

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

Before acceptance, publicly verify that the steward approves the Toolkit
home and precise MIT-covered paths, no unreviewed third-party rights are
altered, and the proposal changes **no normative educational requirement**.
Record the accepted decision and conditions in this RFC and
[issue #57](https://github.com/0xbuffdev/open-engineering-education/issues/57).

Separate implementation PRs must prove pinned immutable Git resolution;
valid and rejected v0.2.0/legacy fixtures; linked-brief error behavior;
stable source-located findings; byte-identical offline exports; independent
Workspace consumer validation; and no spurious education conformance claim.

**Those checks have not been completed by submitting this proposal.**

## 9. Open questions

1. Does the steward affirm `tooling/` in OEE rather than a separate public
   repository for the first release?
2. Which bundled machine-readable schemas, explanatory examples and
   generated artifacts carry MIT versus CC BY notice text?
3. What is the first publicly supported Toolkit package/release version
   and distribution mechanism, if any, after implementation?
4. Which current `scripts/` become internal/shared v0.2.0 modules, and
   which remain temporary migration-only utilities?

## 10. Decision

- **Decision:** Pending public review
- **Decision date:** pending
- **Decision-maker:** OEE steward
- **Rationale:** pending
- **Conditions:** clarify file license scope, source home and supported
  public API before implementation/release
- **Implementation pull request:** pending separately; this RFC proposal
  is **not** a Toolkit implementation
