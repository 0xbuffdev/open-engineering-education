# APP13 — Mobile Application Engineering

**Program:** APP — Application Engineering
**Classification:** `elective`
**Type:** `course`
**Prerequisites:** [APP2](APP2.md), [APP3](APP3.md)
**Duration:** 9 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Extend application engineering to touch-first mobile clients, device lifecycle constraints, intermittent networks and controlled release processes. Build an accessible mobile interface that synchronizes safely with an authenticated backend.

This is an optional specialization. It is not required to complete APP9 or graduate from Application Engineering.

## Learning outcomes

By the end of this course, the learner will be able to:

- Design touch-first, accessible navigation and forms using mobile platform conventions.
- Manage lifecycle events, persistent client state and limited device resources.
- Synchronize user data under intermittent network conditions and conflicting updates.
- Integrate device permissions and secure credential handling with minimum privilege.
- Test across device configurations and document a reproducible release build.
- Architect typed and persistent mobile state that survives platform lifecycle and schema changes.
- Respect mobile permission, privacy, connectivity and device-energy constraints.
- Verify release, staged rollout and recovery across representative devices and OS versions.
- Resolve offline writes and conflicts with transparent user feedback and authenticated synchronization.

## Modules

### Module 1 — Mobile UI & Navigation

#### Outcomes

- Apply platform navigation, touch target and accessibility conventions.
- Build resilient forms across keyboard, rotation and screen sizes.

- Explain and test mobile interaction patterns across diverse screen and accessibility modes.

#### Lessons

1. **Course introduction: Mobile Application Engineering** — `lesson`

   Extend application engineering to touch-first mobile clients, device lifecycle constraints, intermittent networks and controlled release processes. Build an accessible mobile interface that synchronizes safely with an authenticated backend.
2. **Mobile layouts and navigation models** — `lesson`
3. **Touch interaction and screen-reader support** — `lesson`
4. **Android and iOS navigation conventions** — `lesson`
5. **Safe areas, platform text scaling and layout** — `lesson`
6. **Touch target geometry, gestures and focus** — `lesson`
7. **Reviewing mobile usability** — `test`
8. **Audit a mobile workflow** — `lab`

### Module 2 — Lifecycle & Device State

#### Outcomes

- Explain foreground/background lifecycle and interruption recovery.
- Persist state without relying on a continuously running process.

- Restore critical user state after lifecycle interruption without assuming unlimited background execution.

#### Lessons

1. **Lifecycle events and state restoration** — `lesson`
2. **Local storage and device resource budgets** — `lesson`
3. **Activity, process and app lifecycle transitions** — `lesson`
4. **Local persistence, encryption and data retention** — `lesson`
5. **Background-task limits, power and memory management** — `lesson`
6. **Reasoning about app restarts** — `test`
7. **Recover an interrupted task** — `lab`

### Module 3 — Offline Synchronization & Security

#### Outcomes

- Distinguish queued writes from confirmed server state.
- Define conflict handling and protect credentials and sensitive data.

- Synchronize data correctly under partitioned networks and expired credentials.

#### Lessons

1. **Offline-first queues and conflict policies** — `lesson`
2. **Authentication, permissions and secure storage** — `lesson`
3. **Optimistic writes, offline queues and idempotency** — `lesson`
4. **Conflict policies and authenticated synchronization** — `lesson`
5. **Sensitive data minimization and permission prompts** — `lesson`
6. **Handling synchronization conflicts** — `test`
7. **Reconcile offline edits** — `lab`

### Module 4 — Testing & Release

#### Outcomes

- Design unit, integration and device-level mobile tests.
- Prepare signed/reproducible builds and review privacy/permission declarations.

- Test and release a mobile application against reproducible functional and security criteria.

#### Lessons

1. **Device matrices and automated UI tests** — `lesson`
2. **Crash diagnostics and staged release** — `lesson`
3. **Simulator, device farm and physical-device constraints** — `lesson`
4. **UI automation, crash reports and staged rollout** — `lesson`
5. **Build signing, supply-chain hygiene and distribution policy** — `lesson`
6. **Evaluating release readiness** — `test`
7. **Test a release candidate** — `lab`

### Module 5 — Mobile Architecture & Typed Data

#### Outcomes

- Structure a mobile client with testable state and data boundaries.
- Evolve local state schemas without losing existing user data.

#### Lessons

1. **Presentation, domain and persistence boundaries** — `lesson`
2. **Typed navigation and screen state** — `lesson`
3. **Caching, serialization and schema migration** — `lesson`
4. **Dependency injection and testing seams** — `lesson`
5. **Mobile state ownership and typed persistence** — `test`
6. **Refactor a stateful mobile feature** — `lab`

### Module 6 — Device Capabilities, Permissions & Privacy

#### Outcomes

- Request only necessary device permissions at an understandable moment.
- Keep sensitive device data protected across storage, sharing and revocation.

#### Lessons

1. **Permission lifecycle and user education** — `lesson`
2. **Camera, location, notification and file access boundaries** — `lesson`
3. **Device storage encryption and key management** — `lesson`
4. **Privacy disclosures and data deletion behavior** — `lesson`
5. **Permission and privacy failure paths** — `test`
6. **Implement a permission-safe mobile workflow** — `lab`

### Module 7 — Mobile Networking & Energy

#### Outcomes

- Choose network and retry strategies that respect battery and data limits.
- Separate push signals from authoritative client state.

#### Lessons

1. **Cellular latency and intermittent connectivity** — `lesson`
2. **Battery, scheduling and network retry costs** — `lesson`
3. **Push notifications and state refresh** — `lesson`
4. **Sync batching and bandwidth budgets** — `lesson`
5. **Mobile retry and energy considerations** — `test`
6. **Diagnose a high-drain synchronization loop** — `lab`

### Module 8 — App Distribution & Operational Quality

#### Outcomes

- Create a release process with reproducible inputs and secure signing-key handling.
- Monitor crashes and regressions across OS and device variants.

#### Lessons

1. **Build variants and signing keys** — `lesson`
2. **Release channels, staged rollout and rollback** — `lesson`
3. **Crash telemetry, privacy and alerting** — `lesson`
4. **OS upgrades and dependency lifecycle** — `lesson`
5. **Mobile release readiness and compatibility** — `test`
6. **Ship and rollback a simulated mobile release** — `lab`

### Module 9 — Offline-Capable Mobile Client

#### Outcomes

- Integrate the elective's techniques in a demonstrable application change or complete system.
- Evaluate correctness, operational limitations, and engineering trade-offs from repeatable evidence.

#### Lessons

1. **Offline-Capable Mobile Client** — `lab`

## Completion requirements

- Complete the module checkpoints and all listed practical exercises, then complete the final integration lab.
- State tools, versions, runtime assumptions and test data so another learner can reproduce the work.
- Retain artifacts, test results, design decisions, evidence of at least one investigated failure and a technical retrospective according to [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required module checkpoints and exercises:**

- **Module 1 — Mobile UI & Navigation:** Pass `Reviewing mobile usability` by explaining and applying the module outcomes; perform the `Audit a mobile workflow` lab: Build and inspect a navigable form on small and large viewports and with assistive technology. Retain Screenshots, accessibility notes and reproducible UI tests.
- **Module 2 — Lifecycle & Device State:** Pass `Reasoning about app restarts` by explaining and applying the module outcomes; perform the `Recover an interrupted task` lab: Kill or suspend an in-progress workflow, restart the application and verify safe restoration. Retain Lifecycle trace, saved state and test cases.
- **Module 3 — Offline Synchronization & Security:** Pass `Handling synchronization conflicts` by explaining and applying the module outcomes; perform the `Reconcile offline edits` lab: Queue offline changes from two clients, reconnect with conflicts and demonstrate the documented resolution policy. Retain Conflict log, synchronization tests and authorization checks.
- **Module 4 — Testing & Release:** Pass `Evaluating release readiness` by explaining and applying the module outcomes; perform the `Test a release candidate` lab: Run representative device tests, simulate network loss and document a release/rollback decision. Retain Device matrix, crash logs, build instructions and release checklist.

**Final integration lab — Offline-Capable Mobile Client:**

Build a mobile client for an existing APP backend or equivalent service. Support authenticated access, accessible navigation, offline edits, defined conflict resolution, interruption recovery and a documented release candidate.

**Success criteria:**

- Demonstrate functional and accessible navigation on at least two representative device configurations.
- Show correct recovery after app termination and loss/recovery of connectivity.
- Verify authentication, minimal permission requests and safe handling of local sensitive data.
- Provide reproducible build/test steps and a documented synchronization limitation.

**Evidence to retain:**

- A version-controlled implementation, configuration and exact steps for reproduction.
- Input/workload data and automated tests or repeatable manual verification records.
- Observed results, rejected alternatives, important design decisions and a technical retrospective.

**Failure analysis:**

Investigate duplicate queued writes, conflicts, stale tokens, lifecycle data loss and platform-specific regressions without assuming always-on connectivity.

**Expanded module assessment and lab requirements:**

- **Module 1 checkpoint and micro-lab:** Demonstrate navigation, form input, screen-reader announcements and reflow on representative devices.
- **Module 2 checkpoint and micro-lab:** Force stop, suspend and restart a workflow, then verify state and secure storage expectations.
- **Module 3 checkpoint and micro-lab:** Replay queued edits after losing connectivity, reject unauthorized replays, and resolve a conflicting write.
- **Module 4 checkpoint and micro-lab:** Produce a reproducible release artifact and a representative device-test matrix with negative cases.

- **Module 5 — Mobile Architecture & Typed Data (Refactor a stateful mobile feature):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Extract navigation, persistence and remote data access into testable components; migrate a seeded local data record safely.
  - Verification: Demonstrate state restoration and migration while contract tests reject invalid data.
  - Evidence: Architecture diagram, local migration script and tests.
  - Failure analysis: Explain stale navigation events, tight platform coupling and incompatible local migrations.
- **Module 6 — Device Capabilities, Permissions & Privacy (Implement a permission-safe mobile workflow):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Add a feature that uses a device capability, exercise granted, denied, revoked and temporarily unavailable permissions, and verify deletion behavior.
  - Verification: The app degrades gracefully without permission and never retains or exposes data beyond documented policy.
  - Evidence: Permission-state recordings, data inventory and tests.
  - Failure analysis: Explain one-time permission expiry, unexpected background access and leaked local caches.
- **Module 7 — Mobile Networking & Energy (Diagnose a high-drain synchronization loop):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Reproduce unnecessary background network work under a controlled mobile network profile, then reduce requests while preserving correctness.
  - Verification: Show measured request counts/energy proxies and correct behavior after reconnection.
  - Evidence: Network traces, scheduling profile, test settings and trade-off.
  - Failure analysis: Account for platform background limits, repeated push delivery and conflicting offline edits.
- **Module 8 — App Distribution & Operational Quality (Ship and rollback a simulated mobile release):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Build a release candidate, distribute to a testing cohort or local test channel, inject a regression and document containment.
  - Verification: Show versioned build artifacts, release notes, crash reproduction and rollback plan.
  - Evidence: Build metadata, device matrix, test logs and staged rollout record.
  - Failure analysis: Explain non-reversible app-store releases, unrecoverable local migrations and user privacy in crash reports.

**Exit assessment expectation:**

Demonstrate the subject outcomes on an unfamiliar example, show at least one negative path and retain evidence allowing another reviewer to reproduce the result. Checkpoint answers must explain mechanisms, while the final integration lab must integrate and verify the expanded topics.

**Exit demonstration:**

Demonstrate the working implementation, explain the relevant mechanisms, reproduce at least one failure and repair, and defend the chosen trade-offs using retained evidence.
