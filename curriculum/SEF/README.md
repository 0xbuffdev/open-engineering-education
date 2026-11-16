# Program 1 — SEF: Software Engineering Foundations

> [OEE curriculum](../README.md) · [Specification](../../spec/README.md) · [OEE Workspace](https://github.com/0xbuffdev/oee-workspace)

## Overview

Software Engineering Foundations is the common entry program for learners with no programming experience. It begins with how computers compute—from physical-to-logical bit models, gates, memory and processors—then develops Python programming, discrete mathematical reasoning, Linux, algorithms, disciplined software engineering, C, Unix interfaces and numerical mathematics. Professional workflows and independent evidence support one cumulative project. The goal is to prepare graduates for Application, Systems, AI or Security Engineering without hidden foundational gaps.

## Prerequisites

**None.** Basic computer use is helpful, but there is no prior programming or formal mathematics course requirement. SEF11 offers an ungraded mathematics diagnostic and a self-paced arithmetic/algebra bridge, followed by mandatory demonstration of mathematical readiness before proof-intensive algorithms.

## Learning outcomes

By the end of the program, the learner can:

- Explain how bit patterns, logic, storage, instruction execution, devices and operating-system abstractions relate, including limits of a simplified reference machine.
- Implement, structure, test and debug Python software, including explicit state, functions, object construction/composition, type annotations, runtime validation, files, failures and reproducible command-line behavior.
- Solve arithmetic, algebraic, logical, set, counting, proof, recurrence and finite-graph problems independently and apply that reasoning to algorithm correctness.
- Select and implement fundamental data structures and algorithms, transferring SEF11 proof and recurrence foundations into verified invariants, termination/correctness arguments, qualified worst/expected/amortized complexity, and independent test oracles.
- Use Git, testing, debugging, module/interface contracts, cohesive design, code review, reproducible quality gates, requirements and professional engineering workflows with independent ethics, licensing, privacy, accessible communication and responsible AI obligations.
- Explain and safely apply C11 object representation, integer conversions, pointers, allocation and lifetime contracts, undefined-behavior boundaries, build diagnostics, bounded text/binary input, and owned dynamic arrays, linked lists and hash maps.
- Use the Linux shell and foundational Unix process, file-descriptor, signal, filesystem-identity, directory, pipe and bounded loopback-network interfaces, distinguishing C11/POSIX/library boundaries, resource ownership, and verified failure handling.
- Interpret functions, vectors, matrices, probability, statistics, derivatives, integrals and elementary numerical optimization with justified assumptions and uncertainty.
- Deliver, verify, explain and defend a bounded complete software project, including an independently executed or diagnosed change, verified prerequisite-evidence closure, relevant interdisciplinary transfer and an ethical, accessible, privacy- and licensing-aware professional release decision.

## Program completion standard

SEF requires demonstrated competence in **all eleven courses**. Before starting SEF10, verify actual prior completion evidence (or separately approved, genuinely assessed equivalence) for **SEF1–SEF9 and SEF11**. Missing prerequisite evidence cannot be replaced by a capstone portfolio, attendance, a diagnostic score, or self-reported experience.

The capstone develops **one learner-owned command-line developer utility** through its M1–M6 milestones. Its [graduation-evidence requirements](SEF10.md#prerequisite-closure-is-different-from-capstone-integration) link prior course completions to meaningful project work and bounded conceptual explanations, including a technical defense and responsible release decision. The project does **not** require unrelated hardware simulation, calculus demonstrations, C/POSIX network services, or APP/SYS specialization merely to check course names.

The [individual course files](README.md#courses) are authoritative for each outcome, required assessment, success criterion and evidence obligation. Learner completion records retain the course revision under which they were assessed; historical work is not silently upgraded or invalidated by later curriculum changes.

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

The catalog shows **one prerequisite-valid study order**, not a rule that every learner must take one course at a time.

- **Foundations:** SEF1 explains physical-to-logical computing abstractions; SEF2 establishes Python programming, state, files, data modeling and error handling. SEF11 teaches discrete mathematical reasoning with an **ungraded entry diagnostic** and a supported arithmetic/algebra bridge before formal proofs and recurrences. Prior mathematics credentials are not required for entry.
- **Parallel pathways:** After SEF2, learners may study **SEF3 (Linux and shell), SEF5 (software engineering practice), and SEF11** along separate paths. After SEF11, **SEF4 (algorithms) and SEF8 (numerical mathematics)** may proceed concurrently. SEF4 does not require probability or calculus from SEF8; its proofs, invariants and complexity arguments build on SEF11.
- **Low-level programming:** **SEF6** requires SEF3, SEF4 and SEF5, and develops C11 behavior, integer and object representations, memory ownership, safe parsing and data-structure libraries. **SEF7** follows SEF3 and SEF6, extending C11 foundations into bounded POSIX files, processes, signals, pipes, directories and local-loopback networking. Rust, advanced C/Rust comparison, multi-client servers and production-scale systems engineering belong to the later SYS pathway; the [SEF7–SYS competency destination map](UNIX-SYS-BOUNDARY.md) describes that division without removing any required SEF7 capability.
- **Professional responsibility:** **SEF9** follows SEF5 and evaluates genuine requirements, issue and review evidence, ethical decisions, software licensing, privacy, accessible communication and safe AI use. Its [synthetic practice case](../../examples/sef9/README.md) can be completed without private customer records, external model access or paid services.
- **Integration:** **SEF10** begins only after the ten preceding courses are complete. Learners apply relevant algorithms, software design, verification, measurement, professional communication and risk judgment to **one bounded project**. Verified competence from earlier courses is not a demand to recreate every prior artifact inside the capstone.

## Workload and pacing

The course durations above are **provisional study estimates**, generally based on 10–15 focused hours per week. Added across all eleven courses, they total approximately **115–143 course-weeks** (about **1,150–2,145 focused hours** at the nominal weekly workload). These are *totals of course estimates*, **not an elapsed-time requirement, guaranteed graduation date or fixed completion threshold**. Parallel courses can reduce calendar time but not the underlying work; some learners will require additional practice, mathematical preparation, accessibility adjustments or reviewer time.

Progress depends on meeting the published assessment criteria, not accumulating hours or completing a fixed quota of exercises. Assessed code, explanations, tests and project evidence can be **reused and extended** where the relevant published criteria are genuinely satisfied. The eleven courses currently declare **147 learning outcomes across 68 required summative assessment contracts**; these are not 68 separate applications or mandatory per-module quiz/lab pairs. The workloads and teaching sequence will be refined using genuine learner outcomes and recorded feedback, without silently reducing required competencies.

## Course format and readiness

**All eleven SEF course files use the OEE `v0.2.0` outcome-driven draft format and remain `draft`; no historical-format SEF course definitions remain.** The accepted [RFC 0003](../../rfcs/0003-sef-academic-progression.md) curriculum changes—including SEF11 before SEF4/SEF8 and the ten-prerequisite SEF10 capstone—are reflected in the published courses.

`draft` describes **course educational readiness**, not an incomplete course file or a failing student. A structurally complete course is not automatically `tested` or `verified`: those labels require actual learner completions, feedback/revision and independent review evidence under [Status Labels](../../spec/status-labels.md). Formal program conformance is a **separate review** under [Conformance](../../spec/conformance.md). The published curriculum does not claim accreditation, an automatic graduate award or demonstrated learner effectiveness. Study time, review accessibility and assessment quality should be refined from real learner experience; source checks alone cannot establish those results. The [curriculum inventory](../INVENTORY.md) provides reproducible source-format observations.

## Independent study

All mandatory outcomes, work, evidence and assessment criteria are publicly accessible. Use [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) or another learner-controlled environment to retain evidence. A paid learning platform, specific book, proprietary grader or mandatory external account cannot be a prerequisite for course completion.

The binding educational contract is in [Course Format](../../spec/course-format.md) and [Evidence Rules](../../spec/evidence-rules.md). For non-normative authoring guidance see the [Curriculum Design Guide](../DESIGN-GUIDE.md).
