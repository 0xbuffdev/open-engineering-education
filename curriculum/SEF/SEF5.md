# SEF5 — Software Engineering Practice

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF2](SEF2.md)
**Duration:** 8 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

This course teaches the practices professional engineers use to keep software working: Git, testing, debugging, refactoring, code organization, logging, and code review. Each practice is applied to software the learner has already built.

- [**SEF2 — Programming & Computational Thinking**](SEF2.md)

[SEF3 — Linux & the Command Line](SEF3.md) and [SEF4 — Data Structures & Algorithms](SEF4.md) are complementary preparation but are not required for version control, testing, debugging, refactoring, or code review.

## Learning outcomes

By the end of the course, the learner will be able to:

- Use Git branches, commits, merges, and pull-request workflows.
- Design meaningful tests for software behavior.
- Debug failures using evidence rather than guesswork.
- Refactor code without changing its intended behavior.
- Organize a growing codebase into maintainable components.
- Review code and explain engineering improvements.
- Automate basic testing and quality checks with CI.
- Develop reproducible test and CI workflows, review code changes, diagnose failures, and refactor a documented software project without altering behavior.

## Modules

### Module 1 — Version Control & Collaboration

#### Outcomes

- Record, inspect, and navigate project history with Git.
- Create, merge, and resolve conflicts between branches, and collaborate through a remote.

- Recover a Git mistake without destroying unrelated work or rewriting shared history.

#### Lessons

1. **Course introduction: Software Engineering Practice** — `lesson`

   Writing code is a small part of software engineering. This course teaches the practices that keep software working as it grows and as more people work on it.
2. **Repositories and commits** — `lesson`
3. **History and diffs** — `lesson`
4. **Branches** — `lesson`
5. **Merging** — `lesson`
6. **Merge conflicts** — `lesson`
7. **Remotes and pull requests** — `lesson`
8. **Staged versus working-tree changes** — `lesson`
9. **Reverting published changes versus rewriting history** — `lesson`
10. **Generated files, ignore rules and secret hygiene** — `lesson`
11. **Git workflows** — `test`
12. **Resolve a conflict** — `lab`

### Module 2 — Testing & Debugging

#### Outcomes

- Write unit tests and choose test cases that expose failures.
- Diagnose a failing program from evidence rather than guesses.

- Seed failures to establish which test layer detects which risk.

#### Lessons

1. **Assertions** — `lesson`
2. **Unit tests with pytest** — `lesson`
3. **Choosing test cases** — `lesson`
4. **Reproducing failures** — `lesson`
5. **Debugging by evidence** — `lesson`
6. **Unit and integration testing responsibilities** — `lesson`
7. **Parameterized cases, fixtures and isolation** — `lesson`
8. **Regression cases for previously observed defects** — `lesson`
9. **Testing and debugging** — `test`
10. **Diagnose a broken program** — `lab`

### Module 3 — Maintainable Software

#### Outcomes

- Recognize code smells and improve code with behavior-preserving refactorings.
- Use logging, style guides, and code review to keep software maintainable, and read unfamiliar code.

- Show a tested, reversible refactor with clear module contracts.

#### Lessons

1. **Code smells** — `lesson`
2. **Refactoring** — `lesson`
3. **Style guides** — `lesson`
4. **Logging** — `lesson`
5. **Code review** — `lesson`
6. **Reading unfamiliar code** — `lesson`
7. **Module boundaries and dependency direction** — `lesson`
8. **Behavior-preserving refactoring strategies** — `lesson`
9. **User-facing documentation and review evidence** — `lesson`
10. **Maintainability** — `test`
11. **Review a pull request** — `lab`

### Module 4 — Testing Strategy & Reliability

#### Outcomes

- Design stable tests that expose meaningful behavioral defects.
- Demonstrate reasoning with both ordinary and deliberately failing inputs.

#### Lessons

1. **Equivalence classes and boundary values** — `lesson`
2. **State-based testing and invariants** — `lesson`
3. **Unit, integration and end-to-end test selection** — `lesson`
4. **Property-based testing principles** — `lesson`
5. **Flaky tests, time and randomness** — `lesson`
6. **Testing negative paths and side effects** — `lesson`
7. **Testing Strategy & Reliability reasoning and diagnosis** — `test`
8. **Repair a flaky CLI test suite** — `lab`

### Module 5 — Continuous Integration & Build Reproducibility

#### Outcomes

- Create quality gates that fail safely and reproduce locally.
- Demonstrate reasoning with both ordinary and deliberately failing inputs.

#### Lessons

1. **Dependency lockfiles and isolated environments** — `lesson`
2. **Formatter, linter and static type checks** — `lesson`
3. **CI workflows, stages and failure gates** — `lesson`
4. **Secrets, permissions and untrusted CI input** — `lesson`
5. **Clean-checkout builds and release artifacts** — `lesson`
6. **Continuous Integration & Build Reproducibility reasoning and diagnosis** — `test`
7. **Build a red-green CI workflow** — `lab`

### Module 6 — Code Maintenance, Documentation & Handoff

#### Outcomes

- Produce a small reviewable change another engineer can reproduce and maintain.
- Demonstrate reasoning with both ordinary and deliberately failing inputs.

#### Lessons

1. **Contracts, coupling and interface stability** — `lesson`
2. **Logging, error context and sensitive data** — `lesson`
3. **Small reversible changes and meaningful commit history** — `lesson`
4. **Peer review and actionable feedback** — `lesson`
5. **README setup and contributor guidance** — `lesson`
6. **Dependency upgrades and technical-debt decisions** — `lesson`
7. **Code Maintenance, Documentation & Handoff reasoning and diagnosis** — `test`
8. **Refactor a shared feature and prepare a review** — `lab`

### Module 7 — Tested CLI Application

#### Outcomes

- Complete and explain the **Tested CLI Application** integration lab, demonstrating the relevant course outcomes and retained evidence.

#### Lessons

1. **Tested CLI application** — `lab`

   **Final integration lab — required work**

   **Tested CLI Application**

   Convert the SEF2 application into a maintainable software project with:

   - Meaningful Git history
   - Automated tests
   - Linting/formatting
   - Structured logging
   - Error handling
   - Refactored modules
   - CI test execution
   - Documentation

## Completion requirements

- Complete the required course exercises, checkpoints and evaluated labs below.
- Complete the final integrated `lab` in the last module and meet its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

Complete these required exercises:

**Practical practice:**

- Resolve a controlled merge conflict.
- Debug a deliberately broken application.
- Turn untested code into tested code.
- Refactor duplicated code without changing behavior.
- Review another learner's pull request.

**Expanded assessment and lab criteria:**

- **Module 1 checkpoint:** Recover a Git mistake without destroying unrelated work or rewriting shared history.
- **Module 2 checkpoint:** Seed failures to establish which test layer detects which risk.
- **Module 3 checkpoint:** Show a tested, reversible refactor with clear module contracts.

- **Module 4 — Repair a flaky CLI test suite:**
  - Objective: Design stable tests that expose meaningful behavioral defects.
  - Prerequisites: Complete the teaching lessons and conceptual checkpoint.
  - Environment: Record the language/runtime and tool versions and provide self-contained safe input fixtures.
  - Work: Add cases for invalid inputs, a previously missed edge case and a nondeterministic fixture; prove the suite runs repeatedly.
  - Verification: Failure occurs before repair, all cases pass afterward and fixtures are deterministic.
  - Evidence: Test matrix, failing trace, corrected code and rerun logs.
  - Failure analysis: Explain at least one incorrect result, boundary condition or runtime failure and the correction.
- **Module 5 — Build a red-green CI workflow:**
  - Objective: Create quality gates that fail safely and reproduce locally.
  - Prerequisites: Complete the teaching lessons and conceptual checkpoint.
  - Environment: Record the language/runtime and tool versions and provide self-contained safe input fixtures.
  - Work: Add automated tests and static checks; inject a failing test and formatting defect to verify both block delivery.
  - Verification: CI fails for each injected defect and passes on a clean checkout with pinned tool versions.
  - Evidence: Workflow, lockfile, logs, clean build and review record.
  - Failure analysis: Explain at least one incorrect result, boundary condition or runtime failure and the correction.
- **Module 6 — Refactor a shared feature and prepare a review:**
  - Objective: Produce a small reviewable change another engineer can reproduce and maintain.
  - Prerequisites: Complete the teaching lessons and conceptual checkpoint.
  - Environment: Record the language/runtime and tool versions and provide self-contained safe input fixtures.
  - Work: Improve an unfamiliar feature, preserve observed behavior, add regression tests and document setup and trade-offs.
  - Verification: A reviewer can reproduce the feature, inspect failures and verify unchanged external behavior.
  - Evidence: Diff, test report, review notes and updated instructions.
  - Failure analysis: Explain at least one incorrect result, boundary condition or runtime failure and the correction.

**Final integration lab extension:**

- The final integrated lab must demonstrate the existing course outcomes and the additional outcomes in this expanded software engineering pathway.
- Provide explicit negative tests, clean-checkout reproduction, explanation of assumptions, and a technical retrospective.

**Exit demonstration:**

The learner must diagnose a failing test or bug from evidence rather than by guesswork.
