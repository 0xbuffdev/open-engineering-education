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

**Feasibility, accessibility and workload:** Use stable Rust/Cargo, a nonprivileged local Linux environment, learner-owned synthetic fixtures and a deterministic local process/test harness. No proprietary checker, paid cloud, privileged kernel or external production traffic is required. Public criteria and equivalent accessible text/recorded/written defense options enable independent self-study while allowing a reviewer to supply a new *bounded* variant to test transfer. The **18–24-week** duration at **10–15 focused hours/week** (approximately 180–360 hours) is provisional; work is paced by actual scope, debugging, feedback and revision, never elapsed time as a graduation condition. Educational status stays `draft` until authentic learner and qualified independent review evidence supports a different label.

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

1. **Admission requires completed assessed predecessors** — Audit existing evaluation decisions for SYS1–SYS8 and SYS10, including course/spec revisions, applicable outcome-equivalence approvals and evidence references. A project cannot award or backfill missing predecessor competence, and a completed activity checklist is not an assessed decision.
2. **Prior-art reuse without repeated courses** — Inventory previously built SYS artifacts and suitable openly licensed examples; identify modules that can be reused unchanged, new integrations that require evaluation and work that would merely repeat SYS3/SYS4/SYS5/SYS6 assignments.
3. **Systems problem, people and use context** — Choose a bounded infrastructure or low-level service with a credible user or operator need: durable message processing, fault-aware job runner, streaming protocol service, replication component or equally justified systems tool. State who observes success and why a stock library alone is insufficient.
4. **Feasibility and available resources** — Inventory nonprivileged Linux access, toolchain, CPU/memory/disk/network limits, realistic study time, test fixtures and reviewer availability before selecting an algorithm or deployment requirement.
5. **Problem alternatives and legitimacy** — Compare an existing library, a narrowly composed prior-course component and a new bounded implementation; prefer reuse unless the extra low-level mechanism produces an actual independently assessable engineering capability.
6. **Public scope and explicit non-goals** — State functional boundaries, expected input/output, operational constraints, threat/failure conditions and excluded concerns; defend why attempting every prior SYS technology or a production cluster would dilute one coherent exit capability.
7. **Provenance, license and responsible assistance** — Record external code dependencies, prior personal work, collaborative contributions and any generated assistance used to produce artifacts. Identify the learner's owned design and code decisions, license/privacy obligations and how a reviewer can challenge understanding rather than equate repository authorship with competence.
8. **Admission decision and evidence integrity** — Record a separate reviewed admit/hold/equivalence decision before assessed capstone implementation, linking verifiable predecessor decisions and any missing evidence. If admission is held, the route is to satisfy the outstanding predecessor, not to waive its mastery in SYS9.

*Formative reviewer prompt:* Examine a capstone application with an impressive Rust service but an unreviewed SYS5 assessment and determine the honest admission disposition.

### Module 2 — Engineering Contract, Architecture and Proof Obligations

#### Outcomes

- SYS9-O2
- SYS9-O3
- SYS9-O5
- SYS9-O9
- SYS9-O11

#### Lessons

1. **Externally decidable acceptance behavior** — Describe a small published API or CLI with valid, boundary and invalid operations, response/error semantics, identity rules, bounded capacities and one clean observable success path before writing source.
2. **Resource ownership and lifecycle maps** — Trace the ownership of Rust values, task/thread contexts, buffers, file descriptors, processes, files or sockets actually used by this project. Explain cleanup order across shutdown, cancellation and unexpected errors without repeating Rust language tutorials.
3. **Concurrency and progress invariant** — State an actual synchronization, single-writer or work-queue rule derived from SYS3; include linearization/visibility point where relevant, wait/lock order, cancellation ownership and a case that would violate it.
4. **Network/storage/distributed boundary chosen by need** — Select one substantial SYS4/SYS5/SYS6 domain that materially changes the project's behavior; show its protocol, commit/recovery or membership/consistency semantics without requiring all three domains as feature checkboxes.
5. **Structured error and partial-progress states** — Model which operations are admitted, pending, committed, failed, canceled, retriable or unknown and what clients can legitimately infer. Distinguish a timeout from rollback and a successful write call from a universal durability guarantee.
6. **Trust assumptions and state invariants** — Define input trust, file or message format validation, permission/secret boundaries, legitimate transitions, denied requests and resource exhaustion refusal; align claimed security to exact checks performed.
7. **Design alternatives and trade-off matrix** — Compare at least two credible architecture/algorithm options in a common workload and failure model, including implementation complexity, correctness risk, operational maintenance and measured or explicitly estimated resource demand.
8. **Verification plan and independent oracles** — For every claimed invariant and important output, design a hand-derived or separately implemented normal, invalid and failure oracle and identify which observation would falsify it; never generate expected results from the system under test.
9. **Architecture review and change threshold** — Use a scoped review to reject impossible durability/availability targets, unsafe resource assumptions and unnecessary complexity before coding. Publish criteria for re-opening the architecture if later measurements or defects invalidate it.

### Module 3 — Incremental Rust Systems Construction and Authorship

#### Outcomes

- SYS9-O3
- SYS9-O4
- SYS9-O5
- SYS9-O6
- SYS9-O11

#### Lessons

1. **Minimal integrated vertical slice** — Implement the smallest source-controlled Rust operation crossing the actual chosen boundary (worker plus bounded queue, framed peer plus handler or WAL plus recovered state), with an independently expected output.
2. **New learning versus legitimately reused code** — Identify which prior-course Rust modules are imported, adapted or extended and what capstone-specific integration/new constraints are assessed. A verbatim previously reviewed mini-project with a renamed README does not establish SYS9 implementation mastery.
3. **Public interfaces and versioned data contracts** — Publish typed and bounded API, protocol frames, durable records or job messages as appropriate, including version, size, malformed-input and compatibility behavior; avoid extra serialization technologies without a genuine need.
4. **Failure-aware ownership and RAII** — Demonstrate the project's actual resource owners, fallible construction/destruction and cleanup after partially initialized tasks/files/sockets. Show that errors do not leak clients, leave unjoined work or silently reuse invalid state.
5. **Concurrency and load control integration** — Apply SYS3 synchronization to the real path: single-writer admission, actor ownership, worker queue or lock protocol, termination and backpressure. Verify no broken invariant under multiple clients or operations rather than adding threads decoratively.
6. **Systems mechanism deepening** — Implement one substantive networking, persistence or distributed correctness feature that extends predecessor work: e.g. durable job dedup after restart, bounded streaming checkpoint, safe peer reconnect or term-fenced task processing, with a precise applicable contract.
7. **Partial work, idempotence and error returns** — Handle failed I/O, duplicate input, canceled request, unknown completion and retry under the selected mechanism. Show why a rejected request is observable and why any replay or compensation rule is safe.
8. **Resource caps and adversarial inputs** — Specify numeric limits on byte/frame sizes, queue depths, outstanding tasks, file sizes, disk usage, retries and elapsed test time; reject overlong lengths, invalid paths, unsupported version and resource-exhaustion requests before unbounded allocation.
9. **Build reproducibility and trust boundaries** — Pin Rust toolchain/edition/dependencies, record Linux/target/platform assumptions, and make the clean checkout build work without private secrets, production network, root or unknown external data.
10. **Cumulative checkpoint, not a new mini-project** — Review the same growing source tree with traceable requirements, commits, independent fixture output, unresolved risks and architectural changes, ensuring the next module tests this implementation rather than demands a separate service.
11. **Attribution and code-level defense rehearsal** — Explain critical Rust modules, invariants and error conditions without relying on copied snippets or generated explanations alone; demonstrate a small unseen code-level change to check genuine comprehension.

### Module 4 — Independent Correctness, Adversarial Failure and Recovery

#### Outcomes

- SYS9-O5
- SYS9-O6
- SYS9-O7
- SYS9-O9

#### Lessons

1. **Reference model separate from implementation** — Create a tiny independent sequential or state-transition oracle for the chosen project, with input histories, expected responses and legal recovery states; it must not call the same internal handler that is being tested.
2. **Normal and boundary-contract regression** — Exercise valid commands, zero or maximum configured payload, repeated operation, empty input, shutdown/stop and resource limit; compare observed bytes/state against precomputed expectations rather than treating a green build as a correctness proof.
3. **Malformation and trust-boundary failures** — Inject truncated/oversized protocol or file records, invalid config, unauthorized paths or incompatible versions as applicable; verify safe refusal/containment without leaking secrets, accepting corrupt committed state or crashing other fixtures.
4. **Concurrency and cancellation schedules** — Control overlapping requests, delays, task joins or state changes to challenge a real progress/ownership invariant. Distinguish 'no observed race' from a tested schedule or proof that all interleavings are safe.
5. **Storage and restart cut points** — For a persistence-bearing project, stop a process before/after actual append/sync/acknowledgment and compare acknowledged versus ambiguous post-restart state. If no persistent store is in scope, substitute a meaningful recovery/failure case and explain the omission.
6. **Network failure and unknown completion** — For remote-client designs, inject delayed/duplicated frames, peer disconnect, blocked writer or partition simulation and track retry identity and incomplete outcomes; for strictly local designs, use relevant process/task loss instead of adding artificial networking.
7. **Bounded overload and cleanup** — Saturate a declared queue/file/connection/CPU resource limit under synthetic load, verify backpressure/rejection policy, bounded memory and recovery after cancellation or shutdown, and demonstrate no damage to unrelated host state.
8. **Independent fault-sequence ledger** — Publish a seeded fault timeline with injection stage, expected allowed outcomes, actual behavior and model/platform limitations. Process kill and injected short I/O do not prove universal device power-loss behavior or security.
9. **A real failing or risky case and correction** — Show an authentic failing baseline or a deliberately specified unsafe scenario that the independent checker rejects; make a minimal justified correction or a verified fail-closed limitation, then retain a negative regression. Do not manufacture a fake incident or hide a known material defect.
10. **Evidence limits and assurance conclusion** — Separate fully checked fixture properties from untested machine, concurrency, cryptographic or production guarantees; a test suite can establish only its specified observations, not universal correctness.

*Formative reviewer prompt:* Given a crash after durable storage but before reply, predict valid recovery and client ambiguity, then explain why a repeated retry must not cause a second effect when dedup was promised.

### Module 5 — Performance, Capacity and Evidence-Based Engineering Choices

#### Outcomes

- SYS9-O8
- SYS9-O9
- SYS9-O11

#### Lessons

1. **Choose a meaningful user critical path** — Name the operation and correct work whose latency/throughput matters; distinguish client response from CPU time, queue waiting, disk sync and retries using SYS7's previously learned measurement discipline.
2. **Baseline workloads and reference correctness** — Publish two representative finite workloads or resource conditions (e.g., different payloads, concurrency or durability policy) using the same declared guarantee. Compare accepted/completed/error work to an independent response oracle before timing.
3. **Arrival and waiting accounting** — Choose scheduled-arrival or a correctly caveated response-driven load generator, logging offered, admitted, completed, refused, timed-out and outstanding operations so slow or unavailable requests do not disappear from claims.
4. **Repeated raw observations and uncertainty** — Capture at least five independent timed trials per meaningful comparison, units, configuration, warmup/cache details, center/spread and a stated tail-latency sampling limitation rather than a cherry-picked fastest run or fabricated p99 confidence.
5. **Resource ceiling and queue evidence** — Measure or estimate CPU use, memory/heap, file descriptors, queue depth, disk and local network utilization as appropriate, and identify the bottleneck or a valid unresolved pair of causes without inventing a production service ceiling.
6. **Discriminating intervention and correctness** — Compare a targeted change, controlled perturbation or justified no-change choice with the baseline using the same useful-work and failure contracts; detect an apparent speedup that drops work, weakens durability or shifts burden into the client.
7. **Cost of complexity and alternative trade-offs** — Connect measured effects and uncertain extrapolation to one chosen architectural alternative from the design module, including resource, portability, operational and maintenance costs.
8. **Regression check and honest decision** — Retain reproducible finite performance checks and functional failures while making a supported retain/revert/optimize/no-change conclusion. A negative or inconclusive experiment can be correct engineering evidence.

### Module 6 — Operator Handoff, Privacy and Responsible Release

#### Outcomes

- SYS9-O9
- SYS9-O10
- SYS9-O13

#### Lessons

1. **Source, fixture and dependency provenance** — Provide a reproducible clean checkout/lockfile and artifact inventory describing which code/data originated from prior SYS work, external licenses, generated assistance or new authoring, without requiring proprietary tools.
2. **Nonprivileged installation and safe defaults** — Publish commands for build, configuration, local startup, listen/fixture directory ownership, numeric limits and clean teardown on supported Linux; avoid root, public services and writes outside learner-controlled paths.
3. **Readiness, liveness and supported operations** — Define meaningful health checks that distinguish a running process from a service able to uphold its actual contract, including a quorum or storage-recovery requirement if those mechanisms were chosen.
4. **Configuration and secrets without private prerequisites** — Use synthetic values, typed validation and safe refusal for invalid state, and demonstrate no credentials, user payloads or raw keys are included in public logs/trace fixtures.
5. **Failure operation and incident mini-runbook** — Document at least one relevant alarm/symptom, diagnostic command, stop-admission decision, graceful/hard shutdown, restart and interpretation of ambiguous in-flight work in a format another reviewer can follow.
6. **State preservation, backup or reset procedures** — Where applicable, specify how to recover committed state or safely restore a supplied fixture/backup. A destructive reset is allowed only for a disposable learning directory and must never masquerade as preserving acknowledged data.
7. **Compatibility and safe rollback boundaries** — Describe supported binary/protocol/storage versions and when a rollback is unsafe after state migration; provide a bounded release gate/hold procedure rather than promising a complete deployment platform.
8. **Accessibility, privacy and ethical impact** — Provide readable text alternatives to diagrams/plots, bounded synthetic test data, artifact redaction and risks to downstream users from loss, latency, resource abuse or misleading availability claims.
9. **Independent runbook rehearsal and release decision** — Have a reviewer or clearly independent scripted replication run essential commands from a clean fixture, record actual versus expected, correct confusing steps and defend a restricted local release or no-go decision without claiming production certification.

### Module 7 — Independent Reproduction, Unseen Challenge and Revision

#### Outcomes

- SYS9-O6
- SYS9-O7
- SYS9-O10
- SYS9-O12
- SYS9-O13

#### Lessons

1. **Prepare a reviewer-independent reproduction bundle** — Identify exact source commit, clean build/run commands, pinned dependencies, config examples, fixture bytes, run order and expected output so another person can reproduce without undocumented private state.
2. **Separate learner tests from the reviewer oracle** — Publish criteria and reasonable challenge envelope while allowing a different reviewer-supplied seed/input; independently compute accepted behavior instead of trusting an implementation-generated golden output.
3. **Unfamiliar but bounded challenge definition** — Define permissible novel failure, malformed input, workload shift, shutdown race or resource constraint that exercises a **previously published capstone outcome** without requiring a new full project, paid hardware or an unseen unrelated subject.
4. **Predict two competing causes before execution** — On receiving the unknown case, identify at least two possible mechanisms, an expected discriminating trace or measurement and what each explanation would imply for the published system contract.
5. **Locate the first violated invariant or honest limit** — Use source, model and observed state to distinguish a violated safety property from unsupported behavior or finite experiment limits; show why a lost client response, process crash or noisy benchmark need not mean data loss.
6. **Repair, containment and controlled rerun** — Implement a minimal verifiable correction or a bounded safe refusal and rerun both the novel negative and an earlier valid fixture. If a key required guarantee remains unsatisfied, classify it as an outstanding assessment failure rather than passing by a disclaimer.
7. **Independent test of operator and resource constraints** — Verify that the correction preserves startup, resource caps, teardown, privacy, config and reproducibility without quietly introducing a privileged dependency or new unassessed interface.
8. **Reviewer feedback and coherent artifact history** — Publish changed assumptions, one real regression/failure explanation, remaining unknowns, commit or patch provenance and an accountable decision; separate formative comments from the final summative reviewer judgment.
9. **Accessibility of challenge evaluation** — Support live, written, recorded or similarly reviewable explanations where they establish the same applied reasoning, authorship and unfamiliar-case transfer; avoid time-pressure theater or requiring an inaccessible secret answer key.

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
3. **Explain architecture and source-level authorship** — Defend the learner-owned Rust code, borrowed components, concurrency/ownership invariants, API/state transitions and significant alternatives through direct questions, not a polished diagram or narrated build log.
4. **Explain measured capacity and decision limits** — Present actual raw trial conditions, effect versus uncertainty, key resource ceiling and why any chosen optimization or no-change decision follows from tested evidence rather than unsupported scalability assertions.
5. **Revisit consistency, safety and trust guarantees** — State precisely which durability, ordering, security and availability properties the project proves under its failure model, which errors are detected and which guarantees are *not* established by the local tests.
6. **Defend the unfamiliar correction** — Present the independently supplied challenge, two pre-test hypotheses, discriminating observation, minimal fix/refusal and passing regression or a genuine outstanding blocker; show that the explanation survives a small new variation.
7. **Make a responsible release recommendation** — Distinguish graduation mastery of a bounded educational project from permission to deploy a production service or use real customer data; include confidentiality, license, safety, maintenance and unresolved assurance risks.
8. **Two independent graduation decisions** — Trace each of the fourteen SYS9 outcomes to accepted assessment evidence and each of the six assessment decisions, *then separately* confirm SYS1–SYS8 and SYS10 predecessor decisions. A failed capstone outcome, missing predecessor mastery or unsupported defense is not cured by time spent, a green CI job or a live demo.

## Completion requirements

**Six required summative evaluations and fourteen capstone outcomes are mandatory**, in addition to, and separately from, the **pre-entry** prerequisite completion decision. Assessments are milestones for **one cumulative Rust project**, not six applications, a second SYS curriculum, a mandatory set of stack/vendor technologies or six duplicative reports. Previously reviewed source and genuine prior tests may be reused with provenance; each distinct new criterion still needs evidence. A reviewer must evaluate actual understanding, not merely accept evidence files. Module exercises and informal reviews are formative unless an explicitly listed assessment below requires the resulting performance.

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
  - **Outcomes:** SYS9-O2, SYS9-O3, SYS9-O4, SYS9-O5, SYS9-O6, SYS9-O7, SYS9-O8, SYS9-O9, SYS9-O10, SYS9-O11, SYS9-O12, SYS9-O13, SYS9-O14.
  - **Work:** Have a reviewer or transparent public generator supply a **previously unseen bounded failure, input, workload or operational change** within the learner's published system domain and existing outcome scope. **Before running it**, record **two causal or architecture hypotheses** and a discriminating expected observation. Diagnose the changed behavior using source and independently derived operation/failure oracles; deliver a minimal justified patch, changed operating decision or **tested fail-closed containment**; rerun both the unseen case and previously correct fixtures. Finally provide a written, recorded, live or equivalently reviewable **individual defense** of a normal end-to-end use, a material controlled failure, the new case, code ownership, alternative architectures, measurements, ethical/release limitations and the role of predecessor evidence.
  - **Criteria:** The unknown case tests a real transfer of existing outcomes but does not require unannounced professional infrastructure, a second project or a hidden paid grader. The learner predicts, reproduces and isolates the first violated invariant or accurately demonstrates a supported refusal; any actual flaw in a required core contract must be repaired to the published criteria rather than excused by disclaimers. At least one independent observation differentiates the initial hypotheses, and the change preserves resource, safety, operator and behavioral regression obligations. The reviewer can examine the learner's authored Rust mechanisms and sourced reuse, ask or otherwise inspect substantive reasoning about a new variant, and decide each cited outcome separately. A green CI run, memorized presentation, copied code or unsubstantiated production claim is insufficient.
  - **Evidence:** Unfamiliar challenge/seed and pre-observation hypotheses, expected and observed operation/trace table, discriminating test, minimal code/runbook/config delta or bounded refusal, regression and limitations, written/recorded/live defense with concrete technical responses, independent reviewer evaluation tied to IDs and source versions.

### Evaluation integrity and graduation gates

There are **two independent judgments**, not one omnibus capstone pass: **(1)** verified pre-entry completion of SYS1–SYS8 and SYS10 through real reviewed decisions or governed outcome-equivalence; **(2)** accepted evidence and reviewer decisions for **all six SYS9-AS1–SYS9-AS6 and all SYS9-O1–SYS9-O14** under this course revision. The outcome-to-assessment mappings are necessary for traceability but cannot replace substantial evaluation of each competency. The reviewer may ask for clarifying source evidence or a bounded unseen variant when understanding is not established, and **must not invent reviewer signatures, team contributions, earlier assessments or real incidents**.

A learner who has demonstrated rigorous engineering judgment may reasonably recommend **do not deploy** because a production claim exceeds evidence. This can satisfy an ethical/release judgment when all mandatory bounded project capabilities are actually demonstrated; it cannot automatically satisfy a missing low-level implementation, safe failure or independent reproduction requirement. Completed lessons, effort hours, a screenshot, a polished video, a passing test run without interpretation or old code without new assessed integration do not independently confer graduation.

### Academic scope, accessibility, safety and provenance

SYS9 assesses integration, transferable systems judgment and accountable ownership beyond the completed predecessors, **not** a second full assessment of SYS1 architecture, SYS2 Rust syntax, SYS10 kernel subsystems, SYS3 atomics, SYS4 networking, SYS5 storage, SYS6 consensus, SYS7 profiling and SYS8 production operations. A valid capstone combines essential ownership/concurrency and one meaningful systems boundary dictated by its problem; no requirement mandates a cloud, SQL database, cluster, every syscall, B+tree, full Raft implementation or branded monitoring stack. Optional C comparisons, advanced storage, or multi-node fault models are valid only when actually needed and bounded.

All experiments must remain on disposable, locally owned synthetic files/processes/ports with published resource caps. No attack on external systems, live credential exfiltration, destructive host modification, paid cloud or root privileges are required. A reviewer may use independent scripted tests plus a written individual defense when geography, hardware, accessibility or time zone prevents a live presentation; the published same-outcome evaluation standard still applies. Diagrams, charts and sampled traces must have accessible text/tabular alternatives with units and source provenance. Learner privacy is protected in review material; the evaluation record retains only necessary evidence and decision references.

### Reproducibility, historical decisions and status

Keep an exact course/spec revision, source commit, stable outcome and assessment IDs, clean-checkout commands, fixture seeds and expected-versus-observed behavior for each summative decision. Significant changes to this project's public Work/Criteria/Evidence are **prospective to the SYS9 source revision**; prior learner completions and predecessor evaluations remain interpretable under their original course/spec revision and are never silently regraded. Neither repository structural tests nor a hypothetical well-scoped capstone establishes authentic learner graduation or OEE readiness advancement. The public status remains `draft` until real learner and independent reviewer evidence supports the status procedure.

## Optional disciplinary references

These references inform scope and review method; they do not transfer accreditation, require enrollment or substitute for published OEE outcome decisions.

- [ABET Computing Accreditation Criteria 2026–2027](https://www.abet.org/accreditation/accreditation-criteria/criteria-for-accrediting-computing-programs-2026-2027/) — complex computing-problem analysis, design, implementation, evaluation, ethics and communication as separate evidence-worthy competencies, not an assertion that OEE is ABET-accredited.
- [Carnegie Mellon Eberly Center — Creating and Using Rubrics](https://www.cmu.edu/teaching/assessment/assesslearning/rubrics.html) — explicitly stated project-performance criteria, feedback and independently reviewable assessment, including a published capstone rubric illustration.
- [Carnegie Mellon Eberly Center — Align Assessments, Objectives, Instructional Strategies](https://www.cmu.edu/teaching/assessment/basics/alignment.html) — instruction and criterion alignment rather than judging a capstone by demo polish alone.
- [Carnegie Mellon Eberly Center — Program-level assessment](https://www.cmu.edu/teaching/assessment/assessprogram/levels/levels4.html) — direct evidence and program-wide outcome mapping, distinct from individual capstone artifacts.
