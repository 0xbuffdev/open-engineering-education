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

**Six publicly required assessments** develop one evolving accessible React product: validated browser baseline/causal trace, critical delivery and private-cache correctness, real input/React improvement, long-session memory/CLS/accessibility, field-aware local budgets and independent unfamiliar-change defense. **Instructional sufficiency is mandatory in this outline:** each distinct measurement or browser mechanism must receive a comprehensible model, an observed example or worked trace, application, a negative/counterexample and useful feedback *before* summative evaluation. Earlier APP20/APP6 mechanisms are applied rather than re-taught, but a new browser-performance concept is never hidden in a compressed checklist. Formative lessons add no secret gates. Local workload/duration remain provisional until genuine learner evidence exists.

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

1. **Frontend performance specialization and historical shift** — Trace why browser engineering evolved from transfer-size and page-load benchmarks toward user-completed tasks, interaction latency and real-user signals. Identify which mechanics APP20 and APP6 already assess and what APP10 newly requires: browser causal diagnosis and safe optimization.

2. **Choose a protected and consequential user task** — Select a meaningful cold-to-interactive or long-session React workflow with a real loading, input or navigation symptom, including actual server-backed data, authorized/denied state and accessible completion.

3. **Nonnegotiable correctness and accessibility guardrails** — Define what remains true after optimization: semantic control names, keyboard/focus and screen-reader access, no old-user/tenant content, accurate pending/error states and preserved domain facts.

4. **Falsifiable bottleneck, competing cause and rejected fix** — Predict a measurable bottleneck, a simple alternative and a plausible counterexample; state what task, source trace and negative control would distinguish a real improvement from an attractive score.

5. **Matched baseline, profiles and measurement provenance** — Pin free local app/fixture, browser and React build, hardware, viewport, input mix, CPU/network, cold/warm state, tool versions and enough repeats for meaningful uncertainty; separate production-style run from instrumented diagnostic overhead.

6. **Reject metric-first performance theater** — Analyze why a faster empty route, smaller asset or fewer React renders can coexist with a slower/inaccessible protected task; choose evidence that would reject the inappropriate optimization.

*Optional practice — experiment review:* Reject an optimization proposal lacking a controlled baseline, meaningful interaction and trustworthy result threshold.

### Module 2 — Laboratory, Field, Core Web Vitals and Bias

#### Outcomes

- APP10-O1
- APP10-O2
- APP10-O12
- APP10-O13

#### Lessons

1. **Lab scenarios, real field visits and different inferences** — Contrast repeatable browser traces with real-device population measurements and a fabricated illustrative dataset, explicitly marking actual, synthetic and unobserved sessions before using any percentile.

2. **LCP, INP, CLS and their observation boundaries** — Explain current Core Web Vitals loading, interaction and layout semantics with a worked timeline, browser support and relevant user-journey conditions rather than memorized threshold colors.

3. **An interacted lab trace is not page-load-only TBT** — Use a genuine tested click/input for event timing where supported, show what Lighthouse page-load-only Total Blocking Time measures and why a TBT improvement cannot be reported as observed field INP.

4. **Navigation scope, SPA transitions and bfcache** — Compare initial document navigation, same-document routes and restored history state; specify supported soft-navigation/SPA instrumentation and what the chosen browser never observed.

5. **Population quantiles and small-sample counterexample** — Compute a sample 75th percentile over the correct metric population/aggregation unit, contrast mobile and desktop cohorts and explain why one local measurement or missing interaction cannot be represented as a field p75.

6. **Warmup, cache and device throttling confounders** — Demonstrate how JIT, cold/warm media, memory/GC, CPU throttling and thermal/tool overhead can reverse apparent winners; reset or record these variables instead of averaging incompatible runs.

7. **Repeated trials, failure denominators and confidence** — Report actual supported browser APIs, sample counts, spread, missing iframe/interaction/SPA cases, and rejected/time-out user tasks alongside measured successes; show when a proposed improvement is indistinguishable from noise.

*Optional practice — bad-vitals audit:* Correct a report that advertises a TBT-only synthetic audit as 'INP passed' and conflates field with lab results.

### Module 3 — Browser Main Thread, Frames and Rendering Traces

#### Outcomes

- APP10-O2
- APP10-O3
- APP10-O7
- APP10-O10

#### Lessons

1. **Browser parse-to-paint with observable phases** — Map markup parsing and CSSOM through style, layout, paint and compositing on a real trace, noting that modern browser pipelines/parallel work are not a single universal serial diagram.

2. **Event loop, microtasks and rendering opportunity** — Trace a queued input, event task, microtask checkpoint and rendering opportunity, then construct a case where an unbounded microtask chain postpones visible feedback.

3. **Long tasks versus LoAF evidence and feature detection** — Distinguish long task blocking from Long Animation Frame observations, check support and script attribution limitations, and reproduce a long JS phase without assuming every frame is reportable.

4. **Style recalculation and selector/layout work** — Profile large DOM changes and costly style invalidation before selecting containment or DOM restructuring.

5. **Forced layout read–write loop and causal correction** — Trigger a measurable DOM measure/mutate feedback loop, use browser trace forced-layout evidence and verify a batching or ordering repair does not change scroll, focus or calculated geometry.

6. **Painting, layering and compositing** — Analyze paint regions, layer proliferation, GPU memory and the risk that transforms create performance regressions.

7. **Actual interaction input/processing/presentation timeline** — Correlate user input delay, handler execution and paint/presentation delay with browser and React traces where available, using a real controlled interaction and noting unsupported timing details.

8. **Source attribution, instrument overhead and alternate cause** — Connect source-mapped chunks and DOM/React frame phases to a task-level symptom, run one targeted controlled change, and reject a competing explanation only to the extent the trace supports.

*Optional practice — render trace repair:* Explain a jank sequence that persists despite reducing JS handler time because layout and paint still dominate.

### Module 4 — Largest Contentful Paint and Critical Content Delivery

#### Outcomes

- APP10-O2
- APP10-O3
- APP10-O4
- APP10-O10

#### Lessons

1. **Four LCP subparts and a measured critical candidate** — Break actual LCP into server response/TTFB, discovery delay, resource load duration and element render delay; identify what intervention can move time between subparts without changing total LCP.

2. **Discoverable LCP media, request priority and no lazy hero** — Compare an initially visible image discoverable in HTML with CSS/JS-late or lazily loaded variants; try bounded fetchpriority/preload, showing an early request can still await render blocking, and avoid prioritizing every resource.

3. **Responsive media width, formats and decode cost** — Compare srcset/sizes and supported image encoding at real viewport/quality, actual bytes and decode/render cost, including a counterexample where compression improves transfer but not observed LCP.

4. **Render-blocking styles, font display and layout shifts** — Control critical CSS and font fallback/subset/metrics, inspect text LCP and CLS/focus impact, and state accessibility/legibility costs rather than universally recommending display-swap.

5. **Server time versus client discovery/hydration** — Measure response timing, HTML availability, React client-only rendering and fallback states, and test whether earlier visible content is genuinely usable without requiring new server rendering infrastructure.

6. **Preload, modulepreload, preconnect and counterproductive hints** — Inspect actual waterfall for resource-hint benefits and saturation/duplicate download, including which browser support and cache conditions were assumed.

7. **Verify actual content and protected task completion** — Check that improved LCP candidate remained semantically usable, authorized and responsive with keyboard/focus and delayed network; reject a fast decorative hero masking a stalled application.

*Optional practice — slow-hero experiment:* Repair a late discovered or overcompressed image and show the relevant waterfall plus rendering consequences.

### Module 5 — JavaScript Supply, Bundles and Startup Work

#### Outcomes

- APP10-O3
- APP10-O4
- APP10-O5
- APP10-O8

#### Lessons

1. **Transfer bytes, execution time and third-party ownership** — Use a real build graph/waterfall to distinguish compressed transfer, parsed/evaluated JS, module execution, external scripts and high-cost CPU work, preserving dependency/provenance context.

2. **Dynamic route and component boundaries with fallback** — Introduce a measured code-split that improves one cold task without causing a slow second-navigation request chain, and test deep links, errors, Suspense and keyboard/focus behavior.

3. **Lazy-import graph and sequential waterfall** — Use devtools to identify dependent chunk and style requests created by a split, test one preload/preinit alternative and compare both cold and warm navigation.

4. **Side effects, tree shaking and runtime correctness** — Inspect whether bundled modules can be eliminated under actual package sideEffects/export settings and verify a library's required initialization still occurs.

5. **Third-party execution cost and protected information** — Run one locally controlled optional script/embedded fixture with blocked/delayed execution and compare main-thread time, privacy exposure, permission policy and safe fallback.

6. **Transfer vs compile/parse/evaluate vs React startup** — Compare bundles with similar transfer but different evaluated work and measure source/runtime execution including controlled profiling overhead. Refer CPU-worker placement and cancellation to M7 rather than teach that mechanism twice.

7. **Hashed asset update and actual old/new client behavior** — Serve versioned JS/CSS/HTML under local HTTP, reproduce one deep-link/mixed-version failure and verify cache headers and supported previous/new sessions survive deployment.

*Optional practice — startup regression:* Catch a route split that reduces entry bytes but breaks deep-link/slow-network navigation and restore accessible fallback.

### Module 6 — HTTP, Browser Cache, Service Workers and Return Visits

#### Outcomes

- APP10-O4
- APP10-O5
- APP10-O6
- APP10-O9
- APP10-O12

#### Lessons

1. **Actual HTTP freshness, validators and user authority** — Compare public immutable assets, index HTML and authenticated API caching using Cache-Control/ETag/Vary under observed headers; show why a shared cache without private scope can leak personalized data.

2. **Versioned assets, mutable HTML and release rollback** — Trace hashed JS/CSS URLs, short-lived HTML, retained previous assets and one rollback when an old open tab requests a lazy chunk after deployment.

3. **Cross-identity caching denial and real response traces** — Switch synthetic users/tenants, inspect browser/service-worker/proxy and app caches, and show no previously authenticated record can be served because of an unsafe key or shared response policy.

4. **Cold/revisit/back-forward experiment on controlled state** — Record cold/warm and history-navigation resource requests, old page heap and service worker state; distinguish a memory-resident bfcache page from ordinary HTTP revalidation.

5. **Service worker registration, lifecycle and justified use** — Demonstrate install/activate/fetch/update when optional offline support solves a real user task; if not, use a bounded local thought/fixture probe and do not require a PWA/service worker to pass.

6. **Offline policy for private reads and writes** — Test offline/expired session and slow network cases, choosing which public read-only assets survive and which private task must reverify identity or explicitly fail and reconcile.

7. **Mixed-version service worker update and rollback** — Reproduce an older controlling worker or changed cached HTML/asset combination; verify a safe update path, uncontrolled-client handling and explicit state clearing without deleting genuine user-owned data.

8. **Browser bfcache restoration, no-store exception and privacy** — Verify pageshow persisted and actual browser eligibility on backward navigation, including modern limited Chrome no-store eligibility; check current session/tenant before exposing restored private UI or running stale timers, not a blanket no-store guarantee.

*Optional practice — cache poisoning scenario:* Repair an identity-scoped resource or version mismatch that becomes observable on repeat navigation.

### Module 7 — INP, Input Handling, Scheduling and Worker Offload

#### Outcomes

- APP10-O2
- APP10-O3
- APP10-O7
- APP10-O10
- APP10-O14

#### Lessons

1. **Interacted INP scope and critical-user timing** — Measure a real visible click/input and divide observed latency into input delay, event processing and presentation delay, explaining how a long session's interaction set differs from one synthetic probe.

2. **Unrelated blocking main-thread work before input** — Reproduce a click queued behind a long unrelated task and repair the source or schedule, verifying it did not merely postpone essential operation completion.

3. **Event callback computation with semantic result** — Measure actual input/change handler work, use a worked trace to distinguish algorithmic processing from waiting for server truth, and test correctness of resulting form/state.

4. **Presentation delay after fast handler** — Instrument a handler that completes quickly while layout, paint or React commit blocks the next frame, and fix browser rendering rather than claiming handler timing is sufficient.

5. **Yielding, chunking and scheduling semantics** — Compare bounded chunk boundaries, task yielding and scheduler support with a reproducible input, ensuring queue interleaving, progress and cancellation do not change domain results.

6. **rAF frame opportunity and layout-risk counterexample** — Show when requestAnimationFrame schedules a callback before a render opportunity but cannot guarantee fast paint, and contrast it with a long rAF callback that causes visible jank.

7. **A real CPU-worker boundary, transfer and lifecycle** — Offload a justified computation, independently compare main-thread responsiveness with message clone/transfer cost, cancellation, worker failure and disposal, rejecting worker use when latency gets worse.

8. **Accessible immediate feedback versus authoritative completion** — Give usable pending/progress state while heavy work runs, verify a keyboard user can interrupt/recover, and never announce persisted success before the server commits it.

*Optional practice — INP breakdown repair:* Reduce a slow interaction and demonstrate which phase improved instead of calling TBT directly measured INP.

### Module 8 — React Render/Commit Attribution and State Ownership

#### Outcomes

- APP10-O3
- APP10-O5
- APP10-O7
- APP10-O8
- APP10-O14

#### Lessons

1. **Correlate browser timeline, React profiler and build mode** — Trace render/commit versus DOM paint, input delay and browser layout; control production-like build mode and profiling overhead rather than compare dev Strict Mode counts with production timing.

2. **Profiler-attributed actual update propagation** — Identify a costly subtree through React profiler/performance tracks and distinguish prop, context, external subscription and callback instability, comparing a real user interaction before optimization.

3. **State ownership, derived computation and stable data** — Move frequently changing state to its justified owner and avoid global refetch/recompute without copying stale server data into persistent local state.

4. **React Compiler versus manual memo and correctness** — Inspect whether a pinned React Compiler is actually enabled/eligible, compare generated optimization with selective memo/useMemo/useCallback, and test stale closures, subscription changes and task time rather than count memoized components.

5. **Stable keys, actual identity and invalid remounts** — Reorder/filter an owned list and trace keyed identity and local form/selection state, proving a fast but wrong remount or reused identity is not acceptable.

6. **Strict Mode, Effects and actual external subscriptions** — Find a duplicated fetch/listener or cleanup bug in development rehearsal and verify a supported production-like scenario without treating React Strict Mode replay counts as universal.

7. **Suspense, transitions and delayed server state** — Profile a high-priority input and supported transition/deferred/Suspense boundary, verifying a busy indicator and correct server/error/retry semantics with realistic browser work.

8. **Route/data waterfalls and old-identity response race** — Trace navigation-triggered redundant fetching and delayed responses, remove a measured waterfall and prove an earlier user's protected result cannot overwrite a later identity.

*Optional practice — React optimization audit:* Reject global memoization where profiling shows network image decode or unrelated layout is the actual bottleneck.

### Module 9 — Large Data Interfaces, Virtualization and Accessibility

#### Outcomes

- APP10-O7
- APP10-O8
- APP10-O9
- APP10-O10
- APP10-O14

#### Lessons

1. **What actually limits a large UI** — Measure browser DOM/layout, React reconciliation, CPU filtering and data/network loading on synthetic high-row lists to select the primary bottleneck.

2. **Windowed versus progressive rendering decision** — Compare virtualized, paginated and incremental DOM under an actual user-task trace, including the cost of hidden content and screen-reader semantics.

3. **Item identity, focus and scroll restoration** — Demonstrate sorted/filtered updates with stable keys and a virtualized item unmount; keep selection, logical position and focus restoration consistent.

4. **Keyboard and assistive navigation across unmounted rows** — Specify aria-list/table semantics, focus anchors, item count/position and keyboard operations for a windowed list; reproduce a focus trap and verify an accessible route to omitted items.

5. **Find-in-page, print and full-content alternatives** — Test native browser search/printing and screen reader access over windowed content, adding a search/full-list/export or unvirtualized alternative when necessary.

6. **Filtering input under bounded data/CPU conditions** — Use a controlled large list to compare synchronous sort/filter, deferred rendering, a worker or server query; verify the input results and cancellation/state identity.

7. **Virtualized cache, tenant isolation and row existence** — Switch two synthetic principals across cached lists, ensure hidden or virtualized rows do not reveal forbidden records and preserve current server-authorized selection.

8. **Zoom, reflow, reduced motion and task success** — Repeat actual keyboard/AT-supported user tasks under constrained width, zoom and motion preferences; report usability caveats instead of a blanket accessibility compliance score.

*Optional practice — virtualization failure:* Repair a fast list that traps focus or loses screen-reader context and show the corrected task despite DOM limits.

### Module 10 — Visual Stability, Animations and User Preferences

#### Outcomes

- APP10-O3
- APP10-O4
- APP10-O9
- APP10-O10
- APP10-O14

#### Lessons

1. **Layout shift source and session-window calculation** — Trace a real set of unexpected layout shifts and compute the appropriate CLS session-window aggregation, distinguishing intended user-driven movement and visual instability.

2. **Reserved media geometry across device widths** — Use width/height/aspect-ratio placeholders, then inject late responsive media to verify no disruptive shift during form completion.

3. **Text fallback metrics, readable font and shift trade-off** — Measure font swap text layout and font-display/size-adjust alternatives in a real content task, preserving readability and language coverage rather than optimizing only a transfer score.

4. **Late content insertion, user input and focus** — Inject banner, validation message or async data while a user is editing; compare shifted target, focus and input continuity with a reserved/reflow-safe alternative.

5. **Animations, paint cost and compositing memory** — Profile transform/opacity versus layout-triggered animation and layer proliferation using actual paint/frame traces, not an untested blanket GPU recommendation.

6. **Reduced-motion preference with equivalent feedback** — Test system prefers-reduced-motion and animation-disabled states while preserving navigation, progress and semantic status descriptions.

7. **CLS under long sessions, zoom and delayed widgets** — Measure unexpected layout changes beyond first load, including a small viewport and delayed async content, and reject an improvement that only shifts the problem later.

8. **Nonvisual operation as a performance invariant** — Verify accessible form, keyboard, spoken status and content order remain usable under loading, motion/reflow and cache changes; do not infer accessibility from screenshots.

*Optional practice — fast-but-unstable design:* Reject a slight transfer-size gain if font/image shifts disrupt form completion or focus context.

### Module 11 — Memory Retention, Long Sessions and Navigation Lifecycle

#### Outcomes

- APP10-O3
- APP10-O6
- APP10-O8
- APP10-O11

#### Lessons

1. **Heap allocated, retained, garbage collection and noise** — Compare JS heap, browser process memory and GC/renderer activity over repeated tasks, explain what a single heap screenshot cannot establish and define credible leak oracle.

2. **Retainer tree and detached-resource ownership** — Identify one real retained detached DOM/closure, observer or event handler chain through a suitable heap retaining path and note inspection tool limitations.

3. **Repeatable lifecycle and cross-run baseline** — Control mount/unmount count, navigation, synthetic users, cache size and GC schedule where observable; compare multiple runs rather than call legitimate warm cache a leak.

4. **Effect, timer and subscription cleanup at logout** — Reproduce an actual surviving listener/timer/socket on route or session change, repair cleanup and verify no previous-user event or data persists.

5. **Object URLs, workers, media and decoded memory** — Inspect a concrete blob, worker or resource lifetime and a fail/abort path; implement revocation/termination and compare actual state after navigation.

6. **Finite application caches and working-set policy** — Identify unbounded history/tenant data retention, add bounded eviction by safe ownership rules and verify records remain recoverable from trusted server state.

7. **Back/forward restored heap and stale identity** — Navigate away/back under supported bfcache conditions, detect persisted JS heap, polling/subscriptions and obsolete principal state; reverify before displaying protected information.

8. **Long-session repair and residual-risk statement** — Demonstrate repeated route/task and heap/interaction time before/after one concrete fix, preserving user data/keyboard behavior and disclosing GC/OS/browser variability.

*Optional practice — non-leak distinction:* Separate legitimate warm cache or GC variability from a demonstrably retained detached component.

### Module 12 — Field Telemetry, Performance Budgets and CI Governance

#### Outcomes

- APP10-O1
- APP10-O2
- APP10-O12
- APP10-O13
- APP10-O14

#### Lessons

1. **Define valid field task, event and page cohort** — Choose privacy-safe navigation, route and user-interaction eligibility, business completion and data retention without manufacturing a real population.

2. **Observed Web Vitals API support and missing records** — Use supported performance observers or maintained helper for LCP/CLS/INP where real interactions permit; explicitly log unsupported browser/iframe/soft-route gaps and instrumentation overhead.

3. **Consent, data minimization and high-cardinality risks** — Demonstrate local telemetry output with no form content, full sensitive URL or principal labels and describe who may access or delete collected signals.

4. **Synthetic cohort p75 versus actual field p75** — Work through a disclosed illustrative visit distribution, segment mobile/desktop and incomplete interaction observations, refusing to present synthetic data as real-world p75.

5. **Budget for real task success, not metric quotas** — Choose proportionate cold/warm LCP/CLS, actual exercised interaction and memory/byte budgets with accessible and identity-safe correctness constraints, explaining which thresholds are provisional.

6. **Pinned repeated local gate and false-positive model** — Run a free browser/trace harness with controlled environment, repeat samples and transparent decision tolerance; separate unstable host noise from a meaningful regression.

7. **Seeded actual regression that fails the gate** — Introduce a real late LCP fetch, costly rendering, cross-version cache bug or memory growth, show independent detected failing result, fix and re-run under matching profiles.

8. **Human review, overrides and honest release decision** — Investigate a near-threshold run, missing metric or other flake, document appropriate override/rollback and safeguard user correctness rather than turn budget noise into a mandatory impossible cutoff.

*Optional practice — field-to-lab confusion:* Correct a dashboard that reports synthetic TBT as production INP or leaks raw user search terms.

### Module 13 — One Measured Frontend Upgrade and Independent Defense

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

1. **One maintained React product and prior accepted evidence** — Reuse the same accessible APP20-based product evaluated in AS1–AS5, link genuinely accepted benchmark, cache/security/interaction, memory and telemetry observations without recreating five separate apps.

2. **Independent causal loading/interaction improvement** — Show one coherent user task and the two distinct AS2 loading/cache and AS3 input/React decisions with their actual traces and justified alternatives, not a second capstone implementation checklist.

3. **Preserved accessibility, private state and long sessions** — Reference and selectively recheck AS2–AS5 keyboard/focus, identity/cache, layout, reduced-motion and lifecycle tests, including one real adverse path after the optimization.

4. **Fresh unknown regression and independent failure diagnosis** — Accept a new bounded slow interaction, stale asset, misordered React state, layout shift or retained-resource fault; independently collect failing-before evidence, identify the likely mechanism and repair or reject a mistaken optimization.

5. **Matched remeasurement and reproducible gate regression** — Rerun actual local browser/cold/warm task with appropriate sample/noise controls and privacy-safe CI gate, showing new changes preserve previously accepted evidence and did not merely hide a failing interaction.

6. **Clean local technical defense and honest trade-offs** — Start the free pinned application and explain source/trace provenance, field-versus-lab boundaries, user/energy/resource/maintenance cost, unsupported browser cases and accepted AS1–AS5 evidence through an accessible live/written/recorded equivalent.

## Completion requirements

All **fifteen APP10 outcomes** must be established through **six independently decidable assessments** on one maintained React application: AS1 valid user/task/browser evidence; AS2 critical delivery and correct private caching; AS3 genuine input/React remediation; AS4 long-session memory/visual/accessibility protection; AS5 privacy-aware local performance governance; AS6 an independently reproduced **unfamiliar bounded failure**. Reference already accepted AS1–AS5 results rather than resubmit all measurements as six unrelated projects. Formative investigation and optional real-user monitoring remain optional, and this **elective does not affect APP9 or core graduation**.

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
  - Work: Use one meaningful accessible protected React/TypeScript user task and controlled free browser environment to derive a falsifiable **task-level** performance problem. Record pinned build, browser/tool versions, data, CPU/network/viewport and cold/warm state, actual normal/denied/failed task completion, repeated navigation/waterfall/LoAF or supported trace, and a **real exercised** input where supported. Decompose relevant LCP, CLS and interaction input/processing/presentation paths and distinguish what page-load Lighthouse **TBT** cannot measure about INP; label optional genuine field evidence or illustrative synthetic records honestly. Compare a competing cause and note trace overhead/missing support.
  - Criteria: An independent reviewer reproduces an actual user-task, not just an empty-page score; browser/React metrics and actual requests support a plausible causal hypothesis and a contrary test. Repeated observations state sample counts, error/timeout/missing-interaction denominator, source and environment limits. A page-load-only Lighthouse score is **not** claimed to measure INP or represent real visit-level p75; unsupported soft-navigation/LoAF/iframe data are not called passing. Correct protected data, keyboard/focus, meaningful content and server truth are recorded as optimization invariants.
  - Evidence: Versioned app and workload, browser/toolchain config, repeated trace/waterfall records, annotated rendering/LoAF and interaction phases, LCP/CLS/TBT-versus-INP explanation, environment/sampling/bias table and falsifiable hypothesis.

- **APP10-AS2** (required critical loading, javascript delivery and safe cache lifecycle)
  - Outcomes: APP10-O3, APP10-O4, APP10-O5, APP10-O6, APP10-O10, APP10-O14
  - Work: Starting from the AS1 baseline in the **same** React product, identify a real slow critical-content or route transition and evaluate its LCP subparts, early resource discovery, inline-visible image prioritization versus lazy load, image sizes/font/CSS and JavaScript chunk/dependency waterfalls. Make one justified measurable content/asset delivery improvement, including a no-change outcome if evidence invalidates the proposed fix. Exercise a local old/new asset/HTML build, deep-link/error/slow-network behavior, cold/warm repeat navigation and identity-switched HTTP/worker/private caching. If a service worker is **actually justified and used**, verify its update/offline behavior; otherwise do not require a PWA. Inspect bfcache behavior under the tested browser, including the fact that Cache-Control: no-store does not universally guarantee no bfcache restoration.
  - Criteria: A matched real-browser waterfall and content/usable-task observation establish the claimed LCP/route outcome and explain any delay moved to render/parse/paint; reducing bytes alone is insufficient. Critical visible images are not accidentally late/lazy, and priority/preload hints do not starve necessary content. Hashed chunks, old/new HTML, user-facing fallback, return/back navigation and server-held authorization preserve correct current-identity state. Private data never leak via a shared cache, service worker or restored prior session; security cannot be established solely by a cache header, no-store or client UI hiding. Correct keyboard, CLS and route recovery remain demonstrable.
  - Evidence: App/assets/build and HTTP cache headers, before/after repeated navigation and resource/byte/parse traces, LCP decomposition, versioned asset/update and security tests, correct UI/accessibility behavior and trade-off record.

- **APP10-AS3** (required inp interaction and react rendering remediation)
  - Outcomes: APP10-O1, APP10-O2, APP10-O3, APP10-O7, APP10-O8, APP10-O9, APP10-O14
  - Work: Reproduce a genuine slow click/input/navigation or complex large-list operation with real controlled browser input. Correlate browser main-thread/LoAF and React render/commit/profiler traces to distinguish input delay, handler processing and presentation delay. Test an actual justified cause such as state ownership, scheduling/yielding, React Compiler **when configured and eligible**, selective memoization, worker offload or accessible virtualization, including a deliberately plausible alternative that does **not** improve the user task. Compare production-like performance build and diagnostic profiler overhead where appropriate and test canceled/late old-identity results and keyboard/focus.
  - Criteria: Observed interacted input and actual rendering improve under matched conditions or a sound evidence-based no-change choice is defended—not by inferring real INP from TBT, shrinking component count or counting memo wrappers. Render and DOM paint have correctly distinguished meanings, React Compiler optimization is not presumed without checked configuration, and no stale closure, wrong keyed identity, dropped user input or hidden late privileged data is introduced. Virtualization, when selected, includes find/search and keyboard/screen-reader routes to unmounted content; an untested specialist browser capability is not mandatory.
  - Evidence: Browser interaction/LoAF traces and React profile, tested before/after code and controlled input timings, rejected alternatives, accessible functional/negative test results, data/identity assurance and profiling interpretation.

- **APP10-AS4** (required long-session memory, cls and accessibility regression)
  - Outcomes: APP10-O3, APP10-O8, APP10-O9, APP10-O10, APP10-O11, APP10-O14
  - Work: Using the same application and real repeated navigation/large-list user task, reproduce a **specific** retained listener, detached node, timer, worker, object URL or unbounded principal-scoped cache with actual retainer/heap/lifecycle evidence across multiple runs. Correct its cleanup/ownership under route, logout and relevant supported bfcache restoration. Separately measure a concrete layout shift or undesirable animation/font/media transition over realistic viewport, zoom and reduced-motion preferences, check CLS session-window interpretation, and verify focus/keyboard/assistive access before/after the correction.
  - Criteria: The failure and repair have credible repeated retention/GC/retainer evidence, not a one-off heap screenshot or promise of universal leak absence. Retained legitimate cache memory and browser variability are distinguished from an actual lifetime defect. Visual movement and CLS are reported with correct session/interaction context, and preserved keyboard focus, find-in-page/accessible row access, reduced motion, protected data/session isolation and resource teardown are independently demonstrated. A faster but unusable or stale-private-data interface fails.
  - Evidence: Repeated-session script, profiler/heap/LoAF and CLS trace with relevant snapshots, fixed lifecycle/layout code, long-session and accessibility/identity tests, environment assumptions and bounded residual-risk statement.

- **APP10-AS5** (required privacy-aware field signals and reproducible regression gate)
  - Outcomes: APP10-O1, APP10-O2, APP10-O6, APP10-O12, APP10-O13, APP10-O14
  - Work: Implement an appropriately privacy-minimal local performance-event collector **or** an explicitly labeled illustrative synthetic field dataset for the same app. Define eligible navigation/route and actually observed interaction events, browser support, sample/segmentation windows, missing observations, consent/retention/label limits and field-versus-lab conclusions. Set a **task-centered**, testable cold/warm delivery, input, long-session and correctness budget and one pinned free-browser locally executable repeated CI-style performance gate with variance/false-positive policy. Inject a material asset, React/input, cache or layout regression, observe a meaningful failing result, correct and recheck it, and demonstrate that real user-field p75 is never inferred from fictional records.
  - Criteria: No personal forms, full sensitive URLs, session identifiers or unbounded high-cardinality attributes enter data. Actual field results, synthetic dataset quantiles and local interacted timing have distinct provenance and denominator semantics; unavailable soft navigation/INP/iframe data are disclosed. The local repeated gate detects an **observed seeded regression** under pinned conditions, documents tool/CPU variation, human override and false alarms, and protects real task completion, accessibility, server-held permissions and identity-scoped cache behavior rather than chasing arbitrary universal Web Vitals thresholds.
  - Evidence: Instrumentation/data schema, eligibility/consent/retention and sampling notes, field-versus-lab report, versioned browser harness/gate and fixtures, seeded failure/passing logs, thresholds/variance/override rationale and redacted artifacts.

- **APP10-AS6** (required integrated upgrade, comparative judgment and independent defense)
  - Outcomes: APP10-O1, APP10-O2, APP10-O3, APP10-O4, APP10-O5, APP10-O6, APP10-O7, APP10-O8, APP10-O9, APP10-O10, APP10-O11, APP10-O12, APP10-O13, APP10-O14, APP10-O15
  - Work: Defend **one evolving accessible APP20 React product** and its separately accepted APP10-AS1–AS5 observations **by reference**, not via five newly created applications or repeated full reports. Reproduce the justified critical-content/cache and actual user-interaction/React decisions, long-session layout/memory behavior and privacy-safe local gate from a clean free pre-provisioned checkout. A reviewer introduces a **new, previously unseen bounded** slowdown, stale asset, identity-leaking cache, React update, inaccessible virtual list, layout shift or retained-resource challenge; predict the real symptom, measure an independent before-fix browser/user-state oracle, repair or correctly reject the faulty optimization, and repeat targeted security/accessibility/functional/performance regression.
  - Criteria: A reviewer can reproduce the protected user task, relevant actual browser/React traces, valid lab versus synthetic/field distinction and independent response to the unfamiliar challenge; **AS6 cannot excuse missing or failed AS1–AS5 evidence**. The change improves or legitimately preserves user-completed work under stated sample/noise limits and does not leak identity, erase content/focus or misreport pending/failed server results. Browser-specific features, proprietary field analytics, paid services and invented p75 populations are not required. Trade-offs in bytes, CPU/memory, energy proxies, maintainability and release compatibility remain explicit.
  - Evidence: One versioned existing React product with pinned local browser/profile/data fixtures, a **references-first outcome-to-accepted-AS1–AS5 evidence index**, selected matched waterfall/interaction/heap/CLS observations and real denied/keyboard tests, locally seeded regression gate, new assessor fault and independent before/after traces, honest field/virtualization/support limits and accessible written, recorded or synchronous technical defense.

### Completion decision and revision safety

A learner completes APP10 only when an evaluator accepts `APP10-AS1` through `APP10-AS6` with independently inspectable evidence jointly demonstrating `APP10-O1` through `APP10-O15`. Source, user tasks, failures, measurements and preserved semantic/privacy behavior must be reproduced as claimed. A green Lighthouse report, high React memoization count, single heap snapshot or unsupported p75 field statement is **not** sufficient on its own. Material failures in accessibility, security, resource isolation, correctness of input, data freshness or measurement integrity must be corrected.

Store course/OEE revision, assessment/outcome IDs, maintained source/lockfile and environment, browser/CPU/network/viewport and cached data profile, actual traces/sample summaries, security and accessibility negatives, before/after hypotheses and evidence, release/cache effects, privacy constraints, independent defense and review decision under [OEE Evidence Rules](../../spec/evidence-rules.md).

APP10 remains the existing **optional `elective`** OEE `v0.2.0` **draft** with direct APP20 + APP6 prerequisites, fifteen published outcomes and six required assessments. The previous APP2 + APP6 and seven-week checkpoint design is an already completed historical migration, not a pending change in this PR. APP9 graduation, all other core/elective courses and historical assessed revisions remain unchanged. A structurally passing PR cannot establish learner `tested` or `verified` readiness or silently update content/book mappings, OEE Workspace/0xNAND source pins or prior learner records.

### Public optional technical references

These version-specific open references inform review; they do not introduce additional hidden assessments.

- [Core Web Vitals](https://web.dev/articles/vitals) explains LCP, INP, CLS, field data and lab/TBT limitations.
- [Optimize INP](https://web.dev/articles/optimize-inp) and [Long Animation Frame timing](https://developer.mozilla.org/en-US/docs/Web/API/Performance_API/Long_animation_frame_timing) describe input delay, rendering work and available trace evidence.
- [Optimize LCP](https://web.dev/articles/optimize-lcp) covers resource discovery, priority and four subparts of visible-content loading.
- [Cumulative Layout Shift](https://web.dev/articles/cls) and [Optimize CLS](https://web.dev/articles/optimize-cls) describe session-window aggregation and stability decisions.
- [React Profiler](https://react.dev/reference/react/Profiler) and [React memo](https://react.dev/reference/react/memo) explain measured rendering and memoization trade-offs.
- [MDN HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching), [Service Worker API](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) and [Back/forward cache](https://web.dev/articles/bfcache) describe browser/asset version and navigation lifecycle behavior.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) provides accessibility review criteria; compliance must not be falsely inferred from performance traces.
