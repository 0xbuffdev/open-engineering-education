# APP4 — Databases & Data Modeling

**Program:** APP — Application Engineering
**Type:** `course`
**Prerequisites:** [APP3](APP3.md)
**Duration:** 8 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Learn how applications turn domain requirements into durable data. You will model relational data, write and analyze SQL, use constraints and indexes, reason about transactions, and evolve schemas safely.

## Learning outcomes

By the end of this course, the learner will be able to:

- Translate application requirements into relational data models.
- Write and reason about SQL involving filtering, joins, aggregation, and updates.
- Choose appropriate constraints and indexes and investigate query performance.
- Define transaction boundaries and explain relevant isolation behavior.
- Design and execute safe schema migrations.
- Build a tested application data layer with recovery and integrity considerations.
- Construct analytical SQL queries involving aggregation, windows and missing values and verify their outputs against independent fixtures.
- Demonstrate tenant isolation, parameterized query handling and appropriate data-access privileges.
- Rehearse a schema migration and tested backup restoration under realistic data integrity constraints.
- Identify database contention and performance risks through query plans, transaction evidence and operational telemetry.

## Modules

### Module 1 — Relational Modeling & SQL

#### Outcomes

- Explain **Entities, relationships, and relational schemas** in the context of the course.
- Apply **SQL queries and joins** in a problem, implementation, experiment, or design decision.

- Use SQL and relational reasoning to produce correct result sets for nontrivial domain questions.

#### Lessons

1. **Course introduction: Databases & Data Modeling** — `lesson`

   Learn how applications turn domain requirements into durable data. You will model relational data, write and analyze SQL, use constraints and indexes, reason about transactions, and evolve schemas safely.
2. **Entities, relationships, and relational schemas** — `lesson`
3. **SQL queries and joins** — `lesson`
4. **Relational algebra and logical query meaning** — `lesson`
5. **Joins, grouping, aggregation, and NULL behavior** — `lesson`
6. **Schema design from functional requirements** — `lesson`
7. **data modeling** — `test`
8. **Model a small domain and answer business questions with SQL** — `lab`

### Module 2 — Constraints & Schema Quality

#### Outcomes

- Explain **Keys, constraints, normalization, and denormalization** in the context of the course.
- Apply **Designing schema integrity rules** in a problem, implementation, experiment, or design decision.

- Use relational constraints to prevent invalid states while recognizing what the database cannot verify.

#### Lessons

1. **Keys, constraints, normalization, and denormalization** — `lesson`
2. **Designing schema integrity rules** — `lesson`
3. **Functional dependencies and normalization** — `lesson`
4. **Foreign keys, uniqueness, checks, and generated identifiers** — `lesson`
5. **Denormalization costs and application-layer invariants** — `lesson`
6. **relational integrity** — `test`
7. **Introduce bad data deliberately and make constraints reject it** — `lab`

### Module 3 — Indexes & Query Performance

#### Outcomes

- Explain **Indexes and access paths** in the context of the course.
- Apply **Query plans and performance reasoning** in a problem, implementation, experiment, or design decision.

- Explain query access paths and optimize a repeatable workload without relying on timing guesses.

#### Lessons

1. **Indexes and access paths** — `lesson`
2. **Query plans and performance reasoning** — `lesson`
3. **B-tree indexes, selectivity, and composite key order** — `lesson`
4. **Execution plans, estimates, statistics, and join strategies** — `lesson`
5. **Pagination strategies and query workload profiles** — `lesson`
6. **index selection** — `test`
7. **Compare a query before and after adding an appropriate index** — `lab`

### Module 4 — Transactions & Change Management

#### Outcomes

- Explain **Transactions and isolation concepts** in the context of the course.
- Apply **Migrations, seed data, backups, and recovery planning** in a problem, implementation, experiment, or design decision.

- Manage data changes and concurrent access with explicit recovery and integrity guarantees.

#### Lessons

1. **Transactions and isolation concepts** — `lesson`
2. **Migrations, seed data, backups, and recovery planning** — `lesson`
3. **Atomicity, isolation anomalies, and concurrent updates** — `lesson`
4. **Backward-compatible schema changes and migrations** — `lesson`
5. **Backups, restore drills, and transaction retry policies** — `lesson`
6. **transaction boundaries** — `test`
7. **Write and test a forward migration and a safe recovery procedure** — `lab`

### Module 5 — Advanced SQL & Analytical Queries

#### Outcomes

- Build correct analytical queries with windowing, filtering, and nested result sets.
- Explain query correctness under duplicates, missing values, and nontrivial ordering.

#### Lessons

1. **Common table expressions and recursive queries** — `lesson`
2. **Window functions, ranks, and running totals** — `lesson`
3. **Sets, grouping sets, and analytical query trade-offs** — `lesson`
4. **NULL semantics and query correctness checks** — `lesson`
5. **Window functions and data result correctness** — `test`
6. **Audit an analytical SQL report** — `lab`

### Module 6 — Data Security & Multi-Tenancy

#### Outcomes

- Restrict data access with least privilege and tested tenant boundaries.
- Prevent injection and inadvertent cross-tenant disclosure through structured queries.

#### Lessons

1. **Application authorization versus database roles** — `lesson`
2. **Tenant scoping and row-level security concepts** — `lesson`
3. **SQL injection prevention and parameterization** — `lesson`
4. **Sensitive data retention, auditing, and migrations** — `lesson`
5. **Database authorization and data isolation** — `test`
6. **Test tenant isolation against malicious queries** — `lab`

### Module 7 — Database Operations, Recovery & Evolution

#### Outcomes

- Plan and rehearse backup restoration and safe schema evolution under running traffic.
- Observe query and connection health and document performance and recovery limits.

#### Lessons

1. **Connection pools, limits, and slow query monitoring** — `lesson`
2. **Backup consistency, restore objectives, and verification** — `lesson`
3. **Online schema evolution and expand-contract migrations** — `lesson`
4. **Data lifecycle, retention, and operational health** — `lesson`
5. **Recovery objectives and schema evolution** — `test`
6. **Perform a reversible production-style migration** — `lab`

### Module 8 — Application Data Layer

#### Outcomes

- Complete and explain the Application Data Layer lab, demonstrating the applicable course outcomes and retaining required evidence.

#### Lessons

1. **Design, implement, test, and document the Application Data Layer** — `lab`

## Completion requirements

- Complete the required practical exercises, knowledge checkpoints, and evaluated labs described in the modules.
- Complete the final integrated `lab` in the last module and satisfy its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, failures investigated, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required practical exercises:**

- model a domain from requirements
- write and optimize queries
- inspect an index/query plan
- reproduce a transaction anomaly
- design a migration and rollback
**Final integration lab — required work:**

Required artifact: **Application Data Layer**.

Design and implement a production-oriented database for the APP3 service, including migrations, constraints, indexes, seed data, backup/recovery notes and tested queries.

**Expanded module assessments and practical work:**

- **Module 1 checkpoint and micro-lab:** Verify inner and outer joins, missing values, grouping, and invariants against realistic fixtures.
- **Module 2 checkpoint and micro-lab:** Prove invalid inserts and updates fail and demonstrate why normalization choices fit the business rules.
- **Module 3 checkpoint and micro-lab:** Compare plans and representative query measurements before and after indexing.
- **Module 4 checkpoint and micro-lab:** Execute a migration and restore rehearsal; reproduce and resolve one transaction anomaly.

- **Module 5 — Advanced SQL & Analytical Queries (Audit an analytical SQL report):**
  - Prerequisites: Complete the module lessons and explain its stated outcomes.
  - Environment: A controlled local application or service, with tool versions and test data documented.
  - Required work: Build a report using joins, aggregation and window functions; include fixtures with duplicates, NULLs and tied ordering.
  - Verification: Compare outputs with independently computed expected results and verify predictable ordering.
  - Evidence: SQL files, fixtures, expected rows, and correctness tests.
  - Failure analysis: Explain double counting, misleading joins, unbounded recursion, and NULL-sensitive predicates.
- **Module 6 — Data Security & Multi-Tenancy (Test tenant isolation against malicious queries):**
  - Prerequisites: Complete the module lessons and explain its stated outcomes.
  - Environment: A controlled local application or service, with tool versions and test data documented.
  - Required work: Build two tenant fixtures, attempt cross-tenant reads/writes, and compare application guards with database-enforced access.
  - Verification: Prove unauthorized queries fail even when client-side filters are omitted; demonstrate parameterized query handling.
  - Evidence: Test accounts, rejected queries, policies and authorization matrix.
  - Failure analysis: Identify connection-pool tenant context leaks, overprivileged service accounts, and unsafe dynamic SQL.
- **Module 7 — Database Operations, Recovery & Evolution (Perform a reversible production-style migration):**
  - Prerequisites: Complete the module lessons and explain its stated outcomes.
  - Environment: A controlled local application or service, with tool versions and test data documented.
  - Required work: Run a forward-compatible migration with a realistic dataset while the old application version remains active, then rehearse rollback or a documented recovery path.
  - Verification: Show integrity checks and old/new compatibility, a successful restore, and measured recovery time.
  - Evidence: Migration scripts, compatibility tests, backup checksum and restore log.
  - Failure analysis: Explain locking migrations, irreversible data loss, snapshot inconsistency, and unsafe assumptions about rollback.

**Exit assessment expectation:**

Demonstrate the course outcomes through a new scenario, including at least one negative path and independently reproducible evidence. Checkpoint answers must explain the mechanism and not merely name a tool. The final integration lab must incorporate and verify the expanded material.

**Exit demonstration:**

The learner can justify a schema and index, explain a transaction boundary, and investigate a slow query using evidence.

---
