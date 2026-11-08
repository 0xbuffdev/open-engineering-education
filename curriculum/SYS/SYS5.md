# SYS5 — Storage Engines & Data Systems

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** SYS2 and SYS3 *(legacy mapping; reconcile before activation)*
**Duration:** 6 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/SYS.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Study persistence, serialization, write-ahead logging, indexing, checksums, storage layout, compaction, and crash recovery. The emphasis is on understanding storage behavior by implementing core mechanisms.

## Learning outcomes

- Explain the main components of a durable storage engine.
- Design persistence formats and reason about recovery after failure.
- Implement core storage mechanisms such as WAL, indexing, and compaction.
- Use checksums and integrity checks to detect corruption.
- Test crash-recovery behavior and prove which writes survive controlled failures.

## Modules

### Module 1 — Persistence & On-Disk Structure

#### Outcomes

By the end of this module, the learner can:

- Explain **Persistence and serialization** in the context of the course.
- Apply **Pages, records, and checksums** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Persistence and serialization** — `lesson`
2. **Pages, records, and checksums** — `lesson`
3. **Checkpoint: storage layout** — `test`
4. **Micro-lab: Design a small on-disk record format and verify corruption detection.** — `lab`

### Module 2 — Write-Ahead Logging & Durability

#### Outcomes

By the end of this module, the learner can:

- Explain **WAL and durable writes** in the context of the course.
- Apply **Crash points and recovery** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **WAL and durable writes** — `lesson`
2. **Crash points and recovery** — `lesson`
3. **Checkpoint: durability guarantees** — `test`
4. **Micro-lab: Inject a crash after controlled write stages and inspect recovery behavior.** — `lab`

### Module 3 — Ordered Storage Structures

#### Outcomes

By the end of this module, the learner can:

- Explain **B-trees and sorted access** in the context of the course.
- Apply **LSM trees and sorted tables** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **B-trees and sorted access** — `lesson`
2. **LSM trees and sorted tables** — `lesson`
3. **Checkpoint: storage-structure trade-offs** — `test`
4. **Micro-lab: Compare lookup/write behavior of tree-like and log-structured designs.** — `lab`

### Module 4 — Compaction & Recovery

#### Outcomes

By the end of this module, the learner can:

- Explain **Compaction and background maintenance** in the context of the course.
- Apply **Checksums, restart behavior, and guarantees** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Compaction and background maintenance** — `lesson`
2. **Checksums, restart behavior, and guarantees** — `lesson`
3. **Checkpoint: recovery reasoning** — `test`
4. **Micro-lab: Verify which operations survive restart under a defined workload.** — `lab`

### Module 5 — Rust LSM Key-Value Store

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Build, crash-test, benchmark, and document the Rust LSM Key-Value Store** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

### Topics

- persistence
- serialization
- page layout
- WAL
- checksums
- B-trees
- LSM trees
- sorted tables
- compaction
- crash recovery
- durability guarantees

### Labs

- page-format experiment
- WAL writer
- checksum verification
- crash-recovery test
- B-tree/LSM comparison

### Substantial course lab

**Rust LSM Key-Value Store**

Required:

- WAL
- sorted tables
- compaction
- checksums
- recovery
- benchmark workload
