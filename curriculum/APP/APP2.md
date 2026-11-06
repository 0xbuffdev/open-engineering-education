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

1. **Build, test, and evaluate the Production Frontend** — `lab`

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

Build a responsive, accessible frontend backed by a real API. Include loading, empty, error and success states, automated tests, and performance notes.

**Expanded module assessments and practical work:**

- **Module 1 checkpoint and micro-lab:** Demonstrate keyboard-only use, programmatic labels and recoverable validation errors, not just visual appearance.
- **Module 2 checkpoint and micro-lab:** Test zoom and reflow, prevent clipped controls, and use an explicit responsive layout rationale.
- **Module 3 checkpoint and micro-lab:** Explain task order and demonstrate cancellation, no leaked listeners, and clear fetch error reporting.
- **Module 4 checkpoint and micro-lab:** Exercise loading, empty, error, partial-success, and stale-result cases in tests.

- **Module 5 — TypeScript & Component Design (Refactor a brittle frontend flow into typed components):**
  - Prerequisites: Complete the module lessons and explain its stated outcomes.
  - Environment: A controlled local application or service, with tool versions and test data documented.
  - Required work: Refactor a complex form or asynchronous feature into typed components with explicit state transitions and runtime validation.
  - Verification: Show invalid states are unreachable through supported controls and malformed server responses are rejected.
  - Evidence: Component contracts, transition table, tests, and before/after architecture note.
  - Failure analysis: Identify unsound casts, duplicated state, implicit shared dependencies, and unhandled rejected promises.
- **Module 6 — Frontend Data & API Integration (Make a multi-step frontend workflow recoverable):**
  - Prerequisites: Complete the module lessons and explain its stated outcomes.
  - Environment: A controlled local application or service, with tool versions and test data documented.
  - Required work: Connect a frontend to a real API, test retries and unauthorized responses, then introduce and repair a stale-cache or optimistic-update defect.
  - Verification: Demonstrate loading, empty, failed, successful, and cancelled interactions without displaying stale authorized data.
  - Evidence: Automated integration tests, API responses, UI recordings, and error-state checklist.
  - Failure analysis: Explain duplicate mutations, stale rendering, cached private data, and retry loops.
- **Module 7 — Accessibility & Usability Engineering (Audit and repair an inaccessible interface):**
  - Prerequisites: Complete the module lessons and explain its stated outcomes.
  - Environment: A controlled local application or service, with tool versions and test data documented.
  - Required work: Run a documented accessibility audit including keyboard-only navigation and screen-reader inspection, then fix representative failures.
  - Verification: Demonstrate resolved focus, labeling, contrast, announcement, and reflow issues in the same test environment.
  - Evidence: Audit checklist, recordings, accessibility tree observations, and regression tests.
  - Failure analysis: Explain automation blind spots, focus traps, announcements that fire too late, and screen-reader versus visual discrepancies.
- **Module 8 — Browser Performance & Production Diagnostics (Profile and fix a slow frontend interaction):**
  - Prerequisites: Complete the module lessons and explain its stated outcomes.
  - Environment: A controlled local application or service, with tool versions and test data documented.
  - Required work: Measure a deliberately slow interaction or load path under repeatable CPU/network constraints, fix a demonstrated bottleneck, and rerun usability tests.
  - Verification: Show comparable baseline and updated traces and no regression in the feature's functional and accessibility tests.
  - Evidence: Profile settings, traces, measurement variance, tests, and optimization trade-off.
  - Failure analysis: Account for cold versus warm caches, variable networks, misleading averages, and over-optimized microbenchmarks.

**Exit assessment expectation:**

Demonstrate the course outcomes through a new scenario, including at least one negative path and independently reproducible evidence. Checkpoint answers must explain the mechanism and not merely name a tool. The final integration lab must incorporate and verify the expanded material.

**Exit demonstration:**

The learner can structure a frontend application, explain state ownership, and diagnose a broken asynchronous flow without relying on trial-and-error edits.

---
