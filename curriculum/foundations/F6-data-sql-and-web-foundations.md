# F6 — Data, SQL & Web Foundations

**Track:** Foundations · **Prerequisite:** F2, F3 · **Core for all tracks** · **Time:** 5 weeks, 75 hours · **Project:** P1 SQL/API increment

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Almost every professional system stores data and talks over a network. This course fills the gap between "I can write a program" and "I can build a service": relational modelling, SQL, data formats, HTTP, and the basic architecture of a web request.

## Outcomes

You can:

- design a normalized schema and explain the trade-offs of denormalization;
- write correct SQL with joins, aggregation, subqueries, CTEs, and window functions;
- read a query plan and add the right index;
- explain transactions, isolation levels, and anomalies;
- validate and transform CSV/JSON/JSONL data;
- debug an HTTP request end to end (DNS → TCP → TLS → request → response);
- design a small REST API with status codes, pagination, idempotency, and error shapes;
- explain authentication vs authorization, sessions, cookies, and CORS;
- threat-model a basic web service.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html) or [SQLite docs](https://www.sqlite.org/docs.html) | Full tutorial | SQL spine |
| [Use The Index, Luke](https://use-the-index-luke.com/) | Select chapters on indexing and query plans | Practical indexing |
| [MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) | Overview, methods, status, headers, cookies, CORS | Web fundamentals |
| [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/) | Ch. 1–6 | Sockets and client/server (preview of S10) |
| *Designing Data-Intensive Applications* (DDIA) | Ch. **1–2** | Data models, storage, and architecture trade-offs |
| B5 *The Linux Programming Interface* | Ch. **56–58** | Sockets and TCP/IP fundamentals (optional preview) |

## Modules

### 1. Relational modelling

- entities, attributes, relationships, keys;
- normalization (1NF–3NF/BCNF) and when to denormalize;
- constraints: primary key, foreign key, unique, check, not null;
- schema migrations and versioning;
- data dictionaries and sample fixtures;
- representing time, money, enums, and optional fields;
- soft deletes, audit columns, and immutable logs.

### 2. SQL

- `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`;
- joins: inner, left, right, full, cross, self;
- aggregation, `GROUP BY`, `HAVING`;
- subqueries, `EXISTS`, `IN`, CTEs;
- window functions: `ROW_NUMBER`, `RANK`, `LAG`, `LEAD`, running totals;
- `INSERT`/`UPDATE`/`DELETE`, upsert;
- transactions, `BEGIN`/`COMMIT`/`ROLLBACK`;
- isolation levels and anomalies (dirty read, non-repeatable read, phantom);
- indexes: B-tree, composite, covering, partial; when indexes hurt;
- `EXPLAIN`/`EXPLAIN ANALYZE` and query plans;
- views, materialized views, triggers (cautiously).

### 3. Data formats and quality

- CSV: quoting, escaping, schema, streaming;
- JSON/JSONL: nesting, schema validation, line-delimited records;
- Parquet/columnar formats (concept);
- character encodings, Unicode normalization, time zones;
- missing data, duplicates, invalid ranges, outliers;
- data validation at boundaries;
- idempotent imports and atomic writes.

### 4. HTTP and web architecture

- client/server, request/response, statelessness;
- methods, status codes, headers, content negotiation;
- REST resource design, versioning, pagination, filtering;
- idempotency keys and retries;
- JSON error shape and problem details;
- DNS, TCP, TLS, HTTP/1.1 vs HTTP/2 vs HTTP/3 (overview);
- cookies, sessions, tokens, `Authorization`;
- authentication vs authorization;
- CORS, CSRF, same-origin policy;
- caching, proxies, reverse proxies, load balancers, CDNs;
- queues and background jobs (concept);
- rate limits, timeouts, and backpressure.

### 5. Building a small service

- choose SQLite for a local tool or PostgreSQL for a service;
- schema + migrations;
- API handlers with validation;
- integration tests against a real database;
- structured logs and error handling;
- a threat model for the service.

## Labs

### Lab 1 — Schema and queries

Design a schema for `ledgerlab` (accounts, transactions, categories, imports). Write 20 queries covering joins, aggregation, CTEs, and window functions. Add constraints and test invalid inserts.

### Lab 2 — Query plan and index

Take three slow queries, run `EXPLAIN ANALYZE`, add or change indexes, and measure the improvement. Include one case where an index makes a query slower.

### Lab 3 — Data import pipeline

Import a messy CSV and a JSONL file into SQLite/PostgreSQL. Handle malformed rows, duplicates, missing fields, encoding issues, and partial failure. Document idempotency.

### Lab 4 — HTTP client and server

Build a small HTTP client that handles status codes, redirects, timeouts, and retries. Then build a minimal server with three endpoints, validation, and a consistent error shape. Test with `curl` and automated tests.

### Lab 5 — Threat model

Draw the data flow for the service. Identify assets, actors, entry points, trust boundaries, and five threats. Turn the top two into tests or controls.

## Exercises

1. Normalize a denormalized table to 3NF and explain one trade-off.
2. Write ten joins, including a self-join and an anti-join.
3. Write five window-function queries.
4. Explain four isolation anomalies with a concrete schedule.
5. Design indexes for five query patterns.
6. Parse a malformed CSV and decide reject vs repair.
7. Debug a DNS/TLS/HTTP failure from `curl -v` output.
8. Design a REST API for a small resource, including pagination and errors.
9. Explain why client-side validation is not authorization.
10. Threat-model a login flow.

## Project increment — P1 SQL/API

Extend `ledgerlab` with:

- a SQLite or PostgreSQL backend;
- schema migrations;
- idempotent import;
- a small read-only HTTP API (optional but recommended);
- query-plan evidence for one index;
- a threat model.

**Brief:** [P1 — ledgerlab](../projects/project-ladder.md#p1--ledgerlab)

## Exit check

- [ ] design a schema and justify normalization/denormalization;
- [ ] write a correct multi-table query with aggregation and a window function;
- [ ] read a query plan and explain an index choice;
- [ ] explain a transaction anomaly and the isolation level that prevents it;
- [ ] debug an HTTP request from DNS to response;
- [ ] demonstrate input validation and a consistent error shape;
- [ ] identify a trust boundary and one authorization failure.

## Common failure modes

- Storing everything in one JSON column and calling it a schema.
- Using `SELECT *` in production queries.
- Adding indexes without measuring write cost.
- Trusting client-side validation.
- Treating HTTP 200 as success for every API.
- Ignoring time zones and encoding until data is corrupted.
- Building auth before understanding sessions/tokens and authorization.

## Evidence to commit

- `labs/foundations/F6/` with schema, queries, query plans, API, and threat model
- `exercises/foundations/F6/`
- P1 SQL/API increment
- `notes/foundations/F6/summary.md`

## Optional depth

- *Designing Data-Intensive Applications* Ch. 1–3.
- *SQL Performance Explained* (Winand).
- *Web Application Security* (OWASP) after D1.
- OpenAPI/Swagger and contract testing.
