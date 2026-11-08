# SYS9 — Systems Engineering Capstone

**Program:** SYS — Systems Engineering
**Type:** `project`
**Prerequisites:** Pending reconciliation of historical prerequisite notes
**Duration:** 8–10 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/SYS.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

The capstone is the final project course in Systems Engineering. You will design and implement a systems-oriented service or infrastructure component, subject it to realistic load and failure conditions, and use measurement to explain its behavior and trade-offs.

## Learning outcomes

- Design a systems project from explicit functional and nonfunctional requirements.
- Implement resource ownership, concurrency, networking, persistence, or distributed behavior appropriately.
- Measure system performance and identify bottlenecks using evidence.
- Test failure, restart, overload, and recovery behavior.
- Document guarantees, operational requirements, and failure modes.
- Defend low-level and architectural trade-offs using observed behavior.

## Modules

### Module 1 — System Requirements & Architecture

#### Outcomes

By the end of this module, the learner can:

- Explain **Requirements, guarantees, resource model, protocol, and architecture** in the context of the course.

#### Lessons

1. **Requirements, guarantees, resource model, protocol, and architecture** — `lesson`
2. **Architecture checkpoint** — `test`
3. **Micro-lab: Define system invariants and draw the data/control flow.** — `lab`

### Module 2 — Core Implementation

#### Outcomes

By the end of this module, the learner can:

- Explain **Incremental implementation of the core systems component** in the context of the course.

#### Lessons

1. **Incremental implementation of the core systems component** — `lesson`
2. **Implementation checkpoint** — `test`
3. **Micro-lab: Implement and instrument one critical path before expanding the system.** — `lab`

### Module 3 — Concurrency, Failure & Recovery

#### Outcomes

By the end of this module, the learner can:

- Explain **Concurrency, resource failures, restart behavior, and recovery** in the context of the course.

#### Lessons

1. **Concurrency, resource failures, restart behavior, and recovery** — `lesson`
2. **Failure analysis checkpoint** — `test`
3. **Micro-lab: Inject one controlled failure and record the observed recovery path.** — `lab`

### Module 4 — Performance & Operations

#### Outcomes

By the end of this module, the learner can:

- Explain **Benchmarking, observability, load testing, capacity, and operational readiness** in the context of the course.
- Apply **Production readiness review** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Benchmarking, observability, load testing, capacity, and operational readiness** — `lesson`
2. **Production readiness review** — `test`
3. **Micro-lab: Establish a baseline benchmark and isolate one bottleneck.** — `lab`

### Module 5 — Final Project Lab

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Build, stress, measure, fault-inject, document, and prepare the systems project for defense** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

### Suitable capstone shapes

- replicated storage service
- durable message/stream service
- high-performance network service
- local distributed database
- systems-oriented developer infrastructure

### Required qualities

- architecture/design document
- Rust implementation
- automated tests
- failure injection
- load testing
- benchmarks
- observability
- recovery procedure
- deployment instructions
- security considerations
- API/protocol documentation
- architecture diagram
- incident/failure report
- retrospective

### Project defense

The final defense must include a **live failure demonstration** and explanation of the system's guarantees.

This is the **Program 3 — SYS graduation requirement**.
