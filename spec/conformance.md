# Conformance

**Specification status:** Draft, version `v0.0.1`.

This document defines a provisional baseline for evaluating whether a course, program, or implementation follows Open Engineering Education (OEE). Because OEE is still a draft, any assessment against this version MUST be identified as an assessment against the draft specification.

Conformance is evaluated against a stated version and scope. A claim MUST NOT imply that a wider body of work has been assessed when only a portion was reviewed.

## 1. Conformance scopes

An assessment MUST identify which of the following scopes it covers:

- **Course:** one course definition and its required assessments and evidence conditions.
- **Program:** a named program and the complete set of courses it includes.
- **Implementation:** a system or process intended to implement or enforce OEE requirements.

Conformance at one scope MUST NOT be presented as conformance at another scope.

## 2. Conformance states

The following states may be used in a documented assessment:

| State | Meaning |
| --- | --- |
| `not-assessed` | No documented assessment has been completed for the stated scope and version. |
| `conforming` | The assessed scope meets all applicable requirements of the stated specification version. |
| `non-conforming` | The assessment found one or more unmet requirements. |

A state MUST be supported by a review record identifying the version, scope, review date, reviewer, and findings.

An unassessed item MUST NOT be described as conforming by implication.

## 3. Course-level requirements

A course may be assessed as conforming only when all applicable requirements below are satisfied:

1. Required course metadata is present and internally consistent.
2. Required course sections are present.
3. Learning outcomes are observable and suitable for assessment.
4. Prerequisites and any stated course identifiers resolve correctly.
5. Lessons, assessments, and labs follow the required course structure.
6. Completion requirements align with the stated outcomes.
7. Evidence requirements are explicit and follow [Evidence Rules](evidence-rules.md).
8. The published status label is supported by the evidence required in [Status Labels](status-labels.md).
9. Internal links and cross-references resolve.
10. No course instruction contradicts a normative requirement without an approved specification change.

A course cannot be assessed as conforming solely because it has the required headings. Its substantive requirements and assessment design must also be reviewed.

A finding that the course structure is conforming does not automatically make the course `tested` or `verified`. Structural conformance and evidence-based course status are related but distinct determinations.

## 4. Program-level requirements

A program may be assessed as conforming only when:

1. Its course catalogue and program definition agree.
2. Every required course is identified, and any stated course code is unique.
3. Course titles, prerequisites, ordering, and durations are consistent.
4. Required course files exist and satisfy course-level requirements.
5. Required cross-course dependencies are valid.
6. Program-level statements do not claim stronger readiness than the supporting course evidence establishes.

If a required course fails a mandatory conformance requirement, the program MUST NOT be described as fully conforming. The assessment may identify the specific courses that do conform, provided the scope is explicit.

## 5. Implementation-level requirements

An implementation may be assessed as conforming only when:

1. It correctly represents the applicable specification requirements.
2. It does not silently replace normative requirements with product-specific rules.
3. It implements the status labels and evidence requirements consistently where those functions are in scope.
4. Its behavior can be evaluated against documented criteria.
5. Known limitations and unimplemented requirements are disclosed.
6. The assessment evidence supports the claim made about the implementation.

An implementation need not automate every part of the specification to be useful. Its stated scope MUST accurately describe what it implements and what remains a manual responsibility.

A tool that assists with one requirement MUST NOT claim full OEE conformance solely on that basis.

## 6. Review record

A conformance review SHOULD record:

- The specification version assessed.
- The assessment scope and included files or components.
- The review date and reviewer.
- Requirements checked and evidence examined.
- Findings, exceptions, and unresolved issues.
- The resulting conformance state and its justification.

Any exception to a `SHOULD` requirement MUST be documented with its rationale. An exception MUST NOT waive a `MUST` requirement.

## 7. Public claims

Public conformance claims MUST identify the assessed scope and specification version.

During the draft phase, claims MUST make the draft status clear. No wording may imply official certification, accreditation, or endorsement unless a separate, explicitly defined process authorizes that claim.

OEE conformance is not, by itself, proof of professional accreditation, employment readiness, or mastery outside the assessed scope.

## 8. Updating the conformance rules

This baseline may be revised through the [RFC process](../rfcs/README.md).

Changes MUST explain how the new requirements affect existing courses, program assessments, and implementations. A new requirement MUST NOT be treated as retrospectively satisfied without reviewing the relevant evidence.
