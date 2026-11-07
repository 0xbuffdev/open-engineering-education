# APP17 — HTML & CSS Engineering

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `core`
**Prerequisites:** [APP1](APP1.md) — Web & Internet Foundations
**Duration:** 10–12 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 9–12 focused hours/week (planning estimate; subject to learner calibration)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md) · [Migration decision](ARCHITECTURE.md)

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
It does **not** teach JavaScript language programming (APP18), TypeScript
(APP19), DOM application logic (the revised APP2), React (APP20), or backend
services (APP21/APP3). It is not a second Internet/protocol course.

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

### Module 1 — From Web Documents to Authored Interfaces

#### Outcomes

- APP17-O1
- APP17-O11

#### Lessons

1. **Course Orientation** — Introduce the course's purpose, the history and evolution of HTML/CSS, common applications, prerequisites, and what this course does not teach.
2. **The Authoring Loop** — Create, serve on loopback, inspect, and modify a tiny document with freely available tools.
3. **HTML Document Skeleton** — Construct doctype, html, head, body, language, encoding, and viewport metadata; explain their roles.
4. **HTML Parsing and the DOM** — Compare source markup, the parsed DOM, and a rendered view; recognize implicit element repair.
5. **Text and Document Hierarchy** — Build a coherent page outline using headings, paragraphs, emphasis, quotations, and lists.
6. **Source Validation** — Identify invalid nesting, duplicate identifiers, missing metadata, and repair effects using validation and DOM inspection.

### Module 2 — Semantic Content and Navigation

#### Outcomes

- APP17-O1
- APP17-O2
- APP17-O8

#### Lessons

1. **Page Landmarks** — Distinguish header, main, nav, article, section, aside, and footer through content purpose.
2. **Navigation Architecture** — Build consistent local and cross-page navigation with understandable link text.
3. **URLs and Link Safety** — Use relative references, fragments, external destinations, and safe new-window disclosure deliberately.
4. **Figures and Alternatives** — Choose informative, decorative, and complex-image text alternatives and captions for their actual purpose.
5. **Data Versus Layout Tables** — Represent genuinely tabular relationships with headers, scope, and captions instead of using tables for layout.
6. **Media and Embedded Content** — Provide meaningful fallback or captions for local media and explain when an embed creates a privacy boundary.
7. **Semantics Inspection** — Compare visual grouping with programmatic names, roles, and relationships in developer tools.

### Module 3 — Native Forms and User Input

#### Outcomes

- APP17-O3
- APP17-O8

#### Lessons

1. **How Native Forms Work** — Distinguish controls, labels, names, values, submission methods, and what a static demonstration can verify.
2. **Text and Choice Controls** — Select fitting text, email, number, checkbox, radio, select, and textarea semantics for a stated requirement.
3. **Labels and Help** — Associate explicit labels, fieldsets, legends, hints, and required-state descriptions without placeholder-only labeling.
4. **Native Constraints** — Apply suitable required, length, type, range, and pattern constraints and inspect browser validity behavior.
5. **Error and Success Boundaries** — Distinguish built-in client-side feedback from nonexistent server processing and provide readable correction guidance.
6. **Keyboard Form Journey** — Complete and repair a form using only a keyboard with understandable order and visible focus.
7. **Privacy-Safe Test Fixtures** — Use fabricated input and local-only demonstrations; avoid collecting or transmitting real personal data.

### Module 4 — The CSS Cascade and Computed Styles

#### Outcomes

- APP17-O4
- APP17-O10
- APP17-O11

#### Lessons

1. **CSS Rules and Selectors** — Write type, class, attribute, combinator, and state selectors while minimizing unintentional matches.
2. **The Cascade Algorithm** — Predict winning declarations from relevance, origin, importance, layers, specificity, scoping proximity, and order.
3. **Inheritance and Initial Values** — Explain inherited versus noninherited properties and the effects of initial, inherit, unset, and revert.
4. **Specificity and Layers** — Refactor competing rules with low-specificity selectors and predictable cascade layers.
5. **Custom Properties** — Use named tokens, fallback expressions, and inheritance to manage a coherent visual system.
6. **Pseudo-Classes and States** — Style focus, focus-visible, hover, active, invalid, and disabled states without removing usable defaults.
7. **Computed-Style Diagnosis** — Inspect a contradictory stylesheet and show precisely why a declaration wins or is ignored.

### Module 5 — Typography, Color, and Box Geometry

#### Outcomes

- APP17-O5
- APP17-O8

#### Lessons

1. **Typography and Reading** — Choose font stacks, relative sizes, line height, readable line length, and robust text alignment.
2. **Color and Meaning** — Establish usable contrast and ensure status and emphasis are not communicated by color alone.
3. **The CSS Box Model** — Predict content, padding, border, and margin dimensions with appropriate box sizing.
4. **Flow and Spacing** — Use normal flow, block/inline formatting, spacing relationships, and logical direction-aware properties.
5. **Sizing and Overflow** — Apply min/max constraints, intrinsic sizes, overflow behavior, and sensible long-word wrapping.
6. **Visual Tokens** — Establish reusable spacing, typography, color, and surface variables without concealing semantics.
7. **User Text Preferences** — Test text enlargement, zoom, and high-contrast settings for reading and navigation failures.

### Module 6 — Layout with Flow, Flexbox, and Grid

#### Outcomes

- APP17-O6
- APP17-O11

#### Lessons

1. **Intrinsic Layout First** — Use normal flow and content-based sizing before introducing explicit layout constraints.
2. **Flexbox Axes and Distribution** — Build one-dimensional navigation and card arrangements using axes, wrapping, gap, and alignment.
3. **Grid Tracks and Areas** — Build two-dimensional page structure using tracks, auto-placement, and explicit areas when justified.
4. **Flex or Grid** — Explain why each mechanism fits different content requirements, including source versus visual order.
5. **Alignment and Min-Content Failures** — Diagnose shrinking, min-content overflow, and unexpected grid/flex item sizing.
6. **Positioning and Layering** — Use relative, absolute, sticky, and stacking contexts cautiously without obscuring content or focus.
7. **Long and Sparse Content** — Test layouts with unusually long headings, missing images, short content, and localization-like text growth.

### Module 7 — Responsive and Adaptive Interface Design

#### Outcomes

- APP17-O6
- APP17-O7
- APP17-O8

#### Lessons

1. **Content-First Breakpoints** — Derive breakpoints from actual layout failure instead of a device catalog.
2. **Fluid Dimensions** — Use percentages, rem, flexible tracks, min/max, clamp, and intrinsic sizing appropriately.
3. **Viewport Media Queries** — Respond to constrained space without requiring one fixed screen resolution.
4. **Component-Level Adaptation** — Use container queries where supported and provide a usable fallback for unsupported environments.
5. **No-Horizontal-Scroll Review** — Test narrow viewports and 200% zoom, distinguishing justified exceptions from broken layout.
6. **Input and Motion Preferences** — Respond to reduced motion and relevant user preferences without removing essential information.
7. **Responsive Failure Triage** — Record measured layout causes and repairs instead of relying on screenshots alone.

### Module 8 — Accessible Documents and Interaction

#### Outcomes

- APP17-O2
- APP17-O3
- APP17-O8
- APP17-O11

#### Lessons

1. **Accessibility Foundations** — Relate semantic HTML, assistive-technology exposure, and the limitations of visual inspection.
2. **Keyboard Reachability** — Test links and native controls by tabbing through meaningful focus order with no keyboard trap.
3. **Focus Visibility** — Provide unmistakable focus indication and prevent sticky content from fully obscuring focused controls.
4. **Names and Relationships** — Inspect image alternatives, form labels, table relationships, and landmark names.
5. **Contrast and Resizing** — Check representative text/non-text contrast and text resizing against explicit criteria.
6. **Native Versus Custom Widgets** — Prefer real anchors, buttons, and controls over inaccessible clickable containers.
7. **Accessibility Test Limits** — Combine keyboard testing, browser accessibility-tree inspection, and automated checks without claiming certification.
8. **Accessible Error Repair** — Reproduce and fix a missing label, invisible focus, and invalid-form guidance regression.

### Module 9 — Assets, Resilience, and CSS Maintenance

#### Outcomes

- APP17-O9
- APP17-O10
- APP17-O11

#### Lessons

1. **Image Formats and Sources** — Select an appropriate format and local asset sizes without an external hosting dependency.
2. **Responsive Images** — Use width/size information, srcset and sizes or picture where genuinely beneficial.
3. **Loading and Layout Stability** — Provide intrinsic dimensions or aspect ratios, inspect waterfalls, and reduce image-caused layout shifts.
4. **File Organization** — Organize semantic page templates and layered or component-based CSS without importing a UI framework.
5. **Progressive Enhancement** — Start with usable documents, add supported CSS features, and evaluate fallback when a feature is absent.
6. **Cross-Browser Differences** — Reproduce one meaningful standards/support difference or a supplied compatibility scenario.
7. **Regressions and Refactoring** — Refactor repeated styles while proving navigation, layout, and focus behavior did not regress.

### Module 10 — Static Site Integration and Technical Review

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

1. **Define the Content Contract** — Choose a concrete multi-page information service, audiences, tasks, constraints, and success criteria.
2. **Architecture and Navigation** — Plan pages, landmarks, content hierarchy, form purposes, and reusable presentation patterns.
3. **Incremental Implementation** — Build the static interface using semantic HTML and maintainable styles with meaningful commits.
4. **Responsive and Keyboard Audit** — Exercise real tasks in narrow/wide viewports, keyboard-only use, zoom, and relevant preference modes.
5. **Failure Injection** — Introduce broken resource, invalid-control, and overflow scenarios and document their repair.
6. **Evidence and Reproduction** — Prepare a self-contained clean-checkout project with validation steps and verifiable observations.
7. **Trade-Off Defense** — Explain semantic, accessibility, cascade, layout, compatibility, and resource decisions with known limitations.

## Completion requirements

All **twelve required course outcomes** are evaluated through five public,
required summative assessments. The learning activities in the modules
prepare learners for these evaluations but do **not** create separate
submission requirements by being listed. A checklist or automated pass
alone is insufficient evidence of semantic correctness, accessibility,
maintainable styling or independent implementation.

| Assessment | Required outcome coverage | Principal evidence |
| --- | --- | --- |
| `APP17-AS1` — Document Structure and Semantic Navigation | APP17-O1, APP17-O2, APP17-O11 | Semantic documents and validation evidence |
| `APP17-AS2` — Native Form and Inclusive Input Review | APP17-O3, APP17-O8, APP17-O11 | Local form and keyboard-error evidence |
| `APP17-AS3` — CSS Cascade and Layout Diagnosis | APP17-O4, APP17-O5, APP17-O6, APP17-O10, APP17-O11 | Cascade diagnosis and responsive layout |
| `APP17-AS4` — Responsive Accessibility and Asset Review | APP17-O2, APP17-O6, APP17-O7, APP17-O8, APP17-O9, APP17-O11 | Accessibility, responsive and asset test matrix |
| `APP17-AS5` — Multi-Page Static Interface and Engineering Defense | APP17-O1, APP17-O2, APP17-O3, APP17-O4, APP17-O5, APP17-O6, APP17-O7, APP17-O8, APP17-O9, APP17-O10, APP17-O11, APP17-O12 | Reproducible static project and technical defense |

### Shared execution and review boundaries

Use local assets and sanitized or synthetic test cases. Record browser
family/version, viewport conditions, relevant accessibility
preferences, environment and steps sufficient to reproduce observed
behavior. A browser screenshot alone does not prove accessibility
semantics; combine source/DOM inspection and meaningful keyboard use.
An automated linter cannot certify full accessibility, and absence
of visible failures does not prove broad cross-browser compatibility.

Assessment of design and user experience is made against **published
functional and accessibility criteria**, not personal taste or
mandatory reliance on one branded CSS library. A learner can satisfy
requirements with standard HTML and CSS, an equivalent free editor,
locally available fonts, and offline assets.

To verify a static form without an external receiver, inspect browser
constraint-validation states and controls' names/values locally.
If a submission is demonstrated, it must use a safe local
nontransmitting fixture; do not suggest that a GET query or local page
load constitutes server-side processing.

Use these explicit review conditions where applicable:

- Inspect narrow and wide viewports, keyboard-only navigation,
  200% zoom, and relevant text/contrast/motion preferences.
- Test representative WCAG 2.2 AA text contrast thresholds
  (4.5:1 normal text, 3:1 large text), name/label relationships,
  focus indication and content reflow. Do not claim the entire
  site is WCAG-conformant based on those checks alone.
- Distinguish content-dependent design decisions from arbitrary
  viewport or fixed-technology assumptions; document meaningful
  browser-support exceptions.
- Disclose unsupported CSS features, data/form-processing limitations,
  visual regressions and unresolved issues instead of inventing
  positive test results.
- Never require public hosting, real personal-data collection,
  tracking scripts, server implementation or paid accessibility tools.

### Required summative assessments

- **APP17-AS1** (required document structure and semantic navigation)
  - Outcomes: APP17-O1, APP17-O2, APP17-O11
  - Work: Create two linked, independently intelligible HTML documents for a realistic public-information task. One must include a nested content hierarchy, a navigation landmark, an informative figure, and a genuinely tabular dataset with suitable table semantics. Inspect both source and parsed DOM, document at least two deliberate semantic corrections, and demonstrate that links and fragments work without scripting.
  - Criteria: Documents parse without unaddressed errors that affect meaning; language, title, headings, landmarks, unique identifiers, links, meaningful alternative text, table headings/caption, and source order match the stated information relationships. The learner distinguishes informative from decorative imagery, traces navigation and fragment targets, and explains any remaining browser-repair behavior.
  - Evidence: Complete local HTML files and assets; a page/link map; validator findings with corrections; before/after source and DOM excerpts; keyboard navigation observations and a short rationale for semantics.

- **APP17-AS2** (required native form and inclusive input review)
  - Outcomes: APP17-O3, APP17-O8, APP17-O11
  - Work: Author a static contact or request form with text, one grouped choice, contextual help, and at least two meaningful native validation constraints. Demonstrate a valid-input path and invalid-input variants with fabricated data; explain submission semantics and why a static-only page does not persist or process input. Perform a keyboard-only review including label activation, focus indication, required-state and error recovery.
  - Criteria: Every relevant control has an accessible name and meaningful input purpose; grouped choices use suitable semantics; native validation distinguishes missing, malformed, and valid states where applicable; focus is visible; keyboard navigation is logical; user data is not silently sent to an outside endpoint. The learner correctly identifies the limits of native client-side validation and avoids claiming backend security.
  - Evidence: HTML form, synthetic test matrix, inspection of labels/relationships, keyboard/focus observations, documented invalid and corrected inputs, and explanation of local-only handling and its limitations.

- **APP17-AS3** (required css cascade and layout diagnosis)
  - Outcomes: APP17-O4, APP17-O5, APP17-O6, APP17-O10, APP17-O11
  - Work: Implement a small responsive article-and-cards interface using a reusable visual token set and both Flexbox and Grid where each is justified. Predict and then inspect at least five competing CSS declarations covering specificity, layering, inheritance, and source order; introduce an overflow or alignment defect and repair it without a broad important override. Refactor one repeated style pattern and verify the result.
  - Criteria: Predictions match browser computed styles with correct cascade reasoning; visual hierarchy remains readable; box and layout decisions respond to content rather than fixed pixels; Flexbox and Grid are used for their appropriate layout axes; the injected defect has a reproducible root cause and regression check; reuse does not create unexplainable overrides.
  - Evidence: HTML/CSS source, a five-case prediction-versus-observation sheet, DevTools computed-style notes, wide/narrow comparison, injected-failure reproduction and repair, and concise rationale for the refactor.

- **APP17-AS4** (required responsive accessibility and asset review)
  - Outcomes: APP17-O2, APP17-O6, APP17-O7, APP17-O8, APP17-O9, APP17-O11
  - Work: Extend an interface with responsive media and a resource-aware content layout. Test at narrow and wide CSS viewports, at 200% browser zoom, and with keyboard navigation; assess representative contrast and focus visibility, form or navigation usability, image alternatives, image dimensions and one loading-related trade-off. Exercise a supported and a fallback CSS behavior without relying on JavaScript.
  - Criteria: Ordinary content and controls remain operable and understandable at constrained sizes without unintended horizontal page scrolling; focus is visible and not completely obscured by authored elements; tested color combinations meet stated contrast thresholds (normal text 4.5:1 and large text 3:1 where WCAG 2.2 AA applies); images have appropriate alternatives or decorative treatment and do not cause avoidable layout jumps; relevant fallback content remains usable. These checks do not assert full WCAG conformance.
  - Evidence: Browser/viewport/zoom test log with limitations, keyboard focus sequence, contrast calculations, image inspection/waterfall or equivalent local observation, source and repaired states, and a cross-browser or supplied-support-case explanation.

- **APP17-AS5** (required multi-page static interface and engineering defense)
  - Outcomes: APP17-O1, APP17-O2, APP17-O3, APP17-O4, APP17-O5, APP17-O6, APP17-O7, APP17-O8, APP17-O9, APP17-O10, APP17-O11, APP17-O12
  - Work: Deliver a cohesive, at-least-three-page static information site for an explicitly defined audience. Include a structured content page, a meaningful native form demonstration, and reusable responsive layouts; provide linked navigation, local assets, a stylesheet organization strategy, and tested failure states. Conduct a clean-checkout reproduction and defend selected trade-offs in a reviewable written or recorded explanation.
  - Criteria: The complete site is reproducible with freely available local tooling, usable without JavaScript, backed by appropriate semantic structure, and navigable by keyboard. Required pages, links, forms, assets, responsive states, and documented acceptance tests work as claimed. Validation and observed failures are reported accurately; significant accessibility, layout, and resource defects are fixed or explicitly identified as unresolved limitations. The defense ties concrete implementation and debugging evidence to decisions and avoids claiming untested accessibility or cross-browser guarantees.
  - Evidence: Repository or portable source archive, README with clean-start commands, page and asset inventory, requirement-to-test matrix, representative keyboard/zoom/viewport and invalid-input checks, validation/diagnostic records, an injected failure and repair, version/environment notes, and a reviewable technical defense.

### Completion decision and revision safety

A learner completes this course only when **all five required
assessments** satisfy their published criteria and collectively
establish APP17-O1 through APP17-O12. Weak or fabricated evidence
must be revised; effort, passive study, an unchecked page, or
a successful validator alone cannot substitute for demonstrated
capability. Independent reviewers may request a justified,
reproducible clarification or defense tied to a published outcome.

The capstone assessment reuses and strengthens previous work where
appropriate; learners need not produce five unrelated sites.
Additional module exercises, sample layouts and practice audits
are **optional formative work**, not hidden summative gates.

This newly introduced APP17 revision uses the `v0.2.0`
outcome-and-evidence contract. Earlier published APP2 includes
overlapping HTML/CSS lessons until its separate migration PR
narrows that course to framework-neutral browser/frontend engineering.
Existing APP2/APP9 work and learner completion records remain
attributable to their original course revisions; the new catalog
does not silently revise historical evidence or claim equivalent
competency without reassessment.
