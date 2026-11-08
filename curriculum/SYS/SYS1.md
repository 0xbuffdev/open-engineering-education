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


### Resource map

**Required**

- **B3** Ch. 1, 5–7 (esp. §§7.2–7.5 and §7.8), §5.5 and §§8.1–8.4 · **B6** Ch. 2, §§3.1–3.5, Ch. 4, §§6.2–6.3 and App. A.1 — carried from ZtP S2–S5.
- **B14** Ch. 3 (§§3.1–3.7), Ch. 5 and Ch. 6 — added for assembly inspection, program optimization and the memory hierarchy.

**Optional**

- **B32** Ch. 2 and 12 (Methodologies; Benchmarking) as forward reading for SYS7.

### Modules

#### Module 1 — CPU & Instruction Execution

**Reading:** **B3** Ch. 1 (From Zero to One), Ch. 5 (Digital Building Blocks), Ch. 6 §§6.1–6.4 (assembly language, machine language, programming), Ch. 7 §§7.2–7.5 (performance analysis; single-cycle, multicycle and pipelined processors). Review **B1**: “More of the Processor” → “Ta Daa!”.


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

**Reading:** **B3** Ch. 6 §§6.2–6.5 (assembly language; machine language; programming; addressing modes), Ch. 7 §7.8 (advanced microarchitecture: branch prediction, superscalar and out-of-order execution). **B14** Ch. 3 §§3.1–3.7 (machine-level representation: data movement, control, procedures). **B6** App. A.2 (Debug Branch Prediction).


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

**Reading:** **B3** §5.5 and §§8.1–8.4 (memory arrays; memory-system performance; caches; virtual memory). **B6** Ch. 2 (Commodity Hardware Today), §§3.1–3.5 (CPU caches), Ch. 4 §§4.1–4.3 (virtual memory, page tables, TLB behavior). **B14** Ch. 6 §§6.1–6.5 (storage technologies; locality; the memory hierarchy; cache memories; writing cache-friendly code). **B4** Ch. 19 (Paging: Faster Translations — TLBs).


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

**Reading:** **B6** Ch. 7 (Memory Performance Tools), App. A.4 (Measure Cache Size). **B14** Ch. 5 (Optimizing Program Performance), §6.6 (The Impact of Caches on Program Performance). *Optional:* **B32** Ch. 2 (Methodologies), Ch. 12 (Benchmarking).


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

**Reading:** **B3** §8.3 (caches: direct-mapped, set-associative and fully associative organizations; replacement and write policies). **B6** §3.2 (Cache Operation at High Level), §3.3 (CPU Cache Implementation Details), App. A.1 (Matrix Multiplication — tiling) and A.4. **B14** §6.4 (Cache Memories).


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

