## SYS5 — Storage Engines & Data Systems

**Duration:** 6 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** SYS2 and SYS3

### Overview

Study persistence, serialization, write-ahead logging, indexing, checksums, storage layout, compaction, and crash recovery. The emphasis is on understanding storage behavior by implementing core mechanisms.

### Prerequisites

**SYS2 — Systems Programming with C & Rust**
**SYS3 — Concurrency, Atomics & Memory Models**

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Explain the main components of a durable storage engine.
- Design persistence formats and reason about recovery after failure.
- Implement core storage mechanisms such as WAL, indexing, and compaction.
- Use checksums and integrity checks to detect corruption.
- Test crash-recovery behavior and prove which writes survive controlled failures.


### Modules

#### Module 1 — Persistence & On-Disk Structure



### Module outcomes

By the end of this module, the learner can:

- Explain **Persistence and serialization** in the context of the course.
- Apply **Pages, records, and checksums** in a problem, implementation, experiment, or design decision.

1. **Persistence and serialization**
   - kind: `lesson`
2. **Pages, records, and checksums**
   - kind: `lesson`
3. **Checkpoint: storage layout**
   - kind: `test`

4. **Micro-lab: Design a small on-disk record format and verify corruption detection.**
   - kind: `lab`
#### Module 2 — Write-Ahead Logging & Durability



### Module outcomes

By the end of this module, the learner can:

- Explain **WAL and durable writes** in the context of the course.
- Apply **Crash points and recovery** in a problem, implementation, experiment, or design decision.

1. **WAL and durable writes**
   - kind: `lesson`
2. **Crash points and recovery**
   - kind: `lesson`
3. **Checkpoint: durability guarantees**
   - kind: `test`

4. **Micro-lab: Inject a crash after controlled write stages and inspect recovery behavior.**
   - kind: `lab`
#### Module 3 — Ordered Storage Structures



### Module outcomes

By the end of this module, the learner can:

- Explain **B-trees and sorted access** in the context of the course.
- Apply **LSM trees and sorted tables** in a problem, implementation, experiment, or design decision.

1. **B-trees and sorted access**
   - kind: `lesson`
2. **LSM trees and sorted tables**
   - kind: `lesson`
3. **Checkpoint: storage-structure trade-offs**
   - kind: `test`

4. **Micro-lab: Compare lookup/write behavior of tree-like and log-structured designs.**
   - kind: `lab`
#### Module 4 — Compaction & Recovery



### Module outcomes

By the end of this module, the learner can:

- Explain **Compaction and background maintenance** in the context of the course.
- Apply **Checksums, restart behavior, and guarantees** in a problem, implementation, experiment, or design decision.

1. **Compaction and background maintenance**
   - kind: `lesson`
2. **Checksums, restart behavior, and guarantees**
   - kind: `lesson`
3. **Checkpoint: recovery reasoning**
   - kind: `test`

4. **Micro-lab: Verify which operations survive restart under a defined workload.**
   - kind: `lab`
#### Module 5 — Rust LSM Key-Value Store



1. **Build, crash-test, benchmark, and document the Rust LSM Key-Value Store**
   - kind: `lab`

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

---

