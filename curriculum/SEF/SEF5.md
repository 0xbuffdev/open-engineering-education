> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

# SEF5 — Software Engineering Practice

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** SEF2
**Duration:** 5 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

## Overview

This course teaches the practices professional engineers use to keep software working: Git, testing, debugging, refactoring, code organization, logging, and code review. Each practice is applied to software the learner has already built.

## Course brief

The course introduction is the first lesson of the first module. It combines the overview above with these fields.

- **Introduction:** Writing code is a small part of software engineering. This course teaches the practices that keep software working as it grows and as more people work on it.
- **History:** The term software engineering was popularized by a NATO conference in 1968, convened in response to what participants called the software crisis. Version control, automated testing, refactoring, and code review each developed over the following decades and are now standard practice.
- **Usage:** The learner applies each practice to software they have already written: committing and branching in Git, writing tests, debugging from evidence, refactoring, and reviewing changes.
- **Applications:** Every professional software team, open-source project, and long-lived codebase.
- **Strengths:** These practices make change safe and make failures visible early.
- **Limitations:** They cost time up front, and they work only when the whole team follows them consistently.
- **Key concepts:** repository; commit; branch; merge; test; assertion; debugging; refactoring; code smell; code review; continuous integration

## Prerequisites

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

#### Module brief

- **Introduction:** Software changes constantly and is built by many people. Version control records every change and lets people work in parallel.
- **Overview:** It covers repositories and commits, history and diffs, branches, merging, merge conflicts, and remotes and pull requests.
- **History:** SCCS in 1972 and RCS in 1982 tracked file versions, CVS and Subversion added shared repositories, Linus Torvalds created Git in 2005, and GitHub popularized pull requests from 2008.
- **Strengths:** Complete history, safe experimentation, and parallel work.
- **Limitations:** Merge conflicts need human judgment, large binary files are handled poorly, and rewriting shared history confuses teams.
- **Key concepts:** repository; commit; branch; merge; conflict; remote; pull request

#### Module outcomes

By the end of this module, the learner can:

- Record, inspect, and navigate project history with Git.
- Create, merge, and resolve conflicts between branches, and collaborate through a remote.

1. **Course introduction: Software Engineering Practice** — what the subject is, where it came from, where it is used, and its strengths and limits
2. **Introduction: Version Control & Collaboration** — what the topic is, where it is used, and its strengths and limits
3. **Repositories and commits**
4. **History and diffs**
5. **Branches**
6. **Merging**
7. **Merge conflicts**
8. **Remotes and pull requests**
9. **Git workflows**
   - kind: `test`
10. **Resolve a conflict**

- kind: `lab`

### Module 2 — Testing & Debugging

#### Module brief

- **Introduction:** Programs fail in ways their authors did not expect. Tests find failures early, and debugging finds their causes.
- **Overview:** It covers assertions, unit tests with pytest, choosing test cases, reproducing failures, and debugging by evidence.
- **History:** The xUnit family of testing frameworks descends from Kent Beck's SUnit for Smalltalk in the 1990s, and pytest is a widely used Python framework.
- **Strengths:** Tests are repeatable and document intended behavior.
- **Limitations:** Tests can show that bugs exist but never that none remain, and poorly designed tests are brittle or slow.
- **Key concepts:** assertion; unit test; test-case selection; reproduction; hypothesis; regression

#### Module outcomes

By the end of this module, the learner can:

- Write unit tests and choose test cases that expose failures.
- Diagnose a failing program from evidence rather than guesses.

1. **Introduction: Testing & Debugging** — what the topic is, where it is used, and its strengths and limits
2. **Assertions**
3. **Unit tests with pytest**
4. **Choosing test cases**
5. **Reproducing failures**
6. **Debugging by evidence**
7. **Testing and debugging**
   - kind: `test`
8. **Diagnose a broken program**
   - kind: `lab`

### Module 3 — Maintainable Software

#### Module brief

- **Introduction:** Most of a program's life is spent being changed. This module covers the practices that keep code easy to change.
- **Overview:** It covers code smells, refactoring, style guides, logging, code review, and reading unfamiliar code.
- **History:** Michael Fagan formalized code inspections at IBM in 1976, and Martin Fowler's 1999 book popularized refactoring.
- **Strengths:** Clean code is cheaper to change and easier for newcomers to understand.
- **Limitations:** Refactoring without tests is risky, and style rules become busywork when they are not tied to a purpose.
- **Key concepts:** code smell; refactoring; style guide; logging; code review

#### Module outcomes

By the end of this module, the learner can:

- Recognize code smells and improve code with behavior-preserving refactorings.
- Use logging, style guides, and code review to keep software maintainable, and read unfamiliar code.

1. **Introduction: Maintainable Software** — what the topic is, where it is used, and its strengths and limits
2. **Code smells**
3. **Refactoring**
4. **Style guides**
5. **Logging**
6. **Code review**
7. **Reading unfamiliar code**
8. **Maintainability**
   - kind: `test`
9. **Review a pull request**
   - kind: `lab`

### Module 4 — Tested CLI Application

#### Module brief

- **Introduction:** This lab integrates the course. The learner turns the SEF2 application into a maintainable, tested, reviewed project.
- **Overview:** It combines Git history, automated tests, logging, refactoring, continuous integration, and documentation in one repository.
- **Applications:** Every team that ships software maintains projects in this way.
- **Key concepts integrated:** version control; testing; debugging; refactoring; logging; continuous integration

1. **Tested CLI application**
   - kind: `lab`

## Topics

- Git
- Branches and merges
- Commit design
- Code organization
- Testing
- Assertions
- Debugging
- Logging
- Refactoring
- Command-line workflows
- Basic code review
- Reading unfamiliar code

## Practical exercises

2. Resolve a controlled merge conflict.
3. Debug a deliberately broken application.
4. Turn untested code into tested code.
5. Refactor duplicated code without changing behavior.
6. Review another learner's pull request.

## Course lab

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

## Exit check

The learner must diagnose a failing test or bug from evidence rather than by guesswork.
