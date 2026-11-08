# Program 3 — SYS: Systems Engineering

> [OEE curriculum](../README.md) · [Specification](../../spec/README.md) · [Historical source at 0e14d4ff5808](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/SYS.md)

**Migration status:** The course documents below are preserved historical drafts and **not yet conforming to OEE v0.2.0**. Their old curriculum sequence and prerequisites must be reviewed; the source's books, chapters, and other resource assignments stay in the content repository.

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

## Courses

| Code | Course | Type | Duration |
| --- | --- | --- | --- |
| [SYS1](SYS1.md) | Computer Architecture, Memory & Performance | `course` | 6 weeks |
| [SYS2](SYS2.md) | Systems Programming with C & Rust | `course` | 6 weeks |
| [SYS3](SYS3.md) | Concurrency, Atomics & Memory Models | `course` | 6 weeks |
| [SYS4](SYS4.md) | Linux Networking & Services | `course` | 6 weeks |
| [SYS5](SYS5.md) | Storage Engines & Data Systems | `course` | 6 weeks |
| [SYS6](SYS6.md) | Distributed Systems | `course` | 7 weeks |
| [SYS7](SYS7.md) | Performance Engineering & Observability | `course` | 5 weeks |
| [SYS8](SYS8.md) | Systems Design & Production Engineering | `course` | 5 weeks |
| [SYS9](SYS9.md) | Systems Engineering Capstone | `project` | 8–10 weeks |

## Required next review

1. Reconcile original prerequisites against today's OEE SEF/APP course codes and the full program dependency graph.
2. Review the learning outcomes and lesson progression under [Course Format](../../spec/course-format.md) and the one-primary-objective-per-lesson guidance in [Curriculum Design Guide](../DESIGN-GUIDE.md).
3. Give the course observable, stable outcome IDs and required summative assessment IDs, with public work, success criteria, and proportionate evidence for **every** required outcome.
4. Treat old module checkpoint and micro-lab placements as **historical proposals**, not mandatory `v0.2.0` completion gates.
5. Specify safe, reproducible experimentation and a reviewable technical defense when substantial project outcomes require it.
6. Preserve book/resource mappings **outside OEE**, keyed by OEE course codes in the content repository.
7. Verify educational coverage manually. A structurally valid file or `draft` status does not constitute course or implementation conformance.
