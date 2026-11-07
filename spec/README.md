# OEE Specification

This directory defines the requirements that govern Open Engineering Education (OEE). The documents apply to the public curriculum and to implementations that claim to follow the specification.

**Specification status:** Draft, version `v0.2.0`.

## Documents

| Document | Purpose |
| --- | --- |
| [Principles](principles.md) | Defines the commitments that govern OEE |
| [Course Format](course-format.md) | Defines outcome-driven course structure and public assessment requirements |
| [Evidence Rules](evidence-rules.md) | Defines proportionate evidence, course completion, and reproducible engineering work |
| [Status Labels](status-labels.md) | Defines `draft`, `tested`, and `verified` |
| [Conformance](conformance.md) | Defines how adherence to OEE is evaluated |
| [Implementation Boundary](implementation-boundary.md) | Separates specification requirements from curriculum and implementation choices |

## Normative language

The terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** have the following meanings when written in uppercase in a specification requirement:

- **MUST** or **MUST NOT** indicates a requirement necessary for conformance.
- **SHOULD** or **SHOULD NOT** indicates a strong recommendation. A documented, technically justified exception may be acceptable.
- **MAY** indicates a permitted option that is not required.

These terms apply only where a document states a normative requirement. Explanatory prose and examples are not requirements unless the text explicitly says otherwise.

## Reading order

Read the documents in this order:

1. [Principles](principles.md)
2. [Course Format](course-format.md)
3. [Evidence Rules](evidence-rules.md)
4. [Status Labels](status-labels.md)
5. [Conformance](conformance.md)
6. [Implementation Boundary](implementation-boundary.md)

## Authority and change control

The specification defines the common requirements. Curriculum authors and implementation maintainers may add detail within their scope, but they MUST NOT silently contradict a normative requirement.

A proposed normative change MUST follow the [RFC process](../rfcs/README.md), apart from the one-time initial v0.0.1 course-format stabilization described in [Governance](../GOVERNANCE.md). Until a change is approved and merged, the published normative text remains the reference for the draft version.

## Revision note

The `v0.2.0` draft (succeeding `v0.1.0`) adopts [RFC 0001](../rfcs/0001-outcome-driven-curriculum.md), replacing mandatory activity counts and final-lab placement with outcome-based evaluation. Earlier published course revisions must be interpreted under their original rules until they are explicitly migrated. A validator passing, or a course file existing, does not establish conformance to this revision. The APP and SEF program validators now support both formats: legacy courses retain historical test/lab checks, while newly authored or migrated `v0.2.0` courses are routed to the outcome-coverage structural validator. This dual-format tooling does not assess pedagogical validity or imply that remaining legacy courses have migrated. See [Curriculum validation tools](../scripts/README.md).

## Current limitations

OEE is a draft. The presence of a requirement in this directory does not mean that every course or implementation has already been assessed against it.

Conformance and course status claims must be supported by the evidence and review procedures described in this specification.
