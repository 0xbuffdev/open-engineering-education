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

1. **From teaching CPU to actual ISA** — Contrast SEF1's bit-to-program abstraction with target-specific architecture, microarchitecture and OS execution. Use a specific real ISA and a hypothetical educational machine side by side; list which assumptions about registers, protection and execution must not be transferred between them.
2. **Historical constraints** — Explain how stored programs, caches, virtual memory and out-of-order machines address distinct resource costs. Give a concrete latency, storage or control-flow pressure for each historical mechanism and explain why later designs retain older architectural interfaces.
3. **Representation and ABI** — Calculate signed, unsigned, padding, alignment and endianness examples and state target assumptions. Derive actual layout from a stated ABI and compare hand results with C sizeof/offsetof checks; distinguish target-defined signed representation from C signed-overflow rules.
4. **User, kernel and interrupts** — Trace a call through a library wrapper, privilege boundary and return; distinguish an interrupt from an ordinary function call. Identify the distinction between a libc wrapper and a syscall, and between a synchronous fault and an external interrupt; leave kernel handling policy to SYS10.
5. **Observation provenance** — Compare an emulator trace, a disassembly and a Linux syscall trace; state what each can establish. Classify each observation as ISA/ABI, OS, compiler or microarchitectural evidence; explain what source and sampling limits prevent it from proving.
6. **Contracts and machine state** — Distinguish architectural registers, exceptions and instruction effects from hidden predictor and cache state. Given two hypothetical implementations of one ISA, explain which outcomes must agree and which performance results may differ.
7. **Address values versus pointer validity** — Contrast numeric machine addresses, object lifetime and C pointer validity with a safe hypothetical trace; show why a bit pattern being expressible does not authorize dereference.

*Optional formative feedback:* Given one defined C struct and a specified target-layout table, compute alignment, byte offsets and endian storage; identify two facts that would change under a different ABI.

### Module 2 — Compiled Code, ISA and ABI

#### Outcomes

- SYS1-O1
- SYS1-O2
- SYS1-O3
- SYS1-O8

#### Lessons

1. **Compiler outputs** — Compare preprocessing, assembly, object relocation and linking without equating source statements with instructions. Inspect a real object's symbols and relocations; identify what the linker may resolve and why disassembly does not faithfully reconstruct source-level variables.
2. **Registers and addressing** — Trace loads, stores, register changes and addressing modes in a small emitted assembly example. Provide initial register/memory state and calculate effective addresses, operand widths and visible register effects, including a wrong-width counterexample.
3. **Stack and call ABI** — Follow arguments, call/return state and stack alignment across several functions. Use a named ABI to trace nested-call arguments, return values, volatile/preserved registers and stack alignment, then predict a deliberate ABI-violation symptom.
4. **Optimized machine code** — Explain differences between -O0 and optimized output while verifying identical defined behavior. Show why optimizing compilers may inline, unroll or eliminate work without altering defined outputs; reject undefined C or unused-result benchmarks as evidence.
5. **Object files and relocations** — Use a short symbol/relocation listing to identify unresolved addresses before linking, explain ELF as one target-dependent format, and connect the final binary with the inspected disassembly.
6. **Branches and machine control** — Trace taken and not-taken branch paths for concrete initial state, including PC and register changes, and distinguish architectural correctness from predictor efficiency.
7. **Calling convention portability** — Compare one documented ABI difference in argument registers or stack alignment across two named targets, using supplied reference disassembly if no cross compiler exists.

*Optional formative feedback:* Annotate one small real machine function with register/stack state; cross-check a deliberately wrong caller/callee-saved annotation.

### Module 3 — Pipelines and Quantitative Processor Models

#### Outcomes

- SYS1-O4
- SYS1-O7
- SYS1-O8
- SYS1-O9

#### Lessons

1. **Instruction dependencies** — Construct dependency graphs and identify the serial critical path. Calculate dependency edges and critical-path latency for a declared instruction sequence; distinguish hazards from source-level expression order.
2. **Pipelines and stalls** — Predict data and control hazards in a declared instructional pipeline. Count hazards in a specifically defined teaching pipeline and document forwarding, stage and branch-resolve assumptions rather than claiming hardware timing.
3. **Branch behavior** — Contrast a branch-heavy input with equivalent branch-stable work, controlling compiler optimization. Design an input pair whose branch predictability differs and verify compiled code still contains the relevant conditional before drawing performance conclusions.
4. **Latency, throughput and cycles** — Distinguish clock frequency, instruction latency, reciprocal throughput and elapsed time; calculate a bounded example and identify why a faster frequency alone does not imply faster execution.
5. **Branch predictor teaching model** — Apply a declared one-bit or two-bit toy predictor to a sequence and count misses and penalty cycles, clearly separating the model from an actual chip.
6. **Memory-level parallelism** — Contrast dependent pointer-chasing loads with independent loads in a schematic out-of-order execution timeline; preserve in-order architectural retirement as a separate idea.
7. **CPI, IPC and critical path** — Calculate CPI and IPC with explicit cycle/instruction counts and compare to dependency critical path; explain why retired instructions and micro-operations are not universally interchangeable.
8. **Amdahl and end-to-end speedup** — Compute speedup using a stated accelerated fraction and local speedup, check limiting cases, and reject claims that a fast microbenchmark proves an overall application win.

*Optional formative feedback:* Work one declared dependency schedule, one branch-prediction sequence and one Amdahl calculation; distinguish model output from CPU measurement.

### Module 4 — Cache Organization and Memory Locality

#### Outcomes

- SYS1-O4
- SYS1-O5
- SYS1-O7
- SYS1-O10

#### Lessons

1. **Temporal and spatial locality** — Predict reuse in scans, strides and pointer-chasing from concrete address traces. Generate a concrete address trace for each locality claim and contrast sequential access with irregular pointer chasing without presuming physical prefetch.
2. **Address decomposition** — Compute line offset, set index and tag for configurable geometry. Derive offset bits, set bits and tag for declared power-of-two geometry; independently check cache capacity and reject impossible combinations.
3. **Associativity and conflicts** — Predict collision patterns and distinguish capacity from conflict misses. Explain compulsory, conflict and capacity misses through hand traces and a fully associative comparison, noting that classification depends on reference model.
4. **Replacement and stores** — Model dirty eviction, write-back/write-through and write-allocate with an explicit selected policy. Trace LRU hit updates, dirty state, write-back eviction and write allocation; distinguish these modeled cache writes from persistent durability.
5. **Cache hierarchy** — Explain why private and shared caches complicate interpreting local measurements. Explain inclusive/noninclusive and private/shared cache possibilities while explicitly excluding coherence and actual multilevel timing from the simulator.
6. **Prefetch and bandwidth** — Separate latency-hiding from bandwidth limits without promising hardware-specific speedups. Compute a bandwidth lower bound and explain when hardware prefetch hides latency but consumes traffic; a modeled miss reduction is not automatically speedup.
7. **Hand-derived expected results** — Create golden traces independently of simulator code, including adversarial conflict cases. Produce independent tabular per-access expected state and negative/boundary examples BEFORE running the submitted simulator.
8. **Average memory access time** — Calculate a stated one- or two-level AMAT example with units; enumerate conditions such as overlap, queues and prefetch that break the simple estimate.
9. **Model exclusions and coherence** — Explain why one serial, private cache cannot model coherence, speculative access or multicore interference, and identify which trace-level claims remain demonstrable.

*Optional formative feedback:* Derive direct-mapped and two-way per-access set/tag, LRU and dirty-writeback tables independently; challenge an impossible claimed counter total.

### Module 5 — Virtual Translation, TLB and Protection

#### Outcomes

- SYS1-O2
- SYS1-O6
- SYS1-O7
- SYS1-O10

#### Lessons

1. **Virtual and physical addresses** — Identify page offset, frame and address-space boundaries in a hypothetical machine. Compute VPN and page offset using declared page size; separate virtual identity from physical frame allocation and OS authority.
2. **Page-table walk** — Compute multi-level translations and permission failures from supplied entries. Compute a multilevel index walk using specified PTE widths, present bits and permissions, and classify a missing entry separately from a TLB miss.
3. **TLB and locality** — Model hits, misses and mapping changes without claiming a universal TLB policy. Trace hit, miss and invalidation with a specified educational replacement policy; avoid assuming Linux or a target CPU implements that policy.
4. **Demand faults and COW** — Explain fault handling, copy-on-write and mapped files conceptually. Explain a first-touch or COW write as a fault plus an OS mapping action, not as automatic hardware allocation, and leave implementation to SYS10.
5. **Permissions and privilege** — Compare user and kernel protections and state what ordinary processes can observe. Use read/write/execute and user/kernel access modes in a stated permission table; explain why C pointer validity is a different layer.
6. **Translation experiment** — Use page-size and stride changes to test hypotheses while disclosing cache confounders. Create two patterns with similar byte traffic but different page footprints; state cache/prefetch confounders and why timings cannot uniquely identify TLB misses.
7. **Permissions and fault oracles** — Independently solve present, absent, read-only and user/supervisor access cases under a supplied PTE model; separate protection faults from language-level undefined behavior.
8. **Mapping changes and TLB state** — Show a mapping update with stale TLB contents and a correctly modeled invalidation; distinguish OS mechanisms delegated to SYS10 from SYS1 address-translation semantics.
9. **Translation-cache composition** — Decide whether a teaching cache consumes virtual or translated physical addresses and trace permission-check ordering; prove a denied access cannot silently become a successful cache event.

*Optional formative feedback:* Hand-walk a page table including a TLB reuse, missing page and denied write; explain a mapping update requiring model invalidation.

### Module 6 — Reproducible Performance Investigation

#### Outcomes

- SYS1-O4
- SYS1-O7
- SYS1-O8
- SYS1-O9
- SYS1-O11

#### Lessons

1. **Hypothesis versus story** — Write competing explanations and a discriminator before collecting numbers. List at least two explanations that imply different observable results and a genuine falsifier; do so before seeing benchmark output.
2. **Benchmark oracles** — Prevent eliminated work and independently verify the same outputs across variants. Compare variants that compute equivalent defined results with independent output checks; inspect assembly so dead-code elimination cannot invalidate conclusions.
3. **Measurement setup** — Record compiler, CPU, OS, affinity, thermal and background-load considerations when relevant. Record compiler version/flags, target, OS, workload, warmup and environment constraints; avoid requiring privileges or unavailable NUMA hardware.
4. **Latency and throughput** — Use separate methods for short latency, sustained throughput and bandwidth. Select throughput, latency or bandwidth metrics with units and correct denominator; explain why elapsed-time ratios from unequal work are meaningless.
5. **Sampling and uncertainty** — Present repetitions, spread and plausible confounders rather than a single best timing. Report individual repeated trials with spread and a justified uncertainty statement, not a cherry-picked best number.
6. **Optional hardware counters** — Interpret available counters cautiously and provide a portable alternative when blocked. Interpret optional counter availability, scaling and multiplexing when present; provide user-space timers and disassembly as accessible alternatives.
7. **Unfamiliar diagnosis** — Choose an intervention that distinguishes branch, cache or translation explanations. Design a second intervention for each diagnosis and explain why an unchanged result may fail to discriminate the alternatives.
8. **Quantitative performance bounds** — Estimate traffic bytes, arithmetic intensity and sustained bandwidth lower bounds under specified assumptions; compare them to AMAT and Amdahl calculations without asserting machine-specific constants.
9. **Timer overhead and controls** — Use a no-work/control run and a sufficiently sized workload to expose timer overhead, background noise and changes to code generation that could invalidate timing.
10. **Interpretation and limitations** — Write a claim/evidence/alternative/limit table across at least two experiments and propose an observation that would overturn the favored hypothesis.

*Optional formative feedback:* Before observing timings, write competing hypotheses with predicted discriminators and a correctness oracle, then critique confounding variables.

### Module 7 — Cache/TLB Simulator and Independent Defense

#### Outcomes

- SYS1-O5
- SYS1-O6
- SYS1-O9
- SYS1-O10
- SYS1-O11

#### Lessons

1. **Behavior contract** — Specify trace syntax, cache geometry, errors and independent expected output. State address radix and width, grammar, supported cache/TLB geometry, permissions, policy, counters, reset semantics and deterministic errors.
2. **Core cache simulator** — Implement state, indexing, replacement, stores and eviction counters. Validate nonzero power-of-two parameters and overflow-safe capacity computation before allocating; specify a single-byte access for baseline trace semantics.
3. **Translation trace model** — Add a bounded TLB/page-table fixture model or an explicitly separate translation component. Implement a separately configurable page-table/TLB model with access-denied, absent and mapping-change cases; deny a cache access if translation fails.
4. **Negative and golden tests** — Exercise malformed traces, impossible geometry, dirty writeback and hand-computed misses. Use independently hand-solved LRU, dirty eviction, page/permission and malformed-input fixtures, not the program's own counters as oracle.
5. **Comparative experiments** — Explain how line size, capacity and associativity change modeled results. Change only one parameter at a time and predict the model delta before running it; distinguish outputs of model from real cache miss/latency observations.
6. **Independent defense** — Investigate an unseen discrepancy, repair or justify it, and list unsupported hardware features. Apply an unseen trace or parameter and defend a diagnosis with a hand calculation, a falsifying alternative and a reproducible revision if needed.
7. **Independent simulator specification** — Publish testable public input/output formats, treatment of reads and stores, line/way/set capacity, LRU, write-back/write-allocate and TLB fault states before implementation; state what is intentionally excluded.
8. **Invariant-based verification** — Check hits+misses=accepted cache accesses, evictions≤misses and writebacks≤evictions, plus exact independent tiny traces for associativity, dirty state and failed translations.
9. **Unseen scenario review** — Predict one newly supplied trace or performance discrepancy by hand before executing it; explain a correction or bounded uncertainty in a reviewable defense.

*Optional formative feedback:* Exchange an unseen tiny trace, predict outcomes by hand, compare against simulator output and explain or correct any mismatch.

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
  - **Outcomes:** SYS1-O1, SYS1-O4, SYS1-O5, SYS1-O6, SYS1-O9, SYS1-O11.
  - **Work:** Independently investigate a **previously unseen**, small, reproducible instruction/cache/TLB/benchmark scenario, using a reviewer-supplied trace or transparent public generation rule. Predict relevant state and discriminating observations **before** running a simulator or timing fixture; compare at least two plausible explanations, then revise or defend the conclusion with an independent check. The new case must materially differ from the learner's submitted golden examples; no inaccessible hardware counters or secret services are necessary.
  - **Criteria:** The learner reconstructs the relevant instruction/dependency, cache replacement or page-translation facts under a stated model; uses evidence that truly distinguishes or honestly fails to distinguish hypotheses; detects a meaningful edge or violated assumption (for example an ABI preservation mistake, dirty eviction, stale TLB mapping or optimized-away branch). A hand-derived check agrees with the final conclusion or a corrected explanation identifies the remaining uncertainty. Review demonstrates independent understanding rather than copied output or a rehearsed test.
  - **Evidence:** Unseen case and reproduction parameters, ordered pre-observation predictions and observations, hand reasoning and test results as relevant, documented diagnostic decision, corrections/limits and a reviewable written, recorded or live defense.

### Boundary, safety, revisions and independent review

SEF1 owns gate-to-CPU foundations; SEF6 owns C object memory and lifetime correctness; SEF7 owns introductory Unix user-space interfaces. SYS1 deepens real machine execution, ABI interpretation, locality/translation arithmetic and evidence-based performance reasoning. SYS10 owns real kernel trap/translation/scheduling implementation, SYS3 owns concurrent memory-ordering correctness and SYS7 owns deeper production profiling. Hardware cache policy, TLB structure and branch predictors are explicitly model-specific, not universal contracts.

Use only owned bounded fixtures and local processes, never privileged profiling requirements, uncontrolled kernel modification, unsafe C behavior or public network traffic. Textual trace tables are valid accessible alternatives to diagrams. Required work and acceptance criteria are publicly specified and independently reviewable without paid products.

These edits preserve **SYS1-O1–O11** and **SYS1-AS1–AS4** but clarify the evaluation obligations, including independent simulator oracles, an unfamiliar variant, two benchmark mechanism comparisons and minimum repeated observations. Such changes apply only to this source revision: historical learner evaluations must remain identified by their prior contract and must not be retroactively regraded. Required records associate the course and assessment revision, outcome IDs, review decision, evidence and material limitations. The course remains `draft` pending actual learner testing and qualified review; structural checks do not prove educational validity.

### Optional disciplinary references

- [UC Berkeley CS61C course materials](https://cs61c.org/fa26/) and [open notes](https://notes.cs61c.org/) — ISA, processor organization, locality and virtual memory.
- [Carnegie Mellon 15-213](https://www.cs.cmu.edu/~213/) — machine-level programming, optimization and performance.
- [RISC-V ISA specifications](https://docs.riscv.org/) and [ELF psABI](https://riscv-non-isa.github.io/riscv-elf-psabi-doc/) — target-dependent ISA and calling-convention standards.
- [Linux perf-stat](https://man7.org/linux/man-pages/man1/perf-stat.1.html) and [perf_event_open](https://man7.org/linux/man-pages/man2/perf_event_open.2.html) — optional hardware counter limits.

These are review/learning aids, not paid prerequisites or claims of accreditation.
