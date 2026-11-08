# SYS2 — Systems Programming with C & Rust

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** SYS1 *(legacy mapping; reconcile before activation)*
**Duration:** 6 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/SYS.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Work with Unix processes, memory allocation, files, system calls, and resource lifetimes in C and Rust. The course uses side-by-side implementations to make memory safety and ownership meaningful rather than abstract.

## Learning outcomes

- Use Unix system interfaces to interact with processes, files, and operating-system resources.
- Reason about resource ownership and lifetime in systems programs.
- Inspect and diagnose low-level memory and process behavior.
- Compare manual memory-management risks with Rust ownership and borrowing.
- Build a multi-module systems utility and test its failure and cleanup paths.

## Modules

### Module 1 — Unix Processes & Resources

#### Outcomes

By the end of this module, the learner can:

- Explain **Unix process model and process creation** in the context of the course.
- Apply **Resource ownership and lifetime** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Unix process model and process creation** — `lesson`
2. **Resource ownership and lifetime** — `lesson`
3. **Checkpoint: process and resource reasoning** — `test`
4. **Micro-lab: Track which component owns each file descriptor or allocated resource.** — `lab`

### Module 2 — Memory & System Calls

#### Outcomes

By the end of this module, the learner can:

- Explain **Memory allocation and address spaces** in the context of the course.
- Apply **Files, descriptors, and system calls** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Memory allocation and address spaces** — `lesson`
2. **Files, descriptors, and system calls** — `lesson`
3. **Checkpoint: system interfaces** — `test`
4. **Micro-lab: Observe a system call boundary and explain its inputs and outputs.** — `lab`

### Module 3 — C/Rust Safety Boundaries

#### Outcomes

By the end of this module, the learner can:

- Explain **C memory hazards and Rust ownership** in the context of the course.
- Apply **Unsafe boundaries and FFI concepts** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **C memory hazards and Rust ownership** — `lesson`
2. **Unsafe boundaries and FFI concepts** — `lesson`
3. **Checkpoint: safety guarantees** — `test`
4. **Micro-lab: Compare one resource-management implementation in C and Rust.** — `lab`

### Module 4 — Signals & Robust Services

#### Outcomes

By the end of this module, the learner can:

- Explain **Signals and controlled shutdown** in the context of the course.
- Apply **Error handling in systems programs** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Signals and controlled shutdown** — `lesson`
2. **Error handling in systems programs** — `lesson`
3. **Checkpoint: service correctness** — `test`
4. **Micro-lab: Add graceful signal handling and verify cleanup.** — `lab`

### Module 5 — Rust Unix Service Utility

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Build and validate the Rust Unix Service Utility** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

### Topics

- Unix process model
- memory allocation
- files and descriptors
- system calls
- ownership and resource lifetime
- unsafe versus safe boundaries
- process creation
- signals
- error handling
- FFI concepts

### Labs

- file-descriptor monitor
- process launcher
- allocator experiment
- C-to-Rust comparison
- resource cleanup tests

### Substantial course lab

**Rust Unix Service Utility**

A multi-module command-line or daemon-style utility that interacts directly with Linux facilities.
