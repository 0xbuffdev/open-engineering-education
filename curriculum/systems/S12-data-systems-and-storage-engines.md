# S12 — Data Systems & Storage Engines

**Track:** Systems · **Prerequisite:** S5, S9 · **Core** · **Time:** 6 weeks, 90 hours · **Project:** P5 minikv
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Every durable system eventually depends on a storage engine. You will learn how data is laid out on disk, how B-trees and LSM-trees work, how write-ahead logging and crash recovery provide durability, and how to benchmark a storage workload honestly.

## Outcomes

You can:

- explain the I/O path from `write()` to durable media;
- compare B-tree and LSM-tree designs;
- implement a write-ahead log with checksums and recovery;
- implement a sorted string table with bloom filters and compaction;
- explain MVCC, isolation, and garbage collection;
- reason about fsync, group commit, and durability levels;
- crash a process at controlled stages and prove what survives;
- benchmark with a stated workload and hardware limits.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| B4 *OSTEP* | Ch. **36–45** | I/O devices, disks, RAID, files, FFS, journaling, LFS, SSD, integrity |
| B5 | Ch. **13–14, 49–50, 55** | Buffering, filesystems, mappings, VM operations, file locking |
| *Database Internals* (Petrov) | Ch. **1–5, 7** | Storage organization, B-trees, file formats, recovery, LSM |
| DDIA | Ch. **3–4** | Storage engines and encoding |
| [SQLite WAL docs](https://www.sqlite.org/wal.html) | Full | A real WAL design |

## Modules

### 1. Durable I/O

- devices, sectors, pages, block layer;
- page cache and buffered I/O;
- `fsync`, `fdatasync`, `O_DIRECT`, `O_SYNC`;
- write barriers and ordering;
- torn writes and checksums;
- group commit;
- SSD erase blocks, wear leveling, FTL;
- RAID levels and failure modes.

### 2. B-trees

- page layout, slotted pages;
- search, insert, split, delete, merge;
- fanout and height;
- clustered vs secondary indexes;
- concurrency: latches, B-link trees;
- buffer pool;
- write amplification.

### 3. LSM-trees

- memtable, immutable memtable, WAL;
- SSTable format, index, bloom filter;
- flush;
- compaction (size-tiered, leveled);
- tombstones and deletion;
- read path: memtable → SSTables → compaction;
- write/read/space amplification;
- LSM vs B-tree trade-offs.

### 4. Recovery and integrity

- WAL records, LSN, redo/undo;
- checkpointing;
- crash consistency;
- checksums (CRC32C), torn-write detection;
- fsck vs journaling vs WAL;
- backup and restore.

### 5. Transactions and MVCC

- ACID;
- isolation levels and anomalies;
- MVCC versions and snapshots;
- write conflicts;
- garbage collection;
- optimistic vs pessimistic concurrency;
- distributed transactions preview (S11).

## Labs

### Lab 1 — WAL

Implement an append-only WAL with:

- record framing, length, checksum, LSN;
- fsync policy;
- replay/recovery;
- truncation/checkpoint;
- tests for torn write, partial record, and corruption.

### Lab 2 — SSTable

Implement a sorted string table with:

- data blocks and index;
- bloom filter;
- point lookup and range scan;
- checksums;
- a compaction merge iterator.

### Lab 3 — LSM engine

Build `minikv`:

- memtable + WAL;
- flush to SSTable;
- leveled compaction;
- tombstones;
- crash recovery;
- a simple CLI/API.

### Lab 4 — Crash matrix

Inject a crash at each stage: before WAL write, after WAL write, before fsync, after fsync, during flush, during compaction. For each, prove which acknowledged writes survive and which do not.

### Lab 5 — Benchmark

Benchmark sequential write, random write, point read, range scan, and mixed workload. Report throughput, p50/p95/p99, write amplification, space amplification, and hardware limits.

## Exercises

1. Compare B-tree and LSM for write-heavy and read-heavy workloads.
2. Calculate the height of a B-tree for a given fanout and row count.
3. Explain write amplification in leveled compaction.
4. Explain why a bloom filter cannot answer range queries.
5. Explain torn writes and how a checksum detects them.
6. Explain group commit and its latency/durability trade-off.
7. Explain MVCC visibility for a snapshot.
8. Explain a tombstone's lifecycle and a deletion bug.
9. Explain why `fsync` on a directory matters for rename durability.
10. Explain one benchmark confound (page cache, SSD cache, compression).

## Project increment — P5 minikv

Build the storage engine and its evidence:

- WAL + recovery;
- SSTable + bloom filter;
- compaction;
- checksums;
- crash matrix;
- benchmark;
- README with durability contract and limitations.

**Brief:** [P5 — minikv](../projects/project-ladder.md#p5--minikv)

## Exit check

- [ ] crash the process at controlled write stages and prove which committed data survives;
- [ ] explain the read and write paths of your engine;
- [ ] explain write/read/space amplification trade-offs;
- [ ] show a corrupted record is detected, not silently returned;
- [ ] benchmark with a stated workload and hardware;
- [ ] state the durability guarantee precisely.

## Common failure modes

- Acknowledging a write before fsync when durability was promised.
- Forgetting to fsync the directory after a rename.
- Assuming a checksum catches every corruption.
- Compaction that loses tombstones too early.
- Benchmarking with the page cache warm and calling it disk performance.
- Claiming ACID without defining isolation.

## Evidence to commit

- `labs/systems/S12/` with WAL, SSTable, LSM, crash matrix, benchmark
- P5 minikv
- `notes/systems/S12/summary.md`

## Optional depth

- *Database Internals* Part I in full.
- *Designing Data-Intensive Applications* Ch. 3.
- SQLite source code and WAL documentation.
- RocksDB/LevelDB design docs.
- `fio` for storage benchmarking.
