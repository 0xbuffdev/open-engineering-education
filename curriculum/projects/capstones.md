# Capstones

A capstone is the final integration phase: **harden, evaluate, operate, and explain** a system you already built. It is not a new tutorial project. Each capstone is about 180 hours (roughly 12 weeks at the default pace with buffer).

## Rules common to all capstones

- Prerequisite projects are complete and runnable from a clean checkout.
- The scope is smaller than you want; cut features, not evidence.
- A written design doc, evaluation, threat model, and retrospective are mandatory.
- At least one claim must be tested under failure, load, or adversarial conditions.
- No secrets, private data, model weights, or copyrighted books in Git.
- Security work only under written authorization.
- A reviewer who has not seen the project can run the demo and the evaluation.

---

## C1 — Resilient Backend Platform

**Track:** Systems · **Builds on:** P4 `workbenchd` + P5 `minikv` · **Time:** 180 h · **Prerequisites:** S10, S12, S14, S15; P4 and P5 MVP complete.

### Question

Can you operate a real stateful service with explicit durability, SLOs, failure recovery, and a rollback you have tested?

### Scope

Combine the network service and storage engine into one small platform:

- P4 protocol/service exposes a durable job or record API;
- P5 storage engine persists state;
- containerized deployment with non-root, limits, probes, and persistent volume;
- metrics, logs, traces, dashboards, alerts, and runbooks;
- SLO with error budget;
- backup/restore and crash recovery;
- load test and failure injection.

### Non-goals

Multi-region, autoscaling to thousands of nodes, a full Kubernetes operator, or a general-purpose database. Do not add a UI before the operational evidence exists.

### Phases

| Phase | Weeks | Work | Exit evidence |
| --- | --- | ---: | --- |
| 1. Integrate | 2 | Service → storage API; ownership; error mapping | End-to-end test; no leaked resources |
| 2. Harden | 2 | Limits, timeouts, shutdown, crash consistency | Failure matrix; crash test |
| 3. Deploy | 2 | Container, manifests, secrets, persistent storage | Clean deploy and rollback |
| 4. Observe | 2 | SLI/SLO, metrics, logs, dashboard, alerts | Injected failure detected |
| 5. Prove | 2 | Load, overload, restart, backup/restore | p50/p95/p99; RTO/RPO |
| 6. Explain | 2 | Design doc, incident drill, postmortem, retrospective | Reviewer walkthrough |

### Required deliverables

- `README.md`: problem, architecture, quick start, tests, demo, limitations.
- `docs/design.md`: requirements, components, state ownership, failure handling, decisions.
- `docs/evaluation.md`: workload, hardware, results, variance, limitations.
- `docs/threat-model.md`: assets, boundaries, abuse cases, controls, residual risk.
- `docs/runbook.md`: deploy, rollback, restore, alert response.
- `docs/postmortem.md`: one real/simulated incident.
- Tests and a one-command evaluation.

### Acceptance gate

- [ ] Clean checkout builds and runs the demo.
- [ ] Acknowledged writes obey the documented durability contract.
- [ ] Service stays bounded under overload and shuts down cleanly.
- [ ] SLO/alert fires for a real injected failure.
- [ ] Rollback and restore are demonstrated with timings.
- [ ] A reviewer can explain the architecture from the design doc.
- [ ] Residual risks and non-goals are explicit.

### What can go wrong

- Integration reveals that P4 and P5 have incompatible ownership/error models.
- The storage engine's fsync policy is too slow for the SLO.
- Kubernetes probes restart a healthy-but-slow service.
- The backup exists but the restore has never been tested.
- The dashboard measures the process, not the user journey.

### Stretch

TLS, authentication, multi-tenant isolation, a second node with read replicas, or a chaos test suite.

---

## C2 — Distributed Storage Service

**Track:** Systems · **Builds on:** P5 `minikv` + P6 `raftkv` · **Time:** 180 h · **Prerequisites:** S11, S12, S15; P5 and P6 MVP complete.

### Question

Can you make a replicated store whose client guarantee is precise and whose failure behavior is demonstrated?

### Scope

Harden P6 into a defensible small distributed service:

- durable Raft log and state;
- client sessions, request IDs, and deduplication;
- read/write API with a documented guarantee;
- snapshot/log compaction;
- a fault-injection harness: drops, duplicates, delays, partitions, restarts;
- metrics for leader, term, commit index, lag, and errors;
- availability/latency measurements under faults;
- a safety argument and a clear non-goal list.

### Non-goals

Global scale, multi-datacenter consensus, Byzantine fault tolerance, or production SLA. Do not claim linearizability without a test or proof.

### Phases

| Phase | Weeks | Work | Exit evidence |
| --- | --- | ---: | --- |
| 1. Baseline | 2 | Reproduce P6; add deterministic tests | All fault cases pass/fail as expected |
| 2. Durability | 2 | Crash matrix, snapshot, recovery | No committed loss in model |
| 3. Client contract | 2 | Sessions, dedup, retries, read semantics | Duplicate/retry test |
| 4. Faults | 3 | Partition, delay, restart, old leader | Fault matrix + metrics |
| 5. Evaluate | 2 | Availability/latency under load/fault | Reproducible report |
| 6. Argue | 1 | Safety argument + limitations | Reviewer defense |

### Required deliverables

- README with API, consistency guarantee, and quick start.
- Design doc with Raft state, persistence, client protocol, and failure model.
- Fault matrix: scenario → expected → observed → guarantee.
- Safety argument for election, log matching, commit, and dedup.
- Benchmark and availability report with hardware/network conditions.
- Operational runbook and threat model.

### Acceptance gate

- [ ] Every fault case has an expected and observed outcome.
- [ ] Committed entries survive the documented crash model.
- [ ] Duplicate requests do not apply twice.
- [ ] Old leader cannot silently serve stale writes as fresh.
- [ ] Snapshot/restore or compaction is tested.
- [ ] The report states what is **not** guaranteed.
- [ ] Reviewer can reproduce one partition test.

### What can go wrong

- Tests are nondeterministic and hide races.
- Dedup state grows without bound.
- Snapshot install breaks the log index.
- A read from a follower is presented as linearizable.
- The benchmark measures loopback and claims WAN behavior.

### Stretch

Membership change, read-index/lease reads, a Jepsen-style checker, or a second datacenter simulation.

---

## C3 — Evaluated AI Assistant

**Track:** AI & ML · **Builds on:** P7 `signal-score` + P8 `tinygpt` + P9 `doc-compass` · **Time:** 180 h · **Prerequisites:** AI3, AI6, AI9–AI12; P9 MVP complete.

### Question

Can you build an AI system whose quality, safety, latency, and cost claims are backed by reproducible evaluation and operational evidence?

### Scope

Harden P9 into a complete applied-AI case study:

- documented corpus and data card;
- retrieval + generation with citations/abstention;
- bounded read-only tools and human approval for one action;
- offline evaluation set (retrieval, faithfulness, citation, task success);
- red-team suite (injection, tool abuse, data isolation);
- serving benchmark (TTFT, inter-token latency, p50/p95/p99, cost);
- monitoring, rollback, incident plan;
- system card and risk register.

### Non-goals

Training a frontier model, arbitrary autonomous actions, or high-stakes decisions about people. Do not claim safety from a narrow test pass.

### Phases

| Phase | Weeks | Work | Exit evidence |
| --- | --- | ---: | --- |
| 1. Define | 1 | Use/non-use, corpus, evaluation claims | Predeclared metrics and thresholds |
| 2. Retrieve | 2 | Baseline, chunking, labelled set | Retrieval metrics |
| 3. Ground | 2 | Citations, abstention, faithfulness eval | Quality report |
| 4. Bound | 2 | Tools, limits, injection suite | Regression tests |
| 5. Serve | 2 | Load test, cost, monitoring, rollback | Benchmark + rollback |
| 6. Govern | 2 | System card, risk register, incident drill | Review package |
| 7. Defend | 1 | Case study and demo | Reviewer walkthrough |

### Required deliverables

- README, design doc, data/corpus card, system card.
- Evaluation set and reproducible evaluation command.
- Retrieval/answer metrics with limitations.
- Red-team report and fixed regression tests.
- Serving benchmark with quality/cost trade-off.
- Risk register, incident/rollback plan, and retrospective.

### Acceptance gate

- [ ] Predeclared evaluation exists before the final model/config.
- [ ] Retrieval and answer quality are measured separately.
- [ ] Citations are verifiable or the system abstains.
- [ ] Agent authority is bounded and tested.
- [ ] One injection/tool-abuse finding is fixed and retested.
- [ ] Load/overload behavior is bounded.
- [ ] System card states intended use, non-use, and residual risk.
- [ ] A reviewer can reproduce the evaluation from a clean checkout.

### What can go wrong

- Evaluation is tuned after seeing results.
- Retrieval is good but answers ignore the evidence.
- Prompt injection is "fixed" only in the system prompt.
- Latency is measured without quality or cost.
- The model card claims safety from a tiny red-team suite.
- Private corpus data leaks into logs or Git.

### Stretch

A reranker, canary model migration, human-approval tool, or a second domain evaluation.

---

## C4 — Authorized Security Assessment

**Track:** Security · **Builds on:** P10 `secure-review` + P11 `authorized-assessment` · **Time:** 180 h · **Prerequisites:** D4, D5, D7 or D8, D9/D10 as relevant; P10/P11 MVP complete.

### Question

Can you run a scoped assessment of a private system, produce developer-actionable findings, remediate, retest, and communicate residual risk?

### Scope

Assess exactly one target you own:

- P4/P6/P9, or a local isolated lab network;
- written authorization, scope, exclusions, stop conditions;
- asset/threat inventory;
- validated findings with minimal evidence;
- at least one systems/web finding and one design/process finding;
- detection/IR or cloud/AI component depending on track;
- remediation and retest;
- privacy/retention review;
- executive and technical reports.

### Non-goals

Testing third-party/public systems, destructive exploitation, persistence, or publishing weaponized payloads. This is not a "capture the flag" writeup.

### Phases

| Phase | Weeks | Work | Exit evidence |
| --- | --- | ---: | --- |
| 1. Authorize | 1 | Scope, rules, target snapshot, stop conditions | Signed authorization |
| 2. Model | 1 | Architecture, assets, threat model, test plan | Reviewed plan |
| 3. Assess | 3 | Inventory, validation, minimal evidence | Validated findings |
| 4. Remediate | 2 | Fix highest-priority items, add tests | Patches + regression tests |
| 5. Retest | 2 | Verify fixes, classify residual | Retest table |
| 6. Detect/IR | 1 | Detection or tabletop/incident drill | Timeline + improvements |
| 7. Report | 2 | Technical + executive report, debrief | Reviewer walkthrough |

### Required deliverables

- Authorization/scope record (sanitized).
- Threat model and test plan.
- Findings with evidence, severity, root cause, remediation, owner.
- Retest results (fixed/partial/accepted).
- Detection/IR or cloud/AI evidence as relevant.
- Executive summary and technical report.
- Privacy/data-handling and residual-risk statement.
- Retrospective and disclosure note.

### Acceptance gate

- [ ] Authorization precedes all testing.
- [ ] Every action is in scope; stop conditions are documented.
- [ ] Findings are validated, not scanner output.
- [ ] Evidence avoids real secrets/PII and weaponized payloads.
- [ ] Fixes are verified with tests.
- [ ] Retest distinguishes fixed, partial, and accepted risk.
- [ ] Report is actionable for a developer and readable by a decision-maker.
- [ ] Residual risk has an owner.

### What can go wrong

- Scope creep into production or third-party services.
- Evidence collection exposes credentials.
- Severity is inflated with generic CVSS.
- A partial fix is marked closed.
- The report lists tools, not impact.
- No one owns the residual risk after the engagement.

### Stretch

Cloud/Kubernetes assessment (D8), AI red-team (D6), privacy impact assessment (D10), or a purple-team detection loop (D7/D14).

---

## Choosing a capstone

| If your target is... | Choose | Why |
| --- | --- | --- |
| Backend / platform / SRE | C1 | Service + storage + operations |
| Storage / distributed systems | C2 | Consensus + fault evidence |
| Applied AI / LLM product | C3 | Evaluation + safety + serving |
| AppSec / cloud / red team | C4 | Scope + findings + remediation |

Do **one**. A completed capstone with honest limits is stronger than three half-finished systems.

## Capstone retrospective questions

1. What claim did you believe at the start that the evidence changed?
2. What is the most likely production failure you did not test?
3. Which design decision would you reverse with another month?
4. What did you cut, and why was that the right cut?
5. Can a new engineer run the demo and the evaluation without you?
6. What would you tell a user **not** to trust about this system?
