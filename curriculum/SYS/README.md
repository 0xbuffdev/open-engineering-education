# Program 3 — SYS: Systems Engineering

> [OEE curriculum](../README.md) · [OEE specification](../../spec/README.md) · [Curriculum design guide](../DESIGN-GUIDE.md) · [OEE Workspace](https://github.com/0xbuffdev/oee-workspace)

## Overview

Systems Engineering develops the skills needed to explain how computers execute programs and build reliable infrastructure software. Learners study machine execution and memory, program in Rust with explicit C comparisons, and examine operating-system internals. They then construct concurrent components, network services, recoverable storage engines and small replicated systems. Performance investigations and operational design lead to a defended Rust systems capstone.

SEF supplies the programming foundation. SEF7 covers C/POSIX files, processes, pipes, signals and bounded single-peer loopback networking. SYS1 examines machine execution in greater depth; SYS2 teaches Rust systems programming; SYS10 studies kernel mechanisms. SYS3–SYS8 extend these foundations into specialist work. **No SEF7 outcome or assessment is transferred** to SYS. Each course evaluates its published competencies.

APP courses are not prerequisites for SYS graduation. APP15 may draw on SYS2's Rust foundation where relevant, but its application specialization is optional for SYS learners.

## Prerequisites

Entry requires assessed completion of [Software Engineering Foundations](../SEF/README.md), including **SEF1–SEF11** and the [SEF10 capstone](../SEF/SEF10.md). SEF10 checks assessed completion of its predecessors. SYS1 begins after that decision. Each later SYS course has its own prerequisites in the catalog below; course numbers alone do not determine study order.

Practical work uses nonprivileged Linux, a C compiler, Rust/Cargo and learner-owned synthetic files and processes. A modest single computer is sufficient for the reference exercises. Learners may use a Linux VM and must identify relevant CPU, OS, filesystem and timing assumptions. Real clusters, root privileges, hardware performance counters, public networks and paid clouds are not required. Local experiments and declared models must still meet each course's evidence criteria.

## Program learning outcomes

By the end of the core program, the learner can:

- Trace compiled software through machine instructions, ABI, architectural memory and translation, identifying the limits of microarchitectural models and measurements.
- Implement resource-safe Rust systems components, explain ownership/borrowing and diagnose C/Rust and OS boundary failures.
- Trace kernel traps, scheduling, paging, filesystem/device I/O and protection using reproducible educational OS models.
- Construct and verify concurrent components through explicit synchronization invariants, atomic memory-order reasoning, progress conditions and measured contention.
- Build multi-client network services with framed protocols, bounded state, nonblocking I/O, backpressure, failure handling and graceful shutdown.
- Implement a recoverable single-node storage engine and distinguish write completion, atomic replacement, integrity and durability guarantees.
- Analyze and implement a scoped replicated service with operation identity, consistency semantics, consensus-style log safety, fault injection and crash recovery.
- Profile, instrument and investigate actual systems bottlenecks, disclosing variability, confounders and the limits of any performance claim.
- Defend capacity, availability, security, deployment and incident-response trade-offs under published operational constraints.
- Independently design, implement, verify, measure, operate and technically defend a cumulative Rust systems project against an unfamiliar fault or change.

## Graduate competence and assessment ownership

Each capability is assessed in its owning course. The table points to the required work; course definitions contain the acceptance criteria and evidence. A source artifact may be reused for several assessments when reviewers evaluate each claimed competency separately.

| Graduate capability | Primary owner | Required assessed evidence |
| --- | --- | --- |
| Compiled execution, ABI, cache, TLB and machine reasoning | [SYS1](SYS1.md) | Machine/ABI trace, cache/TLB simulator, controlled measurements and unseen diagnosis (`SYS1-AS1`–`SYS1-AS4`) |
| Rust systems resource ownership and C/Rust comparison | [SYS2](SYS2.md) | Rust contracts, C/Rust behavior, child supervision, integrated Unix utility and unfamiliar repair (`SYS2-AS1`–`SYS2-AS5`) |
| Kernel privilege, scheduling, memory, filesystem and devices | [SYS10](SYS10.md) | Source-grounded kernel traces, scheduler and memory models, file/device pathway and technical defense (`SYS10-AS1`–`SYS10-AS5`) |
| Synchronization, atomic ordering and bounded concurrent progress | [SYS3](SYS3.md) | Synchronization/atomic reasoning, multi-producer/consumer component, contention study and unknown-case defense (`SYS3-AS1`–`SYS3-AS5`) |
| Safe nonblocking multi-client networking | [SYS4](SYS4.md) | TCP/wire contract, real reactor, backpressure/overload tests, operation evidence and fault defense (`SYS4-AS1`–`SYS4-AS5`) |
| Crash-recoverable local storage and integrity | [SYS5](SYS5.md) | Durable format, WAL/replay, indexed segments/compaction, measured Rust engine and recovery defense (`SYS5-AS1`–`SYS5-AS5`) |
| Replication, consistency and partition/recovery safety | [SYS6](SYS6.md) | Client histories, log/election safety, three-node Rust service, adversarial checking and replication study (`SYS6-AS1`–`SYS6-AS6`) |
| Scientific performance diagnosis and observability | [SYS7](SYS7.md) | Controlled loads, CPU/wait profiles, bounded signals, optimization decision and unseen incident (`SYS7-AS1`–`SYS7-AS5`) |
| Capacity, SLOs, safe operations and release judgment | [SYS8](SYS8.md) | Architecture, capacity/recovery model, secure lifecycle, independent readiness review and changed-constraint defense (`SYS8-AS1`–`SYS8-AS5`) |
| Independent cumulative systems integration and graduation defense | [SYS9](SYS9.md) | Separate admission decision, one Rust capstone, failure/capacity work, operator handoff and unfamiliar individual defense (`SYS9-AS1`–`SYS9-AS6`) |

SYS9 evaluates integration and transfer on one cumulative Rust project. Completing it does not establish missing evidence from an earlier course.

## Program completion standard

Graduation requires **two separate reviewed decisions**:

1. Actual assessed completion of **SYS1–SYS8 and SYS10** (or independently approved outcome-equivalent decisions preserving the applicable course/specification revisions). SYS9 admission verifies this evidence **before** beginning the project.
2. Satisfactory evidence for **SYS9's fourteen outcomes and six required assessments**, including a controlled failure demonstration, independently reproducible operation, an unfamiliar engineering challenge and a reviewable technical defense.

A project demo cannot replace missing prerequisite mastery, and attendance, elapsed study time or finished exercises alone cannot establish completion. Prior authentic artifacts may be reused and extended where new criteria genuinely apply; no fabricated review decisions or compulsory recreation of eight unrelated projects.

## Courses

This table is the current SYS core catalog under OEE `v0.2.0`. It follows prerequisite order: SYS10 comes before SYS3; SYS4 and SYS5 can proceed in parallel after SYS3. All ten courses remain educationally `draft`. Durations estimate study effort and do not replace assessed competence.

| Course | Title | Duration | Prerequisites | Kind | Status |
| --- | --- | --- | --- | --- | --- |
| [SYS1](SYS1.md) | Computer Architecture, Memory & Performance | 12–16 weeks | Completed SEF (SEF10) | `course` | Core · draft |
| [SYS2](SYS2.md) | Systems Programming with C & Rust | 16–20 weeks | SYS1 | `course` | Core · draft |
| [SYS10](SYS10.md) | Operating Systems Internals & Virtualization | 16–20 weeks | SYS1, SYS2 | `course` | Core · draft |
| [SYS3](SYS3.md) | Concurrency, Atomics & Memory Models | 14–18 weeks | SYS10 | `course` | Core · draft |
| [SYS4](SYS4.md) | Linux Networking & Services | 14–18 weeks | SYS2, SYS3 | `course` | Core · draft |
| [SYS5](SYS5.md) | Storage Engines & Data Systems | 16–20 weeks | SYS2, SYS3 | `course` | Core · draft |
| [SYS6](SYS6.md) | Distributed Systems | 18–24 weeks | SYS4, SYS5 | `course` | Core · draft |
| [SYS7](SYS7.md) | Performance Engineering & Observability | 12–16 weeks | SYS3, SYS4 | `course` | Core · draft |
| [SYS8](SYS8.md) | Systems Design & Production Engineering | 12–16 weeks | SYS6, SYS7 | `course` | Core · draft |
| [SYS9](SYS9.md) | Systems Engineering Capstone | 18–24 weeks | SYS1–SYS8 and SYS10 | `project` | Core · draft |

```text
SEF10 → SYS1 → SYS2 → SYS10 → SYS3
SYS2 + SYS3 → SYS4, SYS5
SYS4 + SYS5 → SYS6
SYS3 + SYS4 → SYS7
SYS6 + SYS7 → SYS8
SYS1–SYS8 + SYS10 → SYS9
```

## How the courses develop competence

- **Machine, Rust and OS internals (SYS1, SYS2, SYS10):** SYS1 develops ISA/ABI, cache/TLB models and machine evidence beyond SEF. SYS2 is the first *fully taught and assessed Rust foundation*, covering Cargo, ownership, fallible APIs, C/Rust comparisons and multi-child Linux supervision. SYS10 owns kernel traps, scheduling, paging, filesystem/device pathways, protection and virtualization before SYS3 introduces advanced concurrency. Stable IDs indicate course identity rather than study order. No early course silently assumes Rust or kernel internals.
- **Parallel specialist branches (SYS3–SYS5):** SYS3 owns threads, memory ordering, synchronization and progress; SYS4 advances from SEF7 loopback exercises to scalable multi-client protocols and load control; SYS5 owns persistent formats, WAL ordering, indexing, compaction and crash state. SYS4 and SYS5 may proceed in parallel after SYS3.
- **Distributed correctness and performance (SYS6–SYS7):** SYS6 combines networking and storage into bounded replicated systems, client histories, fault models, log safety and recovery. SYS7 is separately available after SYS3/SYS4, measuring real bottlenecks and invalidating performance hypotheses rather than merely optimizing for a score.
- **Production and cumulative defense (SYS8–SYS9):** SYS8 translates known reliability and measurement models into capacity decisions, service operations, release/rollback and incident readiness. SYS9 integrates relevant prior depth in one justified system; it does not demand a feature checklist reproducing every predecessor's final assessment.

Cross-cutting reasoning about security, privacy, accessibility, responsible experimentation and operational safety appears wherever it changes engineering correctness. SYS does not claim to replace a specialist SEC program or APP's application-product specialization.

## Workload and pacing

Adding the published durations gives **148–192 course-weeks**, or approximately **1,480–2,880 focused hours** at 10–15 hours a week. These totals estimate work, not calendar time to graduation. SYS4 and SYS5 can run in parallel after SYS3, and SYS7 can begin after SYS3 and SYS4. SYS6 requires SYS4 and SYS5; SYS8 requires SYS6 and SYS7. Projects, debugging and reviewer feedback may take longer than the estimates. Future revisions should use real learner timing evidence.

The ten courses publish **131 learning outcomes and 51 required summative assessments**. Work may reuse an implementation when each outcome receives an independent assessment decision. Individual course files define the actual Work, Criteria and Evidence.

## Format, readiness and independent study

All ten SYS courses publish `v0.2.0` outcome IDs, module sequences and summative criteria. Source validation checks those contracts; learner-tested effectiveness, formal conformance and professional competence require separate evidence.

All course labels remain **`draft`**. Promotion to `tested` or `verified` follows the learner, feedback and reviewer requirements in [Status Labels](../../spec/status-labels.md). [Conformance](../../spec/conformance.md) is a separate decision. Assessment records identify the applicable source and assessment revision; editing the curriculum cannot automatically change a learner's result.

Every mandatory outcome, assessment and success criterion is published in the course definitions. Any learner may use [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) or a self-controlled environment; no subscription, proprietary grader or hidden paid book is mandatory. Refer to [Course Format](../../spec/course-format.md), [Evidence Rules](../../spec/evidence-rules.md), the editorial [Curriculum Design Guide](../DESIGN-GUIDE.md) and the reproducible [curriculum inventory](../INVENTORY.md).
