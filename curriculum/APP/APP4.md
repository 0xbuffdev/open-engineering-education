# APP4 — Databases & Data Modeling

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `core`
**Prerequisites:** [SEF10](../SEF/SEF10.md) — Software Engineering Foundations
**Duration:** 12–16 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–14 focused hours/week (planning estimate; calibrate with learner evidence)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Engineer durable relational data from first principles, **before**
building a backend framework service. Begin with domain requirements,
entities, keys, functional dependencies, relational modeling and
SQL semantics. Progress through normalized schemas, integrity
constraints, advanced reporting, execution plans, measured index
selection, transaction isolation and concurrency, versioned migrations,
least-privilege data access, tenant separation and independently
verified backup recovery. Finish by building and defending a small,
reproducible data component against explicit invariants and failure
scenarios.

[SEF10](../SEF/SEF10.md) supplies programming, mathematical
reasoning, basic tooling and engineering practices. APP4 is an
independent database foundation rather than an APP3-dependent
backend service specialization.
Database design does not fundamentally require DOM, React,
TypeScript or a backend HTTP framework. Learners may perform the
required work through SQL files and a local command-line client.
[APP3](APP3.md) later integrates these database competencies in
an authenticated framework service; APP5 extends them across
full-stack application boundaries. APP7 owns infrastructure-scale
operations and service release management, not introductory SQL.

**PostgreSQL is the recommended open-source reference engine.**
It provides concrete facilities for explain plans, SQL constraints,
MVCC/isolation, roles, row-level security and local dump/restore.
A local self-managed PostgreSQL instance, disposable databases,
`psql`, SQL scripts and synthetic records suffice; optional
adapters may use a pre-provisioned free driver. Engine-specific
statements must be identified as such. Alternative free
relational systems may be used when the learner can actually
demonstrate **equivalent claimed outcomes and evidence**;
a substitute without enforced row-level access or an honest
isolation experiment is not sufficient for those outcomes.

A learner can install or receive the reference tooling through
a public download or local pre-provisioning and then execute
required assessments **offline**, without a paid cloud account,
external database, Internet-accessible server, proprietary GUI,
third-party API, domain, production data, superuser OS privileges
or public hosting. A learner-controlled disposable local cluster
may require a database administration role for initial fixture
setup, but security assessments must run against a genuinely
restricted non-owner test role. Never ask learners to change a
shared or production database or disclose credentials.

**Precision matters.** Relational theory explains logical
constraints, while particular systems implement transactions,
optimizers, index access and isolation differently. PostgreSQL
`READ UNCOMMITTED` behaves as `READ COMMITTED`, and PostgreSQL
`REPEATABLE READ` prevents phantom reads even though the SQL
standard permits them at that level. Its table owners and
privileged bypass roles can evade row-level policies unless
appropriately constrained. Logical backups do not necessarily
include all cluster-level roles or configuration. Learners must
demonstrate these boundaries rather than memorize slogans.

The 12–16-week duration is a provisional estimate from the
breadth of design, SQL investigation, concurrent-session
reasoning, migration rehearsal, query benchmarking and tested
restoration. It is **not** evidence of course readiness. Lessons
provide focused explanation, investigations and practice.
Only the assessments in Completion requirements establish
required summative evidence; formative steps are not hidden
graduation obligations.

## Learning outcomes

- **APP4-O1:** Translate bounded application requirements and data-access questions into a coherent relational model, identifying entities, relationships, cardinalities, ownership, data lifecycle, and explicit assumptions.
- **APP4-O2:** Design and justify relations, keys, functional dependencies, normalization choices, and database-enforceable integrity constraints; explain where an invariant instead requires a transaction or trusted application boundary.
- **APP4-O3:** Write and verify correct SQL reads and writes involving filtering, joins, subqueries, grouping, NULL semantics, duplicates, and deterministic ordering, with independently calculated expected results.
- **APP4-O4:** Produce and audit analytical SQL with common table expressions and window functions; demonstrate correct treatment of missing values, ties, aggregate grain and query-result reproducibility.
- **APP4-O5:** Apply atomic data changes, explicit constraints and transaction-safe write policies; demonstrate normal, invalid, duplicate and partial-failure behavior without silently losing or corrupting committed data.
- **APP4-O6:** Interpret database execution plans, access paths, cardinality estimates and index choices; conduct a repeatable query experiment and justify both benefits and write/storage costs with qualified measurements.
- **APP4-O7:** Explain ACID properties, MVCC/snapshot behavior, isolation levels, locks and representative concurrency anomalies; reproduce an anomaly and demonstrate a defensible mitigation with appropriate retry behavior.
- **APP4-O8:** Plan, implement and validate incremental schema/data migrations that protect integrity and declared old/new consumer compatibility; distinguish a safe reversal from restoration or forward repair when data is irreversibly transformed.
- **APP4-O9:** Enforce and test least-privilege database access and multi-tenant data separation, including parameterized statements, server-side authorization boundaries and negative-path evidence that does not rely only on application filters.
- **APP4-O10:** Create and verify a restorable, appropriately consistent local database backup, document the recovery scope and limitations, and rehearse a failed-change recovery with measured and qualified restoration evidence.
- **APP4-O11:** Publish a small, independently testable data-access contract using SQL scripts or a minimal local adapter, with explicit transactions, parameter handling, expected results and error classification, without requiring a Web framework.
- **APP4-O12:** Deliver, reproduce, improve and defend a cohesive relational data component against published requirements, including a previously unseen bounded change or fault and evidence-backed engineering trade-offs.

## Modules

### Module 1 — Relational Purpose, Local SQL and Domain Questions

#### Outcomes

- APP4-O1
- APP4-O3

#### Lessons

1. **Relational Domain Purpose and Requirements** — Use a fictional lending or inventory problem to identify durable facts, derived/cache state, entity ownership, relevant data-access questions and preservation needs. Situate relational systems historically in one concrete authoring task, not a separate orientation lesson; record data assumptions and constraints.

2. **Relations, Tuples, Attributes, and Domains** — Relate mathematical sets and predicates to practical SQL tables, rows and columns; explain how SQL bags, NULLs and ordering differ from the idealized relational model.

3. **Database, Session and Safe Local Fixture** — Identify server, database, schema, connection and SQL client roles while setting up a disposable local PostgreSQL environment with synthetic data, recorded versions and reliable teardown; distinguish engine behavior from SQL standard guarantees.

4. **First Query and Model Counterexample** — Create a minimal relation, execute a small SELECT and compare with independently expected rows; use an impossible or duplicated business fact to expose a modeling assumption that the schema cannot yet enforce.

*Optional practice — Investigation: A Misleading Table:* Explain why one wide, duplicated spreadsheet-like table cannot reliably represent every domain update; propose a bounded relational decomposition.

### Module 2 — Entities, Keys, Dependencies and Normalization

#### Outcomes

- APP4-O1
- APP4-O2
- APP4-O5

#### Lessons

1. **Entity Identity and Relationships** — Model one-to-one, one-to-many and many-to-many relationships using explicit keys and referential constraints; explain junction tables and optional participation.

2. **Candidate, Primary, and Foreign Keys** — Derive identity from domain facts, compare natural and surrogate identifiers, and distinguish uniqueness from a policy of stable external identifiers.

3. **Functional Dependencies** — Infer supported dependencies from stated business rules; separate accidental sample-data correlation from a genuine constraint.

4. **Normalization, Lossless Change and Denormalization** — Diagnose insert/update/delete anomalies, derive a justified 1NF–3NF decomposition and a bounded BCNF exception, and check meaningful lossless joins and dependency-enforcement trade-offs rather than treating higher forms as a score.

5. **Missingness, Lifecycle and Domain Meaning** — Explain nullable/optional relationships with a data dictionary of units, field meaning, ownership and lifecycle, and test PostgreSQL NULL effects on uniqueness, predicates and referential links against actual domain rules.

*Optional practice — Schema Review:* Compare two designs against a counterexample dataset and demonstrate which one preserves stated identities and modification invariants.

### Module 3 — SQL Queries, Results and Bounded Data Changes

#### Outcomes

- APP4-O2
- APP4-O3
- APP4-O5

#### Lessons

1. **Typed Values and SQL's Three-Valued Predicates** — Choose safe storage types for IDs, money and timestamps, then predict filtered query results with TRUE/FALSE/UNKNOWN including NULL edge cases; do not repeat schema normalization.

2. **Joins and Cardinality** — Implement INNER, LEFT and selected other joins; predict row multiplication and distinguish missing matches from duplicate matches.

3. **Grouping and Aggregate Meaning** — Use COUNT variants, SUM, MIN/MAX, GROUP BY and HAVING with explicit group grain and null-handling policy.

4. **Subqueries, EXISTS, and Set Semantics** — Compare EXISTS, NOT EXISTS and IN/NOT IN behaviors, especially with NULLs; use tests to confirm expected matches.

5. **INSERT, UPDATE, DELETE, and RETURNING** — Write bounded data modifications with clear predicates, affected-row checks and transaction boundaries; inspect unintended unqualified updates before execution.

6. **Ordering, Pagination, and Determinism** — Explain why tables and query results lack guaranteed row order without ORDER BY; use stable tie-breakers and describe offset/keyset trade-offs.

*Optional practice — SQL Counterexamples:* Predict and verify result sets containing zero matches, duplicated relationships, nulls and tied sort keys using independently computed expected rows.

### Module 4 — Analytical Queries and Independent Reporting

#### Outcomes

- APP4-O3
- APP4-O4

#### Lessons

1. **Aggregation Grain and Double Counting** — Identify the grain of each fact table and explain why joining multiple one-to-many relations can inflate totals.

2. **Common Table Expressions** — Use CTEs to structure a readable multi-step query while recognizing that optimizer behavior is version- and query-dependent.

3. **Window Results, Rankings and Ties** — Compute ranks, running totals and row numbers using PARTITION BY and explicit ORDER BY; distinguish row-preserving window calculations from GROUP BY and record ties and NULL ordering so outputs can be reproduced.

4. **Conditional Aggregates and Missing Records** — Test filters, CASE expressions and empty groups; distinguish missing rows from zero results and null results.

5. **Date Buckets and Time Interpretation** — Represent reporting intervals, time zones and inclusive/exclusive time bounds explicitly rather than assume timestamp strings encode local time.

6. **Independent Reporting Oracle and Repair** — Calculate a small expected report from source rows without copying the SQL logic, then reproduce and repair a wrong grain, inflated join total, nullable filter or unstable tie. Discuss a bounded recursive CTE only where the domain actually requires hierarchical traversal.

*Optional practice — Report Audit:* Fix a wrong total, unstable tie or unexpected NULL omission and defend the correction using source rows and expected result tables.

### Module 5 — Database-Enforced Invariants and Safe Writes

#### Outcomes

- APP4-O2
- APP4-O5

#### Lessons

1. **Declarative Constraints and Enforcement Timing** — Implement appropriate NOT NULL, CHECK, PK, FK and UNIQUE rules, explain cross-row limits, and contrast immediate and deliberately deferred constraint evaluation without mistaking constraints for authorization.

2. **Identity Generation, Conflict Handling and Retry Meaning** — Explain sequence/default generation including nonrollback sequence consumption, and select a justified INSERT ON CONFLICT policy without equating upsert with exactly-once distributed execution.

3. **Transaction-Scoped Multi-Row Operations** — Apply related writes in one transaction and prove a declared invariant survives a failed intermediate statement.

4. **Cross-Row Invariants and Trigger Limits** — Compare transactional application SQL with a narrowly justified trigger or database procedure for a cross-row rule; state concurrency and readability costs instead of assuming a trigger by itself prevents races.

5. **Negative-Path Integrity Tests** — Attempt invalid references, double claims, impossible quantities and failed multi-row updates in disposable sessions; inspect rejection versus silent acceptance.

*Optional practice — Repair without Data Loss:* Correct a flawed constraint or write statement and re-run both valid and invalid fixtures to prove the improvement.

### Module 6 — Execution Plans, Index Selection and Measured Trade-offs

#### Outcomes

- APP4-O3
- APP4-O6

#### Lessons

1. **Execution Paths, Statistics and Selectivity** — Explain scan and join choices as physical implementation of an unchanged SQL result, comparing planner estimates, statistics and actual row counts, including stale-statistics counterexamples.

2. **B-Tree Indexes and Composite Ordering** — Explain search keys, leading columns, range predicates and sort support with concrete index layouts.

3. **Safe EXPLAIN and Statement Effects** — Interpret plans and timed EXPLAIN ANALYZE results, remembering that ANALYZE executes writes. Run only with disposable fixtures: ROLLBACK may not reverse sequence increments or external side effects, so inspect final state.

4. **Designing a Controlled Query Experiment** — Use synthetic data at appropriate scale, record warmup, plan, row count and run conditions, and compare repeated trials without manufacturing performance conclusions.

5. **Index Decisions, Maintenance and Measurement Limits** — Compare a query rewrite/index with write and storage costs, autovacuum, cache warmth and environment effects; reject universal speedup claims based on a single synthetic plan.

6. **Pagination and Bounded Work** — Analyze OFFSET growth, deterministic keyset pagination, limit/ordering correctness and input bounds on potentially expensive queries.

*Optional practice — Index Decision:* Recommend, reject or revise an index based on observed plans and stated write/read workload rather than an unsupported rule of thumb.

### Module 7 — Transactions, MVCC, Isolation and Conflict Recovery

#### Outcomes

- APP4-O5
- APP4-O7

#### Lessons

1. **Atomicity, Consistency, Isolation, Durability** — Relate ACID terms to concrete application invariants, failure boundaries and storage guarantees; avoid treating a transaction as a substitute for a correct schema.

2. **MVCC and Snapshot Visibility** — Trace committed and uncommitted versions across two SQL sessions and distinguish a snapshot from a physical database copy.

3. **Isolation Semantics and a Reproducible Two-Session Anomaly** — Trace a real stale-read/read-modify-write failure under Read Committed or write skew under Repeatable Read with exact interleaving and final invariant. PostgreSQL treats READ UNCOMMITTED as READ COMMITTED and prevents Repeatable Read phantoms; do not claim a conflict that the engine disallows.

4. **Serializable Failures and Whole-Transaction Retry** — Reproduce a serialization conflict under a stated test fixture, then defend bounded retries of the complete transaction with fresh reads, avoiding duplicated external side effects.

5. **Explicit Locks and Deadlocks** — Use row-level locking or a documented alternative to protect a stated invariant; explain deadlock detection and why lock order and short transactions matter.

6. **Commit Failure and External Side Effects** — Separate database atomicity from sending an email or calling another service; introduce the need for outbox/idempotency strategies without teaching the full APP3 service course.

*Optional practice — Two-Session Investigation:* Record an interleaving table with initial state, each session's actions, observed results and the corrected mitigation.

### Module 8 — Versioned Migrations, Data Backfills and Compatibility

#### Outcomes

- APP4-O2
- APP4-O5
- APP4-O8

#### Lessons

1. **Versioned Schema Ownership** — Maintain ordered SQL migration files with a migration ledger or equivalent reviewable procedure; explain one-time application and schema history.

2. **Non-Destructive Expand-and-Contract** — Add optional structure, backfill safely, coordinate old/new consumers, enforce the new constraint and remove obsolete structure only after compatibility is verified.

3. **Existing-Data Validation and DDL Lock Safety** — Inspect real existing rows before tightening CHECK/NOT NULL/UNIQUE rules, choose staged validation where appropriate and identify PostgreSQL-specific DDL transaction and locking constraints.

4. **Safe Data Backfills and Migration Verification** — Choose bounded batches, checkpointing and repeat-safe transformations that do not duplicate or lose rows; check row counts, integrity invariants, existing query consumers and version compatibility before and after a change; preserve the migration artifact.

5. **Reversal versus Restore versus Forward Repair** — Distinguish changes that are safely reversible from destructive data transformations requiring backup restoration or a separately justified forward correction.

*Optional practice — Rolling-Upgrade Scenario:* Demonstrate two successive consumer versions on an expanded schema and explain exactly when the contract step becomes safe.

### Module 9 — Least-Privilege Access, Tenant Isolation and Injection Safety

#### Outcomes

- APP4-O2
- APP4-O5
- APP4-O9
- APP4-O11

#### Lessons

1. **Threat Model, Restricted Roles and Sensitive Data** — Define actual tenant principals, sensitive data and authorized actions; use GRANT/REVOKE with non-owner/non-superuser/non-BYPASSRLS test roles and distinguish role setup from tested access. Include log, retention and backup exposure limits.

2. **Safe Bound Values and Identifiers** — Demonstrate SQL injection from unsafe interpolation and correct server PREPARE/EXECUTE or checked driver value binding; explain why dynamic identifiers require explicit allowlists and naive psql variable substitution does not count as binding.

3. **RLS Read and Write Policies with Bypass Cases** — Test both USING and WITH CHECK semantics and distinguish policy and privilege decisions, FORCE RLS, table-owner exemptions and superuser/BYPASSRLS privileges under the actual session roles.

4. **Tenant Scoping in Pooled Connections** — Investigate the hazard of a session- or transaction-context tenant identifier surviving a pooled connection; explain why client-controlled context alone is not a trusted identity boundary.

5. **Authenticated Tenant Matrix and Negative Paths** — Exercise cross-tenant SELECT, INSERT, UPDATE, DELETE and RETURNING with real effective-role records, try spoofed or pooled tenant-context data, and verify unauthorized rows remain unchanged; a caller-set session variable is not trusted identity.

*Optional practice — Authorized-Role Test:* Demonstrate a bypass caused by an overprivileged fixture, then repair the roles/policies and capture effective-role evidence.

### Module 10 — Consistent Logical Backup and Independently Tested Restore

#### Outcomes

- APP4-O6
- APP4-O8
- APP4-O10

#### Lessons

1. **Backup Scope, Global Dependencies and Confidentiality** — Compare pg_dump logical snapshots with physical/WAL recovery only to establish scope; identify omitted cluster roles/configuration, table access and protections for exported synthetic data.

2. **Dump Scope and Consistency** — Create a consistent disposable-database logical backup, record the exact database/schema scope, versions, permissions and inclusion/exclusion assumptions.

3. **Restore into a Clean Target** — Use a separate locally controlled target database to rehearse restoration, including schema ordering, role dependencies and failure handling.

4. **Integrity Verification after Restore** — Compare independently defined row/constraint checks, reproducible queries and a bounded checksum or manifest where appropriate; avoid declaring recovery successful from tool exit status alone.

5. **A Bounded Recovery-Point and Recovery-Time Decision** — Compare a real failed-change local restoration with a stated scenario's RPO/RTO goals, record restore timing and possible loss, and explicitly reject extrapolating a single drill to production reliability.

*Optional practice — Interrupted Migration Recovery:* Take a validated backup, inject a safe migration fault into a disposable database, recover into a clean target and explain data that could not be recovered.

### Module 11 — SQL Data-Access Interfaces and Independent Contract Tests

#### Outcomes

- APP4-O3
- APP4-O5
- APP4-O9
- APP4-O11

#### Lessons

1. **A Public SQL Contract and Invariant Ownership** — Define input shape, results, affected rows, error policies and transaction boundaries, separating SQL facts from domain authorization and server service responsibilities.

2. **Local SQL, Prepared Statements and Optional Clients** — Package executable SQL scripts and psql commands with safe value parameters using server PREPARE/EXECUTE or a pre-provisioned free driver; state why psql textual substitution is not an injection defense.

3. **Deterministic Fixture Setup and Teardown** — Initialize synthetic tenants and records in a fresh disposable database and cleanly reset state without requiring root OS access or cloud services.

4. **Independent Verification Oracles** — Write expected result tables and contract tests for joins, duplicates, invalid writes, tenant boundaries and transaction outcomes; do not test only with self-referential query copies.

5. **Schema/Client Compatibility Regression** — Execute an old consumer and revised consumer against a staged schema and verify intended compatibility and explicitly rejected obsolete behavior.

*Optional practice — External-Consumer Review:* Provide another reviewer with just the SQL/scripts, setup instructions and contract; investigate one discovered ambiguity and amend the interface.

### Module 12 — One Integrated Relational Component and Technical Defense

#### Outcomes

- APP4-O1
- APP4-O2
- APP4-O3
- APP4-O4
- APP4-O5
- APP4-O6
- APP4-O7
- APP4-O8
- APP4-O9
- APP4-O10
- APP4-O11
- APP4-O12

#### Lessons

1. **One Domain, Schema and Accepted Evidence** — Choose a bounded two-tenant domain and meaningful data invariants, publish a coherent model and reuse one evolving schema, SQL source and previously reviewed APP4-AS1–AS5 evidence rather than require six unrelated databases.

2. **Queries, Reports and Measured Access Paths** — Integrate independently expected operational/analytical results and one honest index decision with data-integrity tests; refer to already accepted evidence where it evaluates the same capability.

3. **Prove Integrity and Concurrency Behavior** — Record invalid-write rejections and a two-session isolation or locking scenario, then demonstrate mitigation without hidden application-server behavior.

4. **Restrict, Migrate, and Recover** — Run a non-owner tenant authorization matrix, a staged schema migration with old/new consumers, and a separate clean restore with verified invariants.

5. **Unfamiliar Change, Clean Reproduction and Defense** — Diagnose a reviewer-supplied bounded new invariant, denied access, query failure or migration issue, verify repairs and regressions and reproduce the local fixture cleanly. Defend schema, isolation, tenant safety, backup scope and performance limits without inventing production claims.

## Completion requirements

**All twelve APP4 outcomes** must be demonstrated by **six distinct
summative decisions**, usually on **one evolving local database**.
APP4-AS1–AS5 each assess a different competence; APP4-AS6
integrates and challenges the accepted results with an unfamiliar
bounded change and independent defense. Previously accepted
source/test evidence may be referenced rather than duplicated.
Six independent database applications or repeated evidence packets
are not required. Optional formative investigations never become
hidden completion conditions.

| Required assessment | Required outcome coverage | Principal evidence |
| --- | --- | --- |
| `APP4-AS1` — Relational Model, Functional Dependencies and Integrity Design | APP4-O1, APP4-O2, APP4-O3, APP4-O5 | Requirements and domain diagram, data dictionary, functional dependency notes, SQL DDL and fixtures, normalization rationale, query scripts, positive/negative test results and a concise mismatch/correction log |
| `APP4-AS2` — SQL Semantics and Analytical Report Audit | APP4-O3, APP4-O4 | Versioned SQL and synthetic fixture inputs, expected result tables produced independently, observed result comparison, corrected report and a written explanation of duplicates, NULLs and ordering |
| `APP4-AS3` — Execution Plan and Index Trade-off Investigation | APP4-O3, APP4-O6 | Schema and synthetic workload generator, actual plans, repeatable run script/results, before/after integrity verification, a bounded hypothesis and trade-off report with limitations |
| `APP4-AS4` — Transaction Anomaly and Safe Schema Evolution | APP4-O2, APP4-O5, APP4-O7, APP4-O8 | Versioned SQL migrations, two-session action/observation log, initial/final invariant checks, regression tests, old/new consumer compatibility fixtures, fail/retry or recovery evidence and a documented risk decision |
| `APP4-AS5` — Tenant Access Controls and Verified Restore | APP4-O5, APP4-O8, APP4-O9, APP4-O10, APP4-O11 | Role and RLS policy SQL, access matrix and negative test logs with effective-role evidence, prepared-statement or bound-parameter demonstration, backup/restore commands and target inventory, integrity comparisons, recovery measurements and documented limitations |
| `APP4-AS6` — Integrated Relational Data Component and Engineering Defense | APP4-O1, APP4-O2, APP4-O3, APP4-O4, APP4-O5, APP4-O6, APP4-O7, APP4-O8, APP4-O9, APP4-O10, APP4-O11, APP4-O12 | Portable versioned project or repository with DDL/migration/seed SQL, independent expected-result fixtures, read/write contract documentation, normal/negative SQL tests, transaction log, query plan evidence, role matrix, backup/restore drill, clean-start instructions, bounded change history and written/recorded/equivalently accessible defense |

### Shared execution, assessment, and safety boundaries

- Use a documented maintained PostgreSQL release on a disposable
  local cluster/database with a recorded server/client version,
  safe SQL files, synthetic records and freely available tools.
  An equivalently capable open database environment may be
  accepted only when it demonstrably supports the specified
  outcomes; do not fake PostgreSQL-specific guarantees.
- State SQL versus engine behavior explicitly: SQL bags/NULLs,
  query order, NULL distinctness, transaction isolation,
  index paths, row-level security and backup coverage differ
  across systems and sometimes across versions.
- Do not use real learner, customer, tenant, or employee data;
  do not access third-party production endpoints. Local
  database roles, commands and backup files should not
  contain real credentials or unauthorized private records.
  No privileged OS account, commercial service, paid course,
  live Internet connection during evaluation, cloud host,
  GUI tool, or prior APP3 API implementation is required.
- Relational results must be verified against **independent**
  small expected datasets and invariants rather than merely
  cross-checking two equivalent SQL queries. Use explicit
  ORDER BY and tie behavior when result order matters.
- Treat data that came from a client or file as untrusted.
  Use server prepared statements or safe client-side value
  binding for dynamic values; identifiers and raw SQL fragments
  need separately reviewed allowlists. Avoid calling an
  interpolated psql variable a safe driver parameter.
- Test RLS `USING` and `WITH CHECK` behavior from truly restricted,
  non-owner/non-superuser/non-`BYPASSRLS` sessions. Distinguish
  trusted identity/role binding from a caller-controlled tenant
  variable; explicitly challenge forged or stale pooled-session
  context. Owner/superuser bypass must never be hidden behind
  apparently passing tenant-policy checks.
- Concurrency experiments must record actual isolation level,
  session roles, statement interleavings, initial/final
  states, observed errors and retry policy. Do not claim
  `READ UNCOMMITTED` dirty reads or `REPEATABLE READ`
  phantoms were reproduced in PostgreSQL when the engine
  prevents them.
- `EXPLAIN ANALYZE` **executes** the statement. Use only disposable
  data for write-plan experiments: even ROLLBACK does not necessarily
  undo nontransactional sequence increments or external effects.
  Inspect actual final state and never exercise destructive plans
  on a shared database.
- Backup and restore evidence must identify the backup
  method, which database objects/roles it includes, source
  consistency assumptions and the scope of recovery.
  Recreate in a **separate clean target** and test expected
  invariants; a successful dump command or checksum alone
  does not prove the restored data is usable.
- Static schemas, automated query tests, plan snippets and
  screenshots each provide limited evidence. Include the
  actual SQL, execution conditions, rejected paths and
  reasoned explanations where a claim depends on them.
- An independent reviewer may provide an unfamiliar bounded
  requirement, invalid fixture or concurrency schedule.
  A technical defense may be written, recorded,
  synchronous or otherwise reviewable under the same
  published criteria. Do not demand a proprietary platform
  or private assessment service.

### Required summative assessments

- **APP4-AS1** (required relational model, functional dependencies and integrity design)
  - Outcomes: APP4-O1, APP4-O2, APP4-O3, APP4-O5
  - Work: Given a fictional shared-inventory or lending product brief, derive entities, cardinalities, primary/foreign/candidate keys and documented functional dependencies. Create a normalized relational schema and synthetic fixtures, describe one permissible denormalization trade-off, then write bounded read/write SQL. Prove that invalid references, duplicate identities, incompatible quantities and wrong-type/null values are handled by explicit constraints or transactions as appropriate.
  - Criteria: The model represents stated relationships without unintentional duplication or lost updates; key and normalization explanations follow actual requirements rather than sample-data coincidence. Required referential, uniqueness and check invariants are enforced; false assumptions about NULL uniqueness or aggregate results are corrected. The learner distinguishes what a constraint enforces from cross-row or external state that it cannot ensure on its own. Valid and invalid insert/update cases have independently specified expected results.
  - Evidence: Requirements and domain diagram, data dictionary, functional dependency notes, SQL DDL and fixtures, normalization rationale, query scripts, positive/negative test results and a concise mismatch/correction log.

- **APP4-AS2** (required sql semantics and analytical report audit)
  - Outcomes: APP4-O3, APP4-O4
  - Work: Construct a reporting dataset with one-to-many and many-to-many relationships, deliberately duplicated joined rows, missing/null data and tied rankings. Implement a set of SELECT, joined aggregate, EXISTS/NOT EXISTS, CTE and window queries answering published business questions. Independently calculate expected rows for at least one nontrivial report and identify a seeded double-counting, NULL filtering or nondeterministic ordering error.
  - Criteria: Queries return correct rows and aggregates for supplied small fixtures, with declared grain, join multiplicity, three-valued logic and stable tie-breaking. DISTINCT is not used to mask a broken join without justified semantics; a window result is correctly distinguished from grouping. A report error is reproduced, traced to its SQL mechanism and repaired with a regression case.
  - Evidence: Versioned SQL and synthetic fixture inputs, expected result tables produced independently, observed result comparison, corrected report and a written explanation of duplicates, NULLs and ordering.

- **APP4-AS3** (required execution plan and index trade-off investigation)
  - Outcomes: APP4-O3, APP4-O6
  - Work: Given a controlled local dataset and an explicitly specified lookup/report query, capture an initial EXPLAIN plan (and safe EXPLAIN ANALYZE where feasible), formulate an index or query-shape hypothesis, change one variable, then repeat the measurement under recorded conditions. Explain join/access paths, planner estimates versus actual execution, selectivity, write/storage effects and conditions under which the proposal is not beneficial.
  - Criteria: Query semantics remain unchanged and results pass correctness tests before and after optimization. Observed plans, data volume, index definitions, server version, representative timings and measurement variance are reported without cherry-picked universal speedup claims. The recommendation follows evidence, explains scan/index/estimate behavior, and explicitly accounts for writes and maintenance cost. EXPLAIN ANALYZE is not run on destructive statements without a controlled rollback or equivalent safe environment.
  - Evidence: Schema and synthetic workload generator, actual plans, repeatable run script/results, before/after integrity verification, a bounded hypothesis and trade-off report with limitations.

- **APP4-AS4** (required transaction anomaly and safe schema evolution)
  - Outcomes: APP4-O2, APP4-O5, APP4-O7, APP4-O8
  - Work: From a stated inventory/allocation invariant, orchestrate two **actual local PostgreSQL sessions** to demonstrate a Read Committed stale-read/read-modify-write failure or a Repeatable Read write-skew scenario with a published interleaving and observed violating final state. Do not assert a lost update for a concurrent single-statement arithmetic UPDATE that the engine serializes safely. Apply a justified locking/isolation change and bounded **whole-transaction retry** when warranted, then stage a versioned expand/backfill/validate/contract migration with actual old/new consumer fixtures, a seeded failure and independently checked recovery or forward repair.
  - Criteria: Session evidence reproduces the named anomaly and shows an actual invariant violation before mitigation and an intact invariant afterward. Interpret PostgreSQL READ UNCOMMITTED as READ COMMITTED, Repeatable Read's phantom protection, and Serializable retry semantics accurately. The migration preserves declared identities, constraints, consumer compatibility and bounded locking assumptions, with no false claim that irreversible transformations can be rolled back trivially.
  - Evidence: Versioned SQL migrations, two-session action/observation log, initial/final invariant checks, regression tests, old/new consumer compatibility fixtures, fail/retry or recovery evidence and a documented risk decision.

- **APP4-AS5** (required tenant access controls and verified restore)
  - Outcomes: APP4-O5, APP4-O8, APP4-O9, APP4-O10, APP4-O11
  - Work: Using the same synthetic two-tenant schema, configure a genuinely restricted non-owner test role with documented trusted role/tenant identity binding. Demonstrate safe prepared value parameters and explain identifier allowlisting, then test RLS reads (`USING`) and writes (`WITH CHECK`) for cross-tenant SELECT/INSERT/UPDATE/DELETE, including effective-role, owner/BYPASSRLS and caller-forged or stale pooled tenant-context counterexamples. Take a consistent local logical backup, simulate a controlled failed data/schema change, restore into a **separate clean target** and independently re-verify row identities, invariants and restricted access.
  - Criteria: Authorized and denied operations match the actual role/tenant/action matrix, including negative modification cases and verified unchanged protected rows. The session is genuinely subject to policy, and a user-controlled tenant-context variable alone is not accepted as secure identity. Parameter binding cannot be confused with raw SQL/psql string interpolation. Record dump scope, omitted cluster-global roles/configuration, restore commands and independently verified data/policy behavior in the clean target; do not extrapolate local recovery timing into production guarantees.
  - Evidence: Role and RLS policy SQL, access matrix and negative test logs with effective-role evidence, prepared-statement or bound-parameter demonstration, backup/restore commands and target inventory, integrity comparisons, recovery measurements and documented limitations.

- **APP4-AS6** (required integrated relational data component and engineering defense)
  - Outcomes: APP4-O1, APP4-O2, APP4-O3, APP4-O4, APP4-O5, APP4-O6, APP4-O7, APP4-O8, APP4-O9, APP4-O10, APP4-O11, APP4-O12
  - Work: Complete **the same evolving local relational component** whose model, SQL/reporting, transaction, indexing, authorization, migration and recovery behavior was evaluated in APP4-AS1–AS5. Cite accepted prior evidence instead of resubmitting separate databases. Address a new bounded invariant, access attempt, query counterexample or schema-change failure, diagnose the cause, recheck regressions and independently reproduce the project using only SQL scripts/psql or a free local adapter; defend alternatives and limitations without requiring APP3 or public hosting.
  - Criteria: A fresh reviewer can run documented local normal and adverse tests with no hidden cloud access or credential. Actual data/authorization/recovery evidence supports every stated claim, and the unfamiliar change preserves accepted invariants with a demonstrated regression repair. AS6 integration cannot substitute for missing AS1–AS5 evidence. Required tenant, integrity and restoration blockers must be corrected before passing; the defense explains real SQL, index/isolation and recovery trade-offs without unsupported production assurances.
  - Evidence: One versioned source/fixture package, local clean-start instructions, a short outcome-to-accepted-AS1–AS5 evidence index, the new unfamiliar change and observed regression checks, material integration observations and a reviewable written, recorded or otherwise accessible defense. Existing full backup, plan, SQL oracle and transaction logs may be linked rather than duplicated.

### Completion decision, cross-program boundaries, and revision safety

Completion requires an inspectable acceptable decision for
`APP4-AS1` through `APP4-AS6` that collectively establishes
`APP4-O1` through `APP4-O12`. Passing only happy-path queries,
submitting an untested model, or observing a successful backup
exit status is not sufficient. A material violation of a
published integrity, authorization, migration or recovery
criterion must be corrected. Reviewer decisions must identify
the course/spec revision, assessment/outcome IDs, relevant
evidence references, observed limitations and any further
work necessary for a sound decision.

This competency-first editorial reassessment preserves APP4's
subject identity, SEF10 direct prerequisite, twelve public
outcome IDs and six summative assessment IDs. Earlier completion
records remain attributed to their actual course/specification
revision; historical decisions and downstream APP3/APP5 learner
evidence are not silently rewritten by source consolidation.

APP4 is published as an OEE `v0.2.0` **draft**, not learner-tested,
verified or independently pedagogically conforming merely
because its source and structural validation pass.
Follow [OEE Evidence Rules](../../spec/evidence-rules.md)
for reproducibility, proportionality, privacy and truthful
readiness claims.

### Public non-mandatory study references

The references below help learners inspect mechanisms and
version-specific behavior. All mandatory tasks, outcomes,
success criteria and evidence requirements appear above.

- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)
  for relations, SQL and local database exploration.
- [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)
  for keys, constraints and engine-specific treatment of NULL.
- [PostgreSQL queries](https://www.postgresql.org/docs/current/queries.html)
  and [window functions](https://www.postgresql.org/docs/current/tutorial-window.html)
  for SQL correctness and reporting.
- [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html)
  for execution plans, statistics, safe measurement and trade-offs.
- [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
  and [explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html)
  for actual concurrency semantics and anomaly mitigation.
- [PostgreSQL row security policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)
  and [database privileges](https://www.postgresql.org/docs/current/ddl-priv.html)
  for real authorization boundaries and bypass conditions.
- [PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup.html)
  for logical/physical backups and explicit recovery limitations.
- [PostgreSQL server programming / prepared statements](https://www.postgresql.org/docs/current/sql-prepare.html)
  for parameterized server statements and their scope.
