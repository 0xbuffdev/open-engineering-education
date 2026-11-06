# APP4 — Databases & Data Modeling

**Program:** APP — Application Engineering
**Type:** `course`
**Prerequisites:** [APP3](APP3.md)
**Duration:** 5 weeks
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

## Modules

### Module 1 — Relational Modeling & SQL

#### Outcomes

- Explain **Entities, relationships, and relational schemas** in the context of the course.
- Apply **SQL queries and joins** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Course introduction: Databases & Data Modeling** — `lesson`

   Learn how applications turn domain requirements into durable data. You will model relational data, write and analyze SQL, use constraints and indexes, reason about transactions, and evolve schemas safely.
2. **Entities, relationships, and relational schemas** — `lesson`
3. **SQL queries and joins** — `lesson`
4. **data modeling** — `test`
5. **Model a small domain and answer business questions with SQL** — `lab`

### Module 2 — Constraints & Schema Quality

#### Outcomes

- Explain **Keys, constraints, normalization, and denormalization** in the context of the course.
- Apply **Designing schema integrity rules** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Keys, constraints, normalization, and denormalization** — `lesson`
2. **Designing schema integrity rules** — `lesson`
3. **relational integrity** — `test`
4. **Introduce bad data deliberately and make constraints reject it** — `lab`

### Module 3 — Indexes & Query Performance

#### Outcomes

- Explain **Indexes and access paths** in the context of the course.
- Apply **Query plans and performance reasoning** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Indexes and access paths** — `lesson`
2. **Query plans and performance reasoning** — `lesson`
3. **index selection** — `test`
4. **Compare a query before and after adding an appropriate index** — `lab`

### Module 4 — Transactions & Change Management

#### Outcomes

- Explain **Transactions and isolation concepts** in the context of the course.
- Apply **Migrations, seed data, backups, and recovery planning** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Transactions and isolation concepts** — `lesson`
2. **Migrations, seed data, backups, and recovery planning** — `lesson`
3. **transaction boundaries** — `test`
4. **Write and test a forward migration and a safe recovery procedure** — `lab`

### Module 5 — Application Data Layer

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

**Exit demonstration:**

The learner can justify a schema and index, explain a transaction boundary, and investigate a slow query using evidence.

---
