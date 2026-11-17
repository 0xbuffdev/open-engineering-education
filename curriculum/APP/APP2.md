# APP2 — Browser & Frontend Engineering

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `core`
**Prerequisites:** [APP17](APP17.md) — HTML & CSS Engineering, [APP19](APP19.md) — TypeScript Programming
**Duration:** 12–16 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–14 focused hours/week (provisional; calibrate against learner evidence)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Engineer interactive browser applications **without first depending
on a UI framework**. Begin with user tasks and acceptance criteria,
then make semantic, responsive documents interactive through
browser DOM and event APIs. Model typed state and validation,
handle asynchronous data and network failures, preserve user
intent across transitions and navigation, protect browser trust
boundaries, evaluate accessible interaction and usability,
and diagnose a measured performance or lifecycle defect.
Finish with a reproducible, tested application and an
independent engineering defense.

This is the **browser interaction** course, not a second
course in HTML/CSS, JavaScript or the TypeScript language.
[APP17](APP17.md) already teaches semantic markup, native
forms, accessibility foundations and responsive CSS.
[APP18](APP18.md) and [APP19](APP19.md) supply language,
asynchrony, module, testing and static type competencies;
APP19 also depends on APP18. APP2 teaches their application
to browser host APIs, DOM ownership, interactive components,
asynchronous views, client-side navigation and user needs.

**Framework-neutral is a real assessment boundary.**
Use TypeScript and standard browser DOM/Fetch/History APIs,
not React component lifecycles, framework routers,
framework-specific state management or server rendering.
Those belong to planned [APP20](ARCHITECTURE.md)
React Application Engineering. Likewise, designing a
production API, implementing authorization on a server,
building Node HTTP infrastructure, database engineering,
distributed caching and infrastructure deployment belong
to APP3, APP21, APP4, APP8 or other specialized courses.

A locally served static document and compiled browser JavaScript
are sufficient for the core project. Use a supplied local
HTTP fixture server, deterministic injected transport adapter,
or equivalent free mock responses to model real request
outcomes; students are **not required to implement a backend**.
The direct prerequisites are APP17 and APP19; APP1/APP18
are satisfied transitively. A compiler and supported browser
with development tools can be installed or provided before
the assessments. The implemented project must remain
reproducible with local synthetic data and no required
public endpoint, remote test harness, paid tool, domain,
proprietary accessibility software, account, API key or
production identity system.

User research and accessibility evidence must be honest.
A synthetic persona is a design hypothesis, not a human
interview. A keyboard-only review or automated audit is
not proof that a screen-reader user tested the interface.
Actual participant feedback is optional where access or
consent is unavailable; publish what was observed, not
fictional conclusions. Do not collect or publish private
user data to satisfy an OEE assessment.

Browser guarantees must also be accurately bounded.
`fetch()` normally **fulfills** for an HTTP 404 or 500
response, but rejects for a network or abort-related
failure; successful TypeScript checking does not validate
JSON at runtime. `history.pushState()` does not itself
emit `popstate`. Client-side route and permission checks
do not replace server-side authentication/authorization;
CORS restricts browser script access, not who is allowed
to use an API. Avoid claiming a fixed rendering interval,
universal cache policy or complete WCAG certification
from one synthetic environment.

Duration and workload are estimates, not proof of educational
quality. Modules organize authentic explanations,
investigations, failure analysis and progressively less
scaffolded implementation. Only the explicitly required
assessments below establish summative completion evidence;
other module activities are formative.

## Learning outcomes

- **APP2-O1:** Translate a bounded user task into observable interaction requirements, acceptance criteria, data/privacy assumptions and state-transition scenarios, distinguishing supplied assumptions from genuine user-research findings.
- **APP2-O2:** Implement predictable, semantic DOM updates using standard browser APIs and TypeScript, explaining browser-owned versus application-owned state, safe content rendering, and differences between DOM properties and HTML strings.
- **APP2-O3:** Explain and correctly handle browser event propagation, delegation, defaults and listener lifecycles; preserve keyboard, pointer, focus and cleanup behavior through dynamic interface changes.
- **APP2-O4:** Investigate browser task/microtask scheduling, rendering opportunities and work on the main thread; choose appropriate updates and cleanup strategies for timing-sensitive interactions without assuming exact frame or network timing.
- **APP2-O5:** Implement accessible interactive forms with native semantics, explicit domain validation and useful field-level error/recovery behavior, and distinguish client checks from server trust and authorization.
- **APP2-O6:** Model typed UI inputs and state transitions with reusable framework-independent components and discriminated states, validating untrusted runtime values before presenting them and preventing unsupported actions.
- **APP2-O7:** Implement and diagnose browser Fetch API workflows, distinguishing HTTP failure status from rejected network operations, response decoding, abort/cancellation limits, origin/credentials rules and data trust boundaries.
- **APP2-O8:** Manage asynchronous view state, request races, stale results, simple cache validity, mutations and recovery without losing user intent, replaying unsafe actions, or exposing stale private content.
- **APP2-O9:** Provide usable client-side navigation with meaningful URLs, History API behavior, direct-link fallback, back/forward correctness, and intentional keyboard focus, title and scroll behavior.
- **APP2-O10:** Identify and mitigate representative browser application security and privacy risks, including untrusted DOM content, origin/CORS misconceptions, credential exposure, client storage limits and unauthorized UI data handling.
- **APP2-O11:** Audit and repair dynamic accessibility behavior using keyboard interaction, focus management, accessible names/status announcements, semantic controls, responsive reflow and reasonable assistive-technology inspection or disclosed equivalent evidence.
- **APP2-O12:** Evaluate a representative interaction against explicit usability, localization and human-centered requirements, accounting for user feedback provenance, error comprehension, input methods, reduced motion and variable text direction or length.
- **APP2-O13:** Design deterministic browser integration and negative-path tests, reproduce real DOM/network/focus defects, and measure a bounded loading or interaction bottleneck without mistaking a noisy trace for universal performance evidence.
- **APP2-O14:** Deliver, reproduce, maintain and defend a cohesive framework-neutral browser application with accessible user flows, typed and validated state, resilient data access, security boundaries, automated verification and an unfamiliar bounded change.

## Modules

### Module 1 — Course Orientation, Browser App Boundaries and User Tasks

#### Outcomes

- APP2-O1
- APP2-O2
- APP2-O12

#### Lessons

1. **Browser Application Scope and Prior Foundations** — Explain how static documents gained scriptable DOM and application-like behavior; situate browser apps among progressive enhancement, client-rendered and traditional navigation models; identify which prerequisites supply Web mechanisms, semantic markup/CSS and TypeScript contracts; list capabilities APP2 applies rather than re-teaches.

2. **The browser as a constrained application host** — Describe Window, Document, DOM, events, storage, fetch and history as host APIs with security, lifecycle and support constraints.

3. **Problems, users and tasks** — Convert a fictional service request into a defined primary user task, expected result, business boundary and observable success without invented field research.

4. **State inventory and failure inventory** — Enumerate idle, editing, loading, success, empty, invalid, forbidden, failed, stale and recovery states appropriate to the actual workflow.

5. **Acceptance criteria and risk** — Write testable examples for keyboard access, correct results, invalid input, privacy, network failure and navigation while separating functional from nonfunctional criteria.

6. **Data provenance and ethical evaluation** — Distinguish synthetic personas and supplied stakeholder briefs from interviews, usability observations and real user evidence; minimize any collected feedback.

*Optional practice — task-mapping review:* Inspect a misleading happy-path-only interface specification and identify absent error, focus and authorization outcome cases.

### Module 2 — DOM Ownership, Safe Content and Structured Updates

#### Outcomes

- APP2-O2
- APP2-O3
- APP2-O6
- APP2-O10

#### Lessons

1. **DOM trees, references and mutations** — Inspect elements, text, attributes and event targets; distinguish DOM state from visual CSS rendering and JavaScript object state.

2. **Selectors and element construction** — Use querySelector, createElement, append, replaceChildren and textContent with explicit missing-target handling and stable ownership.

3. **Safe rendering of external values** — Demonstrate why textContent is safer for untrusted text than innerHTML; distinguish intentional trusted markup from unsafe string interpolation.

4. **Properties, attributes and live values** — Compare input.value, checked and DOM attributes as relevant; distinguish property state from serialized HTML.

5. **Incremental updates and preservation** — Update the smallest necessary region while preserving input selection, user-entered values, focus and unrelated content.

6. **Conditional structures and empty states** — Render meaningful loading, empty, failure and successful content with semantically appropriate elements and accessible descriptions.

7. **Component boundary without frameworks** — Organize a typed render/update/destroy interface using plain functions or classes; avoid assuming a virtual DOM or React lifecycle.

*Optional practice — DOM security defect:* Replace an unsafe dynamic HTML insertion with safe DOM construction and assert both displayed content and absence of injected executable elements.

### Module 3 — Events, Interaction and Lifecycle Cleanup

#### Outcomes

- APP2-O2
- APP2-O3
- APP2-O4
- APP2-O11

#### Lessons

1. **Capture, target and bubble phases** — Trace event propagation with explicit DOM structure and explain capture/bubble ordering without treating every event as bubbling.

2. **Event delegation and dynamic nodes** — Attach delegated handlers to a stable parent, interpret event.target/currentTarget and choose closest/contains checks.

3. **Default actions and prevention** — Use preventDefault only where replacing native behavior is justified; explain link, form and keyboard default semantics.

4. **Keyboard and pointer parity** — Keep native buttons and links where possible; test click, Enter, Space, touch and pointer behavior without inventing custom keyboard rules.

5. **Focus moves and focus restoration** — Explain document.activeElement, focus order and programmatic focus; restore focus after disclosure/dialog dismissal or routed updates when appropriate.

6. **Listeners and AbortSignal cleanup** — Add/remove event listeners intentionally, use listener signals where supported, and prevent duplicated callbacks after remount.

7. **DOM replacement and stale references** — Demonstrate a handler or selector referencing removed elements, then fix ownership and teardown rather than masking exceptions.

8. **Custom events and event contracts** — Use CustomEvent for a justified boundary, define payload shape and avoid accidental propagation or global event-bus coupling.

*Optional practice — interaction repair:* Reproduce a duplicate-action or lost-focus bug, provide failing test evidence and demonstrate a corrected listener lifecycle.

### Module 4 — Browser Scheduling and Rendering Work

#### Outcomes

- APP2-O3
- APP2-O4
- APP2-O13

#### Lessons

1. **Synchronous scripts and responsiveness** — Reproduce a bounded main-thread task that delays pointer/keyboard responses; distinguish a long task from slow network transfer.

2. **Tasks, microtasks and browser hosts** — Compare promises, queueMicrotask, timers and event dispatch with APP18 language foundations, identifying behavior dependent on the browser host.

3. **Rendering opportunities and animation frames** — Use requestAnimationFrame for visual update scheduling when appropriate and explain why it is not a guaranteed fixed-interval timer.

4. **Reading layout and writing style** — Trace style/layout invalidation and forced synchronous layout patterns, and explain how batching measurements and updates can reduce avoidable work.

5. **Timers, throttling and debouncing** — Apply bounded rate controls to search or resize interactions without losing the final user request and without using sleeps for correctness tests.

6. **Visibility and inactive pages** — Account for visibility and background scheduling limitations; avoid relying on hidden-tab timers as a durable operation queue.

7. **Cleanup of pending work** — Cancel owned timers, animation frames, listeners or pending requests on navigation/teardown; distinguish stop-notification from rollback of completed actions.

*Optional practice — scheduling trace:* Predict an interaction trace, collect actual browser observations, repair one ordering or responsiveness fault and state unproven timing assumptions.

### Module 5 — Interactive Forms, Validation and User Recovery

#### Outcomes

- APP2-O1
- APP2-O3
- APP2-O5
- APP2-O11

#### Lessons

1. **Native form semantics in a dynamic app** — Reuse APP17 labels, fieldsets, required constraints and submit behavior; add justifiable JavaScript interactions without replacing robust native semantics.

2. **Input parsing and explicit domain constraints** — Separate blank, malformed, out-of-range and business-rule-invalid fields; avoid using TypeScript types as input validation.

3. **Constraint Validation API** — Use checkValidity, validity states and controlled custom messages while acknowledging cross-browser message presentation differences.

4. **Submission and pending-state policy** — Prevent accidental duplicate submissions where required without trapping users in an indefinitely disabled UI.

5. **Accessible field feedback** — Associate error text with controls, provide concise actionable guidance, place focus appropriately and avoid excessive live announcements.

6. **Multi-step and draft forms** — Preserve entered values across conditional steps and recoverable failures while stating whether data is only in memory or stored.

7. **Progressive enhancement and server boundaries** — Explain native fallback and why JavaScript/client validation cannot replace server checks or prove authorization.

*Optional practice — form audit:* Inject missing and invalid values and repair a misleading success banner, hidden error or lost in-progress input.

### Module 6 — Typed Components and State Machines without React

#### Outcomes

- APP2-O2
- APP2-O5
- APP2-O6
- APP2-O13

#### Lessons

1. **TypeScript in a browser project** — Build TypeScript to browser-executable JS using documented local tooling, ES modules and browser-compatible imports; distinguish tsc checking from runtime validation.

2. **Component input and output contracts** — Define typed function or class inputs, DOM ownership, output events and teardown responsibility without a framework registry.

3. **Discriminated UI state models** — Represent idle/loading/success/empty/error/forbidden variants with state-specific data instead of contradictory booleans.

4. **Events as transitions** — Write an explicit transition table for user actions, async completion, cancellation and navigation, and identify invalid transitions.

5. **State versus DOM duplication** — Choose canonical application state and derived views; avoid storing stale duplicate state simultaneously in a model and uncontrolled DOM properties.

6. **External data as unknown** — Validate a local JSON fixture and reject malformed shapes before converting them into typed view models.

7. **Shared state and accidental coupling** — Create two component instances and verify no unintentional singleton state, listener or cache cross-contamination.

*Optional practice — state refactor:* Turn an ad-hoc conditional UI into a typed transition-driven component and demonstrate corrected invalid-state behavior.

### Module 7 — Fetch, HTTP Failure and Browser Trust Boundaries

#### Outcomes

- APP2-O6
- APP2-O7
- APP2-O10

#### Lessons

1. **Fetch versus server responses** — Explain Request, Response and response-body decoding, distinguishing network rejection from resolved 404/403/500 responses.

2. **HTTP Request and Response Contracts** — Use suitable methods, headers and JSON encoding with explicit media-type expectations and observable acceptance criteria; classify success, no-content, authentication-required, forbidden, conflict, rate-limited and server failure results without equating an HTTP 200 with a correct domain response.

3. **AbortController and request lifetime** — Abort a superseded fetch where appropriate, distinguish aborting consumption from undoing server side effects and test race behavior explicitly.

4. **Same-origin and CORS** — Explain browser-enforced origin restrictions, preflight, CORS response headers and why CORS is not an authentication or authorization mechanism.

5. **Credentials, cookies and CSRF limits** — Reason about fetch credentials mode, cookie attributes and cross-site request threats without asking learners to implement a full identity provider.

6. **Response validation** — Parse unknown JSON, reject wrong shapes and report errors without showing untrusted HTML; connect APP19 type/runtime boundaries to real browser input.

7. **Fixture service and deterministic transports** — Use supplied free local HTTP response fixtures, a service stub or an injected fetch adapter; no APP21 server authoring or cloud API is a prerequisite.

*Optional practice — network matrix:* Simulate 200/204/400/401/403/404/409/500, malformed JSON, aborted fetch and offline cases; compare the visible UI to its documented failure policy.

### Module 8 — Asynchronous Views, Cache Policies and Mutation Recovery

#### Outcomes

- APP2-O1
- APP2-O6
- APP2-O7
- APP2-O8
- APP2-O10

#### Lessons

1. **Explicit loading, empty, success and error states** — Show differences between no results, an unrequested resource, a genuine network error, and forbidden access.

2. **Latest-request-wins and request identity** — Introduce request IDs or lifecycle tokens to prevent an earlier response overwriting newer user intent, even if abort is unsupported or late.

3. **Separation of server and local UI state** — Explain which data belongs to the remote authority and which is an ephemeral selection, draft or display preference.

4. **Cache lifetime and freshness** — Define key, invalidation, stale/fresh and eviction policies for a small in-memory cache; avoid treating cache entries as permanently valid.

5. **Confidential-data cache rules** — Clear or isolate identity-scoped results after authorization changes and never persist sensitive API responses by accident.

6. **Optimistic updates and rollback** — Only use an optimistic UI when invariants, failure recovery, duplicate actions and conflict reconciliation are explicitly defined.

7. **Idempotent retry and unsafe replay** — Distinguish safe reading/retrying from retrying side-effecting mutations that may already have succeeded; represent uncertain outcomes truthfully.

8. **Partial results and pagination** — Handle empty pages, partial success, cursor or offset mismatches and merged page state with stable keys.

*Optional practice — race and cache defect:* Reproduce a stale authorized result or duplicate mutation, repair it and write a deterministic regression test without network sleep timing.

### Module 9 — Navigation, Browser History and Recovery of Context

#### Outcomes

- APP2-O1
- APP2-O3
- APP2-O9
- APP2-O11

#### Lessons

1. **Navigation models and server fallback** — Distinguish ordinary links/full navigations from client-rendered route handling, and explain why a direct deep link needs a working server/static-host fallback.

2. **URL anatomy and route input safety** — Parse query, hash and pathname with URL APIs, validate route parameters and avoid trusting unstructured URL strings.

3. **History API and browser Back/Forward** — Use pushState/replaceState with state restoration and popstate handling; note that pushState does not itself trigger popstate.

4. **Link semantics and interception rules** — Preserve modifier-click, context menu, copy-link and normal anchor behavior rather than hijack every navigation event.

5. **Focus, headings and document titles** — Update document title and focus intentionally on a client navigation, and verify screen-reader/keyboard awareness without inventing a universal focus rule.

6. **Scroll restoration and interaction continuity** — Plan scroll position, pending requests and draft-form state for backward and forward navigation.

7. **Route change and resource cleanup** — Cancel or ignore stale requests, dispose old listeners and avoid unauthorized content flashes on a changed route.

*Optional practice — deep-link incident:* Demonstrate a failure when loading a route directly or pressing Back, fix the environment/routing policy and record keyboard behavior.

### Module 10 — Browser Security, Persistence and Privacy

#### Outcomes

- APP2-O2
- APP2-O7
- APP2-O8
- APP2-O10

#### Lessons

1. **Threat models for a browser feature** — Identify attacker-controlled content, URLs, storage, responses, third-party scripts, credentials and cache visibility at a user-task boundary.

2. **DOM XSS and safe injection** — Reproduce a synthetic HTML-injection defect without executing real harmful code, then replace dangerous sinks with DOM construction/text content.

3. **Same-origin and CORS revisited** — Distinguish same-origin policy and CORS visibility restrictions from server authentication, authorization and deliberate content-sharing policy.

4. **Tokens, cookies and storage choices** — Explain risks of localStorage/sessionStorage and in-memory state for sensitive tokens; choose not to store secrets where unnecessary.

5. **Browser storage APIs and lifecycle** — Compare ephemeral in-memory state, local/session storage and IndexedDB at conceptual depth with retention and data-clear expectations; advanced offline architecture is elective.

6. **Cross-Site Requests and User Intent** — Explain why a browser can send some cross-site requests even if scripts cannot read responses and when CSRF protections belong to the server.

7. **CSP and defense in depth** — Describe a restrictive Content Security Policy, its interaction with script execution and why it is not a substitute for encoding/validation.

8. **Sensitive-state transitions** — Handle sign-out and forbidden responses by clearing identity-scoped views and caches, never displaying data solely because a hidden button exists.

*Optional practice — security and privacy test:* Repair untrusted text rendering or an identity-scoped stale-cache leak, and state server-side protections that APP2 cannot prove.

### Module 11 — Accessibility and Inclusive Dynamic Interaction

#### Outcomes

- APP2-O3
- APP2-O5
- APP2-O9
- APP2-O11
- APP2-O12

#### Lessons

1. **Native semantics before ARIA** — Reuse APP17 semantic controls; distinguish adding appropriate ARIA from overriding built-in behavior with incorrect roles.

2. **Keyboard operation and focus order** — Audit sequential focus, Enter/Space activation, visible focus, escape/cancel behavior and focus return after UI updates.

3. **Dialog, disclosure and composite patterns** — Use a justified accessible interaction pattern with defined keyboard navigation, modal focus containment and disclosure labeling.

4. **Accessible names, descriptions and status** — Expose meaningful dynamic button names, instructions, error descriptions and status messages with proportionate live-region semantics.

5. **State, visibility and accessibility tree** — Inspect how hidden, inert, disabled and offscreen elements differ for focus and assistive technologies.

6. **Zoom, reflow and multiple inputs** — Validate interaction at representative viewport/zoom conditions with touch and keyboard, avoiding offscreen error banners or obscured focus.

7. **WCAG 2.2 application review** — Select relevant published success criteria for the actual widget and disclose any criterion not tested rather than claim whole-site certification.

8. **Automated and manual evidence** — Combine automated checks, keyboard-only inspection and feasible screen-reader observations; clearly disclose when actual assistive-technology testing was not performed.

*Optional practice — accessibility defect triage:* Repair a focus trap, missing error announcement or inaccessible async status and show the before/after behavior in the same environment.

### Module 12 — Human-Centered Evaluation, Localization and Feedback

#### Outcomes

- APP2-O1
- APP2-O5
- APP2-O11
- APP2-O12

#### Lessons

1. **From user job to usable flow** — Establish the intended user action, context, success signal and recoverable failure path rather than treating polished visual styling as usability.

2. **Task-based usability inspection** — Write a repeatable task and observation rubric covering confusion, error recovery, discoverability and completion; separate observed behavior from speculation.

3. **Feedback provenance and consent** — Explain when synthetic walkthroughs, accessibility heuristics, peer testing and real-user studies provide different strengths; use consent and minimal data collection for real participants.

4. **Useful guidance and error language** — Write plain, specific error and recovery messages and test whether a learner can interpret the next action.

5. **Input, language and locale variability** — Use appropriate Intl facilities for dates/numbers/display, avoid guessing user locale from one value and keep domain storage semantics clear.

6. **Long strings, bidi and writing direction** — Test representative translated/long strings and right-to-left content, including focus and logical CSS behavior without duplicating APP17's layout curriculum.

7. **Reduced motion and user preferences** — Honor `prefers-reduced-motion` and related user settings; ensure essential state changes remain understandable without animation.

8. **Assistive and low-bandwidth scenarios** — Inspect a constrained device/network/keyboard-only workflow and record usability evidence and explicitly unverified contexts.

*Optional practice — user-task improvement:* Use documented synthetic or consenting participant observations to correct one confusing state transition; explain limitations of the evaluation method.

### Module 13 — Browser Performance, Testing and Independent Frontend Defense

#### Outcomes

- APP2-O1
- APP2-O2
- APP2-O3
- APP2-O4
- APP2-O5
- APP2-O6
- APP2-O7
- APP2-O8
- APP2-O9
- APP2-O10
- APP2-O11
- APP2-O12
- APP2-O13
- APP2-O14

#### Lessons

1. **Instrumentation and reproducibility** — Record browser/runtime, throttling setup, cache state, fixture sizes, devtools trace inputs and repeated trials before drawing performance conclusions.

2. **Loading and rendering metrics at course depth** — Observe resource loading, long tasks, layout shifts or interaction delay as applicable; connect symptoms to actual user-facing effects.

3. **Measure one real bottleneck** — Investigate a DOM update, unnecessary event listener, costly layout read/write or oversized request; show before/after traces and variance.

4. **Prevent accessibility regressions** — Repeat keyboard, focus and reduced-motion checks after an optimization, showing it did not trade usable behavior for a better synthetic score.

5. **Deterministic component and fetch tests** — Test pure state transitions, DOM actions and injected transport fixtures separately from an actual local-browser integration test.

6. **Negative-path integration matrix** — Assert invalid form inputs, HTTP errors, network reject, late responses, abort, forbidden, history traversal, and cleanup without relying only on happy-path screenshots.

7. **Complete a cohesive user task** — Integrate framework-free typed components, form and route behavior, resilient data fetching, safe rendering and accessible feedback into one bounded local application.

8. **Fresh checkout and unfamiliar change** — Reproduce the browser app on a free local server, verify build/test commands, handle a previously unseen change or defect and defend implementation boundaries and remaining limitations.

## Completion requirements

All **fourteen required course outcomes** must be demonstrated
through the **six required summative assessments** listed here.
A learner can progressively improve the same scoped browser
application rather than build six unrelated frontends.
Formative module exercises and exploratory experiments are
not independent completion gates merely because they appear
in the module sequence.

| Required assessment | Required outcome coverage | Principal evidence |
| --- | --- | --- |
| `APP2-AS1` — User-task Requirements and Framework-Neutral DOM Interaction | APP2-O1, APP2-O2, APP2-O3, APP2-O4, APP2-O6 | Requirements/task table, typed DOM component source, synthetic fixtures, event/timing and focus traces, before/after cleanup test, security-negative test for untrusted text, and a concise mechanism-based rationale |
| `APP2-AS2` — Accessible Form and Typed State-Transition Investigation | APP2-O1, APP2-O3, APP2-O5, APP2-O6, APP2-O11, APP2-O12 | Form HTML/TypeScript component, state diagram, acceptance and invalid-input matrix, keyboard/focus/error recordings or equivalent annotated observations, regression tests, and a short task-evaluation limitations note |
| `APP2-AS3` — Asynchronous Data, Cache, and Navigation Recovery | APP2-O6, APP2-O7, APP2-O8, APP2-O9, APP2-O10, APP2-O13 | Typed transport and state code, locally reproducible fixture/adapter and versioned response scenarios, deterministic race/abort tests, route/history and focus traces, cache invalidation tests, and a failure-policy explanation |
| `APP2-AS4` — Dynamic Accessibility, Usability and Browser Security Audit | APP2-O1, APP2-O2, APP2-O5, APP2-O9, APP2-O10, APP2-O11, APP2-O12 | Audit scope and WCAG-criterion references, test environments, failing/passing examples, DOM/security regression tests, focus/status observations, representative localized/reflowed interaction, usability-task notes and remaining-risk statement |
| `APP2-AS5` — Browser Performance and Regression Diagnosis | APP2-O3, APP2-O4, APP2-O8, APP2-O11, APP2-O13 | Fixture and runnable app, before/after profiler trace or bounded observation log, reproducible procedure and timing summaries, identified cause, diff and normal/negative regression tests, and performance/accessibility trade-off rationale |
| `APP2-AS6` — Framework-Neutral Browser Application and Technical Defense | APP2-O1, APP2-O2, APP2-O3, APP2-O4, APP2-O5, APP2-O6, APP2-O7, APP2-O8, APP2-O9, APP2-O10, APP2-O11, APP2-O12, APP2-O13, APP2-O14 | Versioned source, static assets and local fixture recipe, TypeScript build steps, task/acceptance and state-transition matrices, scripted and browser test results, negative request and DOM security evidence, keyboard/focus and usability notes, performance measurements, clean-checkout verification, changed code history and accessible written/recorded/otherwise reviewable defense |

### Shared assessment, reproducibility and safety boundaries

- Use a supported standards-capable browser and current free
  TypeScript/JavaScript tooling from APP19/APP18. Record browser
  and tool versions, build/start/test commands and local origin.
  Serve local pages on loopback rather than relying on
  `file://` restrictions or a paid/public deployment.
- Use a synthetic documented dataset. Demonstrate HTTP and
  async failure behavior with a **provided local fixture
  service** or an injected Fetch-compatible adapter; do not
  make writing APP21 or APP3 backend service code a hidden
  prerequisite. An independently testable mock alone can
  establish many state transitions, while a bounded local
  browser/integration test checks actual DOM behavior.
- Use semantic APP17 HTML/CSS and browser-compatible
  JavaScript output from TypeScript without a React,
  component framework or paid bundler dependency. Do not
  falsely claim types exist at runtime. Validate actual
  response payloads before the internal model.
- At minimum, inspect happy, empty, malformed, forbidden,
  transient failure, abort and out-of-order completion
  cases as appropriate to the implemented workflow.
  Distinguish a fulfilled HTTP error `Response` from
  a rejected network operation and do not blindly retry
  a non-idempotent mutation after an uncertain outcome.
- Preserve native semantics, keyboard and focus behavior,
  accessible error/status presentation and navigability
  across success and failure states. Report which WCAG
  criteria or assistive technologies were actually
  inspected, with limitations, rather than offering
  unsupported whole-site conformance claims.
- Never paste secrets, session cookies, authorization
  tokens or personal data into source, browser logs,
  local fixtures, network captures or review evidence.
  Browser storage, CORS and hidden UI controls are not
  server-side authorization safeguards. Untrusted text
  must not enter executable HTML sinks.
- A provided synthetic persona/task, peer inspection,
  heuristic evaluation and actual participant usability
  observations are different kinds of evidence. Label
  their source truthfully and avoid manufacturing user
  interviews. If involving real participants, use
  consent and proportionate data minimization.
- For performance, record browser/device, network/CPU
  profiles, workload, warm/cold cache conditions and
  comparable before/after traces. A single performance
  score or noisy millisecond reading is not a reliable
  general production claim. Retest accessibility and
  correctness after optimizations.
- Include an appropriately scoped unseen fault or
  maintenance request aligned with the published
  outcomes. A technical defense can be written,
  recorded, synchronous or another equivalently
  accessible reviewable format; no hidden proprietary
  environment or additional backend course may be
  imposed by an evaluator.

### Required summative assessments

- **APP2-AS1** (required user-task requirements and framework-neutral dom interaction)
  - Outcomes: APP2-O1, APP2-O2, APP2-O3, APP2-O4, APP2-O6
  - Work: Given a fictional user task and accessible APP17-style static document, publish acceptance criteria and a state/interaction map, then add typed framework-neutral DOM behavior with event delegation or clearly owned handlers. Use safe text rendering for supplied synthetic untrusted values, preserve keyboard and native default behavior, and demonstrate disposal/cleanup after a controlled navigation or DOM replacement. Trace one browser task/microtask/rendering timing example with appropriately qualified predictions.
  - Criteria: The user/task brief identifies normal, invalid and recovery paths without inventing genuine interview evidence; the UI meets all published action, state and focus criteria and does not use an unsafe HTML injection sink for untrusted content. Event behavior distinguishes target/currentTarget and default actions, does not duplicate listeners on reinitialization, and supports keyboard input. Timing claims are consistent with documented browser observations rather than assumed exact frame ordering.
  - Evidence: Requirements/task table, typed DOM component source, synthetic fixtures, event/timing and focus traces, before/after cleanup test, security-negative test for untrusted text, and a concise mechanism-based rationale.

- **APP2-AS2** (required accessible form and typed state-transition investigation)
  - Outcomes: APP2-O1, APP2-O3, APP2-O5, APP2-O6, APP2-O11, APP2-O12
  - Work: Implement a multi-state, accessible form workflow with native HTML semantics, explicit typed state transitions and correct validation of runtime values. Document idle/editing/invalid/pending/success/failure/retry behavior, preserve draft input through recoverable errors, give field-specific accessible guidance and test keyboard navigation, status announcement and focus movement. Provide a task-based usability check using synthetic or ethically obtained observations, clearly labeling the provenance.
  - Criteria: The declared transition table has no reachable contradictory states or unhandled submission path, valid input produces expected results, and invalid input does not falsely show success or erase values. Keyboard-only operation and semantic label/error association work; live announcements are proportionate and nonduplicative; source types do not substitute for runtime validation. Feedback is disclosed accurately as synthetic/peer/observed, without exaggerated user research or accessibility certification claims.
  - Evidence: Form HTML/TypeScript component, state diagram, acceptance and invalid-input matrix, keyboard/focus/error recordings or equivalent annotated observations, regression tests, and a short task-evaluation limitations note.

- **APP2-AS3** (required asynchronous data, cache, and navigation recovery)
  - Outcomes: APP2-O6, APP2-O7, APP2-O8, APP2-O9, APP2-O10, APP2-O13
  - Work: Build a browser data-access boundary with a supplied local fixture HTTP service or independently testable injected fetch adapter, and a browser view with documented route/history behavior. Handle successful, empty, malformed, unauthorized/forbidden, conflict and HTTP 5xx responses, rejected network operations, abort and out-of-order completions; prove a superseded request cannot overwrite current user intent. If a mutation or cache is included, specify invalidation/retry/rollback and identity-scoped cleanup; test direct links and Back/Forward without requiring a learner-written backend framework.
  - Criteria: Fetch success checks Response.ok/status and validates body shape; HTTP 4xx/5xx fulfillment is not misclassified as a network rejection. Stale responses and late aborts do not leak or re-render private identity-scoped data; mutations are not naively replayed after uncertain failure. Route URLs, Back/Forward, page titles, focus and cleanup match the stated policy. Browser CORS/credential behavior is explained without claiming CORS enforces application authorization.
  - Evidence: Typed transport and state code, locally reproducible fixture/adapter and versioned response scenarios, deterministic race/abort tests, route/history and focus traces, cache invalidation tests, and a failure-policy explanation.

- **APP2-AS4** (required dynamic accessibility, usability and browser security audit)
  - Outcomes: APP2-O1, APP2-O2, APP2-O5, APP2-O9, APP2-O10, APP2-O11, APP2-O12
  - Work: Audit an interactive browser flow with deliberate defects in focus, status announcement, untrusted DOM rendering, state persistence and at least one localization/zoom issue. Select applicable WCAG 2.2 criteria and published task requirements, perform keyboard/manual inspection plus an automated tool when free and available, and carry out feasible screen-reader inspection or explicitly report an unperformed portion. Repair the defects, explain data/privacy and origin boundaries, and perform a repeatable task-based usability walkthrough with honest observation provenance.
  - Criteria: A relevant set of real keyboard, focus, error and status scenarios is tested with documented expected behavior and inspected after repair. Unsafe insertion of untrusted strings is removed; no client-only hiding, CORS check or storage choice is claimed as proof of server-side access control. The audit differentiates actual observed assistive-technology evidence from heuristic inference, accounts for RTL/long text or reduced motion where applicable, and offers no unsupported WCAG conformance claim.
  - Evidence: Audit scope and WCAG-criterion references, test environments, failing/passing examples, DOM/security regression tests, focus/status observations, representative localized/reflowed interaction, usability-task notes and remaining-risk statement.

- **APP2-AS5** (required browser performance and regression diagnosis)
  - Outcomes: APP2-O3, APP2-O4, APP2-O8, APP2-O11, APP2-O13
  - Work: Reproduce an observable slow loading or interaction path in a locally served framework-free browser application. Capture comparable browser measurements with stated device/browser/throttling and warm/cold-cache conditions, identify a DOM/layout/event/network cause, implement a bounded correction, and rerun both measurements and keyboard/accessibility/async recovery regression tests. Investigate one additional listener leak, stale-state or user-perceived latency defect without requiring deep bundler optimization.
  - Criteria: The identified bottleneck is supported by trace or timing evidence rather than an invented universal threshold; repeat measurements disclose variance and browser conditions. The corrected behavior preserves user task completion, accessible focus/status and correct data state; no evidence depends solely on a synthetic audit score. Resource/listener cleanup and repeated interaction paths are testable and there is no unsupported claim of production-wide speedup.
  - Evidence: Fixture and runnable app, before/after profiler trace or bounded observation log, reproducible procedure and timing summaries, identified cause, diff and normal/negative regression tests, and performance/accessibility trade-off rationale.

- **APP2-AS6** (required framework-neutral browser application and technical defense)
  - Outcomes: APP2-O1, APP2-O2, APP2-O3, APP2-O4, APP2-O5, APP2-O6, APP2-O7, APP2-O8, APP2-O9, APP2-O10, APP2-O11, APP2-O12, APP2-O13, APP2-O14
  - Work: Deliver one cohesive, locally reproducible browser application using semantic APP17-style HTML/CSS, APP19 TypeScript built into browser-compatible JavaScript, framework-independent DOM components, an accessible form and navigation path, and a typed data-access boundary with controlled fixture-backed async state. Reuse suitable AS1–AS5 artifacts rather than producing unrelated apps. Demonstrate meaningful error, empty, loading, success, unauthorized and retry behavior, deliberate focus and history handling, safely rendered untrusted values, measurable interaction performance and a published keyboard/security test matrix. Accept an unfamiliar bounded change or bug report, verify it and independently defend the decisions, limitations and responsibility boundaries.
  - Criteria: A reviewer can build and launch the app from a clean checkout with free local tools and fixture data without React, paid cloud, proprietary accessibility platform, authentication provider or a real backend service. All documented user-task and failure criteria are reproducibly met with tests that include lost focus, malformed/late response, unsafe text, lifecycle cleanup and navigation. The unfamiliar change does not regress stated invariants; the learner accurately explains browser scheduling, TypeScript/runtime validation, Fetch response semantics, CORS/security limits, user feedback provenance and measurement uncertainty.
  - Evidence: Versioned source, static assets and local fixture recipe, TypeScript build steps, task/acceptance and state-transition matrices, scripted and browser test results, negative request and DOM security evidence, keyboard/focus and usability notes, performance measurements, clean-checkout verification, changed code history and accessible written/recorded/otherwise reviewable defense.

### Completion decision, readiness and revision safety

APP2 completion requires an inspectable acceptable decision
for `APP2-AS1` through `APP2-AS6` that jointly
establishes `APP2-O1` through `APP2-O14`. A working
demo, one successful network request, an automatic
accessibility report or a TypeScript check alone
does not prove independent interaction-engineering
competence. Materially incorrect security boundaries,
loss of user intent, inaccessible recovery or
unreproducible work must be repaired before passing.

Record the current course/spec revision, evaluated
assessment/outcome IDs, environment and fixture
assumptions, tested and untested cases, observations,
defect traces, review decisions, and acknowledged
limitations according to
[OEE Evidence Rules](../../spec/evidence-rules.md).

This course is an outcome-driven OEE `v0.2.0`
**draft**, not verified or learner-tested merely
because the source validator passes. The revision
retains APP2's recognizable browser/frontend course
identity while replacing its obsolete prerequisite
APP1 with the more precise APP17 + APP19 pair.
Prior APP2 completions retain their own recorded
course revision and cannot be silently converted
into passes under the new outcome/assessment IDs.
The optional deeper performance course APP10 and
future React course APP20 remain separate.

### Public non-mandatory study references

These free sources support inspection of actual browser
behavior and relevant public standards. They do not
replace the requirements and criteria stated above.

- [MDN DOM introduction](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
  and [MDN Events](https://developer.mozilla.org/en-US/docs/Web/Events)
  for element ownership, event propagation and cleanup.
- [MDN Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
  for HTTP status, response streams, abort and credentials.
- [MDN History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API/Working_with_the_History_API)
  for navigation and `popstate` semantics.
- [MDN web security](https://developer.mozilla.org/en-US/docs/Web/Security)
  for origin policy, injection, credentials and client-side limits.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
  and [WAI ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
  for tested interaction accessibility patterns.
- [MDN browser performance](https://developer.mozilla.org/en-US/docs/Web/Performance)
  and [web.dev performance](https://web.dev/learn/performance)
  for profiling, responsiveness and qualified interpretation.
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
  for static contracts; APP19 owns complete language instruction.
