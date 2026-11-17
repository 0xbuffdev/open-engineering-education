# SYS4 — Linux Networking & Services

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** [SYS2](SYS2.md), [SYS3](SYS3.md)
**Duration:** 14–18 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional)

> [Systems Engineering](README.md) · [Course format](../../spec/course-format.md) · [Design guide](../DESIGN-GUIDE.md)

## Overview

Build reliable, bounded Linux network services from socket and transport behavior through event-driven I/O, resource budgets, fault handling and observability. SEF7 already assesses one blocking and one nonblocking **single-peer** loopback case; SYS3 supplies thread synchronization. SYS4 develops genuinely new **multi-client** network invariants, backpressure and protocol failure analysis. Rust is the reference implementation language; `poll` is a portable explanatory fallback to Linux-specific `epoll`. No privileged networking, public deployment, external certificate, commercial cloud or packet-sniffing permission is required. Use disposable loopback ports, synthetic clients, reproducible byte fixtures and optional packet captures.

## Learning outcomes

- **SYS4-O1:** Trace socket establishment, addressing and TCP byte-stream lifecycle while distinguishing network-layer and transport behavior.
- **SYS4-O2:** Diagnose partial I/O, framing, EOF, half-close, resets and timeout outcomes without treating TCP as message-delimited.
- **SYS4-O3:** Implement nonblocking sockets with correct readiness-driven state machines and bounded per-connection memory.
- **SYS4-O4:** Compare blocking, thread-per-connection and event-driven service models on correctness, fairness and resource use.
- **SYS4-O5:** Define a versioned protocol with explicit length limits, input validation, response errors and independent oracles.
- **SYS4-O6:** Implement bounded admission, queues, backpressure and slow-client behavior under deliberate overload.
- **SYS4-O7:** Manage connection/process lifecycles, cancellation, signals, graceful stop and forced termination without leaking resources.
- **SYS4-O8:** Explain IPv4/IPv6, DNS lookup, routing and network namespaces at the level required to debug a Linux service.
- **SYS4-O9:** Observe service behavior with privacy-safe logs, counters and traces while distinguishing network evidence from application assertions.
- **SYS4-O10:** Use controlled fault injection for dropped/delayed bytes, reconnect, malformed frames, exhaustion and partial shutdown.
- **SYS4-O11:** Specify and verify network-facing trust assumptions, local exposure policy and operational limits without claiming TLS or application authentication is automatic.
- **SYS4-O12:** Build and reproduce a concurrent Rust protocol server with documented measured constraints and failure semantics.
- **SYS4-O13:** Defend an unfamiliar service outage or protocol defect using packet/stream timelines and independent tests.

## Modules

### Module 1 — Networked Program Boundaries

#### Outcomes

- SYS4-O1
- SYS4-O8
- SYS4-O11

#### Lessons

1. **Why packet networks differ** — Trace packet switching and end-to-end transport concerns without assuming a reliable peer.
2. **Address and route** — Identify IPv4/IPv6 addresses, interface, port, route and network namespace on a local Linux host.
3. **DNS as lookup** — Differentiate resolver answers, TTL/caching and socket connect; avoid assuming the name stays attached to a connection.
4. **Transport choice** — Compare TCP stream guarantees and UDP datagram semantics without claiming either implies an application transaction.
5. **Controlled loopback fixtures** — Use 127.0.0.1 or ::1 ephemeral ports and disposable logs; no public listener required.
6. **Security boundary** — Model untrusted clients, nonprivileged ports, payload limits and prohibited arbitrary file/process access.

### Module 2 — TCP Streams and Robust Protocol I/O

#### Outcomes

- SYS4-O1
- SYS4-O2
- SYS4-O5

#### Lessons

1. **TCP lifecycle** — Trace listen, connect, handshake, accepted socket, FIN, RST, half-close and TIME_WAIT.
2. **Stream not messages** — Demonstrate split and coalesced writes against one length-framed request protocol.
3. **Partial writes and reads** — Track buffer offsets, EOF, EINTR and EAGAIN without losing transferred bytes.
4. **Framing and errors** — Define maximum sizes, version fields, invalid input and explicit refusal behavior.
5. **Connection deadlines** — Use monotonic clocks and state-aware timeouts; contrast idle and request deadlines.
6. **Wire-level oracle** — Independently encode golden request and response frames, including truncated hostile payloads.
7. **Socket options** — Discuss nonblocking, reuse, keepalive and backlog as OS-dependent operating choices.

### Module 3 — Nonblocking and Event-Driven Linux I/O

#### Outcomes

- SYS4-O2
- SYS4-O3
- SYS4-O4

#### Lessons

1. **Blocking concurrency alternatives** — Compare process/thread-per-client with readiness event loops and their constraints.
2. **Readiness versus completion** — Explain why poll/epoll readiness does not guarantee a full frame can be transferred.
3. **One event-loop state machine** — Represent accept, read, parse, write, close and error transitions explicitly.
4. **Level and edge-triggered readiness** — Explain drain-to-EAGAIN for edge-triggered mode and document selected API behavior.
5. **Writable interests** — Enable/disable write readiness according to pending bytes to avoid busy-looping.
6. **Fairness and starvation** — Bound per-client work per iteration to prevent one peer from monopolizing the loop.
7. **Portable fallback** — Use poll or equivalent when epoll is inaccessible, disclosing platform differences.

### Module 4 — Admission, Backpressure and Limits

#### Outcomes

- SYS4-O3
- SYS4-O6
- SYS4-O10

#### Lessons

1. **Resource budgets** — Set maximum connections, buffered bytes, frame lengths and per-client deadlines.
2. **Slow-reader scenario** — Show bounded write queues and an explicit reject/defer/drop policy.
3. **Slow-sender scenario** — Prevent indefinite accumulation of incomplete frames and explain timeout semantics.
4. **Admission and fairness** — Test a flood of idle peers without starving established active clients.
5. **Load generators** — Measure offered versus completed work and distinguish overload from server correctness.
6. **Negative scenarios** — Verify zero-length, too-large, duplicate, truncated, dropped and delayed inputs.

### Module 5 — Lifecycle, Failure and Transport Guarantees

#### Outcomes

- SYS4-O2
- SYS4-O7
- SYS4-O9
- SYS4-O10
- SYS4-O11

#### Lessons

1. **Shutdown ownership** — Specify who stops accepting, drains active work and closes sockets.
2. **Signal and cancellation paths** — Handle SIGTERM with bounded cleanup outside unsafe signal-handler work.
3. **Uncertain request completion** — Explain why disconnect/retry cannot establish exactly-once effects by itself.
4. **Failure taxonomy** — Distinguish unreachable destination, refused connection, timeout, reset and corrupt application frame.
5. **TLS boundary** — Discuss confidentiality, peer authentication and certificate validation as separate concerns without requiring internet certificates.
6. **Operational diagnostics** — Use request IDs, counter labels and sanitized peer observations, never full sensitive payload dumps.

### Module 6 — Diagnosis, Measurement and Resilience

#### Outcomes

- SYS4-O4
- SYS4-O8
- SYS4-O9
- SYS4-O10
- SYS4-O13

#### Lessons

1. **Packet versus stream capture** — Interpret short synthetic packet captures and application logs without overclaiming root cause.
2. **Controlled impairment** — Inject delay, drop, fragmentation of application writes or forced disconnect using a local proxy/test harness.
3. **Socket/process observability** — Inspect relevant Linux tools or equivalent program counters under restricted permissions.
4. **Load and latency** — Report connection capacity, goodput, error rates and p50/tail latency under a declared workload.
5. **Cause discrimination** — Separate slow peer, event-loop starvation, serialization bug and resource exhaustion.
6. **Corrective experiment** — Apply one targeted change and demonstrate independent regression results.
7. **Portability statement** — Declare Linux kernel assumptions and the limits of observations on alternate stacks.

### Module 7 — Bounded Multi-Client Rust Service

#### Outcomes

- SYS4-O3
- SYS4-O5
- SYS4-O6
- SYS4-O7
- SYS4-O9
- SYS4-O10
- SYS4-O12
- SYS4-O13

#### Lessons

1. **Contract and wire format** — Publish a narrow protocol and accepted/rejected byte sequences.
2. **Implementation slices** — Build safe accept, read, parse, write, timeout and close components.
3. **Overload behavior** — Use explicit queue/connection budgets and inspectably bounded allocations.
4. **Fault harness** — Exercise short I/O, slow clients, resets, malformed frames and shutdown under load.
5. **Runbook and defense** — Reproduce cleanly and resolve an unfamiliar client or server failure with a corrected test.

## Completion requirements

The assessments below establish the outcomes; exercises in lessons are formative unless reused as identified required evidence. A single service can support several criteria without duplicate final projects.

- **SYS4-AS1** — Network Model and Framing Analysis
  - **Outcomes:** SYS4-O1, SYS4-O2, SYS4-O5, SYS4-O8.
  - **Work:** Interpret a supplied TCP/socket timeline and design a fully specified bounded binary or text frame protocol.
  - **Criteria:** Correctly distinguish stream/packet/connection semantics; calculate partial buffers, invalid frames and state transitions; address/DNS claims are limited.
  - **Evidence:** Annotated timeline, protocol spec, wire examples and independent oracle.

- **SYS4-AS2** — Event-Driven Server State Machine
  - **Outcomes:** SYS4-O2, SYS4-O3, SYS4-O4, SYS4-O7.
  - **Work:** Implement or fully instrument a nonblocking multi-client server with explicit lifecycle and deadline transitions.
  - **Criteria:** No busy-loop for idle clients, correct partial read/write offsets, bounded cleanup, readiness semantics verified under fixture conditions.
  - **Evidence:** Source, state table, replayable socket tests, limits and traces.

- **SYS4-AS3** — Overload, Backpressure and Trust Tests
  - **Outcomes:** SYS4-O5, SYS4-O6, SYS4-O10, SYS4-O11.
  - **Work:** Challenge the server with slow senders/readers, malformed input, exhaustion and explicitly unsafe operations.
  - **Criteria:** Explicit rejection or bounded delay; connections and memory stay under declared caps; untrusted clients cannot select arbitrary files or commands.
  - **Evidence:** Synthetic adversarial corpus, resource logs, negative tests and observed rejection states.

- **SYS4-AS4** — Service Observability and Reliability
  - **Outcomes:** SYS4-O7, SYS4-O9, SYS4-O10, SYS4-O12.
  - **Work:** Run load/fault tests on the Rust service and document shutdown, reconnection and honest partial-completion semantics.
  - **Criteria:** Error, latency and resource observations support stated guarantees; no unsupported exactly-once, encryption or availability claims.
  - **Evidence:** Runbook, load setup, logs/metrics, failure matrix and clean checkout build.

- **SYS4-AS5** — Independent Network Failure Defense
  - **Outcomes:** SYS4-O1, SYS4-O4, SYS4-O8, SYS4-O9, SYS4-O12, SYS4-O13.
  - **Work:** Diagnose an unseen malformed-framing, starvation, timeout or connection teardown scenario and implement one fix.
  - **Criteria:** Failure causally explained, regression reproduced and corrected, alternative causes considered, limitations stated.
  - **Evidence:** Before/after trace, patch, independent test and technical defense.

### Limits and responsibility

Transport delivery is not business-transaction completion. TLS, identity and security-hardening beyond explicit service trust boundaries require separate study; a server must still reject hostile input. Event-driven Linux interfaces and counters are version-dependent, and no single local benchmark establishes global availability. SYS6 owns replication and cross-machine consistency; SYS7 owns deeper performance-inference methodology. All failure injection remains within learner-owned loopback fixtures.

### Reproducibility and decisions

Required code and tests reproduce from a clean checkout using documented Rust toolchain, Linux/kernel assumptions, bounded workload settings and independently generated frame oracles. Include normal, boundary, invalid, overload, interrupted and graceful-stop tests, measured uncertainty and confidentiality-safe evidence. Each assessment decision cites its ID, outcome IDs, course revision, result and limitations. Legacy work retains its historical completion basis; the source is `draft` until actual learner and qualified-review evidence supports status change.
