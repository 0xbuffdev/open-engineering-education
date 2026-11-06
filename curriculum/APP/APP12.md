# APP12 — Realtime Systems

**Program:** APP — Application Engineering
**Classification:** `elective`
**Type:** `course`
**Prerequisites:** [APP3](APP3.md), [APP5](APP5.md), [APP6](APP6.md)
**Duration:** 7 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Build application features that deliver timely updates while preserving authorization, ordering and recoverability. Distinguish realtime transport from durable state, then design for reconnects, slow clients, duplicate events and operational visibility.

This is an optional specialization. It is not required to complete APP9 or graduate from Application Engineering.

## Learning outcomes

By the end of this course, the learner will be able to:

- Select polling, server-sent events, WebSockets or messaging according to delivery needs.
- Define event identity, sequencing, replay windows and client resynchronization.
- Implement authorization and bounded resource use for persistent connections.
- Handle reconnects, slow consumers and transient failures without losing core application state.
- Test realtime behavior under concurrent clients and observable failure scenarios.
- Specify concurrent editing, event ordering and conflict resolution for disconnected clients.
- Enforce per-message authorization and bound slow-client and abusive traffic impact.
- Demonstrate state recovery after broker outages, reconnect storms and duplicated notifications.

## Modules

### Module 1 — Delivery Models & Protocols

#### Outcomes

- Compare latency, directionality and failure characteristics of common transports.
- Separate authoritative stored state from transient notifications.

- Choose a transport based on directionality, retry, ordering and infrastructure constraints.

#### Lessons

1. **Course introduction: Realtime Systems** — `lesson`

   Build application features that deliver timely updates while preserving authorization, ordering and recoverability. Distinguish realtime transport from durable state, then design for reconnects, slow clients, duplicate events and operational visibility.
2. **Polling, SSE and bidirectional WebSockets** — `lesson`
3. **Event versus state semantics** — `lesson`
4. **HTTP long polling and SSE reconnection semantics** — `lesson`
5. **WebSocket handshake and framing fundamentals** — `lesson`
6. **Infrastructure limits and proxy idle timeouts** — `lesson`
7. **Selecting a transport** — `test`
8. **Measure notification delivery** — `lab`

### Module 2 — Event Ordering & Synchronization

#### Outcomes

- Define ordering domains and identifiers for application events.
- Recover from missed, repeated or out-of-order notifications.

- Keep client-visible state correct when notifications arrive late, out of order or repeatedly.

#### Lessons

1. **Event identifiers and sequence numbers** — `lesson`
2. **Snapshot, replay and resynchronization** — `lesson`
3. **Event IDs, ordering domains and replay windows** — `lesson`
4. **State snapshots, deltas and conflict resolution** — `lesson`
5. **Clock skew, causality and duplicate events** — `lesson`
6. **Client state correctness** — `test`
7. **Repair an inconsistent client** — `lab`

### Module 3 — Connection Lifecycle & Security

#### Outcomes

- Enforce per-client authorization and session expiry.
- Bound buffering, heartbeat traffic and connection lifetimes.

- Maintain access control and predictable memory use throughout persistent connection lifecycles.

#### Lessons

1. **Connection authentication and access checks** — `lesson`
2. **Heartbeats, rate limits and backpressure** — `lesson`
3. **Origin restrictions and connection authentication** — `lesson`
4. **Per-message authorization and session revocation** — `lesson`
5. **Slow consumers, bounded buffers and heartbeat policy** — `lesson`
6. **Securing realtime streams** — `test`
7. **Test slow and unauthorized clients** — `lab`

### Module 4 — Scale & Observability

#### Outcomes

- Identify fan-out and broker trade-offs without assuming global ordering.
- Monitor delivery delays, dropped connections and recovery success.

- Design a measurable fan-out service with honest event-delivery guarantees.

#### Lessons

1. **Fan-out workers and broker trade-offs** — `lesson`
2. **Latency, saturation and failure visibility** — `lesson`
3. **Fan-out and broker delivery guarantees** — `lesson`
4. **Presence lifecycle, lease expiry and reconnect storms** — `lesson`
5. **Delivery latency and loss-rate telemetry** — `lesson`
6. **Diagnosing delivery failures** — `test`
7. **Load-test subscriptions** — `lab`

### Module 5 — Collaboration & Concurrent Editing

#### Outcomes

- Choose a conflict model that matches product semantics.
- Handle simultaneous edits and reconnection without silently losing confirmed work.

#### Lessons

1. **Shared state and authoritative conflict rules** — `lesson`
2. **Optimistic concurrency and version vectors** — `lesson`
3. **Operational transforms versus CRDT design choices** — `lesson`
4. **Client reconciliation and user conflict feedback** — `lesson`
5. **Concurrent editing convergence and correctness** — `test`
6. **Resolve conflicting collaborative edits** — `lab`

### Module 6 — Realtime Security & Abuse Resilience

#### Outcomes

- Enforce authorization on every state-changing event, not only connection establishment.
- Bound resource consumption and data disclosure under malicious event patterns.

#### Lessons

1. **Message validation and origin trust** — `lesson`
2. **Per-room authorization and role changes** — `lesson`
3. **Flood control and resource exhaustion** — `lesson`
4. **Auditing actions and private-event redaction** — `lesson`
5. **Realtime event access and abuse controls** — `test`
6. **Harden a multi-user event channel** — `lab`

### Module 7 — Realtime Deployment, Failure & Recovery

#### Outcomes

- Recover reliable application state after transport or broker failure.
- Document deployment topology, monitoring and scaling limits.

#### Lessons

1. **Sticky routing versus external connection state** — `lesson`
2. **Broker outages and resubscription** — `lesson`
3. **Observability across connection lifecycle** — `lesson`
4. **Backpressure and reconnect storm handling** — `lesson`
5. **Resilience under reconnect storms** — `test`
6. **Recover from a realtime broker outage** — `lab`

### Module 8 — Recoverable Realtime Collaboration Feature

#### Outcomes

- Integrate the elective's techniques in a demonstrable application change or complete system.
- Evaluate correctness, operational limitations, and engineering trade-offs from repeatable evidence.

#### Lessons

1. **Recoverable Realtime Collaboration Feature** — `lab`

## Completion requirements

- Complete the module checkpoints and all listed practical exercises, then complete the final integration lab.
- State tools, versions, runtime assumptions and test data so another learner can reproduce the work.
- Retain artifacts, test results, design decisions, evidence of at least one investigated failure and a technical retrospective according to [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required module checkpoints and exercises:**

- **Module 1 — Delivery Models & Protocols:** Pass `Selecting a transport` by explaining and applying the module outcomes; perform the `Measure notification delivery` lab: Implement two notification paths and compare latency, resource usage and reconnect behavior. Retain Protocol trace and a comparison under one test workload.
- **Module 2 — Event Ordering & Synchronization:** Pass `Client state correctness` by explaining and applying the module outcomes; perform the `Repair an inconsistent client` lab: Inject dropped and duplicated events, then reconcile client state from authoritative storage. Retain Replayed event log and state invariant tests.
- **Module 3 — Connection Lifecycle & Security:** Pass `Securing realtime streams` by explaining and applying the module outcomes; perform the `Test slow and unauthorized clients` lab: Simulate an unauthorized subscription and slow reader; verify rejection and bounded server resources. Retain Access-denial evidence, buffer metrics and connection logs.
- **Module 4 — Scale & Observability:** Pass `Diagnosing delivery failures` by explaining and applying the module outcomes; perform the `Load-test subscriptions` lab: Exercise concurrent subscriptions, failure/restart and recovery; explain observed limits and mitigations. Retain Run configuration, metrics, traces and a recovery report.

**Final integration lab — Recoverable Realtime Collaboration Feature:**

Implement a collaborative notification or shared-workflow feature with persistent authoritative state, realtime updates, client resynchronization, authentication and bounded reconnect handling. Demonstrate it with multiple clients and deliberate network faults.

**Success criteria:**

- Show correct state after dropped, duplicated and out-of-order notifications.
- Reject unauthorized subscriptions and bound slow-consumer impact.
- Measure notification delay and demonstrate reconnect recovery under a stated test load.
- Keep persistence correct when the realtime transport is unavailable.

**Evidence to retain:**

- A version-controlled implementation, configuration and exact steps for reproduction.
- Input/workload data and automated tests or repeatable manual verification records.
- Observed results, rejected alternatives, important design decisions and a technical retrospective.

**Failure analysis:**

Explain stale client state, event races, leaked subscriptions, expired sessions and retry storms with reproducible evidence.

**Expanded module assessment and lab requirements:**

- **Module 1 checkpoint and micro-lab:** Observe protocol handshakes, failure behavior and reconnects for two delivery approaches.
- **Module 2 checkpoint and micro-lab:** Prove client state matches authoritative server state after lost and duplicate messages.
- **Module 3 checkpoint and micro-lab:** Show rejection of unauthorized subscribe/publish and bounds on slow-client buffers.
- **Module 4 checkpoint and micro-lab:** Measure system limits under realistic concurrent clients and recover after a broker restart.

- **Module 5 — Collaboration & Concurrent Editing (Resolve conflicting collaborative edits):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Simulate two users editing shared state under latency and disconnects, implement explicit conflict resolution and replay reconciliation.
  - Verification: Final state obeys documented invariants and both users receive deterministic conflict feedback.
  - Evidence: Event histories, final state assertions and conflict tests.
  - Failure analysis: Explain why last-writer-wins is not always safe and how clock skew affects naive orderings.
- **Module 6 — Realtime Security & Abuse Resilience (Harden a multi-user event channel):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Inject forged room IDs, high-rate message bursts and expired credentials into a test channel, then demonstrate safe rejection.
  - Verification: No cross-room event disclosure occurs and server buffers and handler work remain bounded.
  - Evidence: Attack traces, authorization tests and rate metrics.
  - Failure analysis: Identify time-of-check authorization gaps and identity confusion during reconnect.
- **Module 7 — Realtime Deployment, Failure & Recovery (Recover from a realtime broker outage):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Restart the broker or fan-out layer during active subscriptions, inject slow consumers and verify resynchronization.
  - Verification: No required authoritative state is lost, clients resubscribe safely and reconnection rate remains bounded.
  - Evidence: Run topology, failure timeline, client state checks and metrics.
  - Failure analysis: Explain duplicate replay, missed ephemeral updates and reconnect amplification.

**Exit assessment expectation:**

Demonstrate the subject outcomes on an unfamiliar example, show at least one negative path and retain evidence allowing another reviewer to reproduce the result. Checkpoint answers must explain mechanisms, while the final integration lab must integrate and verify the expanded topics.

**Exit demonstration:**

Demonstrate the working implementation, explain the relevant mechanisms, reproduce at least one failure and repair, and defend the chosen trade-offs using retained evidence.
