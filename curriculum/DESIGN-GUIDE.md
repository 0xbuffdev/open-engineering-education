# Curriculum Design Guide

This guide explains how to **research, design, review, and revise** Open Engineering Education (OEE) programs, courses, modules, lessons, practice, and assessments. Use it across the published [SEF](SEF/README.md), [APP](APP/README.md), [SYS](SYS/README.md), [AI](AI/README.md), and [SEC](SEC/README.md) programs.

**Status:** Non-normative editorial guidance. Binding educational requirements remain in [Course Format](../spec/course-format.md), [Evidence Rules](../spec/evidence-rules.md), [Status Labels](../spec/status-labels.md), and [Conformance](../spec/conformance.md). This is **not** a separate authoring specification, required document template, course-completion rubric, or new conformance test. It establishes no fixed counts of courses, modules, lessons, activities, assessments, or weeks. Where this guide and the OEE specification disagree, the specification takes precedence.

**Central principle:** Research the capabilities a learner must demonstrate; establish the knowledge, reasoning, and experience needed to achieve them; then derive the appropriate course architecture. Never begin by choosing how many modules or lessons to produce.

## 1. Use the seven-stage curriculum-design workflow

The same workflow applies to new programs and courses, substantive revisions, and reviews of published curricula.

1. **Establish the subject boundary.** Research the discipline, relevant primary technical documentation, appropriate academic syllabi and curriculum standards, representative engineering practice, and skills already taught by prerequisites. Define what belongs in the subject and what does not.
2. **Revalidate course learning outcomes.** Specify observable exit capabilities at the appropriate depth. Retain existing stable identifiers when their competency meaning is unchanged; do not design toward a preferred outcome count.
3. **Derive module responsibilities.** Group the mechanisms and decisions necessary for those outcomes into cohesive stages, following real conceptual and prerequisite dependencies. Do not start from a target number of modules.
4. **Design individual lessons.** Give each instructional unit one primary learning objective, the necessary mechanisms, an observation or application, and useful feedback. Split or combine lessons based on cognitive and instructional coherence.
5. **Select proportional practice and assessment.** Place formative work where it improves understanding. Choose summative work that actually measures required outcomes and publishes clear success criteria and evidence, without duplicate submissions.
6. **Review against neighboring courses.** Remove needless repetition, prerequisite jumps, hidden tool or language assumptions, unjustified vendor restrictions, and unsupported claims. Protect a clear foundational-to-advanced progression.
7. **Recalculate workload and validate.** Estimate time from actual learner activities, experiments, debugging, assessments, and iteration. Review technical accuracy, curriculum alignment, course/catalog consistency, accessibility, reproducibility, and change impact.

These stages are **iterative**, not a rigid waterfall. If the designed assessments cannot validly evaluate an outcome, revisit the outcome. If a module assumes skills never previously taught, revise the prerequisites or the progression. If workload is unrealistic, correct the scope or learning sequence rather than deleting essential concepts to satisfy a timetable.

A temporary working research map or editorial checklist can support the process. It does not become a mandatory public course artifact or a parallel source of curricular authority.

## 2. Research before designing the outline

A curriculum is not made academically sound by increasing its length or naming more advanced topics. For each substantial course or program review, investigate at least these **types of evidence**, selecting sources relevant to the subject:

| Evidence | What to learn from it | What not to assume |
| --- | --- | --- |
| Primary standards and official documentation | Mechanisms, supported behavior, formal models, constraints, version-dependent details | One vendor's tutorial defines the discipline |
| Respected university and disciplinary curricula | Foundational concepts, prerequisite expectations, levels of rigor, and possible coverage gaps | Another university's course packaging is the only correct packaging |
| Discipline-wide guidance (for example, CS2023) | Knowledge areas, competencies, relationships, and representative educational scope | Every knowledge unit requires its own OEE module |
| Reproducible engineering practice | Real workflows, errors, incident patterns, trade-offs, and skills needed in unfamiliar situations | Popularity, benchmarks, or anecdote prove correctness |
| Existing OEE catalogs and courses | Competency ownership, already-assessed prerequisites, graduate capability, and progression | A similar lesson title means the same depth was taught |
| Learner and environment constraints | Setup cost, tooling access, hardware, safe experiments, accessibility, and realistic independent-study effort | Every learner has paid infrastructure, specialized equipment, or an instructor |

**Source evaluation:** Prefer authoritative and current sources for changing technologies. Check publication or specification versions, distinguish standard behavior from implementation-specific behavior, and identify where evidence is provisional, disputed, historical, or context-dependent. Compare multiple credible perspectives for substantial design decisions. Do not invent citations, claimed experiments, learner feedback, formal accreditation, or consensus.

**Research questions:**

- What is the discipline's indispensable conceptual and mathematical foundation?
- What can an appropriately prepared graduate actually explain, predict, implement, diagnose, evaluate, or defend?
- Which mechanisms matter independently of specific tools, products, or languages?
- Which capabilities are fundamental, applied, advanced, or elective?
- What failures, unsafe assumptions, or limitations reveal shallow understanding?
- What do the prerequisites already teach, and what is missing from the actual prerequisite closure?
- Which representative tasks could be demonstrated with accessible, reproducible resources?
- What knowledge is evolving, and what confidence should an educator attach to the selected source?

Make a **working competency coverage map** before drafting or removing lessons. The map can link capability, primary source or rationale, first course owner, prerequisites, expected depth, evidence of mastery, and appropriate follow-on specialization. Use it to find omissions and duplication, not to generate a mandatory document for every learner.

Research informs the public curriculum. It must not silently become a required paid reading list or hidden assessment prerequisite.

For a substantial review, record the full OEE commit SHA (or an immutable curriculum release and its source revision), repository-relative file path, relevant stable outcome or assessment ID where available, and heading or line range. For external research, identify the issuing body, edition or version, relevant section, and persistent link; for evolving online documentation, record the inspected revision or access date. Explain why the cited material applies to the actual OEE claim, rather than treating a citation as a requirement. A pinned source review remains reproducible even if `main` changes; recheck affected findings against the proposed merge base before editing.

## 3. Define program architecture and competency ownership

A program should develop recognizable graduate capabilities through a sequence of distinct, complementary courses. Begin with those capabilities and their dependencies; choose course names and ordering afterward.

A useful working matrix is:

| Capability | First substantial owner | Preparation needed | Evidence of understanding | Later application |
| --- | --- | --- | --- | --- |
| Explain DNS resolution and failure | Web foundations | Addressing and networking concepts | Trace an actual or supplied resolution failure | Deployment and operations |
| Reason about shared mutable state | Appropriate programming/systems foundations | Control flow and state | Predict and reproduce a race | Database and distributed correctness |
| Evaluate model failure modes | Appropriate AI/data course | Statistics and evaluation concepts | Analyze held-out errors and limitations | Deployment and monitoring |
| Diagnose authorization errors | Appropriate application/security owner | Identity and trust boundaries | Show rejected access and unaffected authoritative state | Security assurance and incident response |

These are **illustrative** rows, not newly adopted OEE course assignments.

Review the **entire prerequisite graph**, including transitive preparation. A course prerequisite should supply knowledge actually needed before starting, not merely be numerically earlier or fashionable. Do not introduce an elective as a hidden core-graduation condition. When competence is available through a different program or equivalent preparation, document that boundary appropriately without inventing a current course code.

### Test prerequisite closure against real work

For each significant entry assumption, identify the specific earlier outcome and evidence that establish it, not just a prerequisite course title. Trace direct and transitive edges, including branches that can run in parallel. Inspect the actual tasks, environment and language or framework assumptions before adding or removing a prerequisite.

| Question | Possible editorial response |
| --- | --- |
| Is the required competence already assessed in the closure? | Reference the owning course; avoid redundant edges and introductory work. |
| Is the missing mechanism small enough to teach in the dependent course? | Design a bounded bridge with practice and a check of readiness before the dependent work. |
| Is substantial prior competence absent? | Investigate an appropriate prerequisite or governed equivalent preparation; check downstream impact. |
| Does a reference technology require skills not needed by the underlying outcome? | Teach the necessary setup or offer an equivalent accessible implementation path, where the course permits it. |

A diagnostic can identify preparation needs; it does not establish mastery merely by being administered. Do not use an elective, a private resource or an unassessed assumption as a hidden graduation condition. A proposed change to binding requirements follows the existing governance process.

### Distribute cross-cutting competencies deliberately

Some capabilities, including system design, security, verification and professional practice, develop across several courses. Locate the first substantial teaching and assessment, identify its later applications, and specify the new depth each later owner contributes. Use actual outcome and assessment references in working review notes; avoid a duplicate canonical competency registry.

For system design, for example, distinguish small-program decomposition and interface invariants from application integration, then from production-scale capacity, consistency, failure recovery and cost, and finally from domain-specific assurance. Architecture diagrams and decision records can support evidence, but are not substitutes for reasoning, observed behavior or verification. A justified simple architecture should not lose credit merely because it lacks distributed components. This progression is illustrative; derive ownership from actual course requirements.

### Distinguish repetition from progression

Concepts may legitimately recur when the next course makes a **new claim of competence**:

- **Foundation:** Explain the mechanism and its key assumptions.
- **Application:** Use the mechanism responsibly in a different engineering task.
- **Specialization:** Analyze a subtle failure, scale limit, security property, or competing technique.
- **Integration:** Select and defend an approach in an unfamiliar system or project.

Ask what is genuinely *new* the second time. A brief recall or link may be appropriate; repeating the same introduction, example, and assessment is usually not. Conversely, deleting every recurrence would prevent valuable transfer. Protect critical foundations without turning every advanced course into an introductory one.

### Cross-program boundaries

All five programs should use the **same quality of research and review**, not the same course shape.

- **SEF:** Transferable computing, mathematical and programming foundations. Subsequent programs should rely on capabilities it actually demonstrates, not merely on its course titles.
- **APP:** Application, integration, delivery, operating and specialization capabilities. Systems-level Rust ownership and C/Rust comparison should not be re-taught just to fill an APP interoperability elective.
- **SYS:** Investigate its own hardware-near, language/runtime, operating-system, concurrency, memory, performance, and resource boundaries before selecting courses; do not inherit APP's structure.
- **AI:** Determine which mathematical, statistical, data, modeling, evaluation and deployment capabilities belong at each level. Map prerequisites against what SEF and APP **actually** provide rather than assuming every AI learner starts from zero.
- **SEC:** Cover security-specific reasoning, threats, controls, validation, safe experimentation, privacy and incident work while relying transparently on software and systems preparation already acquired.

These descriptions identify **review concerns**, not new authoritative course lists, approved prerequisite changes, or a universal sequence among programs. Refer to each program's current catalog for its actual published scope.

## 4. Define coherent course boundaries and outcomes

Each taught course should develop a recognizable, substantial exit capability. A project course may integrate multiple prior capabilities into a coherent product, investigation, or engineering defense. Electives should deepen competence without being necessary for unrelated core graduation.

**Too broad:** Unrelated skill sets with different prerequisite paths, many detached topics, and an assessment that cannot convincingly evaluate the whole scope.

**Artificially fragmented:** Several course boundaries around one mechanism, duplicated onboarding, or multiple submissions for a single authentic performance.

Review the intended boundary:

1. Can the main exit competence be expressed without listing dozens of unrelated technologies?
2. Are the outcomes mutually reinforcing and appropriate for the same prerequisite level?
3. Does another course already own the foundational treatment?
4. What new mechanism or failure mode makes this course different?
5. Would splitting, merging, or reordering genuinely improve the learning pathway?
6. Does the course depend on a single vendor even when the competency is portable?

### Decide what belongs in the common core

Separate competencies needed by every graduate of a named program from optional specialist depth. A topic's importance to one professional role does not by itself make it a universal prerequisite for all roles. Compare current graduate claims, prerequisite closure, alternative pathways, assessment effort and the cost of losing a capability before changing classification or graduation scope.

A useful classification exercise begins with representative roles and their actual engineering tasks, using disciplinary competency frameworks and primary technical sources rather than job-title popularity. Compare those tasks against the published program's graduate claims and assessed prerequisite closure. For each capability, distinguish:

| Candidate classification | Decision question |
| --- | --- |
| Shared program core | Would a graduate of the published program be unable to substantiate a common graduate claim without this capability? |
| Role-specific or elective depth | Does it primarily support a particular specialization while the common graduate claims remain demonstrable without it? |
| Prior or equivalent preparation | Is it already established elsewhere, or can an existing permitted preparation path supply it without an unassessed dependency? |
| Research or expansion candidate | Is the value, level, ownership or feasibility still unestablished? |

For a candidate elective, trace every required successor and capstone through the graph to ensure the proposed classification does not create an indirect mandatory elective. Compare the actual assessed capabilities of alternative routes, not just their titles, time estimates or popularity. Role profiles are research aids, not new OEE credentials or a second catalog; classification changes remain subject to the published curriculum and governance.

If investigating a narrower or alternative pathway, identify the competencies it retains, omits or moves; the claims graduates could honestly make; and impacts on current learner evidence, dependent courses and implementation consumers. Treat intermediate milestones as descriptions of evidenced competence, not automatic credentials. Do not adopt new graduation conditions through this guide; use the existing [RFC process](../rfcs/README.md) when required.

### Write observable learning outcomes

Outcomes should specify a performance and useful context: trace, explain, calculate, implement, verify, compare, investigate, justify, or defend. Replace vague statements such as "know X" with something a reviewer could recognize in a solution, demonstration, or explanation.

Check each outcome for **observability, importance, distinctness, depth, prerequisite readiness, and assessability**. Outcomes should not be artificially multiplied to fill a standard count, nor combined so broadly that meaningful evaluation becomes impossible.

Where OEE has already published stable outcome identifiers, retain them for genuine continuity. A material change in the expected capability requires explicit treatment under the existing [Course Format](../spec/course-format.md); reusing an old ID must not silently misrepresent a new requirement. The same applies to changed assessment expectations.

An authentic exit task is often useful for testing the course boundary before modules are written: if it cannot demonstrate the proposed outcomes without a collection of unrelated exercises, reconsider the scope.

## 5. Derive modules from conceptual cohesion

A module is a meaningful stage in developing the course capability. Group concepts when they explain the **same mechanism**, depend on one another, or jointly support an engineering decision. Separate them when the learner must acquire a genuinely different model, prerequisite, or independent capability.

**Do not choose a preferred module count or lessons-per-module range.** A course introduction may be brief; a transaction, operating-system scheduler, statistical inference, or security boundary may require greater depth. They should not be forced into equal-sized outlines.

Split a module if:

- It contains two independent primary competencies.
- The second portion requires materially different preparation.
- A distinct learning, practice, or feedback stage would improve comprehension.
- The module title no longer describes the contents.

Keep it together if:

- Splitting would disconnect a mechanism from its essential assumptions or failure cases.
- Several topics form one causal model or engineering decision.
- A unified experiment makes relationships clearer.
- The apparent length comes from genuinely necessary depth rather than unrelated scope.

Module titles should express a real capability or system, not "Part Two", "Advanced Topics", or a convenient difficulty label.

### Investigate numerical and template patterns

Repeated counts are **diagnostic signals**, not automatic violations. When nearly every module has eight or nine lessons, every module ends with a formative task, or every course ends in the same final lab, inspect the learning objectives before changing the source.

- Can two neighboring lessons be combined because they support one objective?
- Does a repeated "introduction" merely recap a prerequisite?
- Is a formative exercise better inside a lesson or cumulative project milestone?
- Does a large lesson contain distinct objectives that merit separation?
- Is the final integration stage assessing previously developed work or re-teaching the entire course?

**Do not "fix" an arbitrary uniform count by creating artificial numerical variety.** Reorganize only when the conceptual and instructional evidence supports a change. Programmatically flagging repetitive counts may help human review but cannot serve as a course-design rule.

## 6. Design lessons around one primary learning objective

A *topic* identifies an area (such as DNS). A *concept* identifies an idea (such as recursive resolution). A *lesson* is a focused instructional unit whose primary objective can be explained, observed, practiced, and checked.

Before accepting a lesson, ask:

1. **Purpose:** What should the learner be able to do or reason about afterward?
2. **Mechanism:** Which definitions, relationships, invariants, assumptions, constraints, or failure modes are necessary?
3. **Observation/application:** What concrete trace, worked example, comparison, proof, simulation, or experiment makes the mechanism tangible?
4. **Feedback:** What misconception, negative case, prediction, or correction would reveal incomplete understanding?

These are authoring **questions**, not four mandatory lesson headings. A lesson may contain several closely related concepts. It does not need a separate lab, quiz, worksheet, or retained evidence record merely because it is a lesson.

### Example: choosing a useful DNS lesson boundary

| Unit | Name | Primary instructional aim |
| --- | --- | --- |
| Module | Domain Names and DNS | Explain name ownership, lookup and failures |
| Lesson | Domain Names | Explain naming structure and purpose |
| Lesson | Domain Registration | Trace registration and delegation responsibilities |
| Lesson | DNS Records | Interpret records relevant to an observed resolution |
| Lesson | DNS Resolution | Trace resolver, authoritative server, referrals and response |
| Lesson | Caching and Failures | Diagnose stale results, TTL behavior and resolution errors |

The "DNS Resolution" lesson can contain several mechanisms that belong together. Splitting every named component into a separate lesson would fragment the explanation. Conversely, registration and cache-related failure analysis can justify separate lessons because their primary objectives differ.

Prefer short, descriptive titles that distinguish neighboring lessons. Two to five words often work well, but this is **only a readability heuristic**, not a quota or a reason to omit necessary precision. Avoid decorative or repeated "Introduction to..." labels. A concise title is not permission to teach the subject superficially.

## 7. Sequence learning for understanding and transfer

The sequence must respect **prerequisite knowledge**, support progressive reasoning, and give learners opportunities to apply knowledge under changing conditions.

A useful design may move through scope and motivation, foundational mechanism, guided observation, independent application, failure diagnosis, and integration. This is **not** a six-stage template for every course or module. Different subjects require different teaching sequences:

- A mathematical module may move from definitions and proofs to counterexamples and derivations.
- An operating-system module may use scheduling traces, resource models, controlled experiments and failure cases.
- An AI module may use a data hypothesis, evaluation design, baseline model, errors and limitations.
- A security module may begin with a threat, then establish the mechanism and test safe countermeasures.
- A capstone may follow cumulative product milestones, independent evaluation, revision and defense rather than repeating previous courses.

Use worked examples and feedback to support learning, then gradually reduce scaffolding. An unfamiliar problem is particularly useful where a course claims transferable reasoning or independent engineering judgment.

Do not create a separate "formative lesson" at the end of every module by habit. Feedback might be embedded in a worked example, an observation task, a failure investigation, a revision, or a project checkpoint. It need not always produce permanent evidence.

## 8. Align practice, assessment, and outcome evidence

Start by asking: **What would convince an independent reviewer that the learner has achieved this outcome?** Then ensure lessons and formative practice prepare the learner for that performance.

| Claimed capability | Suitable evidence or assessment form |
| --- | --- |
| Explain a mechanism | Causal explanation, trace, prediction, counterexample |
| Apply mathematical reasoning | Derivation, calculation, justification of assumptions |
| Implement a system | Behavior and negative tests, inspected artifact, rationale |
| Conduct an experiment | Reproducible method, measurements, uncertainty, interpretation |
| Evaluate security or safety | Threat model, denied/allowed behavior, safe failure analysis |
| Make an architecture decision | Alternatives, constraints, measured consequences, defended trade-offs |
| Integrate a product | Cumulative deliverables, independent reproduction, technical defense |

Choose formative activities for **feedback**; choose summative assessments for **decisions about required outcomes**. One authentic assessment may support several outcomes if its criteria genuinely distinguish competence in each. Software tests run inside an assessed lab are not automatically additional learner knowledge tests.

Challenge each assessment:

- Could a learner pass by memorizing definitions or reproducing a tutorial without understanding?
- Are the test oracles independent, or do they merely restate the implementation's assumptions?
- Are important invalid, hostile, partial-failure or limitation cases missing?
- Is the required evidence proportional to what is claimed?
- Is some artifact submitted repeatedly despite establishing no new outcome?
- Can an independent learner understand and reproduce the required work without hidden tools or a paid provider?

The binding rules for assessed work and evidence remain in [Course Format](../spec/course-format.md) and [Evidence Rules](../spec/evidence-rules.md). This guide does not impose a test-then-lab sequence or a universal final integration exercise.

### Sample assessment validity before expanding a review

A source audit can start by sampling risk-bearing assessments: first exposure to a prerequisite, a cross-cutting capability, an integration or capstone task, a safety-critical or expensive exercise, or a repeated assessment pattern. Record the reason for selecting the sample, the source revision, the outcome and assessment identifiers, and the portion of the program not yet inspected. Choose a different sample when the risk differs; no fixed sample size or percentage is implied.

For a sampled assessment, trace the outcome through the learning sequence to the required work, criteria and evidence. Try a plausible acceptable response and a counterexample that meets superficial instructions but lacks the intended competence. Where executable work is involved, inspect or attempt a clean-state reproduction and relevant negative cases when feasible. Report the observed result, not an assumed one. A criterion that accepts the counterexample may reveal a confirmed assessment defect; an unexecuted example or an uninspected course remains an open question. Expand the review when a repeated failure pattern or important dependency warrants it. Sampling supports prioritization, not a declaration that every unsampled assessment is valid or a relaxation of the requirement to demonstrate every required outcome.

### Distinguish individual performance from collaborative performance

An individual Git exercise, a simulated review and a genuine contribution to shared work can teach different things. Where an outcome claims collaborative engineering, inspect whether evidence actually shows independent contributions, negotiated interfaces or decisions, review and integration. A role-play or self-review may support learning but should not be represented as observed team performance or independent endorsement.

Consider accessible ways for independent learners to collaborate, such as bounded peer exercises or authorized open-source contributions, without imposing a particular hosting platform. Where only individual or simulated work is feasible, state the limits of the evidence and align the claim to the published outcome. Individual technical ownership remains assessable even when work is shared.

## 9. Recalculate workload after designing the real work

Estimate time from **conceptual study, worked reasoning, setup, practice, experimentation, debugging, assessment, evidence preparation, feedback and revision**. A short lesson list may demand substantial time, while a long list of terminology items may be shallow.

Make the assumptions explicit: prior knowledge, weekly focused hours, access to hardware or emulators, tool installation, mathematical maturity, realistic experiment duration, and expected iterations. Distinguish prerequisite gaps from time required to learn the current course.

If the total looks excessive, inspect unrelated scope, repeated onboarding, duplicated submissions, needless technology requirements and artificial course boundaries **before removing important mechanisms**. If it looks unrealistically short, look for unspoken prerequisites and tasks whose difficulty was underestimated.

A lightweight workload sample can trace a representative learner path through an actual lesson, setup, practice, required assessment and revision. Estimate effort per activity with an explicit range and preparation assumptions; separate active work, elapsed waiting time and optional enrichment. Where feasible, perform a clean-environment setup or task walkthrough and record elapsed time as an editorial or reviewer observation, not a novice completion time. Compare a familiar task with one that has new concepts, uncertain tooling or substantial debugging. When sampling, disclose unexamined activities, possible shared setup and the uncertainty of extrapolating to the whole course; do not multiply a convenient average by a lesson count. Compare the resulting estimate against the published course duration and any declared weekly study commitment without inventing one.

Duration is provisional until learner evidence supports calibration. A repository check, author's intuition, or another university's credit timetable is not proof that OEE learners can complete the work at the stated pace.

For a program-wide review, distinguish additive course effort from the prerequisite-constrained calendar sequence. Check catalog arithmetic, concurrent branches, competing weekly workloads, repeated setup and assessment effort, and the time to intermediate competence. Compare alternative paths against the actual capabilities they preserve; parallel scheduling does not remove work. Record assumed hours separately from observed learner timings, and revise estimates when genuine feedback warrants it.

## 10. Build accessibility and independent study into the curriculum

The public curriculum should be understandable without a commercial service, a particular instructor, or undisclosed paid books. Identify essential environment requirements, free reproducible alternatives where reasonable, assumptions about devices and operating systems, and limitations of a simulation versus real-world behavior.

Review whether required work can be understood and demonstrated using accessible explanations, diagrams or equivalent descriptions, keyboard/assistive navigation where relevant, inspectable examples, and appropriate alternative forms of expression that preserve the same competency. Do not equate accessibility with removing important reasoning or safety criteria.

OEE publishes competencies and assessment expectations. OEE Workspace, 0xNAND and other implementations may add teaching, guidance, practice and feedback without becoming the only place where the public completion contract can be discovered. This guide is about curriculum **design**, not a platform-specific lesson-content schema.

### Inspect the availability of required assessment resources

Where an assessment depends on a supplied fixture, dataset, recorded model proposal, provider trace, reviewer-selected case or reference service, inspect how a learner can obtain it legitimately. Check provenance and license, version, setup and reset instructions, accessible environment and independent observation of required behavior. Distinguish a resource actually inspected or reproduced from one merely described in a course. A fixture can be intentionally defective or synthetic without being fabricated evidence of real external behavior.

Start from the canonical course and any explicitly linked public assessment brief, as an independent learner would. Follow the actual acquisition route rather than searching a private author workspace: find the artifact or generation procedure, check the declared version or seed when relevant, access it without a commercial account, and attempt setup or reproduction if possible. Distinguish public availability, discoverability, license permission, environmental feasibility and successful reproduction. An accessible equivalent can be a public synthetic fixture, a documented learner-generated case or a permitted alternative with the same evaluation criteria; a private item bank need not expose its answers or exact hidden variants. A missing public path is a confirmed access defect only when the assessment genuinely requires that resource and no usable equivalent path is published. Otherwise record the unresolved question and what was inspected.

If a resource is inaccessible, investigate a free reproducible alternative, a public resource maintained at an appropriate implementation boundary, or a revision that preserves the competency. Record what has not been executed and avoid implying that a simulation proves production behavior. Review the practical route to independent feedback and assessment, not just the existence of an instruction to seek a reviewer. This guidance does not require moving all teaching materials into the specification repository.

## 11. Review a whole program, not just one course file

A course can look comprehensive in isolation while creating gaps or redundant teaching in the program. Review across the entire published prerequisite graph.

| Program-wide question | What to inspect |
| --- | --- |
| Coverage | Does every essential graduate capability have a deliberate substantial owner? |
| Dependency | Does each course inherit the concepts its actual prerequisites teach? |
| Depth | Where is a mechanism first taught, later applied, and finally specialized? |
| Duplication | Are the same explanations or assessments repeated without a new competency? |
| Sequence | Does every course progress toward independent transfer rather than only tutorial following? |
| Access | Are tools, environments, mathematical preparation and experiment constraints disclosed? |
| Scope | Are electives truly optional, and are project courses integrations rather than repetitions? |
| Coherence | Are course outcomes, modules, lessons, practice, and required evidence mutually aligned? |

Across all five programs, examine repeated module and lesson structures against the actual competencies and prerequisite dependencies. Matching counts are not automatically a defect, but they are never a design target. Do not transplant one program's outline, fixed workload, assessment pattern, or course architecture into another discipline.

A temporary coverage matrix or review notes may be useful for decisions, but the authoritative result is the revised public program catalog and course definitions—not a permanent duplicate curriculum registry.

### Classify and close review findings

Use a pinned source revision and record the affected course, outcome, lesson, assessment or catalog. A finding may be a confirmed defect (for example a demonstrated missing prerequisite), a suspected gap requiring inspection, a proposed expansion or architectural alternative, or an unestablished readiness claim. A keyword absence or module title alone does not prove missing competence. Check adjacent courses, criteria and evidence before recommending new requirements.

Use the following distinctions when triaging evidence; they are not repository labels or a new scoring rubric:

| Finding kind | Evidence that supports the classification |
| --- | --- |
| Confirmed defect | A specific contradiction of an adopted requirement, demonstrable technical error, broken published path, or concrete mismatch between a claimed capability and its assessment or prerequisite evidence. Cite the actual sources and show the discrepancy. |
| Coverage hypothesis | A plausible missing or weak capability suggested by disciplinary research, a keyword search or limited inspection. State what additional course, prerequisite, criterion or experiment would resolve it. |
| Expansion or design proposal | A possible new capability, pathway or architectural choice. Compare alternatives and consequences; do not treat external guidance alone as an adopted OEE obligation. |
| Readiness evidence gap | An unestablished educational claim that needs actual learner or independent review evidence under the existing status rules. Do not infer learner failure or success from source quality alone. |

For a substantial finding, explain the observed behavior or source, expected competency, consequence, supporting disciplinary evidence, alternatives, and an independently checkable acceptance condition. Prioritize defects by impact on learner safety, correctness, preparation and assessment validity; distinguish a research opportunity from a blocker. Record a disposition and rationale even if the proposal is rejected or deferred. In the issue or PR, link the baseline and proposed revision, distinguish inspected source, executed checks and untested assumptions, and describe the scope of the impact review. Reconcile only affected course/catalog metadata, outcomes and IDs, assessment mappings, prerequisites, workload and downstream resource or implementation references; explicitly state when none changed. Record the relevant [source checks](../scripts/README.md), their outcomes and limitations. A finding resolved in source is not automatically a learner-validation finding resolved in practice. Keep these records in issues and PRs rather than treating a review backlog as a binding curriculum.

## 12. Revise courses without losing educational meaning

Before changing a published course, compare its current and proposed outcomes, assessments, modules, prerequisites, classification, workload, and independent-study assumptions.

- Preserve established course identities and stable outcome/assessment IDs where their meaning remains continuous.
- Identify materially replaced outcomes and changed evaluation expectations explicitly.
- Protect useful learning when reorganizing lessons; do not discard a required capability because its explanation was awkwardly placed.
- Examine affected prerequisite closure and downstream courses, resource mappings and consumer integrations.
- Keep course revision and learner-evidence records interpretable; do not silently regrade assessed work against changed requirements.
- Update course source and its authoritative program catalog consistently through the repository's review process.
- Record rationale and substantive review findings in the existing PR or governance channel, not in a permanent audit report that competes with the current curriculum.

Editorial course reorganization alone does not automatically change normative OEE requirements. If a proposal actually alters binding specification rules, follow [OEE governance](../GOVERNANCE.md) and its RFC process.

## 13. Academic review beyond source validation

Use **separate review lenses**. A passing structural validator cannot establish whether lessons are well chosen or assessments really measure the claimed capability.

| Review lens | Questions |
| --- | --- |
| Disciplinary accuracy | Are mechanisms, technical claims, and cited references correct, complete within scope and current enough? |
| Program architecture | Are graduate capabilities covered? Are prerequisites and ownership coherent? |
| Instructional sequence | Are modules cohesive and lessons focused without filler, fragmentation or arbitrary symmetry? |
| Assessment validity | Do required tasks and criteria genuinely measure all claimed outcomes? |
| Workload and accessibility | Are the tasks feasible under stated preparation, access and time assumptions? |
| Change and provenance | Are identifiers, prior evidence, catalog data and downstream dependencies treated correctly? |
| Source maintenance | Do links, metadata, parser-supported format, assessments and repository checks pass? |
| Learner evidence | Do real study and independent review support claims about effectiveness or readiness? |

A reviewer should identify **the concrete defect, its effect on learner capability, the proposed correction, and evidence or reasoning for it**. Avoid vague labels such as "needs more depth" or replacing a uniform lesson count with a random distribution.

A structurally valid course may still require independent expert review and observed learner evidence. Keep its published readiness status until the evidence required by [Status Labels](../spec/status-labels.md) supports a change. A successful source check alone cannot make a course `tested` or `verified`.

### Plan learner validation separately

Source-level review can establish accuracy and plausible assessment design; it cannot establish observed learner success. Plan trials with appropriate learner preparation, accessible resources, actual effort, observed misconceptions, assessment difficulties, review and revision. Distinguish anonymized or consented evidence from author assumptions; do not publish private learner records. Apply the existing [Status Labels](../spec/status-labels.md) thresholds independently of source checks, release publication or completion of a remediation backlog.

### Final editorial questions

Use these questions as a review aid, **not** a mandatory new metadata section or a scoring formula:

1. Was the course researched against credible, attributable, discipline-appropriate sources?
2. Is its substantial exit capability clear and distinct from neighboring courses?
3. Does each outcome describe something observable and important?
4. Are assumed prerequisites actually provided by the published path?
5. Does each module exist because of a coherent conceptual stage rather than a numerical target?
6. Does each lesson contribute a focused, necessary objective and meaningful depth?
7. Is formative practice placed where learners need feedback rather than at a fixed template position?
8. Are assessments aligned with outcomes and free of unnecessary duplicate evidence?
9. Are failure cases, uncertainty, accessibility and safety addressed where materially relevant?
10. Is the workload plausible under independently reproducible conditions?
11. Are versioned source records and downstream consumers treated explicitly?
12. Are readiness, conformance and performance claims limited to available evidence?

## 14. Editorial foundations and further reading

These public sources informed the guide's research-led, outcome-aligned approach; they are **review references**, not mandatory learner resources or evidence of OEE accreditation.

- [Carnegie Mellon Eberly Center — Align Assessments, Objectives, Instructional Strategies](https://www.cmu.edu/teaching/assessment/basics/alignment.html): alignment between learning outcomes, evaluation and teaching.
- [Carnegie Mellon Eberly Center — Plan Your Course Content and Schedule](https://www.cmu.edu/teaching/designteach/design/contentschedule.html): purposeful topic selection, sequencing, practice and workload planning.
- [Carnegie Mellon Eberly Center — Learning Objectives](https://www.cmu.edu/teaching/designteach/syllabus/newcourse/learningobjectives.html): measurable, student-centered objectives.
- [ACM/IEEE-CS/AAAI, Computer Science Curricula 2023 (final report, 2024)](https://doi.org/10.1145/3664191): the Knowledge Model, Competency Framework and Software Engineering knowledge area support capability mapping, role-sensitive curriculum design and review of collaboration. Compare the report's scope and expected competencies with the relevant OEE program, not its course counts.
- [IEEE Computer Society, Guide to the Software Engineering Body of Knowledge (SWEBOK), version 4.0 (2024)](https://www.computer.org/education/bodies-of-knowledge/software-engineering): software architecture, design, testing and professional practice knowledge areas offer disciplinary reference points for system-design progression and assessment review. A body of knowledge is not a prescribed OEE course catalog.
- [CAST Universal Design for Learning Guidelines, version 3.0 (2024)](https://udlguidelines.cast.org/): accessible engagement, representation, feedback and expression of learning.

Sources guide editorial reasoning rather than overriding OEE's adopted curriculum, specifications, governance or evidence requirements.
