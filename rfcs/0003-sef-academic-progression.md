# RFC 0003: SEF Academic Progression and Mathematical Readiness

- **Status:** `accepted`
- **Author:** 0xBUFF (proposal for steward review)
- **Created:** 2026-11-16
- **Last updated:** 2026-11-20
- **Related issue:** [#79 — SEF academic hardening](https://github.com/0xbuffdev/open-engineering-education/issues/79)
- **Affected specification version:** existing draft `v0.2.0` course format; proposed SEF curriculum revisions only

**Current implementation:** The eleven-course SEF catalog and its assessment contracts are published as `v0.2.0` drafts. The original problems and delivery steps below describe the November 16 decision. The [SEF catalog](../curriculum/SEF/README.md) and course definitions describe current requirements; no course-format migration or bundled SEF9 example is required.

## 1. Summary

Revise Software Engineering Foundations (SEF) before treating its course architecture as settled. Preserve the program's first-principles computer education, Python, C, Linux, algorithms, professional engineering, and cumulative capstone. Make mathematical prerequisites explicit; extract discrete mathematics and proof readiness from the overloaded SEF8 into a distinct required course; ensure remaining numerical mathematics is taught coherently; and close gaps in programming abstraction, professional practice, and cross-program competency ownership.

This proposal changes the **SEF curriculum contract and course catalog**, not the repository-wide OEE `v0.2.0` course format, evidence rules, or status-label meanings. It must be accepted before implementation; publication and structural validation do not establish educational readiness.

## 2. Problem

The ten published SEF courses are `draft` and collectively offer a substantial foundation. Their source contracts nonetheless expose material sequencing and feasibility issues:

1. **Hidden proof prerequisites.** [SEF4](../curriculum/SEF/SEF4.md) has only SEF2 as a prerequisite but expects induction, recurrence bounds, loop invariants, combinatorial reasoning, and graph properties. These are formally introduced in [SEF8](../curriculum/SEF/SEF8.md), which is currently allowed to run concurrently with SEF4. Prerequisite competence is therefore not assured when assessed.
2. **Different mathematical exit competencies compressed into one course.** SEF8 covers an ungraded arithmetic/pre-algebra bridge, logic and proofs, linear algebra, probability and inference, calculus, numerical behavior, and optimization in a nominal 11–12 weeks at 10–15 focused hours/week. Those estimates have not been established through learner trials, especially for a learner who must first remediate arithmetic.
3. **Implicit programming abstractions.** [SEF2](../curriculum/SEF/SEF2.md) teaches Python functions, modules, collections and mutation, but lacks clearly owned, evaluated introductory user-defined data abstractions and a distinct account of annotations/static checking versus runtime semantics.
4. **Unsettled systems boundary.** [SEF7](../curriculum/SEF/SEF7.md) combines introductory POSIX resource/process interfaces with nonblocking TCP state machines and event-loop reliability. Advanced systems networking naturally fits later SYS work, but removing it from SEF without first publishing its downstream owner would create a gap.
5. **Professional obligations lack an explicit complete map.** SEF5 and SEF9 cover reviews, CI, AI authorization and provenance, but general engineering ethics, software licensing, privacy, communication and accessibility responsibilities need clearer outcome ownership.
6. **Completion evidence is demanding.** Several courses require substantial repeated defect histories, clean-start reproductions and reviewer responses. The [Course Format](../spec/course-format.md) and [Evidence Rules](../spec/evidence-rules.md) require authentic, proportional outcomes-based evaluations, not paperwork quotas. Reuse, learner access and independently available fixtures need review.
7. **Catalog/tooling assume exactly ten numerically ordered courses.** The [SEF validator](../scripts/check-sef-curriculum.py) and migration tests assume SEF1–SEF10 and will need deliberate changes rather than silent exceptions.

The [ACM/IEEE-CS/AAAI CS2023 curricular report](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm) treats discrete mathematical reasoning, proofs, counting, functions, graphs, and asymptotic notation as foundational computing knowledge. That supports a distinct readiness gate, not any mandated OEE course count or claim of university accreditation.

## 3. Proposed change

### 3.1 Architectural decisions

**D1 — Preserve existing course identities.** Existing SEF1–SEF10 codes identify established course contracts. Do not renumber those courses to force catalog order to match numeric order; neither rename a moved competency without mapping its old evidence nor silently rewrite historical completion records.

**D2 — Add `SEF11 — Discrete Mathematics for Computing` as a required course in study order after SEF2 and before SEF4.** Its public prerequisite is SEF2. Its entry diagnostic is ungraded and cannot be used to exclude learners. Mathematical readiness must be demonstrated through actual required assessment, with reassessment on equivalent unfamiliar cases. The code `SEF11` identifies the newly introduced course; its placement **before** SEF4 is intentional. Prerequisite relations, not numeric codes, determine the educational sequence.

**D3 — Require SEF11 before SEF4.** SEF4 retains SEF2 through transitive dependency, but its published immediate prerequisite becomes SEF11. Recursion, sorting, invariants, amortized analysis, shortest paths and dynamic programming stay in SEF4. Proof methods and mathematical foundations are first learned in SEF11, then applied and deepened using real algorithms in SEF4.

**D4 — Re-scope SEF8 to numerical mathematics for computing and AI.** SEF8's immediate prerequisite becomes SEF11. Preserve and deepen the mathematical capabilities that remain: functions/graphs and necessary algebra, linear algebra, probability, descriptive statistics, uncertainty and inference, differentiation, numerical error and introductory optimization. Explicitly introduce logarithms, elementary limit intuition and the required function algebra *before* calculus; do not imply numerical differentiation replaces analytic understanding. Do not require NumPy, a paid account or proprietary grading.

**D5 — Complete all eleven required courses before SEF10.** The capstone must require SEF11 in addition to SEF1–SEF9. SEF10 remains the existing coherent learner-owned project; do not introduce an unrelated additional capstone.

**D6 — Preserve the foundational/specialist boundary.** SEF6 continues to teach foundational C semantics, object lifetime, pointer validity, allocation and resource contracts. Rust and the advanced C/Rust comparison remain for SYS. SEF7 retains required foundational descriptor, process, directory, signal and pipe reasoning, plus a correctly bounded introduction to loopback framing. More advanced nonblocking networking belongs in SYS **only once** the corresponding SYS outcomes and assessments are publicly adopted. No outcome is removed from SEF merely on the assumption that another program will eventually teach it.

**D7 — Improve other SEF courses with explicit instructional and assessment ownership.** Add beginner-appropriate Python data abstraction/typing capabilities to SEF2, refine physical-to-logic and representation explanations in SEF1, clarify Bash/POSIX/GNU portability in SEF3, strengthen design reasoning in SEF5, and make general professional responsibility and non-AI engineering competence explicit in SEF9. Retain SEF10's reproducible independent defense and evaluate integration across prior competencies without requiring unrelated extra applications.

### 3.2 Required SEF11 competency contract

The adopted SEF11 course definition must provide observable, appropriately bounded outcomes in the following clusters. The precise stable `SEF11-O*` and `SEF11-AS*` identifiers are established in the implementation course file and audited before merge:

| Cluster | Essential independently demonstrable capability | Representative evidence |
| --- | --- | --- |
| Arithmetic and pre-algebra bridge | Signed arithmetic, fractions, ratios, units, powers, equations, inequalities and simple function tables | Unfamiliar hand-worked cases, explanation and independent check, corrected misconception |
| Logic, sets and functions | Connectives, truth tables, quantifiers/negation, finite sets, relations, equivalence and function properties | Correct formal reasoning, counterexample, finite representation |
| Discrete counting | Sum/product rules, permutations, combinations, elementary inclusion/exclusion and pigeonhole reasoning | Explanation and independently checked small enumeration |
| Proof and recursion | Direct proof, contradiction, induction, recursively defined sequences and termination reasoning | Complete base/induction steps, counterexample to false generalization |
| Asymptotic and recurrence reasoning | Growth notation and valid bounds on simple recurrences, including assumptions and limitations | Proof/derivation and distinction from finite timing |
| Graph and state reasoning | Finite graph degree, paths and connectivity, basic relation/graph invariants and simple finite-state transition reasoning | Reproducible hand trace and argument |

The course MUST publish enough required assessments to demonstrate **every cluster** with public work, criteria and evidence. One integrated investigation MAY reuse checked work rather than requiring independent reports for each lesson. No fixed `lesson → test → lab` pattern is introduced. Safe standard-library Python or paper-based equivalents may support independent reasoning, but programming fluency alone is not proof of the mathematics.

The initial catalog duration is a **provisional learner-tested estimate to be set during implementation**; do not assert that a beginner can complete mathematical remediation and proofs in a fixed time without evidence.

### 3.3 Preserve SEF8 coverage and identifiers

The following is a proposed migration map, not an automatic equivalence of old and new completions:

| Existing SEF8 outcome(s) | Proposed responsibility | Identifier/evidence treatment |
| --- | --- | --- |
| `SEF8-O1`, `SEF8-O2` — number sense and pre-algebra | New SEF11 mathematical bridge | New `SEF11-O*` IDs; old SEF8 IDs preserved in historical revisions, not reused for different outcomes |
| `SEF8-O4`, `SEF8-O5` — logic, counting, proofs and graphs | New SEF11 discrete foundation | New `SEF11-O*` IDs; corresponding SEF8 outcomes retired prospectively |
| `SEF8-O13` — growth and recurrence reasoning | SEF11 foundation, applied again in SEF4 | New `SEF11-O*` ID; SEF4 maintains its algorithm-specific evaluation |
| `SEF8-O3` — exact/approximate Python verification | Retain in re-scoped SEF8; a separate simple checking capability may exist in SEF11 | Preserve only if outcome meaning and criteria remain substantively unchanged |
| `SEF8-O6`–`O12`, `O14`–`O18` | Re-scoped SEF8 numerical/statistical/AI foundation | Preserve existing IDs when the evaluated competency stays the same; add new IDs for genuinely new requirements |
| `SEF8-AS1`, `SEF8-AS2` | Replaced by SEF11 assessments | Do not silently reuse assessment IDs; associate historical evidence with original revision |
| `SEF8-AS3`–`AS7` | Remain in re-scoped SEF8, subject to substantive review | Retain only where the required work, criteria and evidence are equivalent |
| `SEF8-AS8` — entire old 18-outcome notebook | Replace with integrated **remaining** SEF8 mathematical competence assessment | New assessment ID if materially changed; reuse existing valid numerical artifacts by explicit reviewer mapping |

Course files MUST distinguish unchanged requirements, substantial replacements and retired IDs. A new course completion is not granted by merely copying an old assessment ID or renaming a file.

### 3.4 Catalog, prerequisites and tooling

After approval, the SEF catalog must list courses in a **valid study order**, not numeric order:

- SEF1 → SEF2.
- SEF2 → SEF3, SEF5, SEF11 and, where still appropriate, SEF9 through SEF5.
- SEF11 → SEF4 and SEF8.
- SEF3 + SEF4 + SEF5 → SEF6.
- SEF3 + SEF6 → SEF7.
- SEF1–SEF9 **and** SEF11 → SEF10.

SEF8 may proceed concurrently with SEF4 once SEF11 is complete; completion of both is required before SEF10. Optional concurrency does not waive any module's mathematical readiness.

The validator and inventory MUST derive the public expected course set and dependencies consistently with the adopted catalog. Update `scripts/check-sef-curriculum.py`, relevant unit tests, course-inventory assumptions, and any validators that hardcode exactly ten courses or numeric-only study ordering. Preserve checks for missing/orphan files, mismatched metadata, duplicate IDs, invalid prerequisites, cycles, dead links, required outcome coverage and actual draft statuses. Any new test that merely accepts an eleventh file without checking the curricular graph is insufficient.

### 3.5 Course-level follow-up requirements

The implementation must also review, in separate focused course PRs:

- **SEF1:** Physical switching versus abstract signals, representation interpretations and model limitations; add conceptual depth without inventing a full electronics prerequisite.
- **SEF2:** Classes/instances, object composition and encapsulation, basic Python type annotations and runtime/static distinctions; supply outcomes and genuine new summative evidence when needed.
- **SEF3:** Bash vs POSIX vs GNU platform dependencies, process environment and safe progression from introductory commands to robust automation.
- **SEF4:** Mathematical prerequisite and algorithmic invariant/complexity assessment alignment; retain unfamiliar test cases and independent oracles.
- **SEF5:** Design fundamentals (cohesion, coupling, interface contracts, dependency direction), professional software quality and accessible review.
- **SEF6:** Realistic study-time and C-library depth; no removal of core C memory semantics, ownership or undefined-behavior competence.
- **SEF7:** Clear SEF/SYS depth split and published destination mapping **before** any assessment removal.
- **SEF8:** Complete mathematics extraction, algebra/calculus preparation, workload calibration and retained assessment coverage.
- **SEF9:** Ethics, licensing, privacy, communication, accessibility awareness and non-AI professional obligations; provide authentic public example fixtures where the assessment requires them and proportionate documentation.
- **SEF10:** Capstone prerequisite closure and integration evidence without turning the project into an APP or SYS specialization.

A follow-up PR MUST identify any material changes to outcomes/completion requirements and map prior IDs to new ones. No new repository-wide OEE course-format, assessment-count, or lesson-schema rule is authorized by this RFC.

## 4. Alternatives considered

| Alternative | Advantages | Disadvantages | Decision |
| --- | --- | --- | --- |
| Keep ten courses and expect SEF8 alongside SEF4 | No new IDs or validator changes | Unmet proof readiness; overloaded mathematics persists | Reject |
| Move proof lessons wholly into SEF4 | No extra course; local readiness | Weakens coherent mathematical preparation and overloads algorithms | Reject |
| Require entire existing SEF8 before SEF4 | Simple graph change | Imposes probability, calculus, inference and optimization before they are needed for algorithmic proof | Reject |
| Renumber SEF4–SEF10 to insert mathematics | Numeric order matches study sequence | Breaks stable course identifiers and historical references; large downstream migration | Reject |
| **Add SEF11, split SEF8, sequence by prerequisites** | Clear competency ownership, preserves existing IDs, flexible concurrent paths | More course/catalog/tooling work and longer realistic mathematics pathway | **Propose** |

## 5. Impact assessment

### Existing courses and programs

SEF1–SEF10 remain recognizable course contracts but some receive revised outcomes, assessments, prerequisites or durations. SEF11 becomes a required additional course and changes SEF10 graduation dependencies. SEF4 proof-readiness moves to an earlier explicit prerequisite.

SYS, APP, AI and SEC programs are **not changed by this RFC alone**. Their existing dependencies and draft status remain authoritative until separately reviewed and merged. AI may rely on re-scoped SEF8 once updated; SYS must adopt any advanced material before SEF7's required coverage is reduced.

### Implementations

OEE Workspace, 0xNAND, alternate implementers and resource mappings must consume the new public catalog/versioned course definitions after they become authoritative. They may have to migrate course navigation, prerequisite checks, content mappings, assessment IDs and learner records, but must not overwrite or silently relabel existing learner evidence. Optional instruction resources and paid guidance remain non-normative.

### Evidence and status labels

This changes course-specific assessed capabilities and completion contracts, but **not** OEE's general evidence rules, completion principles or readiness-status thresholds. All affected courses retain `draft` until supporting learner completion, feedback and independent review evidence justifies their published status. A historical learner completion remains valid for its assessed revision; equivalence to a new outcome requires an explicit evidence-based decision.

### Conformance

A structurally valid new SEF course does not prove course or program conformance. Program-level review must trace every required capability to a sufficient assessment, verify new prerequisite closure, and document remaining gaps. Checks cannot infer content equivalence from shared identifiers or green results.

### Licensing and governance

No licensing, contribution-policy or steward authority change is proposed. This RFC is required because the proposal affects required course prerequisites, completion and public curriculum structure. It remains `draft` until the steward's decision is recorded. If follow-up SYS changes amount to additional normative structural decisions, submit their own RFC before implementing them.

## 6. Compatibility and transition

This is a **non-backward-compatible curricular revision**, not a repository-wide breaking change to the OEE `v0.2.0` authoring schema.

1. Record a public decision on this RFC before changing the live SEF contract.
2. Draft SEF11 and the revised SEF8 outcomes/assessments together, preserving all topic coverage and documenting source/replacement IDs.
3. Update SEF4 prerequisites and relevant assessment assumptions, then the SEF catalog and SEF10 completion dependency.
4. Update the validator, inventory assumptions and tests in the same reviewed change so an invalid intermediary catalog cannot be merged.
5. Make the remaining SEF content corrections in separate coherent PRs; coordinate any substantive SYS transfer with the actual SYS course definition.
6. Publish an explicit course-revision migration note and preserve historical evidence tied to its original revision or commit. Do not automatically mark courses or learners complete.
7. Notify downstream implementations to adopt the new catalog by version/revision, with separate data/content migration. Do not require paid content or silent backward-compatibility shims.

There is **no proposed overlap period** where contradictory catalogs both claim to be the current SEF graduation contract. A merged catalog revision is authoritative going forward; old records remain interpretable historically.

## 7. Risks and mitigations

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Existing SEF8 mathematics accidentally disappears | High | Explicit topic/outcome/assessment ownership matrix and manual review before removal |
| New SEF11 appears after capstone numerically | Medium | Show instructional order explicitly; graph-based course validation; never infer order from ID |
| Workload increases beyond learner capacity | High | Honest provisional durations, entry diagnostics, learner pilots and revision from observed effort |
| Old SEF8 learner evidence becomes misleading | High | Revision-pinned evidence, retired/replacement ID map, no automatic equivalence |
| SEF7 material moves before SYS can teach it | High | Block removal until downstream normative owner and evidence are published |
| Inconsistent Workspace or 0xNAND prerequisites | High | Coordinate explicit post-merge consumer updates and preserve historical progress |
| Assessment bureaucracy replaces learning | Medium | Reuse defensible evidence; proportionate criteria, public fixtures and independent review |
| Validator passes without genuine assessment validity | High | Automated structural checks plus manual educational evaluation and learner trials |

## 8. Validation plan

Implementation acceptance requires all of the following:

1. Every old SEF8 capability has an explicit remaining or new instructional owner; no orphaned mathematical prerequisite and no unsupported equivalence claims.
2. SEF11 and revised SEF8 have observable stable outcome IDs, mapped modules, substantive public required assessments, work, criteria, evidence and independent-study alternatives.
3. SEF4 cannot be formally attempted for completion without its published proof-readiness prerequisite or equivalent assessed competence; its graph is acyclic.
4. SEF10 requires all mandated courses, including SEF11; course metadata, catalog, validators, inventory and public cross-program references agree.
5. The original SEF8 assessment/ID history is preserved and the replacement mapping is understandable to downstream consumers.
6. The same source revision passes the outcome curriculum checker, SEF program checker, relevant unit tests and link/Markdown checks; any unrun tool is disclosed.
7. Manual reviewers inspect proof correctness, numerical/algebra readiness, independent oracles, authentic assessments, C/Unix scope and realistic project workload.
8. Novice learner pilots measure prerequisite bottlenecks, study time, confusion, assessment completion and feedback-driven corrections. No `tested` or `verified` status is claimed before meeting [Status Labels](../spec/status-labels.md).

### Delivery and verification

Normative implementation must follow **after acceptance** in separately reviewed PR(s), beginning with the SEF11/SEF8/SEF4/catalog/test migration as one coherent dependency change, then course-specific refinements. This RFC itself neither edits course definitions nor changes the current graduation contract.

## 9. Open questions

- What provisional duration ranges best reflect SEF11 bridge/remediation and SEF8 numerical mathematics? Initial estimates are not readiness claims; pilot evidence should determine the final catalog values.
- Which parts of SEF7's nonblocking TCP and signal-reliability work can safely transfer to a revised SYS course without creating an unowned capability? No transfer occurs until the SYS side has an adopted owner.

These questions do not alter the central proposed prerequisite and competency-ownership decision.

## 10. Decision

- **Decision:** Accepted — steward-approved architecture; implementation subject to review
- **Decision date:** 2026-11-16
- **Decision-maker:** 0xBUFF steward
- **Rationale:** The steward approved the RFC and its SEF11-first mathematical prerequisite architecture after review and merger of [proposal PR #80](https://github.com/0xbuffdev/open-engineering-education/pull/80). Explicit proof readiness before SEF4 and bounded numerical mathematics in SEF8 correct material learning dependencies without renumbering public course IDs.
- **Conditions:** Implement the curriculum and catalog together with automated and substantive review; preserve historical outcome/assessment evidence by revision; keep all courses `draft` without learner validation; defer any SEF7-to-SYS transfer until SYS adopts the receiving competency; preserve free independent study.
- **Initial implementation pull request:** [#83 — SEF11 mathematical progression and SEF8 curriculum migration](https://github.com/0xbuffdev/open-engineering-education/pull/83) (**merged 2026-11-16**). Subsequent focused course PRs are recorded in the closure appendix below. The preceding proposal, risk analysis and delivery plan remain **historical statements about the pre-change curriculum**; they do not override today's authoritative SEF catalog.

## 11. Implementation closure record — 2026-11-16

**Implementation disposition: course-level curriculum architecture and RFC 0003 follow-up edits complete and merged.** The original proposal sections above describe the problems, options and open questions **as they stood at acceptance**. They remain historical decision context; current adopted prerequisites, outcomes and evidence contracts are in the actual [SEF catalog](../curriculum/SEF/README.md) and course files.

| Accepted component | Merged implementation |
| --- | --- |
| Formal RFC adoption | [PR #80](https://github.com/0xbuffdev/open-engineering-education/pull/80) |
| Physical-to-logical SEF1 foundations | [PR #81](https://github.com/0xbuffdev/open-engineering-education/pull/81) |
| New SEF11, numerical SEF8, mathematical migration/catalog/validation | [PR #83](https://github.com/0xbuffdev/open-engineering-education/pull/83) |
| Python abstraction and typing in SEF2 | [PR #85](https://github.com/0xbuffdev/open-engineering-education/pull/85) |
| Shell/portability/environment in SEF3 | [PR #88](https://github.com/0xbuffdev/open-engineering-education/pull/88) |
| Cohesive design, interfaces and accessible review in SEF5 | [PR #90](https://github.com/0xbuffdev/open-engineering-education/pull/90) |
| Proof/algorithm correctness transfer in SEF4 | [PR #92](https://github.com/0xbuffdev/open-engineering-education/pull/92) |
| C11 memory and data-structure library in SEF6 | [PR #94](https://github.com/0xbuffdev/open-engineering-education/pull/94) |
| Unix/POSIX foundations and non-normative SYS destination mapping in SEF7 | [PR #96](https://github.com/0xbuffdev/open-engineering-education/pull/96) |
| Non-AI ethics, rights, privacy and accessibility in SEF9, including the original public examples | [PR #98](https://github.com/0xbuffdev/open-engineering-education/pull/98) |
| Ten-prerequisite closure, integrated capstone and responsible release in SEF10 | [PR #101](https://github.com/0xbuffdev/open-engineering-education/pull/101) |

The SEF9 example files introduced during the original implementation are no longer part of the current repository. [SEF9](../curriculum/SEF/SEF9.md) specifies the synthetic scenarios and attributable assistant material that learners or instructors must prepare, without requiring a bundled example pack.

The [SEF catalog](../curriculum/SEF/README.md) now publishes the current course order, prerequisites, workload guidance and graduation requirements. Authentic learner completions, feedback and qualified review remain necessary for course-readiness promotion. **This closes the RFC's planned course-edit milestones, not the learner-testing or program-conformance requirements.** All eleven current SEF courses are still labelled `draft`. None is promoted to `tested` or `verified` by the merge of the course PRs, by a structural validator, or by this closure record. The original `## 9. Open questions` remain informative historically; workload calibration, learner pilots, real independent review and any future SYS transfer continue to require actual evidence and separately reviewed decisions.
