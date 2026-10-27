# AI17 — Causal Inference & Experimentation

**Track:** AI & ML · **Prerequisite:** AI3, F4 · **Elective** · **Time:** 4 weeks, 60 hours · **Project:** elective
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Learn when a prediction or observed association supports a causal claim, and how to design and analyze experiments and quasi-experiments. This protects you from the most common analytical failure in applied ML and product data.

## Outcomes

You can:

- define estimands, potential outcomes, and counterfactuals;
- draw a causal graph and identify confounders, mediators, and colliders;
- explain randomization, blocking, and assignment;
- design an A/B test with power, sample size, and guardrails;
- analyze experiments without peeking or multiple-testing errors;
- apply propensity scores, matching, difference-in-differences, and instrumental variables;
- distinguish predictive from causal models;
- state identification assumptions and sensitivity;
- communicate uncertainty and operational trade-offs.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [Causal Inference: What If](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/) (Hernán & Robins) | Ch. **1–10** | Potential outcomes, DAGs, confounding, standardization, matching, IPW |
| [Trustworthy Online Controlled Experiments](https://experimentguide.com/) (Kohavi et al.) | Ch. **1–4, 7–9, 17** | A/B testing at scale |
| [Mostly Harmless Econometrics](https://www.mostlyharmlesseconometrics.com/) | Ch. **1–4** (selected) | Regression, IV, DiD |
| [Causal Inference for the Brave and True](https://matheusfacure.github.io/python-causality-handbook/) | Ch. **1–8** | Practical implementation |
| [DoWhy docs](https://www.pywhy.org/dowhy/) | Identification, refutation | Implementation |

## Modules

1. **Causal framing** — estimand, treatment, outcome, potential outcomes, SUTVA, consistency, positivity.
2. **Graphs** — DAGs, backdoor paths, front-door criterion, confounders, mediators, colliders, selection bias.
3. **Experiments** — randomization, blocking, factorial designs, power, sample size, guardrail metrics, interference.
4. **Analysis** — difference in means, regression adjustment, cluster-robust errors, sequential testing, multiple comparisons, heterogeneous effects.
5. **Observational methods** — matching, propensity scores, IPW, doubly robust estimators, DiD, fixed effects, IV, regression discontinuity.
6. **Sensitivity and communication** — unmeasured confounding, placebo tests, negative controls, refutation, decision memo.

## Labs

### Lab 1 — DAG and estimand

Draw a causal graph for a realistic product question. Identify the estimand, confounders, colliders, and a bad adjustment set. Write the identification assumption and one refutation test.

### Lab 2 — Experiment design

Design an A/B test with a primary metric, guardrails, power calculation, assignment unit, duration, and stopping rule. Simulate the experiment and show the false-positive rate under no effect.

### Lab 3 — Analysis without peeking

Analyze a simulated experiment. Compare a naive t-test, regression adjustment, and a sequential method. Show how optional stopping inflates false positives.

### Lab 4 — Observational study

Estimate an effect from observational data using propensity weighting or matching. Check covariate balance and run at least two refutations. State why the result may still be biased.

### Lab 5 — Decision memo

Write a one-page decision memo: claim, estimand, assumptions, evidence, uncertainty, limitations, and recommended action. Include what would change your mind.

## Exercises

1. Define an estimand for a product change.
2. Identify a collider in a supplied DAG.
3. Explain why adjusting for a mediator is wrong for a total effect.
4. Calculate sample size for a given effect and power.
5. Explain peeking and alpha inflation.
6. Compare ITT and per-protocol effects.
7. Explain propensity-score positivity.
8. Interpret a DiD parallel-trends assumption.
9. Design a placebo test.
10. Distinguish prediction from causation.

## Project increment (optional)

Add a causal or experiment-analysis study to P7: state the identification assumption, draw the causal graph, adjust for confounders, and run a sensitivity analysis. The deliverable is a short report, not a new model. This is an elective extension, not a new ladder project.

## Exit check

- [ ] state an estimand and identification assumptions;
- [ ] draw and defend a causal graph;
- [ ] design a powered experiment with guardrails;
- [ ] analyze without optional stopping or multiple-testing errors;
- [ ] apply one observational method and check balance;
- [ ] write a decision memo with uncertainty and limits.

## Common failure modes

- Adjusting for colliders or mediators.
- Treating a predictive model as causal.
- Peeking and stopping when significant.
- Ignoring interference between units.
- Reporting a subgroup effect found after many tests.
- Claiming parallel trends without evidence.
- Confusing statistical and practical significance.

## Evidence to commit

- `labs/ai/AI17/` with DAG, experiment design/simulation, observational analysis, decision memo
- `notes/ai/AI17/summary.md`

## Optional depth

- *Causal Inference: The Mixtape* (Cunningham).
- *Elements of Causal Inference* (Peters, Janzing, Schölkopf).
- *Field Experiments* (Gerber & Green).
- `EconML` and `CausalML` docs.
- Sensitivity analysis for unmeasured confounding.
