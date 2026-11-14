# Program 3 — SYS: Systems Engineering

> [OEE curriculum](../README.md) · [Specification](../../spec/README.md) · Previous: [APP](../APP/README.md) · Next: [AI](../AI/README.md)

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

The imported courses below are **legacy drafts**, not v0.2.0-conforming course definitions. Their existing activities and completion requirements are retained for migration review; published outcome IDs, summative evidence contracts and readiness assessments must be authored and reviewed separately before any v0.2.0 claim.

| Course | Title | Duration | Prerequisites | Type |
| --- | --- | --- | --- | --- |
| [SYS1](SYS1.md) | Computer Architecture, Memory & Performance | 6 weeks | SEF6 | `course` |
| [SYS2](SYS2.md) | Systems Programming with C & Rust | 6 weeks | SYS1 | `course` |
| [SYS3](SYS3.md) | Concurrency, Atomics & Memory Models | 6 weeks | SYS2 | `course` |
| [SYS4](SYS4.md) | Linux Networking & Services | 6 weeks | SYS2 and SYS3 | `course` |
| [SYS5](SYS5.md) | Storage Engines & Data Systems | 6 weeks | SYS2 and SYS3 | `course` |
| [SYS6](SYS6.md) | Distributed Systems | 7 weeks | SYS4 and SYS5 | `course` |
| [SYS7](SYS7.md) | Performance Engineering & Observability | 5 weeks | SYS3 and SYS4 | `course` |
| [SYS8](SYS8.md) | Systems Design & Production Engineering | 5 weeks | SYS6 and SYS7 | `course` |
| [SYS9](SYS9.md) | Systems Engineering Capstone | 8–10 weeks | SYS1–SYS8 | `project` |

This list describes the imported source material, not verified learner readiness or a new specification version.
