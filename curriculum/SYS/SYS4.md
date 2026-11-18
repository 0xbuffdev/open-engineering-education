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

The curriculum moves from network and trust boundaries to wire framing, owned nonblocking connection state, poll/epoll readiness and reactor fairness, admission/backpressure, teardown, independent fault verification, measured service behavior and one cumulative defense. In particular, **TCP writes are not messages**, `epoll` readiness is not completion, edge-triggered operation must not strand already-buffered bytes, and a writable socket must not be watched forever when the service has no bytes to send. Listener backlog is not the application admission cap, a fixed per-peer buffer does not bound aggregate memory, and a socket handle reused after close must not inherit stale event-loop state.

**Reference environment:** Nonprivileged Linux, stable Rust and Cargo, learner-owned ephemeral loopback listener(s), deterministic synthetic multi-client tests and small local resource budgets. The executable server may use a **documented, public, freely available safe readiness wrapper**, such as Mio, or an equivalent audited `poll`/`epoll` abstraction with pinned/recorded dependency versions. Rust's standard `std::net` API alone does not supply an `epoll` reactor. A teaching reactor simulator, thread-per-connection comparator or deterministic fault adapter may complement, **not replace**, the assessed real nonblocking multi-client server. No root, external DNS, public listener, real packet capture, paid cloud, proprietary load generator, mandatory unsafe Rust, TLS certificates or network administrator privileges are necessary; equivalent packet/state fixtures may be supplied when host observations are limited.

**Security and evidence boundaries:** The reference app is explicitly a **loopback-only, unauthenticated teaching service**, not a production-ready Internet server. Model disclosure of sensitive inputs, adversarial clients, memory/CPU/connection exhaustion, untrusted frame lengths, exposure on wildcard addresses and ambiguous request completion. TLS authentication, durable distributed RPC deduplication, general production deployment and deep kernel profiling are not silently promised: specialized transport security belongs to SEC, cross-machine operation semantics to [SYS6](SYS6.md), and deeper performance attribution to [SYS7](SYS7.md). Demonstrations must not require attacking unrelated services.

**Workload:** The **14–18-week** duration at **10–15 focused hours/week** (approximately 140–270 focused hours) is a provisional planning estimate, not a credit threshold. Assessments reuse one actual multi-client server and independently specified fixtures rather than several final services. A lesson represents a coherent instructional purpose that can involve multiple lectures, exercises and revisions; fewer entries do not imply less work or weaker assessment. All thirteen established course outcomes and five summative assessment IDs remain stable; materially clarified evaluation expectations apply to this source revision without retroactively regrading historical work.

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

1. **Network layers, prerequisite boundary and evidence provenance** — Extend the assessed SEF7 single-peer socket path using SYS2 resource ownership and SYS3 progress invariants. Trace application bytes across TCP, IP and Linux socket buffers, explicitly separating protocol promises, Rust abstractions, source-backed kernel observations and simulated fixtures. Show why transport delivery does not establish complete application processing.
2. **What a network-layer packet does not promise** — Trace one localhost request across application bytes, TCP segments, IP routing and kernel socket buffers; distinguish segment boundaries, delivery acknowledgments and application processing without treating packets as protocol messages.
3. **IPv4, IPv6, ports and socket identity** — Interpret endpoint tuples, loopback v4/v6 addresses, listener versus accepted socket and ephemeral port selection. Explain why binding only 127.0.0.1 is different from binding 0.0.0.0 or an IPv6 wildcard, including dual-stack variation.
4. **Routes, interfaces and namespaces** — Trace a packet through a local route and network namespace using nonprivileged observation or a supplied fixture; distinguish route selection, neighbor discovery and an unreachable or refused destination from a malformed application request.
5. **DNS and name-resolution limitations** — Follow resolver result selection through connect; explain multiple A/AAAA answers, cache/TTL behavior, connection identity and why a hostname lookup neither authenticates the peer nor guarantees which endpoint stays reachable.
6. **TCP establishment and connection phases** — Explain listen/bind/accept, the handshake, established state, half-close, reset and TIME_WAIT with a short state/timeline. Separate listener backlog, active application admission and established-socket counts.
7. **Transport alternatives, TLS and local authority** — Contrast UDP datagram boundaries with ordered TCP byte streams, and locate where TLS confidentiality/integrity and peer authentication would be added. Declare a learner-owned loopback-only, bounded, unauthenticated service and refuse untrusted command/path effects or exposed public listeners; a reachable TCP peer is not automatically authorized.

*Optional formative feedback:* Annotate a loopback connection timeline with separate network and application claims; identify one case where the server is reachable but its protocol request is invalid.

### Module 2 — Versioned Wire Protocols, Stream Parsing and Completion Semantics

#### Outcomes

- SYS4-O2
- SYS4-O5
- SYS4-O11

#### Lessons

1. **Versioned wire contract and independent golden fixtures** — Publish a versioned bounded request/response byte grammar with header, endianness, length, opcode, errors, connection reuse and maximum in-flight requests. Independently hand-derive valid and invalid hex/byte fixtures, including truncated, coalesced, invalid-version, oversized, unknown-opcode and trailing-data cases, before testing an implementation.
2. **Framing versus TCP writes and incremental parse states** — Derive an incremental header/body/complete parser over a byte stream when writes split frames or multiple frames arrive in one read. Track header, body and leftover offsets across partial reads without confusing one sender write with one application message; verify exact state against independently solved fixtures.
3. **Length arithmetic and allocation caps** — Reject overflowed, inconsistent, oversized and impossible lengths before buffer growth; specify whether empty payloads are valid and how length fields and total per-connection memory budgets interact.
4. **Text encoding and raw bytes** — Distinguish UTF-8 validation from arbitrary binary payload acceptance, never use lossy conversion to define a wire oracle, and document when byte comparisons, canonical encodings or text normalization matter.
5. **Partial sends and application write queues** — Maintain a pending-response buffer and an output offset under nonblocking writes. Correctly handle zero progress, Interrupted, WouldBlock, peer close and multiple response frames without duplicating or dropping accepted bytes.
6. **EOF, FIN, half-close and RST** — Differentiate clean EOF at a frame boundary, EOF with a truncated frame, a client shutdown of its write direction, and reset/error; explain why a server may still have a response to flush after receiving FIN.
7. **Time and sequencing** — Specify maximum request-frame assembly time, idle time, response-drain time and request count; distinguish absolute deadlines from continuously refreshed idle timeouts that allow slow trickle attacks.
8. **Request identity, ambiguous completion and retry** — Separate bytes written, TCP acknowledgement, server acceptance and application result. Model a disconnect after effect but before response and explain why retrying a state-changing request can duplicate effects unless a separate operation-identity protocol is designed.

*Optional formative feedback:* Write a five-step partial-header/partial-body trace and calculate exact parser state, input-buffer occupancy and rejection decision at each boundary.

### Module 3 — Rust Nonblocking Socket State Machines and Readiness Correctness

#### Outcomes

- SYS4-O2
- SYS4-O3
- SYS4-O4
- SYS4-O7

#### Lessons

1. **Rust socket ownership and typed connection states** — Define ownership of Rust TcpListener/TcpStream, registration token and per-client buffers using a safe nonblocking API. Represent accepting, reading, pending response, flushing, half-closed, draining and closed states with valid transitions; diagnose a duplicated owner or stale closed-state registration.
2. **Bounded accepting, reading and EOF interpretation** — Accept and read under finite per-iteration and global admission limits, updating incremental parser offsets only from actual nonblocking results. Distinguish short read, WouldBlock, Interrupted, zero-byte EOF, error and accepted complete frames; a readiness event is not a completed request.
3. **Partial writes and conditional writable interest** — Advance pending output only by successfully written bytes, retaining unwritten suffixes through short writes and WouldBlock. Arm writable interest only for nonempty output and update it on drain; show both a duplicate/drop error from incorrect offsets and a writable-event spin from unconditional monitoring.
4. **Half-close and tear-down transitions** — Distinguish receiving EOF from an outright reset, preserve legitimate final response behavior under a published policy and close only after flushing or a declared finite drain deadline.
5. **Connection identity and readiness races** — Explain how an event referring to a closed/reused numeric file descriptor may refer to a different connection unless registration tokens/generations are managed; reject handling stale events as current state.
6. **Readiness is a hint, not completion** — Compare poll/epoll readiness with the actual socket read/write result and account for spurious or changing readiness. A ready event cannot promise a full frame or guarantee that an immediate nonblocking call makes progress.
7. **Safe implementation boundary** — Use a pinned, public, freely available safe readiness wrapper such as Mio or a documented equivalent. Standard Rust networking alone does not expose Linux epoll; a teaching event-state simulator may accompany, but not substitute for, the required actual multi-client nonblocking implementation.

*Optional formative feedback:* Replay accepted/read-ready/write-ready/EOF events against two connection tokens and identify a case where using a stale token causes incorrect state attribution.

### Module 4 — Linux poll/epoll Reactor Semantics and Scheduling Fairness

#### Outcomes

- SYS4-O3
- SYS4-O4
- SYS4-O6

#### Lessons

1. **Readiness API contracts** — Compare poll and Linux epoll registration, interest, wakeup and error reporting while distinguishing edge-, level- and one-shot semantics. Select one actual safe API for the executable Rust service.
2. **Level-triggered iteration** — Analyze a level-triggered readable connection that remains ready until its receive buffer is drained; show a bounded per-iteration service quota and how pending work will be revisited fairly.
3. **Edge-triggered draining, ready worklists and fairness** — Derive why EPOLLET or edge-style readiness can strand bytes when a fair per-turn quota stops before WouldBlock. Specify drain-until-WouldBlock or an explicit retained ready-worklist continuation and show how fairness budgets avoid starving other peers without relying on an unwarranted future edge.
4. **One-shot and registration transitions** — Trace EPOLLONESHOT disable/rearm and interest modification after processing; explain consequences of forgetting rearm or registering the wrong writable/readable interest.
5. **HUP, ERR and peer half-close** — Handle EPOLLERR, EPOLLHUP and optional EPOLLRDHUP in accordance with actual read/write outcomes. Explain why a hangup report is not by itself evidence that no buffered bytes remain.
6. **Fd reuse and deregistration lifecycle** — Order deregistration, removal from per-connection state and close safely; use generation-aware opaque tokens when readiness backend may report events retained from an older connection.
7. **Blocking/thread-per-client trade-offs and reactor work isolation** — Compare blocking thread-per-client, bounded workers and one readiness reactor under the same wire contract and workload, identifying resource and fairness trade-offs. Show how a slow handler or blocking file I/O stalls other clients on an event loop; justify a finite work quota or bounded handler offload.
8. **Deterministic reactor schedule tests** — Supply synthetic event sequences including duplicate readiness, unready-after-notification, stale registration, partial I/O and simultaneous clients; check against a separately written state/interest oracle and then run equivalent real loopback cases.

*Optional formative feedback:* Present an edge-triggered receive event followed by a quota stop with unread bytes. Correct the event-loop scheduling contract and test that the second complete frame is not stranded.

### Module 5 — Multi-Client Service Architecture, Budgets and Backpressure

#### Outcomes

- SYS4-O3
- SYS4-O4
- SYS4-O6
- SYS4-O11
- SYS4-O12

#### Lessons

1. **Per-client and aggregate service resource ledger** — Compute numeric per-client and global limits for connections, partial input frames, queued/pending output, parser metadata, staged/in-flight handler tasks and CPU work. Trace every reservation and release during success, cancellation and disconnect, rejecting a case where individually bounded buffers still exceed aggregate application memory.
2. **Admission is not listener backlog** — Separate SYN/accept backlog and kernel receive buffers from the number of connections application code accepts. Enforce own caps, explicitly drop/refuse excess connections and report what those policies can and cannot guarantee.
3. **Input-side backpressure** — Limit unread/partial-frame memory, stop or restrict reading when application output backlog reaches its high-water mark, and specify timeouts for slow senders rather than accepting infinite trickled headers.
4. **Output-side slow-reader policy** — Use per-connection and global high/low-water marks or explicit hard caps. Choose backpressure, deadline-driven rejection or bounded close; avoid accumulating unlimited responses for clients that do not drain.
5. **Fair scheduling and bounded handler offload** — Limit accepts, read/write bytes, completed frames and CPU work per loop turn while retaining ready clients for fair revisits. If handlers are offloaded, apply SYS3's proven bounded worker queue and propagate full-queue backpressure to the reactor without hidden unbounded staging.
6. **Overload and retry etiquette** — Differentiate immediate rejection, limited deferral, idle timeout and graceful degradation. Publish stable error categories and where a retry is safe, but do not claim that simple TCP reconnection creates distributed at-most-once effects.
7. **Hostile-load fixtures versus kernel TCP flow control** — Challenge partial-header floods, slow readers, idle clients and oversized declarations with finite local fixtures, checking refusal, backpressure and later reclamation. Distinguish Linux TCP window/kernel buffers from the application's declared capacity; a bounded Rust Vec alone cannot establish host-wide memory bounds.

*Optional formative feedback:* Compute an upper bound for 12 accepted clients each with fixed input/output caps plus a global response queue; expose a counterexample where per-client caps alone exceed a desired total budget.

### Module 6 — Trust, Timeouts, Shutdown and Connection Failure Semantics

#### Outcomes

- SYS4-O2
- SYS4-O7
- SYS4-O10
- SYS4-O11

#### Lessons

1. **Loopback trust, authentication and TLS boundaries** — Document a loopback-only unauthenticated teaching service, distinguishing transport reachability from TLS integrity/confidentiality, authenticated identity and operation authorization. Refuse arbitrary filesystem access, shell construction or public exposure from client bytes; no live TLS or privileged deployment is a hidden prerequisite.
2. **Socket failure taxonomy and bounded error reporting** — Classify DNS/connect refusal, EOF, reset, partial frame, timeout and overload by actual observable socket/protocol state rather than universal errno assumptions. Define when a bounded error frame may be attempted and when output limits or a disconnected peer require a documented close/drop instead of promising error delivery.
3. **Idle, frame and total connection deadlines** — Use monotonic elapsed time for idle, absolute frame-assembly and response-drain policies; prove a slow trickle cannot indefinitely extend an absolute frame budget by sending one byte before each idle timeout.
4. **Graceful shutdown, signal-safe cancellation and resource ownership** — Specify stop-accepting, notification/wakeup, owned response drain or cancellation and connection close under a finite shutdown budget. Use a safe loop-driven cancellation mechanism rather than doing async-signal-unsafe work inside OS signal handlers, and trace each accepted request's final ownership state.
5. **Forced versus graceful termination** — Distinguish an orderly server drain from forcibly closing sockets or the process. Prove which accepted operations have completed by application contract and which remain ambiguous after partial or aborted response.
6. **Input and log sanitization** — Prevent allocation bombs, payload injections into log lines, lossily decoded wire identities and secret-bearing diagnostics. Use fixed label sets or bounded fields and disclose when peer addresses or raw bytes could be personal information.

*Optional formative feedback:* Design a 3-client shutdown trace including an idle peer, an incomplete request and a completed request awaiting drain. Classify each result without inventing a transactional guarantee.

### Module 7 — Protocol Verification, Hostile Clients and Deterministic Fault Injection

#### Outcomes

- SYS4-O2
- SYS4-O5
- SYS4-O6
- SYS4-O10
- SYS4-O11

#### Lessons

1. **Independent parser oracles and malformed frame corpus** — Derive independent parser/response oracles from the published byte grammar for normal, version/opcode invalid, truncated, overflowed, repeated and trailing-data cases. Verify exact rejection, resource caps and connection policy without using server-generated responses as the expected result.
2. **Fragmented streams, short I/O and deterministic fault seams** — Use controlled adapters and bounded loopback clients to split/coalesce writes, force partial read/write, WouldBlock and interrupted I/O, then verify response offsets. Explain which observed cases are deterministic synthetic faults and why application write fragmentation is not actual packet-loss injection.
3. **Slow/fast clients and overload recovery** — Coordinate at least three clients including a slow sender, slow receiver and healthy peer, checking the healthy request under a declared finite fairness budget. Exhaust admission, per-peer and global caps, then verify independently expected refusal/backpressure and recovery after a peer closes or queues drain.
4. **Half-close, reset and interrupted shutdown** — Exercise FIN before a full request, FIN after complete request, abrupt reset, interrupted output and server cancellation. Identify where application outcome is observable versus necessarily uncertain.
5. **Distinct causal hypotheses** — For a newly supplied hang, consider at least two hypotheses such as lost edge notification, incomplete framing, slow-reader output cap or blocked reactor handler; identify a discriminating trace rather than blame TCP generically.
6. **Model limits and safe isolation** — Use deterministic logical event fixtures as a first layer and finite real loopback trials as a second. Record resource ceiling, event backend and synthetic-vs-observed provenance; never require network administration or public packet interception.

*Optional formative feedback:* Make a replay file with partial frame, writable-event storm and stale socket event, then state exactly which observations a real loopback test can and cannot reproduce deterministically.

### Module 8 — Service Instrumentation, Measurement and Diagnostic Inference

#### Outcomes

- SYS4-O4
- SYS4-O8
- SYS4-O9
- SYS4-O10
- SYS4-O13

#### Lessons

1. **Bounded transition observability, correlation and privacy** — Instrument accepted/refused/active peers, parsed frames, pending bytes, deadlines, short I/O and cleanup as bounded counters with safe synthetic correlation tokens. Separate application observations from packet facts, keep labels cardinality-limited and redact raw payloads, peer identity and secrets.
2. **Compare models under one contract** — Run a bounded blocking/thread-per-client reference and the event-driven service under the same frame spec and offered workload; state which differences are architectural and which arise from implementation choices.
3. **Offered/admitted/completed load and observed latency** — Distinguish attempted, admitted, completed-on-server and client-verified results before calculating goodput, errors, response time and tail latency. Disclose the denominator and sample count, refusing a tail-percentile or success claim unsupported by actual observations or masked refusal counts.
4. **Competing hypotheses and repeated controlled trials** — Compare competing bottleneck explanations under repeated controlled useful work, with at least five raw timings per variant and CPU/OS/toolchain, queue, thread and buffer context. Report center/spread and background scheduling or allocator confounders rather than assert a single Linux kernel cause from one local timing.
5. **Regressions and postmortem evidence** — Make one targeted intervention, compare against an independent failure/regression corpus and preserve before/after event traces; describe a plausible unexcluded explanation or limitation.

*Optional formative feedback:* Given a synthetic log showing accepted connections but low completed responses, formulate two explanations and the smallest additional counters that distinguish them.

### Module 9 — Integrated Nonblocking Multi-Client Rust Service and Unseen Defense

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

1. **One real nonblocking Rust service from a public contract** — Implement one real nonblocking Rust loopback service using AS2's safe readiness backend, M2's versioned framing and explicit generation-aware connection tokens, output offsets and typed lifecycle states. Publish the small handler authority and real build instructions; do not replace actual multi-client execution with a toy simulator or second project.
2. **Integrated capacity, cancellation and multi-client fairness** — Re-use the same server with aggregate input/output limits, admission control, finite deadlines, correct registration and stop/drain behavior. Drive simultaneous fragmented, half-closed, output-flooding and healthy clients, demonstrating under defined test bounds that one slow peer cannot stall valid peers.
3. **Independent fault evidence, measurements and operator handoff** — Run independent grammar oracles, deterministic readiness histories and real loopback hostile/normal cases on the same implementation. Publish manifest/lockfile, backend/kernel assumptions, clean checkout, bounded numeric limits, raw controlled measurements, safe logs, cleanup runbook and the limits of remote delivery inferences.
4. **Unfamiliar defect diagnosis and independent defense** — For one reviewer-supplied unseen service defect, record two competing causes and a discriminating stream/readiness timeline before execution. Safely reproduce and minimally correct the fault or justify a bounded refusal, regress previously correct behavior, and defend observed versus simulated evidence without inventing complete production guarantees.

*Optional formative feedback:* Ask a reviewer to insert a write-ready storm followed by a half-close and a new socket reusing a descriptor; predict current connection state and document the one check that prevents stale-event corruption.

## Completion requirements

**Five summative assessments establish all thirteen SYS4 outcomes.** Lesson practice, optional packet captures and model-checking utilities are formative; all required behavior, evidence and review criteria are published here. AS5 assesses unfamiliar diagnosis (O13), while AS1–AS4 independently establish the other outcomes. One implementation may supply AS2's reactor, AS3's backpressure/security challenge, AS4's reproducibility and measured operation and AS5's independent defense. They are separate evaluation decisions, **not four independent server projects**. Every assessed execution must use learner-owned bounded loopback fixtures and separately specified expected results.

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
  - **Criteria:** The implementation enforces per-client **and aggregate** buffer/admission caps *before and during allocations*, with a numerical ledger for partial input frames, pending/staged responses, parser metadata and any staged or in-flight handler work. It correctly reserves/releases capacity and resumes read interest through backpressure, cancellation, partial failure and disconnect; merely setting socket backlog or truncating after collection is insufficient. Slow clients receive documented bounded backpressure, timeout, rejection or closure and do not monopolize the event loop under the published test schedule. A partial trickle cannot indefinitely extend an absolute frame assembly deadline; no trusted shell execution, arbitrary path access, sensitive log dumping or wildcard/public listener is introduced by untrusted payloads. Each refusal/error/close outcome is independently specified, testable with synthetic clients and honest about kernel-owned buffers and unobserved whole-host resource effects.
  - **Evidence:** Numeric resource/capacity ledger with worst-case arithmetic, scripted adversarial client corpus, real and synthetic admission/pressure traces, bounded allocation/counter logs, false-input tests, monitored clean-up results, refusal semantics and documented host limits.

- **SYS4-AS4** — Reproducible Service Operation, Shutdown and Measurements
  - **Outcomes:** SYS4-O4, SYS4-O7, SYS4-O9, SYS4-O10, SYS4-O12.
  - **Work:** Release the **same integrated SYS4 Rust service** with a fresh-checkout runbook, local client suite and documented bind/security policy. Perform controlled load, idle/deadline, half-close/reset, reconnection and graceful/forced stop scenarios; compare at least two offered-load conditions or the event model against a declared baseline, recording client-observed success and service-side state. Explain what happens when a request takes effect but its reply is lost.
  - **Criteria:** Toolchain, dependency versions, Linux/runtime assumptions, numeric limits and exact clean-run commands reproduce the correct documented protocol and failure matrix. Record **at least five independent trials per comparable load condition** with accepted/admitted/completed/refused counts, throughput or goodput, client-observed latencies with units, and environment/confounder notes; report center/spread and only justified tail claims. Logs/counters have bounded cardinality and avoid exposing raw sensitive frames; claims about partial completion, retry, TLS, remote availability and exactly-once effects remain bounded by actually observed/application-defined semantics. Shutdown stops admission, accounts for in-flight work, drains or explicitly drops within a declared time budget, and releases local listener/connection resources without pretending remote delivery is guaranteed.
  - **Evidence:** Complete Rust source/manifest and pinned features, clean-checkout runbook, synthetic client and fault harness, independent response oracles, raw per-trial workload/timing and result data, latency/resource summaries, privacy-safe event logs, restart/shutdown traces and qualified limitations.

- **SYS4-AS5** — Unfamiliar Multi-Client Network Defect Defense
  - **Outcomes:** SYS4-O13.
  - **Work:** Independently diagnose **one previously unseen** bounded service/network failure supplied by a reviewer or public deterministic variant rule: for example lost edge-triggered work after quota, stale-fd reuse, permanently writable interest, framing desynchronization, false DNS/IPv6 attribution, slow-client starvation or ambiguous disconnect. **Before testing**, identify two competing causal hypotheses, a stream/readiness/resource history and a discriminating observation; use synthetic and actual loopback evidence where appropriate. Make the smallest justified correction or bounded refusal, then verify earlier correct behavior. This specifically evaluates **SYS4-O13 unfamiliar causal diagnosis and defense**; a single case cannot automatically establish all distinct prior addressing, instrumentation, implementation and architecture outcomes.
  - **Criteria:** A source-consistent TCP/application/readiness/resource history identifies the violated invariant and genuinely discriminates at least two plausible causes. The bounded correction or justified refusal follows from the failure precondition and independently solved before/after results, preserving previously correct parsing, caps, fairness and cleanup. The learner distinguishes synthetic from real Linux observations, identifies untested schedules and remote-delivery limits, and defends individual reasoning. **O1/O4/O8/O9/O12 remain mandatory under AS1–AS4**, not automatically awarded from a variable-kind unfamiliar case.
  - **Evidence:** Unknown-case description/seed, pre-execution predictions, annotated packet/stream and readiness histories, discriminating tests with provenance, minimal patch or justified analysis, independent regression data, remaining limitations and a reviewable written, recorded or live defense.

### Course boundary, access and safety

Completed SEF7 already includes C/POSIX descriptor contracts, one blocking/single nonblocking TCP peer and independently tested simple framing; that work remains required **in SEF7** and receives no SYS4 transfer/automatic credit. SYS2 supplies Rust byte parsing and ownership; SYS3 supplies bounded shared-state coordination and fair work accounting; SYS10 supplies prior kernel scheduling models. SYS4 uniquely requires an **actually running, multi-client, nonblocking Rust protocol service** with honest Linux readiness semantics, bounded application resource state and independently verified failure behavior. [SYS6](SYS6.md) owns replicated state, operation identity and distributed retry/idempotency protocols; [SYS7](SYS7.md) owns deeper profiling/production tracing and causal capacity engineering; SEC owns specialist threat modeling and deployed transport security. Referencing TLS is not a claim of TLS implementation or production suitability.

All executable assessments use safe synthetic clients, local-loopback listeners and finite thread, memory and time budgets; production deployment, traffic interception, public-network scanning, kernel modifications and privileged capture are unnecessary. Any optional Linux `epoll` wrapper and dependency must be freely accessible, publicly documented and fixed to a reproducible version. Pure state diagrams, text event traces and nonvisual alternatives are valid accessibility accommodations; independence of the required server behavior and performance evidence must still be demonstrable.

### Assessment records and readiness

Records identify source revision, Linux/network test conditions, assessed outcomes, independent stream and readiness expectations, client-observed results and evaluator decision. Fault-injection and performance claims must state their limits. The course remains `draft` until learner testing and qualified review support a status change.

## Optional disciplinary references

These freely accessible sources aid research without becoming mandatory hidden materials or paid resources:

- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html) — connection behavior, byte-stream sequencing, FIN, resets and transport semantics.
- [Linux epoll(7)](https://man7.org/linux/man-pages/man7/epoll.7.html) and [epoll_ctl(2)](https://man7.org/linux/man-pages/man2/epoll_ctl.2.html) — edge/level/one-shot readiness, interest management and event-loop caveats.
- [Rust std::net::TcpStream](https://doc.rust-lang.org/stable/std/net/struct.TcpStream.html), [TcpListener](https://doc.rust-lang.org/stable/std/net/struct.TcpListener.html) and [std::io](https://doc.rust-lang.org/stable/std/io/) — real nonblocking, read/write, EOF and error contracts.
- [Mio documentation](https://docs.rs/mio/latest/mio/) — publicly available Rust readiness abstraction (an example, not the required assessment API).
- [OWASP Denial of Service Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Denial_of_Service_Cheat_Sheet.html) — application-layer exhaustion, input and timeout policies.
