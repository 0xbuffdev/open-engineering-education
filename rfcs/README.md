# Requests for Comments (RFCs)

An RFC is the formal proposal process for changes that affect the normative requirements or governance of Open Engineering Education (OEE).

The process gives contributors a place to explain a problem, evaluate alternatives, identify consequences, and record a decision before implementing a significant change.

## One-time initial course-format stabilization

OEE v0.0.1 began with a draft specification but no populated canonical curriculum. The first usable course-format baseline can therefore be established by the steward through a **focused public pull request**, without an additional RFC.

**This exception applies only to the initial format-stabilization pull request** and changes directly necessary to align its course-format requirements, conformance checks, and related governance documentation. The pull request MUST explain the reasons for the change, affected requirements, compatibility considerations, and review decision. The exception expires when that pull request is merged. It does not waive contributor sign-off, licensing obligations, public review, learning-evidence requirements, or course status checks, and it does not authorize unrelated changes to principles, commercial boundaries, or status evidence.

Until the first format-stabilization pull request is merged, the published draft specification remains authoritative. All subsequent normative changes MUST follow the RFC process. The prior [RFC proposal PR #6](https://github.com/0xbuffdev/open-engineering-education/pull/6) was closed as superseded without being accepted or merged; its discussion remains accessible.

## When an RFC is required

After this one-time initial course-format stabilization, an RFC MUST be proposed for changes that affect:

- The principles or normative documents in `spec/`.
- Required course metadata, structure, assessment, or completion requirements.
- The meaning or evidence requirements of status labels.
- Conformance criteria or public conformance claims.
- Licensing, contributor obligations, or governance policy.
- The boundary between the specification, curriculum, and implementations.
- Repository-wide structure where the change affects the standard's scope.
- Any existing requirement whose modification could affect whether courses or implementations satisfy the specification.

Routine corrections that do not change normative meaning may proceed directly through a pull request.

If it is unclear whether a change is normative, open an issue to establish the appropriate process before implementation.

## RFC lifecycle

An RFC uses one of four states:

| State | Meaning |
| --- | --- |
| `draft` | The proposal is being prepared or discussed and has not been accepted. |
| `accepted` | The proposal has been approved for implementation, subject to its recorded conditions. |
| `rejected` | The proposal has been declined, with the decision recorded. |
| `withdrawn` | The author has withdrawn the proposal before implementation. |

A status is not a measure of technical quality. It records the proposal's current decision state.

## Process

1. **Identify the problem.** Open an issue or begin an RFC proposal explaining the affected requirement and the reason for change.
2. **Write the proposal.** Use [`TEMPLATE.md`](TEMPLATE.md) to describe the proposed change, alternatives, impacts, and unanswered questions.
3. **Discuss the proposal.** Address technical objections and revise the proposal as needed. Discussion must distinguish established facts from assumptions.
4. **Record the decision.** The steward accepts, rejects, or returns the proposal for revision under the current governance policy.
5. **Implement accepted changes.** Open a pull request that links to the RFC and updates all affected normative text, references, and tests.
6. **Record completion.** Update the RFC with the merged change or the reason implementation did not proceed.

An accepted RFC authorizes implementation; it does not itself change the published specification. The specification changes when the corresponding pull request is reviewed and merged.

## What a proposal must contain

An RFC MUST identify:

- The problem and the people or systems affected.
- The proposed change in concrete terms.
- At least one meaningful alternative considered.
- The effect on existing courses and implementations.
- Any effect on status labels, evidence requirements, or conformance.
- Any transition steps needed to adopt the change.
- Unresolved questions that affect the decision.

The proposal SHOULD include the exact proposed wording when the wording itself is the change.

## Decision records

A decision MUST be recorded in the RFC or linked decision discussion.

For an acceptance, the record SHOULD state any conditions and required migration steps. For a rejection, it SHOULD explain the material reasons. A proposal returned for revision remains a draft until a decision is recorded.

## Index

Add a row for each substantive RFC so contributors can find previous decisions.

| RFC | Title | Status | Decision |
| --- | --- | --- | --- |
| [0001](0001-outcome-driven-curriculum.md) | Outcome-Driven Curriculum and Proportionate Assessment | `accepted` | Accepted in principle; normative implementation pending |
