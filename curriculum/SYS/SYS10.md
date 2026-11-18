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

**Required path:** Read relevant public kernel source and derive independently checked trace/invariant oracles; implement **one bounded educational memory subsystem** (frame allocation/ownership, page-table translation or replacement, or a tightly scoped guest patch meeting the same model contract), reason independently about scheduler policies and defend an unfamiliar cross-layer fault. A nonprivileged QEMU guest may provide executable xv6 evidence where supported, but a portable source-grounded simulator plus published kernel source/trace analysis must be able to satisfy the **same learning outcomes and assessment criteria** when a guest cannot run. No learner must compile a Linux kernel, install host kernel modules, run privileged namespaces, manipulate real DMA hardware, use expensive paid cloud hosts or demonstrate a real host crash. Unsafe kernel code is not a prerequisite to complete the simulator route.

**Workload and readiness:** **16–20 weeks** at approximately **10–15 focused hours/week** (160–300 hours) is a provisional allocation for source reading, hand derivations, modeled implementation, failure fixtures, review and revision, not a learning guarantee or completion gate. The five required assessments evaluate separate claims about kernel transitions, scheduling, memory, filesystem/devices and independent subsystem defense, **reusing** source/model artifacts wherever justified. Only the scoped memory-model pathway in AS3 requires a new implemented subsystem; AS2 scheduling may be a fully derived hand-worked or reproducible simulation, and AS5 builds on the same AS3 work. A successful teaching-guest test or structurally valid curriculum is not by itself proof of general Linux correctness or readiness beyond `draft`.

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

### Module 1 — Kernel Boundaries, Traps and System Calls

#### Outcomes

- SYS10-O1
- SYS10-O2
- SYS10-O11

#### Lessons

1. **Userspace contract versus kernel implementation** — Begin with an already assessed SYS2 process/file API, then follow one call to a named kernel implementation. Distinguish ISO C or Rust wrapper behavior, a public syscall contract, the target ISA trap instruction, kernel privilege and internal dispatcher. Correct a trace that treats kernel entry as an ordinary function call.
2. **Source-pinned OS and execution domains** — Pin the exact xv6 RISC-V source/architecture, or another public educational kernel, before attributing any behavior to it. Identify privileged execution, kernel stack, process address space and firmware responsibility; contrast monolithic versus microkernel organization without projecting Linux details onto the selected source.
3. **Trap entry, saved state and return** — For a real reference source path, annotate user/supervisor mode, saved PC/cause/status, registers, checked syscall arguments, trapframe/trampoline where present, dispatcher and return. Independently predict one invalid argument or return-state consequence and check it against the cited source.
4. **Exceptions, interrupts and safe user access** — Classify explicit syscall, protection fault, invalid instruction, timer and device interrupt by initiating event and permitted response. Trace a user-memory copy across a valid and denied mapping, explaining why an in-range numeric pointer cannot replace ownership, access and page checks.
5. **Limits of an observed kernel trace** — Compare a source-backed educational-kernel transition with a documented Linux example and a supplied hypothetical model. Label which observations are implementation details, ISA requirements or API promises, and identify at least one property a user trace or simulator cannot establish.

*Optional formative feedback:* Annotate one successful syscall and one denied user-buffer access with source locations, trap state and an independently reasoned correction to a false assumption.

### Module 2 — Kernel Process Lifecycle, Context Switching and Scheduling

#### Outcomes

- SYS10-O2
- SYS10-O3
- SYS10-O4

#### Lessons

1. **Kernel-owned process and thread state** — Trace the chosen kernel's process table, user mappings, trapframe, kernel stack and scheduler context through allocation and release, distinguishing these resources from a userspace Child handle. Contrast its process representation with Linux task/thread concepts only where public documentation supports the claim.
2. **Fork, exec, exit and wait below the API** — Follow source-backed creation, replacement of address-space image, exit status, zombie retention and final reaping; draw a resource ownership ledger for one parent and child. Diagnose a double release or premature free without repeating SEF7's public fork/exec usage.
3. **Runnable, blocked and terminated state invariants** — Define legal transitions and an atomic run-queue selection obligation for a small kernel scheduling model. Show a counterexample where the same task runs on two CPUs or a blocked task is treated as runnable; disclose whether the reference kernel uses a single or multicore scheduler.
4. **Trap context versus scheduler context** — Trace what a trap saves and what a kernel context switch saves, including the scheduler stack and per-CPU state on the declared target. Explain why a reschedule is not a plain call between user functions and show when a timer event may trigger preemption.
5. **Hand-derived policy comparisons** — Calculate waiting time, response time, turnaround and CPU service for a supplied arrival/blocking workload under FIFO and round-robin, and challenge a priority/MLFQ alternative under explicitly documented assumptions. Compare identical workloads using independently solved schedules, not one policy's self-reported statistics.
6. **Fairness, starvation and preemption limits** — Diagnose a blocked/ready workload with a timer quantum, CPU idling and repeated high-priority arrivals. Distinguish policy fairness from guaranteed bounded completion under adversarial scheduling, resource exhaustion or host preemption; do not label finite simulation runs proof of liveness.
7. **Wakeups as observable scheduling events** — Connect a blocked-task transition and wake event to the scheduler's ready queue and subsequent service without assuming a Linux wakeup implementation. Predict an observable missed-wakeup symptom; develop its lock/atomicity repair in the next module rather than repeating synchronization protocol here.

*Optional formative feedback:* Hand-solve one blocked three-process schedule, then use its state ledger to find a falsely runnable or prematurely reaped process.

### Module 3 — Kernel Locks, Interrupt Context and Wakeup Safety

#### Outcomes

- SYS10-O3
- SYS10-O10
- SYS10-O11

#### Lessons

1. **Execution context and permissible operations** — Distinguish process context, a hard interrupt handler, deferred work and ordinary user mode in the pinned kernel or labeled Linux comparison. Identify which operations can sleep, acquire particular locks or allocate memory under the declared implementation; a generic 'kernel code may block' rule is insufficient.
2. **Spin locks, interrupts and protected invariants** — Derive the critical section needed for a run queue or free-list invariant under one- and multi-CPU assumptions. Trace interrupt masking and spin-lock ownership where implemented and show why disabling local interrupts does not serialize a shared structure across CPUs.
3. **Atomic sleep/wakeup and the lost-wakeup counterexample** — Construct a check/sleep/wake history with a gap that loses a notification, then specify the reference kernel's lock and state-transition protocol that closes it. Verify the corrected schedule with an independent event history, not a successful guest run alone.
4. **Lock order, interrupt completion and deadlock** — Analyze an AB/BA dependency and a device interrupt/deferred wakeup crossing that lock boundary. Identify the first illegal waiting or reentrancy transition and repair ordering or ownership; distinguish an interrupt acknowledgement from a blocked process becoming runnable.
5. **Memory-order and test limitations** — Explain conceptually why compiler and CPU reordering affect kernel lock and device ownership and when a documented architectural barrier is relevant. Use an explicit trace or source annotation rather than inventing a generic barrier recipe; leave Rust user-space atomic litmus and lock-free proofs to SYS3.

*Optional formative feedback:* Given a lock/wakeup trace on two CPUs, identify the first unsound state and derive a corrected sequence under explicit interrupt assumptions.

### Module 4 — Kernel Page Tables, Faults and Copy-on-Write

#### Outcomes

- SYS10-O2
- SYS10-O5
- SYS10-O6
- SYS10-O11

#### Lessons

1. **OS ownership behind virtual translation** — Extend SYS1's already assessed page/TLB arithmetic into kernel allocation, page table installation, permissions and teardown. For a selected Sv39 source path, calculate VPN levels, PTE validity and accessible versus forbidden translations; distinguish specified ISA behavior from teaching-kernel choices.
2. **Process address-space creation and destruction** — Follow kernel source or a declared model for executable mappings, user stack, trapframe/trampoline and free paths where applicable. Draw ownership of page-table pages and mapped frames and identify a leak or stale mapping at process exit.
3. **Fault delivery and policy** — Trace read/write/execute faults, absent mappings and protection failures from trap through kernel decision and resume/termination. Distinguish hardware fault classification from optional OS handling policies such as lazy allocation; do not claim unmodified xv6 implements Linux demand paging.
4. **Fork and copy-on-write variants** — Compare eager-copy fork with an explicitly added COW extension or independently specified model; derive read-only sharing, frame reference-count increments, write-fault copy and last-reference free. Identify where baseline source does not implement the lab extension and test a second write, failure-to-allocate and exit.
5. **Page-table modification and translation synchronization** — Analyze mapping updates, address-space switch and reuse under declared RISC-V assumptions, including when SFENCE.VMA or appropriate cross-hart synchronization is necessary. Explain that speculative/cached translations and permission checks cannot be replaced by a universal 'flush the TLB' slogan.
6. **User buffer validation and fault oracles** — Work copyin/copyout and a request crossing a page boundary with an invalid user pointer or partial result; state exactly which validation is source-observed. Prepare hand-solved normal, unmapped, protection and stale-translation cases before consulting any simulator.
7. **Memory protection and model scope** — Contrast a modeled successful translation, a denied access and a kernel-owned frame whose mapping has changed; demonstrate why one cannot authorize the other. Identify which COW, swap or replacement behavior is a teaching extension and what must be tested later in the independent memory subsystem.

*Optional formative feedback:* Hand-calculate an Sv39 permission failure and a COW shared-frame trace, separating baseline source behavior from a declared lab or simulator extension.

### Module 5 — Physical Frames, Allocation and Reclamation Invariants

#### Outcomes

- SYS10-O5
- SYS10-O6
- SYS10-O10
- SYS10-O12

#### Lessons

1. **Frame identity, free-list and references** — Model the difference between a physical frame, a page-table entry and allocator metadata. Specify unique free/owned membership and legal reference counts; trace allocation, mapping, sharing and release with a deliberately invalid free.
2. **Checked allocator operations and failures** — Implement or inspect a bounded frame allocator state machine that rejects out-of-range, double-free, integer-overflow and exhaustion cases without mutating unrelated state. Independently predict post-failure ownership rather than accepting one clean allocator test.
3. **Shared ownership, COW and safe last-reference free** — Work a reference-counted frame trace that includes last-owner release, underflow, a failed allocation and an outstanding mapping. State who must synchronize updates and why reclaiming a frame before removing or synchronizing mappings violates isolation.
4. **Replacement and working-set policy models** — Compare FIFO and clock/second-chance traces under a small fixed frame budget, with accessed/dirty state, workload choices and legal victim selection. Mark swap/replacement as an explicitly configured educational model or Linux comparison, not a claim about untouched xv6.
5. **Pressure, paging and system-level guarantees** — Differentiate page faults, memory pressure, eligible reclamation, writeback and out-of-memory responses under a specified OS model. Analyze a bounded failure/recovery case and avoid attributing a simulator's OOM decision to the host Linux policy.
6. **Subsystem invariants and independent oracles** — Choose one scoped implementation among allocation/ownership, translation/permissions or replacement, and publish its state-machine contract and implementation-specific invariants. Verify normal and adversarial cases with independent expected state, documenting which mechanisms are only solved by hand or source trace rather than implemented.

*Optional formative feedback:* Derive a four-frame ownership trace with a shared mapping and failed free; identify the first invariant violation without treating a host OOM event as evidence.

### Module 6 — Kernel File Objects, Filesystems and Durability Boundaries

#### Outcomes

- SYS10-O2
- SYS10-O7
- SYS10-O10
- SYS10-O11

#### Lessons

1. **File descriptor to kernel object and lifetime** — Trace a SYS2 user file operation to process fd table, shared open-file description, offsets, permissions and final release in the named teaching source. Compare Linux struct file semantics only as documented and identify a counterexample where a removed pathname is not equivalent to a closed handle.
2. **Path lookup, inode identity and Linux VFS contrast** — Follow directory lookup and inode references through an open and unlink case. Contrast xv6 file/inode/buffer structures with Linux superblock, dentry, inode and struct file without asserting xv6 has Linux VFS or the same symlink and permission policies.
3. **Read/write to buffers and block I/O** — Trace a bounded syscall through file position, inode/block mapping, buffer lookup and a device request/return. Show where short read/write, end-of-file, denied access or I/O error changes the observable result rather than treating every operation as one whole message.
4. **Dirty state, journal and crash ordering** — Analyze a source-supported teaching filesystem log or a declared toy commit/flush sequence with a crash between metadata/data stages. Distinguish block buffer, Linux page cache and application data buffer, and explain why a filesystem journal is not SYS5's application WAL.
5. **Acknowledgement versus persistence** — Differentiate userspace buffering, OS write acceptance, kernel dirty state, file sync, directory entry persistence and device flush under named assumptions. Reject a claim that ordinary write or a simulated journal commit always proves power-loss durability.
6. **Independent filesystem failure path** — Build a source-backed state/ownership table for missing inode, open-unlink lifetime and one injected block or writeback failure. Derive expected behavior before consulting a fixture, and explain which recovery semantics depend on actual journal/device guarantees.

*Optional formative feedback:* Trace one byte write through an actual xv6 source path, then mark where a Linux VFS or crash-durability claim would require different evidence.

### Module 7 — Devices, Interrupts and I/O Completion

#### Outcomes

- SYS10-O1
- SYS10-O8
- SYS10-O10
- SYS10-O11

#### Lessons

1. **Polling, interrupts and request ownership** — Compare bounded polling, interrupt notification and deferred completion for a single guest device. Specify queue, in-flight and owned-buffer state; identify why a request may be waiting despite a ready CPU.
2. **MMIO and interrupt routing** — Trace a named emulated device's control/status access, interrupt-controller route, trap entry, acknowledge and wake-up sequence, separating guest-source behavior from Linux driver variations. Explain why MMIO is not ordinary cacheable RAM and why volatile alone is not a complete synchronization policy.
3. **DMA and distinct address domains** — Distinguish CPU virtual, physical, guest physical and device DMA/bus addresses, including when IOMMU mappings and buffer-ownership transitions matter. Identify an invalid attempt to hand a raw user pointer directly to hardware, without any real DMA demonstration.
4. **Device-visible ordering and buffered writes** — Analyze a small queue descriptor or DMA ownership sequence, specifying coherent versus streaming mapping assumptions and appropriate synchronization. Contrast an acknowledged block request with device flush/persistence guarantees; avoid claiming a CPU fence alone solves every DMA visibility problem.
5. **Cancellation, duplicate completion and recovery** — Construct a request state machine for queued, in-flight, completed, canceled and failed states. Inject one late interrupt, duplicate completion or device error; prove by state/identity checks that a buffer cannot be freed twice or a waiter silently remain blocked.
6. **Source-grounded device observation and limits** — Compare a reproducible source trace and a synthetic failure fixture for the same bounded completion mechanism. State which events were actually observed and which were inferred, and identify one Linux-specific or physical-device behavior that the simulator cannot establish.

*Optional formative feedback:* Reason through a completion interrupt that races with cancellation; specify a single valid report and surviving ownership of each buffer.

### Module 8 — Process Isolation, Resource Control and Virtualization

#### Outcomes

- SYS10-O2
- SYS10-O9
- SYS10-O11
- SYS10-O13

#### Lessons

1. **Privileges, credentials and denied operations** — Use a named kernel or Linux documentation to trace a user/kernel protection decision, permission/credential state and a rejected operation. Contrast actual xv6 mechanisms with documented Linux credential and capability behavior without running a privileged exploit.
2. **Namespaces as scoped views, not full security** — Compare PID, mount and network namespace effects on identity and visibility in a stated Linux process example. Identify shared-kernel operations that namespaces alone do not prohibit, and state explicitly that unmodified xv6 does not implement Linux namespaces.
3. **Cgroup v2 resource policy** — Interpret a declared Linux cgroup v2 CPU/memory/pids example, its accounting/limit response and an overload/denial case. Distinguish resource allocation from authentication and verify which controller behavior the cited Linux documentation actually promises.
4. **Container boundary composition** — Reason about namespace, mount, capabilities, seccomp and cgroup contributions to a bounded service sandbox. Show one bypassable assumption if only a single mechanism is configured; identify which protections still depend on the shared host kernel.
5. **Hypervisors and layered address translation** — Contrast guest kernel, hypervisor, host and hardware protections for a toy virtual machine. Trace guest virtual, guest physical and host physical identity in a declared model, and explain why virtualization is not proof of secure device passthrough or side-channel isolation.
6. **Cross-layer threat and source provenance** — Analyze supplied failed access or resource exhaustion using a comparison table of source-observed teaching-kernel behavior, Linux-documented features and synthetic model states. State exactly which layer should reject the request; do not infer equivalence from similar API names.

*Optional formative feedback:* Given a proposed container or VM sandbox, identify a denied operation, resource-control mechanism and residual shared-kernel or device trust assumption.

### Module 9 — Integrated Educational-Kernel Investigation and Defense

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

1. **One source-pinned investigation contract** — Pin the public educational kernel and selected RISC-V/other target, document absent lab extensions and choose a safe nonprivileged guest or reproducible source-backed simulator route. Reference the real syscall, scheduler and memory pathways studied earlier; no second kernel project or invented Linux implementation is required.
2. **Reuse one implemented memory subsystem** — Extend the already assessed AS3 allocator/translation/replacement implementation with a small, justified interaction with trap, scheduling, protection or I/O. Use AS2's independent scheduling table and AS4's file/device paths as cross-layer evidence where relevant, not as two new full implementations.
3. **Explicit safety, progress and resource claims** — Write one inspectable state contract with ownership invariants, an appropriate progress or fairness assumption, and a denied-access condition for the chosen interaction. Label source-backed transitions separately from simulator assumptions and demonstrate normal, boundary and fault effects with independently hand-derived oracles.
4. **Safe reproducible fault injection** — Use isolated synthetic state, declared deterministic seeds or an optional QEMU guest to introduce a lost wakeup, stale mapping, invalid owner, I/O error or denied privilege. Limit memory, time and permissions, and distinguish actual guest execution from a modeled event without risky host-kernel actions.
5. **Unfamiliar cross-layer differential diagnosis** — For a reviewer-supplied mixed-symptom trace, consider scheduling, memory translation, filesystem, device and isolation hypotheses. For each class, identify a relevant confirming or excluding observation, record predictions before inspection, then select a discriminating test or state why the available evidence is insufficient.
6. **Minimal correction and previously-correct regression** — Repair the first violated invariant in the implemented model or explain a justified bounded refusal when the safe change cannot be established. Re-run both the unfamiliar failure and previously successful fixtures against independent expected states, not the implementation's own output.
7. **Handoff, limitations and independent defense** — Reproduce the same source/model artifact from a clean state with published versions, fixture inputs and bounded run commands. Defend why the chosen subsystem, abstraction boundaries, observed failures and tradeoffs justify the claimed conclusions; avoid presenting a synthetic trace as Linux or real-hardware evidence.

*Optional formative feedback:* Explain an unseen cross-layer failure from its earliest invalid event, defend one competing hypothesis, and verify the repair under a documented source/model boundary.

## Completion requirements

**Five summative assessments are required** and collectively establish **SYS10-O1–SYS10-O14**. Each has public Work/Criteria/Evidence and a separately inspectable decision; reading lists, formative traces, guest setup and optional experiments are not hidden completion gates. The **same one bounded implemented memory subsystem** satisfies AS3's appropriate implementation criteria and is reused in AS5's cross-layer integration. AS2's independently derived scheduler analysis may be performed with hand-worked event schedules or a bounded model; it does not require a second separately implemented kernel subsystem. No second full OS, Linux kernel patch, live device driver or privileged host environment is required.

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
  - **Work:** **Implement one** publicly specified, bounded educational **memory subsystem**: (a) physical-frame allocation/ownership, (b) page-table translation/permissions, or (c) page-replacement/reclamation with owned-frame state. A tightly scoped educational-guest patch is an alternative implementation. Publish its exact input/state contract, source-pinned OS/target correspondence, chosen invariants and explicit model exclusions. Separately hand-derive *common* memory reasoning for a normal mapped access, an absent/protection fault, an exhausted/invalid release case and one COW/shared-frame or mapping-change/invalidation scenario; the teaching implementation need only execute its **chosen** subsystem, not all alternatives. Identify lazy paging, COW and swap as declared extensions when absent from the pinned kernel.
  - **Criteria:** **Common verification:** valid/invalid mapping and fault explanations follow a specified architecture/policy; independent page/owner-state oracles distinguish the modeled transition from kernel-source observation; appropriate translation synchronization and lock/concurrency assumptions are named. **Chosen-subsystem correctness:** a frame allocator prevents duplicate membership, invalid free and reference errors; a page-table implementation rejects unmapped/forbidden/invalidated access without corrupting unrelated state; a replacement implementation makes legal victims, dirty-state and ownership transitions without duplicate release, according to its *declared* model. Apply the relevant invariants **only to the selected implementation**, including checked capacity/overflow and independently reasoned invalid/failure cases. An allocator-only submission need not implement TLB replacement; a translator-only submission need not manufacture a freelist, but all must correctly reason through the common page/fault/ownership cases and identify a source-backed correspondence. The student discloses simulation and reference-kernel limitations and does not claim a toy fault is a measured Linux fault.
  - **Evidence:** One clean-build executable subsystem or scoped educational-guest patch, published schema/invariants, independently solved common memory/fault traces, implementation-specific normal/boundary/invalid fixtures, results and source revision links. Mark which traces were executed in the chosen model versus derived from source or a declared different policy.

- **SYS10-AS4** — Kernel File, Device and I/O Completion Pathway
  - **Outcomes:** SYS10-O7, SYS10-O8, SYS10-O10, SYS10-O11, SYS10-O12.
  - **Work:** Follow **one file operation and one device completion** through a specified source-pinned educational kernel or supplied real kernel excerpts, drawing kernel-owned object lifetimes and buffer/request states. Compare the teaching file/inode/buffer path with documented Linux VFS and page-cache abstractions; apply a bounded device interrupt, block-write completion, failed I/O or delayed notification fixture. Explain an MMIO/DMA/address-space condition where relevant without requiring actual device access.
  - **Criteria:** The learner differentiates descriptor/file object, inode/path identity, teaching block buffer versus Linux VFS/page cache, and application write versus cache/writeback/durable acknowledgment under named assumptions. The device trace correctly distinguishes interrupt entry, acknowledgement, deferred work, request completion and wakeup; invalid/delayed/duplicate completion cannot silently release a resource twice. CPU virtual/physical and DMA/bus/IOMMU addresses are not conflated; driver/caching claims match the chosen source and documented platform rather than importing unsupported Linux features into xv6. Normal and injected failure expected results are independently derived.
  - **Evidence:** Reproducible source references, both annotated cross-layer timelines, state/ownership table and cache boundary notes, synthetic I/O failure inputs with expected versus observed results, Linux comparison and safety limitations.

- **SYS10-AS5** — Integrated Educational OS Mechanism and Unfamiliar Fault Defense
  - **Outcomes:** SYS10-O13, SYS10-O14.
  - **Work:** Reuse the **same AS3 memory subsystem** and source-grounded models from AS1/AS2/AS4, extending it with **one bounded, substantively relevant interaction** with a kernel trap, scheduler, permission or I/O completion pathway. Then analyze a **previously unseen** mixed-symptom case supplied by an independent reviewer or reproducible public generation rule. Before executing the case, classify candidate explanations across **scheduling, virtual memory, filesystem, device and isolation** and specify an observation that supports, excludes or cannot decide each class; identify at least two plausible competing causes and a genuinely discriminating intervention. Implement a justified correction to the chosen model, or give a bounded technical refusal when correctness cannot be established, and recheck a previously correct case. Do not build another complete OS or redo AS1–AS4; those assessments already establish their separate outcomes.
  - **Criteria:** **Transfer/diagnosis (O13):** a source-consistent differential diagnosis distinguishes the relevant kernel failure classes with causal traces, not superficial vocabulary, and records uncertainty when observations do not separate them. Predictions precede observations; the first relevant violated invariant and an alternative cause are explained. **Engineering defense (O14):** the reused subsystem and scoped interaction have a public ownership/protection/progress contract, independently computed normal/negative oracles, reproducible correction (or justified refusal) and regression evidence. The reviewer can examine authorship, why the solution applies only under declared kernel/ISA assumptions, and the evidence limits of simulations, guest execution or Linux comparisons. An unfamiliar trace of just one mechanism cannot silently re-establish O1, O3, O5, O6, O9, O10, O11 or O12; those outcomes retain required decisions in AS1–AS4.
  - **Evidence:** One reused implemented memory subsystem with a source/model cross-layer trace; pinned version, build/run or source-reproduction instructions; an unfamiliar case and all five differential categories with pre-observation predictions; chosen discriminator, expected and observed results, patch or bounded refusal, independent regression case, technical trade-offs and a written, recorded or live defense.

### Scope, safe study and assessment records

A kernel mechanism is not a user-space Rust application API and not automatically a Linux implementation detail. [SYS1](SYS1.md) owns architectural execution and abstract translation; [SYS2](SYS2.md) owns safe Rust, Unix process/resource APIs and C/Rust contracts; [SYS3](SYS3.md) owns user-space concurrent algorithms and atomic memory ordering; [SYS5](SYS5.md) owns application-level durable engines and crash recovery; [SYS8](SYS8.md) owns production operational practice. SYS10 instead establishes source-grounded kernel traps, scheduling, virtual memory, kernel context locks/wakeups, file/device pathways and isolation models.

Default exercises are unprivileged, local and synthetic. A source-pinned xv6 guest is an optional implementation route, but never the **only** route to demonstrate the specified kernel mechanisms: reading public source and implementing a bounded model with independent tests remains valid. Kernel traces from unmodified xv6 must not be misrepresented as evidence that it implements Linux VFS, cgroups, namespaces, COW without the extension, general lazy paging or real device DMA. No experiment may overwrite real block devices, modify a running host kernel or require real exploit code. Source/trace tables and text diagrams are valid alternatives to graphical visualizations.

Assessment decisions identify the source and educational-kernel revision, outcome and assessment IDs, expected versus observed traces, reviewer and model limitations. The course remains `draft` until learner testing and independent review support a status change.

## Optional disciplinary references

The following are open study references, not compulsory paid readings, hidden tests or proof of institutional equivalence:

- [MIT 6.1810 operating systems course](https://pdos.csail.mit.edu/6.S081/2026/schedule.html) and [xv6 RISC-V source/book](https://pdos.csail.mit.edu/6.S081/2025/xv6/book-riscv-rev5.pdf) — real traps, context switches, page tables, locks, memory and filesystem teaching-kernel observations; learners must pin the actual source revision they use.
- [MIT xv6 copy-on-write lab](https://pdos.csail.mit.edu/6.S081/2026/labs/cow.html) — an **extension** with tests, not a feature to assert exists in an unmodified teaching kernel.
- [Linux kernel VFS overview](https://docs.kernel.org/filesystems/vfs.html) — the Linux dentry/inode/file and filesystem interface model distinct from xv6's simpler file/buffer structures.
- [Linux cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) — Linux-specific resource controllers and accounting distinct from namespace/process isolation.
- [Linux kernel locking guide](https://docs.kernel.org/kernel-hacking/locking.html) and [DMA mapping guide](https://docs.kernel.org/core-api/dma-api-howto.html) — interrupt-context locking and CPU/device address and ownership constraints.
