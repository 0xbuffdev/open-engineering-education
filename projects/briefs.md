# Planned Capstone Briefs

These are deliberately scoped professional-style projects, not starter code to rush through. Begin one only after its prerequisites in [curriculum.md](../curriculum.md#capstones) are complete. Create its workspace with `./scripts/new-project-workspace <project-slug>` and select the smallest MVP that can produce the listed evidence.

## P1 — Reliable CLI Data Tool

**Suggested product:** `tidy-ledger`, a Python command-line tool that imports a small CSV expense/habit/measurement log, validates it against a documented schema, normalizes it to JSONL or SQLite, and produces deterministic summaries.

**MVP:** `import`, `validate`, `summary`, and `export` commands; clear error messages; atomic output behavior; help text; 90%+ meaningful branch coverage is a target, not a substitute for good tests.

**Milestones:** define a file format and sample fixtures → implement parser/validation → persist safely → add summaries → add CLI/error tests → package and document.

**Acceptance evidence:** invalid rows never silently change records; repeat imports have documented idempotency behavior; all commands run from a clean virtual environment; README includes a failure/recovery example.

**Stretch:** configurable schemas, streaming large files, or import diff report. Do not add a web UI before the CLI and tests are solid.

## P2 — Systems Service

**Suggested product:** `workbenchd`, a private Rust job-queue/echo-style service for local clients: length-delimited messages, bounded work queue, worker pool, per-client limits, metrics endpoint/logs, and graceful shutdown.

**MVP:** a documented local protocol; multi-client operation; backpressure and timeouts; structured logs/metrics; load test; no leaked descriptors/tasks after shutdown.

**Milestones:** protocol/test client → single-client service → bounded concurrency → cancellation/shutdown → observability → local load/failure tests.

**Acceptance evidence:** tests cover partial I/O, malformed requests, disconnect, overload, and shutdown; benchmark/report names p50/p95/p99 and resource limits; owner of every resource is documented.

**Stretch:** durable job state, TLS using established libraries, or an administrative CLI. Keep it local/private unless deployment security is designed first.

## P3 — Durable Distributed Store

**Suggested product:** `minikv`, a private Rust key-value store with a write-ahead log, checksummed sorted tables, compaction, leader/replica operation, request IDs, fault injection, and recovery proof.

**MVP:** one-node WAL/recovery → LSM lookup/flush → controlled crash injection → two-replica request protocol → retry/deduplication → metrics and fault matrix.

**Milestones:** define API/durability contract → storage/recovery tests → compaction/integrity → RPC → replication → fault/restart suite → benchmark/report.

**Acceptance evidence:** each acknowledgement claim is specified; interruption at each write stage has a tested outcome; duplicate/dropped/delayed requests have client-visible guarantees; benchmarks distinguish workload, hardware, and limits.

**Stretch:** membership changes or snapshots. Do not claim linearizability or production fault tolerance without a proof/test suite that supports it.

## P4 — Evaluated ML System

**Suggested product:** `signal-score`, a reproducible classifier or regressor on an open, non-sensitive tabular dataset. Select a problem without consequential decisions about people; the objective is rigorous evaluation, not model novelty.

**MVP:** dataset card; frozen split; trivial baseline; preprocessing pipeline; at least two model families; cross-validation; held-out evaluation; calibration/error analysis; model card.

**Milestones:** choose/license dataset → data audit → baseline → pipelines/models → evaluation protocol → error analysis → reproducible report.

**Acceptance evidence:** no target leakage; metric matches stated error cost; comparisons share the same split/budget; data/model/config versions and seed reproduce the result; limitations are prominent.

**Stretch:** group-shift analysis, monitoring simulation, or a small non-public demo with synthetic inputs. Do not deploy high-stakes predictions.

## P5 — Safe Generative-AI Service

**Suggested product:** `doc-compass`, a private, bounded RAG or tool-using assistant over a small licensed, non-sensitive corpus such as your own project documentation.

**MVP:** citation-visible retrieval baseline; allowlisted read-only tools; explicit authority boundary; request/response limits; offline evaluation set; injection/failure tests; observability; incident and rollback plan.

**Milestones:** define use/non-use cases → corpus/data card → retrieval baseline/evaluation → bounded orchestration → safety controls → serving/load tests → system card and incident rehearsal.

**Acceptance evidence:** retrieval, unsupported-answer, prompt-injection, tool-denial, overload, and rollback cases are automated or reproducibly exercised; metrics include quality and operational behavior; no sensitive corpus is used.

**Stretch:** human approval for a non-destructive tool, multi-tenant isolation simulation, or deployment to a controlled private environment. Do not grant arbitrary shell, network, or write authority.

## P6 — Authorized Security Assessment

**Suggested engagement:** assess exactly one completed private target—P3 or P5—under a written scope. This is an assessment and remediation project, not a new system build.

**MVP:** rules of engagement; asset/threat inventory; authorized test plan; minimal non-destructive evidence; severity rationale; remediation tickets; retest; residual-risk statement.

**Milestones:** confirm written authorization and stop conditions → review architecture/configuration → execute safe in-scope tests → report → remediate → retest → close or transfer residual risk.

**Acceptance evidence:** every action is in scope; evidence avoids secrets and weaponized payloads; findings are developer-actionable; retest clearly distinguishes fixed, partially fixed, and accepted risk.

**Stretch:** tabletop incident response or secure-design review. Never test external, public, or third-party systems without explicit authorization.
