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

Build, measure, fault-test, document and **independently defend one genuine systems component or service**. Acceptable shapes include a durable local message processor, replicated key-value service, fault-aware job runner, bounded streaming network service or useful infrastructure tool. A systems project must apply meaningful low-level ownership and concurrency reasoning together with a justified networking, storage or distributed-state mechanism; it is not required to implement every topic in SYS1–SYS8 and SYS10 as unrelated feature checkboxes. Rust is the primary implementation language, while C comparison may be reused from SYS2 without redoing that course.

**Admission is distinct from integration.** Before starting, demonstrate authentic assessed completion of SYS1–SYS8 and SYS10 or separately governed assessed outcome-equivalence tied to the relevant revisions. The capstone cannot replace uncompleted prior courses. Its project milestones are cumulative and use one learner-owned artifact. Use a nonprivileged local Linux environment with synthetic data and controlled fault injection, not a paid cloud or a real production system. The final defense must demonstrate success, a controlled failure, reasoned engineering choices, reproducible evidence and an unfamiliar reviewer-supplied challenge.

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

### Module 1 — Capstone Admission and Systems Problem

#### Outcomes

- SYS9-O1
- SYS9-O2
- SYS9-O13

#### Lessons

1. **Prior evidence closure** — Verify assessed completion of SYS1–SYS8 and SYS10; record exact revisions/decisions without reproducing every prior course's assignments.
2. **Authentic problem and users** — Choose a focused infrastructure or systems service with a reason to exist and measurable behavior.
3. **Reference solution alternatives** — Compare a simple existing library or architecture against a justified custom component.
4. **Scope and non-goals** — List essential capabilities, excluded features, technical risk and available local resources.
5. **Acceptance and safety criteria** — Write externally observable success, refusal and failure conditions before implementation.
6. **Project ethics and provenance** — Declare dependencies, copied code, license obligations, sensitive data boundaries and limitations.

### Module 2 — Requirements, Invariants and Architecture

#### Outcomes

- SYS9-O2
- SYS9-O3
- SYS9-O5
- SYS9-O9
- SYS9-O11

#### Lessons

1. **Resource and concurrency model** — Define owned buffers, children, tasks, file descriptors and coordination rules.
2. **Data/communication contract** — Specify versioned wire/on-disk formats and trusted/untrusted input limits where applicable.
3. **State invariants** — Describe valid transitions, initialization, commit points and shutdown behavior.
4. **Failure model** — Bound process crash, network loss, disk corruption, overload and other relevant faults.
5. **Architecture alternatives** — Use measured constraints and failure consequences to justify selected components.
6. **Review gate** — Record conflicting requirements or impossible promises and repair the scope before building.

### Module 3 — Incremental Systems Implementation

#### Outcomes

- SYS9-O3
- SYS9-O4
- SYS9-O5
- SYS9-O6

#### Lessons

1. **Vertical system slice** — Implement a smallest meaningful end-to-end operation with independent output oracle.
2. **Dependency isolation** — Separate core logic, OS/network/storage adapters and policy decisions.
3. **Bounded concurrency** — Implement ownership and backpressure appropriate to the chosen service.
4. **Persistent or remote state** — Add a genuinely systems-level storage, networking or distributed behavior with explicit guarantee.
5. **Errors and partial progress** — Make cancellation, incomplete writes, retries or partial commands observable and safe.
6. **Adversarial contract tests** — Exercise invalid sizes, unexpected peer/process state, resource exhaustion and cleanup paths.
7. **Implementation checkpoint** — Explain changed invariants and trade-offs in source rather than constructing artificial module mini-projects.

### Module 4 — Failure, Recovery and Safety

#### Outcomes

- SYS9-O5
- SYS9-O6
- SYS9-O7
- SYS9-O9

#### Lessons

1. **Fault injection plan** — Select failure points that challenge the stated acknowledgement and cleanup contract.
2. **Crash and restart** — Reproduce process-kill and recovery behavior only on isolated synthetic state.
3. **Network and coordination fault** — Where relevant, drop, delay or reorder messages and distinguish unknown completion.
4. **Overload and cancellation** — Validate bounded queues, deadlines and shutdown under stress.
5. **Security boundary checks** — Reject hostile files, frames, configuration and privilege requests in the selected threat model.
6. **Independent negative evidence** — Publish at least one failed baseline and an explained correction or explicit containment.
7. **Recovery guarantees** — Separate tested scenarios from untested hardware, operator and production claims.

### Module 5 — Benchmarking and Operational Work

#### Outcomes

- SYS9-O8
- SYS9-O9
- SYS9-O10
- SYS9-O11

#### Lessons

1. **Output correctness before timing** — Use a reference oracle and fixed workload before collecting benchmark samples.
2. **Resource and latency baseline** — Measure CPU, memory, I/O, queues and p50/tail latency where meaningful.
3. **Independent variation** — Vary one realistic size, concurrency or fault condition and assess scaling limits.
4. **Performance decision** — Test an optimization or explain why the measured trade-off does not justify it.
5. **Run and recover** — Write unprivileged startup, configuration, health, shutdown, backup/recovery and troubleshooting commands.
6. **Incident rehearsal** — Follow the runbook on a fresh fixture and document what an unfamiliar operator might miss.

### Module 6 — Independent Verification and Project Revision

#### Outcomes

- SYS9-O6
- SYS9-O7
- SYS9-O8
- SYS9-O10
- SYS9-O12
- SYS9-O13

#### Lessons

1. **Clean reconstruction** — Build from a clean checkout or equivalent clean environment with pinned dependencies and synthetic data.
2. **Traceability matrix** — Map every required capstone outcome to distinct existing evidence without duplicate submissions.
3. **Unseen challenge** — Respond to a new bounded failure, malformed input, scale requirement or resource constraint set by a reviewer.
4. **Regression and revised design** — Document the failing observation, causality, correction and resulting tests.
5. **Scope honesty** — Disclose remaining risks, unsupported platforms and incomplete safety/performance evidence.
6. **Responsible release gate** — Decide release, restricted pilot or do-not-release with concrete reasoning and accessible review materials.

### Module 7 — Systems Engineering Technical Defense

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

1. **System demonstration** — Run a representative use case with independently recognizable output and resource state.
2. **Failure demonstration** — Show a relevant controlled failure and restart or safe-failure path with observed state.
3. **Architecture defense** — Explain alternative choices, invariants, language/runtime boundaries and risks.
4. **Measurement defense** — Explain baseline, experimental method, uncertainty and whether a proposed optimization is justified.
5. **Unfamiliar question** — Reason through a new counterexample and identify a test or change before asserting a guarantee.
6. **Evidence handoff** — Supply reproduction commands, links to authentic prerequisite decisions and reviewable outcome coverage.

## Completion requirements

The six summative evaluation decisions below operate on **one cumulative project**, not six separate applications or repeated courses.

**Mandatory project deliverables:** complete Rust source and reproducible build, acceptance/failure tests, architecture and requirement record, fault-injection evidence, performance observations, operating and recovery instructions, provenance and responsible-release decision, plus an independently reviewable technical defense. Milestone feedback, routine local tests and reviewer discussions are formative until a required assessment criterion explicitly names the evidence. Passing prerequisite courses is separately verified before entry and does not by itself complete this project.

- **SYS9-AS1** — Admission, Problem and Engineering Contract
  - **Outcomes:** SYS9-O1, SYS9-O2, SYS9-O3, SYS9-O5, SYS9-O13.
  - **Work:** Verify prior SYS1–SYS8 and SYS10 completion evidence, define project objectives, constraints, invariants, threat/failure model and a reason to engineer the selected system.
  - **Criteria:** Every predecessor decision identified by revision and evidence without a blanket capstone waiver; credible exit scope with testable success/failure criteria; non-goals explicit.
  - **Evidence:** Prerequisite completion matrix, user/problem brief, architecture/risk record, acceptance scenarios and reuse/provenance notes.

- **SYS9-AS2** — Bounded Rust Systems Implementation
  - **Outcomes:** SYS9-O3, SYS9-O4, SYS9-O5, SYS9-O6, SYS9-O11.
  - **Work:** Deliver one coherent service or infrastructure component combining justified resource and concurrency models with meaningful networking, storage or distributed-state depth.
  - **Criteria:** Correct clean build and public interface; bounded work/resource ownership; independently derived oracles; no hidden privileged/paid dependency; implementation alternatives defended.
  - **Evidence:** Versioned source, build lockfiles, tests, interface and architecture documents, configuration and reviewable commit history.

- **SYS9-AS3** — Adversarial Failure and Recovery
  - **Outcomes:** SYS9-O5, SYS9-O6, SYS9-O7, SYS9-O9.
  - **Work:** Run fault injection and negative tests covering important operational failure and recovery paths of the chosen system.
  - **Criteria:** Failure/incomplete state is observable; at least one baseline defect or genuinely risky scenario is reproduced and corrected/contained; no untested exactly-once or durability claim.
  - **Evidence:** Failure matrix, seeds/fixtures, before/after traces, independent expected state, regressions and limits.

- **SYS9-AS4** — Performance and Capacity Decision
  - **Outcomes:** SYS9-O8, SYS9-O9, SYS9-O11.
  - **Work:** Measure a real critical path under more than one workload or resource condition and decide whether to optimize or change design.
  - **Criteria:** Correctness preserved; repeated samples and uncertainty disclosed; resource and tail behavior meaningful; decision supported by data including negative results where applicable.
  - **Evidence:** Benchmark harness, raw results, system configuration, hypothesis analysis, figures/table and rationale.

- **SYS9-AS5** — Operator Handoff and Responsible Release
  - **Outcomes:** SYS9-O9, SYS9-O10, SYS9-O13.
  - **Work:** Prepare a reproducible installation, operation, recovery and incident package plus provenance, risk and responsible-release judgment.
  - **Criteria:** Independent reviewer can follow declared commands and fixture recovery; unsafe secret/personal-data exposure avoided; honest release or no-release decision.
  - **Evidence:** Runbook, health/restart examples, fixture artifact, privacy/security check and risk/decision record.

- **SYS9-AS6** — Unfamiliar Change and Technical Defense
  - **Outcomes:** SYS9-O2, SYS9-O3, SYS9-O4, SYS9-O5, SYS9-O6, SYS9-O7, SYS9-O8, SYS9-O9, SYS9-O10, SYS9-O11, SYS9-O12, SYS9-O13, SYS9-O14.
  - **Work:** Resolve an independently supplied realistic fault, change or unusual workload and defend the entire original and revised system.
  - **Criteria:** Reproduce challenge, explain root cause and corrected behavior or safe limitation; demonstrate representative success and failure; answer architectural, evidence and ethical questions.
  - **Evidence:** Challenge prompt, diagnostic trace, patch or defended containment, regression suite, recorded/live/written reviewable defense and limitations.

### Project boundary and technical defense

The evaluator should select an unfamiliar but **bounded** scenario so that independent transfer can be assessed without requiring a new full project. Defense can be live, recorded, written or otherwise reviewable, and must allow the learner to demonstrate authorship, failure reasoning, a technical change and limitations. A missing material failure guarantee, unexplained component or unreviewable evidence cannot be concealed by a polished demo. Prior course artifacts may be reused and extended with explicit source/version attribution; no fabricated learner evaluations, reviewer decisions or operational incidents are accepted.

### Independent reproduction and graduation decision

Required source, fixture state, dependencies, tests, load generator, fault harness and runbooks must reproduce from a clean checkout or equivalently clean state on disclosed supported hardware/OS. Record actual versus expected behavior, resource budgets, measurement uncertainty and limitations. The graduation decision requires **(1)** authentic reviewable predecessor completion for SYS1–SYS8 and SYS10 and **(2)** satisfactory evidence for **all fourteen SYS9 outcomes and six assessments**, including independent technical defense. Time spent, prior-course attendance or an untested project screenshot cannot confer a SYS graduation result. Historical learner evidence remains associated with its original course revision. Course readiness remains `draft` pending learner testing and independent review.
