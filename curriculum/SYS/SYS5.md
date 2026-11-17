# SYS5 — Storage Engines & Data Systems

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** [SYS2](SYS2.md), [SYS3](SYS3.md)
**Duration:** 16–20 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional)

> [Systems Engineering](README.md) · [Course format](../../spec/course-format.md) · [Design guide](../DESIGN-GUIDE.md)

## Overview

Study how a single-node storage engine turns writes into recoverable and verifiable state. SYS2 supplies Rust I/O/resource contracts and SYS3 supplies concurrency invariants. This course owns log ordering, file formats, indexing, immutable segments, compaction, crash injection and evidence-based durability claims. Its cumulative implementation is a **bounded Rust log-structured key-value engine**, not a general SQL database. Prior APP relational modeling is not assumed or re-taught. Use disposable local files and controlled *process-level* failure injection; no raw block device, privileged mount, cluster or paid cloud is required. A simulated crash cannot prove power-loss guarantees for every device or filesystem.

## Learning outcomes

- **SYS5-O1:** Specify read/write/delete semantics, durability assumptions and crash invariants for a bounded single-node storage engine.
- **SYS5-O2:** Design a versioned on-disk record format with bounded encoding, lengths, checksums and corruption behavior.
- **SYS5-O3:** Explain OS buffering, write ordering, file and directory synchronization and the limits of crash-durability claims.
- **SYS5-O4:** Implement and validate append-only logging, WAL replay, truncation and idempotent crash recovery.
- **SYS5-O5:** Analyze page, B+tree and log-structured index trade-offs with explicit workload and access assumptions.
- **SYS5-O6:** Implement sorted-table, in-memory index, immutable-segment and compaction mechanisms with safe replacement rules.
- **SYS5-O7:** Explain tombstones, snapshot/read visibility, stale versions and resource reclamation in a single-node engine.
- **SYS5-O8:** Apply concurrency control to shared engine state and state precisely which transactions/isolation guarantees are and are not provided.
- **SYS5-O9:** Design checksum, length, offset and version checks that prevent silently accepting malformed or torn data.
- **SYS5-O10:** Construct a deterministic crash/fault-injection harness and compare recovered state with an independent oracle.
- **SYS5-O11:** Benchmark read/write/scan/compaction workloads with warm/cold cache caveats and write-amplification metrics.
- **SYS5-O12:** Build an inspectable Rust key-value engine with bounded memory, recovery, maintenance and correct shutdown.
- **SYS5-O13:** Distinguish storage correctness, operational resilience, encryption, permissions and secure erase boundaries.
- **SYS5-O14:** Defend a previously unseen corruption or durability defect with an explicit recovered-state proof and repair.

## Modules

### Module 1 — Storage Contracts and OS Guarantees

#### Outcomes

- SYS5-O1
- SYS5-O3
- SYS5-O13

#### Lessons

1. **From SEF files to persistence** — Distinguish checked file I/O from an engine's consistency and restart contract.
2. **Records and durability** — Define acknowledged write, visible read and expected post-crash state under explicit failure assumptions.
3. **File versus memory** — Trace page cache, user-space buffers, inode metadata and persistence barriers conceptually.
4. **Write ordering** — Explain why operation completion or flush alone may not imply stable storage.
5. **File and directory sync** — Analyze atomic rename, new files and parent directory durability with platform caveats.
6. **Threat and failure boundary** — List power loss, process crash, corrupt bytes and storage-full scenarios without claiming simulation proves hardware.

### Module 2 — Formats, Pages and Integrity

#### Outcomes

- SYS5-O2
- SYS5-O9
- SYS5-O13

#### Lessons

1. **Binary format contract** — Specify magic, version, length, checksum, key encoding and maximum record size.
2. **Variable length and arithmetic** — Use checked offsets and reject truncation/overflow before allocation.
3. **Pages and layout** — Model slotted pages, fixed blocks and alignment trade-offs without requiring raw direct I/O.
4. **Checksums and corruption** — Differentiate accidental corruption detection from malicious tampering or cryptographic authentication.
5. **Format evolution** — Design a compatible reader or a clear migration/rejection strategy for older files.
6. **Golden binary fixtures** — Derive expected bytes independently and test malformed, truncated and bit-flipped examples.

### Module 3 — Logging and Crash Recovery

#### Outcomes

- SYS5-O1
- SYS5-O3
- SYS5-O4
- SYS5-O10

#### Lessons

1. **Append-only log** — Specify atomic record interpretation even when OS writes are split or partial.
2. **WAL-before-data** — Establish ordering rule and acknowledge point for a stated durability guarantee.
3. **Sync discipline** — Test file sync and metadata policy at required transitions, declaring filesystem assumptions.
4. **Replay state machine** — Reconstruct state from valid complete records, ignore or reject a torn tail by a published policy.
5. **Idempotent replay** — Explain repeated restart and replay without double-applying an effect.
6. **Checkpoint and truncation** — Define safe checkpoint publication and log retirement under injected failure.
7. **Fault stages** — Inject failure before append, after append, before sync, after sync and during replacement.
8. **Recovery oracle** — Calculate legal recovered versions from an independent operation history.

### Module 4 — Indexes and Read Path

#### Outcomes

- SYS5-O5
- SYS5-O7
- SYS5-O11

#### Lessons

1. **In-memory index** — Represent key-to-offset and version state under a bounded dataset.
2. **B+tree reasoning** — Trace lookup, insert, split and page cost for a supplied page-oriented tree.
3. **LSM rationale** — Contrast buffering writes in memory and sorted runs with point-lookups and scans.
4. **Bloom filters and limits** — Discuss false positives, size trade-offs and why a filter cannot prove a key exists.
5. **Range scans** — Merge ordered keys across segments while honoring tombstones and snapshot policy.
6. **Read amplification** — Count potential files, seeks, cache effects and lookup work for representative datasets.

### Module 5 — Immutable Segments and Compaction

#### Outcomes

- SYS5-O6
- SYS5-O7
- SYS5-O9
- SYS5-O12

#### Lessons

1. **Memtable flush** — Sort and write a segment with a durable publication protocol.
2. **Sorted-table layout** — Implement index and block metadata for bounded range and point access.
3. **Manifest and generations** — Track active segment versions without exposing partially published files.
4. **Compaction mechanics** — Merge old and new versions and honor tombstone retention constraints.
5. **Reader lifetime** — Protect readers from reclamation of files they still reference.
6. **Interrupted compaction** — Test crash before publish, during rename and after publish with recovery.
7. **Space amplification** — Compare additional writes and peak disk needs for compaction policies.

### Module 6 — Concurrency, Visibility and Resource Limits

#### Outcomes

- SYS5-O7
- SYS5-O8
- SYS5-O12

#### Lessons

1. **Single-writer model** — Select initial serialization constraints and explain where they simplify correctness.
2. **Locking and snapshots** — Use SYS3 invariants to reason about reader visibility during mutation and compaction.
3. **Atomic batch boundary** — Compare multi-key batch semantics with claimed transactional isolation; publish only supported guarantees.
4. **Resource budgets** — Bound memtable, open files, compaction memory, disk growth and work queues.
5. **Partial failures** — Reject out-of-space and permission errors without acknowledging unsafe writes.
6. **Shutdown and restart** — Separate clean flushing from crash recovery and prove read behavior afterward.

### Module 7 — Verification and Performance

#### Outcomes

- SYS5-O3
- SYS5-O9
- SYS5-O10
- SYS5-O11
- SYS5-O14

#### Lessons

1. **Reference-model testing** — Maintain a simple independent in-memory map for operation histories.
2. **Randomized state-machine traces** — Generate deterministic put/get/delete sequences and compare observable results.
3. **Crash sweep** — Inject failure at every chosen commit and publish stage then reopen repeatedly.
4. **Corrupt fixtures** — Flip bits, truncate records and corrupt indices to verify defined failure/recovery behavior.
5. **Workload classes** — Measure sequential/random writes, hot/cold reads, range scans and compaction pressure.
6. **Interpreting benchmarks** — Report cache, hardware, dataset, repetitions, variance and durability mode.
7. **Unknown recovery challenge** — Explain a novel broken manifest or WAL boundary with a minimal reproducer.

### Module 8 — Rust Key-Value Engine Integration

#### Outcomes

- SYS5-O1
- SYS5-O2
- SYS5-O4
- SYS5-O6
- SYS5-O8
- SYS5-O10
- SYS5-O12
- SYS5-O14

#### Lessons

1. **Engine API** — Define bounded get, put, delete and scan behavior with published errors.
2. **Persistence integration** — Combine WAL, memtable, immutable runs, checksums and manifest publication.
3. **Recovery and maintenance** — Demonstrate restart and interrupted compaction under controlled faults.
4. **Workload report** — Evaluate performance under correctness-preserving durable and less-durable modes without conflation.
5. **Technical defense** — Repair an unfamiliar crash state and disclose remaining failure classes.

## Completion requirements

These are the required summative evaluations. Their work may share the same engine artifacts; module practice, reading and self-checks are not separate completion conditions.

- **SYS5-AS1** — Format and Durability Contract
  - **Outcomes:** SYS5-O1, SYS5-O2, SYS5-O3, SYS5-O9.
  - **Work:** Specify a storage API, recovery invariants, binary record format and accepted/rejected bytes; solve write-ordering cases.
  - **Criteria:** Independent record oracle, bounded lengths, correct sync-versus-atomicity distinctions and named filesystem assumptions.
  - **Evidence:** Format specification, fixtures, byte calculations, durability-state diagram and limitations.

- **SYS5-AS2** — WAL and Crash-Recovery Implementation
  - **Outcomes:** SYS5-O1, SYS5-O3, SYS5-O4, SYS5-O10.
  - **Work:** Implement append/sync/replay with deterministic injected crashes around each acknowledgement boundary.
  - **Criteria:** Recovery matches allowed states; no silently committed unacknowledged claim; torn tails treated by explicit policy; repeated replay safe.
  - **Evidence:** Rust source, fault hooks, operation histories, recovered-state oracle and restart logs.

- **SYS5-AS3** — Indexed Segments and Safe Compaction
  - **Outcomes:** SYS5-O5, SYS5-O6, SYS5-O7, SYS5-O8, SYS5-O9.
  - **Work:** Build an indexed immutable segment format, tombstones and compaction with atomic publication/reader policies.
  - **Criteria:** Correct get/scan after updates and deletes; interrupted compaction never makes invalid active data visible; resource bounds and snapshot behavior explicit.
  - **Evidence:** Source, manifest/segment fixture tests, compaction fault traces and correctness rationale.

- **SYS5-AS4** — Reproducible Key-Value Engine and Measurement
  - **Outcomes:** SYS5-O1, SYS5-O4, SYS5-O6, SYS5-O8, SYS5-O11, SYS5-O12, SYS5-O13.
  - **Work:** Integrate engine API, durability, recovery, integrity and measured workloads for local synthetic data.
  - **Criteria:** Clean build; bounded behavior in storage-full/corrupt cases; honest durability level; repeated meaningful benchmark data with limitations.
  - **Evidence:** Runnable source, configuration, model tests, benchmark corpus/results, operator instructions and guarantee table.

- **SYS5-AS5** — Unfamiliar Crash/Integrity Defense
  - **Outcomes:** SYS5-O2, SYS5-O3, SYS5-O5, SYS5-O9, SYS5-O10, SYS5-O12, SYS5-O14.
  - **Work:** Investigate an unknown WAL, version-index or manifest failure and repair or contain it.
  - **Criteria:** Explain exact violated invariant, distinguish data loss from detected corruption, prove correction with independent fault replay.
  - **Evidence:** Failing fixture, root-cause trace, patch, regression tests and defense.

### Storage guarantees and boundaries

Durable acknowledgement depends on a stated write/sync protocol and filesystem assumptions; no single local fsync demonstration guarantees all physical devices survive power failure. Checksums are error detection, not authenticated tamper protection. Full SQL transactions, distributed replication and formal proofs of consensus belong elsewhere. Encryption at rest is not assumed to emerge from Rust ownership. All destructive tests must operate only on learner-created disposable fixture directories, never a personal or production database.

### Reproducibility and course decisions

Retain a pinned Rust toolchain, source, independent state-machine oracle, fixture bytes, deterministic crash-injection stages, restart commands and full observed/expected distinctions. Include relevant OS/filesystem details, durability mode, dataset sizes and measurement variance. Every required assessment is evaluated against its published criteria, with revision/ID and evidence references; none can be replaced by a completed activity counter. Pre-migration learner evidence remains tied to its original course revision. Status stays `draft` until authentic learner/reviewer evidence establishes readiness.
