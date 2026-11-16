# Program 1 — SEF: Software Engineering Foundations

> [OEE curriculum](../README.md) · [Specification](../../spec/README.md) · [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) · [Mathematics migration](MATH-MIGRATION.md)

## Overview

Software Engineering Foundations is the common entry program for learners with no programming experience. It begins with how computers compute—from physical-to-logical bit models, gates, memory and processors—then develops Python programming, discrete mathematical reasoning, Linux, algorithms, disciplined software engineering, C, Unix interfaces and numerical mathematics. Professional workflows and independent evidence support one cumulative project. The goal is to prepare graduates for Application, Systems, AI or Security Engineering without hidden foundational gaps.

## Prerequisites

**None.** Basic computer use is helpful, but there is no prior programming or formal mathematics course requirement. SEF11 offers an ungraded mathematics diagnostic and a self-paced arithmetic/algebra bridge, followed by mandatory demonstration of mathematical readiness before proof-intensive algorithms.

## Learning outcomes

By the end of the program, the learner can:

- Explain how bit patterns, logic, storage, instruction execution, devices and operating-system abstractions relate, including limits of a simplified reference machine.
- Implement, structure, test and debug Python software, including explicit state, functions, object construction/composition, type annotations, runtime validation, files, failures and reproducible command-line behavior.
- Solve arithmetic, algebraic, logical, set, counting, proof, recurrence and finite-graph problems independently and apply that reasoning to algorithm correctness.
- Select and implement fundamental data structures and algorithms and justify invariants, worst/expected/amortized complexity and trade-offs with independent evidence.
- Use Git, testing, debugging, module/interface contracts, cohesive and appropriately decoupled designs, accessible code review, documentation, reproducible CI-equivalent checks, requirements and professional engineering workflows.
- Explain and safely apply C object representation, pointers, lifetimes, dynamic allocation and compiler/linker behavior.
- Use the Linux shell and foundational Unix process, file-descriptor, filesystem, pipe and bounded-network interfaces.
- Interpret functions, vectors, matrices, probability, statistics, derivatives, integrals and elementary numerical optimization with justified assumptions and uncertainty.
- Deliver, verify, explain and defend a bounded complete software project, including an independently executed or diagnosed change.

## Program completion standard

Complete and demonstrate the required outcomes for **all eleven courses**, including discrete mathematics (SEF11) and revised numerical mathematics (SEF8), then successfully defend the **same** learner-owned project in SEF10. Completing the arithmetic diagnostic, attending classes, or reporting elapsed hours does not establish mastery. The [course files](README.md#courses) define the current required summative evidence; completed work remains pinned to the course revision under which it was evaluated.

---

## Courses

This table is the **authoritative prerequisite-valid study order**, not numerical course-ID order. Stable identifiers are retained for historical compatibility; SEF11 is introduced between foundational programming and proof-intensive algorithms without renumbering SEF4–SEF10.

| Course | Title | Duration | Prerequisite | Kind |
| --- | --- | --- | --- | --- |
| [SEF1](SEF1.md) | Demystifying the Computer System | 5 weeks | — | `course` |
| [SEF2](SEF2.md) | Programming & Computational Thinking | 10–12 weeks | SEF1 | `course` |
| [SEF11](SEF11.md) | Discrete Mathematics for Computing | 10–14 weeks | SEF2 | `course` |
| [SEF3](SEF3.md) | Linux & the Command Line | 10–12 weeks | SEF2 | `course` |
| [SEF4](SEF4.md) | Data Structures & Algorithms | 10 weeks | SEF11 | `course` |
| [SEF5](SEF5.md) | Software Engineering Practice | 10–12 weeks | SEF2 | `course` |
| [SEF8](SEF8.md) | Mathematics for Numerical Computing & AI | 12–14 weeks | SEF11 | `course` |
| [SEF6](SEF6.md) | C Programming & Machine Memory | 8 weeks | SEF3, SEF4, SEF5 | `course` |
| [SEF7](SEF7.md) | Unix System Interfaces | 7 weeks | SEF3, SEF6 | `course` |
| [SEF9](SEF9.md) | Professional Workflow & AI-Assisted Engineering | 6 weeks | SEF5 | `course` |
| [SEF10](SEF10.md) | Software Engineering Foundations Capstone | 8–10 weeks | SEF1–SEF9, SEF11 | `project` |

```text
SEF1 → SEF2
SEF2 → SEF3, SEF5, SEF11
SEF11 → SEF4, SEF8
SEF3 + SEF4 + SEF5 → SEF6
SEF3 + SEF6 → SEF7
SEF5 → SEF9
SEF1–SEF9 + SEF11 → SEF10
```

## Study notes and course maturity

SEF3 and SEF5 can begin after SEF2 while SEF11's required mathematical preparation is underway. SEF3 develops Bash automation, explicit POSIX-sh/GNU portability boundaries and reproducible environment reasoning before later Unix/C system interfaces in SEF7; its portability and process-environment work has publicly assessed outcomes, not hidden prerequisites. Once SEF11 is complete, SEF4 and SEF8 may be studied in parallel. Course codes are stable identifiers, not rigid sequential enrollment numbers. Learners who need additional foundational mathematics are supported by SEF11's **ungraded entry diagnostic** and unlimited reasonable remediation/reassessment under published criteria.

**All eleven SEF course files use the OEE `v0.2.0` outcome-driven draft format and remain `draft`.** (no historical-format SEF course definitions remain). A clean structural migration does not show verified learner outcomes or educational effectiveness. The estimated durations, including SEF11's bridge and SEF8's revised numerical work, remain provisional until actual learner and reviewer feedback justifies them. See [curriculum inventory](../INVENTORY.md) for reproducible structural observations.

The accepted [RFC 0003](../../rfcs/0003-sef-academic-progression.md) introduced SEF11 and moved discrete mathematical readiness out of the previous SEF8. The [historical evidence map](MATH-MIGRATION.md) records the old/current outcome and assessment identities; neither learners nor implementations may silently convert old completion records into completion of a new course. Other SEF academic hardening work proceeds in separate reviewable course revisions under the accepted RFC. Focused SEF2, SEF3 and SEF5 revisions respectively establish Python abstractions/typing, shell portability/environment reasoning, and demonstrable software design/quality/review, preserving their original outcome IDs and assessment contracts while newly assessed competencies receive new IDs.

## Independent study

All mandatory outcomes, work, evidence and assessment criteria are publicly accessible. Use [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) or another learner-controlled environment to retain evidence. A paid learning platform, specific book, proprietary grader or mandatory external account cannot be a prerequisite for course completion.

The binding educational contract is in [Course Format](../../spec/course-format.md) and [Evidence Rules](../../spec/evidence-rules.md). For non-normative authoring guidance see the [Curriculum Design Guide](../DESIGN-GUIDE.md).
