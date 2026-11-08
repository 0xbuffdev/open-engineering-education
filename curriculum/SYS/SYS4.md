# SYS4 — Linux Networking & Services

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** SYS2 and SYS3 *(legacy mapping; reconcile before activation)*
**Duration:** 6 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/SYS.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Move from local systems programming to networked services. You will work with sockets, TCP/IP, event-driven I/O, connection lifecycle, protocol design, and service behavior under real network conditions.

## Learning outcomes

- Explain the socket and TCP/IP model used by Linux network services.
- Handle partial reads/writes, disconnects, malformed input, and timeouts correctly.
- Design a concurrent service with explicit backpressure and resource limits.
- Diagnose common network-service failures using logs, traces, and controlled tests.
- Build a safe multi-client network service with clean shutdown behavior.

## Modules

### Module 1 — Sockets & TCP

#### Outcomes

By the end of this module, the learner can:

- Explain **Socket APIs and TCP/IP behavior** in the context of the course.
- Apply **Blocking clients and servers** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Socket APIs and TCP/IP behavior** — `lesson`
2. **Blocking clients and servers** — `lesson`
3. **Checkpoint: socket fundamentals** — `test`
4. **Micro-lab: Build a minimal TCP client and server and trace the lifecycle.** — `lab`

### Module 2 — Non-Blocking & Event-Driven I/O

#### Outcomes

By the end of this module, the learner can:

- Explain **Blocking versus non-blocking I/O** in the context of the course.
- Apply **Event-driven server architecture** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Blocking versus non-blocking I/O** — `lesson`
2. **Event-driven server architecture** — `lesson`
3. **Checkpoint: I/O models** — `test`
4. **Micro-lab: Convert a blocking server into an event-driven design.** — `lab`

### Module 3 — Backpressure & Reliability

#### Outcomes

By the end of this module, the learner can:

- Explain **Backpressure and bounded resources** in the context of the course.
- Apply **Timeouts, retries, and partial I/O** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Backpressure and bounded resources** — `lesson`
2. **Timeouts, retries, and partial I/O** — `lesson`
3. **Checkpoint: failure-aware networking** — `test`
4. **Micro-lab: Simulate slow or partial clients and verify the server remains bounded.** — `lab`

### Module 4 — Protocols & Shutdown

#### Outcomes

By the end of this module, the learner can:

- Explain **Protocol design and message framing** in the context of the course.
- Apply **Graceful shutdown and observability** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Protocol design and message framing** — `lesson`
2. **Graceful shutdown and observability** — `lesson`
3. **Checkpoint: service behavior** — `test`
4. **Micro-lab: Design a small protocol and verify clean shutdown for active clients.** — `lab`

### Module 5 — Multi-Client Rust Service

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Build, load-test, and document the Multi-Client Rust Service** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

### Topics

- sockets
- TCP/IP
- DNS basics
- blocking versus non-blocking I/O
- event-driven servers
- backpressure
- timeouts
- retries
- graceful shutdown
- protocol design

### Labs

- TCP echo server
- packet and socket inspection
- partial-read/write experiments
- timeout handling
- concurrent client benchmark

### Substantial course lab

**Multi-Client Rust Service**

A protocol-driven network service with:

- concurrent clients
- bounded resources
- backpressure
- timeouts
- structured logs
- metrics
- load tests
