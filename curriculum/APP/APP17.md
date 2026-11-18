# APP17 — HTML & CSS Engineering

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `core`
**Prerequisites:** [APP1](APP1.md) — Web & Internet Foundations
**Duration:** 10–12 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 9–12 focused hours/week (planning estimate; subject to learner calibration)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Build web documents that preserve meaning, readability, accessibility and
layout across content and device constraints. Start by authoring valid HTML,
then build navigation, accessible information, media and native forms. Learn
how the browser chooses CSS declarations, computes styles, lays out content,
and resolves responsive and user-preference constraints. Finish by delivering
and defending a complete, maintainable **static** information interface.

APP1 already introduced how the network and browser turn resources into
visible pixels. This course develops the complementary authoring capability:
how to express semantic content in HTML and engineer its presentation in CSS.
It does **not** teach JavaScript or TypeScript programming, interactive
browser application logic, React application engineering, or backend
services. Those capabilities belong to separate courses or planned
course revisions; they are not prerequisites for APP17. It is not
a second Internet/protocol course.

Learners need only a plain text editor, a current standards-capable browser
with developer tools, a terminal and local file/static-serving capabilities.
A simple unprivileged localhost static server is sufficient; for example,
`python3 -m http.server 8000 --bind 127.0.0.1` from a disposable project
directory. No paid hosting, domain, framework, JavaScript runtime,
proprietary accessibility service, API key, analytics account or commercial
resource is required. If a learner uses a different free local server,
the assessment does not depend on Python specifically.

**Native forms are demonstrated locally; they do not implement data
persistence, server-side validation or authentication.** Use fictional
data and nontransmitting fixtures. No real third-party submission,
personal information, or public deployment is required.

The 10–12-week duration is a **draft estimate** at 9–12 focused hours
per week, including deliberate practice, debugging, revision and
assessment. Readiness remains `draft`; no learner-tested, verified
or course-conformance claim follows merely from publication.

## Learning outcomes

- **APP17-O1:** Author valid, meaningful HTML documents with appropriate metadata, document structure, headings, landmarks, and semantic elements; explain what the browser constructs from their markup.
- **APP17-O2:** Structure navigable content using accurate links, lists, figures, images, and data tables, including suitable text alternatives and understandable relationships.
- **APP17-O3:** Create usable native HTML forms with correctly associated labels, input types, field grouping, constraints, accessible error guidance, and an honest explanation of client-side validation limits.
- **APP17-O4:** Predict, explain, and debug computed CSS results using selectors, cascade origins, layers, importance, specificity, inheritance, custom properties, and source order.
- **APP17-O5:** Apply readable type, color, spacing, box-model geometry, logical properties, and maintainable visual tokens while retaining content readability and user control.
- **APP17-O6:** Implement robust document-flow, Flexbox, and Grid layouts, selecting mechanisms according to content and diagnosing overflow, sizing, and alignment failures.
- **APP17-O7:** Design interfaces that adapt to viewport and content constraints using fluid dimensions, responsive breakpoints, media and container queries where appropriate, and resilient fallback behavior.
- **APP17-O8:** Build and evaluate essential semantic, keyboard, focus, form, contrast, and reduced-motion accessibility behavior, identifying limitations of automated checks.
- **APP17-O9:** Select and integrate suitable local media assets with descriptive alternatives, dimensions, responsive image options, and measured loading and layout-stability considerations.
- **APP17-O10:** Organize a maintainable HTML/CSS codebase with reusable patterns, low-conflict selectors, progressive enhancement, and defensible cross-browser fallbacks without requiring JavaScript or a CSS framework.
- **APP17-O11:** Reproduce, investigate, and correct representative markup, cascade, layout, form, accessibility, and asset-loading failures using browser tools, validation, and documented observations.
- **APP17-O12:** Deliver and defend a complete, independently reproducible, multi-page static interface that meets stated content, accessibility, responsiveness, and maintenance constraints.

## Modules

### Module 1 — From Web Foundations to Correct HTML Documents

#### Outcomes

- APP17-O1
- APP17-O11

#### Lessons

1. **Purpose and Authoring Loop** — Build an authored local page from APP1's observational foundation using an editor, static server and browser inspection; briefly situate HTML/CSS development and applications rather than requiring separate history.
2. **Document Identity and Metadata** — Author doctype, html/head/body, document language, title, encoding and viewport metadata; choose writing direction where needed and verify their effects.
3. **Readable Content Hierarchy** — Use meaningful headings, paragraphs, emphasis, quotations and lists based on information relationships, not visual appearance.
4. **Validation, DOM Recovery and Correction** — Compare source to the parsed DOM; reproduce an invalid nesting, duplicate identifier or missing metadata defect and correct it without repeating APP1's complete parsing theory.

### Module 2 — Semantic Relationships, Navigation and Content Media

#### Outcomes

- APP17-O1
- APP17-O2
- APP17-O8

#### Lessons

1. **Landmarks and Content Relationships** — Choose header, main, nav, article, section, aside and footer according to real meaning; inspect programmatic roles and reject mandatory landmark templates.
2. **Links and Navigation Integrity** — Apply prior URL/fragment knowledge to linked pages, meaningful link text and safe destination behavior; diagnose broken links and misleading new-window actions.
3. **Figures and Image Alternatives** — Distinguish informative, decorative and complex images; select captions, text alternatives and longer explanation when the communication task needs them.
4. **Real Data Tables** — Use table caption, header cells and scope/associations for genuine tabular data; avoid using tables merely for visual layout.
5. **Local Media and Embeds** — Provide usable text or captions for included audio/video, suitable fallbacks and honest privacy limits; no third-party embed is a mandatory dependency.
6. **Semantic Inspection and Repair** — Compare visual groups and accessible names, roles and relationships through browser observations; repair a misleading landmark or content structure.

### Module 3 — Native Forms, Feedback and Safe Demonstration

#### Outcomes

- APP17-O3
- APP17-O8
- APP17-O11

#### Lessons

1. **Controls and Submission Semantics** — Select text, email, number, radio, checkbox, select and textarea by input purpose; explain form names/values and why a static page is not a processing service.
2. **Labels, Groups and Persistent Guidance** — Associate explicit labels, fieldsets, legends and instructions with controls; demonstrate why placeholders do not replace labels.
3. **Native Constraints and Error Limits** — Apply justified required/type/length/range/pattern constraints, distinguish valid and invalid states and explain browser differences and the limits of client-side security or announced error feedback.
4. **Keyboard Form Recovery** — Use keyboard-only input and correction; inspect focus indication, activation and grouping, without claiming dynamic error announcements from CSS alone.
5. **Nontransmitting Fixtures and Privacy** — Use synthetic data and local-only validation; prevent accidental external actions and GET query leaks. Testing constraints does not require form transmission.

### Module 4 — Predictable CSS Cascade and State Styling

#### Outcomes

- APP17-O4
- APP17-O10
- APP17-O11

#### Lessons

1. **Selectors and Relevant Rules** — Apply type, class, attribute, combinator and state selectors to actual elements, minimizing incidental matches.
2. **Origins, Importance and Cascade Layers** — Trace relevant declarations through user-agent, user and author origins, normal/important precedence and reversed important-layer order; reject specificity-first shortcuts.
3. **Specificity, Scope and Order** — Compare specificity, applicable scoping proximity and final source-order ties, choosing low-conflict CSS rather than escalating !important.
4. **Inheritance and Resolved Values** — Explain inherited/noninherited properties, initial/inherit/unset/revert and specified versus computed styles.
5. **Interactive and Focus States** — Style hover, focus-visible, active, invalid and disabled states without removing meaningful native affordances or conveying status by color alone.
6. **Contradictory Rule Diagnosis** — Predict and inspect a rule conflict, including a scoped tie case (supplied when unsupported locally); repair it and show which observable declaration won.

### Module 5 — Readable Visual Design and Box Constraints

#### Outcomes

- APP17-O5
- APP17-O8

#### Lessons

1. **Typography and Readability** — Use robust font stacks, relative sizes, line height and readable measures that survive text enlargement and unavailable fonts.
2. **Color and Noncolor Communication** — Check normal and large text contrasts as well as meaningful non-text indicators and focus cues; never rely on hue alone.
3. **CSS Box Geometry** — Predict dimensions from content, padding, border, margin and box-sizing rules, then explain an observed sizing defect.
4. **Flow, Spacing and Logical Directions** — Use normal flow, proportional spacing and logical properties instead of fragile physical-direction assumptions or source order distortion.
5. **Intrinsic Sizes and Overflow** — Investigate min/max constraints, long words, replaced-element dimensions and overflow without clipping essential information.
6. **Reusable Design Tokens** — Define coherent typography, spacing and color custom properties with fallbacks; inspect inheritance and maintainability trade-offs.
7. **User Preference Stress Test** — Observe zoom, enlarged text and forced-colors/high-contrast where available; repair a legitimate reading obstacle and document coverage limits.

### Module 6 — Flow, Flexbox, Grid and Content-Based Layout

#### Outcomes

- APP17-O6
- APP17-O11

#### Lessons

1. **Intrinsic Flow as Baseline** — Establish usable normal formatting and content-based sizing before imposing rigid layout constraints.
2. **Flexbox for One-Dimensional Relationships** — Choose axis, alignment, gaps and wrapping for a realistic navigation or card group and predict long-content behavior.
3. **Grid for Two-Dimensional Relationships** — Choose tracks, placement or areas for a genuinely two-dimensional page arrangement, preserving source meaning.
4. **Choosing a Layout Mechanism** — Compare Flexbox, Grid and flow for identical content demands; defend source order and keyboard progression.
5. **Min-Content and Alignment Faults** — Reproduce and repair shrink/overflow or surprising sizing in flex/grid items by finding the underlying constraint.
6. **Positioning, Stacking and Obscuration** — Use sticky, relative and absolute positioning deliberately; inspect overlap, stacking context and hidden focused content.

### Module 7 — Responsive Behavior from Actual Constraints

#### Outcomes

- APP17-O6
- APP17-O7
- APP17-O8
- APP17-O11

#### Lessons

1. **Fluid Sizing and Content-Derived Breakpoints** — Combine intrinsic, percentage, rem, min/max and clamp sizing and derive breakpoint changes from a genuine content failure rather than preset device categories.
2. **Viewport-Based Adaptation** — Use media queries for actual space constraints while maintaining accessible content and function.
3. **Container-Based Adaptation and Fallback** — Use container queries where appropriate, explain support assumptions and preserve usable baseline styles.
4. **Reflow Versus Text Resize** — Inspect approximately 320 CSS pixels for WCAG-style reflow (honoring necessary two-dimensional data exceptions), and independently test 200% text/zoom behavior; one does not prove the other.
5. **User Preferences Without Content Loss** — Adapt to reduced motion and relevant color/contrast/input preferences while preserving essential information without hover.
6. **Content Stress and Failure Diagnosis** — Test long translated-like strings, missing imagery and constrained space; identify overflow/focus causes and recheck a repair.

### Module 8 — Independent Accessibility Evaluation and Repair

#### Outcomes

- APP17-O2
- APP17-O3
- APP17-O8
- APP17-O11

#### Lessons

1. **Scoped Accessibility Evaluation** — Choose realistic keyboard, reading, navigation and form tasks and identify which representative WCAG 2.2 AA criteria can be tested without claiming certification.
2. **Keyboard Reachability and Focus** — Follow actual tab/activation paths; identify traps, invisible or fully obscured focus and inappropriate source/visual order.
3. **Names, Roles and Relationships** — Compare actual heading, table, landmark, image and form semantics using DOM/accessibility-tree inspection, not just a visual screenshot.
4. **Contrast, Reflow and Preferences** — Evaluate applicable 4.5:1 ordinary text, 3:1 large text and 3:1 meaningful non-text contrast; check constrained reflow and user preference states.
5. **Adversarial Repairs and Test Limits** — Reproduce label, keyboard/focus and content/contrast failures, repair and re-observe; distinguish automated hints and browser observations from real assistive-technology user testing.

### Module 9 — Resource-Aware Assets and Maintainable Static Delivery

#### Outcomes

- APP17-O9
- APP17-O10
- APP17-O11

#### Lessons

1. **Asset Choice and Communication** — Select local asset formats and text alternatives according to content, size and accessibility requirements rather than technology fashion.
2. **Responsive Images and Reserved Geometry** — Use srcset/sizes or picture when beneficial; reserve dimensions/aspect ratios and compare loading evidence and visible layout shifts.
3. **Resource Failure and Resilience** — Verify missing/delayed media and unsupported formats retain text meaning, accessible layout and safe local privacy boundaries.
4. **Progressive Enhancement and Compatibility** — Keep the baseline HTML usable without script; compare an optional CSS feature and fallback with disclosed browser-version or supplied compatibility evidence.
5. **CSS Organization and Regression Checks** — Organize maintainable source, refactor repeated styling and verify that meaning, navigation, focus and responsiveness do not regress.

### Module 10 — One Integrated Static Site and Technical Defense

#### Outcomes

- APP17-O1
- APP17-O2
- APP17-O3
- APP17-O4
- APP17-O5
- APP17-O6
- APP17-O7
- APP17-O8
- APP17-O9
- APP17-O10
- APP17-O11
- APP17-O12

#### Lessons

1. **One Product and Reusable Evidence** — Define real audience, information tasks, three or more purposeful pages and observable acceptance criteria; plan APP17-AS1–AS5 around the same evolving site.
2. **Information Architecture and Safe Native Form** — Build linked semantic content, informative media and a nontransmitting form demonstration with explicit privacy and functional limits.
3. **Integrate and Refine Static Delivery** — Combine readable CSS, appropriate layout, responsive behavior and local assets in maintainable, script-free source.
4. **Unfamiliar Change and Negative Cases** — Apply a bounded unexpected content or styling change, diagnose a real failure, verify the correction and check previously accepted evidence without recreating earlier submissions.
5. **Clean Reproduction and Technical Defense** — Supply simple local setup, a single indexed evidence record, transparent limitations and defensible decisions with independent reproduction and a reviewable defense.

## Completion requirements

All twelve required APP17 outcomes must be demonstrated through **five distinct summative decisions on one cumulative static information site**. APP17-AS1–AS4 evaluate different capabilities as the same source evolves; APP17-AS5 evaluates the integrated artifact, unfamiliar correction and defense. Evidence meeting a previously evaluated criterion may be **referenced**, not rebuilt or repeatedly submitted. Five assessments do not mean five websites or five compulsory sets of identical test logs. Module lessons, suggestions and formative checks do not independently gate completion.

| Assessment | Required outcome coverage | Primary decision |
| --- | --- | --- |
| `APP17-AS1` — Semantic Documents and Navigation | APP17-O1, APP17-O2, APP17-O11 | Accurate authored markup, linked content and reasoned semantic repair |
| `APP17-AS2` — Safe Native Form and Inclusive Input | APP17-O3, APP17-O8, APP17-O11 | Valid/invalid state reasoning and accessible, nontransmitting form interaction |
| `APP17-AS3` — CSS Cascade and Layout Investigation | APP17-O4, APP17-O5, APP17-O6, APP17-O10, APP17-O11 | Correct cascade prediction, layout construction and causal repair |
| `APP17-AS4` — Responsive Accessibility and Assets | APP17-O2, APP17-O6, APP17-O7, APP17-O8, APP17-O9, APP17-O11 | Measured reflow, focused access, contrast, assets and fallback review |
| `APP17-AS5` — Static-Site Integration and Defense | APP17-O1–APP17-O12 | One independently reproducible site, new bounded correction and defended trade-offs |

### Shared environment, evidence and safety

A text editor, a standards-capable browser and browser developer tools, local assets and an unprivileged local static server are sufficient. A command such as `python3 -m http.server 8000 --bind 127.0.0.1` may serve fixtures, but Python, a hosted account, a domain, public network, framework, JS runtime, tracking tool or paid accessibility service is **not mandatory**. Equivalent free local serving is acceptable. Record browser/version, tool and environment information only where material to evaluation. Source/DOM inspection and keyboard testing provide evidence that screenshots or passing validators alone cannot.

Forms are **demonstrations of native controls and validation**, not a backend. Inspect named values and valid/invalid states with fabricated inputs **without needing to transmit** any submission. If submission is optionally shown, specify a demonstrably safe local nontransmitting mechanism; avoid real user data, external actions and GET query-string disclosures. Browser-native validity bubbles and CSS-only pseudo-classes are not evidence of reliable dynamically announced error messages or server-side protection.

Representative **WCAG 2.2 AA** checks, where relevant to the authored content, must distinguish: (a) normal text contrast **4.5:1**, large text **3:1**; (b) meaningful non-text UI indicators **3:1** where the criterion applies; (c) keyboard reachability, visible and not-entirely-obscured focus; (d) reflow around **320 CSS pixels of available viewport width**, allowing legitimate separately scrollable two-dimensional data such as a table; and (e) **200% text resize/zoom as a separate test**. Ordinary page content must not be inadvertently clipped or require two-dimensional scrolling. These focused observations do not prove full WCAG conformance, screen-reader user testing or universal browser support. Compare different browser implementations only when there is actual evidence or clearly labeled supplied scenarios.

### Required summative assessments

- **APP17-AS1** (required document structure and semantic navigation)
  - Outcomes: APP17-O1, APP17-O2, APP17-O11
  - Work: Establish the first **two linked pages of the same eventual site** for a realistic public-information task. Include a meaningful nested content structure, navigation landmark, informative figure, and one genuinely tabular dataset with appropriate captions/headers. Inspect source and parsed DOM, record two substantive semantic faults and their corrections, and verify linked/fragment navigation without scripting.
  - Criteria: Accurate language/title, meaningful headings, landmarks, unique IDs, useful link text, images/alternatives, table relationships and source order; no unresolved parsing or navigation defect that changes meaning. The learner distinguishes an authored structure from browser-repaired DOM and explains why each correction is semantically necessary.
  - Evidence: Local HTML and assets, an interpretable page/link map, before/after source and DOM observations, relevant validator findings and a concise semantic rationale.

- **APP17-AS2** (required native form and inclusive input)
  - Outcomes: APP17-O3, APP17-O8, APP17-O11
  - Work: Add a native static form **within that same site**, with text entry, grouped choices, useful persistent guidance and at least two justified native constraints. With fictional input, inspect missing/malformed/valid states and recovery by keyboard, including label activation and visible focus. Explain browser submission semantics and why the static page does not process, persist or authorize an input. A real submission is **not required**.
  - Criteria: Controls have accurate labels, group relationships, meaningful purposes, persistent instructions and recoverable invalid states; documented native constraints work as claimed where applicable, with a logical keyboard sequence and visible focus. No data is transmitted to an unknown endpoint or leaked through a GET query. The learner does not mistake client validity or CSS styling for assured accessible error announcement or backend security.
  - Evidence: The same site and form source, fictional input/validity examples, keyboard/label/focus observation and bounded explanation of nontransmission, browser differences and client-only limits.

- **APP17-AS3** (required CSS cascade and layout diagnosis)
  - Outcomes: APP17-O4, APP17-O5, APP17-O6, APP17-O10, APP17-O11
  - Work: Extend **the same site** with an article and responsive cards using reusable visual tokens and Flow, Flexbox and Grid only where each fits. Predict and inspect competing rules that exercise user-agent versus author origin, importance, **normal and important layer order**, specificity, inheritance and source order. Reason about a provided scoped-rule proximity tie case (a labeled standards-based example is acceptable if the browser lacks support). Inject and repair a sizing/overflow or alignment fault without blanket `!important`; refactor one duplicated style.
  - Criteria: Prediction and observed computed styles align when the browser supports the case; the learner uses the correct ordering of origin/importance, layers, specificity, scoping proximity where applicable and source order rather than treating specificity as the first rule. Layout choices are content-driven and preserve useful source/keyboard order; a reproduced fault has a justified repair and regression check; refactoring does not add opaque overrides.
  - Evidence: Existing site source, a concise rule-prediction/observation table (identify supplied, unexecuted cases), selected computed-style traces, fault/repair demonstration and explanation of layout/selector decisions.

- **APP17-AS4** (required responsive accessibility and asset review)
  - Outcomes: APP17-O2, APP17-O6, APP17-O7, APP17-O8, APP17-O9, APP17-O11
  - Work: Audit and improve **the same site** with local responsive imagery and content-aware layout. Test wide/narrow viewports, reflow around 320 CSS pixels, a separate 200% text/zoom condition, keyboard travel, focus visibility/obscuration, representative normal/large text and relevant non-text contrast, image alternatives, reserved image dimensions and a loading trade-off. Compare one optional CSS feature with a usable fallback, reproduce a real failure and recheck its repair.
  - Criteria: Ordinary content and controls remain understandable and operable at required constraints without unnecessary two-dimensional scrolling; legitimate exceptional tables or diagrams may have bounded independent scrolling. Focus is reachable, visible and not fully obscured. Applicable measured contrast meets **4.5:1** ordinary text, **3:1** large text and **3:1** necessary non-text indicators. Images have meaningful text treatment and avoidable layout shifts are mitigated; fallback works without JavaScript. No full conformance claim is inferred.
  - Evidence: One bounded browser/viewport/reflow/zoom/keyboard observation log, relevant contrast calculations, image/loading or reserved-dimension trace, before/after defect evidence and version-qualified support/fallback explanation. Reference AS1–AS3 evidence instead of resubmitting it.

- **APP17-AS5** (required integrated static site and independent defense)
  - Outcomes: APP17-O1, APP17-O2, APP17-O3, APP17-O4, APP17-O5, APP17-O6, APP17-O7, APP17-O8, APP17-O9, APP17-O10, APP17-O11, APP17-O12
  - Work: Complete **the one evolving static site** of at least three purposeful pages for an explicit audience. Integrate linked semantic information, safe native form demonstration, local assets, maintainable reusable CSS, responsive layouts and a documented failure-repair history. Reproduce it from clean source. Address an **unfamiliar but bounded content, accessibility, CSS or asset defect/change**, verify the correction without regressing earlier accepted criteria, and give a reviewable written, recorded or live technical defense.
  - Criteria: Independent reproduction requires only disclosed, free local steps; navigation, content, forms, asset and responsive behaviors meet their public acceptance criteria without JavaScript. The new problem is understood, corrected and rechecked. Unresolved critical semantic, keyboard/focus, form, required contrast or responsive failures preclude passing even if disclosed; other material limitations are recorded and bounded. The defense distinguishes direct evidence from guesses, explains real decisions and avoids untested accessibility or compatibility claims.
  - Evidence: One repository or portable source archive, clean-start instructions, a concise requirement-to-criterion map **referencing** already accepted AS1–AS4 evidence, the unfamiliar change/repair and regression record, materially necessary environment facts, limitations and a reviewable defense. No duplicate site or evidence packet is required.

### Completion decision and revision safety

APP17 completion requires a defensible, separately recorded evaluation decision for every required assessment and demonstrated APP17-O1–APP17-O12. The cumulative assessment design reduces redundant artifacts, **not the required competencies**: passing AS5 cannot replace an unproven AS1–AS4 outcome. Optional formative exercises do not count as extra gates. A learner can use the public criteria without a paid platform or private answer key.

Prior course and learner records remain identified with the applicable specification and source revision; the reorganization does not silently regrade or equate historical APP2, APP9 or APP17 evidence. APP17 remains **`draft`**: source validation and editorial review do not establish learner-tested effectiveness, full accessibility conformance, accreditation or `verified` readiness. See [Evidence Rules](../../spec/evidence-rules.md) and [Status Labels](../../spec/status-labels.md).
