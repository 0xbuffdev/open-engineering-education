# Project Ladder

Eleven projects, ordered by dependency. Each project has a smallest defensible MVP, a sequence of milestones, and evidence that a reviewer can verify. Do not start at the top of the ladder because it looks impressive; start at the gate.

**Time estimates** are integration time, not the sum of course hours. They assume the prerequisite labs are complete. A project can be extended, but the MVP must be finished first.

---

## P1 — ledgerlab

**Courses:** F1, F2, F3, F6 · **Gate:** F2 + F3 · **Time:** 25–40 h · **Type:** CLI + data

### Question

Can you turn a messy personal data source into a validated, queryable, reproducible tool without hiding failures?

### MVP

A Python CLI that imports a documented CSV/JSONL log, validates it against a schema, normalizes it into SQLite, and produces deterministic summaries.

Commands:

- `import <file>` — validate and load; reject bad rows with row numbers and reasons;
- `list` — filter by date/category, with stable ordering;
- `summary` — totals, counts, and a time-bucketed report;
- `export` — JSON/CSV output with a schema version;
- `--help` and useful exit codes.

### Milestones

1. Write the input schema, fixture files, and failure examples.
2. Build the parser/validator with pure functions and tests.
3. Add SQLite schema, migrations, and idempotent import.
4. Add queries and deterministic summaries.
5. Add CLI, logging, atomic output, and packaging.
6. Write a README with a failure/recovery example and a clean-environment test.

### Acceptance evidence

- Invalid rows never silently change records; each rejection has a reason.
- Repeated imports have documented idempotency behavior.
- A query yields the same result across runs and platforms.
- Tests cover normal, boundary, invalid, and duplicate data.
- The tool runs from a clean virtual environment.
- One bug's root cause is written up.

### Do not

Add a web UI, authentication, or a distributed database. The project is about correctness and interface discipline.

### Stretch

Streaming import for large files; configurable schemas; query plans and indexes; a read-only HTTP API.

---

## P2 — sysprobe

**Courses:** F5, S1, S2 · **Gate:** F5 + S1 · **Time:** 30–45 h · **Type:** Systems tool

### Question

Can you inspect a running process and its binary with enough precision to explain what the OS and CPU are doing?

### MVP

A Rust CLI (with a small C comparison probe) that reports:

- `sysprobe info` — PID/PPID, UID/GID, cwd, executable, environment summary;
- `sysprobe fds` — open descriptors and targets, with permission errors handled;
- `sysprobe maps` — memory regions and permissions from `/proc/<pid>/maps`;
- `sysprobe elf <path>` — ELF class, entry point, sections, imported symbols, interpreter;
- `sysprobe trace <cmd>` — run a command under `strace` and summarize syscall counts/errors.

### Milestones

1. C probes for `/proc`, descriptors, `fork`/`exec`/`wait`.
2. Rust rewrite with `Result`-based errors and tests on synthetic processes.
3. ELF parser (use a crate or parse headers yourself; document the choice).
4. Trace summary with error filtering.
5. Failure tests: permission denied, process exits mid-read, malformed ELF, missing `strace`.
6. README with a process-to-ELF-to-syscall diagram.

### Acceptance evidence

- Works on at least two Linux distributions or kernel versions.
- Handles processes that exit during inspection; no panic.
- Shows a real file-descriptor leak and a real ELF dependency.
- Explains one C/Rust safety difference with evidence.
- No root requirement for normal operation; privilege errors are clear.

### Security

Inspect only processes you own or are authorized to inspect. Do not add ptrace-based injection or credential dumping.

### Stretch

A TUI, `perf trace` backend, cgroup/namespace view, or a small eBPF probe.

---

## P3 — cachebench

**Courses:** S3, S4, S7, S8, S9 · **Gate:** S4 + S9 · **Time:** 40–60 h · **Type:** Measurement + simulator

### Question

Can you measure a memory hierarchy, reproduce a cache effect, and explain the gap between the model and the machine?

### MVP

A benchmark and cache simulator suite:

- pointer-chase latency across working-set sizes (memory mountain);
- sequential/strided bandwidth at several access patterns;
- a configurable set-associative cache simulator with LRU and a replacement-policy comparison;
- a false-sharing experiment with two threads writing adjacent/separated cache lines;
- a NUMA local/remote access comparison where hardware permits;
- a report with hardware, compiler flags, repetitions, and variance.

### Milestones

1. Write the measurement harness and record machine metadata.
2. Implement pointer chase and bandwidth tests; validate against `perf`.
3. Build the cache simulator; validate on small traces against a reference or hand calculation.
4. Add false-sharing and affinity experiments.
5. Write a performance report with a roofline/latency model and limitations.

### Acceptance evidence

- Warm-up and repetition are documented; variance is reported.
- Simulator results match hand-computed cases.
- At least one result contradicts a naive model assumption.
- A false-sharing penalty is demonstrated and explained.
- Hardware limits and unavailable counters are stated.

### Do not

Claim precise cache sizes from a noisy VM without evidence; use `lscpu` and corroborate.

### Stretch

A visual memory mountain, `perf c2c` analysis, huge-page/TLB experiment, or a small `bpftrace` probe.

---

## P4 — workbenchd

**Courses:** S6, S10, S14, S15 · **Gate:** S6 + S10 · **Time:** 60–90 h · **Type:** Network service + operations

### Question

Can you build a concurrent network service that handles partial I/O, overload, failure, and shutdown without leaking resources?

### MVP

A Rust (or C for the learning version) TCP service with a length-delimited protocol:

- multiple clients;
- bounded work queue and worker pool;
- per-client input/output limits;
- timeouts, backpressure, and load shedding;
- structured logs and a metrics endpoint;
- graceful shutdown;
- tests for partial reads/writes, malformed frames, disconnect, overload, and shutdown.

### Milestones

1. Protocol spec and test client.
2. Single-client blocking server; break it with partial I/O and disconnect.
3. Nonblocking/event loop or thread pool with bounded queues.
4. Cancellation, timeouts, and shutdown.
5. Observability: request count, errors, latency histogram, queue depth.
6. Containerize, deploy locally, add SLO/alert/rollback.
7. Load test and failure matrix; write an incident drill and postmortem.

### Acceptance evidence

- No descriptor, thread, or task leak after shutdown.
- Memory stays bounded under a slow/overload client.
- p50/p95/p99 benchmark with stated workload and hardware.
- Readiness failure removes traffic; rollback is demonstrated.
- A crash/restart test shows which state survives.
- One incident timeline and postmortem.

### Security

Local/private deployment only. Add auth before exposing it beyond localhost. Threat-model the protocol, limits, and admin surface.

### Stretch

TLS with a vetted library, durable job state, a simple admin CLI, or Kubernetes manifests with network policy.

---

## P5 — minikv

**Courses:** S12 · **Gate:** S12 · **Time:** 60–90 h · **Type:** Storage engine

### Question

Can you build a durable key-value engine and prove exactly what survives a crash?

### MVP

A Rust storage engine with:

- append-only WAL with framing, checksum, LSN, and fsync policy;
- memtable and immutable memtable;
- SSTable with index, bloom filter, and checksums;
- flush and compaction;
- tombstones;
- point lookup and range scan;
- recovery and a crash matrix;
- a CLI/API and benchmark.

### Milestones

1. Define the durability contract and API.
2. WAL + recovery; test torn/partial/corrupt records.
3. SSTable + bloom filter; validate lookups and scans.
4. Flush/compaction + tombstone lifecycle.
5. Crash injection at each write stage; record survivor set.
6. Benchmark sequential/random read/write and mixed workloads.
7. README with the exact guarantee and limitations.

### Acceptance evidence

- Acknowledged writes survive the documented crash points; unacknowledged writes may not.
- Corrupted records are detected, not silently returned.
- Compaction preserves the latest value and does not resurrect tombstones.
- Recovery is deterministic and tested.
- Benchmark states cache state, hardware, and amplification.
- A precise durability/consistency statement.

### Do not

Call it ACID, linearizable, or production-ready without defining isolation and testing the claims.

### Stretch

MVCC snapshots, range deletes, compression, checksums with repair, or a small query layer.

---

## P6 — raftkv

**Courses:** S11, S12 · **Gate:** P5 + S11 · **Time:** 80–120 h · **Type:** Distributed system

### Question

Can you replicate a key-value store and state the client guarantee under drops, duplicates, delays, partitions, and restarts?

### MVP

Replicated key-value service:

- RPC with correlation IDs and timeouts;
- durable Raft log and persistent state;
- leader election, log replication, and commit rules;
- client request IDs and duplicate suppression;
- read/write API with a documented consistency guarantee;
- fault-injection harness: drop request/reply, duplicate, delay, partition, restart;
- metrics and a fault matrix.

### Milestones

1. RPC layer and deterministic test harness.
2. Durable log and recovery (reuse P5).
3. Leader election; test split votes and terms.
4. Log replication and commit; test an old leader.
5. Client sessions/dedup; test retries and duplicate replies.
6. Snapshot or log compaction (optional but valuable).
7. Fault matrix, availability/latency measurements, and a safety argument.

### Acceptance evidence

- Each fault case states the client guarantee and verifies it.
- No committed entry is lost across the documented crash model.
- Duplicate client requests do not apply twice.
- A partition test shows old-leader behavior and recovery.
- The report states what is not guaranteed.
- Safety argument for election and log matching.

### Security

Local/private cluster only. If networked beyond localhost, add authentication and TLS; do not expose an unauthenticated Raft port.

### Stretch

Membership changes, snapshots, read-index/lease reads, or a Jepsen-style consistency test.

---

## P7 — signal-score

**Courses:** AI1–AI4, AI13 · **Gate:** AI3 + AI4 · **Time:** 50–80 h · **Type:** Applied ML

### Question

Can you produce a reproducible, honestly evaluated prediction system on a non-sensitive dataset?

### MVP

A tabular prediction pipeline:

- licensed, non-sensitive dataset and dataset card;
- frozen split with group/temporal validity;
- preprocessing pipeline with no leakage;
- trivial baseline, linear model, tree ensemble, and small neural baseline;
- cross-validation and held-out test;
- calibration and threshold rationale;
- error analysis and model card;
- one-command reproduction.

### Milestones

1. Data audit and dataset card.
2. Baseline and evaluation protocol.
3. Models and preprocessing pipeline.
4. Cross-validation, tuning, and final test.
5. Calibration, subgroup/error analysis, model card.
6. Reproducibility check from a clean checkout.

### Acceptance evidence

- The metric follows from the real error cost.
- No target leakage or duplicate contamination.
- All models use the same split and budget.
- Seeds/versions/hardware reproduce the result.
- Error analysis includes concrete failures and a subgroup.
- Model card states intended use, non-use, and limits.

### Do not

Use high-stakes decisions about people, sensitive data, or a model you cannot explain. This is an evaluation project, not a product launch.

### Stretch

Conformal intervals, drift simulation, a small read-only demo, or a causal/experiment extension (AI17).

---

## P8 — tinygpt

**Courses:** AI5–AI8 · **Gate:** AI6 · **Time:** 70–110 h · **Type:** Deep learning system

### Question

Can you implement and evaluate a small language model without confusing fluency with capability?

### MVP

A decoder-only Transformer trained on a small licensed corpus:

- tokenizer and corpus card;
- configurable model (layers, heads, width, context);
- causal mask verified by a leakage test;
- training loop with checkpoint/resume and logs;
- held-out loss/perplexity plus one task-level evaluation;
- sampling controls and failure examples;
- parameter/KV-cache memory calculation;
- model card and compute report.

### Milestones

1. Tokenizer audit and corpus split.
2. Attention/mask implementation and shape tests.
3. Training loop and overfit-a-tiny-batch test.
4. Full training run; loss and task evaluation.
5. Sampling and failure analysis.
6. Optional: LoRA comparison (AI7) or scaling report (AI8).
7. Model card, reproducibility check, and one negative result.

### Acceptance evidence

- Causal masking is tested, not asserted.
- Training reproduces from a clean checkout and fixed seed.
- Evaluation uses held-out, deduplicated data.
- Parameter and KV-cache memory are calculated.
- Fluent-but-wrong outputs are shown.
- Limitations and contamination risks are explicit.

### Security

Use licensed/public or synthetic text. Do not train on private data or commit weights/large corpora.

### Stretch

LoRA/DPO experiment, distributed training report, KV-cache benchmark, or a tiny grounded task.

---

## P9 — doc-compass

**Courses:** AI9–AI12, S13 · **Gate:** AI10 + AI12 · **Time:** 70–100 h · **Type:** Applied generative system

### Question

Can you build a bounded generative-AI service with citations, authority limits, evaluation, and rollback?

### MVP

A private RAG/agent service over a small licensed corpus:

- corpus/data card and chunking;
- retrieval baseline and labelled evaluation set;
- grounded answer with citations and abstention;
- allowlisted read-only tools with JSON schemas, max steps, timeouts, and budgets;
- prompt-injection and tool-abuse tests;
- streaming API, rate limits, structured logs, metrics;
- serving benchmark (TTFT, inter-token latency, p50/p95/p99);
- system card, risk register, incident/rollback plan.

### Milestones

1. Corpus, retrieval, and 30–50 labelled queries.
2. Grounded generation with citations/abstention.
3. Bounded agent/tool layer.
4. Evaluation: retrieval, faithfulness, citation, task success.
5. Serving, load test, and one optimization experiment.
6. Safety/red-team suite, system card, and deployment/rollback.

### Acceptance evidence

- Retrieval metrics and answer quality are reported separately.
- Every answer can point to the supporting passage.
- The agent cannot exceed its step/time/tool authority.
- Injection, tool denial, and context overflow have regression tests.
- Quality, latency, and cost are reported together.
- System card names intended use, non-use, and residual risk.

### Security

Use a private corpus and synthetic secrets for tests. Never grant arbitrary shell, network, or write authority. Human approval for consequential actions.

### Stretch

A reranker, hybrid search, canary deployment, human-approval tool, or multitenant isolation simulation.

---

## P10 — secure-review

**Courses:** D1, D2, D3, D9 · **Gate:** D2 + D3 · **Time:** 50–80 h · **Type:** Security engineering

### Question

Can you find, explain, fix, and verify security weaknesses in a system you own, without publishing weaponized material?

### MVP

A private vulnerable/fixed pair plus a secure review:

- rules of engagement and threat model;
- a deliberately vulnerable local app;
- five weakness classes (e.g., memory safety, SQLi, XSS, access control, CSRF/SSRF);
- harmless reproduction and root-cause analysis;
- fixes at the correct layer;
- regression tests that fail before/pass after;
- secure SDLC checks (SAST, dependency, secrets, SBOM);
- developer-facing report and retest.

### Milestones

1. Scope, threat model, and safe lab.
2. Build/choose the vulnerable app; document only benign evidence.
3. Reproduce and diagnose each class.
4. Fix and add regression tests.
5. Add CI checks, SBOM, and artifact verification.
6. Report, retest, and residual risk.

### Acceptance evidence

- Every finding is in scope and reproducible locally.
- Fixes are at the server/root-cause layer, not UI-only.
- Tests prove the vulnerability is closed.
- No secrets, personal data, or weaponized payloads in the repo.
- At least one verified control and one accepted risk.
- SDLC evidence includes a failing check and a passing fix.

### Do not

Test public/third-party systems or publish exploit chains. Keep the vulnerable app clearly marked and isolated.

### Stretch

Container/cloud review (D8), AI red-team (D6), or a threat-model-to-ASVS mapping.

---

## P11 — authorized-assessment

**Courses:** D4–D5, D7–D10 (D6 optional) · **Gate:** D4 + D5 · **Time:** 70–110 h · **Type:** Assessment + remediation

### Question

Can you assess one private system under written authorization and produce a report that changes what the owner does?

### MVP

An assessment of P4, P6, P9, or a local lab network:

- authorization, scope, exclusions, stop conditions;
- asset and attack-surface inventory;
- validated findings (no unvalidated scanner output);
- minimal, non-destructive evidence;
- severity with environmental context;
- remediation guidance and owners;
- retest results;
- residual-risk statement;
- detection/IR or cloud/AI component as relevant.

### Milestones

1. Authorization and test plan.
2. Inventory and architecture/trust review.
3. Safe validation of at least three findings.
4. Report and developer review.
5. Remediate the highest-priority items.
6. Retest and close/accept with evidence.
7. Tabletop or detection drill if D7/D8 selected.

### Acceptance evidence

- Written authorization exists before evidence.
- Every finding is validated and in scope.
- Evidence avoids real secrets/PII and weaponized payloads.
- Severity rationale considers the actual environment.
- Retest distinguishes fixed/partial/accepted.
- The report is useful to a developer, not just a list.

### Do not

Assess a public, employer, school, client, or third-party system without explicit signed authorization. Do not use destructive tests or persistence.

### Stretch

Cloud/Kubernetes assessment (D8), AI red-team (D6), detection/IR drill (D7), or privacy review (D10).

---

## Project selection by track

| Track | Core ladder | Capstone |
| --- | --- | --- |
| Systems | P1 → P2 → P3 → P4 → P5 → P6 | C1 or C2 |
| AI | P1 → P7 → P8 → P9 | C3 |
| Security | P1 → P2 → P4/P5 → P10 → P11 | C4 |

You may skip P3 if you are not targeting performance work, but P4 still requires S9's measurement discipline. You may skip P8 if you are not targeting model training, but P9 still requires AI6-level understanding of the model you serve.

## What makes a project portfolio-grade

- A clear problem and a small scope.
- Tests and failure evidence.
- A design decision with a real alternative.
- A measurement that changed your mind.
- A security/authorization boundary.
- A limitation you can explain without excuses.
- A clean checkout and a five-minute demo.

See [portfolio-guide.md](portfolio-guide.md) for how to present these.
