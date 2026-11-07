# SEF10 — Software Engineering Foundations Capstone

**Program:** SEF — Software Engineering Foundations
**Type:** `project`
**Prerequisites:** [SEF1](SEF1.md)–[SEF9](SEF9.md)
**Duration:** 8–10 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; calibrate with learner evidence)

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Design, build, measure, release, and defend **one useful command-line
developer utility**. This is a cumulative engineering project: the learner
chooses and scopes the problem in the first module, implements it
incrementally, and develops the **same artifact** through review and
technical defense. The final module is not where the project begins.

The capstone integrates software construction, algorithms, data
structures, systems knowledge, version control, tests, debugging,
measurement, and mathematical reasoning acquired across SEF. It does
not force arbitrary features merely to showcase every earlier topic.

There is no prescribed implementation language, repository hosting
platform, paid infrastructure, AI assistant, or external mentor. All
requirements and evaluation criteria are public. Instructional
examples should demonstrate **different** problems rather than
supply a complete assessed implementation. Feedback and escalating
hints are permitted; the learner must own the technical decisions,
code, verification, and final unassisted challenge.

SEF8 may be studied alongside earlier SEF courses, but the required
SEF1–SEF9 capabilities must be demonstrated before this capstone is
completed. The duration is a planning estimate, not evidence of
completion or course readiness.

## Learning outcomes

- **SEF10-O1:** Select and bound a useful developer-utility problem with users, safe operating constraints, testable acceptance cases, and explicit exclusions.
- **SEF10-O2:** Design a modular architecture with clear interfaces and justify at least one substantial data-structure and algorithmic choice, including time/space reasoning.
- **SEF10-O3:** Implement a usable, safe CLI incrementally with meaningful version history, input contracts, error handling, and reproducible behavior.
- **SEF10-O4:** Use automated tests, debugging, and a repeatable CI or equivalent local workflow to verify normal, boundary, invalid, and operational-failure cases.
- **SEF10-O5:** Measure a meaningful engineering property under controlled conditions and use a documented before/after comparison to justify a technical decision.
- **SEF10-O6:** Package and document the project for clean-checkout installation, execution, testing, and independent evaluation.
- **SEF10-O7:** Relate each core requirement to inspectable evidence, reproduce the project independently, and resolve material review and safety findings.
- **SEF10-O8:** Defend the implementation, limitations, trade-offs, and any AI assistance, and complete a scoped change or debugging challenge without an assistant.

## Modules

### Module 1 — Problem and Scope

#### Outcomes

- SEF10-O1
- SEF10-O2

#### Lessons

1. **Capstone Orientation** — Explain why one learner-owned project develops throughout the course and how evaluation differs from optional practice.
2. **Users and Problems** — Identify a specific user, useful task, and observable improvement.
3. **CLI Contracts** — Define commands, input formats, output behavior, exit codes, and safe file effects.
4. **Acceptance Scenarios** — Specify normal, empty, boundary, invalid, and failure cases with checkable expected behavior.
5. **Scope and Risk** — Distinguish achievable core work from optional stretch features and identify environmental constraints.
6. **Scope Review** — Evaluate feasibility and record an explicit approval or structured self-review before substantial implementation.

**Milestone M1 — Scope:** A bounded public-format project brief and
acceptance cases exist. Any unbounded, destructive, untestable, or
unreasonably large proposal must be revised before proceeding. M1
contributes evidence to SEF10-AS1; it is not an additional standalone
quiz or lab.

### Module 2 — Architecture and Design

#### Outcomes

- SEF10-O2
- SEF10-O1
- SEF10-O4

#### Lessons

1. **System Decomposition** — Separate parsing, validation, core processing, and reporting into justified components.
2. **Interfaces and Ownership** — Describe data movement, errors, resource ownership, and trust boundaries.
3. **Data Structures** — Select a useful representation and explain the alternatives.
4. **Algorithmic Reasoning** — Estimate correctness constraints, time cost, and space cost under stated assumptions.
5. **Test Strategy** — Map acceptance cases and risks to initial tests and fixtures.
6. **Design Review** — Challenge an architectural assumption and record the response and first vertical slice.

**Milestone M2 — Design:** Architecture sketch, interface contracts,
data/algorithm decision, acceptance-to-component mapping, and the
first test plan are inspectable. Material design gaps must be
corrected before the affected implementation is relied upon. M2
completes the initial evidence for SEF10-AS1.

### Module 3 — Incremental Implementation

#### Outcomes

- SEF10-O3
- SEF10-O4
- SEF10-O2

#### Lessons

1. **Project Setup** — Establish a version-controlled project and documented build/test commands.
2. **First Failing Test** — Define an acceptance test that exposes missing behavior before implementing it.
3. **Vertical Slice** — Implement one useful command-to-result path with all relevant layers connected.
4. **Input Validation** — Handle malformed, empty, and boundary inputs safely.
5. **Debugging and Regression** — Reproduce a failure, correct it, and retain a test preventing recurrence.
6. **Versioned Iteration** — Evolve the same project through explainable commits and repeatable checks.

**Milestone M3 — Build:** At least one complete feature and one
negative path execute from documented commands. Retain the red/green
test evidence, incremental history, and at least one diagnosed and
corrected error. This is part of SEF10-AS2, not a separately
mandated per-module lab.

### Module 4 — Measurement and Release

#### Outcomes

- SEF10-O5
- SEF10-O6
- SEF10-O4

#### Lessons

1. **Measurement Design** — Choose a meaningful property, fixed fixtures, units, and relevant environment conditions.
2. **Baseline Analysis** — Collect repeated measurements and describe variability and limitations.
3. **Evidence-Based Revision** — Make or reject a justified change using comparable before/after results.
4. **Technical Documentation** — Write clear setup, use, testing, failure-handling, and architecture instructions.
5. **Reproducible Packaging** — Prepare a build or release that does not depend on undocumented local state.
6. **Release Verification** — Repeat declared test/build/package checks from a clean checkout.

**Milestone M4 — Measure and Prepare:** Reproducible measurements,
documented decision, README, release instructions, and repeatable
validation are reviewable. An observed regression or inconclusive
result may be reported honestly; a fabricated improvement is never
required to satisfy the outcome. This evidence contributes to
SEF10-AS2.

### Module 5 — Integration and Review

#### Outcomes

- SEF10-O7
- SEF10-O6
- SEF10-O4

#### Lessons

1. **Requirements Traceability** — Link each mandatory acceptance case to code, tests, observations, or explanation.
2. **Failure-Path Review** — Check cleanup, permissions, invalid data, and critical safety conditions.
3. **Clean-Start Reproduction** — Rebuild and rerun the project without relying on the original working directory.
4. **Evidence Review** — Compare actual implementation and measurements with the submitted claims.
5. **Finding Remediation** — Correct material defects and retain regression evidence.
6. **Defense Preparation** — Organize a reviewer-accessible explanation without supplying scripted answers.

**Milestone M5 — Rehearse:** A clean isolated checkout reproduces
the project; the requirements-to-evidence map is usable; critical
findings are resolved or explicitly reopen the relevant earlier
milestone. A self-directed learner may provide a dated independent
replay and self-review, disclosing the lack of external sign-off.
M5 contributes to SEF10-AS3.

### Module 6 — Delivery and Defense

#### Outcomes

- SEF10-O8
- SEF10-O7
- SEF10-O3
- SEF10-O5

#### Lessons

1. **Release Inspection** — Present the approved scope, delivered behavior, tests, version history, and reproducible build.
2. **Design Defense** — Explain actual algorithm and data choices, interfaces, errors, and limitations.
3. **Measurement Defense** — Interpret what the evidence proves and what remains uncertain.
4. **Independent Change** — Diagnose a bounded new case or implement a small change without an assistant.
5. **Final Evaluation** — Apply the published rubric and record pass or specific revise-and-reassess findings.

**Milestone M6 — Defend:** Deliver and defend the **same project**
begun in Module 1. Complete the independent change, show its test
evidence, and record the final rubric decision. M6 is evaluated
through SEF10-AS3; it is not designated a mandatory final `lab`.

## Completion requirements

The capstone is completed by satisfying all required outcomes,
the public project contract, and the three **required summative
assessments** below. These evaluate **one cumulative project**;
they do not require three unrelated builds or a quiz/lab pair
in every module.

| Assessment | Required outcome coverage | Primary evaluation |
| --- | --- | --- |
| `SEF10-AS1` — Scope and Architecture | SEF10-O1, SEF10-O2 | Approved problem brief, acceptance and safety contract, design and algorithm decisions |
| `SEF10-AS2` — Engineering Delivery | SEF10-O3, SEF10-O4, SEF10-O5, SEF10-O6 | Working utility, tests, Git history, reproducible build, measured revision |
| `SEF10-AS3` — Review and Defense | SEF10-O7, SEF10-O8, SEF10-O3, SEF10-O5, SEF10-O6 | Clean-environment review, defended technical choices, bounded unassisted change |

A milestone is a progress and review gate for the same project.
Milestones M1–M6 identify when evidence should become inspectable;
they are **not six additional submissions** or separate graded labs.
Earlier material may be refined when findings justify revision.
The final evaluation must consider the current complete artifact
and the retained evidence of its engineering progression.

### Public project brief

Before substantial implementation, record these items in a
learner-owned version-controlled brief:

- **User and problem:** intended user, practical need, and bounded
  result that is independently useful.
- **CLI contract:** commands, arguments, accepted inputs, outputs,
  exit statuses, persistence or file effects, and exclusions.
- **Acceptance cases:** concrete normal, empty, boundary,
  malformed, and operational-failure scenarios, each with
  expected observable outcomes.
- **Environment and safety:** supported runtime/toolchain, data
  boundaries, file permissions, cleanup behavior, dependencies,
  and conditions for reproducible offline testing.
- **Data and algorithms:** one nontrivial operation and
  substantive structure, expected complexity, and a measurement
  question related to the design.
- **Risk and evidence:** likely failures, verification strategy,
  relevant limitations, and the evidence that will support
  each acceptance claim.
- **Core versus stretch:** the smallest useful deliverable
  and expressly optional enhancements.
- **Scope review:** recorded approval against the public
  criteria or reasoned self-review; rejected proposals must
  be revised, not treated as silently accepted.

### Project options

Choose one of these public problem briefs or propose an equivalent
bounded CLI utility. They describe **problem space**, not a
provided solution, implementation template, or prescribed algorithm:

| Option | Minimum useful behavior | Safety and reasoning |
| --- | --- | --- |
| Local log analyzer | Parse fixture logs, filter and aggregate events, report deterministic counts | Define malformed-record policy, data structure, and a measured property |
| Read-only duplicate-file finder | Scan an explicitly disposable directory and report duplicate candidates | Never delete; justify size/digest/content verification and time or memory trade-offs |
| Dependency explorer | Read a documented local manifest and report a graph and cycles | Reject invalid references; explain traversal, ordering, and complexity |
| Test-result reporter | Parse a bounded local test-result format and summarize outcomes and durations | Account for missing/malformed results and defend data collection/indexing |

A different project is acceptable when it satisfies the same
outcomes, core complexity, safe operating boundaries, and public
evaluation standards. Cosmetic changes to a copied full
implementation or reproducing a tutorial solution alone do
not demonstrate independent engineering ownership.

### Required core deliverables

Every approved project must provide:

1. **Usable CLI:** meaningful normal behavior, documented
   inputs and outputs, validation, informative errors,
   correct exit statuses, and safe handling of empty,
   boundary, invalid, and failure cases.
2. **Engineering design:** modular components with explainable
   interfaces, a nontrivial algorithm and data-structure
   decision, correctness argument, and justified time/space
   complexity under stated assumptions.
3. **Engineering history:** incremental version control,
   an initially failing acceptance test that is made to
   pass, subsequent regression evidence, and a documented
   significant design or debugging correction.
4. **Verification:** automated tests for the agreed
   acceptance and failure cases, safe filesystem behavior,
   a reproducible test command, and CI configuration or
   a locally runnable equivalent verification workflow.
5. **Measurement:** controlled before/after evaluation of
   one relevant property, fixed or comparable fixtures,
   units, repetitions, conditions, observed variability,
   and a justified decision including any uncertainty.
6. **Documentation and release:** a README, install/run/test
   commands, architecture diagram, important decisions,
   local release/package instructions, explicit
   environmental assumptions and known limitations.
7. **Reproducibility and review:** independent clean-checkout
   rehearsal, acceptance-to-evidence map, material
   review findings and fixes, and a meaningful
   engineering retrospective appropriate to a capstone.
8. **Defense:** evaluated explanation of the actual code,
   data structures, performance claims, safety boundaries,
   AI assistance where used, and a small scoped
   independently implemented or diagnosed change.

Do not add requirements for concurrency, extensive
visualizations, plugins, cloud deployment, advanced
performance optimization, cross-platform installation,
or unrelated production features solely to demonstrate
breadth. These are optional stretch work and cannot
compensate for a missing core criterion.

### Safe and independent environment

Use a nonprivileged local toolchain and version-controlled
source with synthetic or explicitly authorized public
fixtures. Test file-writing behavior only in a known
disposable project/temporary directory. Read-only
operation is the default for analysis tools; a
utility requiring writes must clearly bound its allowed
paths and cleanup behavior.

Record meaningful OS, compiler/runtime, dependency,
and build/test command information, including deterministic
inputs or seeds as applicable. Do not use real personal
files, secrets, privileged execution, destructive operations,
mandatory hosted CI, paid cloud resources, or proprietary
credentials in required evaluation.

An automated test or green CI badge is supporting
evidence, not proof of untested safety or capability.
No paid teaching platform, compulsory mentor, or AI
assistant is required.

### Milestone review criteria

| Gate | What must be inspectable | Stop or revise when |
| --- | --- | --- |
| M1 — Scope | Feasible brief, user task, safe CLI contract, acceptance cases | Scope is unsafe, unbounded, vague, or untestable |
| M2 — Design | Interfaces, decision record, algorithm/structure reasoning, test plan | Core scenarios lack a credible path or material risks are hidden |
| M3 — Build | First red/green test, vertical slice, incremental history, failure handling | End-to-end behavior or key safety case does not work |
| M4 — Measure | Controlled baseline and revision, repeatable tests, release guide | Measurement is uninterpretable or setup depends on hidden state |
| M5 — Rehearse | Independent clean-start replay, traceability matrix, reviewed fixes | Critical issues remain unaddressed or evidence cannot be inspected |
| M6 — Defend | Final deliverable, defense record, independent change, rubric decision | Technical ownership or any mandatory rubric dimension is unproven |

Pacing within 8–10 weeks should reserve the largest
share of work for iterative implementation and adequate
time for independent review. Failing a gate means revise
and reassess the relevant work; it is not a demand for
a new standalone lab or an arbitrary numerical score.

### Required assessments

- **SEF10-AS1** (required scope and architecture evaluation)
  - Outcomes: SEF10-O1, SEF10-O2
  - Work: choose one bounded useful developer utility and
    complete the public project brief. Explain who needs
    the utility, define its safe CLI and input/output
    contracts, enumerate concrete acceptance and
    failure cases, and distinguish core behavior from
    optional features. Propose a modular design,
    interface boundaries, selected data structures,
    a substantial algorithm and its expected
    time/space cost. Identify risks and a failing
    initial test; conduct a recorded scope/design
    review or structured self-review before building
    the core implementation.
  - Criteria: useful and feasible scoped objective,
    explicit safe operating envelope, testable normal
    and failure paths, credible decomposition, correct
    assumptions for complexity reasoning, planned
    evaluation and measurement, and meaningful
    response to a challenged design assumption.
    Projects with arbitrary complexity, unsupported
    destructive behavior, or no independently
    checkable acceptance conditions must be revised.
  - Evidence: versioned brief, acceptance-case matrix,
    architecture and interface sketches, data/algorithm
    reasoning, risk register, initial test plan,
    design decision record, and reviewer/self-review
    findings with any revised scope.

- **SEF10-AS2** (required implementation, verification, and measurement)
  - Outcomes: SEF10-O3, SEF10-O4, SEF10-O5, SEF10-O6
  - Work: develop the approved project from an initial
    failing acceptance test through a working vertical
    slice to the complete core scope. Demonstrate safe
    input validation, meaningful failures, a versioned
    correction and regression test, and repeatable
    build/test/CI-equivalent commands. Explain
    the implemented algorithms and their data costs.
    Perform a controlled baseline and a justified
    revision with comparable measurements. Prepare
    install/run/test and release documentation and
    demonstrate clean-checkout setup.
  - Criteria: required scenarios behave as specified;
    no unexplained critical data-loss, trust-boundary,
    permission, or resource-cleanup failure; meaningful
    history and test coverage; independently verifiable
    algorithm choice; honest measurement with recorded
    conditions, repetitions, variability, and limitations;
    reproduction from declared commands without hidden
    files, services, secrets, or undocumented state.
    An inconclusive measurement may support a decision
    to revert, retain, or investigate rather than a
    fabricated improvement.
  - Evidence: complete version-controlled code,
    red/green and regression history, normal/invalid
    and boundary test fixtures/results, local
    CI-equivalent commands or CI config, actual
    measurement records and revision identifiers,
    documented trade-offs, architecture diagram,
    README and release/packaging instructions,
    clean-environment test record, and limitations.

- **SEF10-AS3** (required independent review and technical defense)
  - Outcomes: SEF10-O7, SEF10-O8, SEF10-O3, SEF10-O5, SEF10-O6
  - Work: map every agreed core criterion to project
    evidence; replay build, tests, normal/failure
    behavior and the release from an isolated clean
    environment, or obtain an equivalent independent
    review. Correct each critical finding or explicitly
    reopen an earlier milestone. Present and defend
    the **same project** begun under SEF10-AS1.
    Explain architecture, algorithms, time/space
    reasoning, measurement interpretation, significant
    mistakes and corrections, limitations, and
    AI assistance where used. Without AI help during
    the defense, complete one reviewer-selected
    small change or debugging challenge from the
    published categories: a new valid input, a
    controlled malformed-input case, a minor CLI
    option, or a repaired edge-case regression test.
    Record a dimension-by-dimension decision.
  - Criteria: clean-start operation and material
    acceptance cases reproduce; there are no
    unresolved critical safety defects; the learner
    can substantively explain and change their own
    implementation, trace evidence to requirements,
    justify measurement claims, disclose relevant
    assistance, and verify the scoped challenge
    using appropriate tests. A challenge must
    stay within the existing system and may not
    require a brand-new subsystem. The final
    defense must be reviewable in the format used.
  - Evidence: clean-checkout reproduction and
    requirement-to-evidence map, review findings
    and remediations, final release and assessment
    rubric, code/command/output inspection record,
    a focused unassisted change or debugging trace
    with verification results, AI-use disclosure
    if applicable, technical defense recording
    or written transcript with references, and
    technical retrospective.

### Project defense and assessment rubric

A live technical review is appropriate where
available, but a recorded walkthrough, structured
written defense with inspectable code/commands, or
another reviewable evaluation may establish the
same outcomes. A reviewer may choose a challenge
within one of the published categories; the
category is disclosed, but the specific input
or bug need not be disclosed in advance.

For independent learners without access to a
reviewer, a time-ordered unassisted session
record, a separate clean-environment replay
and an explicitly declared self-evaluation
can supply reviewable evidence. **Lack of
external sign-off must be disclosed**; a
self-review is not an independent reviewer
endorsement. AI assistance is permitted in
the broader project consistent with SEF9,
but it must be understood, verified, and
disclosed where applicable; no assistant may
perform the scoped defense change for the learner.

All mandatory rubric dimensions must pass:

| Dimension | Required demonstration |
| --- | --- |
| User value and scope | The approved useful task and acceptance boundaries are met |
| Correctness and safety | Normal, empty, malformed, boundary, and failure behavior is verified without unresolved critical hazards |
| Engineering quality | Modularity, meaningful Git progression, reproducible tests and release, and documentation |
| Algorithms and quantitative reasoning | Justified data structure/algorithm, complexity analysis, and interpretable measurement-based decision |
| Traceability and reproduction | Core claims link to inspectable evidence and can be repeated from a clean start |
| Ownership and defense | Learner explains actual implementation, responds to a bounded challenge unassisted, and documents limitations |

A missing dimension results in **revise and reassess**,
with a specific evidence gap or defect recorded;
there is no arbitrary numerical passing score.
A polished interface, optional stretch feature,
copied tutorial, AI-generated code, or successful
happy-path demonstration cannot substitute for
required capability and safety evidence.

### Formative activities and revision history

Optional practice may include critiquing unrelated
sample project briefs, testing hypothetical
algorithm claims, exploring design alternatives,
debugging small synthetic examples, or rehearsing
an explanation. These activities help learning but
are not extra graded submissions.

The previous SEF10 revision mandated one checkpoint
and one lab in each of six modules plus a final
lab-shaped delivery requirement. This revision
retains the **one-project, six-stage progression,
public safety rules, defined project options,
milestone gates, measurement, clean-checkout
reproduction, and independent defense**, but
evaluates the work through three coherent
summative assessments. Historical learner
evidence remains attributable to the
requirements actually in effect when evaluated;
the rewrite neither invalidates earlier records
nor claims automatic equivalence.

This capstone remains `draft`. Passing the
structural validator does not establish
teaching efficacy, independently reproduced
project options, learner testing, or `verified`
status. See [Evidence Rules](../../spec/evidence-rules.md)
and [Status Labels](../../spec/status-labels.md).

This is the **Program 1 graduation requirement**.
