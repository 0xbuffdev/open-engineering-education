# OEE Specification

Open Engineering Education (OEE) publishes the educational requirements for its public curriculum and for implementations claiming to follow the specification.

**Current version:** `v0.2.0` — **draft**. Published requirements may evolve through the [governance process](../GOVERNANCE.md). Draft publication does not establish that any particular course or implementation is conforming, tested, or verified.

## Authoritative documents

Each document owns a distinct part of the educational contract. Refer to the owning document rather than copying its requirements into curriculum guidance, implementation notes, or RFC history.

| Document | Authority |
| --- | --- |
| [Principles](principles.md) | Governing educational principles |
| [Course Format](course-format.md) | Course structure, metadata, stable identifiers, and assessment definitions |
| [Evidence Rules](evidence-rules.md) | Learner completion, assessment decisions, evidence quality, reproducibility, and privacy |
| [Status Labels](status-labels.md) | `draft`, `tested`, and `verified` course-readiness thresholds and promotion records |
| [Conformance](conformance.md) | Assessment scope, review procedure, conformance states, and public claims |
| [Implementation Boundary](implementation-boundary.md) | Responsibilities of the specification, curriculum, tools, and learning implementations |

Start with [Principles](principles.md), then read [Course Format](course-format.md) and [Evidence Rules](evidence-rules.md). Use [Status Labels](status-labels.md) when evaluating course readiness, and [Conformance](conformance.md) when making a versioned claim about adherence to OEE.

## Normative language

Uppercase requirement words have these meanings when used in a normative specification statement:

- **MUST** and **MUST NOT** identify requirements necessary for conformance.
- **SHOULD** and **SHOULD NOT** identify strong recommendations; a documented, technically justified exception may be acceptable.
- **MAY** identifies a permitted option, not an obligation.

Explanatory prose and examples do not create additional requirements unless the text expressly states otherwise.

## Source of truth and changes

The specification defines shared requirements. Course definitions apply them to particular subjects; scripts and supporting tools may check or present them. None may silently contradict or replace normative text.

Changes to binding requirements MUST follow [OEE governance](../GOVERNANCE.md) and the public [RFC process](../rfcs/README.md). An accepted RFC records the rationale and decision; it is not a substitute for the reviewed and merged normative document.

## Version scope and limitations

The active public curriculum uses the `v0.2.0` outcome-based course contract. Unsupported source formats cannot pass the current structural checker or support a current conformance claim. Source revisions and assessed evidence remain attributable to the requirements actually evaluated; their records do not introduce another supported course format.

[Curriculum validation tools](../scripts/README.md) describes current-course repository checks and their limitations. Passing an automated structural check does not establish educational validity, course-readiness status, or conformance. These claims require the evidence and review defined by the specification.
