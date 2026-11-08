# SYS1 — Computer Architecture, Memory & Performance

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** SEF5 *(legacy mapping; reconcile before activation)*
**Duration:** 6 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/SYS.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Build the mental model needed to explain why software behaves differently at the machine level. You will study instruction execution, registers, branches, caches, locality, translation, and performance measurement through experiments and low-level inspection.

## Learning outcomes

- Explain the relationship among instructions, registers, execution, and program behavior.
- Read basic generated assembly and connect it to source-level operations.
- Explain memory hierarchy, locality, caches, and TLBs at a practical level.
- Design experiments that distinguish competing explanations for performance behavior.
- Use benchmarks and measurements to support conclusions about system performance.

## Modules

### Module 1 — CPU & Instruction Execution

#### Outcomes

By the end of this module, the learner can:

- Explain **Digital logic and CPU organization** in the context of the course.
- Apply **Instructions, registers, and basic execution** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Digital logic and CPU organization** — `lesson`
2. **Instructions, registers, and basic execution** — `lesson`
3. **Checkpoint: CPU execution** — `test`
4. **Micro-lab: Trace a short sequence of instructions and identify register changes.** — `lab`

### Module 2 — Assembly & Program Behavior

#### Outcomes

By the end of this module, the learner can:

- Explain **Inspecting generated assembly** in the context of the course.
- Apply **Calls, branches, and prediction** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Inspecting generated assembly** — `lesson`
2. **Calls, branches, and prediction** — `lesson`
3. **Checkpoint: source-to-instruction reasoning** — `test`
4. **Micro-lab: Compare optimized and unoptimized assembly for a small function.** — `lab`

### Module 3 — Memory Hierarchy & Locality

#### Outcomes

By the end of this module, the learner can:

- Explain **Caches and locality** in the context of the course.
- Apply **TLBs and memory-access costs** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Caches and locality** — `lesson`
2. **TLBs and memory-access costs** — `lesson`
3. **Checkpoint: memory behavior** — `test`
4. **Micro-lab: Compare sequential and strided memory access on the same data.** — `lab`

### Module 4 — Performance Measurement

#### Outcomes

By the end of this module, the learner can:

- Explain **Benchmarks and experimental design** in the context of the course.
- Apply **Connecting measurements to explanations** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Benchmarks and experimental design** — `lesson`
2. **Connecting measurements to explanations** — `lesson`
3. **Checkpoint: evidence-based performance** — `test`
4. **Micro-lab: Form a performance hypothesis and design an experiment that can falsify it.** — `lab`

### Module 5 — Configurable Cache & Locality Simulator

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Build, run, and explain the Configurable Cache & Locality Simulator** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

### Topics

- digital logic foundations
- CPU organization
- instructions and registers
- assembly inspection
- instruction execution
- branches and prediction
- memory hierarchy
- caches
- locality
- TLBs
- performance measurement

### Labs

- inspect generated assembly
- trace instructions
- build a simple cache simulator
- compare sequential and strided memory access
- benchmark tiled versus naïve matrix multiplication

### Substantial course lab

**Configurable Cache & Locality Simulator**

The learner predicts performance, runs experiments, and explains why measured behavior differs from naïve Big-O reasoning.
