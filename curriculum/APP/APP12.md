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

**Instructional sufficiency:** All 17 outcomes use 15 distinct modules and **six required cumulative summative assessments**. Each new protocol, concurrency, trust and accessibility mechanism requires a clear model/assumptions, worked observable trace, implemented or reasoned counterexample, correction and feedback before independent summative work. SSE framing and browser limits, WebSocket authenticated upgrade and backpressure, coherent SQL snapshot/watermark, generation-safe React state, server-authoritative edit conflicts and revoked live permissions cannot be flattened into one generic socket lesson. Formative investigations are not additional hidden graduation gates. The 14–18-week duration and workload are provisional; CI does not establish learner-tested or officially verified educational readiness.

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

1. **Why timely updates became a user-state problem** — Place polling, long-held HTTP, SSE and WebSockets in the history of stateful web experiences; separate familiar APP5 authenticated HTTP and APP6 monitoring from APP12's new notification loss, concurrent-client and lifecycle guarantees.

2. **A user task requiring honest shared state** — Choose one real React/Fastify/PostgreSQL workflow with two authorized users, two synthetic tenants and a stale-state consequence; identify when an on-screen change is not yet committed.

3. **Committed facts, ephemeral signals and delayed observers** — Work through a transaction whose notification is dropped after commit and a notification received before the client has fetched authority; compare independent SQL and display outcomes.

4. **Freshness objective, scope and truthful fallback** — Define eligible committed updates, acceptable observed stale interval, reconnect deadline, resource budgets and meaningful manual/slow-path behavior, qualifying unsynchronized clocks.

5. **Permission, ordering and consistency invariants** — Describe current tenant/object/field rights, per-room version and authoritative completed mutation, then identify one duplicate, gap, stale permission or false-success counterexample.

6. **Local topology, trust and repeatable fault harness** — Map actual React, HTTPS/Fastify, PostgreSQL and optionally restartable notifier ownership, pin browser/runtime and bounded tenant fixtures, and show which behaviors are simulated rather than real network partitions.

*Optional practice — contract critique:* Reject claims that an open socket implies durable delivery, universal order or human attention.

### Module 2 — Polling, HTTP Long Polling and Streaming Trade-offs

#### Outcomes

- APP12-O1
- APP12-O2
- APP12-O3
- APP12-O4
- APP12-O14

#### Lessons

1. **Conditional polling, data revisions and empty response cost** — Implement real conditional GET/version-based short polling with authentication, actual no-change requests and a committed update; inspect HTTP cache behavior and measured staleness.

2. **Long-poll wait, timeout, cancellation and resource ownership** — Run an actual held response through proxy/backend with bounded wait, client disconnect and repeated request, comparing resource pressure and trustworthy user status.

3. **SSE's HTTP stream and independent mutation path** — Probe a genuine text/event-stream response and ordinary protected HTTP write, separating one-way event delivery from durable SQL commit and browser native reconnect.

4. **WebSocket duplex upgrade and application command authority** — Inspect one real authenticated Origin-checked upgrade, duplex message and close; distinguish transport frames from validated application commands and acknowledged SQL effects.

5. **Proxy idle/buffering and browser connection budgeting** — Compare HTTP/1.x per-origin SSE tab exhaustion, negotiated HTTP/2 concurrent streams, proxy timeouts and buffered responses, while noting browser EventSource cannot set arbitrary Authorization headers and standard WebSocket lacks receive backpressure.

6. **Measured transport choice under matching real tasks** — Repeat idle and burst synthetic sessions with actual committed read/write work and controlled snapshots; count update age, bytes, open resources, errors and unauthorized refusals for polling versus the chosen primary stream.

7. **Failure and user-completion counterexample** — Disconnect a stream as the DB commits, compare a failed command versus missed push and use independent SQL/user observation to reject the claim that lowest socket latency is always best.

*Optional practice — transport decision:* Select the least costly sufficient option and define what evidence would justify switching.

### Module 3 — SSE Framing, Last-Event-ID and Authorized Resume

#### Outcomes

- APP12-O2
- APP12-O3
- APP12-O5
- APP12-O6
- APP12-O9

#### Lessons

1. **WHATWG SSE parsing and newline dispatch** — Transmit valid UTF-8 text/event-stream with comment, data, event, id and retry, multiline data and empty-line dispatch; show an incomplete frame that must not dispatch.

2. **Named events, runtime schema and trusted data** — Separate browser EventSource parser events from versioned app payload validation; reject a type-correct untrusted tenant/room label rather than using it to grant access.

3. **Native reconnect, retry semantics and cleared event ID** — Interrupt an actual EventSource connection, inspect Last-Event-ID and native retry; exercise empty id field resetting the browser's stored ID and do not assume native reconnection replays missing server history.

4. **Authenticated retention cursors, not bearer authorization** — Bind server-recognized cursor to room/tenant/epoch/current identity with limits and a retained server-side source; test valid replay, foreign-room and oversize/malformed Last-Event-ID independently of the browser's internal state.

5. **Expired cursor versus closed stream and fresh snapshot** — Distinguish a cursor below actual retained floor from invalid authorization, mark replay unfulfillable through an explicit app-level resync path and fetch a freshly authorized SQL snapshot, not silent gap skipping.

6. **Proxy flush, comments and canceled subscriber cleanup** — Show an actual streamed comment heartbeat and update under local buffering/timeout settings; inspect memory/registry cleanup after cancellation without confusing a keepalive with durable event history.

7. **Revocation during live SSE and replay refusal** — Expire/revoke an authenticated session while connected, stop private events and reject a previously valid cursor on reconnect; independently inspect that SQL and protected content remain inaccessible.

*Optional practice — foreign-room resume:* Demonstrate unauthorized Last-Event-ID misuse then repair cursor scope and fallback.

### Module 4 — WebSocket Upgrade, Framing and Persistent Command Security

#### Outcomes

- APP12-O2
- APP12-O4
- APP12-O9
- APP12-O10
- APP12-O11

#### Lessons

1. **WebSocket handshake, cookies, Origin and hijack denial** — Run a real WebSocket upgrade using a verified session and exact allowed Origin, then deny a cross-site browser handshake and unauthenticated client; Origin is a request signal, not proof of user identity.

2. **Application frame validation, types and limits** — Accept only a bounded schema-validated event/command with permitted room/action/field; exercise oversized, malformed and unauthorized frames before expensive fan-out.

3. **Handshake accepted is not continuous authorization** — Keep separate connection identity, scoped room membership, permitted publish actions and current role state; test an allowed socket attempting a newly forbidden command.

4. **Browser WebSocket state and bounded send-side signals** — Inspect readyState, bufferedAmount and close/error status; demonstrate why bufferedAmount only counts browser outbound queued bytes and does **not** bound incoming receive work or permit JavaScript protocol Ping.

5. **Server Ping/Pong versus app-visible heartbeat** — Observe a server-controlled RFC6455 Ping/Pong, and separately test an application status heartbeat for browser-visible liveness; avoid claiming one proves durable SQL state.

6. **Membership transitions and identity-switch cleanup** — Subscribe/unsubscribe with max room count, verify cleanup on route/logout/revocation and test a late packet from the former user/room.

7. **Command receipt, DB commit and push acknowledgement** — Send a real client command, distinguish parsed/accepted, committed mutation and broadcast delivery, then lose one reply after SQL commit and verify safe idempotent client reconciliation.

8. **Invalid frames, close behavior and bounded failure path** — Test malformed payloads, slow writes, expired sessions and clean close, recording server membership/byte limits and actual retained authoritative data after the connection dies.

*Optional practice — forged publish:* Reject a syntactically valid WebSocket message attempting a forbidden tenant action.

### Module 5 — Event Identity, Ordering Domains and Delivery Contracts

#### Outcomes

- APP12-O3
- APP12-O4
- APP12-O5
- APP12-O6
- APP12-O7

#### Lessons

1. **Authoritative row version versus notification delivery** — From an actual PostgreSQL transaction produce a committed resource revision, then show two delivered notifications with no newer business fact, and a committed fact with no delivered notification.

2. **Cursor envelope, schema, room and epoch boundaries** — Define stable server-issued event ID, resource/tenant/room scope, stream epoch and schema revision with nonsecret payload, and test wrong-room ID reuse.

3. **Per-key version assignment in the commit boundary** — Use real atomic PostgreSQL increment/constraint for a per-resource version, contrast timestamp/nontransactional app counter and show revision continuity under two writers and process restart.

4. **Duplicate, gap and late-version test table** — Deliver 4,4,6,5 against acknowledged revision 3; distinguish discard, buffer, gap/resync and what independently verified SQL version is now authoritative.

5. **Epoch reset and incomparable stream histories** — Restart a notifier or recreate a room and test a reused sequence with a new epoch, refusing stale cursor arithmetic or cross-tenant state leakage.

6. **Real retention floor and authorized replay window** — Delete old optional notification records under a controlled retention policy, prove the server knows its earliest safely replayable version and forces an authorized full snapshot if incomplete.

7. **Transport delivery, command idempotency and user completion** — Build a table contrasting ephemeral best-effort notice, retained at-least-once replay, duplicate delivery, protected business commit and end-to-end status, explicitly refusing exactly-once claims.

8. **Clock skew and observational order limits** — Skew client wall time, use comparable server monotonic durations only within one clock domain and base ordering on committed revisions, not perceived browser arrival timestamps.

*Optional practice — stale overwrite:* Prevent an old notification from replacing a newer committed version in client state.

### Module 6 — Snapshot, Delta and Bootstrap Race-Free Synchronization

#### Outcomes

- APP12-O5
- APP12-O6
- APP12-O7
- APP12-O8
- APP12-O15

#### Lessons

1. **Consistent protected SQL snapshot plus watermark** — Read current authorized data and a matching server-issued committed version in a coherent database snapshot/transaction; test why independent read-committed queries can pair incompatible content and watermark.

2. **Demonstrate the snapshot → subscribe lost-update race** — Pause before stream registration, commit an actual second-client transaction and show a naive subscriber remains stale even though its socket is open.

3. **Subscribe-buffer-snapshot with proven event boundary** — Register authorized subscription first and buffer bounded events while retrieving a consistent protected snapshot, dedupe/apply only versions after its watermark and handle overflow by full resync.

4. **Watermark → retained replay with actual contiguous history** — Take a transaction-consistent SQL snapshot/watermark, replay every later authorized revision from the retention floor and demonstrate a case where a pruned/incomplete event source invalidates the protocol.

5. **Versioned delta application, epoch/gap checks** — Apply only contiguous permitted versions or an explicitly proven commutative policy; reject wrong epoch, stale actor and out-of-order updates, with a concrete failing trace.

6. **Patch versus complete snapshot and authorized replacement** — Compare incremental patches with full resource replacement for a slow/stale reader, checking whether removed fields and a revoked role are purged from client state.

7. **Overflow, retention gap and known recovery condition** — Exhaust bounded replay/buffer capacity, refuse false catch-up, request a clean currently authorized snapshot and verify final SQL/client equality after another transaction.

8. **Account switch and old generation race guard** — Abort room/subscription fetch and ignore old-generation delayed event/snapshot after switching tenant or session; confirm previous-user private state never flashes.

*Optional practice — convergence proof:* Verify multiple clients match independent PostgreSQL after a forced bootstrap gap.

### Module 7 — React Synchronization, Reconnect and Offline Lifecycle

#### Outcomes

- APP12-O5
- APP12-O6
- APP12-O7
- APP12-O10
- APP12-O16

#### Lessons

1. **Explicit UI freshness and committed-work state machine** — Model disconnected, authenticating, catching-up, live, stale, forbidden and terminal errors, separately tracking locally pending, server committed and unconfirmed operations.

2. **React subscriptions and Strict Mode cleanup** — Use React Effect lifecycle for room/session subscriptions, reproduce double-listener setup and actual cleanup after route change, including tolerated dev Strict Mode replay.

3. **Native SSE retry versus application WS jitter** — Inspect EventSource's browser-managed retry and finite server rate controls, compare a custom WebSocket backoff/jitter policy and reject a home-grown duplicate SSE reconnect loop.

4. **Late fetch and packet after account/room change** — Race two session-scoped bootstrap requests and a delayed SSE/WS message, using current generation and server authority to reject stale private content.

5. **Accepted/unknown commit versus visible success** — Lose an HTTP reply after PostgreSQL commit while a notification arrives late; reconcile client attempt/revision with current server truth rather than announce an unconfirmed success.

6. **Visibility, bfcache and page revival on real browser** — Exercise pagehide/pageshow, visibility and back-forward restoration where supported, considering persistent JS heap and changed permissions before resuming the stream.

7. **Manual fallback accessible during long outage** — Offer an actual keyboard-usable protected refresh/conditional polling path and honest offline/stale states, not a disabled interface that assumes the push transport always returns.

8. **Expired session and terminal unauthorized reconnect** — Close private connections and clear old tenant state on logout/revocation, ensure unauthorized retries stop and new permitted login bootstrap requires fresh validation.

*Optional practice — duplicate-subscription defect:* Repair a React lifecycle issue creating multiple stale streams after navigation.

### Module 8 — Concurrent Collaborative Edits and Conflict Semantics

#### Outcomes

- APP12-O6
- APP12-O7
- APP12-O8
- APP12-O15
- APP12-O16

#### Lessons

1. **Authoritative revision precondition for every edit** — Use actual resource version/If-Match or server-side compare-and-set for a protected mutation, test one valid edit and one stale edit independently of push order.

2. **Simultaneous real clients against PostgreSQL** — Schedule two authenticated separate HTTP sessions writing the same resource, inspect row constraints/revisions and show how socket arrival order differs from committed order.

3. **Conflict status and accessible current-versus-draft review** — Return a documented 409/412/domain conflict, preserve the user's draft with real current state and test keyboard/focus and screen-reader explanation.

4. **Idempotent mutation identity under lost acknowledgement** — Bind retries to verified user/resource/action/fingerprint on server, lose a post-commit response and show no repeated business effect despite duplicate push events.

5. **Policy-specific merge versus authoritative rejection** — Compare independent per-field merge, append-only activity and a protected nonmergeable invariant, avoiding a universal merge policy for permissions or inventory.

6. **Why last-write-wins loses legitimate work** — Replay two competing writes with skewed client timestamps and show a lost update; require an explicit user/developer policy for discard, conflict or intentional merge.

7. **OT/CRDT alternatives, assumptions and trade-offs** — Work through a small concurrent text or set operation trace to understand convergence, metadata and conflict semantics; full collaborative editor/consensus implementation is not mandatory.

8. **Delayed acknowledgement and current-user state guard** — Cause an old command result/notification to arrive after a newer revision or user switch, verify UI never overwrites committed data or private current-identity state.

*Optional practice — two-user recovery:* Demonstrate a conflict and reconcile both clients without inventing missing updates.

### Module 9 — Origin, Room Permissions and Live Security Revocation

#### Outcomes

- APP12-O4
- APP12-O7
- APP12-O9
- APP12-O10
- APP12-O15

#### Lessons

1. **Cross-site WebSocket hijack and origin boundary** — Use a controlled cross-origin browser test with cookie-authenticated handshake, deny unapproved Origin and independently verify current session—CORS headers alone do not protect WS upgrade.

2. **Per-room and per-cursor server authorization** — Join then revoke membership; independently attempt guessed room IDs, foreign tenant event streams and retained cursor replay, inspecting whether any private payload is emitted.

3. **Message-level object/action/property authorization** — Attempt syntactically valid publish/subscribe edits with forged role and forbidden fields on an already accepted socket; deny real PostgreSQL side effects.

4. **Revocation while connected and queued-events purge** — Revoke an authorized account with a real live room, verify active connection closes or is rechecked and already buffered private messages are not delivered after revocation.

5. **Untrusted stream cursor, length and epoch policy** — Send oversized, forged, expired, foreign-room and changed-epoch resume values, rejecting/rebootstrapping safely without using a cursor as proof of current identity.

6. **Service actor versus caller-provided user claims** — Show server-authorized service dispatch distinct from human participant rights; reject client-supplied proxy headers, room metadata or websocket JSON identity as authorization.

7. **Handshake flood, room/cardinality and payload protection** — Rate/bound unauthorized connection attempts, subscriptions, message/frame bytes and reconnect work ahead of database or fan-out allocation.

8. **Private payload/logs and independent negative matrix** — Review room events and redacted diagnostic fields, test old user/tenant after role removal, and verify forbidden HTTP/WS/SQL results rather than count closed sockets alone.

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

1. **Classic browser WebSocket has no receive backpressure** — Under a bounded high-rate local producer, demonstrate incoming processing overrun and growing app work while explaining why WebSocketStream/WebTransport are nonrequired alternatives, not automatic browser WebSocket controls.

2. **Explicit bounded server per-client send queue** — Choose queue-byte, item-count, age and aggregate tenant budgets; overflow triggers a defined coalesce/disconnect/resync response rather than unbounded memory.

3. **Write backpressure versus browser outbound bufferedAmount** — Inspect actual Node/WS server socket writable drain or library buffered state and browser bufferedAmount for **outgoing** messages; never claim either bounds browser receive work.

4. **Hot room and fair client/tenant scheduling** — Send a burst from one legitimate tenant while another performs a protected task, measuring queue age, rejection and resource share, with current access enforced before fan-out.

5. **Publish, parser and membership rate enforcement** — Test oversized frames, invalid payloads, excessive room joins and fast publishers, applying rate/CPU/memory and subscription limits before expensive serialization.

6. **Paused slow reader and healthy peer preservation** — Throttle a controlled subscriber, measure bytes/memory/age and explicit close/resync or replaceable coalesce; prove unaffected authorized clients still reconcile.

7. **SSE HTTP response draining and cancellation** — Force a paused HTTP stream consumer, inspect server write buffering, drain and client cancellation under local proxy, then bound pending notices without treating write acceptance as delivery.

8. **Drop only replaceable notifications; never business truth** — Coalesce status-change *hints* only if an authorized SQL snapshot can restore all state; demonstrate a case where a discarded uncommitted user action would be a correctness failure.

*Optional practice — overflow diagnosis:* Fix memory growth from a disconnected subscriber retaining an unlimited stream buffer.

### Module 11 — Ephemeral Presence and Typing as Lease-Based Hints

#### Outcomes

- APP12-O10
- APP12-O11
- APP12-O12
- APP12-O16

#### Lessons

1. **Presence lease is approximate, not proof of attention** — Define bounded server-observed recent activity and what a user is allowed to infer; compare a silent backgrounded tab with a genuinely active room participant.

2. **Lease renewal, monotonic expiry and crash behavior** — Use server-owned TTL/clock boundaries for join/renew/expiry, intentionally drop disconnect, and verify eventual absence without assuming reliable browser close notifications.

3. **Multi-tab reference/identity and logout semantics** — Maintain separately authorized tab/subscription identities, close one of two tabs and keep user present if appropriate; revoke all after logout or permission change.

4. **Typing and cursor hints with privacy-safe throttling** — Bound per-room ephemeral typing/selection rates and TTL, never persist private draft text, and demonstrate that presence notifications cannot grant permissions.

5. **Ghost members and sleep/network-loss counterexample** — Suspend a test client, bypass close handshake and inject lost heartbeat, observe a ghost until lease expiry and reconcile server membership fairly.

6. **Scope, consent and current-permission presence** — Authorize who may see a user online/typing and for how long, purge after room/role change and document narrow retention without inferring human attention.

7. **Accessible quiet updates and manual presence refresh** — Provide meaningful low-frequency text state, accessible keyboard focus and an alternative refresh, avoiding endless assistive live-region announcements.

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

1. **Owned single-process subscription registry baseline** — Inspect actual current room membership and cache events in one process while keeping authoritative writes in PostgreSQL; test a notifier restart that loses this ephemeral registry.

2. **Two socket servers do not share in-memory subscribers** — Run locally isolated processes or a controlled equivalent, demonstrate that a room update on one process misses another and test connection routing/affinity consequences.

3. **Optional free pub/sub adapter and limits** — When useful, link locally controlled fan-out processes through a free pub/sub fixture, distinguish ephemeral notification relay from retained ordered SQL event history and avoid mandatory broker subscriptions.

4. **True independent notifier-process crash with SQL writes** — Stop the actual restartable notification layer while separate app PostgreSQL mutations commit, inspect missing pushes and verify private business state never disappears.

5. **Authenticated replay or snapshot after notifier reboot** — Reconnect clients with valid room identity, known epoch/cursor and retained authoritative source or complete snapshot; show why only replaying in-memory vanished notices cannot recover.

6. **Correlation without imagined global total order** — Propagate only safe stream/operation/room revision markers across processes, demonstrate duplicate/late notices and avoid inferring clock-synchronized total order.

7. **Reconnect thundering herd with finite admission** — Trigger bounded simultaneous 2–N local clients reconnecting after process loss, measure retry/jitter, replay slots and current-session denial before resync.

8. **Maintainability and simpler alternative decision** — Compare one-process SSE, polling and local pub/sub on connections, SQL reads, memory, observability and incident response; defend not adding a broker if no supported need.

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

1. **Correct authorized client freshness and completed work** — Define an eligible committed resource revision and actual authorized client-visible state with independent SQL snapshots, refusing an open-socket metric as user-task success.

2. **Clock domain, propagation samples and uncertainty** — Use server monotonic event durations and client-observed intervals without subtracting unsynchronized browser/server wall timestamps; report sample size, errors and missing events.

3. **Gap, floor, replay and complete-state restoration** — Track server-issued stream epoch, retained floor, client cursor, gap detection and verified snapshot reconciliation latency with no raw tenant identifiers.

4. **Rejected rooms, revoked sessions and finite queue measures** — Count authentically denied subscribes/publishes, current connected clients, buffer bytes and slow-consumer policy, limiting label cardinality and sensitive logging.

5. **Independent lost/duplicated/reordered live fault schedule** — Use seeded pause, kill, delay, duplicate, foreign-room cursor and changed role tests against real SSE/WS clients, with a baseline failing trace and corrected state.

6. **Two independent clients and actual SQL truth oracle** — Compare two browser/HTTP identities across tenant boundaries and concurrent writes; inspect committed row versions rather than infer correctness from synchronized UI screenshots.

7. **Capacity- and identity-aware reconnect experiment** — Exercise bounded reconnect storms including revoked sessions and missing replay, measure CPU, attempts, access denial and complete client resync rather than raw connection restoration.

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

1. **Manual low-bandwidth authorized task pathway** — Keep protected read/write and a real user-recoverable refresh possible without SSE/WS; show what remains correct after a prolonged transport failure.

2. **Live-region pacing, keyboard and focus stability** — Use a restrained ARIA status/announcements strategy on real updates and bursts, compare assistive-tech checks where supported, and avoid stealing focus on every notification.

3. **Explicit stale, pending, conflict and forbidden states** — Show honest disconnected/unknown-commit/conflict/reauth UI, actual server-authorized current state and keyboard-accessible action; never mark a delivered hint as committed work.

4. **Scoped presence and private activity disclosure** — Test room membership and current authorization before distributing cursor, typing or status hints, and provide a less intrusive user choice with bounded retention.

5. **Logout, old account and multi-tab secret purge** — Clear cached/queued previous-user data across React state, page restoration and stream events; simulate a late event after identity switch and verify no private DOM flash.

6. **Retention, participation rights and evidence limits** — Document retained notice cursor floor, optional activity trails and user privacy boundaries without claiming participant consent, external real-user observation or formal WCAG verification.

7. **Operator fault recovery and accessible handoff** — Publish a short actionable local playbook for expired cursor, leaked room, proxy idle timeout and notifier loss, with real SQL state check and keyboard-friendly user fallback.

*Optional practice — deceptive success badge:* Fix UI claiming a write committed merely because a push notification arrived.

### Module 15 — One Recoverable Realtime Feature and Independent Defense

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

1. **One actual collaborative task and previously accepted judgments** — Reuse the evolving APP5 product, cite independent accepted APP12-AS1–AS5 evidence and identify the real SQL record, protected room and permitted peer updates without creating six separate apps.

2. **Reproduce selected protocol, version and bootstrap behavior** — From a clean pinned local fixture, run polling plus primary stream and alternate protocol probe, perform a consistent watermark/bootstrap and show one actual SQL/protected-user state convergence and a missed-notice correction.

3. **Restore correct users under revocation, overload and outage** — Recheck relevant accepted two-client conflicts, current role/room/replay denial, bounded slow-reader queue, lease expiry, browser lifecycle and restartable notifier outage with real persisted PostgreSQL truth.

4. **Assessor introduces unfamiliar bounded live failure** — Independently reproduce a new snapshot-to-subscribe race, expired/forged cursor, old-account packet, missing version, stale permission, slow client or reconnect storm, predicting a user-visible and authoritative-state failure before implementation.

5. **Causal correction and focused independent regression** — Fix or safely reconcile the unfamiliar scenario with before/after actual HTTP/SSE/WS/SQL and client evidence, rerun affected already accepted AS1–AS5 invariants and disclose any unsupported browser/clock/topology guarantee.

6. **Clean technical defense with honest transport and human costs** — Demonstrate user-accessible manual recovery and explain source authorship, server authority, protocol choice, latency/buffering, privacy, optional broker versus simple design and measurement limitations through equivalent accessible review.

## Completion requirements

All **APP12-O1–APP12-O17** require six **independently decidable** summative assessments: AS1 actual transport/protocol comparison; AS2 coherent bootstrap, gap/replay and two-client PostgreSQL convergence; AS3 live identity/room/permission denial; AS4 bounded buffers, presence and actual notifier process interruption; AS5 trustworthy freshness/reconnect and accessible degraded use; AS6 a **new unfamiliar** bounded failure and independent technical defense. One evolving APP5 product and separately controlled local notifier are sufficient. **Previously accepted AS1–AS5 evidence may be referenced, not resubmitted as six products; AS6 cannot replace a missing decision.** Practice, optional brokers and this elective never create APP9 graduation gates.

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
  - Work: Implement one real authenticated APP5 shared task with independent protected PostgreSQL state and two actually running delivery choices: conditional/short polling plus primary **SSE or browser WebSocket**; separately demonstrate a bounded working probe of the other streaming protocol (valid SSE framing/native reconnect/**empty-id reset**/Last-Event-ID or origin/session-checked WS upgrade/message/close). Exercise actual idle/burst updates, local HTTP/2 or HTTP/1.x/proxy behavior as available, native browser API header and buffering limits, live error/authorization and SQL mutation, and measure delivered **correct task state** alongside bytes/connections/error/timing with honest clock and sample limitations.
  - Criteria: An independent browser/client can run the chosen two delivery paths and other-protocol probe, inspect valid WHATWG SSE or RFC6455 behavior and prove authenticated/forbidden status and actual SQL facts. SSE browser Last-Event-ID alone is not durable replay; native browser WS bufferedAmount cannot bound receive memory and JS cannot send protocol Ping. Browser EventSource cannot set arbitrary Authorization headers. Supported proxy connections, idle error rates, CPU and sample-clock limitations are declared. The selected transport improves the real authorized task with an explicit no-realtime alternative rather than presume more sockets equal better collaboration.
  - Evidence: Versioned local React/HTTP/stream source, fixture and pinned versions, browser/network trace of polling and primary stream, bounded secondary protocol probe, local traffic/latency/byte/CPU/resource/error comparison, actual SQL observations, architecture decision and known limitations.

- **APP12-AS2** (required authoritative snapshot, gap-replay and concurrent client convergence)
  - Outcomes: APP12-O5, APP12-O6, APP12-O7, APP12-O8, APP12-O15, APP12-O16
  - Work: Implement one real PostgreSQL-backed protected resource with server-issued **per-room/tenant/epoch revision**, authorized retained cursor policy and a **transaction-consistent snapshot plus matching watermark**; or prove an equivalent subscribe-buffer-snapshot bound. **First reproduce** the naive snapshot→subscribe lost-update race with a concurrent actual committed second-client write. Then correct it with contiguous retained replay from the actual floor or bounded buffer with explicit overflow resync. Deliver duplicates, out-of-order, missing versions, stale epochs and foreign/expired cursors; use separate authenticated clients to race writes with real SQL revision preconditions, retain a recoverable draft and show final authorized browser state matching independently queried committed rows.
  - Criteria: A verifier sees a failing-before/passing-after bootstrap race, with snapshot content/watermark demonstrably consistent under actual PostgreSQL transaction semantics—not two independent read-committed queries guessed to describe one snapshot. Actual server retention source suffices for full replay or forces a fresh authorized snapshot; missed/late/duplicated updates cannot silently skip or overwrite committed revisions or leak a previous tenant. Two real independent simultaneous HTTP/SQL writers preserve authoritative invariants under declared conflict/merge rules and no operation is counted completed simply because a notification arrived. Keyboard/focus/conflict and current identity changes remain correctly recoverable.
  - Evidence: Snapshot and stream cursor/epoch contract, server-side sequence/retention policy, two-client deterministic fault schedule, tests of bootstrap race and out-of-order/expired/gap inputs, conflict HTTP/DB logs, authorized final-state comparison, screenshots/transcripts of accessible recovery and limitation notes.

- **APP12-AS3** (required live authorization, connection lifecycle and cross-tenant attack resistance)
  - Outcomes: APP12-O3, APP12-O4, APP12-O7, APP12-O9, APP12-O10, APP12-O15, APP12-O16
  - Work: Operate authenticated SSE/WS and current authorized rooms/subscriptions with finite connection limits and React Effect cleanup. Using actual browser and independent HTTP/WS clients, test forbidden Origin/cookie handshake (WS), invalid/malformed/oversize message, anonymous/expired user, guessed cross-tenant room, forged Last-Event-ID/stream epoch, unauthorized per-message object/action/property mutation and **permission or session revocation while a socket is still connected and a private event is queued**. Switch users, tabs and routes and observe real listener/room/HTTP/SQL/private DOM state and denied replay after the change.
  - Criteria: Origin validation and actual session verification are both needed; CORS or an accepted WS handshake alone does not authorize protected actions. A formerly authorized persistent subscriber cannot receive newly forbidden event bytes after revocation (including queued/buffered path under the disclosed strategy), and a cursor never becomes an authorization credential. Actual independent HTTP/WS/SQL and server membership evidence shows denied cross-tenant/field effects and terminates unauthenticated reconnect loops. Browser Ping control is not misrepresented; client generations, route cleanup, limited rooms and secure status/fallback remain inspectable.
  - Evidence: Origin and authentication configuration, versioned subscription/WS command contracts, multi-tenant/role/revocation threat matrix and independent rejected requests, actual server registry and React effect traces, authorized/denied DB inspection, multi-tab/logout/timeout transcript and redacted log evidence.

- **APP12-AS4** (required bounded fan-out, slow consumers, ephemeral presence and process restart)
  - Outcomes: APP12-O2, APP12-O10, APP12-O11, APP12-O12, APP12-O13, APP12-O14, APP12-O15
  - Work: Run the **same** protected React/Fastify/PostgreSQL realtime product with several actual local clients, a deliberately slow reader, one high-rate tenant, healthy other-tenant work and two tabs for one identity. Instrument server-side per-client outbound queue bytes/age and finite room/connection/payload/publish budgets; distinguish browser outgoing bufferedAmount from incoming receive constraints. Test honest coalescing/disconnect-and-authorized-snapshot recovery, real server-driven presence lease expiry on dropped close and permitted multi-tab state. **Stop a separately running notifier/fan-out process while PostgreSQL writes a new resource revision**, then restart and verify actual clients recover authoritative state even if transient notifications vanished.
  - Criteria: Actual measured queue/worker/memory limits prevent local slow-client/noisy-tenant overload and protect unaffected authorized users under the stated bounded load; only replaceable update hints may be dropped, never committed business truth. Presence remains approximate, scoped and based on observed server lease rather than proof of human attention, and an abrupt missing disconnect is eventually resolved. True local process interruption with independent SQL snapshot and client resynchronization is demonstrated, rather than a mocked event handler, while no multi-region or guaranteed broker-delivery claims are inferred.
  - Evidence: Local fan-out/optional broker and worker configuration, load and slow-reader schedule, byte/connection/resource/latency graphs or logs, lease-state/multi-tab evidence, real process stop/start and SQL state before/after, convergence tests, security/privacy checks and resource cost rationale.

- **APP12-AS5** (required privacy-safe observability, reconnect storm and accessible degradation)
  - Outcomes: APP12-O1, APP12-O9, APP12-O10, APP12-O11, APP12-O12, APP12-O14, APP12-O15, APP12-O16
  - Work: Collect privacy-minimal actual local user-task freshness (committed authority versus authorized client), reconnection/cursor floor/gaps/resync, protected/denied session and outbound queue metrics on the same product. Define eligible changed records, controlled server durations, unsupported cross-device one-way latency and honest error/sample counts. Inject a **distinct bounded** reconnect wave with some sessions revoked, a room membership change and a stale delayed notifier, and measure attempts, CPU/queue use, jitter, failed user work and verified SQL/browser convergence. Show actual keyboard-focus, restrained live-announcement, manual protected refresh and truthful pending/unknown/forbidden/offline UX, with short practical operator recovery steps.
  - Criteria: An open connection or successfully delivered notice is not treated as committed authorized user success; clock-domain and selection bias are explicit and data labels avoid private user/message identities. A reconnect surge is finite, current authorization prevents stale/revoked replay, and a lost server response has correct unknown-commit messaging until authoritative SQL checked. User input, focus and assistive status remain usable with optional/available supported testing; no invented WCAG certification, real field sample or production SLO. A separate actual fault is diagnosed with an actionable runbook rather than reusing only AS4's interrupted process transcript.
  - Evidence: Instrumented server/client and privacy audit, measure definitions and clock/source limitations, reproducible reconnect test profiles, buffer/connection/freshness metrics with errors and sample counts, access-control failure matrix, accessible UX observations and short operator recovery instructions.

- **APP12-AS6** (required integrated recoverable realtime feature and independent technical defense)
  - Outcomes: APP12-O1, APP12-O2, APP12-O3, APP12-O4, APP12-O5, APP12-O6, APP12-O7, APP12-O8, APP12-O9, APP12-O10, APP12-O11, APP12-O12, APP12-O13, APP12-O14, APP12-O15, APP12-O16, APP12-O17
  - Work: Deliver **one evolving APP5 protected shared React/Fastify/PostgreSQL feature** and **reference separately accepted APP12-AS1–AS5 evidence** rather than repeat whole transport, replay, security, buffer/presence and recovery tests as six new applications. Reproduce representative live stream/protocol, transaction-consistent bootstrap, independent concurrent conflict, current identity/room denial and a bounded notifier failure from a clean pinned free local fixture. The reviewer supplies a **previously unseen bounded** wrong epoch/retention, revocation with buffered event, snapshot race, old-user result, slow reader, process restart or reconnect issue. Predict an observable defect, reproduce an independent failing-before client/HTTP/SSE/WS/SQL oracle, repair the root cause or implement a safe demonstrated reconciliation and rerun targeted previously accepted invariants. Explain transport simplicity, privacy, accessibility, costs and honest local/platform limits.
  - Criteria: APP12-AS1–AS5 must each have an independently passing decision; AS6 does not waive any or turn an elective into an APP9 gate. The genuinely unfamiliar problem is inside the published outcomes and locally feasible, and the new correction has an independent observed before/after event and authoritative SQL/user-state check—not rehearsed logs or a synthetic-only mock. The protected task, keyboard/focus/manual fallback, finite buffers and current permissions remain correct. No Kafka, paid broker, public DNS, SYS consensus or cross-region network partition proof is required; every ordering/delivery/clock/availability claim is limited to what was actually tested.
  - Evidence: One versioned APP5 application/lockfile and free synthetic two-tenant client/SQL/fan-out fixture, **references-first outcome-to-accepted-APP12-AS1–AS5 index**, actual SSE/WS/HTTP and DB traces of scoped bootstrap/replay, independent concurrent auth/slow-reader/fan-out tests, selected privacy/freshness/accessibility observations, unfamiliar reviewer scenario and targeted failing-before/passing-after correction, local resource/cost limits and accessible written/recorded/live technical defense.

### Completion decision, revision safety and readiness

Passing APP12 requires independently inspectable satisfactory decisions for `APP12-AS1` through `APP12-AS6` jointly demonstrating `APP12-O1` through `APP12-O17`. A visually busy chat demo, a high socket count, an unverified stream reconnect, fabricated message history or successful unit mock cannot compensate for missed durable updates, cross-tenant disclosure, invalid concurrent edits, unbounded fan-out, inaccessible failure presentation or untestable recovery.

Record OEE specification and APP12 source revision, assessment/outcome IDs, actual source and test artifacts, safe synthetic identity and environment, stream/snapshot/version contracts, real HTTP/SQL and transport/fault evidence, negative security results, resource and latency measures with uncertainty, privacy and accessible user-state checks, and review decision under [OEE Evidence Rules](../../spec/evidence-rules.md).

APP12 remains the published OEE `v0.2.0` **draft** `course`, **optional `elective`**, with APP3 + APP5 + APP6 direct prerequisites. The seven-week checkpoint format is a historical migration already reflected in the current catalog, not a newly imposed revision. APP9's core graduation and APP13–APP16 remain unchanged; prior learner decisions stay bound to their actual assessed course revision, and OEE Workspace/content/0xNAND source/evidence pins require deliberate separate review. Neither source CI nor this editorial reassessment establishes learner `tested`/`verified` status, public production guarantees or external accreditation.

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
