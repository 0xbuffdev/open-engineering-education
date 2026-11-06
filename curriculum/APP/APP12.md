# APP12 — Realtime Systems

**Program:** APP — Application Engineering
**Classification:** `elective`
**Type:** `course`
**Prerequisites:** [APP3](APP3.md), [APP5](APP5.md), [APP6](APP6.md)
**Duration:** 5 weeks
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

## Modules

### Module 1 — Delivery Models & Protocols

#### Outcomes

- Compare latency, directionality and failure characteristics of common transports.
- Separate authoritative stored state from transient notifications.

#### Lessons

1. **Course introduction: Realtime Systems** — `lesson`

   Build application features that deliver timely updates while preserving authorization, ordering and recoverability. Distinguish realtime transport from durable state, then design for reconnects, slow clients, duplicate events and operational visibility.
2. **Polling, SSE and bidirectional WebSockets** — `lesson`
3. **Event versus state semantics** — `lesson`
4. **Selecting a transport** — `test`
5. **Measure notification delivery** — `lab`

### Module 2 — Event Ordering & Synchronization

#### Outcomes

- Define ordering domains and identifiers for application events.
- Recover from missed, repeated or out-of-order notifications.

#### Lessons

1. **Event identifiers and sequence numbers** — `lesson`
2. **Snapshot, replay and resynchronization** — `lesson`
3. **Client state correctness** — `test`
4. **Repair an inconsistent client** — `lab`

### Module 3 — Connection Lifecycle & Security

#### Outcomes

- Enforce per-client authorization and session expiry.
- Bound buffering, heartbeat traffic and connection lifetimes.

#### Lessons

1. **Connection authentication and access checks** — `lesson`
2. **Heartbeats, rate limits and backpressure** — `lesson`
3. **Securing realtime streams** — `test`
4. **Test slow and unauthorized clients** — `lab`

### Module 4 — Scale & Observability

#### Outcomes

- Identify fan-out and broker trade-offs without assuming global ordering.
- Monitor delivery delays, dropped connections and recovery success.

#### Lessons

1. **Fan-out workers and broker trade-offs** — `lesson`
2. **Latency, saturation and failure visibility** — `lesson`
3. **Diagnosing delivery failures** — `test`
4. **Load-test subscriptions** — `lab`

### Module 5 — Recoverable Realtime Collaboration Feature

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

**Exit demonstration:**

Demonstrate the working implementation, explain the relevant mechanisms, reproduce at least one failure and repair, and defend the chosen trade-offs using retained evidence.
