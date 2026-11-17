# Program 3 — SYS: Systems Engineering

> [OEE curriculum](../README.md) · [OEE specification](../../spec/README.md) · [Curriculum design guide](../DESIGN-GUIDE.md) · [OEE Workspace](https://github.com/0xbuffdev/oee-workspace)

## Overview

Systems Engineering is the hardware-near and infrastructure-oriented pathway after **Software Engineering Foundations**. It develops a reliable mental model of actual machine execution and resource behavior; teaches Rust with explicit C/Rust comparison; then examines operating-system internals before building depth in synchronization, networking, crash-durable storage, distributed consistency, performance engineering and production operations. Learners finish with a single reproducible systems project that must withstand controlled failures and an unfamiliar technical challenge.

This program **builds on, and does not re-teach, completed SEF**. SEF1 and SEF6 establish computer and C object-memory foundations; SEF7 assesses single-process POSIX interfaces, pipes, signals, single-peer TCP and one nonblocking loopback connection. SYS1 deepens machine models, SYS2 formally teaches Rust and advanced user-space resource supervision; SYS10 develops kernel scheduling, memory and isolation models before SYS3–SYS9 introduce further specialist engineering judgments. The [SEF7–SYS boundary map](../SEF/UNIX-SYS-BOUNDARY.md) documents historical competence ownership; no SEF7 outcome or assessment is transferred, canceled or retroactively awarded by this SYS migration.

**APP is not a SYS graduation prerequisite.** APP15's optional TypeScript–Rust specialization may use SYS2 competence or equivalent established Rust preparation, but that APP elective is not required here. Each SYS course's direct prerequisites and assessed outcomes are authoritative.

## Prerequisites

**Completed [SEF — Software Engineering Foundations](../SEF/README.md)**, with genuine assessed completion of SEF1–SEF11 under the published SEF graduation rules. SYS1 explicitly starts after SEF10. Later SYS courses require the particular SYS predecessors listed below; these prerequisites are derived from required mechanisms, not a rule that every course must be taken serially.

A **nonprivileged Linux environment** is the reference platform for practical work, together with common open-source C/Rust toolchains and self-created synthetic files and processes. One local computer with modest resources is adequate for most reference tasks. A Linux VM or equivalent isolated environment may be used when available; exact OS, CPU, filesystem and timing assumptions must be recorded where materially relevant. Hardware performance counters, NUMA hosts, public networks, root permissions, real clusters and paid clouds are not required to demonstrate baseline competencies; declared reproducible simulations and controlled local experiments substitute when appropriate.

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

## Program completion standard

Graduation requires **two separate reviewed decisions**:

1. Actual assessed completion of **SYS1–SYS8 and SYS10** (or independently approved outcome-equivalent decisions preserving the applicable course/specification revisions). SYS9 admission verifies this evidence **before** beginning the project.
2. Satisfactory evidence for **SYS9's fourteen outcomes and six required assessments**, including a controlled failure demonstration, independently reproducible operation, an unfamiliar engineering challenge and a reviewable technical defense.

A project demo cannot replace missing prerequisite mastery, and attendance, elapsed study time or finished exercises alone cannot establish completion. Prior authentic artifacts may be reused and extended where new criteria genuinely apply; no fabricated review decisions or compulsory recreation of eight unrelated projects.

## Courses

This is the **authoritative prerequisite-valid core course catalog** for the migrated OEE `v0.2.0` course definitions. All ten courses remain educationally `draft`, regardless of completed source migration. Durations are provisional estimates, not completion thresholds.

| Course | Title | Duration | Prerequisites | Kind | Status |
| --- | --- | --- | --- | --- | --- |
| [SYS1](SYS1.md) | Computer Architecture, Memory & Performance | 12–16 weeks | SEF10 | `course` | Core · draft |
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

- **Machine, Rust and OS internals (SYS1, SYS2, SYS10):** SYS1 develops ISA/ABI, cache/TLB models and machine evidence beyond SEF. SYS2 is the first *fully taught and assessed Rust foundation*, covering Cargo, ownership, fallible APIs, C/Rust comparisons and multi-child Linux supervision. SYS10 owns kernel traps, scheduling, paging, filesystem/device pathways, protection and virtualization before SYS3 introduces advanced concurrency. Stable course IDs are not renumbered. No early course silently assumes Rust or kernel internals.
- **Parallel specialist branches (SYS3–SYS5):** SYS3 owns threads, memory ordering, synchronization and progress; SYS4 advances from SEF7 loopback exercises to scalable multi-client protocols and load control; SYS5 owns persistent formats, WAL ordering, indexing, compaction and crash state. SYS4 and SYS5 may proceed in parallel after SYS3.
- **Distributed correctness and performance (SYS6–SYS7):** SYS6 combines networking and storage into bounded replicated systems, client histories, fault models, log safety and recovery. SYS7 is separately available after SYS3/SYS4, measuring real bottlenecks and invalidating performance hypotheses rather than merely optimizing for a score.
- **Production and cumulative defense (SYS8–SYS9):** SYS8 translates known reliability and measurement models into capacity decisions, service operations, release/rollback and incident readiness. SYS9 integrates relevant prior depth in one justified system; it does not demand a feature checklist reproducing every predecessor's final assessment.

Cross-cutting reasoning about security, privacy, accessibility, responsible experimentation and operational safety appears wherever it changes engineering correctness. SYS does not claim to replace a specialist SEC program or APP's application-product specialization.

## Workload and pacing

The ten provisional durations total approximately **148–192 course-weeks**, or roughly **1,480–2,880 focused hours** at 10–15 hours/week. These are sums of estimated course effort, **not an elapsed-time requirement, guaranteed graduation date or fixed credential threshold**. SYS4/SYS5 and parts of SYS6/SYS7 can overlap where their actual prerequisite dependencies permit, but parallel study does not remove work. Learners may need more time for tooling, mathematical repair, debugging, inaccessible hardware alternatives, project revision and reviewer feedback. Course durations will be recalibrated using genuine learner evidence rather than artificial matching to SEF or APP week counts.

The ten courses currently publish **131 stable learning outcomes and 51 required summative assessment contracts**, not 51 separate final projects. A meaningful exercise may support several outcomes when its criteria independently evaluate them. Course files are authoritative for work, criteria and evidence; this catalog does not duplicate individual assessment briefs.

## Format, readiness and independent study

All ten SYS course sources now use the outcome-driven **OEE `v0.2.0` draft format** with stable IDs, module outcomes and public summative Work/Criteria/Evidence. This is a **source-format migration and editorial realignment**, not a claim of learner-tested readiness, independently established conformance, accreditation or guaranteed employer competence.

Course labels remain **`draft`**. Promotion to `tested` or `verified` requires the learner completions, feedback, revision records and qualified reviewer evidence defined by [Status Labels](../../spec/status-labels.md); conformance is a separate scoped decision under [Conformance](../../spec/conformance.md). Historical SYS learner work must remain interpretable under the course/spec revision that applied at the time. Updated prerequisites, workload and evaluation contracts do not silently regrade or confer new completion credit.

Every mandatory outcome, assessment and success criterion is published in the course definitions. Any learner may use [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) or a self-controlled environment; no subscription, proprietary grader or hidden paid book is mandatory. Refer to [Course Format](../../spec/course-format.md), [Evidence Rules](../../spec/evidence-rules.md), the editorial [Curriculum Design Guide](../DESIGN-GUIDE.md) and the reproducible [curriculum inventory](../INVENTORY.md).
