# Program 1 — SEF: Software Engineering Foundations

> [OEE curriculum](../README.md) · [Specification](../../spec/README.md) · [OEE Workspace](https://github.com/0xbuffdev/oee-workspace)

## Overview

Software Engineering Foundations is the entry program for people without programming experience. It begins with a small model of bits, logic, memory and instruction execution. Learners then write Python programs, study the mathematics needed to reason about them, work in a Linux shell and build software with tests and version control.

Later courses introduce algorithms, numerical mathematics, C memory management, Unix system interfaces and professional engineering practice. One cumulative developer utility brings relevant skills together at graduation. The program prepares learners for the published entry requirements of Application, Systems, AI and Security Engineering. Each of those programs defines its own specialist work.

## Prerequisites

No previous programming or formal mathematics course is required. Basic computer use is helpful.

[SEF11](SEF11.md) offers an ungraded arithmetic and algebra diagnostic. Learners use it to select bridge practice before studying proofs and recurrences. It does not exclude learners or confer course credit. Required SEF11 assessments determine mathematical readiness for dependent courses.

## Learning outcomes

Learners who have satisfied the published course assessments can:

- Explain how bit representations, logic gates, memory and instruction execution produce observable behavior, including the limits of a simplified teaching computer.
- Write and debug Python programs with functions, collections, classes, type annotations, runtime validation, persistent files and predictable command-line behavior.
- Solve discrete mathematical problems using algebra, logic, relations, counting, proof, recurrences and graphs, then apply that reasoning to unfamiliar computing questions.
- Implement and evaluate data structures and algorithms with correctness and termination arguments, qualified time/space costs and independently determined test expectations.
- Work with Git, modular interfaces, maintainable designs, automated tests, failure diagnosis and reproducible checks. Review and document engineering changes for other people.
- Apply C11 representation, conversion and object-lifetime rules, including pointer boundaries, allocation failures, undefined behavior, bounded parsing and owned data structures.
- Use the Linux shell and foundational Unix interfaces for controlled files, processes, descriptors, signals, directories, pipes and loopback networking, while respecting Bash, C11, POSIX and Linux-specific boundaries.
- Use functions, vectors, matrices, probability, statistics, calculus and elementary numerical optimization to investigate programs with justified assumptions and uncertainty.
- Deliver and defend a useful software project with traceable evidence, ethical and licensing decisions, privacy and accessibility safeguards, accurate AI-use disclosure where relevant, independent review and an unassisted technical challenge.

## Program completion standard

**All eleven courses are required.** Each course has its own published outcomes and summative assessments. Attendance, lesson checkmarks and optional practice alone do not establish completion.

Before entering [SEF10](SEF10.md), an assessor verifies genuine assessed completion decisions for SEF1–SEF9 and SEF11. Records must identify the applicable course revision and supporting evidence. A governed equivalence can be used only when it assesses the relevant outcomes and records an actual approval. Missing or uncertain prior work goes back to its originating course for assessment or reassessment.

The capstone develops **one learner-owned command-line developer utility** through six milestones, M1–M6. Its [graduation-evidence requirements](SEF10.md#prerequisite-closure-is-different-from-capstone-integration) distinguish previously verified competence from skills applied in the utility and relevant conceptual explanations. Learners do not need to recreate hardware, calculus exercises, C programs or POSIX services merely to demonstrate each previous course again.

SEF10 also requires independent reproduction, meaningful measurement, a responsible release or hold decision and a bounded change or debugging task completed without an assistant. Clearly labeled self-review is permitted under the published defense rules; it cannot be presented as independent third-party endorsement. The [course definitions](README.md#courses) provide the evaluation criteria. Historical learner decisions retain the course revisions under which they were evaluated.

---

## Courses

This table is the **authoritative prerequisite-valid study order**, not numerical course-ID order. Stable identifiers are retained for historical compatibility; SEF11 is introduced between foundational programming and proof-intensive algorithms without renumbering SEF4–SEF10.

| Course | Title | Duration | Prerequisite | Kind |
| --- | --- | --- | --- | --- |
| [SEF1](SEF1.md) | Demystifying the Computer System | 5 weeks | — | `course` |
| [SEF2](SEF2.md) | Programming & Computational Thinking | 10–12 weeks | SEF1 | `course` |
| [SEF11](SEF11.md) | Discrete Mathematics for Computing | 10–14 weeks | SEF2 | `course` |
| [SEF3](SEF3.md) | Linux & the Command Line | 10–12 weeks | SEF2 | `course` |
| [SEF4](SEF4.md) | Data Structures & Algorithms | 12–14 weeks | SEF11 | `course` |
| [SEF5](SEF5.md) | Software Engineering Practice | 10–12 weeks | SEF2 | `course` |
| [SEF8](SEF8.md) | Mathematics for Numerical Computing & AI | 12–14 weeks | SEF11 | `course` |
| [SEF6](SEF6.md) | C Programming & Machine Memory | 14–18 weeks | SEF3, SEF4, SEF5 | `course` |
| [SEF7](SEF7.md) | Unix System Interfaces | 12–16 weeks | SEF3, SEF6 | `course` |
| [SEF9](SEF9.md) | Professional Workflow & AI-Assisted Engineering | 10–12 weeks | SEF5 | `course` |
| [SEF10](SEF10.md) | Software Engineering Foundations Capstone | 10–14 weeks | SEF1–SEF9, SEF11 | `project` |

```text
SEF1 → SEF2
SEF2 → SEF3, SEF5, SEF11
SEF11 → SEF4, SEF8
SEF3 + SEF4 + SEF5 → SEF6
SEF3 + SEF6 → SEF7
SEF5 → SEF9
SEF1–SEF9 + SEF11 → SEF10
```

## How the courses fit together

The catalog gives one prerequisite-valid order. Different branches may proceed concurrently when their listed prerequisites are met.

- **Initial foundations:** SEF1 explains the bit-to-program machine model. SEF2 introduces Python, state, files and programming abstractions. SEF11 adds an ungraded arithmetic/algebra diagnostic and the mathematics needed for independent proof and counting.
- **Branches after SEF2:** SEF3 develops Linux and shell skills, SEF5 covers Git, software design, verification and review, and SEF11 develops discrete mathematics. Following SEF11, **SEF4 and SEF8 may proceed concurrently**. Algorithms in SEF4 use SEF11; they do not secretly require SEF8 probability or calculus.
- **C and Unix systems:** SEF6 follows SEF3, SEF4 and SEF5, applying prior programming and algorithm reasoning to C11 memory and failure-safe resource contracts. SEF7 follows SEF3 and SEF6, adding POSIX files, processes, pipes, directories and bounded local-loopback networking. The [SEF7–SYS competency destination map](UNIX-SYS-BOUNDARY.md) describes deeper Rust and systems topics without transferring SEF7 assessment credit.
- **Professional work:** SEF9 follows SEF5. Learners manage requirements and decisions, review changes, verify proposed AI code, address ethics, rights and privacy, and communicate accessibly. Its [synthetic practice case](../../examples/sef9/README.md) can be completed without a paid assistant, private customer records or a hosted tracker.
- **Graduation:** SEF10 starts after verified completion of the other ten courses. The learner implements one bounded project and explains relevant transfer from previous study; no second specialist application is required.

## Workload and pacing

The listed durations are provisional estimates, generally based on 10–15 focused hours a week. Added together, the courses total **115–143 course-weeks**, approximately **1,150–2,145 focused hours** at those weekly workloads. These sums are **not an elapsed-time requirement**, a guaranteed graduation date or a fixed passing threshold. Parallel courses can shorten calendar time, while preparation, debugging, accessibility needs and review may increase individual study time.

The current courses publish **147 learning outcomes and 68 required summative assessments**. These are source counts, not design targets or a requirement to submit 68 separate applications. A previously evaluated artifact may be reused where it genuinely demonstrates later published criteria. Actual assessed competence determines progress; planning estimates require calibration with real learner experience.

## Course format and readiness

All eleven SEF course files use the outcome-driven OEE `v0.2.0` format and remain `draft`; no historical-format SEF course definitions remain. [RFC 0003](../../rfcs/0003-sef-academic-progression.md) records the adopted placement of SEF11 before algorithms and the ten-prerequisite capstone.

A `draft` status describes educational readiness, not an incomplete course file or a learner grade. Moving to `tested` or `verified` requires actual learner completions, revisions and independent review evidence under [Status Labels](../../spec/status-labels.md). Formal program conformance is a separate decision under [Conformance](../../spec/conformance.md). Passing source checks or completing an editorial assessment cannot establish learner-tested effectiveness. The [curriculum inventory](../INVENTORY.md) supplies reproducible source-format observations.

## Independent study

All mandatory outcomes, work, evidence and assessment criteria are publicly accessible. Use [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) or another learner-controlled environment to retain evidence. A paid learning platform, specific book, proprietary grader or mandatory external account cannot be a prerequisite for course completion.

The binding educational contract is in [Course Format](../../spec/course-format.md) and [Evidence Rules](../../spec/evidence-rules.md). For non-normative authoring guidance see the [Curriculum Design Guide](../DESIGN-GUIDE.md).
