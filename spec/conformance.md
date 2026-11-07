# Conformance

**Specification status:** Draft, version `v0.2.0`.

This document establishes a provisional baseline for assessing whether a
course, program, or implementation meets Open Engineering Education (OEE)
requirements. This revision implements
[accepted RFC 0001](../rfcs/0001-outcome-driven-curriculum.md).

An assessment MUST state its specification version and scope.
Conformance to a draft version MUST be described as such; a limited
review MUST NOT imply a broader certification or endorsement.

## 1. Conformance scopes

A conformance assessment MUST identify the scope:

- **Course:** one versioned course definition, required evaluations,
  and evidence conditions.
- **Program:** a named program and all required courses in its scope.
- **Implementation:** a system or process applying specified OEE
  requirements.

Conformance at one scope MUST NOT be presented as conformance at another.

## 2. States and records

| State | Meaning |
| --- | --- |
| `not-assessed` | No documented assessment for the stated version and scope |
| `conforming` | All applicable requirements are met within the assessed scope |
| `non-conforming` | At least one applicable mandatory requirement is unmet |

A finding MUST be supported by a review record identifying version,
scope, date, reviewer, evidence, and findings. An unassessed course or
implementation MUST NOT be described as conforming by implication.

## 3. Course-level requirements

A course may be assessed as conforming to this version only when:

1. Metadata, title, program assignment, type, status, prerequisite
   references, and duration are consistent and valid.
2. The four required course sections (Overview, Learning outcomes,
   Modules, Completion requirements) exist and provide their required
   substantive information.
3. Required outcomes are observable, evaluable, and assigned stable,
   unique IDs for the course revision under assessment.
4. Every required summative assessment has a stable unique ID and
   identifies the outcomes evaluated, required work, published success
   criteria, and required evidence.
5. Every required outcome is covered by sufficient summative evaluation.
   The reviewer examines substantive validity of the assessment, not
   just the presence of matching identifiers.
6. Modules have coherent sequencing, stated outcomes, and an ordered
   learning sequence; no fixed per-module tests or labs are required.
7. Mandatory evaluation is distinguishable from optional formative
   practice and does not impose unjustified duplicate work.
8. Applicable practical tasks and executable artifacts meet the
   proportional reproducibility, verification, and evidence requirements
   of [Evidence Rules](evidence-rules.md).
9. A `project` course defines required deliverables, published evaluation
   criteria, and a suitable reviewable technical defense.
10. Status labels and published claims are supported according to
    [Status Labels](status-labels.md); internal links and references resolve;
    no course requirement contradicts the applicable specification.

A concluding `lab`, a knowledge test in each module, or a prescribed
order of learning activity types is not a conformance requirement.
Integration SHOULD be assessed when the required course outcomes
depend on combining capabilities.

A structural validator MAY help verify IDs, sections, links, and
references, but it cannot establish whether an assessment actually
measures an outcome. Course conformance requires manual or otherwise
defensible substantive review of the evaluation design.

A course's format conformance does not by itself justify `tested`
or `verified` status.

## 4. Program-level requirements

A program may be assessed as conforming only when:

1. Its program definition and course catalog agree.
2. All required courses and unique course codes are identified.
3. Titles, course relationships, prerequisites, order, and durations
   are internally consistent.
4. Required courses exist and meet the applicable course-level
   requirements for the stated specification version.
5. Cross-course dependencies are valid and stated program capabilities
   are supported by the curriculum's evidence requirements.
6. Program-level claims do not exceed the scope and strength of
   supporting course evidence.

If a required course does not meet a mandatory requirement for the
version under review, the program MUST NOT be described as fully
conforming. Individual course assessments MAY be reported separately
with their correct version and scope.

## 5. Implementation-level requirements

An implementation may be assessed as conforming only when:

1. It represents required public outcomes, assessment criteria,
   and evidence rules without silently changing their meaning.
2. It distinguishes canonical completion requirements from its own
   instruction, formative practice, optional resources, and product
   features.
3. It does not assert demonstrated outcomes from attendance, lesson
   consumption, unchecked activity completion, or unrelated scores.
4. It evaluates required outcomes with criteria equivalent to the
   canonical published requirements, even when using unseen variants
   or local tooling.
5. It represents relevant evidence and status labels accurately
   for the functions it claims to implement.
6. Its documented evaluation method, limitations, and observed
   behavior support the precise scope of its conformance claim.

An implementation need not automate every OEE requirement. It MUST
disclose manual responsibilities and unsupported capabilities.
No platform-specific service, including 0xNAND, is required to study,
implement, or assess the public curriculum.

A supporting tool MUST NOT claim full implementation conformance
solely because it validates one aspect of OEE.

## 6. Review record

A review SHOULD record:

- The precise specification version and course revision, when relevant.
- The scope and included files, components, or assessments.
- The review date, reviewer, criteria, and evidence inspected.
- Findings about actual outcome coverage and evaluation validity.
- Findings about portability, reproduction, and implementation independence.
- Any exceptions, unresolved issues, decision, and justification.

A documented exception to a `SHOULD` requirement MUST be justified.
A `MUST` requirement cannot be waived through an exception.

## 7. Transitional course versions

This is a breaking revision of the prior draft authoring contract.
Legacy course revisions MAY remain published and evaluated against
the historical specification that governed them. Such legacy content
MUST NOT automatically claim conformance to `v0.2.0`. A new
or migrated course MUST satisfy the revised ID, coverage, evidence,
and evaluation requirements before claiming conformance.

A learner's historical result MUST remain interpretable against the
course revision and requirements that were actually evaluated.
Reclassifying an older result requires explicit substantive
re-evaluation when outcome or success criteria materially change.
Tooling and consumer migrations SHOULD be documented, reviewable,
and non-destructive.

## 8. Public claims

Public conformance claims MUST identify their version, assessed scope,
and draft status. Nothing in OEE conformance alone constitutes
professional accreditation, proof of employment readiness, or mastery
outside the capabilities assessed. An implementation MUST NOT imply
endorsement or certification beyond the available evidence.

## 9. Change control

Future normative changes MUST follow the
[RFC process](../rfcs/README.md). Changes MUST document implications
for curriculum authors, downstream implementations, historical learner
records, and previously assessed conformance.
