# SYS10 — Operating Systems Internals & Virtualization

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** [SYS1](SYS1.md), [SYS2](SYS2.md)
**Duration:** 16–20 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional)

> [Systems Engineering](README.md) · [Course format](../../spec/course-format.md) · [Design guide](../DESIGN-GUIDE.md)

## Overview

This course fills the **operating-systems internals** capability between SYS2's Linux user-space programming and SYS3's advanced concurrent subsystems. SEF7 and SYS2 already teach *using* process, descriptor and OS resource APIs; SYS10 explains how a kernel implements CPU scheduling, address spaces, page faults, file/device I/O, protection and isolation, and how these mechanisms fail. SYS1 provides ISA, cache and virtual address translation models, while SYS2 provides C/Rust low-level reasoning. SYS10 does not reteach their introductory material or introduce a second Rust grammar course.

The reference work uses a readable open **teaching kernel** (such as xv6) with unprivileged QEMU when available, or a portable and explicitly equivalent scheduler/virtual-memory subsystem simulator plus supplied kernel source/trace analysis. Both paths must demonstrate the same kernel transitions, invariant reasoning, invalid states and diagnosis; simulated evidence is never misrepresented as actual Linux kernel behavior. No host kernel modification, root privileges, specialized device, cloud account or paid reading is required. The exit performance is a small defended OS subsystem with a reproducible independent fault or failure analysis.

## Learning outcomes

- **SYS10-O1:** Trace a program through trap entry, system-call dispatch, privilege transition and kernel return using a declared OS model.
- **SYS10-O2:** Explain kernel isolation, resource ownership, protection domains and the distinction between API guarantees and implementation details.
- **SYS10-O3:** Model context switching, scheduling states, fairness, preemption and starvation with independently reproducible traces.
- **SYS10-O4:** Analyze scheduling policies for latency, throughput, priority and bounded progress under specified workloads.
- **SYS10-O5:** Explain page tables, address-space switching, demand paging, copy-on-write, page faults and TLB invalidation beyond SYS1's external translation model.
- **SYS10-O6:** Implement and verify a bounded educational page allocator/replacement or translation subsystem with explicit invariants.
- **SYS10-O7:** Trace file descriptor to VFS, inode, page cache and block I/O paths, distinguishing kernel filesystem guarantees from SYS5 engine-level durability.
- **SYS10-O8:** Explain device interrupts, MMIO, DMA, polling, buffering and asynchronous completion under explicit hardware assumptions.
- **SYS10-O9:** Analyze process isolation, credentials, permissions, namespaces, cgroups and virtualization without asserting containers are security boundaries by default.
- **SYS10-O10:** Identify kernel concurrency hazards around interrupt context, locks, blocking, preemption and deferred work.
- **SYS10-O11:** Interpret a teaching-kernel source/trace and compare its abstractions with Linux without assuming implementation equivalence.
- **SYS10-O12:** Design a safe reproducible educational OS experiment with failure injection, normal/invalid oracles and resource controls.
- **SYS10-O13:** Distinguish scheduling, memory, device, filesystem and isolation failure symptoms in an unfamiliar OS trace.
- **SYS10-O14:** Defend a modeled kernel subsystem or source-level extension by demonstrating correctness, limitations and technical trade-offs.

## Modules

### Module 1 — From Unix APIs to Kernel Mechanisms

#### Outcomes

- SYS10-O1
- SYS10-O2
- SYS10-O11

#### Lessons

1. **Course boundary and history** — Move from SYS2's user-space Rust/POSIX utility to the OS mechanisms that implement protection and resource scheduling.
2. **Kernel and user mode** — Distinguish address spaces, page protections and processor privilege states.
3. **System-call transition** — Trace a user-space wrapper, trap entry, argument validation, dispatch and return on a specified educational architecture.
4. **Interrupts and exceptions** — Compare synchronous faults, external interrupts and normal control flow.
5. **Mechanism and policy** — Separate kernel mechanisms from scheduler, memory and protection policy decisions.
6. **Teaching kernel and Linux** — Read one small educational-kernel trace and label design choices that Linux does not promise.
7. **Safety of experiments** — Use a simulator or unprivileged QEMU guest; never alter the host kernel or real user files.

### Module 2 — Processes, Context Switches and Scheduling

#### Outcomes

- SYS10-O2
- SYS10-O3
- SYS10-O4
- SYS10-O10

#### Lessons

1. **Processes and threads** — Represent runnable state, address-space ownership and kernel stacks in a process table.
2. **Context switch mechanics** — Explain saved registers, kernel entry and why switching is not a normal function call.
3. **Round-robin baseline** — Trace a simple quantum-based scheduler with runnable/blocking events.
4. **Priority and fairness** — Compare FIFO, priority, multi-level feedback and starvation counterexamples.
5. **Preemption and timer interrupts** — Trace what happens when a running thread is interrupted or yields.
6. **Sleeping and wakeup** — Prevent lost wakeups by reasoning about sleep/wakeup ordering and lock discipline.
7. **Scheduler oracles** — Use an independent hand schedule to verify CPU-time, wait and response calculations.
8. **Multicore limits** — Explain load balancing and cache affinity without assuming deterministic Linux scheduling.

### Module 3 — Virtual Memory and Page Management

#### Outcomes

- SYS10-O5
- SYS10-O6
- SYS10-O11

#### Lessons

1. **Address-space maps** — Relate process segments, kernel mappings and permission attributes to runtime behavior.
2. **Page fault path** — Trace invalid, protection, demand-zero and copy-on-write faults as distinct cases.
3. **Physical-frame management** — Model free lists, reference counts and allocation exhaustion.
4. **Replacement decisions** — Compare FIFO, clock and working-set approximations using explicit reference strings.
5. **Page-table lifecycle** — Explain fork/COW, page release and stale mapping hazards.
6. **TLB coherence** — Trace invalidation needs after mapping and permission changes.
7. **Memory pressure** — Discuss swapping, eviction, thrashing and OOM policies without requiring a destructive host stress test.
8. **Memory subsystem simulator** — Implement a bounded translation/fault/replacement component with independently computed oracles.

### Module 4 — Kernel Synchronization and Execution Context

#### Outcomes

- SYS10-O3
- SYS10-O10
- SYS10-O11

#### Lessons

1. **Kernel locks and interrupts** — Distinguish process-context and interrupt-context restrictions; avoid blocking in an interrupt handler.
2. **Critical sections** — Protect run queues and page metadata under concurrent execution assumptions.
3. **Atomic sleep/wakeup protocols** — Show why checking a predicate then sleeping without synchronization loses events.
4. **Deferred work** — Contrast immediate interrupt handling, bottom halves/work queues and safe later processing.
5. **Lock order and deadlock** — Trace kernel lock dependency graphs and a bounded repair case.
6. **Timing and concurrency evidence** — Explain what a deterministic simulator can and cannot prove on multicore hardware.

### Module 5 — Filesystem and Device Pathways

#### Outcomes

- SYS10-O7
- SYS10-O8
- SYS10-O10

#### Lessons

1. **VFS and inode abstraction** — Trace open/read/write from descriptors through file objects to filesystem operations.
2. **Directory and name lookup** — Distinguish namespace path resolution from final inode identity and permissions.
3. **Page cache and writeback** — Explain buffering, dirty pages and writeback scheduling independently of a user-space WAL.
4. **Block I/O scheduling** — Model request queues and completion ordering, identifying persistence boundaries.
5. **Device interrupts** — Trace an interrupt-driven device event to completion notification.
6. **DMA and MMIO** — Explain memory visibility, ownership, IOMMU concepts and device boundary risks without requiring actual hardware.
7. **Crash-sensitive metadata** — Contrast a filesystem journal or copy-on-write update with SYS5's application-level log guarantees.

### Module 6 — Protection, Isolation and Virtualization

#### Outcomes

- SYS10-O2
- SYS10-O9
- SYS10-O11

#### Lessons

1. **Credentials and permission checks** — Trace user IDs, process credentials and permission decisions on protected resources.
2. **System-call attack surface** — Validate untrusted pointers, lengths and capability-sensitive operations in a teaching kernel.
3. **Namespaces** — Explain process, mount and network namespace isolation in a Linux conceptual model.
4. **cgroups and limits** — Differentiate accounting/limiting mechanisms from filesystem or identity isolation.
5. **Containers versus virtual machines** — Compare shared-kernel isolation with hypervisor-enforced guest boundaries and limitations.
6. **Kernel capability model** — Describe least privilege and a safe local scenario where a default isolation assumption fails.

### Module 7 — Educational OS Experimentation

#### Outcomes

- SYS10-O1
- SYS10-O4
- SYS10-O6
- SYS10-O7
- SYS10-O8
- SYS10-O12

#### Lessons

1. **Reproducible reference** — Choose supplied source/trace from a teaching kernel or an openly documented equivalent simulator.
2. **Subsytem contract** — Specify one small scheduler, page replacement or resource-lifecycle change without building a new general OS.
3. **Golden state transitions** — Derive expected process/page/device states by hand before implementing.
4. **Negative and injected faults** — Exercise invalid syscall input, starvation, allocation exhaustion or interrupt/wakeup ordering.
5. **Bounded guest setup** — Record architecture, emulator version, fixtures and unprivileged host constraints.
6. **Source and model correspondence** — Explain where real kernel trace behavior differs from simplified simulation.
7. **Repair and regression** — Address one observed invariant failure without editing the host kernel.

### Module 8 — OS Subsystem Integration and Defense

#### Outcomes

- SYS10-O3
- SYS10-O5
- SYS10-O6
- SYS10-O9
- SYS10-O12
- SYS10-O13
- SYS10-O14

#### Lessons

1. **Trace complete operation** — Follow a supplied operation across entry, scheduling, memory and I/O boundaries.
2. **Implement chosen subsystem** — Deliver one functioning scheduler/page-manager or equivalent teaching-kernel change.
3. **Verify progress and protection** — Test at least one invalid request, resource limit and adversarial schedule.
4. **Cross-layer diagnosis** — Distinguish competing scheduling, page fault, I/O and isolation explanations for an unfamiliar trace.
5. **Independent defense** — Explain invariants, observed behavior, model limitations and a justified correction.

## Completion requirements

The assessments below are required; module demonstrations, optional source reading and small formative checks are not automatic completion gates. A single reviewed OS subsystem or simulator artifact may contribute evidence to several assessments when their correctness conditions differ.

- **SYS10-AS1** — Kernel Transition and Isolation Analysis
  - **Outcomes:** SYS10-O1, SYS10-O2, SYS10-O9, SYS10-O11.
  - **Work:** Explain an actual or supplied educational kernel system-call/interrupt trace and inspect permission/namespace scenarios.
  - **Criteria:** Correct kernel/user transitions, validation and protection reasoning; Linux versus teaching-kernel guarantees distinguished; invalid accesses denied.
  - **Evidence:** Annotated kernel trace, source references, state/permission table and limitations.

- **SYS10-AS2** — Scheduling and Wakeup Model
  - **Outcomes:** SYS10-O3, SYS10-O4, SYS10-O10.
  - **Work:** Implement or simulate scheduling with runnable/blocking events and demonstrate a lost-wakeup or starvation defect and repair.
  - **Criteria:** Independent schedule oracle matches output; policy latency/fairness analyzed; locks, preemption and cancellation assumptions explicit.
  - **Evidence:** Source/simulator, hand schedules, counterexample and repaired tests.

- **SYS10-AS3** — Virtual Memory Model and Recovery
  - **Outcomes:** SYS10-O5, SYS10-O6.
  - **Work:** Implement a bounded page/translation or allocator/replacement model and trace invalid access and copy-on-write cases.
  - **Criteria:** Page/fault results independently calculated; resource reclamation and permissions preserved; invalid/overflow requests rejected.
  - **Evidence:** Source, page-table/frame fixtures, reference-string oracle, negative tests and explanation.

- **SYS10-AS4** — Filesystem and Device Pathway Reasoning
  - **Outcomes:** SYS10-O7, SYS10-O8, SYS10-O12.
  - **Work:** Trace file read/write, caching and device completion in a teaching kernel; test a bounded fault or ordering scenario.
  - **Criteria:** VFS/page-cache/block distinctions accurate; no unsupported durability or DMA claims; failure state observed and explained.
  - **Evidence:** Pathway diagram, source/trace, failure fixture and OS limitations.

- **SYS10-AS5** — Integrated OS Subsystem and Unfamiliar Defense
  - **Outcomes:** SYS10-O1, SYS10-O3, SYS10-O5, SYS10-O9, SYS10-O10, SYS10-O11, SYS10-O12, SYS10-O13, SYS10-O14.
  - **Work:** Deliver one coherent teaching OS/simulator subsystem plus analyze a new scheduling, VM, I/O or protection defect.
  - **Criteria:** Clean rebuild or supplied reproducible trace; independent normal/negative tests; violated invariant isolated; regression and honest model limits.
  - **Evidence:** Executable artifact or educational-kernel source patch, fixtures, expected/observed traces, correction and technical defense.

### Disciplinary and safety boundaries

This course concerns kernel mechanisms, not generic deployment automation. Direct Linux kernel hacking, ring-0 code on the host and driver DMA experiments are unnecessary and unsafe for the baseline. An equivalent educational model still requires source/trace-based reasoning about real protection and OS API boundaries; a simple toy queue with no kernel explanation does not establish the outcome. Further topics such as realtime certified systems, confidential computing, BPF internals, device driver production and formal kernel verification are explicitly outside this core course. SYS3 then specializes in concurrent memory-order correctness; SYS5 in user-space engine durability.

### Reproducibility and review

Provide kernel/emulator or simulator version, source and build commands, synthetic fixtures, independent scheduling/page reference results, fault conditions and observed-versus-expected outcomes. Explain what is modeled versus actually measured and the assumptions needed for correctness. All required evidence must be publicly reviewable without a paid service, with appropriate text alternatives to diagrams and nonprivileged experiments. Assessment decisions reference course revision and outcome/assessment IDs. Preexisting SYS legacy evidence is not silently regraded and this new course remains `draft` pending real learner validation and qualified review.

## Optional disciplinary references

- [ACM/IEEE-CS/AAAI CS2023 knowledge areas](https://csed.acm.org/knowledge-areas/): disciplinary boundaries between architecture, operating systems, systems fundamentals and parallel computing.
- [MIT 6.1810 — Operating System Engineering syllabus](https://ocw.mit.edu/courses/6-1810-operating-system-engineering-fall-2023/pages/syllabus/): a public academic reference for traps, scheduling, virtual memory, filesystems and controlled xv6 kernel laboratories.

These sources inform curricular scope but do not prescribe OEE course packaging, confer accreditation or replace the course's published competence and evaluation rules.
