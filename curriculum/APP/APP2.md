# APP2 — Frontend Engineering

**Program:** APP — Application Engineering
**Type:** `course`
**Prerequisites:** [APP1](APP1.md)
**Duration:** 9 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Develop browser-based software from semantic markup through TypeScript application logic, component architecture, state management, accessibility, routing, and performance.

## Learning outcomes

By the end of this course, the learner will be able to:

- Build semantic, responsive, and accessible interfaces.
- Structure browser applications using JavaScript/TypeScript and reusable components.
- Manage local and asynchronous application state deliberately.
- Implement robust forms, validation, loading, empty, and error states.
- Test frontend behavior and investigate client-side performance problems.
- Design and verify typed frontend component contracts, including server-response validation and explicit UI state transitions.
- Evaluate interfaces for keyboard, screen-reader, localization and responsive-layout correctness.
- Profile browser loading and interaction performance and defend a measured optimization without degrading accessible behavior.
- Test asynchronous data-fetching, caching and mutation recovery against network and authorization failures.

## Modules

### Module 1 — Semantic Web Foundations

#### Outcomes

- Explain **Semantic HTML and document structure** in the context of the course.
- Apply **Forms, labels, and accessible interaction** in a problem, implementation, experiment, or design decision.

- Implement and verify form semantics with keyboard and assistive-technology behavior.

#### Lessons

1. **Course introduction: Frontend Engineering** — `lesson`

   Develop browser-based software from semantic markup through TypeScript application logic, component architecture, state management, accessibility, routing, and performance.
2. **Semantic HTML and document structure** — `lesson`
3. **Forms, labels, and accessible interaction** — `lesson`
4. **Accessibility tree and semantic control behavior** — `lesson`
5. **Keyboard focus order, errors, and announcements** — `lesson`
6. **Accessible names, descriptions, and form constraints** — `lesson`
7. **semantic structure** — `test`
8. **Build an accessible form from a written specification** — `lab`

### Module 2 — CSS & Responsive Interfaces

#### Outcomes

- Explain **Layout, positioning, and responsive design** in the context of the course.
- Apply **Designing consistent UI structure** in a problem, implementation, experiment, or design decision.

- Explain and debug responsive layout constraints on multiple screen sizes and input methods.

#### Lessons

1. **Layout, positioning, and responsive design** — `lesson`
2. **Designing consistent UI structure** — `lesson`
3. **CSS cascade, inheritance, and specificity** — `lesson`
4. **Grid, flexbox, intrinsic sizing, and overflow** — `lesson`
5. **Responsive images, text reflow, and reduced motion** — `lesson`
6. **layout reasoning** — `test`
7. **Recreate a responsive interface from a reference specification** — `lab`

### Module 3 — Browser Programming

#### Outcomes

- Explain **JavaScript/TypeScript in the browser** in the context of the course.
- Apply **DOM, events, and browser APIs** in a problem, implementation, experiment, or design decision.

- Trace asynchronous browser behavior and manage cleanup and failures predictably.

#### Lessons

1. **JavaScript/TypeScript in the browser** — `lesson`
2. **DOM, events, and browser APIs** — `lesson`
3. **Event loop, task queue, and microtasks** — `lesson`
4. **Async/await, promises, cancellation, and fetch errors** — `lesson`
5. **DOM ownership, event delegation, and lifecycle cleanup** — `lesson`
6. **browser execution** — `test`
7. **Build an interactive component using browser APIs without a framework** — `lab`

### Module 4 — Application State & UX States

#### Outcomes

- Explain **Components, composition, and application state** in the context of the course.
- Apply **Forms, validation, routing, loading, empty, and error states** in a problem, implementation, experiment, or design decision.

- Structure state and asynchronous UI transitions so failures and retries preserve user intent.

#### Lessons

1. **Components, composition, and application state** — `lesson`
2. **Forms, validation, routing, loading, empty, and error states** — `lesson`
3. **Typed component inputs and state invariants** — `lesson`
4. **Client-state versus server-state ownership** — `lesson`
5. **Router boundaries, optimistic updates, and stale responses** — `lesson`
6. **state ownership** — `test`
7. **Implement all user-visible states for one asynchronous workflow** — `lab`

### Module 5 — TypeScript & Component Design

#### Outcomes

- Design typed component contracts without confusing compile-time checks with runtime validation.
- Use explicit state transitions and component boundaries to constrain invalid user flows.

#### Lessons

1. **Types as constraints and runtime validation boundaries** — `lesson`
2. **Reusable components and composition contracts** — `lesson`
3. **State machines and discriminated UI states** — `lesson`
4. **Dependency boundaries, rendering ownership, and events** — `lesson`
5. **Typed component contracts and state transitions** — `test`
6. **Refactor a brittle frontend flow into typed components** — `lab`

### Module 6 — Frontend Data & API Integration

#### Outcomes

- Implement a typed data-access boundary that handles invalid data, retries, and stale cache state.
- Present accurate interaction states when requests are rejected, cancelled, or repeated.

#### Lessons

1. **Request lifecycle and response parsing** — `lesson`
2. **Authentication/session UX and authorization outcomes** — `lesson`
3. **Data fetching caches and invalidation** — `lesson`
4. **Mutations, optimistic UI, and rollback** — `lesson`
5. **Pagination, loading boundaries, and network resilience** — `lesson`
6. **Server state and mutation failure scenarios** — `test`
7. **Make a multi-step frontend workflow recoverable** — `lab`

### Module 7 — Accessibility & Usability Engineering

#### Outcomes

- Evaluate a realistic workflow against explicit accessibility criteria with testable findings.
- Preserve meaningful interaction across keyboard, touch, screen reader, and translated text.

#### Lessons

1. **WCAG principles and applicable success criteria** — `lesson`
2. **Screen-reader and keyboard testing protocols** — `lesson`
3. **Internationalization, localization, and bidirectional layout** — `lesson`
4. **Usability checks and accessible visual feedback** — `lesson`
5. **Accessibility and interaction defect triage** — `test`
6. **Audit and repair an inaccessible interface** — `lab`

### Module 8 — Browser Performance & Production Diagnostics

#### Outcomes

- Identify the dominant loading or interaction bottleneck using repeatable measurements.
- Improve measured responsiveness without sacrificing correctness and accessibility.

#### Lessons

1. **Critical rendering path and asset budgets** — `lesson`
2. **Browser performance profiling and long tasks** — `lesson`
3. **Bundle loading, code splitting, and caching** — `lesson`
4. **Memory leaks, event-listener cleanup, and client telemetry** — `lesson`
5. **Interpreting client performance measurements** — `test`
6. **Profile and fix a slow frontend interaction** — `lab`

### Module 9 — Production Frontend

#### Outcomes

- Complete and explain the Production Frontend lab, demonstrating the applicable course outcomes and retaining required evidence.

#### Lessons

1. **Production frontend contract and readiness** — `test`
2. **Build, test, and evaluate the Production Frontend** — `lab`

## Completion requirements

- Complete the required practical exercises, knowledge checkpoints, and evaluated labs described in the modules.
- Complete the final integrated `lab` in the last module and satisfy its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, failures investigated, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required practical exercises:**

- reproduce a UI from a specification
- build accessible forms
- manage asynchronous state
- measure a slow interaction

**Final integration lab — required work:**

Required artifact: **Production Frontend**.

Build a responsive, keyboard-accessible TypeScript frontend backed by a **real locally running HTTP API** using synthetic data. Include loading, empty, success, invalid-input, authorization, cancellation, stale-response and recoverable error states; runtime response validation; automated and manual accessibility tests; and interpretable before/after browser performance measurements. A free framework is optional, and a paid production deployment is not required.

**Required module checkpoints and reproducible frontend labs:**

Each module has two example reasoning checkpoints with expected-answer guidance and one evaluated practical lab. Equivalent unfamiliar prompts may be used when they assess the same outcomes. Every lab distinguishes expected behavior from observed results and requires enough evidence for a reviewer to reproduce failures and corrections.

**Shared environment, accessibility and privacy:**

Use a local nonprivileged development environment with a current stable browser and developer tools, TypeScript in strict mode, a supported free Node.js runtime/package manager or equivalent reproducible TypeScript toolchain, and synthetic fixtures. Record exact browser/runtime/TypeScript/compiler/framework versions, lockfiles where applicable, build/test commands and relevant network/throttle settings. Use 127.0.0.1 with unprivileged ports for the APP1-compatible local HTTP API; do not use real user records, passwords, third-party telemetry, paid hosting, production credentials or privileged network access. Frameworks and test runners may be chosen from free/open-source tools, with reproducible local dependency setup; no named commercial framework or hosted service is mandatory. For manually observable accessibility, a free screen reader or an authentic instructor-provided sanitized observation can supplement DOM checks; distinguish direct personal tests from provided evidence and disclose coverage gaps.

**Shared assessment rules:**

- Develop against a synthetic local task/list frontend and APP1-compatible loopback HTTP fixture, or an equivalent documented local API and UI. No live production API, paid account or hidden service is required.
- Predict and test both normal and negative behavior. Browser screenshot appearance alone cannot establish semantic accessibility; static type-checking cannot validate unknown JSON, and a passing unit test cannot establish asynchronous UI recovery.
- Preserve meaningful focus, accessible names, keyboard use and error text across invalid-input and failure states; document manual checks and any untested assistive-technology behavior.
- Use explicit UI state transitions and guard against stale fetch completion, cancelled work, bad server shapes, failed mutations and cross-account cached data.
- Retain versioned source, test fixtures, relevant browser/HTTP traces, expected versus observed outputs, performance measurement conditions, independent reproduction instructions and a technical retrospective. Record tool limitations without inventing observations.
- The final Production Frontend integrates frontend and a running local API. It may use a free framework but must not rely on one particular provider or require commercial deployment.

**Module 1 — Semantic Web Foundations: checkpoint** — Required assessment details

- **Q1 (free):** A form shows the text 'Email' beside an input, but the text is not programmatically connected. Does visual proximity give the input an accessible name?
  - Expected answer and scoring: No. Associate an explicit label with the control using `for` and `id` or nesting when valid. An accessible name may come from other valid techniques, but visual adjacency alone does not provide a robust programmatic label. Test label activation and the accessibility tree.
- **Q2 (free):** A user submits an invalid required field. Why are a red border and placeholder text insufficient, and what should happen to error feedback and focus?
  - Expected answer and scoring: A color-only cue is inadequate and a placeholder is not a label. Expose a textual error linked to the field (such as `aria-describedby`), mark invalid state appropriately, maintain a predictable focus path to the error summary or first invalid control, and ensure the correction is possible with only a keyboard.

**Module 1 — Build an accessible form from a written specification: required lab** — Required assessment details

- **Objective:** Implement a meaningful semantic HTML form with inspectable accessible names, keyboard interaction and recoverable validation.
- **Prerequisites:** Complete the module's concepts and explain the checkpoint questions. Previously developed frontend/API fixtures may be reused only after their behavior and version assumptions are verified.
- **Environment:** Use a local nonprivileged development environment with a current stable browser and developer tools, TypeScript in strict mode, a supported free Node.js runtime/package manager or equivalent reproducible TypeScript toolchain, and synthetic fixtures. Record exact browser/runtime/TypeScript/compiler/framework versions, lockfiles where applicable, build/test commands and relevant network/throttle settings. Use 127.0.0.1 with unprivileged ports for the APP1-compatible local HTTP API; do not use real user records, passwords, third-party telemetry, paid hosting, production credentials or privileged network access. Frameworks and test runners may be chosen from free/open-source tools, with reproducible local dependency setup; no named commercial framework or hosted service is mandatory. For manually observable accessibility, a free screen reader or an authentic instructor-provided sanitized observation can supplement DOM checks; distinguish direct personal tests from provided evidence and disclose coverage gaps.
- **Procedure:**
  1. Given a written fixture asking for title, email and optional description, create a standalone HTML form with a heading hierarchy, associated labels, correct input types and a visible submit control.
  2. Document the expected tab/focus sequence and activate every control using the keyboard alone; verify the label focuses or toggles its intended control.
  3. Create client validation for missing title, invalid email and a bounded description length. Present each failure as visible text associated with the affected input without relying on color or placeholder alone.
  4. Demonstrate errors being announced or exposed in the browser accessibility tree with a documented method; do not use ARIA attributes as a substitute for correctly chosen native elements.
  5. Fix a seeded defect such as an unlabeled field or a submit button hidden from keyboard focus and record before/after observations.
  6. Run successful, empty, invalid and corrected submissions and compare output/error messages to the written form contract.
- **Expected result:** The form exposes correct labels and input semantics, supports keyboard-only submission and recovery, and rejects invalid inputs with understandable field-level feedback.
- **Verification:** Inspect DOM and accessibility names, tab order, keyboard submission and expected error/corrected state with manual reproduction and automated semantic assertions where available.
- **Evidence:** HTML source, form contract, input fixtures, keyboard-focus record, accessibility-tree observation, error screenshots or test output, and repaired defect.
- **Failure analysis:** Explain a visually labeled but unnamed control, inaccessible focus, invalid error association or incorrect use of aria-hidden/role.
- **Acceptance:** The documented normal, boundary, invalid and relevant failure cases meet the expected user-visible and technical contract. Actual tests, accessibility observations and reproduction evidence must support each accepted claim; missing required safety, state or keyboard behavior blocks completion.

**Module 2 — CSS & Responsive Interfaces: checkpoint** — Required assessment details

- **Q1 (free):** A flex item with a long unbreakable token causes horizontal overflow even though its container has width 100%. What constraints should you inspect?
  - Expected answer and scoring: Inspect the item's intrinsic minimum size, flex shrink, and whether `min-width: 0` (or an appropriate break strategy) is needed. A percentage width does not override all intrinsic sizing and overflow constraints; choose wrapping or scroll where semantics justify it.
- **Q2 (free):** What should happen when a learner requests reduced motion and enlarges text? Why is hiding overflow not a general accessibility fix?
  - Expected answer and scoring: Respect `prefers-reduced-motion` by removing or reducing nonessential animations, and retain readable reflow under enlarged text. Arbitrary `overflow: hidden` can clip content and controls; fix layout constraints or provide intentional scrolling for exceptional two-dimensional content.

**Module 2 — Recreate a responsive interface from a reference specification: required lab** — Required assessment details

- **Objective:** Implement a responsive layout that preserves content, controls and keyboard operation under narrow viewports, zoom and translated text.
- **Prerequisites:** Complete the module's concepts and explain the checkpoint questions. Previously developed frontend/API fixtures may be reused only after their behavior and version assumptions are verified.
- **Environment:** Use a local nonprivileged development environment with a current stable browser and developer tools, TypeScript in strict mode, a supported free Node.js runtime/package manager or equivalent reproducible TypeScript toolchain, and synthetic fixtures. Record exact browser/runtime/TypeScript/compiler/framework versions, lockfiles where applicable, build/test commands and relevant network/throttle settings. Use 127.0.0.1 with unprivileged ports for the APP1-compatible local HTTP API; do not use real user records, passwords, third-party telemetry, paid hosting, production credentials or privileged network access. Frameworks and test runners may be chosen from free/open-source tools, with reproducible local dependency setup; no named commercial framework or hosted service is mandatory. For manually observable accessibility, a free screen reader or an authentic instructor-provided sanitized observation can supplement DOM checks; distinguish direct personal tests from provided evidence and disclose coverage gaps.
- **Procedure:**
  1. Use a provided reference layout showing header/navigation, a task-list panel, filter controls and an item detail panel; capture required content hierarchy and responsive behavior before styling.
  2. Use CSS grid or flexbox with a declared container and breakpoint policy to implement a wide two-column view and a narrow one-column view; explain why each layout rule is needed.
  3. Test at a narrow 320-CSS-pixel equivalent viewport and at high browser zoom using the same functional content. Record any clipping or unintended horizontal document scroll.
  4. Insert a long unbroken item title, a translated longer navigation label and 200% text scaling; inspect min-size behavior and correct reflow without hiding interactive controls.
  5. Add focus-visible styling, responsive media behavior and a reduced-motion rule for any included transitions; verify visible focus and legible text.
  6. Introduce a controlled overflow defect, identify its container/intrinsic-size cause with developer tools and produce an independent regression case.
- **Expected result:** The layout rearranges predictably, essential content and controls remain usable at narrow width/high zoom, keyboard focus is visible, and nonessential movement respects user preferences.
- **Verification:** Compare reference semantics to computed browser layout, check widths and text expansion, and repeat the bad-case fixture after the correction.
- **Evidence:** CSS/HTML, layout rationale, responsive screenshots with viewport/zoom metadata, overflow inspection, focus/reduced-motion evidence and before/after measurements.
- **Failure analysis:** Explain hard-coded dimensions, overflow clipping, misplaced stacking order, unreadable zoom or an unsupported claim of full accessibility from screenshots alone.
- **Acceptance:** The documented normal, boundary, invalid and relevant failure cases meet the expected user-visible and technical contract. Actual tests, accessibility observations and reproduction evidence must support each accepted claim; missing required safety, state or keyboard behavior blocks completion.

**Module 3 — Browser Programming: checkpoint** — Required assessment details

- **Q1 (free):** Predict the typical log order for synchronous `console.log('A')`, a queued `setTimeout(() => console.log('T'), 0)`, a fulfilled-Promise `.then(() => console.log('M'))`, and synchronous `console.log('B')` in one browser task.
  - Expected answer and scoring: A then B then M then T under ordinary browser event-loop semantics: synchronous code runs to completion, a Promise reaction microtask runs at the microtask checkpoint, and the timer callback is scheduled as a later task. A zero delay is not a guarantee of a particular wall-clock execution time.
- **Q2 (free):** Does calling `AbortController.abort()` guarantee that an earlier fetch or application callback can never update a component?
  - Expected answer and scoring: No. Abort signals can cancel compatible pending operations, but completion/races and other callbacks may already be in flight. Verify current request identity or state generation before applying results, handle AbortError deliberately and clean up listeners when the component is removed.

**Module 3 — Build an interactive component without a framework: required lab** — Required assessment details

- **Objective:** Construct and debug a DOM interaction using JavaScript/TypeScript events, async behavior and explicit resource cleanup without a UI framework.
- **Prerequisites:** Complete the module's concepts and explain the checkpoint questions. Previously developed frontend/API fixtures may be reused only after their behavior and version assumptions are verified.
- **Environment:** Use a local nonprivileged development environment with a current stable browser and developer tools, TypeScript in strict mode, a supported free Node.js runtime/package manager or equivalent reproducible TypeScript toolchain, and synthetic fixtures. Record exact browser/runtime/TypeScript/compiler/framework versions, lockfiles where applicable, build/test commands and relevant network/throttle settings. Use 127.0.0.1 with unprivileged ports for the APP1-compatible local HTTP API; do not use real user records, passwords, third-party telemetry, paid hosting, production credentials or privileged network access. Frameworks and test runners may be chosen from free/open-source tools, with reproducible local dependency setup; no named commercial framework or hosted service is mandatory. For manually observable accessibility, a free screen reader or an authentic instructor-provided sanitized observation can supplement DOM checks; distinguish direct personal tests from provided evidence and disclose coverage gaps.
- **Procedure:**
  1. Create a vanilla browser component for searching a supplied local list or a loopback API with input, submit, results, empty state and visible error text.
  2. Implement DOM event delegation or deliberate listener binding, then explain which node owns each listener and how it is removed when the component unmounts.
  3. Run a small synchronous/microtask/task ordering trace and predict the event log before measuring its actual sequence and timing caveats.
  4. Trigger two requests in rapid succession with controlled delays. Ensure the older response cannot overwrite the newer result, even if cancellation races with completion.
  5. Simulate network refusal and a server HTTP error separately; show the distinct user-visible states, and cancel an in-flight request during removal/navigation.
  6. Add an automated or repeatable manual regression for stale response, missing cleanup and invalid input and demonstrate a repaired seeded defect.
- **Expected result:** The component displays the most recent valid response, reports failures predictably, and leaves no intentionally retained event listener or stale UI update after teardown.
- **Verification:** Compare controlled request ordering and DOM snapshots with a hand-worked state table; check listener lifetimes, cancellation behavior and error display across repeat runs.
- **Evidence:** Source, event-loop trace, delayed fixture server logs, DOM transition results, teardown/cancellation tests, error fixtures and defect explanation.
- **Failure analysis:** Explain an unhandled rejected promise, assuming abort prevents every stale callback, a leaked listener or misunderstanding the microtask/task boundary.
- **Acceptance:** The documented normal, boundary, invalid and relevant failure cases meet the expected user-visible and technical contract. Actual tests, accessibility observations and reproduction evidence must support each accepted claim; missing required safety, state or keyboard behavior blocks completion.

**Module 4 — Application State & UX States: checkpoint** — Required assessment details

- **Q1 (free):** A data-loading component tracks independent booleans `loading`, `error`, `ready` and `empty`. What is a risk of this design, and how could you specify a clearer state contract?
  - Expected answer and scoring: Independent booleans permit contradictory combinations. Use an explicit state machine or a tagged state such as idle/loading/success/empty/error with defined allowed transitions and appropriate payloads, then test that unsupported combinations cannot be reached through supported events.
- **Q2 (free):** A user navigates from account A to account B while a request for A is still pending. What must prevent the old response from appearing in B's view?
  - Expected answer and scoring: Tie results to active identity/request generation, cancel where possible and check identity before applying. Clear or isolate account-specific cached state on context changes; an old response must not render stale private information in another user's session.

**Module 4 — Implement user-visible states for an asynchronous workflow: required lab** — Required assessment details

- **Objective:** Model and test all relevant UI states for one request-driven workflow with explicit transitions and preserved user intent.
- **Prerequisites:** Complete the module's concepts and explain the checkpoint questions. Previously developed frontend/API fixtures may be reused only after their behavior and version assumptions are verified.
- **Environment:** Use a local nonprivileged development environment with a current stable browser and developer tools, TypeScript in strict mode, a supported free Node.js runtime/package manager or equivalent reproducible TypeScript toolchain, and synthetic fixtures. Record exact browser/runtime/TypeScript/compiler/framework versions, lockfiles where applicable, build/test commands and relevant network/throttle settings. Use 127.0.0.1 with unprivileged ports for the APP1-compatible local HTTP API; do not use real user records, passwords, third-party telemetry, paid hosting, production credentials or privileged network access. Frameworks and test runners may be chosen from free/open-source tools, with reproducible local dependency setup; no named commercial framework or hosted service is mandatory. For manually observable accessibility, a free screen reader or an authentic instructor-provided sanitized observation can supplement DOM checks; distinguish direct personal tests from provided evidence and disclose coverage gaps.
- **Procedure:**
  1. Build a fixture task search or list workflow using a local HTTP API from APP1 (or an equivalent loopback server), documenting idle, loading, empty, success, error and optionally partial-success states.
  2. Define a transition table specifying accepted events, resulting state, data/error payload and user-visible message; prohibit contradictory loading/success/error combinations.
  3. Implement search/input submission and an error recovery action that preserves the user's typed values while allowing a safe retry.
  4. Simulate a slow first request followed by a fast second request; verify a stale success or stale error cannot overwrite the currently selected query.
  5. Test navigation or change of active user context and verify that sensitive cached data from the previous context is not displayed under the new one.
  6. Create and repair a seeded state defect, retaining the counterexample and a regression assertion.
- **Expected result:** Every declared state is visibly understandable and reachable on purpose; invalid combinations are not rendered and stale responses cannot displace active user/query state.
- **Verification:** Run transition tests against a state/event table and verify DOM content and focus for normal, empty, rejected, slow and context-switch cases.
- **Evidence:** State diagram/table, code, controlled API fixtures, UI snapshots or test output, failure/retry trace and corrected regression.
- **Failure analysis:** Explain contradictory booleans, stale authorized data, lost form input, endless loading or a retry that duplicates side effects.
- **Acceptance:** The documented normal, boundary, invalid and relevant failure cases meet the expected user-visible and technical contract. Actual tests, accessibility observations and reproduction evidence must support each accepted claim; missing required safety, state or keyboard behavior blocks completion.

**Module 5 — TypeScript & Component Design: checkpoint** — Required assessment details

- **Q1 (free):** A fetch result is cast as `as User[]`. Does TypeScript verify the JSON response is actually an array of valid User objects?
  - Expected answer and scoring: No. Type assertions affect static checking and are removed at runtime. Parse untrusted JSON as unknown, validate its shape/fields at runtime and report an explicit failure for unexpected values.
- **Q2 (free):** What does a discriminated union improve when rendering loading, ready and error components, and what can it not guarantee?
  - Expected answer and scoring: A tagged union constrains compile-time states and enables exhaustive branch checking, reducing invalid combinations in typed code. It does not validate external JSON, prohibit casts/any or automatically prove correct runtime transitions or accessible UI behavior.

**Module 5 — Refactor a brittle frontend flow into typed components: required lab** — Required assessment details

- **Objective:** Turn brittle duplicated frontend logic into typed, testable components with explicit runtime boundaries and predictable state transitions.
- **Prerequisites:** Complete the module's concepts and explain the checkpoint questions. Previously developed frontend/API fixtures may be reused only after their behavior and version assumptions are verified.
- **Environment:** Use a local nonprivileged development environment with a current stable browser and developer tools, TypeScript in strict mode, a supported free Node.js runtime/package manager or equivalent reproducible TypeScript toolchain, and synthetic fixtures. Record exact browser/runtime/TypeScript/compiler/framework versions, lockfiles where applicable, build/test commands and relevant network/throttle settings. Use 127.0.0.1 with unprivileged ports for the APP1-compatible local HTTP API; do not use real user records, passwords, third-party telemetry, paid hosting, production credentials or privileged network access. Frameworks and test runners may be chosen from free/open-source tools, with reproducible local dependency setup; no named commercial framework or hosted service is mandatory. For manually observable accessibility, a free screen reader or an authentic instructor-provided sanitized observation can supplement DOM checks; distinguish direct personal tests from provided evidence and disclose coverage gaps.
- **Procedure:**
  1. Begin with a small provided TypeScript UI flow containing a permissive cast of server data, repeated rendering logic and independent state booleans; capture a failing malformed-response fixture first.
  2. Define public component input/output contracts and a discriminated UI-state union with payload only for appropriate variants.
  3. Implement a runtime decoder or type guard for API JSON starting from `unknown`, rejecting missing IDs, wrong field types and unexpected top-level structure with safe error text.
  4. Refactor into small rendering and data-access components or functions with explicit dependencies, preserving the original successful visible behavior.
  5. Run TypeScript strict type-checking plus runtime tests for malformed JSON, normal result, empty list, error and deliberately invalid event order.
  6. Document the distinction among compile-time type safety, runtime validation, component ownership and accessibility, and retain a repaired defect.
- **Expected result:** Strict compilation succeeds; all tested unknown/malformed server responses fail safely; the component API admits coherent typed states and preserves behavior for valid data.
- **Verification:** Compare before/after type-check results, runtime decoder tests and DOM state traces; inspect whether invalid external values can bypass checks without an explicit escape hatch.
- **Evidence:** Type declarations, runtime validator, input/output contract, strict compiler configuration, red/green tests, component diagram and defect rationale.
- **Failure analysis:** Explain an unsound type assertion, misuse of any, shared mutable dependencies, unreachable union case omitted or believing type-checking replaces runtime tests.
- **Acceptance:** The documented normal, boundary, invalid and relevant failure cases meet the expected user-visible and technical contract. Actual tests, accessibility observations and reproduction evidence must support each accepted claim; missing required safety, state or keyboard behavior blocks completion.

**Module 6 — Frontend Data & API Integration: checkpoint** — Required assessment details

- **Q1 (free):** A GET request returns HTTP 401 but the fetch promise resolves normally. What should frontend code do, and why might retrying blindly be unsafe?
  - Expected answer and scoring: The fetch promise generally resolves for an HTTP response including 401; inspect response.ok/status and handle authorization/user state explicitly. Do not loop retries for rejected credentials or automatically repeat non-idempotent writes.
- **Q2 (free):** A user optimistically marks a task complete, but the server rejects the mutation while a stale list fetch finishes. What state must be reconciled?
  - Expected answer and scoring: Rollback or reconcile the optimistic local item to the authoritative server outcome, prevent an older list response from overwriting newer current state, and display recoverable error feedback. Cache invalidation and request identity should be specified, not inferred.

**Module 6 — Make a multi-step frontend workflow recoverable: required lab** — Required assessment details

- **Objective:** Connect a typed UI to a local API, correctly handle authorization, caching, mutation rollback and stale/out-of-order results.
- **Prerequisites:** Complete the module's concepts and explain the checkpoint questions. Previously developed frontend/API fixtures may be reused only after their behavior and version assumptions are verified.
- **Environment:** Use a local nonprivileged development environment with a current stable browser and developer tools, TypeScript in strict mode, a supported free Node.js runtime/package manager or equivalent reproducible TypeScript toolchain, and synthetic fixtures. Record exact browser/runtime/TypeScript/compiler/framework versions, lockfiles where applicable, build/test commands and relevant network/throttle settings. Use 127.0.0.1 with unprivileged ports for the APP1-compatible local HTTP API; do not use real user records, passwords, third-party telemetry, paid hosting, production credentials or privileged network access. Frameworks and test runners may be chosen from free/open-source tools, with reproducible local dependency setup; no named commercial framework or hosted service is mandatory. For manually observable accessibility, a free screen reader or an authentic instructor-provided sanitized observation can supplement DOM checks; distinguish direct personal tests from provided evidence and disclose coverage gaps.
- **Procedure:**
  1. Run a local APP1-compatible API providing list/detail/update routes with synthetic records and a controllable response delay and error mode.
  2. Define the frontend data-access contract: parse JSON as unknown, validate it, distinguish transport refusal, HTTP errors and schema failures, and map these to visible UI states.
  3. Build a paginated task list and one optimistic update with explicit rollback or refetch behavior; document which state is cached and what invalidates it.
  4. Simulate unauthorized 401 and forbidden 403 results, ensuring the UI neither reports success nor leaks data from a previous user context; exercise a simulated logout/context switch.
  5. Trigger out-of-order requests, mutation conflicts and an aborted read; ensure only the active valid response updates the current view.
  6. Test bounded retry only for chosen safe/idempotent operations with documented retry count and no duplicate write effects; demonstrate an unretriable case.
  7. Document a cache/rollback defect and its repair, including which automated integration tests would catch it.
- **Expected result:** The view is consistent with authoritative data, never displays stale user-context data on a context switch and provides clear paths for failed, cancelled and retried actions.
- **Verification:** Run scripted API fixtures and UI tests across success, 401/403, network refusal, stale response, failed mutation, rollback and pagination boundaries.
- **Evidence:** Typed API interface and decoder, local server fixtures, state traces, integration assertions, cache policy, rollback logs and corrected defect.
- **Failure analysis:** Explain retry storms, stale cache after auth changes, non-idempotent mutation replay, optimistic state that never rolls back or treating JSON types as trustworthy.
- **Acceptance:** The documented normal, boundary, invalid and relevant failure cases meet the expected user-visible and technical contract. Actual tests, accessibility observations and reproduction evidence must support each accepted claim; missing required safety, state or keyboard behavior blocks completion.

**Module 7 — Accessibility & Usability Engineering: checkpoint** — Required assessment details

- **Q1 (free):** A custom menu opens with a mouse but cannot be reached or closed with a keyboard. Why is adding a tabIndex to its container insufficient?
  - Expected answer and scoring: Making a container focusable does not supply appropriate native/menu semantics, focus management, selection behavior, Escape handling, or a clear tab path. Prefer native controls when possible; evaluate keyboard and accessible-name behavior manually.
- **Q2 (free):** How can a frontend look acceptable in its default language but fail when translated or displayed right-to-left?
  - Expected answer and scoring: Longer strings can clip controls, fixed dimensions can truncate labels, and direction-dependent layouts may reverse unexpectedly. Use scalable constraints, direction-aware logical CSS properties, appropriate lang/dir handling and meaningful locale formatting, and verify with representative fixtures.

**Module 7 — Audit and repair an inaccessible interface: required lab** — Required assessment details

- **Objective:** Find, prioritize and correct accessibility/usability defects using manual keyboard, assistive technology and responsive/locale evidence.
- **Prerequisites:** Complete the module's concepts and explain the checkpoint questions. Previously developed frontend/API fixtures may be reused only after their behavior and version assumptions are verified.
- **Environment:** Use a local nonprivileged development environment with a current stable browser and developer tools, TypeScript in strict mode, a supported free Node.js runtime/package manager or equivalent reproducible TypeScript toolchain, and synthetic fixtures. Record exact browser/runtime/TypeScript/compiler/framework versions, lockfiles where applicable, build/test commands and relevant network/throttle settings. Use 127.0.0.1 with unprivileged ports for the APP1-compatible local HTTP API; do not use real user records, passwords, third-party telemetry, paid hosting, production credentials or privileged network access. Frameworks and test runners may be chosen from free/open-source tools, with reproducible local dependency setup; no named commercial framework or hosted service is mandatory. For manually observable accessibility, a free screen reader or an authentic instructor-provided sanitized observation can supplement DOM checks; distinguish direct personal tests from provided evidence and disclose coverage gaps.
- **Procedure:**
  1. Start with a provided intentionally flawed task workflow containing three independent issues: missing accessible name, incorrect focus after a dialog closes and clipped text at high zoom or translated length.
  2. Record the browser, OS and any available assistive technology, and audit named controls, document structure, keyboard-only access, focus order/visibility, validation errors and semantic announcement expectations.
  3. Perform at least one actual keyboard-only walkthrough. Where a free local screen reader is available, inspect one critical flow; otherwise analyze authentic sanitized screen-reader evidence and explicitly state that direct assistive-technology behavior was not independently tested.
  4. Test narrow/reflow layout at 320 CSS pixels or a comparable 400% zoom situation, longer localized strings, and an RTL fixture when layout supports bidirectional text; inspect clipped controls and reading order.
  5. Fix the three defects without disabling keyboard controls or hiding errors; run semantic/automated checks where available but retain manual evidence.
  6. Retest focus restoration, label naming, high-zoom reflow, error messaging and at least one nonvisual interaction; document any limitation of assistive-technology coverage.
- **Expected result:** The tested controls expose appropriate accessible names and focus behavior; high-zoom/translated content remains usable; unresolved assistive-technology limitations are transparently reported.
- **Verification:** Repeat an audit checklist and before/after keyboard and accessibility-tree observations; compare automated findings with manual evidence and explicitly limit untested claims.
- **Evidence:** Audit matrix, browser/assistive tool versions, screenshots or recordings, keyboard and screen-reader/reference observations, fixed source and regression checks.
- **Failure analysis:** Explain a false-positive automated pass, focus lost after dialog closure, an ARIA attribute hiding a control, a clipped localized label or claiming direct screen-reader verification without observing it.
- **Acceptance:** The documented normal, boundary, invalid and relevant failure cases meet the expected user-visible and technical contract. Actual tests, accessibility observations and reproduction evidence must support each accepted claim; missing required safety, state or keyboard behavior blocks completion.

**Module 8 — Browser Performance & Production Diagnostics: checkpoint** — Required assessment details

- **Q1 (free):** A learner measures a page-load time once before an optimization and once after using different network throttles. Can the result establish an improvement?
  - Expected answer and scoring: No. Define consistent test hardware/browser, cache state, network/CPU settings, fixture data and multiple runs. Report distribution/variance and avoid overclaiming from uncontrolled one-off timings.
- **Q2 (free):** A list virtualization optimization improves scroll timing but removes offscreen items from the accessibility tree unexpectedly. Is it acceptable without further evaluation?
  - Expected answer and scoring: Not automatically. Verify correct keyboard navigation, accessible counts/positions where applicable, focus preservation and functional behavior. A performance win cannot compensate for an important accessibility or correctness regression.

**Module 8 — Profile and fix a slow frontend interaction: required lab** — Required assessment details

- **Objective:** Use repeatable profiling evidence to choose, evaluate and defend a frontend optimization without degrading accessibility or correctness.
- **Prerequisites:** Complete the module's concepts and explain the checkpoint questions. Previously developed frontend/API fixtures may be reused only after their behavior and version assumptions are verified.
- **Environment:** Use a local nonprivileged development environment with a current stable browser and developer tools, TypeScript in strict mode, a supported free Node.js runtime/package manager or equivalent reproducible TypeScript toolchain, and synthetic fixtures. Record exact browser/runtime/TypeScript/compiler/framework versions, lockfiles where applicable, build/test commands and relevant network/throttle settings. Use 127.0.0.1 with unprivileged ports for the APP1-compatible local HTTP API; do not use real user records, passwords, third-party telemetry, paid hosting, production credentials or privileged network access. Frameworks and test runners may be chosen from free/open-source tools, with reproducible local dependency setup; no named commercial framework or hosted service is mandatory. For manually observable accessibility, a free screen reader or an authentic instructor-provided sanitized observation can supplement DOM checks; distinguish direct personal tests from provided evidence and disclose coverage gaps.
- **Procedure:**
  1. Run a local fixture page with an intentionally slow list interaction or oversized initial bundle, using a fixed synthetic dataset and a specified browser build.
  2. Capture at least five baseline measurements under documented CPU/network constraints and cache conditions. Record an interaction duration or comparable trace metric, units, variability and relevant performance timeline events.
  3. Inspect performance tooling for excessive DOM work, repeated renders, layout thrashing, unnecessary asset loading or long tasks; identify one probable bottleneck supported by evidence.
  4. Make one bounded change such as DOM batching, reduced redundant rendering or deferred noncritical work; retain the pre-change revision for comparison.
  5. Repeat measurements with identical fixtures and conditions, calculate a representative summary with variance, and describe uncertainty or regressions honestly even if the change is not faster.
  6. Repeat functional, keyboard, accessible-name and focus tests, and check any change in network/cache behavior before claiming the optimization is acceptable.
  7. Record a retrospective covering one misleading initial metric or assumption and the revised explanation.
- **Expected result:** The submitted report identifies a real observed bottleneck and an evidence-based decision with comparable traces; the final version preserves required correctness and accessibility.
- **Verification:** Compare repeat-run traces, settings and test results; inspect whether the alleged optimization improves the chosen user-relevant metric or whether a rollback was justified.
- **Evidence:** Browser/OS/profile configuration, raw samples and variability, before/after trace, changed code, regression suite and engineering decision.
- **Failure analysis:** Explain cold-versus-warm cache confusion, an unreliable mean, optimizing a microbenchmark unrelated to UX or a performance change that breaks keyboard access.
- **Acceptance:** The documented normal, boundary, invalid and relevant failure cases meet the expected user-visible and technical contract. Actual tests, accessibility observations and reproduction evidence must support each accepted claim; missing required safety, state or keyboard behavior blocks completion.

**Module 9 — Production Frontend: checkpoint** — Required assessment details

- **Q1 (free):** A production-like UI shows correct happy-path data but remains stuck in loading after a 401 response. Which acceptance requirements fail?
  - Expected answer and scoring: Failure-state visibility, authorization handling, recoverable interaction and explicit UI transitions fail. Passing a successful request does not demonstrate robust frontend behavior. Add a controlled 401 fixture and assert correct state and user-facing guidance.
- **Q2 (free):** Why does a screenshot of a responsive layout plus a green type-check fail to establish a production-ready course integration?
  - Expected answer and scoring: It does not demonstrate runtime schema validation, keyboard/assistive interaction, API failures, stale-response defense, test reproducibility, release documentation or measured client behavior. Independent observable evidence is needed for each relevant course outcome.

**Module 9 — Build, test and defend the Production Frontend: required lab** — Required assessment details

- **Objective:** Deliver one tested, responsive and accessible TypeScript frontend backed by a real local HTTP API, with independently reproducible correctness, failure handling and performance evidence.
- **Prerequisites:** Complete the module's concepts and explain the checkpoint questions. Previously developed frontend/API fixtures may be reused only after their behavior and version assumptions are verified.
- **Environment:** Use a local nonprivileged development environment with a current stable browser and developer tools, TypeScript in strict mode, a supported free Node.js runtime/package manager or equivalent reproducible TypeScript toolchain, and synthetic fixtures. Record exact browser/runtime/TypeScript/compiler/framework versions, lockfiles where applicable, build/test commands and relevant network/throttle settings. Use 127.0.0.1 with unprivileged ports for the APP1-compatible local HTTP API; do not use real user records, passwords, third-party telemetry, paid hosting, production credentials or privileged network access. Frameworks and test runners may be chosen from free/open-source tools, with reproducible local dependency setup; no named commercial framework or hosted service is mandatory. For manually observable accessibility, a free screen reader or an authentic instructor-provided sanitized observation can supplement DOM checks; distinguish direct personal tests from provided evidence and disclose coverage gaps.
- **Procedure:**
  1. Choose a bounded synthetic project such as a task board or issue list with at least a list/search route, detail view and one mutation, and publish its frontend contract including valid, empty, rejected and invalid states.
  2. Use semantic HTML, responsive CSS, TypeScript strict checking and components with explicit data/state contracts; a free UI framework is optional, not a compulsory product choice. Document dependency versions and installation.
  3. Connect the running frontend to a real loopback HTTP API (from APP1 or equivalent) that returns JSON and supports controlled response delays, invalid schema and authorization failure fixtures; a frontend-only mocked promise does not satisfy the integration requirement.
  4. Implement usable loading, empty, success, invalid-input, network error, authorization error, cancellation, stale-request and retry/recovery paths. Bound retries and protect user-specific cached data during context changes.
  5. Build a repeatable browser/unit/integration test suite for semantics, keyboard behavior, runtime validation, UI transitions, out-of-order requests, rollback and API response boundaries.
  6. Demonstrate narrow-screen/high-zoom reflow, text expansion, visible focus and an accessible form or dialog; record at least one manual keyboard audit plus actual assistive-tech observation where available, disclosing any limitations.
  7. Collect repeatable measurements for one meaningful load or interaction property and justify a constrained improvement or rollback without damaging functionality or accessibility.
  8. From a clean checkout, reproduce frontend build/run/test and the local API fixture; record a technical defense covering component/state ownership, trust boundaries, known limitations, an original fault and a verified correction.
- **Expected result:** A reviewer can build the app and local API, complete a successful task workflow, trigger documented negative paths, inspect accessible keyboard behavior and reproduce a meaningful performance comparison.
- **Verification:** Use the same published acceptance matrix across browser and API fixtures, run from a clean environment and reproduce one error recovery and one stale-request scenario independently.
- **Evidence:** Versioned frontend/API fixture, component diagram, state machine, HTTP contract, test logs, manual accessibility notes, responsive/locale checks, performance samples, README, review and retrospective.
- **Failure analysis:** Explain a happy-path-only app, trusting TypeScript to validate server JSON, stale private data, inaccessible controls, missing error recovery, undocumented dependencies or unsupported performance claims.
- **Acceptance:** The documented normal, boundary, invalid and relevant failure cases meet the expected user-visible and technical contract. Actual tests, accessibility observations and reproduction evidence must support each accepted claim; missing required safety, state or keyboard behavior blocks completion.

**Exit demonstration:**

The learner can structure a frontend application, explain state ownership, and diagnose a broken asynchronous flow without relying on trial-and-error edits.

---
