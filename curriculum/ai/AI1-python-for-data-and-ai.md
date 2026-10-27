# AI1 — Python for Data & AI

**Track:** AI & ML · **Prerequisite:** F1, F6 · **Core** · **Time:** 4 weeks, 60 hours · **Project:** P7 data audit
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Build the data-handling habits that make every later ML result trustworthy: load and inspect data, preserve provenance, write reproducible transformations, visualize honestly, and turn a notebook into a rerunnable pipeline. This is not a pandas tour; it is the first half of an evaluation discipline.

## Outcomes

You can:

- create a pinned Python environment and run a pipeline from a clean checkout;
- load CSV/JSON/Parquet data without silently coercing types;
- profile missingness, duplicates, ranges, cardinality, and suspicious values;
- join and reshape tables while preserving row counts and keys;
- write vectorized NumPy/pandas code and explain when it is worth it;
- produce plots that do not mislead;
- split data deterministically and document leakage risks;
- write a dataset card with source, license, limitations, and sensitive fields;
- convert exploratory notebook code into tested modules and a CLI.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [Python for Data Analysis](https://wesmckinney.com/book/) (3rd ed., free online) | Ch. **2–6, 7–10** | NumPy, pandas, data cleaning, joins, aggregation |
| [NumPy absolute beginner's guide](https://numpy.org/doc/stable/user/absolute_beginners.html) and broadcasting docs | Full | Arrays, shapes, broadcasting, vectorization |
| [pandas user guide](https://pandas.pydata.org/docs/user_guide/) | “10 minutes”, indexing, merge, groupby, missing data | Correct table operations |
| [Matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html) | Pyplot, lifecycle, histograms | Honest visualization |
| [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) | Full | Dataset documentation |
| [The Turing Way](https://the-turing-way.netlify.app/) | Reproducibility, data management | Research-grade habits |
| [Parquet format](https://parquet.apache.org/docs/) | Overview | Columnar storage trade-offs |

## Modules

### 1. Reproducible environment and data provenance

- virtual environments, lockfiles, pinned versions;
- project layout: `src/`, `data/raw/`, `data/processed/`, `tests/`, `reports/`;
- raw data immutable; processed data derived;
- checksums and source URLs;
- secrets and private data never committed;
- notebook versus script: when to use each.

### 2. NumPy and shapes

- arrays, dtype, strides, views versus copies;
- indexing, boolean masks, fancy indexing;
- broadcasting rules and shape errors;
- reductions and axis semantics;
- vectorization, memory cost, and when a loop is clearer;
- random generators and seeds.

### 3. pandas for tabular data

- Series/DataFrame, index alignment;
- reading with explicit dtypes and parse rules;
- selection: `.loc`, `.iloc`, boolean masks;
- missing data: representation, imputation, deletion;
- `merge`/`join` cardinality and duplicate keys;
- `groupby`, `pivot_table`, `melt`;
- categorical data and memory;
- method chaining and avoiding `SettingWithCopyWarning`.

### 4. Data quality and profiling

- schema and data dictionary;
- missingness mechanisms (MCAR/MAR/MNAR, conceptually);
- duplicates and entity resolution;
- range, domain, and consistency checks;
- outliers: error versus signal;
- class imbalance and group representation;
- temporal and group leakage;
- data validation with `pandera` or explicit assertions.

### 5. Visualization and communication

- chart choice: distribution, relationship, composition, change;
- axis scales, binning, aggregation, and truncation;
- uncertainty and sample size;
- color and accessibility;
- small multiples;
- a figure that supports a decision, not decoration.

### 6. From notebook to pipeline

- pure functions for transformations;
- tests with small fixture tables;
- CLI entry point with `argparse` or `typer`;
- logging and failure messages;
- deterministic output ordering;
- dataset card and model-ready split.

## Labs

### Lab 1 — Dataset audit

Choose one open, non-sensitive tabular dataset with a clear license. Produce:

- a data dictionary for every column;
- row/column counts, dtypes, missingness, duplicates;
- distributions and at least three suspicious patterns;
- a leakage and representation risk list;
- a dataset card.

### Lab 2 — Cleaning pipeline

Write a pipeline that ingests raw data, validates schema, normalizes types, handles missing values with an explicit policy, and writes Parquet plus a manifest. Rerun from a clean environment and show identical output hashes.

### Lab 3 — Join and aggregation correctness

Build two small related tables. Demonstrate a one-to-many join, detect duplicate-key fan-out, and add an assertion that prevents row-count inflation. Produce a grouped summary and one honest plot.

### Lab 4 — Vectorization and memory

Implement one transformation as a Python loop and as a vectorized operation. Verify equality, measure runtime and peak memory, and explain the result. Then show one case where vectorization is not the right choice.

### Lab 5 — Notebook to package

Refactor an exploratory notebook into modules with tests and a CLI. The CLI must fail clearly on malformed input and produce a deterministic report. Include the original notebook only as a narrative artifact.

## Exercises

1. Fix a dtype bug caused by a column with mixed numbers and `"N/A"`.
2. Detect duplicate keys before a merge and choose a policy.
3. Compute group statistics with correct denominators.
4. Explain copy versus view in NumPy and pandas.
5. Write a deterministic 70/15/15 split with a fixed seed.
6. Identify three leakage risks in a supplied feature table.
7. Redraw a misleading chart with an honest scale.
8. Write five assertions for a schema contract.
9. Explain why `dropna()` can bias a result.
10. Make a pipeline idempotent and prove it with hashes.

## Project increment — P7 data audit

Produce the P7 `signal-score` data foundation:

- licensed dataset and dataset card;
- immutable raw data with checksum;
- validated, documented preprocessing;
- frozen split manifest with seeds;
- leakage/representation audit;
- reproducible pipeline command and tests.

**Brief:** [P7 — signal-score](../projects/project-ladder.md#p7--signal-score)

## Exit check

- [ ] run the pipeline from a clean environment and reproduce the output hash;
- [ ] explain every column's type, meaning, and missingness policy;
- [ ] demonstrate a join-fan-out bug and the assertion that prevents it;
- [ ] show one vectorized speedup with measured memory cost;
- [ ] present a dataset card naming license, limitations, and sensitive fields;
- [ ] explain the split and at least two leakage risks.

## Common failure modes

- Imputing before splitting, leaking test information.
- Using row counts without checking merge cardinality.
- Treating `object` dtype as a meaningful type.
- Dropping missing rows and silently changing the population.
- Plotting averages without sample size or uncertainty.
- Committing raw private data or credentials.
- Leaving the only working version inside a notebook's hidden state.

## Evidence to commit

- `labs/ai/AI1/` with audit, cleaning pipeline, join test, vectorization benchmark, report
- P7 data card, split manifest, and pipeline
- `notes/ai/AI1/summary.md`

## Optional depth

- *Python for Data Analysis* Ch. 11–13 (time series, advanced NumPy, modeling).
- *R for Data Science* (2nd ed.) for tidy-data principles, even if you use Python.
- Great Expectations or pandera for data contracts.
- DuckDB for local analytical SQL.
- `polars` for a lazy/columnar alternative.
