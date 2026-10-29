# OEE Specification

This directory defines the requirements that govern Open Engineering Education (OEE). The documents apply to the public curriculum and to implementations that claim to follow the specification.

**Specification status:** Draft, version `v0.0.1`.

## Documents

| Document | Purpose |
| --- | --- |
| [Principles](principles.md) | Defines the commitments that govern OEE |
| [Course Format](course-format.md) | Defines the required structure of a course |
| [Evidence Rules](evidence-rules.md) | Defines completion evidence and reproducible engineering work |
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

A proposed change to a normative document MUST follow the [RFC process](../rfcs/README.md). Until a change is accepted and published, existing normative text remains the reference for the draft version.

## Current limitations

OEE is a draft. The presence of a requirement in this directory does not mean that every course or implementation has already been assessed against it.

Conformance and course status claims must be supported by the evidence and review procedures described in this specification.