# RFC 0004: Current-Only OEE Course Sources

- **Status:** `accepted`
- **Author:** 0xBUFF (proposal for steward review)
- **Created:** 2026-11-19
- **Last updated:** 2026-11-19
- **Related issue:** [#223 — SEC professional competency architecture and integration](https://github.com/0xbuffdev/open-engineering-education/issues/223)
- **Affected specification version:** current draft `v0.2.0`

## 1. Summary

Make the supported OEE course-source contract unambiguous: the five published curricula use the outcome-driven `v0.2.0` specification, and current course validation and conformance claims must not accept a separate earlier course format. An archived source or assessed learner record can remain identifiable by its exact revision without becoming a supported active course or an automatic claim of current conformance.

The decision concerns **source-format and conformance scope**, not course depth, required learning outcomes, summative evidence, learner grading, status promotion, or a new authoring specification.

## 2. Problem

All five public catalogs—[SEF](../curriculum/SEF/README.md), [APP](../curriculum/APP/README.md), [SYS](../curriculum/SYS/README.md), [AI](../curriculum/AI/README.md), and [SEC](../curriculum/SEC/README.md)—publish current `v0.2.0` course definitions. Following [PR #248](https://github.com/0xbuffdev/open-engineering-education/pull/248), APP and SEF no longer accept a second lesson/test/lab/final-lab course validation path. The shared source classifier rejects an explicitly unsupported version. The Toolkit checks source content at a pinned Git revision and does not provide an alternative-format reader.

The published specification and contributor guidance still contradict that behavior:

1. [Conformance, section 7](../spec/conformance.md) permits previously published course formats to remain available **for evaluation under a different specification**. That transitional permission reads like an active supported conformance route.
2. [Course Format, sections 1, 3 and 9](../spec/course-format.md) frames the current contract in terms of courses being migrated and separate older source formats, rather than describing the active `v0.2.0` contract directly.
3. The [specification index](../spec/README.md), [curriculum design guide](../curriculum/DESIGN-GUIDE.md), and [contributor instructions](../CONTRIBUTING.md) continue to describe source migration or old-format exclusion as an ongoing publishing workflow.

This is not only a writing problem: section 7 includes a normative permission, so removing its current-evaluation meaning changes conformance scope. Under [OEE governance](../GOVERNANCE.md) and the [RFC process](README.md), that decision needs steward approval before changing `spec/`.

## 3. Proposed change

### D1 — One active public course source contract

Current OEE course definitions use the `v0.2.0` outcome-driven course contract. To assert conformance with this version, a source must satisfy the existing stable course/outcome/assessment identifiers, required outcome coverage, public success criteria, evidence, and completion requirements. A source with an unsupported version or without the current course structure is not an alternative conforming course.

No converter, second parser, legacy quiz/lab rule, automatic source-upgrade behavior, or mixed-format graduation credit is introduced.

### D2 — Preserve evidence provenance, not obsolete source-format support

Versioned source and learner-assessment records can be retained for attribution, accurate interpretation and auditability. They must remain tied to the actual course revision, criteria and recorded decision. **Keeping a record is not accepting that record as a current `v0.2.0` course definition**, importing a missing outcome, or granting equivalent current completion. A material change to assessed outcomes or criteria requires substantive re-evaluation before claiming equivalent credit.

This preserves educational honesty and traceability without requiring supported execution or grading under an alternate old-format curriculum.

### D3 — Keep existing educational requirements unchanged

Do not alter OEE `v0.2.0` outcome definitions, required assessment fields, learner independence, source accessibility, project defense, status-label meanings, course durations or completion decisions. Do not introduce a fixed module/lesson count or require paid tools. Courses remain `draft` until independent reviewer and learner evidence justify promotion.

This RFC does not invent another metadata field. Unmarked sources with recognizable stable outcome/assessment IDs remain subject to current structural inspection; current catalog and program-specific rules may require explicit metadata independently.

### D4 — Align normative and explanatory documents

After acceptance, make a **separate implementation PR** for:

- [Course Format](../spec/course-format.md): describe the active `v0.2.0` source contract and existing versioned evidence obligation without transitional authoring-format language.
- [Conformance](../spec/conformance.md): replace section 7's permission to evaluate earlier source formats as an active route with clear current-only conformance and preserved record interpretation.
- [Specification index](../spec/README.md): describe supported course sources consistently.
- [Curriculum Design Guide](../curriculum/DESIGN-GUIDE.md) and [Contributing](../CONTRIBUTING.md): use current-source revision and review language. Explain that `--all` inspects every published course and reports unsupported input; it does not silently skip files.

The implementing PR must preserve established current `MUST` rules around outcome, assessment and evidence, and retain the exact links and source identities.

### Proposed conformance wording

> Active course definitions claiming OEE `v0.2.0` conformance must satisfy this specification's stable identifier, required outcome coverage, assessment, evidence and evaluation requirements. An unsupported source format provides no alternative current conformance path.
>
> Past course and learner-assessment records may remain accessible for provenance and interpretation. Their presence does not make an archived course a supported active source or grant current conformance. Recorded results must remain interpretable against the actual course revision and criteria evaluated; materially changed outcomes require substantive re-evaluation.

The implementation should use normative requirement words consistently with the rest of [Conformance](../spec/conformance.md).

## 4. Alternatives considered

| Alternative | Benefit | Drawback | Decision |
| --- | --- | --- | --- |
| Keep both course-format validation paths | Existing archived sources could continue through an alternate route | Contradicts the current published catalog and risks mistaking old quiz/lab completion for outcome-based evidence | Reject |
| Delete earlier Git history and assessment records | Removes visible old material | Destroys attribution and makes previous decisions impossible to interpret accurately | Reject |
| Current-only sources with exact revision provenance | One enforceable contract without falsifying past evidence | Consumers of a former contract must explicitly update; conformance wording needs governance approval | **Propose** |

## 5. Impact assessment

### Existing courses and programs

The current 76 published course files across five programs already use `v0.2.0` source definitions: SEF 11; APP 21, including seven electives; SYS 10; AI 20, including four electives; and SEC 14. This decision changes **none** of their outcomes, summative assessments, direct or transitive prerequisites, classifications, status labels, or graduate requirements. In particular, SEC9 still independently verifies the other thirteen specialist courses before capstone work.

### Implementations

The shared checker, APP and SEF validators, curriculum inventory and repository-local Toolkit already reject unsupported source formats after PR #248. There is no new implementation API. Downstream curriculum readers and source-pinned consumers must continue to distinguish current source validity, unknown or unsupported input, and past evidence records. No reader should silently convert an unsupported source or mark it as passed.

### Evidence and status labels

No change to [Evidence Rules](../spec/evidence-rules.md) or [Status Labels](../spec/status-labels.md). Previously recorded assessment evidence remains version-attributed; it is not automatically regraded. A structural checker pass does not promote `draft` to `tested` or `verified`.

### Conformance

The proposed scope **does remove the transitional option to present an earlier course format as an actively evaluated alternative source contract**. Current `v0.2.0` course/implementation conformance criteria remain otherwise unchanged. Previously asserted conformance cannot be retroactively upgraded by replacing a version label.

### Licensing and governance

No licensing, attribution, steward authority or DCO changes. The normative scope decision requires steward acceptance under the RFC process; documentation changes follow in a separate PR. No new release tag is created by the RFC itself. Exact Git source revisions remain material to existing draft-version claims.

## 6. Compatibility and transition

This decision is intentionally **not backward-compatible** with alternate source-format validation or active evaluation under a former course contract. The repository has no active course sources requiring conversion, and its current checker already fails unsupported input. Therefore, no grace period, alternate parser or conversion pipeline is proposed.

Archived files remain in Git history. Synthetic rejected-format fixtures may remain in tests specifically to prove that unsupported sources cannot pass; they are not public courses. Existing learner evidence and decisions remain interpretable through their original revision and criteria, without silently granting new credit.

The implementation must update explanatory wording and conformance scope, not rewrite source history or course identifiers.

## 7. Risks and mitigations

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Archives are mistaken for accepted active courses | Incorrect completion or conformance claims | Explicit current-source definition and rejection tests |
| Removing transitional wording is read as permission to erase past evidence | Lost reviewability and attribution | Preserve exact revision and evidence-record interpretation in the normative text |
| Documentation outruns validator behavior | Misleading contributor instructions | Compare docs with active validators and full-repository CI |
| Source validation is mistaken for teaching effectiveness | Unsupported readiness claims | Preserve `draft` labels, status-gate evidence and public limitations |
| Normative permission changes without governance | Invalid adoption | Require steward decision on this RFC before the implementation PR is merged |

## 8. Validation plan

After acceptance, reviewers should:

1. Confirm source/catalog consistency for the five programs, including SEC9's independent predecessor completion gate and the distinction between elective and core dependencies.
2. Run the complete current-source structural scan and confirm that every published course passes, while the synthetic unsupported-version fixture fails with a clear unsupported/incomplete result.
3. Run APP, SEF, SEC and Toolkit regression checks, Git-pinned exports, link and Markdown checks, and public-document boundary checks.
4. Review `spec/course-format.md` and `spec/conformance.md` line by line to confirm current stable IDs, assessment evidence, learner record provenance and status criteria were not weakened or silently enlarged.
5. Verify that public contributor instructions describe the actual `--all` behavior and that no active documentation promises alternate-format support.
6. Obtain independent maintainer approval and DCO sign-off. Do not count this RFC's source checks as learner validation, professional accreditation or publication of a stable Toolkit API.

The accepted decision and implementation PR should be linked in this RFC's decision record. No permanent duplicate curriculum audit document is needed.

## 9. Open questions

None for the proposed current-source contract. A future released versioning policy or public archival viewer is out of scope.

## 10. Decision

- **Decision:** Accepted
- **Decision date:** 2026-11-19
- **Decision-maker:** OEE steward; explicit approval recorded in [PR #249 discussion](https://github.com/0xbuffdev/open-engineering-education/pull/249#issuecomment-7024184637)
- **Rationale:** Use one current `v0.2.0` source and conformance contract, while retaining revision-attributed records for interpretability. Unsupported course formats are not alternative paths to assessed credit.
- **Conditions:** Preserve all existing course outcome, evidence, status and independent-study rules. Implement the approved wording in a separately reviewed and signed pull request, keep prior records attributable, and do not modify `main` directly.
- **Implementation pull request:** [PR #250 — current-only source and conformance wording](https://github.com/0xbuffdev/open-engineering-education/pull/250) (in review)
