# Requests for Comments (RFCs)

RFCs document proposed changes to the requirements, governance, or public scope of Open Engineering Education (OEE). They explain the problem, relevant alternatives, the proposed decision, and its consequences.

**A proposal is not a requirement.** The current educational requirements live in [`spec/`](../spec/README.md). An accepted RFC records a decision; normative changes take effect only when the corresponding specification update is reviewed and merged.

## When to write an RFC

An RFC is required for a change that affects:

- Normative principles or other binding requirements in `spec/`.
- Required course metadata, assessment, structure, or completion conditions.
- The meaning or evidence requirements of course status labels.
- Conformance criteria or claims.
- Licensing, contributor obligations, or governance policy.
- The boundary between OEE's specification, curriculum, and implementations.
- Repository-wide structural decisions that change the standard's scope.

Routine corrections that preserve normative meaning can proceed directly through a pull request. If the distinction is unclear, raise the question in a public issue before changing a requirement.

The one-time exception for initial course-format stabilization has **expired**. Its original scope remains recorded in [Governance](../GOVERNANCE.md); it is not an exception available to new proposals.

## Write a self-contained proposal

Start from the [RFC template](TEMPLATE.md). A reader should be able to understand the proposal and its trade-offs without consulting internal architecture decisions, private planning documents, or implementation tickets.

A substantive proposal must cover the problem, affected people or systems, the recommended change, a credible alternative, impacts on courses and implementations, relevant conformance or evidence implications, migration considerations, and unresolved questions.

Include proposed wording when the wording is material to the decision. Refer to public specification documents for existing requirements, but explain the **new** decision fully in the RFC. Keep changing task ownership, progress updates, and release scheduling in public issue or pull-request discussions, not in the adopted technical contract.

## Decision lifecycle

| Status | Meaning |
| --- | --- |
| `draft` | Open for preparation or discussion; not approved |
| `accepted` | Approved for implementation under the recorded conditions |
| `rejected` | Declined, with a recorded reason |
| `withdrawn` | Withdrawn by the proposer |

The process follows [Governance](../GOVERNANCE.md):

1. Describe the problem and draft an RFC using the template.
2. Discuss the proposal publicly and revise it in response to substantive feedback.
3. Record the steward's acceptance, rejection, or request for revision.
4. For an accepted change, submit a separate implementation PR updating the affected authoritative documents and validation.
5. Record the implementation outcome or any unresolved work without rewriting the historical rationale.

The decision record should identify the decision-maker, date, reasons, significant alternatives or objections, conditions, and adopted implementation when applicable. Discussion alone is not approval.

## RFC index

| RFC | Decision | Implementation |
| --- | --- | --- |
| [0001 — Outcome-driven curriculum and proportionate assessment](0001-outcome-driven-curriculum.md) | Accepted, 2026-11-07 | [Normative specification update, PR #34](https://github.com/0xbuffdev/open-engineering-education/pull/34) |
| [0002 — Public Toolkit stewardship, scope, and licensing](0002-toolkit-stewardship-and-licensing.md) | Accepted, 2026-11-15 | [Steward decision, PR #63](https://github.com/0xbuffdev/open-engineering-education/pull/63); official package release remains separately gated |
| [0003 — SEF academic progression and mathematical readiness](0003-sef-academic-progression.md) | Accepted, 2026-11-16; course changes merged | [SEF11/SEF8 migration PR #83](https://github.com/0xbuffdev/open-engineering-education/pull/83) through [SEF10 completion PR #101](https://github.com/0xbuffdev/open-engineering-education/pull/101); [current SEF curriculum](../curriculum/SEF/README.md). Learner validation remains separate. |
| [0004 — Current-only OEE course sources](0004-current-only-course-sources.md) | Accepted, 2026-11-19 | [Current source and conformance wording, PR #250](https://github.com/0xbuffdev/open-engineering-education/pull/250) (merged into SEC integration in PR #250) |
