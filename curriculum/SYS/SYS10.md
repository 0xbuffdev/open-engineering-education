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

**SYS10 supplies the kernel-mechanism understanding required before SYS3's concurrent systems work and later SYS courses.** It begins where [SYS1](SYS1.md)'s externally observable ISA, ABI, cache/TLB and instruction models and [SYS2](SYS2.md)'s assessed C/Rust, file/descriptor and process **user-space** APIs end. Learners trace how a declared teaching operating system implements privilege transitions, system calls, scheduling, locks and wakeups, virtual memory, process protection, file/block pathways, device interrupts and lifecycle failure handling. SYS3 separately owns user-space Rust memory-ordering, non-blocking algorithms, and advanced synchronization; SYS5 later owns application-level storage engines and crash recovery; SYS8 owns production deployment policy.

The reference source is a **public, commit-pinned xv6 RISC-V teaching kernel** or an equivalently readable, version-pinned educational OS. Its small scope is a strength for tracing real kernel source. It is **not Linux**: unmodified xv6 must not be represented as implementing Linux VFS layers, namespaces, cgroup v2, general demand paging/swap, or the optional copy-on-write lab extension. Each lesson and assessed trace therefore distinguishes **(a) observed reference-kernel code and its architectural target, (b) explicitly added teaching extensions or independently specified simulator behavior, and (c) documented modern Linux mechanisms used only for comparison**. An explanatory model is not a measured Linux kernel observation.

**Required path:** Read relevant public kernel source and derive independently checked trace/invariant oracles; implement **one bounded educational scheduler, page-table/physical-frame or replacement subsystem** (or a tightly scoped guest patch) and defend an unfamiliar cross-layer fault. A nonprivileged QEMU guest may provide executable xv6 evidence where supported, but a portable source-grounded simulator plus published kernel source/trace analysis must be able to satisfy the **same learning outcomes and assessment criteria** when a guest cannot run. No learner must compile a Linux kernel, install host kernel modules, run privileged namespaces, manipulate real DMA hardware, use expensive paid cloud hosts or demonstrate a real host crash. Unsafe kernel code is not a prerequisite to complete the simulator route.

**Workload and readiness:** **16–20 weeks** at approximately **10–15 focused hours/week** (160–300 hours) is a provisional allocation for source reading, hand derivations, modeled implementation, failure fixtures, review and revision, not a learning guarantee or completion gate. The five required assessments evaluate separate claims about kernel transitions, scheduling, memory, filesystem/devices and independent subsystem defense, **reusing** source/model artifacts wherever justified. A successful teaching-guest test or structurally valid curriculum is not by itself proof of general Linux correctness or readiness beyond `draft`.

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

### Module 1 — Kernel Organization, Privilege and the System-Call Boundary

#### Outcomes

- SYS10-O1
- SYS10-O2
- SYS10-O11

#### Lessons

1. **Contract from userspace to kernel** — Use SYS2's already-assessed C/Rust process and descriptor APIs as the starting point. For one call, distinguish its language wrapper and POSIX-facing contract from the chosen kernel's actual implementation and processor privilege transitions.
2. **Kernel designs and execution domains** — Compare monolithic kernels, microkernels and a small Unix-like teaching kernel at the mechanism level. Explain where drivers, address spaces and privileged execution reside without implying that one organization is inherently safe.
3. **RISC-V privilege and trap state** — On a declared RISC-V educational target, identify user and supervisor modes, trap vector, saved PC/cause and status fields, and kernel stacks; label machine-mode firmware responsibilities that are not automatically part of the OS.
4. **System-call argument and result path** — Trace a user wrapper through the architecture-specific trap instruction, trampoline or entry code, register preservation, syscall dispatch, checked arguments and return. Give named source locations and state changes rather than treating the call as an ordinary C function.
5. **Synchronous exceptions versus interrupts** — Distinguish an explicit system call, invalid memory access, illegal instruction, timer event and device interrupt by trigger, trap cause and permissible response; classify when execution resumes or a process is terminated.
6. **Safe user-memory access** — Study how kernel code validates and copies from or into user virtual addresses, including bounds, permissions and changed mappings. Reject a caller pointer that happens to be numerically in range but is not valid for the requested operation.
7. **Kernel API boundaries versus implementation** — Contrast a portable API promise with xv6-specific dispatch and Linux-specific implementation details. Explain why the observed path of one reference version is not an ABI guarantee for every kernel.
8. **Provenance of a teaching kernel** — Select a pinned public xv6 RISC-V source revision or an equivalent readable educational kernel and document architecture, branch, trace provenance and which optional lab extensions are installed. Name features absent from the selected baseline rather than silently assuming them.

*Optional formative feedback:* Trace one call's saved registers, checked user pointer and return value against the supplied source; identify a missing permission check before discussing a repair.

### Module 2 — Process Ownership, Context Switches and Scheduling Policy

#### Outcomes

- SYS10-O2
- SYS10-O3
- SYS10-O4
- SYS10-O10

#### Lessons

1. **Process versus kernel thread state** — Model process identifiers, user address spaces, kernel stacks, CPU-local state and scheduling state as separate resources. Compare xv6's process model with Linux task/thread abstractions without claiming identical layout or policies.
2. **Creation, exec and exit internally** — Follow fork/exec/exit/wait as kernel resource and process-table transitions, building on but not retesting SEF7's use of their public APIs. Account for parent/child ownership, exit status, orphans and reaping in the chosen reference.
3. **Runnable, running, sleeping and zombie** — Define a state machine with permitted transitions and one-to-one resource ownership. Produce a negative trace in which a process is scheduled twice or freed before a waiter can observe its result.
4. **Kernel context switching** — Show which registers are saved by trap entry versus by a scheduler context switch, how a per-process kernel stack and scheduler context are used, and why changing tasks does not simply mean calling a different function.
5. **Timer-driven preemption** — Follow a timer interrupt, tick/accounting decision, runnable-state transition and yield/reschedule path. Distinguish timer hardware/firmware behavior from OS scheduling choices on the declared architecture.
6. **Round-robin with independent metrics** — Calculate waiting time, first-response time, turnaround, and CPU service time for a small fixed workload with arrivals, quantum and blocking. Compare exact hand schedules with simulator output.
7. **Scheduling policies and trade-offs** — Contrast FIFO, round-robin, priority and multi-level feedback using the same workload. Demonstrate throughput, latency, starvation and response-time differences without asserting an unqualified universal winner.
8. **Blocking, wakeup and idle execution** — Explain the atomicity needed between releasing a scheduling lock and entering sleep; trace a wakeup race that leaves runnable work blocked. Connect a CPU's idle state to a concrete 'no runnable work' decision.
9. **Multicore run queues and affinity** — Identify the additional coordination required for concurrent scheduling decisions, CPU affinity, load balancing and cache locality. Keep Linux policy details as comparison, not assumptions about single-queue teaching kernels.
10. **Progress and priority assumptions** — Distinguish fairness under a specified runnable selection policy from guaranteed bounded response under arbitrary preemption; document what the chosen workload and scheduler model actually establish.

*Optional formative feedback:* Compute a hand schedule for two CPU-bound tasks and one sleeping task, then expose a counterexample to a lost-wakeup or starvation claim.

### Module 3 — Kernel Execution Context, Locks and Interrupt-Safe Wakeups

#### Outcomes

- SYS10-O3
- SYS10-O10
- SYS10-O11

#### Lessons

1. **Execution context as a restriction** — Differentiate user mode, process-context kernel code, hard interrupt context and deferred work. State which code may sleep, acquire a blocking lock or allocate memory under the selected reference design.
2. **Spin locks and interrupt state** — Trace lock acquisition, interrupt masking where applicable and release on one CPU; explain why a blocking mutex or unbounded wait is inappropriate in hard interrupt context, while details vary by kernel and execution mode.
3. **Critical invariants across CPUs** — Protect a run queue or free-page list with a named invariant and lock; identify the precise reads/writes that must be serialized, not just the presence of a lock variable.
4. **Atomic sleep and wakeup** — Derive a check/lock/sleep/wakeup sequence with no lost-notification gap, including why releasing the lock and becoming non-runnable must form a valid kernel protocol.
5. **Lock ordering and deadlock paths** — Analyze a two-lock dependency graph around scheduler and page metadata. Repair an AB/BA cycle with an explicit lock order or redesign rather than relying on one successful QEMU run.
6. **Interrupt versus deferred completion** — Trace when an interrupt acknowledges a device event, schedules deferred processing and wakes a blocked waiter; separate completion handling from work forbidden in interrupt context.
7. **Per-CPU state and memory ordering limits** — Explain why CPU-local data or disabling local interrupts does not by itself serialize access across cores. Note necessary architecture memory barriers conceptually, reserving user-space atomic litmus and lock-free proof depth for SYS3.
8. **Failure and race evidence** — Use a bounded teaching trace or supplied kernel source to demonstrate an interrupt/sleep ordering defect and a corrected transition; disclose whether the test ran on multiple emulated CPUs or only a single-CPU model.

*Optional formative feedback:* Hand-check a scheduler wakeup while an interrupt races with a state change; prove the repair under stated lock and scheduling assumptions.

### Module 4 — Page Tables, Fault Handling and Copy-on-Write Lifecycle

#### Outcomes

- SYS10-O2
- SYS10-O5
- SYS10-O6
- SYS10-O11

#### Lessons

1. **From SYS1's translations to kernel-owned mappings** — Start from SYS1's external TLB/page-table model and identify what an OS must allocate, map, protect and free. Distinguish user versus kernel mapping policy and memory actually backed by a physical frame.
2. **RISC-V page-table mechanics** — Trace a declared Sv39 virtual address through page-table levels and PTE permission/status bits on a source-pinned teaching kernel; identify user, supervisor, read/write/execute permissions and invalid entries without assuming all possible flags are implemented.
3. **Address-space creation and teardown** — Follow setup of process user mappings, stack/trampoline/trapframe as applicable, and resource release at exit. Establish that no owned physical frame or page-table page is leaked or freed while still referenced.
4. **Fault classification and diagnostics** — Differentiate unmapped address, protection fault, invalid instruction, demand-allocation fault and copy-on-write write fault by access type, PTE state and the implementation's policy; never call every fault a TLB miss.
5. **Zero-fill and demand paging as variations** — Explain lazy allocation through a compact *declared extension/model* and compare with the actual selected kernel revision. Do not assume untouched xv6 includes general Linux demand paging or swap.
6. **Fork versus copy-on-write** — Trace eager-copy fork and copy-on-write as different designs with shared physical-frame reference counts, read-only mappings and a write-fault copy path. Explicitly identify whether COW is an optional lab extension rather than present in baseline xv6.
7. **Permission change and TLB invalidation** — Show why changing a PTE or switching a relevant address-space context may require RISC-V architectural synchronization (such as sfence.vma under appropriate assumptions), without treating one hardcoded TLB flush as platform-universal.
8. **Kernel-to-user copy under faults** — Analyze copyin/copyout across a page boundary, invalid user pointer or partial buffer; identify what is validated and how failed copy is returned without interpreting the pointer as a trustworthy kernel address.
9. **Independent page-fault oracles** — Hand-derive successful translations and at least three failures for a bounded page-table fixture; distinguish a simulator's declared simplifying assumptions from actual RISC-V and Linux behavior.
10. **Correctness under repeated faults** — Challenge duplicate mapping, a second COW write, frame exhaustion and process exit during shared-frame ownership. Record an invariant-preserving or bounded-rejection outcome for every case.

*Optional formative feedback:* Derive a parent/child COW reference-count trace and an invalid-store fault; identify exactly which steps are a teaching extension and not an unmodified xv6 guarantee.

### Module 5 — Physical Frame Allocation, Reclamation and Memory Pressure

#### Outcomes

- SYS10-O5
- SYS10-O6
- SYS10-O10
- SYS10-O12

#### Lessons

1. **Physical versus virtual page ownership** — Distinguish a free physical frame, a page-table mapping to that frame and the kernel allocator's metadata; draw valid ownership/reference states across allocation, mapping and release.
2. **Free-list allocator invariant** — Specify a bounded physical-frame allocator with unique free/owned membership, legal range/alignment and no duplicate allocation. Trace allocation and deallocation under an independent initial-state fixture.
3. **Reference counting and shared frames** — Model pinned/shared COW frames, underflow/overflow protection, last-owner reclamation and a failed allocation while existing references remain. Explain that an accurate reference count needs synchronized lifecycle updates.
4. **Replacement-policy models** — Compare FIFO and clock/second-chance under identical reference strings, tracking frame identities, dirty/accessed bits and accepted eviction decisions. State that this is a *model*, not an unmodified xv6 swap implementation.
5. **Kernel memory pressure and faults** — Explain reclaim, eviction, swap, working-set pressure and out-of-memory policies using explicitly named Linux or teaching-model assumptions; a VM simulator's simulated OOM is not an observation of host Linux OOM killer policy.
6. **Mapping changes and stale references** — Connect free/reallocate decisions with page-table invalidation and outstanding readers; show why a freed frame must not be exposed to a second process through a stale mapping.
7. **Checked resource geometry** — Reject zero-frame pools, invalid frame numbers, impossible page sizes, duplicated free-list entries and capacity arithmetic overflow before mutating model state.
8. **Concurrent allocator limits** — Apply kernel lock discipline to a free-list transition and model a competing allocation, while leaving comprehensive user-space atomics and concurrent queue formalization to SYS3.
9. **Independent negative verification** — Derive allocator and replacement outputs by hand, then compare with executable simulation or a small educational-kernel extension; include double-free, exhaustion, reference leak and recovery cases.

*Optional formative feedback:* Use a four-frame model with one shared frame to prove free-list uniqueness and refcount correctness before/after a failed allocation.

### Module 6 — Open Files, Filesystem Pathways and Crash-Sensitive Buffering

#### Outcomes

- SYS10-O2
- SYS10-O7
- SYS10-O10
- SYS10-O11

#### Lessons

1. **Descriptor to kernel file object** — Translate a SYS2 user-space open/read/write example into the kernel-owned descriptor table, shared open-file description, offset, permission and final release path; identify which OS structures implement each guarantee.
2. **Inodes, directories and path resolution** — Trace a controlled pathname through directory entries, inode lookup and permission checks, distinguishing name identity from opened-object identity. Keep path-race and symlink claims explicitly within the chosen kernel's policy.
3. **Teaching FS versus Linux VFS** — Show xv6 file-table, inode and buffer-cache paths beside **Linux** VFS objects such as superblock, dentry, inode and struct file. Do not assert that xv6 implements Linux's VFS layering or identical inode/journal semantics.
4. **System-call read/write to block requests** — Trace an application syscall to kernel file object, filesystem offset/blocks, cache lookup, device queue and return, including short I/O and errors without claiming a return necessarily means durable media state.
5. **Buffer cache and dirty state** — Identify cache ownership, dirty buffers, eviction rules and writeback lifecycle in a named implementation; distinguish the Linux page cache from an xv6 block buffer cache and from a SYS5 application buffer.
6. **Filesystem crash consistency** — Study a toy journal/commit record or write-ordering trace and identify a crash between metadata/data stages. Explain the limits of the selected teaching implementation and do not confuse a filesystem journal with SYS5's application-level WAL.
7. **Open and unlink lifetimes** — Trace a file open while a directory entry is removed, accounting for reference counts, inode reclaim and permission/namespace behavior under the chosen model.
8. **Durability boundaries** — Distinguish user write completion, library flush, kernel cache, file sync, directory metadata sync, block-device acknowledgment and power-loss assumptions; never promise persistence solely from a successful write.
9. **Pathway failure fixture** — Independently hand-derive expected states for missing inode, invalid offset, read past EOF, unavailable block or injected writeback failure and compare with one reproducible source/trace model.

*Optional formative feedback:* Follow one byte write from SYS2 File through a named teaching FS and show exactly where Linux VFS comparison is conceptual rather than the same code path.

### Module 7 — Device Registers, Interrupts and Asynchronous I/O

#### Outcomes

- SYS10-O1
- SYS10-O8
- SYS10-O10
- SYS10-O11

#### Lessons

1. **Polling and interrupt delivery** — Compare busy polling, interrupt notification and asynchronous I/O completion in a bounded device model. Account for CPU work, device state and which participant owns the in-flight request.
2. **Device registers and MMIO** — Explain control/status registers mapped into CPU address space, ordering and volatile device access conceptually; distinguish MMIO from regular cacheable RAM without writing unsafe host device code.
3. **Interrupt controller and acknowledge path** — Trace device event, interrupt-controller routing, trap entry, source identification, acknowledgement, deferred handling and wakeup; state which steps vary between xv6's emulated device and Linux drivers.
4. **Request, queue and completion state** — Specify an I/O request state machine with enqueue, in-flight, completed, failed and canceled states, making duplicate completion and resource reuse invalid under a declared policy.
5. **DMA and address domains** — Differentiate CPU virtual, physical and device/bus/DMA addresses, and why an IOMMU or mapping API may be necessary; reject the claim that a device can dereference an arbitrary user pointer as a DMA address.
6. **DMA coherence and memory visibility** — Explain streaming versus coherent mapping assumptions and needed synchronization, including why a CPU cache barrier does not universally replace DMA mapping or ownership transitions. No actual device-DMA operation is required.
7. **Block device buffering and ordering** — Follow a sample block request through guest driver, emulated device and completion, distinguishing read completion, write acknowledgement, flush/barrier and what the declared storage device promises.
8. **Safe failure and ordering analysis** — Inject a delayed or duplicate interrupt, failed request, disconnected device or incomplete DMA transfer into a small simulator; identify which waiters remain blocked and how the state machine recovers or refuses further work.

*Optional formative feedback:* Reconcile an I/O-completion interrupt that arrives after cancellation with request identity, ownership, buffer state and a valid single completion report.

### Module 8 — Permissions, Namespaces, Resource Control and Virtualization

#### Outcomes

- SYS10-O2
- SYS10-O9
- SYS10-O11
- SYS10-O13

#### Lessons

1. **OS protection domains and credentials** — Describe user/kernel separation, process identity, credentials and access-control checks on a named filesystem or syscall path. Analyze an invalid request that crosses an unprivileged boundary and why the kernel must reject it.
2. **Least privilege and capability reasoning** — Compare a coarse root/user distinction with scoped Linux capabilities, and document how dropping one privilege affects the allowed operation. Keep demonstrations theoretical or nonprivileged where required.
3. **PID, mount and network namespaces** — Model what identity, filesystem view and network namespace isolation change or do not change in Linux. Explicitly state that unmodified xv6 has no Linux namespace implementation.
4. **Cgroups and resource accounting** — Explain how a Linux cgroup v2 controller can account for or limit CPU/memory/pids under a declared configuration, and why a controller is not itself an authentication or confinement security boundary.
5. **Container composition and escape assumptions** — Distinguish namespaces, cgroups, filesystem mounts, seccomp and Linux capabilities as separable pieces; identify how containers share the host kernel and why 'runs inside a container' is not a proof of isolation.
6. **Virtual machines and hypervisors** — Compare guest kernel, hypervisor and host execution domains; contrast emulated hardware with hardware-assisted virtualization and the independence of guest memory/protection from container namespace mechanisms.
7. **Nested trust boundaries and IOMMU** — Explain guest virtual versus guest physical and host physical addresses in a simple two-stage translation/IOMMU model. Do not claim that adding a virtual machine automatically secures every device or side channel.
8. **Threat and denial cases** — Solve a small scenario involving privilege escalation attempts, out-of-range user pointers and resource exhaustion; identify the responsible layer and show the required denied/limited behavior without exploit execution.
9. **Document exact version and missing features** — Publish a two-column table separating *source-observed xv6* behavior from Linux namespace/cgroup/VFS/hypervisor documentation and explicit simulations; reject translating one platform's API names into equivalence without source evidence.

*Optional formative feedback:* Given a proposed container sandbox, identify one boundary enforced by namespaces, one by cgroups, and one property that still depends on the shared host kernel.

### Module 9 — Reproducible Educational-Kernel Investigation and Validation

#### Outcomes

- SYS10-O1
- SYS10-O4
- SYS10-O6
- SYS10-O7
- SYS10-O8
- SYS10-O11
- SYS10-O12

#### Lessons

1. **Select a source-pinned, safe reference** — Use publicly available xv6 RISC-V source and a specified unprivileged QEMU release, or an equivalent reproducible educational kernel source/trace combined with a portable, bounded simulator. Document exact commit, version, architecture and optional applied lab features.
2. **One coherent subsystem contract** — Select a scheduler/wakeup, physical-page allocator/replacement or translation subsystem with a small public state machine, invariant, input grammar and expected outputs; resist building a whole new OS as an unrelated capstone.
3. **Source-to-model traceability** — Annotate at least two actual source paths explaining entry to the subsystem and its cleanup/error exit, and map which operations the simulator intentionally omits. Use source excerpts when running a guest is unavailable.
4. **Independent hand-derived oracles** — Construct normal, boundary and invalid traces and calculate resource/scheduler state independently of the implementation, including a failure transition and recovery or bounded rejection.
5. **Kernel-specific versus simulated fixtures** — Declare whether each result came from an actual guest run, a fixture or educational model, and explain why a simulated kernel trap does not prove Linux kernel behavior.
6. **Failure injection without host risk** — Use isolated guest state or synthetic state transitions to test invalid pointers, deadlock/lost wakeup, frame exhaustion and incomplete I/O. Never require root, real-device DMA, raw disk writes or host kernel modifications.
7. **Accessibility and resource economy** — Provide deterministic text tables/diagrams, limits on CPU/memory/time, fixed inputs and build scripts or public read-only source references; preserve the same outcome contract for users without QEMU-capable hardware.
8. **Regressions and alternative hypotheses** — Reproduce a deliberately flawed subsystem transition, change the smallest required condition and run a previously correct case alongside the negative test; disclose configurations not explored.

*Optional formative feedback:* Compare a source-level kernel trace with a simulator event timeline, explaining the one missing intermediate state that matters for correctness.

### Module 10 — Integrated OS Mechanism, Cross-Layer Diagnosis and Defense

#### Outcomes

- SYS10-O1
- SYS10-O3
- SYS10-O5
- SYS10-O6
- SYS10-O9
- SYS10-O10
- SYS10-O11
- SYS10-O12
- SYS10-O13
- SYS10-O14

#### Lessons

1. **Build on prior verified work** — Reuse the source-pinned subsystem or model implemented for AS2/AS3 rather than demanding an unrelated second kernel extension; add a small interaction with scheduling, page faults, protection or I/O as relevant to the selected design.
2. **Cross-subsystem causal graph** — Track one bounded operation through trap, runnable/blocking state, memory translation and file/device or permission events as applicable. Label source-grounded and simulated edges and explain what the OS actually guarantees.
3. **Work and failure invariants** — State a primary safety invariant, one relevant progress/resource policy and a protection denial condition; verify that invalid, duplicate or canceled events do not leave an unrecoverable unowned resource.
4. **Adversarial case generation** — Accept a reviewer-supplied unseen scheduling, memory, filesystem, device or isolation failure or a public deterministic seed with materially new transitions; explain two competing causes before running the model.
5. **Minimal fix and regression** — Produce one independently reviewed change to a simulator or educational-kernel subsystem and re-check both a previously correct trace and an independently computed failure oracle.
6. **Performance and policy trade-offs** — Defend a bounded scheduling quantum, page-policy or buffering trade-off using transparent workload assumptions; distinguish simulated resource costs from host Linux timing or physical hardware observations.
7. **Reproducible handoff and defense** — Provide build/run commands, source revision, fixture inputs, expected and actual traces, known limits, an accessible narrative and a written, recorded or live technical defense in which the learner answers an unfamiliar variant.

*Optional formative feedback:* Reason from a newly supplied trace back to a violated kernel invariant, name a second plausible cause, and propose a discriminating observation before modifying the subsystem.

## Completion requirements

**Five summative assessments are required** and collectively establish **SYS10-O1–SYS10-O14**. Each has public Work/Criteria/Evidence and a separately inspectable decision; reading lists, formative traces, guest setup and optional experiments are not hidden completion gates. The **same one bounded educational subsystem/model** may support AS2's schedule or AS3's allocator/translation evidence and AS5's integration and defense where its behavior genuinely establishes the distinct criteria. No second full OS, Linux kernel patch, live device driver or privileged host environment is required.

- **SYS10-AS1** — Kernel Entry, Source Provenance and Protection Trace
  - **Outcomes:** SYS10-O1, SYS10-O2, SYS10-O9, SYS10-O11.
  - **Work:** Choose a public, source-pinned kernel/target and trace **two different kernel entries**: a valid system call with inspected user argument transfer and a rejected memory/protection request, or an interrupt/exception with equivalent protection evidence. Annotate saved execution state, privilege transition, checked kernel objects and return/termination conditions. Compare one actual source-backed teaching-kernel path with a documented Linux namespace, credential or protection mechanism without claiming code equivalence.
  - **Criteria:** Each trace identifies its kernel version and real source/trace points, the architecture-specific entry and privilege boundary, owned process/address-space state, validation decisions, and precisely which outcome is allowed or denied. Distinguish a system call from an exception/interrupt, distinguish checked user pointers from raw virtual-address arithmetic, and distinguish xv6-only mechanisms from Linux credential/namespace/cgroup guarantees. The student can predict one invalid case before executing it and defend a bounded explanation of what the reference evidence does **not** establish.
  - **Evidence:** Source revision and independently reproducible excerpt/path references, annotated call/exception tables, register/state and protection maps, known-good and denied-access fixtures, source-versus-Linux comparison and limitations.

- **SYS10-AS2** — Process Scheduling, Context-Switch and Wakeup Investigation
  - **Outcomes:** SYS10-O3, SYS10-O4, SYS10-O10, SYS10-O11.
  - **Work:** Specify a bounded educational runnable/sleeping/exit state machine and **at least two contrasting scheduler policies** (such as FIFO versus round-robin) under a fixed, small workload; implement or simulate scheduler transitions with a source-pinned kernel correspondence. Add an independent lost-wakeup, lock-order or starvation counterexample that exercises kernel execution context, and demonstrate a principled repair or explicitly bounded refusal.
  - **Criteria:** Hand-derived event schedules agree with actual model output for arrival, run, block, wake, exit and resource reaping; waiting, response and turnaround calculations use a declared clock and assumptions. Policy comparisons are based on the same workload; starvation/liveness conclusions are properly qualified by scheduler fairness and resource budgets. The lock/interrupt/sleep sequence states its actual execution context, never performs an unjustified blocking wait in a hard interrupt handler and eliminates the demonstrated unsafe transition without guessing from one passing test.
  - **Evidence:** Versioned scheduler/source model, state-transition diagram, two independently derived policy schedules and metrics, failing wait/lock history, corrected case with reproducible positive/negative results and a source correspondence explanation.

- **SYS10-AS3** — Page Tables, Frame Ownership and Memory Failure Model
  - **Outcomes:** SYS10-O5, SYS10-O6, SYS10-O10, SYS10-O12.
  - **Work:** **Implement** a bounded educational virtual-page/physical-frame allocator, translation, reference-counting or page-replacement subsystem (which may be the same reusable code used by AS5). Publish the target architecture, page geometry, PTE/permission model, frame ownership and fault/reclaim policy; independently calculate page/owner states for a valid access, a protection/unmapped fault, an exhaustion/invalid-free case and a fork/COW or mapping-invalidation example. Label demand paging, COW and swap as explicitly added extensions where absent from the reference kernel.
  - **Criteria:** Allocated frame identity and reference accounting remain valid (no duplicate free-list membership, double free, invalid reuse or unchecked capacity overflow); invalid mapping/permission requests fail predictably and do not corrupt existing state. Exact hand-derived translation/fault/replacement results agree with the model for normal, invalid and recovery cases, including a correctly identified TLB invalidation precondition under the declared architecture. The learner identifies what an xv6 source path actually implements, what is synthetic/extended and how kernel concurrency rules protect relevant allocator state. A simulator is acceptable only with real source-linked reasoning, not as an unlabelled Linux observation.
  - **Evidence:** Implemented subsystem source and clean build/run commands, public model schema/invariants, independent page tables/free-list/reference fixtures, before/after ownership traces, invalid/fault tests and revision-pinned source-versus-model limitations.

- **SYS10-AS4** — Kernel File, Device and I/O Completion Pathway
  - **Outcomes:** SYS10-O7, SYS10-O8, SYS10-O10, SYS10-O11, SYS10-O12.
  - **Work:** Follow **one file operation and one device completion** through a specified source-pinned educational kernel or supplied real kernel excerpts, drawing kernel-owned object lifetimes and buffer/request states. Compare the teaching file/inode/buffer path with documented Linux VFS and page-cache abstractions; apply a bounded device interrupt, block-write completion, failed I/O or delayed notification fixture. Explain an MMIO/DMA/address-space condition where relevant without requiring actual device access.
  - **Criteria:** The learner differentiates descriptor/file object, inode/path identity, teaching block buffer versus Linux VFS/page cache, and application write versus cache/writeback/durable acknowledgment under named assumptions. The device trace correctly distinguishes interrupt entry, acknowledgement, deferred work, request completion and wakeup; invalid/delayed/duplicate completion cannot silently release a resource twice. CPU virtual/physical and DMA/bus/IOMMU addresses are not conflated; driver/caching claims match the chosen source and documented platform rather than importing unsupported Linux features into xv6. Normal and injected failure expected results are independently derived.
  - **Evidence:** Reproducible source references, both annotated cross-layer timelines, state/ownership table and cache boundary notes, synthetic I/O failure inputs with expected versus observed results, Linux comparison and safety limitations.

- **SYS10-AS5** — Integrated Educational OS Mechanism and Unfamiliar Fault Defense
  - **Outcomes:** SYS10-O1, SYS10-O3, SYS10-O5, SYS10-O6, SYS10-O9, SYS10-O10, SYS10-O11, SYS10-O12, SYS10-O13, SYS10-O14.
  - **Work:** Reuse the reviewed educational scheduler or memory subsystem from AS2/AS3, extending or explaining **one meaningful interaction with another kernel mechanism** (trap, preemption, page fault, device wakeup or protection). Independently analyze a **previously unseen**, small, source-consistent failure scenario supplied by a reviewer or public reproducible generation rule. Before execution, identify **two plausible causes** and a discriminating event/ownership trace; make one justified correction or bounded refusal and rerun both the challenge and a previously correct case.
  - **Criteria:** The implementation/source model rebuilds or the supplied source-grounded trace is independently reproducible without paid hardware, privileged host modifications or an entire guest OS rewrite. The cross-layer graph explains a legal event sequence, identifies the first violated safety/progress/protection invariant, distinguishes scheduler, VM, filesystem/device and isolation explanations, and confirms a correction with an independently derived oracle. Review defends ownership, exact environment, source provenance, limits of simulation, fault injection and trade-offs, not just a copied lab result. Earlier assessments need not be reimplemented; demonstrated new understanding and unknown-case transfer are required.
  - **Evidence:** One reusable subsystem or source-backed extension, pinned versions/commands and fixture seeds, cross-layer state diagram, unseen scenario with pre-observation hypotheses, independently solved expected output, minimal patch or rigorously reasoned alternative, regression trace and a written, recorded or live technical defense.

### Scope, safe study and historical evidence

A kernel mechanism is not a user-space Rust application API and not automatically a Linux implementation detail. [SYS1](SYS1.md) owns architectural execution and abstract translation; [SYS2](SYS2.md) owns safe Rust, Unix process/resource APIs and C/Rust contracts; [SYS3](SYS3.md) owns user-space concurrent algorithms and atomic memory ordering; [SYS5](SYS5.md) owns application-level durable engines and crash recovery; [SYS8](SYS8.md) owns production operational practice. SYS10 instead establishes source-grounded kernel traps, scheduling, virtual memory, kernel context locks/wakeups, file/device pathways and isolation models.

Default exercises are unprivileged, local and synthetic. A source-pinned xv6 guest is an optional implementation route, but never the **only** route to demonstrate the specified kernel mechanisms: reading public source and implementing a bounded model with independent tests remains valid. Kernel traces from unmodified xv6 must not be misrepresented as evidence that it implements Linux VFS, cgroups, namespaces, COW without the extension, general lazy paging or real device DMA. No experiment may overwrite real block devices, modify a running host kernel or require real exploit code. Source/trace tables and text diagrams are valid alternatives to graphical visualizations.

Assessment decisions record the course/spec revision, actual source/guest/model version, assessable outcome and assessment IDs, learner artifacts, reviewer decision and explicit limitations. Changes preserve the fourteen `SYS10-O1–SYS10-O14` and five `SYS10-AS1–SYS10-AS5` identities while strengthening evidence and correctness criteria **for this revision only**; past learner reviews must be interpreted against their original contract and are not automatically regraded. This course remains `draft` until actual learner testing and independent review establish status readiness.

## Optional disciplinary references

The following are open study references, not compulsory paid readings, hidden tests or proof of institutional equivalence:

- [MIT 6.1810 operating systems course](https://pdos.csail.mit.edu/6.S081/2026/schedule.html) and [xv6 RISC-V source/book](https://pdos.csail.mit.edu/6.S081/2025/xv6/book-riscv-rev5.pdf) — real traps, context switches, page tables, locks, memory and filesystem teaching-kernel observations; learners must pin the actual source revision they use.
- [MIT xv6 copy-on-write lab](https://pdos.csail.mit.edu/6.S081/2026/labs/cow.html) — an **extension** with tests, not a feature to assert exists in an unmodified teaching kernel.
- [Linux kernel VFS overview](https://docs.kernel.org/filesystems/vfs.html) — the Linux dentry/inode/file and filesystem interface model distinct from xv6's simpler file/buffer structures.
- [Linux cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) — Linux-specific resource controllers and accounting distinct from namespace/process isolation.
- [Linux kernel locking guide](https://docs.kernel.org/kernel-hacking/locking.html) and [DMA mapping guide](https://docs.kernel.org/core-api/dma-api-howto.html) — interrupt-context locking and CPU/device address and ownership constraints.
