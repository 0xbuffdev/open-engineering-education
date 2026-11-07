# RFC 0001: Outcome-Driven Curriculum and Proportionate Assessment

- **Status:** `accepted`
- **Author:** 0xBUFF (proposal for steward review)
- **Created:** 2026-11-07
- **Last updated:** 2026-11-07
- **Related issue:** [APP curriculum redesign #30](https://github.com/0xbuffdev/open-engineering-education/issues/30) (related implementation dependency, not a substitute for this RFC)
- **Affected specification version:** published draft `v0.0.1`; target version to be determined at adoption

## 1. Summary

Make demonstrated learning outcomes, rather than a uniform activity template, the basis of OEE course design and completion. Retain rigorous public assessment criteria and reproducible evidence for substantial engineering work, while allowing each course to choose the most appropriate combination of teaching, practice, feedback, tests, investigations, labs, projects, and defenses.

The curriculum will continue to be independently usable without any paid platform. OEE Workspace and 0xNAND will share a stable public educational contract rather than independently redefining course completion.

This RFC is accepted as a design decision. Its requirements are **not yet normative**: the current published specification remains in force until separate implementation changes are reviewed and merged.

## 2. Problem

### Current requirements that create rigidity

1. [Course Format §4](../spec/course-format.md) currently requires the final lesson entry of **every** course, including project courses, to be a `lab`, whether or not that is the most suitable integrated demonstration.
2. Course Format §3 places `lesson`, `test`, and `lab` in a single lesson-kind list. Section 4 recommends the sequence `lesson → test → lab` when all three appear. Even though a module may omit a test or lab, the representation encourages near-identical assessment patterns.
3. [Evidence Rules §2](../spec/evidence-rules.md) defaults to requiring conceptual checkpoints, exercises, a final lab, documented tests, design explanations, a retrospective, and evidence, even when those requirements overlap or do not fit the assessed outcome.
4. Project courses additionally require deliverables, evaluation, and defense. Their tests and labs can duplicate work that is already part of one cumulative project.
5. Lesson navigation entries and assessment requirements are entangled, which makes it harder for independent and commercial implementations to give different forms of instruction while evaluating the same capability.

### Representative examples on main at proposal time

- SEF1: 10 modules, 9 typed tests, 10 typed labs.
- APP1: 8 modules, 8 typed tests, 8 typed labs.
- SEF10: 6 modules, 6 typed tests, 6 typed labs, plus project deliverables and defense.
- APP9: 9 modules, 8 typed tests, 9 typed labs, plus project deliverables and defense.

These are counts of typed navigation entries, not an assertion that every activity is pedagogically redundant. The proposal aims to eliminate unjustified *requirements*, not useful practical work.

[APP1 draft PR #31](https://github.com/0xbuffdev/open-engineering-education/pull/31) is an important dependency: it proposes 17 tests and 17 labs, and must be reassessed against any adopted model before merging.

## 3. Proposed change

### 3.1 Core principle and terms

Replace activity-count-driven course completion with outcome-driven evaluation.

- A **learning outcome** describes an observable capability the learner must demonstrate.
- A **learning activity** provides instruction or practice (for example a lesson, worked example, exercise, simulation, investigation, or lab).
- A **formative check** provides feedback for improvement. It does not independently establish course completion unless explicitly designated as required evidence for an outcome.
- A **summative assessment** evaluates one or more learning outcomes against published success criteria to support a completion decision.
- A **lab** is a practical activity format, not a mandatory assessment stage.
- An **evidence record** documents an artifact or observed performance and the criteria against which it was evaluated.

An automated test of software behavior is not the same thing as a learner knowledge test. Lab verification is an evaluation technique, not a mandatory additional exam.

### 3.2 Proposed requirements for Course Format

Proposed normative wording:

> Every course MUST define observable learning outcomes and a publicly understandable means of evaluating each required outcome. Every required summative assessment MUST identify the outcomes assessed, the work expected, the applicable success criteria, and sufficient evidence for a reviewer to make an evaluation decision. One assessment MAY address multiple outcomes, and an outcome MAY be evaluated through multiple assessments.
>
> OEE MUST NOT require a fixed number or sequence of tests, exercises, labs, or projects for every module or course. A course MUST provide an appropriate integrated demonstration of its outcomes, but that demonstration need not be designated a `lab`. Course authors SHOULD choose assessment methods that are authentic to the capabilities evaluated and avoid requiring repetitive evidence for the same outcome without an educational justification.
>
> An instructional module MUST describe its expected outcomes and an ordered learning sequence. It MAY contain practical activities or checks. Assessment definitions MAY be linked from the module, the Completion requirements section, or a public assessment brief, provided there is one authoritative set of requirements.
>
> Required activities and optional practice MUST be distinguishable. Optional practice or formative checks MUST NOT silently become a condition of completion.

Preserve the four existing course-level headings (`Overview`, `Learning outcomes`, `Modules`, `Completion requirements`) for the first transition to minimize disruption. Remove the requirement to type every item inside `Lessons` as exactly `lesson`, `test`, or `lab`. Keep concise typed activity labels where pedagogically useful; do not prescribe a closed universal taxonomy.

Project courses MUST still define public deliverables, evaluation criteria, and a suitable defense of the learner's own work. Their implementation milestones SHOULD be treated as stages of one coherent project rather than independent labs by default. A defense MAY be live, recorded, written, or otherwise reviewable as appropriate to the work, without reducing the strength of the evaluation.

### 3.3 Proposed requirements for Evidence Rules

Replace the default completion checklist with:

> A learner completes a course only after the course's required learning outcomes are demonstrated against the published criteria and the required evidence is recorded. The course MUST make these requirements available before assessment. Reading, attendance, elapsed time, activity checkmarks, or unsubstantiated claims MUST NOT alone establish completion.
>
> Evidence obligations MUST be proportionate to the assessed work. For executable engineering artifacts, applicable reproduction instructions, environment assumptions, verification results, and material limitations MUST be available. For non-executable conceptual or analytical work, an inspectable explanation or evaluated performance MAY be suitable evidence. A course MUST NOT impose a generic build log, project retrospective, or complete lab report on every small exercise.
>
> Substantial engineering work MUST include an appropriate account of important trade-offs, failures, corrections, or limitations when they are relevant to interpreting the result. A substantive project MUST include a reviewable explanation of the learner's technical decisions. Self-check activities MAY supply feedback without generating a permanent evidence record.

The existing privacy, traceability, reproducibility, evidence-integrity, and truthful-claims principles remain in force.

### 3.4 Minimal stable identifiers and outcome coverage

For downstream interoperability, required course outcomes and required summative assessments SHOULD initially have stable, human-readable IDs during the pilot; after migration, they MUST have stable IDs in canonical course definitions. IDs MUST be preserved across editorial revisions unless the associated requirement is substantially replaced.

Example (illustrative rather than a new required serialization):

```markdown
## Learning outcomes

- **APP1-O1:** Trace a web request and distinguish name-resolution,
  transport, HTTP, and browser-policy failures.

## Modules

### Module 1 — How Web Requests Work
#### Outcomes
- APP1-O1
#### Lessons
1. Client/server communication
2. Addressing and name resolution
3. Optional: inspect a supplied browser trace

## Completion requirements

- **APP1-AS1** (required, practical investigation)
  - Outcomes: APP1-O1
  - Work: diagnose an unfamiliar failing browser request.
  - Evidence: observations, fault classification, and reasoned explanation.
  - Criteria: correct layer distinctions, reproducible observations where
    feasible, and conclusions supported by evidence.
```

A course MUST make it possible to trace every required outcome to at least one required summative assessment. This is an **outcome coverage** guarantee, not a rule demanding one independent assessment per outcome. Authors MUST check that each assessment can actually establish the claimed outcomes; matching IDs alone does not establish validity.

Module and lesson IDs MAY be introduced incrementally, provided any exposed IDs are stable. A versioned, machine-readable export and its transport schema will be handled in a separate implementation proposal; this RFC does not require YAML, JSON, a database, or a proprietary service.

### 3.5 Public assessment independence and delivery flexibility

A public OEE course MUST publish the assessed capabilities, required work, success criteria, and evidence expectations sufficiently for independent study and evaluation without a commercial account or paid book.

The specification MUST NOT require publication of every exact reusable examination item, private evaluation scenario, grading implementation, or answer key. Implementations MAY supply equivalent unseen scenarios, automated checks, and coached practice, but MUST NOT weaken published outcome criteria while claiming the same OEE completion requirement.

Additional instructional exercises, resources, mentoring, adaptive guidance, feedback, and assessment attempts offered by 0xNAND or another implementation MUST be distinguishable from the canonical OEE completion requirements.

### 3.6 Proposed related specification updates

- `spec/course-format.md`: remove mandatory final `lab`, fixed lesson-kind taxonomy, and assessment-order expectations; retain required outcome and public-criteria contract.
- `spec/evidence-rules.md`: replace the default activity checklist with proportionate, outcome-based evidence and completion.
- `spec/conformance.md`: assess outcome coverage, assessment appropriateness, independence, and evidence quality rather than mandatory lab placement/count.
- `spec/status-labels.md` and the matching section of Evidence Rules: replace lab-specific references with review/reproduction of **required summative evaluations**, where relevant. **Do not change** numerical learner thresholds or independent reviewer sign-off in this RFC; educational strength of status labels warrants separate review.
- Curriculum examples and scripts: validate meaningful coverage rather than mechanically requiring every module to contain a test and lab.

## 4. Alternatives considered

| Alternative | Advantages | Disadvantages | Decision |
| --- | --- | --- | --- |
| Keep current test/lab pattern and offer exceptions | Minimal migration | Makes redundancy the default; project courses remain awkward | Reject |
| Require exactly one final assessment per course | Simpler records | One activity may be insufficient to judge different outcome types | Reject |
| Make every activity and evidence format completely free-form | Maximum flexibility | Weakens conformance and interoperability | Reject |
| Outcomes plus appropriate required evidence, with flexible activities | Educationally authentic; supports different implementations | Requires author judgment and stronger review | **Propose** |

## 5. Impact assessment

### Existing courses and programs

Existing course and project definitions remain the canonical published requirements until an implementation PR is merged. A course must not silently drop previously required completion activities while the old normative specification still applies.

Pilot with:

1. SEF1 (foundational/conceptual-plus-simulation).
2. APP1 (web investigation and diagnosis, with draft PR #31 reviewed).
3. SEF10 or APP9 (one cumulative project with milestones and defense).

For every pilot, map current outcomes to proposed assessments, retain useful exercises as formative activities, remove duplicative compulsory submissions only after coverage review, and document substantive competency changes.

### Implementations

- **OEE Workspace:** existing learner files remain intact; generator updates should follow a separate review and must not overwrite or reclassify existing work.
- **0xNAND:** may add guided lessons, question banks, automated grading, and mentoring; it must use the same published outcome/evaluation requirements when claiming OEE completion.
- **External implementations:** must be able to satisfy public requirements without vendor-specific infrastructure.

### Evidence and status labels

Course completion requirements change. Existing evidence remains historically interpretable against the course revision under which it was produced. Do not retroactively declare a learner incomplete or completed merely by relabeling activities. Re-evaluation is required when substantial outcome/criteria changes occur.

This RFC does not propose changing the current `draft`, `tested`, or `verified` promotion thresholds; only replace lab-specific references where the new evaluation model makes those references inaccurate. A separate review may assess whether those thresholds are strong enough.

### Conformance

A structural validator must not infer educational validity from IDs alone. Conformance evaluations must identify the course/spec version and examine actual required outcome coverage, assessment design, evidence instructions, and implementation independence.

### Licensing and governance

No proposed licensing or stewardship change. Normative updates follow the existing RFC decision process, with implementation PR(s) only after acceptance.

## 6. Compatibility and transition

This is **not strictly backward-compatible** with the old mandatory-final-lab and default activity checklist. Implement in distinct reviewed stages:

1. Accept/revise this RFC; record final decision.
2. Update the normative specification in a separate PR; reconcile published version metadata across specification, catalogs, validators, and README.
3. Pilot SEF1, APP1, and one project course with old-to-new outcome/assessment mapping.
4. Add minimal validation for stable IDs, broken references, outcome coverage, and required assessment criteria.
5. Update OEE Workspace mappings/generators; verify existing workspace safety.
6. Provide a versioned export and 0xNAND integration contract in a later change.
7. Migrate remaining courses in small reviewable groups.

Preserve old revision references for evidence records and avoid silently rewriting a learner's historical results. Do not claim migration complete merely because Markdown passes linting.

## 7. Risks and mitigations

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Flexible assessments become too weak | High | Require outcome coverage and substantive, published success criteria; use expert review |
| Courses become inconsistent | Medium | Shared authoring examples and validation, not mandatory activity counts |
| Existing workspaces lose evidence relationships | High | Stable IDs, version pinning, non-destructive migrations |
| Paid platforms hide mandatory requirements | High | Public assessment contract and independent study alternative |
| Too many new metadata fields complicate authoring | Medium | Start with outcome/assessment IDs and public Markdown; defer export schema |
| Open APP1 draft entrenches old structure | Medium | Review PR #31 against adopted model before merge |
| Existing course status becomes misleading | Medium | Preserve historical revision attribution; independently review promotion evidence |

## 8. Validation plan

A pilot is successful only if reviewers can:

1. Trace each required outcome to sufficient, published summative evaluation criteria.
2. Verify that no required assessment is present solely because of a fixed template.
3. Demonstrate that foundational, applied, and project courses can use different appropriate evaluation patterns.
4. Complete the public required work using free tools/resources without a 0xNAND subscription.
5. Represent the same requirements in OEE Workspace and a hypothetical 0xNAND experience without contradictory completion rules.
6. Reproduce applicable engineering artifacts and review meaningful limitations, while not requiring full lab reports for trivial exercises.
7. Explain historical evidence against pinned course revisions without overwriting or silently altering progress.
8. Pass structural validation **and** a manual pedagogical/assessment-quality review.

Track learner time and reviewer burden when pilot learners are available, rather than claiming these are improved before testing.

## 9. Decisions and follow-up questions

1. **Resolved — integration:** required outcomes need adequate cumulative summative evidence; require an integrated demonstration only where course outcomes justify it. No universal mandatory final lab.
2. **Resolved — identifiers:** introduce stable identifiers for required course outcomes and summative assessments during the pilot; defer mandatory module and lesson identifiers.
3. **Implementation condition — versioning:** the normative implementation PR must identify the actual published baseline and select, document, and consistently apply the appropriate new draft specification version and migration rules. Until then, published `v0.0.1` requirements remain authoritative.
4. **Deferred — status-label strength:** existing learner-count thresholds and reviewer requirements remain unchanged by this decision; evaluate any strengthening in a separate RFC.

## 10. Decision

- **Decision:** Accepted (decision record proposed following the merge of [PR #32](https://github.com/0xbuffdev/open-engineering-education/pull/32))
- **Decision date:** 2026-11-07
- **Decision-maker:** 0xBUFF steward (subject to review and confirmation of this record)
- **Rationale:** Observable competence and published assessment criteria provide a stronger, less repetitive contract than mandated activity counts. The approach preserves serious engineering evidence, public independence, and multiple learning implementations, while allowing appropriate instructional and project assessment designs.
- **Conditions:** Make no normative change until an implementation PR is reviewed and merged; preserve current completion contracts for existing courses until separately migrated; reconcile specification versioning and downstream compatibility; require outcome-to-assessment coverage and an explicit manual quality review beyond structural checks. Keep 0xNAND-only delivery features non-normative. Do not change existing course status promotion thresholds through this RFC.
- **Implementation pull request:** [#34 — implement RFC 0001 normative specification](https://github.com/0xbuffdev/open-engineering-education/pull/34) (pending review and merge)

**Governance boundary:** Acceptance authorizes implementation work but does not change the published normative specification. This document records the accepted direction; adoption takes effect only through a separate merged implementation PR.
