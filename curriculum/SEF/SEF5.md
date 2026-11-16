# SEF5 — Software Engineering Practice

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF2](SEF2.md)
**Duration:** 10–12 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; calibrate with learner evidence)

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

SEF2 provides the foundational Python vocabulary for this engineering-practice course: function and module boundaries, small user-defined classes, meaningful composition, basic type annotations and explicit runtime validation. SEF5 extends that prior knowledge into maintainable software design, collaborative review, testing and release discipline; it does not silently treat a type hint as proof of safety or require a third-party type checker.

Develop the engineering practices needed to improve software safely after it works for the first time. In addition to Git, testing, CI, and maintainable delivery, explicitly investigate design responsibilities, cohesion, coupling, information hiding, dependency direction, public interface contracts, and how real reviewers can inspect quality evidence in accessible formats. Start with the program and tests built in SEF2, or a comparable small learner-owned command-line application. Learn to isolate changes in Git, diagnose failures with evidence, design meaningful tests, refactor without breaking a public contract, review code, build repeatable quality checks, and hand off a maintainable application for independent reproduction.

The reference environment is Python 3.11 or later, the Python standard library, and a local Git installation. The course can be completed offline with disposable repositories, `unittest` or equivalent independently runnable tests, a local quality-gate script, and a reviewable version-controlled CI configuration. Optional `pytest`, hosted Git platforms, remote pull requests, formatting tools, or type checkers may be used when available but are **not** required for completion. Any additional development dependency used in submitted work must be recorded with a reproducible installation procedure; a standard-library-only route requires none.

A local branch, reviewable diff and written review can demonstrate the relevant collaboration outcomes without contacting an external service. For CI, the required behavior is a reproducible quality-gate contract and a documented least-privilege workflow; learners may demonstrate failed and passing gates locally and have an independent reviewer inspect their CI configuration without publishing secrets or running an online pipeline. Actual hosted job logs are welcome as additional evidence, not a hidden gate.

The nine-module instructional sequence extends the earlier seven-module progression with distinct design-analysis and software-quality/review stages. Seven summative assessments evaluate connected skills; verified code, fixtures and review material may be reused rather than recreated for each module. A fixed quiz/lab pair, hosted CI service, or final lab beyond the published assessments is not required. All examples, test repositories, credentials, logs, and input records must be synthetic or owned by the learner. The course remains `draft`; the revised 10–12-week workload estimate is provisional and subject to learner validation. The design investigation extends the existing tested CLI and code-review evidence; no independent second project or paid design tool is required.

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
- **SEF5-O13:** Diagnose and improve a small application's cohesion, coupling, information hiding, component responsibilities and dependency direction, using an inspectable dependency map and behavior-preserving evidence rather than counting classes or pursuing abstraction for its own sake.
- **SEF5-O14:** Specify and verify module/API contracts for valid and invalid inputs, invariants, return and error semantics, side effects, compatibility and change impact; demonstrate a replaceable dependency boundary without letting test doubles conceal real end-to-end failures.
- **SEF5-O15:** Evaluate a software change's maintainability and professional quality with reproducible, appropriately bounded evidence, and prepare an accessible, actionable review that communicates design alternatives, quality risks, verification and unresolved limitations to an independent reviewer.

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
9. Tests at component boundaries — Distinguish a test double used to isolate a dependency from a subprocess test that actually exercises the production wiring; explain how an unrealistic mock may let a defect escape.

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
10. Cohesion, coupling and information hiding — Identify modules with mixed unrelated responsibilities, leaked storage details, hidden global state and circular imports.
11. Interfaces and compatibility — Compare a public return/error/side-effect contract with a private implementation detail and a type annotation, which alone cannot validate runtime inputs.

*Optional practice:* Inspect a small change for coupling, logging, interface drift, and unnecessary churn; write a review comment describing an actionable correction.

### Module 4 — Design Boundaries, Dependencies and Contracts

#### Outcomes

- SEF5-O5
- SEF5-O10
- SEF5-O13
- SEF5-O14

#### Lessons

1. **Responsibilities before files and classes** — Identify the distinct reasons the task-manager command parser, domain rules and JSON persistence may need to change; distinguish a meaningful component from a folder containing arbitrary code.
2. **Cohesion and coupling** — Trace a change's blast radius, internal responsibilities, shared mutable state and imports; explain high cohesion/low coupling as useful design tendencies, not numerical guarantees.
3. **Information hiding and encapsulation** — Keep storage representation and CLI parsing private to their owners; explain which domain operations are intentionally public and why language visibility conventions are not security enforcement.
4. **Dependency direction** — Draw an inspectable text/table/diagram map of actual imports and calls; distinguish a domain module that imports `argparse` or `json` from a command/persistence adapter that depends on domain rules, and detect cycles.
5. **Function-first and object-first alternatives** — Compare a small functional module with composed objects from SEF2; avoid mechanical inheritance trees and overgeneralized factories when simple functions serve the contract.
6. **Contracts and invariants** — State parameter/return types, preconditions, postconditions, valid state transitions, externally visible errors, side effects and mutation ownership; runtime validation must be shown rather than inferred from annotations.
7. **Dependency substitution and test seams** — Pass an explicit storage boundary or callable to domain logic, exercise a simple in-memory test double, then check the real file adapter end-to-end to avoid a misleading isolated pass.
8. **API and data compatibility** — Preserve a documented command/exit-code/data-format contract; explain when a breaking API or serialized-schema change needs a new version or an explicit migration policy.
9. **Characterization before change** — Capture representative normal, boundary, malformed and persistence-failure behavior before altering internals; keep defect fixes separate from unrelated refactors.
10. **A bounded change-impact exercise** — Given a new read-only query or adjusted validation rule, predict affected components, implement one focused change and verify the actual blast radius against the original map.

*Optional practice:* On the existing task manager, compare domain code that reads JSON directly with a variant accepting a narrow storage interface. Trace one malformed input across each boundary and state which explanation is supported by actual tests, not only a class diagram.

### Module 5 — Testing Strategy & Reliability

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

### Module 6 — Continuous Integration & Build Reproducibility

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

### Module 7 — Code Maintenance, Documentation & Handoff

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

### Module 8 — Software Quality, Change Evidence and Accessible Review

#### Outcomes

- SEF5-O6
- SEF5-O10
- SEF5-O12
- SEF5-O13
- SEF5-O14
- SEF5-O15

#### Lessons

1. **Quality is multidimensional** — Distinguish functional correctness from maintainability, readability, security, reliability, portability and usable documentation; identify which risks matter for this bounded CLI.
2. **Evidence versus metrics theater** — Interpret dependency counts, changed files, test results and simple complexity indicators as contextual signals; reject claims that any single metric or green check proves quality.
3. **Maintainability in an actual change** — Compare a before/after responsibility map and change diff; document one reduction in unnecessary propagation or one justified trade-off without requiring that every number improve.
4. **Review a design decision** — Compare at least two credible choices (for example, direct JSON access versus a narrow persistence boundary), evaluate simplicity, change cost and failure risk, and document why a choice fits present scope.
5. **Review severity and actionable comments** — Identify correctness, contract, security and maintainability risks; give file/function context, observable evidence, impact and an attainable suggested resolution rather than merely saying code is bad.
6. **Accessible written review** — Prepare navigable plain-text or semantic Markdown notes using descriptive headings, named source locations and file paths, explicit expected/observed behavior and meaningful descriptions for optional diagrams or screenshots; do not convey an essential requirement only by color or image.
7. **Collaborative review and independent reproduction** — Ask a real reviewer to follow a clean-start walkthrough or independently inspect a supplied accessible source/diff; retain independent reproduction notes, reviewer questions, resolution, differing interpretations and any limits. Simulated platform PRs must be labeled simulated.
8. **Compatibility, regression and rollback reasoning** — Explain impact on CLI errors, exit statuses, storage, consumers and release notes; use focused commits, contract tests and a credible reversible change plan.
9. **Communicating uncertainty** — State exactly what tests, code inspection and reviewer exercises established, and what they did not; retain an honest limitation list without inventing user study data or code-review approval.

*Optional practice:* Produce a short screen-reader-navigable Markdown review of a tiny storage-interface change, with a dependency table, one reproducible risk, one suggested alternative and evidence from real CLI tests. A diagram, hosted review platform or accessibility audit service is not required.

### Module 9 — Tested CLI Application

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
- SEF5-O13
- SEF5-O14
- SEF5-O15

#### Lessons

1. CLI behavior and versioned project contract
2. Unit, integration and subprocess-based tests
3. Logging, configuration and safe persistence
4. Reproducible local quality checks and CI workflow
5. Reviewable changes and clean-start handoff
6. Responsibility and dependency audit of the finished application
7. Public module contracts and production-adapter validation
8. Accessible design review and evidence-based trade-off defense

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

- **SEF5-AS7** (required maintainable design, interface contracts and accessible quality review)
  - Outcomes: SEF5-O3, SEF5-O5, SEF5-O6, SEF5-O10, SEF5-O11, SEF5-O12, SEF5-O13, SEF5-O14, SEF5-O15
  - Work: Extend and audit the **same** tested SEF5-AS6 CLI application; do not build a second independent project. Record its initial command, domain and persistence components in a human-readable responsibility/dependency table (or accessible textual equivalent of a diagram), identifying one actual cohesion/coupling problem, a dependency-direction issue or a domain/storage implementation leak. Provide two realistic design options, including the option to retain the simpler current design, and justify the chosen proportionate improvement. Define one explicit module contract with accepted/invalid inputs, return behavior, exceptions or error values, observable side effects, storage invariants and compatibility expectations. Implement one focused change on a reviewable branch or diff, using a narrow dependency seam where warranted; demonstrate it with both a constrained unit-level test double and real subprocess/persistence integration tests, including a seeded contract violation that the meaningful tests catch. Under an unfamiliar reviewer-supplied small change request, predict which components and tests would change, make or explain a bounded revision, and compare observed with predicted impact. Evaluate maintainability and one other applicable quality risk (such as error clarity, reliability or portability) through explicit before/after evidence rather than a score or unsupported universal metric. Present a concise, accessible Markdown or plain-text design review with descriptive headings, source locations, expected and observed behaviors, risk severity, alternatives, review findings/responses and limitations; ensure essential information does not depend on diagrams, color or screenshots. Reuse the independent handoff reviewer from SEF5-AS6 where appropriate, without claiming a simulated review is a live one.
  - Criteria: The responsibility and dependency map matches actual production imports/calls and identifies a concrete change pressure; the learner correctly distinguishes cohesion, coupling, information hiding and dependency direction without making an unjustified architectural abstraction. The proposed boundary has a real behavioral purpose and is tested through valid/invalid state transitions, error/side-effect contracts and actual CLI/storage wiring; no fake-only pass is accepted as proof of end-to-end correctness. Previously documented CLI outputs, exit statuses and persisted-data format remain consistent except for clearly declared, separately verified intentional changes. The chosen design is supported by an explicit comparison with at least one viable alternative and a bounded actual change-impact result; quality evidence documents trade-offs and limitations, not claims that a single metric guarantees maintainability. The review is readable and navigable as text, supplies actionable evidence-linked findings, records the reviewer response, and enables an independent reviewer to reproduce or challenge the outcome with no paid account, visual-only evidence or proprietary grader. A failing contract, safety or compatibility case must be resolved before a passing decision.
  - Evidence: Same versioned CLI source and reproducible fixture set used in earlier SEF5 work, baseline and revised responsibility/dependency maps, written public interface contract, alternative-design comparison with consequences, focused diff and associated Git history, direct contract tests and subprocess/persistence regression results, a pre-fix failing/repaired behavior record, original-versus-observed change-impact table, bounded maintainability and quality-risk analysis, accessible structured review and independent reviewer response, plus an honest technical defense and remaining limitation list.

### Completion decision

All **seven required assessments** must satisfy their published criteria and collectively demonstrate SEF5-O1 through SEF5-O15. Earlier assessed branches, tests, refactors, diagnostics, workflow configuration and documentation may be reused in the integrated handoff; no duplicate final project or extra quiz/lab quota is imposed. Guided learning activities and optional tests are formative, not hidden completion conditions.

An independent reviewer must record the course assessment decisions and sufficient reproducible evidence for each outcome. Substantial correctness, security, trust-boundary, and reproducibility failures must be corrected before a passing decision; an unsupported CI badge, unverifiable review claim, or unexplained mock pass cannot substitute for demonstrated behavior. The course itself remains `draft`; passing structural validation does not establish `tested` or `verified` course readiness under [Status Labels](../../spec/status-labels.md).

### Revision history and evidence compatibility

This focused academic revision implements the SEF5 requirements in [accepted RFC 0003](../../rfcs/0003-sef-academic-progression.md). The [historical SEF5 course at OEE commit `168b30cc304b0d57f019b2b289d2b11b647708e4`](https://github.com/0xbuffdev/open-engineering-education/blob/168b30cc304b0d57f019b2b289d2b11b647708e4/curriculum/SEF/SEF5.md) anchors interpretation of previously assessed work.

| Historical evidence contract | Current contract | Review consequence |
| --- | --- | --- |
| `SEF5-O1`–`O12` | Identical stable IDs and outcome descriptions | No earlier outcome is silently broadened or renumbered |
| `SEF5-AS1`–`AS6` | Unchanged Work, Criteria, Evidence and review variations | Prior learner evidence stays attributable to the revision actually assessed |
| Design terms embedded in existing lessons, but no independent design-quality outcome | New `SEF5-O13`, evaluated by `SEF5-AS7` | Requires genuine responsibility/dependency and change-impact evidence |
| Interfaces and runtime safety discussed inside existing refactoring | New `SEF5-O14`, evaluated by `SEF5-AS7` | Requires explicit API/error/side-effect contract and real-adapter verification |
| Code review and documentation taught, but no separate accessible evidence-based quality outcome | New `SEF5-O15`, evaluated by `SEF5-AS7` | Requires an accessible, actionable review and proportionate quality assessment |

Two new modules and expanded formative lessons introduce these capabilities in a deliberate order. The learner **reuses the existing application**, its tests and independent reviewer where appropriate; the seventh assessment requires new demonstrable evidence, not a duplicate capstone. The provisional duration changes from 8 to 10–12 weeks pending learner calibration. Historical completions are not automatically revoked or converted to fulfillment of `O13`–`O15`; prior artifacts may be recognized only against actual reviewable evidence. No global OEE course-format rule, fixed activity quota, paid service, professional software license, or status promotion is introduced.

For optional open reference reading, see the [ACM software-engineering knowledge-area guidance](https://csed.acm.org/wp-content/uploads/2023/09/SE-Version-Gamma.pdf) on coupling/cohesion and interface contracts, and [Google's public engineering review guide](https://google.github.io/eng-practices/review/reviewer/looking-for.html) for design, functionality, maintainability and constructive feedback. These resources supplement but do not replace the assessment requirements defined here.
