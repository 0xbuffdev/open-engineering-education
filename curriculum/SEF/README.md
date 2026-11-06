# Program 1 — SEF: Software Engineering Foundations

> [OEE curriculum](../README.md) · [Specification](../../spec/README.md) · [OEE Workspace](https://github.com/0xbuffdev/oee-workspace)

## Overview

Software Engineering Foundations is the common entry program for learners with no programming experience. It begins with how a computer works, from bits and logic gates to memory, processors, operating systems, and booting. It then introduces software and software engineering, sets up a terminal, an editor, and Python, and teaches programming in Python, data structures and algorithms, Git and testing, C and Linux, and the mathematics that later courses build on. Learners build, debug, and explain their work, and finish with a complete project that prepares them for Application, Systems, AI, or Security Engineering.

## Prerequisites

**None.**

No prior programming experience is required. Basic computer skills (typing, managing files, and browsing the web) are helpful.

## Learning outcomes

By the end of this program, the learner will be able to:

- Explain what software and software engineering are, and set up and use a terminal, a code editor, and Python.
- Write, structure, test, and debug programs independently.
- Choose and implement appropriate data structures and algorithms and explain their time and space complexity.
- Use Git, testing, debugging, refactoring, and code review to build and maintain software.
- Explain how bits, logic gates, memory, processors, storage, and operating systems fit together.
- Use the Linux terminal and work with processes, files, memory, and basic networking.
- Read and reason about basic C programs, pointers, memory, compilation, and operating-system interaction.
- Apply foundational mathematics such as logic, vectors, matrices, probability, derivatives, and Big-O reasoning to computing problems.
- Design, build, test, document, and explain a complete software project.

## Program completion standard

The learner must be able to take an unfamiliar programming problem, design a solution, implement it, test it, debug it, explain its complexity and major trade-offs, and ship the result as a documented project.

---

## Courses

| Course            | Title                                           | Duration   | Prerequisite              | Kind      |
| ----------------- | ----------------------------------------------- | ---------- | ------------------------- | --------- |
| [SEF1](SEF1.md)   | Demystifying the Computer System                | 5 weeks    | —                         | `course`  |
| [SEF2](SEF2.md)   | Programming & Computational Thinking            | 8 weeks    | SEF1                      | `course`  |
| [SEF3](SEF3.md)   | Linux & the Command Line                        | 8 weeks    | SEF2                      | `course`  |
| [SEF4](SEF4.md)   | Data Structures & Algorithms                    | 10 weeks   | SEF2                      | `course`  |
| [SEF5](SEF5.md)   | Software Engineering Practice                   | 8 weeks    | SEF2                      | `course`  |
| [SEF6](SEF6.md)   | C Programming & Machine Memory                  | 8 weeks    | SEF3, SEF4, SEF5          | `course`  |
| [SEF7](SEF7.md)   | Unix System Interfaces                          | 7 weeks    | SEF3, SEF6                | `course`  |
| [SEF8](SEF8.md)   | Mathematics for Computing & AI                  | 10 weeks   | SEF2 (plus basic algebra) | `course`  |
| [SEF9](SEF9.md)   | Professional Workflow & AI-Assisted Engineering | 6 weeks    | SEF5                      | `course`  |
| [SEF10](SEF10.md) | Software Engineering Foundations Capstone       | 8–10 weeks | SEF1–SEF9                 | `project` |

```text
SEF1 → SEF2
SEF2 → SEF3, SEF4, SEF5, SEF8
SEF3 + SEF4 + SEF5 → SEF6
SEF3 + SEF6 → SEF7
SEF5 → SEF9
SEF1–SEF9 → SEF10
```

SEF8 may be taken alongside SEF4–SEF7. Instructional lessons, assessments and practical labs are identified separately in each course.

**Draft duration estimates** reflect expanded topics and require calibration with learner evidence. Typed lesson entries must use the uniform format `1. **Title** — \`lesson\`` (or `\`test\`` / `\`lab\``). Do not add trailing inline explanations; required exercises and lab procedures belong in the course's **Completion requirements**.

---

## Independent study

OEE curriculum requirements are public and free to use. [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) helps learners organize practical work and evidence. Books, free online materials, chapter references and optional purchase links are curated outside the OEE specification; using 0xNAND or purchasing a resource is not required to follow the curriculum.

All ten courses remain `draft`. This curriculum underwent an initial technical-depth expansion, but it still needs independent subject-matter review, hands-on lab reproduction, assessment question/rubric authoring, realistic pacing checks and learner evidence. The published [Course Format](../../spec/course-format.md) governs the structure. The number of modules and lessons varies with the subject rather than an arbitrary cap. See the [SEF coverage review](REVIEW.md) for the work completed and the outstanding quality gates.
