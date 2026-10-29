# Principles

These principles govern Open Engineering Education (OEE), its curriculum, and implementations that claim to follow the specification. Normative requirements in the other specification documents turn these principles into testable expectations.

## 1. Evidence over completion

Learning is demonstrated through observable work, not inferred from time spent, activity completion, or familiarity with terminology.

A course MUST define observable outcomes and the evidence required to demonstrate them. Where executable work is required, the evidence SHOULD make independent reproduction possible.

**This rules out:**

- Treating time spent as proof of competence.
- Treating unchecked activities as proof of completion.
- Claiming completion without evidence that supports the claim.
- Using a certificate or completion indicator as a substitute for demonstrated capability.

## 2. Mechanism before tooling

Learners should develop an understanding of the mechanisms behind the systems they use.

Courses SHOULD connect visible behavior to the underlying concepts, constraints, interfaces, and failure modes. Learners SHOULD be able to explain why an approach works, under what conditions it works, and where it may fail.

**This rules out:**

- Defining competence solely as the ability to call a framework or service API.
- Requiring memorized procedures without understanding their purpose.
- Assessments that can be passed without demonstrating the intended engineering capability.

## 3. Honest claims

Claims about course readiness, learner outcomes, benchmark results, and implementation conformance MUST be supported by evidence appropriate to the claim.

Limitations, assumptions, and known gaps MUST be stated where they materially affect interpretation. Status labels MUST follow the requirements in [Status Labels](status-labels.md).

**This rules out:**

- Presenting untested course content as proven.
- Generalizing from a small or unrepresentative set of results.
- Omitting important limitations from a project report.
- Using status labels as marketing descriptions rather than evidence-based classifications.

## 4. Open by default

The public specification and curriculum are published under their declared licenses. The ability to read and apply OEE MUST NOT depend on purchasing a particular commercial product.

Optional products may offer hosted execution, managed assessment, instructor support, or other services. Such offerings MUST remain distinct from the normative requirements unless a change is proposed and adopted through OEE governance.

**This rules out:**

- Silently moving existing public specification requirements behind a paywall.
- Making conformance depend on one vendor's proprietary implementation.
- Changing the public boundary through product documentation or marketing alone.

## How the principles become requirements

| Principle | Primary specification |
| --- | --- |
| Evidence over completion | [Evidence Rules](evidence-rules.md) |
| Mechanism before tooling | [Course Format](course-format.md) |
| Honest claims | [Status Labels](status-labels.md) and [Conformance](conformance.md) |
| Open by default | [Implementation Boundary](implementation-boundary.md) |

## Changing the principles

A change to these principles MUST be proposed through an [RFC](../rfcs/README.md). The proposal must explain the reason for the change, the requirements affected, and the implications for existing course files and implementations.

A principle MUST NOT be weakened indirectly through a course template, script, or implementation change.