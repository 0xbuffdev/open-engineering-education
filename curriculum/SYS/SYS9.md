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

### Modules

#### Module 1 — System Requirements & Architecture



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