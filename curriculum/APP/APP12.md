# APP12 — Realtime Systems

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `elective`
**Prerequisites:** [APP3](APP3.md) — Backend Framework Engineering, [APP5](APP5.md) — Full-Stack Application Architecture, [APP6](APP6.md) — Software Quality & Engineering Operations
**Duration:** 14–18 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–14 focused hours/week (provisional; requires independent calibration)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

**Design timely, authorized multi-user application features that remain correct when notifications are delayed, duplicated, reordered, missed or unavailable.** Measure and compare polling, Server-Sent Events and WebSockets on a real local product, then develop authoritative snapshot and versioned event synchronization, client recovery, conflict handling, continuous permissions, bounded connections and slow-client resources, ephemeral presence, fan-out failure response and accessible degraded interaction.

This is an **optional Application Engineering elective**, never a hidden APP9 graduation requirement. The approved direct prerequisites **APP3 + APP5 + APP6** remain unchanged. APP3 supplies typed, validated Fastify services, real PostgreSQL and authorization boundaries. APP5 provides integrated React/browser and backend state, authenticated user workflows, optimistic mutations and introductory polling/reconnect handling. APP6 supplies independent quality, workload and observability methods. APP12 deepens **application-level live transport, lifecycle and synchronization** rather than re-teaching introductory HTTP, the entire APP11 outbox/saga discipline, APP8 system-wide scaling or SYS consensus/distributed protocol internals. APP11, APP8 and SYS are not additional mandatory prerequisites.

**State authority first:** Use a real protected multi-user workflow, such as collaborative task status, incident updates or shared resource scheduling, built atop TypeScript React/Fastify/PostgreSQL with at least two synthetic tenants/roles. PostgreSQL remains authoritative for committed changes, resource versions and user authorization. An SSE or WebSocket notification tells a client that something may have changed; delivery itself is not proof of a durable business commit. At least one real two-client concurrent mutation, one access denial and a reconciling replay must be independently verified against SQL state.

**Transport competence without unnecessary duplication:** Compare a real conditional/short polling path with one primary fully operational SSE or WebSocket channel for the same task. Implement a *bounded working security/protocol probe* of the other streaming transport (valid SSE framing/reconnect or valid authenticated WebSocket upgrade/message/close) to demonstrate both technologies without demanding two full frontend applications. The selection depends on direction, latency, idle overhead, browser compatibility and operational cost. Standard `EventSource` provides one-way `text/event-stream` and native reconnect/optional `Last-Event-ID`, but the browser stores neither reliable business history nor permission proofs, and standard EventSource does not allow arbitrary custom Authorization headers. Browser `WebSocket` is duplex but has **no automatic receive backpressure**, and browser JavaScript cannot send WebSocket Ping control frames. Nonstandard experimental `WebSocketStream` is not a required platform.

**Ordered state, not imagined guarantees:** Design a stable server-issued per-resource/room version and stream epoch, event ID and authorized replay retention floor. Document which events may be duplicate, reordered or dropped. A disconnected client can safely resume from an authorized retained cursor or abandon stale replay and take a fresh authorized snapshot. A naive `fetch snapshot → subscribe` may miss a commit between steps; reproduce and resolve this using an explicit watermark-plus-replay or subscribe-buffer-snapshot contract. No ordinary socket or timestamp implies global total order, exactly-once business effects or instantaneous cross-device convergence. Use server-side revision checks for simultaneous edits; evaluate OT and CRDT design choices but do not require implementing a full collaborative text engine.

**Continuous trust:** Check session, Origin, room/tenant/resource, action and replay cursor permissions at their actual live boundaries, not merely at successful initial connection. Revalidate appropriately when roles change, a session expires or a client switches identity. Close/abort React listeners on route change, logout or page lifecycle where appropriate. Keep private room content, raw authentication tokens and presence data out of cross-tenant logs, shared caches and unaudited event payloads.

**Explicit bounded failure behavior:** Configure connection/subscription budgets, incoming message sizes and rates, outgoing per-client queue bytes and a finite overflow policy. A slow reader may receive coalesced disposable notifications or be disconnected and required to resync from PostgreSQL. Background visibility throttling, server-side Ping/Pong, application heartbeats, proxy idle timeouts and reconnect jitter have distinct behavior. Reboot a controlled local fan-out/notification process and prove database truth survives despite ephemeral update loss; this is **not** a claim about multi-region partitions or a managed broker.

**Privacy and accessible collaboration:** Presence, typing and cursor indicators are approximate scoped lease-based hints, not proof that a person is online or attending. Provide accessible keyboard/focus and moderated live status, honest offline/stale/conflict/pending states and usable manual refresh for intermittent connections. Avoid personal telemetry or actual user credentials; tests target owned disposable local endpoints and synthetic tenants only. Latency and capacity measurements disclose client/server clock assumptions, hardware, sample counts, transport errors and test-tool limitations.

**Free reproducible study:** A pinned Node/TypeScript/Fastify and React toolchain, local PostgreSQL, browser DevTools and free HTTP/WebSocket clients plus a restartable local fan-out fixture are sufficient. Initial free provisioning can fetch dependencies, but assessed runs must use documented local inputs. No paid queue or broker, cloud account, public DNS, cross-region cluster, required participant panel or proprietary monitoring platform is necessary.

The **17 learning outcomes** flow through 15 varied modules and **six required cumulative summative assessments**. Other exercises are formative. The 14–18-week duration and workload estimates are provisional. Structural parser success does not confer learner-tested or officially verified educational readiness.

## Learning outcomes

- **APP12-O1:** Select a realtime delivery model for a bounded user task by comparing freshness, interaction direction, retention, connection cost, privacy and offline behavior, and defend polling, SSE, WebSocket or a justified alternative.
- **APP12-O2:** Implement and measure at least two locally running delivery approaches under matched resource, failure and workload conditions, separating transport properties from durable business state guarantees.
- **APP12-O3:** Implement standards-aware SSE framing, named events, event IDs and native EventSource reconnect, with a secure bounded application-level replay or snapshot fallback for invalid, expired or unauthorized Last-Event-ID cursors.
- **APP12-O4:** Implement and examine a secure browser WebSocket channel with valid origin and authenticated upgrade policy, runtime-validated bidirectional application messages, scoped actions, payload limits and correct connection/close semantics.
- **APP12-O5:** Define stream/resource identity, epochs, per-key ordering and server-issued sequence/cursor scope, replay/retention windows and documented lost/duplicated/out-of-order behavior without promising global total order or exactly-once delivery.
- **APP12-O6:** Build a race-free snapshot-to-stream or subscribe-and-buffer bootstrap that resolves changes committed during handoff, rejects stale/gap deltas and reconciles the client to authoritative PostgreSQL state.
- **APP12-O7:** Implement React/browser realtime synchronization state and lifecycle for reconnect, replay, pending/unknown commit, account switching, deduplication and accessible stale/offline/forbidden/conflict states.
- **APP12-O8:** Enforce concurrent client edits through real PostgreSQL state/version checks and explicit domain conflict or merge policy, comparing simple authoritative revision checks with OT/CRDT alternatives without requiring an entire CRDT implementation.
- **APP12-O9:** Verify authentication, origin, room/resource/tenant and per-action permissions throughout stream/WS subscription, event replay and live session revocation, preventing cross-tenant disclosures after identity changes.
- **APP12-O10:** Manage finite browser/server connection lifecycles: React Effect teardown, tab/page visibility, proxy timeouts, heartbeats, reconnect/backoff/jitter and cleanup; distinguish browser WS APIs from server control-frame Ping/Pong capabilities.
- **APP12-O11:** Prevent slow clients and abusive publishers from exhausting memory, CPU or network through bounded send queues, fan-out, incoming bytes, connection/room limits, rate quotas and honest coalesce/disconnect/resync policy.
- **APP12-O12:** Model ephemeral presence, typing and cursors with authorized scoped leases, expiry, multi-tab disconnect semantics, privacy and accessible alternative indications instead of treating presence as a guaranteed durable fact.
- **APP12-O13:** Compare one-process fan-out with an optional restartable local process/broker adapter; demonstrate lost ephemeral notifications under notification-layer failure and recovery to unchanged durable state.
- **APP12-O14:** Instrument and interpret privacy-safe connection, stream, event freshness, cursor gaps, replay time, delivery failures, slow readers and user-task success, with clock-skew, sample size and instrumentation limits disclosed.
- **APP12-O15:** Test multi-client sync correctness against real local services under controlled missing/duplicated/reordered events, expired cursors, role revocation, network interruptions, reconnect storms, broker/fan-out restarts and contention.
- **APP12-O16:** Maintain inclusive and privacy-aware realtime interaction: keyboard/focus, restrained live announcements, readable stale/pending/conflict recovery, protected data retention and a usable slower/manual fallback.
- **APP12-O17:** Deliver and independently defend a reproducible, secure and recoverable realtime feature under an unfamiliar bounded stream, race, permission, reconnection, slow-consumer or process failure while documenting measured trade-offs.

## Modules

### Module 1 — Realtime as a User and State Correctness Problem

#### Outcomes

- APP12-O1
- APP12-O2
- APP12-O5
- APP12-O16

#### Lessons

1. **Course scope and historical context** — Contrast polling, long polling, push, collaboration and event streaming as product responses rather than fashionable infrastructure.

2. **Define a credible user task** — Choose a protected shared workflow where stale status or slow updates matter to users.

3. **Authoritative facts versus signals** — Model PostgreSQL commits as truth and push events as possibly delayed notifications.

4. **Freshness and response objectives** — State eligible state-change tasks, target age, delays, permissions and user-visible fallback.

5. **Data and permission invariants** — Describe what may never be exposed, duplicated, overwritten or silently acknowledged.

6. **Reasonable workload envelopes** — Define synthetic tenants, update frequency, idle periods and controlled failure limits.

7. **Architecture and trust map** — Locate browser, Fastify, SQL and notification process boundaries and who owns each action.

8. **Independent local test harness** — Pin free tools, browser versions, synthetic data, real ports and disposable resources.

*Optional practice — contract critique:* Reject claims that an open socket implies durable delivery, universal order or human attention.

### Module 2 — Polling, HTTP Long Polling and Streaming Trade-offs

#### Outcomes

- APP12-O1
- APP12-O2
- APP12-O3
- APP12-O4
- APP12-O14

#### Lessons

1. **Conditional short polling** — Build ETag or version-based checks and measure empty requests and freshness.

2. **Long-polling response lifecycle** — Observe server pending wait, timeout, cancel, reconnection and operational resource cost.

3. **SSE one-way streams** — Explain HTTP text/event-stream with a server-to-client update channel and ordinary mutation endpoints.

4. **WebSocket duplex channels** — Inspect HTTP upgrade, WSS origin, framing, close and independent command/notification flow.

5. **Proxy and connection considerations** — Evaluate idle timeouts, buffering and HTTP/1 tab connection limits versus HTTP/2 stream support.

6. **Matched workload comparison** — Compare actual update delay, bytes, open connections, CPU and errors under idle and burst load.

7. **Correct failure interpretation** — Distinguish lost notification, rejected command, delayed request and persistent SQL state.

8. **Browser API capability limits** — Compare EventSource header/credential constraints and browser WebSocket no built-in receive backpressure.

*Optional practice — transport decision:* Select the least costly sufficient option and define what evidence would justify switching.

### Module 3 — SSE Framing, Last-Event-ID and Authorized Resume

#### Outcomes

- APP12-O2
- APP12-O3
- APP12-O5
- APP12-O6
- APP12-O9

#### Lessons

1. **Correct stream response** — Emit UTF-8 text/event-stream with proper event/data/id/retry fields and blank-line dispatch.

2. **Named events and payload validation** — Separate native stream parsing from typed application event schema enforcement.

3. **EventSource native reconnect** — Observe browser-managed retry and Last-Event-ID after an actual interrupted SSE connection.

4. **Authorized Resume Cursors and Replay** — Bind last-event cursors to tenant/room/version and reject mismatched or malformed input; replay events still available within explicit server retention without depending on browser memory.

5. **Expired or invalid cursor** — Reject an unfulfillable replay gap and require fresh authorized snapshot resync.

6. **Proxy flushing and keepalives** — Exercise comment heartbeats, buffering, idle closes and cancellation with local settings.

7. **Session expiry during a stream** — Close or block invalid subscriptions and verify old cursor cannot disclose a revoked resource.

*Optional practice — foreign-room resume:* Demonstrate unauthorized Last-Event-ID misuse then repair cursor scope and fallback.

### Module 4 — WebSocket Upgrade, Framing and Persistent Command Security

#### Outcomes

- APP12-O2
- APP12-O4
- APP12-O9
- APP12-O10
- APP12-O11

#### Lessons

1. **Inspect real HTTP upgrade** — Enforce explicit trusted Origin and appropriate authenticated cookie/token session handling.

2. **Typed messages with bounded frames** — Validate application type, schema, resource and maximum bytes before processing.

3. **Transport connection versus permission** — Distinguish accepted socket, authenticated user and authorized room/action.

4. **Browser protocol capabilities** — Explain readyState, bufferedAmount, close codes and no JS Ping control-frame API.

5. **Server Ping/Pong and client heartbeat** — Compare server-side protocol liveness with optional application-level status heartbeat.

6. **Subscribe and unsubscribe transitions** — Limit per-connection rooms and remove abandoned memberships after close or logout.

7. **Publish action and acknowledgement** — Clearly differentiate accepted request, committed mutation and delivered notification.

8. **Error, timeout and cleanup** — Handle malformed payloads, close, session expiry, route navigation and resource release.

*Optional practice — forged publish:* Reject a syntactically valid WebSocket message attempting a forbidden tenant action.

### Module 5 — Event Identity, Ordering Domains and Delivery Contracts

#### Outcomes

- APP12-O3
- APP12-O4
- APP12-O5
- APP12-O6
- APP12-O7

#### Lessons

1. **Event versus authoritative record** — Use durable resource revisions to identify what a notification actually represents.

2. **Stream envelope design** — Define event ID, schema version, room/tenant, aggregate revision and safe payload fields.

3. **Monotonic per-resource sequence** — Use committed server-issued version rather than client timestamps for ordering.

4. **Duplicate and missing versions** — Exercise repeated events, skipped events, delayed earlier versions and correction logic.

5. **Epoch and stream restart semantics** — Avoid reused or incomparable sequence IDs after process restart or room recreation.

6. **Replay limits and retention** — Define earliest/latest cursor and exact conditions requiring a full snapshot.

7. **At-most and at-least-once boundaries** — Describe best-effort push, replayable reads and server-command idempotency distinctly.

8. **Clock skew and causality** — Demonstrate why browser wall-clock time cannot prove total order or one-way latency.

*Optional practice — stale overwrite:* Prevent an old notification from replacing a newer committed version in client state.

### Module 6 — Snapshot, Delta and Bootstrap Race-Free Synchronization

#### Outcomes

- APP12-O5
- APP12-O6
- APP12-O7
- APP12-O8
- APP12-O15

#### Lessons

1. **Authorized initial state** — Read room/tenant-scoped snapshot and a server-authoritative revision or watermark.

2. **Snapshot-to-subscribe race** — Induce a mutation between snapshot and stream registration and inspect the missing update.

3. **Buffered subscribe-first strategy** — Register a stream before snapshot then apply buffered deltas past the snapshot version.

4. **Replay-after-watermark strategy** — Obtain a consistent snapshot revision and replay all subsequent retained authorized events.

5. **Ordered delta application** — Reject wrong stream epochs and gaps, and avoid applying stale out-of-order changes.

6. **Snapshot replacement vs patch** — Compare full authorized refetch against carefully versioned incremental updates.

7. **Retention gap and recovery** — Signal incomplete replay and securely replace state rather than silently skipping commits.

8. **Cross-account and page switch** — Cancel old reads and streams and ignore late events from prior generation identifiers.

*Optional practice — convergence proof:* Verify multiple clients match independent PostgreSQL after a forced bootstrap gap.

### Module 7 — React Synchronization, Reconnect and Offline Lifecycle

#### Outcomes

- APP12-O5
- APP12-O6
- APP12-O7
- APP12-O10
- APP12-O16

#### Lessons

1. **Explicit browser sync state** — Model disconnected, connecting, live, catching-up, stale, forbidden and permanently failed states.

2. **React Effect cleanup** — Own subscriptions by user/room and avoid duplicate sockets after rerender or Strict Mode setup.

3. **Backoff and reconnect jitter** — Bound retries and honor native EventSource behavior separately from custom WebSocket logic.

4. **Stale async result guards** — Ignore fetch and stream results tied to old tenant, route, authentication or generation.

5. **Pending and uncertain mutations** — Reflect accepted, pending, committed, rejected and unknown outcomes without false success.

6. **Page visibility and bfcache** — Evaluate background throttling, pagehide/pageshow and transport restoration in supported browsers.

7. **Offline/manual fallback** — Provide accessible refresh or polling when live updates cannot connect.

8. **Session expiration and logout** — Stop replaying protected data and re-bootstrap after current valid authorization.

*Optional practice — duplicate-subscription defect:* Repair a React lifecycle issue creating multiple stale streams after navigation.

### Module 8 — Concurrent Collaborative Edits and Conflict Semantics

#### Outcomes

- APP12-O6
- APP12-O7
- APP12-O8
- APP12-O15
- APP12-O16

#### Lessons

1. **Authoritative update with revision** — Use a server-side resource version/If-Match or equivalent compare-and-set contract.

2. **Real competing clients** — Submit simultaneous valid actions through separate HTTP sessions and observe real PostgreSQL outcomes.

3. **Meaningful conflict responses** — Report 409/412 or documented domain conflict and preserve the attempted edit.

4. **Idempotent operation identity** — Bind mutation retry IDs to validated principal, resource and content.

5. **Domain merge versus rejection** — Choose appropriate field merge, append-only event or explicit user conflict.

6. **Limitations of last-write-wins** — Show timestamp/order assumptions that silently lose work or override a valid change.

7. **OT and CRDT design comparison** — Explain where automatic convergence helps and what additional complexity/metadata it requires.

8. **Out-of-order command acknowledgements** — Prevent delayed events from overriding a more recent confirmed user revision.

*Optional practice — two-user recovery:* Demonstrate a conflict and reconcile both clients without inventing missing updates.

### Module 9 — Origin, Room Permissions and Live Security Revocation

#### Outcomes

- APP12-O4
- APP12-O7
- APP12-O9
- APP12-O10
- APP12-O15

#### Lessons

1. **Handshake and Origin defense** — Test cross-site WebSocket handshake and cookie-session trust against an allowlist.

2. **Room and resource subscriptions** — Check user/tenant membership independently for initial join and every replay request.

3. **Per-message publish rights** — Verify current server-side action/object/field permissions on each incoming message.

4. **Session revoke while connected** — Recheck current rights or close protected streams after logout, expiry and privilege change.

5. **Untrusted cursor and room IDs** — Validate forged, oversized, stale and cross-tenant stream cursors and room identifiers.

6. **Service trust versus user claims** — Do not authorize based solely on forwarded client headers or message fields.

7. **Connection floods and message size** — Apply bounded unauthorized handshake, frame, room and rate policies.

8. **Privacy-safe event and audit payload** — Keep protected fields, raw auth tokens and private presence out of unauthorized logs.

*Optional practice — cross-tenant leak:* Seed a guessed room subscription and prove it produces no protected event or DB effect.

### Module 10 — Backpressure, Slow Readers and Abuse-Resistant Fan-out

#### Outcomes

- APP12-O2
- APP12-O4
- APP12-O10
- APP12-O11
- APP12-O14
- APP12-O15

#### Lessons

1. **Native WebSocket backpressure limits** — Demonstrate why browser WebSocket lacks automatic receiving flow control.

2. **Bounded outgoing queues** — Limit per-client bytes/messages and report explicit overflow action.

3. **Send buffering and drain** — Inspect server write pressure and browser bufferedAmount with documented API limitations.

4. **Fair work across tenants** — Prevent one hot room or unauthenticated source from exhausting peer capacity.

5. **Publish and payload quotas** — Limit frames, requests, event-size, room-count and parser work before expensive fan-out.

6. **Slow-client injection** — Pause a subscriber and inspect queue bytes, disconnect/recovery and unaffected legitimate clients.

7. **SSE server-write backpressure** — Respect drain, cancellation and finite pending events with a local proxy where applicable.

8. **Coalescing versus durable commands** — Drop replaceable notifications only when a snapshot can recover persisted business state.

*Optional practice — overflow diagnosis:* Fix memory growth from a disconnected subscriber retaining an unlimited stream buffer.

### Module 11 — Ephemeral Presence and Typing as Lease-Based Hints

#### Outcomes

- APP12-O10
- APP12-O11
- APP12-O12
- APP12-O16

#### Lessons

1. **Presence is not guaranteed attention** — Define recent validated activity rather than definitive human online status.

2. **Lease renewal and expiry** — Model join, refresh, timeout, disconnect and crash with finite server-managed TTL.

3. **Multiple tabs and identities** — Aggregate approved connections carefully without marking a user absent after one tab closes.

4. **Protocol heartbeat versus app liveness** — Distinguish browser limitations, server Ping/Pong and client-visible status.

5. **Throttled ephemeral typing** — Limit per-room rates and avoid persisting private draft text in notification history.

6. **Ghost users and clock assumptions** — Test network loss, sleep and missed disconnect against expiration semantics.

7. **Presence privacy and consent** — Broadcast only legitimately needed activity to currently authorized participants.

8. **Accessible lower-rate alternatives** — Offer textual state and manual refresh without flickering or endless announcements.

*Optional practice — ghost-presence repair:* Correct a stale member list after a sudden disconnected or terminated process.

### Module 12 — Fan-out Topologies, Broker/Process Loss and Recovery

#### Outcomes

- APP12-O2
- APP12-O5
- APP12-O11
- APP12-O13
- APP12-O14
- APP12-O15

#### Lessons

1. **Single-process room registry** — Implement local subscription index and distinguish memory-resident updates from SQL facts.

2. **Multiple server instances and routing** — Explain sticky connections, node ownership and why in-memory fan-out does not cross processes.

3. **Optional local broker comparison** — Use controlled in-memory adapter or free local pub/sub service without paid requirements.

4. **Loss of notification process** — Stop an independently restartable fan-out component while PostgreSQL commits correct state.

5. **Replay or snapshot after restart** — Recover clients via authorized revisions rather than claiming lost ephemeral events were delivered.

6. **Cross-process ID propagation** — Preserve per-room versions and trace IDs without assuming global ordering.

7. **Reconnect surge handling** — Bound admission, replay work and jitter under a synchronized network restart.

8. **Topology and maintenance cost** — Compare sockets, DB connections, proxy limits, incident labor and monitoring complexity.

*Optional practice — no-broker decision:* Show why simpler polling or one-process SSE can be optimal for the actual use case.

### Module 13 — Observability, Clock Limits and Failure Test Methodology

#### Outcomes

- APP12-O1
- APP12-O5
- APP12-O9
- APP12-O11
- APP12-O14
- APP12-O15

#### Lessons

1. **User-centered freshness metrics** — Measure actual correct client state age and successful user task rather than only open sockets.

2. **Event delivery timing caveats** — Separate same-process monotonic durations from clock-skewed browser/server wall time.

3. **Gap, replay and stream metrics** — Record current cursor, retained floor, resync duration and failed catch-up reasons.

4. **Security and bounded-buffer counters** — Track rejected subscriptions, auth expiry, slow readers and queue occupancy safely.

5. **Controlled failure matrix** — Inject delayed, missing, duplicate and reordered messages plus wrong identities and role change.

6. **Independent multi-client DB tests** — Compare two browser clients, two tenants and authoritative SQL after each injected fault.

7. **Reconnect storm scenario** — Produce finite synchronized reconnect attempts and measure resources, failure rates and convergence.

8. **Privacy-aware fixture and logs** — Seed synthetic records and redact IDs/tokens/content while preserving diagnostic correlation.

*Optional practice — false-green monitor:* Catch a metrics page reporting healthy sockets despite stale or unauthorized room state.

### Module 14 — Accessible Collaboration, Privacy and Operations

#### Outcomes

- APP12-O1
- APP12-O7
- APP12-O9
- APP12-O12
- APP12-O14
- APP12-O16

#### Lessons

1. **Manual and low-bandwidth interaction** — Preserve meaningful application use when realtime transport is absent.

2. **Moderate live-region announcements** — Prioritize significant status updates without screen-reader or focus overload.

3. **Pending, stale and conflicting content** — Show correct user-facing language and keyboard-accessible action to reconcile.

4. **Presence disclosure limits** — Scope typing/cursor/online information to authorized participants and legitimate product need.

5. **Logout, account swap and multi-tab privacy** — Stop previous streams and remove sensitive cached or replayed state.

6. **Retention and participant consent** — Declare event history and telemetry periods, minimizing personal activity trails.

7. **Bandwidth and CPU trade-offs** — Compare per-keystroke push with batched, throttled or pull-based decisions.

8. **Operator recovery instructions** — Document diagnosing room leaks, cursor expiry, proxy close and broker/notification outage.

*Optional practice — deceptive success badge:* Fix UI claiming a write committed merely because a push notification arrived.

### Module 15 — Integrated Recoverable Realtime Feature and Defense

#### Outcomes

- APP12-O1
- APP12-O2
- APP12-O3
- APP12-O4
- APP12-O5
- APP12-O6
- APP12-O7
- APP12-O8
- APP12-O9
- APP12-O10
- APP12-O11
- APP12-O12
- APP12-O13
- APP12-O14
- APP12-O15
- APP12-O16
- APP12-O17

#### Lessons

1. **Choose a shared authorized product task** — Extend APP5 real React/Fastify/PostgreSQL with a justified freshness requirement.

2. **Implement comparable transports** — Run polling plus a primary SSE or WebSocket path and a bounded security/protocol probe of the other.

3. **Declare authorized stream contract** — Publish room/tenant identity, version, epoch, snapshot watermark, retention and gap behavior.

4. **Secure connect and message actions** — Verify Origin, session, live room permission, per-command trust and logout cleanup.

5. **Demonstrate race-safe bootstrap** — Inject a commit between snapshot and subscription and recover it exactly by versioned authority.

6. **Prove multi-client convergence** — Force missed/duplicate/out-of-order notifications, cursor expiry and identity change.

7. **Test concurrent editing semantics** — Use separate real sessions/SQL to show conflicts and accessible non-lossy reconciliation.

8. **Protect slow peers and resource limits** — Bound buffers, payloads, room membership, retry and tenant quotas under bursts.

9. **Test approximate presence and lifecycle** — Observe multi-tab lease expiration and private activity controls after a sudden close.

10. **Interrupt push/fan-out and restore** — Restart a real local notification layer while persistent state remains correct.

11. **Compare observability and UX costs** — Inspect user-state freshness, resource and errors, accessibility, privacy and operating trade-offs.

12. **Handle unfamiliar bounded failure** — Diagnose or correct a new stream, race, room authorization, slow reader or reconnect incident.

## Completion requirements

All **APP12-O1–APP12-O17** must be substantiated through the **six mandatory summative assessments**. One coherent APP5 application and controlled independent local notification process may supply evidence for all six. Practice lessons, transport experiments and optional technologies are formative except where specifically required in a public summative assessment; there are no unpublished graduation gates.

| Required assessment | Required outcome coverage | Principal evidence |
| --- | --- | --- |
| `APP12-AS1` — Working Transport Comparison and Standards-Aware Protocols | APP12-O1, APP12-O2, APP12-O3, APP12-O4, APP12-O14 | Versioned local React/HTTP/stream source, fixture and pinned versions, browser/network trace of polling and primary stream, bounded secondary protocol probe, local traffic/latency/byte/CPU/resource/error comparison, actual SQL observations, architecture decision and known limitations |
| `APP12-AS2` — Authoritative Snapshot, Gap-Replay and Concurrent Client Convergence | APP12-O5, APP12-O6, APP12-O7, APP12-O8, APP12-O15, APP12-O16 | Snapshot and stream cursor/epoch contract, server-side sequence/retention policy, two-client deterministic fault schedule, tests of bootstrap race and out-of-order/expired/gap inputs, conflict HTTP/DB logs, authorized final-state comparison, screenshots/transcripts of accessible recovery and limitation notes |
| `APP12-AS3` — Live Authorization, Connection Lifecycle and Cross-Tenant Attack Resistance | APP12-O3, APP12-O4, APP12-O7, APP12-O9, APP12-O10, APP12-O15, APP12-O16 | Origin and authentication configuration, versioned subscription/WS command contracts, multi-tenant/role/revocation threat matrix and independent rejected requests, actual server registry and React effect traces, authorized/denied DB inspection, multi-tab/logout/timeout transcript and redacted log evidence |
| `APP12-AS4` — Bounded Fan-out, Slow Consumers, Ephemeral Presence and Process Restart | APP12-O2, APP12-O10, APP12-O11, APP12-O12, APP12-O13, APP12-O14, APP12-O15 | Local fan-out/optional broker and worker configuration, load and slow-reader schedule, byte/connection/resource/latency graphs or logs, lease-state/multi-tab evidence, real process stop/start and SQL state before/after, convergence tests, security/privacy checks and resource cost rationale |
| `APP12-AS5` — Privacy-Safe Observability, Reconnect Storm and Accessible Degradation | APP12-O1, APP12-O9, APP12-O10, APP12-O11, APP12-O12, APP12-O14, APP12-O15, APP12-O16 | Instrumented server/client and privacy audit, measure definitions and clock/source limitations, reproducible reconnect test profiles, buffer/connection/freshness metrics with errors and sample counts, access-control failure matrix, accessible UX observations and short operator recovery instructions |
| `APP12-AS6` — Integrated Recoverable Realtime Feature and Independent Technical Defense | APP12-O1, APP12-O2, APP12-O3, APP12-O4, APP12-O5, APP12-O6, APP12-O7, APP12-O8, APP12-O9, APP12-O10, APP12-O11, APP12-O12, APP12-O13, APP12-O14, APP12-O15, APP12-O16, APP12-O17 | Complete source/lockfiles and starter instructions, protocol/authority/threat/replay documents, reproducible two-tenant browser and SQL fixtures, bootstrap/cursor/concurrency/auth/slow-consumer/reconnect tests and traces, actual fan-out restart and recovered client state, privacy/UX/runbook and cost decision, unfamiliar review diff/tests and accessible technical defense |

### Shared independent technical and educational boundaries

- Record a runnable versioned TypeScript/Node/Fastify, React, actual PostgreSQL and locally controlled transport fixture, browser/runtime versions, synthetic user and tenant data, reproducible faults, CPU/network limits, cleanup and privacy boundaries. Initial free dependencies may be downloaded, but assessments must be reproducible using disclosed locally available inputs and no required paid account, managed broker or public deployment.
- Implement **polling plus one working primary SSE or WebSocket** transport and a **narrow independently executable security/protocol probe** of the other stream type. Two complete application architectures are not required. Observe actual browser/HTTP/WS traffic and compare real user-task/freshness behavior, latency, errors and resource consumption under controlled load.
- For SSE, implement real correct UTF-8 `text/event-stream` framing, native reconnect and optional `Last-Event-ID`; test the server's **independent** bounded retained replay or snapshot fallback and current cursor/tenant authorization. Standard `EventSource` does not support arbitrary request headers and cannot by itself supply durable event history. For browser WebSocket, inspect the real authenticated Origin/upgrade and action/message schema, appropriate close/error semantics and finite buffers; do not claim browser JavaScript emits protocol Ping frames or native automatic receive backpressure.
- Prove a **snapshot-subscribe race** in the original naive design and its correction through a consistent watermark/replay boundary or subscribe-buffer-snapshot policy. Simulate and detect duplicate, out-of-order, delayed, missing, wrong stream-epoch and expired cursors; final client views must reconcile with independent real PostgreSQL authorization and durable data. No global event ordering or exactly-once business effects are silently assumed.
- Enforce two-client concurrent edits against actual server revisions and PostgreSQL constraints, distinguish conflict rejection/merge from silent last-writer-wins loss, and present accessible current-versus-draft resolution. Understanding OT/CRDT design options is educational; implementing a full rich-text convergence algorithm is not a requirement.
- Check current Origin, user/session, room, tenant, resource, action, fields, replay and subscriber rights at actual boundaries; include forgery, account switch, logout, role revocation and terminal unauthorized reconnect tests. Never infer continued authorization merely from a previously authenticated socket or user-supplied room field.
- Put explicit limits on connections per tenant, room subscriptions, incoming bytes/rates, outbound queue bytes, retry work and fan-out memory/CPU. Reproduce a slow reader and a reconnect burst; choose honest coalescing, a bounded disconnect-and-resync or a documented alternate policy. A notification may be dropped if authoritative business state can be safely recovered, but a committed database write may not be silently discarded.
- Exercise React Effect and browser page cleanup, canceled or delayed connections, visibility/bfcache where supported, server application heartbeat, proxy idle close and bounded jitter/backoff; separate actual test findings from platform-independent guarantees.
- Treat online presence, typing and cursor hints as ephemeral, consent/privacy constrained, approximate leases; test expiration, multi-tab and abrupt disconnection. They cannot act as role/identity authority or imply certain user attention.
- Run an actual locally controlled notification/fan-out **process interruption** while PostgreSQL commits a domain change, and prove clients regain correct state via authorized snapshot/replay. In-process local pub/sub and mock external brokers are acceptable when labeled; no multi-region replication, distributed consensus or paid realtime provider is a completion condition.
- Report useful user-task freshness, replay gap/resync and connection/resource metrics with declared sample/window, browser support and clock-skew limits; avoid raw credentials, private message payloads, identifying URLs and unlimited presence history in telemetry. One-way client/server timing cannot be declared exact without trustworthy synchronized clocks.
- Preserve keyboard/focus, sensible live-region announcements, understandable pending/unknown/offline/stale/conflict/forbidden state and a usable manual refresh fallback. Realtime speed never compensates for broken accessibility, isolation, data correctness or untruthful status.
- Run security and load/fault tests only against learner-owned, synthetic, bounded localhost services, databases and clients. Never attack or overload third-party realtime systems or collect private user activity without authorization.
- An independent reviewer may supply an unfamiliar **bounded** cursor, session, permission, version, reconnect, slow-consumer, process-failure or accessibility case from published outcomes. The same evaluation may be defended accessibly in written, recorded, live or equivalent inspectable form, without secret technology or commercial infrastructure demands.

### Required summative assessments

- **APP12-AS1** (required working transport comparison and standards-aware protocols)
  - Outcomes: APP12-O1, APP12-O2, APP12-O3, APP12-O4, APP12-O14
  - Work: Choose one legitimate authenticated APP5 user task and implement an actual conditional/short polling path plus one primary production-style **SSE or WebSocket** notification path. Also demonstrate a narrow locally working probe of the *other* streaming protocol: a valid SSE event frame, reconnect and Last-Event-ID, or a valid WebSocket upgrade, authorized schema-checked exchange and close. Compare idle and burst behavior with real browser/server observations and independent SQL state. Report directionality, origin/session/credential capabilities, measured update delay, requests/bytes, server connection resources, disconnects and task correctness under declared profiles.
  - Criteria: At least two real alternative transport paths plus the bounded other-protocol probe are independently executable; diagrams or mocked callbacks alone do not pass. SSE framing/Last-Event-ID and WS origin/upgrade/message boundaries are correct as applicable, and a browser's lack of WS receive backpressure/control Ping access is recognized. No claim that pushing a notification commits SQL, that TBT/performance metrics prove user freshness, or that a transport guarantees exactly-once delivery. Evidence preserves protected task access, browser compatibility notes, meaningful sampling and a justified choice.
  - Evidence: Versioned local React/HTTP/stream source, fixture and pinned versions, browser/network trace of polling and primary stream, bounded secondary protocol probe, local traffic/latency/byte/CPU/resource/error comparison, actual SQL observations, architecture decision and known limitations.

- **APP12-AS2** (required authoritative snapshot, gap-replay and concurrent client convergence)
  - Outcomes: APP12-O5, APP12-O6, APP12-O7, APP12-O8, APP12-O15, APP12-O16
  - Work: Implement a protected PostgreSQL-backed shared resource, server-issued scoped stream epoch/version/cursor, authenticated snapshot endpoint and versioned update notification. Reproduce the race between snapshot read and subscription; choose and prove a reliable watermark-plus-replay or subscribe-buffer-snapshot handoff. Inject duplicate, delayed, missing, reordered and expired/foreign-epoch events, change room/identity, and submit conflicting edits simultaneously from two independent clients with real server-side revision checks. Restore correct client state via allowed retained events or fresh protected snapshot and report conflict/pending/stale status accessibly.
  - Criteria: An independent test exposes the original bootstrap race and shows the repaired handoff preserves the final committed version even with intervening writes. Replay does not leak another tenant and cannot silently resume from an expired cursor, overwrite a newer version or conceal a gap. Actual PostgreSQL revisions and two real HTTP/browser clients establish final authorized domain invariants, with a meaningful 409/412 or documented merge behavior and no duplicate business effect after uncertain acknowledgement. Clients converge to independently observed DB truth, with honest user feedback.
  - Evidence: Snapshot and stream cursor/epoch contract, server-side sequence/retention policy, two-client deterministic fault schedule, tests of bootstrap race and out-of-order/expired/gap inputs, conflict HTTP/DB logs, authorized final-state comparison, screenshots/transcripts of accessible recovery and limitation notes.

- **APP12-AS3** (required live authorization, connection lifecycle and cross-tenant attack resistance)
  - Outcomes: APP12-O3, APP12-O4, APP12-O7, APP12-O9, APP12-O10, APP12-O15, APP12-O16
  - Work: Implement actual authenticated persistent streams and controlled protected rooms/subscriptions, with finite connection/room budgets, React lifecycle cleanup and server-side permission revalidation. Exercise wrong Origin where applicable, anonymous and expired clients, forged room/tenant IDs, unauthorized SSE replay cursors, WS publish/subscribe attempts and forbidden object/action/field operations. Change role or revoke the session while still connected; switch account/tenant and navigate between React routes; use multiple tabs and a local idle/disconnect trigger. Capture independent HTTP/WS/SQL checks and real server registry/cleanup measurements.
  - Criteria: A valid initial connection does not grant subsequent unauthorized publish, subscribe, replay, or data access. Wrong-tenant, wrong-role, forged cursor and revoked identities cannot receive protected events, including delayed events from a prior browser generation. Handshake Origin and session authority are explicitly tested with an appropriate browser/client, and all application messages require schema/size validation. Cleanup closes inappropriate streams, releases listener/room registrations, and avoids duplicate subscriptions or infinite unauthorized reconnect loops; claims about browser Ping and proxy behavior stay within tested support. UI status and permitted recovery remain accessible.
  - Evidence: Origin and authentication configuration, versioned subscription/WS command contracts, multi-tenant/role/revocation threat matrix and independent rejected requests, actual server registry and React effect traces, authorized/denied DB inspection, multi-tab/logout/timeout transcript and redacted log evidence.

- **APP12-AS4** (required bounded fan-out, slow consumers, ephemeral presence and process restart)
  - Outcomes: APP12-O2, APP12-O10, APP12-O11, APP12-O12, APP12-O13, APP12-O14, APP12-O15
  - Work: Run controlled authorized local clients with one deliberately slow or paused reader, a bursty publisher, a second healthy tenant and two tabs representing one identity. Establish and test finite send-buffer/message/connection/room/publish limits with a deliberate coalesce/disconnect-and-resync policy. Implement an ephemeral protected presence or typing lease, including abrupt close, missed heartbeat and TTL expiry; preserve accessibility and privacy. Stop and restart an independently controlled notification/fan-out process or isolated process adapter while actual PostgreSQL commits a domain update; show healthy users recover via authorized replay or snapshot without treating transient events as durable.
  - Criteria: Queued outbound work and memory are bounded and slow/noisy clients cannot exhaust all healthy tenant capacity under the declared test budget. Any dropped/coalesced notifications are explicitly replaceable or safely recovered from authority; protected business mutation is never discarded merely to preserve socket throughput. Presence remains approximate under multi-tab and crash and cannot be used as an authorization source or disclosed to unauthorized users. A true local process interruption is observed, followed by independent DB/client state recovery and transparent topology/broker limitations; no multi-region reliability claims.
  - Evidence: Local fan-out/optional broker and worker configuration, load and slow-reader schedule, byte/connection/resource/latency graphs or logs, lease-state/multi-tab evidence, real process stop/start and SQL state before/after, convergence tests, security/privacy checks and resource cost rationale.

- **APP12-AS5** (required privacy-safe observability, reconnect storm and accessible degradation)
  - Outcomes: APP12-O1, APP12-O9, APP12-O10, APP12-O11, APP12-O12, APP12-O14, APP12-O15, APP12-O16
  - Work: Instrument actual authorized state freshness, stream/cursor gap and resync, connection counts, expired sessions, denied subscriptions, outbound buffer bytes, slow-client closes and key user task outcomes, with sanitized limited labels. Inject a bounded synchronized reconnect surge after local network/proxy or fan-out loss, including expired sessions and changed room permissions; measure CPU/memory/requests, jitter/backoff, failed recoveries and legitimate tenant convergence. Validate accessible stale/connecting/offline/pending/conflict and forbidden states, keyboard/focus stability, restrained live announcements and a usable manual refresh or polling fallback. Explain sampling, clock uncertainty, retention and privacy decisions.
  - Criteria: Metric claims concern actual delivered/authorized business state, not simply green socket counts or observed client-side timestamps treated as synchronized network clocks. Reconnect work remains bounded and expired/revoked users are not continually reconnected or given prior private state. The status interface communicates uncertain commits, missing data and recovery without hiding focus or spamming screen readers; manual fallback remains usable. Logs exclude raw credentials/private message payloads and telemetry is scope/consent/retention aware. Results identify local profile, missing observations and resource budget limitations.
  - Evidence: Instrumented server/client and privacy audit, measure definitions and clock/source limitations, reproducible reconnect test profiles, buffer/connection/freshness metrics with errors and sample counts, access-control failure matrix, accessible UX observations and short operator recovery instructions.

- **APP12-AS6** (required integrated recoverable realtime feature and independent technical defense)
  - Outcomes: APP12-O1, APP12-O2, APP12-O3, APP12-O4, APP12-O5, APP12-O6, APP12-O7, APP12-O8, APP12-O9, APP12-O10, APP12-O11, APP12-O12, APP12-O13, APP12-O14, APP12-O15, APP12-O16, APP12-O17
  - Work: Deliver one coherent APP5 application feature demonstrating primary live delivery and a bounded alternative/second-protocol comparison, authority-scoped snapshots/cursors with gap and bootstrap-race recovery, two-client version/conflict correctness, current room/tenant/action permissions, finite slow-client queue and reconnect policy, approximate presence, restartable local fan-out outage with intact PostgreSQL state, privacy-safe useful monitoring, accessibility and justified resource/complexity choice. Reuse qualifying APP12-AS1–AS5 observations instead of building six disconnected apps. Under an independently supplied unfamiliar **bounded** stale/forged cursor, version race, revoked client, reconnect storm, slow reader, process restart or browser lifecycle defect, produce reproducible failed-before/passing-after tests or a documented safe diagnosis and defend the repaired guarantees.
  - Criteria: An independent reviewer can clean-start the documented free local browser/TypeScript/Fastify/PostgreSQL environment, use two actual synthetic accounts, observe real protocol traffic and HTTP/SQL facts, repeat negative authorization and network/fault scenarios, and verify final protected client views match authoritative data. Every asserted ordering, retention, delivery and resource guarantee is scoped, and no required Kafka, managed broker, public cloud/DNS, third-party user data or SYS consensus mechanism is introduced. The bounded unknown case is addressed without sacrificing privacy, authorization, accessible recovery or durable invariants. The learner explains personally implemented code, failed design alternatives, real measurements and unresolved transport/browser/topology limits in written, recorded, live or equivalent accessible defense.
  - Evidence: Complete source/lockfiles and starter instructions, protocol/authority/threat/replay documents, reproducible two-tenant browser and SQL fixtures, bootstrap/cursor/concurrency/auth/slow-consumer/reconnect tests and traces, actual fan-out restart and recovered client state, privacy/UX/runbook and cost decision, unfamiliar review diff/tests and accessible technical defense.

### Completion decision, revision safety and readiness

Passing APP12 requires independently inspectable satisfactory decisions for `APP12-AS1` through `APP12-AS6` jointly demonstrating `APP12-O1` through `APP12-O17`. A visually busy chat demo, a high socket count, an unverified stream reconnect, fabricated message history or successful unit mock cannot compensate for missed durable updates, cross-tenant disclosure, invalid concurrent edits, unbounded fan-out, inaccessible failure presentation or untestable recovery.

Record OEE specification and APP12 source revision, assessment/outcome IDs, actual source and test artifacts, safe synthetic identity and environment, stream/snapshot/version contracts, real HTTP/SQL and transport/fault evidence, negative security results, resource and latency measures with uncertainty, privacy and accessible user-state checks, and review decision under [OEE Evidence Rules](../../spec/evidence-rules.md).

APP12 preserves its `course` type, title, **optional `elective`** classification and approved direct prerequisites **APP3 + APP5 + APP6**, replacing the legacy seven-week checkpoint/final-lab contract with an OEE `v0.2.0` **draft**. Earlier learner evidence remains pinned to its original assessed revision and cannot be silently converted to newly defined outcomes or assessments. APP9's complete core graduation requirements are unchanged; APP13–APP16 elective source revisions and OEE Workspace/content/0xNAND consumer mappings require separate review and cannot be auto-reinterpreted. Structural CI is not learner testing, official educational verification or evidence of public production scalability.

### Public non-mandatory references

These references inform study and independent technical review; they do not add hidden graduation criteria.

- [WHATWG HTML — Server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html) defines `EventSource`, event-stream format and `Last-Event-ID` reconnect behavior.
- [MDN — Using server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) documents browser EventSource limitations and HTTP/1 connection budgeting.
- [RFC 6455 — WebSocket](https://www.rfc-editor.org/rfc/rfc6455.html) specifies handshake, control frames and close semantics.
- [MDN — WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) explains stable browser messaging and absence of automatic receive backpressure.
- [OWASP — WebSocket Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html) covers origin, authorization, session revocation, message validation and resource controls.
- [MDN — WebSocketStream](https://developer.mozilla.org/en-US/docs/Web/API/WebSocketStream) describes a nonstandard experimental streaming option; it is not a course dependency.
- [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) supplies concurrency/commit reality checks.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) and [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/) inform accessible status, focus and interaction behavior.
