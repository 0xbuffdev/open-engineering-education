# Governance

This document defines how decisions about Open Engineering Education (OEE) are proposed, reviewed, recorded, and adopted.

OEE is currently stewarded by 0xBUFF. Its governance is intentionally lightweight, but decisions affecting the public specification must remain transparent and traceable.

## 1. Stewardship

**0xBUFF is the steward of OEE.** Christopher S. Aondona exercises the stewardship role on its behalf.

The steward is responsible for maintaining the public specification, making decisions under the current governance process, coordinating reviews, and ensuring that material decisions are recorded.

Stewardship does not eliminate the need for public reasoning. Significant decisions should explain their rationale, consequences, and relationship to the existing specification.

## 2. Decision categories

### Routine changes

Examples include spelling corrections, broken-link fixes, formatting improvements, and clarifications that do not change a normative requirement.

Routine changes may proceed through a pull request. The pull request and its review history form the decision record.

### Normative changes

Changes to `spec/`, required course structure, assessment requirements, status-label definitions, conformance criteria, or other binding requirements MUST follow the [RFC process](rfcs/README.md).

An accepted RFC does not itself update the specification. The resulting change must be implemented in a pull request, reviewed, and merged.

### Course status changes

Status changes MUST be supported by the evidence required by [Status Labels](spec/status-labels.md) and [Evidence Rules](spec/evidence-rules.md).

Reviewers must be able to inspect the basis for the status change. A product release, publication date, or steward preference is not evidence of course readiness.

### Governance and licensing changes

Changes to governance, contributor obligations, licensing policy, or the scope of the public specification MUST follow the RFC process.

Legal or licensing changes must identify the affected files and explain the implications for existing contributions and downstream users.

## 3. RFC decisions

The steward accepts, rejects, or returns an RFC for revision. Each decision MUST be recorded in the relevant RFC discussion or associated decision record.

A decision record should identify:

- The decision and its date.
- The reasoning behind the decision.
- Important alternatives or objections considered.
- The affected specification requirements.
- Required follow-up work or migration steps.

An RFC that is returned for revision is not accepted. Discussion or preliminary approval must not be represented as an adopted specification change.

## 4. Maintainers

Additional maintainers may be appointed when sustained contributions and review experience justify the responsibility.

An appointment SHOULD record:

- The maintainer's identity and relevant contribution history.
- The areas they are authorized to review or maintain.
- Any limits on their authority to approve or merge changes.
- The process for revisiting or withdrawing the appointment.

Until broader authority is explicitly recorded, the steward retains responsibility for final normative specification decisions.

Maintainer status does not authorize a person to change the specification outside the documented process.

## 5. Independence and conflicts of interest

0xBUFF may develop or offer products that implement OEE. That commercial relationship MUST remain distinct from the governance of the public specification.

People participating in a decision SHOULD disclose a material conflict of interest when it could reasonably affect the decision.

The following principles apply:

- The public specification is changed through the same documented process regardless of who proposes the change.
- A commercial product's implementation choices do not automatically become normative requirements.
- Product adoption or purchase MUST NOT determine a course's published status.
- Compatibility with alternative implementations MUST NOT be rejected solely because an implementation is not a 0xBUFF product.
- Decisions with a material commercial implication SHOULD explain the relevant reasoning.

## 6. Intellectual property and attribution

Contributions are submitted under the applicable repository license and sign-off policy. The DCO is an attestation of the contributor's right to submit the work; it is not a copyright assignment.

Authorship, copyright, trademark rights, and stewardship are separate matters. A trademark registration does not, by itself, establish ownership of every text or code contribution in the repository.

The repository MUST preserve appropriate notices and follow the terms of its declared licenses.

## 7. Revisiting the governance model

The steward SHOULD review whether a broader governance model is warranted as external adoption, recurring contributions, or implementation activity increases.

Relevant triggers include:

- Multiple independent maintainers regularly reviewing and merging changes.
- Adoption of OEE by external organizations.
- Formal use of an OEE conformance claim or mark.
- A material dispute over stewardship, attribution, or the direction of the specification.
- A reasonable request for greater institutional independence.

Any change to the governance model MUST be documented and adopted through the established process.

## 8. Public decision record

Material decisions about the specification MUST be recorded in public issues, RFCs, pull requests, or other repository records.

Private communication may help resolve a question, but it MUST NOT be the sole record of a normative decision that changes the public specification.

The repository's public history is the reference for determining which requirements were adopted and when.
