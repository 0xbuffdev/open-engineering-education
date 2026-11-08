## SYS1 — Computer Architecture, Memory & Performance

**Duration:** 6 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** SEF5

### Overview

Build the mental model needed to explain why software behaves differently at the machine level. You will study instruction execution, registers, branches, caches, locality, translation, and performance measurement through experiments and low-level inspection.

### Prerequisites

**SEF5 — Low-Level Programming with C & Linux**

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Explain the relationship among instructions, registers, execution, and program behavior.
- Read basic generated assembly and connect it to source-level operations.
- Explain memory hierarchy, locality, caches, and TLBs at a practical level.
- Design experiments that distinguish competing explanations for performance behavior.
- Use benchmarks and measurements to support conclusions about system performance.


### Modules

#### Module 1 — CPU & Instruction Execution



### Module outcomes

By the end of this module, the learner can:

- Explain **Digital logic and CPU organization** in the context of the course.
- Apply **Instructions, registers, and basic execution** in a problem, implementation, experiment, or design decision.

1. **Digital logic and CPU organization**
   - kind: `lesson`
2. **Instructions, registers, and basic execution**
   - kind: `lesson`
3. **Checkpoint: CPU execution**
   - kind: `test`

4. **Micro-lab: Trace a short sequence of instructions and identify register changes.**
   - kind: `lab`
#### Module 2 — Assembly & Program Behavior



### Module outcomes

By the end of this module, the learner can:

- Explain **Inspecting generated assembly** in the context of the course.
- Apply **Calls, branches, and prediction** in a problem, implementation, experiment, or design decision.

1. **Inspecting generated assembly**
   - kind: `lesson`
2. **Calls, branches, and prediction**
   - kind: `lesson`
3. **Checkpoint: source-to-instruction reasoning**
   - kind: `test`

4. **Micro-lab: Compare optimized and unoptimized assembly for a small function.**
   - kind: `lab`
#### Module 3 — Memory Hierarchy & Locality



### Module outcomes

By the end of this module, the learner can:

- Explain **Caches and locality** in the context of the course.
- Apply **TLBs and memory-access costs** in a problem, implementation, experiment, or design decision.

1. **Caches and locality**
   - kind: `lesson`
2. **TLBs and memory-access costs**
   - kind: `lesson`
3. **Checkpoint: memory behavior**
   - kind: `test`

4. **Micro-lab: Compare sequential and strided memory access on the same data.**
   - kind: `lab`
#### Module 4 — Performance Measurement



### Module outcomes

By the end of this module, the learner can:

- Explain **Benchmarks and experimental design** in the context of the course.
- Apply **Connecting measurements to explanations** in a problem, implementation, experiment, or design decision.

1. **Benchmarks and experimental design**
   - kind: `lesson`
2. **Connecting measurements to explanations**
   - kind: `lesson`
3. **Checkpoint: evidence-based performance**
   - kind: `test`

4. **Micro-lab: Form a performance hypothesis and design an experiment that can falsify it.**
   - kind: `lab`
#### Module 5 — Configurable Cache & Locality Simulator



1. **Build, run, and explain the Configurable Cache & Locality Simulator**
   - kind: `lab`

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

---

