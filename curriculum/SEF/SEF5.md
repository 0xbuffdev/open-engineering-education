# SEF5 — Software Engineering Practice

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF2](SEF2.md)
**Duration:** 5 weeks
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

## Modules

### Module 1 — Version Control & Collaboration

#### Outcomes

- Record, inspect, and navigate project history with Git.
- Create, merge, and resolve conflicts between branches, and collaborate through a remote.

#### Lessons

1. **Course introduction: Software Engineering Practice** — `lesson`

   Writing code is a small part of software engineering. This course teaches the practices that keep software working as it grows and as more people work on it.
2. **Repositories and commits** — `lesson`
3. **History and diffs** — `lesson`
4. **Branches** — `lesson`
5. **Merging** — `lesson`
6. **Merge conflicts** — `lesson`
7. **Remotes and pull requests** — `lesson`
8. **Git workflows** — `test`
9. **Resolve a conflict** — `lab`

### Module 2 — Testing & Debugging

#### Outcomes

- Write unit tests and choose test cases that expose failures.
- Diagnose a failing program from evidence rather than guesses.

#### Lessons

1. **Assertions** — `lesson`
2. **Unit tests with pytest** — `lesson`
3. **Choosing test cases** — `lesson`
4. **Reproducing failures** — `lesson`
5. **Debugging by evidence** — `lesson`
6. **Testing and debugging** — `test`
7. **Diagnose a broken program** — `lab`

### Module 3 — Maintainable Software

#### Outcomes

- Recognize code smells and improve code with behavior-preserving refactorings.
- Use logging, style guides, and code review to keep software maintainable, and read unfamiliar code.

#### Lessons

1. **Code smells** — `lesson`
2. **Refactoring** — `lesson`
3. **Style guides** — `lesson`
4. **Logging** — `lesson`
5. **Code review** — `lesson`
6. **Reading unfamiliar code** — `lesson`
7. **Maintainability** — `test`
8. **Review a pull request** — `lab`

### Module 4 — Tested CLI Application

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

**Required exercises**

**Practical practice:**

- Resolve a controlled merge conflict.
- Debug a deliberately broken application.
- Turn untested code into tested code.
- Refactor duplicated code without changing behavior.
- Review another learner's pull request.

**Exit demonstration:**

The learner must diagnose a failing test or bug from evidence rather than by guesswork.
