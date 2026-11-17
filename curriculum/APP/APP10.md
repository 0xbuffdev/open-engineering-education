# APP10 — Advanced Frontend Performance

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `elective`
**Prerequisites:** [APP20](APP20.md) — React Application Engineering, [APP6](APP6.md) — Software Quality & Engineering Operations
**Duration:** 12–16 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–14 focused hours/week (provisional; requires learner/workload review)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

**Measure, explain and responsibly improve real frontend performance** across loading, browser rendering, input responsiveness, React state and render/commit behavior, caching, long sessions, memory retention and visual stability. Advance an already correct, accessible React application through trace-based investigations and reproducible experiments, not optimization folklore or unqualified benchmark scores. This is an **optional** APP specialization and is **not required for APP9 or Application Engineering graduation**.

**Direct prerequisites: APP20 and APP6.** APP20 owns core React state/render/commit, Hooks, Suspense, routing, testing and accessibility. APP6 owns controlled measurements, risk-based quality, reproducible CI and regression investigation. APP2 and APP17/18/19 are inherited through those dependencies. APP10 deepens browser/React-specific loading, responsiveness, memory and performance governance; it does **not** re-teach basic HTML/CSS, beginner browser APIs, foundational React, general backend testing or APP8's system-wide database/scaling architecture. APP7 deployments, cloud accounts and APP8 capacity studies are **not** required for this elective.

**Reference product and learner access:** Use a meaningful existing TypeScript React product (for example the APP20 project) with authentic user workflows, keyboard/focus states, a few representative routes and versioned synthetic data. Exercise a free local server, maintained browser DevTools and optionally open-source Playwright, Lighthouse, Web Vitals helper and trace/React Profiler tools. Browser binaries and dependencies may be downloaded during initial free provisioning; provide pinned/browser-profile instructions and local fixtures for assessment reproduction. No paid real-user monitoring (RUM), real participants, third-party analytics, public CDN, production domain or proprietary profiler is required.

**Separate what metrics actually mean.** As of this draft, LCP, INP and CLS are the Core Web Vitals: they describe loading, interaction responsiveness and visual stability. They are especially useful as *field* metrics when sampled over relevant visits and population segments; Chrome/Web Vitals published reference thresholds can inform priorities but do not become an inflexible local grading rubric. A page-load-only Lighthouse run cannot directly measure INP without a real user interaction: Total Blocking Time (TBT) is a useful **lab proxy**, not interchangeable with observed INP. If recording interaction timing, distinguish input delay, event processing and presentation delay, observed browser/API support, session context and the measured input. Field data, if genuinely available and ethically collected, must identify aggregation/population windows and missing navigation or SPA interactions; synthetic lab runs must never be labeled production field percentiles.

**Causal performance reasoning:** A slow LCP can involve TTFB, critical-resource discovery, network load and rendering delay. A slow interaction can originate in unrelated long main-thread tasks, React update work, style/layout, paint or queued follow-up rendering—not merely handler code. Inference must follow reproducible browser traces/controlled interventions, including resource waterfall, Long Animation Frame (LoAF) and React Profiler where supported. Always inspect cold/warm cache, CPU/network profiles, sample counts, expected interaction success, JS parse/evaluate cost, delayed work and measurement overhead.

**The baseline must remain usable and safe.** Improving bytes, a render count, a synthetic TBT score or an image load does not justify losing semantic content, keyboard focus, screen reader access, responsive layout, correct permission-scoped data, truthful loading/error states, secure cache invalidation or service-worker update behavior. Virtualization may reduce DOM work but can disrupt focus, find-in-page and assistive technologies. Overeager preload, memoization, browser worker, animation or cached data can increase CPU/memory, stale data and delivery complexity. Reject optimizations that lack measured user benefit or introduce unacceptable regression.

**Privacy and security are performance constraints.** Use synthetic identities and learner-owned local pages. Record only necessary performance signals; do not upload full URLs with tokens, user IDs, form content or confidential traces to a shared dashboard. Cache scope must not expose personalized data across logout, tenant changes, back/forward navigation or app version updates. Document user consent, retention and browser support for any real field telemetry without making public participant recruitment compulsory.

**Six publicly required assessments** build on one evolving frontend: baseline/causal trace, critical delivery and cache correctness, real input/React improvement, memory/CLS/accessibility, field-aware budgets and local regression governance, and independent integrated defense. Lesson investigations are formative unless included in those assessments. A performance result is meaningful only relative to declared environment and legitimate tasks. Course duration and workload are **provisional**; independent learner/reviewer evidence is necessary before any higher educational readiness claim.

## Learning outcomes

- **APP10-O1:** Establish a user-centered frontend performance problem, representative device/network/task conditions, explicit functionality/accessibility/security invariants and a falsifiable optimization hypothesis instead of optimizing metrics without user impact.
- **APP10-O2:** Design, collect and critically interpret valid browser laboratory and field performance measurements, including LCP, CLS, interaction responsiveness/INP, useful diagnostic proxies, sampling limits, warm/cold behavior, and realistic repeatability without confusing Lighthouse TBT with measured INP.
- **APP10-O3:** Diagnose actual browser loading and rendering behavior through navigation, tasks, Long Animation Frames, style/layout, paint and compositing traces, identifying an evidenced critical path and meaningful causal uncertainty.
- **APP10-O4:** Improve critical-content delivery and LCP by measuring resource discovery, TTFB, network load delay/duration and render delay, choosing suitable image sizes/formats, CSS, fonts, fetch priority and hints while preserving accessible content and layout stability.
- **APP10-O5:** Profile and improve JavaScript/React bundle delivery, dependency and third-party cost, parse/evaluate work, code-splitting and lazy imports while avoiding waterfalls, inaccessible fallback states, unnecessary hydration and broken feature behavior.
- **APP10-O6:** Design and verify safe HTTP/browser/application caching and repeat-navigation behavior including cache-control, versioned immutable assets, service-worker lifecycle where justified, navigation history/bfcache eligibility and sensitive identity-scoped data isolation.
- **APP10-O7:** Analyze input delay, event processing and presentation delay for meaningful user interactions, then apply justified task partitioning, scheduling, browser APIs and worker boundaries to improve interaction responsiveness without inventing an INP score from an unobserved interaction.
- **APP10-O8:** Identify actual React render/commit causes with profiler evidence, component ownership and stable identity; assess memoization, state locality, subscriptions, Suspense/transitions and route boundaries without cargo-cult optimization or hidden stale data.
- **APP10-O9:** Implement a measured high-data or complex-interaction performance improvement using bounded DOM work, virtualized or progressive rendering where appropriate, preserving keyboard focus, screen-reader usability, find/navigation behavior and accessible content alternatives.
- **APP10-O10:** Prevent layout instability and visually disruptive loading/animation by reasoning about CLS session windows, reserved space, media and font sizing, transitions and reduced-motion expectations under varied viewport and user settings.
- **APP10-O11:** Diagnose memory retention and long-session performance using repeatable heap/listener/worker/timer/resource evidence, repair a demonstrable lifecycle defect and avoid claiming 'no leaks' from a single noisy heap snapshot.
- **APP10-O12:** Introduce privacy-safe, consent- and retention-aware field/performance instrumentation where feasible, distinguishing field population/percentile segmentation, missing observations, browser API support and synthetic lab evidence.
- **APP10-O13:** Establish transparent performance budgets and regression detection with a fixed, locally reproducible workload, justified noise tolerance and false-positive/negative review, demonstrating failure on a seeded regression and correction without mandating commercial monitoring.
- **APP10-O14:** Evaluate performance alternatives quantitatively across cold and warm use, CPU/network/energy proxies, perceived task completion, accessibility, privacy, maintenance and deployment risk, and explain why a change or no-change decision is defensible.
- **APP10-O15:** Reproduce, improve and independently defend an integrated frontend performance upgrade under an unfamiliar bounded load, delivery, React rendering, interaction, visual-stability, cache or memory regression while preserving correct protected user behavior.

## Modules

### Module 1 — Performance as User-Centered Applied Science

#### Outcomes

- APP10-O1
- APP10-O2
- APP10-O14
- APP10-O15

#### Lessons

1. **Specialization and foundations** — Distinguish APP10 deep rendering and responsiveness investigation from APP2 browser fundamentals, APP20 React correctness and APP6 system-level measurement/CI.

2. **Evolution of Web performance practice** — Trace network waterfalls, synthetic benchmarks, user-centric milestones, responsiveness and field metrics as different tools rather than a universal ranking.

3. **Choose a consequential user workflow** — Select a real loading-to-task or long-session interaction in an APP20 React application, with clear user task, permission and data correctness.

4. **Define protected invariants** — Identify semantic HTML, keyboard/focus, accessible status, correct identity-scoped content and server-backed state that optimization must preserve.

5. **Form a falsifiable hypothesis** — Specify measured bottleneck, predicted user benefit, risk of regression and what a contrary trace would show.

6. **Create a two-configuration test matrix** — Choose constrained and typical CPU/network/viewport profiles, cache warm/cold, tool/browser versions and input data size.

7. **Source provenance and local tools** — Pin React/browser build and measurement harness versions and supply synthetic data and a free local served site.

8. **Avoid a benchmark-first design trap** — Explain why a faster synthetic empty page, isolated component or compressed transfer does not alone prove a better task.

*Optional practice — experiment review:* Reject an optimization proposal lacking a controlled baseline, meaningful interaction and trustworthy result threshold.

### Module 2 — Laboratory, Field, Core Web Vitals and Bias

#### Outcomes

- APP10-O1
- APP10-O2
- APP10-O12
- APP10-O13

#### Lessons

1. **Lab trace versus real-user monitoring** — Distinguish reproducible development tests from anonymized actual session distributions and explain why each can mislead.

2. **Core Web Vitals and metric scope** — Interpret Largest Contentful Paint (LCP), Interaction to Next Paint (INP) and Cumulative Layout Shift (CLS) for user loading, interaction and layout stability.

3. **INP is not synthetic TBT** — Explain that ordinary page-load-only Lighthouse tests can measure Total Blocking Time but cannot infer actual INP absent interactions.

4. **Initial navigation and soft navigation** — Discuss SPA route changes, bfcache and browser/measurement support limitations; document exactly which route transitions are sampled.

5. **Field percentile and population segments** — Use properly aggregated visit-level metrics and 75th-percentile mobile/desktop examples without treating a local trace as field percentile.

6. **Cache, warmup and thermal conditions** — Separate first load, return visit, JS JIT, browser memory, throttling and local machine interference.

7. **Measurement Coverage and Reproducibility** — Record representative input types, incomplete measurement, cross-origin iframe, browser API support and noisy trace overhead; use repeated runs with sample counts/spread and an explicit declared error/timeout policy rather than one winning trial.

*Optional practice — bad-vitals audit:* Correct a report that advertises a TBT-only synthetic audit as 'INP passed' and conflates field with lab results.

### Module 3 — Browser Main Thread, Frames and Rendering Traces

#### Outcomes

- APP10-O2
- APP10-O3
- APP10-O7
- APP10-O10

#### Lessons

1. **HTML parse to visible frames** — Trace document parsing, CSSOM, style calculation, layout, paint and compositing with a browser profiler rather than treating them as a fixed uniform pipeline.

2. **Task sources, microtasks and frame budget** — Explain browser task queues, microtask checkpoints, event callbacks and requestAnimationFrame timing relevant to input response.

3. **Long tasks and Long Animation Frames** — Interpret task duration and LoAF evidence where available, distinguishing each API's visibility/support from guaranteed universal coverage.

4. **Style recalculation and selector/layout work** — Profile large DOM changes and costly style invalidation before selecting containment or DOM restructuring.

5. **Layout thrashing and forced synchronous layout** — Reproduce a DOM read/write loop with forced reflow then batch or reorder mutations and compare trace phases.

6. **Painting, layering and compositing** — Analyze paint regions, layer proliferation, GPU memory and the risk that transforms create performance regressions.

7. **Correlate input to next paint** — Locate input delay, processing and presentation delay using instrumentation and actual browser traces.

8. **Source maps and causality** — Locate source and dependency chunks in a trace, mark the affected task and distinguish observational correlation from proven cause.

*Optional practice — render trace repair:* Explain a jank sequence that persists despite reducing JS handler time because layout and paint still dominate.

### Module 4 — Largest Contentful Paint and Critical Content Delivery

#### Outcomes

- APP10-O2
- APP10-O3
- APP10-O4
- APP10-O10

#### Lessons

1. **Decompose a slow LCP** — Compare TTFB, resource load delay, load duration and element render delay for a named candidate element and measured page.

2. **HTML discoverability and priority** — Prefer important visible image resources discoverable by early markup; examine fetchpriority and limit overprioritization.

3. **Don't lazy-load the LCP image** — Demonstrate that deferring initial viewport media can add request discovery delay, while offscreen lazy loading may be appropriate.

4. **Responsive image and modern encoding choices** — Compare srcset/sizes, appropriate width and compression/format against image decode, visual quality and bandwidth.

5. **Critical CSS and font effects** — Assess render-blocking styles, font-display choices, subset/font loading, fallback metrics and accessibility/CLS trade-offs.

6. **Server response and hydration gates** — Distinguish slow TTFB, client-only late discovery, loading overlays and JavaScript-rendered critical content.

7. **Resource hints and mistaken preloads** — Inspect preconnect, preload, modulepreload and priority under real waterfall rather than adding hints indiscriminately.

8. **Verify content paint and task usability** — Check LCP and first usable protected interaction separately, ensuring fast hero image isn't concealing unusable application.

*Optional practice — slow-hero experiment:* Repair a late discovered or overcompressed image and show the relevant waterfall plus rendering consequences.

### Module 5 — JavaScript Supply, Bundles and Startup Work

#### Outcomes

- APP10-O3
- APP10-O4
- APP10-O5
- APP10-O8

#### Lessons

1. **Bundle inventory and dependency provenance** — Identify entry chunks, common/vendor modules, transfer size, parse/evaluate cost and long third-party scripts.

2. **Route and component code splitting** — Measure initial load and subsequent navigation with dynamic import boundaries and correct error/loading handling.

3. **Import waterfalls and critical depth** — Inspect dependent lazy chunks, CSS requests and preloaded modules to avoid trading one bottleneck for sequential fetch delay.

4. **Tree-shaking and side-effect semantics** — Review module exports, build settings, dead code and sideEffects assumptions without removing necessary runtime behavior.

5. **External script and embed containment** — Evaluate third-party JS execution/permissions and performance, deferring optional code while preserving user choice and privacy.

6. **Parse, compile and hydration work** — Correlate bytes with actual scripting time and avoid claiming smaller gzip necessarily yields faster interaction.

7. **Worker candidate analysis** — Evaluate moving standalone CPU work off the main thread, structured-clone/transfer costs and worker lifecycle constraints.

8. **Deployable asset build and rollback** — Verify chunk names/hashes, old page/new asset availability, cache compatibility and versioned client behavior.

*Optional practice — startup regression:* Catch a route split that reduces entry bytes but breaks deep-link/slow-network navigation and restore accessible fallback.

### Module 6 — HTTP, Browser Cache, Service Workers and Return Visits

#### Outcomes

- APP10-O4
- APP10-O5
- APP10-O6
- APP10-O9
- APP10-O12

#### Lessons

1. **HTTP freshness and validators** — Review Cache-Control, ETag, conditional requests, vary and authorization impacts on resource freshness.

2. **Immutable versioned static assets** — Serve hashed JS/CSS/media with suitable caching while keeping entry HTML and manifest updates coherent.

3. **Avoid private data in shared caches** — Test login/logout/tenant switch and CDN/proxy/key policy against unauthorized cached personalized responses.

4. **Cold, warm and repeat navigation** — Measure first load, ordinary revisit, back/forward and stale resource handling with stated browser state and cache controls.

5. **Service worker scope and installation** — Explain registration, installation, activate, fetch and update without assuming a service worker improves all sites.

6. **Offline versus protected task correctness** — Define what may be safely offline and when authentication, writes and stale state must fail visibly or await reconciliation.

7. **Worker update and mixed-version assets** — Reproduce stale cached HTML/JS mismatch or an old service worker and select a safe update/recovery strategy.

8. **Back/forward cache versus app cache** — Check bfcache restoration and page lifecycle, including reasons it may not apply; preserve private UI state cleanup.

*Optional practice — cache poisoning scenario:* Repair an identity-scoped resource or version mismatch that becomes observable on repeat navigation.

### Module 7 — INP, Input Handling, Scheduling and Worker Offload

#### Outcomes

- APP10-O2
- APP10-O3
- APP10-O7
- APP10-O10
- APP10-O14

#### Lessons

1. **What INP measures** — Interpret page-level observed interactions and their input delay, event-processing and presentation-delay subparts across a real visit.

2. **Input delay from unrelated long work** — Trace a slow click queued behind unrelated scripting and decide whether scheduling or less main-thread work is necessary.

3. **Event handler processing cost** — Measure an expensive input/change/click handler and separate app computation from user-facing actual outcome.

4. **Presentation delay and rendering** — Demonstrate how DOM/layout/paint work after a handler can dominate responsiveness even with a fast callback.

5. **Task partitioning and yielding** — Compare safe chunking, yielding and scheduling mechanisms with available browser support and interleaving semantics.

6. **RequestAnimationFrame and rendering timing** — Use rAF deliberately, explain what it does not guarantee about input responsiveness, and avoid long callback paint stalls.

7. **Worker offload tradeoffs** — Move an appropriate CPU-bound operation to a worker and measure message-transfer, memory and cancellation effects.

8. **Perceived feedback and accessible pending states** — Show immediate truthful feedback while heavy work progresses without lying about committed server results.

*Optional practice — INP breakdown repair:* Reduce a slow interaction and demonstrate which phase improved instead of calling TBT directly measured INP.

### Module 8 — React Render/Commit Attribution and State Ownership

#### Outcomes

- APP10-O3
- APP10-O5
- APP10-O7
- APP10-O8
- APP10-O14

#### Lessons

1. **React Profiler and browser trace roles** — Distinguish React render and commit timing, actual DOM paint and browser input delay with correlated evidence.

2. **Render causes and cascading updates** — Locate props, context, external subscriptions and unstable callback/value identities responsible for expensive subtree work.

3. **State locality and derived data** — Reduce accidental high-level state updates and redundant transforms rather than copying props into cache state without proof.

4. **Memoization tradeoffs** — Measure React.memo, useMemo and useCallback costs and correctness; recognize stale closures and identity changes.

5. **List keys and reconciliation** — Test stable keys, component state preservation and remount behavior under sorting, filtering and live updates.

6. **Effects and hidden repeated work** — Inspect Effect cleanup, development Strict Mode, subscriptions and accidental fetch/recompute loops under profiler.

7. **Suspense and transition boundaries** — Evaluate transitions, deferred values or Suspense for responsiveness while retaining accessible loading/error and unsupported behavior caveats.

8. **Route and asynchronous data architecture** — Avoid redundant refetch, race, cascading loading boundary and inaccurate optimistic state during route changes.

*Optional practice — React optimization audit:* Reject global memoization where profiling shows network image decode or unrelated layout is the actual bottleneck.

### Module 9 — Large Data Interfaces, Virtualization and Accessibility

#### Outcomes

- APP10-O7
- APP10-O8
- APP10-O9
- APP10-O10
- APP10-O14

#### Lessons

1. **Large datasets and bottleneck taxonomy** — Measure DOM depth, reconciliation, sorting, filtering, painting and network/data effects separately.

2. **Virtualization or progressive rendering** — Choose a bounded visible-window or incremental rendering strategy only where measurements show benefit.

3. **Stable item identity and scroll anchoring** — Preserve selection, focus, logical order and scroll position through data changes and pagination.

4. **Keyboard access across virtual boundaries** — Design focus restoration and arrow/tab navigation when elements mount/unmount, including screen reader expectations.

5. **Find-in-page, links and content access** — Describe virtualization's native find/search, print and accessible content limitations and provide equivalent search/navigation when necessary.

6. **Long list updates under CPU constraint** — Measure filtering and input latency with controlled data profiles and optional worker/transition techniques.

7. **Data caches and privacy boundary** — Ensure hidden rows or stale user data are not exposed across tenant changes or inferred through cached list variants.

8. **Responsive, zoom and reduced-motion states** — Verify constrained viewport, zoom/reflow, keyboard and accessible feedback after virtualization.

*Optional practice — virtualization failure:* Repair a fast list that traps focus or loses screen-reader context and show the corrected task despite DOM limits.

### Module 10 — Visual Stability, Animations and User Preferences

#### Outcomes

- APP10-O3
- APP10-O4
- APP10-O9
- APP10-O10
- APP10-O14

#### Lessons

1. **CLS event sources and session windows** — Explain unexpected layout-shift metrics and session-window aggregation without labeling every visible movement a CLS defect.

2. **Reserved dimensions and responsive media** — Prevent load-induced jumps through dimensions, aspect-ratio and appropriate placeholders across device widths.

3. **Font swaps and fallback metrics** — Measure text reflow after font load and balance display strategy, access, readability and render speed.

4. **Dynamic content insertion** — Avoid late banners, notifications and async data shifting active content or stealing keyboard focus.

5. **Animation and compositing cost** — Compare transform/opacity and layout-triggering animation while measuring paint, layer memory and accessibility.

6. **Reduced motion and user preference** — Honor prefers-reduced-motion and ensure interactions remain understandable when animations are disabled.

7. **Visual regressions and responsive layout** — Measure layout stability and correct status changes under varying viewport and content growth.

8. **Non-visual user performance** — Consider keyboard, assistive technology, speech output and perceived wait feedback beyond screenshots or visual speed.

*Optional practice — fast-but-unstable design:* Reject a slight transfer-size gain if font/image shifts disrupt form completion or focus context.

### Module 11 — Memory Retention, Long Sessions and Navigation Lifecycle

#### Outcomes

- APP10-O3
- APP10-O6
- APP10-O8
- APP10-O11

#### Lessons

1. **Memory measurement and GC caveats** — Distinguish allocated heap, retained size, GC pauses, browser-process memory and why one sample proves little.

2. **Heap snapshots and retainer trees** — Find listeners, detached DOM nodes, closures, timers and cached data retaining otherwise disposable objects.

3. **Leak reproduction protocol** — Use repeated mount/unmount/navigation and steady baseline; record snapshots after stable interactions and GC caveats.

4. **React Effect and subscription cleanup** — Correct stale sockets, event listeners, observers and timers on route change, component removal or session end.

5. **Object URLs, workers and media lifecycle** — Manage blob URLs, workers, graphics contexts and large decoded media when no longer needed.

6. **Unbounded caches and state growth** — Bound query caches, per-tenant collections and history buffers without losing protected user records.

7. **Back/forward restored context and identity** — Prevent private session content or stale polling from persisting inappropriately across bfcache/navigation.

8. **Long-running interaction and memory test** — Measure repeated browsing task, heap trend, responsiveness and source of retained data after a justified repair.

*Optional practice — non-leak distinction:* Separate legitimate warm cache or GC variability from a demonstrably retained detached component.

### Module 12 — Field Telemetry, Performance Budgets and CI Governance

#### Outcomes

- APP10-O1
- APP10-O2
- APP10-O12
- APP10-O13
- APP10-O14

#### Lessons

1. **Which events to observe in field** — Define load and interaction eligibility, page/route grouping, sampling and user-task completion.

2. **Web Vitals APIs and support variability** — Collect available LCP/CLS/INP signals with a maintained helper or supported browser PerformanceObserver, labeling missing browsers or navigation phases.

3. **Privacy and consent-by-design** — Avoid PII, form contents, raw full URLs or high-cardinality identities in telemetry; document consent/retention and access.

4. **Mobile/desktop and route cohort analysis** — Interpret population and 75th-percentile segment differences without claiming laboratory runs measure field distributions.

5. **Set a risk-based performance budget** — Define concrete cold/warm LCP/CLS and tested interactions, JS/image sizes, long task/LoAF or memory constraints appropriate to the product.

6. **Design a reproducible local performance gate** — Use pinned browser/toolchain/data/network/CPU settings and repeated measurements for a regression criterion that tolerates expected variance.

7. **Seed a material slowdown** — Inject an expensive render, large bundle, LCP late discovery or cache bug, demonstrate actual gate failure and correction.

8. **Flaky performance checks and human judgment** — Distinguish meaningful regression from noisy machines, small samples and threshold chasing; document override/escalation.

*Optional practice — field-to-lab confusion:* Correct a dashboard that reports synthetic TBT as production INP or leaks raw user search terms.

### Module 13 — Integrated Measured Frontend Upgrade and Defense

#### Outcomes

- APP10-O1
- APP10-O2
- APP10-O3
- APP10-O4
- APP10-O5
- APP10-O6
- APP10-O7
- APP10-O8
- APP10-O9
- APP10-O10
- APP10-O11
- APP10-O12
- APP10-O13
- APP10-O14
- APP10-O15

#### Lessons

1. **Choose a maintained React user workflow** — Start from APP20 accessible browser app with APP6 reproducible quality checks, not a screenshot-only performance toy.

2. **State public performance and integrity criteria** — Specify user task, cold/warm environment, CPU/network/viewport profiles, errors, keyboard/security/data outcomes and measurement uncertainty.

3. **Collect lab and optional field baseline** — Capture real browser navigation, interaction and memory traces, LCP/CLS and interaction measures with TBT limitations recorded.

4. **Diagnose critical delivery or React/render bottleneck** — Use waterfall, trace or profiler evidence to isolate primary problem and compare an alternate hypothesis.

5. **Apply a justified loading and caching change** — Improve asset discoverability, bundle or safe cache/version strategy without stale/identity-scoped data or broken entry HTML.

6. **Apply a justified interaction or state change** — Reduce expensive React/DOM work, schedule heavy operations or use appropriate virtualization/worker boundary while preserving accessible feedback.

7. **Inspect long-session memory and visual stability** — Check retention, repeated navigation, layout shifts, reduced-motion behavior and focus/keyboard handling.

8. **Run matched before/after and negative tests** — Repeat with same data, browser/hardware profiles and count failures and confidence; demonstrate actual preserved protected user task.

9. **Integrate privacy-aware telemetry and regression gate** — Define suitable signals, bounded labels and a local policy gate that detects a deliberately seeded performance regression.

10. **Record rejected alternatives and operational cost** — Explain transfer/CPU/energy proxy, accessibility/privacy, implementation, cache rollout and maintenance consequences.

11. **Unfamiliar bounded slowdown and technical defense** — Investigate an assessor-provided new rendering, delivery, cache, input, memory or user-preference regression and defend causal evidence.

## Completion requirements

Every **APP10-O1–APP10-O15** outcome must be assessed through the **six required summative assessments**. Qualifying results can come from one maintained and independently reproducible React application rather than six unrelated products. Lesson experiments, practice traces and optional field monitoring are formative and do not add hidden graduation gates.

| Required assessment | Required outcome coverage | Principal evidence |
| --- | --- | --- |
| `APP10-AS1` — User-Centered Baseline, Browser Trace and Metric Validity | APP10-O1, APP10-O2, APP10-O3, APP10-O7, APP10-O12 | Versioned app and workload, browser/toolchain config, repeated trace/waterfall records, annotated rendering/LoAF and interaction phases, LCP/CLS/TBT-versus-INP explanation, environment/sampling/bias table and falsifiable hypothesis |
| `APP10-AS2` — Critical Loading, JavaScript Delivery and Safe Cache Lifecycle | APP10-O3, APP10-O4, APP10-O5, APP10-O6, APP10-O10, APP10-O14 | App/assets/build and HTTP cache headers, before/after repeated navigation and resource/byte/parse traces, LCP decomposition, versioned asset/update and security tests, correct UI/accessibility behavior and trade-off record |
| `APP10-AS3` — INP Interaction and React Rendering Remediation | APP10-O1, APP10-O2, APP10-O3, APP10-O7, APP10-O8, APP10-O9, APP10-O14 | Browser interaction/LoAF traces and React profile, tested before/after code and controlled input timings, rejected alternatives, accessible functional/negative test results, data/identity assurance and profiling interpretation |
| `APP10-AS4` — Long-Session Memory, CLS and Accessibility Regression | APP10-O3, APP10-O8, APP10-O9, APP10-O10, APP10-O11, APP10-O14 | Repeated-session script, profiler/heap/LoAF and CLS trace with relevant snapshots, fixed lifecycle/layout code, long-session and accessibility/identity tests, environment assumptions and bounded residual-risk statement |
| `APP10-AS5` — Privacy-Aware Field Signals and Reproducible Regression Gate | APP10-O1, APP10-O2, APP10-O6, APP10-O12, APP10-O13, APP10-O14 | Instrumentation/data schema, eligibility/consent/retention and sampling notes, field-versus-lab report, versioned browser harness/gate and fixtures, seeded failure/passing logs, thresholds/variance/override rationale and redacted artifacts |
| `APP10-AS6` — Integrated Upgrade, Comparative Judgment and Independent Defense | APP10-O1, APP10-O2, APP10-O3, APP10-O4, APP10-O5, APP10-O6, APP10-O7, APP10-O8, APP10-O9, APP10-O10, APP10-O11, APP10-O12, APP10-O13, APP10-O14, APP10-O15 | Versioned React code and local fixtures, baseline/post-change waterfall/browser/react/memory traces, functional/security/accessibility tests, correctly scoped vitals and cache validation, regression-gate seeded test, engineering trade-off record and clean-state accessible written/recorded/live defense |

### Shared evidence, fairness and safety boundaries

- Work from a pinned, maintained React/TypeScript/browser and local server baseline with versioned synthetic data, reproducible routes/interactions, browser/toolchain versions and measured CPU/network/viewport settings. Initial free downloads are acceptable; assessable experiments should then run from disclosed local artifacts without paid services.
- Measure actual **user-completing behavior**. Report task success/error, accessible controls, late results and unobserved interactions rather than citing one favorable trace. A speedup on a nonfunctional or forbidden view is not a passing optimization.
- Separate **lab, synthetic replay and actual field observations**. Report LCP/CLS and any user-input timing supported by the browser, plus sample counts, cold/warm cache, CPU/network and missing SPA navigation measurement. Page-load-only Lighthouse TBT must never be reported as a measured INP; one local trace is not a real user population's p75.
- Distinguish task/input delay, event processing, style/layout, paint and React render/commit; use browser trace and React profiler appropriately. Long tasks and Long Animation Frame observations are not universally interchangeable and may be missing on some browsers. State unsupported APIs and instrumentation overhead.
- Protect meaningful semantic/keyboard/focus, screen reader/large text/reflow and reduced-motion behavior. Virtualization requires an accessible means to find/navigate content, correct mounted/unmounted focus and reasonable task completion; never hide inaccessible results to improve a frame budget.
- Prioritize LCP resources based on measured discovery and viewport needs: do not deliberately lazy-load a critical visible LCP image or preload all resources indiscriminately. Account for responsive media sizes, image decode, font metrics, critical CSS, render-blocking JavaScript and appropriate early discovery.
- Keep private data out of shared HTTP/CDN/service-worker caches and telemetry. Verify asset version update, repeat/back navigation, logout and identity change as applicable; never treat CORS, obscured UI or a cache hit as a substitute for server authorization.
- Use bounded synthetic CPU, memory and navigation exercises on learner-owned localhost pages only. Do not run high concurrency, intrusive profiling or security tests on unrelated production sites or collect sensitive real-user traces without consent.
- Prefer repeated controlled comparisons and documented uncertainty, including confidence where warranted. A seedable local performance gate must fail on a material injected regression and acknowledge natural variance and false positives/negatives, not rely on arbitrary universally fixed thresholds.
- Report full trade-offs: bytes versus parse/evaluate/paint, memory versus CPU, accessibility versus virtualization, caching versus correctness/update safety, scheduling versus interaction truth and code complexity versus user benefit. A rigorously justified *no-change decision* may satisfy a proposed optimization where evidence disproves its value.
- An evaluator may introduce an unfamiliar but bounded interaction, layout, cache, rendering, load, memory or navigation failure aligned with published outcomes. An equivalent accessible written, recorded, live or inspectable defense must be accepted; no hidden paid RUM, cloud service, special hardware, private trace source or elective becomes compulsory.

### Required summative assessments

- **APP10-AS1** (required user-centered baseline, browser trace and metric validity)
  - Outcomes: APP10-O1, APP10-O2, APP10-O3, APP10-O7, APP10-O12
  - Work: Select a meaningful accessible task in an APP20 React product and create reproducible low/typical CPU/network/viewport and cold/warm test conditions with a known fixture. Capture and interpret real browser navigation/network/main-thread traces, identify LCP/CLS and one actual observed interaction latency/phase where the browser supports it. Compare available field evidence or clearly disclosed synthetic observations, state sample counts and variability, and explain why TBT or a page-load-only Lighthouse score is not measured INP.
  - Criteria: The workflow and device profiles are relevant; actual failed requests, missing interactions, browser support and cache conditions are documented. An observed slow task is connected to a traceable resource/render/input phase rather than an unsupported score claim. Recorded lab/field distinctions, variance and source/tool versions allow another reviewer to repeat or bound the experiment. Security, keyboard and accurate task outcomes are named as protected non-performance invariants.
  - Evidence: Versioned app and workload, browser/toolchain config, repeated trace/waterfall records, annotated rendering/LoAF and interaction phases, LCP/CLS/TBT-versus-INP explanation, environment/sampling/bias table and falsifiable hypothesis.

- **APP10-AS2** (required critical loading, javascript delivery and safe cache lifecycle)
  - Outcomes: APP10-O3, APP10-O4, APP10-O5, APP10-O6, APP10-O10, APP10-O14
  - Work: Improve a genuinely slow content-loading or route-delivery path, using measured resource discoverability and LCP subparts, image/font/CSS and JS chunk/dependency costs. Compare cold/warm page and route transitions after a justified change (for example correctly prioritized LCP media, responsive image, safer async chunk split or immutable asset caching). Test a versioned release, repeat navigation and logout/account switch using an appropriately isolated local HTTP server/cache or service-worker environment.
  - Criteria: Before/after network waterfalls and browser visual content metrics establish a meaningful benefit (or justified no-change conclusion) under matched conditions, and no lazy LCP, preload overuse, unreviewed third-party script or stale cache illusion is counted as optimization. Deep-link/error/loading paths work with slow network and previous/new asset revisions, and personalized data are not served across identity/tenant boundaries. Any service worker/bfcache claim is limited to observed support and scope. Accessibility/CLS and safe failures are preserved.
  - Evidence: App/assets/build and HTTP cache headers, before/after repeated navigation and resource/byte/parse traces, LCP decomposition, versioned asset/update and security tests, correct UI/accessibility behavior and trade-off record.

- **APP10-AS3** (required inp interaction and react rendering remediation)
  - Outcomes: APP10-O1, APP10-O2, APP10-O3, APP10-O7, APP10-O8, APP10-O9, APP10-O14
  - Work: Instrument and reproduce a visibly slow real click/input/navigation/large-list action. Attribute input delay, handler processing and presentation delay with browser traces and React profiler where available. Experiment with state locality, render causes, stable component identity, schedule/yield, expensive computation or worker migration; select the smallest measured fix, including rejecting unnecessary memoization. Exercise keyboard, screen-reader/focus, accessible pending/errors, async cancellation and a plausible list virtualization alternative when justified by the task.
  - Criteria: An actual interaction and its rendering path improve according to comparable observations (or a defensible non-performance trade-off is documented), not solely a Lighthouse TBT change or an unverified React render count. The fix preserves authenticated data/state correctness, user comprehension, keyboard/focus and responsive layouts; no stale closures, dropped inputs or virtualization focus traps. Browser/React measurements are distinguished and limitations of unobserved field INP are stated.
  - Evidence: Browser interaction/LoAF traces and React profile, tested before/after code and controlled input timings, rejected alternatives, accessible functional/negative test results, data/identity assurance and profiling interpretation.

- **APP10-AS4** (required long-session memory, cls and accessibility regression)
  - Outcomes: APP10-O3, APP10-O8, APP10-O9, APP10-O10, APP10-O11, APP10-O14
  - Work: In the same frontend, reproduce a measurable repeated navigation/component/large-list session with suspected retained listeners, detached nodes, timers, workers or cache objects and one visual shift or animation issue. Record repeated heap/resource/interaction traces, identify a concrete lifecycle cause, correct cleanup or bounded data ownership, and investigate layout/paint shift or font/image/reserved-space behavior under at least two viewport/user motion settings. Verify keyboard/focus and accessible content before and after.
  - Criteria: A reproducible retainer chain or equivalent credible lifecycle evidence backs the repair; single noisy heap samples are not described as proof of memory freedom. Layout movement and CLS aggregation are interpreted correctly and changes do not trap focus or remove screen-reader/find/navigation access. The improvement retains functional correctness, protected data isolation and accurate async teardown after route/logout or browser restore. Residual legitimate caches and browser variability are disclosed.
  - Evidence: Repeated-session script, profiler/heap/LoAF and CLS trace with relevant snapshots, fixed lifecycle/layout code, long-session and accessibility/identity tests, environment assumptions and bounded residual-risk statement.

- **APP10-AS5** (required privacy-aware field signals and reproducible regression gate)
  - Outcomes: APP10-O1, APP10-O2, APP10-O6, APP10-O12, APP10-O13, APP10-O14
  - Work: Define page/route and task-relevant web-vitals and interaction telemetry eligibility, segmenting where appropriate without collecting identifiable form/URL/tenant data. Implement locally reviewable collection or a faithful synthetic dataset/replay with explicit consent, browser support and field limitations. Set defensible cold/warm loading and interaction/perceived-task budgets; implement a versioned locally runnable CI-compatible performance gate with repeated runs, pinned profiles, justified noise tolerance and diagnostic artifacts. Inject a deliberate slowness or cache/layout issue to prove a meaningful gate fails and passes after correction.
  - Criteria: Instrumentation and data retention/attribution are privacy-safe; real field performance is not inferred from a synthetic sample, and unsupported browsers/SPA routes are not silently reported as good results. The locally repeatable gate detects the seeded material regression while documenting flake/noise and override criteria, not inventing universal p75 field guarantees. The budget protects an actual user workflow, layout/accessibility and identity-aware cache behavior rather than blindly optimizing one metric.
  - Evidence: Instrumentation/data schema, eligibility/consent/retention and sampling notes, field-versus-lab report, versioned browser harness/gate and fixtures, seeded failure/passing logs, thresholds/variance/override rationale and redacted artifacts.

- **APP10-AS6** (required integrated upgrade, comparative judgment and independent defense)
  - Outcomes: APP10-O1, APP10-O2, APP10-O3, APP10-O4, APP10-O5, APP10-O6, APP10-O7, APP10-O8, APP10-O9, APP10-O10, APP10-O11, APP10-O12, APP10-O13, APP10-O14, APP10-O15
  - Work: Deliver one cohesive advanced frontend performance upgrade to an existing accessible APP20 React product, reusing qualifying AS1–AS5 evidence rather than five separate apps. Demonstrate a user-centered baseline and causal browser/React investigation, a justified loading/caching and interaction change, preserved privacy/security/accessibility and long-session memory/CLS behavior, explicit lab/field limitations, performance regression detection, before/after comparison and documented deployment/cost/maintainability trade-offs. An assessor then introduces an unfamiliar bounded interaction, delivery, cache, React render, memory, layout or navigation regression; reproduce or diagnose it independently and defend measured outcome and preserved behavior.
  - Criteria: A reviewer can reproduce the submitted behavior and performance work with a free documented local browser/toolchain and synthetic data, inspect normal/denied/cold/warm/keyboard/identity behavior and confirm at least one real attributable optimization or a clearly evidenced no-change decision. Source and traces are coherent, measurements have controlled profiles and uncertainty, the unfamiliar change is addressed with a tested fault/repair, and unsupported field/global Core Web Vitals certifications are refused. No paid RUM, external CDN, cloud hosting, mandatory browser extension or public service load is required.
  - Evidence: Versioned React code and local fixtures, baseline/post-change waterfall/browser/react/memory traces, functional/security/accessibility tests, correctly scoped vitals and cache validation, regression-gate seeded test, engineering trade-off record and clean-state accessible written/recorded/live defense.

### Completion decision and revision safety

A learner completes APP10 only when an evaluator accepts `APP10-AS1` through `APP10-AS6` with independently inspectable evidence jointly demonstrating `APP10-O1` through `APP10-O15`. Source, user tasks, failures, measurements and preserved semantic/privacy behavior must be reproduced as claimed. A green Lighthouse report, high React memoization count, single heap snapshot or unsupported p75 field statement is **not** sufficient on its own. Material failures in accessibility, security, resource isolation, correctness of input, data freshness or measurement integrity must be corrected.

Store course/OEE revision, assessment/outcome IDs, maintained source/lockfile and environment, browser/CPU/network/viewport and cached data profile, actual traces/sample summaries, security and accessibility negatives, before/after hypotheses and evidence, release/cache effects, privacy constraints, independent defense and review decision under [OEE Evidence Rules](../../spec/evidence-rules.md).

APP10 keeps its code, title, `course` type and **optional `elective`** classification but migrates from the legacy seven-week checkpoint/final-lab design and direct APP2 + APP6 prerequisites to a new OEE `v0.2.0` **draft** requiring APP20 + APP6. Earlier APP10 evidence stays attached to its historical source revision rather than silently passing or failing revised outcome IDs. APP9 graduation and all 14 core courses are unchanged; APP11–APP16 remain legacy elective drafts requiring distinct migration. No content/book mapping, OEE Workspace pin or 0xNAND learner record is automatically rewritten.

### Public optional technical references

These version-specific open references inform review; they do not introduce additional hidden assessments.

- [Core Web Vitals](https://web.dev/articles/vitals) explains LCP, INP, CLS, field data and lab/TBT limitations.
- [Optimize INP](https://web.dev/articles/optimize-inp) and [Long Animation Frame timing](https://developer.mozilla.org/en-US/docs/Web/API/Performance_API/Long_animation_frame_timing) describe input delay, rendering work and available trace evidence.
- [Optimize LCP](https://web.dev/articles/optimize-lcp) covers resource discovery, priority and four subparts of visible-content loading.
- [Cumulative Layout Shift](https://web.dev/articles/cls) and [Optimize CLS](https://web.dev/articles/optimize-cls) describe session-window aggregation and stability decisions.
- [React Profiler](https://react.dev/reference/react/Profiler) and [React memo](https://react.dev/reference/react/memo) explain measured rendering and memoization trade-offs.
- [MDN HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching), [Service Worker API](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) and [Back/forward cache](https://web.dev/articles/bfcache) describe browser/asset version and navigation lifecycle behavior.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) provides accessibility review criteria; compliance must not be falsely inferred from performance traces.
