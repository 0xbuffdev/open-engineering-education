# S11 — Distributed Systems

**Track:** Systems · **Prerequisite:** S9, S10 · **Core** · **Time:** 7 weeks, 105 hours · **Project:** P6 raftkv
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

A distributed system is a set of independent computers that must appear to behave as one. You will learn the failure models, communication patterns, replication and consensus mechanisms, and the discipline of proving what a client is guaranteed when messages are lost, delayed, duplicated, or reordered.

## Outcomes

You can:

- explain partial failure, asynchrony, and the impossibility of a perfect failure detector;
- design RPC with timeouts, retries, idempotency, and request IDs;
- explain replication, consistency models, and the CAP/PACELC trade-offs without slogans;
- implement a durable log and a leader-based replication protocol;
- explain Raft's terms, elections, log matching, and commit rules;
- inject partitions, dropped replies, duplicates, and restarts;
- define the client guarantee for each failure;
- measure availability and latency under fault injection.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| B4 *OSTEP* | Ch. **47–50** | Distributed systems, NFS, AFS |
| *Designing Data-Intensive Applications* (DDIA, 2nd ed.) | Ch. **1–2, 5–10** | Trade-offs, encoding, replication, sharding, transactions, failure, consensus |
| [MIT 6.5840](https://pdos.csail.mit.edu/6.824/) | RPC, fault tolerance, consensus labs | Guided implementation |
| [Raft paper](https://raft.github.io/raft.pdf) | Full | Consensus reference |
| [Jepsen consistency models](https://jepsen.io/consistency) | Selected models | Precise guarantees |
| B5 | Ch. **43–44, 56, 59–61** | IPC and sockets reference |

## Modules

### 1. Failure models

- crash-stop, crash-recovery, omission, Byzantine;
- network partitions, delays, duplicates, reordering;
- clocks and time;
- partial failure;
- synchronous vs asynchronous systems;
- FLP impossibility (awareness);
- exactly-once vs at-least-once vs at-most-once.

### 2. RPC and messaging

- request/response, correlation IDs;
- timeouts and retries;
- idempotency keys;
- duplicate suppression;
- backoff and jitter;
- connection pools;
- message queues and logs;
- at-least-once delivery;
- schema evolution.

### 3. Replication

- single-leader, multi-leader, leaderless;
- synchronous vs asynchronous replication;
- replication lag;
- failover and split brain;
- quorums;
- read-your-writes, monotonic reads, consistent prefix;
- conflict resolution (LWW, vector clocks, CRDTs).

### 4. Consistency and consensus

- linearizability, sequential consistency, causal consistency, eventual consistency;
- CAP and PACELC;
- two-phase commit vs consensus;
- Raft: terms, leader election, log replication, commit index, snapshots;
- Paxos/Zab (awareness);
- membership changes;
- leases and fencing tokens.

### 5. Sharding and transactions

- range vs hash sharding;
- rebalancing;
- hotspots;
- distributed transactions;
- sagas;
- idempotent consumers;
- exactly-once processing (and why it is usually at-least-once + dedup).

## Labs

### Lab 1 — RPC layer

Implement a small RPC protocol with correlation IDs, timeouts, retries, and duplicate suppression. Test dropped replies and delayed requests.

### Lab 2 — Durable log

Build an append-only log with checksums, fsync policy, truncation, and crash recovery. Test recovery after a crash at each write stage.

### Lab 3 — Leader and replication

Implement a single-leader replication protocol:

- leader election or static leader;
- follower log replication;
- commit index;
- client read/write API;
- leader failure and restart.

### Lab 4 — Raft

Implement Raft in stages:

1. leader election;
2. log replication;
3. commit rules;
4. persistence;
5. snapshots (optional);
6. membership change (optional).

Use the MIT 6.5840 tests or write equivalent deterministic tests.

### Lab 5 — Fault injection

Create a test harness that injects:

- dropped request;
- dropped reply;
- duplicate request;
- delayed message;
- partition;
- process restart.

For each, state the client guarantee and verify it.

## Exercises

1. Define linearizability and give a violating history.
2. Explain why exactly-once delivery is impossible without idempotency.
3. Compare at-least-once and at-most-once with a failure timeline.
4. Explain Raft election safety and log matching.
5. Explain a split-brain scenario and a fencing solution.
6. Compare quorum reads/writes for consistency and availability.
7. Explain CAP with a concrete partition.
8. Explain vector clocks and one limitation.
9. Design a deduplication table with garbage collection.
10. Explain why a lease needs a fencing token.

## Project increment — P6 raftkv

Build a replicated key-value store:

- RPC;
- durable log;
- leader/follower replication;
- client request IDs and deduplication;
- fault injection;
- metrics;
- a report with the client guarantee for each failure.

Reuse P5 `minikv` as the storage layer if available.

**Brief:** [P6 — raftkv](../projects/project-ladder.md#p6--raftkv)

## Exit check

- [ ] demonstrate a partition, dropped reply, duplicate request, and restart;
- [ ] explain the client guarantee in each case;
- [ ] show a Raft safety argument;
- [ ] prove what survives a crash;
- [ ] measure availability/latency under fault injection;
- [ ] state what your system does not guarantee.

## Common failure modes

- Retrying non-idempotent writes.
- Using wall-clock time for ordering.
- Claiming linearizability without a test.
- Ignoring duplicate requests after a timeout.
- Assuming a leader is always alive.
- Forgetting fsync before acknowledging a write.
- Testing only the happy path.

## Evidence to commit

- `labs/systems/S11/` with RPC, log, replication, Raft, fault matrix
- P6 raftkv
- `notes/systems/S11/summary.md`

## Optional depth

- *Designing Data-Intensive Applications* Ch. 5–9 in full.
- *Database Internals* Part II.
- MIT 6.824/6.5840 all labs.
- Jepsen analyses of real systems.
- *Distributed Systems* (Tanenbaum & van Steen).
