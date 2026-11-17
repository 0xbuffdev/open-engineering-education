# SYS1 — Computer Architecture, Memory & Performance

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** [SEF10](../SEF/SEF10.md)
**Duration:** 10–14 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; validate through learner pilots)

> [Systems Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Explain what a compiled program does at the machine boundary and why physical implementation affects behavior and cost. Move from the simplified computer model of SEF1 and C objects of SEF6 to real instruction sets, executable construction, microarchitecture, memory hierarchy and evidence-based investigations. An x86-64 or RISC-V reference architecture is acceptable if instruction/ABI assumptions are made explicit.

**SEF baseline (already assessed; do not reteach):** SEF1 already assesses an educational processor model; SEF6 assesses C object representation and compiler/linker diagnostics; SEF8 covers basic numerical precision and statistics.

**New SYS competency (must be taught and assessed):** Teach actual ISA/ABI traces, relocations and ELF loading, CPU pipelines, cache/TLB effects and reproducible machine-level causal experiments. Neither basic gate construction nor general C compilation is reassessed.

**Course boundary:** SYS1 is architecture and measurable machine behavior, not repeated digital-logic construction from SEF1 or advanced OS implementation from SYS4.

**Environment and accessibility:** Use an unprivileged, learner-controlled Linux environment or an explicitly equivalent local simulator. Document tools and versions when they affect results; no paid platform or external host is required.

The duration is a planning estimate, not a completion or readiness claim. Required mastery is demonstrated through the assessments below, not time spent or lesson attendance.

## Learning outcomes

- **SYS1-O1:** Predict and verify ISA/ABI-specific register, flag, sign-extension, endianness and memory behavior of unfamiliar compiled code, distinguishing machine contracts from prior C11 number reasoning.
- **SYS1-O2:** Read and explain compiled assembly, stack frames, calls, returns, control flow and calling conventions for a declared instruction set and ABI.
- **SYS1-O3:** Trace preprocessing, compilation, assembly, linking, relocation, loading and initialization for a multi-file executable.
- **SYS1-O4:** Explain pipeline, branch prediction, superscalar/out-of-order execution and their limitations without assuming a particular CPU implementation.
- **SYS1-O5:** Predict and investigate cache, memory locality, TLB, page translation and memory-bandwidth effects under declared assumptions.
- **SYS1-O6:** Distinguish C abstract-machine behavior, undefined behavior, generated code, virtual addresses and actual machine observations.
- **SYS1-O7:** Design reproducible controlled performance experiments with baseline, warmup, repeated observations and uncertainty.
- **SYS1-O8:** Reason about machine isolation, privilege transitions, alignment, ABI and limits of microarchitectural performance or security claims.
- **SYS1-O9:** Produce and defend a falsifiable source-to-machine performance investigation using independent predictions and observed evidence.

## Modules

**Practice design:** Begin with traced or guided examples, progress to bounded independent investigations, and include one unfamiliar diagnostic or transfer task. Practice is formative unless named in a required assessment below.

### Module 1 — Course Orientation and Real Machines

#### Outcomes

- SYS1-O1
- SYS1-O8

#### Lessons

1. **From Teaching CPU to Modern Machine** — Contrast SEF1's simplified processor with a documented real ISA, its ABI and modern implementation limits; do not rebuild logic gates or the toy CPU.
2. **Architectural Contract** — Distinguish instruction-set architecture, microarchitecture, ABI, operating-system interface and language abstract machine.
3. **Hardware Components** — Trace how cores, registers, memory controllers, devices and interconnects participate in one program operation.
4. **Observation Boundaries** — Explain what a program, debugger, disassembler and CPU counter can and cannot reveal.
5. **Controlled Environment** — Identify architecture, CPU topology, compiler options and privilege constraints without requiring specialized hardware.

**Formative investigation:** Compare a reference-machine trace with a short real compiled example and label each layer's assumptions.

### Module 2 — Representation and Machine Arithmetic

#### Outcomes

- SYS1-O1
- SYS1-O6

#### Lessons

1. **Cross-ABI Data Layout** — Compare byte order and storage layout across two documented ABI/ISA contracts; trace interoperability consequences beyond SEF6 object-representation exercises.
2. **Instruction Flags and Widths** — Interpret ISA-level carry, overflow, sign extension and condition flags against C-language semantics already established in SEF6.
3. **Address and Loader Contracts** — Connect SEF6 pointer/provenance guarantees to relocation, virtual mappings and concrete machine address traces without treating pointer casts as portable C.
4. **Floating-Point Instructions** — Inspect FPU/SIMD instructions, rounding-mode and contraction assumptions in a compiled numerical operation using SEF8 numerical concepts.
5. **ABI Layout Constraints** — Predict padding, alignment, argument placement and FFI structure compatibility under named ABIs, extending rather than repeating SEF6 layout assumptions.
6. **Optimization Under C Semantics** — Explain how SEF6-known undefined or implementation-defined behaviors affect compiler transformations and why observed assembly cannot establish a portable C guarantee.

**Formative investigation:** Predict raw byte layouts and verify only defined cases with a small inspection program.

### Module 3 — Instruction Sets and Assembly

#### Outcomes

- SYS1-O1
- SYS1-O2

#### Lessons

1. **Instruction Encoding** — Decode a small sequence using the selected ISA's documented operand and register conventions.
2. **Arithmetic and Bitwise Operations** — Connect C expressions to register and instruction behavior, including width and sign extension.
3. **Memory Addressing** — Trace base/index/offset addressing and distinguish addresses from loaded values.
4. **Branches and Loops** — Relate conditional branches, comparisons and loop state to source control flow.
5. **Procedures and Stack Frames** — Trace calls, return addresses, saved registers and stack allocation under a named ABI.
6. **Debugger Investigation** — Step through a function while checking register and stack predictions.

**Formative investigation:** Explain an unfamiliar assembly function from its inputs, control flow and memory effects.

### Module 4 — From Source to Process

#### Outcomes

- SYS1-O2
- SYS1-O3

#### Lessons

1. **Real Toolchain Artifacts** — Build on SEF6's known compilation stages to inspect emitted assembly, symbol tables, relocation records and linked binary differences.
2. **Symbols and Relocations** — Resolve local/global symbol references and demonstrate a link error and its correction.
3. **Static and Dynamic Linking** — Compare object files, shared libraries, symbol resolution and runtime dependencies.
4. **Executable Format** — Inspect ELF sections, segments and entry points without confusing file sections with mapped memory.
5. **Program Loading** — Trace loader, runtime initialization, arguments, environment and the first application instruction.
6. **Calling Conventions** — Trace how a caller and callee exchange arguments, return values and preserved registers.

**Formative investigation:** Build two small C translation units and explain every stage required to run the resulting program.

### Module 5 — Processor Microarchitecture

#### Outcomes

- SYS1-O4
- SYS1-O8

#### Lessons

1. **Pipeline Stages** — Distinguish the pedagogical fetch/decode/execute sequence from modern implementation pipelines.
2. **Data Dependencies** — Explain read-after-write dependencies, forwarding and stalls on a simplified pipeline.
3. **Branch Prediction** — Predict performance effects of correctly versus incorrectly predicted branch patterns.
4. **Instruction-Level Parallelism** — Explain superscalar and out-of-order execution qualitatively without asserting unsupported CPU internals.
5. **Speculation and Boundaries** — Explain why speculative work may differ from architectural state and avoid claiming arbitrary side-channel exploits.
6. **Measurement Limitations** — Distinguish instruction counts, cycles, wall time and hardware-counter availability.

**Formative investigation:** Compare two bounded branch patterns and explain confounders before interpreting timing differences.

### Module 6 — Cache and Memory Hierarchy

#### Outcomes

- SYS1-O5

#### Lessons

1. **Locality** — Distinguish temporal and spatial locality with access traces and working-set changes.
2. **Cache Organization** — Model blocks, sets, ways, replacement and write policies for a declared cache model.
3. **Miss Classification** — Explain compulsory, capacity and conflict misses using trace-based counterexamples.
4. **Cache Coherence Overview** — Identify why multicore caches must coordinate shared lines; defer full concurrency reasoning to SYS5.
5. **Bandwidth and Latency** — Show why transfer rate, access latency and computation throughput describe different constraints.
6. **Simulator Design** — Build a bounded configurable trace-driven cache simulator with independent expected miss counts.

**Formative investigation:** Test a cache model against hand-derived traces before applying it to a program workload.

### Module 7 — Address Translation and Allocation

#### Outcomes

- SYS1-O5
- SYS1-O6
- SYS1-O8

#### Lessons

1. **Virtual and Physical Addresses** — Explain page mappings and address-space isolation using small page-table examples.
2. **TLB Behavior** — Predict translation-hit and miss consequences while distinguishing TLB from data caches.
3. **Page Fault Mechanisms** — Distinguish mapping, demand paging, protection faults and ordinary cache misses.
4. **Heap Allocation** — Observe allocation, lifetime and fragmentation trade-offs without promising a specific allocator's internals.
5. **Stack, Heap and Mappings** — Identify stack, heap, code and shared-object mappings and their platform variability.
6. **Protection Mechanisms** — Relate address-space separation and privilege to faults and access restrictions.

**Formative investigation:** Use a synthetic page-table and TLB trace to justify translation behavior and a declared model's limits.

### Module 8 — Reliable Benchmarking

#### Outcomes

- SYS1-O7
- SYS1-O9

#### Lessons

1. **Hypothesis and Metric** — Form a falsifiable source-to-machine prediction with a defined response variable.
2. **Experimental Controls** — Bound CPU state, compiler optimization, datasets, cache warmup and background interference.
3. **Repeated Sampling** — Compute simple distributions and express variability without cherry-picking the fastest sample.
4. **Optimization and Observability** — Distinguish dead-code elimination, constant folding and observable work in benchmarks.
5. **Instrumentation Limits** — Use available timers, disassembly or counters, recording tool privilege and precision limits.
6. **Interpretation** — Reject unsupported causal explanations and state alternative hypotheses.

**Formative investigation:** Prepare a measurement plan that would still be interpretable if the predicted speedup does not occur.

### Module 9 — Integrated Machine Investigation

#### Outcomes

- SYS1-O3
- SYS1-O4
- SYS1-O5
- SYS1-O7
- SYS1-O8
- SYS1-O9

#### Lessons

1. **Workload Selection** — Select deterministic matrix, traversal or parsing workloads with independent functional oracles.
2. **Assembly Evidence** — Connect selected source-level decisions to generated instructions and ABI behavior.
3. **Cache/Branch Prediction** — Predict resource effects and verify expectations against bounded traces or simulations.
4. **Implementation Alternatives** — Introduce one controlled change and inspect both functional and performance consequences.
5. **Independent Reproduction** — Prepare clean-build instructions, measured baseline, variance and resource limitations.
6. **Technical Defense** — Explain an unfamiliar result or counterexample without reverse-engineering a desired conclusion.

**Formative investigation:** Peer-review or independently challenge one causal claim before submitting the final investigation.

## Completion requirements

The evaluations below are **required summative assessments**. Exercises, investigations and checks in module lessons are formative unless explicitly included in a required assessment. All course outcomes must be demonstrated, and each decision must remain inspectable against this course revision. Equivalent accessible methods may demonstrate the same public criteria.

### Required summative assessments

- **SYS1-AS1** — Machine representations and execution
  - Outcomes: SYS1-O1, SYS1-O2, SYS1-O6
  - Work: Trace two bounded C functions from defined input through source semantics, generated assembly, registers, ABI calls and stack state; include one deliberately misleading undefined-behavior example without relying on its output.
  - Criteria: Width, sign, layout, control flow and ABI claims match declared architecture/compiler; no property is inferred from an undefined run.
  - Evidence: Annotated source/assembly, register-state tables, compilation flags and corrected misconception.
- **SYS1-AS2** — Build and load analysis
  - Outcomes: SYS1-O2, SYS1-O3, SYS1-O8
  - Work: Create a multi-file executable and explain symbols, relocations, linked libraries, load segments and privilege assumptions; induce and resolve one failure.
  - Criteria: Compilation stages and loader claims are accurate, independently reproducible and correctly separated.
  - Evidence: Source/build scripts, inspection commands/outputs, failure diagnosis and ABI/format caveats.
- **SYS1-AS3** — Memory hierarchy investigation
  - Outcomes: SYS1-O4, SYS1-O5, SYS1-O7
  - Work: Implement or validate a configurable cache model; compare sequential, strided and working-set cases and justify predicted versus observed performance.
  - Criteria: Simulator matches independently hand-derived traces; tests control confounders and avoid claiming cache internals from timing alone.
  - Evidence: Trace fixtures/oracles, simulator, measured samples, system description and limits.
- **SYS1-AS4** — Architecture reasoning and security boundary
  - Outcomes: SYS1-O5, SYS1-O6, SYS1-O8
  - Work: Solve unfamiliar page-table/TLB, memory layout and processor-boundary problems and identify unsupported isolation or performance conclusions.
  - Criteria: Translation and protection reasoning is consistent with stated model; assumptions and confidence limits are visible.
  - Evidence: Solved traces, checked mappings, counterexamples and reasoned boundaries.
- **SYS1-AS5** — Independent source-to-machine defense
  - Outcomes: SYS1-O3, SYS1-O4, SYS1-O5, SYS1-O7, SYS1-O9
  - Work: Choose a previously unseen program variation, predict a resource effect, implement and measure it, then explain disagreement or failure without changing the success criteria.
  - Criteria: Behavior is correct; claims follow measurements with uncertainty; source-to-machine causal arguments withstand questioning.
  - Evidence: Reproducible repository and report, raw samples, change diff, prediction, limitation and written/recorded/live equivalent defense.

### Completion decision

A reviewer confirms that **every required outcome** is evidenced against its assessment criteria, all required evaluations have inspectable decisions, executable results are reproducible from documented clean state, and stated correctness/performance/security guarantees are no stronger than the evidence supports. A missing essential capability may be reassessed with an equivalent new case; unrelated repeated submissions are not required.

Historical evidence remains associated with its original course identity and revision; this proposed redesigned course does not silently award, revoke, or convert earlier learner credit.
