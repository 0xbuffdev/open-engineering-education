# SEF5 — Lesson authoring notes

> Optional instructional context preserved from the original source. These are not required course metadata, assessments or module briefs.

## Course orientation

- **Introduction:** Writing code is a small part of software engineering. This course teaches the practices that keep software working as it grows and as more people work on it.
- **History:** The term software engineering was popularized by a NATO conference in 1968, convened in response to what participants called the software crisis. Version control, automated testing, refactoring, and code review each developed over the following decades and are now standard practice.
- **Usage:** The learner applies each practice to software they have already written: committing and branching in Git, writing tests, debugging from evidence, refactoring, and reviewing changes.
- **Applications:** Every professional software team, open-source project, and long-lived codebase.
- **Strengths:** These practices make change safe and make failures visible early.
- **Limitations:** They cost time up front, and they work only when the whole team follows them consistently.
- **Key concepts:** repository; commit; branch; merge; test; assertion; debugging; refactoring; code smell; code review; continuous integration

## Module 1 — Version Control & Collaboration

- **Introduction:** Software changes constantly and is built by many people. Version control records every change and lets people work in parallel.
- **Overview:** It covers repositories and commits, history and diffs, branches, merging, merge conflicts, and remotes and pull requests.
- **History:** SCCS in 1972 and RCS in 1982 tracked file versions, CVS and Subversion added shared repositories, Linus Torvalds created Git in 2005, and GitHub popularized pull requests from 2008.
- **Strengths:** Complete history, safe experimentation, and parallel work.
- **Limitations:** Merge conflicts need human judgment, large binary files are handled poorly, and rewriting shared history confuses teams.
- **Key concepts:** repository; commit; branch; merge; conflict; remote; pull request

## Module 2 — Testing & Debugging

- **Introduction:** Programs fail in ways their authors did not expect. Tests find failures early, and debugging finds their causes.
- **Overview:** It covers assertions, unit tests with pytest, choosing test cases, reproducing failures, and debugging by evidence.
- **History:** The xUnit family of testing frameworks descends from Kent Beck's SUnit for Smalltalk in the 1990s, and pytest is a widely used Python framework.
- **Strengths:** Tests are repeatable and document intended behavior.
- **Limitations:** Tests can show that bugs exist but never that none remain, and poorly designed tests are brittle or slow.
- **Key concepts:** assertion; unit test; test-case selection; reproduction; hypothesis; regression

## Module 3 — Maintainable Software

- **Introduction:** Most of a program's life is spent being changed. This module covers the practices that keep code easy to change.
- **Overview:** It covers code smells, refactoring, style guides, logging, code review, and reading unfamiliar code.
- **History:** Michael Fagan formalized code inspections at IBM in 1976, and Martin Fowler's 1999 book popularized refactoring.
- **Strengths:** Clean code is cheaper to change and easier for newcomers to understand.
- **Limitations:** Refactoring without tests is risky, and style rules become busywork when they are not tied to a purpose.
- **Key concepts:** code smell; refactoring; style guide; logging; code review

## Module 4 — Tested CLI Application

- **Introduction:** This lab integrates the course. The learner turns the SEF2 application into a maintainable, tested, reviewed project.
- **Overview:** It combines Git history, automated tests, logging, refactoring, continuous integration, and documentation in one repository.
- **Applications:** Every team that ships software maintains projects in this way.
- **Key concepts integrated:** version control; testing; debugging; refactoring; logging; continuous integration

1. **Tested CLI application**
   - kind: `lab`

## Original topic inventory

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
