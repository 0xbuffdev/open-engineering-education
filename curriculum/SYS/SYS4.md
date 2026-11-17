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

**SYS4 develops verified user-space multi-client networking beyond the completed SEF and SYS core foundations.** [SEF7](../SEF/SEF7.md) already assesses one blocking TCP peer, one nonblocking `poll` connection, framed bytes and single-peer deadlines. [SYS2](SYS2.md) already teaches Rust, owned resources, process lifecycle and bounded I/O. [SYS3](SYS3.md) already teaches threads, invariants, bounded queues, synchronization and concurrent progress; [SYS10](SYS10.md) explains the kernel's networking-adjacent scheduling and protection mechanisms. SYS4 therefore does **not** award repeat credit for those lessons. Its distinctive obligation is a **real, nonblocking, event-driven Rust server for simultaneous clients**, with a published network protocol, accurate Linux readiness behavior, independent wire and event oracles, enforced resource limits, fairness, explicit failure semantics and reasoned operational diagnosis.

The curriculum moves from network and trust boundaries to stream framing, per-connection state machines, Linux `poll`/`epoll` readiness and reactor scheduling, client admission/backpressure, teardown and trust policy, fault-injection verification, measured service behavior and one integrated technical defense. In particular, **TCP writes are not messages**, `epoll` readiness is not completion, edge-triggered operation must not strand already-buffered bytes, and a writable socket must not be watched forever when the service has no bytes to send. Listener backlog is not the application admission cap, a fixed per-peer buffer does not bound aggregate memory, and a socket handle reused after close must not inherit stale event-loop state.

**Reference environment:** Nonprivileged Linux, stable Rust and Cargo, learner-owned ephemeral loopback listener(s), deterministic synthetic multi-client tests and small local resource budgets. The executable server may use a **documented, public, freely available safe readiness wrapper**, such as Mio, or an equivalent audited `poll`/`epoll` abstraction with pinned/recorded dependency versions. Rust's standard `std::net` API alone does not supply an `epoll` reactor. A teaching reactor simulator, thread-per-connection comparator or deterministic fault adapter may complement, **not replace**, the assessed real nonblocking multi-client server. No root, external DNS, public listener, real packet capture, paid cloud, proprietary load generator, mandatory unsafe Rust, TLS certificates or network administrator privileges are necessary; equivalent packet/state fixtures may be supplied when host observations are limited.

**Security and evidence boundaries:** The reference app is explicitly a **loopback-only, unauthenticated teaching service**, not a production-ready Internet server. Model disclosure of sensitive inputs, adversarial clients, memory/CPU/connection exhaustion, untrusted frame lengths, exposure on wildcard addresses and ambiguous request completion. TLS authentication, durable distributed RPC deduplication, general production deployment and deep kernel profiling are not silently promised: specialized transport security belongs to SEC, cross-machine operation semantics to [SYS6](SYS6.md), and deeper performance attribution to [SYS7](SYS7.md). Demonstrations must not require attacking unrelated services.

**Workload:** The existing **14–18-week** duration at **10–15 focused hours/week** (approximately 140–270 focused hours) is a provisional planning estimate, not a credit threshold. Assessments may reuse one source tree and the same independent test corpus to avoid unnecessary duplicate final services. All thirteen established course outcomes and five summative assessment IDs remain stable; materially clarified evaluation expectations apply to this source revision without retroactively regrading historical work.

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

### Module 1 — Linux Network Boundaries, Addressing and Transport Contracts

#### Outcomes

- SYS4-O1
- SYS4-O8
- SYS4-O11

#### Lessons

1. **Prerequisite contract and disciplinary boundary** — Begin from SEF7's assessed single-peer TCP byte-stream and poll exercises, SYS2's Rust resource ownership and SYS3's bounded concurrency invariants. Diagnose the new burden of simultaneous untrusted clients instead of re-examining elementary socket I/O.
2. **What a network-layer packet does not promise** — Trace one localhost request across application bytes, TCP segments, IP routing and kernel socket buffers; distinguish segment boundaries, delivery acknowledgments and application processing without treating packets as protocol messages.
3. **IPv4, IPv6, ports and socket identity** — Interpret endpoint tuples, loopback v4/v6 addresses, listener versus accepted socket and ephemeral port selection. Explain why binding only 127.0.0.1 is different from binding 0.0.0.0 or an IPv6 wildcard, including dual-stack variation.
4. **Routes, interfaces and namespaces** — Trace a packet through a local route and network namespace using nonprivileged observation or a supplied fixture; distinguish route selection, neighbor discovery and an unreachable or refused destination from a malformed application request.
5. **DNS and name-resolution limitations** — Follow resolver result selection through connect; explain multiple A/AAAA answers, cache/TTL behavior, connection identity and why a hostname lookup neither authenticates the peer nor guarantees which endpoint stays reachable.
6. **TCP establishment and connection phases** — Explain listen/bind/accept, the handshake, established state, half-close, reset and TIME_WAIT with a short state/timeline. Separate listener backlog, active application admission and established-socket counts.
7. **UDP, TLS and transport tradeoffs** — Contrast UDP datagram boundaries with TCP stream ordering; describe where TLS confidentiality, peer identity and integrity would be layered, without claiming either ordinary TCP or a local service has them automatically.
8. **Local exposure and authority model** — Use randomly assigned learner-owned loopback ports, nonprivileged resource limits and synthetic clients. Threat-model untrusted payloads, resource exhaustion, logs and unauthorized file/command actions; never require binding a public interface.
9. **Evidence provenance and OS guarantees** — Compare Linux kernel behavior, Rust std::net abstractions and protocol-level promises; label optional namespace/packet-capture observations as environment-specific and provide inspectable synthetic equivalents.

*Optional formative feedback:* Annotate a loopback connection timeline with separate network and application claims; identify one case where the server is reachable but its protocol request is invalid.

### Module 2 — Versioned Wire Protocols, Stream Parsing and Completion Semantics

#### Outcomes

- SYS4-O2
- SYS4-O5
- SYS4-O11

#### Lessons

1. **A public binary wire contract** — Specify a small versioned request/response protocol with byte order, bounded length, operation code, status/error response, connection reuse rule and maximum requests per connection; reject undocumented ambiguous encodings.
2. **Frames versus TCP writes** — Show a sequence of tiny/coalesced writes delivering one frame in several reads, several frames in one read and a frame split midheader. Derive a parser state machine independent of sender write boundaries.
3. **Incremental header and body parsing** — Track header byte count, declared payload size, remaining body, completed frames and left-over bytes without allocating a claimed length before checking bounds. Preserve multiple complete requests in one receive buffer.
4. **Length arithmetic and allocation caps** — Reject overflowed, inconsistent, oversized and impossible lengths before buffer growth; specify whether empty payloads are valid and how length fields and total per-connection memory budgets interact.
5. **Text encoding and raw bytes** — Distinguish UTF-8 validation from arbitrary binary payload acceptance, never use lossy conversion to define a wire oracle, and document when byte comparisons, canonical encodings or text normalization matter.
6. **Partial sends and application write queues** — Maintain a pending-response buffer and an output offset under nonblocking writes. Correctly handle zero progress, Interrupted, WouldBlock, peer close and multiple response frames without duplicating or dropping accepted bytes.
7. **EOF, FIN, half-close and RST** — Differentiate clean EOF at a frame boundary, EOF with a truncated frame, a client shutdown of its write direction, and reset/error; explain why a server may still have a response to flush after receiving FIN.
8. **Time and sequencing** — Specify maximum request-frame assembly time, idle time, response-drain time and request count; distinguish absolute deadlines from continuously refreshed idle timeouts that allow slow trickle attacks.
9. **Request identity, ambiguous completion and retry** — Separate bytes written, TCP acknowledgement, server acceptance and application result. Model a disconnect after effect but before response and explain why retrying a state-changing request can duplicate effects unless a separate operation-identity protocol is designed.
10. **Independent golden byte fixtures** — Construct hand-derived request/response byte arrays and expected parser transitions for normal, truncated, coalesced, invalid-version, overlimit, unknown-opcode, extra-trailing-data and half-closed cases, rather than accepting program-generated output as the oracle.

*Optional formative feedback:* Write a five-step partial-header/partial-body trace and calculate exact parser state, input-buffer occupancy and rejection decision at each boundary.

### Module 3 — Rust Nonblocking Socket State Machines and Readiness Correctness

#### Outcomes

- SYS4-O2
- SYS4-O3
- SYS4-O4
- SYS4-O7

#### Lessons

1. **Safe socket ownership and nonblocking mode** — Use Rust TcpListener/TcpStream and OwnedFd/BorrowedFd concepts to define who registers, closes and owns each accepted connection; call set_nonblocking and correctly classify WouldBlock and Interrupted as conditional outcomes.
2. **State as an explicit typed contract** — Define accepting, reading header/body, queued response, flushing, half-closed, draining, error and closed states; specify transitions and independently expected offsets rather than hiding state in ad hoc booleans.
3. **Nonblocking accept and fairness** — Process accepted sockets under an explicit maximum per iteration and a global admission cap; correctly resume a pending listener rather than assuming one readiness notification represents one client.
4. **Read progression and EOF classification** — Attempt bounded read work, update parser offsets, handle zero-byte EOF and read errors, and decide whether a complete request remains actionable. Avoid treating WouldBlock as EOF or a partial frame as an application request.
5. **Write progression and backpressure** — Advance a pending-response offset only by bytes actually written, preserve unsent suffixes and handle WouldBlock correctly. Never assume one write transfers an entire frame or that the OS buffer equals application capacity.
6. **Registration and writable interest** — Explain why sockets are frequently writable without application output and why unconditional writable registration can cause a spin. Enable/disable or rearm write interest in concert with nonempty pending output.
7. **Half-close and tear-down transitions** — Distinguish receiving EOF from an outright reset, preserve legitimate final response behavior under a published policy and close only after flushing or a declared finite drain deadline.
8. **Connection identity and readiness races** — Explain how an event referring to a closed/reused numeric file descriptor may refer to a different connection unless registration tokens/generations are managed; reject handling stale events as current state.
9. **Readiness is a hint, not completion** — Compare poll/epoll readiness with the actual socket read/write result and account for spurious or changing readiness. A ready event cannot promise a full frame or guarantee that an immediate nonblocking call makes progress.
10. **Safe implementation boundary** — Use a pinned, public, freely available safe readiness wrapper such as Mio or a documented equivalent. Standard Rust networking alone does not expose Linux epoll; a teaching event-state simulator may accompany, but not substitute for, the required actual multi-client nonblocking implementation.

*Optional formative feedback:* Replay accepted/read-ready/write-ready/EOF events against two connection tokens and identify a case where using a stale token causes incorrect state attribution.

### Module 4 — Linux poll/epoll Reactor Semantics and Scheduling Fairness

#### Outcomes

- SYS4-O3
- SYS4-O4
- SYS4-O6

#### Lessons

1. **Readiness API contracts** — Compare poll and Linux epoll registration, interest, wakeup and error reporting while distinguishing edge-, level- and one-shot semantics. Select one actual safe API for the executable Rust service.
2. **Level-triggered iteration** — Analyze a level-triggered readable connection that remains ready until its receive buffer is drained; show a bounded per-iteration service quota and how pending work will be revisited fairly.
3. **Edge-triggered drain obligation** — Under EPOLLET, drain each nonblocking endpoint until WouldBlock or maintain an explicit ready worklist/rearm arrangement that does not rely on a future edge; show a lost-wakeup-style hang if unread bytes are forgotten.
4. **Fair work despite drain requirements** — Reconcile drain-to-WouldBlock with a bytes/frames-per-turn budget: if a quota stops draining early, retain the connection as runnable or deliberately use level triggering, rather than waiting for an edge that might never arrive.
5. **One-shot and registration transitions** — Trace EPOLLONESHOT disable/rearm and interest modification after processing; explain consequences of forgetting rearm or registering the wrong writable/readable interest.
6. **HUP, ERR and peer half-close** — Handle EPOLLERR, EPOLLHUP and optional EPOLLRDHUP in accordance with actual read/write outcomes. Explain why a hangup report is not by itself evidence that no buffered bytes remain.
7. **Fd reuse and deregistration lifecycle** — Order deregistration, removal from per-connection state and close safely; use generation-aware opaque tokens when readiness backend may report events retained from an older connection.
8. **Blocking threads versus one reactor** — Compare one blocking thread per client, a bounded worker pool and a readiness-driven event loop using the same protocol contract. Predict thread-count, memory, fairness and latency consequences without claiming the event loop always wins.
9. **Blocking work inside a reactor** — Show how an expensive handler or blocking filesystem call halts I/O progress for other connections; define a bounded offload or bounded-work policy when a service operation is not constant/short-duration.
10. **Deterministic reactor schedule tests** — Supply synthetic event sequences including duplicate readiness, unready-after-notification, stale registration, partial I/O and simultaneous clients; check against a separately written state/interest oracle and then run equivalent real loopback cases.

*Optional formative feedback:* Present an edge-triggered receive event followed by a quota stop with unread bytes. Correct the event-loop scheduling contract and test that the second complete frame is not stranded.

### Module 5 — Multi-Client Service Architecture, Budgets and Backpressure

#### Outcomes

- SYS4-O3
- SYS4-O4
- SYS4-O6
- SYS4-O11
- SYS4-O12

#### Lessons

1. **Bound the actual work model** — Define a maximum active-connection count, input buffer size, output buffer size, frame payload size, total queued bytes, work-in-flight and CPU work per iteration; calculate worst-case bound before allocating.
2. **Admission is not listener backlog** — Separate SYN/accept backlog and kernel receive buffers from the number of connections application code accepts. Enforce own caps, explicitly drop/refuse excess connections and report what those policies can and cannot guarantee.
3. **Input-side backpressure** — Limit unread/partial-frame memory, stop or restrict reading when application output backlog reaches its high-water mark, and specify timeouts for slow senders rather than accepting infinite trickled headers.
4. **Output-side slow-reader policy** — Use per-connection and global high/low-water marks or explicit hard caps. Choose backpressure, deadline-driven rejection or bounded close; avoid accumulating unlimited responses for clients that do not drain.
5. **CPU scheduling and per-peer fairness** — Cap accepted connections, bytes and completed frames per loop turn, and schedule previously runnable clients fairly. Demonstrate that one malicious high-volume peer cannot starve small valid requests under the tested budget.
6. **Capacity accounting invariant** — For each connection, track buffered input + queued output + parser metadata and a global aggregate. Verify aggregate buffers and active connections never exceed the declared cap in a bounded fixture, including cleanup and partial failures.
7. **Concurrent handlers and worker queues** — If handlers run outside the reactor, apply SYS3 bounded queue/ownership rules and publish how a full worker queue propagates admission refusal or backpressure without an unbounded intermediate buffer.
8. **Overload and retry etiquette** — Differentiate immediate rejection, limited deferral, idle timeout and graceful degradation. Publish stable error categories and where a retry is safe, but do not claim that simple TCP reconnection creates distributed at-most-once effects.
9. **Slowloris and resource-exhaustion tests** — Challenge many partial headers, very large declared frames, idle keepalive clients and slow output receivers with synthetic loopback clients and finite OS-safe process/thread bounds.
10. **Capacity versus TCP flow control** — Explain receive-window and kernel socket buffering qualitatively while separating them from the application's own queue caps. A bounded Rust Vec does not prove total kernel or whole-host memory is bounded.

*Optional formative feedback:* Compute an upper bound for 12 accepted clients each with fixed input/output caps plus a global response queue; expose a counterexample where per-client caps alone exceed a desired total budget.

### Module 6 — Trust, Timeouts, Shutdown and Connection Failure Semantics

#### Outcomes

- SYS4-O2
- SYS4-O7
- SYS4-O10
- SYS4-O11

#### Lessons

1. **Network trust and exposure policy** — Bind to loopback by default and distinguish local listener exposure from real user identity, TLS encryption, peer authentication and authorization. Refuse attempts to access arbitrary filesystem paths, run shell commands or interpret client content as trusted configuration.
2. **Authentication/TLS as scoped boundaries** — Explain basic TLS handshake/certificate/peer-auth and version constraints in architectural terms without requiring certificates, public infrastructure or a homegrown cryptographic protocol. Declare the reference service explicitly unauthenticated and local-only.
3. **Socket errors and cancellation taxonomy** — Distinguish name resolution failures, connect refused, incomplete handshake, deadline exceeded, EOF, peer reset, application malformed frame and server overload; ensure tests assert the appropriate observation rather than rely on one error code across all hosts.
4. **Idle, frame and total connection deadlines** — Use monotonic elapsed time for idle, absolute frame-assembly and response-drain policies; prove a slow trickle cannot indefinitely extend an absolute frame budget by sending one byte before each idle timeout.
5. **Liveness across teardown** — Specify who stops accepting, which queued responses finish, which clients are rejected, and what happens to half-closed sockets under shutdown. Maintain an explicit per-connection state and overall finite shutdown budget.
6. **Signal handling without unsafe hidden work** — Arrange graceful stop through a testable cancellation flag/wakeup and loop-controlled close/drain transition; keep async-signal-unsafe operations out of actual OS signal handlers, with signal integration documented as optional platform-specific glue.
7. **Forced versus graceful termination** — Distinguish an orderly server drain from forcibly closing sockets or the process. Prove which accepted operations have completed by application contract and which remain ambiguous after partial or aborted response.
8. **Input and log sanitization** — Prevent allocation bombs, payload injections into log lines, lossily decoded wire identities and secret-bearing diagnostics. Use fixed label sets or bounded fields and disclose when peer addresses or raw bytes could be personal information.
9. **Error reporting under stress** — Define protocol error responses when possible, and explicit drop/close outcomes when writing an error would exceed a limit or the peer is disconnected. Avoid claiming a refusal frame is guaranteed delivered to a failed remote peer.

*Optional formative feedback:* Design a 3-client shutdown trace including an idle peer, an incomplete request and a completed request awaiting drain. Classify each result without inventing a transactional guarantee.

### Module 7 — Protocol Verification, Hostile Clients and Deterministic Fault Injection

#### Outcomes

- SYS4-O2
- SYS4-O5
- SYS4-O6
- SYS4-O10
- SYS4-O11
- SYS4-O13

#### Lessons

1. **Independent parser and response oracles** — Derive golden byte sequences and accepted/rejected state transitions by hand or from a separate published specification; never use the service itself to generate the only expected results.
2. **Fragmentation and coalescing fixture control** — Deliberately split and combine application writes at every header/body boundary with one or more clients; do not mislabel application write fragmentation as emulating physical TCP segment loss or reordering.
3. **Partial-send and partial-receive seams** — Use controlled test adapters or constrained socket-buffer behavior to induce WouldBlock/short I/O and verify exact output offsets. Distinguish deterministic fake I/O from probabilistic behavior on localhost.
4. **Malformed and abusive framing corpus** — Check bad version/opcode, truncated header, length overflow, impossible size, repeated request, extra trailing bytes and unknown error code against explicit protocol grammar, capped buffers and predictable connection policy.
5. **Slow-client fairness scenarios** — Coordinate at least three simultaneous peers including a slow sender, slow reader and well-behaved requestor. Require the good client to finish within the published bounded fixture deadline without asserting universal fairness.
6. **Pressure and recovery tests** — Reach active-connection, per-client-buffer, global-queue and work-iteration caps; record refusal/drop/backpressure transitions and recovery after a client closes or the queue drains.
7. **Half-close, reset and interrupted shutdown** — Exercise FIN before a full request, FIN after complete request, abrupt reset, interrupted output and server cancellation. Identify where application outcome is observable versus necessarily uncertain.
8. **Distinct causal hypotheses** — For a newly supplied hang, consider at least two hypotheses such as lost edge notification, incomplete framing, slow-reader output cap or blocked reactor handler; identify a discriminating trace rather than blame TCP generically.
9. **Model limits and safe isolation** — Use deterministic logical event fixtures as a first layer and finite real loopback trials as a second. Record resource ceiling, event backend and synthetic-vs-observed provenance; never require network administration or public packet interception.

*Optional formative feedback:* Make a replay file with partial frame, writable-event storm and stale socket event, then state exactly which observations a real loopback test can and cannot reproduce deterministically.

### Module 8 — Service Instrumentation, Measurement and Diagnostic Inference

#### Outcomes

- SYS4-O4
- SYS4-O8
- SYS4-O9
- SYS4-O10
- SYS4-O13

#### Lessons

1. **Instrument transitions, not just final logs** — Expose bounded counts for accepted/rejected connections, active clients, decoded frames, queue bytes, timeout categories, short I/O and shutdown outcomes; distinguish counters recorded at the event loop from inferred TCP packet facts.
2. **Correlation with minimal disclosure** — Use synthetic request IDs or fixed-size correlation tokens, redact raw payloads and avoid unbounded labels or peer address retention. Explain how sampling or lost logs can bias conclusions.
3. **Compare models under one contract** — Run a bounded blocking/thread-per-client reference and the event-driven service under the same frame spec and offered workload; state which differences are architectural and which arise from implementation choices.
4. **Offered, admitted, completed and failed load** — Distinguish client attempted requests, accepted connections, admitted frames, fully sent responses and client-verified completion; derive a goodput denominator and error rate that do not hide overload.
5. **Latency and tails with context** — Measure client-observed round-trip time and a declared server-side phase when available; calculate median and a high percentile only when sample count justifies it and disclose the size/order of the observed distribution.
6. **Attribution and uncertainty** — Test competing hypotheses for throughput collapse, tail latency or starvation; record TCP/application buffers, CPU load, thread counts and scheduling/allocator effects without claiming any single metric proves kernel root cause.
7. **Controlled repeats and resource variation** — For each comparable configuration record at least five raw run results with units and a summary statistic/spread, fixed workload and correctness checks, and explain why a local laptop result is not a global service-capacity guarantee.
8. **Regressions and postmortem evidence** — Make one targeted intervention, compare against an independent failure/regression corpus and preserve before/after event traces; describe a plausible unexcluded explanation or limitation.

*Optional formative feedback:* Given a synthetic log showing accepted connections but low completed responses, formulate two explanations and the smallest additional counters that distinguish them.

### Module 9 — Integrated Nonblocking Multi-Client Rust Service and Unseen Defense

#### Outcomes

- SYS4-O1
- SYS4-O2
- SYS4-O3
- SYS4-O4
- SYS4-O5
- SYS4-O6
- SYS4-O7
- SYS4-O8
- SYS4-O9
- SYS4-O10
- SYS4-O11
- SYS4-O12
- SYS4-O13

#### Lessons

1. **Publish the exact service contract** — Select a small request/response handler such as bounded echo/transform or pure lookup over owned synthetic fixtures; specify versioned frames, errors, request limits, no unauthorized filesystem/process effects, and declared support for reusing or closing a connection.
2. **Build the executable reactor slice by slice** — Use safe Rust nonblocking TcpListener/TcpStream plus a documented readiness wrapper, an event loop with connection-generation tokens, parser/output offsets and stable lifecycle states. Preserve no accidental blocking operation in the I/O loop.
3. **Integrate capacity and cancellation** — Enforce per-connection and aggregate input/output limits, active-client caps, finite CPU work and deadlines while retaining correct event interest/rearm and explicit stop-accepting/drain/forced-close states.
4. **Demonstrate true multi-client progress** — Use multiple independently scheduled synthetic clients with fragmentation, slow output reads, half-close and simultaneous requests. Show one client's overload does not stall another within the published test and fairness conditions.
5. **Make failure oracles reproducible** — Run the separate protocol grammar oracle, scripted readiness traces, bounded real loopback fault harness and resource-accounting checks; show clean rerun of invalid, timed-out, over-capacity and interrupted cases.
6. **Evidence and measurement package** — Publish Cargo manifest/lockfile, Rust edition/target/kernel/backend versions, exact commands, fixed input seeds, resource limits, privacy-safe event counts, client-verified response data and raw limited-run measurements.
7. **Graceful operation and constraint disclosure** — Write a short runbook with bind and cleanup behavior, signal/cancellation policy, error categories, safe exposure decisions and honesty about ephemeral kernel buffers, missing TLS, host scheduler and unknown remote completion.
8. **Independent unknown-case diagnosis** — Receive an unseen bounded client/server fault or load change, state two competing causes and a predictive event timeline, reproduce, patch and independently verify behavior without changing unrelated passed protocol cases.
9. **Technical defense and revision provenance** — Defend the chosen reactor/backpressure/contract design and its tradeoffs, identifying which results follow from the model, which from bounded Linux observations and which remain unproven. Keep prior learner evidence bound to the original course revision.

*Optional formative feedback:* Ask a reviewer to insert a write-ready storm followed by a half-close and a new socket reusing a descriptor; predict current connection state and document the one check that prevents stale-event corruption.

## Completion requirements

**Five summative assessments establish all thirteen SYS4 outcomes.** Lesson practice, optional packet captures and model-checking utilities are formative; all required behavior, evidence and review criteria are published here. One implementation may supply AS2's reactor, AS3's backpressure/security challenge, AS4's reproducibility and measured operation and AS5's independent defense. They are separate evaluation decisions, **not four independent server projects**. Every assessed execution must use learner-owned bounded loopback fixtures and separately specified expected results.

- **SYS4-AS1** — Network, TCP Stream and Versioned Wire Contract
  - **Outcomes:** SYS4-O1, SYS4-O2, SYS4-O5, SYS4-O8, SYS4-O11.
  - **Work:** Specify a versioned binary/text byte protocol with an explicit header, bounded payload, response/error framing, maximum in-flight requests, connection-reuse and half-close policy. Independently solve at least **five distinct socket/stream scenarios** including a split header/body, coalesced requests, incomplete EOF, a half-close/reset distinction and one IPv4/IPv6/DNS or routing/namespace observation. State application authority and TLS/authentication boundaries.
  - **Criteria:** Given byte sequences and declared target/endianness, exact parser offsets and expected accept/reject/response decisions match hand-derived wire oracles; version/length arithmetic and UTF-8 versus raw bytes are unambiguous. A TCP write, segment or acknowledgement is not treated as one application message or as proof of transaction completion. The learner distinguishes port/bind identities, wildcard exposure, DNS lookup, network delivery and service-level authorization, and explains why loopback or TCP by itself gives neither TLS nor peer identity. At least one malformed, oversized and trailing-extra-byte case has an explicit bounded rejection policy.
  - **Evidence:** Public protocol grammar and byte layouts, independent golden and invalid frame hex/text samples, five annotated TCP/connection histories, parser transition table, relevant IP/routing/DNS assumptions and a short documented trust/exposure policy.

- **SYS4-AS2** — Real Nonblocking Multi-Client Reactor and Fairness
  - **Outcomes:** SYS4-O2, SYS4-O3, SYS4-O4, SYS4-O7.
  - **Work:** Implement the **actual** nonblocking multi-client Rust accept/read/parse/write/close reactor using a documented safe `poll`/`epoll`-style readiness API, with **at least three simultaneous independently driven clients**. Publish per-connection states and opaque registration/generation identities, read/write offsets, interest changes, bounded per-turn work and shutdown transitions. Compare one declared blocking/thread-per-client strategy against the chosen event model by reasoned traces or a bounded executable reference.
  - **Criteria:** WouldBlock and Interrupted are not confused with EOF/completion; short I/O never loses or duplicates bytes, writable monitoring cannot spin when no output is queued, and a ready event never substitutes for a successful I/O operation. Edge-triggered use must drain until WouldBlock or explicitly retain/rearm all remaining work under fair service quotas; level and one-shot alternatives must meet their own registration contract. Stale/closed/reused connection events do not mutate a new peer, half-close/reset and final response behavior follow the protocol, and all directly owned connections and readiness interests are released on every tested shutdown/failure path. A slow or idle peer does not prevent a well-behaved peer's progress in bounded fixture tests. No mandatory unsafe Rust, private runtime or privileged kernel operation.
  - **Evidence:** Rust server/manifest/lockfile, explicit event/state/interest tables, generation/ownership diagram, exact real-loopback inputs and returned bytes, reactor schedule oracles for partial I/O/EOF/edge rearm/stale events, comparative architecture note and finite cleanup/fairness traces.

- **SYS4-AS3** — Admission, Backpressure, Resource Caps and Trust
  - **Outcomes:** SYS4-O3, SYS4-O5, SYS4-O6, SYS4-O10, SYS4-O11.
  - **Work:** Challenge the **same AS2 service** with simultaneous slow senders, slow readers, oversized/truncated/invalid frames, idle clients, a response flood, full admission and shutdown during pressure. Configure **explicit numeric maxima** for active connections, per-connection input/output bytes, global queued/held application bytes, declared frame count/size and a finite fairness/deadline budget. Include attempts to use client content as an arbitrary filesystem path or command.
  - **Criteria:** The implementation enforces per-client **and aggregate** buffer/admission caps *before and during allocations*, accounting for existing responses and partial frames; merely setting socket backlog or truncating only after collection is insufficient. Slow clients receive documented bounded backpressure, timeout, rejection or closure and do not monopolize the event loop under the published test schedule. A partial trickle cannot indefinitely extend an absolute frame assembly deadline; no trusted shell execution, arbitrary path access, sensitive log dumping or wildcard/public listener is introduced by untrusted payloads. Each refusal/error/close outcome is independently specified, testable with synthetic clients and honest about kernel-owned buffers and unobserved whole-host resource effects.
  - **Evidence:** Numeric resource/capacity ledger with worst-case arithmetic, scripted adversarial client corpus, real and synthetic admission/pressure traces, bounded allocation/counter logs, false-input tests, monitored clean-up results, refusal semantics and documented host limits.

- **SYS4-AS4** — Reproducible Service Operation, Shutdown and Measurements
  - **Outcomes:** SYS4-O4, SYS4-O7, SYS4-O9, SYS4-O10, SYS4-O12.
  - **Work:** Release the **same integrated SYS4 Rust service** with a fresh-checkout runbook, local client suite and documented bind/security policy. Perform controlled load, idle/deadline, half-close/reset, reconnection and graceful/forced stop scenarios; compare at least two offered-load conditions or the event model against a declared baseline, recording client-observed success and service-side state. Explain what happens when a request takes effect but its reply is lost.
  - **Criteria:** Toolchain, dependency versions, Linux/runtime assumptions, numeric limits and exact clean-run commands reproduce the correct documented protocol and failure matrix. Record **at least five independent trials per comparable load condition** with accepted/admitted/completed/refused counts, throughput or goodput, client-observed latencies with units, and environment/confounder notes; report center/spread and only justified tail claims. Logs/counters have bounded cardinality and avoid exposing raw sensitive frames; claims about partial completion, retry, TLS, remote availability and exactly-once effects remain bounded by actually observed/application-defined semantics. Shutdown stops admission, accounts for in-flight work, drains or explicitly drops within a declared time budget, and releases local listener/connection resources without pretending remote delivery is guaranteed.
  - **Evidence:** Complete Rust source/manifest and pinned features, clean-checkout runbook, synthetic client and fault harness, independent response oracles, raw per-trial workload/timing and result data, latency/resource summaries, privacy-safe event logs, restart/shutdown traces and qualified limitations.

- **SYS4-AS5** — Unfamiliar Multi-Client Network Defect Defense
  - **Outcomes:** SYS4-O1, SYS4-O4, SYS4-O8, SYS4-O9, SYS4-O12, SYS4-O13.
  - **Work:** Independently diagnose a **previously unseen** small, bounded service/network scenario supplied by a reviewer or public deterministic variant rule. Possible cases include lost edge-triggered work after quota, stale-fd token reuse, incorrectly serviced writable interest, partial-frame desynchronization, false DNS/IPv6 attribution, slow-reader starvation or ambiguous disconnect. Before running a test, record **two competing causal hypotheses** and an event/stream timeline prediction; perform discriminating synthetic and loopback checks, make the smallest justified change or reasoned bounded refusal and test existing correct behavior.
  - **Criteria:** The learner separates TCP/network-layer observations from application, readiness-registration, resource-accounting or kernel-assumption errors; supplies one legally possible event history that explains the fault and distinguishes plausible alternatives. A correction addresses the relevant state transition or invariant without breaking valid parsing, limit enforcement, fairness and cleanup. The demonstration uses independent before/after expected results, accurately labels simulated versus actually observed evidence, and discloses residual nondeterministic/host-dependent possibilities. A rehearsed trace or green stress run without a causal explanation cannot establish independent defense.
  - **Evidence:** Unknown-case description/seed, pre-execution predictions, annotated packet/stream and readiness histories, discriminating tests with provenance, minimal patch or justified analysis, independent regression data, remaining limitations and a reviewable written, recorded or live defense.

### Course boundary, access and safety

Completed SEF7 already includes C/POSIX descriptor contracts, one blocking/single nonblocking TCP peer and independently tested simple framing; that work remains required **in SEF7** and receives no SYS4 transfer/automatic credit. SYS2 supplies Rust byte parsing and ownership; SYS3 supplies bounded shared-state coordination and fair work accounting; SYS10 supplies prior kernel scheduling models. SYS4 uniquely requires an **actually running, multi-client, nonblocking Rust protocol service** with honest Linux readiness semantics, bounded application resource state and independently verified failure behavior. [SYS6](SYS6.md) owns replicated state, operation identity and distributed retry/idempotency protocols; [SYS7](SYS7.md) owns deeper profiling/production tracing and causal capacity engineering; SEC owns specialist threat modeling and deployed transport security. Referencing TLS is not a claim of TLS implementation or production suitability.

All executable assessments use safe synthetic clients, local-loopback listeners and finite thread, memory and time budgets; production deployment, traffic interception, public-network scanning, kernel modifications and privileged capture are unnecessary. Any optional Linux `epoll` wrapper and dependency must be freely accessible, publicly documented and fixed to a reproducible version. Pure state diagrams, text event traces and nonvisual alternatives are valid accessibility accommodations; independence of the required server behavior and performance evidence must still be demonstrable.

### Evidence retention, status and revisions

The established **SYS4-O1–SYS4-O13** and **SYS4-AS1–SYS4-AS5** identities remain, while explicit readiness, resource-accounting and multi-client failure thresholds materially clarify assessment expectations for **this course revision only**. Preserve previously reviewed learner outcomes against their actual source/specification revision and never retroactively regrade solely because a parser, lesson count or performance rubric changed. Each decision records course revision, assessment ID, evaluated outcome IDs, actual test conditions, independent expected output, decision and material limits. Structural validation or CI success does not promote this `draft` course to `tested` or `verified`; real learner completion and independent reviewer evidence remain necessary.

## Optional disciplinary references

These freely accessible sources aid research without becoming mandatory hidden materials or paid resources:

- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html) — connection behavior, byte-stream sequencing, FIN, resets and transport semantics.
- [Linux epoll(7)](https://man7.org/linux/man-pages/man7/epoll.7.html) and [epoll_ctl(2)](https://man7.org/linux/man-pages/man2/epoll_ctl.2.html) — edge/level/one-shot readiness, interest management and event-loop caveats.
- [Rust std::net::TcpStream](https://doc.rust-lang.org/stable/std/net/struct.TcpStream.html), [TcpListener](https://doc.rust-lang.org/stable/std/net/struct.TcpListener.html) and [std::io](https://doc.rust-lang.org/stable/std/io/) — real nonblocking, read/write, EOF and error contracts.
- [Mio documentation](https://docs.rs/mio/latest/mio/) — publicly available Rust readiness abstraction (an example, not the required assessment API).
- [OWASP Denial of Service Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Denial_of_Service_Cheat_Sheet.html) — application-layer exhaustion, input and timeout policies.
