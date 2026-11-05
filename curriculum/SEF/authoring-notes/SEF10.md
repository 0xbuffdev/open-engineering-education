# SEF10 — Lesson authoring notes

> Optional instructional context preserved from the original source. These are not required course metadata, assessments or module briefs.

## Course orientation

- **Introduction:** The capstone shows that the learner can carry a project from an open-ended brief to a delivered, measured, documented tool and defend it.
- **Usage:** The learner defines the problem, designs and builds a command-line developer utility, tests and measures it, packages it, and defends it live.
- **Applications:** The same cycle underlies every professional project.
- **Strengths:** A whole-project view shows how the separate skills combine and where each one is needed.
- **Limitations:** A single project cannot cover every kind of engineering, so the specialist programs that follow add depth in a chosen direction.
- **Key concepts:** requirements; architecture; implementation; testing; measurement; documentation; release; defense

## Module 1 — Problem Definition & Scope

- **Introduction:** A good project begins with a clear problem. This module teaches how to define one.
- **Overview:** It covers the project brief, users, requirements, constraints, success criteria, and a one-page problem statement.
- **Key concepts:** user; requirement; constraint; success criterion; scope

## Module 2 — Architecture & Design

- **Introduction:** Structure decides how easily a program can change. This module covers how to decompose a project and design its interfaces.
- **Overview:** It covers decomposition, data structures, interfaces, architecture diagrams, project structure, and design review.
- **History:** David Parnas argued in 1972 that modules should be chosen to hide design decisions that are likely to change, an idea that still underlies interface design.
- **Limitations:** Designs made before building are guesses, and over-designing wastes effort.
- **Key concepts:** decomposition; interface; information hiding; architecture diagram; design review

## Module 3 — Implementation & Testing

- **Introduction:** Building in small verified steps keeps a project from collapsing under its own mistakes. This module covers incremental implementation with tests.
- **Overview:** It covers incremental implementation, testing as you build, debugging, and a version-control workflow.
- **Limitations:** Incremental work can drift from the design, so each step needs checking against the plan.
- **Key concepts:** increment; automated test; debugging; branch and merge workflow; review

## Module 4 — Measurement, Documentation & Release

- **Introduction:** Software is finished only when others can install and run it, and its behavior has been measured. This module covers measurement, documentation, and release.
- **Overview:** It covers benchmarking, profiling, technical documentation, reproducible setup, and release preparation.
- **History:** Donald Knuth's 1974 paper on structured programming contains the often-quoted warning against premature optimization, which is why measurement comes first.
- **Limitations:** Benchmarks vary between machines and runs, and documentation goes stale if it is not maintained.
- **Key concepts:** benchmark; profiler; documentation; reproducibility; release

## Module 5 — Final Project Lab

- **Introduction:** This lab integrates the entire program. The learner delivers a complete developer utility and defends it live.
- **Overview:** It combines requirements, design, implementation, tests, measurement, documentation, release, and a defense.
- **Applications:** Every professional engineering role requires delivering and explaining work in this way.
- **Key concepts integrated:** requirements; architecture; testing; measurement; documentation; release; defense

1. **Developer utility**
   - kind: `lab`
