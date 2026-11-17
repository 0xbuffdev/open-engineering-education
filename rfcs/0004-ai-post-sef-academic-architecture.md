# RFC 0004: Post-SEF AI Engineering Architecture and Identity-Safe Migration

- **Status:** draft
- **Author:** 0xBUFF (proposal for steward review)
- **Created:** 2026-11-17
- **Last updated:** 2026-11-17
- **Related issue:** [#108 — AI academic architecture and staged migration](https://github.com/0xbuffdev/open-engineering-education/issues/108)
- **Affected specification version:** Existing draft v0.2.0; proposed AI curriculum contract only

## 1. Summary

Redesign AI Engineering as an advanced, independent-study-capable specialization taken after completion of all eleven [Software Engineering Foundations courses](../curriculum/SEF/README.md). Adopt a proposed 16-course core, ending in one cumulative independent AI16 project, and three optional electives. Establish observable course competencies and a valid prerequisite graph, extend rather than reteach SEF, and require targeted APP preparation only where the AI-specific work actually uses it.

The existing [AI catalog](../curriculum/AI/README.md) and [AI1–AI9](../curriculum/AI/README.md#courses) are published legacy drafts. The target numbering deliberately reassigns several existing AI codes to different capabilities. This is an **intentional prospective breaking curriculum change** requiring an explicit reviewed decision and atomic transition of conflicting course identities. Historical course revisions, citations and assessed learner evidence remain meaningful under their original contracts. No automatic equivalence, backward-format reader, or retroactive completion is proposed.

**This RFC is a draft proposal, not a replacement for the current catalog or evidence of conformance.** It changes no repository-wide OEE educational rule in [Course Format](../spec/course-format.md), [Evidence Rules](../spec/evidence-rules.md), [Conformance](../spec/conformance.md), or [Status Labels](../spec/status-labels.md).

## 2. Problem

The imported nine-course legacy curriculum compresses data, statistical learning, neural networks, transformer mechanisms, retrieval and tool use, adaptation, production operations, and governance into brief outlines with repeated module checkpoints and labs. Those older course files do not define the stable outcome IDs and substantive summative work, success criteria, and evidence needed by the current outcome-driven format. The compressed path also omits coherent ownership of classical AI search/planning, sequential decisions, visual and multimodal learning, independent AI evaluation, and several foundational steps before production systems.

The eleven-course SEF program now explicitly assesses Python, discrete reasoning, data structures and search, fundamental numerical mathematics, software engineering and testing, Unix/C foundations, professional obligations and trustworthy AI-assisted work. A replacement AI program must **assume** that assessed knowledge instead of requiring learners to repeat it.

Cross-program dependencies must be real: backend/database engineering, web transport, deployment, and low-level systems skills have distinct ownership elsewhere in OEE. A course may depend on specific APP outcomes where unavoidable; the AI program must not silently require the full APP/SYS/SEC pathways, nor claim that a learner mastered services or database engineering merely because an AI reference project supplies a scaffold.

Finally, keeping legacy course codes while assigning new meanings can make an AI9 historical capstone appear to be the new AI9 transformer course, or an AI3 historical deep-learning completion appear to be the new AI3 classical-reasoning completion. Those are not educationally equivalent. The catalog and consumers must not silently reinterpret them.

## 3. Proposed change

### 3.1 Architecture decisions

**D1 — A completed SEF program is the sole common entry foundation.** Prior completion of the eleven-course SEF program, including its SEF10 prerequisite-evidence closure, is required before AI1. SEF10 is the shared program-entry reference; later AI courses transitively inherit this requirement. A diagnostic, attendance claim or self-report does not substitute for completion evidence; any formally reviewed equivalence must demonstrate the same prerequisite capabilities rather than awarding unearned credit.

**D2 — AI teaches genuinely new AI-specific competency.** Do not repeat beginner Python, generic file or CSV handling, SEF4 graph implementations, introductory Git/CI/test methodology, SEF8 elementary calculus/probability/optimization or SEF9 professional ethics and AI-tool boundaries. Advanced numerical arrays, data provenance, AI search, likelihood/information theory, model-specific optimization, statistical generalization, AI evaluation, governance and research judgment are legitimate extensions.

**D3 — Use focused competency ownership instead of a universal course shape.** Courses must have coherent exit capabilities, variable module and lesson lengths, ordered prerequisite-valid teaching progressions, focused lesson objectives and assessment chosen for actual outcomes. Neither fixed module counts nor a test/lab per module is required. Project work may accumulate in one artifact.

**D4 — The proposed core has fifteen taught courses and one capstone project, followed by three truly optional electives.** The 16 core courses collectively cover data, mathematical modeling, classical AI, machine learning, deep learning, reinforcement learning, language, vision, generative modeling, adaptation, retrieval, agentic systems, independent evaluation, responsible engineering, operations and a defended integrated project. AI17–AI19 add audio, robotics and causal/graph specialization without gating core graduation. Course count is a provisional boundary decision justified by distinct assessed capabilities, not a new OEE rule.

**D5 — Require narrow APP courses where indispensable.** [APP4 — Databases & Data Modeling](../curriculum/APP/APP4.md) is an explicit prerequisite for AI11 and its successor-dependent core work: correct relational identity, permissions, persistent index/record joins, transactions and recovery are needed to evaluate RAG provenance and authorization. [APP1 — Web & Internet Foundations](../curriculum/APP/APP1.md) is an explicit prerequisite for AI15's service/transport security and HTTP operations. Both already require SEF10 and can be completed in parallel before their respective AI dependencies. APP3, APP6, APP7 and APP8 are **not** blanket AI core prerequisites; they offer deeper service, deployment and product-engineering specialization. Every required AI11/AI15 assessment must be scoped so that its APP assumptions match the published prerequisites. Where the system task requires full backend authoring or production deployment skills beyond APP1/APP4, either supply a pre-implemented inspectable service/runtime and assess only new AI-specific competence, or revise the prerequisite through review before adopting the course.

**D6 — Preserve independent, vendor-neutral and attainable work.** Public work and success criteria must be complete without a paid model API, hosted dataset account, proprietary grader, commercial platform or top-end GPU. Require small local models, synthetic/publicly licensed data, bounded local serving or other genuinely equivalent accessible routes. Optional large-scale training may deepen practice without silently becoming a graduation gate. No assessment may require publication of sensitive credentials, identifiable personal data or unauthorized tool/network actions.

**D7 — Preserve identities only while educational meaning is continuous.** The proposed AI1 remains recognizably a data/scientific Python course and may be reviewed as an initial standalone revision. Existing AI2–AI9 identities are substantially repurposed, split or moved. Their successor requirements receive new outcome and assessment IDs tied to the new published revision; legacy IDs and any prior learner results stay tied to the original Git revision. A matching numeric code is not an equivalence statement.

**D8 — Cut over conflicting course identities atomically.** Complete the architecture decision first, then prepare distinct, independently reviewed course changes in a controlled AI integration branch without publishing inconsistent active code meanings in main. The eventual integration-to-main change must atomically publish the accepted AI2–AI19 source definitions, authoritative program catalog, prerequisite/consumer references, and applicable validators. AI1 may merge independently before that cutover because its underlying capability is preserved. Do not create duplicate authoritative migration registries or permanent pre-publication audit files.

**D9 — Keep OEE status and conformance claims honest.** Every new/migrated file begins as draft. Structural or link checks establish neither academic quality nor learner-tested readiness; course-level and program-level conformance are separate review decisions under current OEE guidance. No normative new assessment assistance profile or accessibility rule is introduced in this RFC.

### 3.2 Proposed core catalog and direct prerequisite graph

A course identifier is a stable capability identity *within the accepted revision*, not a universal learning-step number. The proposed numeric sequence is a convenient prerequisite-valid presentation; independent study may parallelize any nondependent courses.

| Code | Proposed core capability owner | Direct prerequisites | Type |
| --- | --- | --- | --- |
| AI1 | Scientific Computing & Data Engineering for AI | SEF10 | course |
| AI2 | Mathematics of Statistical and Neural Models | AI1 | course |
| AI3 | Classical Artificial Intelligence, Search & Reasoning | AI1 | course |
| AI4 | Machine Learning & Statistical Learning Theory | AI2 | course |
| AI5 | Deep Learning & Representation Learning | AI4 | course |
| AI6 | Sequential Decision Making & Reinforcement Learning | AI3, AI5 | course |
| AI7 | Natural Language Processing & Information Retrieval | AI4 | course |
| AI8 | Computer Vision & Multimodal Learning | AI5 | course |
| AI9 | Transformers & Generative Modeling | AI5, AI7 | course |
| AI10 | Model Training, Adaptation & Optimization | AI9 | course |
| AI11 | Retrieval-Augmented AI Systems | AI7, AI9, APP4 | course |
| AI12 | Agentic AI & Tool-Using Systems | AI3, AI11 | course |
| AI13 | AI Evaluation, Testing & Reliability | AI4, AI9, AI11 | course |
| AI14 | Responsible AI, Security & Governance | AI12, AI13 | course |
| AI15 | Production AI Systems & MLOps | AI10, AI13, AI14, APP1 | course |
| AI16 | AI Engineering Capstone | AI1–AI15 | project |

All 15 taught core courses must have independent completion evidence before AI16 begins. A passed AI16 project must not grant or imply completion of missing prerequisite courses. AI16 integrates one coherent learner-owned problem and system; it must not demand separate unrelated implementations of every modality.

### 3.3 Optional elective specialization

| Code | Proposed elective | Direct prerequisites |
| --- | --- | --- |
| AI17 | Speech & Audio Intelligence | AI5, AI7, AI9 |
| AI18 | Robotics & Embodied Intelligence | AI6, AI8 |
| AI19 | Causal Inference & Graph Machine Learning | AI2, AI4, AI13 |

No elective is directly or transitively required by any core course, including AI16. Optional SYS/APP/SEC preparation for a particular ambitious elective project must not be reclassified as a program-wide core requirement.

### 3.4 Existing-to-target capability and identity map

This map documents academic subject movement **without conferring completion equivalence**. It is not a rename script or automated credit transfer.

| Published legacy source | Original capability | Proposed academic destination | Identity decision |
| --- | --- | --- | --- |
| AI1 | Data & Scientific Python | AI1 scientific data engineering | Recognizable continuing capability; substantive review of changed outcomes |
| AI2 | Machine Learning Foundations | AI4 ML/statistical learning | AI2 repurposed to advanced mathematics; old evidence remains legacy AI2 |
| AI3 | Deep Learning & Representation Learning | AI5 deep learning | AI3 repurposed to classical search/reasoning; not equivalent |
| AI4 | Transformers & Large Language Models | AI9 transformer/generative systems | AI4 repurposed to classical statistical ML; not equivalent |
| AI5 | Retrieval, Agents & Applied Generative AI | AI11 retrieval plus AI12 agents | Split into independent prerequisites and evaluations |
| AI6 | Training, Fine-Tuning & Evaluation | AI10 adaptation plus AI13 evaluation | Split training competence from independent evaluation |
| AI7 | Production AI Systems & MLOps | AI15 production AI | AI7 repurposed to NLP/IR; not equivalent |
| AI8 | Responsible AI, Safety & Governance | AI14 responsible AI | AI8 repurposed to vision/multimodal; not equivalent |
| AI9 | AI Engineering Capstone | AI16 cumulative project | AI9 becomes generative modeling; not equivalent |

New AI2, AI3, AI6, AI7, AI8, AI13 and the electives fill separately justified graduate-capability gaps. The implementation review must verify that every useful original topic is present at appropriate new depth, while avoiding duplicate introductory work. This table alone does not authorize automated remapping of learners' historical outcomes or assessment records.

### 3.5 Evidence, teaching and capstone contract

Each adopted course must provide the four required sections in order: **Overview**, **Learning outcomes**, **Modules**, **Completion requirements**. Metadata must match its active catalog row. Every required outcome uses stable AI-course IDs, and every required summative assessment has an ID and explicit **Outcomes, Work, Criteria, Evidence**. All outcomes must have substantive support: naming them in an assessment is not proof they were evaluated.

AI-specific practical evaluation should cover, where relevant:

- **Data and mathematical modeling:** independent shape/numerical oracles, derivations, data integrity, leakage, provenance, valid baselines and sampling uncertainty.
- **Learning and representation:** reproducible training, ablations, robust comparison, optimization failure diagnosis, honest generalization and independent held-out evaluation.
- **Classical and decision AI:** state-space correctness, constraints, search/planning proof limits, uncertainty and decision-policy evaluation; do not reassess generic SEF graph traversal for its own sake.
- **Language, perception and generative AI:** tokenizer/embedding and attention mechanisms, retrieval metrics, multimodal shift, memorization/contamination, and realistic failure boundaries.
- **Retrieval and agents:** record- and document-level authorization, provenance, injected instructions and untrusted retrieval, bounded tool effects, permissions and controlled recovery; do not equate a polished demo with verified security.
- **Evaluation and governance:** independently specified protocols, error taxonomies, calibration, fairness/privacy/security threats, incident response, intended-use limits and accountable no-deploy decisions.
- **AI operations:** actual local model-service behavior, model/version identity, latency and throughput under explicit workloads, release/rollback or safe forward correction, monitoring of model-specific quality and cost. A toy request handler without executable or observable serving behavior is insufficient, while APP7-scale deployment is not silently required.

Assessment evidence must distinguish expected from observed behavior and support clean-checkout reproduction or a disclosed equivalent clean state. Required independent reasoning must be reviewed beyond green automated tests. Use authentic test cases, including relevant negative, boundary, failure and unfamiliar modifications. Documentation should be proportionate rather than one full report per small lesson.

**AI16 must define a coherent project space, staged milestones, mandatory deliverables, real evaluation, a model/system incident or unseen change, independently reproducible evidence, and an accessible written/recorded/live or equivalent technical defense.** It must require verified assessed evidence for the fifteen earlier core courses, but cannot replace that evidence with attendance, a portfolio assertion or unrelated compulsory mini-projects. A reasoned and evidenced **do not deploy** conclusion is a valid engineering decision if applicable controls or measured quality fail.

### 3.6 Student and instructor contract; source ownership

The published [AI README](../curriculum/AI/README.md) will own the approved program overview, outcomes, core/elective classification, actual study order, workload estimates, prerequisite requirements and graduation route. Individual [AI course Markdown](../curriculum/AI/README.md#courses) will own each course's outcomes, lessons and assessments. No separate editable curriculum registry or duplicate assessment brief is created merely to house a migration plan.

[OEE Workspace](https://github.com/0xbuffdev/oee-workspace), independent instructors and optional paid implementations may add exercises or change delivery mechanisms but may not silently weaken public required outcomes or evidence. Optional book mapping, hosted services and instructional prose belong outside the OEE course contract as appropriate.

## 4. Alternatives considered

| Alternative | Advantage | Disadvantage | Recommendation |
| --- | --- | --- | --- |
| Retain the original nine courses and merely reformat them | Small diff, no code reassignment | Preserves inadequate and overloaded subject boundaries; leaves essential independent capabilities unspecified | Reject |
| Preserve all legacy IDs and append new courses in irregular study order | Strongest historic identifier continuity; mirrors SEF/APP practice | Conflicts with the explicitly proposed pre-migration numbered academic design, complicates distinct course boundaries and public navigation | Viable fallback if identifier stability is judged more important |
| Replace legacy AI2–AI9 one by one directly on main | Small individual PRs | Creates temporary, contradictory active program meaning and misleading prerequisite/learner evidence references | Reject |
| Require full APP9/APP7 or a broad SYS program before entering AI | Existing production competence | Unnecessary education load; repeats other programs; makes AI access less independent | Reject unless individual outcomes demonstrate necessity |
| Keep AI2–AI9 old until new replacements are separately reviewed on a staged integration branch, then switch together | Maintains reviewable changes and one coherent public cutover | Requires coordination and an integration review | Preferred, subject to steward approval |

## 5. Impact assessment

### Existing courses and programs

AI1 can migrate independently as a continuing scientific-data course; [AI1 proposal PR #109](https://github.com/0xbuffdev/open-engineering-education/pull/109) is separately reviewable. This RFC neither approves that PR nor changes its acceptance criteria. The incompatible AI2–AI9 reassignments, new AI10–AI19, program graduation rule, catalog and source references must be reviewed and published together as a consistent active state. SEF, APP, SYS and SEC course requirements are unchanged by this proposal.

### Implementations and source consumers

Any references to an AI code alone are insufficient during this breaking transition. Resource maps, exports, cached links, 0xNAND/course consumers and OEE Workspace must use an actual source path **and full Git source commit** or another published revision-precise reference as required by their own contracts; they must audit old-to-new mapping rather than silently repin by code. Check the public content repository's AI mappings and linked course identifiers before switching the active catalog. Historic release tags and learner-owned evidence are not rewritten. No backward-format reader is required.

### Evidence, status and conformance

No changes to universal status thresholds or evidence rules. New requirements must be evaluated against their published revision. Existing untested legacy drafts do not become v0.2.0 merely by renaming or inclusion. Final program conformance requires a separately documented review of all required courses and graph integrity; successful source validators alone are insufficient.

### Licensing and governance

No licensing or attribution change. The public RFC process and steward decision govern whether this proposed curriculum architecture may replace the current catalog. No context planning document, private roadmap or partial implementation PR can substitute for that decision.

## 6. Compatibility and transition

**Prospective breaking curriculum revision.** Review acceptance of this RFC before the conflicting AI2–AI9 source definitions are adopted. After approval:

1. Retain the original nine-course source and evidence under their historical Git revisions; no automatic credit equivalence or global code redirects.
2. Merge AI1 independently if its separately reviewed continuity and requirements are accepted.
3. Prepare individually reviewable AI2–AI19 course changes against a designated **AI integration branch**, not the public active main catalog. The integration branch is nonauthoritative until a reviewed adoption PR merges.
4. Audit all nineteen source files, active catalog, cross-course prerequisite graph, core/elective closure, code identity mapping, linked public references, project defense, workload and actual assessment quality.
5. Publish a **single atomic catalog and source cutover to main** when the entire accepted core is ready; optional electives may be adopted after the core only if their new IDs and catalog consistency remain unambiguous. Prefer publishing all reviewed target files together when feasible.
6. Notify source consumers and require validated, deliberate resource-map updates pinned to the adopted source commit; preserve historic learner records.
7. Regenerate derived curriculum inventory and run format, link, documentation and structural regression checks. Keep AI sources at draft until learner evidence supports a status change.

An architecture-only PR must not change the live learner catalog or assert that migration is complete.

## 7. Risks and mitigations

| Risk | Consequence | Mitigation |
| --- | --- | --- |
| Reusing AI2–AI9 for different outcomes | False learner completion or broken references | Explicit historic-to-new mapping, exact-source evidence, atomic catalog transition |
| Hidden APP/SYS prerequisites | Learner unable to complete required assessment from declared entry | Outcome-level prerequisite audit and a genuinely runnable local reference fixture |
| Repeat SEF instruction | Excessive workload and redundant assessment | Each course specifies the SEF competency it extends and tests only new AI work |
| Hardware or paid access dependency | Public independent completion becomes infeasible | Small CPU-capable reproducible baseline or truly equivalent public assessment route |
| Uniform module/lab counts | Shallow or artificial teaching | Course-specific outcome-first lesson and evidence design |
| Model-demo bias | Impressive output mistaken for dependable competency | Fixed baselines, negative cases, independent evaluation, reasoning defense and uncertainty |
| Fragile multi-branch migration | Misleading temporary active prerequisite graph | Isolated integration branch, code review per course, one reviewed main cutover |
| Overpromised maturity | Unjustified conformance or educational validation claim | Draft status, real learner/reviewer checks, accurate program/source scope |

## 8. Validation plan

**Architecture acceptance:** A reviewer should verify (a) every essential AI program competency has a primary course owner, (b) a valid topological prerequisite order without an elective-to-core path, (c) complete SEF10 entry closure, (d) APP4 and APP1 necessity and accurate transitive closure, (e) original AI coverage preservation/extension, (f) the identity-breaking map and consumer migration are safe, and (g) core versus elective placement is educationally defensible.

**Per-course implementation:** Review coherent outcome descriptions, mechanisms and nonrepetitive SEF transfer, module/outcome links, numbered lessons, published summative Work/Criteria/Evidence, negative cases and bounded execution. Use the OEE outcome checker on each new source; check the authoritative catalog row and prerequisite links. A parser's pass is a *structural result*, not pedagogical validation.

**Program acceptance:** Validate all active course files and paths, duplicate IDs, assessment-to-outcome mapping, published course statuses, active links, prerequisite order and cycles, capstone required closure and technical defense. Run available Python unit tests, program/inventory checks, Markdown lint, documentation and local-link checks, and review the resulting source diff. Record explicitly if a check is unavailable. Independently inspect whether the evidence actually establishes each claimed outcome. Request learner pilots and qualified review before any tested/verified promotion.

**Delivery:** This RFC and its index entry are proposal-only. A steward-recorded acceptance must precede conflicting course/source cutover. Focused course PRs and the final integration PR must cite the adopted decision and public review evidence.

## 9. Open questions

1. Does the steward approve a prospective change of legacy AI2–AI9 code meanings for the sake of numeric study order, or prefer immutable original code identities with a nonnumeric catalog order? This choice must be settled **before** replacing AI2–AI9.
2. Do the proposed core requirements in AI6 (reinforcement learning) and AI8 (vision/multimodal) match the intended AI graduate exit capability, or should either become elective with explicit revised program outcomes?
3. Does any required AI11/AI15 assessment currently assume backend application construction or cloud operations beyond APP4/APP1? Identify and adjust the task/environment or prerequisite before acceptance.
4. Which downstream content and workspace references still depend on legacy AI course codes and module indices? The cutover cannot silently reinterpret them.

## 10. Decision

- **Decision:** Pending steward review
- **Decision date:** pending
- **Decision-maker:** OEE steward
- **Rationale:** Pending resolution of course identity, curriculum boundary, assessed APP readiness and safe adoption.
- **Conditions:** Pending academic and source-consumer review.
- **Implementation pull request:** pending; [AI1 PR #109](https://github.com/0xbuffdev/open-engineering-education/pull/109) is independently in review.
