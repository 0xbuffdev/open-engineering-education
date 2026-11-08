> Part of the [Zero to Software Engineer](../00-overview.md) curriculum · Program 3 of 5 · [Resource library](../resources/README.md) · [Shared standards](../shared/electives-assessment-graduation.md) · Previous: [APP](02-APP-application-engineering.md) · Next: [AI](04-AI-ai-engineering.md)

# PROGRAM 3 — SYS
# Systems Engineering

## Overview

Systems Engineering teaches you to reason about and build software close to the machine. You work through computer architecture and memory, systems programming, concurrency, networking, storage, distributed systems, performance engineering, and production systems design. Rust is the primary language for substantial systems work, and you finish by designing, measuring, and defending a real systems component.

## Prerequisites

**Program 1 — SEF — Software Engineering Foundations.**

A Linux environment is required for the program. Individual SYS courses may additionally require specific preceding SYS courses.

## Learning outcomes

By the end of this program, you will be able to:

- Explain how source code, machine instructions, CPUs, memory hierarchies, operating systems, and hardware interact during program execution.
- Write systems software using C and Rust while reasoning explicitly about resource ownership, memory, and operating-system interfaces.
- Design and analyze concurrent programs using synchronization, atomics, memory-ordering concepts, and measurable contention behavior.
- Build networked services that handle partial I/O, concurrency, backpressure, timeouts, and clean shutdown.
- Design storage systems with durable writes, indexing, compaction, checksums, and crash-recovery behavior.
- Reason about replication, failure, consistency, and recovery in distributed systems.
- Profile and benchmark systems software and attribute performance problems to measurable causes.
- Design, build, measure, and defend a production-grade systems component or service.

## Program completion standard

The learner must demonstrate the knowledge, practical skills, and engineering judgment described by the program outcomes and successfully complete the program capstone.

---

---

## SYS resource index

*Generated from the master library: 31 resources are used in this program. "Also used in" shows reuse by other programs. Full details: [books](../resources/books.md) · [online](../resources/online.md) · [matrix](../resources/matrix.md) · [glossary](../resources/glossary.md).*

> Access markers: 📚 local library · 🌐 free online/download · 🛒 obtain (borrow or buy) · 🔐 account, isolated lab or GPU needed.

### Books

| Code | Resource | Access | Courses in this program | Also used in |
|---|---|---|---|---|
| B1 | *But How Do It Know?* — J. Clark Scott | 📚 | SYS1 | SEF |
| B2 | *The C Programming Language*, 2nd ed. — Kernighan & Ritchie | 📚 | SYS2, SYS4 | SEF, SEC |
| B3 | *Digital Design and Computer Architecture* — Harris & Harris | 📚 | SYS1, SYS3 | SEF, AI |
| B4 | *Operating Systems: Three Easy Pieces* — Arpaci-Dusseau & Arpaci-Dusseau | 📚 | SYS1, SYS2, SYS3, SYS4, SYS5, SYS6 | SEF, SEC |
| B5 | *The Linux Programming Interface* — Michael Kerrisk | 📚 | SYS2, SYS3, SYS4, SYS5, SYS6, SYS7, SYS9 | SEF, APP, SEC |
| B6 | *What Every Programmer Should Know About Memory* — Ulrich Drepper | 📚 | SYS1, SYS3, SYS7 | AI |
| B14 | *Computer Systems: A Programmer's Perspective*, 3rd ed. (CS:APP) — Bryant & O'Hallaron (Pearson, 2015) | 🛒 | SYS1 | SEF, SEC |
| B15 | *The Rust Programming Language* (2024 edition) — Klabnik, Nichols & Krycho | 🌐 | SYS2, SYS4 | SEF, SEC |
| B19 | *Computer Networking: A Top-Down Approach*, 8th ed. — Kurose & Ross (Pearson, 2020); the 9th ed. (2026) moves Socket Programming to §2.6 | 🛒 | SYS4 | APP, SEC |
| B25 | *Designing Data-Intensive Applications*, 2nd ed. — Kleppmann & Riccomini (O'Reilly, 2026) | 🛒 | SYS5, SYS6, SYS8, SYS9 | APP |
| B26 | *Site Reliability Engineering* — Beyer, Jones, Petoff & Murphy (O'Reilly, 2016) | 🌐 | SYS7, SYS8, SYS9 | APP, AI, SEC |
| B27 | *Observability Engineering* — Majors, Fong-Jones & Miranda (O'Reilly, 2022) | 🛒 | SYS7, SYS8, SYS9 | APP |
| B29 | *Release It!*, 2nd ed. — Michael T. Nygard (Pragmatic Bookshelf, 2018) | 🛒 | SYS4, SYS8, SYS9 | APP |
| B30 | *Rust Atomics and Locks* — Mara Bos (O'Reilly, 2023) | 🌐 | SYS3, SYS9 | — |
| B31 | *Database Internals* — Alex Petrov (O'Reilly, 2019) | 🛒 | SYS5, SYS9 | — |
| B32 | *Systems Performance*, 2nd ed. — Brendan Gregg (Addison-Wesley, 2020) | 🛒 | SYS1, SYS7, SYS8, SYS9 | APP |
| B43 | *Building Secure and Reliable Systems* — Adkins et al. (O'Reilly / Google, 2020) | 🌐 | SYS8, SYS9 | SEC |

### Online resources, standards and papers

| Code | Resource | Access | Courses in this program | Also used in |
|---|---|---|---|---|
| R7 | The C4 model — Simon Brown (c4model.com) | 🌐 | SYS9 | SEF, APP |
| R10 | Google Cloud API Design Guide and API Improvement Proposals (AIPs) (cloud.google.com/apis/design · aip.dev) | 🌐 | SYS6 | APP |
| R16 | The Twelve-Factor App (12factor.net) | 🌐 | SYS8 | APP |
| R17 | Stripe API documentation — “Idempotent requests” | 🌐 | SYS6 | APP |
| R25 | “The Tail at Scale” — Dean & Barroso (CACM, 2013) | 🌐 | SYS7 | APP |
| R36 | The Rustonomicon (doc.rust-lang.org/nomicon) | 🌐 | SYS2 | SEC |
| R37 | Tokio tutorial (tokio.rs/tokio/tutorial) | 🌐 | SYS4 | — |
| R38 | MIT 6.5840 (formerly 6.824) Distributed Systems — lectures and labs (pdos.csail.mit.edu/6.824) | 🌐 | SYS6, SYS9 | — |
| R39 | “In Search of an Understandable Consensus Algorithm” (Raft) — Ongaro & Ousterhout (2014) (raft.github.io) | 🌐 | SYS6 | — |
| R40 | Mini-LSM — build an LSM-tree storage engine in Rust (skyzh.github.io/mini-lsm) | 🌐 | SYS5 | — |
| R41 | Brendan Gregg — “The USE Method” and “CPU Flame Graphs” pages (brendangregg.com) | 🌐 | SYS7 | — |
| R42 | Command-line apps in Rust (cli.rs book) (rust-cli.github.io/book) | 🌐 | SYS2 | — |
| R43 | Linux `perf` and kernel tracing documentation | 🌐 | SYS7 | — |
| R44 | Linux NUMA documentation | 🌐 | SYS3 | — |

---

