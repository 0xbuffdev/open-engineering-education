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

This course retains and deepens the important subjects in the
earlier APP4 draft while **removing its obsolete prerequisite
on APP3**. [SEF10](../SEF/SEF10.md) supplies prior programming,
technical reasoning, basic tooling and engineering practices.
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

### Module 1 — Database Purpose, Relational Thinking, and Study Environment

#### Outcomes

- APP4-O1
- APP4-O3
- APP4-O10

#### Lessons

1. **Course Orientation and Database History** — Introduce durable shared data and the progression from file processing and hierarchical/network models to relational systems; locate relational databases within modern application architecture without presupposing an API framework.

2. **Data versus Application Behavior** — Contrast persistent domain facts, derived values, cached representations and ephemeral state; identify ownership, access patterns, retention and consistency questions in a supplied product brief.

3. **Relations, Tuples, Attributes, and Domains** — Relate mathematical sets and predicates to practical SQL tables, rows and columns; explain how SQL bags, NULLs and ordering differ from the idealized relational model.

4. **Database Process, Sessions, and Client Roles** — Identify server, database, schema, connection, transaction and SQL client responsibilities; distinguish language-portable concepts from vendor implementation.

5. **Safe Local PostgreSQL Laboratory** — Prepare a disposable locally controlled PostgreSQL database under ordinary OS-user permissions, record server/client versions, and establish safe teardown and synthetic-data rules.

6. **Requirements-to-Questions Walkthrough** — List entities, user-facing questions, integrity invariants, expected data volume and privacy assumptions for a fictional lending, inventory or reservation problem.

7. **Exploratory Schema and Query** — Create minimal tables with sample records, run SELECT safely, inspect exact results and list model assumptions that require correction.

8. **Formative Investigation: A Misleading Table** — Explain why one wide, duplicated spreadsheet-like table cannot reliably represent every domain update; propose a bounded relational decomposition.

### Module 2 — Entities, Keys, Dependencies, and Normalization

#### Outcomes

- APP4-O1
- APP4-O2
- APP4-O5

#### Lessons

1. **Entity Identity and Relationships** — Model one-to-one, one-to-many and many-to-many relationships using explicit keys and referential constraints; explain junction tables and optional participation.

2. **Candidate, Primary, and Foreign Keys** — Derive identity from domain facts, compare natural and surrogate identifiers, and distinguish uniqueness from a policy of stable external identifiers.

3. **Functional Dependencies** — Infer supported dependencies from stated business rules; separate accidental sample-data correlation from a genuine constraint.

4. **First through Third Normal Forms** — Diagnose repeating groups, partial dependencies and transitive dependencies; choose decompositions that avoid update/insert/delete anomalies.

5. **Beyond Third Normal Form** — Recognize BCNF-style conflicts and the trade-offs of a selective denormalization decision without treating higher normal forms as a universal scorecard.

6. **Nullable Relationships and Missingness** — Model unknown, not applicable and optional data deliberately; explain how SQL NULL affects uniqueness, foreign keys and predicates in the chosen engine.

7. **Evolving Requirements and Data Dictionaries** — Document field meaning, units, ranges, lifecycle and ownership; record a newly discovered cardinality requirement before writing migration SQL.

8. **Formative Schema Review** — Compare two designs against a counterexample dataset and demonstrate which one preserves stated identities and modification invariants.

### Module 3 — SQL Retrieval, Joins, and Data Modification

#### Outcomes

- APP4-O2
- APP4-O3
- APP4-O5

#### Lessons

1. **SQL Tables and Typed Values** — Create domain-appropriate columns, keys and constraints; distinguish numeric versus text identifiers, timestamps, decimal money and engine-dependent representation.

2. **Projection, Filtering, and Three-Valued Logic** — Write SELECT/WHERE queries using explicit predicates and reason about TRUE, FALSE and UNKNOWN when NULL values appear.

3. **Joins and Cardinality** — Implement INNER, LEFT and selected other joins; predict row multiplication and distinguish missing matches from duplicate matches.

4. **Grouping and Aggregate Meaning** — Use COUNT variants, SUM, MIN/MAX, GROUP BY and HAVING with explicit group grain and null-handling policy.

5. **Subqueries, EXISTS, and Set Semantics** — Compare EXISTS, NOT EXISTS and IN/NOT IN behaviors, especially with NULLs; use tests to confirm expected matches.

6. **INSERT, UPDATE, DELETE, and RETURNING** — Write bounded data modifications with clear predicates, affected-row checks and transaction boundaries; inspect unintended unqualified updates before execution.

7. **Ordering, Pagination, and Determinism** — Explain why tables and query results lack guaranteed row order without ORDER BY; use stable tie-breakers and describe offset/keyset trade-offs.

8. **Formative SQL Counterexamples** — Predict and verify result sets containing zero matches, duplicated relationships, nulls and tied sort keys using independently computed expected rows.

### Module 4 — Analytical SQL, CTEs, and Reporting Correctness

#### Outcomes

- APP4-O3
- APP4-O4

#### Lessons

1. **Aggregation Grain and Double Counting** — Identify the grain of each fact table and explain why joining multiple one-to-many relations can inflate totals.

2. **Common Table Expressions** — Use CTEs to structure a readable multi-step query while recognizing that optimizer behavior is version- and query-dependent.

3. **Window Functions and PARTITION BY** — Compute ranks and running totals without collapsing the underlying result set; distinguish window partitions from GROUP BY grouping.

4. **Ranking, Ties, and Stable Ordering** — Compare ROW_NUMBER, RANK and DENSE_RANK; declare tie and NULL positioning policies so a report is reproducible.

5. **Conditional Aggregates and Missing Records** — Test filters, CASE expressions and empty groups; distinguish missing rows from zero results and null results.

6. **Date Buckets and Time Interpretation** — Represent reporting intervals, time zones and inclusive/exclusive time bounds explicitly rather than assume timestamp strings encode local time.

7. **Recursive Queries and Bounded Traversal** — Use a small recursive CTE where justified and impose finite termination or depth checks; document cycles and unsafe unbounded recursion.

8. **Independent Analytical Oracle** — Compute a sample report from a small hand-checkable fixture in plain reasoning or independent code; compare it with the SQL output.

9. **Formative Report Audit** — Fix a wrong total, unstable tie or unexpected NULL omission and defend the correction using source rows and expected result tables.

### Module 5 — Database Integrity, Constraints, and Safe Writes

#### Outcomes

- APP4-O2
- APP4-O3
- APP4-O5

#### Lessons

1. **Constraints as Executable Domain Rules** — Use NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY and CHECK; distinguish shape constraints from cross-row business rules.

2. **Defaults, Generated Values, and Sequence Behavior** — Explain identity generation, default expressions and PostgreSQL sequence gaps, including why sequence increments need not roll back with a failed transaction.

3. **Transaction-Scoped Multi-Row Operations** — Apply related writes in one transaction and prove a declared invariant survives a failed intermediate statement.

4. **Upserts and Duplicate Identity** — Compare unique-conflict handling and idempotent write semantics; avoid equating INSERT ON CONFLICT with general exactly-once processing.

5. **Deferrable Constraints and Ordering** — Investigate when constraint evaluation may be deferred, what remains checked and why this is not an authorization bypass.

6. **Triggers and Derived State** — Use a small trigger as an optional investigation of enforcement trade-offs; explain when declarative constraints and explicit writes are easier to audit.

7. **Negative-Path Integrity Tests** — Attempt invalid references, double claims, impossible quantities and failed multi-row updates in disposable sessions; inspect rejection versus silent acceptance.

8. **Formative Repair without Data Loss** — Correct a flawed constraint or write statement and re-run both valid and invalid fixtures to prove the improvement.

### Module 6 — Indexes, Query Plans, and Performance Experiments

#### Outcomes

- APP4-O3
- APP4-O6

#### Lessons

1. **From Query Meaning to Access Paths** — Distinguish logical query meaning from physical execution and identify sequential scans, index scans and join strategies.

2. **B-Tree Indexes and Composite Ordering** — Explain search keys, leading columns, range predicates and sort support with concrete index layouts.

3. **Selectivity and Statistics** — Inspect row estimates versus actual rows, learn when ANALYZE refreshes planner statistics and avoid presenting a single EXPLAIN estimate as a measurement.

4. **EXPLAIN and Safe ANALYZE** — Read representative plans, distinguish estimated cost from wall-clock time, and explain that EXPLAIN ANALYZE executes a query—including writes unless safely rolled back.

5. **Designing a Controlled Query Experiment** — Use synthetic data at appropriate scale, record warmup, plan, row count and run conditions, and compare repeated trials without manufacturing performance conclusions.

6. **Query Rewrites and Index Trade-offs** — Compare predicate form, join order opportunities, selectivity and an optional covering index while accounting for index storage and write amplification.

7. **Pagination and Bounded Work** — Analyze OFFSET growth, deterministic keyset pagination, limit/ordering correctness and input bounds on potentially expensive queries.

8. **Maintenance and Performance Limitations** — Recognize vacuum/autovacuum, stale statistics, locks and cache effects as reasons benchmark results may vary; distinguish a local result from a production forecast.

9. **Formative Index Decision** — Recommend, reject or revise an index based on observed plans and stated write/read workload rather than an unsupported rule of thumb.

### Module 7 — Transactions, Isolation, Locks, and Retry

#### Outcomes

- APP4-O5
- APP4-O7

#### Lessons

1. **Atomicity, Consistency, Isolation, Durability** — Relate ACID terms to concrete application invariants, failure boundaries and storage guarantees; avoid treating a transaction as a substitute for a correct schema.

2. **MVCC and Snapshot Visibility** — Trace committed and uncommitted versions across two SQL sessions and distinguish a snapshot from a physical database copy.

3. **Read Committed and Repeatable Read** — Demonstrate nonrepeatable-read visibility and explain PostgreSQL's stronger-than-minimum Repeatable Read behavior, including why phantom anomalies are not reproduced there.

4. **Lost Updates and Write Skew** — Build a controlled interleaving with two sessions and evaluate which data invariants each isolation configuration does or does not preserve.

5. **Serializable Transactions and Retry** — Interpret a serialization failure and require a bounded retry of the complete transaction with re-evaluated inputs, rather than a blind retry of one statement.

6. **Explicit Locks and Deadlocks** — Use row-level locking or a documented alternative to protect a stated invariant; explain deadlock detection and why lock order and short transactions matter.

7. **Commit Failure and External Side Effects** — Separate database atomicity from sending an email or calling another service; introduce the need for outbox/idempotency strategies without teaching the full APP3 service course.

8. **Formative Two-Session Investigation** — Record an interleaving table with initial state, each session's actions, observed results and the corrected mitigation.

### Module 8 — Schema Migration, Compatibility, and Change Safety

#### Outcomes

- APP4-O2
- APP4-O5
- APP4-O8

#### Lessons

1. **Versioned Schema Ownership** — Maintain ordered SQL migration files with a migration ledger or equivalent reviewable procedure; explain one-time application and schema history.

2. **Non-Destructive Expand-and-Contract** — Add optional structure, backfill safely, coordinate old/new consumers, enforce the new constraint and remove obsolete structure only after compatibility is verified.

3. **Constraints on Existing Data** — Inspect old rows before adding new CHECK/NOT NULL/UNIQUE constraints; use staged validation or a documented alternative on a realistic fixture.

4. **Index and DDL Locking Risks** — Explain transactionality and operational risks of a schema change, distinguishing transactional DDL from operations with special restrictions.

5. **Data Backfills and Idempotence** — Choose bounded batches, checkpointing and repeat-safe transformations that do not duplicate or lose rows.

6. **Migration Verification and Historical Revisions** — Check row counts, integrity invariants, existing query consumers and version compatibility before and after a change; preserve the migration artifact.

7. **Reversal versus Restore versus Forward Repair** — Distinguish changes that are safely reversible from destructive data transformations requiring backup restoration or a separately justified forward correction.

8. **Formative Rolling-Upgrade Scenario** — Demonstrate two successive consumer versions on an expanded schema and explain exactly when the contract step becomes safe.

### Module 9 — Access Control, Tenant Isolation, and Query Safety

#### Outcomes

- APP4-O2
- APP4-O5
- APP4-O9
- APP4-O11

#### Lessons

1. **Threat Model and Data Classification** — Inventory tenants, confidential fields, authentication claims, database roles and access paths; keep synthetic records and state the trust assumptions.

2. **Privileges, Roles, and Least Authority** — Use GRANT/REVOKE and non-owner, non-superuser session roles; distinguish database privileges from application authorization decisions.

3. **SQL Injection and Bound Parameters** — Show the failure of concatenating untrusted input into SQL; use server PREPARE/EXECUTE to demonstrate statement parameters and explain how an application driver safely binds values.

4. **Object Identifiers and Dynamic SQL** — Explain why parameters bind values rather than arbitrary table/column identifiers; apply explicit allowlists when a query legitimately varies its structure.

5. **Row-Level Security and Its Limitations** — Construct a row-level security example with correct policies, and test as a role that does not bypass them; explain owner, superuser and BYPASSRLS exemptions.

6. **Tenant Scoping in Pooled Connections** — Investigate the hazard of a session- or transaction-context tenant identifier surviving a pooled connection; explain why client-controlled context alone is not a trusted identity boundary.

7. **Negative Access Matrix** — Test cross-tenant reads, writes and update-returning paths under a defined authorization matrix; distinguish policy enforcement from merely adding a WHERE tenant_id clause.

8. **Privacy, Retention, and Audit Trade-offs** — Minimize stored sensitive data, document retention and selective logging, and protect backups and dumps against unintended exposure.

9. **Formative Authorized-Role Test** — Demonstrate a bypass caused by an overprivileged fixture, then repair the roles/policies and capture effective-role evidence.

### Module 10 — Operations, Backups, and Reproducible Recovery

#### Outcomes

- APP4-O6
- APP4-O8
- APP4-O10

#### Lessons

1. **Logical versus Physical Backup** — Explain what a logical pg_dump captures, what cluster-level global objects it omits, and when a physical backup or WAL-based recovery would require a different procedure.

2. **Dump Scope and Consistency** — Create a consistent disposable-database logical backup, record the exact database/schema scope, versions, permissions and inclusion/exclusion assumptions.

3. **Restore into a Clean Target** — Use a separate locally controlled target database to rehearse restoration, including schema ordering, role dependencies and failure handling.

4. **Integrity Verification after Restore** — Compare independently defined row/constraint checks, reproducible queries and a bounded checksum or manifest where appropriate; avoid declaring recovery successful from tool exit status alone.

5. **Recovery Point and Recovery Time** — State a scenario's recovery point objective and recovery time objective; measure a local drill without pretending it demonstrates production guarantees.

6. **Connections, Locks, and Query Health** — Inspect a limited set of session and query signals, timeouts and lock waits; distinguish diagnosis from infrastructure tuning owned by APP7.

7. **Sensitive Information in Backups** — Explain least-privilege dump access, synthetic data, backup access control, retention and why an exported SQL file is not harmless metadata.

8. **Formative Interrupted Migration Recovery** — Take a validated backup, inject a safe migration fault into a disposable database, recover into a clean target and explain data that could not be recovered.

### Module 11 — Minimal Data Access Interfaces and Independent Tests

#### Outcomes

- APP4-O3
- APP4-O5
- APP4-O9
- APP4-O11

#### Lessons

1. **A Database Contract without a Backend Framework** — Publish a small local command/query interface with input schema, result columns, affected-row policy, transactional behavior and error categories.

2. **SQL Files, psql and Parameter Discipline** — Organize numbered SQL files and predictable psql invocation; explain why unsafe string substitution is not a replacement for safe driver parameters.

3. **Server Prepared Statements and Optional Adapters** — Demonstrate PREPARE/EXECUTE for value placeholders; an optional Python or other client adapter may be used if its required free driver is pre-provisioned locally.

4. **Data Access and Domain Invariants** — Separate records, queries and domain decisions; keep transaction ownership explicit and document where an API layer would add authorization.

5. **Deterministic Fixture Setup and Teardown** — Initialize synthetic tenants and records in a fresh disposable database and cleanly reset state without requiring root OS access or cloud services.

6. **Independent Verification Oracles** — Write expected result tables and contract tests for joins, duplicates, invalid writes, tenant boundaries and transaction outcomes; do not test only with self-referential query copies.

7. **Schema/Client Compatibility Regression** — Execute an old consumer and revised consumer against a staged schema and verify intended compatibility and explicitly rejected obsolete behavior.

8. **Formative External-Consumer Review** — Provide another reviewer with just the SQL/scripts, setup instructions and contract; investigate one discovered ambiguity and amend the interface.

### Module 12 — Integrated Relational Data Component and Engineering Defense

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

1. **Choose the Bounded Problem and Invariants** — Select a fictional inventory, subscription entitlement, lending or similar system with two independent tenants, meaningful integrity rules and explicit data-access requirements.

2. **Design and Normalize the Schema** — Publish a relationship diagram, functional dependencies, SQL DDL, sample data dictionary and one explained denormalization-or-not decision.

3. **Build Reusable SQL and Analytics** — Implement transactional reads/writes and one analytical report with independently computed expected outputs, including duplicates, NULLs and tied ordering.

4. **Prove Integrity and Concurrency Behavior** — Record invalid-write rejections and a two-session isolation or locking scenario, then demonstrate mitigation without hidden application-server behavior.

5. **Measure a Representative Query** — Record an EXPLAIN plan and repeatable experiment, evaluate a justified index change and disclose measurement limitations.

6. **Restrict, Migrate, and Recover** — Run a non-owner tenant authorization matrix, a staged schema migration with old/new consumers, and a separate clean restore with verified invariants.

7. **Unfamiliar Change and Technical Defense** — Respond to a bounded new requirement or fault, update schema/queries/tests safely, reproduce the result from a clean state and defend alternatives, security boundaries and remaining limitations.

## Completion requirements

**All twelve APP4 outcomes** must be demonstrated through the
**six required summative assessments** below. Assessment artifacts
may share one evolving domain database; learners do not need to
produce six separate database applications. Modules include
formative investigations, but each is **not** an additional
compulsory assessment simply because it appears in the lesson list.

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
- Test tenant permissions through sessions actually subject
  to privilege and row policy checks, identifying owner,
  superuser and `BYPASSRLS` exceptions. A caller-set
  tenant variable is not by itself an authenticated security
  boundary; policy tests must verify the real trust model.
- Concurrency experiments must record actual isolation level,
  session roles, statement interleavings, initial/final
  states, observed errors and retry policy. Do not claim
  `READ UNCOMMITTED` dirty reads or `REPEATABLE READ`
  phantoms were reproduced in PostgreSQL when the engine
  prevents them.
- `EXPLAIN ANALYZE` **executes** the statement. For a write
  experiment use a controlled disposable transaction and
  rollback or an otherwise harmless fixture, and verify no
  unintended modifications remained.
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
  - Work: Implement a two-session transaction schedule for a stated invariant (such as shared-stock reservation or reciprocal resource allocation), reproduce a lost-update or write-skew style failure under a documented isolation/locking setup, and apply a justified mitigation including bounded full-transaction retry when required. Then evolve the same dataset using a versioned expand/backfill/validate/contract migration while verifying defined old and new consumer queries; inject a staged failure and show a safe recovery or forward-repair plan.
  - Criteria: The anomaly is real and shown by an explicit interleaving/state table, not merely asserted from concurrency terminology. PostgreSQL-specific Read Committed, Repeatable Read and Serializable semantics are described accurately (including Repeatable Read's phantom protections); the mitigation preserves the invariant under tested interleavings. Migrations are reproducible and check affected data, constraints, compatibility and locking risks. Any destructive or irreversible change is not falsely described as trivially reversible.
  - Evidence: Versioned SQL migrations, two-session action/observation log, initial/final invariant checks, regression tests, old/new consumer compatibility fixtures, fail/retry or recovery evidence and a documented risk decision.

- **APP4-AS5** (required tenant access controls and verified restore)
  - Outcomes: APP4-O5, APP4-O8, APP4-O9, APP4-O10, APP4-O11
  - Work: Using synthetic records for at least two tenants, define a least-privilege non-owner access role and a documented trust model. Demonstrate parametrized values rather than interpolated SQL; implement and test a database-enforced tenant boundary (PostgreSQL RLS in the reference environment) against attempted cross-tenant reads/writes and privilege misuse, including the owner/BYPASSRLS caveat. Create a local logical backup and restore into a separate clean target after a controlled failed migration or corrupted fixture. Re-verify row identities, invariants and access controls.
  - Criteria: Authorized and rejected operations match a published role/tenant/action matrix, including negative-path modification attempts. Tests run as a role genuinely subject to policies, not a table owner, superuser or BYPASSRLS role; client-provided tenant context is not treated as intrinsically trustworthy. SQL value binding is distinguished from dynamic identifier handling. The backup's exact scope (including role/privilege or global-object limitations), restore process and data-integrity tests are recorded; measured local recovery is not claimed as a general production RPO/RTO guarantee.
  - Evidence: Role and RLS policy SQL, access matrix and negative test logs with effective-role evidence, prepared-statement or bound-parameter demonstration, backup/restore commands and target inventory, integrity comparisons, recovery measurements and documented limitations.

- **APP4-AS6** (required integrated relational data component and engineering defense)
  - Outcomes: APP4-O1, APP4-O2, APP4-O3, APP4-O4, APP4-O5, APP4-O6, APP4-O7, APP4-O8, APP4-O9, APP4-O10, APP4-O11, APP4-O12
  - Work: Deliver a cohesive, reproducible local relational data component for a bounded multi-user domain with normalized schema, declared invariants, SQL query interface, analytic report, appropriate index measurement, tested transaction behavior, staged schema change, tenant isolation and clean restoration. Provide a minimal client interface through SQL scripts or an optional pre-provisioned language adapter; no Web framework, remote PostgreSQL instance or paid host may be assumed. Reuse and integrate qualifying artifacts from APP4-AS1–AS5 instead of requiring six unrelated databases. Complete an unfamiliar bounded change or seeded failure, and defend the choices and limitations in an accessible reviewable format.
  - Criteria: A fresh reviewer can initialize the declared local reference environment and run verified normal and failure cases without hidden network, global state or credentials. The component satisfies published data/authorization contracts and retains integrity under an invalid write, controlled concurrency and a schema-revision case. The learner correctly interprets an actual plan, demonstrates effective tenant restrictions, verifies recovered state rather than relying on a successful dump/restore exit code, and explains why schema, indexes, isolation, migration and recovery choices fit the stated requirements. The unfamiliar change is integrated without violating existing invariants; remaining risks and unsupported claims are explicit.
  - Evidence: Portable versioned project or repository with DDL/migration/seed SQL, independent expected-result fixtures, read/write contract documentation, normal/negative SQL tests, transaction log, query plan evidence, role matrix, backup/restore drill, clean-start instructions, bounded change history and written/recorded/equivalently accessible defense.

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

This migration preserves APP4's subject identity and useful
legacy scope, but changes its direct prerequisite from
APP3 to SEF10 and publishes new stable assessment/outcome
identities. Earlier APP4 completions and historical project
records must remain attributable to the previously published
course revision; they do not automatically satisfy this
revision. Its related APP3/APP5 integrations and subsequent
operational specialization require separate course reviews.

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
