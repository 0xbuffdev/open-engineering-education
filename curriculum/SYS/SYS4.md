## SYS4 — Linux Networking & Services

**Duration:** 6 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** SYS2 and SYS3

### Overview

Move from local systems programming to networked services. You will work with sockets, TCP/IP, event-driven I/O, connection lifecycle, protocol design, and service behavior under real network conditions.

### Prerequisites

**SYS2 — Systems Programming with C & Rust**
**SYS3 — Concurrency, Atomics & Memory Models**

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Explain the socket and TCP/IP model used by Linux network services.
- Handle partial reads/writes, disconnects, malformed input, and timeouts correctly.
- Design a concurrent service with explicit backpressure and resource limits.
- Diagnose common network-service failures using logs, traces, and controlled tests.
- Build a safe multi-client network service with clean shutdown behavior.


### Resource map

**Required**

- **B5** Ch. 20–22, 25, 37, 43–44, 56–61 and 63 · **B2** Ch. 8 · **B4** Ch. 33 — carried from ZtP S10 (signals Ch. 20–22 added for clean shutdown).
- **B19** §3.5 (TCP) — added.
- **R37** Tokio tutorial and **B15** Ch. 17 and 21 — added for the Rust service lab.
- **B29** Ch. 5 (Stability Patterns) — timeouts, back pressure, load shedding.

### Modules

#### Module 1 — Sockets & TCP

**Reading:** **B5** Ch. 56 (Sockets: Introduction), Ch. 57 (Sockets: UNIX Domain), Ch. 58 (Sockets: Fundamentals of TCP/IP Networks), Ch. 59 (Sockets: Internet Domains). **B19** §3.5 (Connection-Oriented Transport: TCP).


### Module outcomes

By the end of this module, the learner can:

- Explain **Socket APIs and TCP/IP behavior** in the context of the course.
- Apply **Blocking clients and servers** in a problem, implementation, experiment, or design decision.

1. **Socket APIs and TCP/IP behavior**
   - kind: `lesson`
2. **Blocking clients and servers**
   - kind: `lesson`
3. **Checkpoint: socket fundamentals**
   - kind: `test`

4. **Micro-lab: Build a minimal TCP client and server and trace the lifecycle.**
   - kind: `lab`
#### Module 2 — Non-Blocking & Event-Driven I/O

**Reading:** **B5** Ch. 63 (Alternative I/O Models), Ch. 60 (Sockets: Server Design). **B4** Ch. 33 (Event-based Concurrency). **R37** I/O; Async in depth; Select.


### Module outcomes

By the end of this module, the learner can:

- Explain **Blocking versus non-blocking I/O** in the context of the course.
- Apply **Event-driven server architecture** in a problem, implementation, experiment, or design decision.

1. **Blocking versus non-blocking I/O**
   - kind: `lesson`
2. **Event-driven server architecture**
   - kind: `lesson`
3. **Checkpoint: I/O models**
   - kind: `test`

4. **Micro-lab: Convert a blocking server into an event-driven design.**
   - kind: `lab`
#### Module 3 — Backpressure & Reliability

**Reading:** **B5** Ch. 61 (Sockets: Advanced Topics — partial reads and writes, `shutdown()`, socket options), Ch. 60. **B29** Ch. 5 (Stability Patterns: timeouts, back pressure, load shedding). **R37** Channels; Shared state.


### Module outcomes

By the end of this module, the learner can:

- Explain **Backpressure and bounded resources** in the context of the course.
- Apply **Timeouts, retries, and partial I/O** in a problem, implementation, experiment, or design decision.

1. **Backpressure and bounded resources**
   - kind: `lesson`
2. **Timeouts, retries, and partial I/O**
   - kind: `lesson`
3. **Checkpoint: failure-aware networking**
   - kind: `test`

4. **Micro-lab: Simulate slow or partial clients and verify the server remains bounded.**
   - kind: `lab`
#### Module 4 — Protocols & Shutdown

**Reading:** **B5** §§59.2–59.3 (network byte order; data representation), Ch. 20–22 (Signals), Ch. 25 (Process Termination), Ch. 37 (Daemons). **R37** Framing; Graceful Shutdown. **B15** Ch. 21 §21.3 (Graceful Shutdown and Cleanup).


### Module outcomes

By the end of this module, the learner can:

- Explain **Protocol design and message framing** in the context of the course.
- Apply **Graceful shutdown and observability** in a problem, implementation, experiment, or design decision.

1. **Protocol design and message framing**
   - kind: `lesson`
2. **Graceful shutdown and observability**
   - kind: `lesson`
3. **Checkpoint: service behavior**
   - kind: `test`

4. **Micro-lab: Design a small protocol and verify clean shutdown for active clients.**
   - kind: `lab`
#### Module 5 — Multi-Client Rust Service

**Reading:** **R37** the whole tutorial. **B15** Ch. 17 (Fundamentals of Asynchronous Programming), Ch. 21 (Final Project: Building a Multithreaded Web Server). **B5** Ch. 60 and 63.


1. **Build, load-test, and document the Multi-Client Rust Service**
   - kind: `lab`

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

---

