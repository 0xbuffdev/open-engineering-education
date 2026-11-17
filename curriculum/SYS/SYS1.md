# SYS1 — Computer Architecture, Memory & Performance

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** [SEF10](../SEF/SEF10.md) (completed SEF)
**Duration:** 12–16 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; requires learner calibration)

> [Systems Engineering](README.md) · [Course format](../../spec/course-format.md) · [Design guide](../DESIGN-GUIDE.md)

## Overview

Advance SEF1's simplified computer and SEF6's C memory model into a realistic, measurable understanding of machine behavior. Study instruction sets, ABI, compilation, pipelines, branches, cache hierarchies, translation and performance experiments. The principal assessed artifact is a parameterized trace-driven cache/translation simulator paired with an independently reproducible performance investigation. Use Linux, an ordinary C compiler and disassembler; simulators and supplied traces substitute for hardware performance counters when permissions or hardware differ. Do not reinterpret one observed microarchitecture as a universal ISA or OS guarantee.

## Learning outcomes

- **SYS1-O1:** Trace a compiled program through ISA instructions, registers, calling conventions and observable behavior.
- **SYS1-O2:** Differentiate architectural, microarchitectural, operating-system, compiler and C-language guarantees in a technical explanation.
- **SYS1-O3:** Calculate machine representation, alignment, endian and ABI effects from declared assumptions.
- **SYS1-O4:** Explain instruction dependencies, pipeline stalls, branch prediction and memory-level parallelism using an explicit model.
- **SYS1-O5:** Compute set, tag, block, associativity, replacement and write events for cache traces.
- **SYS1-O6:** Translate example virtual addresses through page tables and TLBs; explain faults, permissions and isolation.
- **SYS1-O7:** Investigate cache, TLB, memory bandwidth and execution effects with alternative falsifiable hypotheses.
- **SYS1-O8:** Use controlled disassembly to connect source-level changes and compiler options to machine-code behavior.
- **SYS1-O9:** Design reproducible performance tests with correctness checks, repeated samples, variability and environmental limitations.
- **SYS1-O10:** Implement and independently verify a configurable locality simulator against hand-derived and invalid-input cases.
- **SYS1-O11:** Defend an unfamiliar program-performance diagnosis using observations that discriminate competing explanations.

## Modules

### Module 1 — The Real Machine Boundary

#### Outcomes

- SYS1-O1
- SYS1-O2
- SYS1-O3

#### Lessons

1. **From teaching CPU to actual ISA** — Contrast SEF1's bit-to-program abstraction with target-specific architecture, microarchitecture and OS execution.
2. **Historical constraints** — Explain how stored programs, caches, virtual memory and out-of-order machines address distinct resource costs.
3. **Representation and ABI** — Calculate signed, unsigned, padding, alignment and endianness examples and state target assumptions.
4. **User, kernel and interrupts** — Trace a call through a library wrapper, privilege boundary and return; distinguish an interrupt from an ordinary function call.
5. **Observation provenance** — Compare an emulator trace, a disassembly and a Linux syscall trace; state what each can establish.

*Optional investigation: annotate a machine trace and mark all unobservable internal states.*

### Module 2 — Instructions and Execution

#### Outcomes

- SYS1-O1
- SYS1-O4
- SYS1-O8

#### Lessons

1. **Compiler outputs** — Compare preprocessing, assembly, object relocation and linking without equating source statements with instructions.
2. **Registers and addressing** — Trace loads, stores, register changes and addressing modes in a small emitted assembly example.
3. **Stack and call ABI** — Follow arguments, call/return state and stack alignment across several functions.
4. **Instruction dependencies** — Construct dependency graphs and identify the serial critical path.
5. **Pipelines and stalls** — Predict data and control hazards in a declared instructional pipeline.
6. **Branch behavior** — Contrast a branch-heavy input with equivalent branch-stable work, controlling compiler optimization.
7. **Optimized machine code** — Explain differences between -O0 and optimized output while verifying identical defined behavior.

### Module 3 — Cache Organization and Locality

#### Outcomes

- SYS1-O4
- SYS1-O5
- SYS1-O7
- SYS1-O10

#### Lessons

1. **Temporal and spatial locality** — Predict reuse in scans, strides and pointer-chasing from concrete address traces.
2. **Address decomposition** — Compute line offset, set index and tag for configurable geometry.
3. **Associativity and conflicts** — Predict collision patterns and distinguish capacity from conflict misses.
4. **Replacement and stores** — Model dirty eviction, write-back/write-through and write-allocate with an explicit selected policy.
5. **Cache hierarchy** — Explain why private and shared caches complicate interpreting local measurements.
6. **Prefetch and bandwidth** — Separate latency-hiding from bandwidth limits without promising hardware-specific speedups.
7. **Hand-derived expected results** — Create golden traces independently of simulator code, including adversarial conflict cases.

### Module 4 — Virtual Memory and Protection

#### Outcomes

- SYS1-O2
- SYS1-O6
- SYS1-O7

#### Lessons

1. **Virtual and physical addresses** — Identify page offset, frame and address-space boundaries in a hypothetical machine.
2. **Page-table walk** — Compute multi-level translations and permission failures from supplied entries.
3. **TLB and locality** — Model hits, misses and mapping changes without claiming a universal TLB policy.
4. **Demand faults and COW** — Explain fault handling, copy-on-write and mapped files conceptually.
5. **Permissions and privilege** — Compare user and kernel protections and state what ordinary processes can observe.
6. **Translation experiment** — Use page-size and stride changes to test hypotheses while disclosing cache confounders.

### Module 5 — Evidence-Based Performance Investigation

#### Outcomes

- SYS1-O4
- SYS1-O7
- SYS1-O8
- SYS1-O9
- SYS1-O11

#### Lessons

1. **Hypothesis versus story** — Write competing explanations and a discriminator before collecting numbers.
2. **Benchmark oracles** — Prevent eliminated work and independently verify the same outputs across variants.
3. **Measurement setup** — Record compiler, CPU, OS, affinity, thermal and background-load considerations when relevant.
4. **Latency and throughput** — Use separate methods for short latency, sustained throughput and bandwidth.
5. **Sampling and uncertainty** — Present repetitions, spread and plausible confounders rather than a single best timing.
6. **Optional hardware counters** — Interpret available counters cautiously and provide a portable alternative when blocked.
7. **Unfamiliar diagnosis** — Choose an intervention that distinguishes branch, cache or translation explanations.

### Module 6 — Simulator Integration and Review

#### Outcomes

- SYS1-O5
- SYS1-O6
- SYS1-O9
- SYS1-O10
- SYS1-O11

#### Lessons

1. **Behavior contract** — Specify trace syntax, cache geometry, errors and independent expected output.
2. **Core cache simulator** — Implement state, indexing, replacement, stores and eviction counters.
3. **Translation trace model** — Add a bounded TLB/page-table fixture model or an explicitly separate translation component.
4. **Negative and golden tests** — Exercise malformed traces, impossible geometry, dirty writeback and hand-computed misses.
5. **Comparative experiments** — Explain how line size, capacity and associativity change modeled results.
6. **Independent defense** — Investigate an unseen discrepancy, repair or justify it, and list unsupported hardware features.

## Completion requirements

Only the following are required summative evaluations. Lesson investigations and other formative work provide feedback; completion depends on demonstrated outcomes, not exercise checkmarks. Evidence may be reused across evaluations when criteria genuinely differ.

- **SYS1-AS1** — ISA, ABI and Translation Trace
  - **Outcomes:** SYS1-O1, SYS1-O2, SYS1-O3, SYS1-O6, SYS1-O8.
  - **Work:** Explain source, generated code, calling convention and privilege boundary for one small C program and compute supplied translation cases.
  - **Criteria:** Calculations and register/control-flow traces are reproducible; denied/invalid translations are recognized; C, ISA, ABI and OS claims are not conflated.
  - **Evidence:** Source, build flags, annotated disassembly, hand translations and written limits.

- **SYS1-AS2** — Cache/Translation Simulator
  - **Outcomes:** SYS1-O5, SYS1-O6, SYS1-O10.
  - **Work:** Build a configurable trace-driven simulator and test against independent oracle traces.
  - **Criteria:** Matches independently solved hit/miss/eviction and address-translation fixtures; rejects invalid geometry and malformed input; clean rebuild works.
  - **Evidence:** Source, model assumptions, golden traces, negative tests, output and reproduction commands.

- **SYS1-AS3** — Architectural Performance Experiment
  - **Outcomes:** SYS1-O4, SYS1-O7, SYS1-O8, SYS1-O9.
  - **Work:** Compare at least two controlled variants under falsifiable hypotheses, with correctness checked before measurement.
  - **Criteria:** Measurements repeated with variability and environment; evidence supports only warranted conclusions and acknowledges unavailable hardware counters.
  - **Evidence:** Benchmark harness, expected output, individual timings, compiler settings, plots/table and hypothesis evaluation.

- **SYS1-AS4** — Unfamiliar Machine-Behavior Defense
  - **Outcomes:** SYS1-O1, SYS1-O4, SYS1-O5, SYS1-O6, SYS1-O9, SYS1-O11.
  - **Work:** Analyze a new instruction or locality workload and decide between competing bottleneck explanations.
  - **Criteria:** Predict before measuring, explain results and invalid assumptions, implement or justify a correction and show an independent check.
  - **Evidence:** Challenge trace, before/after reasoning, tests and reviewable defense.

### Disciplinary and resource boundaries

SEF1 owns the introductory logic-to-CPU model; SEF6 owns C language/object memory correctness; SEF7 owns foundational Unix user-space interfaces. This course adds measurable machine organization and performance interpretation, not duplicated beginner coverage. CPU counters and privileged tooling are optional. Simulation is not proof of physical cache performance, and a microbenchmark cannot establish an application-wide speedup.

### Reproducibility and decisions

Required executable work must reproduce from a clean state with documented commands, recorded compiler/runtime and OS assumptions, synthetic fixtures and an independent expected-result oracle. Report measurement repetitions and uncertainty when quantitative claims are assessed. Evaluation records identify course revision, assessment, outcomes, decision, supporting evidence and material limitations; past legacy submissions are not silently regraded. All required work can be studied and reviewed without paid services. A `draft` course is not learner-tested or independently verified.
