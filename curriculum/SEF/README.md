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

| Course            | Title                                           | Duration    | Prerequisite              | Kind      |
| ----------------- | ----------------------------------------------- | ----------- | ------------------------- | --------- |
| [SEF1](SEF1.md)   | Demystifying the Computer System                | 5 weeks     | —                         | `course`  |
| [SEF2](SEF2.md)   | Programming & Computational Thinking            | 8 weeks     | SEF1                      | `course`  |
| [SEF3](SEF3.md)   | Linux & the Command Line                        | 8 weeks     | SEF2                      | `course`  |
| [SEF4](SEF4.md)   | Data Structures & Algorithms                    | 10 weeks    | SEF2                      | `course`  |
| [SEF5](SEF5.md)   | Software Engineering Practice                   | 8 weeks     | SEF2                      | `course`  |
| [SEF6](SEF6.md)   | C Programming & Machine Memory                  | 8 weeks     | SEF3, SEF4, SEF5          | `course`  |
| [SEF7](SEF7.md)   | Unix System Interfaces                          | 7 weeks     | SEF3, SEF6                | `course`  |
| [SEF8](SEF8.md)   | Mathematics for Computing & AI                  | 11–12 weeks | SEF2                      | `course`  |
| [SEF9](SEF9.md)   | Professional Workflow & AI-Assisted Engineering | 6 weeks     | SEF5                      | `course`  |
| [SEF10](SEF10.md) | Software Engineering Foundations Capstone       | 8–10 weeks  | SEF1–SEF9                 | `project` |

```text
SEF1 → SEF2
SEF2 → SEF3, SEF4, SEF5, SEF8
SEF3 + SEF4 + SEF5 → SEF6
SEF3 + SEF6 → SEF7
SEF5 → SEF9
SEF1–SEF9 → SEF10
```

## Study notes and course maturity

SEF8 may be taken alongside SEF4–SEF7. It begins with a self-paced mathematical literacy and pre-algebra bridge, so prior algebra is **not** an entry prerequisite; an ungraded diagnostic identifies where additional practice is needed. Basic numeracy and algebra readiness are still needed before progressing.

SEF1, SEF2, SEF3, SEF4 and SEF10 use the outcome-driven `v0.2.0` course format. The other five courses retain their historical assessment structure pending individual migration reviews. All ten are `draft`; duration estimates, technical coverage, practical-work reproducibility, assessment quality, and learner feedback still need validation. See the [curriculum inventory](../INVENTORY.md) for the generated migration report.

## Independent study

All required course information is publicly available. Use [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) or another learner-controlled environment to record practical work and evidence. Optional books and commercial instruction are not prerequisites for access to OEE.

For the binding authoring contract, consult [Course Format](../../spec/course-format.md). For course-planning advice, use the non-normative [Curriculum Design Guide](../DESIGN-GUIDE.md).
