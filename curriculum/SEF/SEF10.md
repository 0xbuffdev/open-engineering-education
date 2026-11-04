> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

# SEF10 — Software Engineering Foundations Capstone

**Program:** SEF — Software Engineering Foundations
**Type:** `project`
**Prerequisites:** SEF1–SEF9
**Duration:** 6–8 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

## Overview

The capstone is the final project course in Software Engineering Foundations. The learner builds one integrated developer utility from an open-ended brief: a command-line tool that solves a real problem and combines the programming, data structures, algorithms, engineering practice, systems, and mathematics from the foundation courses. The learner takes it from requirements through design, implementation, testing, packaging, measurement, and a live defense. The project must demonstrate independent problem-solving and engineering judgment rather than tutorial completion.

## Course brief

The course introduction is the first lesson of the first module. It combines the overview above with these fields.

- **Introduction:** The capstone shows that the learner can carry a project from an open-ended brief to a delivered, measured, documented tool and defend it.
- **Usage:** The learner defines the problem, designs and builds a command-line developer utility, tests and measures it, packages it, and defends it live.
- **Applications:** The same cycle underlies every professional project.
- **Strengths:** A whole-project view shows how the separate skills combine and where each one is needed.
- **Limitations:** A single project cannot cover every kind of engineering, so the specialist programs that follow add depth in a chosen direction.
- **Key concepts:** requirements; architecture; implementation; testing; measurement; documentation; release; defense

## Prerequisites

- **SEF1–SEF9 — Software Engineering Foundations**

SEF8 may be completed alongside SEF4–SEF7, but all SEF1–SEF9 competencies must be demonstrated before the capstone is completed.

## Learning outcomes

By the end of the project, the learner will be able to:

- Turn an open-ended problem into scoped requirements, acceptance criteria, and a design.
- Build a working command-line developer utility that integrates the programming, data structures, systems, and mathematical skills from the foundation courses.
- Apply version control, automated testing, debugging, and refactoring throughout the build.
- Use appropriate data structures and algorithms and explain their time and space cost.
- Package and document the tool so another person can install, run, and extend it.
- Measure one meaningful property of the tool and use the evidence to improve it.
- Defend the implementation and explain the major design and trade-off decisions.

## Modules

### Module 1 — Problem Definition & Scope

#### Module brief

- **Introduction:** A good project begins with a clear problem. This module teaches how to define one.
- **Overview:** It covers the project brief, users, requirements, constraints, success criteria, and a one-page problem statement.
- **Key concepts:** user; requirement; constraint; success criterion; scope

#### Module outcomes

By the end of this module, the learner can:

- Turn a vague idea into a scoped problem with users, requirements, constraints, and success criteria.

1. **Course introduction: Software Engineering Foundations Capstone** — what the subject is, where it came from, where it is used, and its strengths and limits
2. **Introduction: Problem Definition & Scope** — what the topic is, where it is used, and its strengths and limits
3. **Project brief**
4. **Users**
5. **Requirements**
6. **Constraints**
7. **Success criteria**
8. **Scope and requirements**
   - kind: `test`
9. **Problem statement**
   - kind: `lab`

### Module 2 — Architecture & Design

#### Module brief

- **Introduction:** Structure decides how easily a program can change. This module covers how to decompose a project and design its interfaces.
- **Overview:** It covers decomposition, data structures, interfaces, architecture diagrams, project structure, and design review.
- **History:** David Parnas argued in 1972 that modules should be chosen to hide design decisions that are likely to change, an idea that still underlies interface design.
- **Limitations:** Designs made before building are guesses, and over-designing wastes effort.
- **Key concepts:** decomposition; interface; information hiding; architecture diagram; design review

#### Module outcomes

By the end of this module, the learner can:

- Decompose a project into components with clear interfaces and a sensible structure.
- Review a design against its requirements.

1. **Introduction: Architecture & Design** — what the topic is, where it is used, and its strengths and limits
2. **Decomposition**
3. **Data structures**
4. **Interfaces**
5. **Architecture diagrams**
6. **Project structure**
7. **Design review**
   - kind: `test`
8. **Component sketch**
   - kind: `lab`

### Module 3 — Implementation & Testing

#### Module brief

- **Introduction:** Building in small verified steps keeps a project from collapsing under its own mistakes. This module covers incremental implementation with tests.
- **Overview:** It covers incremental implementation, testing as you build, debugging, and a version-control workflow.
- **Limitations:** Incremental work can drift from the design, so each step needs checking against the plan.
- **Key concepts:** increment; automated test; debugging; branch and merge workflow; review

#### Module outcomes

By the end of this module, the learner can:

- Build the project incrementally, with tests and version control, and debug it from evidence.

1. **Introduction: Implementation & Testing** — what the topic is, where it is used, and its strengths and limits
2. **Incremental implementation**
3. **Testing during the build**
4. **Debugging**
5. **Version control workflow**
6. **Implementation review**
   - kind: `test`
7. **First failing test**
   - kind: `lab`

### Module 4 — Measurement, Documentation & Release

#### Module brief

- **Introduction:** Software is finished only when others can install and run it, and its behavior has been measured. This module covers measurement, documentation, and release.
- **Overview:** It covers benchmarking, profiling, technical documentation, reproducible setup, and release preparation.
- **History:** Donald Knuth's 1974 paper on structured programming contains the often-quoted warning against premature optimization, which is why measurement comes first.
- **Limitations:** Benchmarks vary between machines and runs, and documentation goes stale if it is not maintained.
- **Key concepts:** benchmark; profiler; documentation; reproducibility; release

#### Module outcomes

By the end of this module, the learner can:

- Measure performance, document the project, and make it reproducible.
- Review a project's readiness for release.

1. **Introduction: Measurement, Documentation & Release** — what the topic is, where it is used, and its strengths and limits
2. **Benchmarking**
3. **Profiling**
4. **Technical documentation**
5. **Reproducibility**
6. **Release preparation**
7. **Readiness review**
   - kind: `test`
8. **Baseline measurement**
   - kind: `lab`

### Module 5 — Final Project Lab

#### Module brief

- **Introduction:** This lab integrates the entire program. The learner delivers a complete developer utility and defends it live.
- **Overview:** It combines requirements, design, implementation, tests, measurement, documentation, release, and a defense.
- **Applications:** Every professional engineering role requires delivering and explaining work in this way.
- **Key concepts integrated:** requirements; architecture; testing; measurement; documentation; release; defense

1. **Developer utility**
   - kind: `lab`

## Required qualities

The project must include:

- Clear requirements
- Modular architecture
- Git history
- Automated tests
- Input validation
- Error handling
- Documentation
- Reproducible setup
- CI
- Basic performance measurements
- Release/package instructions
- Architecture diagram
- Decision records
- Technical retrospective

## Project defense

The learner demonstrates the application live and explains:

- Architecture
- Data structures
- Important design decisions
- Failures encountered
- Testing strategy
- One measured improvement

This is the **Program 1 graduation requirement**.
