# OEE competency-first curriculum audit — temporary review protocol

**Protocol revision:** 1.0 (2026-11-18)
**Scope:** SEF (11 courses), APP (21 courses), SYS (10 courses); program catalogs, affected prerequisites, summative evaluations, cross-program boundaries and graduation conditions.
**Working status:** Temporary reviewer playbook, not an OEE specification, an authoring format, a course file, a mandatory learner resource, an educational-readiness status, or a new conformance test.
**Lifecycle:** Keep this file on the dedicated review branch while the three-program audit runs. Reference its branch/path and revision in every audit PR. Delete the branch and close the tracking PR when the audit and cross-program verification are complete. Do not merge the temporary file into `main`.

## 0. Authority, invariants and scope

Read, in order of authority:

1. Binding [Course Format](../../spec/course-format.md), [Evidence Rules](../../spec/evidence-rules.md), [Status Labels](../../spec/status-labels.md), [Conformance](../../spec/conformance.md), and applicable [Governance](../../GOVERNANCE.md).
2. Non-normative [Curriculum Design Guide](../DESIGN-GUIDE.md), which guides this review but cannot override binding requirements.
3. The actual current [SEF](../SEF/README.md), [APP](../APP/README.md), and [SYS](../SYS/README.md) catalogs, course definitions, and applicable accepted governance decisions.
4. Credible, version-aware disciplinary evidence selected for each course (primary standards/docs, academic curricula, domain research, and real reproducible engineering practices).

For each review, identify the exact base commit, file revisions, course/spec versions, and outstanding conflicting PRs. Do not treat an unmerged branch as the authoritative catalog. The AI program is being corrected separately: read its merged state as a dependency when needed; do not overwrite its work or assume its open PR is complete.

**Nonnegotiable working principles:**
- Start from independently justified graduate/exit capabilities, not the existing lesson outline or any fixed count. Courses, outcomes, modules, lessons, tests, labs, assessments, and weeks have no target quota or preferred distribution.
- Matching module/lesson counts are investigation signals, never automatic defects. Artificially varying counts is equally unacceptable.
- Do not maximize curriculum length, detail, vocabulary, tool coverage, or assessment volume for their own sake. Teach indispensable mechanisms at the depth needed for transfer and independent judgment.
- Honor actual prerequisite closure: a later course may reuse demonstrated competence but must not assume unassessed knowledge. Core graduation must not secretly depend on an elective.
- Preserve useful prior learning and stable identifiers where meaning is unchanged; materially replaced capabilities/criteria need explicit revision treatment, impact analysis, and correct historical interpretation.
- An activity is not automatically assessed. Required summative work must be explicit, relevant, proportionate, independently reviewable and reproducible as applicable.
- No paid resources, hidden private implementation, unsupported research claim, or undeclared specialized infrastructure may be necessary to understand public completion criteria.
- A passing structure/CI check is not academic review, learner testing, verification, accreditation, or proof of educational effectiveness.
- Findings and decisions live in relevant GitHub PRs/issues, not permanent parallel audit registries. Canonical changes belong in the published program READMEs and course definitions.
- This protocol never changes normative OEE requirements. Proposed binding changes require the existing RFC/governance process.

## 1. Repeatable audit sequence and output at each stage

Use the same steps for each program and each course. Repeat earlier steps when later evidence invalidates an assumption.

### A. Freeze the review baseline
- Record reviewed commit, branch, source files, catalog, course status, spec version, and any relevant concurrently open PR.
- Inventory existing exit outcomes, module titles, lesson objectives, formative work, required summative assessments, dependencies and projected workload.
- Run existing structural/inventory checks as baseline diagnostics. Treat reported counts, duplication and status as leads, not academic conclusions.
- Output in PR: exact scope and initial known risks. Do **not** edit before establishing the expected competency boundary.

### B. Independently reconstruct graduate/exit competencies
- Define the discipline boundary, authentic engineering tasks, relevant methods, limitations, safety concerns, and foundational mathematical or scientific prerequisites.
- Compare multiple relevant source categories: authoritative standards/primary documentation, credible university/discipline curricula, engineering practice, and what predecessor OEE courses actually assess.
- Record specific source/version and why each supports or challenges a competency; distinguish source facts from reviewer interpretation. Never invent evidence or claim accreditation.
- State capabilities in observable terms: explain, predict, calculate, derive, implement, diagnose, verify, evaluate, justify, defend, or similar.
- Give each capability a primary owner and depth: first taught, applied, specialized, or integrated. Do not introduce a new course or split existing ones solely for tidy taxonomy.
- Output in PR: compact competency ownership/coverage summary, meaningful gaps/overlaps and proposed boundary decisions.

### C. Validate program architecture before course editing
- Verify program graduate claims against required courses and their actual summative evidence; keep electives outside core graduation unless the published architecture explicitly and legitimately differs.
- Traverse transitive prerequisites, not only direct declarations; inspect for missing mathematics, language, runtime, systems, tools or platform assumptions.
- Challenge excess fragmentation, overbroad course aggregation, circular dependencies, stale order, and unjustified vendor-only pathways.
- For cross-program overlap, distinguish foundational teaching from deeper application; retain legitimate transfer, remove unproductive retreading.
- If architecture changes (course split/merge, major transfer of competency, prerequisites, core/elective classification), propose and review those program-level decisions first, then rebase affected course work.

### D. Revalidate a single course's outcomes, before modules
- Express a coherent course exit capability without a list of unrelated technologies.
- For every outcome check: importance to that exit capability; observability; one distinguishable assessment decision; appropriate depth; prerequisite readiness; genuine novelty; defensible scope and conditions.
- Identify absent/overbroad/duplicate/redundant outcomes. Avoid producing a fixed number of outcomes. Retain stable outcome IDs only for genuine continuity.
- Invert the map: each indispensable course competency must have an outcome; each retained outcome must represent a necessary capability.
- Output in PR: outcome dispositions (retain, clarify, add, replace, remove, reassign) with reasons and revision impact.

### E. Derive modules and individual lessons
- Independently group the mechanisms necessary for outcomes by conceptual cohesion, dependency and learning feedback; only then compare to existing modules.
- A module exists because it develops a coherent stage, not because every course is supposed to have 9, 13 or 15 modules.
- For **every** lesson, answer four *questions*, not four required headings: (1) What is its primary learner objective? (2) Which mechanisms, assumptions, limits and failure modes matter? (3) What observable reasoning, example, derivation, trace, experiment, or application makes this teachable? (4) What feedback would reveal misunderstanding?
- Combine lessons when they are fragments of one primary objective; split only when distinct aims, prerequisites or feedback justify it. Keep related mechanisms together even if a lesson becomes longer.
- Watch for decorative introductions, repetitive history/tool setup, isolated vocabulary, generic "best practices", duplicated endings, gratuitous "advanced" modules, sequence jumps, stale technologies, unwarranted vendor choices, and formulaic per-module labs/quizzes.
- Required history/usage/application context belongs where it improves comprehension (often an early lesson), not in repeated course metadata or a forced four-field template.
- Output in PR: module-by-module decisions and substantive lesson edits justified by competency—not numerical count targets.

### F. Design/verify practice, assessments, and evidence
- For each required outcome, write the *kind of independently inspectable performance* that would demonstrate it before deciding which existing assessment to keep.
- Check bidirectional mapping: **each outcome → actual summative criteria/evidence**, **each required assessment → outcomes it demonstrably measures**, **each necessary lesson → outcome/preparation**, and **each required task → a justified evaluation purpose**.
- Prefer authentic tasks and proportional reusable evidence. Multiple outcomes may be assessed by one task when criteria can distinguish competence in each.
- Challenge rote repetition, tutorial copying, insufficient negative/boundary/failure cases, nonindependent test oracles, false benchmark claims, unseen author prerequisites, and unverified assertions of correctness/security/performance.
- Assess correctness of evaluation criteria, required artifacts, independence, failure behavior, environment, safety and reproducibility. Formative activities remain optional unless explicitly justified as assessed performance.
- For project courses: one coherent cumulative problem, milestones that serve real progress, independently reviewable completion evidence, a meaningful unfamiliar change/fault/constraint and technical defense; do not recreate every predecessor assignment.
- Output in PR: outcome-to-assessment justification, revised evidence contract, and a clear explanation for retained/removed submissions.

### G. Challenge accuracy, workload, access and program integration
- Verify current/version-specific technical facts against authoritative sources; differentiate standards, language/runtime behavior, platform policy, emulator/simulation behavior and performance measurements.
- Recalculate study effort from reasoning, actual implementation, setup, practice, debugging, experiments, evaluation, feedback and revision—not counts of lessons or a preferred course duration.
- Require realistic free and accessible reference alternatives, safe experiments, reproducible instructions and transparent constraints. Document where learners need particular prior skills without quietly making electives required.
- Re-run transitive prerequisite and graduation checks with the proposed revisions; inspect SEF → APP/SYS and touched AI/SEC assumptions.
- Independently perform adversarial review: could learners pass without underlying competence? Are competent learners asked for unrelated work? Would an unknown-but-reasonably-scoped case expose a misunderstanding?
- Run repository validators, tests, link/catalog checks and inventory reports where applicable, and verify all affected references.
- Output in PR: findings resolved, remaining limitations, tests performed, revisions/impact and readiness claims that evidence genuinely supports.

## 2. Program-specific checks

### SEF — foundational completeness
- Establish what a learner with no programming background must understand before later specialization.
- Verify SEF1 → SEF2 → SEF11 → SEF4 reasoning pathway; check SEF8's numerical/statistical preparation separately from discrete foundations.
- Verify Linux, C11/POSIX, object/lifetime, mathematical, algorithmic, engineering workflow and independent professional-release boundaries.
- Check that SEF10 requires authentic prerequisite evidence and integrates meaningful work without unrelated repeated capstone mini-projects.
- Do not transfer mandatory SEF outcomes into SYS or APP merely to shorten SEF.

### SYS — mechanisms, Rust, and scientific evidence
- Verify SYS1 machine/ISA/ABI groundwork; SYS2 Rust ownership, C/Rust comparison and process supervision before later Rust-heavy work; SYS10 kernel reasoning before SYS3 advanced concurrency.
- Validate SYS4 networking, SYS5 crash recovery, SYS6 distributed correctness, SYS7 measurement, SYS8 operational decisions and SYS9 independent systems integration at their *distinct* depths.
- Require explicit invariants, causal traces, fault models, measured limitations and negative/failure tests where appropriate, not wordy lessons covering tool names.
- Separate SEF's user-space POSIX fundamentals from SYS kernel, concurrency and production specialization; do not silently require APP.

### APP — structural independence, authentic application engineering
- Review all 21 courses, including electives. Especially scrutinize repeated 7/8-lesson module patterns and repeated 15-module outlines, but **never** use count diversity as an acceptance criterion.
- Trace real learning from internet/web and accessible HTML/CSS through JS, TS, browser engineering, React, Node runtime, data modeling, framework services, full-stack quality, deployment and production operation.
- Check that topics owned by APP1/17/18/19/2/20/21/4/3 do not reappear as full introductions in later courses without added competency.
- Check APP5/6/7/8 boundaries, capstone prerequisite closure, and whether APP9 demonstrates integration/decision making rather than just evidence volume.
- Review each APP10–APP16 elective for substantial specialist exit capability with legitimate preparation. Investigate APP15's Rust-readiness route against SYS2/equivalent competence without inventing a hidden mandatory SYS graduation prerequisite.
- Recompute durations **after** justified course/lesson/assessment architecture, not as an editing target.

## 3. Findings, decisions and escalation

Every substantive finding must include:
- **Locator:** course/program, exact file and heading/module/lesson/outcome/assessment.
- **Observation:** the concrete defect or credible risk, not "not detailed enough" or "many lessons".
- **Academic consequence:** what capability is missing, distorted, unassessed, mis-sequenced or unnecessarily duplicated.
- **Evidence:** relevant current course text and authoritative technical/educational source or an explicitly reasoned competency argument.
- **Disposition:** retain with justification; revise; consolidate; split; move/reassign; remove; or defer with a named dependency.
- **Impact:** outcomes/assessment IDs, prerequisites, catalog/workload, prior evidence, downstream consumers and other programs.
- **Verification:** how the proposed correction was inspected, independently challenged and checked.

**Triage terms are for internal review, not course readiness labels or a numeric quality score:**
- `blocker` — required outcome absent/unassessable, invalid mandatory evidence/criteria, broken prerequisite closure, substantive technical error, or spec violation preventing defensible completion/conformance.
- `major` — material conceptual/sequence/coverage defect, unjustified curriculum ownership, misleading assessment claim, or costly systematic fragmentation/repetition.
- `minor` — clarity, title, unnecessary duplication or presentation defect without a material competency effect.
- `investigate` — pattern or uncertainty requiring examination; *not* itself a confirmed violation.

Do not automatically reject or approve courses from heuristics. When evidence is incomplete, mark the claim unresolved and identify exactly what could settle it. A review is not complete while a blocker/major defect remains unaddressed, but editorial completion **does not** promote `draft` to `tested` or `verified`.

## 4. Per-course review record — use in each course PR

Include these headings in the PR body or review discussion (not in permanent curriculum source):

1. **Baseline:** reviewed base SHA, spec and course revision, scope, relevant parallel PRs.
2. **Independent competency reconstruction:** intended exit capability, source-based benchmark, meaningful prerequisites, graduate-course owner.
3. **Outcomes:** retain/clarify/add/replace/move/remove decisions with IDs and semantic continuity.
4. **Module-by-module audit:** competency served, coherence, sequence, lesson merge/split/retention rationale; actual lesson objectives reviewed, not just titles/counts.
5. **Assessment and evidence:** outcome-to-criteria-to-evidence map; independent, invalid/failure cases and reproducibility.
6. **Cross-course effects:** prerequisite closure, differentiated coverage, elective boundaries, catalogs, capstones, historical revisions, downstream tools/resources.
7. **Review findings:** locator, severity, evidence, correction and resolution, including explicitly justified nonchanges.
8. **Verification:** CI/validator/link checks, independent challenge, accessibility/workload estimates, outstanding unknowns.
9. **Decision:** reviewed change ready for maintainer decision, needs correction, or blocked; no unsupported readiness or conformance claim.

### Consistent review questions (must be answered substantively, not ticked without inspection)
- Is each important graduate/course capability owned, prepared, and actually evaluated?
- Can each course outcome be observed in an unfamiliar but fair performance?
- Does each module represent a real coherent conceptual stage?
- For each lesson, is there a necessary distinct objective, teachable mechanism, observation/application and feedback?
- Are there missing indispensable topics or unnecessary introductory repeats?
- Are the outcome/assessment links *substantively* valid rather than only structurally present?
- Are duration, access, environment, assumptions and safety credible?
- Can the learner/independent assessor understand the completion contract without a paid platform?
- Do changes preserve valid historical IDs/evidence and course/catalog/governance consistency?
- Does the independently justified design support the course structure regardless of lesson/module numbers?

## 5. Review order, branch discipline and completion

1. **M0 program-level baseline:** review all SEF, APP and SYS architecture and cross-program dependency graph. Do not mistake inventory for the academic decision.
2. **SEF course PRs:** move in prerequisite-valid order, checking integration after changes.
3. **SYS course PRs:** move in prerequisite-valid order, validating Rust/C and SEF boundaries.
4. **APP core PRs then electives:** independently derive each course architecture, applying the same protocol without a fixed outline.
5. **Final three-program pass:** revalidate every graduate capability, required course, elective boundary, capstone, external dependency, changed source reference, and published claim against the merged default branch.

Each curriculum correction uses its own focused branch/PR unless a documented architecture decision requires a coupled change. Do not merge until maintainer approval; do not modify the active AI review branch. Refer to **`audit/oee-competency-review-protocol` / `curriculum/.audit/REVIEW-PROTOCOL.md` (revision 1.0)** in each relevant PR.

If review evidence changes the protocol, revise **this one working file** on the review branch, increment its revision, explain the reasoning in the tracking PR, and check whether prior assessments require reassessment. No silent drift.

**Closing condition:** Every one of the 42 course files has an explicit substantive review decision; program-level and cross-program findings have been resolved or accurately disclosed; course/README/CI consistency has been checked; unresolved learner-testing claims remain correctly `draft`. Close the protocol tracking PR, delete this temporary review branch, and leave no duplicate audit protocol in `main`. GitHub review/decision history remains the durable record.
