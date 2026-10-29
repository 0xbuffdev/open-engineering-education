# Implementation Boundary

This document defines the responsibilities of the OEE specification, its curriculum, supporting tools, and individual implementations.

The purpose of this boundary is to keep the public standard consistent even when different people or organizations build different ways to use it.

## 1. The specification

The specification defines the common requirements for OEE.

Its normative documents establish:

- The principles governing engineering education in OEE.
- The required course format.
- The evidence needed to demonstrate learning and completion.
- The meaning and requirements of the course status labels.
- The criteria used to assess conformance.

The specification MUST NOT prescribe a vendor-specific implementation when different approaches can satisfy the same educational requirement.

A tool, course, or product MUST NOT silently change a normative requirement.

## 2. The curriculum

The curriculum applies the specification to particular programs and courses.

Curriculum authors are responsible for defining course outcomes, teaching sequences, assessments, labs, completion requirements, and the evidence learners are expected to produce.

Curriculum files MAY provide more specific requirements than the general specification when those requirements are appropriate to the subject. They MUST NOT contradict the specification.

A course-specific requirement does not automatically become a new global requirement for OEE. A proposed change to the shared standard MUST follow the [RFC process](../rfcs/README.md).

## 3. Supporting tools

Templates, scripts, automated checks, assessment tools, and other supporting systems may help authors and learners apply OEE.

Such tools SHOULD make required actions easier to understand, perform, and review. Where a tool automatically checks a requirement, its behavior SHOULD be documented well enough to interpret the result.

A supporting tool MUST NOT:

- Change the meaning of a course status label.
- Treat activity completion as sufficient proof when evidence is required.
- Claim to establish outcomes it does not evaluate.
- Make an undocumented product-specific rule part of the public specification.
- Require a particular commercial service where the specification allows other approaches.

Manual review remains valid where automated evaluation would be insufficient or inappropriate.

## 4. Reference implementation

0xNAND is the paid reference implementation developed under 0xBUFF.

It may demonstrate how OEE requirements can be applied in a working product. Its implementation choices, pricing, and additional features are distinct from the public specification.

Using 0xNAND is optional. An implementation may apply OEE without using 0xNAND, and use of 0xNAND alone does not establish conformance.

Any claim that 0xNAND or another implementation conforms to OEE MUST be supported by an assessment appropriate to the scope of the claim.

## 5. Commercial boundaries

Optional commercial products or services may provide hosted execution, automated assessment, instructor support, managed cohorts, or other additional capabilities.

The existence of such services MUST NOT make the public specification dependent on purchasing them.

A commercial implementation MAY provide additional capabilities, but it MUST distinguish those capabilities from the requirements defined by OEE.

Changes to the public specification MUST be made through the documented governance process. Product releases, pricing changes, and marketing statements do not amend the standard.

## 6. Learner ownership and evidence

Learners control their own working environments and learner artifacts, subject to the terms of any platform they choose to use.

Supporting tools MAY help learners record and organize evidence. They MUST NOT imply that an artifact exists or that an outcome has been demonstrated when the required evidence has not been produced or reviewed.

Evidence and status claims must follow [Evidence Rules](evidence-rules.md) and [Status Labels](status-labels.md).

Credentials, secrets, and private learner information MUST be handled responsibly and MUST NOT be exposed merely to satisfy a documentation requirement.

## 7. Changes to this boundary

Changes that alter the responsibilities of the specification, curriculum, tools, or reference implementation MUST be proposed through the [RFC process](../rfcs/README.md).

The proposal MUST explain the affected requirements, the reason for the change, and its consequences for existing material and implementations.