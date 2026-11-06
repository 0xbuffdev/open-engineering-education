# APP13 — Mobile Application Engineering

**Program:** APP — Application Engineering
**Classification:** `elective`
**Type:** `course`
**Prerequisites:** [APP2](APP2.md), [APP3](APP3.md)
**Duration:** 6 weeks
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

## Modules

### Module 1 — Mobile UI & Navigation

#### Outcomes

- Apply platform navigation, touch target and accessibility conventions.
- Build resilient forms across keyboard, rotation and screen sizes.

#### Lessons

1. **Course introduction: Mobile Application Engineering** — `lesson`

   Extend application engineering to touch-first mobile clients, device lifecycle constraints, intermittent networks and controlled release processes. Build an accessible mobile interface that synchronizes safely with an authenticated backend.
2. **Mobile layouts and navigation models** — `lesson`
3. **Touch interaction and screen-reader support** — `lesson`
4. **Reviewing mobile usability** — `test`
5. **Audit a mobile workflow** — `lab`

### Module 2 — Lifecycle & Device State

#### Outcomes

- Explain foreground/background lifecycle and interruption recovery.
- Persist state without relying on a continuously running process.

#### Lessons

1. **Lifecycle events and state restoration** — `lesson`
2. **Local storage and device resource budgets** — `lesson`
3. **Reasoning about app restarts** — `test`
4. **Recover an interrupted task** — `lab`

### Module 3 — Offline Synchronization & Security

#### Outcomes

- Distinguish queued writes from confirmed server state.
- Define conflict handling and protect credentials and sensitive data.

#### Lessons

1. **Offline-first queues and conflict policies** — `lesson`
2. **Authentication, permissions and secure storage** — `lesson`
3. **Handling synchronization conflicts** — `test`
4. **Reconcile offline edits** — `lab`

### Module 4 — Testing & Release

#### Outcomes

- Design unit, integration and device-level mobile tests.
- Prepare signed/reproducible builds and review privacy/permission declarations.

#### Lessons

1. **Device matrices and automated UI tests** — `lesson`
2. **Crash diagnostics and staged release** — `lesson`
3. **Evaluating release readiness** — `test`
4. **Test a release candidate** — `lab`

### Module 5 — Offline-Capable Mobile Client

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

**Exit demonstration:**

Demonstrate the working implementation, explain the relevant mechanisms, reproduce at least one failure and repair, and defend the chosen trade-offs using retained evidence.
