# SYS9 — Systems Engineering Capstone

**Program:** SYS — Systems Engineering
**Type:** `project`
**Prerequisites:** [SYS1](SYS1.md)–[SYS8](SYS8.md), [SYS10](SYS10.md) (assessed completion of every predecessor)
**Duration:** 18–24 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; dependent on project complexity)

> [Systems Engineering](README.md) · [Course format](../../spec/course-format.md) · [Design guide](../DESIGN-GUIDE.md)

## Overview

**SYS9 is the cumulative evidence-and-defense project for the entire SYS pathway, not another specialist course or a feature checklist.** It requires one authentic, bounded, inspectable **Rust systems component or infrastructure service** that integrates real low-level resource and concurrency reasoning with a necessary network, persistent-state, process or distributed-system mechanism; demonstrates correct externally observed behavior; handles selected hostile/failure conditions; measures relevant operating costs; can be rebuilt and operated by another reviewer; and survives a genuinely unfamiliar engineering challenge. Suitable shapes include a fault-aware job runner, durable local message processor, bounded streaming service, recoverable task coordinator or a fixed-scope replicated service. The chosen problem must warrant the mechanism rather than merely showcase a technology. **One coherent, cumulative source tree** is extended from admission through final defense; no new mini-project is compulsory at each module.

**A separate entry gate protects graduate meaning.** Before capstone admission, the learner must already hold authentic assessed completion decisions for **SYS1–SYS8 and SYS10**, or separately governed outcome-equivalent decisions tied to applicable revisions. The entry record lists the decision and evidence for **each** predecessor. Work in SYS9 may reuse legitimate prior source and extend it, but **cannot backfill, waive or silently regrade missing predecessor evidence**. Capstone admission is not graduation: after entry, **all fourteen SYS9 outcomes and six required summative evaluations** must independently receive satisfactory, reviewable decisions. A screenshot, repository star count, attendance, accumulated hours or paid platform grade is not a substitute.

**Authorship and substantial new integration:** A previous SYS3 queue, SYS4 network server, SYS5 storage engine or SYS6 replication artifact is an acceptable starting point, not an automatic pass. The capstone must disclose what is inherited and show meaningful new integration, constraints, error contracts, evidence or an original extension; a renamed prior final assignment without evaluated new engineering cannot establish SYS9-O4/O11/O14. Rust remains the primary implementation language, with C/ABI comparison invoked only where the chosen architecture genuinely needs it. Solo work is acceptable. For collaborative artifacts, each learner's owned decisions, contributions and individual defense must be inspectable; team membership does not automatically confer any outcome.

**A bounded system, not a production certification:** Define visible operations, numeric memory/CPU/disk/queue/work budgets, invariants, failure and trust assumptions, and the exact promise made to a user. Test normal, boundary, invalid and a relevant adverse/partial-progress scenario using **independently derived expected outputs**. Demonstrate a controlled failure, a correction or safe containment, repeatable benchmark evidence, an operator handoff and an **unfamiliar bounded reviewer-supplied change**. Distinguish simulator/model evidence, actual local-process observations and unsupported physical crash, geographically independent availability, encryption or production-SLA claims. A principled **no-go or restricted local release recommendation** is acceptable when risks warrant it; however, naming a limitation does not waive a broken required correctness outcome.

**Feasibility, accessibility and workload:** Use stable Rust/Cargo, a nonprivileged local Linux environment, learner-owned synthetic fixtures and a deterministic local process/test harness. No proprietary checker, paid cloud, privileged kernel or external production traffic is required. Public criteria and equivalent accessible text/recorded/written defense options enable independent self-study while allowing a reviewer to supply a new *bounded* variant to test transfer. The **18–24-week** duration at **10–15 focused hours/week** (approximately 180–360 hours) is provisional; work is paced by actual scope, debugging, feedback and revision, never elapsed time as a graduation condition. Consolidated lesson entries can each require several substantial source revisions, fault histories, independently checked experiments and reviewer cycles; fewer headings do not reduce the evidence needed for graduation. Educational status stays `draft` until authentic learner and qualified independent review evidence supports a different label.

## Learning outcomes

- **SYS9-O1:** Verify prerequisite completion decisions for SYS1–SYS8 and SYS10 before capstone entry, distinguishing prior evidence from new integration work.
- **SYS9-O2:** Select and bound an authentic systems problem with users, expected behavior, resource constraints and testable failure guarantees.
- **SYS9-O3:** Design a coherent architecture with explicit resource ownership, concurrency, I/O and persistent/distributed-state boundaries appropriate to the problem.
- **SYS9-O4:** Implement a Rust systems component whose new low-level mechanisms, interfaces and error contracts are explainable and reviewable.
- **SYS9-O5:** Specify invariants, trust assumptions, resource limits and admissible state transitions under partial progress and failure.
- **SYS9-O6:** Verify critical behavior through independently derived normal, boundary, invalid and adversarial test oracles.
- **SYS9-O7:** Reproduce failure, overload, cancellation, crash/restart or network-loss scenarios appropriate to the chosen component.
- **SYS9-O8:** Measure system bottlenecks, latency/throughput and resource demand with controlled baselines, variability and justified conclusions.
- **SYS9-O9:** Explain reliability, durability, consistency and security guarantees only to the extent supported by design and evidence.
- **SYS9-O10:** Produce nonprivileged clean-state build, installation, configuration, startup, stop, recovery and troubleshooting instructions.
- **SYS9-O11:** Evaluate architecture and implementation alternatives against complexity, performance, safety and maintainability.
- **SYS9-O12:** Respond to an independently supplied unfamiliar change, incident or failure without hiding new limitations.
- **SYS9-O13:** Communicate project design, provenance, limitations, ethical impact and responsible-release recommendation in accessible reviewable form.
- **SYS9-O14:** Defend the authored system end-to-end, including observed failures, corrected regressions and remaining risks.

## Modules

### Module 1 — Capstone Admission, Prior Mastery and Responsible Problem Selection

#### Outcomes

- SYS9-O1
- SYS9-O2
- SYS9-O13

#### Lessons

1. **Pre-entry evidence and independent capstone admission** — Before any assessed capstone implementation, audit all nine predecessor course decisions for SYS1–SYS8 and SYS10 by actual outcome evidence, course/spec revision, reviewer and governed equivalence if applicable. Record an explicit admit/hold result; missing competence must be completed under its own governing assessment, never inferred from a promising SYS9 proposal or later project work.
2. **Prior-art reuse without repeated courses** — Inventory previously built SYS artifacts and suitable openly licensed examples; identify modules that can be reused unchanged, new integrations that require evaluation and work that would merely repeat SYS3/SYS4/SYS5/SYS6 assignments.
3. **Legitimate systems problem and minimal credible solution** — Select one real bounded operator/user need such as a durable local processor, streaming service or fault-aware runner, then compare a library-only answer, composition of existing SYS work and one justified new Rust systems mechanism. Show who observes correctness, why an added mechanism changes genuine capability and why gratuitous cluster/network/storage features would weaken the scope.
4. **Feasibility and available resources** — Inventory nonprivileged Linux access, toolchain, CPU/memory/disk/network limits, realistic study time, test fixtures and reviewer availability before selecting an algorithm or deployment requirement.
5. **Public scope and explicit non-goals** — State functional boundaries, expected input/output, operational constraints, threat/failure conditions and excluded concerns; defend why attempting every prior SYS technology or a production cluster would dilute one coherent exit capability.
6. **Provenance, license and responsible assistance** — Record external code dependencies, prior personal work, collaborative contributions and any generated assistance used to produce artifacts. Identify the learner's owned design and code decisions, license/privacy obligations and how a reviewer can challenge understanding rather than equate repository authorship with competence.

*Formative reviewer prompt:* Examine a capstone application with an impressive Rust service but an unreviewed SYS5 assessment and determine the honest admission disposition.

### Module 2 — Engineering Contract, Architecture and Proof Obligations

#### Outcomes

- SYS9-O2
- SYS9-O3
- SYS9-O5
- SYS9-O9
- SYS9-O11

#### Lessons

1. **Public operation contract and partial-progress semantics** — Specify independently decidable normal, boundary, invalid and refused requests with result bytes/state, identity, cancellation, pending versus committed progress and explicit unknown outcomes. Include the case where a timeout follows a completed effect and distinguish it from rollback, and where an unsynced file write cannot justify an unqualified durable acknowledgment.
2. **Resource ownership and lifecycle maps** — Trace the ownership of Rust values, task/thread contexts, buffers, file descriptors, processes, files or sockets actually used by this project. Explain cleanup order across shutdown, cancellation and unexpected errors without repeating Rust language tutorials.
3. **Concurrency and progress invariant** — State an actual synchronization, single-writer or work-queue rule derived from SYS3; include linearization/visibility point where relevant, wait/lock order, cancellation ownership and a case that would violate it.
4. **Network/storage/distributed boundary chosen by need** — Select one substantial SYS4/SYS5/SYS6 domain that materially changes the project's behavior; show its protocol, commit/recovery or membership/consistency semantics without requiring all three domains as feature checkboxes.
5. **Trust assumptions and state invariants** — Define input trust, file or message format validation, permission/secret boundaries, legitimate transitions, denied requests and resource exhaustion refusal; align claimed security to exact checks performed.
6. **Alternative architecture, risk threshold and design review** — Compare two feasible ownership/algorithm choices under identical workload, failure, security and maintenance constraints, stating their resource and complexity costs. Set a review criterion that would reject unsafe assumptions, unsupported durability/availability or excessive implementation scope before coding and a measurable signal that would reopen the decision.
7. **Verification plan and independent oracles** — For every claimed invariant and important output, design a hand-derived or separately implemented normal, invalid and failure oracle and identify which observation would falsify it; never generate expected results from the system under test.

### Module 3 — Incremental Rust Systems Construction and Authorship

#### Outcomes

- SYS9-O3
- SYS9-O4
- SYS9-O5
- SYS9-O6
- SYS9-O11

#### Lessons

1. **One executable vertical slice and cumulative source checkpoint** — Build the smallest correct Rust operation crossing the chosen concurrency/resource boundary and meaningful process, socket, durable-state or distributed mechanism, with independently expected output. Keep it in the same versioned source tree through every milestone, recording validated behavior, newly introduced constraints, regressions and unresolved risks rather than starting another course-shaped mini-project.
2. **Inherited Rust components, authorship and code-level defense** — Mark reused SYS3/SYS4/SYS5/SYS6 source, external dependencies, prior personal work and generated assistance separately from newly owned integration and invariants. Demonstrate comprehension by tracing a concrete new error path and answering a bounded unfamiliar code-level modification; copying an earlier reviewed project or explanation is not newly assessed capstone competence.
3. **Versioned interfaces, strict validation and resource budgets** — Publish typed bounded API/record/message rules for the mechanism actually used, including version and compatibility, checked length arithmetic, request counts, file/queue/byte/worker budgets, malformed data and unsupported-operation refusal before allocation. Test a hostile boundary that would otherwise grow memory or admit an invalid path; no unrelated formats or protocols are mandatory.
4. **Failure-aware ownership and RAII** — Demonstrate the project's actual resource owners, fallible construction/destruction and cleanup after partially initialized tasks/files/sockets. Show that errors do not leak clients, leave unjoined work or silently reuse invalid state.
5. **Concurrency and load control integration** — Apply SYS3 synchronization to the real path: single-writer admission, actor ownership, worker queue or lock protocol, termination and backpressure. Verify no broken invariant under multiple clients or operations rather than adding threads decoratively.
6. **Systems mechanism deepening** — Implement one substantive networking, persistence or distributed correctness feature that extends predecessor work: e.g. durable job dedup after restart, bounded streaming checkpoint, safe peer reconnect or term-fenced task processing, with a precise applicable contract.
7. **Partial work, idempotence and error returns** — Handle failed I/O, duplicate input, canceled request, unknown completion and retry under the selected mechanism. Show why a rejected request is observable and why any replay or compensation rule is safe.
8. **Build reproducibility and trust boundaries** — Pin Rust toolchain/edition/dependencies, record Linux/target/platform assumptions, and make the clean checkout build work without private secrets, production network, root or unknown external data.

### Module 4 — Independent Correctness, Adversarial Failure and Recovery

#### Outcomes

- SYS9-O5
- SYS9-O6
- SYS9-O7
- SYS9-O9

#### Lessons

1. **Independent reference oracle and normal/boundary regression** — Derive a separate small sequential or state-transition model with explicit input histories, permitted states and expected response bytes, without calling the implementation's handlers. Run legitimate, empty, maximum-size, repeated and controlled stop cases, matching exact independently calculated results rather than treating a clean build or snapshot produced by the system as its own oracle.
2. **Malformation and trust-boundary failures** — Inject truncated/oversized protocol or file records, invalid config, unauthorized paths or incompatible versions as applicable; verify safe refusal/containment without leaking secrets, accepting corrupt committed state or crashing other fixtures.
3. **Concurrency and cancellation schedules** — Control overlapping requests, delays, task joins or state changes to challenge a real progress/ownership invariant. Distinguish 'no observed race' from a tested schedule or proof that all interleavings are safe.
4. **Storage and restart cut points** — For a persistence-bearing project, stop a process before/after actual append/sync/acknowledgment and compare acknowledged versus ambiguous post-restart state. If no persistent store is in scope, substitute a meaningful recovery/failure case and explain the omission.
5. **Network failure and unknown completion** — For remote-client designs, inject delayed/duplicated frames, peer disconnect, blocked writer or partition simulation and track retry identity and incomplete outcomes; for strictly local designs, use relevant process/task loss instead of adding artificial networking.
6. **Bounded overload and cleanup** — Saturate a declared queue/file/connection/CPU resource limit under synthetic load, verify backpressure/rejection policy, bounded memory and recovery after cancellation or shutdown, and demonstrate no damage to unrelated host state.
7. **Fault history, physical-assumption limits and assurance scope** — Record bounded seeded injection stages and independently allowed post-fault outcomes, differentiating synthetic short I/O, controlled process termination, Linux observations and unsupported power-cut or multi-host claims. Publish which transitions and invariants each fixture tested, which remain untested and why even many green cases are not a universal concurrency, security or durability proof.
8. **A real failing or risky case and correction** — Show an authentic failing baseline or a deliberately specified unsafe scenario that the independent checker rejects; make a minimal justified correction or a verified fail-closed limitation, then retain a negative regression. Do not manufacture a fake incident or hide a known material defect.

*Formative reviewer prompt:* Given a crash after durable storage but before reply, predict valid recovery and client ambiguity, then explain why a repeated retry must not cause a second effect when dedup was promised.

### Module 5 — Performance, Capacity and Evidence-Based Engineering Choices

#### Outcomes

- SYS9-O8
- SYS9-O9
- SYS9-O11

#### Lessons

1. **Critical-path selection, comparable workloads and correct results** — Choose one meaningful client-observed operation and two bounded comparable workload/resource configurations under the same correctness and durability contract. Independently verify completed, refused and erroneous work before timing; separate service CPU, synchronization, queue waiting, disk I/O and network completion rather than measuring a changed amount of useful work.
2. **Arrival and waiting accounting** — Choose scheduled-arrival or a correctly caveated response-driven load generator, logging offered, admitted, completed, refused, timed-out and outstanding operations so slow or unavailable requests do not disappear from claims.
3. **Repeated raw observations and uncertainty** — Capture at least five independent timed trials per meaningful comparison, units, configuration, warmup/cache details, center/spread and a stated tail-latency sampling limitation rather than a cherry-picked fastest run or fabricated p99 confidence.
4. **Resource ceiling and queue evidence** — Measure or estimate CPU use, memory/heap, file descriptors, queue depth, disk and local network utilization as appropriate, and identify the bottleneck or a valid unresolved pair of causes without inventing a production service ceiling.
5. **Discriminating intervention and correctness** — Compare a targeted change, controlled perturbation or justified no-change choice with the baseline using the same useful-work and failure contracts; detect an apparent speedup that drops work, weakens durability or shifts burden into the client.
6. **Measured trade-off, negative cases and maintainable regression decision** — Compare the selected implementation or algorithm alternative against raw effect/uncertainty, resource demands, portability, maintenance and operational risk. Retain a reproducible correctness and finite performance guard, including an inconclusive or harmful option, and defend optimize/revert/retain/no-change without cherry-picking throughput or inventing an SLA.

### Module 6 — Operator Handoff, Privacy and Responsible Release

#### Outcomes

- SYS9-O9
- SYS9-O10
- SYS9-O13

#### Lessons

1. **Attributed clean build, nonprivileged install and safe cleanup** — Publish exact source commit, dependency/license/assistance inventory, pinned Rust toolchain and lockfile, synthetic fixtures, accepted target/OS assumptions and nonprivileged build/start/config commands. Keep state, socket and temp paths entirely learner owned, with numeric resource budgets and cleanup that cannot damage unrelated data or require credentials or root.
2. **Readiness, liveness and supported operations** — Define meaningful health checks that distinguish a running process from a service able to uphold its actual contract, including a quorum or storage-recovery requirement if those mechanisms were chosen.
3. **Configuration and secrets without private prerequisites** — Use synthetic values, typed validation and safe refusal for invalid state, and demonstrate no credentials, user payloads or raw keys are included in public logs/trace fixtures.
4. **Actionable failure runbook, independent rehearsal and release judgment** — Write one symptom-to-diagnosis, stop-admission, safe shutdown/restart and ambiguous-work runbook tied to the actual mechanism; have another reviewer or independent scripted procedure reproduce it from fresh state and compare expected versus actual outcomes. Correct unusable steps and make a defensible limited-local-release or no-go decision rather than calling a green startup production certification.
5. **State preservation, backup or reset procedures** — Where applicable, specify how to recover committed state or safely restore a supplied fixture/backup. A destructive reset is allowed only for a disposable learning directory and must never masquerade as preserving acknowledged data.
6. **Compatibility and safe rollback boundaries** — Describe supported binary/protocol/storage versions and when a rollback is unsafe after state migration; provide a bounded release gate/hold procedure rather than promising a complete deployment platform.
7. **Accessibility, privacy and ethical impact** — Provide readable text alternatives to diagrams/plots, bounded synthetic test data, artifact redaction and risks to downstream users from loss, latency, resource abuse or misleading availability claims.

### Module 7 — Independent Reproduction, Unseen Challenge and Revision

#### Outcomes

- SYS9-O6
- SYS9-O7
- SYS9-O10
- SYS9-O12
- SYS9-O13

#### Lessons

1. **Reviewer-independent reproduction and separately derived oracles** — Publish the exact commit, fixture seed, deterministic run order, bounded commands and expected user-visible output in an independently reproducible bundle. Separate the learner's previously written tests from reviewer-generated challenge input and an independently calculated oracle; passing a copied golden fixture is not proof of transferable understanding.
2. **Fair unfamiliar-case envelope and equivalent defense access** — Prepublish the bounded allowed novelty classes—invalid input, race, failure, demand change or resource bound—without revealing a specific future variant or requiring new professional infrastructure. Permit written, recorded, live or equivalent accessible technical reasoning under the same evidence standard, with no hidden paid grader or artificial speed-pressure criterion.
3. **Predict two competing causes before execution** — On receiving the unknown case, identify at least two possible mechanisms, an expected discriminating trace or measurement and what each explanation would imply for the published system contract.
4. **Locate the first violated invariant or honest limit** — Use source, model and observed state to distinguish a violated safety property from unsupported behavior or finite experiment limits; show why a lost client response, process crash or noisy benchmark need not mean data loss.
5. **Causal correction, old-case regression and operator safety** — Given a new failure, apply the smallest justified code/config/runbook correction or proven bounded refusal; rerun a reviewer-supplied negative and an existing valid case. Verify that resource caps, safe startup, teardown, secrets/log redaction and compatibility still hold; a material missing core invariant remains a failed assessment rather than disappearing behind a stated limitation.
6. **Reviewer feedback and coherent artifact history** — Publish changed assumptions, one real regression/failure explanation, remaining unknowns, commit or patch provenance and an accountable decision; separate formative comments from the final summative reviewer judgment.

*Formative reviewer prompt:* Given a new failure seed that invalidates an earlier optimization, write two hypotheses and a minimal discriminating experiment before changing source.

### Module 8 — Graduation Defense, Decision Records and Limitations

#### Outcomes

- SYS9-O2
- SYS9-O3
- SYS9-O4
- SYS9-O5
- SYS9-O7
- SYS9-O8
- SYS9-O9
- SYS9-O11
- SYS9-O12
- SYS9-O13
- SYS9-O14

#### Lessons

1. **Demonstrate a real end-to-end accepted operation** — Run or show an independently reproducible clean-state request that crosses the chosen systems boundary with observable bytes/state, declared resource owners and expected-versus-actual outputs.
2. **Demonstrate one meaningful controlled failure** — Exercise an actual faulty/adversarial sequence appropriate to the project with evidence of bounded refusal, recovery or corrected regression; a healthy demonstration alone cannot satisfy the failure requirements.
3. **Source-level ownership, invariants and appropriately limited claims** — Defend the new Rust code and inherited pieces through exact resource, synchronization, command/protocol, error and state transitions, showing which trust, consistency, durability and availability properties follow from observed/model evidence. Identify untested physical fault modes, replay ambiguity, security exposure and alternative architectures instead of conflating local passes with fully proven production guarantees.
4. **Capacity evidence, economic choice and responsible release** — Present raw repeated trial conditions, offered/admitted/completed work, uncertainty and a real resource ceiling, tying an optimization or no-change decision to operational/maintenance costs. State a justified local-go, restricted-go or no-go result with privacy, licensing, reliability and support risks, without turning a successful graduation defense into permission to deploy real customer data.
5. **Defend the unfamiliar correction** — Present the independently supplied challenge, two pre-test hypotheses, discriminating observation, minimal fix/refusal and passing regression or a genuine outstanding blocker; show that the explanation survives a small new variation.
6. **Two independent graduation decisions** — Trace each of the fourteen SYS9 outcomes to accepted assessment evidence and each of the six assessment decisions, *then separately* confirm SYS1–SYS8 and SYS10 predecessor decisions. A failed capstone outcome, missing predecessor mastery or unsupported defense is not cured by time spent, a green CI job or a live demo.

## Completion requirements

**Six required summative evaluations and fourteen capstone outcomes are mandatory**, in addition to, and separately from, the **pre-entry** prerequisite completion decision. AS6 measures unfamiliar-case transfer (O12) and integrative individual authorship defense (O14), while AS1–AS5 independently establish every other outcome; the final defense cannot substitute for a missing mandatory predecessor or project assessment. Assessments are milestones for **one cumulative Rust project**, not six applications, a second SYS curriculum, a mandatory set of stack/vendor technologies or six duplicative reports. Previously reviewed source and genuine prior tests may be reused with provenance; each distinct new criterion still needs evidence. A reviewer must evaluate actual understanding, not merely accept evidence files. Module exercises and informal reviews are formative unless an explicitly listed assessment below requires the resulting performance.

**Mandatory capstone deliverables:** independently buildable Rust source (or declared scoped patch/extension of an attributable base), bounded public interface and architecture/state invariants; normal/boundary/invalid independent verification; controlled failure and repair/containment with replayable fixtures; honest repeated performance evidence with uncertainty; nonprivileged install/start/stop/recovery and privacy-aware runbook; source/assistance/license provenance, material limitation and responsible-release decision; a bounded unfamiliar-case solution; and a reviewable technical defense of authorship, choices, actual results and unresolved risks. All deliverables may be part of a single repository with references rather than repeated in separate binders. The project may be a local tool without any external network listener if a meaningful OS/storage/process boundary meets the actual systems depth.

- **SYS9-AS1** — Admission, Authentic Problem and Systems Engineering Contract
  - **Outcomes:** SYS9-O1, SYS9-O2, SYS9-O3, SYS9-O5, SYS9-O13.
  - **Work:** **Before starting assessed implementation**, verify reviewable prior completion decisions for **SYS1–SYS8 and SYS10** (or independently authorized, revision-scoped outcome equivalence), recording each course, source/spec version, decision and evidence link. Select one meaningful systems problem with a genuine user/operator scenario; define observable valid/invalid behavior, non-goals, numeric resource/trust/failure bounds, one material low-level concurrency/ownership invariant, a necessary networking/storage/process/distributed mechanism and two credible alternative solutions. Disclose inherited components, authorship, third-party/generated assistance, license and sensitive-data risks.
  - **Criteria:** No prerequisite is waved through via capstone work, project promise or self-declared course completion; a missing predecessor results in an admission hold or independently governed equivalence decision, not invented credit. The chosen project can be implemented and verified within the available nonprivileged environment without requiring an entire production platform; its user-visible success, safe refusal, ambiguous outcomes and constraints can be tested independently. The Rust systems contribution genuinely extends prior competence instead of merely repackaging an already-completed course artifact; major security, durability and availability assumptions are honestly bounded and the stated alternatives are compared on meaningful engineering dimensions.
  - **Evidence:** Nine-row predecessor revision/decision/evidence matrix and documented admission outcome, problem/user brief, proposed source/provenance inventory, accepted/invalid/failure scenarios, initial state/resource/threat model, two-option architecture rationale and workload/feasibility notes.

- **SYS9-AS2** — Coherent Rust Systems Implementation and Independently Checked Interfaces
  - **Outcomes:** SYS9-O3, SYS9-O4, SYS9-O5, SYS9-O6, SYS9-O11.
  - **Work:** Implement **one evolving Rust systems component**, reusing attributed predecessor artifacts where justified. Build a valid end-to-end operation crossing an owned resource/concurrency boundary and a meaningful process/network/storage/replication boundary; specify fallible API, format or command transitions, cancellation/partial-progress semantics, numeric input/queue/file/process budgets and safe shutdown. Demonstrate an original capstone-specific constraint, extension or integration that requires substantive new reasoning. Verify normal, boundary and invalid cases against reference outputs derived separately from the program under test and explain one rejected architectural alternative.
  - **Criteria:** Source builds and runs from clean, documented supported tools with versioned dependencies, without undisclosed credentials, root or public traffic. Ownership/cleanup and synchronization invariants hold in tested transitions, no unbounded uncontrolled resource growth occurs within the declared input range, public errors are distinguished from success/unknown, and malformed or unsupported inputs fail predictably. The independently derived oracle checks actual client-observed state or bytes rather than calling implementation internals; test failure means a real discrepancy. The learner can locate and explain the new low-level code, inherited pieces, chosen alternative, partial work and risk without passing through copied documentation alone.
  - **Evidence:** Rust source, Cargo manifest/lockfile and build/run commands, API/protocol/state contract and resource table, source/attribution map, independent golden fixtures and normal/boundary/invalid transcripts, code-level design/ownership notes and reviewable changes.

- **SYS9-AS3** — Controlled Failure, Safety and Recovery Verification
  - **Outcomes:** SYS9-O5, SYS9-O6, SYS9-O7, SYS9-O9.
  - **Work:** Reuse the AS2 project and construct a **risk-derived finite fault matrix** with at least **two different relevant failure families** selected from short/failed I/O, process crash/restart, network/reply loss, cancellation race, malformed trusted state, resource exhaustion or overload. Include one condition where an independently reasoned failure oracle detects an actual defect or unacceptable naïve behavior, followed by a correction **or demonstrated safe containment/refusal**. Exercise normal recovery and an invalid case from disposable learner-created fixtures.
  - **Criteria:** Each fault occurs at a named stage with explicit input/expected/observed results, safe resource cleanup and preservation of any promised acknowledged-state or operation-identity property under the declared model. If the project makes no network/disk guarantee, substitute a genuinely relevant process/queue/coordination fault rather than mandate artificial technologies. Process termination or simulated faults are not called proof of every physical power-loss or cross-host case. The correction prevents the specific failure without breaking previously accepted cases, and the learner distinguishes a demonstrable failed safety invariant from an allowed ambiguous client result. Missing a core required invariant cannot be excused merely by saying the code is educational.
  - **Evidence:** Failure model and two-family injection matrix, source harness/seeds, independent oracle and before/after traces, minimal patch or explicit tested safe refusal, repeated normal/negative regression results, cleanup and residual assurance limitations.

- **SYS9-AS4** — Reproducible Performance and Capacity Decision
  - **Outcomes:** SYS9-O8, SYS9-O9, SYS9-O11.
  - **Work:** Select one end-user critical path on the **same project** and compare at least **two meaningful workloads or resource conditions** with fixed correctness, error semantics and applicable durability mode. Publish actual offered/admitted/completed/failed counts, latency/throughput and relevant CPU, memory, queue, I/O or descriptor demand. Capture **at least five independent raw timed trials per comparable configuration**, record warmup/cache/toolchain and environment limitations, analyze an explicit performance hypothesis and make a supported optimization, redesign, revert or **no-change** decision.
  - **Criteria:** Results preserve independently verified useful work; no invisible speedup from dropped requests, relaxed sync, ignored errors or missing stalled samples. Center/spread, units, sample sizes and measurement biases are visible; tail percentiles are not asserted at an unsupported resolution or averaged incorrectly. The learner identifies a plausible bottleneck, competing explanation and why the selected change or lack of change is proportionate to measured effect, operating cost and maintainability. Local fixtures support only scope-appropriate capacity claims, not invented production SLOs or physical scaling assurances.
  - **Evidence:** Reusable load/benchmark harness, correctness fixtures, exact configuration and raw trial values, independent output/error ledger, measurement summary with uncertainty and competing explanations, code/config change when justified and a regression or no-change rationale.

- **SYS9-AS5** — Independent Operator Reproduction, Provenance and Responsible Release
  - **Outcomes:** SYS9-O9, SYS9-O10, SYS9-O13.
  - **Work:** Produce the same project's reproducible clean-state handoff: build, nonprivileged install/config, bounded start and health/readiness, stop/cancel, supported restart/recovery, troubleshooting of at least one injected condition and safe cleanup. Include fixture-only synthetic secrets, privacy/diagnostic handling, license and assistance provenance, actual platform/portability restrictions, and a responsible local-release/restricted-pilot/no-go decision. Have **another reviewer or an independently reproducible scripted run with reviewer inspection** follow a core operation and failure or recovery path without undocumented local knowledge.
  - **Criteria:** The runbook names exact supported environment and source revisions, uses learner-owned paths and sane numeric caps, and has meaningful expected/observed states that a third party can reproduce. Where persistence exists, a recovery command must not erase acknowledged data; where a remote service exists, a healthy process is not automatically a safe/ready endpoint. Secret/private-data leakage, unsupported permissions and irreversible unsafe rollback are honestly prevented or classified as release blockers. Legal/ethical risk and project maturity are not concealed by a completed demo, and an unverified production readiness claim is disallowed.
  - **Evidence:** Versioned operating package and lockfile, install/start/health/shutdown/recover/troubleshoot commands, synthetic fixture and expected output, independent fresh-state reproduction notes, redaction/permission/security boundary checks, dependency/license/assistance inventory, risk and conditional release decision.

- **SYS9-AS6** — Unfamiliar Challenge, Integration Judgment and Graduation Defense
  - **Outcomes:** SYS9-O12, SYS9-O14.
  - **Work:** Have an independent reviewer or a transparent public generator provide **one previously unseen bounded failure, malformed input, workload change or operational constraint** inside the project's already published failure model and outcome scope. **Before running or observing it**, state two competing causal/architecture hypotheses, a predicted result under each and a discriminating measurement or oracle. Trace the actual events, make a minimal justified correction or changed operating decision or **tested fail-closed containment**, then regress both the unfamiliar case and existing correct fixtures. Independently defend the **entire authored Rust system** in written, recorded, live or equivalent reviewable form, including a normal end-to-end path, material controlled failure, ownership/invariants, prior-course provenance, capacity evidence, alternatives, responsible release and residual risks. **O12 evaluates unfamiliar transfer; O14 evaluates the integrative individual technical defense.** AS1–AS5 retain mandatory proof of all other SYS9 outcomes: defending one variable unseen incident does not automatically re-award those separate capabilities.
  - **Criteria:** The unfamiliar scenario is genuinely new yet bounded by the published project domain: two prior hypotheses and one independently predicted distinguishing observation isolate a causal mechanism, failed invariant or justified refusal **before** a minimal correction or honest hold and regression. The individual defense demonstrates direct understanding of the authored Rust resource/concurrency mechanisms, chosen systems boundary, failure and replay conditions, independently verified useful work, measured trade-offs, inherited code and unproven claims; the evaluator can probe another small case without an undisclosed paid platform. Any unsatisfied required source or safety contract remains a failed earlier assessment, not converted into success by a fluent defense. **O12 and O14 are decided independently**, and AS1–AS5 remain separately required for O1–O11 and O13. A polished demonstration, a copied explanation or a green CI run is not sufficient.
  - **Evidence:** Unfamiliar challenge/seed and pre-observation hypotheses, expected and observed operation/trace table, discriminating test, minimal code/runbook/config delta or bounded refusal, regression and limitations, written/recorded/live defense with concrete technical responses, independent reviewer evaluation tied to IDs and source versions.

### Evaluation integrity and graduation gates

There are **two independent judgments**, not one omnibus capstone pass: **(1)** verified pre-entry completion of SYS1–SYS8 and SYS10 through real reviewed decisions or governed outcome-equivalence; **(2)** accepted evidence and reviewer decisions for **all six SYS9-AS1–SYS9-AS6 and all SYS9-O1–SYS9-O14** under this course revision. The outcome-to-assessment mappings are necessary for traceability but cannot replace substantial evaluation of each competency. The reviewer may ask for clarifying source evidence or a bounded unseen variant when understanding is not established, and **must not invent reviewer signatures, team contributions, earlier assessments or real incidents**.

A learner who has demonstrated rigorous engineering judgment may reasonably recommend **do not deploy** because a production claim exceeds evidence. This can satisfy an ethical/release judgment when all mandatory bounded project capabilities are actually demonstrated; it cannot automatically satisfy a missing low-level implementation, safe failure or independent reproduction requirement. Completed lessons, effort hours, a screenshot, a polished video, a passing test run without interpretation or old code without new assessed integration do not independently confer graduation.

### Academic scope, accessibility, safety and provenance

SYS9 assesses integration, transferable systems judgment and accountable ownership beyond the completed predecessors, **not** a second full assessment of SYS1 architecture, SYS2 Rust syntax, SYS10 kernel subsystems, SYS3 atomics, SYS4 networking, SYS5 storage, SYS6 consensus, SYS7 profiling and SYS8 production operations. A valid capstone combines essential ownership/concurrency and one meaningful systems boundary dictated by its problem; no requirement mandates a cloud, SQL database, cluster, every syscall, B+tree, full Raft implementation or branded monitoring stack. Optional C comparisons, advanced storage, or multi-node fault models are valid only when actually needed and bounded.

All experiments must remain on disposable, locally owned synthetic files/processes/ports with published resource caps. No attack on external systems, live credential exfiltration, destructive host modification, paid cloud or root privileges are required. A reviewer may use independent scripted tests plus a written individual defense when geography, hardware, accessibility or time zone prevents a live presentation; the published same-outcome evaluation standard still applies. Diagrams, charts and sampled traces must have accessible text/tabular alternatives with units and source provenance. Learner privacy is protected in review material; the evaluation record retains only necessary evidence and decision references.

### Reproducibility, historical decisions and status

Keep an exact course/spec revision, source commit, stable outcome and assessment IDs, clean-checkout commands, fixture seeds and expected-versus-observed behavior for each summative decision. This revision consolidates repeated admission, project checkpoint and evidence-hand-off instructions rather than low-level reasoning or genuine independent performance. AS6 now evaluates O12 and O14 alone, with O1–O11 and O13 still independently required under AS1–AS5. Significant changes to this project's public Work/Criteria/Evidence are **prospective to the SYS9 source revision**; prior learner completions and predecessor evaluations remain interpretable under their original course/spec revision and are never silently regraded. Neither repository structural tests nor a hypothetical well-scoped capstone establishes authentic learner graduation or OEE readiness advancement. The public status remains `draft` until real learner and independent reviewer evidence supports the status procedure.

## Optional disciplinary references

These references inform scope and review method; they do not transfer accreditation, require enrollment or substitute for published OEE outcome decisions.

- [ABET Computing Accreditation Criteria 2026–2027](https://www.abet.org/accreditation/accreditation-criteria/criteria-for-accrediting-computing-programs-2026-2027/) — complex computing-problem analysis, design, implementation, evaluation, ethics and communication as separate evidence-worthy competencies, not an assertion that OEE is ABET-accredited.
- [Carnegie Mellon Eberly Center — Creating and Using Rubrics](https://www.cmu.edu/teaching/assessment/assesslearning/rubrics.html) — explicitly stated project-performance criteria, feedback and independently reviewable assessment, including a published capstone rubric illustration.
- [Carnegie Mellon Eberly Center — Align Assessments, Objectives, Instructional Strategies](https://www.cmu.edu/teaching/assessment/basics/alignment.html) — instruction and criterion alignment rather than judging a capstone by demo polish alone.
- [Carnegie Mellon Eberly Center — Program-level assessment](https://www.cmu.edu/teaching/assessment/assessprogram/levels/levels4.html) — direct evidence and program-wide outcome mapping, distinct from individual capstone artifacts.
