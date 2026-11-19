# AI1 — Scientific Computing & Data Engineering for AI

**Program:** AI — AI Engineering
**Type:** course
**Prerequisites:** [SEF10](../SEF/SEF10.md) (completed Software Engineering Foundations)
**Duration:** 14–18 weeks
**Status:** draft
**Specification:** v0.2.0
**Expected workload:** 10–15 focused hours per week; provisional, not a graduation threshold

> [AI Engineering](README.md) · [Curriculum design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

AI1 converts the programming, algorithms, and numerical mathematics already demonstrated in completed SEF into **reliable, inspectable scientific data work**. The course's new competence is not basic Python or probability: it is designing and defending the transformation from messy, bounded source records into an analysis-ready dataset with known meaning, correct numerical operations, testable integrity rules, meaningful exploratory evidence, leakage-resistant partitions, and independently reproducible outputs. These are prerequisites for honest modeling and evaluation in later AI courses.

**Entry readiness.** Admission requires an authentic assessed SEF10 completion decision, which already closes the completed SEF program. In particular, learners apply SEF2's Python control flow, functions, collections, modules, files and exceptions; SEF4's complexity and basic algorithm reasoning; SEF5's testing and reproducibility; SEF8's functions, statistics, vectors, matrices, probability, uncertainty, derivatives and numerical work; and SEF9's licenses, privacy and trustworthy evidence. AI1 does not award or repair missing prerequisite evidence. A voluntary self-check may ask the learner to parse a small CSV, compute a hand-checkable mean and explain a Git revision; that practice is not another completion requirement.

**Reference environment.** A locally runnable Python 3 environment, NumPy, pandas and an accessible plotting or tabular reporting tool are sufficient. Learners may use equivalent open scientific libraries if they reproduce the published behavior and explain differences. CPU-only and offline-after-installation work on small synthetic or appropriately licensed datasets is sufficient; no GPU, cloud, paid notebook, private dataset, external AI API or particular learning platform is needed. Record package versions and numeric tolerances where relevant. Every required dataset may be synthetically generated; no real person's records are needed. Textual tables and written descriptions must make visual findings accessible.

**Teaching and evaluation approach.** Modules give instructional progression, worked and negative examples, and optional formative checks. Five required summative assessments use a small collection of linked, learner-owned data and code rather than five unrelated projects. An independently derived oracle and an unfamiliar bounded correction test the learner's reasoning rather than only the output of a library call. The 14–18-week estimate (approximately 140–270 focused hours at the provisional weekly range) includes study, experiments, debugging, revision, and review. It is not learner-tested timing evidence; educational readiness remains draft.

## Learning outcomes

- **AI1-O1:** Frame a bounded scientific-data question, identify the observation unit, source provenance, permission constraints, expected fields, downstream uses and unsupported claims.
- **AI1-O2:** Construct, reshape, slice, aggregate and combine multidimensional numerical arrays while predicting axes, dimensions, broadcasting and intermediate results independently of library output.
- **AI1-O3:** Identify and investigate numeric type, missing-value, overflow, floating-point, reduction-order and measurement issues; justify tolerances and safe transformations for a given dataset.
- **AI1-O4:** Ingest bounded structured data into an explicit schema with stable record identity, parsing rules, data types, units, missingness and demonstrable valid/invalid input behavior.
- **AI1-O5:** Implement and verify tabular selection, grouping, aggregation and joins without silently changing row cardinality, keys, units, or the interpretation of missing data.
- **AI1-O6:** Diagnose a dataset's duplicates, outliers, missingness, schema drift, invalid values, and provenance gaps; choose defensible correction, exclusion, quarantine or retention policies.
- **AI1-O7:** Design and test transformation pipelines whose operations preserve declared invariants, distinguish fitted parameters from deterministic transforms and produce reviewable lineage.
- **AI1-O8:** Conduct exploratory descriptive and comparative analysis, reasoning about denominator choice, uncertainty, sampling, confounding and limits of observational evidence.
- **AI1-O9:** Communicate evidence through correctly labeled and accessible visual or equivalent tabular representations, disclosing scales, units, missing observations and the limits of inference.
- **AI1-O10:** Locate and prevent target, temporal, group, transformation and evaluation leakage, including contamination caused by fitting preprocessing on held-out information.
- **AI1-O11:** Design deterministic and justified train/validation/test or alternative holdout partitions that respect observations, group or time dependence, and evaluation purpose.
- **AI1-O12:** Produce a clean-state reproducible data analysis with versioned inputs, dependencies, deterministic procedures, independent expected results, controlled changes and substantive limitation reporting.
- **AI1-O13:** Diagnose and correct an unfamiliar bounded data or pipeline defect, explaining why the original result was misleading and verifying that the repair does not violate other invariants.

## Modules

### Module 1 — Scientific Questions, Data Contracts and Provenance

#### Outcomes

- AI1-O1
- AI1-O4
- AI1-O6

#### Lessons

1. **From scientific measurements to AI datasets** — Trace numerical experiments into structured records, data pipelines and curated machine-learning datasets. Use a bounded event log or lab measurement to distinguish numerical calculation, source attribution, typed fields and valid interpretation; faster array or DataFrame operations do not establish correctness. Explain how a reasonable-looking table can support an invalid inference or a collection procedure can change what is measured.
2. **Questions, observation units and scope** — Choose a specific data question and distinguish an event, account, sample, subject or time interval as the unit of analysis. State a falsifiable intended result and a claim that the available records cannot support.
3. **Schema, units and semantic contracts** — Define field meaning, type, unit, permitted range, null status, key, and relationship. Explain why a count of transactions is not a count of distinct customers and why a negative refund is not automatically a bad numeric value.
4. **Provenance and lawful use** — Identify origin, permission/license, acquisition conditions, permissible reuse, transformations and retention expectations. Prefer synthetic fixtures; practice redacting sensitive attributes and refusing a requested publication where provenance or consent is insufficient.
5. **Population and collection bias** — Distinguish target population from observed sample, nonresponse from legitimate absence, and collection artifacts from genuine phenomena. Predict how excluding failed measurements can bias an analysis.
6. **A reviewable data contract** — Write a concise data dictionary and expected-value table for a six-event synthetic dataset. Try one conflicting schema change and explain whether to reject, migrate, or reinterpret the affected records.

*Optional feedback:* Given one file of events and one file of entities, predict the number of distinct accounts and explain which column should be a key before opening either file in pandas.

### Module 2 — Numerical Arrays, Shapes and Broadcasting

#### Outcomes

- AI1-O2
- AI1-O3

#### Lessons

1. **Arrays as typed numerical structures** — Explain homogeneous element types, ranks, axes, shapes, strides and storage cost; contrast arrays with Python lists only where the representation changes computational or numeric behavior rather than re-teaching Python syntax.
2. **Indexing and views** — Predict slicing results and distinguish view-like aliasing from independent copies. Reproduce an unintentional in-place mutation and show a safe correction; do not assume every indexing operation is a view.
3. **Axis-aware aggregation** — Compute row-wise and column-wise sums/means by hand before calling the library. State what happens when an axis is invalid, a slice is empty or the denominator excludes missing observations.
4. **Broadcasting rules and refusal** — Derive compatibility from trailing dimension alignment. Contrast a valid feature-vector broadcast with an invalid shape pair and explain why an implicit expansion may conceal a semantic mistake.
5. **Linear algebra in concrete data transformations** — Apply matrix-vector products and dot products from SEF8 to real feature representations. Check the expected shape and selected numeric entries independently.
6. **Vectorization, allocation and memory** — Compare a clear loop with vectorized work under controlled input sizes; distinguish asymptotic complexity, allocations, temporaries, native kernels and benchmark noise without claiming every vectorized expression is faster.
7. **Finite values and safe casting** — Investigate integer truncation/overflow, float precision, infinities, NaN propagation, division by zero and type promotion in the actual chosen library; verify behavior experimentally rather than assuming behavior across all versions.
8. **Array trace and independent oracle** — For the required small array fixture, predict all requested sums, means, products and an invalid broadcast before executing code, and identify one plausible axis mistake that would still yield a numeric answer.

*Optional feedback:* Explain why a (2, 3) array can combine with a (3,) feature vector but cannot combine elementwise with a (2,) vector under standard trailing-axis rules.

### Module 3 — Numerical Evidence and Scientific Reproducibility

#### Outcomes

- AI1-O2
- AI1-O3
- AI1-O8
- AI1-O12

#### Lessons

1. **Magnitude, scale and stability** — Identify quantities with incompatible units or scales, cancellation errors and cases where summation order matters. Explain when a tiny floating-point discrepancy is acceptable and when it indicates a wrong algorithm.
2. **Reductions and missing-value conventions** — Compare arithmetic mean, weighted mean and conditional aggregation; state whether missing, zero and invalid entries participate and how the denominator was chosen.
3. **Sampling and empirical summaries** — Use SEF8 probability and statistics to compute descriptive measures with a clear population/sample interpretation; no general probability refresher is required.
4. **Random generators and repeatability** — Separate reproducible pseudo-random sequences from independent scientific validity. Record seeds and algorithms, and explain why an identical random seed cannot prevent data leakage or unrepresentative sampling.
5. **Numerical reference implementations** — Write a tiny transparent implementation or hand-derived calculation against which array output can be checked. Distinguish approximate comparisons from exact integer identity and explain tolerance choice.
6. **Experiment interpretation** — Compare measured outputs from two operations while controlling input, environment, warm-up and repetitions as needed; report variability and decline unsupported broad performance claims.

### Module 4 — Tabular Schemas, Keys and Relationships

#### Outcomes

- AI1-O4
- AI1-O5
- AI1-O7

#### Lessons

1. **Parsing is not interpretation** — Ingest CSV or equivalent delimited records with explicit encoding, separators, numeric parsing, date interpretation and null conventions. Detect a malformed record instead of silently accepting shifted columns.
2. **Types, timestamps and categories** — Compare strings, numeric types, categorical labels and timestamp values; explain how a local-time ambiguity or lexical ordering can change a result.
3. **Keys and row cardinality** — Verify primary-key uniqueness at the chosen observation level; contrast event identity with entity identity, and investigate unintended duplication caused by repeated dimension rows.
4. **Filtering, grouping and denominator correctness** — Build reproducible filters and aggregations while stating which observations were excluded. Check total count, unique-entity count and grouped totals independently.
5. **Join types and multiplicities** — Explain one-to-one, one-to-many and many-to-many relationships; compare inner, left and anti-join semantics on a known fixture. Require a documented handling policy for unmatched or duplicate keys.
6. **Reproducible transformations and lineage** — Express transformations as inspectable functions or pipeline stages; record source columns, derived units and changed row counts. Include a regression test for a key-preserving transformation.
7. **Cross-file discrepancy investigation** — Detect a duplicated key in an entity reference file that inflates an aggregate after merging; reject the join or explicitly resolve the duplicate without pretending the duplicated rows were genuine events.

*Optional feedback:* Predict whether an event-to-dimension join preserves the event count when one entity has two matching reference rows; explain the difference between an input error and a legitimate one-to-many relationship.

### Module 5 — Data Quality and Defensible Feature Construction

#### Outcomes

- AI1-O4
- AI1-O6
- AI1-O7
- AI1-O10

#### Lessons

1. **Quality dimensions and operational consequences** — Distinguish completeness, validity, consistency, uniqueness, timeliness and representativeness. Map each failure to a possible downstream modeling or evaluation error.
2. **Missingness mechanisms and policies** — Distinguish unknown, not applicable, unobserved and missing-by-design; demonstrate how a mean changes under exclusion or imputation. Document when a missingness mechanism cannot be inferred from the observed records.
3. **Outliers and valid extreme cases** — Compare malformed records, real tail observations and legitimate negative values. Justify a robust statistic or explicit quarantine rather than deleting every inconvenient sample.
4. **Duplicate detection and identity** — Contrast exact duplicate byte rows, identical measurements, repeated event IDs and legitimate repeated entity visits. Define a record-identity policy with an independently checked cardinality.
5. **Feature semantics and units** — Derive features from timestamp, category and numeric fields, specifying temporal availability, units and interpretation; reject features that encode the answer after the target event.
6. **Transform order and fitted state** — Distinguish pure deterministic conversions from a normalization, imputation or category vocabulary fit on observed data. Record fitted parameters separately and identify which later stages may reuse them.
7. **Schema drift and invalid-input behavior** — Introduce an unexpected category, absent column, reordered field or changed type. Show explicit validated refusal, safe fallback or a documented migration rather than silent corruption.
8. **Quality gate review** — Make a validation decision for each adversarial input, including missing amounts, repeated IDs, unmatched dimension keys and invalid dates. Explain which imperfections remain permitted and why.

### Module 6 — Exploration, Visual Communication and Uncertainty

#### Outcomes

- AI1-O1
- AI1-O8
- AI1-O9

#### Lessons

1. **Descriptive questions and denominators** — Translate a business/scientific question into measurable quantities and population definitions. Distinguish event-level frequency, entity-level frequency and a conditional rate.
2. **Distribution and grouping** — Compute and inspect ranges, quantiles, dispersion, missingness patterns and relevant stratification. Explore how summaries mask rare but consequential groups.
3. **Comparisons under confounding** — Explain why a difference across observed groups does not independently prove causality; identify a plausible confounder and state what additional evidence is needed.
4. **Sample uncertainty and robustness** — Use SEF8 inference to compare estimates and discuss sample size, variability and limitations. Prefer a justified simple uncertainty report to an unearned significance claim.
5. **Plot selection and truthful scales** — Choose a labeled table, distribution plot, time series or scatter comparison according to the question. Avoid misleading truncated axes, implicit interpolation, unexplained log scales and decorative chart types.
6. **Accessible evidence delivery** — Supply chart titles, units, clear legends, readable labels and textual/tabular equivalents that communicate the same conclusion without color-only encoding.
7. **Counterexample and interpretation review** — Show how a filtered or duplicated dataset changes one chart and construct a written correction identifying the underlying source or denominator error.

*Optional feedback:* Compare two plots with different denominators and identify which, if either, addresses the original question without an unsupported causal leap.

### Module 7 — Leakage, Partitions and Evaluation Boundaries

#### Outcomes

- AI1-O7
- AI1-O10
- AI1-O11

#### Lessons

1. **What a held-out estimate can claim** — Identify the prediction or analysis unit, deployment setting and data-generation process before deciding whether an independent holdout is appropriate.
2. **Target and post-outcome leakage** — Find a variable recorded after the target event or directly derived from the answer; remove it from predictive inputs and explain why high apparent correlation is not enough to retain it.
3. **Group dependence and repeated entities** — Demonstrate why different events from one account or subject may not constitute independent train/test observations. Compare row-random assignment against group-disjoint assignment.
4. **Chronological splits and future information** — Distinguish random, time-ordered and forward-chaining strategies. Explain why future timestamps, later corrections or hindsight-derived labels can invalidate an earlier prediction.
5. **Fitted preprocessing must respect partitions** — Fit imputation, scaling or categorical vocabulary using training information only; apply frozen parameters to validation/test. Demonstrate the contamination caused by fitting on the combined dataset.
6. **Validation versus final test use** — Distinguish exploratory model choices made on validation evidence from a final held-out estimate. Avoid repeated test-based selection, and state when group/time constraints prevent a simplistic split ratio.
7. **Data lineage and duplicate contamination** — Trace a sample from raw source through cleaned identifiers, grouping and partitions. Detect an accidental duplicate or transformed sibling crossing the boundary.
8. **A partition decision memo** — Compare at least two plausible split policies on one bounded dataset, choose a defensible option and specify the exact overlap or temporal-order assertions that would falsify it.

*Optional feedback:* Explain why a zero intersection of row IDs does not guarantee independence if records share a subject or are near-duplicates from the same source.

### Module 8 — Reproducible Data Pipelines and Failure Diagnosis

#### Outcomes

- AI1-O6
- AI1-O7
- AI1-O10
- AI1-O12
- AI1-O13

#### Lessons

1. **Clean-state scientific project structure** — Organize source files, synthetic fixtures, data contracts, tests, dependencies and generated outputs so that a reviewer can recreate the result without hidden notebook state or machine-specific paths.
2. **Deterministic pipeline execution** — Control input ordering, canonical data types, seeds, time zones, output paths and floating-point tolerance; run the pipeline twice and explain any permitted nondeterminism.
3. **Independent checks and transformation invariants** — Verify identity preservation, expected row counts, numeric reference outputs, admissible nulls and partition disjointness with oracles not derived from the output under test.
4. **Failure injection and repair** — Intentionally introduce a duplicate dimension key, schema change or cross-partition entity. Diagnose the faulty stage, repair it and demonstrate that unrelated checks still pass.
5. **Auditability, privacy and reproducibility limits** — Publish what can be inspected without releasing secrets, personal information or unlicensed records. Explain the difference between reproducibility, validity and external generalizability.
6. **Unfamiliar data challenge** — Practice adapting to an instructor/reviewer-provided bounded change in a field definition, malformed input or split constraint without starting another course or depending on a private platform.

### Module 9 — Integrated Dataset Investigation and Technical Defense

#### Outcomes

- AI1-O1
- AI1-O4
- AI1-O5
- AI1-O6
- AI1-O7
- AI1-O8
- AI1-O9
- AI1-O10
- AI1-O11
- AI1-O12
- AI1-O13

#### Lessons

1. **Choose one credible dataset question** — Fix a measurable use case, observation level, acceptance conditions and excluded claims before exploring data. Use a small permitted corpus with at least one authentic quality issue or an equivalent synthetic fixture.
2. **Carry one dataset through all stages** — Preserve source lineage while validating schemas and keys, cleaning appropriately, deriving features, assessing relevant distributions and selecting defensible evaluation partitions.
3. **Separate observations from conclusions** — Compare expected and observed row/aggregate counts, include accessible evidence, and explain how a changed filtering, join or split decision changes what can be claimed.
4. **Review reproducibility and risk** — Execute a clean-state rebuild, repeat outputs, inject and correct a realistic error, and document remaining limitations, provenance and privacy implications.
5. **Explain and defend the work** — Present independently checkable evidence, answer a bounded unfamiliar change and justify why the final dataset can support specific future AI experiments but cannot guarantee generalization or model fairness.

The nine modules describe instruction and an integrated application, not nine required lab submissions. A formative prompt, worked trace or self-check is optional unless the assessment below explicitly requires the performance.

## Completion requirements

### Shared public reference fixtures

Assessments may use the following small fixtures or learner-owned equivalents that preserve their evaluation properties. These literal values are public for independent study; an assessor may vary values while preserving the same published criteria.

**Array fixture:** A is the 2 × 3 matrix with rows (1, 2, 3) and (4, 5, 6). A has shape (2, 3); row sums are (6, 15), column means are (2.5, 3.5, 4.5), and multiplying A by the 3 × 1 vector (1, 0, -1) gives (-2, -2). A feature vector of shape (3,) can broadcast over columns; a vector of shape (2,) cannot be broadcast over A under ordinary trailing-dimension rules. Equivalent fixtures must expose a calculable shape, an intentional invalid broadcast and a numeric reference independent of the tested NumPy call.

**Event fixture:** A CSV-like event table contains:

| event_id | entity_id | event_date | amount | category | target |
| --- | --- | --- | ---: | --- | ---: |
| E01 | A | 2025-01-01 | 12 | retail | 1 |
| E02 | A | 2025-01-03 | 8 | retail | 0 |
| E03 | B | 2025-01-04 | 20 | service | 1 |
| E04 | C | 2025-01-05 | missing | service | 0 |
| E05 | C | 2025-01-06 | 0 | service | 0 |
| E06 | D | 2025-01-07 | -3 | retail | 1 |

This fixture has **six event rows, four distinct entities, five observed amounts and an observed amount sum of 37**. The negative value is defined as a legitimate refund; zero is a legitimate amount; missing is not zero. The observed-value mean is 7.4, not a value imputed from unseen data. The target is a synthetic illustration, not a validated classification label or a reason to train a model in AI1.

**Entity fixture:** An entity table maps A→north, B→south, B→east, C→north and D→west. The repeated B key is intentionally ambiguous: an unrestricted event-to-entity join yields seven rows and double-counts event E03, increasing the observed amount sum from 37 to 57. A valid implementation **must not silently accept** this cardinality inflation; it may reject the conflicting entity dimension, quarantine B, or apply a documented domain-justified resolution that restores the declared relationship. Arbitrarily selecting a row without disclosure is not acceptable.

An independent reviewer may introduce malformed dates, missing fields, duplicate event IDs, unseen categories, a late-arriving event or a repeated entity spanning partitions. The learner is assessed against the same stated invariants and reasoning, not a secret vendor grader.

### Required summative assessments

- **AI1-AS1** (required numerical-array investigation)
  - **Outcomes:** AI1-O2, AI1-O3.
  - **Work:** Build a small script that executes the array fixture's index, reshape, row/column reduction, matrix-vector operation and valid/invalid broadcasts. Predict shapes and numeric values **before running** the library. Add a numerical failure or precision case (such as unsafe integer cast, NaN-sensitive reduction or unstable subtraction) and compare at least one transparent reference calculation. Compare a loop and vectorized computation only under disclosed conditions; performance superiority is not an acceptance assumption.
  - **Criteria:** All public expected values and shapes match; the incompatible (2,) broadcast is rejected or reported as invalid; the numeric case demonstrates the actual observed risk and a justified repair or tolerance; independent predictions agree with the tested computations; the learner explains type behavior, aliasing or intermediate allocations relevant to the chosen implementation.
  - **Evidence:** Executable source, version information, independent hand calculations/reference oracle, normal and negative test results, and a concise numerical interpretation.

- **AI1-AS2** (required source contract, joins and quality investigation)
  - **Outcomes:** AI1-O1, AI1-O4, AI1-O5, AI1-O6.
  - **Work:** Define an explicit schema, observation unit, lineage and legal/synthetic provenance for the event fixture or equivalent. Parse and validate records; distinguish missing from zero, refund from invalid value, events from distinct entities, and duplicate dimension keys from valid repeat events. Compare a naive join and a defended corrective policy. Exercise valid, malformed, duplicate-key and unmatched-reference inputs.
  - **Criteria:** On the public fixture, the verified raw record/event count is six, the entity count is four, the nonmissing amount count is five, the observed amount sum is 37, and the unrepaired duplicated-key join is identified as seven rows and sum 57; a repaired or refused join cannot be presented as having preserved the intended one-to-one key contract without evidence. Units, dates, nulls, allowed refund values and row-identity behavior are explicit. No sensitive or unlicensed source is required.
  - **Evidence:** Data dictionary and provenance statement, input fixture or reproducible generator, parsing/transformation source, independently established cardinality and aggregate oracles, invalid-input decisions and their results.

- **AI1-AS3** (required exploratory evidence and communication)
  - **Outcomes:** AI1-O7, AI1-O8, AI1-O9.
  - **Work:** Reuse the verified dataset from AI1-AS2 or an equivalent. Construct at least two **meaningfully different** descriptive comparisons motivated by a question, including an appropriate denominator and a comparison sensitive to a missingness, group or join policy. Show a clear visual representation or an equally inspectable accessible textual/table alternative. Explain uncertainty, possible collection bias and a plausible competing interpretation; do not infer causality from correlation.
  - **Criteria:** Values and group counts are traceable to verified records rather than a duplicated merge; units, time scope, sample/observation unit, included/excluded records and missing values are disclosed; the displayed quantities agree with a simple independent calculation; alternative handling demonstrably changes (or robustly does not change) a stated conclusion; all key conclusions remain understandable without color or access to a proprietary visualization service.
  - **Evidence:** Reproducible analysis script or notebook plus clean execution instructions, labeled chart(s) or equivalent tables, independent numerical check(s), concise interpretation and stated limitations.

- **AI1-AS4** (required leakage and partition investigation)
  - **Outcomes:** AI1-O7, AI1-O10, AI1-O11.
  - **Work:** Extend the same dataset or a small related synthetic generator with repeated entities and a deliberately post-outcome field. Compare row-random and group-disjoint or time-ordered partitions appropriate to a declared prospective use. Demonstrate a leakage path (group overlap, future information or fit-on-all-data preprocessing), its effect on the claimed evaluation design, and the corrected data flow. Do **not** require training a model: the object of evaluation is trustworthy partition design and preprocessing boundaries.
  - **Criteria:** The final partitions have deterministic membership, no shared entity across group-disjoint train/test sets, and no future information in a forward-looking training window; chosen preprocessing parameters are fit only on allowed training records. The defective path is reproduced and shown to violate an explicit assertion or lead to a misleading interpretation. Ratios and representativeness limitations are discussed rather than concealed by arbitrary percentages.
  - **Evidence:** Split specification, reproducible test fixture/generator, memberships or hashes, positive and negative assertions, demonstration of the defect and repair, and a short rationale linking split policy to intended use.

- **AI1-AS5** (required clean-state integrated investigation and unfamiliar correction)
  - **Outcomes:** AI1-O1, AI1-O4, AI1-O6, AI1-O7, AI1-O9, AI1-O12, AI1-O13.
  - **Work:** Present **one cumulative, versioned source tree** connecting the prior assessments into a complete bounded dataset investigation. Supply configuration, declared source fixtures, dependency versions, deterministic commands, output definitions, data-quality policy, suitable independent regression oracles, readable findings and a limitation/risk statement. From a new checkout or equivalent clean state, reproduce the documented outputs twice. Handle an assessor-selected **unfamiliar, bounded** schema, join, missingness or partition failure and explain the fault and repair. Prior assessment files may be reused, not resubmitted as separate mini-projects.
  - **Criteria:** An independent reviewer can prepare the local environment using publicly described steps, run the analysis without hidden credentials/data, and verify claimed deterministic outputs or disclosed numeric tolerances. At least one new adversarial input is safely refused or corrected without corrupting unrelated invariants. The learner personally explains the pipeline's source-to-result lineage and the actual limits of inference; an unexplained passing script or a pasted figure is insufficient.
  - **Evidence:** Clean repository/revision or inspectable artifact, README reproduction commands, source/data or generator, recorded clean-run results, version and seed assumptions, automated/independent checks, unfamiliar-case before/after evidence, and a written, recorded or live reviewable technical explanation.

### Assessment coverage and graduation boundary

| Required outcome | Summative evidence |
| --- | --- |
| AI1-O1 | AI1-AS2, AI1-AS5 |
| AI1-O2 | AI1-AS1 |
| AI1-O3 | AI1-AS1 |
| AI1-O4 | AI1-AS2, AI1-AS5 |
| AI1-O5 | AI1-AS2 |
| AI1-O6 | AI1-AS2, AI1-AS5 |
| AI1-O7 | AI1-AS3, AI1-AS4, AI1-AS5 |
| AI1-O8 | AI1-AS3 |
| AI1-O9 | AI1-AS3, AI1-AS5 |
| AI1-O10 | AI1-AS4 |
| AI1-O11 | AI1-AS4 |
| AI1-O12 | AI1-AS5 |
| AI1-O13 | AI1-AS5 |

A reviewer must make an inspectable satisfactory decision for **all thirteen AI1 outcomes** through the five required evaluations, using the applicable source revision and OEE evidence rules. Assessments may build on the same dataset and codebase; reviewers evaluate distinct claims rather than demand redundant projects. Formative prompts, optional investigations, study hours, attendance, visual polish or a green tool check are not independent completion evidence.

A defensible partial or negative finding is academically acceptable where the measurement warrants it, but not a substitute for an unpassed required correctness or integrity criterion. A changed input or unseen test must use equivalent public success criteria. Reproduction may be demonstrated with Python code plus an accessible explanation in writing, speech or a reviewable recording; neither a private paid account nor unrestricted hardware is mandatory.

### Optional technical references

- [NumPy: broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) and [NumPy: floating-point errors](https://numpy.org/doc/stable/reference/generated/numpy.seterr.html) for implementation-dependent behaviors to verify, not universal performance claims.
- [pandas: merge, join and concatenate](https://pandas.pydata.org/docs/user_guide/merging.html) and [pandas: missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html) for tabular semantics.
- [scikit-learn: common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) for leakage and preprocessing boundaries; AI1 uses these for data design, not to require ML training.
- [ACM/IEEE-CS/AAAI CS2023](https://csed.acm.org/) for broad academic competence context, not a mandated course outline.

These are freely available supporting references. They are not required paid materials, exclusive implementation choices, or replacements for the complete public assessment criteria above.
