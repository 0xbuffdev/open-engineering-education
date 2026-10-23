# AI13 — Data Engineering for ML

**Track:** AI & ML · **Prerequisite:** F6, AI1 · **Core** · **Time:** 5 weeks, 75 hours · **Project:** P7 data pipeline

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Build reliable data pipelines for ML: ingestion, storage, transformation, orchestration, contracts, quality checks, and lineage. Most ML failures are data failures; this course gives you the tools to detect them before training.

## Outcomes

You can:

- design batch and incremental ingestion with idempotency;
- choose file formats, partitioning, and storage layout;
- write SQL and dataframe transformations with clear grain;
- build a DAG with retries, backfills, and idempotent tasks;
- define data contracts and quality checks;
- track lineage from source to feature to model;
- handle late, duplicate, and malformed data;
- protect PII and enforce retention;
- measure pipeline freshness, completeness, and cost;
- reproduce a training dataset from a version identifier.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) (Reis & Housley) | Ch. **1–4, 6–9** | Lifecycle, architecture, ingestion, storage, orchestration |
| DDIA | Ch. **3–4, 10–11** | Storage, encoding, batch and stream processing |
| [The Data Engineering Cookbook](https://github.com/andkret/Cookbook) | Selected | Practical patterns (verify currency) |
| [dbt docs](https://docs.getdbt.com/) | Models, tests, lineage | Transformation and contracts |
| [Apache Airflow docs](https://airflow.apache.org/docs/) or [Dagster docs](https://docs.dagster.io/) | DAGs, retries, backfills, assets | Orchestration |
| [Great Expectations](https://greatexpectations.io/) or [pandera](https://pandera.readthedocs.io/) | Validation | Data quality |
| [OpenLineage](https://openlineage.io/) | Spec overview | Lineage |

## Modules

### 1. Data lifecycle and architecture

- source systems and ownership;
- ingestion, storage, transformation, serving;
- batch, micro-batch, streaming;
- lake, warehouse, lakehouse;
- operational vs analytical workloads;
- data mesh/centralization trade-offs;
- cost and governance.

### 2. Ingestion

- full vs incremental;
- change data capture (awareness);
- idempotent loads;
- watermarks and late data;
- schema evolution;
- API pagination and rate limits;
- file arrival and checksums;
- dead-letter queues;
- exactly-once claims and deduplication.

### 3. Storage and modeling

- Parquet/ORC/Avro;
- columnar layout, row groups, compression;
- partitioning and small files;
- table formats (Iceberg/Delta/Hudi) concepts;
- star schema, facts/dimensions;
- grain and slowly changing dimensions;
- normalization vs denormalization for ML;
- feature tables and point-in-time correctness.

### 4. Transformation and orchestration

- SQL and dataframe transforms;
- idempotent tasks;
- DAG dependencies;
- retries, timeouts, alerts;
- backfills and catch-up;
- data intervals and partitions;
- environment promotion;
- code review and testing;
- orchestration vs scheduling.

### 5. Quality, lineage, and privacy

- completeness, uniqueness, validity, timeliness, consistency;
- data contracts;
- anomaly detection;
- lineage and impact analysis;
- PII classification and minimization;
- retention and deletion;
- access control;
- audit logging.

### 6. ML-specific data work

- training-serving skew;
- point-in-time joins;
- label windows and leakage;
- feature versioning;
- dataset snapshots;
- reproducibility;
- drift inputs.

## Labs

### Lab 1 — Batch ingestion

Ingest a public dataset from an API or files into a raw zone. Make the job idempotent, record source metadata/checksum, handle pagination and one malformed record, and produce a run manifest.

### Lab 2 — Modeled tables

Build staging and mart tables with a documented grain. Write SQL for at least three analyses. Add uniqueness and referential-integrity tests. Show one fan-out bug and its fix.

### Lab 3 — Orchestrated pipeline

Create a DAG with extract → validate → transform → publish. Add retries, timeout, alerting, and a backfill for one partition. Prove a rerun does not duplicate data.

### Lab 4 — Data contract and quality

Define a contract for one table (schema, freshness, nullability, ranges). Add automated checks. Inject three failures: late data, schema change, and duplicate rows. Show detection and operator response.

### Lab 5 — Training snapshot

Produce a versioned, reproducible training dataset from the pipeline. Record the source intervals, transform commit, row counts, and hash. Rebuild it and compare. Explain one point-in-time correctness risk.

## Exercises

1. Choose batch versus streaming for three scenarios.
2. Design an idempotent load key.
3. Explain why small files hurt a lake.
4. Define the grain of a fact table.
5. Write a point-in-time join.
6. Design a data contract for a feature table.
7. Explain backfill correctness.
8. Trace lineage from a model metric to a source column.
9. Classify PII and propose retention.
10. Explain one cause of training-serving skew.

## Project increment — P7 data pipeline

Add:

- ingestion with manifest/checksum;
- modeled tables with tests;
- orchestrated, idempotent pipeline;
- data contract and quality checks;
- versioned training snapshot and lineage;
- freshness/cost metrics;
- privacy/retention note.

**Brief:** [P7 — signal-score](../projects/project-ladder.md#p7--signal-score)

## Exit check

- [ ] rerun the pipeline without duplicates;
- [ ] backfill one partition and prove correctness;
- [ ] show a data-contract violation and the response;
- [ ] rebuild the training dataset from its version;
- [ ] trace a feature to its source and transform;
- [ ] explain one leakage/skew risk and its control;
- [ ] report freshness, completeness, and cost.

## Common failure modes

- Retrying a non-idempotent load.
- Using ingestion time instead of event time.
- Ignoring late-arriving data.
- Partitioning by high-cardinality keys and creating small files.
- A data contract with no owner or enforcement.
- Training on a mutable "latest" table.
- Copying PII into logs or notebooks.
- Calling a pipeline "fresh" without measuring lag.

## Evidence to commit

- `labs/ai/AI13/` with ingestion, models, DAG, contract tests, snapshot, lineage
- P7 pipeline and data documentation
- `notes/ai/AI13/summary.md`

## Optional depth

- *The Data Warehouse Toolkit* (Kimball & Ross), selected chapters.
- *Streaming Systems* (Akidau et al.).
- Apache Iceberg spec and docs.
- *Data Quality Fundamentals* (Moses et al.).
- dbt advanced materializations and exposures.
