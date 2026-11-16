# SEF5 — Software Engineering Practice

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF2](SEF2.md)
**Duration:** 8 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; calibrate with learner evidence)

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

SEF2 provides the foundational Python vocabulary for this engineering-practice course: function and module boundaries, small user-defined classes, meaningful composition, basic type annotations and explicit runtime validation. SEF5 extends that prior knowledge into maintainable software design, collaborative review, testing and release discipline; it does not silently treat a type hint as proof of safety or require a third-party type checker.

Develop the engineering practices needed to improve software safely after it works for the first time. Start with the program and tests built in SEF2, or a comparable small learner-owned command-line application. Learn to isolate changes in Git, diagnose failures with evidence, design meaningful tests, refactor without breaking a public contract, review code, build repeatable quality checks, and hand off a maintainable application for independent reproduction.

The reference environment is Python 3.11 or later, the Python standard library, and a local Git installation. The course can be completed offline with disposable repositories, `unittest` or equivalent independently runnable tests, a local quality-gate script, and a reviewable version-controlled CI configuration. Optional `pytest`, hosted Git platforms, remote pull requests, formatting tools, or type checkers may be used when available but are **not** required for completion. Any additional development dependency used in submitted work must be recorded with a reproducible installation procedure; a standard-library-only route requires none.

A local branch, reviewable diff and written review can demonstrate the relevant collaboration outcomes without contacting an external service. For CI, the required behavior is a reproducible quality-gate contract and a documented least-privilege workflow; learners may demonstrate failed and passing gates locally and have an independent reviewer inspect their CI configuration without publishing secrets or running an online pipeline. Actual hosted job logs are welcome as additional evidence, not a hidden gate.

The original seven-module instructional sequence is preserved. Six summative assessments evaluate connected skills; verified code, fixtures and review material may be reused rather than recreated for each module. A fixed quiz/lab pair, hosted CI service, or final lab beyond the published assessments is not required. All examples, test repositories, credentials, logs, and input records must be synthetic or owned by the learner. The course remains `draft`, with the 8-week workload estimate subject to learner validation.

## Learning outcomes

- **SEF5-O1:** Use Git staging, commits, branches, merges, and diffs to isolate intended changes and preserve an inspectable project history.
- **SEF5-O2:** Resolve merge conflicts, undo faulty changes without destroying unrelated work, and explain the safety difference between reverting published history and rewriting it.
- **SEF5-O3:** Design meaningful unit, integration, and command-line tests that exercise required behavior, failure contracts, and state changes using independent expected results.
- **SEF5-O4:** Diagnose a real or deliberately introduced defect through a reproducible failure, hypothesis-driven investigation, corrective change, and durable regression test.
- **SEF5-O5:** Refactor code into coherent components with explicit public interfaces while verifying that existing behavior, failure messages, exit statuses, and persistence contracts remain stable.
- **SEF5-O6:** Write maintainable code, safe diagnostic logs, and useful technical documentation without disclosing secrets or sensitive input data.
- **SEF5-O7:** Make tests deterministic and isolated by controlling state, clock, randomness, filesystem paths, and ordering; distinguish flaky tests from genuine product defects.
- **SEF5-O8:** Build repeatable local quality gates and a reviewable CI workflow that reject failures and reproduce successfully from a documented clean checkout.
- **SEF5-O9:** Identify and reduce risks from workflow permissions, untrusted input, dependency installation, secrets, and unreviewed automation, including safe offline equivalents.
- **SEF5-O10:** Conduct a focused code review, document material findings and their responses, and provide an independently reproducible engineering handoff.
- **SEF5-O11:** Prepare and verify a versioned, tested, maintainable command-line application that preserves a public behavioral contract across normal and failure paths.
- **SEF5-O12:** Defend engineering trade-offs, limits of automated checks, and a concrete failure-and-repair history using inspectable source and observed evidence.

## Modules

### Module 1 — Version Control & Collaboration

#### Outcomes

- SEF5-O1
- SEF5-O2
- SEF5-O10

#### Lessons

1. Course introduction: Software Engineering Practice
2. Repositories and commits
3. History and diffs
4. Branches
5. Merging
6. Merge conflicts
7. Remotes and pull requests
8. Staged versus working-tree changes
9. Reverting published changes versus rewriting history
10. Generated files, ignore rules and secret hygiene

*Optional practice:* Use a throwaway local Git repository to compare staged, unstaged, ignored, and committed changes; practice a conflict resolution and a non-destructive revert without a remote account.

### Module 2 — Testing & Debugging

#### Outcomes

- SEF5-O3
- SEF5-O4

#### Lessons

1. Assertions
2. Unit tests with Python unittest and optional pytest
3. Choosing test cases
4. Reproducing failures
5. Debugging by evidence
6. Unit and integration testing responsibilities
7. Parameterized cases, fixtures and isolation
8. Regression cases for previously observed defects

*Optional practice:* Create a small failure fixture for a function and a CLI entry point, then compare the evidence each test layer can observe.

### Module 3 — Maintainable Software

#### Outcomes

- SEF5-O5
- SEF5-O6
- SEF5-O10

#### Lessons

1. Code smells
2. Refactoring
3. Style guides
4. Logging
5. Code review
6. Reading unfamiliar code
7. Module boundaries and dependency direction
8. Behavior-preserving refactoring strategies
9. User-facing documentation and review evidence

*Optional practice:* Inspect a small change for coupling, logging, interface drift, and unnecessary churn; write a review comment describing an actionable correction.

### Module 4 — Testing Strategy & Reliability

#### Outcomes

- SEF5-O3
- SEF5-O7
- SEF5-O4

#### Lessons

1. Equivalence classes and boundary values
2. State-based testing and invariants
3. Unit, integration and end-to-end test selection
4. Property-based testing principles
5. Flaky tests, time and randomness
6. Testing negative paths and side effects

*Optional practice:* Compare a clock-dependent test and a test using an injected fixed clock, then isolate temporary directories and seed any generated data.

### Module 5 — Continuous Integration & Build Reproducibility

#### Outcomes

- SEF5-O8
- SEF5-O9

#### Lessons

1. Dependency lockfiles and isolated environments
2. Formatter, linter and static type checks
3. CI workflows, stages and failure gates
4. Secrets, permissions and untrusted CI input
5. Clean-checkout builds and release artifacts

*Optional practice:* Create a local `quality` command that runs tests and a deterministic syntax or formatting check; inspect a minimal, read-only CI workflow without giving it real credentials.

### Module 6 — Code Maintenance, Documentation & Handoff

#### Outcomes

- SEF5-O5
- SEF5-O6
- SEF5-O10
- SEF5-O12

#### Lessons

1. Contracts, coupling and interface stability
2. Logging, error context and sensitive data
3. Small reversible changes and meaningful commit history
4. Peer review and actionable feedback
5. README setup and contributor guidance
6. Dependency upgrades and technical-debt decisions

*Optional practice:* Ask a reviewer to follow a README in a disposable checkout; improve one missing instruction and explain a bounded change's risk.

### Module 7 — Tested CLI Application

#### Outcomes

- SEF5-O3
- SEF5-O4
- SEF5-O5
- SEF5-O6
- SEF5-O7
- SEF5-O8
- SEF5-O9
- SEF5-O10
- SEF5-O11
- SEF5-O12

#### Lessons

1. CLI behavior and versioned project contract
2. Unit, integration and subprocess-based tests
3. Logging, configuration and safe persistence
4. Reproducible local quality checks and CI workflow
5. Reviewable changes and clean-start handoff

*Optional practice:* Draft a release checklist covering CLI operations, failure and persistence cases, logging, test isolation, quality gates, and reviewer evidence.

## Completion requirements

### Environment, assessment decisions, and independent review

Use a disposable local repository and Python 3.11+; record Git, interpreter, test-runner, and optional tool versions. Provide exact commands to recreate test input, run checks, and reproduce a failure and its correction. Prefer `python -m unittest discover -s tests -v` for the dependency-free route; `pytest` or other tools are permitted when their versions, dependencies, and offline accessibility are documented. No real remote repository, credential, paid service, production file, or destructive action against unrelated work is required.

Each required assessment must have a reviewable source revision or portable artifacts, explicit expected behavior, observed outcomes and exit statuses, normal, boundary and negative-case evidence, a reasoned correction where an error is found, and a documented reviewer decision. When using a simulated pull request, include a diff, rationale, tests, and response to substantive feedback. A self-review using a separate role or structured checklist can provide preparation but does not substitute for the **independent reproduction** required for a final handoff.

All correctness, security, reproducibility and relevant review requirements stated below are mandatory. A green badge, a screenshot, a passing mock that bypasses behavior, or a cosmetic refactor is insufficient on its own. A reviewer may vary inputs or ask for a technical explanation within the published criteria. Previous assessed work may be revised and reused if the required evidence remains inspectable.

### Required summative assessments

- **SEF5-AS1** (required version control and reversible collaboration)
  - Outcomes: SEF5-O1, SEF5-O2, SEF5-O10
  - Work: In a disposable Git repository with a small Python CLI, create a baseline commit, two branches with conflicting functional edits, and an integration branch. Record the conflict, resolve it to a written behavioral contract, run the relevant tests and commit the resolution. Stage a generated report unintentionally alongside an unrelated working-tree edit, then unstage only the report and preserve the edit. Create and revert a separate defective change, explaining when `git revert`, selective staging and merge are safer than hard reset or force-pushing shared history. Write a simulated pull-request summary for the merged change, including diff, tests and potential risk.
  - Criteria: The intended features survive the conflict resolution; tests pass on the reconciled behavior; the generated report is not committed and unrelated edits are not discarded. The repository history, working tree and index demonstrate the claimed operations. The revert adds a reversible history entry rather than destroying unrelated work. The learner explains how local branch simulation relates to a hosted pull request without claiming that an online review occurred.
  - Evidence: Disposable repository or exportable Git history, conflict/status and diff snapshots, exact commands, pre- and post-merge tests, revert result, recorded staging corrections and a focused review summary.
  - Review variation: Provide an unfamiliar second conflict or staging state and ask for the safe sequence before executing it.

- **SEF5-AS2** (required failure reproduction and meaningful test design)
  - Outcomes: SEF5-O3, SEF5-O4, SEF5-O12
  - Work: Start from a small task-manager or import-capable CLI. Deliberately introduce a duplicate-identifier or malformed-record bug and demonstrate the original failure with an inspectable fixture. State competing hypotheses and collect evidence to identify the actual cause. Add both a direct unit test for the relevant behavior and an integration/subprocess test that exercises the real CLI entry point, including its exit status and persisted data. Correct the defect, then test normal input, missing or empty data, malformed content, duplicate identifiers and a persistence failure without relying only on mocked return values.
  - Criteria: The original tests or reproducer fail before correction and pass afterward with the same fixture. Unit and CLI-level tests exercise different observable boundaries and detect the originally seeded defect; errors are predictable and do not silently overwrite an existing valid state. The diagnosis distinguishes an actual code fault from a mock that bypasses the critical logic. Regression evidence demonstrates why the fix, rather than an exception-swallowing workaround, explains the behavior.
  - Evidence: Original and repaired source revisions, written input/output and storage contract, fixtures and exact commands, before/after test results, hypotheses and observations, CLI output/exit status, and retained persisted-data checks.

- **SEF5-AS3** (required behavior-preserving refactoring and code review)
  - Outcomes: SEF5-O5, SEF5-O6, SEF5-O10, SEF5-O12
  - Work: Select a duplicated or overly coupled feature from the SEF2-derived CLI, record its public command, output, persistence and error contract, and create characterization tests. Refactor parsing, domain operations and persistence into clear modules without changing the documented behavior; identify any intentionally corrected defect separately. Produce a compact reviewable patch, a rationale for dependency direction, and a simulated or actual code review containing at least one substantive finding. Address that finding in a follow-up change and update a README with setup, test commands, usage, and an example failure. Audit diagnostic logs so they expose useful context but no credentials or sensitive input.
  - Criteria: Existing public behavior, exit statuses, expected error text and data format match the before-state contract except for explicitly documented bug fixes; tests cover both normal and invalid paths. The diff remains focused, module interfaces are understandable and logging is safe. The review finding is actionable, has a documented resolution or defensible rejection, and is verified by rerunning the relevant tests. A reviewer can understand the change without an undocumented tool or hidden service.
  - Evidence: Before/after diff and characterization cases, module interface notes, CLI and persistence regression tests, written review and response, updated README, logging sample with synthetic data, and a short trade-off explanation.

- **SEF5-AS4** (required deterministic and isolated test suite)
  - Outcomes: SEF5-O3, SEF5-O4, SEF5-O7
  - Work: Prepare a small CLI test suite with two deliberately flaky mechanisms, such as a test depending on wall-clock time and a test assuming filesystem enumeration order. Demonstrate their failure or contract instability under controlled variation; explain why each is test nondeterminism rather than proof that the product fails. Replace ambient time with a controlled clock and define output order where the behavioral contract requires it; isolate mutable fixtures in a disposable temporary directory. Add separate equivalence-class, boundary, invalid-input and state-invariant cases for the CLI. Repeat the complete revised suite at least 20 times under the documented conditions, retaining results, and seed a genuine application bug to show the suite still rejects incorrect behavior.
  - Criteria: The submitted fixtures reproduce or deterministically expose both instability mechanisms; revised tests no longer depend on the uncontrolled clock or incidental enumeration order. All 20 repeated runs pass after correction, but the learner explicitly disclaims that this proves absence of all flakiness. A seeded behavioral defect still fails a meaningful assertion, not merely a timing assertion. Tests run without altering unrelated state or leaking fixtures between runs.
  - Evidence: Pre-repair fixture/observations, corrected tests and clock/order contract, isolated paths and input tables, 20-run test log or machine-readable tally, a rejected genuine defect, and an explanation of remaining reliability limits.

- **SEF5-AS5** (required reproducible quality gates and CI security)
  - Outcomes: SEF5-O8, SEF5-O9, SEF5-O12
  - Work: Define a version-controlled `quality` command that runs the project's tests plus a deterministic source-format, syntax or static check and exits nonzero if either fails. Document Python/tool requirements; use only standard-library checks or include reproducible dependency pins. Provide a reviewable CI workflow that invokes the same checks on a fresh source checkout with read-only/minimal permissions and no injected real secrets. Deliberately introduce one assertion failure and one source/static-check violation, record separate red results of the local quality gate, correct both, and record the final green run. Explain how a hosted CI job would receive untrusted pull-request content safely and why no secret or write token should be available to the untrusted test process.
  - Criteria: Both seeded faults independently fail the local quality command with nonzero status and no skipped later checks; a clean revision completes all documented checks. The workflow and local command express equivalent tests and validation, with clear version/dependency and environment assumptions. No live token or production credential is necessary; read-only workflow permissions and safe event/trust boundaries are documented. The learner does not claim hosted CI ran unless independently verifiable logs were actually produced.
  - Evidence: Quality script, workflow definition, clean-start instructions, tool versions or lockfile when applicable, two isolated failing revisions/logs, corrected green logs, static inspection of permissions and untrusted-code flow, and remaining CI limitations.

- **SEF5-AS6** (required maintainable CLI handoff and engineering defense)
  - Outcomes: SEF5-O1, SEF5-O3, SEF5-O4, SEF5-O5, SEF5-O6, SEF5-O7, SEF5-O8, SEF5-O9, SEF5-O10, SEF5-O11, SEF5-O12
  - Work: Produce a versioned, maintainable Python CLI application from the SEF2 task manager or comparable learner-authored command, with at least three public operations, explicit validation, predictable error and exit behavior, controlled JSON or equivalent persistence, clear component boundaries, and safe diagnostic logging. Reuse verified Git, defect-repair, refactoring, test and quality-gate work from SEF5-AS1–AS5. Provide a test suite spanning unit behavior and subprocess-based CLI interactions with normal, boundary, invalid and simulated storage-failure cases; include the equivalent quality/CI configuration. Ask an independent reviewer to follow the README in a fresh disposable checkout or portable project extraction, run tests, exercise the CLI, inspect one review finding and record corrections and limitations. Demonstrate an unfamiliar error case and defend a specific engineering trade-off.
  - Criteria: Documented commands and storage work consistently across separate processes; expected errors are distinguishable from successful no-ops, invalid data does not silently destroy valid state, and test coverage catches at least one deliberately demonstrated defect. The fresh reviewer setup reproduces the relevant results without hidden services, private data, network, or paid dependencies. Changes have focused history, valid documented interfaces, appropriate logging, reproducible quality checks and an inspectable review-and-response record. The technical defense ties actual behaviors, design boundaries, remaining risks and CI security assumptions to evidence rather than claiming that a green suite proves release quality.
  - Evidence: Versioned repository or portable source, clean-start README, fixture and error contract, unit/integration/subprocess outputs, documented test/quality run results, representative Git change history, red/green defect example, code review and response record, independent reproduction notes, and a concise written, recorded or otherwise accessible defense.

### Completion decision

All **six required assessments** must satisfy their published criteria and collectively demonstrate SEF5-O1 through SEF5-O12. Earlier assessed branches, tests, refactors, diagnostics, workflow configuration and documentation may be reused in the integrated handoff; no duplicate final project or extra quiz/lab quota is imposed. Guided learning activities and optional tests are formative, not hidden completion conditions.

An independent reviewer must record the course assessment decisions and sufficient reproducible evidence for each outcome. Substantial correctness, security, trust-boundary, and reproducibility failures must be corrected before a passing decision; an unsupported CI badge, unverifiable review claim, or unexplained mock pass cannot substitute for demonstrated behavior. The course itself remains `draft`; passing structural validation does not establish `tested` or `verified` course readiness under [Status Labels](../../spec/status-labels.md).
