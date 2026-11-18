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

Develop a rigorous **programmer's view of actual machine execution** after the assessed SEF foundations. Investigate a real compiled C program's ISA/ABI and layout, model instruction dependencies and throughput, calculate cache and virtual-address behavior, then test competing performance explanations. The substantial work is a configurable cache/TLB teaching simulator, independently solved machine traces and an explicitly controlled C benchmark investigation with an unfamiliar diagnostic defense. SYS1 establishes architecture and measurement competence; SYS10 later studies kernel implementation and SYS7 extends production profiling. It does **not** repeat SEF1's logic-gate computer, SEF6's C object/lifetime curriculum or SEF7's foundational Unix APIs.

**Accessibility and hardware assumptions:** One nonprivileged Linux environment, C11 compiler, debugger/disassembler or equivalent free inspection tool and self-created small synthetic files suffice. Inspect a **named real target and ABI** (for example local x86-64 System V/Linux or AArch64/Linux); an independent RISC-V or invented educational ISA may be used for supplied hand traces if its semantics are specified. Do not mix calling conventions from different targets. Hardware performance counters, vendor tools, root access, a paid service, a specific CPU model, specialized multicore hosts and public networks are **not** required. Supplied tabular traces, textual explanations and simulators are legitimate conceptual evidence; simulated hits/misses must never be reported as measured CPU events.

**Correctness and scope:** Only defined-behavior C is used for experimental comparisons; integer representation and ABI assumptions must be explicit. Cache/TLB teaching models describe declared policies, not hardware replacement, prefetch, coherence or actual Linux page-fault handlers. No physical timing conclusion follows solely from a cache simulation. Study OS privilege/fault *observable boundaries* here; implement OS handlers, page-table management and scheduling in [SYS10](SYS10.md).

**Workload:** 12–16 weeks at 10–15 focused hours/week is a provisional 120–240-hour study allocation for instruction tracing, hand calculations, simulator design/debugging, experimental measurements, independent verification, feedback and defense. Real learner evidence may require recalibration; completion is by outcomes and assessments, never time or formative checkmarks.

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

### Module 1 — Machine Contracts and Representation

#### Outcomes

- SYS1-O1
- SYS1-O2
- SYS1-O3

#### Lessons

1. **From a teaching computer to a real ISA contract** — Start with a defined program and the SEF1 machine model, then inspect the observable registers, instruction effects and exceptions of one named real ISA. Explain why stored-program execution remains compatible with changing pipelines and memory hierarchies; identify one behavior that an ISA promises and one that depends on an implementation. Do not repeat gate construction or a survey of computer history.
2. **Machine data and ABI-dependent layout** — Calculate integer widths, endian byte order, field offsets, padding and alignment for a declared target ABI, then check a defined-behavior C example with `sizeof` and `offsetof`. Contrast a valid numeric address calculation with a C pointer that cannot legally be dereferenced because of provenance or lifetime; reject signed-overflow and representation assumptions not justified by the selected language/target contract.
3. **Privilege transitions, exceptions and observation limits** — Trace a user call through a library wrapper and a syscall boundary, distinguishing a synchronous exception, external interrupt and normal function call. Compare what a disassembler, emulator trace and Linux userspace syscall trace can actually observe. Explain which mechanism must be investigated later in SYS10 rather than falsely inferring kernel implementation from a user trace.
4. **Architectural state versus hidden execution mechanisms** — Given two hypothetical implementations of the same ISA, predict which register/memory results must agree for a defined program and which cache, predictor or timing behavior may differ. Assign sample claims to C language, compiler, ABI, ISA, microarchitecture or OS authority, and correct an example that treats simulated or observed timing as a machine guarantee.

*Optional formative feedback:* Hand-calculate one struct layout under a named ABI and classify a misleading cross-layer trace; explain a counterexample rather than merely matching its label.

### Module 2 — Compiled Code, ISA and ABI

#### Outcomes

- SYS1-O1
- SYS1-O2
- SYS1-O3
- SYS1-O8

#### Lessons

1. **From C source to relocatable and linked machine code** — Follow one small defined C program through compilation, symbols, relocation and linking, inspecting an object file and the final binary. Explain why source statements do not correspond one-to-one to instructions, how a linker resolves references and why ELF is a target-specific object format rather than a universal execution contract.
2. **Instruction, register and control-flow tracing** — Starting from supplied register and memory state, derive effective addresses, operand sizes, branch destinations and observable state changes in real disassembly. Annotate a wrong-width operand or incorrectly interpreted branch as a negative case; check the trace against the selected ISA rather than guessing from source expressions.
3. **Calling conventions and nested-stack state** — Trace nested calls, argument and return placement, stack alignment and caller/callee-preserved registers under one documented target ABI. Predict the consequence of a deliberate preservation/alignment violation. Compare one meaningful convention difference using a separately documented target; never splice two target ABIs into a single trace.
4. **Optimization and observational equivalence** — Compare two compiler optimization settings using the same defined-behavior program, verified outputs and inspected disassembly. Account for inlining, removed work, changed branches or altered stack layout without assuming those are guaranteed optimizations. Explain how an invalid benchmark or undefined operation could make a purported speedup uninterpretable.

*Optional formative feedback:* Independently annotate a short compiled function and identify a wrong ABI or relocation interpretation using a target reference.

### Module 3 — Pipelines and Quantitative Processor Models

#### Outcomes

- SYS1-O4
- SYS1-O7
- SYS1-O8
- SYS1-O9

#### Lessons

1. **Instruction dependencies and pipeline hazards** — Derive a dependency graph and critical path for a supplied instruction sequence, then count data/control stalls in an explicitly defined teaching pipeline. State stages, forwarding and branch resolution assumptions; correct a false hazard inferred solely from source order or a model that silently assumes ideal forwarding.
2. **Branch predictions and control cost** — Apply a stated one- or two-bit teaching predictor to a branch sequence, calculate predictions and penalties, and contrast predictable with varying input paths. Check an actual compiled C branch comparison to ensure the optimizing compiler has not eliminated the feature being studied; distinguish toy-model misses from real hardware events.
3. **Latency, throughput, CPI and IPC** — Calculate instruction latency, reciprocal throughput, cycle counts, CPI and IPC under explicit workload and clock assumptions. Contrast dependency-limited and throughput-limited cases and identify why CPU clock rate or retired instruction counts alone cannot establish elapsed performance or a universal micro-operation count.
4. **Memory-level and out-of-order overlap** — Trace dependent pointer-chasing loads against independent memory operations in a bounded schematic schedule. Distinguish overlap, speculative execution and in-order retirement as separate claims; explain a counterexample where apparent instruction parallelism cannot hide a serial data dependency.
5. **Quantitative speedup and model limitations** — Apply Amdahl's law to a declared accelerated fraction and check limiting cases; relate bottleneck reasoning to a simple pipeline or memory-bound model. Reject a reported end-to-end improvement when only a small microbenchmark or an unspecified instruction timeline was observed.

*Optional formative feedback:* Solve one dependency schedule and one predictor counterexample; state which answers follow only from the supplied model.

### Module 4 — Cache Organization and Memory Locality

#### Outcomes

- SYS1-O4
- SYS1-O5
- SYS1-O7
- SYS1-O10

#### Lessons

1. **Locality from actual access sequences** — Generate and inspect address traces for scans, strides, reuse and pointer chasing. Predict temporal/spatial locality under a declared line size; identify how prefetching, cache capacity and compiler transformations could undermine a direct timing inference.
2. **Cache geometry, mapping and misses** — Derive offset, set and tag for valid power-of-two geometry, verify total capacity with safe integer arithmetic and classify compulsory/conflict/capacity misses relative to a stated reference model. Compare direct-mapped, set-associative and fully associative traces rather than assigning a universal miss label without reference.
3. **Replacement, writes and state invariants** — Hand-trace hit recency, LRU victim selection, write allocation, dirty eviction and write-back versus write-through under separately declared policies. Explain why cache write-back is not persistent storage durability and detect an impossible counter or incorrect post-eviction state.
4. **Hierarchy, latency and bandwidth bounds** — Work a declared single- or two-level average-memory-access-time estimate and an achievable-bandwidth lower bound. Distinguish latency hiding, prefetch traffic, private/shared caches and hierarchy organization from a serial simulator's simplified results; explain the assumptions that make overlap invalidate a simple AMAT calculation.
5. **Independent oracle traces for later implementation** — Produce short expected per-access set/tag/LRU/dirty-state tables before writing a simulator. Include a cold start, repeated hit, conflict, associativity change and write policy negative case, so later correctness does not rely on the learner's own implementation output.
6. **Model boundary and causal diagnosis** — For one unexplained locality or simulated miss result, compare two hypotheses and select an address or policy change that discriminates them. State explicitly why a serial private-cache trace cannot establish coherence, speculative access or a particular physical processor's timing.

*Optional formative feedback:* Hand-solve two-way LRU with a dirty eviction and challenge an incorrect hit/miss total.

### Module 5 — Virtual Translation, TLB and Protection

#### Outcomes

- SYS1-O2
- SYS1-O6
- SYS1-O7
- SYS1-O10

#### Lessons

1. **Virtual-address decomposition and page walks** — Compute virtual page numbers, page offsets, page-table indices and physical addresses from supplied page size, levels, entries and mappings. Distinguish a missing page mapping from a TLB miss and avoid inventing properties of Linux's actual page tables.
2. **TLB reuse, replacement and mapping changes** — Trace a declared TLB policy across hits, misses and address-space/mapping changes. Show why a changed mapping requires an appropriate invalidation in the teaching model; identify and correct an incorrectly reused stale translation without claiming a universal hardware policy.
3. **Protection, faults and OS responsibility** — Evaluate present, absent, read-only and user/supervisor cases using a specified permission table. Explain how demand faults or copy-on-write require an OS mapping decision and distinguish that decision from permission checks, cache misses and C pointer validity. Kernel implementation remains SYS10's responsibility.
4. **Composition of translation and data-cache state** — Specify whether a toy cache consumes virtual or translated physical addresses, and perform permission validation in a defined order. Demonstrate by trace why denied/absent accesses cannot increment a successful data-cache-access count or expose a fictional physical mapping.
5. **Page footprints and independent fault oracles** — Compare access patterns with similar byte work but different page footprints, calculate predicted TLB/page events and test independently hand-derived invalidation and protection fixtures. State cache/prefetch and OS scheduling confounders that prevent attributing a timing change uniquely to TLB misses.

*Optional formative feedback:* Hand-walk one mapping update and denied write, then correct a stale-TLB result without any privileged observation.

### Module 6 — Reproducible Performance Investigation

#### Outcomes

- SYS1-O4
- SYS1-O7
- SYS1-O8
- SYS1-O9
- SYS1-O11

#### Lessons

1. **Falsifiable performance questions and correctness oracles** — Before measuring, write competing explanations for a real defined-behavior C workload and predict an observation that separates them. Confirm identical intended outputs on boundary inputs, inspect machine code to rule out eliminated work, and reject a hypothesis if the compared variants perform different work.
2. **Metrics, controls and environment** — Choose latency, throughput or bandwidth metrics with meaningful units and denominators, then specify compiler flags, target, OS, input sizes, warmups, timer and sampling conditions. Design a no-work timer control and sufficient workload size to reveal overhead; explain when CPU frequency, scheduling, caches or thermal changes threaten comparison.
3. **Repeated measurement and uncertainty** — Collect individual trial results, center, spread and relevant confounders rather than a best-time screenshot. State assumptions about independence and variability; explain how an observed difference may be too small or inconsistent to support a claimed speedup.
4. **Analytical bounds and optional hardware evidence** — Calculate a traffic, dependency, bandwidth, CPI/IPC, AMAT or Amdahl bound with declared parameters and compare it to actual observations. Where hardware counters are accessible, interpret counting scope, multiplexing and scaling; otherwise use free nonprivileged timers, disassembly and explicitly labeled synthetic models without pretending they observed physical misses.
5. **Discriminating interventions and bounded conclusions** — Vary one causal factor at a time in instruction/branch and locality/page-footprint comparisons; inspect negative or inconclusive results and propose a follow-up falsifier. Report claims, evidence, alternative explanations and limitations; do not extend a bounded microbenchmark to an unknown production workload.
6. **Unfamiliar diagnostic reasoning** — Given a new timing or trace discrepancy, predict which observation would distinguish compiler removal, branch behavior, cache locality or translation effects. Justify an affordable intervention, revise the explanation when contradicted and separate a reasoned uncertainty from a verified diagnosis.

*Optional formative feedback:* Critique a two-variant speedup claim whose compiler output, work equivalence or timing variance is unknown.

### Module 7 — Cache/TLB Simulator and Independent Defense

#### Outcomes

- SYS1-O5
- SYS1-O6
- SYS1-O9
- SYS1-O10
- SYS1-O11

#### Lessons

1. **Define the public simulator contract** — Publish supported trace grammar, address radix/width, one-byte access semantics, cache geometry and policy, translation permissions, error behavior, counters, reset behavior and deliberate exclusions. Use checked arithmetic and explicit memory limits to reject impossible allocations or address/geometry overflow before implementation.
2. **Implement deterministic cache state** — Build set/tag lookup, LRU state updates, read/write behavior, dirty evictions and exact hit/miss/writeback accounting in a reproducible implementation. Trace state transitions for a small input and explain why the declared serial model does not simulate physical latency or coherence.
3. **Compose a bounded translation model** — Implement or cleanly separate a parameterized teaching page table and TLB with absent, denied, reuse and invalidation cases. If composed with cache simulation, enforce translation and permission checks before successful cache accounting; make unsupported permission/mapping combinations fail deterministically.
4. **Independently verify and challenge invariants** — Compare results against previously hand-computed golden traces for associativity, LRU, dirty writes, protection, TLB reuse and stale mapping. Verify hits + misses = accepted cache accesses and bounded eviction/writeback relationships; include malformed grammar, out-of-range addresses and geometry overflow rather than using simulator output as its own oracle.
5. **Interpret variations and defend an unfamiliar case** — Predict the effect of an unseen trace, changed capacity, associativity or translation state before executing it; reconcile observed and expected results with an independently checkable derivation. Explain model limitations and distinguish a genuine implementation bug from a change of assumptions; for a performance question, seek additional real evidence rather than inferring physical speed from the simulator.

*Optional formative feedback:* Exchange one tiny unseen trace, solve it by hand and explain a discrepancy or a justified uncertainty.

## Completion requirements

**Four summative assessments are required**, with one reviewable decision for each assessment and evidence supporting **all eleven course outcomes**. Module feedback prompts and other exploratory work remain optional practice. Shared source, fixtures or measurements may support several assessments without duplicating submissions, but each outcome-specific criterion must be independently evaluated.

- **SYS1-AS1** — ISA, ABI, Representation and Translation Trace
  - **Outcomes:** SYS1-O1, SYS1-O2, SYS1-O3, SYS1-O6, SYS1-O8.
  - **Work:** Build a small *defined-behavior* C program containing nested calls, a struct and an indexed memory access, document a real ISA/OS/ABI/compiler target, inspect its compiled artifact and compare two optimization settings. Annotate register/stack changes, preserved state, layout/endianness and selected control-flow instructions. Independently calculate an educational page-table/TLB fixture with successful translation, missing mapping, denied access and mapping-change/invalidation behavior.
  - **Criteria:** The local binary can be rebuilt and its annotated trace is consistent with the declared target and ABI; the learner derives a struct layout, calling-convention state, branch/register result and address-translation path rather than copying tool output. The same defined observable behavior is checked across optimization settings. Missing page, TLB miss, access denial and C pointer invalidity are **not** conflated. The learner explicitly categorizes claims under ISO C, compiler, ABI, ISA, microarchitecture or OS and rejects at least one tempting unsupported inference.
  - **Evidence:** Source/inputs and independent expected outputs; target/toolchain identity, compile options, inspectable disassembly/symbol excerpts, annotated machine-state trace, hand-computed layout and translation tables, plus concise contract/limitation explanation. A supplied cross-target fixture can support comparison; at least one locally compiled binary must be inspected.

- **SYS1-AS2** — Trace-Driven Cache/Translation Simulator
  - **Outcomes:** SYS1-O5, SYS1-O6, SYS1-O10.
  - **Work:** Implement a deterministic serialized-access cache simulator with configurable unsigned address width, power-of-two line size and set count, positive ways, loads/stores, **LRU replacement and write-back/write-allocate**, hit/miss/eviction/writeback counters and one-byte baseline accesses. Implement a separately configurable teaching page-table/TLB fixture supporting page size, presence, access permissions, TLB reuse/replacement and mapping change/invalidation. The two components may operate separately or together; if combined, translate and check permissions before recording a successful cache access.
  - **Criteria:** **Contract:** Specify input grammar, address radix/bounds, operation semantics, cache geometry, eviction/update policy, mapping/permission format, reset behavior, counters and explicit exclusions. For a stated power-of-two geometry, set = floor(address/line_size) mod number_of_sets and tag = floor(address/(line_size×number_of_sets)). Invalid or overflowing geometry cannot silently allocate or wrap. **Independent accuracy:** Publish hand-derived per-access state and exact expected totals for cold/repeated hits, a direct-mapped conflict, a two-way LRU reorder, dirty writeback, TLB miss/hit and at least one absent/denied/stale mapping with correct invalidation. For every successful modeled cache access, hits + misses = accesses; evictions cannot exceed misses; dirty writebacks cannot exceed evictions. Independently explain why changing associativity, capacity or translation state changes a supplied trace, without claiming that the model predicts physical cache latency. A reviewer may supply a new, equivalent trace to distinguish understanding from memorizing an example. **Robustness:** Reject unknown/truncated operations, out-of-range addresses, zero/non-power-of-two parameters where disallowed, arithmetic overflow, invalid permission combinations and impossible mappings safely and deterministically; test normal, boundary and invalid paths. Clean rebuild uses documented, freely available tools with no privilege or hidden fixture.
  - **Evidence:** Source, documented format and invariants, clean build/run commands, hand-computed golden tables prepared independently of implementation output, test results for negative/boundary cases and clear limitations.

- **SYS1-AS3** — Reproducible Architecture Performance Investigation
  - **Outcomes:** SYS1-O4, SYS1-O7, SYS1-O8, SYS1-O9.
  - **Work:** Study **at least two meaningfully different mechanisms** using bounded defined C workloads: one locality/page-footprint/bandwidth comparison and one instruction-dependency/branch/compiler-code comparison. Before measuring each, state competing explanations and observations that would distinguish them. Examine compiled machine code to confirm that the intended difference survived optimization. Perform a quantitative hand calculation using relevant declared dependency/pipeline, CPI/IPC, bandwidth, AMAT or Amdahl models and contrast the model with empirical timing.
  - **Criteria:** **Validity:** Correctness of equivalent observed results is independently verified on representative and boundary inputs; no undefined behavior, eliminated benchmark or unexplained workload mismatch supports a performance conclusion. Source/flags, workload, input sizes and hypotheses are published. **Measurement:** Record target/OS/compiler/flags, benchmark procedure, warmup and measurement conditions; give **five or more individual timed trials for each variant**, with units, a center and spread, and reasonable limitations for scheduling/CPU-frequency/cache effects. Privileged counters are optional; when used, explain availability/multiplexing/scaling as relevant. If a physically inaccessible hardware feature is not observed, analyze the corresponding synthetic model without presenting its values as measured counters. **Inference:** Compare measured and predicted effects, evaluate alternatives against discriminating observations, identify at least one confounder per comparison and limit the claimed speedup to what the experiment actually established. Do not infer a specific microarchitecture or whole-application optimization from a single benchmark.
  - **Evidence:** Benchmark source and output oracle, inspected disassembly, preregistered hypothesis notes, raw trial timings, calculations, reproducible commands and evidence/alternative/limitation interpretation.

- **SYS1-AS4** — Unfamiliar Machine-Behavior Defense
  - **Outcomes:** SYS1-O11.
  - **Work:** Independently diagnose a **previously unseen**, bounded machine-behavior or performance discrepancy using a reviewer-supplied public trace, controlled C fixture, or transparent case-generation rule. The scenario may involve ISA/ABI state, a dependency/branch model, a cache/TLB trace or measurement validity; it must genuinely require choosing between competing explanations. Predict relevant observations **before** running a tool, compare at least two plausible explanations and revise or defend a conclusion against an independent check. SYS1-AS1–AS3 separately establish the machine, model, simulator and measurement outcomes; this review measures their transfer into an unfamiliar diagnosis, not six new complete submissions. No inaccessible hardware counter or secret service is required.
  - **Criteria:** The learner identifies the stated model and assumptions, reconstructs the relevant machine or measurement facts rather than relying on unexplained tool output, and chooses a diagnostic intervention whose expected result distinguishes hypotheses or explicitly explains why it cannot. At least one meaningful negative/edge condition or violated assumption is addressed. The hand-derived or independently checked evidence supports the diagnosis, or an honest correction records unresolved uncertainty without claiming proof. The new case differs materially from submitted examples and demonstrates independent reasoning, not a memorized simulator trace or repetition of SYS1-AS1–AS3.
  - **Evidence:** Unseen case and reproduction parameters, predictions made before observation, relevant hand reasoning or independent reference check, observed results where applicable, the discriminating decision and a reviewable written, recorded or live defense with corrections and material limits.

### Boundary, safety, revisions and independent review

SEF1 owns gate-to-CPU foundations; SEF6 owns C object memory and lifetime correctness; SEF7 owns introductory Unix user-space interfaces. SYS1 deepens real machine execution, ABI interpretation, locality/translation arithmetic and evidence-based performance reasoning. SYS10 owns real kernel trap/translation/scheduling implementation, SYS3 owns concurrent memory-ordering correctness and SYS7 owns deeper production profiling. Hardware cache policy, TLB structure and branch predictors are explicitly model-specific, not universal contracts.

Use only owned bounded fixtures and local processes, never privileged profiling requirements, uncontrolled kernel modification, unsafe C behavior or public network traffic. Textual trace tables are valid accessible alternatives to diagrams. Required work and acceptance criteria are publicly specified and independently reviewable without paid products.

These revisions preserve **SYS1-O1–O11** and **SYS1-AS1–AS4**, consolidate lessons around distinguishable capabilities and correct **SYS1-AS4** to evaluate its distinct transfer/diagnosis outcome (**SYS1-O11**) rather than claiming that one optional kind of unfamiliar scenario independently re-evaluates six different outcomes. SYS1-AS1–AS3 continue to establish those earlier competencies through their explicit criteria; independent simulator oracles, controlled benchmark comparisons and repeated observations remain required. Such changes apply only to this source revision: historical learner evaluations must remain identified by their prior contract and must not be retroactively regraded. Required records associate the course and assessment revision, outcome IDs, review decision, evidence and material limitations. The course remains `draft` pending actual learner testing and qualified review; structural checks do not prove educational validity.

### Optional disciplinary references

- [UC Berkeley CS61C course materials](https://cs61c.org/fa26/) and [open notes](https://notes.cs61c.org/) — ISA, processor organization, locality and virtual memory.
- [Carnegie Mellon 15-213](https://www.cs.cmu.edu/~213/) — machine-level programming, optimization and performance.
- [RISC-V ISA specifications](https://docs.riscv.org/) and [ELF psABI](https://riscv-non-isa.github.io/riscv-elf-psabi-doc/) — target-dependent ISA and calling-convention standards.
- [Linux perf-stat](https://man7.org/linux/man-pages/man1/perf-stat.1.html) and [perf_event_open](https://man7.org/linux/man-pages/man2/perf_event_open.2.html) — optional hardware counter limits.

These are review/learning aids, not paid prerequisites or claims of accreditation.
