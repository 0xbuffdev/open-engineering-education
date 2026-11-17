# RFC 0004: SYS Post-SEF Academic Architecture and Identity-Safe v0.2.0 Migration

- **Status:** `draft`
- **Author:** OEE SYS curriculum proposal (steward review required)
- **Created:** 2026-11-17
- **Last updated:** 2026-11-17
- **Related issue:** [SYS migration tracker #106](https://github.com/0xbuffdev/open-engineering-education/issues/106)
- **Affected specification version:** `v0.2.0` (program and course definitions; no change to the normative `spec/` contract proposed)

## 1. Summary

Propose a **post-SEF Systems Engineering** core with twelve numerically ordered courses, including a new independently taught Rust foundation, an educational operating-systems/kernel course, a Linux virtualization/isolation course, and an independent systems capstone. All SYS enrollment requires demonstrated **completion of the entire published SEF program**, including its SEF10 capstone. No SYS course may silently reteach or re-award SEF competencies.

Nine publicly published legacy SYS course identities are reorganized under revised numbers. This is a substantive *breaking curricular identity revision*, not an editorial rename. The RFC proposes an **identity-safe staging and atomic public cutover**: individual course-and-catalog reviews may occur against a dedicated integration branch, but the public `main` catalog must never mix old and new meanings of a reused `SYS#` identifier. This proposal does not itself authorize implementation, promote any course readiness status, change an existing SEF requirement, or establish OEE conformance.

The current authoritative curriculum remains the nine [legacy SYS drafts](../curriculum/SYS/README.md) until a reviewed cutover merges. The proposal is scoped to the curriculum and its mappings; OEE [Course Format](../spec/course-format.md), [Evidence Rules](../spec/evidence-rules.md), [Status Labels](../spec/status-labels.md), and [Conformance](../spec/conformance.md) remain unchanged.

## 2. Problem and evidence

The historical SYS1–SYS9 import used short course outlines with common checkpoint/micro-lab/final-lab patterns and a nominal five-to-seven-week course duration, without the full `v0.2.0` outcome/evidence contract. The source [SYS catalog](../curriculum/SYS/README.md) correctly identifies them as legacy drafts. A conversion that simply adds `SYS#-O#` and `SYS#-AS#` to the legacy outlines would preserve significant academic gaps.

The currently [completed SEF program](../curriculum/SEF/README.md) already teaches and assesses digital logic/reference-machine execution, Python, formal/discrete and numerical mathematics, algorithms, software engineering practice, C11 memory and toolchains, Linux shells, foundational POSIX process/filesystem/pipe/signal interfaces, framed single-peer loopback TCP, nonblocking `poll`, professional software delivery, and a cumulative SEF capstone. The published [SEF7/SYS boundary](../curriculum/SEF/UNIX-SYS-BOUNDARY.md) explicitly retains all fourteen SEF7 outcomes and seven summative assessments while identifying possible *advanced* SYS destinations.

The legacy SYS curriculum does not separately establish Rust language proficiency before asking for C/Rust lifetime comparison and unsafe/FFI reasoning. It does not provide a sustained education in how an actual kernel implements the OS services SEF7 uses, or a coherent isolation/virtualization capability. Its short course outlines are not adequate evidence that concurrency ordering, crash durability, distributed failure and production recovery can be taught and validly assessed at sufficient depth.

Without an explicit identity strategy, renumbering legacy SYS2 (C/Rust systems programming) to proposed SYS3 while assigning proposed SYS2 to Rust foundations would make archived and new references to `SYS2` ambiguously mean different courses. Repeating this for the remaining codes risks corrupting catalog links, SEF7 destination mapping, external learning-resource mappings and historic learner provenance.

## 3. Proposed change

### 3.1 Program mission, entry and graduation

SYS is a specialization in **systems software and infrastructure engineering**, not an electrical-engineering degree, full compiler specialization, security certification or guaranteed production-operations credential. Graduates must independently build, reason about, diagnose, measure and defend systems mechanisms with explicit resource bounds, platform assumptions, failures and limits.

**Entry condition:** Before starting the SYS program, a learner must hold actual assessed completion evidence for **all eleven currently required SEF courses including SEF10** under their applicable pinned course revisions, or an expressly reviewed, genuinely assessed equivalent completion of that *entire* SEF program. A diagnostic, job title, claimed experience, individual SEF6/SEF7 completion, or SYS capstone portfolio does not satisfy this requirement. On the proposed course graph, SYS1 and SYS2 have direct prerequisite `SEF10`; every later SYS course has `SEF10` in its transitive prerequisite closure. Catalog, course definitions and enrollment interpretations must agree.

**Graduation:** Complete all eleven pre-capstone SYS core courses against their published revisions, then meet every required SYS12 project outcome, substantive deliverable, required evaluation and technical defense. SYS12 may integrate previous skills but must not silently regrade or replace missing prerequisite completion evidence. No elective is a hidden graduation prerequisite.

**Reference environments:** Unprivileged learner-controlled Linux, synthetic fixtures, local loopback/fault-controlled clusters and emulator or disposable guest for kernel exercises. Required evidence has a no-paid-service, no-proprietary-grader route. Native host root, real production outages, unauthorized scanning and public infrastructure are not required. Alternative accessible or simulated environments must demonstrate equivalent stated outcomes, not claim unsupported kernel or isolation guarantees.

### 3.2 Proposed authoritative course identities and order

**These are proposed identities, not present learner-facing authority.** Duration ranges assume 10–15 focused hours per week initially; every range remains provisional pending actual learner evidence. The numeric sequence expresses suggested teaching order; the *direct prerequisites* are the eligibility contract, so independent learning branches are permitted.

| Course | Target capability | Provisional weeks | Direct prerequisite |
| --- | --- | --- | --- |
| SYS1 | Computer Architecture, Memory & Performance | 10–14 | SEF10 |
| SYS2 | Rust Programming Foundations | 12–16 | SEF10 |
| SYS3 | Systems Programming with C & Rust | 10–14 | SYS1, SYS2 |
| SYS4 | Operating Systems & Kernel Fundamentals | 12–16 | SYS1 |
| SYS5 | Concurrency, Atomics & Memory Models | 12–16 | SYS2, SYS3, SYS4 |
| SYS6 | Linux Networking & Services | 10–14 | SYS3, SYS5 |
| SYS7 | Storage Engines & Data Systems | 12–16 | SYS3, SYS5 |
| SYS8 | Virtualization, Containers & Linux Isolation | 8–12 | SYS4, SYS5 |
| SYS9 | Distributed Systems | 14–18 | SYS6, SYS7 |
| SYS10 | Performance Engineering & Observability | 8–12 | SYS5, SYS6 |
| SYS11 | Systems Design & Production Engineering | 10–14 | SYS8, SYS9, SYS10 |
| SYS12 | Independent Systems Engineering Capstone (`project`) | 16–20 | SYS1–SYS11 |

An ordinary taught course has `Type: course`; SYS12 has `Type: project`. All first-published course revisions are `Status: draft`, `Specification: v0.2.0`. No number of weeks, lessons, fixed activity stages or assessment count is a completion standard.

**Prerequisite rationale:** SYS4 may teach a C-based educational kernel using SEF6/SEF7 and machine-level SYS1 competence, without demanding Rust/FFI or SYS3. SYS8 requires kernel, synchronization and resource-control foundations, not an arbitrary network-server prerequisite. SYS6 and SYS7 become independent advanced service and persistence branches; SYS9 joins them for fault-tolerant replication; SYS10 supports measured production design. SYS12 has explicit closure across every preceding core competency.

### 3.3 Graduate competency ownership and assessment direction

Required graduate capabilities are **owned**, not merely mentioned, as follows:

| Primary owner | New assessed capability beyond SEF | Required substantive evidence direction |
| --- | --- | --- |
| SYS1 | Explain and investigate real ISA/ABI, compiled binary execution, caches/TLB and observed microarchitecture | Assembly/link/load trace, controlled locality experiment and falsifiable measurement/limits |
| SYS2 | Independently develop idiomatic *safe Rust* with moves, borrowing, lifetime relationships, algebraic types, traits and package/toolchain semantics | Owned reusable Rust component, compiler-diagnostic transfer and tests |
| SYS3 | Engineer advanced resource supervision and sound narrow C/Rust unsafe/FFI boundaries | Cross-language resource contract, invalid-state/fault investigation, safety argument and bounded utility |
| SYS4 | Explain and safely extend kernel traps, scheduling, virtual memory, synchronization, filesystems and device I/O | Bounded educational-kernel modification or equivalent transparent simulator, trace and defense |
| SYS5 | Specify and verify shared-memory concurrency, locks/condition variables, atomics, memory order and progress bounds | Race/deadlock/correctness analysis, concurrent component and controlled schedule/failure evidence |
| SYS6 | Build multi-client Linux services with protocol states, event-driven/async I/O, security, resource caps and backpressure | Protocol/overload correctness under partial I/O, cancellation, timeouts and clean shutdown |
| SYS7 | Build and fault-test local physical persistence, storage layouts, WAL, indexing, corruption checks and recovery | Recoverable key-value component, deterministic crash cut points, guarantees/limitations and performance |
| SYS8 | Evaluate Linux namespaces/cgroups/capabilities, virtualization, rootless containment and security limits | Safe controlled isolation demonstration, resource-limit checks and honest threat-boundary analysis |
| SYS9 | Reason about causal order, histories, consistency, replication, quorum, consensus safety/liveness and partial failure | Small replicated service plus deterministic fault schedule, safety arguments and restricted liveness claims |
| SYS10 | Attribute CPU/memory/lock/network/storage bottlenecks and evaluate measurable change with uncertainty | Independently reproducible baseline, profiling, alternative hypothesis and post-change regression evidence |
| SYS11 | Engineer infrastructure reliability, hardening, recoverability, SLOs, capacity, incidents and operability | Production-readiness review on a genuine systems component with a tested recovery/handoff |
| SYS12 | Independently integrate mechanisms, apply realistic failure reasoning and defend original system decisions | Original cumulative artifact, reproducible correctness/performance/fault campaign and unfamiliar change/defense |

Course authors must develop coherent module and lesson objectives from these capabilities, with scaffolding faded over time. The canonical course files, not this RFC, must publish the final explicit course outcomes and `SYS#-AS#` **Outcomes/Work/Criteria/Evidence** definitions. A topic in a module does not establish a demonstrated outcome. The final curriculum must not enforce repetitive per-module quizzes, compulsory labs for every concept, a universal final-lab template or meaningless duplicate submissions.

### 3.4 Preserve SEF ownership: no foundational repetition

- **SEF1:** bit patterns, Boolean gates, reference CPU and program-to-output models are already assessed. SYS1 begins from real executable/ISA/ABI and hardware-performance investigation rather than re-teaching gate construction or educational fetch/decode basics.
- **SEF2, SEF5:** general programming, functions, design, Git, debugging, tests and CI are complete. SYS2 teaches **Rust-specific** semantics and tooling, not fundamental programming or generic testing from zero.
- **SEF6:** C syntax, pointer/array bounds, object lifetime, allocation, defined/undefined behavior, simple data structures and multi-file compilation are complete. SYS3 uses these foundations for comparative Rust resource APIs, FFI, soundness and advanced process supervision.
- **SEF7:** descriptor/OFD contracts, controlled fork/exec/waitpid and signals, directory identity, two-child pipes, single-peer framed TCP, one nonblocking `poll` peer and independent failure evidence are complete. SYS3/6 go beyond this to advanced supervision, cross-language I/O design, multiclient scale, overload and cancellation. No current SEF7 outcome or assessment is moved or deleted.
- **SEF4/SEF11/SEF8:** proof methods, basic algorithm complexity and numerical statistics are complete. SYS5/9/10 apply them to new memory-ordering, distributed-safety and empirical-systems claims rather than teaching basic proofs, graphs, probability or regression from scratch.
- **SEF9/SEF10:** software delivery, ethics, privacy, licensing, responsible AI, independent review and a complete developer CLI are complete. SYS11/12 assess new infrastructure threats, fault resilience, operation and independent systems synthesis.

Any repeated terminology must be explicitly justified by a deeper observable exit capability. Prerequisite refreshers are optional, formative and cannot be new completion gates unless the new outcome is materially distinct.

### 3.5 Identity revision and collision-free public publication

The present legacy identifiers are not unused. **The Git commit/tag/revision is part of historic meaning**. The target identity map is:

| Legacy code at pre-migration source revision | Target code after adopted cutover | Status of semantic relation |
| --- | --- | --- |
| SYS1 — Computer Architecture, Memory & Performance | SYS1 | Retains subject, major rewrite; no automatic assessment equivalence |
| SYS2 — Systems Programming with C & Rust | SYS3 | Renumbered and deepened |
| SYS3 — Concurrency, Atomics & Memory Models | SYS5 | Renumbered and deepened |
| SYS4 — Linux Networking & Services | SYS6 | Renumbered and deepened |
| SYS5 — Storage Engines & Data Systems | SYS7 | Renumbered and deepened |
| SYS6 — Distributed Systems | SYS9 | Renumbered and deepened |
| SYS7 — Performance Engineering & Observability | SYS10 | Renumbered and deepened |
| SYS8 — Systems Design & Production Engineering | SYS11 | Renumbered and deepened |
| SYS9 — Systems Engineering Capstone | SYS12 | Renumbered and deepened |
| No equivalent legacy identity | SYS2 — Rust Programming Foundations | New capability |
| No equivalent legacy identity | SYS4 — Operating Systems & Kernel Fundamentals | New capability |
| No equivalent legacy identity | SYS8 — Virtualization, Containers & Linux Isolation | New capability |

**Collision policy:** It is unacceptable to overwrite legacy `SYS2` in the public catalog with Rust while leaving the old `SYS2` semantics referenced as current elsewhere, or to retain both meanings in one active public catalog.

**Proposed execution method:**

1. Record an accepted steward decision on this RFC **before** repurposing existing SYS codes.
2. Create a dedicated SYS v0.2.0 **integration branch** from then-current `main`, with explicit *target/proposed* catalog semantics restricted to that branch. Leave `main` authoritative and undisturbed.
3. Prepare **one course-and-target-catalog PR per course**, targeted at the integration branch and separately reviewed. Course files must use the final adopted codes, complete `v0.2.0` public requirements and explicit `draft` status. Individual PR merge into the integration branch is *not publication* or main-branch approval.
4. Keep the integration branch's target catalog and file graph coherent while staging: if a required target course is not yet present, mark the integration branch incomplete in its review/validation summary and do **not** claim full catalog conformance or promote/publish to `main`. Design reviews may be parallel; publication remains gated.
5. After **all twelve** targets are fully reviewed, perform a single **atomic main cutover PR** from the integration branch updating the active SYS catalog, all twelve course files, internal/cross-program references (including the SEF7 target map and APP15 if its scope/requirements are actually approved), old-to-new identity documentation, source validators/inventory and tests. Resolve conflicting concurrent `main` changes before final review.
6. Preserve immutable historic Git tags, commit SHAs, prior assessment IDs and learner evidence, and document the source-revision-qualified translation of legacy links. No automatic old-to-new completion/assessment credit, no forced learner record rewrite and no legacy-format runtime parser are required.

The implementation mechanism above is proposed to eliminate identity collisions while maintaining course-level review. If tooling limitations require another method, an equivalent **atomic, independently reviewed** public cutover must be approved in this RFC before execution. A partial main migration that reuses existing codes for new subjects is disallowed.

### 3.6 Program/public source boundaries

- `curriculum/SYS/README.md` and linked `SYS1.md`–`SYS12.md` are the authoritative **published** curriculum after cutover. This RFC remains decision history, not a second mutable curriculum registry or detailed authoring spec.
- The current [SEF7 destination map](../curriculum/SEF/UNIX-SYS-BOUNDARY.md) is non-normative and must be corrected for the new codes at cutover; the **assessed SEF7 obligations do not change**. Candidate new advanced destinations: legacy SYS2→target SYS3, legacy SYS3→target SYS5, legacy SYS4→target SYS6, legacy SYS5→target SYS7, legacy SYS7→target SYS10, legacy SYS8→target SYS11 and legacy SYS9→target SYS12. Verify every explicit outcome and assessment destination after remapping; new SYS4/SYS8 are additional mechanism owners, not excuses to drop SEF7 evidence.
- APP15 (TypeScript–Rust Application Interoperability) currently has an unresolved Rust prerequisite. Its published owner must explicitly review whether target SYS2 Rust foundations and/or SYS3 C/Rust FFI are substantively necessary; do not silently add a new graduation dependency or change an elective's requirements based on a title.
- `content` resource/book mappings, OEE Workspace and 0xNAND are **downstream consumers**, not authorities over course requirements. Review their pinned course/revision references explicitly. Changes to their records are separate approved actions; no silent repinning.
- Keep old and new source semantics distinguishable with exact commit/release revision and source path. Update README navigation, repository-wide program catalogs, link targets, inventory and scripts when the approved cutover actually occurs.

## 4. Alternatives considered

| Alternative | Advantage | Disadvantage | Decision proposed |
| --- | --- | --- | --- |
| Keep original SYS1–SYS9 meanings, append SYS10–SYS12 and sort display order | No breaking ID reassignment; simple incremental main migration | Codes no longer follow the requested academic order, and new Rust/OS foundations appear late numerically | Reject for this **pre-substantive-migration** restructuring, while noting its superior identity stability |
| Rename and migrate one old course at a time directly on `main` | Visible incremental main progress | Reused IDs collide with unfinished legacy catalog, links and learner evidence | Reject |
| Publish all twelve outcomes/lessons/assessments in one monolithic main PR | One identity cutover | Review is unmanageably large; defects are difficult to isolate | Reject |
| Review each course on a dedicated integration branch, then cut over `main` atomically | Preserves independent course review and unambiguous public IDs | Integration branch requires extra coordination and main sync | **Prefer** |
| Retain nine courses and add only a brief Rust introduction inside SYS2 | Fewer courses | Hides language prerequisites and OS/isolation mechanisms; promotes shallow course evidence | Reject |

## 5. Impact assessment

### Existing courses and programs

All current SYS1–SYS9 identities, prerequisites, titles, course code references and program graduation requirements are affected. Three new course capabilities are introduced. The already assessed SEF curriculum remains intact, including all SEF7 outcomes and seven assessments; SYS program entry is explicitly completed SEF, not SEF6 alone. SYS capstone becomes the final proposed core SYS12 and requires full preceding core closure.

APP15 and the SEF7/SYS map require scoped destination review. No APP or SEF completion outcome may be silently amended by this RFC.

### Implementations

Tools and platforms must use the revision-qualified adopted course IDs and prerequisites after cutover; historic course evidence is still interpreted under its original published revision. No private host, tool service or 0xNAND account may become a compulsory means of reading or completing public OEE requirements.

### Evidence and status labels

No global status rules change. All newly migrated courses begin `draft`. Required assessments must include observable outcomes and public Work/Criteria/Evidence. Course completion requires genuine inspectable evaluation and project defense where relevant; passing parser/CI checks does not establish substantive competence or educational readiness.

### Conformance

The RFC does not change `spec/conformance.md`. A revised SYS program cannot claim `v0.2.0` conformance merely because all source files validate. It must have a separately recorded actual course- and program-scope review under existing conformance rules. `draft`, `tested` and `verified` are separate evidence-based educational-readiness statuses.

### Licensing and governance

No license or contributor-obligation change. Course source licensing/attribution and authentic DCO sign-offs still apply. Significant publicly visible curriculum/identity decisions require steward record, reviewed PRs and a credible revision history; proposed RFC is not self-approving.

## 6. Compatibility and transition

This is an intentionally breaking **curricular identity revision**, not a request for an old runtime-format compatibility adapter. Existing Git releases, prior source revisions, old assessments and learner-owned evidence stay intact and interpretable. Before cutover, a consumer cannot assume target `SYS2` means Rust. After cutover, a reader must pin source version or revision to distinguish historic `SYS2` C/Rust from new `SYS2` Rust foundations. This rule applies to every reassigned code in §3.5.

The final atomic cutover PR must link or embed a stable historical identity mapping and identify any links/bookmarks that are expected to point at previous Git revisions. Do not create a synthetic learner completion or bulk rewrite pinned evidence.

There is no automatic credit transfer. A historically assessed capability can only be considered against a new criterion through explicit, justified substantive re-evaluation.

## 7. Risks and mitigations

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Historic codes silently change meaning | High | Recorded old→new mapping, revision-qualified references, integration review and atomic cutover |
| Repetition of SEF coursework | High | Outcome-level SEF→SYS competency ownership review in each course PR |
| Missing prerequisite or cycle | High | Catalog graph tests; full `SEF10` entry closure for every core |
| Unsupported course depth or inflated workload estimates | High | Detailed module/lesson and assessment review, proportionate evidence, empirical learner pilot before status promotion |
| False memory-order, crash, distributed or isolation claims | High | Independent technical review, bounded reproducible fault tests, explicit assumptions and unproved-limit disclosures |
| Review burden and branch divergence | Medium–high | One course per PR into integration; routine main sync; final full-program independent review |
| Mandatory root, production fault or paid tooling | High | Unprivileged Linux, disposable kernels/fixtures and demonstrably equivalent accessible routes |
| Misstated program readiness | High | Every course `draft`; separate conformance and `tested`/`verified` evidence decisions |
| Cross-program or external consumer drift | Medium–high | Link, inventory, source SHA and pinned-mapping review before and after cutover |

## 8. Validation plan and required delivery

Before architecture acceptance:

1. Inspect the live SYS and SEF course files and source inventory at an exact main commit.
2. Independently assess whether the twelve proposed course competencies provide sufficient systems coverage without an artificial microcourse or hidden foundation.
3. Review every legacy→target code mapping, collision risk, program completion rule and exact transitive prerequisite closure.
4. Confirm no proposed change removes or reduces required SEF7 assessed competencies.

For **every** course-and-catalog integration PR:

1. Verify OEE `v0.2.0` title, metadata, four required top-level sections, coherent modules and ordered lesson sequence.
2. Verify unique `SYS#-O#` and `SYS#-AS#` identities, substantive assessment validity and explicit **Outcomes, Work, Criteria, Evidence**, with applicable failure/safety and accessible alternative conditions.
3. Review genuine new SYS depth beyond SEF outcomes; avoid universal quiz/lab/proof-of-attendance patterns and unnecessary reports.
4. Check prerequisite graph, catalog, tests, Markdown/link correctness, historical revision effects and pinned downstream mapping changes.
5. Run applicable official repository validation and obtain independent technical/academic review, steward review and authentic contributor DCO sign-off.

For the final main cutover:

- Verify **all twelve** source courses, full core course completion, SYS12 technical defense and program outcome coverage; no duplicate current course IDs and no missing legacy/source identity explanation.
- Validate source/links/inventory, SEF7 map, APP15 boundary decision and any identified public related references against the exact final commit.
- Require the same authenticity and independent review; merge only after an explicit steward-approved RFC and separately reviewed integration.
- Record separately any empirical learner pilots and readiness promotion. Structural source completion is not learner validation.

**Delivery order proposed:** public decision → integration branch/target catalog → SYS1 and SYS2 foundational course reviews → SYS3 and SYS4 mechanism reviews → SYS5 concurrency → SYS6/SYS7 service and storage branches → SYS8 isolation → SYS9 distributed, SYS10 performance → SYS11 production → SYS12 independent capstone → whole-program review → atomic main cutover. All stages must remain distinct from claims of `tested`, `verified` or accredited graduation.

## 9. Open questions for steward review

1. **Approve deliberate numeric renumbering?** The alternative of preserving old IDs is less disruptive but violates the requested clean code order; accepting a new numbering explicitly accepts breaking identity semantics with retained historical records.
2. **Approve integration-branch staging and atomic public cutover?** This avoids collisions but delays main publication until all twelve course reviews finish. Confirm required head/base branch procedure and whether source CI needs non-main catalog handling.
3. **Approve strict full-SEF program entry?** Every SYS course depends directly or transitively on SEF10; reviewed full-program equivalence, where allowed, must be genuinely assessed rather than self-reported.
4. **Approve SYS4's direct prerequisite of SYS1?** The kernel course uses a C educational kernel and previously assessed SEF6/SEF7; it does not need mandatory SYS3 FFI.
5. **Should APP15 require SYS2 only, or also SYS3?** The consuming elective's actual Rust and FFI outcomes must determine this, without speculative enforcement in SYS itself.

## 10. Decision

- **Decision:** Pending
- **Decision date:** pending
- **Decision-maker:** OEE steward
- **Rationale:** pending independent academic/technical review and recorded steward decision
- **Conditions:** No course identity cutover or normative implementation before acceptance; authentic contributor DCO; source/evidence histories unchanged; all courses remain `draft`.
- **Implementation pull request:** pending

This RFC is a proposal and a public rationale, **not** accepted curriculum authority, source implementation, learner-testing evidence, or independent conformance certification.
