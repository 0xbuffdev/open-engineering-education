# AI1 — Scientific Computing & Data Engineering for AI

**Program:** AI — AI Engineering
**Type:** `course`
**Prerequisites:** [SEF10](../SEF/SEF10.md)
**Duration:** 7–9 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; subject to learner calibration)

> [AI Engineering](README.md) · [OEE Course Format](../../spec/course-format.md) · [Evidence Rules](../../spec/evidence-rules.md)

## Overview

Develop and verify the data and scientific-computing foundations used by machine-learning systems. Work with numerical arrays, reproducible tabular transformations, scientific analysis, data contracts, provenance, data leakage, and the controlled construction of AI-ready datasets. The goal is not to call a library until a model trains: it is to **establish trustworthy data and reproducible evidence before model building**.

**Prior learning is mandatory.** Learners enter only after completing all eleven Software Engineering Foundations courses through [SEF10](../SEF/SEF10.md). This course **does not reteach** SEF2 Python, lists, CSV/JSON, functions, classes and errors; SEF4 algorithmic cost and invariants; SEF5 Git, debugging and elementary tests; SEF8 vectors, matrices, probabilities, derivatives and basic statistical inference; or SEF9 privacy, licensing and ethical decision-making. Those assessed abilities are *applied at new scientific-data depth*. In particular, vectorized array semantics, index alignment, data-frame joins, learned preprocessing state, leakage, scientific provenance and distribution shifts are new here.

A local Python environment with widely available open-source scientific packages (such as NumPy, pandas and Matplotlib) is the reference environment. Document precise versions and a repeatable setup; an equivalent free environment is acceptable when it supports the published outcomes and evaluation criteria. All mandatory work must be possible with small licensed or synthetic datasets on modest CPU hardware. No external data account, paid API, managed data warehouse or GPU is necessary. Keep real credentials, personal records and proprietary datasets out of submitted evidence.

**Teaching progression:** start with scientific questions and observations; progress through array reasoning, data semantics, descriptive exploration, repeatable feature construction and leakage control; culminate in one independently reproducible dataset investigation. Estimates of weeks or checkmarks do not establish completion. Optional practice does not become mandatory evidence unless incorporated into an explicitly named required assessment.

## Learning outcomes

- **AI1-O1:** Define the observational unit, target population, measurement assumptions, dataset rights and specific empirical question for a bounded AI data workflow, distinguishing observation, transformation, training and evaluation.
- **AI1-O2:** Implement and verify multidimensional numerical-array operations, including broadcasting, axis reductions, views/copies, data types, nonfinite values and bounded memory behavior, using independent numeric references.
- **AI1-O3:** Apply explicit schema, row identity, join-cardinality, unit and missingness policies to heterogeneous tables while detecting duplication, record loss and invalid transformations.
- **AI1-O4:** Use suitable quantitative summaries and graphics to investigate a specified data question, qualifying outliers, selection effects, uncertainty and unsupported causal interpretations.
- **AI1-O5:** Construct an inspectable, deterministic raw-to-feature pipeline with separated input, validation and transformation stages, stable identities, repeatable outputs and documented failure handling.
- **AI1-O6:** Detect and demonstrate at least two distinct leakage or data-integrity failures, including fit/split ordering or repeated-entity overlap, and verify corrections with defensible partition policies.
- **AI1-O7:** Reproduce an analysis from a clean state and identify the numerical environment, random seeds, input version, transformation identity and tolerance assumptions that materially affect interpretation.
- **AI1-O8:** Deliver a bounded AI-ready dataset investigation with a meaningful data dictionary, quality report, provenance, reproducible analysis and explicit fitness-for-use limitations.
- **AI1-O9:** Independently diagnose and repair an unfamiliar controlled data defect, preserving relevant invariants and explaining which conclusions can and cannot be supported after correction.

## Modules

### Module 1 — From observations to an AI dataset

#### Outcomes

- AI1-O1
- AI1-O8

#### Lessons

1. **Course scope and SEF transfer** — Identify the precise scientific-data abilities introduced here and demonstrate where prior programming, statistics and professional obligations are assumed.
2. **Observation and unit of analysis** — Define what one row denotes, distinguish repeated measurements from independent subjects, and trace consequences for evaluation.
3. **Population and sampling frame** — State the population of interest, collection mechanism, excluded cases and the limits of generalization.
4. **Questions before features** — Write a bounded measurable empirical question and distinguish prediction, description, association and causal claims.
5. **Data-to-model boundaries** — Trace observed records, labels, engineered features, fitted preprocessing and evaluation splits without using accuracy as proof of data quality.
6. **Source permissions and data minimization** — Apply SEF9 provenance and confidentiality decisions to licensed, permitted or fully synthetic input; reject undocumented redistribution authority.
7. **Dataset acceptance contract** — Specify intended use, required fields, invalid cases, fitness-for-use criteria and what a reviewer must be able to reproduce.

*Formative investigation:* inspect a synthetic dataset whose rows mix people and transactions; state why random row splitting may be invalid. This investigation is not a separate required assessment.

### Module 2 — Multidimensional numerical computation

#### Outcomes

- AI1-O2
- AI1-O7

#### Lessons

1. **Array construction and shapes** — Map a nested dataset into explicit dimensions, dtypes and expected operations rather than relying on displayed formatting.
2. **Indexing and axis semantics** — Predict resulting shapes for basic indexing, slicing, Boolean masks and reductions; compare preserved versus dropped axes.
3. **Broadcasting rules** — Derive alignment from trailing dimensions and reject incompatible shapes instead of allowing silent accidental arithmetic.
4. **Views, copies and aliasing** — Trace mutation through slices, advanced indexing and explicit copies, showing when transformations alter their source.
5. **Dtypes, promotion and nonfinite data** — Diagnose integer overflow, float precision changes, NaN/infinity propagation and misleading sentinel values.
6. **Strides and memory layout** — Explain contiguity and noncontiguous views, when computation copies storage and why that can affect memory.
7. **Vectorization and allocation cost** — Compare loop and vectorized calculations under recorded input size, warm-up, repeated trials and peak-memory constraints.
8. **Numeric reference oracles** — Derive tiny expected results by hand or a logically independent implementation and specify justified comparison tolerances.
9. **Bounded and invalid input** — Handle empty arrays, incorrect rank, incompatible axes, nonfinite values and excessive allocation with explicit contracts.

*Optional practice:* investigate a deliberately mutated view and demonstrate a robust copy boundary.

### Module 3 — Tables, records and schema semantics

#### Outcomes

- AI1-O3
- AI1-O5

#### Lessons

1. **Row identity and cardinality** — Specify primary/foreign key candidates, uniqueness, granularity and the consequences of duplicate observations.
2. **Scientific column types** — Distinguish numeric magnitudes, nominal/ordinal labels, times, identifiers and missing values; prevent accidental treatment of identifiers as measurements.
3. **Schema validation** — Check required columns, dtypes, ranges, categories, uniqueness and parsing rules before transformation.
4. **Units, time and locale** — Normalize compatible measurements and timezones with documented assumptions; reject ambiguous unit conversion and invalid timestamps.
5. **Missingness policies** — Record why values are missing, distinguish structural absence from sensor errors and explain how an imputation choice changes analysis.
6. **Joins and alignment** — Predict one-to-one, one-to-many and many-to-many result cardinality; reject unexpected multiplication and unmatched records.
7. **Categorical encodings** — Compare explicit codebooks and category mappings, including unknown-category handling and inappropriate ordinal assumptions.
8. **Tabular transformation invariants** — Verify row counts, identities, schema, source preservation and stable output ordering after each transformation.

### Module 4 — Scientific exploration and communication

#### Outcomes

- AI1-O1
- AI1-O4

#### Lessons

1. **Analysis plan and denominators** — Translate the empirical question into population, summary, comparison groups and relevant denominators.
2. **Robust summary statistics** — Apply SEF8 inference to skewed and missing observations; compare median, quantiles, spread and influence-sensitive estimates.
3. **Outliers and rare values** — Distinguish errors from legitimate rare cases using provenance and domain constraints rather than automatically deleting extremes.
4. **Groups and aggregation traps** — Diagnose unequal group size, mix shifts, confounding and Simpson-style reversals with appropriately qualified conclusions.
5. **Visual representation choices** — Justify plots by task and measurement scale; choose readable axes, units, grouping and accessible textual summaries.
6. **Misleading visualization** — Detect truncated/ambiguous scales, inappropriate bins, duplicate axes and selective presentation.
7. **Uncertainty and missingness displays** — Show known uncertainty or gaps without inventing representative intervals or population claims.
8. **Interpretation and handoff** — Produce evidence-linked observations, explicitly label exploratory findings and distinguish them from established causal effects.

### Module 5 — Reproducible data and feature pipelines

#### Outcomes

- AI1-O3
- AI1-O5
- AI1-O7

#### Lessons

1. **Raw and derived data boundaries** — Keep source records separately from cleaned/features output; document immutable inputs and derived material.
2. **Transformation contracts** — Define accepted schema, output schema, correction policy, row ordering, failure behavior and known limitations.
3. **Fit versus transform state** — Distinguish fitting statistics/encoders on training data from applying frozen parameters to other partitions.
4. **Feature lineage** — Trace generated columns to exact source fields, code revision and computation parameters.
5. **Idempotent materialization** — Show that repeated runs neither duplicate observations nor leave inconsistent results under stable inputs.
6. **Incremental and late data** — Handle repeated input, late arrival, partial updates and schema evolution without silent row loss.
7. **Failure injection and restart** — Reproduce malformed-source, interrupted transform or invalid-schema failure and verify a safe bounded rerun.
8. **Pipeline verification** — Use independent fixture checks for schema, row/key integrity, transformation isolation and record preservation, extending rather than repeating SEF5 testing methods.

### Module 6 — Dataset quality, partitioning and leakage

#### Outcomes

- AI1-O3
- AI1-O6
- AI1-O8

#### Lessons

1. **Data dictionary and rights record** — Define fields, units, categories, expected missingness, collected sources, access boundaries and permitted use.
2. **Quality dimensions** — Measure validity, completeness, duplicates, inconsistent units, stale records and class/group coverage.
3. **Target-proxy leakage** — Identify variables that encode the label through post-outcome events or unintended publication.
4. **Preprocessing leakage** — Demonstrate why fitting imputers, scalers, encoders or selectors before partitioning biases held-out evaluation.
5. **Entity-aware partitions** — Prevent the same customer, patient, document or device from crossing splits when the evaluation task assumes independence.
6. **Time-dependent partitions** — Respect chronology and look-ahead restrictions for future-facing predictions.
7. **Distribution comparison** — Diagnose subgroup or time-window shift without assuming statistical significance or that an observed shift proves deployment failure.
8. **Leakage tests and correction** — Build positive/negative fixtures that catch overlap, target proxies, fit-state reuse or invalid chronological access.

### Module 7 — Scientific reproducibility and limitations

#### Outcomes

- AI1-O4
- AI1-O7
- AI1-O9

#### Lessons

1. **Notebook state and execution order** — Reproduce hidden-state divergence and rebuild the same results with a clean sequential run.
2. **Dependency and data identity** — Record package versions, dataset checksum/revision and relevant numerical platform details.
3. **Randomness and repeatability** — Control seeds where effective, identify nondeterministic mechanisms and avoid claims that one seed proves robustness.
4. **Tolerance and numerical stability** — Choose justified approximate comparison policies and report when dtype or operation order alters a result.
5. **Independent result checking** — Compare the analysis against small reference calculations and an independently derived expected data invariant.
6. **Sensitivity analysis** — Change a defensible data-quality or sampling assumption and explain how conclusions vary.
7. **Reproducible failure diagnosis** — Document a causal hypothesis, a bounded correction and a negative regression fixture for an unfamiliar defect.
8. **Readable scientific reporting** — Separate methods, observed results, supported conclusions, uncertainty and unresolved limitations for independent review.

### Module 8 — Independent AI dataset investigation

#### Outcomes

- AI1-O1
- AI1-O2
- AI1-O3
- AI1-O4
- AI1-O5
- AI1-O6
- AI1-O7
- AI1-O8
- AI1-O9

#### Lessons

1. **Dataset study charter** — Define a permissible source or synthetic generator, target population, question and measurable acceptance criteria.
2. **Schema and quality review** — Publish key constraints, types, units, missingness, row granularity and explicit exclusions.
3. **Numeric and tabular analysis** — Build a bounded vectorized calculation and validated joins using independent small expected results.
4. **Partition and transform design** — Establish the correct split policy before fitting preprocessing and record leakage controls.
5. **Reproducible implementation** — Package data ingestion, validation, transformation, analysis and repeatable commands into one small project.
6. **Evidence and visualization review** — Explain supported findings, summary choices, selection limitations and misleading alternatives.
7. **Independent failure challenge** — Diagnose a reviewer-selected or equivalent publicly specified unfamiliar data-integrity failure and verify repair.
8. **Handoff and defense** — Demonstrate a clean rerun, provenance, legitimate source use, reproducibility and honest fitness-for-use limitations.

The study develops **one artifact across stages**. A learner may reuse inspected outputs from earlier required assessments instead of creating a second unrelated dataset project.

## Completion requirements

### Environment, fixtures and evidence

Use Python 3.11+ and free scientific packages or an equivalent openly reviewable reference environment. The required experiments work with small local inputs on an ordinary CPU; any larger real dataset or cloud service is optional. Publish the actual supported dependency versions, dataset/source identity, seeds, commands and numerical tolerance choices. Synthetic test fixtures must not contain real private records. Where input licensing is uncertain, use self-generated fixtures and do not claim permissions that cannot be established.

The following fixture classes are mandatory **in the assessment work**, not new permanent OEE repository resource files: (a) clean small arrays with independently calculable expected values; (b) a typed table with unique observation IDs and an intentionally duplicated join key; (c) records containing at least one missing/invalid numeric value; (d) two or more observations per entity with a plausible group-leakage path; and (e) timestamped or post-outcome fields that can expose look-ahead or target-proxy leakage. Learners may generate and document their own concrete values as long as the expected outcomes, failure mechanism and evaluation criteria below remain checkable.

Every required assessment has one authoritative definition below. Formative exercises and optional studies are not independent course completion conditions. In an accessible equivalent demonstration, evaluate the **same** mathematical, computational and evidence criteria. A private grader, unseen variant or paid resource cannot replace the published contract.

### Required summative assessments

- **AI1-AS1** — Numerical computation and tabular integrity
  - Outcomes: AI1-O1, AI1-O2, AI1-O3
  - Work: Define the observational unit and intended use for a small, lawful/synthetic measurement dataset. Implement correct 2D array indexing, a row-wise and column-wise reduction, a valid and invalid broadcasting example, and a view-versus-copy mutation comparison. Use the matrix `[[1,2,3],[4,5,6]]` for an independent hand-derived row-sum oracle `[6,15]` and column-sum oracle `[5,7,9]`. Show one incompatible broadcast that fails deliberately. Join a three-row observation table by a declared key with a lookup table containing a duplicated key; first reproduce the unintended multiplication and then reject it using an explicit cardinality contract. Supply missing, invalid dtype, nonfinite and unknown-category cases.
  - Criteria: Shapes and axis results agree with independently calculated oracles, and comparison tolerances are justified for floating results. Views and copies have accurately predicted mutation behavior. Invalid broadcasts and data/schema violations are detected, not silently accepted. The join never passes as one-to-one when a key is repeated, and row identities remain traceable. The learner distinguishes a described data workflow from a demonstrated trained model.
  - Evidence: Code and exact run commands, source/rights statement, hand calculations, shape and mutation traces, join-before/after fixture counts, positive/negative tests, and a short decision note about numerical/data assumptions.

- **AI1-AS2** — Validated feature pipeline and trustworthy exploration
  - Outcomes: AI1-O4, AI1-O5, AI1-O6
  - Work: Produce a small versioned raw-to-feature pipeline using licensed/local or synthetic observations with at least two repeated entities, a time field, a numeric missingness case and a candidate target-proxy field. Declare the empirical question, units and split policy, then produce at least three *different purpose* analytical outputs: a distribution summary, a subgroup comparison, and a chart with a textual interpretation. Deliberately run an invalid entity-overlap split and a preprocessing-fit or temporal/target-proxy leakage case; show which assertions detect each, implement corrections and reproduce the corrected run twice. A reviewer must be able to supply a new record or duplicate without silent corruption.
  - Criteria: The pipeline rejects unexpected schema, duplicated keys, wrong units or missing required fields according to explicit policy. It is idempotent for unchanged inputs and produces attributable derived fields. Split isolation and fit-on-training-only behavior are established with positive and negative controls; leakage mechanisms are demonstrated, not merely named. Visual/statistical interpretations match observed evidence and do not claim causation, certainty or representative sampling without support. A failed transform does not silently replace previously valid output with misleading success.
  - Evidence: Versioned raw/derived fixture manifests, schema and data dictionary, deterministic run/re-run artifacts, analysis figures with text equivalents, independent expected row/key counts, leakage-failure and repaired test results, and a source-to-feature lineage table.

- **AI1-AS3** — Independent dataset-study reproduction and defense
  - Outcomes: AI1-O1, AI1-O2, AI1-O3, AI1-O4, AI1-O5, AI1-O6, AI1-O7, AI1-O8, AI1-O9
  - Work: Consolidate and extend (do not recopy unnecessarily) AS1/AS2 into a bounded, lawful data study with a concise question, acceptance criteria, defensible population/split assumptions, reproducible computation, quality and source-use report, a meaningful investigation and explicitly limited conclusions. From a clean checkout or equivalent state, an independent reviewer executes the study. The learner must independently diagnose one unfamiliar but safe defect selected by the reviewer from the published classes **duplicate join key**, **incorrect axis**, **unseen category**, **entity leakage**, **wrong unit**, or **chronology violation**, propose a correction, produce the corresponding regression evidence, and explain whether earlier conclusions remain valid. A written, recorded or live technical defense may be used.
  - Criteria: Setup has no undocumented hidden data, environment or manual preprocessing step; independently calculated fixtures and raw-to-output lineage establish the claims being made. Every material fault/limitation is disclosed and invalid data is not reported as successful analysis. The unfamiliar defect is correctly diagnosed and repaired without weakening the declared constraints or silently changing the observed population. The final interpretation distinguishes empirical observation, modeling assumptions, and causal claims. The learner explains the new scientific-array and dataset-engineering mechanisms rather than merely rerunning scripts. Prior AS1/AS2 artifacts may count as inspected supporting evidence.
  - Evidence: Source revision, data/rights manifest, environment and commands, actual clean-run record, required assessments and fixture links, outputs and quality checks, diagnostic/repair trace, independent reviewer observations and reviewable technical defense.

### Completion decision

All three required assessments must receive positive evaluation decisions under their published criteria, jointly demonstrating **AI1-O1–AI1-O9**. Record the applicable course revision and inspectable evidence without exposing secrets or personal data. Reproduction of executable claims is required, but attendance, completed lesson checkmarks, a green test alone or a polished graph cannot substitute for actual demonstrated understanding. The course remains `draft` pending the learner and independent-review evidence required for a higher readiness label.
