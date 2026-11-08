## SYS9 — Systems Engineering Capstone

**Duration:** 8–10 weeks
**Expected workload:** 10–15 focused hours/week

### Overview
The capstone is the final project course in Systems Engineering. You will design and implement a systems-oriented service or infrastructure component, subject it to realistic load and failure conditions, and use measurement to explain its behavior and trade-offs.

### Prerequisites
**SYS1–SYS8 — Systems Engineering**

**Kind:** `project`

### Learning outcomes
By the end of the project, you will be able to:

- Design a systems project from explicit functional and nonfunctional requirements.
- Implement resource ownership, concurrency, networking, persistence, or distributed behavior appropriately.
- Measure system performance and identify bottlenecks using evidence.
- Test failure, restart, overload, and recovery behavior.
- Document guarantees, operational requirements, and failure modes.
- Defend low-level and architectural trade-offs using observed behavior.

### Resource map

**Required**

- Review the SYS1–SYS8 readings module by module and pick the chapters that match your capstone shape (storage: **B31**; network service: **B5** Ch. 56–63; concurrent runtime: **B30**; replicated service: **B25** and **R38**).
- **R7** the C4 model for the architecture diagram.

### Modules

#### Module 1 — System Requirements & Architecture

**Reading:** **B25** Ch. 1–2 (trade-offs; nonfunctional requirements). **B26** Ch. 3–4 (risk; SLOs). **B43** Ch. 4 (Design Tradeoffs). **R7** C4 diagrams.


### Module outcomes

By the end of this module, the learner can:

- Explain **Requirements, guarantees, resource model, protocol, and architecture** in the context of the course.

1. **Requirements, guarantees, resource model, protocol, and architecture**
   - kind: `lesson`
2. **Architecture checkpoint**
   - kind: `test`

3. **Micro-lab: Define system invariants and draw the data/control flow.**
   - kind: `lab`
#### Module 2 — Core Implementation

**Reading:** Chapters matching the chosen shape: **B31** Ch. 3–7 (storage), **B5** Ch. 56–63 (network service), **B30** Ch. 1–5 (concurrent components), **B25** Ch. 6–10 (replicated services).


### Module outcomes

By the end of this module, the learner can:

- Explain **Incremental implementation of the core systems component** in the context of the course.

1. **Incremental implementation of the core systems component**
   - kind: `lesson`
2. **Implementation checkpoint**
   - kind: `test`

3. **Micro-lab: Implement and instrument one critical path before expanding the system.**
   - kind: `lab`
#### Module 3 — Concurrency, Failure & Recovery

**Reading:** **B30** Ch. 1–5. **B31** Ch. 5. **B25** Ch. 9–10. **B29** Ch. 4–5.


### Module outcomes

By the end of this module, the learner can:

- Explain **Concurrency, resource failures, restart behavior, and recovery** in the context of the course.

1. **Concurrency, resource failures, restart behavior, and recovery**
   - kind: `lesson`
2. **Failure analysis checkpoint**
   - kind: `test`

3. **Micro-lab: Inject one controlled failure and record the observed recovery path.**
   - kind: `lab`
#### Module 4 — Performance & Operations

**Reading:** **B32** Ch. 2, 12 and 13. **B26** Ch. 6, 17 and 21. **B27** Ch. 5–8.


### Module outcomes

By the end of this module, the learner can:

- Explain **Benchmarking, observability, load testing, capacity, and operational readiness** in the context of the course.
- Apply **Production readiness review** in a problem, implementation, experiment, or design decision.

1. **Benchmarking, observability, load testing, capacity, and operational readiness**
   - kind: `lesson`
2. **Production readiness review**
   - kind: `test`

3. **Micro-lab: Establish a baseline benchmark and isolate one bottleneck.**
   - kind: `lab`
#### Module 5 — Final Project Lab

**Reading:** **B26** Ch. 14–15 (incidents; postmortems) and **B43** Ch. 16–18 for the incident/failure report; **B32** Ch. 12 (Benchmarking) for the final measurements.


1. **Build, stress, measure, fault-inject, document, and prepare the systems project for defense**
   - kind: `lab`

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